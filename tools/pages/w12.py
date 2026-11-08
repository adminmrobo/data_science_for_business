# 12주차 · 효과적인 비즈니스 데이터 시각화
SLUG = 'dsb_w12_visualization'
FILE = 'week12_visualization.html'
TITLE = '숫자의 얼굴 — 효과적인 비즈니스 데이터 시각화'
DESC = '비즈니스를 위한 데이터 과학 12주차 연구실 해설. 평균·중앙값·최빈값, 분산·표준편차·변동계수, 왜도·첨도, 공분산·상관계수를 직접 움직여 보고, 데이터 모양과 목적에 맞는 차트를 고른다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 한쪽으로 길게 늘어진 막대그래프와 시소 위의 평균·중앙값 추를 바라보는 표지'
COVER_PROP = '📊'
SEARCH_PH = '예: 중앙값, 변동계수, 왜도, 상관계수, 박스 플롯, 히트맵'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 대표값'), ('#lv2', '② 분산도'), ('#lv3', '③ 왜도·첨도'), ('#lv4', '④ 상관'), ('#lv5', '⑤ 차트 선택'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week11_time_series.html"><small>← 이전 · 11주차</small>시간이 기억하는 숫자</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week13_bi_kpi.html"><small>다음 · 13주차</small>계기판을 설계하다 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:concept/central-tendency', 'lab:concept/dispersion', 'lab:concept/skewness-kurtosis', 'lab:concept/correlation', 'lab:method/chart-selection']
KGPATH = ['concept/central-tendency', 'limitation/no-spread', 'concept/dispersion', 'limitation/symmetric', 'concept/skewness-kurtosis', 'limitation/one-variable', 'concept/correlation', 'limitation/no-picture', 'method/chart-selection']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '교안의 B회사 변동계수 0.18 표기(15,000 ÷ 80,000 = 0.1875) 반올림 방식 확인']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 12. 효과적인 비즈니스 데이터 시각화. 인공지능융합학과. — 월급 예(200·300·350·400·1,000만 원), 평균·중앙값·최빈값, 분산·표준편차·변동계수(A·B 회사 연봉), 왜도·첨도 공식, 신용카드 사용 금액의 양의 편향, 공분산·상관계수와 해석 기준, 상관과 인과(아이스크림·익사, 해적·기온), 목적별 차트, 박스 플롯·캔들·히트맵·네트워크, Matplotlib·Seaborn 실습(자산 배분 40·30·15·10·5%), 대시보드 5초 규칙은 교안 본문을 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/1CqE-oK109zyiZqScpqwa2m6fWbyzNhNh?usp=sharing" target="_blank" rel="noopener">Colab</a>',
 '[2] 한국기술교육대학교. "핀테크데이터분석". 국민평생직업능력개발 STEP 온라인평생교육원. — 교안이 인용한 집중화 경향·상관관계·카드 금액 분포 자료의 출처.',
 '[3] Matplotlib(<a href="https://matplotlib.org/" target="_blank" rel="noopener">matplotlib.org</a>), Seaborn(<a href="https://seaborn.pydata.org/" target="_blank" rel="noopener">seaborn.pydata.org</a>) 공식 문서.']
ILLUSTRATIVE = [
 '월급 다섯 명, A·B 회사의 평균·표준편차, 자산 배분 비율은 교안의 예입니다. A·B 회사 직원 400명씩의 개별 연봉, 결제액 1,000건, 앱 사용-거래금액 120명, ⑤칸의 월별 매출·광고비·부서별 급여·기술주 상관은 설명용 예시 데이터입니다.',
 '①칸의 결제 방식 건수는 최빈값 설명을 위한 예시 숫자입니다.',
 '대결의 결제액은 로그정규분포에서 만든 예시(시드 51·52)이며, 실제 카드 데이터가 아닙니다.']

GL = {
 '평균': ['평균', '통계', '모든 값의 합 ÷ 개수. 이상치에 끌려간다.', 'lab:concept/central-tendency'],
 '중앙값': ['중앙값', '통계', '크기 순으로 줄 세운 가운데 값. 극단값의 영향을 거의 받지 않는다.', None],
 '최빈값': ['최빈값', '통계', '가장 자주 나타나는 값. 범주형 데이터의 대표값.', None],
 '분산': ['분산', '통계', '(값 − 평균)²의 평균. 단위가 제곱이 된다.', 'lab:concept/dispersion'],
 '표준편차': ['표준편차', '통계', '분산의 제곱근. 원래 단위로 흩어짐을 읽는다.', None],
 '변동계수': ['변동계수(CV)', '통계', '표준편차 ÷ 평균. 단위·규모가 다른 집단의 상대적 변동성 비교.', None],
 '왜도': ['왜도(Skewness)', '통계', '분포의 비대칭. 양수면 오른쪽 꼬리, 평균 > 중앙값.', 'lab:concept/skewness-kurtosis'],
 '첨도': ['첨도(Kurtosis)', '통계', '분포의 뾰족함과 꼬리 두께. 정규분포 = 3.', None],
 '공분산': ['공분산', '통계', '두 변수가 함께 변하는 정도. 방향은 알지만 단위에 따라 크기가 변한다.', 'lab:concept/correlation'],
 '상관계수': ['상관계수(피어슨 r)', '통계', '공분산 ÷ (두 표준편차의 곱). −1~+1, 단위와 무관.', None],
 '박스 플롯': ['박스 플롯', '시각화', '사분위수·중앙값·이상치로 분포를 요약. 그룹 비교에 강하다.', 'lab:method/chart-selection'],
 '히트맵': ['히트맵', '시각화', '값을 색 강도로 표현한 2차원 표. 상관 행렬에 쓴다.', None],
 '트리맵': ['트리맵', '시각화', '계층·다수 항목의 비중을 중첩 직사각형 크기로 표현.', None],
}
CORE = ['평균', '중앙값', '최빈값', '분산', '표준편차', '변동계수', '왜도', '첨도', '공분산', '상관계수', '박스 플롯', '히트맵', '트리맵']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '집중화 경향을 나타내는 지표가 아닌 것은? (교안 연습문제 1)', 'o': ['평균', '중앙값', '최빈값', '분산'], 'a': 3, 'why': '분산은 흩어짐(분산도) 지표입니다.', 'hint': '②칸 제목.', 'assess': 'lab:concept/central-tendency'},
  {'id': 'q2', 'q': '월급 200·300·350·400·1,000만 원의 중앙값은?', 'o': ['350만 원', '450만 원', '400만 원'], 'a': 0, 'why': '정렬한 다섯 값의 가운데. 평균은 450만 원.', 'hint': '①칸 초록 선.', 'calc': True, 'assess': 'lab:concept/central-tendency'}],
 'lv2': [
  {'id': 'q3', 'q': '평균 80, 표준편차 16인 집단의 변동계수는?', 'o': ['0.2', '5', '64'], 'a': 0, 'why': '16 ÷ 80 = 0.2.', 'hint': 'σ ÷ μ', 'calc': True, 'assess': 'lab:concept/dispersion'},
  {'id': 'q4', 'q': '연봉 단위를 원에서 만 원으로 바꿀 때 변하지 않는 것은?', 'o': ['분산', '표준편차', '변동계수'], 'a': 2, 'why': '분자·분모가 같은 비율로 줄어 비율은 그대로입니다.', 'hint': '②칸 단위 버튼.', 'assess': 'lab:concept/dispersion'}],
 'lv3': [
  {'id': 'q5', 'q': '평균이 중앙값보다 크게 나왔다. 분포의 모양은?', 'o': ['왼쪽 꼬리(음의 왜도)', '오른쪽 꼬리(양의 왜도)', '완전 대칭'], 'a': 1, 'why': '소수의 큰 값이 평균을 오른쪽으로 끌어당깁니다. 소득·카드 결제액의 전형.', 'hint': '③칸 빨강·초록 선.', 'assess': 'lab:concept/skewness-kurtosis'},
  {'id': 'q6', 'q': '오른쪽 꼬리가 긴 결제액을 모델에 넣기 전 흔히 하는 변환은?', 'o': ['제곱', '로그 변환', '부호 바꾸기'], 'a': 1, 'why': '로그는 큰 값을 접어 편향을 낮춥니다(교안).', 'hint': '③칸 "로그" 버튼.', 'assess': 'lab:concept/skewness-kurtosis'}],
 'lv4': [
  {'id': 'q7', 'q': '두 수치형 변수 간의 관계를 나타내기 가장 적합한 시각화는? (교안 연습문제 2)', 'o': ['막대 그래프', '히트맵', '산점도', '트리맵'], 'a': 2, 'why': '산점도는 두 수치 변수의 관계 방향·강도와 이상치를 보여 줍니다.', 'hint': '④칸 그림.', 'assess': 'lab:concept/correlation'},
  {'id': 'q8', 'q': '상관계수 r = 0.85의 교안 해석은?', 'o': ['약한 관계', '중간 관계', '강한 양의 관계'], 'a': 2, 'why': '|r| ≥ 0.7이면 강한 관계. 인과관계는 별개입니다.', 'hint': '④칸 부제.', 'assess': 'lab:concept/correlation'}],
 'lv5': [
  {'id': 'q9', 'q': '파이썬의 기본 시각화 라이브러리로, 세밀한 제어가 가능한 것은? (교안 연습문제 3)', 'o': ['NumPy', 'Pandas', 'Matplotlib', 'Scikit-learn'], 'a': 2, 'why': 'Matplotlib이 기본, Seaborn은 그 위의 통계 시각화 라이브러리입니다.', 'hint': '큰 그림 3교시.', 'assess': 'lab:method/chart-selection'},
  {'id': 'q10', 'q': '부서 3곳의 급여 분포와 이상치를 함께 비교하려면?', 'o': ['파이 차트', '박스 플롯', '선 그래프'], 'a': 1, 'why': '박스 플롯은 여러 그룹의 분포·중앙값·이상치를 한 번에 비교합니다.', 'hint': '⑤칸 부서별 급여.', 'assess': 'lab:method/chart-selection'},
  {'id': 'q11', 'q': '항목이 30개이고 계층이 있는 매출 구성은?', 'o': ['파이 차트', '트리맵', '캔들스틱'], 'a': 1, 'why': '파이는 5개 이하, 많거나 계층이 있으면 트리맵(교안).', 'hint': '⑤칸 원칙.', 'assess': 'lab:method/chart-selection'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('dataset/salary-five', 'Dataset', '월급 다섯 명(교안 예)', 'five salaries (lecture example)', '#lv1', level=1, family='basics'),
 N('dataset/card-spend', 'Dataset', '카드 결제액 예시 1,000건', 'synthetic card spending', '#lv3', '로그정규분포로 만든 설명용 결제액.', level=1, family='basics'),
 N('task/data-description', 'Task', '데이터 특성 요약과 전달', 'describing and communicating data', '#why', level=1, family='basics'),
 N('concept/central-tendency', 'Concept', '집중화 경향(평균·중앙값·최빈값)', 'central tendency', '#lv1', level=1, family='basics'),
 N('concept/dispersion', 'Concept', '분산도(분산·표준편차·변동계수)', 'dispersion', '#lv2', level=1, family='basics'),
 N('concept/skewness-kurtosis', 'Concept', '왜도·첨도', 'skewness and kurtosis', '#lv3', level=2, family='basics'),
 N('concept/correlation', 'Concept', '공분산·상관계수', 'covariance and correlation', '#lv4', level=1, family='basics'),
 N('method/chart-selection', 'Method', '목적별 차트 선택', 'chart selection by purpose', '#lv5', level=1, family='data'),
 N('method/log-transform', 'Method', '로그 변환', 'log transform', '#lv3', '오른쪽 꼬리를 접어 편향을 낮춘다.', level=1, family='data'),
 N('metric/mae', 'Metric', 'MAE(평균 절대 오차)', 'mean absolute error', '#duel', level=1, family='evaluation'),
 N('limitation/no-spread', 'Limitation', '흩어짐을 모른다', 'spread unknown', '#lv1'),
 N('limitation/symmetric', 'Limitation', '대칭을 가정한 요약', 'assumes symmetry', '#lv2'),
 N('limitation/one-variable', 'Limitation', '변수 하나만 본다', 'one variable only', '#lv3'),
 N('limitation/no-picture', 'Limitation', '아직 그림이 없다', 'no picture yet', '#lv4'),
 N('claim/salary-mean-median', 'Claim', '월급 200·300·350·400·1,000의 평균 450, 중앙값 350', 'mean 450, median 350', '#lv1', source=[{'cite': '교안 12주차', 'loc': '1교시 1'}]),
 N('claim/corr-scale', 'Claim', '상관계수 0.7 이상 강함, 0.3~0.7 중간, 0.3 미만 약함', 'correlation interpretation scale', '#lv4', source=[{'cite': '교안 12주차', 'loc': '1교시 4'}]),
 N('question/core', 'Question', '평균 월급은 직원의 얼굴일까?', 'Is the mean salary a fair face?', '#hero'),
 N('question/duel', 'Question', '전형적인 고객 한 명: 평균이냐 중앙값이냐', 'mean or median for a typical customer?', '#duel'),
 N('analogy/dancers', 'Analogy', '함께 춤추는 두 사람 ↔ 상관관계', 'dancing pair ↔ correlation', '#lv4', anchorType='D'),
 N('analogy/bowls', 'Analogy', '음식에 맞는 그릇 ↔ 데이터에 맞는 차트', 'bowls for dishes ↔ charts for data', '#lv5', anchorType='D'),
 N('sim/w12-center', 'Simulation', '다섯 번째 월급 바꾸기', 'change the fifth salary', '#lv1'),
 N('sim/w12-cv', 'Simulation', '단위 바꾸기와 변동계수', 'units and CV', '#lv2'),
 N('sim/w12-skew', 'Simulation', '꼬리 길이와 로그', 'tail length and log', '#lv3'),
 N('sim/w12-corr', 'Simulation', '공분산·상관과 큰손 1명', 'covariance, r and an outlier', '#lv4'),
 N('sim/w12-chart', 'Simulation', '데이터 × 차트 짝짓기', 'data × chart matcher', '#lv5'),
 N('work/ahn-dsb-w12', 'Work', '안상선, 비즈니스를위한데이터과학 교안 12주차', 'Ahn, DSB lecture notes week 12', '#footer'),
 N('work/step-fintech', 'Work', '한국기술교육대학교, 핀테크데이터분석(STEP)', 'KoreaTech STEP Fintech Data Analysis', '#footer'),
 N('work/matplotlib-seaborn', 'Work', 'Matplotlib · Seaborn 공식 문서', 'Matplotlib and Seaborn docs', '#footer'),
]

EDGES = [
 ('lab:task/data-description', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:concept/central-tendency', 'lab:solves', 'lab:task/data-description', '#lv1'),
 ('lab:concept/central-tendency', 'lab:evaluatedOn', 'lab:dataset/salary-five', '#lv1'),
 ('lab:concept/central-tendency', 'lab:hasLimitation', 'lab:limitation/no-spread', '#lv1'),
 ('lab:limitation/no-spread', 'lab:addressedBy', 'lab:concept/dispersion', '#lv2'),
 ('lab:concept/dispersion', 'lab:hasLimitation', 'lab:limitation/symmetric', '#lv2'),
 ('lab:limitation/symmetric', 'lab:addressedBy', 'lab:concept/skewness-kurtosis', '#lv3'),
 ('lab:concept/skewness-kurtosis', 'lab:evaluatedOn', 'lab:dataset/card-spend', '#lv3'),
 ('lab:method/log-transform', 'lab:addresses', 'lab:concept/skewness-kurtosis', '#lv3'),
 ('lab:concept/skewness-kurtosis', 'lab:hasLimitation', 'lab:limitation/one-variable', '#lv3'),
 ('lab:limitation/one-variable', 'lab:addressedBy', 'lab:concept/correlation', '#lv4'),
 ('lab:concept/correlation', 'lab:hasLimitation', 'lab:limitation/no-picture', '#lv4'),
 ('lab:limitation/no-picture', 'lab:addressedBy', 'lab:method/chart-selection', '#lv5'),
 ('lab:method/chart-selection', 'lab:solves', 'lab:task/data-description', '#lv5'),
 ('lab:concept/central-tendency', 'lab:evaluatedBy', 'lab:metric/mae', '#duel'),
 ('lab:metric/mae', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/dancers', 'lab:analogyOf', 'lab:concept/correlation', '#lv4'),
 ('lab:analogy/bowls', 'lab:analogyOf', 'lab:method/chart-selection', '#lv5'),
 ('lab:concept/central-tendency', 'lab:demonstratedBy', 'lab:sim/w12-center', '#lv1'),
 ('lab:concept/dispersion', 'lab:demonstratedBy', 'lab:sim/w12-cv', '#lv2'),
 ('lab:concept/skewness-kurtosis', 'lab:demonstratedBy', 'lab:sim/w12-skew', '#lv3'),
 ('lab:concept/correlation', 'lab:demonstratedBy', 'lab:sim/w12-corr', '#lv4'),
 ('lab:method/chart-selection', 'lab:demonstratedBy', 'lab:sim/w12-chart', '#lv5'),
 ('lab:claim/salary-mean-median', 'lab:supports', 'lab:concept/central-tendency', '#lv1'), ('lab:claim/salary-mean-median', 'lab:assertedIn', 'lab:work/ahn-dsb-w12', '#lv1'),
 ('lab:claim/corr-scale', 'lab:supports', 'lab:concept/correlation', '#lv4'), ('lab:claim/corr-scale', 'lab:assertedIn', 'lab:work/ahn-dsb-w12', '#lv4'),
 ('lab:concept/correlation', 'lab:relatedTo', 'lab:work/step-fintech', '#footer'),
 ('lab:method/chart-selection', 'lab:relatedTo', 'lab:work/matplotlib-seaborn', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w12', 'report', '비즈니스를위한데이터과학 강의 교안: 12. 효과적인 비즈니스 데이터 시각화', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/salary-mean-median', 'lab:claim/corr-scale', 'lab:concept/central-tendency', 'lab:concept/dispersion', 'lab:method/chart-selection'], 'lab:work/ahn-dsb-w12',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/salary-mean-median', 'loc': '1교시 1. 평균·중앙값'}, {'claim': 'lab:claim/corr-scale', 'loc': '1교시 4. 상관계수'}]),
 R('step_fintech', 'webpage', '핀테크데이터분석', [{'literal': '한국기술교육대학교'}], None, 'background', ['lab:concept/correlation'], 'lab:work/step-fintech',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '교안 인용 서지 그대로', '', publisher='STEP 온라인평생교육원', URL='https://www.step.or.kr'),
 R('mpl_sns', 'webpage', 'Matplotlib / Seaborn documentation', [{'literal': 'Matplotlib and Seaborn developers'}], None, 'background', ['lab:method/chart-selection'], 'lab:work/matplotlib-seaborn',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서 URL 확인', '', URL='https://matplotlib.org/'),
]
