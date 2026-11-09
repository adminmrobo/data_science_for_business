# 9주차 · 데이터 분석 모형: 회귀모형(1)
SLUG = 'dsb_w09_regression_1'
FILE = 'week09_regression_1.html'
TITLE = '숫자를 맞히는 선 — 회귀모형(1): KNN·선형·다항 회귀와 평가 지표'
DESC = '비즈니스를 위한 데이터 과학 9주차 연구실 해설. 교안의 농어 56마리로 KNN 회귀, 최소제곱 직선, 2차 곡선을 그려 보고 MSE·RMSE·MAE·R²·수정 R²를 직접 계산한다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 양궁 과녁 앞에서 농어를 저울에 올리고 칠판의 점들 위로 곡선을 긋는 표지'
COVER_PROP = '🎯'
SEARCH_PH = '예: KNN 회귀, 최소제곱, 다항 회귀, RMSE, MAE, R²'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① KNN 회귀'), ('#lv2', '② 선형'), ('#lv3', '③ 다항'), ('#lv4', '④ 오차 지표'), ('#lv5', '⑤ R²'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week07_model_evaluation.html"><small>← 이전 · 7주차</small>정확도 95%의 함정</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week10_regression_2.html"><small>다음 · 10주차</small>S자 곡선과 스무고개 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:method/knn-regression', 'lab:method/linear-regression', 'lab:method/polynomial-regression', 'lab:metric/mse-rmse-mae', 'lab:metric/r2']
KGPATH = ['method/knn-regression', 'limitation/no-extrapolation', 'method/linear-regression', 'limitation/straight-only', 'method/polynomial-regression', 'limitation/no-error-size', 'metric/mse-rmse-mae', 'limitation/scale-free', 'metric/r2']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 09. 데이터 분석 모형: 회귀모형(1). 인공지능융합학과. — 회귀와 분류의 차이, 양궁 과녁 비유, KNN·선형·비선형(다항·지수·로그) 회귀, 최소제곱법, reshape(−1, 1), 농어 56마리 길이·무게 데이터와 KNN 점수(훈련 0.9699, 시험 0.9928), MSE·RMSE·MAE, SST·SSR·SSE, R²·수정 R² 해석 기준, 배터리 수명·보험료·대출 심사 사례는 교안 본문과 실습 코드를 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/1--zDpgF4sd9_I87Pj4JxsSMRkTxXE8rB?usp=sharing" target="_blank" rel="noopener">Colab</a>',
 '[2] Fish Market 데이터셋(Kaggle 공개 데이터). — 농어(Perch) 56마리 길이·무게. 원 출처와 이용 조건은 확인 필요.',
 '[3] scikit-learn 문서: <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html" target="_blank" rel="noopener">train_test_split</a>, <a href="https://scikit-learn.org/stable/modules/linear_model.html" target="_blank" rel="noopener">Linear Models</a>, <a href="https://scikit-learn.org/stable/modules/neighbors.html#regression" target="_blank" rel="noopener">Nearest Neighbors Regression</a>.']
ILLUSTRATIVE = [
 '훈련·시험 분할은 scikit-learn train_test_split(random_state=42)이 고르는 시험 인덱스 14개를 그대로 옮겨 왔습니다. KNN 점수는 교안과 같습니다. 선형·다항 점수는 교안 그림의 값을 이 분할로 다시 계산한 값으로 바꿨습니다.',
 '④칸의 "+600g 오기"는 지표의 민감도를 보이려고 일부러 넣은 값입니다.',
 '⑤칸의 난수 변수 12개는 무게와 무관하게 만든 값입니다(시드 13).',
 '대결의 큰 농어 10마리(45~48cm)는 교안 데이터에 맞춘 거듭제곱 관계에 잡음을 더해 만든 설명용 예시값입니다.']

GL = {
 '회귀': ['회귀(Regression)', '문제', '입력 변수로 연속적인 수치(무게, 매출, 가격)를 예측하는 모델.', 'lab:task/regression'],
 'KNN 회귀': ['KNN 회귀', '방법', '가까운 K개 이웃의 목표값 평균으로 예측. KNeighborsRegressor.', 'lab:method/knn-regression'],
 '최소제곱법': ['최소제곱법', '방법', '실제 값과 예측 값 차이(잔차)의 제곱합이 최소가 되는 계수를 찾는 방법.', 'lab:method/linear-regression'],
 '잔차': ['잔차(Residual)', '통계', '실제 값 − 예측 값. 그래프에서 점과 회귀선 사이의 세로 거리.', None],
 '다항 회귀': ['다항 회귀', '방법', 'x², x³ 같은 항을 새 특성으로 더해 곡선을 맞추는 회귀.', 'lab:method/polynomial-regression'],
 'reshape': ['reshape(−1, 1)', '파이썬', '1차원 배열을 열 하나짜리 2차원 배열로 바꾼다. −1은 행 수 자동 계산.', None],
 'MSE': ['MSE(평균제곱오차)', '지표', '오차 제곱의 평균. 큰 오차를 크게 벌해 이상치에 민감.', 'lab:metric/mse-rmse-mae'],
 'RMSE': ['RMSE(평균제곱근오차)', '지표', 'MSE의 제곱근. 원래 단위로 읽힌다.', None],
 'MAE': ['MAE(평균절대오차)', '지표', '오차 절댓값의 평균. 이상치에 덜 민감.', None],
 'R²': ['R²(결정계수)', '지표', 'SSR ÷ SST = 1 − SSE ÷ SST. 전체 변동 중 모델이 설명한 비율.', 'lab:metric/r2'],
 '수정 R²': ['수정 R²(Adjusted R²)', '지표', '1 − (1 − R²)(n − 1) ÷ (n − k − 1). 변수 개수에 벌점을 준 결정계수.', None],
 'SST': ['SST·SSR·SSE', '통계', '총 제곱합 = 회귀 제곱합 + 오차 제곱합.', None],
 '과적합': ['과적합', '개념', '훈련 데이터에 지나치게 맞춰 새 데이터에서 예측력이 떨어지는 현상.', None],
}
CORE = ['회귀', 'KNN 회귀', '최소제곱법', '잔차', '다항 회귀', 'MSE', 'RMSE', 'MAE', 'R²', '수정 R²', 'SST', '과적합']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '회귀 모델이 분류 모델과 구별되는 가장 주요한 특징은? (교안 연습문제 1)', 'o': ['범주형 결과를 예측한다', '연속적인 수치 값을 예측한다', '확률값만 출력한다', '이산적인 클래스를 분류한다'], 'a': 1, 'why': '회귀는 온도·가격·무게 같은 연속 수치를 예측합니다.', 'hint': '큰 그림 섹션.', 'assess': 'lab:task/regression'},
  {'id': 'q2', 'q': 'K = 3에서 가장 가까운 이웃 세 마리의 무게가 100g, 120g, 140g이면 KNN 회귀의 예측은?', 'o': ['100g', '120g', '140g'], 'a': 1, 'why': '이웃 값의 평균 (100 + 120 + 140) ÷ 3 = 120g.', 'hint': '분류는 다수결, 회귀는 평균.', 'calc': True, 'assess': 'lab:method/knn-regression'}],
 'lv2': [
  {'id': 'q3', 'q': '최소제곱법이 최소로 만드는 것은?', 'o': ['잔차의 합', '잔차 제곱의 합', '잔차 절댓값의 최댓값'], 'a': 1, 'why': '잔차를 그냥 더하면 부호가 상쇄됩니다. 제곱해서 더한 값을 최소화합니다.', 'hint': '②칸의 사각형 넓이.', 'assess': 'lab:method/linear-regression'},
  {'id': 'q4', 'q': '무게 = 39 × 길이 − 709 에서 길이가 2cm 늘면 예측 무게는?', 'o': ['39g 증가', '78g 증가', '709g 감소'], 'a': 1, 'why': '기울기 39 × 2 = 78g.', 'hint': '계수 = 1단위당 변화.', 'calc': True, 'assess': 'lab:method/linear-regression'}],
 'lv3': [
  {'id': 'q5', 'q': '다항 회귀의 차수를 계속 올리면 일반적으로?', 'o': ['훈련·시험 R² 모두 계속 오른다', '훈련 R²는 오르지만 시험 R²는 어느 순간 떨어진다', '둘 다 떨어진다'], 'a': 1, 'why': '복잡한 곡선이 훈련 점에 과적합되어 새 데이터에서 빗나갑니다.', 'hint': '③칸 차수 6 이상.', 'assess': 'lab:method/polynomial-regression'},
  {'id': 'q6', 'q': '교안의 2차 회귀에서 입력 데이터를 만드는 방법은?', 'o': ['길이를 표준화한다', '길이² 열을 길이 옆에 붙인다', '무게의 로그를 취한다'], 'a': 1, 'why': 'np.column_stack((train_input ** 2, train_input))로 두 열을 만들어 LinearRegression에 넣습니다.', 'hint': '③칸 코드 태그.', 'assess': 'lab:method/polynomial-regression'}],
 'lv4': [
  {'id': 'q7', 'q': 'RMSE가 MSE보다 선호되는 이유는? (교안 연습문제 2)', 'o': ['계산이 더 간단하다', '원본 데이터와 같은 단위를 가진다', '항상 더 작은 값을 가진다', '이상치에 덜 민감하다'], 'a': 1, 'why': '제곱근을 취해 g 같은 원래 단위로 읽힙니다.', 'hint': '④칸 KPI 단위.', 'assess': 'lab:metric/mse-rmse-mae'},
  {'id': 'q8', 'q': '오차가 +3, −3, +4, −4일 때 MAE는?', 'o': ['0', '3.5', '12.5'], 'a': 1, 'why': '(3 + 3 + 4 + 4) ÷ 4 = 3.5. 그냥 평균하면 0이 됩니다.', 'hint': '절댓값의 평균.', 'calc': True, 'assess': 'lab:metric/mse-rmse-mae'}],
 'lv5': [
  {'id': 'q9', 'q': 'SST = 1,000, SSE = 50이면 R²는?', 'o': ['0.05', '0.95', '50'], 'a': 1, 'why': '1 − 50 ÷ 1,000 = 0.95. 교안의 "전체 1,000 중 950을 설명" 예.', 'hint': 'R² = 1 − SSE ÷ SST', 'calc': True, 'assess': 'lab:metric/r2'},
  {'id': 'q10', 'q': '쓸모없는 변수를 더하면 R²와 수정 R²는?', 'o': ['둘 다 오른다', 'R²는 줄지 않고, 수정 R²는 내려갈 수 있다', '둘 다 반드시 내려간다'], 'a': 1, 'why': '수정 R²는 변수 개수 k에 벌점을 줍니다.', 'hint': '⑤칸 슬라이더.', 'assess': 'lab:metric/r2'},
  {'id': 'q11', 'q': '보험료 산정에서 회귀 모델 도입의 주요 목적은? (교안 연습문제 3)', 'o': ['모든 고객에게 동일한 보험료', '개인별 위험도에 따른 차별화된 보험료', '보험료를 최대한 높게', '가입 절차 복잡화'], 'a': 1, 'why': '개인 특성과 위험도를 분석해 공정하고 차별화된 보험료를 책정합니다.', 'hint': '⑤칸 현장에 옮기면.', 'assess': 'lab:task/regression'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('dataset/perch-56', 'Dataset', '농어 56마리 길이·무게', 'Perch length/weight (56)', '#lv1', '교안 9주차 실습 데이터. 훈련 42 · 시험 14.', level=1, family='basics'),
 N('task/regression', 'Task', '회귀(연속 수치 예측)', 'regression', '#why', level=1, family='basics'),
 N('method/knn-regression', 'Method', 'KNN 회귀', 'KNN regression', '#lv1', level=1, family='basics'),
 N('method/linear-regression', 'Method', '선형 회귀(최소제곱)', 'linear regression (least squares)', '#lv2', level=1, family='basics'),
 N('method/polynomial-regression', 'Method', '다항(비선형) 회귀', 'polynomial regression', '#lv3', level=1, family='basics'),
 N('metric/mse-rmse-mae', 'Metric', 'MSE·RMSE·MAE', 'MSE, RMSE, MAE', '#lv4', level=1, family='evaluation'),
 N('metric/r2', 'Metric', 'R²와 수정 R²', 'R² and adjusted R²', '#lv5', level=1, family='evaluation'),
 N('concept/sst-decomposition', 'Concept', 'SST = SSR + SSE', 'variance decomposition', '#lv5', level=2, family='evaluation'),
 N('concept/extrapolation', 'Concept', '훈련 범위 밖 예측(외삽)', 'extrapolation', '#duel', '훈련 데이터 범위를 벗어난 입력에 대한 예측.', level=2, family='evaluation'),
 N('limitation/no-extrapolation', 'Limitation', '범위 밖을 예측하지 못하고 설명도 없다', 'no extrapolation, no explanation', '#lv1'),
 N('limitation/straight-only', 'Limitation', '직선만 그린다', 'straight lines only', '#lv2'),
 N('limitation/no-error-size', 'Limitation', '오차의 크기를 모른다', 'error size unknown', '#lv3'),
 N('limitation/scale-free', 'Limitation', '규모를 모르면 해석할 수 없다', 'no scale reference', '#lv4'),
 N('claim/knn-r2', 'Claim', 'KNN 회귀(K = 5)의 시험 R² 0.9928, 훈련 R² 0.9699', 'KNN test R² 0.9928', '#lv1', source=[{'cite': '교안 9주차', 'loc': '1교시 5'}]),
 N('claim/r2-scale', 'Claim', 'R² 0.7 이상 높음, 0.5~0.7 중간, 0.3 이하 낮음', 'R² interpretation scale', '#lv5', source=[{'cite': '교안 9주차', 'loc': '2교시 3'}]),
 N('question/core', 'Question', '길이만으로 농어 무게를 몇 g까지 맞힐 수 있을까?', 'How precisely can length predict weight?', '#hero'),
 N('question/duel', 'Question', '이웃 평균이냐, 곡선이냐', 'neighbors or curve?', '#duel'),
 N('analogy/archery', 'Analogy', '양궁 과녁 ↔ 회귀 오차', 'archery target ↔ regression error', '#lv4', anchorType='D'),
 N('analogy/puzzle', 'Analogy', '퍼즐 조각 맞추기 ↔ R²', 'puzzle pieces ↔ R²', '#lv5', anchorType='D'),
 N('analogy/tug', 'Analogy', '줄다리기의 극단적 한 명 ↔ 최소제곱의 이상치 민감성', 'tug-of-war ↔ outlier sensitivity', '#lv2', anchorType='D'),
 N('sim/w09-knn', 'Simulation', 'KNN 회귀 계단선', 'KNN step curve', '#lv1'),
 N('sim/w09-ls', 'Simulation', '손으로 맞추는 직선과 잔차²', 'hand-fit line', '#lv2'),
 N('sim/w09-poly', 'Simulation', '차수별 R²', 'R² by degree', '#lv3'),
 N('sim/w09-err', 'Simulation', '오차 막대와 오기', 'residual bars', '#lv4'),
 N('sim/w09-adj', 'Simulation', '난수 변수와 수정 R²', 'noise features and adj. R²', '#lv5'),
 N('work/ahn-dsb-w09', 'Work', '안상선, 비즈니스를위한데이터과학 교안 9주차', 'Ahn, DSB lecture notes week 9', '#footer'),
 N('work/fish-market', 'Work', 'Fish Market 데이터셋(Kaggle)', 'Fish Market dataset (Kaggle)', '#footer'),
 N('work/sklearn-docs', 'Work', 'scikit-learn 문서', 'scikit-learn docs', '#footer'),
]

EDGES = [
 ('lab:task/regression', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:method/knn-regression', 'lab:solves', 'lab:task/regression', '#lv1'),
 ('lab:method/knn-regression', 'lab:evaluatedOn', 'lab:dataset/perch-56', '#lv1'),
 ('lab:method/knn-regression', 'lab:hasLimitation', 'lab:limitation/no-extrapolation', '#lv1'),
 ('lab:limitation/no-extrapolation', 'lab:addressedBy', 'lab:method/linear-regression', '#lv2'),
 ('lab:method/linear-regression', 'lab:solves', 'lab:task/regression', '#lv2'),
 ('lab:method/linear-regression', 'lab:hasLimitation', 'lab:limitation/straight-only', '#lv2'),
 ('lab:limitation/straight-only', 'lab:addressedBy', 'lab:method/polynomial-regression', '#lv3'),
 ('lab:method/linear-regression', 'lab:prerequisiteOf', 'lab:method/polynomial-regression', '#lv3'),
 ('lab:method/polynomial-regression', 'lab:evaluatedOn', 'lab:dataset/perch-56', '#lv3'),
 ('lab:method/polynomial-regression', 'lab:hasLimitation', 'lab:limitation/no-error-size', '#lv3'),
 ('lab:limitation/no-error-size', 'lab:addressedBy', 'lab:metric/mse-rmse-mae', '#lv4'),
 ('lab:metric/mse-rmse-mae', 'lab:hasLimitation', 'lab:limitation/scale-free', '#lv4'),
 ('lab:limitation/scale-free', 'lab:addressedBy', 'lab:metric/r2', '#lv5'),
 ('lab:concept/sst-decomposition', 'lab:partOf', 'lab:metric/r2', '#lv5'),
 ('lab:method/polynomial-regression', 'lab:evaluatedBy', 'lab:metric/r2', '#lv3'),
 ('lab:method/knn-regression', 'lab:evaluatedBy', 'lab:metric/mse-rmse-mae', '#duel'),
 ('lab:concept/extrapolation', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:limitation/no-extrapolation', 'lab:partOf', 'lab:concept/extrapolation', '#duel'),
 ('lab:analogy/archery', 'lab:analogyOf', 'lab:metric/mse-rmse-mae', '#lv4'),
 ('lab:analogy/puzzle', 'lab:analogyOf', 'lab:metric/r2', '#lv5'),
 ('lab:analogy/tug', 'lab:analogyOf', 'lab:method/linear-regression', '#lv2'),
 ('lab:method/knn-regression', 'lab:demonstratedBy', 'lab:sim/w09-knn', '#lv1'),
 ('lab:method/linear-regression', 'lab:demonstratedBy', 'lab:sim/w09-ls', '#lv2'),
 ('lab:method/polynomial-regression', 'lab:demonstratedBy', 'lab:sim/w09-poly', '#lv3'),
 ('lab:metric/mse-rmse-mae', 'lab:demonstratedBy', 'lab:sim/w09-err', '#lv4'),
 ('lab:metric/r2', 'lab:demonstratedBy', 'lab:sim/w09-adj', '#lv5'),
 ('lab:claim/knn-r2', 'lab:supports', 'lab:method/knn-regression', '#lv1'), ('lab:claim/knn-r2', 'lab:assertedIn', 'lab:work/ahn-dsb-w09', '#lv1'),
 ('lab:claim/r2-scale', 'lab:supports', 'lab:metric/r2', '#lv5'), ('lab:claim/r2-scale', 'lab:assertedIn', 'lab:work/ahn-dsb-w09', '#lv5'),
 ('lab:dataset/perch-56', 'lab:relatedTo', 'lab:work/fish-market', '#footer'),
 ('lab:method/linear-regression', 'lab:relatedTo', 'lab:work/sklearn-docs', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w09', 'report', '비즈니스를위한데이터과학 강의 교안: 09. 데이터 분석 모형: 회귀모형(1)', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/knn-r2', 'lab:claim/r2-scale', 'lab:method/knn-regression', 'lab:method/linear-regression', 'lab:metric/mse-rmse-mae', 'lab:metric/r2'], 'lab:work/ahn-dsb-w09',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/knn-r2', 'loc': '1교시 5. KNN 회귀 모델 생성 및 성능 평가'}, {'claim': 'lab:claim/r2-scale', 'loc': '2교시 3. 결정계수의 해석'}]),
 R('fishmarket', 'dataset', 'Fish Market', [{'literal': 'Kaggle 공개 데이터셋'}], None, 'data', ['lab:dataset/perch-56'], 'lab:work/fish-market',
   {'title': True, 'authors': False, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '교안 실습 데이터 값으로 확인', '원 출처·이용 조건 확인 필요', publisher='Kaggle'),
 R('sklearn_docs', 'webpage', 'scikit-learn User Guide: Linear Models, Nearest Neighbors', [{'literal': 'scikit-learn developers'}], None, 'background',
   ['lab:method/linear-regression', 'lab:method/knn-regression'], 'lab:work/sklearn-docs',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서 URL 확인', '', URL='https://scikit-learn.org/stable/'),
]
