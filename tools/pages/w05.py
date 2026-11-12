# 5주차 · 데이터 분석 모형: 분류모형(1)
SLUG = 'dsb_w05_classification_1'
FILE = 'week05_classification_1.html'
TITLE = '도미와 빙어 — 분류모형(1): 데이터 준비에서 KNN까지'
DESC = '비즈니스를 위한 데이터 과학 5주차 연구실 해설. 파이썬 데이터 구조, Fish Market 데이터 입력·점검, zip과 라벨링, KNN 학습·예측을 교안 코드 흐름대로 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 작업대 위 도미와 빙어를 자와 저울로 재며 노트북 산점도에 점을 찍는 표지'
COVER_PROP = '🐟'
SEARCH_PH = '예: 리스트, zip, 라벨, KNN, predict'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 데이터 구조'), ('#lv2', '② 입력·점검'), ('#lv3', '③ zip·라벨'), ('#lv4', '④ KNN'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week04_analysis_concepts.html"><small>← 이전 · 4주차</small>도구와 알고리즘의 지도</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week06_classification_2.html"><small>다음 · 6주차</small>농어가 끼어들자 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'doc_think', 'robo_meh', 'robo_calc', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify']
ABOUT = ['lab:concept/python-data-structures', 'lab:dataset/fish-market', 'lab:method/zip-labeling', 'lab:method/knn', 'lab:concept/train-score-trap']
KGPATH = ['concept/python-data-structures', 'limitation/input-mistakes', 'method/data-check', 'limitation/separate-lists', 'method/zip-labeling', 'limitation/no-model', 'method/knn', 'limitation/easy-data']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', 'Fish Market 데이터셋 [2]의 원 출처(올린 사람)와 이용 조건 확인']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 05. 데이터 분석 모형: 분류모형(1). 인공지능융합학과. — Colab 환경, 파이썬 데이터 구조, Fish Market 데이터 입력·점검·시각화, zip()과 [1]*35+[0]*14 라벨링, KNeighborsClassifier(fit·score·predict·predict_proba), KNN 친구 비유, 금융 분류 연계는 교안 본문과 실습 코드를 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/1xRMkAwoSDTJsD_bkttNcuSG2QNkSwrCl?usp=sharing" target="_blank" rel="noopener">Colab</a>',
 '[2] Fish Market 데이터셋(Kaggle 공개 데이터). — 교안 실습의 도미 35마리·빙어 14마리 길이·무게 값. 원 출처와 이용 조건은 확인 필요.',
 '[3] scikit-learn KNeighborsClassifier 문서. <a href="https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html" target="_blank" rel="noopener">링크</a> — n_neighbors 기본값 5.']
ILLUSTRATIVE = [
 '①칸 파이썬 출력은 교안 코드와 같은 동작의 결과를 화면에 다시 적은 것이며, 브라우저에서 파이썬을 실행하지 않습니다.',
 '②칸의 실수(무게 하나 누락, −390g, 0.6kg)는 점검을 보여 주려고 일부러 넣은 값입니다. 나머지 49마리 값은 교안 실습 데이터 그대로입니다.',
 '④칸 예측과 확률, 대결의 Leave-One-Out 정확도는 교안 데이터로 브라우저에서 같은 KNN 규칙(유클리드 거리, 다수결)으로 계산한 값입니다.']

GL = {
 'Google Colab': ['Google Colab', '도구', '구글이 제공하는 클라우드 Jupyter 환경. 설치 없이 브라우저에서 파이썬을 실행하고 자동 저장한다. 인터넷이 필요하다.', 'lab:concept/colab'],
 'List': ['List (리스트)', '파이썬', '순서가 있고 값을 바꿀 수 있는 그릇. [ ]로 만든다. × 2는 반복.', 'lab:concept/python-data-structures'],
 'Tuple': ['Tuple (튜플)', '파이썬', '순서는 있지만 값을 바꿀 수 없는 그릇. ( )로 만든다.', None],
 'Dictionary': ['Dictionary (딕셔너리)', '파이썬', '키-값 쌍의 그릇. 같은 키에는 값 하나만 저장된다.', None],
 'Set': ['Set (셋)', '파이썬', '중복을 허용하지 않고 순서가 없는 그릇.', None],
 'Array': ['NumPy Array (배열)', '파이썬', '같은 타입 숫자를 빠르게 계산하는 그릇. × 2는 원소마다 곱셈.', None],
 'DataFrame': ['pandas DataFrame', '파이썬', '행과 열에 이름이 붙은 2차원 표.', None],
 'len()': ['len()', '파이썬', '그릇에 든 원소의 개수를 돌려주는 함수. 길이·무게 리스트의 개수가 같은지 확인할 때 쓴다.', None],
 '산점도': ['산점도', '시각화', '두 연속형 변수를 점으로 찍어 관계·분포·이상치를 보는 그림. matplotlib의 scatter.', None],
 'zip()': ['zip()', '파이썬', '여러 리스트에서 같은 자리끼리 짝을 지어 묶는 함수. 짧은 쪽에 맞춰 자른다.', 'lab:method/zip-labeling'],
 '라벨링': ['라벨링', '데이터', '각 샘플에 정답(이름표)을 붙이는 일. 도미 = 1, 빙어 = 0.', None],
 '이진 분류': ['이진 분류', '문제', '두 클래스 중 하나로 나누는 분류. 도미/빙어, 승인/거절, 정상/사기.', 'lab:task/binary-classification'],
 'KNN': ['KNN (K-최근접 이웃)', '방법', '새 데이터와 가장 가까운 K개 이웃의 다수결로 예측하는 알고리즘. 학습 때는 데이터를 저장만 한다.', 'lab:method/knn'],
 '유클리드': ['유클리드 거리', '수학', '두 점 사이의 직선 거리. √((x₁−x₂)² + (y₁−y₂)²).', None],
 'predict_proba': ['predict_proba()', 'scikit-learn', '각 클래스일 확률을 돌려준다. KNN에서는 이웃 중 그 클래스의 비율.', None],
 'scikit-learn': ['scikit-learn', '라이브러리', '파이썬의 대표 머신러닝 라이브러리. fit·predict·score로 모델을 같은 방식으로 다룬다.', None],
 '과적합': ['과적합', '개념', '학습 데이터에 지나치게 맞춰 새 데이터에서 성능이 떨어지는 현상.', 'lab:concept/train-score-trap'],
}
CORE = ['Google Colab', 'List', 'Set', 'Array', 'DataFrame', 'len()', '산점도', 'zip()', '라벨링', 'KNN', 'predict_proba', '과적합']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '파이썬 데이터 구조 중 중복을 허용하지 않는 것은? (교안 연습문제 2)', 'o': ['List', 'Tuple', 'Set'], 'a': 2, 'why': 'Set은 같은 값을 두 번 넣어도 하나만 남깁니다.', 'hint': '①칸에서 Set에 "도미"를 더 넣어 보세요.', 'assess': 'lab:concept/python-data-structures'},
  {'id': 'q2', 'q': '[25.4, 26.3] * 2 (리스트)의 결과는?', 'o': ['[50.8, 52.6]', '[25.4, 26.3, 25.4, 26.3]', '오류'], 'a': 1, 'why': '리스트 × 정수는 반복입니다. 원소마다 곱하려면 NumPy 배열을 씁니다.', 'hint': 'List와 Array의 × 2 결과를 비교하세요.', 'calc': True, 'assess': 'lab:concept/python-data-structures'}],
 'lv2': [
  {'id': 'q3', 'q': 'Google Colab에 대한 설명으로 옳지 않은 것은? (교안 연습문제 1)', 'o': ['설치 없이 브라우저로 파이썬을 쓴다', '코드와 결과가 자동 저장된다', '오프라인 환경에서만 쓸 수 있다'], 'a': 2, 'why': 'Colab은 클라우드 서비스라 인터넷 연결이 필요합니다.', 'hint': '왜 섹션 2번 카드.', 'assess': 'lab:concept/colab'},
  {'id': 'q4', 'q': '한 마리의 무게를 kg으로 잘못 적었을 때 가장 잘 드러나는 점검 방법은?', 'o': ['len()', '최솟값만 보기', '길이-무게 산점도'], 'a': 2, 'why': '0.6은 범위 안이라 최솟값만으론 애매하지만, 산점도에서 길이에 비해 너무 가벼운 점으로 튀어나옵니다.', 'hint': '②칸에서 "한 마리만 kg"을 눌러 보세요.', 'assess': 'lab:method/data-check'}],
 'lv3': [
  {'id': 'q5', 'q': '[1]*35 + [0]*14 로 만든 리스트의 길이는?', 'o': ['35', '49', '2'], 'a': 1, 'why': '35개와 14개를 이어붙여 49개입니다.', 'hint': '리스트 반복과 이어붙이기.', 'calc': True, 'assess': 'lab:method/zip-labeling'},
  {'id': 'q6', 'q': '빙어를 먼저 입력하고 라벨은 [1]*35+[0]*14 그대로 두면?', 'o': ['문제없다', '많은 생선에 틀린 이름표가 붙어 모델이 틀린 규칙을 배운다', 'zip()이 자동으로 고쳐 준다'], 'a': 1, 'why': '특성과 라벨은 같은 순서여야 합니다.', 'hint': '③칸에서 버튼을 바꿔 보세요.', 'assess': 'lab:method/zip-labeling'}],
 'lv4': [
  {'id': 'q7', 'q': 'K = 5에서 이웃 5마리 중 도미가 3마리면 predict_proba의 도미 확률은?', 'o': ['0.3', '0.6', '1.0'], 'a': 1, 'why': '이웃 중 도미 비율 3/5 = 0.6입니다.', 'hint': '확률 = 그 클래스 이웃 수 ÷ K', 'calc': True, 'assess': 'lab:method/knn'},
  {'id': 'q8', 'q': 'kn.score(fish_data, fish_target)가 1.0일 때 조심해야 하는 이유는?', 'o': ['점수가 너무 낮아서', '학습에 쓴 데이터로 채점해 새 데이터 성능을 알 수 없어서', 'K가 짝수라서'], 'a': 1, 'why': '같은 데이터로 평가하면 과적합 여부를 판단하기 어렵습니다(교안). 6주차에서 데이터를 나눕니다.', 'hint': '④칸 풀이 1번.', 'assess': 'lab:concept/train-score-trap'},
  {'id': 'q9', 'q': 'KNN에서 K를 보통 홀수로 정하는 이유는?', 'o': ['계산이 빨라서', '이진 분류에서 투표가 반반으로 갈리는 것을 막으려고', '교안이 짝수를 금지해서'], 'a': 1, 'why': '이웃이 2 대 2로 비기는 일을 피합니다.', 'hint': '친구 비유의 마지막 문장.', 'assess': 'lab:method/knn'},
  {'id': 'q10', 'q': '머신러닝 프로세스의 순서로 맞는 것은?', 'o': ['예측 → 학습 → 평가', '학습 → 예측 → 성능평가', '평가 → 학습 → 예측'], 'a': 1, 'why': '교안 6주차 복습 문제의 정답입니다. fit → predict → score.', 'hint': '큰 그림의 오른쪽 카드.', 'assess': 'lab:method/knn'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/colab', 'Concept', 'Google Colab', 'Google Colab', '#why', level=1, family='systems'),
 N('concept/python-data-structures', 'Concept', '파이썬 데이터 구조', 'Python data structures', '#lv1', 'List, Tuple, Dictionary, Set, NumPy Array, pandas DataFrame.', level=1, family='systems'),
 N('dataset/fish-market', 'Dataset', 'Fish Market(도미 35·빙어 14)', 'Fish Market (bream 35, smelt 14)', '#lv2', '도미와 빙어의 길이(cm)·무게(g) 실측값. 교안 실습 데이터.', level=1, family='basics'),
 N('method/data-check', 'Method', '입력 데이터 점검(len·범위·산점도)', 'input data checks', '#lv2', '개수 일치, 불가능한 값, 길이-무게 관계를 확인하는 점검.', level=1, family='data'),
 N('method/zip-labeling', 'Method', 'zip 결합과 라벨링', 'zip pairing and labeling', '#lv3', '[길이, 무게] 쌍(fish_data)과 정답(fish_target)을 같은 순서로 만드는 것.', level=1, family='data'),
 N('task/binary-classification', 'Task', '이진 분류', 'binary classification', '#why', level=1, family='basics'),
 N('method/knn', 'Method', 'KNN', 'k-nearest neighbors', '#lv4', level=1, family='basics'),
 N('concept/train-score-trap', 'Concept', '학습 데이터로 채점하는 함정', 'scoring on training data', '#lv4', '학습에 쓴 데이터로 평가하면 1.0이 나와도 새 데이터 성능을 알 수 없다.', level=2, family='evaluation'),
 N('concept/scale-difference', 'Concept', '특성 눈금 차이', 'feature scale difference', '#lv4', '무게(g)가 길이(cm)보다 숫자 범위가 커서 거리가 무게로만 정해지는 문제.', level=2, family='data'),
 N('metric/loo-accuracy', 'Metric', 'Leave-One-Out 정확도', 'leave-one-out accuracy', '#duel', '한 마리씩 빼놓고 나머지로 학습해 맞힌 비율.', level=2, family='evaluation'),
 N('limitation/input-mistakes', 'Limitation', '담는 과정의 실수', 'input mistakes', '#lv1'),
 N('limitation/separate-lists', 'Limitation', '길이·무게가 따로 논다', 'features not paired', '#lv2'),
 N('limitation/no-model', 'Limitation', '모델이 아직 없다', 'no model yet', '#lv3'),
 N('limitation/easy-data', 'Limitation', '쉬운 데이터·학습 데이터 채점·눈금 차이', 'easy data, train scoring, scale', '#lv4'),
 N('claim/fish-35-14', 'Claim', '교안 실습 데이터: 도미 35마리, 빙어 14마리', 'bream 35, smelt 14', '#lv2', source=[{'cite': '교안 5주차', 'loc': '2교시 5'}]),
 N('claim/knn-default-5', 'Claim', 'KNeighborsClassifier의 기본 K는 5', 'default n_neighbors = 5', '#lv4', source=[{'cite': '교안 5주차', 'loc': '3교시 3'}]),
 N('question/core', 'Question', '길이와 무게만으로 처음 보는 생선을 맞힐 수 있을까?', 'Can length and weight identify a new fish?', '#hero'),
 N('question/duel', 'Question', '특성은 하나로 충분할까?', 'Is one feature enough?', '#duel'),
 N('question/scale', 'Question', '눈금이 다른 특성의 거리는 어떻게 재야 공정할까?', 'How to measure distance fairly across scales?', '#lv4'),
 N('analogy/friends', 'Analogy', '새 친구의 동아리 맞히기 ↔ KNN', 'guessing a new friend\'s club ↔ KNN', '#lv4', anchorType='D'),
 N('analogy/containers', 'Analogy', '시약 용기 ↔ 데이터 구조', 'lab containers ↔ data structures', '#lv1', anchorType='B'),
 N('sim/w05-ds', 'Simulation', '데이터 구조 실험대', 'data structure bench', '#lv1'),
 N('sim/w05-check', 'Simulation', '측정 기록 실수 점검', 'input check', '#lv2'),
 N('sim/w05-zip', 'Simulation', 'zip·라벨 표', 'zip and label table', '#lv3'),
 N('sim/w05-knn', 'Simulation', '새 생선 KNN 예측', 'KNN prediction', '#lv4'),
 N('work/ahn-dsb-w05', 'Work', '안상선, 비즈니스를위한데이터과학 교안 5주차', 'Ahn, DSB lecture notes week 5', '#footer'),
 N('work/fish-market', 'Work', 'Fish Market 데이터셋(Kaggle)', 'Fish Market dataset (Kaggle)', '#footer'),
]

EDGES = [
 ('lab:concept/colab', 'lab:prerequisiteOf', 'lab:concept/python-data-structures', '#lv1'),
 ('lab:concept/python-data-structures', 'lab:prerequisiteOf', 'lab:method/data-check', '#lv2'),
 ('lab:concept/python-data-structures', 'lab:hasLimitation', 'lab:limitation/input-mistakes', '#lv1'),
 ('lab:limitation/input-mistakes', 'lab:addressedBy', 'lab:method/data-check', '#lv2'),
 ('lab:method/data-check', 'lab:evaluatedOn', 'lab:dataset/fish-market', '#lv2'),
 ('lab:method/data-check', 'lab:hasLimitation', 'lab:limitation/separate-lists', '#lv2'),
 ('lab:limitation/separate-lists', 'lab:addressedBy', 'lab:method/zip-labeling', '#lv3'),
 ('lab:method/data-check', 'lab:prerequisiteOf', 'lab:method/zip-labeling', '#lv3'),
 ('lab:method/zip-labeling', 'lab:hasLimitation', 'lab:limitation/no-model', '#lv3'),
 ('lab:limitation/no-model', 'lab:addressedBy', 'lab:method/knn', '#lv4'),
 ('lab:method/zip-labeling', 'lab:prerequisiteOf', 'lab:method/knn', '#lv4'),
 ('lab:method/knn', 'lab:solves', 'lab:task/binary-classification', '#lv4'),
 ('lab:method/knn', 'lab:evaluatedOn', 'lab:dataset/fish-market', '#lv4'),
 ('lab:method/knn', 'lab:hasLimitation', 'lab:limitation/easy-data', '#lv4'),
 ('lab:concept/train-score-trap', 'lab:partOf', 'lab:limitation/easy-data', '#lv4'),
 ('lab:concept/scale-difference', 'lab:partOf', 'lab:limitation/easy-data', '#lv4'),
 ('lab:concept/scale-difference', 'lab:raises', 'lab:question/scale', '#lv4'),
 ('lab:method/knn', 'lab:evaluatedBy', 'lab:metric/loo-accuracy', '#duel'),
 ('lab:metric/loo-accuracy', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:task/binary-classification', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:analogy/friends', 'lab:analogyOf', 'lab:method/knn', '#lv4'),
 ('lab:analogy/containers', 'lab:analogyOf', 'lab:concept/python-data-structures', '#lv1'),
 ('lab:concept/python-data-structures', 'lab:demonstratedBy', 'lab:sim/w05-ds', '#lv1'),
 ('lab:method/data-check', 'lab:demonstratedBy', 'lab:sim/w05-check', '#lv2'),
 ('lab:method/zip-labeling', 'lab:demonstratedBy', 'lab:sim/w05-zip', '#lv3'),
 ('lab:method/knn', 'lab:demonstratedBy', 'lab:sim/w05-knn', '#lv4'),
 ('lab:claim/fish-35-14', 'lab:supports', 'lab:dataset/fish-market', '#lv2'), ('lab:claim/fish-35-14', 'lab:assertedIn', 'lab:work/ahn-dsb-w05', '#lv2'),
 ('lab:claim/knn-default-5', 'lab:supports', 'lab:method/knn', '#lv4'), ('lab:claim/knn-default-5', 'lab:assertedIn', 'lab:work/ahn-dsb-w05', '#lv4'),
 ('lab:dataset/fish-market', 'lab:relatedTo', 'lab:work/fish-market', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w05', 'report', '비즈니스를위한데이터과학 강의 교안: 05. 데이터 분석 모형: 분류모형(1)', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/fish-35-14', 'lab:claim/knn-default-5', 'lab:method/knn', 'lab:method/zip-labeling', 'lab:concept/python-data-structures'], 'lab:work/ahn-dsb-w05',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/fish-35-14', 'loc': '2교시 5. 데이터 결합 및 라벨링'}, {'claim': 'lab:claim/knn-default-5', 'loc': '3교시 3. 모델 객체 생성'}]),
 R('fishmarket', 'dataset', 'Fish Market', [{'literal': 'Kaggle 공개 데이터셋'}], None, 'data', ['lab:dataset/fish-market'], 'lab:work/fish-market',
   {'title': True, 'authors': False, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '교안 실습 데이터 값으로 확인', '원 출처·이용 조건 확인 필요', publisher='Kaggle'),
]
