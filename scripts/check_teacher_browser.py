#!/usr/bin/env python3
"""교수용 한 장을 6폭에서 렌더링하고 탐색·복사·SVG를 검사한다."""

import argparse
import functools
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import threading

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('chapter', type=int)
    parser.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location('source_browser', args.source / 'scripts/check_browser.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    course = json.loads((ROOT / 'course.json').read_text())
    chapter = next(c for c in course['chapters'] if c['number'] == args.chapter)
    out = ROOT / f"docs/evidence/ch{args.chapter:02d}_{chapter['version']}"
    out.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(QuietHandler, directory=str(ROOT)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/google-chrome', headless=True, args=['--no-sandbox'])
        context = browser.new_context(permissions=['clipboard-read', 'clipboard-write'], reduced_motion='reduce')
        page = context.new_page()
        for width in module.WIDTHS:
            page.set_viewport_size(dict(width=width, height=1000 if width >= 768 else 844))
            response = page.goto(f"http://127.0.0.1:{server.server_port}/{chapter['slug']}_{chapter['version']}.html")
            page.wait_for_selector('.course-ch-link[aria-current="page"]')
            page.evaluate('document.fonts.ready')
            row = page.evaluate(module.MEASURE)
            row.update(width=width, http=response.status,
                       part=page.locator('.course-part-heading').count() == 1,
                       section_count=page.locator('.toc-sections a').count() == page.locator('main section').count(),
                       same_part=page.locator('.course-ch-link').count() == sum((c['number'] - 1)//4 == (args.chapter - 1)//4 for c in course['chapters']))
            if width <= 768:
                page.locator('#mobile-menu').click()
                opened = page.locator('#mobile-menu').get_attribute('aria-expanded') == 'true'
                page.keyboard.press('Escape')
                row['mobile_menu'] = opened and page.locator('#mobile-menu').get_attribute('aria-expanded') == 'false'
            if width == 1366:
                # 모든 코드 박스에서 줄 번호·해설이 섞이지 않는지 실제 클립보드로 검사한다.
                row['copy_boxes'] = 0
                for block in page.locator('.codeblock').all():
                    expected = block.locator('pre').text_content()
                    block.locator('.codebar button').click()
                    page.wait_for_timeout(80)
                    assert page.evaluate('navigator.clipboard.readText()') == expected
                    row['copy_boxes'] += 1
                for index, svg in enumerate(page.locator('main svg').all(), 1):
                    svg.screenshot(path=str(out / f'svg{index}.png'))
                page.locator('.teach-note').last.scroll_into_view_if_needed()
                page.screenshot(path=str(out / 'teaching.png'))
                page.locator('.toc-sections a').last.click()
                row['section_jump'] = page.evaluate('location.hash') == page.locator('.toc-sections a').last.get_attribute('href')
            page.evaluate('scrollTo(0,0)')
            if width in (1366, 390):
                page.screenshot(path=str(out / f'page-{width}.png'))
            rows.append(row)
        browser.close()
    server.shutdown()
    bad = [r for r in rows if r['overflow'] or r['contentOverflow'] or r['headerTextClipped']
           or not r['part'] or not r['section_count'] or not r['same_part']
           or r.get('mobile_menu') is False or r.get('section_jump') is False
           or any(d['outside'] or d['collisions'] for d in r['diagrams'])]
    (out / 'browser.json').write_text(json.dumps(dict(chapter=args.chapter, rows=rows, flagged=len(bad)), ensure_ascii=False, indent=2) + '\n')
    print(f"CH{args.chapter:02d}: browser widths=6 flagged={len(bad)}")
    return 1 if bad else 0


if __name__ == '__main__':
    raise SystemExit(main())
