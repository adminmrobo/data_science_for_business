# 1주차 · 비즈니스 데이터 과학의 이해
SLUG = 'dsb_w01_business_data_science'
FILE = 'week01_business_data_science.html'
TITLE = '데이터는 많은데, 결정은 왜 틀릴까 — 비즈니스 데이터 과학의 이해'
DESC = '비즈니스를 위한 데이터 과학 1주차 연구실 해설. DIKW 계단, 생존자 편향, 상관과 인과, A/B 테스트를 장난감 데이터로 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '밤의 연구실에서 네 캐릭터가 데이터·정보·지식·지혜 네 계단과 돌아온 비행기 모형을 둘러싼 표지'
COVER_PROP = '📊'
SEARCH_PH = '예: 생존자, 교란, A/B, 표준오차'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① DIKW'), ('#lv2', '② 생존자 편향'), ('#lv3', '③ 상관·인과'), ('#lv4', '④ A/B 테스트'), ('#duel', '대결'), ('#cases', '사례 지도'), ('#sum', '정리')]
PREVNEXT = '<a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week02_data_collection.html"><small>다음 · 2주차</small>데이터는 어디서 오는가 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'doc_think', 'robo_meh', 'robo_calc', 'robo_blush', 'asst_shock']
ABOUT = ['lab:framework/dikw', 'lab:concept/survivorship-bias', 'lab:concept/correlation-vs-causation', 'lab:method/ab-test', 'lab:framework/decision-process']
KGPATH = ['framework/dikw', 'limitation/filtered-data', 'concept/survivorship-bias', 'limitation/cause-unknown', 'method/stratification', 'limitation/hidden-variables', 'method/ab-test', 'limitation/small-sample']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '오바마 캠프 수치 [3]는 교안이 인용한 블로그 글의 수치 — 1차 출처 확인 필요']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 01. 비즈니스 데이터 과학의 이해. 인공지능융합학과. — 팔만대장경 99MB, 데이터 총량 약 2,500배, 3V·5V, 의사결정 5단계, 기업 사례, 라이터–폐암 사례는 교안 본문과 교안이 인용한 자료(동아일보 2022.08.24, IDC 2018 등)를 그대로 옮김. 교안 연도 표기 확인 필요.',
 '[2] 조던 엘렌버그 (2016). 『틀리지 않는 법: 수학적 사고의 힘』. 김명남 옮김. 열린책들. — 교안이 생존자 편향(항공기) 사례의 출처로 인용.',
 '[3] John Davier (2023.02.08). A/B Testing Got Obama $60 Million. You Can Do It Too. mailmunch 블로그. <a href="https://www.mailmunch.com/blog/ab-testing-got-obama-60-million" target="_blank" rel="noopener">링크</a> — 교안이 인용. 기부율 10% 이상 증가는 이 글의 수치이며 1차 출처는 확인하지 않음.',
 '[4] 포스터 프로보스트, 톰 포셋 (2014). 『비즈니스를 위한 데이터 과학』. 강권학 옮김. 한빛미디어. — 교안이 데이터 과학의 정의에 인용.']
ILLUSTRATIVE = [
 '①칸 편의점 우산 판매 30일(시드 21), 비 올 확률과 안전재고 20%는 설명을 위해 정한 값입니다.',
 '②칸 비행기 400대, 부위별 면적(엔진 15%, 조종석 10%, 동체 45%, 날개 30%)과 부위별 귀환 확률은 설명용 값입니다. 실제 전쟁 기록이 아닙니다.',
 '③칸 가상 인구 2,000명(시드 283, 흡연 30%, 라이터 소지 흡연자 85%·비흡연자 10%, 폐암 위험 흡연자 15%·비흡연자 2%)은 실제 의학 통계가 아닙니다.',
 '④칸과 대결의 반응률(A 5.0%, B 6.0%)과 1,000번 반복 실험(시드 11)은 설명용 모형입니다.']

GL = {
 '데이터 과학': ['데이터 과학', '개념', '데이터를 수집·분석·해석해 유의미한 인사이트를 끌어내는 학문. 비즈니스에서는 현장 문제 해결이 목적이라 실용적인 성격이 강하다.', 'lab:concept/business-data-science'],
 '빅데이터': ['빅데이터', '개념', '기존 데이터베이스로 다루기 어려운 규모·속도·다양성을 가진 데이터. 3V(Volume·Velocity·Variety)에 가치·정확성을 더해 5V로도 본다.', 'lab:concept/big-data-5v'],
 '데이터 기반 의사결정': ['데이터 기반 의사결정', '방법', '주관적 판단 대신 데이터 분석 결과로 결정하는 것. 객관성·예측 가능성·효율성·확장성이 장점이다.', 'lab:framework/decision-process'],
 '귀납적': ['귀납적 접근', '방법', '데이터를 탐색해 패턴을 찾고 가설을 끌어내는 방식. 데이터 과학의 특징.', 'lab:concept/inductive'],
 '연역적': ['연역적 접근', '방법', '가설을 먼저 세우고 데이터로 검증하는 방식. 전통적 분석의 특징.', 'lab:concept/deductive'],
 '인사이트': ['인사이트', '개념', '데이터 분석에서 얻은, 행동으로 옮길 수 있는 깨달음.', None],
 '생존자 편향': ['생존자 편향', '함정', '살아남은(관측된) 사례만 분석해 잘못된 결론을 내는 것. 걸러진 쪽의 정보가 빠진다.', 'lab:concept/survivorship-bias'],
 '확증 편향': ['확증 편향', '함정', '자기 주장을 뒷받침하는 데이터만 선호하는 것.', 'lab:concept/confirmation-bias'],
 '상관': ['상관(상관관계)', '개념', '두 변수가 함께 움직이는 정도. 원인-결과를 보장하지 않는다.', 'lab:concept/correlation-vs-causation'],
 '인과': ['인과(인과관계)', '개념', '한 변수가 다른 변수의 원인이 되는 관계. 확인하려면 무작위 실험 같은 설계가 필요하다.', None],
 '교란 변수': ['교란 변수', '개념', '두 변수 모두에 영향을 줘서, 둘 사이에 가짜 상관을 만드는 제3의 변수. 예: 라이터와 폐암 뒤의 흡연.', 'lab:concept/confounder'],
 'A/B 테스트': ['A/B 테스트', '방법', '두 버전(A, B)을 무작위로 나눈 집단에 동시에 보여 주고 반응을 비교하는 실험.', 'lab:method/ab-test'],
 '무작위 할당': ['무작위 할당', '방법', '실험 대상을 제비뽑기처럼 집단에 나누는 것. 숨은 변수까지 두 집단에 고르게 퍼뜨린다.', 'lab:concept/random-assignment'],
 '표준오차': ['표준오차', '통계', '같은 실험을 반복할 때 추정값이 흔들리는 정도. 표본이 4배가 되면 절반이 된다.', 'lab:concept/standard-error'],
 '표본': ['표본', '통계', '전체(모집단) 가운데 실제로 관측한 일부. 표본이 작으면 우연한 차이가 크게 보인다.', 'lab:concept/sample-size'],
 'IoT': ['IoT (사물인터넷)', '용어', '센서가 달린 사물이 네트워크로 데이터를 주고받는 기술.', None],
 '데이터마이닝': ['데이터마이닝', '방법', '대량의 데이터에서 숨은 패턴·연관성을 찾는 기법. 예: 함께 팔리는 상품 찾기.', 'lab:concept/data-mining'],
 '동적 요금': ['동적 요금(동적 가격)', '방법', '실시간 수요와 공급에 따라 가격을 바꾸는 방식.', 'lab:concept/dynamic-pricing'],
 '스토리텔링': ['데이터 스토리텔링', '방법', '데이터·시각화·이야기를 엮어 문제 → 분석 → 해결 → 결론으로 전달해 행동을 이끄는 것.', 'lab:concept/data-storytelling'],
 '파일럿 테스트': ['파일럿 테스트', '방법', '전면 적용 전에 작은 규모로 효과를 검증하는 시험.', None],
 '안전재고': ['안전재고', '경영', '수요 변동에 대비해 기대 수요보다 더 갖춰 두는 재고.', None],
 '기대 판매': ['기대값(기대 판매량)', '통계', '일어날 수 있는 경우의 값에 확률을 곱해 더한 평균적인 값.', None],
}
CORE = ['데이터 과학', '빅데이터', '귀납적', '연역적', '생존자 편향', '확증 편향', '교란 변수', 'A/B 테스트', '무작위 할당', '표준오차', '표본', '데이터마이닝']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '숫자 30개를 날짜별 막대그래프로 그린 것은 DIKW의 어느 계단인가?', 'o': ['데이터', '정보', '지혜'], 'a': 1, 'why': '원시 숫자에 형태와 의미를 붙인 표·그래프가 정보입니다.', 'hint': '교안의 예: 숫자(데이터) → 차트(?)', 'assess': 'lab:concept/information'},
  {'id': 'q2', 'q': '비 올 확률 50%, 비 온 날 평균 18개, 맑은 날 평균 3개라면 기대 판매량은?', 'o': ['10.5개', '18개', '21개'], 'a': 0, 'why': '0.5 × 18 + 0.5 × 3 = 10.5개입니다.', 'hint': '확률 × 값을 두 경우에 대해 더합니다.', 'calc': True, 'assess': 'lab:concept/wisdom'}],
 'lv2': [
  {'id': 'q3', 'q': '돌아온 비행기에서 엔진 자국이 가장 적었다. 장갑을 어디에 더해야 하나?', 'o': ['자국이 많은 동체', '자국이 적은 엔진', '어디든 같다'], 'a': 1, 'why': '엔진에 맞은 비행기는 돌아오지 못해 기록에서 빠졌습니다. 자국이 적은 곳이 맞으면 치명적인 곳입니다.', 'hint': '돌아오지 못한 비행기도 보기를 눌러 보세요.', 'assess': 'lab:concept/survivorship-bias'},
  {'id': 'q4', 'q': '다음 중 생존자 편향과 같은 구조인 것은?', 'o': ['남아 있는 고객의 만족도 설문만으로 서비스를 평가한다', '모든 고객에게 무작위로 설문을 보낸다', '해지 고객과 유지 고객을 함께 비교한다'], 'a': 0, 'why': '불만으로 떠난 고객은 설문에 없으므로 만족도가 높게 나옵니다.', 'hint': '누가 걸러졌는지 보세요.', 'assess': 'lab:concept/survivorship-bias'}],
 'lv3': [
  {'id': 'q5', 'q': '가상 인구에서 라이터 소지자의 폐암 비율이 높게 나온 이유는?', 'o': ['라이터가 폐암을 일으켜서', '흡연이 라이터 소지와 폐암 모두에 영향을 줘서', '표본이 작아서'], 'a': 1, 'why': '흡연이 교란 변수입니다. 흡연 여부로 나누면 차이가 거의 사라집니다.', 'hint': '흡연 여부로 나눠 보기를 누른 뒤의 막대를 보세요.', 'assess': 'lab:concept/confounder'},
  {'id': 'q6', 'q': '"라이터가 문제다"라고 이미 믿는 사람이 전체 표만 보고 확신을 굳히는 것은?', 'o': ['확증 편향', '생존자 편향', '무작위 할당'], 'a': 0, 'why': '자기 주장을 뒷받침하는 데이터만 받아들이는 것이 확증 편향입니다.', 'hint': '교안의 함정 세 가지 중 하나입니다.', 'assess': 'lab:concept/confirmation-bias'}],
 'lv4': [
  {'id': 'q7', 'q': 'A/B 테스트에서 고객을 무작위로 나누는 가장 큰 이유는?', 'o': ['계산이 쉬워서', '숨은 변수까지 두 집단에 고르게 퍼뜨려 차이의 원인을 A·B로 볼 수 있게 하려고', '표본을 줄이려고'], 'a': 1, 'why': '무작위 할당은 ③칸의 교란 변수 문제를 설계로 막습니다.', 'hint': '③칸의 한계를 떠올려 보세요.', 'assess': 'lab:concept/random-assignment'},
  {'id': 'q8', 'q': '집단당 표본을 100명에서 400명으로 늘리면 차이의 표준오차는 대략 어떻게 되나?', 'o': ['4분의 1', '절반', '그대로'], 'a': 1, 'why': '표준오차는 1/√n에 비례합니다. n이 4배면 1/2입니다.', 'hint': '√4 = 2', 'calc': True, 'assess': 'lab:concept/standard-error'},
  {'id': 'q9', 'q': '집단당 100명 실험에서 B가 이겼다. 가장 알맞은 다음 행동은?', 'o': ['바로 전면 적용한다', '표본을 미리 정해 더 모으거나 파일럿으로 확인한다', 'A로 되돌린다'], 'a': 1, 'why': '100명이면 정답을 고를 확률이 60% 안팎이라 우연일 수 있습니다.', 'hint': '④칸에서 100명일 때 정답률을 보세요.', 'assess': 'lab:limitation/small-sample'}],
 'cases': [
  {'id': 'q10', 'q': '교안이 구글 독감 트렌드 사례의 한계로 든 것은?', 'o': ['데이터가 너무 적다', '검색 데이터의 신뢰성 문제와 과적합 위험', '실시간 처리가 불가능하다'], 'a': 1, 'why': '검색량은 독감 말고도 뉴스·관심 때문에 늘 수 있어 신뢰성 문제가 있고, 과거에 맞춘 모형이 과적합될 수 있습니다.', 'hint': '사례 카드의 조심할 점을 보세요.', 'assess': 'lab:concept/data-mining'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/business-data-science', 'Concept', '비즈니스 데이터 과학', 'business data science', '#hero', level=1, family='basics', evidence=['F05']),
 N('framework/dikw', 'Framework', 'DIKW 계단', 'DIKW hierarchy', '#lv1', '데이터 → 정보 → 지식 → 지혜로 가공 수준과 가치가 올라가는 단계.', level=1, family='basics'),
 N('concept/data', 'Concept', '데이터', 'data', '#lv1', '원시 자료. 숫자, 문자, 이미지 등.', level=1, family='basics'),
 N('concept/information', 'Concept', '정보', 'information', '#lv1', '데이터를 가공해 의미를 붙인 것. 표, 그래프.', level=1, family='basics'),
 N('concept/knowledge', 'Concept', '지식', 'knowledge', '#lv1', '정보를 분석해 패턴이나 인사이트를 끌어낸 것. 트렌드, 원인 분석.', level=1, family='basics'),
 N('concept/wisdom', 'Concept', '지혜', 'wisdom', '#lv1', '지식을 바탕으로 실천적 결정을 내리는 것. 전략 수립, 실행.', level=1, family='basics'),
 N('concept/big-data-5v', 'Concept', '빅데이터 3V·5V', 'big data 3V/5V', '#big', level=1, family='basics'),
 N('framework/decision-process', 'Framework', '데이터 기반 의사결정 5단계', 'data-driven decision process', '#big', '문제 정의 → 데이터 수집 → 분석 → 해석 → 실행, 그리고 피드백 루프.', level=1, family='basics'),
 N('framework/smart', 'Framework', 'SMART 원칙', 'SMART criteria', '#big', '목표를 Specific·Measurable·Achievable·Relevant·Time-bound로 정하는 틀.', level=1, family='basics', domain=['biz']),
 N('concept/deductive', 'Concept', '전통적 분석(연역)', 'deductive analysis', '#why', level=1, family='basics'),
 N('concept/inductive', 'Concept', '데이터 과학(귀납)', 'inductive data science', '#why', level=1, family='basics'),
 N('concept/survivorship-bias', 'Concept', '생존자 편향', 'survivorship bias', '#lv2', level=2, family='evaluation', domain=['stats', 'biz', 'ai']),
 N('concept/confirmation-bias', 'Concept', '확증 편향', 'confirmation bias', '#lv3', level=2, family='evaluation'),
 N('concept/correlation-vs-causation', 'Concept', '상관과 인과', 'correlation vs causation', '#lv3', '두 변수가 함께 움직이는 것(상관)은 원인-결과(인과)를 보장하지 않는다.', level=2, family='evaluation', domain=['stats', 'ai', 'biz']),
 N('concept/confounder', 'Concept', '교란 변수', 'confounding variable', '#lv3', level=2, family='evaluation', domain=['stats']),
 N('method/stratification', 'Method', '층별로 나눠 비교하기', 'stratified comparison', '#lv3', '교란 변수의 값을 고정한 집단 안에서 비교하는 방법.', level=2, family='evaluation', domain=['stats']),
 N('method/ab-test', 'Method', 'A/B 테스트', 'A/B testing', '#lv4', level=2, family='evaluation', domain=['stats', 'biz', 'ai']),
 N('concept/random-assignment', 'Concept', '무작위 할당', 'random assignment', '#lv4', level=2, family='evaluation', domain=['stats']),
 N('concept/sample-size', 'Concept', '표본 크기', 'sample size', '#lv4', level=2, family='evaluation', domain=['stats']),
 N('concept/standard-error', 'Concept', '표준오차', 'standard error', '#lv4', level=3, family='evaluation', domain=['stats']),
 N('concept/data-storytelling', 'Concept', '데이터 시각화와 스토리텔링', 'data visualization and storytelling', '#sum', level=1, family='basics'),
 N('concept/data-mining', 'Method', '데이터마이닝', 'data mining', '#cases', level=1, family='basics'),
 N('concept/recommender', 'Method', '개인화 추천 시스템', 'recommender system', '#cases', '시청·청취·구매 이력으로 비슷한 취향을 찾아 추천하는 시스템.', level=2, family='basics'),
 N('concept/dynamic-pricing', 'Method', '동적 요금', 'dynamic pricing', '#cases', level=2, family='basics', domain=['biz']),
 N('concept/privacy', 'Concept', '프라이버시·윤리 문제', 'privacy and ethics', '#cases', '데이터 기반 서비스가 개인정보 보호·공정성과 부딪치는 문제.', level=1, family='ethics'),
 N('task/order-decision', 'Task', '발주량 정하기', 'order quantity decision', '#lv1', level=1, family='basics', domain=['biz']),
 N('metric/response-rate', 'Metric', '반응률', 'response rate', '#lv4', '메일을 받은 사람 가운데 반응(클릭·전환)한 비율.', level=1, family='evaluation'),
 N('metric/correct-choice', 'Metric', '정답을 고른 비율', 'correct decision rate', '#duel', '반복 실험에서 더 좋은 안(B)을 고른 실험의 비율.', level=2, family='evaluation'),
 N('limitation/filtered-data', 'Limitation', '걸러진 데이터면 틀린 지혜', 'filtered data leads to wrong decisions', '#lv1', level=1),
 N('limitation/cause-unknown', 'Limitation', '함께 움직이는 것의 원인은 모름', 'cause unknown', '#lv2', level=2),
 N('limitation/hidden-variables', 'Limitation', '숨은 변수를 다 알 수 없음', 'unknown hidden variables', '#lv3', level=2),
 N('limitation/small-sample', 'Limitation', '작은 표본은 우연에 휘둘림', 'small samples are noisy', '#lv4', '표본이 작으면 우연한 차이가 진짜 차이보다 크게 보여 틀린 쪽을 고를 수 있다.', level=2),
 N('claim/tripitaka-99mb', 'Claim', '팔만대장경 5,200만 자는 약 99MB', 'Tripitaka Koreana ≈ 99MB', '#why', evidence=['F01'], source=[{'cite': '교안 1주차', 'loc': '1교시 2'}]),
 N('claim/data-growth-2500x', 'Claim', '데이터 총량 약 20EB → 약 50,000EB(약 2,500배)', 'global data ~2,500x', '#hero', evidence=['F02'], source=[{'cite': '교안 1주차', 'loc': '1교시 2'}], confidence='mid'),
 N('claim/obama-ab', 'Claim', '오바마 캠프 이메일 제목 테스트로 기부율 10% 이상 증가', 'Obama campaign email A/B test', '#lv4', evidence=['F09'], source=[{'cite': 'Davier 2023 (교안 인용)', 'loc': ''}], confidence='mid'),
 N('claim/planes-story', 'Claim', '돌아온 비행기만 보고 장갑 위치를 정하면 틀린다', 'returned-planes survivorship story', '#lv2', source=[{'cite': 'Ellenberg 2016 (교안 인용)', 'loc': ''}]),
 N('question/core', 'Question', '데이터를 많이 모으면 좋은 결정이 저절로 나올까?', 'Does more data automatically mean better decisions?', '#hero'),
 N('question/duel', 'Question', '첫날 결과로 바로 결정해도 될까?', 'Decide on day-one results?', '#duel'),
 N('question/hidden', 'Question', '숨은 교란 변수를 모를 때 원인을 어떻게 확인할까?', 'How to establish causation with unknown confounders?', '#lv3'),
 N('analogy/umbrella', 'Analogy', '편의점 우산 발주 ↔ DIKW', 'umbrella orders ↔ DIKW', '#lv1', anchorType='D'),
 N('analogy/planes-customers', 'Analogy', '돌아온 비행기 ↔ 남아 있는 고객', 'returned planes ↔ retained customers', '#lv2', anchorType='B'),
 N('sim/w01-dikw', 'Simulation', '우산 판매 계단 실험', 'DIKW umbrella simulation', '#lv1'),
 N('sim/w01-planes', 'Simulation', '비행기 400대 실험', 'survivorship planes simulation', '#lv2'),
 N('sim/w01-lighter', 'Simulation', '가상 인구 2,000명 실험', 'confounder simulation', '#lv3'),
 N('sim/w01-ab', 'Simulation', 'A/B 테스트 1,000번 반복', 'A/B repeated experiments', '#lv4'),
 N('work/ahn-dsb-w01', 'Work', '안상선, 비즈니스를위한데이터과학 교안 1주차', 'Ahn, DSB lecture notes week 1', '#footer'),
 N('work/ellenberg2016', 'Work', '엘렌버그(2016) 틀리지 않는 법', 'Ellenberg (2016) How Not to Be Wrong (Korean ed.)', '#footer'),
 N('work/davier2023', 'Work', 'Davier(2023) A/B Testing Got Obama $60 Million', 'Davier (2023)', '#footer'),
 N('work/provost2014', 'Work', '프로보스트·포셋(2014) 비즈니스를 위한 데이터 과학', 'Provost & Fawcett (2014)', '#footer'),
]

EDGES = [
 ('lab:concept/data', 'lab:partOf', 'lab:framework/dikw', '#lv1'), ('lab:concept/information', 'lab:partOf', 'lab:framework/dikw', '#lv1'),
 ('lab:concept/knowledge', 'lab:partOf', 'lab:framework/dikw', '#lv1'), ('lab:concept/wisdom', 'lab:partOf', 'lab:framework/dikw', '#lv1'),
 ('lab:concept/data', 'lab:prerequisiteOf', 'lab:concept/information', '#lv1'), ('lab:concept/information', 'lab:prerequisiteOf', 'lab:concept/knowledge', '#lv1'),
 ('lab:concept/knowledge', 'lab:prerequisiteOf', 'lab:concept/wisdom', '#lv1'),
 ('lab:framework/dikw', 'lab:partOf', 'lab:concept/business-data-science', '#lv1'),
 ('lab:framework/decision-process', 'lab:partOf', 'lab:concept/business-data-science', '#big'),
 ('lab:framework/smart', 'lab:partOf', 'lab:framework/decision-process', '#big'),
 ('lab:concept/big-data-5v', 'lab:relatedTo', 'lab:concept/business-data-science', '#big'),
 ('lab:concept/deductive', 'lab:contrastsWith', 'lab:concept/inductive', '#why'),
 ('lab:concept/inductive', 'lab:broader', 'lab:concept/business-data-science', '#why'),
 ('lab:concept/deductive', 'lab:prerequisiteOf', 'lab:method/ab-test', '#why'),
 ('lab:framework/dikw', 'lab:solves', 'lab:task/order-decision', '#lv1'),
 ('lab:framework/dikw', 'lab:hasLimitation', 'lab:limitation/filtered-data', '#lv1'),
 ('lab:limitation/filtered-data', 'lab:addressedBy', 'lab:concept/survivorship-bias', '#lv2'),
 ('lab:framework/dikw', 'lab:prerequisiteOf', 'lab:concept/survivorship-bias', '#lv2'),
 ('lab:concept/survivorship-bias', 'lab:hasLimitation', 'lab:limitation/cause-unknown', '#lv2'),
 ('lab:limitation/cause-unknown', 'lab:addressedBy', 'lab:method/stratification', '#lv3'),
 ('lab:concept/survivorship-bias', 'lab:prerequisiteOf', 'lab:concept/correlation-vs-causation', '#lv3'),
 ('lab:concept/confounder', 'lab:partOf', 'lab:concept/correlation-vs-causation', '#lv3'),
 ('lab:concept/confounder', 'lab:addressedBy', 'lab:method/stratification', '#lv3'),
 ('lab:concept/confirmation-bias', 'lab:relatedTo', 'lab:concept/correlation-vs-causation', '#lv3'),
 ('lab:method/stratification', 'lab:hasLimitation', 'lab:limitation/hidden-variables', '#lv3'),
 ('lab:limitation/hidden-variables', 'lab:raises', 'lab:question/hidden', '#lv3'),
 ('lab:limitation/hidden-variables', 'lab:addressedBy', 'lab:method/ab-test', '#lv4'),
 ('lab:question/hidden', 'lab:addressedBy', 'lab:concept/random-assignment', '#lv4'),
 ('lab:concept/correlation-vs-causation', 'lab:prerequisiteOf', 'lab:method/ab-test', '#lv4'),
 ('lab:concept/random-assignment', 'lab:partOf', 'lab:method/ab-test', '#lv4'),
 ('lab:concept/sample-size', 'lab:partOf', 'lab:method/ab-test', '#lv4'),
 ('lab:concept/standard-error', 'lab:relatedTo', 'lab:concept/sample-size', '#lv4'),
 ('lab:method/ab-test', 'lab:evaluatedBy', 'lab:metric/response-rate', '#lv4'),
 ('lab:method/ab-test', 'lab:hasLimitation', 'lab:limitation/small-sample', '#lv4'),
 ('lab:limitation/small-sample', 'lab:addressedBy', 'lab:concept/sample-size', '#lv4'),
 ('lab:method/ab-test', 'lab:partOf', 'lab:framework/decision-process', '#big'),
 ('lab:concept/data-storytelling', 'lab:partOf', 'lab:framework/decision-process', '#sum'),
 ('lab:limitation/small-sample', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:method/ab-test', 'lab:evaluatedBy', 'lab:metric/correct-choice', '#duel'),
 ('lab:concept/business-data-science', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:concept/data-mining', 'lab:broader', 'lab:concept/business-data-science', '#cases'),
 ('lab:concept/recommender', 'lab:broader', 'lab:concept/business-data-science', '#cases'),
 ('lab:concept/dynamic-pricing', 'lab:broader', 'lab:concept/business-data-science', '#cases'),
 ('lab:concept/data-mining', 'lab:hasLimitation', 'lab:concept/privacy', '#cases'),
 ('lab:concept/dynamic-pricing', 'lab:hasLimitation', 'lab:concept/privacy', '#cases'),
 ('lab:concept/big-data-5v', 'lab:prerequisiteOf', 'lab:concept/data-mining', '#cases'),
 ('lab:analogy/umbrella', 'lab:analogyOf', 'lab:framework/dikw', '#lv1'),
 ('lab:analogy/planes-customers', 'lab:analogyOf', 'lab:concept/survivorship-bias', '#lv2'),
 ('lab:framework/dikw', 'lab:demonstratedBy', 'lab:sim/w01-dikw', '#lv1'),
 ('lab:concept/survivorship-bias', 'lab:demonstratedBy', 'lab:sim/w01-planes', '#lv2'),
 ('lab:concept/confounder', 'lab:demonstratedBy', 'lab:sim/w01-lighter', '#lv3'),
 ('lab:method/ab-test', 'lab:demonstratedBy', 'lab:sim/w01-ab', '#lv4'),
 ('lab:claim/tripitaka-99mb', 'lab:supports', 'lab:concept/big-data-5v', '#why'), ('lab:claim/tripitaka-99mb', 'lab:assertedIn', 'lab:work/ahn-dsb-w01', '#why'),
 ('lab:claim/data-growth-2500x', 'lab:supports', 'lab:concept/big-data-5v', '#hero'), ('lab:claim/data-growth-2500x', 'lab:assertedIn', 'lab:work/ahn-dsb-w01', '#hero'),
 ('lab:claim/obama-ab', 'lab:supports', 'lab:method/ab-test', '#lv4', 'mid'), ('lab:claim/obama-ab', 'lab:assertedIn', 'lab:work/davier2023', '#lv4', 'mid'),
 ('lab:claim/planes-story', 'lab:supports', 'lab:concept/survivorship-bias', '#lv2'), ('lab:claim/planes-story', 'lab:assertedIn', 'lab:work/ellenberg2016', '#lv2'),
 ('lab:work/provost2014', 'lab:relatedTo', 'lab:concept/business-data-science', '#why'),
 ('lab:framework/smart', 'lab:prerequisiteOf', 'lab:framework/decision-process', '#big'),
]
EDGES = [e for e in EDGES if e]
# 교안 문헌과의 연결
EDGES += [('lab:framework/dikw', 'lab:relatedTo', 'lab:work/ahn-dsb-w01', '#lv1')]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

V_ALL = {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}
REFS = [
 R('ahn_dsb_w01', 'report', '비즈니스를위한데이터과학 강의 교안: 01. 비즈니스 데이터 과학의 이해', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/tripitaka-99mb', 'lab:claim/data-growth-2500x', 'lab:framework/dikw', 'lab:framework/decision-process', 'lab:concept/correlation-vs-causation'], 'lab:work/ahn-dsb-w01',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/tripitaka-99mb', 'loc': '1교시 2. 데이터의 진화과정'}, {'claim': 'lab:claim/data-growth-2500x', 'loc': '1교시 2'}]),
 R('ellenberg2016how', 'book', '틀리지 않는 법: 수학적 사고의 힘', [{'family': '엘렌버그', 'given': '조던'}], 2016, 'background', ['lab:claim/planes-story'], 'lab:work/ellenberg2016',
   V_ALL, '교안의 인용 서지로 확인', '김명남 옮김', publisher='열린책들'),
 R('davier2023ab', 'webpage', 'A/B Testing Got Obama $60 Million. You Can Do It Too.', [{'family': 'Davier', 'given': 'John'}], 2023, 'data', ['lab:claim/obama-ab'], 'lab:work/davier2023',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '교안의 인용 서지로 확인', '수치의 1차 출처 미확인',
   URL='https://www.mailmunch.com/blog/ab-testing-got-obama-60-million', **{'container-title': 'mailmunch'}),
 R('provost2014data', 'book', '비즈니스를 위한 데이터 과학', [{'family': '프로보스트', 'given': '포스터'}, {'family': '포셋', 'given': '톰'}], 2014, 'background', ['lab:concept/business-data-science'], 'lab:work/provost2014',
   V_ALL, '교안의 인용 서지로 확인', '강권학 옮김', publisher='한빛미디어'),
]
