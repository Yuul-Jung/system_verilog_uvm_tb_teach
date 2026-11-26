#!/usr/bin/env python3
"""공개 Pages의 배포 커밋·실제 바이트·Chrome 화면을 확인한다."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import urllib.request

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://yuul-jung.github.io/system_verilog_uvm_tb_teach/'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--check-only', action='store_true', help='기록 파일 변경 없이 배포·바이트만 재확인')
    args = parser.parse_args()
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    build = json.loads(subprocess.check_output([
        'gh', 'api', 'repos/Yuul-Jung/system_verilog_uvm_tb_teach/pages/builds/latest'], text=True))
    assert build['status'] == 'built' and build['commit'] == commit, (build['status'], build['commit'])
    course = json.loads((ROOT / 'course.json').read_text())
    files = ['index.html', 'course.json'] + [f"{c['slug']}_{c['version']}.html" for c in course['chapters']]
    files += sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'assets').rglob('*') if p.is_file())

    def check_file(name):
        with urllib.request.urlopen(BASE + name + '?revision=' + commit, timeout=45) as response:
            data = response.read()
            status = response.status
        actual = hashlib.sha256(data).hexdigest()
        expected = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
        assert status == 200 and actual == expected, name
        return dict(file=name, http=status, sha256=actual)

    with ThreadPoolExecutor(max_workers=6) as pool:
        hashes = list(pool.map(check_file, files))
    if args.check_only:
        print(f'PASS public Pages build={commit} HTTP/SHA256 files={len(hashes)}')
        return

    from playwright.sync_api import sync_playwright
    spec = importlib.util.spec_from_file_location('original_browser', args.source / 'scripts/check_browser.py')
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    out = ROOT / 'docs/evidence/publication'
    out.mkdir(parents=True, exist_ok=True)
    screens = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/google-chrome', headless=True, args=['--no-sandbox'])
        context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'], reduced_motion='reduce')
        page = context.new_page()
        for name in ('index.html', 'ch01_teacher_v02.html', 'ch24_teacher_v01.html'):
            for width in (1366, 390):
                page.set_viewport_size(dict(width=width, height=1000 if width > 768 else 844))
                response = page.goto(BASE + name + '?revision=' + commit)
                page.wait_for_selector('.course-part-code')
                page.evaluate('document.fonts.ready')
                assert response.status == 200
                if name == 'index.html':
                    assert page.locator('main tbody tr').count() == 24
                    assert page.locator('main a[href*="_teacher_v"]').count() == 24
                else:
                    assert page.locator('.course-ch-link').count() == 4
                    assert page.locator('.course-nested-sections a').count() == (7 if name.startswith('ch24') else 8)
                    if width == 1366:
                        block = page.locator('.codeblock').first
                        expected = block.locator('pre').text_content()
                        block.locator('.codebar button').click()
                        page.wait_for_timeout(100)
                        assert page.evaluate('navigator.clipboard.readText()') == expected
                if width == 390:
                    page.locator('#mobile-menu').click()
                    assert page.locator('#mobile-menu').get_attribute('aria-expanded') == 'true'
                    page.keyboard.press('Escape')
                    assert page.locator('#mobile-menu').get_attribute('aria-expanded') == 'false'
                measure = page.evaluate(original.MEASURE)
                assert not any(measure[k] for k in ('overflow', 'contentOverflow', 'headerTextClipped'))
                assert not any(d['outside'] or d['collisions'] for d in measure['diagrams'])
                page.evaluate('scrollTo(0,0)')
                page.screenshot(path=str(out / f'{name[:-5]}-{width}.png'))
                screens.append(dict(file=name, width=width, http=200, measurement=measure))
        browser.close()
    result = dict(base=BASE, commit=commit, build='built', files=hashes, browser=screens,
                  rtl_simulation='NOT_RUN', remote_rtl_ci='NOT_RUN')
    (out / 'pages.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(f'PASS public Pages build={commit} files={len(hashes)} real Chrome screens={len(screens)}')


if __name__ == '__main__':
    main()
