# 11주차 · 데이터 모델 최적화와 시계열 모형
SLUG = 'dsb_w11_time_series'
FILE = 'week11_time_series.html'
TITLE = '시간이 기억하는 숫자 — 데이터 모델 최적화와 시계열 모형'
DESC = '비즈니스를 위한 데이터 과학 11주차 연구실 해설. 시간 추이에 맞는 차트와 상자수염도표, ACF·PACF, 추세·계절성 분해, 정상성과 차분, AR·ARIMA 예측을 예시 월매출로 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 벽에 걸린 긴 달력과 물결치는 매출 그래프 앞에서 작년 같은 달을 손가락으로 짚는 표지'
COVER_PROP = '📅'
SEARCH_PH = '예: 상자수염, ACF, PACF, 계절성, 차분, ARIMA, MAPE'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 차트'), ('#lv2', '② ACF·PACF'), ('#lv3', '③ 분해'), ('#lv4', '④ 차분'), ('#lv5', '⑤ ARIMA'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week10_regression_2.html"><small>← 이전 · 10주차</small>S자 곡선과 스무고개</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week12_visualization.html"><small>다음 · 12주차</small>숫자의 얼굴 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:concept/autocorrelation', 'lab:concept/ts-decomposition', 'lab:method/differencing', 'lab:method/arima', 'lab:method/seasonal-naive']
KGPATH = ['method/chart-choice', 'limitation/order-lost', 'concept/autocorrelation', 'limitation/mixed-patterns', 'concept/ts-decomposition', 'limitation/moving-mean', 'method/differencing', 'limitation/no-forecast', 'method/arima']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '교안의 ACF(0.8·0.65·0.52)·PACF(0.6·0.4·0.1) 그림이 실제 기온 데이터인지 예시인지 확인', '교안 실습의 PayPal 주가 데이터 출처 확인 — 이 페이지에는 싣지 않음']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 11. 데이터 모델 최적화와 시계열 모형. 인공지능융합학과. — 차트 선택(선형 vs 파이), 상자수염도표·히스토그램·트리맵·게이지, Tableau·Power BI, 자기상관·ACF·PACF(친구 비유, 기온 예), 지연효과, 추세·계절성·주기성·불규칙성, 정상성·차분, AR·MA·ARMA·ARIMA, AIC·BIC, MSE·MAE·MAPE, LSTM·GRU 전망은 교안 본문을 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/1HSHADm6JUVITCUz4WlBoPkg4xS0z2mMv?usp=sharing" target="_blank" rel="noopener">Colab</a>',
 '[2] 한국기술교육대학교. "핀테크데이터분석". 국민평생직업능력개발 STEP 온라인평생교육원. — 교안이 인용한 시계열 구성 요소·분해·모델 표의 출처.',
 '[3] Hyndman, R. J., Athanasopoulos, G. Forecasting: Principles and Practice (3rd ed.). OTexts. <a href="https://otexts.com/fpp3/" target="_blank" rel="noopener">링크</a> — 계절 나이브 기준선, 시계열 분해, ARIMA의 일반 설명.']
ILLUSTRATIVE = [
 '이 페이지의 분기 매출, 일매출 90일, AR(2) 시계열, 월매출 72개월, 차분 실험용 시계열은 모두 설명용 예시 데이터입니다.',
 'ARIMA는 MA 항 없이 AR 부분만(ARIMA(p, d, 0)) 최소제곱으로 추정했습니다. statsmodels의 ARIMA(최대우도)와 계수·AIC가 다를 수 있습니다.',
 '④칸의 정상성 판정은 구간 평균·표준편차와 ACF를 눈으로 본 것이며 ADF 검정이 아닙니다.']

GL = {
 '시계열': ['시계열 데이터', '데이터', '시간 순서대로 수집된 데이터. 순서와 시점이 분석의 핵심 변수.', 'lab:concept/time-series'],
 '자기상관': ['자기상관(Autocorrelation)', '통계', '현재 값이 자기 자신의 과거 값과 얼마나 닮았는지.', 'lab:concept/autocorrelation'],
 'ACF': ['ACF(자기상관함수)', '통계', '시차 k마다 현재와 k시점 전의 상관을 그린 것.', None],
 'PACF': ['PACF(부분자기상관함수)', '통계', '중간 시점의 간접 영향을 빼고 k시점 전과의 직접 상관만 잰 것.', None],
 '지연효과': ['지연효과(Lag Effect)', '시계열', '변화의 효과가 시간이 지난 뒤 나타나는 것. 광고 후 몇 달 뒤 매출.', None],
 '추세': ['추세(Trend)', '시계열', '장기적인 상승·하락 방향.', 'lab:concept/ts-decomposition'],
 '계절성': ['계절성(Seasonality)', '시계열', '연·월·주처럼 고정된 주기로 반복되는 패턴.', None],
 '정상성': ['정상성(Stationarity)', '시계열', '평균·분산이 시간에 따라 변하지 않고, 자기공분산이 시차에만 의존하는 성질.', None],
 '차분': ['차분(Differencing)', '시계열', '인접 관측값의 차이 Yₜ − Yₜ₋₁. 추세를 지워 정상화한다.', 'lab:method/differencing'],
 'ARIMA': ['ARIMA(p, d, q)', '모델', '자기회귀(p) + 차분(d) + 이동평균(q). 비정상 시계열을 차분해 예측.', 'lab:method/arima'],
 'AIC': ['AIC', '지표', '적합도와 모델 복잡도를 함께 따지는 정보 기준. 낮을수록 좋다.', None],
 'MAPE': ['MAPE', '지표', '평균 |실제 − 예측| ÷ 실제 × 100%. 규모가 다른 데이터끼리 비교 가능.', None],
 '상자수염도표': ['상자수염도표(Box Plot)', '시각화', '최솟값·Q1·중앙값·Q3·최댓값과 이상값을 한 그림에.', 'lab:method/chart-choice'],
 'IQR': ['IQR(사분위수 범위)', '통계', 'Q3 − Q1. 가운데 50%의 폭.', None],
}
CORE = ['시계열', '자기상관', 'ACF', 'PACF', '지연효과', '추세', '계절성', '정상성', '차분', 'ARIMA', 'AIC', 'MAPE', '상자수염도표', 'IQR']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '시간 추이 데이터를 시각화할 때 가장 적절한 차트와 그 이유는? (교안 연습문제 1)', 'o': ['파이 차트 — 각 시점의 비중', '선형 차트 — 시간 흐름에 따른 변화와 추세', '막대 차트 — 정확한 비교', '산점도 — 상관관계'], 'a': 1, 'why': '파이는 비율용이라 시간 순서 정보가 사라집니다.', 'hint': '①칸 차트 버튼.', 'assess': 'lab:method/chart-choice'},
  {'id': 'q2', 'q': 'Q1 = 280, Q3 = 330일 때 1.5·IQR 기준 상한은?', 'o': ['330', '355', '405'], 'a': 2, 'why': 'IQR = 50, 330 + 1.5 × 50 = 405.', 'hint': 'Q3 + 1.5 × (Q3 − Q1)', 'calc': True, 'assess': 'lab:method/chart-choice'}],
 'lv2': [
  {'id': 'q3', 'q': 'ACF는 서서히 줄고 PACF는 시차 2 뒤 0 근처로 떨어진다. 알맞은 모델은?', 'o': ['AR(2)', 'MA(2)', '백색잡음'], 'a': 0, 'why': 'PACF가 p 시점 뒤 끊기면 AR(p)입니다(교안).', 'hint': '②칸 기본값.', 'assess': 'lab:concept/autocorrelation'},
  {'id': 'q4', 'q': 'PACF가 ACF와 다른 점은?', 'o': ['미래 값을 쓴다', '중간 시점을 거친 간접 영향을 뺀다', '항상 더 크다'], 'a': 1, 'why': 'A→B→C에서 B를 통한 영향을 빼고 A와 C의 직접 연결만 봅니다.', 'hint': '친구 관계 비유.', 'assess': 'lab:concept/autocorrelation'}],
 'lv3': [
  {'id': 'q5', 'q': '시계열 구성 요소 중 계절성에 대한 설명으로 가장 적절한 것은? (교안 연습문제 2)', 'o': ['장기적인 상승·하락 방향', '일정한 주기로 반복되는 패턴(연·월·주)', '계절성보다 긴 경제 순환', '무작위 변동'], 'a': 1, 'why': '소매업의 연말 매출 증가, 여름철 아이스크림 판매가 예입니다.', 'hint': '③칸 주황 줄.', 'assess': 'lab:concept/ts-decomposition'},
  {'id': 'q6', 'q': '분해에서 추세를 찾는 데 쓴 방법은?', 'o': ['12개월 이동평균', '최댓값', '차분'], 'a': 0, 'why': '이동평균은 단기 변동(계절·잡음)을 지우고 장기 방향을 남깁니다.', 'hint': '③칸 부제.', 'assess': 'lab:concept/ts-decomposition'}],
 'lv4': [
  {'id': 'q7', 'q': '정상 시계열의 조건이 아닌 것은?', 'o': ['평균이 일정', '분산이 일정', '값이 계속 증가'], 'a': 2, 'why': '추세가 있으면 평균이 움직이므로 비정상입니다.', 'hint': '④칸 네 구간 평균.', 'assess': 'lab:method/differencing'},
  {'id': 'q8', 'q': '100, 103, 108, 115의 1차 차분은?', 'o': ['3, 5, 7', '2, 2', '103, 108, 115'], 'a': 0, 'why': '103−100, 108−103, 115−108. 다시 차분하면 2, 2(2차 차분).', 'hint': 'Yₜ − Yₜ₋₁', 'calc': True, 'assess': 'lab:method/differencing'}],
 'lv5': [
  {'id': 'q9', 'q': 'ARIMA(p, d, q)에서 d가 뜻하는 것은?', 'o': ['자기회귀 차수', '차분 횟수', '이동평균 차수'], 'a': 1, 'why': 'I(Integrated)가 차분입니다.', 'hint': '⑤칸 d 버튼.', 'assess': 'lab:method/arima'},
  {'id': 'q10', 'q': '실제 100, 예측 90 / 실제 200, 예측 210일 때 MAPE는?', 'o': ['7.5%', '10%', '15%'], 'a': 0, 'why': '(10% + 5%) ÷ 2 = 7.5%.', 'hint': '|오차| ÷ 실제의 평균', 'calc': True, 'assess': 'lab:method/arima'},
  {'id': 'q11', 'q': '시계열 예측 모델이 실무에서 가장 많이 쓰이는 분야는? (교안 연습문제 3)', 'o': ['직원 채용 계획', '매출 예측 및 재고 관리', '제품 품질 검사', '고객 만족도 조사'], 'a': 1, 'why': '시간적 패턴이 중요한 매출·재고·수요 예측에 가장 많이 쓰입니다.', 'hint': '⑤칸 현장에 옮기면.', 'assess': 'lab:method/arima'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('dataset/monthly-sales', 'Dataset', '예시 월매출 72개월', 'synthetic monthly sales (72)', '#lv3', '추세 + 12월 정점 계절성 + AR(1) 잡음. 설명용.', level=1, family='basics'),
 N('concept/time-series', 'Concept', '시계열 데이터', 'time series', '#why', level=1, family='basics'),
 N('task/forecasting', 'Task', '시계열 예측', 'forecasting', '#why', level=1, family='basics'),
 N('method/chart-choice', 'Method', '차트 선택과 상자수염도표', 'chart choice and box plots', '#lv1', level=1, family='data'),
 N('concept/autocorrelation', 'Concept', '자기상관(ACF·PACF)', 'autocorrelation (ACF, PACF)', '#lv2', level=1, family='basics'),
 N('concept/ts-decomposition', 'Concept', '시계열 분해(추세·계절·불규칙)', 'time series decomposition', '#lv3', level=1, family='basics'),
 N('concept/stationarity', 'Concept', '정상성', 'stationarity', '#lv4', level=2, family='basics'),
 N('method/differencing', 'Method', '차분', 'differencing', '#lv4', level=1, family='data'),
 N('method/arima', 'Method', 'AR·ARIMA', 'AR and ARIMA', '#lv5', level=2, family='basics'),
 N('method/seasonal-naive', 'Method', '계절 나이브(작년 같은 달)', 'seasonal naive', '#duel', '작년 같은 달 값 + 최근 연간 증가분으로 예측하는 기준선.', level=1, family='evaluation'),
 N('metric/mape', 'Metric', 'MAPE', 'MAPE', '#lv5', level=1, family='evaluation'),
 N('limitation/order-lost', 'Limitation', '순서 정보를 버린다', 'order is lost', '#lv1'),
 N('limitation/mixed-patterns', 'Limitation', '추세·계절이 섞여 있다', 'patterns are mixed', '#lv2'),
 N('limitation/moving-mean', 'Limitation', '평균이 시간에 따라 움직인다', 'moving mean', '#lv3'),
 N('limitation/no-forecast', 'Limitation', '아직 예측하지 않았다', 'no forecast yet', '#lv4'),
 N('claim/acf-pacf-rule', 'Claim', 'ACF가 서서히 줄고 PACF가 특정 시점 뒤 급감하면 AR 모형이 적합', 'ACF decays + PACF cuts off ⇒ AR', '#lv2', source=[{'cite': '교안 11주차', 'loc': '3교시 3'}]),
 N('claim/pie-time', 'Claim', '파이 차트는 시간 순서 정보를 잃어 시간 추이 분석에 부적절', 'pie charts lose time order', '#lv1', source=[{'cite': '교안 11주차', 'loc': '1교시 1'}]),
 N('question/core', 'Question', '이번 달 매출은 과거를 얼마나 기억하고 있을까?', 'How much does this month remember?', '#hero'),
 N('question/duel', 'Question', '정석 ARIMA와 작년 같은 달, 어느 쪽이 나을까', 'ARIMA or seasonal naive?', '#duel'),
 N('analogy/friends', 'Analogy', 'A→B→C 친구 관계 ↔ PACF', 'chain of friends ↔ PACF', '#lv2', anchorType='D'),
 N('analogy/height', 'Analogy', '아이의 키 vs 올해 큰 만큼 ↔ 차분', 'height vs growth ↔ differencing', '#lv4', anchorType='D'),
 N('sim/w11-box', 'Simulation', '차트 바꾸기와 상자수염', 'chart switch and box plot', '#lv1'),
 N('sim/w11-acf', 'Simulation', 'AR(2) ACF·PACF', 'AR(2) ACF/PACF', '#lv2'),
 N('sim/w11-dec', 'Simulation', '네 줄 분해', 'four-row decomposition', '#lv3'),
 N('sim/w11-diff', 'Simulation', '차분과 구간 평균', 'differencing check', '#lv4'),
 N('sim/w11-arima', 'Simulation', 'ARIMA 12개월 예측', 'ARIMA 12-month forecast', '#lv5'),
 N('work/ahn-dsb-w11', 'Work', '안상선, 비즈니스를위한데이터과학 교안 11주차', 'Ahn, DSB lecture notes week 11', '#footer'),
 N('work/step-fintech', 'Work', '한국기술교육대학교, 핀테크데이터분석(STEP)', 'KoreaTech STEP Fintech Data Analysis', '#footer'),
 N('work/fpp3', 'Work', 'Hyndman·Athanasopoulos, Forecasting: Principles and Practice', 'FPP3', '#footer'),
]

EDGES = [
 ('lab:concept/time-series', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:method/arima', 'lab:solves', 'lab:task/forecasting', '#lv5'),
 ('lab:method/chart-choice', 'lab:hasLimitation', 'lab:limitation/order-lost', '#lv1'),
 ('lab:limitation/order-lost', 'lab:addressedBy', 'lab:concept/autocorrelation', '#lv2'),
 ('lab:concept/autocorrelation', 'lab:partOf', 'lab:concept/time-series', '#lv2'),
 ('lab:concept/autocorrelation', 'lab:hasLimitation', 'lab:limitation/mixed-patterns', '#lv2'),
 ('lab:limitation/mixed-patterns', 'lab:addressedBy', 'lab:concept/ts-decomposition', '#lv3'),
 ('lab:concept/ts-decomposition', 'lab:evaluatedOn', 'lab:dataset/monthly-sales', '#lv3'),
 ('lab:concept/ts-decomposition', 'lab:hasLimitation', 'lab:limitation/moving-mean', '#lv3'),
 ('lab:limitation/moving-mean', 'lab:addressedBy', 'lab:method/differencing', '#lv4'),
 ('lab:method/differencing', 'lab:prerequisiteOf', 'lab:concept/stationarity', '#lv4'),
 ('lab:method/differencing', 'lab:hasLimitation', 'lab:limitation/no-forecast', '#lv4'),
 ('lab:limitation/no-forecast', 'lab:addressedBy', 'lab:method/arima', '#lv5'),
 ('lab:concept/stationarity', 'lab:prerequisiteOf', 'lab:method/arima', '#lv5'),
 ('lab:concept/autocorrelation', 'lab:prerequisiteOf', 'lab:method/arima', '#lv5'),
 ('lab:method/arima', 'lab:evaluatedBy', 'lab:metric/mape', '#lv5'),
 ('lab:method/arima', 'lab:evaluatedOn', 'lab:dataset/monthly-sales', '#lv5'),
 ('lab:method/seasonal-naive', 'lab:solves', 'lab:task/forecasting', '#duel'),
 ('lab:method/seasonal-naive', 'lab:evaluatedBy', 'lab:metric/mape', '#duel'),
 ('lab:metric/mape', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/friends', 'lab:analogyOf', 'lab:concept/autocorrelation', '#lv2'),
 ('lab:analogy/height', 'lab:analogyOf', 'lab:method/differencing', '#lv4'),
 ('lab:method/chart-choice', 'lab:demonstratedBy', 'lab:sim/w11-box', '#lv1'),
 ('lab:concept/autocorrelation', 'lab:demonstratedBy', 'lab:sim/w11-acf', '#lv2'),
 ('lab:concept/ts-decomposition', 'lab:demonstratedBy', 'lab:sim/w11-dec', '#lv3'),
 ('lab:method/differencing', 'lab:demonstratedBy', 'lab:sim/w11-diff', '#lv4'),
 ('lab:method/arima', 'lab:demonstratedBy', 'lab:sim/w11-arima', '#lv5'),
 ('lab:claim/acf-pacf-rule', 'lab:supports', 'lab:method/arima', '#lv2'), ('lab:claim/acf-pacf-rule', 'lab:assertedIn', 'lab:work/ahn-dsb-w11', '#lv2'),
 ('lab:claim/pie-time', 'lab:supports', 'lab:method/chart-choice', '#lv1'), ('lab:claim/pie-time', 'lab:assertedIn', 'lab:work/ahn-dsb-w11', '#lv1'),
 ('lab:concept/ts-decomposition', 'lab:relatedTo', 'lab:work/step-fintech', '#footer'),
 ('lab:method/seasonal-naive', 'lab:relatedTo', 'lab:work/fpp3', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w11', 'report', '비즈니스를위한데이터과학 강의 교안: 11. 데이터 모델 최적화와 시계열 모형', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/acf-pacf-rule', 'lab:claim/pie-time', 'lab:concept/autocorrelation', 'lab:method/differencing', 'lab:method/arima'], 'lab:work/ahn-dsb-w11',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/acf-pacf-rule', 'loc': '3교시 3. ARIMA 파라미터 결정'}, {'claim': 'lab:claim/pie-time', 'loc': '1교시 1. 분기별 매출현황'}]),
 R('step_fintech', 'webpage', '핀테크데이터분석', [{'literal': '한국기술교육대학교'}], None, 'background', ['lab:concept/ts-decomposition'], 'lab:work/step-fintech',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '교안 인용 서지 그대로', '', publisher='STEP 온라인평생교육원', URL='https://www.step.or.kr'),
 R('fpp3', 'book', 'Forecasting: Principles and Practice (3rd ed.)', [{'family': 'Hyndman', 'given': 'Rob J.'}, {'family': 'Athanasopoulos', 'given': 'George'}], 2021, 'background', ['lab:method/seasonal-naive'], 'lab:work/fpp3',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '서지 기억 기반 — 확인 권장', '', publisher='OTexts', URL='https://otexts.com/fpp3/'),
]
