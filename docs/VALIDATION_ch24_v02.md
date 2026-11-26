# 제24장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch24_regression_ci_reporting_v04.html`, Blob `f292c0c9c0987e54d6d8ca93388bd208ded759fb`.
- 교수용 과정 v33. 원본 7절·코드 박스 8개·SVG 2개 및 기존 CSS 유지.
- 시드와 XOR shift, 공통 비교기 및 전용 부정 검출, Python API/정규식/분포/종료 코드, YAML 및 보고서 책임을 실제 구문으로 보강했다. argparse 오류의 보고서 부재, TB Blob 기록과 DUT Blob 검증의 차이, 로그 유일성 및 추가 오류 검사 범위, 원격 CI 실행 여부를 구분했다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 행 | 최대 묶음 |
|---|---:|---:|---:|---:|
| `reference_rtl/uart_echo_controller.v` | 8 | 8 | 13 | 4 |
| `tb/ch24/tb_uart_regression.sv` | 8 | 21 | 99 | 9 |
| `scripts/run_ch24.py` | 9 | 26 | 153 | 13 |
| `scripts/run_ch24.sh` | 1 | 2 | 6 | 4 |
| `.github/workflows/ch24-regression.yml` | 3 | 9 | 30 | 7 |

원본 HTML 절·pre·SVG·정규화 텍스트와 기존 스타일 일치, 다섯 소스 비공백 행 범위 누락/중복 없음. 독립 JS 32비트 계산으로 시드1/7/42 분포 및 첫 상태 00042021, 0x20→0x21을 확인했다. 이는 코드 기반 계산이며 신규 RTL 실행이나 Python 실행기의 실제 반례 시험이 아니다. 신규 RTL_SIM·원격 CI·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 기존 Icarus 실행 증거 및 v25 화면 증거는 해당 시점 기록으로 유지한다. 원본 저장소는 변경하지 않았다.
