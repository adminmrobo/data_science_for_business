# 3주차 · 데이터 분석을 위한 준비
SLUG = 'dsb_w03_analysis_prep'
FILE = 'week03_analysis_prep.html'
TITLE = '분석 전에 데이터를 손보다 — 문제 정의, 전처리, 품질 평가'
DESC = '비즈니스를 위한 데이터 과학 3주차 연구실 해설. SMART 목표, 결측값(MCAR·MAR·MNAR)과 KNN 대체, 이상값 탐지, 중복과 품질 6차원, EDA를 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 빈칸과 튀는 값, 겹친 카드가 섞인 큰 표를 작업대 위에서 함께 손질하는 표지'
COVER_PROP = '🧹'
SEARCH_PH = '예: SMART, MAR, KNN, IQR, 유일성'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 문제 정의'), ('#lv2', '② 결측값'), ('#lv3', '③ 이상값'), ('#lv4', '④ 중복·품질'), ('#lv5', '⑤ EDA'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week02_data_collection.html"><small>← 이전 · 2주차</small>데이터는 어디서 오는가</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><span class="muted" style="padding:10px 14px"><small style="display:block;font-size:12px">다음 · 4주차</small>데이터 분석 개념의 이해 (준비 중)</span>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'doc_think', 'robo_meh', 'robo_calc', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'doc_board']
ABOUT = ['lab:framework/smart', 'lab:concept/missing-mechanism', 'lab:method/knn-imputation', 'lab:method/outlier-detection', 'lab:concept/data-quality-6', 'lab:method/eda']
KGPATH = ['framework/smart', 'limitation/missing-values', 'concept/missing-mechanism', 'method/knn-imputation', 'limitation/outliers-remain', 'method/outlier-detection', 'limitation/duplicates-remain', 'concept/data-quality-6', 'limitation/meaning-unknown', 'method/eda', 'limitation/bivariate-only']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '전처리가 프로젝트 시간의 약 80%라는 수치는 교안의 서술 — 1차 출처 확인 필요']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 03. 데이터 분석을 위한 준비. 인공지능융합학과. — 문제 유형, SMART, 분석 목표 예시, 전처리 프로세스(약 80%), ETL, 결측 메커니즘과 KNN 대체, 이상값 탐지·처리, 중복 유형(ORD001 예시), EDA 기법, 품질 6차원과 지표 식, 도서관 무결성 예시는 교안 본문을 옮김.',
 '[2] Hyndman, R. J., & Athanasopoulos, G. (2018). Forecasting: principles and practice. <a href="https://otexts.com/fppkr/graphics-scatterplots.html" target="_blank" rel="noopener">OTexts 한국어판</a> — 교안이 산점도와 피어슨 상관계수 그림의 출처로 인용.',
 '[3] 위키독스. K-최근접 이웃. <a href="https://wikidocs.net/252249" target="_blank" rel="noopener">링크</a> — 교안이 KNN 개념 그림의 출처로 인용.']
ILLUSTRATIVE = [
 '②칸과 대결: 고객 200명(시드 8)의 나이·연소득, 결측 확률(MCAR 30%, MAR 35세 미만 65%·이상 8%, MNAR 상위 30% 소득 70%·나머지 10%)은 설명용 값입니다.',
 '③칸 구매액 120건(시드 19), VIP 3건과 오류 2건, 1회 구매 한도 300만 원은 설명용 값입니다.',
 '④칸 주문 기록 12줄의 이름·이메일은 만든 값이며 실제 인물이 아닙니다. ORD001 세 줄 중복은 교안 예시를 따랐습니다.',
 '⑤칸 매장 60곳(시드 23)의 광고비·매출과 "매출 ∝ 광고비^0.55" 규칙은 설명을 위해 만든 것입니다.']

GL = {
 '5W1H': ['5W1H', '틀', '누가·언제·어디서·무엇을·왜·어떻게로 문제를 구체화하는 틀.', None],
 'SMART': ['SMART 원칙', '틀', 'Specific·Measurable·Achievable·Relevant·Time-bound. 잴 수 있고 기한이 있는 목표를 세우는 기준.', 'lab:framework/smart'],
 'KPI': ['KPI (핵심 성과 지표)', '지표', '목표 달성 정도를 재는 핵심 숫자. 재무·운영·고객·혁신 지표로 나눈다.', 'lab:metric/kpi'],
 'ETL': ['ETL', '방법', 'Extract(추출) → Transform(변환) → Load(적재). 여러 출처의 데이터를 분석용 저장소로 옮기는 과정.', None],
 '결측값': ['결측값', '데이터', '데이터 세트에서 누락되었거나 알 수 없거나 잘못 입력된 값.', 'lab:concept/missing-mechanism'],
 'MCAR': ['MCAR (완전 무작위 결측)', '통계', '빠지는 것이 어떤 변수와도 관계없이 무작위인 경우.', None],
 'MAR': ['MAR (무작위 결측)', '통계', '빠지는 것이 다른 관측 변수(예: 나이)에 따라 달라지는 경우.', None],
 'MNAR': ['MNAR (비무작위 결측)', '통계', '빠지는 것이 빠진 값 자체(예: 높은 소득)에 따라 달라지는 경우.', None],
 'KNN': ['KNN 대체', '방법', '빈칸이 있는 기록과 가장 가까운 k개 기록의 평균(또는 중앙값)으로 빈칸을 채우는 방법.', 'lab:method/knn-imputation'],
 '이상값': ['이상값(이상치)', '데이터', '전체 분포에서 크게 벗어난 값. 오류일 수도, 중요한 사건(VIP)일 수도 있다.', 'lab:method/outlier-detection'],
 'Z-score': ['Z-score', '통계', '(값 − 평균) ÷ 표준편차. 평균에서 표준편차 몇 개만큼 떨어졌는지.', None],
 'IQR': ['IQR (사분위수 범위)', '통계', 'Q3 − Q1. Q1 − 1.5×IQR보다 작거나 Q3 + 1.5×IQR보다 크면 이상값 후보로 본다.', None],
 '수정 Z-score': ['수정 Z-score', '통계', '평균·표준편차 대신 중앙값과 MAD(중앙값 절대 편차)로 계산해 극단값에 덜 흔들리는 점수.', None],
 '캡핑': ['캡핑', '방법', '정해 둔 경계값을 넘는 값을 경계값으로 바꿔 영향을 줄이는 처리.', None],
 '중복': ['중복 데이터', '데이터', '완전 중복(모든 필드 같음), 부분 중복(식별자 같고 일부 다름), 유사 중복(표기만 다름).', 'lab:concept/duplicates'],
 '개체 무결성': ['개체 무결성', '규칙', '기본키는 유일하고 비어 있지 않아야 한다. 모든 책에 고유한 번호.', None],
 '참조 무결성': ['참조 무결성', '규칙', '참조하는 값은 실제로 있어야 한다. 없는 책은 대출할 수 없다.', None],
 '도메인 무결성': ['도메인 무결성', '규칙', '각 필드에는 정해진 형식과 범위의 값만 들어가야 한다. 나이 0~150.', None],
 '데이터 품질': ['데이터 품질', '개념', '데이터가 의도된 목적에 얼마나 맞는지의 척도. 정확성·완전성·일관성·적시성·유효성·유일성.', 'lab:concept/data-quality-6'],
 'EDA': ['EDA (탐색적 데이터 분석)', '방법', '모델링 전에 그림과 요약 통계로 데이터의 분포·관계·패턴을 살피는 과정.', 'lab:method/eda'],
 '왜도': ['왜도', '통계', '분포가 한쪽으로 치우친 정도. 오른쪽 꼬리가 길면 양수.', None],
 '피어슨': ['피어슨 상관계수', '통계', '두 변수의 직선 관계 강도와 방향(−1~1).', 'lab:metric/pearson'],
 '스피어만': ['스피어만 상관계수', '통계', '순위로 계산한 상관. 휘어진 단조 관계와 극단값에 강하다.', 'lab:metric/spearman'],
 '전처리': ['데이터 전처리', '방법', '분석에 알맞은 형태로 데이터를 통합·정제·변환·검증하는 과정.', 'lab:concept/preprocessing'],
}
CORE = ['SMART', 'KPI', '결측값', 'MAR', 'MNAR', 'KNN', '이상값', 'IQR', 'Z-score', '참조 무결성', '데이터 품질', 'EDA']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': 'SMART 목표 설정 기준에 해당하지 않는 것은? (교안 연습문제 1)', 'o': ['Specific', 'Measurable', 'Reasonable'], 'a': 2, 'why': 'SMART는 Specific, Measurable, Achievable, Relevant, Time-bound입니다.', 'hint': '조립기의 다섯 칩을 보세요.', 'assess': 'lab:framework/smart'},
  {'id': 'q2', 'q': '"다음 달 매장별 판매량은 몇 개일까?"는 어떤 문제 유형인가?', 'o': ['분류', '예측', '탐색'], 'a': 1, 'why': '미래의 값을 맞히는 예측(수요 예측) 문제입니다.', 'hint': '답이 범주인지 숫자인지 보세요.', 'assess': 'lab:concept/problem-types'}],
 'lv2': [
  {'id': 'q3', 'q': '결측값 처리에 대한 설명으로 올바른 것은? (교안 연습문제 2)', 'o': ['모든 결측값은 평균으로 대체한다', '결측값이 있는 행은 모두 삭제하는 것이 안전하다', '결측 패턴과 메커니즘을 분석한 뒤 방법을 고른다'], 'a': 2, 'why': 'MCAR·MAR·MNAR에 따라 알맞은 방법이 다릅니다. 대결이 그 예입니다.', 'hint': '②칸에서 메커니즘을 바꿔 보세요.', 'assess': 'lab:concept/missing-mechanism'},
  {'id': 'q4', 'q': '고소득자가 소득을 일부러 비웠다. 이 결측은?', 'o': ['MCAR', 'MAR', 'MNAR'], 'a': 2, 'why': '빠진 값 자체(높은 소득) 때문에 빠졌으므로 MNAR입니다.', 'hint': '빠진 이유가 무엇과 관련 있나요?', 'assess': 'lab:concept/missing-mechanism'}],
 'lv3': [
  {'id': 'q5', 'q': 'Q1 = 3만 원, Q3 = 7만 원이면 IQR 기준 위쪽 경계는?', 'o': ['10만 원', '13만 원', '7만 원'], 'a': 1, 'why': 'IQR = 4만 원, 위쪽 경계 = 7 + 1.5 × 4 = 13만 원입니다.', 'hint': 'Q3 + 1.5 × (Q3 − Q1)', 'calc': True, 'assess': 'lab:method/outlier-detection'},
  {'id': 'q6', 'q': '999만 원짜리 입력 오류 하나 때문에 Z-score가 다른 이상값을 놓친 이유는?', 'o': ['중앙값이 바뀌어서', '그 값이 평균과 표준편차를 크게 부풀려서', 'IQR이 작아져서'], 'a': 1, 'why': '평균·표준편차는 극단값에 민감합니다. 그래서 강건한 IQR·수정 Z-score를 함께 씁니다.', 'hint': 'Z-score를 고르고 인사이트 문장을 보세요.', 'assess': 'lab:method/outlier-detection'}],
 'lv4': [
  {'id': 'q7', 'q': '데이터 품질 6차원에 포함되지 않는 것은? (교안 연습문제 3)', 'o': ['완전성', '복잡성', '일관성'], 'a': 1, 'why': '정확성·완전성·일관성·적시성·유효성·유일성이 6차원입니다.', 'hint': '④칸 막대의 이름을 세어 보세요.', 'assess': 'lab:concept/data-quality-6'},
  {'id': 'q8', 'q': '대출 기록에 도서관에 없는 책 B999가 있다. 어떤 무결성을 어겼나?', 'o': ['개체 무결성', '참조 무결성', '도메인 무결성'], 'a': 1, 'why': '참조하는 값(도서번호)이 실제로 있어야 한다는 참조 무결성입니다.', 'hint': '교안의 도서관 비유.', 'assess': 'lab:concept/data-quality-6'}],
 'lv5': [
  {'id': 'q9', 'q': '매출 분포가 오른쪽으로 긴 꼬리를 가질 때 평균과 중앙값의 관계는 보통?', 'o': ['평균 > 중앙값', '평균 = 중앙값', '평균 < 중앙값'], 'a': 0, 'why': '큰 값 몇 개가 평균을 끌어올립니다.', 'hint': '단변량 보기의 두 선.', 'assess': 'lab:method/eda'},
  {'id': 'q10', 'q': '극단값 매장 하나를 넣었을 때 덜 흔들리는 것은?', 'o': ['피어슨 상관계수', '스피어만 상관계수', '둘 다 똑같이 흔들린다'], 'a': 1, 'why': '스피어만은 값 대신 순위를 쓰므로 극단값 하나의 영향이 작습니다.', 'hint': '버튼을 눌러 두 숫자를 비교하세요.', 'assess': 'lab:metric/spearman'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('framework/smart', 'Framework', 'SMART 원칙', 'SMART criteria', '#lv1', level=1, family='basics', domain=['biz']),
 N('concept/problem-types', 'Concept', '문제 유형(분류·예측·최적화·탐색)', 'problem types', '#big', '비즈니스 문제를 분류·예측·최적화·탐색으로 나누는 체계. 유형이 모델과 지표를 정한다.', level=1, family='basics'),
 N('metric/kpi', 'Metric', 'KPI', 'key performance indicator', '#lv1', level=1, family='evaluation', domain=['biz']),
 N('concept/preprocessing', 'Concept', '데이터 전처리', 'data preprocessing', '#big', level=1, family='data'),
 N('method/etl', 'Method', 'ETL', 'extract-transform-load', '#big', '추출 → 변환 → 적재. 다중 소스 데이터를 통합하는 과정.', level=2, family='data'),
 N('concept/missing-mechanism', 'Concept', '결측 메커니즘(MCAR·MAR·MNAR)', 'missingness mechanisms', '#lv2', '값이 빠진 이유에 따라 MCAR·MAR·MNAR로 나눈다. 처리 방법의 선택 기준.', level=2, family='data', domain=['stats']),
 N('method/listwise-deletion', 'Method', '결측 행 삭제', 'listwise deletion', '#lv2', '빈칸이 있는 행을 통째로 지우는 방법. MCAR가 아니면 편향을 만든다.', level=1, family='data', domain=['stats']),
 N('method/mean-imputation', 'Method', '평균 대체', 'mean imputation', '#lv2', '빈칸을 관측값 평균으로 채우는 방법. 퍼짐(분산)을 줄인다.', level=1, family='data', domain=['stats']),
 N('method/knn-imputation', 'Method', 'KNN 대체', 'KNN imputation', '#lv2', level=2, family='data', domain=['stats', 'ai']),
 N('method/outlier-detection', 'Method', '이상값 탐지(Z·IQR·수정 Z)', 'outlier detection', '#lv3', level=2, family='data', domain=['stats']),
 N('concept/masking', 'Concept', '가림 효과', 'masking effect', '#lv3', '극단값 하나가 평균·표준편차를 부풀려 다른 이상값을 숨기는 현상.', level=3, family='data', domain=['stats']),
 N('method/outlier-treatment', 'Method', '이상값 처리(제거·캡핑·별도 분석)', 'outlier treatment', '#lv3', '찾은 이상값을 제거·변환·캡핑하거나, 의미 있는 값이면 따로 분석한다.', level=2, family='data'),
 N('concept/duplicates', 'Concept', '중복 데이터', 'duplicate records', '#lv4', level=1, family='data'),
 N('concept/integrity', 'Concept', '무결성(개체·참조·도메인)', 'integrity constraints', '#lv4', '기본키 유일성, 참조 값 존재, 필드 형식·범위를 지키는 규칙.', level=2, family='data'),
 N('concept/data-quality-6', 'Concept', '데이터 품질 6차원', 'six dimensions of data quality', '#lv4', level=2, family='data'),
 N('method/data-profiling', 'Method', '데이터 프로파일링', 'data profiling', '#sum', '구조·내용·관계를 분석해 품질 현황을 파악하는 방법.', level=2, family='data'),
 N('method/eda', 'Method', '탐색적 데이터 분석(EDA)', 'exploratory data analysis', '#lv5', level=1, family='data', domain=['stats', 'ai']),
 N('metric/pearson', 'Metric', '피어슨 상관계수', 'Pearson correlation', '#lv5', level=2, family='evaluation', domain=['stats']),
 N('metric/spearman', 'Metric', '스피어만 상관계수', 'Spearman correlation', '#lv5', level=2, family='evaluation', domain=['stats']),
 N('metric/estimation-error', 'Metric', '평균 추정 오차', 'mean estimation error', '#duel', '추정한 평균과 참값 평균의 차이.', level=1, family='evaluation', domain=['stats']),
 N('limitation/missing-values', 'Limitation', '목표를 잴 데이터에 빈칸', 'missing values distort the metric', '#lv1'),
 N('limitation/outliers-remain', 'Limitation', '채워진 값 속 오류·극단값', 'errors and extremes remain', '#lv2'),
 N('limitation/duplicates-remain', 'Limitation', '겹친 기록·제각각 형식', 'duplicates and inconsistent formats remain', '#lv3'),
 N('limitation/meaning-unknown', 'Limitation', '데이터가 무엇을 말하는지 모름', 'data not yet explored', '#lv4'),
 N('limitation/bivariate-only', 'Limitation', '두 변수까지만 · 상관은 인과 아님', 'bivariate only', '#lv5'),
 N('limitation/mnar', 'Limitation', 'MNAR은 어떤 대체로도 완전히 못 고침', 'MNAR cannot be fully corrected', '#lv2', '빠진 이유가 빠진 값 자체면 남은 정보만으로는 되살릴 수 없다.'),
 N('claim/prep-80', 'Claim', '전처리는 분석 프로젝트 시간의 약 80%', 'preprocessing ≈ 80% of project time', '#hero', source=[{'cite': '교안 3주차', 'loc': '2교시 1'}], confidence='mid'),
 N('claim/smart-example', 'Claim', '분석 목표 예: 3개월 내 이탈률 15% → 10%, 연간 매출 5% 증대', 'SMART goal example', '#lv1', source=[{'cite': '교안 3주차', 'loc': '1교시 14'}]),
 N('question/core', 'Question', '분석 전에 무엇을 정하고 데이터를 얼마나 손봐야 할까?', 'What to define and clean before analysis?', '#hero'),
 N('question/duel', 'Question', '빈칸 있는 줄은 지우는 게 안전할까?', 'Is deleting incomplete rows safe?', '#duel'),
 N('question/mnar', 'Question', 'MNAR이 의심될 때 무엇을 더 모아야 할까?', 'What else to collect under MNAR?', '#lv2'),
 N('analogy/library', 'Analogy', '도서관 책 번호·대출·회원 정보 ↔ 무결성', 'library ↔ integrity constraints', '#lv4', anchorType='D'),
 N('analogy/vip-error', 'Analogy', 'VIP 고객과 입력 실수 ↔ 이상값 판정', 'VIP vs typo ↔ outlier judgment', '#lv3', anchorType='C'),
 N('sim/w03-smart', 'Simulation', 'SMART 목표 조립기', 'SMART builder', '#lv1'),
 N('sim/w03-missing', 'Simulation', '고객 200명 결측값 실험', 'missing data simulation', '#lv2'),
 N('sim/w03-outlier', 'Simulation', '구매액 120건 이상값 실험', 'outlier simulation', '#lv3'),
 N('sim/w03-quality', 'Simulation', '주문 기록 12줄 품질 점수', 'data quality table', '#lv4'),
 N('sim/w03-eda', 'Simulation', '매장 60곳 EDA', 'EDA simulation', '#lv5'),
 N('work/ahn-dsb-w03', 'Work', '안상선, 비즈니스를위한데이터과학 교안 3주차', 'Ahn, DSB lecture notes week 3', '#footer'),
 N('work/hyndman2018', 'Work', 'Hyndman·Athanasopoulos(2018) Forecasting: principles and practice', 'Hyndman & Athanasopoulos (2018)', '#footer'),
]

EDGES = [
 ('lab:concept/problem-types', 'lab:prerequisiteOf', 'lab:framework/smart', '#lv1'),
 ('lab:framework/smart', 'lab:evaluatedBy', 'lab:metric/kpi', '#lv1'),
 ('lab:framework/smart', 'lab:hasLimitation', 'lab:limitation/missing-values', '#lv1'),
 ('lab:limitation/missing-values', 'lab:addressedBy', 'lab:concept/missing-mechanism', '#lv2'),
 ('lab:framework/smart', 'lab:prerequisiteOf', 'lab:concept/preprocessing', '#big'),
 ('lab:method/etl', 'lab:partOf', 'lab:concept/preprocessing', '#big'),
 ('lab:concept/missing-mechanism', 'lab:partOf', 'lab:concept/preprocessing', '#lv2'),
 ('lab:concept/missing-mechanism', 'lab:prerequisiteOf', 'lab:method/knn-imputation', '#lv2'),
 ('lab:method/listwise-deletion', 'lab:contrastsWith', 'lab:method/knn-imputation', '#duel'),
 ('lab:method/mean-imputation', 'lab:contrastsWith', 'lab:method/knn-imputation', '#lv2'),
 ('lab:method/listwise-deletion', 'lab:evaluatedBy', 'lab:metric/estimation-error', '#duel'),
 ('lab:method/knn-imputation', 'lab:evaluatedBy', 'lab:metric/estimation-error', '#duel'),
 ('lab:concept/missing-mechanism', 'lab:hasLimitation', 'lab:limitation/mnar', '#lv2'),
 ('lab:limitation/mnar', 'lab:raises', 'lab:question/mnar', '#lv2'),
 ('lab:method/knn-imputation', 'lab:hasLimitation', 'lab:limitation/outliers-remain', '#lv2'),
 ('lab:limitation/outliers-remain', 'lab:addressedBy', 'lab:method/outlier-detection', '#lv3'),
 ('lab:method/knn-imputation', 'lab:prerequisiteOf', 'lab:method/outlier-detection', '#lv3'),
 ('lab:concept/masking', 'lab:partOf', 'lab:method/outlier-detection', '#lv3'),
 ('lab:method/outlier-detection', 'lab:prerequisiteOf', 'lab:method/outlier-treatment', '#lv3'),
 ('lab:method/outlier-detection', 'lab:hasLimitation', 'lab:limitation/duplicates-remain', '#lv3'),
 ('lab:limitation/duplicates-remain', 'lab:addressedBy', 'lab:concept/duplicates', '#lv4'),
 ('lab:method/outlier-detection', 'lab:prerequisiteOf', 'lab:concept/data-quality-6', '#lv4'),
 ('lab:concept/duplicates', 'lab:partOf', 'lab:concept/preprocessing', '#lv4'),
 ('lab:concept/integrity', 'lab:partOf', 'lab:concept/data-quality-6', '#lv4'),
 ('lab:concept/duplicates', 'lab:evaluatedBy', 'lab:concept/data-quality-6', '#lv4'),
 ('lab:method/data-profiling', 'lab:partOf', 'lab:concept/data-quality-6', '#sum'),
 ('lab:concept/data-quality-6', 'lab:hasLimitation', 'lab:limitation/meaning-unknown', '#lv4'),
 ('lab:limitation/meaning-unknown', 'lab:addressedBy', 'lab:method/eda', '#lv5'),
 ('lab:concept/data-quality-6', 'lab:prerequisiteOf', 'lab:method/eda', '#lv5'),
 ('lab:method/eda', 'lab:evaluatedBy', 'lab:metric/pearson', '#lv5'),
 ('lab:method/eda', 'lab:evaluatedBy', 'lab:metric/spearman', '#lv5'),
 ('lab:metric/pearson', 'lab:contrastsWith', 'lab:metric/spearman', '#lv5'),
 ('lab:method/eda', 'lab:hasLimitation', 'lab:limitation/bivariate-only', '#lv5'),
 ('lab:concept/preprocessing', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:metric/estimation-error', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/library', 'lab:analogyOf', 'lab:concept/integrity', '#lv4'),
 ('lab:analogy/vip-error', 'lab:analogyOf', 'lab:method/outlier-treatment', '#lv3'),
 ('lab:framework/smart', 'lab:demonstratedBy', 'lab:sim/w03-smart', '#lv1'),
 ('lab:concept/missing-mechanism', 'lab:demonstratedBy', 'lab:sim/w03-missing', '#lv2'),
 ('lab:method/outlier-detection', 'lab:demonstratedBy', 'lab:sim/w03-outlier', '#lv3'),
 ('lab:concept/data-quality-6', 'lab:demonstratedBy', 'lab:sim/w03-quality', '#lv4'),
 ('lab:method/eda', 'lab:demonstratedBy', 'lab:sim/w03-eda', '#lv5'),
 ('lab:claim/prep-80', 'lab:supports', 'lab:concept/preprocessing', '#hero', 'mid'), ('lab:claim/prep-80', 'lab:assertedIn', 'lab:work/ahn-dsb-w03', '#hero', 'mid'),
 ('lab:claim/smart-example', 'lab:supports', 'lab:framework/smart', '#lv1'), ('lab:claim/smart-example', 'lab:assertedIn', 'lab:work/ahn-dsb-w03', '#lv1'),
 ('lab:work/hyndman2018', 'lab:relatedTo', 'lab:metric/pearson', '#lv5'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w03', 'report', '비즈니스를위한데이터과학 강의 교안: 03. 데이터 분석을 위한 준비', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/prep-80', 'lab:claim/smart-example', 'lab:concept/missing-mechanism', 'lab:concept/data-quality-6', 'lab:framework/smart'], 'lab:work/ahn-dsb-w03',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/prep-80', 'loc': '2교시 1. 데이터 전처리 개요'}, {'claim': 'lab:claim/smart-example', 'loc': '1교시 14. 분석 목표의 설정'}]),
 R('hyndman2018fpp', 'book', 'Forecasting: principles and practice', [{'family': 'Hyndman', 'given': 'Rob J.'}, {'family': 'Athanasopoulos', 'given': 'George'}], 2018, 'figure', ['lab:metric/pearson'], 'lab:work/hyndman2018',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '교안의 인용 서지로 확인', '교안은 OTexts 한국어판 페이지를 인용',
   publisher='OTexts', URL='https://otexts.com/fppkr/graphics-scatterplots.html'),
]
