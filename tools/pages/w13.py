# 13주차 · 비즈니스 인텔리전스와 KPI 설계
SLUG = 'dsb_w13_bi_kpi'
FILE = 'week13_bi_kpi.html'
TITLE = '계기판을 설계하다 — 비즈니스 인텔리전스와 KPI 설계'
DESC = '비즈니스를 위한 데이터 과학 13주차 연구실 해설. ETL로 출처가 다른 매출을 맞추고, 재고회전율과 품절률의 균형, 광고 퍼널의 CPM·CPC·CPA·ROAS, 어트리뷰션, CLV : CAC를 직접 계산해 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 항공기 조종석 같은 계기판 앞에서 깔때기 모양 광고 퍼널과 창고 선반을 살피는 표지'
COVER_PROP = '🧭'
SEARCH_PH = '예: ETL, 재고회전율, CPC, ROAS, 어트리뷰션, CLV'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① ETL'), ('#lv2', '② 재고 KPI'), ('#lv3', '③ 광고 퍼널'), ('#lv4', '④ 어트리뷰션'), ('#lv5', '⑤ CLV : CAC'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week12_visualization.html"><small>← 이전 · 12주차</small>숫자의 얼굴</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="index.html"><small>다음 · 14주차</small>준비 중</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:method/etl', 'lab:metric/inventory-kpi', 'lab:metric/ad-funnel', 'lab:method/attribution', 'lab:metric/clv-cac']
KGPATH = ['method/etl', 'limitation/what-to-watch', 'metric/inventory-kpi', 'limitation/demand-side', 'metric/ad-funnel', 'limitation/multi-touch', 'method/attribution', 'limitation/single-purchase', 'metric/clv-cac']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '교안 3교시 쿠팡·배달의민족·당근마켓 사례의 인용 출처(뉴스룸·블로그) 날짜 재확인', '"CLV : CAC 3 : 1" 기준의 원 출처 확인(교안 인용)']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 13. 비즈니스 인텔리전스와 KPI 설계. 인공지능융합학과. — BI의 정의와 4단계, 전통적·현대적 아키텍처(ETL·웨어하우스·레이크·클라우드·셀프서비스), 유통 BI 4영역, 재고 KPI(회전율·품절률·과잉재고·정확도)와 계기판 비유, 지능형 발주, 광고 퍼널(노출·클릭·전환), CPC·CPM·CPA·CPS, 전환율·도달률·빈도, 어트리뷰션(퍼스트·라스트·선형), AOV·CLV·ROAS, CLV : CAC 3 : 1, SMART KPI, 대시보드 설계, 쿠팡·배달의민족·당근마켓 사례는 교안 본문을 옮김.',
 '[2] 한국기술교육대학교. "핀테크데이터분석". 국민평생직업능력개발 STEP 온라인평생교육원. — 교안 참고문헌.']
ILLUSTRATIVE = [
 '①칸 세 출처의 주문, ②칸 일별 수요(포아송, 시드 12)와 발주 규칙, ③칸 단가·CTR·전환율, ④칸 고객 8명의 여정, ⑤칸 이익·유지율·CAC, 대결의 캠페인 조건은 모두 설명용 예시·가정이며 실제 기업이나 업계 평균 값이 아닙니다.',
 '⑤칸 CLV는 매년 같은 이익, 일정한 유지율, 할인율 10%를 가정한 단순화 공식입니다.',
 '대결의 점수는 두 목표(도달, ROAS)를 같은 눈금에 놓으려고 각 목표에서 더 나은 캠페인을 100점으로 맞춘 상대 점수입니다.']

GL = {
 '비즈니스 인텔리전스': ['비즈니스 인텔리전스(BI)', 'BI', '기업 데이터를 수집·저장·분석·시각화해 경영 의사결정을 지원하는 시스템.', 'lab:concept/bi'],
 'ETL': ['ETL', 'BI', 'Extract(추출)·Transform(변환)·Load(적재). 원천 데이터를 정제해 웨어하우스에 넣는 과정.', 'lab:method/etl'],
 '데이터 웨어하우스': ['데이터 웨어하우스', 'BI', '분석용으로 통합·정리된 데이터 저장소.', None],
 '재고회전율': ['재고회전율', 'KPI', '판매량 ÷ 평균 재고. 높을수록 자본 효율이 좋지만 너무 높으면 품절 위험.', 'lab:metric/inventory-kpi'],
 '품절률': ['품절률', 'KPI', '품절이 난 기간·품목의 비율. 고객 만족과 직결.', None],
 'CPM': ['CPM', '광고', '노출 1,000회당 비용. 인지도 캠페인에 주로 쓴다.', 'lab:metric/ad-funnel'],
 'CPC': ['CPC', '광고', '클릭 1회당 비용. 성과 기반 과금.', None],
 'CPA': ['CPA', '광고', '고객 1명(전환 1건) 획득 비용.', None],
 'CTR': ['CTR(클릭률)', '광고', '클릭 ÷ 노출.', None],
 'ROAS': ['ROAS', '광고', '광고로 생긴 매출 ÷ 광고비.', None],
 '어트리뷰션': ['어트리뷰션', '광고', '여러 채널을 거친 전환의 공을 채널에 나눠 주는 규칙.', 'lab:method/attribution'],
 'CLV': ['CLV(고객생애가치)', 'KPI', '한 고객이 관계 기간 동안 창출하는 총 수익.', 'lab:metric/clv-cac'],
 'CAC': ['CAC(고객획득비용)', 'KPI', '고객 한 명을 데려오는 데 드는 비용.', None],
 'SMART': ['SMART 원칙', 'KPI', 'Specific·Measurable·Achievable·Relevant·Time-bound.', None],
}
CORE = ['비즈니스 인텔리전스', 'ETL', '데이터 웨어하우스', '재고회전율', '품절률', 'CPM', 'CPC', 'CPA', 'CTR', 'ROAS', '어트리뷰션', 'CLV', 'CAC', 'SMART']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '비즈니스 인텔리전스(BI)의 주요 역할로 가장 적절한 것은? (교안 연습문제 1)', 'o': ['단순한 데이터 저장', '경영진의 데이터 기반 의사결정 지원', '시스템 보안 강화', '직원 업무 관리'], 'a': 1, 'why': '단순 저장은 데이터베이스, 보안·업무 관리는 다른 시스템의 역할입니다.', 'hint': '왜 섹션 1번.', 'assess': 'lab:concept/bi'},
  {'id': 'q2', 'q': '온라인몰이 금액을 천 원 단위로 저장했다. ETL에서 할 일은?', 'o': ['그대로 더한다', '단위를 원으로 통일해 변환한다', '온라인몰을 빼고 집계한다'], 'a': 1, 'why': 'Transform 단계에서 단위·형식을 맞춘 뒤 적재합니다.', 'hint': '①칸 첫 번째 체크.', 'assess': 'lab:method/etl'}],
 'lv2': [
  {'id': 'q3', 'q': '연간 판매 7,300개, 평균 재고 365개면 재고회전율은?', 'o': ['10회', '20회', '0.05회'], 'a': 1, 'why': '7,300 ÷ 365 = 20회.', 'hint': '판매량 ÷ 평균 재고', 'calc': True, 'assess': 'lab:metric/inventory-kpi'},
  {'id': 'q4', 'q': '품절률을 0으로 만들려고 재고를 크게 늘리면?', 'o': ['회전율이 오른다', '회전율이 떨어지고 과잉재고 비용이 생긴다', '아무 변화 없다'], 'a': 1, 'why': '지표끼리 줄다리기합니다. 균형점을 찾아야 합니다(교안).', 'hint': '②칸 오른쪽 곡선.', 'assess': 'lab:metric/inventory-kpi'}],
 'lv3': [
  {'id': 'q5', 'q': '광고비 100만 원, 클릭 2,000회면 CPC는?', 'o': ['50원', '500원', '2,000원'], 'a': 1, 'why': '1,000,000 ÷ 2,000 = 500원.', 'hint': '광고비 ÷ 클릭', 'calc': True, 'assess': 'lab:metric/ad-funnel'},
  {'id': 'q6', 'q': '광고 KPI 계층에서 가장 상위(최종) 단계는? (교안 연습문제 2)', 'o': ['노출', '클릭', '전환', '구매'], 'a': 2, 'why': '퍼널은 노출 → 클릭 → 전환. 전환이 목표 행동을 완료한 최종 단계입니다(구매는 결과·목표).', 'hint': '큰 그림 오른쪽.', 'assess': 'lab:metric/ad-funnel'}],
 'lv4': [
  {'id': 'q7', 'q': 'SNS → 이메일 → 검색 → 구매(10만 원). 라스트 클릭에서 검색의 몫은?', 'o': ['0원', '3.3만 원', '10만 원'], 'a': 2, 'why': '마지막 접점이 전부 가져갑니다. 선형이면 3.3만 원씩.', 'hint': '④칸 규칙 버튼.', 'calc': True, 'assess': 'lab:method/attribution'},
  {'id': 'q8', 'q': '어트리뷰션 규칙을 KPI 정의서에 적어 두는 이유는?', 'o': ['규칙에 따라 채널별 성과와 예산 배분 결론이 달라지므로', '법으로 정해져 있어서', '계산이 빨라서'], 'a': 0, 'why': '같은 매출이 규칙마다 다른 채널의 공이 됩니다.', 'hint': '④칸 풀이 3.', 'assess': 'lab:method/attribution'}],
 'lv5': [
  {'id': 'q9', 'q': 'CLV 60만 원, CAC 15만 원이면 CLV : CAC와 교안 기준 평가는?', 'o': ['4 : 1, 건강함', '0.25 : 1, 손해', '1 : 1, 본전'], 'a': 0, 'why': '60 ÷ 15 = 4, 3 : 1 이상이면 건강한 모델(교안).', 'hint': '⑤칸 기준.', 'calc': True, 'assess': 'lab:metric/clv-cac'},
  {'id': 'q10', 'q': '"매출 증가"보다 "모바일 앱 신규 고객 CPA 30% 감소(이번 분기)"가 나은 KPI인 이유는?', 'o': ['숫자가 커서', '구체적·측정 가능·기한이 있어서(SMART)', '모바일이 중요해서'], 'a': 1, 'why': 'SMART 원칙의 구체성·측정가능성·시한성을 갖췄습니다(교안 예).', 'hint': '교안 2교시 5.', 'assess': 'lab:metric/clv-cac'},
  {'id': 'q11', 'q': '쿠팡의 로켓배송에서 사용되는 기술과 가장 거리가 먼 것은? (교안 연습문제 3)', 'o': ['머신러닝 예측', '랜덤 스토우', '수동 재고 관리', '실시간 대시보드'], 'a': 2, 'why': '교안 해설: 로켓배송은 데이터 기반 자동화로 운영되어 수동 재고 관리는 쓰지 않습니다.', 'hint': '현장에 옮기면.', 'assess': 'lab:concept/bi'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/bi', 'Concept', '비즈니스 인텔리전스(BI)', 'business intelligence', '#why', level=1, family='systems'),
 N('task/decision-support', 'Task', '데이터 기반 경영 의사결정', 'data-driven decision support', '#why', level=1, family='basics'),
 N('dataset/three-sources', 'Dataset', '세 출처 주간 주문(예시)', 'three-source weekly orders (synthetic)', '#lv1', level=1, family='data'),
 N('method/etl', 'Method', 'ETL(추출·변환·적재)', 'ETL', '#lv1', level=1, family='systems'),
 N('metric/inventory-kpi', 'Metric', '재고 KPI(회전율·품절률)', 'inventory KPIs', '#lv2', level=1, family='evaluation'),
 N('metric/ad-funnel', 'Metric', '광고 퍼널 지표(CPM·CPC·CPA·ROAS)', 'ad funnel metrics', '#lv3', level=1, family='evaluation'),
 N('method/attribution', 'Method', '어트리뷰션(퍼스트·라스트·선형)', 'attribution models', '#lv4', level=2, family='evaluation'),
 N('metric/clv-cac', 'Metric', 'CLV : CAC', 'CLV to CAC ratio', '#lv5', level=2, family='evaluation'),
 N('concept/smart-kpi', 'Concept', 'SMART KPI', 'SMART KPIs', '#lv5', level=1, family='evaluation'),
 N('limitation/what-to-watch', 'Limitation', '무엇을 볼지 아직 없다', 'nothing chosen to watch', '#lv1'),
 N('limitation/demand-side', 'Limitation', '수요를 만드는 쪽은 별도', 'demand creation not covered', '#lv2'),
 N('limitation/multi-touch', 'Limitation', '여러 채널을 거친 구매', 'multi-touch journeys', '#lv3'),
 N('limitation/single-purchase', 'Limitation', '한 번의 구매만 셌다', 'single purchase only', '#lv4'),
 N('claim/clv-cac-3', 'Claim', 'CLV : CAC 3 : 1 이상이면 건강한 비즈니스 모델', 'CLV:CAC ≥ 3 is healthy', '#lv5', source=[{'cite': '교안 13주차', 'loc': '2교시 4'}]),
 N('claim/ctr-cvr-tradeoff', 'Claim', 'CTR을 높이려 자극적 광고를 쓰면 전환율이 감소할 수 있다', 'clickbait raises CTR but may lower CVR', '#lv3', source=[{'cite': '교안 13주차', 'loc': '2교시 1'}]),
 N('question/core', 'Question', '대시보드에 띄울 숫자 하나를 무엇으로 고를까?', 'Which number should the dashboard show?', '#hero'),
 N('question/duel', 'Question', '같은 광고비, CPM이냐 CPC냐', 'CPM or CPC for the same budget?', '#duel'),
 N('analogy/cockpit', 'Analogy', '조종석·자동차 계기판 ↔ KPI 대시보드', 'cockpit gauges ↔ KPI dashboard', '#lv2', anchorType='D'),
 N('analogy/relay', 'Analogy', '릴레이 경기의 공 나누기 ↔ 어트리뷰션', 'relay credit ↔ attribution', '#lv4', anchorType='D'),
 N('analogy/cooking', 'Analogy', '재료 준비·손질·조리·플레이팅 ↔ BI 4단계', 'cooking steps ↔ BI stages', '#lv1', anchorType='D'),
 N('sim/w13-etl', 'Simulation', 'ETL 체크박스', 'ETL toggles', '#lv1'),
 N('sim/w13-inv', 'Simulation', '발주점 1년 시뮬레이션', 'reorder point simulation', '#lv2'),
 N('sim/w13-funnel', 'Simulation', '광고 퍼널 계산기', 'ad funnel calculator', '#lv3'),
 N('sim/w13-attr', 'Simulation', '어트리뷰션 규칙 바꾸기', 'switch attribution rules', '#lv4'),
 N('sim/w13-clv', 'Simulation', 'CLV 누적 곡선', 'CLV curve', '#lv5'),
 N('work/ahn-dsb-w13', 'Work', '안상선, 비즈니스를위한데이터과학 교안 13주차', 'Ahn, DSB lecture notes week 13', '#footer'),
 N('work/step-fintech', 'Work', '한국기술교육대학교, 핀테크데이터분석(STEP)', 'KoreaTech STEP Fintech Data Analysis', '#footer'),
]

EDGES = [
 ('lab:concept/bi', 'lab:solves', 'lab:task/decision-support', '#why'),
 ('lab:task/decision-support', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:method/etl', 'lab:partOf', 'lab:concept/bi', '#lv1'),
 ('lab:method/etl', 'lab:evaluatedOn', 'lab:dataset/three-sources', '#lv1'),
 ('lab:method/etl', 'lab:hasLimitation', 'lab:limitation/what-to-watch', '#lv1'),
 ('lab:limitation/what-to-watch', 'lab:addressedBy', 'lab:metric/inventory-kpi', '#lv2'),
 ('lab:metric/inventory-kpi', 'lab:partOf', 'lab:concept/bi', '#lv2'),
 ('lab:metric/inventory-kpi', 'lab:hasLimitation', 'lab:limitation/demand-side', '#lv2'),
 ('lab:limitation/demand-side', 'lab:addressedBy', 'lab:metric/ad-funnel', '#lv3'),
 ('lab:metric/ad-funnel', 'lab:hasLimitation', 'lab:limitation/multi-touch', '#lv3'),
 ('lab:limitation/multi-touch', 'lab:addressedBy', 'lab:method/attribution', '#lv4'),
 ('lab:method/attribution', 'lab:hasLimitation', 'lab:limitation/single-purchase', '#lv4'),
 ('lab:limitation/single-purchase', 'lab:addressedBy', 'lab:metric/clv-cac', '#lv5'),
 ('lab:concept/smart-kpi', 'lab:prerequisiteOf', 'lab:metric/clv-cac', '#lv5'),
 ('lab:metric/ad-funnel', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:concept/smart-kpi', 'lab:partOf', 'lab:concept/bi', '#lv5'),
 ('lab:analogy/cockpit', 'lab:analogyOf', 'lab:metric/inventory-kpi', '#lv2'),
 ('lab:analogy/relay', 'lab:analogyOf', 'lab:method/attribution', '#lv4'),
 ('lab:analogy/cooking', 'lab:analogyOf', 'lab:concept/bi', '#lv1'),
 ('lab:method/etl', 'lab:demonstratedBy', 'lab:sim/w13-etl', '#lv1'),
 ('lab:metric/inventory-kpi', 'lab:demonstratedBy', 'lab:sim/w13-inv', '#lv2'),
 ('lab:metric/ad-funnel', 'lab:demonstratedBy', 'lab:sim/w13-funnel', '#lv3'),
 ('lab:method/attribution', 'lab:demonstratedBy', 'lab:sim/w13-attr', '#lv4'),
 ('lab:metric/clv-cac', 'lab:demonstratedBy', 'lab:sim/w13-clv', '#lv5'),
 ('lab:claim/clv-cac-3', 'lab:supports', 'lab:metric/clv-cac', '#lv5'), ('lab:claim/clv-cac-3', 'lab:assertedIn', 'lab:work/ahn-dsb-w13', '#lv5'),
 ('lab:claim/ctr-cvr-tradeoff', 'lab:supports', 'lab:metric/ad-funnel', '#lv3'), ('lab:claim/ctr-cvr-tradeoff', 'lab:assertedIn', 'lab:work/ahn-dsb-w13', '#lv3'),
 ('lab:concept/bi', 'lab:relatedTo', 'lab:work/step-fintech', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w13', 'report', '비즈니스를위한데이터과학 강의 교안: 13. 비즈니스 인텔리전스와 KPI 설계', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/clv-cac-3', 'lab:claim/ctr-cvr-tradeoff', 'lab:concept/bi', 'lab:method/etl', 'lab:metric/ad-funnel'], 'lab:work/ahn-dsb-w13',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/clv-cac-3', 'loc': '2교시 4. 객단가와 고객생애가치'}, {'claim': 'lab:claim/ctr-cvr-tradeoff', 'loc': '2교시 1. AD-TECH KPI의 계층적 구조'}]),
 R('step_fintech', 'webpage', '핀테크데이터분석', [{'literal': '한국기술교육대학교'}], None, 'background', ['lab:concept/bi'], 'lab:work/step-fintech',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '교안 인용 서지 그대로', '', publisher='STEP 온라인평생교육원', URL='https://www.step.or.kr'),
]
