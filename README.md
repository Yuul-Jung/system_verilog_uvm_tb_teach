# RTL · SystemVerilog · UVM 교수용 해설서

6부 24장의 검증 학습안내서와 1:1 대응하는 교수용 보충 교재입니다. 원본 자료의 절 순서·그림·전체 코드·실행 증거를 보존하며, 개념의 필요성·신호 흐름·줄별 코드 풀이·수업 중 질문과 답변을 보강합니다.

- [전체 목차](index.html)
- [공개 HTML 해설서](https://yuul-jung.github.io/system_verilog_uvm_tb_teach/)
- [제01장 교수용 해설서 v02](ch01_teacher_v02.html) · [정합성·화면 검증](docs/VALIDATION_ch01_v02.md)
- [원본 학습안내서](https://yuul-jung.github.io/system_verilog_uvm_tb/)
- [교수용 확정 제작 규칙 23개 항목](TEACHING_RULES.md)
- [공통 제작 규칙](https://github.com/Yuul-Jung/rule_md)

원본 학습안내서의 외부 검증 수정과 별개로 관리합니다. 각 해설서는 기준 원본의 Git Blob SHA와 버전을 기록하며, 원본 변경 시 대응 장만 재검토합니다. 미제작 장에는 링크를 생성하지 않습니다.

6부 24장 발행을 완료했습니다. 원본 기준은 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`입니다. 각 절의 이론·수치·타이밍·실제 코드 행별 해설·판서·문답을 보강했습니다. 새 RTL 실행은 NOT_RUN이며 원본 실측과 구분합니다.

종합 품질 검증: [제1부](docs/PART01_QUALITY_REVIEW.md) · [제2부](docs/PART02_QUALITY_REVIEW.md) · [제3부](docs/PART03_QUALITY_REVIEW.md) · [제4부](docs/PART04_QUALITY_REVIEW.md) · [제5부](docs/PART05_QUALITY_REVIEW.md) · [제6부](docs/PART06_QUALITY_REVIEW.md). 원본 설명에서 발견한 세 항목은 [별도 기록](docs/SOURCE_ISSUES.md)에 보존했습니다.

[v25 기준 24장 최종 검증 보고서](docs/FINAL_REVIEW_v25.md) · [v25 기준 전체 파일 정합성](docs/evidence/final/integrity.json) · [v25 기준 공개 Pages 실제 검증](docs/evidence/publication/pages.json)

Pages는 `main` 루트의 정적 HTML을 제공합니다. `.nojekyll`로 원본 SystemVerilog·Python·SVG를 템플릿 처리 없이 배포합니다. 공개 배포의 실제 커밋·HTTP·SHA256·화면은 `scripts/check_publication.py`로 확인합니다.

<!-- PUBLISHED -->
- [제01장 · 테스트벤치의 첫 실행](ch01_teacher_v02.html) · [검증 기록](docs/VALIDATION_ch01_v02.md)
- [제02장 · Clock·Reset·이벤트](ch02_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch02_v01.md)
- [제03장 · 반복 자극과 작업 분리](ch03_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch03_v01.md)
- [제04장 · PASS/FAIL 자동 판정](ch04_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch04_v01.md)
- [제05장 · 검증 자료형과 타입](ch05_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch05_v01.md)
- [제06장 · 배열·큐·패키지](ch06_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch06_v01.md)
- [제07장 · 인터페이스·타이밍 분리](ch07_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch07_v01.md)
- [제08장 · 객체와 제약 기반 입력](ch08_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch08_v01.md)
- [제09장 · 참조 모델·스코어보드](ch09_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch09_v01.md)
- [제10장 · 경계조건·오류 주입](ch10_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch10_v01.md)
- [제11장 · 시간적 속성 검사](ch11_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch11_v01.md)
- [제12장 · 기능 커버리지](ch12_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch12_v01.md)
- [제13장 · UART 스트림 검증](ch13_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch13_v01.md)
- [제14장 · FIFO 및 흐름 제어](ch14_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch14_v01.md)
- [제15장 · AXI4-Lite 레지스터 검증](ch15_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch15_v01.md)
- [제16장 · MAC·NPU 정수 연산 검증](ch16_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch16_v01.md)
- [제17장 · 최소 UVM 환경](ch17_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch17_v01.md)
- [제18장 · Sequence에서 Driver까지](ch18_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch18_v01.md)
- [제19장 · Monitor·Agent·Scoreboard](ch19_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch19_v01.md)
- [제20장 · Factory·Config·Objection](ch20_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch20_v01.md)
- [제21장 · UVM 레지스터 추상화](ch21_teacher_v02.html) · [검증 기록](docs/VALIDATION_ch21_v02.md)
- [제22장 · 다중 Agent·VIP](ch22_teacher_v02.html) · [검증 기록](docs/VALIDATION_ch22_v02.md)
- [제23장 · NPU 통합 정답 비교](ch23_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch23_v01.md)
- [제24장 · 회귀·CI·검증 보고](ch24_teacher_v01.html) · [검증 기록](docs/VALIDATION_ch24_v01.md)
<!-- /PUBLISHED -->

교수용 해설 보강 v26: 제21장 v02에서 RAL 구문 및 API 인자, 객체 생성, 독립 예측 경로, 실제 행별 풀이를 세분화했다. [제21장 v02 검증](docs/VALIDATION_ch21_v02.md). 기존 v25 화면·Pages 증거는 해당 시점의 기록이며 v02 화면/공개 HTTP 신규 확인은 별도 수행 대상이다.

교수용 해설 보강 v27: 제22장 v02에서 두 Agent·Virtual Sequencer, Analysis Imp, AR 수락 시각과 IRQ 예상 상태, commit 큐, W1C 동시 충돌 및 구문별 해설을 보강했다. [제22장 v02 검증](docs/VALIDATION_ch22_v02.md). 신규 브라우저·공개 Pages 검사는 별도 수행 대상이다.
