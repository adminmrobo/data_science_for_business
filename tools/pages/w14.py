# 14주차 · 비즈니스를 위한 고급 분석 기법
SLUG = 'dsb_w14_advanced_analytics'
FILE = 'week14_advanced_analytics.html'
TITLE = '정답 없이, 글 속에서, 층을 쌓아 — 비즈니스를 위한 고급 분석 기법'
DESC = '비즈니스를 위한 데이터 과학 14주차 연구실 해설. K-means 고객 세분화, 임계값으로 거르는 연관 규칙, 규칙 기반 감성 분석과 TF-IDF, 은닉층이 곡선 경계를 만드는 신경망을 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 색깔별로 모인 구슬 무리, 말풍선 리뷰 더미, 층층이 쌓인 신경망 탑을 둘러보는 표지'
COVER_PROP = '🧠'
SEARCH_PH = '예: K-means, 엘보우, 향상도, 감성 사전, TF-IDF, 은닉층'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 군집'), ('#lv2', '② 연관 규칙'), ('#lv3', '③ 감성 분석'), ('#lv4', '④ TF-IDF'), ('#lv5', '⑤ 신경망'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week13_bi_kpi.html"><small>← 이전 · 13주차</small>계기판을 설계하다</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week15_practice_2.html"><small>다음 · 15주차</small>연습 ② 9~14주차 문제풀이 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:method/kmeans', 'lab:method/association-rules', 'lab:method/sentiment-lexicon', 'lab:method/tfidf', 'lab:method/neural-network']
KGPATH = ['method/kmeans', 'limitation/no-product-link', 'method/association-rules', 'limitation/no-feeling', 'method/sentiment-lexicon', 'limitation/no-topic', 'method/tfidf', 'limitation/handmade-features', 'method/neural-network']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '교안 실습(Colab)의 데이터 출처 확인 — 이 페이지에는 싣지 않음']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 14. 비즈니스를 위한 고급 분석 기법. 인공지능융합학과. — 비지도학습(군집·연관 규칙·차원 축소), 지도학습과의 차이, RFM 세분화, 지지도·신뢰도·향상도와 임계값, 추천 시스템, 유통·금융 사례, 자연어 처리·VOC·감성 분석(규칙·머신러닝·딥러닝), TF-IDF·N-gram·LDA, 머신러닝 vs 딥러닝, MLP·CNN·RNN·LSTM, 산업별 적용과 도입 전략은 교안 본문을 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/1xHHg8E-gUIgESVMbHTsK9ZQ4bPReKoIM?usp=sharing" target="_blank" rel="noopener">Colab</a>',
 '[2] 한국기술교육대학교. "핀테크데이터분석". 국민평생직업능력개발 STEP 온라인평생교육원. — 교안이 인용한 신경망·RNN·LSTM 그림의 출처.',
 '[3] scikit-learn 문서: <a href="https://scikit-learn.org/stable/modules/clustering.html#k-means" target="_blank" rel="noopener">K-means</a>, <a href="https://scikit-learn.org/stable/modules/feature_extraction.html#tfidf-term-weighting" target="_blank" rel="noopener">TF-IDF</a>, <a href="https://scikit-learn.org/stable/modules/neural_networks_supervised.html" target="_blank" rel="noopener">MLP</a>.']
ILLUSTRATIVE = [
 '①칸 고객 150명, ②칸 영수증 400장, ③칸 리뷰 12개(문장과 토큰), ④칸 VOC 6건, ⑤칸 원형 고객 200명, 대결의 대출 신청 800명은 모두 설명용 예시 데이터입니다.',
 '③칸 감성 사전과 부정어 규칙은 이 페이지에서 정한 단순 규칙이며, 실제 한국어 감성 사전이나 형태소 분석기를 쓰지 않았습니다.',
 '⑤칸과 대결의 신경망은 브라우저에서 은닉층 1개(tanh), 전체 배치 경사하강 2,000회로 직접 학습한 것입니다.']

GL = {
 '비지도학습': ['비지도학습', '학습', '정답 레이블 없이 데이터의 구조와 패턴을 찾는 기계학습.', 'lab:concept/unsupervised'],
 'K-means': ['K-means', '군집', 'K개 중심에 가까운 점을 배정하고 중심을 평균으로 옮기기를 반복하는 군집 알고리즘.', 'lab:method/kmeans'],
 '엘보우': ['엘보우 방법', '군집', 'K에 따른 군집 내 거리 제곱합이 꺾이는 지점으로 K를 고르는 방법.', None],
 '지지도': ['지지도', '연관 규칙', '전체 거래 중 해당 조합이 나온 비율.', 'lab:method/association-rules'],
 '신뢰도': ['신뢰도', '연관 규칙', 'X를 산 거래 중 Y도 산 비율. P(Y | X).', None],
 '향상도': ['향상도', '연관 규칙', '신뢰도 ÷ Y의 지지도. 1보다 크면 함께 사는 경향.', None],
 '감성 분석': ['감성 분석', '자연어 처리', '텍스트의 긍정·부정·중립을 판정하는 분석.', 'lab:method/sentiment-lexicon'],
 'VOC': ['VOC(고객의 소리)', '자연어 처리', '설문·리뷰·상담·소셜미디어 등에서 모은 고객 의견.', None],
 'TF-IDF': ['TF-IDF', '자연어 처리', '문서 안에서 자주, 다른 문서에서는 드물게 나오는 단어에 높은 점수.', 'lab:method/tfidf'],
 '토픽 모델링': ['토픽 모델링(LDA)', '자연어 처리', '대량의 텍스트에서 잠재 주제 그룹을 자동으로 찾는 기법.', None],
 '은닉층': ['은닉층', '딥러닝', '입력층과 출력층 사이의 층. 비선형 특성을 스스로 만든다.', 'lab:method/neural-network'],
 '역전파': ['역전파', '딥러닝', '출력 오차를 거꾸로 전파해 각 가중치의 기울기를 구하는 알고리즘.', None],
 '표현 학습': ['표현 학습', '딥러닝', '사람이 특성을 설계하지 않고 원시 데이터에서 유용한 특성을 스스로 배우는 것.', None],
 'CNN': ['CNN(합성곱 신경망)', '딥러닝', '이미지에 특화. 합성곱·풀링으로 지역 특성을 단계적으로 추출.', None],
 'LSTM': ['LSTM', '딥러닝', '긴 순서의 의존성을 기억하도록 개선한 RNN.', None],
}
CORE = ['비지도학습', 'K-means', '엘보우', '지지도', '신뢰도', '향상도', '감성 분석', 'VOC', 'TF-IDF', '토픽 모델링', '은닉층', '역전파', '표현 학습', 'CNN', 'LSTM']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '비지도학습의 가장 큰 특징은? (교안 연습문제 1)', 'o': ['정답 레이블이 있는 데이터로 학습한다', '정답 레이블 없이 데이터에서 패턴을 찾는다', '분류와 회귀 문제만 해결한다', '예측 정확도를 정확히 측정할 수 있다'], 'a': 1, 'why': '정답 없이 데이터 자체의 구조를 발견하는 것이 핵심입니다.', 'hint': '큰 그림 오른쪽.', 'assess': 'lab:concept/unsupervised'},
  {'id': 'q2', 'q': 'K-means에서 한 번의 반복이 하는 일은?', 'o': ['중심을 무작위로 다시 뽑는다', '가장 가까운 중심에 배정한 뒤 중심을 무리의 평균으로 옮긴다', '정답 라벨과 비교한다'], 'a': 1, 'why': '배정 → 갱신을 중심이 움직이지 않을 때까지 반복합니다.', 'hint': '①칸 반복 슬라이더.', 'assess': 'lab:method/kmeans'}],
 'lv2': [
  {'id': 'q3', 'q': '신뢰도 70%, 결과 상품의 지지도 70%인 규칙의 향상도는?', 'o': ['0.49', '1.0', '1.4'], 'a': 1, 'why': '0.7 ÷ 0.7 = 1. 원래 다들 사는 상품이라 연관이 없습니다.', 'hint': '신뢰도 ÷ Y의 지지도', 'calc': True, 'assess': 'lab:method/association-rules'},
  {'id': 'q4', 'q': '최소 지지도를 너무 높게 잡으면?', 'o': ['규칙이 쏟아진다', '드문 상품의 규칙이 사라진다', '향상도가 올라간다'], 'a': 1, 'why': '자주 나오는 조합만 남아, 매출이 작은 상품의 짝은 걸러집니다.', 'hint': '②칸 지지도 슬라이더.', 'assess': 'lab:method/association-rules'}],
 'lv3': [
  {'id': 'q5', 'q': '다음 중 정형 데이터에 해당하는 것은? (교안 연습문제 2)', 'o': ['고객 리뷰 텍스트', '소셜미디어 게시물', '고객 구매 금액 데이터', '상담원과 고객의 통화 내용'], 'a': 2, 'why': '구매 금액은 행·열 구조의 수치 데이터, 나머지는 비정형 자연어입니다.', 'hint': '왜 섹션 2번.', 'assess': 'lab:method/sentiment-lexicon'},
  {'id': 'q6', 'q': '규칙 기반 감성 분석의 대표적 한계는?', 'o': ['구현이 어렵다', '문맥(부정어·비꼼)을 충분히 고려하지 못한다', '해석이 어렵다'], 'a': 1, 'why': '구현·해석은 쉽지만 문맥에 약합니다(교안).', 'hint': '③칸 "참 잘도 빠르네요".', 'assess': 'lab:method/sentiment-lexicon'}],
 'lv4': [
  {'id': 'q7', 'q': '문서 6개 중 6개 모두에 나오는 단어의 IDF = log(N ÷ df)는?', 'o': ['0', '1', '6'], 'a': 0, 'why': 'log(6 ÷ 6) = log 1 = 0. 어디에나 나오면 구별력이 없습니다.', 'hint': 'log 1', 'calc': True, 'assess': 'lab:method/tfidf'},
  {'id': 'q8', 'q': '대량의 리뷰에서 잠재 주제 그룹을 자동으로 찾는 기법은?', 'o': ['N-gram', 'LDA 토픽 모델링', '워드클라우드'], 'a': 1, 'why': 'LDA는 단어 분포로 주제를 추정합니다(교안).', 'hint': '④칸 머신러닝에서는.', 'assess': 'lab:method/tfidf'}],
 'lv5': [
  {'id': 'q9', 'q': '딥러닝이 머신러닝 대비 갖는 가장 큰 장점은? (교안 연습문제 3)', 'o': ['적은 데이터로도 학습', '빠른 학습 속도', '복잡한 비선형 패턴 학습 능력', '결과 해석의 용이성'], 'a': 2, 'why': '다층 신경망은 이미지·음성·자연어의 복잡한 비선형 관계를 배웁니다.', 'hint': '⑤칸 원형 데이터.', 'assess': 'lab:method/neural-network'},
  {'id': 'q10', 'q': '이미지 결함 검사에 가장 알맞은 딥러닝 구조는?', 'o': ['CNN', 'RNN', '로지스틱 회귀'], 'a': 0, 'why': 'CNN은 합성곱으로 이미지의 지역 특성을 추출합니다. RNN·LSTM은 순서 데이터.', 'hint': '용어 CNN.', 'assess': 'lab:method/neural-network'},
  {'id': 'q11', 'q': '경계가 직선인 문제에서 신경망과 로지스틱 회귀의 정확도가 같다면 현장에서 보통 고르는 것은?', 'o': ['신경망 — 더 최신이라서', '로지스틱 회귀 — 단순하고 설명하기 쉬워서', '아무거나'], 'a': 1, 'why': '같은 성능이면 비용·해석·규제 대응이 쉬운 모델을 고릅니다(교안: 규제 분야의 설명 가능성).', 'hint': '대결 판정.', 'assess': 'lab:method/neural-network'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/unsupervised', 'Concept', '비지도학습', 'unsupervised learning', '#big', level=1, family='basics'),
 N('task/customer-insight', 'Task', '고객 이해와 인사이트 도출', 'customer insight', '#why', level=1, family='basics'),
 N('dataset/customers-150', 'Dataset', '예시 고객 150명(최근성·구매액)', 'synthetic customers (150)', '#lv1', level=1, family='data'),
 N('method/kmeans', 'Method', 'K-means 군집', 'K-means clustering', '#lv1', level=1, family='basics'),
 N('method/association-rules', 'Method', '연관 규칙(임계값 필터)', 'association rules', '#lv2', level=1, family='basics'),
 N('method/sentiment-lexicon', 'Method', '규칙 기반 감성 분석', 'lexicon-based sentiment', '#lv3', level=1, family='basics'),
 N('method/tfidf', 'Method', 'TF-IDF', 'TF-IDF', '#lv4', level=1, family='data'),
 N('method/neural-network', 'Method', '신경망(MLP)', 'neural network (MLP)', '#lv5', level=2, family='basics'),
 N('concept/representation-learning', 'Concept', '표현 학습', 'representation learning', '#lv5', '사람이 특성을 설계하지 않고 원시 데이터에서 특성을 배우는 것.', level=2, family='basics'),
 N('limitation/no-product-link', 'Limitation', '상품 관계는 모른다', 'no product relations', '#lv1'),
 N('limitation/no-feeling', 'Limitation', '고객의 느낌은 모른다', 'no feelings', '#lv2'),
 N('limitation/no-topic', 'Limitation', '무엇에 대한 말인지 모른다', 'no topic', '#lv3'),
 N('limitation/handmade-features', 'Limitation', '사람이 정한 특성뿐', 'hand-made features only', '#lv4'),
 N('claim/rules-thresholds', 'Claim', '최소 지지도·신뢰도 임계값으로 노이즈를 제거하고 가치 높은 규칙만 선별', 'thresholds filter noisy rules', '#lv2', source=[{'cite': '교안 14주차', 'loc': '1교시 4'}]),
 N('claim/lexicon-limit', 'Claim', '규칙 기반 감성 분석은 해석이 쉽지만 문맥을 충분히 고려하지 못한다', 'lexicon methods miss context', '#lv3', source=[{'cite': '교안 14주차', 'loc': '2교시 3'}]),
 N('question/core', 'Question', '정답이 없고, 글이고, 경계가 직선이 아닐 때 어떻게 할까?', 'What if no labels, text, nonlinear?', '#hero'),
 N('question/duel', 'Question', '직선이면 충분한 문제에 딥러닝이 필요할까', 'Does a linear problem need deep learning?', '#duel'),
 N('analogy/party', 'Analogy', '파티장의 자연스러운 무리 ↔ 군집', 'party groups ↔ clustering', '#lv1', anchorType='D'),
 N('analogy/rulers', 'Analogy', '직선 자 여러 개로 원 만들기 ↔ 은닉 뉴런', 'many rulers ↔ hidden units', '#lv5', anchorType='D'),
 N('sim/w14-km', 'Simulation', 'K-means 반복과 엘보우', 'K-means steps and elbow', '#lv1'),
 N('sim/w14-ar', 'Simulation', '임계값 규칙 표', 'threshold rule table', '#lv2'),
 N('sim/w14-sent', 'Simulation', '리뷰 12개 감성 판정', '12-review sentiment', '#lv3'),
 N('sim/w14-tfidf', 'Simulation', 'VOC TF vs TF-IDF', 'VOC TF vs TF-IDF', '#lv4'),
 N('sim/w14-nn', 'Simulation', '은닉 뉴런과 결정 영역', 'hidden units and regions', '#lv5'),
 N('work/ahn-dsb-w14', 'Work', '안상선, 비즈니스를위한데이터과학 교안 14주차', 'Ahn, DSB lecture notes week 14', '#footer'),
 N('work/step-fintech', 'Work', '한국기술교육대학교, 핀테크데이터분석(STEP)', 'KoreaTech STEP Fintech Data Analysis', '#footer'),
 N('work/sklearn-docs', 'Work', 'scikit-learn 문서', 'scikit-learn docs', '#footer'),
]

EDGES = [
 ('lab:task/customer-insight', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:method/kmeans', 'lab:partOf', 'lab:concept/unsupervised', '#lv1'),
 ('lab:method/kmeans', 'lab:solves', 'lab:task/customer-insight', '#lv1'),
 ('lab:method/kmeans', 'lab:evaluatedOn', 'lab:dataset/customers-150', '#lv1'),
 ('lab:method/kmeans', 'lab:hasLimitation', 'lab:limitation/no-product-link', '#lv1'),
 ('lab:limitation/no-product-link', 'lab:addressedBy', 'lab:method/association-rules', '#lv2'),
 ('lab:method/association-rules', 'lab:partOf', 'lab:concept/unsupervised', '#lv2'),
 ('lab:method/association-rules', 'lab:hasLimitation', 'lab:limitation/no-feeling', '#lv2'),
 ('lab:limitation/no-feeling', 'lab:addressedBy', 'lab:method/sentiment-lexicon', '#lv3'),
 ('lab:method/sentiment-lexicon', 'lab:solves', 'lab:task/customer-insight', '#lv3'),
 ('lab:method/sentiment-lexicon', 'lab:hasLimitation', 'lab:limitation/no-topic', '#lv3'),
 ('lab:limitation/no-topic', 'lab:addressedBy', 'lab:method/tfidf', '#lv4'),
 ('lab:method/tfidf', 'lab:hasLimitation', 'lab:limitation/handmade-features', '#lv4'),
 ('lab:limitation/handmade-features', 'lab:addressedBy', 'lab:method/neural-network', '#lv5'),
 ('lab:concept/representation-learning', 'lab:partOf', 'lab:method/neural-network', '#lv5'),
 ('lab:method/neural-network', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/party', 'lab:analogyOf', 'lab:method/kmeans', '#lv1'),
 ('lab:analogy/rulers', 'lab:analogyOf', 'lab:method/neural-network', '#lv5'),
 ('lab:method/kmeans', 'lab:demonstratedBy', 'lab:sim/w14-km', '#lv1'),
 ('lab:method/association-rules', 'lab:demonstratedBy', 'lab:sim/w14-ar', '#lv2'),
 ('lab:method/sentiment-lexicon', 'lab:demonstratedBy', 'lab:sim/w14-sent', '#lv3'),
 ('lab:method/tfidf', 'lab:demonstratedBy', 'lab:sim/w14-tfidf', '#lv4'),
 ('lab:method/neural-network', 'lab:demonstratedBy', 'lab:sim/w14-nn', '#lv5'),
 ('lab:claim/rules-thresholds', 'lab:supports', 'lab:method/association-rules', '#lv2'), ('lab:claim/rules-thresholds', 'lab:assertedIn', 'lab:work/ahn-dsb-w14', '#lv2'),
 ('lab:claim/lexicon-limit', 'lab:supports', 'lab:method/sentiment-lexicon', '#lv3'), ('lab:claim/lexicon-limit', 'lab:assertedIn', 'lab:work/ahn-dsb-w14', '#lv3'),
 ('lab:method/neural-network', 'lab:relatedTo', 'lab:work/step-fintech', '#footer'),
 ('lab:method/tfidf', 'lab:relatedTo', 'lab:work/sklearn-docs', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w14', 'report', '비즈니스를위한데이터과학 강의 교안: 14. 비즈니스를 위한 고급 분석 기법', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/rules-thresholds', 'lab:claim/lexicon-limit', 'lab:method/kmeans', 'lab:method/tfidf', 'lab:method/neural-network'], 'lab:work/ahn-dsb-w14',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/rules-thresholds', 'loc': '1교시 4. 장바구니 분석 기법'}, {'claim': 'lab:claim/lexicon-limit', 'loc': '2교시 3. 감성 분석 기술 개요'}]),
 R('step_fintech', 'webpage', '핀테크데이터분석', [{'literal': '한국기술교육대학교'}], None, 'background', ['lab:method/neural-network'], 'lab:work/step-fintech',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '교안 인용 서지 그대로', '', publisher='STEP 온라인평생교육원', URL='https://www.step.or.kr'),
 R('sklearn_docs', 'webpage', 'scikit-learn User Guide: Clustering, Feature extraction, Neural networks', [{'literal': 'scikit-learn developers'}], None, 'background', ['lab:method/kmeans', 'lab:method/tfidf'], 'lab:work/sklearn-docs',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서 URL 확인', '', URL='https://scikit-learn.org/stable/'),
]
