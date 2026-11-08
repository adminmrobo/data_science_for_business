# 4주차 · 데이터 분석 개념의 이해
SLUG = 'dsb_w04_analysis_concepts'
FILE = 'week04_analysis_concepts.html'
TITLE = '도구와 알고리즘의 지도 — 데이터 분석 개념의 이해'
DESC = '비즈니스를 위한 데이터 과학 4주차 연구실 해설. 분석 도구 고르기, 규칙 기반 대 머신러닝 신용대출 심사, 데이터 분할·교차 검증·과적합, 장바구니 분석(지지도·신뢰도·향상도)을 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 표·차트·코드 도구가 꽂힌 큰 연장통과 갈래가 나뉘는 나무 그림 앞에 모인 표지'
COVER_PROP = '🧰'
SEARCH_PH = '예: 과적합, 교차 검증, 향상도, 지도 학습'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 도구'), ('#lv2', '② 규칙 vs ML'), ('#lv3', '③ 분할·검증'), ('#lv4', '④ 모델 선택'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week03_analysis_prep.html"><small>← 이전 · 3주차</small>분석 전에 데이터를 손보다</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week05_classification_1.html"><small>다음 · 5주차</small>도미와 빙어 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'doc_think', 'robo_meh', 'robo_calc', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'doc_board']
ABOUT = ['lab:concept/analysis-tools', 'lab:concept/rule-vs-ml', 'lab:concept/overfitting', 'lab:method/cross-validation', 'lab:method/association-rules']
KGPATH = ['concept/analysis-tools', 'limitation/who-makes-rules', 'concept/rule-vs-ml', 'limitation/memorized', 'method/cross-validation', 'limitation/other-problem-types', 'concept/model-selection', 'limitation/fairness']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 04. 데이터 분석 개념의 이해. 인공지능융합학과. — 도구 네 계열과 비교표, 학습 경로, 환경·재현성(conda·Docker·Git), 전통적 프로그래밍과 머신러닝(신용대출 사례), 분석 프로세스, 60:20:20·70:15:15 분할, 교차 검증, 지도·비지도·강화 학습 비교표, 평가 지표, KNN·SVM·트리·랜덤 포레스트, 장바구니 예시(지지도 0.6·신뢰도 1.0·향상도 1.25), 산업별 적용, 모델 선택과 윤리는 교안 본문을 옮김.',
 '[2] 한국기술교육대학교 온라인평생교육원. 「핀테크데이터분석」. — 교안의 참고문헌.']
ILLUSTRATIVE = [
 '①칸 도구 점수는 교안의 정성 비교를 규칙으로 옮긴 도식입니다.',
 '②·③칸과 대결: 대출 기록(과거 600건 시드 3, 시험 400건 시드 99), 연소득 2,000만~8,000만 원, 비스듬한 진짜 경계와 예외 8%는 설명을 위해 만든 값이며 실제 심사 기준이 아닙니다.',
 '④칸 장바구니: 라면·달걀 칸은 교안 예시(손님 5명)를 따랐고, 우유·커피·케이크 칸은 설명용으로 더했습니다.']

GL = {
 '피벗 테이블': ['피벗 테이블', '도구', '스프레드시트에서 데이터를 기준별로 묶어 합계·평균을 내는 표.', None],
 'VBA': ['VBA', '도구', '엑셀 등 MS 오피스에서 반복 작업을 자동화하는 프로그래밍 언어.', None],
 'BI': ['BI (비즈니스 인텔리전스)', '도구', '데이터를 시각화·대시보드로 보여 주어 의사결정을 돕는 도구와 활동. Tableau, Power BI 등.', None],
 'IDE': ['IDE (통합개발환경)', '도구', '코드 작성·실행·결과 확인을 한곳에서 하는 프로그램. Jupyter Notebook, RStudio, Google Colab.', None],
 '재현성': ['재현성', '개념', '같은 데이터로 같은 분석을 하면 언제나 같은 결과가 나오는 성질. 도구 버전·코드·처리 과정을 기록해 지킨다.', 'lab:concept/reproducibility'],
 '머신러닝': ['머신러닝(기계학습)', '방법', '알고리즘이 데이터에서 패턴을 스스로 학습해 예측하는 방식.', 'lab:concept/rule-vs-ml'],
 '전통적 프로그래밍': ['전통적 프로그래밍', '방법', '사람이 규칙과 로직을 명시적으로 코드로 적는 방식.', None],
 '지도 학습': ['지도 학습', '방법', '입력과 정답(레이블)이 쌍으로 있는 데이터로 학습. 분류·회귀.', 'lab:concept/supervised'],
 '비지도 학습': ['비지도 학습', '방법', '정답 없이 데이터의 숨은 구조를 찾는 학습. 군집, 차원 축소.', 'lab:concept/unsupervised'],
 '강화 학습': ['강화 학습', '방법', '에이전트가 환경과 주고받으며 보상을 최대화하는 행동을 시행착오로 배우는 학습.', 'lab:concept/reinforcement'],
 '레이블': ['레이블(정답)', '데이터', '지도 학습에서 각 기록에 붙은 정답. 예: 정상 상환/연체.', None],
 '과적합': ['과적합', '개념', '훈련 데이터를 지나치게 외워 새 데이터에서 성능이 떨어지는 현상.', 'lab:concept/overfitting'],
 '과소적합': ['과소적합', '개념', '모델이 너무 단순해 훈련 데이터의 패턴도 제대로 잡지 못하는 상태.', None],
 '교차 검증': ['교차 검증', '방법', '데이터를 k개 묶음으로 나눠 번갈아 검증용으로 쓰며 k번 평가하는 방법.', 'lab:method/cross-validation'],
 '홀드아웃': ['홀드아웃 검증', '방법', '데이터를 고정 비율로 한 번 나눠 한 번 평가하는 방법.', None],
 'KNN': ['KNN (K-최근접 이웃)', '방법', '새 데이터와 가장 가까운 K개 이웃의 다수결(또는 평균)로 예측하는 알고리즘.', 'lab:method/knn'],
 'SVM': ['SVM (서포트 벡터 머신)', '방법', '두 클래스 사이의 여백(마진)이 가장 넓은 경계를 찾는 알고리즘. 커널로 곡선 경계도 만든다.', None],
 '랜덤 포레스트': ['랜덤 포레스트', '방법', '여러 의사결정 트리를 부트스트랩 표본과 무작위 특성으로 만들어 다수결·평균하는 앙상블.', None],
 '지지도': ['지지도', '지표', '전체 거래 중 A와 B를 함께 산 비율.', None],
 '신뢰도': ['신뢰도', '지표', 'A를 산 거래 중 B도 산 비율. P(B|A).', None],
 '향상도': ['향상도', '지표', '신뢰도 ÷ B의 전체 구매 비율. 1보다 크면 양의 연관, 1이면 독립.', 'lab:metric/lift'],
 '혼동행렬': ['혼동행렬', '지표', '실제 클래스와 예측 클래스를 표로 맞대어 맞힘·틀림의 종류를 세는 표.', None],
 '알고리즘 편향': ['알고리즘 편향', '윤리', '데이터나 모델 설계 과정에서 생기는 불공정한 차별.', 'lab:limitation/fairness'],
}
CORE = ['재현성', '머신러닝', '지도 학습', '비지도 학습', '강화 학습', '과적합', '교차 검증', 'KNN', '지지도', '신뢰도', '향상도', '알고리즘 편향']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '교안이 권하는 초보자의 도구 학습 순서는?', 'o': ['프로그래밍 언어 → 통계 프로그램 → 시각화 → 스프레드시트', '스프레드시트 → 시각화 도구 → 통계 프로그램 → 프로그래밍 언어', '시각화 → 스프레드시트 → 프로그래밍 언어 → 통계 프로그램'], 'a': 1, 'why': '간단한 도구부터 단계별로 복잡한 도구로 갑니다.', 'hint': '①칸 풀이 2번.', 'assess': 'lab:concept/analysis-tools'},
  {'id': 'q2', 'q': '분석을 매달 똑같이 반복하고 누구나 같은 결과를 얻게 하려면 특히 무엇이 필요한가?', 'o': ['더 큰 모니터', '코드·도구 버전·처리 과정을 기록하는 재현성 관리(Git, 가상 환경)', '수작업 복사·붙여넣기'], 'a': 1, 'why': '교안의 재현성: 도구 버전, 분석 코드, 데이터 처리 과정을 모두 기록합니다.', 'hint': '반복·재현 조건을 바꿔 보세요.', 'assess': 'lab:concept/reproducibility'}],
 'lv2': [
  {'id': 'q3', 'q': '머신러닝과 전통적 프로그래밍의 차이로 가장 알맞은 것은? (교안 연습문제 1)', 'o': ['머신러닝은 개발자가 모든 규칙을 미리 정의한다', '전통적 프로그래밍은 사람이 규칙을 코드로 적고, 머신러닝은 데이터에서 패턴을 스스로 배운다', '머신러닝은 언제나 더 좋은 성능을 보장한다'], 'a': 1, 'why': '교안의 정답 ②입니다. 머신러닝이 언제나 이기는 것도 아닙니다(대결의 조건 메모).', 'hint': '②칸 짝 카드.', 'assess': 'lab:concept/rule-vs-ml'},
  {'id': 'q4', 'q': '거절 사유를 고객에게 설명해야 하는 업무에서 규칙 기반이 가진 장점은?', 'o': ['정확도가 언제나 높다', '판단 이유를 명확히 말할 수 있다(해석 가능성)', '학습 데이터가 많이 필요하다'], 'a': 1, 'why': '규칙은 로직이 명확합니다. 성능과 해석 가능성 사이에는 균형점이 필요합니다.', 'hint': '②칸 인사이트 두 번째 줄.', 'assess': 'lab:concept/interpretability'}],
 'lv3': [
  {'id': 'q5', 'q': '교차 검증을 쓰는 주된 목적은? (교안 연습문제 2)', 'o': ['처리 속도 향상', '과적합을 막고 일반화 성능을 안정적으로 평가', '결측값 자동 채우기'], 'a': 1, 'why': '제한된 데이터를 모두 학습과 검증에 골고루 쓰며 안정적으로 평가합니다.', 'hint': '③칸 풀이 2번.', 'assess': 'lab:method/cross-validation'},
  {'id': 'q6', 'q': '데이터 1,000건을 70:15:15로 나누면 시험 데이터는 몇 건인가?', 'o': ['70건', '150건', '300건'], 'a': 1, 'why': '1,000 × 0.15 = 150건입니다.', 'hint': '마지막 비율이 시험 데이터입니다.', 'calc': True, 'assess': 'lab:method/data-split'},
  {'id': 'q7', 'q': 'K = 1 KNN의 훈련 정확도가 100%인 이유는?', 'o': ['가장 좋은 모델이라서', '각 훈련 기록의 가장 가까운 이웃이 자기 자신이라서', '시험 데이터를 썼기 때문에'], 'a': 1, 'why': '자기 자신을 보고 답하므로 외운 점수입니다. 교차 검증 점수로 판단합니다.', 'hint': 'K 슬라이더를 1로 두세요.', 'assess': 'lab:concept/overfitting'}],
 'lv4': [
  {'id': 'q8', 'q': '손님 10명 중 커피 6명, 케이크 5명, 둘 다 4명. 커피→케이크의 향상도는?', 'o': ['0.67', '1.33', '0.8'], 'a': 1, 'why': '신뢰도 = 4/6 ≈ 0.667, P(케이크) = 0.5, 향상도 = 0.667 ÷ 0.5 ≈ 1.33입니다.', 'hint': '신뢰도 ÷ 결과 상품의 전체 구매 비율.', 'calc': True, 'assess': 'lab:metric/lift'},
  {'id': 'q9', 'q': '장바구니 분석이 속하는 분석 방법은? (교안 연습문제 3)', 'o': ['최적화 분석', '시계열 분석', '연관성 분석'], 'a': 2, 'why': '항목들의 동시 발생 패턴을 찾는 연관성 분석입니다.', 'hint': '④칸 표의 넷째 줄.', 'assess': 'lab:method/association-rules'},
  {'id': 'q10', 'q': '레이블 없는 고객 데이터로 비슷한 고객 묶음을 찾고 싶다. 알맞은 학습 방법은?', 'o': ['지도 학습', '비지도 학습(군집)', '강화 학습'], 'a': 1, 'why': '정답 없이 구조를 찾는 비지도 학습, 예를 들어 K-means 군집입니다.', 'hint': '큰 그림의 비교표.', 'assess': 'lab:concept/unsupervised'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/analysis-tools', 'Concept', '분석 도구 네 계열', 'analysis tool families', '#lv1', '스프레드시트, 상용 통계 도구, 오픈소스(Python·R), 시각화·BI.', level=1, family='systems'),
 N('concept/reproducibility', 'Concept', '재현성', 'reproducibility', '#lv1', level=2, family='systems'),
 N('concept/rule-vs-ml', 'Concept', '규칙 기반과 머신러닝', 'rule-based vs machine learning', '#lv2', '사람이 규칙을 적는 방식과 데이터·과거 결과에서 규칙을 배우는 방식의 비교.', level=1, family='basics'),
 N('concept/interpretability', 'Concept', '해석 가능성', 'interpretability', '#lv2', '모델의 판단 이유를 사람이 이해하고 설명할 수 있는 정도. 성능과 균형을 이룬다.', level=2, family='ethics'),
 N('method/knn', 'Method', 'KNN', 'k-nearest neighbors', '#lv2', level=1, family='basics'),
 N('method/expert-rule', 'Method', '심사역 규칙(네모 규칙)', 'expert threshold rule', '#lv2', '소득 ≥ A 그리고 부채비율 ≤ B 같은 사람이 정한 기준.', level=1, family='basics', domain=['biz']),
 N('task/loan-screening', 'Task', '신용대출 심사', 'loan screening', '#lv2', '신청자의 정상 상환·연체를 예측해 승인 여부를 정하는 이진 분류 문제.', level=1, family='basics', domain=['biz']),
 N('concept/overfitting', 'Concept', '과적합', 'overfitting', '#lv3', level=2, family='evaluation'),
 N('method/data-split', 'Method', '훈련·검증·시험 분할', 'train/validation/test split', '#lv3', '모델 학습, 설정 선택, 최종 평가에 데이터를 따로 쓰는 것. 60:20:20 또는 70:15:15.', level=1, family='evaluation'),
 N('method/cross-validation', 'Method', '교차 검증(k겹)', 'k-fold cross-validation', '#lv3', level=2, family='evaluation', domain=['stats', 'ai']),
 N('concept/supervised', 'Concept', '지도 학습', 'supervised learning', '#big', level=1, family='basics'),
 N('concept/unsupervised', 'Concept', '비지도 학습', 'unsupervised learning', '#big', level=1, family='unsupervised'),
 N('concept/reinforcement', 'Concept', '강화 학습', 'reinforcement learning', '#big', level=2, family='rl'),
 N('concept/model-selection', 'Concept', '문제 유형별 모델 선택', 'model selection by problem type', '#lv4', '분류·예측·군집·연관·최적화 유형마다 모델과 평가 지표를 고르는 것.', level=2, family='basics'),
 N('method/association-rules', 'Method', '연관성 분석(장바구니 분석)', 'association rules / market basket', '#lv4', '항목의 동시 발생 패턴에서 "A를 사면 B도 산다" 규칙을 찾는 방법. Apriori, FP-Growth.', level=2, family='unsupervised', domain=['biz', 'ai']),
 N('metric/support', 'Metric', '지지도', 'support', '#lv4', 'A와 B를 함께 산 거래의 비율.', level=1, family='evaluation'),
 N('metric/confidence', 'Metric', '신뢰도', 'confidence', '#lv4', 'A를 산 거래 중 B도 산 비율.', level=1, family='evaluation'),
 N('metric/lift', 'Metric', '향상도', 'lift', '#lv4', level=2, family='evaluation'),
 N('metric/accuracy', 'Metric', '정확도', 'accuracy', '#lv2', '전체 예측 중 맞힌 비율.', level=1, family='evaluation'),
 N('limitation/who-makes-rules', 'Limitation', '규칙을 누가 만들지 모름', 'who makes the rules', '#lv1'),
 N('limitation/rectangle', 'Limitation', '네모 규칙은 비스듬한 경계를 못 따라감', 'axis-aligned rules miss diagonal boundaries', '#lv2'),
 N('limitation/memorized', 'Limitation', '외웠는지 배웠는지 모름', 'memorized or learned?', '#lv2'),
 N('limitation/other-problem-types', 'Limitation', '분류 외 문제 유형', 'other problem types', '#lv3'),
 N('limitation/fairness', 'Limitation', '알고리즘 편향·설명 가능성', 'algorithmic bias and explainability', '#sum', '모델 선택은 정확도뿐 아니라 공정성·설명 가능성·개인정보 보호를 함께 따져야 한다.'),
 N('claim/lift-125', 'Claim', '라면→달걀: 지지도 0.6, 신뢰도 1.0, 향상도 1.25', 'ramen→egg lift 1.25', '#lv4', source=[{'cite': '교안 4주차', 'loc': '3교시 2'}]),
 N('claim/split-ratio', 'Claim', '훈련·검증·시험은 60:20:20 또는 70:15:15로 나누는 경우가 많다', 'common split ratios', '#lv3', source=[{'cite': '교안 4주차', 'loc': '2교시 2'}]),
 N('question/core', 'Question', '이 문제에는 어떤 도구와 알고리즘을 써야 할까?', 'Which tool and algorithm fit this problem?', '#hero'),
 N('question/duel', 'Question', '전문가 규칙이냐, 머신러닝이냐?', 'Expert rule or machine learning?', '#duel'),
 N('analogy/locked-exam', 'Analogy', '봉인한 시험지 ↔ 시험 데이터', 'sealed exam ↔ test set', '#lv3', anchorType='B'),
 N('analogy/instruments', 'Analogy', '실험 장비 고르기 ↔ 분석 도구 고르기', 'choosing instruments ↔ choosing tools', '#lv1', anchorType='B'),
 N('sim/w04-tools', 'Simulation', '도구 추천기', 'tool chooser', '#lv1'),
 N('sim/w04-loan', 'Simulation', '대출 600·400건 규칙 vs KNN', 'loan rule vs KNN', '#lv2'),
 N('sim/w04-cv', 'Simulation', 'K와 5겹 교차 검증', 'K and 5-fold CV', '#lv3'),
 N('sim/w04-basket', 'Simulation', '장바구니 계산기', 'market basket calculator', '#lv4'),
 N('work/ahn-dsb-w04', 'Work', '안상선, 비즈니스를위한데이터과학 교안 4주차', 'Ahn, DSB lecture notes week 4', '#footer'),
]

EDGES = [
 ('lab:concept/analysis-tools', 'lab:prerequisiteOf', 'lab:concept/rule-vs-ml', '#lv2'),
 ('lab:concept/reproducibility', 'lab:partOf', 'lab:concept/analysis-tools', '#lv1'),
 ('lab:concept/analysis-tools', 'lab:hasLimitation', 'lab:limitation/who-makes-rules', '#lv1'),
 ('lab:limitation/who-makes-rules', 'lab:addressedBy', 'lab:concept/rule-vs-ml', '#lv2'),
 ('lab:method/expert-rule', 'lab:contrastsWith', 'lab:method/knn', '#duel'),
 ('lab:method/expert-rule', 'lab:partOf', 'lab:concept/rule-vs-ml', '#lv2'),
 ('lab:method/knn', 'lab:partOf', 'lab:concept/rule-vs-ml', '#lv2'),
 ('lab:method/expert-rule', 'lab:hasLimitation', 'lab:limitation/rectangle', '#lv2'),
 ('lab:limitation/rectangle', 'lab:addressedBy', 'lab:method/knn', '#lv2'),
 ('lab:method/knn', 'lab:solves', 'lab:task/loan-screening', '#lv2'),
 ('lab:method/expert-rule', 'lab:solves', 'lab:task/loan-screening', '#lv2'),
 ('lab:task/loan-screening', 'lab:evaluatedBy', 'lab:metric/accuracy', '#duel'),
 ('lab:method/expert-rule', 'lab:relatedTo', 'lab:concept/interpretability', '#lv2'),
 ('lab:method/knn', 'lab:broader', 'lab:concept/supervised', '#big'),
 ('lab:concept/rule-vs-ml', 'lab:hasLimitation', 'lab:limitation/memorized', '#lv2'),
 ('lab:limitation/memorized', 'lab:addressedBy', 'lab:method/cross-validation', '#lv3'),
 ('lab:concept/rule-vs-ml', 'lab:prerequisiteOf', 'lab:concept/overfitting', '#lv3'),
 ('lab:method/data-split', 'lab:prerequisiteOf', 'lab:method/cross-validation', '#lv3'),
 ('lab:concept/overfitting', 'lab:addressedBy', 'lab:method/data-split', '#lv3'),
 ('lab:method/cross-validation', 'lab:hasLimitation', 'lab:limitation/other-problem-types', '#lv3'),
 ('lab:limitation/other-problem-types', 'lab:addressedBy', 'lab:concept/model-selection', '#lv4'),
 ('lab:method/cross-validation', 'lab:prerequisiteOf', 'lab:concept/model-selection', '#lv4'),
 ('lab:method/association-rules', 'lab:partOf', 'lab:concept/model-selection', '#lv4'),
 ('lab:method/association-rules', 'lab:broader', 'lab:concept/unsupervised', '#lv4'),
 ('lab:method/association-rules', 'lab:evaluatedBy', 'lab:metric/support', '#lv4'),
 ('lab:method/association-rules', 'lab:evaluatedBy', 'lab:metric/confidence', '#lv4'),
 ('lab:method/association-rules', 'lab:evaluatedBy', 'lab:metric/lift', '#lv4'),
 ('lab:metric/confidence', 'lab:prerequisiteOf', 'lab:metric/lift', '#lv4'),
 ('lab:concept/supervised', 'lab:contrastsWith', 'lab:concept/unsupervised', '#big'),
 ('lab:concept/reinforcement', 'lab:contrastsWith', 'lab:concept/supervised', '#big'),
 ('lab:concept/model-selection', 'lab:hasLimitation', 'lab:limitation/fairness', '#sum'),
 ('lab:limitation/fairness', 'lab:relatedTo', 'lab:concept/interpretability', '#sum'),
 ('lab:concept/analysis-tools', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:task/loan-screening', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/locked-exam', 'lab:analogyOf', 'lab:method/data-split', '#lv3'),
 ('lab:analogy/instruments', 'lab:analogyOf', 'lab:concept/analysis-tools', '#lv1'),
 ('lab:concept/analysis-tools', 'lab:demonstratedBy', 'lab:sim/w04-tools', '#lv1'),
 ('lab:concept/rule-vs-ml', 'lab:demonstratedBy', 'lab:sim/w04-loan', '#lv2'),
 ('lab:method/cross-validation', 'lab:demonstratedBy', 'lab:sim/w04-cv', '#lv3'),
 ('lab:method/association-rules', 'lab:demonstratedBy', 'lab:sim/w04-basket', '#lv4'),
 ('lab:claim/lift-125', 'lab:supports', 'lab:metric/lift', '#lv4'), ('lab:claim/lift-125', 'lab:assertedIn', 'lab:work/ahn-dsb-w04', '#lv4'),
 ('lab:claim/split-ratio', 'lab:supports', 'lab:method/data-split', '#lv3'), ('lab:claim/split-ratio', 'lab:assertedIn', 'lab:work/ahn-dsb-w04', '#lv3'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w04', 'report', '비즈니스를위한데이터과학 강의 교안: 04. 데이터 분석 개념의 이해', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/lift-125', 'lab:claim/split-ratio', 'lab:concept/analysis-tools', 'lab:concept/rule-vs-ml', 'lab:method/cross-validation'], 'lab:work/ahn-dsb-w04',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/lift-125', 'loc': '3교시 2. 연관성 분석'}, {'claim': 'lab:claim/split-ratio', 'loc': '2교시 2. 교차 검증과 과적합'}]),
]
