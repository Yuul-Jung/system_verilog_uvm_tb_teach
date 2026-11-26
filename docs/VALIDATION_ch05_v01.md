# 제05장 교수용 v01 검증

- 확인일: 2026-11-26 (Asia/Seoul). 최신 원본 외부 AI 검증·수정 완료를 사용자가 확인했다.
- 원본 기준: `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 과정 `v60`.
- 원본 페이지: `ch05_verification_types_v05.html`, Blob `1c818b81e1872acd19f4972aa3ba6efc7487cb33`.
- 교수용 페이지 SHA256: `24eaa6ab5eb0121d488da3400287df6fef0aa27d22a97a8b6eacbe0d52ff44c7`.
- TEACHING_RULES.md 23개 항목 전체 및 과정 AGENTS.md·중앙 rule_md(028248a19afc66e9aafdab393fbe0de10a3930ca)를 적용했다.

## 내용·기술 검토

logic/bit에서 xxxx0101→00000101 변환과 손실된 미정값 복구 불가를 설명했다. 10비트 packed 구조체의 [9:2]/[1]/[0]와 65×4+3=263 계산, 사례 이름 enum과 DUT FSM의 구분, 4사례·12포트 조건·6검사 집계 단위를 대조했다. 원본 RTL 13행·TB 131행의 비공백 행 전체를 해설했다. 네 사례는 1·2·3·4ns에 관찰하고 새 시뮬레이션은 NOT_RUN이다.

## 실제 정합성 및 반례 실행

명령: `python3 scripts/validate_teacher.py --source <원본_체크아웃> --chapter 5 --self-test`

종료 코드 0. 아래는 실제 출력이다.

```text
CH05 adversarial: code / SVG / section mutations rejected
CH05: sections=8 codeboxes=10 SVG=1 PASS
```

원본 각 절의 전체 텍스트·코드 박스 내용과 순서·SVG 원문 및 실제 주 TB를 대조했다. 코드·SVG·절 훼손 반례 3건이 각각 거절되었다. 필수 파일 링크와 개인정보 패턴도 검사했다.

## 실제 화면 검사

명령: `PYTHONPATH=<Playwright_설치경로> python3 scripts/check_teacher_browser.py 5 --source <원본_체크아웃>`

[측정 JSON](evidence/ch05_v01/browser.json)의 6폭(1920·1366·1024·768·390·320px) 모두 flagged=0. 교수용 행별 표를 펼친 상태에서도 전체 가로 넘침, SVG 문자 경계 초과·충돌이 없었다. PART 한 개·같은 부의 발행 CHAPTER·현재 장 하위 SECTION, 절 이동, 모바일 메뉴·Escape, 모든 코드 박스의 실제 클립보드를 검사했다.

[데스크톱](evidence/ch05_v01/page-1366.png), [모바일](evidence/ch05_v01/page-390.png), [보충 해설](evidence/ch05_v01/teaching.png)을 직접 열어 확인했다. 도식별 PNG는 같은 증거 폴더에 보존한다.

새 RTL_SIM은 **NOT_RUN**. 원본의 **PASS** 및 기존 실측 로그·예상 파형의 구분을 유지했다. 합성·보드 검증은 NOT_RUN. 원본 저장소의 작업 트리 변경은 없다.
