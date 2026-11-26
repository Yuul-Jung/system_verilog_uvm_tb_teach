# 제6부 교수용 해설서 종합 품질 검증

2026-11-26. 제21~24장 개별 제작·적대적 대조·실제 화면·장별 커밋·푸시·원격 재조회 후 별도 수행했다. 원본 원격 v60·`2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`, 중앙 규칙 원격 `028248a19afc66e9aafdab393fbe0de10a3930ca`가 기준과 같음을 다시 확인했다.

| 장 | 기술 검토 | 구분한 한계 |
|---|---|---|
| 21 | CONTROL 1+2 RW·29 RO, Frontdoor10거래, 독립 Monitor/Predictor·쓰기 직후 Mirror | 네 레지스터 모델, 부분 WSTRB·W1C/W1P 미시험 |
| 22 | 두 Agent·vsqr·두 분석 imp, 실제 commit 정렬, set 우선, AR 당시 IRQ | commit 시점 자체는 관찰값 의존, 상용 VIP 적합성 아님 |
| 23 | 네 signed41비트 점수·동점·편향·2L+2 지연·최대64·65거부 전제 | 스냅샷 계약, 현행2L+4 엔진·합성·DSP 검증과 구분 |
| 24 | 고정8+난수24·시드별 독립 분포, 정확한 오류 주입 검출, Blob SHA·보고서 | 한 조합 DUT의 회귀, 원격 RTL CI 실제 실행과 구분 |

[독립 수치 실행 결과](evidence/part06/math.json)는 네 분류·편향[-1,5,-7,8]·41비트 극값618475290623/-618473193472·길이1/2/64의4/6/130클록을 확인했다. 원본 Python 독립 모델 함수로 시드1/7/42의 계수[6,12,9,5]/[9,7,11,5]/[12,5,9,6]을 계산하여 총96표본·수락29와 대조했다. RTL 시뮬레이션은 새로 실행하지 않았다.

## 실제 종합 실행

```text
PYTHONPATH=<Playwright_설치경로> python3 scripts/check_part.py 6 --source <원본_체크아웃>
PASS PART 06: 4 chapters, 24 viewport measurements, 12 rejected mutations, online/offline navigation
```

종료0. [실제 검사 출력·해시](evidence/part06/quality.json)를 보존했다. 원본31절·코드 박스36개·SVG6개를 대조했다. 제24장은 원본 그대로7절이며 나머지는8절이다. 종합 검사에서 고정8절 가정을 제거하고 원본 실제 절 수와 비교한다. 코드·SVG·절 훼손12건 거절, 24개 화면 조합 flagged=0, 전체 코드 복사·표 펼침·SVG 경계/충돌·모바일 메뉴·절 이동을 확인했다. 온라인·course.json 차단 모두 같은 부4장·현재 장의 실제 절 수·이전/다음 파일을 확인했다.

장별 실제 화면과 모든 도식 이미지를 직접 검토했다. 제24장 긴 흐름도는 원본 내부 가로 스크롤을 유지하며 [오른쪽 끝](evidence/ch24_v01/svg2-right.png)·[전체 원문 렌더링](evidence/ch24_v01/svg2-full.png)을 추가 확인했다. [스크롤 측정](evidence/ch24_v01/diagram-scroll.json)에서792px 용기 안850px 도식의 오른쪽58px까지 도달함을 확인했다.

제22장의 닫는 구문233행, 제24장 Python else102행의 해설 범위 누락은 생성 단계에서 거절되어 수정 후 대조·반례·화면을 통과했다. 원본 파일은 수정하지 않았다. 제24장 원본 배너 v03 표시는 [CH24-01](SOURCE_ISSUES.md)에 별도 기록했고 교수용 기준 메타데이터는 원본 v04이다.

새 RTL/UVM_SIM·합성·보드·원격 RTL 회귀 CI는 NOT_RUN이다. 기존 원본 Icarus/XSIM 실측과 최신 CH23 v05 재실행 증거는 모두 유지했다. 교수용 공개 HTML 배포 상태는 최종 검증 기록에서 별도로 확인한다.
