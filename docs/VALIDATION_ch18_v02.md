# 제18장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch18_sequence_driver_v04.html`, Blob `7485a07685b8821142d321e6aff0ffcb22443165`.
- 교수용 과정 v30. 원본 8절·코드 박스 9개·SVG 1개 및 기존 CSS 유지.
- Item/Sequence/Sequencer/Driver의 책임, 타입 매개변수, start_item/finish_item/get_next_item/item_done 호출, constraint와 직접 대입, Driver의 적용/표본 검사, 큐 이력 및 제19장 연계를 구문별로 보강했다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 행 | 최대 묶음 |
|---|---:|---:|---:|---:|
| `reference_rtl/pwm_core.v` | 19 | 19 | 70 | 7 |
| `tb/ch18/tb_pwm_sequence_driver.sv` | 13 | 37 | 227 | 10 |
| `scripts/run_ch18.sh` | 3 | 6 | 37 | 10 |

원본 HTML 절·pre·SVG·정규화 텍스트와 기존 스타일 일치, 소스 비공백 행 범위 누락/중복 없음, 공통 PWM 해설 유지. RTL 동작을 별도 JS 계산으로 추적하여 105/265/425ns 적용과 하강 에지 24표본의 11000000/11111100/00000000을 확인했다. 이는 코드 기반 계산이며 신규 RTL 시뮬레이션 또는 실측이 아니다. 신규 RTL/UVM_SIM·합성·보드·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 기존 정상/부정 XSIM 실행 증거 및 v25 화면 증거는 해당 시점 기록으로 유지한다. 원본 저장소는 변경하지 않았다.
