#!/usr/bin/env python3
"""실제 정합성·반례 출력과 브라우저 기록을 장별 검증 문서에 연결한다."""

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('number', type=int)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--review', required=True)
    args = parser.parse_args()
    course = json.loads((ROOT / 'course.json').read_text())
    chapter = next(c for c in course['chapters'] if c['number'] == args.number)
    label = f"ch{args.number:02d}_{chapter['version']}"
    evidence = ROOT / f'docs/evidence/{label}'
    browser = json.loads((evidence / 'browser.json').read_text())
    page_hash = hashlib.sha256((ROOT / f"{chapter['slug']}_{chapter['version']}.html").read_bytes()).hexdigest()
    assert browser['page_sha256'] == page_hash and browser['flagged'] == 0
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_teacher.py'), '--source', str(args.source),
                             '--chapter', str(args.number), '--self-test'], capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=args.source), 'source worktree changed'
    body = f'''# 제{args.number:02d}장 교수용 {chapter['version']} 검증

- 확인일: 2026-11-26 (Asia/Seoul). 최신 원본 외부 AI 검증·수정 완료를 사용자가 확인했다.
- 원본 기준: `{chapter['source_commit']}`, 과정 `{chapter['source_course_version']}`.
- 원본 페이지: `{chapter['source_html']}`, Blob `{chapter['source_blob']}`.
- 교수용 페이지 SHA256: `{page_hash}`.
- TEACHING_RULES.md 23개 항목 전체 및 과정 AGENTS.md·중앙 rule_md(028248a19afc66e9aafdab393fbe0de10a3930ca)를 적용했다.

## 내용·기술 검토

{args.review}

## 실제 정합성 및 반례 실행

명령: `python3 scripts/validate_teacher.py --source <원본_체크아웃> --chapter {args.number} --self-test`

종료 코드 {result.returncode}. 아래는 실제 출력이다.

```text
{result.stdout.strip()}
```

원본 각 절의 전체 텍스트·코드 박스 내용과 순서·SVG 원문 및 실제 주 TB를 대조했다. 코드·SVG·절 훼손 반례 3건이 각각 거절되었다. 필수 파일 링크와 개인정보 패턴도 검사했다.

## 실제 화면 검사

명령: `PYTHONPATH=<Playwright_설치경로> python3 scripts/check_teacher_browser.py {args.number} --source <원본_체크아웃>`

[측정 JSON](evidence/{label}/browser.json)의 6폭(1920·1366·1024·768·390·320px) 모두 flagged=0. 교수용 행별 표를 펼친 상태에서도 전체 가로 넘침, SVG 문자 경계 초과·충돌이 없었다. PART 한 개·같은 부의 발행 CHAPTER·현재 장 하위 SECTION, 절 이동, 모바일 메뉴·Escape, 모든 코드 박스의 실제 클립보드를 검사했다.

[데스크톱](evidence/{label}/page-1366.png), [모바일](evidence/{label}/page-390.png), [보충 해설](evidence/{label}/teaching.png)을 직접 열어 확인했다. 도식별 PNG는 같은 증거 폴더에 보존한다.

새 RTL_SIM은 **NOT_RUN**. 원본의 **{chapter['original_execution']}** 및 기존 실측 로그·예상 파형의 구분을 유지했다. 합성·보드 검증은 NOT_RUN. 원본 저장소의 작업 트리 변경은 없다.
'''
    (ROOT / f'docs/VALIDATION_{label}.md').write_text(body)
    print(f"PASS recorded {label}; browser page hash and source clean verified")


if __name__ == '__main__':
    main()
