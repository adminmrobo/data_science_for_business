# 10주차 · 데이터 분석 모형: 회귀모형(2)
SLUG = 'dsb_w10_regression_2'
FILE = 'week10_regression_2.html'
TITLE = 'S자 곡선과 스무고개 — 회귀모형(2): 로지스틱·의사결정나무·특성공학·릿지·라쏘'
DESC = '비즈니스를 위한 데이터 과학 10주차 연구실 해설. 시그모이드로 확률을 만드는 로지스틱 회귀, 지니 불순도로 질문을 고르는 의사결정나무, PolynomialFeatures 특성공학과 릿지·라쏘 규제를 직접 움직여 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 S자 곡선이 그려진 칠판과 가지를 뻗은 질문 나무 앞에서 가위와 양념통을 든 표지'
COVER_PROP = '🌳'
SEARCH_PH = '예: 시그모이드, 지니, max_depth, PolynomialFeatures, 릿지, 라쏘'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 로지스틱'), ('#lv2', '② 지니'), ('#lv3', '③ 깊이'), ('#lv4', '④ 특성공학'), ('#lv5', '⑤ 릿지·라쏘'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week09_regression_1.html"><small>← 이전 · 9주차</small>숫자를 맞히는 선</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week11_time_series.html"><small>다음 · 11주차</small>시간이 기억하는 숫자 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:method/logistic-regression', 'lab:method/decision-tree', 'lab:concept/feature-engineering', 'lab:method/ridge-lasso']
KGPATH = ['method/logistic-regression', 'limitation/hard-to-explain', 'concept/gini-split', 'limitation/one-question', 'method/decision-tree', 'limitation/given-features', 'concept/feature-engineering', 'limitation/exploding-coef', 'method/ridge-lasso']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '교안 실습의 Fish Market 7종(159마리)·Wine 데이터 원 출처와 이용 조건 확인 — 이 페이지에는 싣지 않음']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 10. 데이터 분석 모형: 회귀모형(2). 인공지능융합학과. — 로지스틱 회귀(시그모이드, 가중치·편향, 비용함수, 공부시간-합격 예), 의사결정나무(스무고개, 지니 불순도, 정보 이득, 가지치기, max_depth, feature_importances_), Fish Market·Wine 실습, 교차 검증·GridSearchCV, 특성공학, PolynomialFeatures(3개·3차 19개, 5차 55개), 계수 크기 문제, 릿지·라쏘(양념 비유), RFE·SelectKBest·Pipeline, 도메인 특화 특성은 교안 본문을 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/1K_S_a63m7ClnRSz1Ys7LVec-O9ZMvzmr?usp=sharing" target="_blank" rel="noopener">Colab 1</a>, <a href="https://colab.research.google.com/drive/1NvJHKbG9Si5fOCgNQQ8k_uqXxVok5U1D?usp=sharing" target="_blank" rel="noopener">Colab 2</a>',
 '[2] Fish Market 데이터셋(Kaggle 공개 데이터). — 농어 56마리 길이·무게(9주차와 같음).',
 '[3] scikit-learn 문서: <a href="https://scikit-learn.org/stable/modules/linear_model.html" target="_blank" rel="noopener">Linear Models(Ridge, Lasso, LogisticRegression)</a>, <a href="https://scikit-learn.org/stable/modules/tree.html" target="_blank" rel="noopener">Decision Trees</a>, <a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html" target="_blank" rel="noopener">PolynomialFeatures</a>.',
 '[4] Li, F.-F., Johnson, J., Yeung, S. (2017). CS231n Lecture 6: Training Neural Networks I. Stanford University. — 교안의 활성함수 그림 출처.']
ILLUSTRATIVE = [
 '①칸 공부시간-합격 40명, ②③칸 "레드·화이트 와인 모양" 600병(잔당·알코올)은 교안의 예를 본떠 만든 예시 데이터입니다. 실제 와인 데이터가 아닙니다. ②③칸에는 라벨 잡음 약 8%를 일부러 넣었습니다.',
 '③칸의 의사결정나무는 브라우저에서 지니 불순도 기준 CART 방식으로 직접 만든 것이며, scikit-learn과 동점 처리 등에서 세부가 다를 수 있습니다.',
 '④⑤칸과 대결은 교안 농어 56마리, 9주차와 같은 random_state = 42 분할입니다. 다항 특성은 PolynomialFeatures(include_bias=False) 후 훈련 데이터 기준 표준화, 릿지·라쏘는 scikit-learn과 같은 목적함수로 계산했습니다.',
 '규제 없는 8차 회귀는 수치적으로 매우 불안정해, 가장 큰 계수의 값이 계산 방법에 따라 크게 달라집니다(이 페이지의 QR 분해 계산과 scikit-learn LinearRegression의 결과가 수백만~수천만 사이에서 다름). "계수가 폭발한다"는 결론은 같습니다.',
 '대결의 교차 검증은 훈련 42마리를 고정 시드로 섞어 5겹으로 나눈 것이며, 표준화 기준은 훈련 42마리 전체로 정했습니다(단순화).']

GL = {
 '로지스틱 회귀': ['로지스틱 회귀', '방법', '회귀식 z를 시그모이드로 0~1 확률로 바꿔 분류하는 모델. "분류의 옷을 입은 회귀".', 'lab:method/logistic-regression'],
 '시그모이드': ['시그모이드 함수', '수학', 'σ(z) = 1 ÷ (1 + e^(−z)). 어떤 z든 0과 1 사이로 바꾸는 S자 곡선.', None],
 '비용함수': ['비용함수(Cost Function)', '학습', '예측이 정답에서 벗어난 정도를 수치화한 함수. 로지스틱 회귀는 로그 손실을 최소화한다.', None],
 '편향': ['편향(Bias, w₀)', '학습', '모든 입력이 0일 때의 기본값. 결정 기준 전체를 옮긴다.', None],
 '의사결정나무': ['의사결정나무', '방법', '"특성 ≤ 기준값?" 질문을 이어 가며 잎에서 결론을 내는 모델. if-then 규칙으로 읽힌다.', 'lab:method/decision-tree'],
 '지니 불순도': ['지니 불순도', '지표', '1 − Σpᵢ². 노드 안에 클래스가 섞인 정도. 0이면 순수, 이진 분류 반반이면 0.5.', 'lab:concept/gini-split'],
 '정보 이득': ['정보 이득', '지표', '분할 전 불순도 − 분할 후 가중 평균 불순도. 클수록 좋은 질문.', None],
 '가지치기': ['가지치기(Pruning)', '최적화', '과적합을 막으려 불필요한 노드를 잘라 내는 일. max_depth 제한 등.', None],
 '특성공학': ['특성공학', '전처리', '원시 데이터에서 모델이 더 잘 배우도록 특성을 새로 만들거나 바꾸는 과정.', 'lab:concept/feature-engineering'],
 'PolynomialFeatures': ['PolynomialFeatures', 'scikit-learn', '특성의 거듭제곱과 서로의 곱을 자동으로 만든다. degree로 차수를 정한다.', None],
 '릿지': ['릿지(Ridge, L2)', '규제', '계수 제곱합에 벌점. 모든 특성을 쓰되 계수를 작게.', 'lab:method/ridge-lasso'],
 '라쏘': ['라쏘(Lasso, L1)', '규제', '계수 절댓값 합에 벌점. 덜 중요한 계수를 0으로 만들어 특성을 고른다.', None],
 '과적합': ['과적합', '개념', '훈련 데이터에 지나치게 맞춰 새 데이터에서 성능이 떨어지는 현상.', None],
 '교차 검증': ['교차 검증', '평가', '훈련 데이터를 K겹으로 나눠 번갈아 검증하며 하이퍼파라미터를 고르는 방법.', None],
}
CORE = ['로지스틱 회귀', '시그모이드', '비용함수', '편향', '의사결정나무', '지니 불순도', '정보 이득', '가지치기', '특성공학', 'PolynomialFeatures', '릿지', '라쏘', '교차 검증']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '로지스틱 회귀에서 시그모이드 함수의 역할로 가장 적절한 것은? (교안 연습문제 1)', 'o': ['입력 데이터의 노이즈 제거', 'z값을 0과 1 사이의 확률로 변환', '데이터 표준화', '학습 속도 향상'], 'a': 1, 'why': '선형 회귀식으로 계산된 z를 0~1 확률로 바꿉니다.', 'hint': '①칸 왼쪽 곡선.', 'assess': 'lab:method/logistic-regression'},
  {'id': 'q2', 'q': 'z = 0일 때 σ(z)의 값은?', 'o': ['0', '0.5', '1'], 'a': 1, 'why': '1 ÷ (1 + e⁰) = 1 ÷ 2 = 0.5. 그래서 z = 0이 결정 경계입니다.', 'hint': 'e⁰ = 1', 'calc': True, 'assess': 'lab:method/logistic-regression'}],
 'lv2': [
  {'id': 'q3', 'q': '레드 40병, 화이트 40병이 섞인 노드의 지니 불순도는?', 'o': ['0', '0.5', '1'], 'a': 1, 'why': '1 − (0.5² + 0.5²) = 0.5. 교안의 루트 노드 예.', 'hint': '1 − Σp²', 'calc': True, 'assess': 'lab:concept/gini-split'},
  {'id': 'q4', 'q': '의사결정나무가 분할 질문을 고르는 기준은?', 'o': ['특성 값이 가장 큰 것', '불순도를 가장 많이 줄이는 것', '무작위'], 'a': 1, 'why': '정보 이득(불순도 감소)이 가장 큰 특성·기준값을 고릅니다.', 'hint': '②칸 "최적 분할 찾기".', 'assess': 'lab:concept/gini-split'}],
 'lv3': [
  {'id': 'q5', 'q': 'max_depth를 제한 없이 키우면 일반적으로?', 'o': ['훈련·시험 정확도 모두 오른다', '훈련은 100%에 가까워지고 시험은 어느 순간 떨어진다', '둘 다 떨어진다'], 'a': 1, 'why': '노이즈까지 외우는 과적합입니다. 가지치기로 막습니다.', 'hint': '③칸 오른쪽 곡선.', 'assess': 'lab:method/decision-tree'},
  {'id': 'q6', 'q': '의사결정나무의 가장 큰 장점으로 교안이 꼽은 것은?', 'o': ['해석가능성', '외삽 능력', '항상 최고 정확도'], 'a': 0, 'why': '어떤 근거로 예측했는지 if-then 규칙으로 추적할 수 있습니다.', 'hint': '③칸 규칙 상자.', 'assess': 'lab:method/decision-tree'}],
 'lv4': [
  {'id': 'q7', 'q': '특성공학에 대한 설명으로 가장 적절한 것은? (교안 연습문제 3)', 'o': ['노이즈를 추가하는 과정', '새로운 특성을 생성하거나 기존 특성을 변환하는 과정', '불필요한 데이터 삭제', '시각화로 패턴 찾기'], 'a': 1, 'why': '원시 데이터를 모델이 더 잘 학습할 형태로 가공합니다.', 'hint': '④칸 일상 비유.', 'assess': 'lab:concept/feature-engineering'},
  {'id': 'q8', 'q': '특성 2개(길이, 너비)를 degree = 2로 늘리면 새 특성은 몇 개? (상수항 제외)', 'o': ['3개', '5개', '6개'], 'a': 1, 'why': '길이, 너비, 길이², 너비², 길이×너비 = 5개. C(4, 2) − 1 = 5.', 'hint': '④칸 계산기에서 2·2.', 'calc': True, 'assess': 'lab:concept/feature-engineering'}],
 'lv5': [
  {'id': 'q9', 'q': '중요하지 않은 특성의 계수를 정확히 0으로 만들어 특성을 고르는 규제는?', 'o': ['릿지', '라쏘', '표준화'], 'a': 1, 'why': '라쏘(L1)는 절댓값 벌점 때문에 계수를 0으로 보냅니다.', 'hint': '⑤칸 회색 막대.', 'assess': 'lab:method/ridge-lasso'},
  {'id': 'q10', 'q': 'α를 너무 크게 하면?', 'o': ['과적합이 심해진다', '모델이 너무 단순해져 훈련·시험 성능이 모두 떨어진다', '계수가 커진다'], 'a': 1, 'why': '규제가 너무 세면 과소적합입니다. α는 교차 검증으로 고릅니다.', 'hint': '⑤칸 α = 100.', 'assess': 'lab:method/ridge-lasso'},
  {'id': 'q11', 'q': 'Fish Market 전처리에서 표준화의 목적은? (교안 연습문제 2)', 'o': ['데이터 양을 늘리려고', '각 특성을 평균 0, 표준편차 1로 바꿔 동등한 중요도를 갖게 하려고', '결측값 제거', '시각화'], 'a': 1, 'why': '단위·범위가 다른 특성을 같은 눈금으로 맞춥니다(6주차 ⑤칸).', 'hint': '규제도 계수 크기를 비교하므로 표준화가 먼저입니다.', 'assess': 'lab:method/ridge-lasso'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('dataset/study-pass', 'Dataset', '공부시간-합격 예시 40명', 'study hours vs pass (synthetic)', '#lv1', level=1, family='basics'),
 N('dataset/wine-like', 'Dataset', '와인 모양 예시 600병', 'wine-like synthetic data', '#lv2', '잔당·알코올 두 특성, 레드·화이트. 설명용 예시.', level=1, family='basics'),
 N('dataset/perch-56', 'Dataset', '농어 56마리 길이·무게', 'Perch length/weight (56)', '#lv4', level=1, family='basics'),
 N('task/classification', 'Task', '분류', 'classification', '#why', level=1, family='basics'),
 N('task/regression', 'Task', '회귀', 'regression', '#lv4', level=1, family='basics'),
 N('method/logistic-regression', 'Method', '로지스틱 회귀', 'logistic regression', '#lv1', level=1, family='basics'),
 N('concept/sigmoid', 'Concept', '시그모이드 함수', 'sigmoid function', '#lv1', level=1, family='basics'),
 N('concept/cost-function', 'Concept', '비용함수(로그 손실)', 'cost function (log loss)', '#lv1', level=2, family='systems'),
 N('concept/gini-split', 'Concept', '지니 불순도와 분할', 'Gini impurity and splits', '#lv2', level=1, family='basics'),
 N('method/decision-tree', 'Method', '의사결정나무', 'decision tree', '#lv3', level=1, family='basics'),
 N('concept/pruning', 'Concept', '가지치기(max_depth)', 'pruning (max_depth)', '#lv3', level=2, family='evaluation'),
 N('concept/feature-engineering', 'Concept', '특성공학(PolynomialFeatures)', 'feature engineering', '#lv4', level=1, family='data'),
 N('method/ridge-lasso', 'Method', '릿지·라쏘 규제', 'ridge and lasso', '#lv5', level=2, family='basics'),
 N('method/cross-validation', 'Method', 'K겹 교차 검증', 'K-fold cross-validation', '#duel', level=1, family='evaluation'),
 N('limitation/hard-to-explain', 'Limitation', '규칙으로 설명하기 어렵다', 'hard to explain as rules', '#lv1'),
 N('limitation/one-question', 'Limitation', '질문 하나로는 부족하다', 'one split is not enough', '#lv2'),
 N('limitation/given-features', 'Limitation', '주어진 특성만 묻는다', 'only given features', '#lv3'),
 N('limitation/exploding-coef', 'Limitation', '특성을 늘리면 계수가 날뛴다', 'exploding coefficients', '#lv4'),
 N('claim/poly-count', 'Claim', '특성 3개를 3차로 늘리면 19개, 5차로 늘리면 55개', '3 features: 19 at degree 3, 55 at degree 5', '#lv4', source=[{'cite': '교안 10주차', 'loc': '3교시 2'}]),
 N('claim/gini-half', 'Claim', '40 : 40으로 섞인 노드의 지니 불순도는 0.5', 'Gini 0.5 for 40:40', '#lv2', source=[{'cite': '교안 10주차', 'loc': '1교시 4'}]),
 N('question/core', 'Question', '특성을 많이 만들수록 모델은 똑똑해질까?', 'Do more features make a smarter model?', '#hero'),
 N('question/duel', 'Question', '특성은 다 쓰되 계수에 고삐를 채울 것인가', 'all features with or without regularization?', '#duel'),
 N('analogy/twenty-q', 'Analogy', '스무고개 ↔ 의사결정나무', 'twenty questions ↔ decision tree', '#lv3', anchorType='D'),
 N('analogy/seasoning', 'Analogy', '양념 조절 ↔ 릿지·라쏘', 'seasoning ↔ ridge/lasso', '#lv5', anchorType='D'),
 N('analogy/marbles', 'Analogy', '색 구슬 상자의 칸막이 ↔ 지니 분할', 'marble box divider ↔ Gini split', '#lv2', anchorType='D'),
 N('sim/w10-logit', 'Simulation', 'S자 곡선 맞추기', 'fit the sigmoid', '#lv1'),
 N('sim/w10-gini', 'Simulation', '칸막이 옮기기', 'move the split', '#lv2'),
 N('sim/w10-depth', 'Simulation', '깊이별 결정 영역', 'regions by depth', '#lv3'),
 N('sim/w10-poly', 'Simulation', '특성 개수와 계수 크기', 'feature count and coefficients', '#lv4'),
 N('sim/w10-reg', 'Simulation', '릿지·라쏘 계수 막대', 'ridge/lasso coefficients', '#lv5'),
 N('work/ahn-dsb-w10', 'Work', '안상선, 비즈니스를위한데이터과학 교안 10주차', 'Ahn, DSB lecture notes week 10', '#footer'),
 N('work/sklearn-docs', 'Work', 'scikit-learn 문서', 'scikit-learn docs', '#footer'),
 N('work/cs231n', 'Work', 'CS231n Lecture 6 (2017)', 'CS231n Lecture 6 (2017)', '#footer'),
]

EDGES = [
 ('lab:method/logistic-regression', 'lab:solves', 'lab:task/classification', '#lv1'),
 ('lab:concept/sigmoid', 'lab:partOf', 'lab:method/logistic-regression', '#lv1'),
 ('lab:concept/cost-function', 'lab:partOf', 'lab:method/logistic-regression', '#lv1'),
 ('lab:method/logistic-regression', 'lab:evaluatedOn', 'lab:dataset/study-pass', '#lv1'),
 ('lab:method/logistic-regression', 'lab:hasLimitation', 'lab:limitation/hard-to-explain', '#lv1'),
 ('lab:limitation/hard-to-explain', 'lab:addressedBy', 'lab:method/decision-tree', '#lv2'),
 ('lab:concept/gini-split', 'lab:partOf', 'lab:method/decision-tree', '#lv2'),
 ('lab:concept/gini-split', 'lab:evaluatedOn', 'lab:dataset/wine-like', '#lv2'),
 ('lab:concept/gini-split', 'lab:hasLimitation', 'lab:limitation/one-question', '#lv2'),
 ('lab:limitation/one-question', 'lab:addressedBy', 'lab:concept/pruning', '#lv3'),
 ('lab:concept/pruning', 'lab:partOf', 'lab:method/decision-tree', '#lv3'),
 ('lab:method/decision-tree', 'lab:solves', 'lab:task/classification', '#lv3'),
 ('lab:method/decision-tree', 'lab:hasLimitation', 'lab:limitation/given-features', '#lv3'),
 ('lab:limitation/given-features', 'lab:addressedBy', 'lab:concept/feature-engineering', '#lv4'),
 ('lab:concept/feature-engineering', 'lab:evaluatedOn', 'lab:dataset/perch-56', '#lv4'),
 ('lab:concept/feature-engineering', 'lab:hasLimitation', 'lab:limitation/exploding-coef', '#lv4'),
 ('lab:limitation/exploding-coef', 'lab:addressedBy', 'lab:method/ridge-lasso', '#lv5'),
 ('lab:method/ridge-lasso', 'lab:solves', 'lab:task/regression', '#lv5'),
 ('lab:method/cross-validation', 'lab:prerequisiteOf', 'lab:method/ridge-lasso', '#duel'),
 ('lab:method/ridge-lasso', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:task/regression', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:analogy/twenty-q', 'lab:analogyOf', 'lab:method/decision-tree', '#lv3'),
 ('lab:analogy/seasoning', 'lab:analogyOf', 'lab:method/ridge-lasso', '#lv5'),
 ('lab:analogy/marbles', 'lab:analogyOf', 'lab:concept/gini-split', '#lv2'),
 ('lab:method/logistic-regression', 'lab:demonstratedBy', 'lab:sim/w10-logit', '#lv1'),
 ('lab:concept/gini-split', 'lab:demonstratedBy', 'lab:sim/w10-gini', '#lv2'),
 ('lab:method/decision-tree', 'lab:demonstratedBy', 'lab:sim/w10-depth', '#lv3'),
 ('lab:concept/feature-engineering', 'lab:demonstratedBy', 'lab:sim/w10-poly', '#lv4'),
 ('lab:method/ridge-lasso', 'lab:demonstratedBy', 'lab:sim/w10-reg', '#lv5'),
 ('lab:claim/poly-count', 'lab:supports', 'lab:concept/feature-engineering', '#lv4'), ('lab:claim/poly-count', 'lab:assertedIn', 'lab:work/ahn-dsb-w10', '#lv4'),
 ('lab:claim/gini-half', 'lab:supports', 'lab:concept/gini-split', '#lv2'), ('lab:claim/gini-half', 'lab:assertedIn', 'lab:work/ahn-dsb-w10', '#lv2'),
 ('lab:method/ridge-lasso', 'lab:relatedTo', 'lab:work/sklearn-docs', '#footer'),
 ('lab:concept/sigmoid', 'lab:relatedTo', 'lab:work/cs231n', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w10', 'report', '비즈니스를위한데이터과학 강의 교안: 10. 데이터 분석 모형: 회귀모형(2)', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/poly-count', 'lab:claim/gini-half', 'lab:method/logistic-regression', 'lab:method/decision-tree', 'lab:method/ridge-lasso'], 'lab:work/ahn-dsb-w10',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/poly-count', 'loc': '3교시 2. 특성 개수 증가에 따른 성능 변화'}, {'claim': 'lab:claim/gini-half', 'loc': '1교시 4. 노드 분할과 불순도'}]),
 R('sklearn_docs', 'webpage', 'scikit-learn User Guide: Linear Models, Decision Trees, PolynomialFeatures', [{'literal': 'scikit-learn developers'}], None, 'background',
   ['lab:method/ridge-lasso', 'lab:method/decision-tree'], 'lab:work/sklearn-docs',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서 URL 확인', '', URL='https://scikit-learn.org/stable/'),
 R('cs231n2017', 'webpage', 'CS231n Lecture 6: Training Neural Networks I', [{'family': 'Li', 'given': 'Fei-Fei'}, {'family': 'Johnson', 'given': 'Justin'}, {'family': 'Yeung', 'given': 'Serena'}], 2017, 'background',
   ['lab:concept/sigmoid'], 'lab:work/cs231n',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '교안 인용 서지 그대로', '', URL='https://cs231n.stanford.edu/slides/2017/cs231n_2017_lecture6.pdf'),
]
