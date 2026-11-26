#!/usr/bin/env python3
"""한 장의 원본 HTML을 보존하며 절별 교수용 보충 해설을 삽입한다."""

import argparse
import html
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--base", type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=source, text=True).strip()
    source_course = json.loads((source / "course.json").read_text())
    original = source_course["chapters"][args.number - 1]
    name = f"{original['slug']}_{original['version']}.html"
    blob = subprocess.check_output(["git", "rev-parse", f"HEAD:{name}"], cwd=source, text=True).strip()
    notes = json.loads((ROOT / f"content/ch{args.number:02d}_notes.json").read_text())
    for line_table in notes.pop('__lines__', []):
        if 'reuse' in line_table:
            line_table = json.loads((ROOT / line_table['reuse']).read_text())
        lines = (source / line_table['path']).read_text().splitlines()
        covered = set()
        rows = []
        for span, explanation in line_table['rows']:
            bounds = [int(v) for v in span.split('-')]
            start, end = bounds[0], bounds[-1]
            assert not covered.intersection(range(start, end + 1)), 'overlapping line commentary'
            covered.update(range(start, end + 1))
            fragment = '\n'.join(lines[start - 1:end])
            rows.append(f'<tr><td>{span}</td><td><code class="teach-fragment">{html.escape(fragment)}</code></td><td>{explanation}</td></tr>')
        assert all(i in covered for i, line in enumerate(lines, 1) if line.strip()), 'missing source line commentary'
        table = (f'<h4>{html.escape(line_table["path"])} · 실제 행별 풀이</h4><details><summary>전체 비공백 행의 코드·의도 펼치기</summary>'
                 '<table><thead><tr><th scope="col">행</th><th scope="col">실제 코드</th><th scope="col">이유와 동작</th></tr></thead><tbody>'
                 + ''.join(rows) + '</tbody></table></details>')
        notes[line_table['section']] += table
    page = args.base.read_text() if args.base else (source / name).read_text()
    if args.base and args.number == 1:
        page = page.replace('기존 Icarus 관찰 실행 완료', '실행 미검증')
    sections = list(re.finditer(r'<section\b[^>]*id="(s\d+)".*?</section>', page, re.S))
    assert set(notes) <= {m[1] for m in sections}, "unknown section in notes"
    for section in reversed(sections):
        if section[1] in notes:
            addition = f'\n<div class="teach-note">{notes[section[1]]}</div>\n'
            page = page[:section.end() - 10] + addition + page[section.end() - 10:]
    if not args.base:
        style = re.search(r'<style>(.*?)</style>', (ROOT / "ch01_teacher_v01.html").read_text(), re.S)[0]
        page = page.replace('</head>', style + '</head>', 1)
        page = page.replace('<title>', '<title>교수용 해설서 · ', 1)
        page = page.replace('class="kicker">', 'class="kicker">교수용 해설서 · ', 1)
        page = page.replace('<main class="content" id="main-content">',
                            '<main class="content" id="main-content">' +
                            f'<p>원본 제{args.number:02d}장 · {original["version"]}의 절·그림·전체 코드·실습을 보존한 교수용 해설서입니다.</p>', 1)
    page = re.sub(r'교수용 보충자료 · v\d+', f'교수용 보충자료 · {args.version}', page)
    page = page.replace('</style>', '.teach-note details table{min-width:680px}.teach-note details th:first-child,.teach-note details td:first-child{min-width:60px;white-space:nowrap}.teach-note details .teach-fragment{min-width:250px}</style>', 1)
    page = re.sub(r'CH(\d+) 교수용 v\d+', rf'CH\1 교수용 {args.version}', page)
    if not args.base:
        page = re.sub(rf'CH{args.number:02d} {original["version"]}',
                      f'CH{args.number:02d} 교수용 {args.version} · 원본 {original["version"]}', page)
    remote = f"https://github.com/Yuul-Jung/system_verilog_uvm_tb/blob/{commit}/"
    def link(match):
        value = html.unescape(match[1])
        if value.startswith('https://github.com/Yuul-Jung/system_verilog_uvm_tb/blob/'):
            value = re.sub(r'/blob/[^/]+/', f'/blob/{commit}/', value)
        elif not urlsplit(value).scheme and not value.startswith(('#', 'assets/')) and value != 'index.html':
            value = remote + value
        return 'href="' + html.escape(value, quote=True) + '"'
    page = re.sub(r'href="([^"]+)"', link, page)
    course = json.loads((ROOT / "course.json").read_text())
    record = dict(id=original['id'], number=args.number, title=original['title'],
                  slug=f'ch{args.number:02d}_teacher', version=args.version,
                  source_html=name, source_version=original['version'], source_blob=blob,
                  source_commit=commit, source_course_version=source_course['version'],
                  source_tb=original['source'], rtl_simulation="NOT_RUN",
                  original_execution="EXECUTED_OBSERVATION" if args.number <= 3 else "PASS")
    previous = next((c for c in course['chapters'] if c['number'] == args.number), None)
    course['chapters'] = sorted([c for c in course['chapters'] if c['number'] != args.number] + [record], key=lambda c: c['number'])
    course['source_commit'] = commit
    course['external_review_confirmation'] = {"date": "2026-11-26", "confirmed_by": "user", "status": "COMPLETE"}
    if not previous or previous['version'] != args.version:
        course['version'] = f"v{int(course['version'][1:]) + 1:02d}"
    for c in course['planned_chapters']:
        src = source_course['chapters'][c['number'] - 1]
        c.update(source_html=f"{src['slug']}_{src['version']}.html", source_version=src['version'],
                 status='published' if any(p['id'] == c['id'] for p in course['chapters']) else 'planned')
    snapshot = dict(title=course['site_title'], short_title=course['course_code'], home_label="전체 교수용 해설서",
                    chapters=[dict(id=c['id'], number=c['number'], title=c['title'], file=f"{c['slug']}_{c['version']}.html") for c in course['chapters']])
    serialized = json.dumps(snapshot, ensure_ascii=False, separators=(',', ':'))
    page = re.sub(r'window.COURSE=\{.*?\};', 'window.COURSE=' + serialized + ';', page, flags=re.S)
    (ROOT / f"{record['slug']}_{args.version}.html").write_text(page)
    (ROOT / 'course.json').write_text(json.dumps(course, ensure_ascii=False, indent=2) + '\n')
    script = ROOT / 'assets/site.js'
    script.write_text(re.sub(r'const fallback = window.COURSE \|\| \{.*?\};',
                            'const fallback = window.COURSE || ' + json.dumps(snapshot, ensure_ascii=False, indent=2) + ';', script.read_text(), count=1, flags=re.S))
    index = (ROOT / 'index.html').read_text()
    for c in course['planned_chapters']:
        index = re.sub(rf'https://yuul-jung.github.io/system_verilog_uvm_tb/ch{c["number"]:02d}_[^"\s]+',
                       'https://yuul-jung.github.io/system_verilog_uvm_tb/' + c['source_html'], index)
    for c in course['chapters']:
        index = re.sub(rf'(<tr><td>{c["number"]:02d}</td><td>.*?</td><td>).*?(</td>)',
                       rf'\g<1><a href="{c["slug"]}_{c["version"]}.html">해설서 보기</a>\2', index, count=1)
    index = re.sub(r'현재 발행 \d+/24장', f'현재 발행 {len(course["chapters"])}/24장', index)
    index = re.sub(r'window.COURSE=\{.*?\};', 'window.COURSE=' + serialized + ';', index, flags=re.S)
    (ROOT / 'index.html').write_text(index)
    print(f"CH{args.number:02d} {args.version}: {len(sections)} sections; source {commit[:7]} blob {blob}")


if __name__ == '__main__':
    main()
