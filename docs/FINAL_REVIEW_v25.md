# 교수용 해설서 6부24장 최종 검증

2026-11-26 (Asia/Seoul). 제01장 기존 해설서 재검토부터 제24장까지 순차 제작하고 장별 검증·커밋·푸시·원격 파일 재조회를 수행했다. 각 부의 네 장이 완료될 때 별도 종합 품질 검증을 수행했다.

- 교수용 과정: v25, 발행24/24장. 제01장 v02, 제02~24장 v01. 기존 제01장 v01은 이력을 보존하며 발행 목차는 v02를 가리킨다.
- 원본: 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`. 사용자 확인으로 외부 AI 검증·수정 완료 상태를 확정한 뒤 제작했다.
- 중앙 규칙: `028248a19afc66e9aafdab393fbe0de10a3930ca`. 장별 제작 전 TEACHING_RULES.md 23개 항목을 읽고 AGENTS.md·교육 HTML·코드·도식 규칙을 적용했다.
- 원본 저장소는 읽기 전용으로 유지했으며 최종 작업 트리는 CLEAN이다. 원본 RTL·정상 TB·실측 증거를 수정하지 않았다.

## 변경 파일과 내용

| 파일 | 변경 목적 |
|---|---|
| `ch01_teacher_v02.html`, `ch02_teacher_v01.html`~`ch24_teacher_v01.html` | 각 원본 장과1:1 대응하는 교수용 해설 |
| `content/ch01_notes.json`~`content/ch24_notes.json`, 공통 RTL 행별 해설 JSON | 실제 구문·행 범위와 연결한 이론·계산·타이밍·판서·문답·오개념 |
| `course.json`, `index.html`, `assets/site.js`, `README.md` | 원본 커밋·페이지 Blob·버전·실행 상태 및 발행24장 탐색 |
| `scripts/build_teacher.py`, `validate_teacher.py`, `record_validation.py` | 원본 보존 생성·정합성/훼손 반례·실행 기록 |
| `scripts/check_teacher_browser.py`, `check_part.py` | 실제6폭 Chrome·코드 복사·도식·온라인/오프라인 목차 |
| `.nojekyll`, `scripts/check_remote.py`, `check_publication.py` | 정적 Pages 배포, 원격 Git/공개 HTTP 바이트·화면 대조 |
| `docs/VALIDATION_*`, `PART01_QUALITY_REVIEW.md`~`PART06_QUALITY_REVIEW.md`, `docs/evidence/` | 실제 실행 출력·측정 JSON·화면·수치 근거 |
| `docs/SOURCE_ISSUES.md` | 원본 표현 차이3건과 교수용 대응을 분리 기록 |

전체 원본191절·코드 박스227개·SVG29개를 보존했다. 제24장은7절, 다른 장은8절이다. 공통 `assets/site.css`는 원본과 바이트가 같다. 원본 코드 박스·복사 내용과 SVG 원문·순서, 각 절 전체 원문을 대조했고 새 해설은 해당 절 내부에 배치했다.

## 실제 검증 결과

| 검사 | 실제 결과·증거 |
|---|---|
| 정상24장 원본 정합성 | PASS · [최종 실행 출력](evidence/final/validation.txt) |
| 코드 변경·SVG 삭제·절 삭제 반례 | 장별3건×24=72건 모두 거절 |
| 원본 Blob·메타데이터·실제 주 TB·공통 CSS·기존 실행 상태 | PASS · [파일별 SHA256·총계](evidence/final/integrity.json) |
| 6부 별도 브라우저 검사 | 24장×6폭=144조합, flagged=0 |
| 실제 코드 복사·SVG 경계/충돌·표 펼침·모바일 메뉴/Escape·절 이동 | PASS · 장별 browser.json·PNG |
| 최종24장 공통 목차 | 온라인/manifest 차단48조합 PASS · [결과](evidence/final/navigation.json) |
| MAC 독립 수치 모델 | 21클록·valid12/10 · [실제 Python 출력](evidence/ch16_v01/model.txt) |
| NPU·회귀 수치 대조 | 네 분류·편향·41비트 극값·4/6/130클록·시드96표본/수락29 PASS · [결과](evidence/part06/math.json) |

부별 보고서: [제1부](PART01_QUALITY_REVIEW.md), [제2부](PART02_QUALITY_REVIEW.md), [제3부](PART03_QUALITY_REVIEW.md), [제4부](PART04_QUALITY_REVIEW.md), [제5부](PART05_QUALITY_REVIEW.md), [제6부](PART06_QUALITY_REVIEW.md).

기술 검토에서는 UVM component 계층과 Sequence/Item/Sample/config object, 정적 DUT·Interface를 구분했다. 실제 코드에 없는 Agent·Monitor·파이프라인·회로 기능을 구현된 것처럼 설명하지 않았다. 수치·관찰 시점·독립 모델의 출처와 검증 범위의 한계를 장별로 명시했다. 생성 단계에서 발견된 행 범위 누락과 최종 검사기의 장별 절 수 가정은 수정 후 재검증했다.

## 공개 배포와 원격 확인

[공개 교수용 해설서](https://yuul-jung.github.io/system_verilog_uvm_tb_teach/)는 `main` 루트의 정적 HTML로 배포했다. 처음 조회에서는 Pages가 비활성화되어404였으며, 활성화와 `.nojekyll` 적용 후 실제 배포를 확인했다. SystemVerilog 중괄호 등이 템플릿 처리되지 않도록 한다.

실제 배포 검사 기준 커밋은 `940b891681ecec6572480ea72115b63bb71ef393`이다. 이 최종 보고서·증거 추가는 교재 HTML·자산 바이트를 바꾸지 않는다. 마지막 문서 커밋 푸시 후에도 배포 커밋·공개 파일을 기록 변경 없이 다시 확인한다.

```text
PASS public Pages build=940b891681ecec6572480ea72115b63bb71ef393 files=28 real Chrome screens=6
```

[공개 검증 JSON](evidence/publication/pages.json)은24장·INDEX·course.json·자산의 HTTP200 및 로컬과 동일한 SHA256을 기록한다. 공개 INDEX·제01장·제24장의1366/390px 실제 Chrome6화면에서 탐색·모바일·코드 복사·넘침·도식을 검사하고 모든 PNG를 직접 열어 확인했다. 긴 제24장 도식은 [오른쪽 스크롤](evidence/ch24_v01/diagram-scroll.json)과 [전체 SVG 렌더링](evidence/ch24_v01/svg2-full.png)까지 확인했다.

로컬 HEAD와 원격 main 비교는 `git status`, `git log -1`, `git push origin main`, `git ls-remote origin refs/heads/main`으로 수행한다. `check_remote.py`는 원격 커밋으로 실제 파일을 내려받아 로컬 SHA256과도 대조한다. 최종 커밋 SHA와 원격 SHA는 실행 후 사용자 보고에 명시한다.

## 미해결·미실행 항목

교수용24장 제작·장별/부별 정합성·화면·원격/공개 배포 확인에 확인된 미해결 결함은 없다. 원본을 보존했으므로 다음 원본 표현의 정정은 별도 항목으로 남는다. 상세 근거와 교수용 대응은 [SOURCE_ISSUES.md](SOURCE_ISSUES.md)에 있다.

1. CH12: XCRG 보고서 경로 `report/dashboard.html` 대신 실제 `report/functionalCoverageReport/dashboard.html`.
2. CH14: 본문 ‘네 시나리오’ 대신 현재 T1~T5 다섯 시험.
3. CH24: 원본 v04 페이지 상단에 남은 이전 v03 배너 문구.

새 RTL/UVM_SIM·합성·보드·원격 RTL 회귀 CI는 **NOT_RUN**이다. 원본의 제01~03장 관찰 실습과 제04~24장 자동 PASS, 기존 Icarus/XSIM 실측·부정 시험·커버리지 및 최신 CH11/14/23 재실행 증거는 그대로 유지했다. 새로 실행한 HTML 검증·Python 수치 확인·브라우저·GitHub Pages 배포와 구분한다.
