# 제12장 교수용 v01 검증

- 확인일: 2026-11-26 (Asia/Seoul). 최신 원본 외부 AI 검증·수정 완료를 사용자가 확인했다.
- 원본 기준: `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 과정 `v60`.
- 원본 페이지: `ch12_functional_coverage_v03.html`, Blob `9a6db6d63c48fc47fa0b8fec04e888ac47a73c7c`.
- 교수용 페이지 SHA256: `11204a8f849021afe56c316c1664dd59dae581e3947e59c78773ea0c478a5797`.
- TEACHING_RULES.md 23개 항목 전체 및 과정 AGENTS.md·중앙 rule_md(028248a19afc66e9aafdab393fbe0de10a3930ca)를 적용했다.

## 내용·기술 검토

middle 단일bin과 개별값 방문、12교차분류와36합법입력조합、cov타입비율과12비트visited를 구분했다. 위상1~7,0의 듀티4 표본11100001、12×8=96표본、1950ns 종료를 실제 코드와 대조했다. RTL73행·TB156행·Bash32행의 전체 비공백 구문을 해설한다. 원본 보고서 경로 표기와 실측 생성 위치의 차이는 SOURCE_ISSUES.md에 별도 기록하고 보충에서 확인된 경로를 안내했다. 새 RTL/커버리지 실행은 NOT_RUN이다.

## 실제 정합성 및 반례 실행

명령: `python3 scripts/validate_teacher.py --source <원본_체크아웃> --chapter 12 --self-test`

종료 코드 0. 아래는 실제 출력이다.

```text
CH12 adversarial: code / SVG / section mutations rejected
CH12: sections=8 codeboxes=8 SVG=1 PASS
```

원본 각 절의 전체 텍스트·코드 박스 내용과 순서·SVG 원문 및 실제 주 TB를 대조했다. 코드·SVG·절 훼손 반례 3건이 각각 거절되었다. 필수 파일 링크와 개인정보 패턴도 검사했다.

## 실제 화면 검사

명령: `PYTHONPATH=<Playwright_설치경로> python3 scripts/check_teacher_browser.py 12 --source <원본_체크아웃>`

[측정 JSON](evidence/ch12_v01/browser.json)의 6폭(1920·1366·1024·768·390·320px) 모두 flagged=0. 교수용 행별 표를 펼친 상태에서도 전체 가로 넘침, SVG 문자 경계 초과·충돌이 없었다. PART 한 개·같은 부의 발행 CHAPTER·현재 장 하위 SECTION, 절 이동, 모바일 메뉴·Escape, 모든 코드 박스의 실제 클립보드를 검사했다.

[데스크톱](evidence/ch12_v01/page-1366.png), [모바일](evidence/ch12_v01/page-390.png), [보충 해설](evidence/ch12_v01/teaching.png)을 직접 열어 확인했다. 도식별 PNG는 같은 증거 폴더에 보존한다.

새 RTL_SIM은 **NOT_RUN**. 원본의 **PASS** 및 기존 실측 로그·예상 파형의 구분을 유지했다. 합성·보드 검증은 NOT_RUN. 원본 저장소의 작업 트리 변경은 없다.
