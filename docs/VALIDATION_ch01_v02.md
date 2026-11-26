# 제01장 교수용 해설서 v02 검증

- 확인일: 2026-11-26 (Asia/Seoul). 사용자가 최신 원본 외부 AI 검증·수정 완료를 명시적으로 확인했다.
- 원본 원격 main / 로컬: `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 과정 v60.
- 원본 페이지: `ch01_testbench_basics_v05.html`, Blob `080bc24ec12d33d2ea081345d96a076571aa4338`.
- 공통 규칙: `rule_md` 원격·로컬 `028248a19afc66e9aafdab393fbe0de10a3930ca`.
- TEACHING_RULES.md 1~23항 전체를 읽고 적용했다. 기존 8절의 해설과 RTL 13행·TB 75행 풀이를 유지하고 4상태, 조합회로/물리 지연, 1,024개 입력 조합 대비 네 관찰 사례, 같은 10ns의 실행 순서와 검증 범위를 보강했다.

## 정합성 및 적대적 검사

`python3 scripts/validate_teacher.py --source <원본_체크아웃> --chapter 1 --self-test`

실제 종료 코드 0. 원본 8절의 전체 텍스트, 9개 코드 박스의 내용·순서, 3개 SVG 원문, 실제 TB와의 일치를 검사했다. 코드·SVG·절을 각각 훼손한 3개 변형본은 모두 거절했다. 기존 v01의 TB 코드 박스 상태 표기가 원본과 달랐던 부분은 원본의 ‘실행 미검증’으로 복원했다. 보존된 Icarus 관찰 증거는 별도 실행 결과 영역에 유지한다.

## 실제 Chrome 검사

`PYTHONPATH=<Playwright_설치경로> python3 scripts/check_teacher_browser.py 1 --source <원본_체크아웃>`

실제 종료 코드 0. [브라우저 측정](evidence/ch01_v02/browser.json): 1920·1366·1024·768·390·320px 모두 전체 가로 넘침 0, SVG 문자 경계 초과·문자 충돌 0. PART 한 개·현재 CHAPTER 하위 SECTION, 절 링크, 모바일 열기·Escape 닫기, 9개 코드 박스의 실제 클립보드 내용 일치를 확인했다. 데스크톱·모바일 및 세 SVG 스크린샷도 직접 열어 가독성을 확인했다.

- [데스크톱](evidence/ch01_v02/page-1366.png), [모바일](evidence/ch01_v02/page-390.png), [추가 문답](evidence/ch01_v02/teaching.png)
- [포트 도식](evidence/ch01_v02/svg1.png), [흐름도](evidence/ch01_v02/svg2.png), [예상 타이밍도](evidence/ch01_v02/svg3.png)

새 RTL 시뮬레이션은 NOT_RUN. 기존 EXECUTED_OBSERVATION을 자동 PASS로 바꾸지 않았다. 원본 저장소의 파일과 작업 트리에는 변경이 없다. 이 검증은 교수용 콘텐츠·브라우저 검증이며 합성·보드 시험의 증거는 아니다.
