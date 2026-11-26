# 제22장 교수용 v02 독립 보강 검증

- 원본 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, `ch22_multi_agent_vip_v05.html`, Blob `8118843b89e7e4a63cf706bf1ae6101d10a6b263`.
- 교수용 과정 v27. 원본 및 기존 v01의 절 순서·코드·SVG·CSS를 유지했다. v01 주소는 최신 v02로 이동한다.
- 두 Agent, virtual sequencer, analysis imp, AR 시각별 IRQ 기대값, commit 큐, W1C/set 우선, fork/join, backpressure, 정상/부정 판정 계수를 실제 코드에 맞춰 보강했다.

| 파일 | 기존 항목 | 개선 항목 | 비공백 소스 행 | 최대 묶음 행 |
|---|---:|---:|---:|---:|
| `reference_rtl/axi4lite_slave_adapter.v` | 5 | 19 | 121 | 12 |
| `reference_rtl/custom_register_bank.v` | 5 | 18 | 134 | 13 |
| `tb/ch22/tb_axi_multiagent_irq.sv` | 26 | 91 | 703 | 16 |
| `scripts/run_ch22.sh` | 3 | 8 | 34 | 6 |

## 직접 확인

고정 원본 HTML과 신규 HTML의 절 8개, pre 코드 박스 11개, SVG 1개 및 각 절 정규화 본문을 대조했다. 기존 CSS 인라인 스타일 동일, 4개 소스의 모든 비공백 행에 중복 없는 행 범위 해설, 마스크 예시 6개 수식 대조를 확인했다. RTL/TB/실행 스크립트 원본을 변경하지 않았다. H 기준 타이밍 표는 실제 코드에서 계산한 교육용 상대 시각이며 신규 실측이 아니다.

## 한계

신규 RTL/UVM_SIM·합성·보드·브라우저 6폭·공개 Pages HTTP는 NOT_RUN. 원본의 XSIM 정상 PASS와 CORRUPT_IRQ 부정 로그 및 이전 v25 화면/Pages 증거를 유지하며 새 검증 결과로 표시하지 않는다.
