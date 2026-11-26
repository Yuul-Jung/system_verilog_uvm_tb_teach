# 제15장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch15_axi4lite_register_verification_v03.html`, Blob `11cd6f719a5a7538a6919b1f68d71961db9b741e`.
- 교수용 과정 v31. 원본 8절·코드 박스 10개·SVG 1개 및 기존 CSS 유지.
- 다섯 채널의 방향과 handshake, 저장 플래그/commit, 바이트 strobe 및 indexed part-select, live payload 변경, B/R backpressure, 리셋 취소, 실제 독립 관찰 계수와 T1~T5를 구문별로 보강했다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 행 | 최대 묶음 |
|---|---:|---:|---:|---:|
| `reference_rtl/axi4lite_slave_adapter.v` | 7 | 19 | 121 | 12 |
| `reference_rtl/custom_register_bank.v` | 8 | 18 | 134 | 13 |
| `tb/ch15/tb_axi4lite_registers.sv` | 12 | 40 | 254 | 10 |
| `scripts/run_ch15.sh` | 2 | 6 | 24 | 6 |

원본 HTML 절·pre·SVG·정규화 텍스트와 기존 스타일 일치, 4개 소스 비공백 행 범위 누락/중복 없음. JS 바이트 마스크 계산으로 11BB33DD, 주소 별칭 110→10, CONTROL5 및 원본 task 호출 수 6쓰기응답/12읽기응답을 확인했다. 상대 에지 표는 교육용 코드 추적이지 신규 실측이 아니다. 신규 RTL_SIM·합성·보드·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 기존 Icarus PASS 및 v25 화면 증거를 해당 시점 기록으로 유지한다. 원본 저장소는 변경하지 않았다.
