# 특강 ① · 이상 탐지 (인포그래픽 「Anomaly Detection Mathematics」를 연구실 형식으로)
SLUG = 'dsb_s1_anomaly_detection'
FILE = 'special01_anomaly_detection.html'
NUMLABEL = '특강 ①'
TITLE = '평소와 다른 한 건 찾기 — 이상 탐지의 다섯 도구'
DESC = '비즈니스를 위한 데이터 과학 연구실 특강 ①. Z 점수, 마할라노비스 거리, 고립 숲(Isolation Forest), 오토인코더의 복원 오차, 문턱값 정하기를 법인카드·출장비·결제·매장 방문객 예시로 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 밤의 연구실에서 수많은 초록 점 사이에 홀로 붉게 빛나는 점 하나를 돋보기와 주판으로 살피는 표지'
COVER_PROP = '🔎'
SEARCH_PH = '예: Z 점수, 마할라노비스, 고립 숲, 경로 길이, 복원 오차, 문턱값'
OGIMG = 'img/og_index.jpg'
FOOT_ORIGIN = ('이 페이지는 소셜미디어에 공유된 인포그래픽 「Anomaly Detection Mathematics」(작성자 미상)의 여섯 칸을 연구실 해설 형식으로 다시 쓴 특강입니다. '
               '인포그래픽의 3번(오토인코더)과 4번(고립 숲) 순서를 바꾸고, 각 칸의 쓰는 조건과 한계를 덧붙였습니다. 수식은 원 논문과 scikit-learn 문서로 확인했습니다.')
NAV = [('#story', '이야기'), ('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① Z 점수'), ('#lv2', '② 마할라노비스'), ('#lv3', '③ 고립 숲'), ('#lv4', '④ 복원 오차'), ('#lv5', '⑤ 문턱값'), ('#duel', '대결'), ('#sum', '정리'), ('#myth', '오해'), ('#code', '코드')]
PREVNEXT = '<a href="week14_advanced_analytics.html"><small>← 함께 보기 · 14주차</small>정답 없이, 글 속에서, 층을 쌓아</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week07_model_evaluation.html"><small>함께 보기 · 7주차</small>정확도 95%의 함정 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think', 'doc_board', 'fly_type', 'robo_wow', 'doc_magic']
ABOUT = ['lab:method/z-score', 'lab:method/mahalanobis', 'lab:method/isolation-forest', 'lab:method/reconstruction-error', 'lab:method/thresholding']
KGPATH = ['method/z-score', 'limitation/one-column', 'method/mahalanobis', 'limitation/one-oval', 'method/isolation-forest', 'limitation/many-columns', 'method/reconstruction-error', 'limitation/score-not-decision', 'method/thresholding']
TODO = ['인포그래픽 원 작성자·게시일 확인 (사용자 제공 이미지, 작성자 미상)', 'Mahalanobis(1936) DOI 없음 — 원문 서지만 확인']

SOURCES = [
 '[1] 「Anomaly Detection Mathematics」 인포그래픽 (작성자 미상, 소셜미디어 게시물, 2026-11 사용자 제공). — 여섯 칸(Z 점수, 마할라노비스 거리, 복원 오차, 고립 기반 점수, 문턱값, 파이썬 코드)과 핵심 정리의 구성·수식을 이 페이지의 뼈대로 삼음.',
 '[2] Liu, F. T., Ting, K. M., &amp; Zhou, Z.-H. (2008). Isolation Forest. <i>Proceedings of the 8th IEEE International Conference on Data Mining (ICDM 2008)</i>, 413–422. <a href="https://doi.org/10.1109/ICDM.2008.17" target="_blank" rel="noopener">doi:10.1109/ICDM.2008.17</a> — 점수 s(x) = 2^(−E[h(x)]/c(n)), c(n), 표본 크기 256, 나무 100그루.',
 '[3] Mahalanobis, P. C. (1936). On the generalised distance in statistics. <i>Proceedings of the National Institute of Sciences of India</i>, 2(1), 49–55.',
 '[4] Chandola, V., Banerjee, A., &amp; Kumar, V. (2009). Anomaly detection: A survey. <i>ACM Computing Surveys</i>, 41(3), Article 15. <a href="https://doi.org/10.1145/1541880.1541882" target="_blank" rel="noopener">doi:10.1145/1541880.1541882</a>',
 '[5] Baldi, P., &amp; Hornik, K. (1989). Neural networks and principal component analysis: Learning from examples without local minima. <i>Neural Networks</i>, 2(1), 53–58. <a href="https://doi.org/10.1016/0893-6080(89)90014-2" target="_blank" rel="noopener">doi:10.1016/0893-6080(89)90014-2</a> — 직선(선형) 오토인코더는 주성분 분석과 같은 공간을 배운다.',
 '[6] scikit-learn 문서: <a href="https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html" target="_blank" rel="noopener">IsolationForest</a> (2026-11-10 확인, 1.5판 기준 문구) — score_samples는 원 논문 점수의 반대 부호(낮을수록 이상), fit_predict는 이상 −1·정상 1, contamination 기본값 "auto".',
 '[7] 함께 읽기: 안상선 (2024). 금융 분야의 이상탐지 모델 보안을 위한 통계 기반의 적대적 데이터 대응 방안 — 실증적 분석과 시뮬레이션 결과. <i>미래사회</i>, 15(3), 147–166. <a href="https://doi.org/10.22987/jifso.2024.15.3.147" target="_blank" rel="noopener">doi:10.22987/jifso.2024.15.3.147</a> · 연구실 해설: <a href="https://adminmrobo.github.io/my_article_04_adversarial_finance_attack/01_adversarial_finance.html" target="_blank" rel="noopener">적대적 데이터와 금융 이상 탐지</a>']
ILLUSTRATIVE = [
 '①칸 식대 결제 200건, ②칸 출장 150건, ③칸 결제 292건, ④칸 매장 방문객 146일, ⑤칸 결제 574건, 대결의 결제 292건은 모두 설명용 예시 데이터입니다. 실제 회사·카드사의 데이터가 아닙니다.',
 '③칸·⑤칸·대결의 고립 숲은 브라우저에서 원 논문 방식대로 직접 만든 것입니다(나무 100그루, 나무마다 256건을 중복 없이 뽑음, 깊이 제한 8). scikit-learn과 난수가 달라 점수가 조금 다릅니다.',
 '④칸의 오토인코더는 "직선 오토인코더"로, 주성분 분석과 같은 답을 냅니다[5]. 실제 현장의 오토인코더는 곡선(비선형) 층을 쓰는 신경망인 경우가 많습니다.',
 '⑤칸의 점검 비용(1건 2만 원)과 놓친 이상의 손실(기본 60만 원)은 예시값입니다.']

GL = {
 '이상 탐지': ['이상 탐지', '개념', '대부분의 데이터와 다르게 움직이는 드문 데이터를 찾아내는 일. 사기 결제·설비 고장·전표 오류 찾기에 쓴다.', 'lab:concept/anomaly-detection', 'anomaly detection', '#big'],
 '이상 점수': ['이상 점수', '개념', '한 건이 얼마나 "평소와 다른지"를 숫자 하나로 나타낸 것. 도구마다 계산법이 다르다.', 'lab:concept/anomaly-score', 'anomaly score', '#big'],
 'Z 점수': ['Z 점수', '통계', '(값 − 평균) ÷ 표준편차. 평균에서 표준편차 몇 개만큼 떨어졌는지.', 'lab:method/z-score'],
 '표준편차': ['표준편차', '통계', '값들이 평균에서 평균적으로 얼마나 퍼져 있는지 나타내는 숫자.', None],
 '중앙값': ['중앙값', '통계', '값을 크기순으로 줄 세웠을 때 한가운데 값. 극단값에 덜 흔들린다.', None],
 '가림 효과': ['가림 효과', '함정', '아주 큰 이상치가 평균과 표준편차를 부풀려, 다른 이상치를 평범해 보이게 하는 현상.', 'lab:concept/masking', 'masking effect', '#lv1'],
 '마할라노비스 거리': ['마할라노비스 거리', '통계', '변수끼리 함께 움직이는 관계(공분산)를 반영해 잰 거리. 관계를 깨는 점이 멀게 나온다.', 'lab:method/mahalanobis'],
 '공분산': ['공분산', '통계', '두 변수가 함께 커지고 작아지는 정도. 표로 모은 것이 공분산 행렬 Σ.', None],
 '고립 숲': ['고립 숲(Isolation Forest)', '머신러닝', '무작위로 선을 그어 한 점을 따로 떼어 내기까지 걸리는 횟수로 이상을 재는 방법. 빨리 떨어지면 이상.', 'lab:method/isolation-forest'],
 '경로 길이': ['경로 길이 h(x)', '고립 숲', '나무의 뿌리에서 그 점이 혼자 남는 칸까지 내려간 단계 수.', None],
 '오토인코더': ['오토인코더', '딥러닝', '입력을 좁은 병목으로 줄였다가 다시 펼쳐 원래대로 복원하도록 배우는 신경망.', 'lab:method/autoencoder', 'autoencoder', '#lv4'],
 '복원 오차': ['복원 오차', '딥러닝', '원래 값과 복원한 값의 차이를 제곱해 더한 것. 크면 평소 패턴과 다르다는 뜻.', 'lab:method/reconstruction-error'],
 '병목': ['병목', '딥러닝', '오토인코더 가운데의 좁은 층. 몇 개의 숫자로 요약할지를 정한다.', None],
 '문턱값': ['문턱값 τ(타우)', '결정', '이상 점수가 이 값을 넘으면 "이상"으로 표시하는 경계선.', 'lab:method/thresholding'],
 '오경보': ['오경보', '평가', '정상인데 이상으로 표시한 경우(7주차의 거짓 양성).', None],
 '재현율': ['재현율', '평가', '실제 이상 가운데 잡아낸 비율(7주차).', None],
 '정밀도': ['정밀도', '평가', '이상으로 표시한 것 가운데 진짜 이상의 비율(7주차).', None],
}
CORE = ['이상 탐지', '이상 점수', 'Z 점수', '표준편차', '중앙값', '가림 효과', '마할라노비스 거리', '공분산', '고립 숲', '경로 길이', '오토인코더', '복원 오차', '병목', '문턱값', '오경보', '재현율', '정밀도']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '식대 평균이 5만 원, 표준편차가 2만 원일 때 15만 원 결제의 Z 점수는?', 'o': ['2.5', '5', '7.5'], 'a': 1, 'why': '(15 − 5) ÷ 2 = 5. 평균에서 표준편차 다섯 개만큼 떨어졌습니다.', 'hint': '(값 − 평균) ÷ 표준편차', 'calc': True, 'assess': 'lab:method/z-score'},
  {'id': 'q2', 'q': '48만 원짜리 결제 한 건 때문에 11.8만 원 결제가 문턱을 못 넘은 이유는?', 'o': ['문턱 τ가 너무 낮아서', '큰 이상치가 표준편차를 부풀려서(가림 효과)', '데이터가 너무 많아서'], 'a': 1, 'why': '48만 원 한 건이 표준편차를 약 1.3만 원에서 3.3만 원으로 키웠습니다. 중앙값·MAD로 바꾸면 세 건이 모두 드러납니다.', 'hint': '①칸 "중앙값·MAD" 버튼.', 'assess': 'lab:concept/masking'}],
 'lv2': [
  {'id': 'q3', 'q': '"출장 1일에 출장비 108만 원"이 칸마다 Z 점수로는 평범한데 마할라노비스 거리로는 큰 이유는?', 'o': ['출장비가 너무 커서', '일수와 출장비가 함께 움직이는 관계를 깨서', '일수가 너무 짧아서'], 'a': 1, 'why': '하루 출장도, 108만 원 출장비도 따로 보면 흔합니다. "하루인데 108만 원"이라는 조합이 드뭅니다.', 'hint': '②칸 타원과 상자.', 'assess': 'lab:method/mahalanobis'},
  {'id': 'q4', 'q': '변수 두 개가 정규분포를 따를 때 D² 가 9를 넘을 확률은? (D² 는 자유도 2인 카이제곱 분포, P = e^(−D²/2))', 'o': ['약 1.1%', '약 5%', '약 0.3%'], 'a': 0, 'why': 'e^(−4.5) ≈ 0.011. 변수 한 개일 때 |z| > 3의 확률(약 0.3%)보다 큽니다. 변수가 늘면 같은 문턱에서 걸리는 비율이 달라집니다.', 'hint': 'e^(−9/2)', 'calc': True, 'assess': 'lab:method/mahalanobis'}],
 'lv3': [
  {'id': 'q5', 'q': '고립 숲에서 이상한 점의 평균 경로 길이 E[h(x)]는 보통?', 'o': ['길다 — 깊이 숨어 있어서', '짧다 — 몇 번만 잘라도 혼자 남아서', '정상 점과 같다'], 'a': 1, 'why': '드물고 동떨어진 점은 무작위 선 몇 번에 떨어져 나갑니다. 경로가 짧을수록 s(x)가 1에 가깝습니다.', 'hint': '③칸 "새 나무 한 그루".', 'assess': 'lab:method/isolation-forest'},
  {'id': 'q6', 'q': 'E[h(x)] = c(n)이면 s(x) = 2^(−E[h(x)]/c(n))은?', 'o': ['0', '0.5', '1'], 'a': 1, 'why': '2^(−1) = 0.5. 평균적인 깊이에서 떨어졌다는 뜻으로, 원 논문은 모든 점이 0.5 근처면 뚜렷한 이상이 없다고 봅니다.', 'hint': '2의 −1제곱', 'calc': True, 'assess': 'lab:method/isolation-forest'}],
 'lv4': [
  {'id': 'q7', 'q': '오토인코더가 이상한 날을 찾는 원리는?', 'o': ['이상한 날만 골라 학습한다', '평소 패턴으로만 배워서, 처음 보는 패턴은 잘 복원하지 못한다', '값이 큰 날을 이상으로 본다'], 'a': 1, 'why': '정상으로 확인한 날로 "평소 모양"을 배우면, 다른 모양의 날은 복원 오차가 커집니다.', 'hint': '④칸 "정점 뒤바뀜"', 'assess': 'lab:method/reconstruction-error'},
  {'id': 'q8', 'q': '병목을 24칸(입력과 같은 크기)으로 넓히면?', 'o': ['이상을 더 잘 찾는다', '모든 날을 그대로 베껴 복원 오차가 0이 되어 아무것도 못 찾는다', '학습이 빨라진다'], 'a': 1, 'why': '좁혀야 요약이 되고, 요약에 안 맞는 날이 드러납니다. 넓으면 그냥 베낍니다.', 'hint': '④칸 병목 24', 'assess': 'lab:method/autoencoder'}],
 'lv5': [
  {'id': 'q9', 'q': '점수 문턱을 "상위 1%"로 정했는데 실제 이상이 4%라면?', 'o': ['경보는 정확하지만 많이 놓친다', '오경보가 많아진다', '아무 차이 없다'], 'a': 0, 'why': '경보 수를 1%로 묶으면 진짜 이상의 상당수가 문턱 아래에 남습니다(재현율↓).', 'hint': '⑤칸 상위 p% = 1', 'assess': 'lab:method/thresholding'},
  {'id': 'q10', 'q': '검증 데이터에서 F1이 가장 높은 문턱을 골랐다면, 성적은 어디서 재야 할까?', 'o': ['같은 검증 데이터', '문턱을 고를 때 쓰지 않은 시험 데이터', '전체 데이터'], 'a': 1, 'why': '문턱을 고른 데이터로 채점하면 성적이 부풀려집니다(7주차). 이 칸의 숫자는 모두 시험 데이터 287건 기준입니다.', 'hint': '⑤칸 KPI 아래 설명', 'assess': 'lab:method/thresholding'},
  {'id': 'q11', 'q': 'scikit-learn IsolationForest의 score_samples 값이 더 낮은 점은?', 'o': ['더 정상', '더 이상', '판단할 수 없음'], 'a': 1, 'why': '원 논문 점수의 부호를 뒤집어 "낮을수록 이상"입니다. fit_predict는 이상 −1, 정상 1을 돌려줍니다[6].', 'hint': '코드 상자', 'assess': 'lab:method/isolation-forest'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/anomaly-detection', 'Concept', '이상 탐지', 'anomaly detection', '#big', level=1, family='evaluation'),
 N('concept/anomaly-score', 'Concept', '이상 점수', 'anomaly score', '#big', level=1, family='evaluation'),
 N('task/fraud-screening', 'Task', '결제·전표·설비 이상 골라내기', 'screening unusual records', '#why', level=1, family='basics'),
 N('method/z-score', 'Method', 'Z 점수', 'z-score', '#lv1', level=1, family='basics'),
 N('concept/masking', 'Concept', '가림 효과', 'masking effect', '#lv1', level=2, family='evaluation'),
 N('method/robust-z', 'Method', '중앙값·MAD로 만든 튼튼한 Z 점수', 'robust z-score (median/MAD)', '#lv1', '중앙값과 MAD×1.4826으로 계산해 극단값에 덜 흔들리는 Z 점수.', level=2, family='basics'),
 N('method/mahalanobis', 'Method', '마할라노비스 거리', 'Mahalanobis distance', '#lv2', level=2, family='basics'),
 N('method/isolation-forest', 'Method', '고립 숲', 'Isolation Forest', '#lv3', level=2, family='ensemble'),
 N('method/autoencoder', 'Method', '오토인코더', 'autoencoder', '#lv4', level=3, family='generative'),
 N('method/reconstruction-error', 'Method', '복원 오차', 'reconstruction error', '#lv4', level=3, family='generative'),
 N('method/pca', 'Method', '주성분 분석', 'principal component analysis', '#lv4', '많은 변수를 퍼짐이 가장 큰 축 몇 개로 요약하는 방법.', level=3, family='unsupervised'),
 N('method/thresholding', 'Method', '문턱값 정하기', 'thresholding', '#lv5', level=2, family='evaluation'),
 N('metric/f1', 'Metric', 'F1 점수', 'F1 score', '#lv5', level=2, family='evaluation'),
 N('metric/precision-at-k', 'Metric', '경보 k건 중 진짜 이상 수', 'hits in top-k alarms', '#duel', level=2, family='evaluation'),
 N('limitation/one-column', 'Limitation', '한 번에 한 칸만 본다', 'one column at a time', '#lv1'),
 N('limitation/one-oval', 'Limitation', '데이터가 타원 하나라고 가정한다', 'assumes a single oval', '#lv2'),
 N('limitation/many-columns', 'Limitation', '칸이 많고 패턴이 중요한 데이터에 약하다', 'weak on long patterns', '#lv3'),
 N('limitation/score-not-decision', 'Limitation', '점수는 결정이 아니다', 'a score is not a decision', '#lv4'),
 N('dataset/meal-200', 'Dataset', '예시 식대 결제 200건', 'synthetic meal payments (200)', '#lv1', level=1, family='data'),
 N('dataset/trip-150', 'Dataset', '예시 출장 150건(일수·출장비)', 'synthetic business trips (150)', '#lv2', level=1, family='data'),
 N('dataset/pay-292', 'Dataset', '예시 결제 292건(금액·횟수, 두 무리)', 'synthetic payments, two groups (292)', '#lv3', level=1, family='data'),
 N('dataset/store-146', 'Dataset', '예시 매장 방문객 146일 × 24시간', 'synthetic store traffic (146 days)', '#lv4', level=1, family='data'),
 N('claim/if-score', 'Claim', '고립 숲 점수 s(x)가 1에 가까우면 이상, 모두 0.5 근처면 뚜렷한 이상이 없다', 'IF score near 1 means anomaly', '#lv3', source=[{'cite': 'Liu et al. 2008', 'loc': '2절, 식 (2)'}]),
 N('claim/sklearn-sign', 'Claim', 'scikit-learn score_samples는 원 논문 점수의 반대 부호로, 낮을수록 이상이다', 'sklearn score_samples: lower is more abnormal', '#code', source=[{'cite': 'scikit-learn IsolationForest 문서', 'loc': 'score_samples'}]),
 N('claim/linear-ae-pca', 'Claim', '직선(선형) 오토인코더는 주성분 분석과 같은 공간을 배운다', 'linear autoencoder spans the PCA subspace', '#lv4', source=[{'cite': 'Baldi & Hornik 1989', 'loc': '본문'}]),
 N('question/core', 'Question', '수만 건 가운데 사람이 먼저 봐야 할 이상한 몇 건을 어떻게 고를까?', 'Which few records should a person check first?', '#hero'),
 N('question/duel', 'Question', '무리가 둘인 결제에서, 경보 15건으로 이상을 더 많이 잡는 쪽은?', 'With 15 alarms, which catches more anomalies?', '#duel'),
 N('analogy/receipt', 'Analogy', '영수증 더미에서 튀는 금액 고르기 ↔ Z 점수', 'odd receipt ↔ z-score', '#lv1', anchorType='D'),
 N('analogy/twenty-questions', 'Analogy', '스무고개 몇 번 만에 맞히나 ↔ 고립 숲 경로 길이', 'twenty questions ↔ path length', '#lv3', anchorType='D'),
 N('analogy/copy-memo', 'Analogy', '요점 메모로 다시 쓰기 ↔ 오토인코더 병목', 'summary memo ↔ bottleneck', '#lv4', anchorType='D'),
 N('sim/s1-z', 'Simulation', '식대 Z 점수와 가림 효과', 'meal z-scores and masking', '#lv1'),
 N('sim/s1-maha', 'Simulation', 'Z 상자 vs 마할라노비스 타원', 'z box vs Mahalanobis ellipse', '#lv2'),
 N('sim/s1-if', 'Simulation', '한 점 고립시키기와 점수 지도', 'isolating one point, score map', '#lv3'),
 N('sim/s1-ae', 'Simulation', '24시간 패턴 복원', '24-hour pattern reconstruction', '#lv4'),
 N('sim/s1-th', 'Simulation', '문턱값 방법 비교', 'threshold methods', '#lv5'),
 N('work/infographic', 'Work', '인포그래픽 「Anomaly Detection Mathematics」', 'infographic: Anomaly Detection Mathematics', '#footer'),
 N('work/liu2008', 'Work', 'Liu, Ting, Zhou (2008) Isolation Forest', 'Liu et al. 2008', '#footer'),
 N('work/mahalanobis1936', 'Work', 'Mahalanobis (1936)', 'Mahalanobis 1936', '#footer'),
 N('work/chandola2009', 'Work', 'Chandola, Banerjee, Kumar (2009) 이상 탐지 서베이', 'Chandola et al. 2009', '#footer'),
 N('work/baldi1989', 'Work', 'Baldi, Hornik (1989)', 'Baldi & Hornik 1989', '#footer'),
 N('work/ahn2024adversarial', 'Work', '안상선 (2024) 금융 이상탐지 모델의 적대적 데이터 대응', 'Ahn 2024 adversarial data in financial anomaly detection', '#footer'),
 N('concept/evasion', 'Concept', '문턱 피해 가기(회피)', 'evasion of thresholds', '#lv5', '탐지 규칙이나 문턱을 알고 기록을 평범해 보이게 꾸미는 일.', level=2, family='evaluation'),
 N('work/sklearn-if', 'Work', 'scikit-learn IsolationForest 문서', 'scikit-learn IsolationForest docs', '#footer'),
]

EDGES = [
 ('lab:task/fraud-screening', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:concept/anomaly-score', 'lab:partOf', 'lab:concept/anomaly-detection', '#big'),
 ('lab:concept/anomaly-detection', 'lab:solves', 'lab:task/fraud-screening', '#why'),
 ('lab:method/z-score', 'lab:partOf', 'lab:concept/anomaly-detection', '#lv1'),
 ('lab:method/z-score', 'lab:evaluatedOn', 'lab:dataset/meal-200', '#lv1'),
 ('lab:concept/masking', 'lab:addressedBy', 'lab:method/robust-z', '#lv1'),
 ('lab:method/z-score', 'lab:hasLimitation', 'lab:concept/masking', '#lv1'),
 ('lab:method/robust-z', 'lab:broader', 'lab:method/z-score', '#lv1'),
 ('lab:method/z-score', 'lab:hasLimitation', 'lab:limitation/one-column', '#lv1'),
 ('lab:limitation/one-column', 'lab:addressedBy', 'lab:method/mahalanobis', '#lv2'),
 ('lab:method/z-score', 'lab:prerequisiteOf', 'lab:method/mahalanobis', '#lv2'),
 ('lab:method/mahalanobis', 'lab:partOf', 'lab:concept/anomaly-detection', '#lv2'),
 ('lab:method/mahalanobis', 'lab:evaluatedOn', 'lab:dataset/trip-150', '#lv2'),
 ('lab:method/mahalanobis', 'lab:hasLimitation', 'lab:limitation/one-oval', '#lv2'),
 ('lab:limitation/one-oval', 'lab:addressedBy', 'lab:method/isolation-forest', '#lv3'),
 ('lab:method/mahalanobis', 'lab:prerequisiteOf', 'lab:method/isolation-forest', '#lv3'),
 ('lab:method/isolation-forest', 'lab:partOf', 'lab:concept/anomaly-detection', '#lv3'),
 ('lab:method/isolation-forest', 'lab:evaluatedOn', 'lab:dataset/pay-292', '#lv3'),
 ('lab:method/isolation-forest', 'lab:hasLimitation', 'lab:limitation/many-columns', '#lv3'),
 ('lab:limitation/many-columns', 'lab:addressedBy', 'lab:method/reconstruction-error', '#lv4'),
 ('lab:method/isolation-forest', 'lab:prerequisiteOf', 'lab:method/reconstruction-error', '#lv4'),
 ('lab:method/reconstruction-error', 'lab:partOf', 'lab:method/autoencoder', '#lv4'),
 ('lab:method/autoencoder', 'lab:partOf', 'lab:concept/anomaly-detection', '#lv4'),
 ('lab:method/pca', 'lab:relatedTo', 'lab:method/autoencoder', '#lv4'),
 ('lab:method/reconstruction-error', 'lab:evaluatedOn', 'lab:dataset/store-146', '#lv4'),
 ('lab:method/reconstruction-error', 'lab:hasLimitation', 'lab:limitation/score-not-decision', '#lv4'),
 ('lab:limitation/score-not-decision', 'lab:addressedBy', 'lab:method/thresholding', '#lv5'),
 ('lab:method/reconstruction-error', 'lab:prerequisiteOf', 'lab:method/thresholding', '#lv5'),
 ('lab:concept/anomaly-score', 'lab:prerequisiteOf', 'lab:method/thresholding', '#lv5'),
 ('lab:method/thresholding', 'lab:evaluatedBy', 'lab:metric/f1', '#lv5'),
 ('lab:method/isolation-forest', 'lab:contrastsWith', 'lab:method/z-score', '#duel'),
 ('lab:method/isolation-forest', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:question/duel', 'lab:evaluatedBy', 'lab:metric/precision-at-k', '#duel'),
 ('lab:analogy/receipt', 'lab:analogyOf', 'lab:method/z-score', '#lv1'),
 ('lab:analogy/twenty-questions', 'lab:analogyOf', 'lab:method/isolation-forest', '#lv3'),
 ('lab:analogy/copy-memo', 'lab:analogyOf', 'lab:method/autoencoder', '#lv4'),
 ('lab:method/z-score', 'lab:demonstratedBy', 'lab:sim/s1-z', '#lv1'),
 ('lab:method/mahalanobis', 'lab:demonstratedBy', 'lab:sim/s1-maha', '#lv2'),
 ('lab:method/isolation-forest', 'lab:demonstratedBy', 'lab:sim/s1-if', '#lv3'),
 ('lab:method/reconstruction-error', 'lab:demonstratedBy', 'lab:sim/s1-ae', '#lv4'),
 ('lab:method/thresholding', 'lab:demonstratedBy', 'lab:sim/s1-th', '#lv5'),
 ('lab:claim/if-score', 'lab:supports', 'lab:method/isolation-forest', '#lv3'), ('lab:claim/if-score', 'lab:assertedIn', 'lab:work/liu2008', '#lv3'),
 ('lab:claim/sklearn-sign', 'lab:supports', 'lab:method/isolation-forest', '#code'), ('lab:claim/sklearn-sign', 'lab:assertedIn', 'lab:work/sklearn-if', '#code'),
 ('lab:claim/linear-ae-pca', 'lab:supports', 'lab:method/autoencoder', '#lv4'), ('lab:claim/linear-ae-pca', 'lab:assertedIn', 'lab:work/baldi1989', '#lv4'),
 ('lab:method/mahalanobis', 'lab:assertedIn', 'lab:work/mahalanobis1936', '#footer'),
 ('lab:concept/anomaly-detection', 'lab:assertedIn', 'lab:work/chandola2009', '#footer'),
 ('lab:concept/anomaly-detection', 'lab:assertedIn', 'lab:work/infographic', '#footer'),
 ('lab:method/thresholding', 'lab:hasLimitation', 'lab:concept/evasion', '#lv5'),
 ('lab:concept/evasion', 'lab:assertedIn', 'lab:work/ahn2024adversarial', '#lv5'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn2024adversarial', 'article-journal', '금융 분야의 이상탐지 모델 보안을 위한 통계 기반의 적대적 데이터 대응 방안 - 실증적 분석과 시뮬레이션 결과 -', [{'family': '안', 'given': '상선'}], 2024, 'background',
   ['lab:concept/evasion'], 'lab:work/ahn2024adversarial',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': True, 'pages': True}, '저자 해설 페이지로 확인 2026-11-10', '함께 읽기',
   **{'container-title': '미래사회', 'volume': '15', 'issue': '3', 'page': '147-166', 'DOI': '10.22987/jifso.2024.15.3.147'}),
 R('anon_anomaly_infographic', 'webpage', 'Anomaly Detection Mathematics (infographic)', [{'literal': '작성자 미상'}], None, 'primary',
   ['lab:concept/anomaly-detection', 'lab:method/z-score', 'lab:method/mahalanobis', 'lab:method/isolation-forest', 'lab:method/reconstruction-error', 'lab:method/thresholding'], 'lab:work/infographic',
   {'title': True, 'authors': False, 'year': False, 'venue': False, 'doi': False, 'pages': False}, '사용자가 제공한 이미지로 확인 2026-11-10', '소셜미디어 게시물, 원 작성자·게시일 미확인'),
 R('liu2008isolation', 'paper-conference', 'Isolation Forest', [{'family': 'Liu', 'given': 'Fei Tony'}, {'family': 'Ting', 'given': 'Kai Ming'}, {'family': 'Zhou', 'given': 'Zhi-Hua'}], 2008, 'primary',
   ['lab:claim/if-score', 'lab:method/isolation-forest'], 'lab:work/liu2008',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': True, 'pages': True}, 'researchr.org 서지로 확인 2026-11-10', '',
   **{'container-title': 'Proceedings of the 8th IEEE International Conference on Data Mining (ICDM 2008)', 'page': '413-422', 'DOI': '10.1109/ICDM.2008.17', 'publisher': 'IEEE Computer Society',
      'locs': [{'claim': 'lab:claim/if-score', 'loc': '2절 (anomaly score s(x, n))'}]}),
 R('mahalanobis1936generalised', 'article-journal', 'On the generalised distance in statistics', [{'family': 'Mahalanobis', 'given': 'P. C.'}], 1936, 'background',
   ['lab:method/mahalanobis'], 'lab:work/mahalanobis1936',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': True}, '서지 데이터베이스로 확인 2026-11-10', 'DOI 없음',
   **{'container-title': 'Proceedings of the National Institute of Sciences of India', 'volume': '2', 'issue': '1', 'page': '49-55'}),
 R('chandola2009anomaly', 'article-journal', 'Anomaly detection: A survey', [{'family': 'Chandola', 'given': 'Varun'}, {'family': 'Banerjee', 'given': 'Arindam'}, {'family': 'Kumar', 'given': 'Vipin'}], 2009, 'background',
   ['lab:concept/anomaly-detection'], 'lab:work/chandola2009',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': True, 'pages': False}, '저자 페이지·DOI 검색으로 확인 2026-11-10', 'Article 15 (쪽 범위 없음)',
   **{'container-title': 'ACM Computing Surveys', 'volume': '41', 'issue': '3', 'number': '15', 'DOI': '10.1145/1541880.1541882'}),
 R('baldi1989neural', 'article-journal', 'Neural networks and principal component analysis: Learning from examples without local minima', [{'family': 'Baldi', 'given': 'Pierre'}, {'family': 'Hornik', 'given': 'Kurt'}], 1989, 'background',
   ['lab:claim/linear-ae-pca'], 'lab:work/baldi1989',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': True, 'pages': True}, 'scilit 서지로 확인 2026-11-10', '',
   **{'container-title': 'Neural Networks', 'volume': '2', 'issue': '1', 'page': '53-58', 'DOI': '10.1016/0893-6080(89)90014-2'}),
 R('sklearn_isolationforest', 'webpage', 'sklearn.ensemble.IsolationForest', [{'literal': 'scikit-learn developers'}], None, 'software',
   ['lab:claim/sklearn-sign'], 'lab:work/sklearn-if',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서(1.5판) 확인 2026-11-10', '',
   URL='https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html', locs=[{'claim': 'lab:claim/sklearn-sign', 'loc': 'score_samples, fit_predict'}]),
]

CSS = '''
.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:13px;color:var(--muted)}
.legend i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:5px;vertical-align:-1px}
pre.code{background:var(--panel2);border:1px solid var(--rule);border-radius:10px;padding:14px;overflow-x:auto;font-size:13px;line-height:1.6;white-space:pre}
 .cloud{background:rgba(176,124,255,.08);border:1px dashed var(--c-doc);border-radius:16px;padding:14px 18px;position:relative}
.cloud b{color:var(--c-doc);display:block;margin-bottom:4px}
.cloud p{margin:0}
.myth{background:rgba(240,96,77,.08);border-left:3px solid var(--eye);border-radius:10px;padding:12px 16px}
.myth b{color:var(--eye)}
.myth p{margin:6px 0 0}
.origin{border-left:3px solid var(--info);padding:6px 0 6px 14px;color:var(--muted);font-size:14px}
'''
