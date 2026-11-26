# 원본 대조에서 발견한 항목

원본 저장소는 읽기 전용이며 아래 항목을 수정하지 않았다. 교수용 자료에서는 원본을 보존하고 실제 근거를 인접 보충 설명에 명시한다.

## CH12-01 · XCRG 보고서 위치 표기

- 확인일: 2026-11-26, 원본 `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch12_functional_coverage_v03.html` 06절.
- 원본 문장: 출력된 폴더의 `output.log` 및 `report/dashboard.html` 확인 안내.
- 실제 근거: [보존 xcrg.log](https://github.com/Yuul-Jung/system_verilog_uvm_tb/blob/2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708/docs/evidence/v59/runs/ch12/xcrg.log)는 `Functional Coverage HTML Report directory : report/functionalCoverageReport`를 기록한다. 로컬 보존 실행 폴더 두 개와 공개 증거 파일도 해당 하위 경로에 있다.
- 실제 파일: [dashboard.html](https://github.com/Yuul-Jung/system_verilog_uvm_tb/blob/2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708/docs/evidence/v59/runs/ch12/report/functionalCoverageReport/dashboard.html).
- 영향: 시뮬레이션·커버리지 수치에는 영향 없으며, 수동으로 보고서를 여는 안내 경로에 영향이 있다.
- 교수용 조치: 06절 보충 설명에서 보존 XSIM 2024.2의 실제 상대 경로를 안내한다. 다른 도구 버전에서는 xcrg 출력의 report directory를 확인하도록 명시한다. 원본 수정은 수행하지 않았다.

## CH14-01 · 시나리오 수의 이전 표현

- 확인일: 2026-11-26, 동일 원본 커밋의 `ch14_fifo_flow_control_v04.html` 05절.
- 원본의 ‘네 시나리오’ 문장과 달리 현재 전체 TB 및 보존 v04 실측에는 T1~T5 다섯 시험이 있다. T5는 정지 비트 오류의 framing_error·미저장을 확인한다.
- 영향: 실행 코드와 보존 결과는 다섯 시험을 포함하며 정상이다. 본문 범위 설명만 이전 표현이다.
- 교수용 조치: 00·04·05절에서 현재 다섯 시나리오와 T5의 의미를 명시했다. 원본은 수정하지 않았다.

## CH24-01 · 상단 배너의 이전 버전 문구

- 확인일: 2026-11-26, 동일 원본 커밋의 `ch24_regression_ci_reporting_v04.html`.
- 원본 페이지 파일·course.json은 v04이지만 상단 chip에는 ‘원본 RTL 변경 없음 · v03’이 남아 있다.
- 영향: 실행 코드·보고서·회귀 결과에는 영향이 없다. 상단 표시 문구만 이전 버전이다.
- 교수용 조치: 원본 배너를 보존했다. 페이지 첫 안내 및 course.json·장별 검증 기록의 원본 기준은 정확한 v04·Blob을 명시한다. 원본 문구 수정은 별도 항목으로 남긴다.
