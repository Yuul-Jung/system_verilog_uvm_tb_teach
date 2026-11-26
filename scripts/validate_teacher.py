#!/usr/bin/env python3
"""원본의 절 전체 텍스트·코드·SVG·TB와 교수용 발행본을 대조한다."""

import argparse
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent.parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and (self.skip or 'teach-note' in dict(attrs).get('class', '').split()):
            self.skip += 1

    def handle_endtag(self, tag):
        if tag == 'div' and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def text(fragment):
    parser = Text()
    parser.feed(fragment)
    return re.sub(r'\s+', ' ', ''.join(parser.parts)).strip()


def validate_page(page, original, chapter, source):
    errors = []
    sections = lambda value: re.findall(r'<section\b[^>]*id="(s\d+)"(.*?)</section>', value, re.S)
    actual, expected = sections(page), sections(original)
    if [s[0] for s in actual] != [s[0] for s in expected]:
        errors.append('section order/count')
    for (sid, body), (expected_id, baseline) in zip(actual, expected):
        if text(body) != text(baseline):
            errors.append(f'{sid}: original section content changed')
        if 'class="teach-note"' not in body:
            errors.append(f'{sid}: missing teaching explanation')
    for tag in ('pre', 'svg'):
        blocks = lambda value: re.findall(rf'<{tag}\b[^>]*>.*?</{tag}>', value, re.S)
        before, after = blocks(original), blocks(page)
        if tag == 'pre':
            before = [text(b) for b in before]
            after = [text(b) for b in after]
        if before != after:
            errors.append(f'{tag}: original blocks changed')
    source_code = (source / chapter['source_tb']).read_text().strip()
    codes = [html.unescape(re.sub(r'<[^>]+>', '', c)).strip()
             for c in re.findall(r'<pre\b[^>]*>(.*?)</pre>', page, re.S)]
    if source_code not in codes:
        errors.append('primary TB differs')
    if 'EXECUTED_OBSERVATION' not in page and chapter['number'] <= 3:
        errors.append('observation status missing')
    if re.search(r'/home/|/tmp/|github_pat_|ghp_[A-Za-z0-9]{20}', page):
        errors.append('private data')
    for href in re.findall(r'href="([^"]+)"', page):
        if not href.startswith(('https:', 'http:', '#', 'mailto:')) and not (ROOT / href.split('#')[0]).is_file():
            errors.append(f'broken local link: {href}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--chapter', type=int)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()
    course = json.loads((ROOT / 'course.json').read_text())
    assert len(course['planned_chapters']) == 24
    assert [c['number'] for c in course['chapters']] == list(range(1, len(course['chapters']) + 1))
    failures = []
    for chapter in course['chapters']:
        if args.chapter and chapter['number'] != args.chapter:
            continue
        original = (args.source / chapter['source_html']).read_text()
        page_path = ROOT / f"{chapter['slug']}_{chapter['version']}.html"
        page = page_path.read_text()
        blob = subprocess.check_output(['git', 'hash-object', chapter['source_html']], cwd=args.source, text=True).strip()
        assert blob == chapter['source_blob'], 'source Blob changed'
        errors = validate_page(page, original, chapter, args.source)
        failures.extend(f"CH{chapter['number']:02d}: {e}" for e in errors)
        if args.self_test:
            mutations = (re.sub(r'(<pre\b[^>]*>)', r'\1TAMPERED', page, count=1),
                         re.sub(r'<svg\b.*?</svg>', '', page, count=1, flags=re.S),
                         re.sub(r'<section\b.*?</section>', '', page, count=1, flags=re.S))
            assert all(validate_page(m, original, chapter, args.source) for m in mutations)
            print(f"CH{chapter['number']:02d} adversarial: code / SVG / section mutations rejected")
        print(f"CH{chapter['number']:02d}: sections={len(re.findall('<section ', original))} "
              f"codeboxes={len(re.findall('<pre ', original))} SVG={len(re.findall('<svg ', original))} "
              + ('FAIL' if errors else 'PASS'))
    for failure in failures:
        print('FAIL ' + failure)
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
