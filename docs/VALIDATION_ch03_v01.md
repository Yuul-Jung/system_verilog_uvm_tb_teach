# 제03장 교수용 v01 검증

- 확인일: 2026-11-26 (Asia/Seoul). 최신 원본 외부 AI 검증·수정 완료를 사용자가 확인했다.
- 원본 기준: `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 과정 `v60`.
- 원본 페이지: `ch03_reusable_stimulus_v04.html`, Blob `4d8e82acddb9321d0caf45b2ca4b61bed095e196`.
- 교수용 페이지 SHA256: `e0f1cc2a4df0265ddf0e1077a648490b42c65ce366bd40bd0a74a08723179b59`.
- TEACHING_RULES.md 23개 항목 전체 및 과정 AGENTS.md·중앙 rule_md(028248a19afc66e9aafdab393fbe0de10a3930ca)를 적용했다.

## 내용·기술 검토

task의 시간 대기와 function의 정수 계산, automatic의 호출별 저장 공간을 실제 구문으로 설명했다. RTL 73행·TB 141행의 모든 비공백 행 풀이를 포함한다. 첫 8표본 100~170ns, 두 번째 요청 180ns와 적용 255/256ns, 전체 40표본·정상 종료 810ns를 코드와 대조했다. 2,000ns watchdog는 진행성 안전장치이고 기능 자동 판정이 아님을 명시했다. HIGH 수가 같은 잘못된 파형과 X 표본을 현재 TB가 놓칠 수 있다는 한계를 해설했다.

## 실제 정합성 및 반례 실행

명령: `python3 scripts/validate_teacher.py --source <원본_체크아웃> --chapter 3 --self-test`

종료 코드 0. 아래는 실제 출력이다.

```text
CH03 adversarial: code / SVG / section mutations rejected
CH03: sections=8 codeboxes=8 SVG=1 PASS
```

원본 각 절의 전체 텍스트·코드 박스 내용과 순서·SVG 원문 및 실제 주 TB를 대조했다. 코드·SVG·절 훼손 반례 3건이 각각 거절되었다. 필수 파일 링크와 개인정보 패턴도 검사했다.

## 실제 화면 검사

명령: `PYTHONPATH=<Playwright_설치경로> python3 scripts/check_teacher_browser.py 3 --source <원본_체크아웃>`

[측정 JSON](evidence/ch03_v01/browser.json)의 6폭(1920·1366·1024·768·390·320px) 모두 flagged=0. 교수용 행별 표를 펼친 상태에서도 전체 가로 넘침, SVG 문자 경계 초과·충돌이 없었다. PART 한 개·같은 부의 발행 CHAPTER·현재 장 하위 SECTION, 절 이동, 모바일 메뉴·Escape, 모든 코드 박스의 실제 클립보드를 검사했다.

[데스크톱](evidence/ch03_v01/page-1366.png), [모바일](evidence/ch03_v01/page-390.png), [보충 해설](evidence/ch03_v01/teaching.png)을 직접 열어 확인했다. 도식별 PNG는 같은 증거 폴더에 보존한다.

새 RTL_SIM은 **NOT_RUN**. 원본의 **EXECUTED_OBSERVATION** 및 기존 실측 로그·예상 파형의 구분을 유지했다. 합성·보드 검증은 NOT_RUN. 원본 저장소의 작업 트리 변경은 없다.
