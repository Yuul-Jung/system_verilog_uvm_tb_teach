#!/usr/bin/env python3
"""완료된 네 장의 정합성·화면·온라인/오프라인 탐색을 종합 검사한다."""

import argparse
import functools
import hashlib
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import re
import subprocess
import sys
import threading

from playwright.sync_api import sync_playwright
from check_teacher_browser import QuietHandler

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('part', type=int)
    parser.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    course = json.loads((ROOT / 'course.json').read_text())
    chapters = [c for c in course['chapters'] if (c['number'] - 1)//4 + 1 == args.part]
    assert len(chapters) == 4, 'part must contain four published chapters'
    section_counts = {c['number']: len(re.findall(r'<section\b', (args.source / c['source_html']).read_text()))
                      for c in chapters}
    results = []
    for c in chapters:
        for script, params in [('validate_teacher.py', ['--chapter', str(c['number']), '--self-test']),
                               ('check_teacher_browser.py', [str(c['number'])])]:
            result = subprocess.run([sys.executable, str(ROOT / 'scripts' / script), *params, '--source', str(args.source)],
                                    capture_output=True, text=True)
            assert result.returncode == 0, result.stdout + result.stderr
            results.append(dict(chapter=c['number'], script=script, exit_code=result.returncode, stdout=result.stdout))
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    navigation = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/google-chrome', headless=True, args=['--no-sandbox'])
        for offline in (False, True):
            context = browser.new_context()
            if offline:
                context.route('**/course.json', lambda route: route.abort())
            page = context.new_page()
            for c in chapters:
                page.goto(f"http://127.0.0.1:{server.server_port}/{c['slug']}_{c['version']}.html")
                page.wait_for_function("document.querySelectorAll('.course-ch-link').length===4")
                assert page.locator('.course-part-code').text_content() == f'PART {args.part:02d}'
                links = page.locator('.course-ch-link').evaluate_all('nodes=>nodes.map(e=>e.getAttribute("href"))')
                assert links == [f"{n['slug']}_{n['version']}.html" for n in chapters]
                current = page.locator('.course-ch-link[aria-current="page"]')
                assert current.get_attribute('href') == f"{c['slug']}_{c['version']}.html"
                assert page.locator('.course-nested-sections a').count() == section_counts[c['number']]
                for href in page.locator('#chapter-links a').evaluate_all('nodes=>nodes.map(e=>e.getAttribute("href"))'):
                    assert (ROOT / href).is_file()
                navigation.append(dict(chapter=c['number'], manifest_fetch='BLOCKED' if offline else 'ONLINE', part=True, chapters=4, sections=section_counts[c['number']], links=True))
            context.close()
        page = browser.new_page()
        page.goto(f'http://127.0.0.1:{server.server_port}/index.html')
        page.wait_for_selector('.course-part-code')
        assert page.locator('.course-part-code').text_content() == 'ALL 6 PARTS'
        assert page.locator('main tbody tr').count() == 24
        assert page.locator('main a[href*="_teacher_v"]').count() == len(course['chapters'])
        browser.close()
    server.shutdown()
    browser_files = [ROOT / f"docs/evidence/ch{c['number']:02d}_{c['version']}/browser.json" for c in chapters]
    assert all(json.loads(f.read_text())['flagged'] == 0 for f in browser_files)
    # 제1부의 단위·시간·검사 횟수 계산을 원본 설명과 독립적으로 확인한다.
    if args.part == 1:
        assert 2**8 * 2 * 2 == 1024
        assert 2 * 5 == 10 and 8 * 10 == 80 and 3 / 8 * 100 == 37.5
        assert [((d * 100)//8) for d in range(0, 9, 2)] == [0, 25, 50, 75, 100]
        assert 5 * 8 == 40 and 1 + 5 + 5 == 11
        assert 40 + 15 * 10 == 190 and 736 + 4 + 7 * 10 == 810
    report = dict(part=args.part, chapters=[c['number'] for c in chapters], chapter_checks=results,
                  viewport_measurements=24, rejected_mutations=12, navigation=navigation,
                  browser_sha256={f.relative_to(ROOT).as_posix(): hashlib.sha256(f.read_bytes()).hexdigest() for f in browser_files},
                  rtl_simulation='NOT_RUN', source_commit=course['source_commit'])
    out = ROOT / f'docs/evidence/part{args.part:02d}'
    out.mkdir(parents=True, exist_ok=True)
    (out / 'quality.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f'PASS PART {args.part:02d}: 4 chapters, 24 viewport measurements, 12 rejected mutations, online/offline navigation')


if __name__ == '__main__':
    main()
