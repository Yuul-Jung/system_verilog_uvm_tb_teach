# 제5부 교수용 해설서 종합 품질 검증

2026-11-26. 제17~20장의 개별 제작·반례·화면·커밋·푸시·원격 파일 확인 이후 별도 종합 검증했다. 원본 기준은 v60, `2d9e981a6059b5b23c9d21d4d76ec5d5fc1c0708`이다.

| 장 | 검토한 연결·수치·시점 | 구분한 한계 |
|---|---|---|
| 17 | test→env, vif·Factory 생성, 병렬 run·done·objection, duty4의8위상 | env 직접 판정이며 Driver·Monitor·Agent는 아직 없음 |
| 18 | object 요청과 component, start/finish_item·get_next/item_done,3거래×8=24 | Driver 내부 비교이며 독립 관찰 아님, 직접 대입은 constraint 우회 |
| 19 | ag 아래 sqr/drv/mon, 형제 sb, 분석 imp, cycles%8,31+3=34관찰 | period8·정해진 초기 리셋·세 요청만 모델링 |
| 20 | override 실제 타입·virtual/super/cast, 공유 cfg 동일성, 두 계획과 정상340ns 종료 | 공유 설정의 공통 오류 가능성, timeout 값 변화 미시험 |

모든 장에서 component 부모·자식과 Sequence/Item/Sample/config object를 구별했다. 별도 정적 top의 Interface·DUT를 UVM 계층의 하위 component로 설명하지 않았다. 각 그림의 화살표는 생성·요청·신호·분석·완료 중 해당 의미와 연결했다. 제20장 EARLY_DROP는 마지막266ns 표본까지17개와 남은7개를 계산하여 종료 미완료 검출을 설명했다. NO_VIF·INVALID_DUTY·Sample 반전·구성 누락의 부정 시험은 서로 다른 검증 층의 검사이며 DUT 전체 변이 검증으로 확대하지 않았다.

## 실제 종합 실행

```text
PYTHONPATH=<Playwright_설치경로> python3 scripts/check_part.py 5 --source <원본_체크아웃>
PASS PART 05: 4 chapters, 24 viewport measurements, 12 rejected mutations, online/offline navigation
```

종료0. [실행 결과와 해시](evidence/part05/quality.json)를 보존했다.32절·코드 박스36개·SVG4개를 원본과 대조했고 코드·SVG·절 훼손12건을 거절했다.24개 화면 조합 flagged=0, 모든 코드 복사·표 펼침·SVG 경계/충돌·모바일 메뉴·절 이동을 확인했다. 온라인 및 course.json 차단 상태에서 같은 부4장·현재8절·이전/다음 링크를 확인했다. 실제 장별 데스크톱·모바일·도식·해설 이미지를 직접 검토했다.

원본 XSIM 정상·부정 실측은 그대로 보존했다. 이번 제작의 새 UVM/RTL_SIM·합성·보드 실행은 NOT_RUN이다. 제5부 대조에서 추가 원본 결함은 확인하지 않았다. 기존 원본 표현 차이는 [별도 기록](SOURCE_ISSUES.md)에 유지한다.
