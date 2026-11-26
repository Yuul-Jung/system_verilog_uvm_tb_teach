# 제21장 교수용 v02 독립 보강 검증

- 원본: 과정 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 페이지 `ch21_uvm_register_abstraction_v04.html`, Blob `e96080913581c31bd9b14c7f831774f9c4ce87b7`.
- 교수용 과정 v26. 원본 페이지와 기존 v01의 CSS·절·코드·SVG는 유지한다. v01 주소는 v02로 이동한다.
- 기존 교수용 본문은 보존하고 RAL 실제 호출·9인자 필드 구성·주소 맵·명시적 예측·읽기/쓰기 판정·부정 시험에 보충 해설을 추가했다. UVM 1.2 [공식 클래스 참조](https://www.accellera.org/images/downloads/standards/uvm/UVM_Class_Reference_Manual_1.2.pdf)와 실제 TB를 대조했다.

| 파일 | 기존 해설 항목 | 개선 항목 | 비공백 소스 행 | 최대 묶음 행 |
|---|---:|---:|---:|---:|
| `reference_rtl/axi4lite_slave_adapter.v` | 5 | 19 | 121 | 12 |
| `reference_rtl/custom_register_bank.v` | 5 | 18 | 134 | 13 |
| `tb/ch21/tb_axi_uvm_ral.sv` | 18 | 77 | 426 | 11 |
| `scripts/run_ch21.sh` | 3 | 8 | 34 | 6 |

## 직접 확인

원본 GitHub 고정 커밋 파일과 새 HTML을 직접 비교했다. 절 8개, pre 코드 박스 9개, SVG 1개 완전 일치. 원본 절 텍스트의 정규화 비교, 기존 교수용 CSS 동일, 네 파일의 모든 비공백 소스 행의 정확한 발췌 및 중복 없는 행 범위, 목차·버전 갱신을 검사했다. 신규 해설은 기존 8절 내부에만 추가했다. 원본 RTL/TB/스크립트는 수정하지 않았다.

## 검증 한계

이번 작업은 저장소 파일 기반 정적 비교이다. 이전 v25의 브라우저/공개 Pages 증거를 v26 신규 검사로 사용하지 않는다. 새 RTL/UVM_SIM·브라우저 6폭·공개 Pages HTTP는 NOT_RUN이며, 기존 원본의 실제 XSIM PASS 및 NO_PREDICT 부정 시험 증거는 보존한다. 원본 v60과의 정합성을 확인했으며 원본 외부 저장소는 수정하지 않았다.
