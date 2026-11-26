# 제19장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch19_monitor_agent_scoreboard_v05.html`, Blob `56bcf0db00b89dbf32524c81d39f5c4aff001c6d`.
- 교수용 과정 v29. 원본 8절·코드 박스 9개·SVG 1개 및 기존 CSS 유지.
- 요청/관찰 객체, 분석 port/imp와 실제 호출, Agent 생성/연결, 독립 상태 모델, 4상태 판정, CORRUPT_SAMPLE 및 계수·완료 시점을 실제 구문으로 보강했다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 행 | 최대 묶음 |
|---|---:|---:|---:|---:|
| `reference_rtl/pwm_core.v` | 19 | 19 | 70 | 7 |
| `tb/ch19/tb_pwm_monitor_agent_scoreboard.sv` | 17 | 51 | 335 | 9 |
| `scripts/run_ch19.sh` | 3 | 6 | 37 | 10 |

원본 HTML 절·pre·SVG·정규화 텍스트와 기존 스타일 일치, 소스 비공백 행 범위 누락/중복 없음, 공통 PWM 해설 유지. 독립 JS 상태 계산으로 정상 31표본의 10개 대표 상태, 활성24표본, 세 PWM 8위상 패턴과 126ns 기대값0을 확인했다. 이는 코드 기반 계산이며 신규 RTL 시뮬레이션 또는 실측이 아니다. 신규 RTL/UVM_SIM·합성·보드·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 기존 정상/부정 XSIM 실행 증거 및 v25 화면 증거는 해당 시점 기록으로 유지한다. 원본 저장소는 변경하지 않았다.
