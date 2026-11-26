# 제20장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch20_factory_config_objection_v04.html`, Blob `4c946e22723b8d2ed9e7d7c95abf133916e9ff70`.
- 교수용 과정 v28. 원본 8절·코드 박스 9개·SVG 1개 및 기존 CSS 유지.
- Factory 등록/생성/virtual dispatch/$cast, Config DB 인자/경로/객체 동일성, Objection/완료 표본의 관계, 독립 모델의 판정 및 세 부정 시험을 실제 구문으로 보강했다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 행 | 최대 묶음 |
|---|---:|---:|---:|---:|
| `reference_rtl/pwm_core.v` | 19 | 19 | 70 | 7 |
| `tb/ch20/tb_pwm_factory_config_objection.sv` | 21 | 68 | 412 | 11 |
| `scripts/run_ch20.sh` | 3 | 9 | 53 | 10 |

원본 HTML 절·pre·SVG·정규화 텍스트와 기존 스타일 일치, 세 소스의 비공백 행 범위 누락/중복 없음, 정상24·부정17 활성 표본·정상31클록·적용지연60ns 산술 확인. 공통 PWM 해설을 보존했다. 타이밍 표는 코드 기반 계산이지 신규 실측이 아니다. 신규 RTL/UVM_SIM·합성·보드·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 기존 원본 정상2·부정3 실측 증거와 기존 v25 화면 증거는 해당 시점 기록으로 유지한다. 원본 저장소를 변경하지 않았다.
