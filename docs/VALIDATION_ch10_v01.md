# 제10장 교수용 v01 검증

- 확인일: 2026-11-26 (Asia/Seoul). 최신 원본 외부 AI 검증·수정 완료를 사용자가 확인했다.
- 원본 기준: `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 과정 `v60`.
- 원본 페이지: `ch10_corner_reset_timeout_v05.html`, Blob `cefdc418474eb3cda20e2eba577c5057a03f3235`.
- 교수용 페이지 SHA256: `97949f965003ee95e00c345071262691cda6026939b48486671427eec1e25b0e`.
- TEACHING_RULES.md 23개 항목 전체 및 과정 AGENTS.md·중앙 rule_md(028248a19afc66e9aafdab393fbe0de10a3930ca)를 적용했다.

## 내용·기술 검토

0/8·8/8 경계와 총48표본、pending0+목표Active 두 조건、요청 누락 시 이전 정상 상태 검사를 대조했다. 488ns 출력 차단·489ns 에지 전 상태 유지·495/496ns 동기 리셋、336ns 관찰 반전·356ns 적용 기한을 해설했다. RTL73행·TB183행·Bash69행의 전체 비공백 구문을 설명하고 전용 진단+비정상 종료라는 부정 시험 판정을 보존했다. 새 RTL 실행은 NOT_RUN이다.

## 실제 정합성 및 반례 실행

명령: `python3 scripts/validate_teacher.py --source <원본_체크아웃> --chapter 10 --self-test`

종료 코드 0. 아래는 실제 출력이다.

```text
CH10 adversarial: code / SVG / section mutations rejected
CH10: sections=8 codeboxes=11 SVG=1 PASS
```

원본 각 절의 전체 텍스트·코드 박스 내용과 순서·SVG 원문 및 실제 주 TB를 대조했다. 코드·SVG·절 훼손 반례 3건이 각각 거절되었다. 필수 파일 링크와 개인정보 패턴도 검사했다.

## 실제 화면 검사

명령: `PYTHONPATH=<Playwright_설치경로> python3 scripts/check_teacher_browser.py 10 --source <원본_체크아웃>`

[측정 JSON](evidence/ch10_v01/browser.json)의 6폭(1920·1366·1024·768·390·320px) 모두 flagged=0. 교수용 행별 표를 펼친 상태에서도 전체 가로 넘침, SVG 문자 경계 초과·충돌이 없었다. PART 한 개·같은 부의 발행 CHAPTER·현재 장 하위 SECTION, 절 이동, 모바일 메뉴·Escape, 모든 코드 박스의 실제 클립보드를 검사했다.

[데스크톱](evidence/ch10_v01/page-1366.png), [모바일](evidence/ch10_v01/page-390.png), [보충 해설](evidence/ch10_v01/teaching.png)을 직접 열어 확인했다. 도식별 PNG는 같은 증거 폴더에 보존한다.

새 RTL_SIM은 **NOT_RUN**. 원본의 **PASS** 및 기존 실측 로그·예상 파형의 구분을 유지했다. 합성·보드 검증은 NOT_RUN. 원본 저장소의 작업 트리 변경은 없다.
