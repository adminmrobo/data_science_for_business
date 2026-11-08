# 6주차 · 데이터 분석 모형: 분류모형(2)
SLUG = 'dsb_w06_classification_2'
FILE = 'week06_classification_2.html'
TITLE = '농어가 끼어들자 — 분류모형(2): K·SVM·데이터 분할·표준화'
DESC = '비즈니스를 위한 데이터 과학 6주차 연구실 해설. 농어가 들어온 3클래스 KNN, K 최적화, SVM과 커널, 훈련·시험 분할과 층화, 표준화를 교안 데이터로 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 도미·농어·빙어가 든 수조 앞에서 자의 눈금을 맞추고 생선을 훈련·시험 두 바구니로 나누는 표지'
COVER_PROP = '🎣'
SEARCH_PH = '예: 다중 분류, K, SVM, 커널, stratify, 표준화'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 3클래스'), ('#lv2', '② K 고르기'), ('#lv3', '③ SVM'), ('#lv4', '④ 분할'), ('#lv5', '⑤ 표준화'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week05_classification_1.html"><small>← 이전 · 5주차</small>도미와 빙어</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week07_model_evaluation.html"><small>다음 · 7주차</small>정확도 95%의 함정 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:task/multiclass-classification', 'lab:method/k-tuning', 'lab:method/svm', 'lab:method/train-test-split', 'lab:method/standardization']
KGPATH = ['method/knn-multiclass', 'limitation/k-unknown', 'method/k-tuning', 'limitation/curved-boundary', 'method/svm', 'limitation/biased-split', 'method/train-test-split', 'limitation/scale', 'method/standardization']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', 'Fish Market 데이터셋 [2]의 원 출처(올린 사람)와 이용 조건 확인', '③칸 SVM은 커널 Pegasos로 단순화한 것 — scikit-learn SVC(libsvm) 결과와 수치가 다를 수 있음']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 06. 데이터 분석 모형: 분류모형(2). 인공지능융합학과. — 농어 10마리 추가와 다중 분류, K 값 최적화(K = 1의 과적합), SVM·커널(선형·RBF)·gamma, 순서대로 나눈 데이터의 함정, train_test_split·stratify·random_state, 표준화(평균·표준편차)와 New Fish [25, 150] 예시는 교안 본문과 실습 코드를 옮김.',
 '[2] Fish Market 데이터셋(Kaggle 공개 데이터). — 도미 35·빙어 14마리 실측값. 농어 10마리 값은 교안 실습 코드의 값.',
 '[3] scikit-learn 문서: <a href="https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html" target="_blank" rel="noopener">train_test_split</a>, <a href="https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html" target="_blank" rel="noopener">StandardScaler</a>, <a href="https://scikit-learn.org/stable/modules/svm.html" target="_blank" rel="noopener">SVM</a>.',
 '[4] Shalev-Shwartz, S., Singer, Y., Srebro, N., Cotter, A. (2011). Pegasos: Primal Estimated sub-GrAdient SOlver for SVM. Mathematical Programming, 127(1), 3–30. — ③칸 학습 규칙의 출처.']
ILLUSTRATIVE = [
 '②칸의 겹치는 두 집단(훈련 200·시험 200)과 ③칸의 원형 데이터는 개념을 보여 주려고 만든 예시 데이터입니다.',
 '③칸 SVM은 브라우저에서 커널 Pegasos(힌지 손실 확률적 경사)로 단순화해 학습한 것이며, scikit-learn SVC와 경계·서포트 벡터 수가 조금 다를 수 있습니다.',
 '④칸 무작위·층화 분할은 브라우저의 난수 생성기로 섞은 결과라 같은 random_state라도 scikit-learn과 뽑히는 생선이 다릅니다.',
 '대결의 새 생선 30마리는 교안 도미·빙어 값을 조금 흔들어 만든 20마리와 어린 도미(24~27cm, 130~230g) 10마리로, 설명용 가상 데이터입니다.']

GL = {
 '다중 분류': ['다중 분류', '문제', '세 개 이상의 클래스 중 하나로 나누는 분류. 도미·농어·빙어.', 'lab:task/multiclass-classification'],
 'K 값': ['K 값(n_neighbors)', '하이퍼파라미터', 'KNN이 참고할 이웃 수. 작으면 과적합, 크면 과소적합 경향.', 'lab:method/k-tuning'],
 '하이퍼파라미터': ['하이퍼파라미터', '개념', '학습 전에 사람이 정하는 설정값. K, C, gamma 등.', None],
 '과적합': ['과적합', '개념', '학습 데이터에 지나치게 맞춰 새 데이터에서 성능이 떨어지는 현상. K = 1, 큰 gamma.', None],
 '과소적합': ['과소적합', '개념', '모델이 너무 단순해 학습 데이터의 패턴도 잡지 못하는 현상.', None],
 'SVM': ['SVM (서포트 벡터 머신)', '방법', '두 클래스 사이 여백(마진)이 가장 넓은 경계를 찾는 분류 알고리즘.', 'lab:method/svm'],
 '서포트 벡터': ['서포트 벡터', 'SVM', '경계에 가장 가까이 있어 경계 위치를 정하는 데이터 점.', None],
 '마진': ['마진(여백)', 'SVM', '경계와 가장 가까운 점 사이의 거리. SVM은 이것을 최대로 한다.', None],
 '커널': ['커널', 'SVM', '데이터를 높은 차원으로 옮긴 것처럼 계산해 곡선 경계를 만드는 함수. 선형, RBF 등.', 'lab:concept/kernel'],
 'RBF': ['RBF 커널', 'SVM', '가까운 점일수록 큰 값을 주는 가우스 모양 커널. gamma가 클수록 경계가 구불구불해진다.', None],
 'gamma': ['gamma', '하이퍼파라미터', 'RBF 커널에서 한 점의 영향 범위. 크면 좁고 날카로운 경계.', None],
 'train_test_split': ['train_test_split()', 'scikit-learn', '데이터를 훈련·시험으로 무작위로 나누는 함수. test_size, random_state, stratify.', 'lab:method/train-test-split'],
 'stratify': ['stratify(층화)', 'scikit-learn', '나눈 뒤에도 클래스 비율이 원본과 같도록 나누는 옵션.', None],
 'random_state': ['random_state', 'scikit-learn', '난수 씨앗. 같은 값이면 같은 분할이 나와 결과를 재현할 수 있다.', None],
 '표준화': ['표준화(Z-점수)', '전처리', '(값 − 평균) ÷ 표준편차. 특성마다 눈금을 맞춰 거리 계산을 공정하게 만든다.', 'lab:method/standardization'],
 'Min-Max': ['Min-Max 정규화', '전처리', '(값 − 최솟값) ÷ (최댓값 − 최솟값). 0~1 범위로 맞춘다.', None],
 'StandardScaler': ['StandardScaler', 'scikit-learn', '훈련 데이터의 평균·표준편차로 표준화하는 도구. 시험 데이터에도 같은 기준을 쓴다.', None],
}
CORE = ['다중 분류', 'K 값', '과적합', 'SVM', '서포트 벡터', '커널', 'gamma', 'train_test_split', 'stratify', 'random_state', '표준화', 'StandardScaler']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': 'K = 5에서 이웃이 도미 1, 농어 3, 빙어 1이면 predict의 결과는?', 'o': ['도미', '농어', '빙어'], 'a': 1, 'why': '다중 분류에서도 가장 많은 표를 받은 클래스로 정합니다. predict_proba는 [0.2, 0.6, 0.2].', 'hint': '①칸 투표 표시.', 'assess': 'lab:task/multiclass-classification'},
  {'id': 'q2', 'q': '위 상황에서 predict_proba의 농어 확률은?', 'o': ['0.3', '0.6', '1.0'], 'a': 1, 'why': '3 ÷ 5 = 0.6.', 'hint': '그 클래스 이웃 수 ÷ K', 'calc': True, 'assess': 'lab:method/knn-multiclass'}],
 'lv2': [
  {'id': 'q3', 'q': 'K = 1일 때 훈련 정확도 100%, 시험 정확도가 낮다. 이것은?', 'o': ['과소적합', '과적합', '데이터 누수'], 'a': 1, 'why': '자기 자신이 가장 가까운 이웃이라 훈련은 늘 맞히지만 새 데이터는 잡음까지 따라가 틀립니다.', 'hint': '②칸 K = 1.', 'assess': 'lab:method/k-tuning'},
  {'id': 'q4', 'q': 'K를 고를 때 기준으로 삼아야 하는 정확도는?', 'o': ['훈련 정확도', '시험(또는 검증) 정확도', '둘 중 높은 쪽'], 'a': 1, 'why': '처음 보는 데이터에서의 성능이 목표이기 때문입니다.', 'hint': '②칸 오른쪽 초록 곡선.', 'assess': 'lab:method/k-tuning'}],
 'lv3': [
  {'id': 'q5', 'q': 'SVM에서 경계의 위치를 실제로 정하는 점은?', 'o': ['모든 점의 평균', '경계에 가장 가까운 서포트 벡터', '가장 멀리 있는 점'], 'a': 1, 'why': '여백 위·안의 점만 경계에 영향을 줍니다. 나머지 점은 지워도 경계가 같습니다.', 'hint': '③칸 흰 테두리.', 'assess': 'lab:method/svm'},
  {'id': 'q6', 'q': '원형으로 섞인 데이터를 선형 커널로 나누면?', 'o': ['완벽히 나뉜다', '직선이라 원을 감쌀 수 없어 정확도가 낮다', 'gamma만 올리면 된다'], 'a': 1, 'why': '곡선 경계가 필요하면 RBF 같은 커널을 씁니다. 선형 커널에는 gamma가 없습니다.', 'hint': '③칸 원형 데이터 + 선형.', 'assess': 'lab:concept/kernel'}],
 'lv4': [
  {'id': 'q7', 'q': '도미 35, 빙어 14 순서의 49마리를 앞 36 / 뒤 13으로 나누면 시험 세트는?', 'o': ['도미와 빙어가 섞여 있다', '전부 빙어', '전부 도미'], 'a': 1, 'why': '36번째 이후(인덱스 36~48)는 모두 빙어입니다. 훈련에는 빙어가 1마리뿐이라 정확도 0이 나옵니다.', 'hint': '④칸 "순서대로".', 'calc': True, 'assess': 'lab:method/train-test-split'},
  {'id': 'q8', 'q': 'stratify=fish_target 옵션의 역할은?', 'o': ['결과를 재현 가능하게 한다', '훈련·시험의 클래스 비율을 원본과 같게 맞춘다', '특성을 표준화한다'], 'a': 1, 'why': '재현은 random_state, 비율 유지는 stratify의 일입니다.', 'hint': '④칸 무작위 vs 층화.', 'assess': 'lab:method/train-test-split'}],
 'lv5': [
  {'id': 'q9', 'q': '길이 평균 27, 표준편차 10일 때 길이 25cm의 Z-점수는?', 'o': ['-0.2', '0.2', '-2'], 'a': 0, 'why': '(25 − 27) ÷ 10 = −0.2.', 'hint': '(값 − 평균) ÷ 표준편차', 'calc': True, 'assess': 'lab:method/standardization'},
  {'id': 'q10', 'q': '시험 데이터를 표준화할 때 써야 하는 평균·표준편차는?', 'o': ['시험 데이터 자신의 값', '훈련 데이터에서 구한 값', '아무거나'], 'a': 1, 'why': '새 데이터에도 같은 눈금을 써야 공정하게 비교됩니다. StandardScaler는 fit은 훈련에만, transform은 둘 다에.', 'hint': '⑤칸 변환 기준.', 'assess': 'lab:method/standardization'},
  {'id': 'q11', 'q': '원자료 KNN이 New Fish [25, 150]을 빙어로 본 까닭은?', 'o': ['길이가 빙어와 같아서', '무게 눈금이 훨씬 넓어 거리가 무게로만 정해져서', 'K가 짝수라서'], 'a': 1, 'why': '무게 범위가 길이보다 약 30배 넓어, 길이 차이가 거리에 거의 반영되지 않습니다.', 'hint': '⑤칸 원자료 오른쪽 그림.', 'assess': 'lab:limitation/scale'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('dataset/fish-3class', 'Dataset', 'Fish Market(도미 35·농어 10·빙어 14)', 'Fish Market 3-class', '#lv1', '교안 6주차 실습 데이터. 라벨 Bream 0, Perch 1, Smelt 2.', level=1, family='basics'),
 N('task/multiclass-classification', 'Task', '다중 분류', 'multiclass classification', '#lv1', level=1, family='basics'),
 N('method/knn-multiclass', 'Method', '다중 클래스 KNN', 'multiclass KNN', '#lv1', '이웃 K개의 투표에서 가장 많은 클래스로 정한다.', level=1, family='basics'),
 N('method/k-tuning', 'Method', 'K 값 최적화', 'tuning K', '#lv2', 'K를 바꿔 가며 시험(검증) 정확도가 가장 높은 값을 고른다.', level=2, family='evaluation'),
 N('method/svm', 'Method', 'SVM', 'support vector machine', '#lv3', level=2, family='basics'),
 N('concept/kernel', 'Concept', '커널(선형·RBF)과 gamma', 'kernels and gamma', '#lv3', level=2, family='basics'),
 N('method/train-test-split', 'Method', '훈련·시험 분할(무작위·층화)', 'train/test split', '#lv4', level=1, family='evaluation'),
 N('method/standardization', 'Method', '표준화', 'standardization', '#lv5', level=1, family='data'),
 N('metric/test-accuracy', 'Metric', '시험 정확도', 'test accuracy', '#lv2', '학습에 쓰지 않은 데이터를 맞힌 비율.', level=1, family='evaluation'),
 N('concept/overfitting', 'Concept', '과적합·과소적합', 'over/underfitting', '#lv2', level=2, family='evaluation'),
 N('limitation/k-unknown', 'Limitation', 'K를 몇으로 할지 모른다', 'which K?', '#lv1'),
 N('limitation/curved-boundary', 'Limitation', '이웃 투표는 경계를 설명하지 못한다', 'no explicit boundary', '#lv2'),
 N('limitation/biased-split', 'Limitation', '평가 데이터가 치우칠 수 있다', 'biased evaluation split', '#lv3'),
 N('limitation/scale', 'Limitation', '눈금 차이가 거리를 왜곡한다', 'scale distorts distance', '#lv4'),
 N('claim/seq-split-zero', 'Claim', '순서대로 나누면 시험 세트가 모두 빙어가 되어 정확도 0', 'sequential split gives 0 accuracy', '#lv4', source=[{'cite': '교안 6주차', 'loc': '데이터 분할'}]),
 N('claim/newfish-raw-smelt', 'Claim', 'New Fish [25, 150]은 원자료 KNN에서 빙어, 표준화 후 도미', 'New Fish: smelt raw, bream scaled', '#lv5', source=[{'cite': '교안 6주차', 'loc': '데이터 전처리'}]),
 N('question/core', 'Question', '농어가 끼어들고 눈금이 다를 때도 공정하게 맞힐 수 있을까?', 'Can we classify fairly with 3 classes and mixed scales?', '#hero'),
 N('question/duel', 'Question', '원자료 그대로냐, 표준화냐', 'raw or standardized?', '#duel'),
 N('analogy/ruler', 'Analogy', 'cm 자와 g 저울을 같은 눈금으로 ↔ 표준화', 'common ruler ↔ standardization', '#lv5', anchorType='B'),
 N('analogy/road', 'Analogy', '가장 넓은 도로 놓기 ↔ SVM 마진', 'widest road ↔ SVM margin', '#lv3', anchorType='D'),
 N('sim/w06-knn3', 'Simulation', '3클래스 KNN 수조', '3-class KNN', '#lv1'),
 N('sim/w06-k', 'Simulation', 'K와 정확도 곡선', 'K vs accuracy', '#lv2'),
 N('sim/w06-svm', 'Simulation', 'SVM 경계·여백', 'SVM boundary', '#lv3'),
 N('sim/w06-split', 'Simulation', '분할 바구니', 'split baskets', '#lv4'),
 N('sim/w06-scale', 'Simulation', '눈금 바꾸기', 'rescaling', '#lv5'),
 N('work/ahn-dsb-w06', 'Work', '안상선, 비즈니스를위한데이터과학 교안 6주차', 'Ahn, DSB lecture notes week 6', '#footer'),
 N('work/sklearn-docs', 'Work', 'scikit-learn 문서', 'scikit-learn docs', '#footer'),
 N('work/pegasos', 'Work', 'Shalev-Shwartz 외 (2011) Pegasos', 'Pegasos (2011)', '#footer'),
]

EDGES = [
 ('lab:method/knn-multiclass', 'lab:solves', 'lab:task/multiclass-classification', '#lv1'),
 ('lab:method/knn-multiclass', 'lab:evaluatedOn', 'lab:dataset/fish-3class', '#lv1'),
 ('lab:task/multiclass-classification', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:method/knn-multiclass', 'lab:hasLimitation', 'lab:limitation/k-unknown', '#lv1'),
 ('lab:limitation/k-unknown', 'lab:addressedBy', 'lab:method/k-tuning', '#lv2'),
 ('lab:method/k-tuning', 'lab:evaluatedBy', 'lab:metric/test-accuracy', '#lv2'),
 ('lab:method/k-tuning', 'lab:prerequisiteOf', 'lab:method/svm', '#lv3'),
 ('lab:concept/overfitting', 'lab:raises', 'lab:question/core', '#lv2'),
 ('lab:method/k-tuning', 'lab:addresses', 'lab:concept/overfitting', '#lv2'),
 ('lab:method/k-tuning', 'lab:hasLimitation', 'lab:limitation/curved-boundary', '#lv2'),
 ('lab:limitation/curved-boundary', 'lab:addressedBy', 'lab:method/svm', '#lv3'),
 ('lab:concept/kernel', 'lab:partOf', 'lab:method/svm', '#lv3'),
 ('lab:method/svm', 'lab:hasLimitation', 'lab:limitation/biased-split', '#lv3'),
 ('lab:limitation/biased-split', 'lab:addressedBy', 'lab:method/train-test-split', '#lv4'),
 ('lab:method/train-test-split', 'lab:prerequisiteOf', 'lab:metric/test-accuracy', '#lv4'),
 ('lab:method/train-test-split', 'lab:hasLimitation', 'lab:limitation/scale', '#lv4'),
 ('lab:limitation/scale', 'lab:addressedBy', 'lab:method/standardization', '#lv5'),
 ('lab:method/standardization', 'lab:evaluatedOn', 'lab:dataset/fish-3class', '#lv5'),
 ('lab:method/standardization', 'lab:evaluatedBy', 'lab:metric/test-accuracy', '#duel'),
 ('lab:metric/test-accuracy', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/ruler', 'lab:analogyOf', 'lab:method/standardization', '#lv5'),
 ('lab:analogy/road', 'lab:analogyOf', 'lab:method/svm', '#lv3'),
 ('lab:method/knn-multiclass', 'lab:demonstratedBy', 'lab:sim/w06-knn3', '#lv1'),
 ('lab:method/k-tuning', 'lab:demonstratedBy', 'lab:sim/w06-k', '#lv2'),
 ('lab:method/svm', 'lab:demonstratedBy', 'lab:sim/w06-svm', '#lv3'),
 ('lab:method/train-test-split', 'lab:demonstratedBy', 'lab:sim/w06-split', '#lv4'),
 ('lab:method/standardization', 'lab:demonstratedBy', 'lab:sim/w06-scale', '#lv5'),
 ('lab:claim/seq-split-zero', 'lab:supports', 'lab:method/train-test-split', '#lv4'), ('lab:claim/seq-split-zero', 'lab:assertedIn', 'lab:work/ahn-dsb-w06', '#lv4'),
 ('lab:claim/newfish-raw-smelt', 'lab:supports', 'lab:method/standardization', '#lv5'), ('lab:claim/newfish-raw-smelt', 'lab:assertedIn', 'lab:work/ahn-dsb-w06', '#lv5'),
 ('lab:method/train-test-split', 'lab:relatedTo', 'lab:work/sklearn-docs', '#footer'),
 ('lab:method/svm', 'lab:relatedTo', 'lab:work/pegasos', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w06', 'report', '비즈니스를위한데이터과학 강의 교안: 06. 데이터 분석 모형: 분류모형(2)', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/seq-split-zero', 'lab:claim/newfish-raw-smelt', 'lab:method/k-tuning', 'lab:method/svm', 'lab:method/standardization'], 'lab:work/ahn-dsb-w06',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/seq-split-zero', 'loc': '데이터 분할'}, {'claim': 'lab:claim/newfish-raw-smelt', 'loc': '데이터 전처리(표준화)'}]),
 R('sklearn_docs', 'webpage', 'scikit-learn User Guide: train_test_split, StandardScaler, SVM', [{'literal': 'scikit-learn developers'}], None, 'background',
   ['lab:method/train-test-split', 'lab:method/standardization'], 'lab:work/sklearn-docs',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서 URL 확인', '', URL='https://scikit-learn.org/stable/'),
 R('pegasos2011', 'article-journal', 'Pegasos: Primal Estimated sub-GrAdient SOlver for SVM', [{'family': 'Shalev-Shwartz', 'given': 'Shai'}, {'family': 'Singer', 'given': 'Yoram'}, {'family': 'Srebro', 'given': 'Nathan'}, {'family': 'Cotter', 'given': 'Andrew'}], 2011, 'method',
   ['lab:method/svm'], 'lab:work/pegasos',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '서지 기억 기반 — DOI 재확인 권장', '', **{'container-title': 'Mathematical Programming', 'volume': '127', 'issue': '1', 'page': '3-30', 'DOI': '10.1007/s10107-010-0420-4'}),
]
