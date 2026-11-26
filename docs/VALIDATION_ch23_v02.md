# 제23장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch23_npu_integrated_scoreboard_v05.html`, Blob `9e9a9819f4b6235932f6e2eac3c1c8cc9dd8d379`.
- 교수용 과정 v32. 원본 8절·코드 박스 8개·SVG 2개 및 기존 CSS 유지.
- 데이터 폭·부호 확장·점수 패킹·독립 모델·파이프라인·실행 수락 및 거부를 실제 구문으로 보강했다. busy 쓰기 시험의 정확한 error 펄스 길이 및 영구 RAM 보존은 별도 독립 검사되지 않았음을 명시했다. 기존 교수용 s07 문구를 좁혔으며 원본 학습안내서는 보존한다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 행 | 최대 묶음 |
|---|---:|---:|---:|---:|
| `reference_rtl/npu_engine4.v` | 7 | 20 | 117 | 10 |
| `reference_rtl/npu_dsp_mac_lane.v` | 2 | 5 | 25 | 9 |
| `reference_rtl/dsp_multiplier.v` | 4 | 7 | 49 | 13 |
| `tb/ch23/tb_npu_integrated.sv` | 12 | 31 | 244 | 12 |
| `scripts/run_ch23.sh` | 2 | 5 | 22 | 6 |

원본 HTML 절·pre·SVG·정규화 텍스트와 기존 스타일 일치, 다섯 소스 비공백 행 범위 누락/중복 없음. 별도 JS/BigInt 계산으로 7개 점수 벡터, 극값 4개, 40비트 음수 확장 및 L1/2/64의 FSM 지연을 확인했다. 이는 코드 기반 산술/추적이며 RTL 실행이 아니다. 신규 RTL_SIM·합성·보드·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 기존 v05 Icarus 실행 증거 및 v25 화면 증거는 해당 시점 기록으로 유지한다. 원본 저장소는 변경하지 않았다.
