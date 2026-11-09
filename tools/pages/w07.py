# 7주차 · 비즈니스 데이터 분석 모델의 평가
SLUG = 'dsb_w07_model_evaluation'
FILE = 'week07_model_evaluation.html'
TITLE = '정확도 95%의 함정 — 비즈니스 데이터 분석 모델의 평가'
DESC = '비즈니스를 위한 데이터 과학 7주차 연구실 해설. 이탈 예측 예시로 혼동행렬, 정밀도·재현율·F1, ROC·AUC를 움직여 보고, 앙상블과 학습률·배치를 실험한 뒤 비용 기반 임계값으로 캠페인 순이익을 겨룬다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 2×2 칸의 커다란 성적표 앞에서 저울로 두 종류의 오류 무게를 다는 표지'
COVER_PROP = '⚖️'
SEARCH_PH = '예: 혼동행렬, 재현율, F1, ROC, AUC, 배깅, 학습률'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 혼동행렬'), ('#lv2', '② 정밀도·재현율'), ('#lv3', '③ ROC·AUC'), ('#lv4', '④ 앙상블'), ('#lv5', '⑤ 학습률'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week06_classification_2.html"><small>← 이전 · 6주차</small>농어가 끼어들자</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week08_practice_1.html"><small>다음 · 8주차</small>연습 ① 1~7주차 문제풀이 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'robo_meh', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify', 'robo_calc', 'doc_think']
ABOUT = ['lab:concept/confusion-matrix', 'lab:metric/precision-recall', 'lab:metric/roc-auc', 'lab:method/ensemble', 'lab:concept/learning-rate-batch', 'lab:method/cost-threshold']
KGPATH = ['concept/confusion-matrix', 'limitation/no-alt-metric', 'metric/precision-recall', 'limitation/threshold-dependent', 'metric/roc-auc', 'limitation/eval-not-improve', 'method/ensemble', 'limitation/single-learner', 'concept/learning-rate-batch', 'limitation/no-money', 'method/cost-threshold']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '"유지 비용이 신규 획득보다 5~25배 저렴" 원칙의 원 출처 확인(교안 인용)']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 07. 비즈니스 데이터 분석 모델의 평가. 인공지능융합학과. — 혼동행렬(TP·TN·FP·FN, 1종·2종 오류), 정확도·정밀도·재현율·F1, 공항 수하물 검사 비유, ROC·TPR·FPR·임계값·AUC 해석, macro·weighted·micro 평균, KNN·SVM 최적화, 특성 공학·스케일링, 배깅·부스팅·스태킹, 배치·에포크·학습률, K-폴드 교차검증, 고객 세분화(RFM)·이탈 예측·추천·캠페인 최적화는 교안 본문을 옮김. 실습 링크: <a href="https://colab.research.google.com/drive/19DG0jyEa9xiO42jNdu3ykKWLWlf8AbZk?usp=sharing" target="_blank" rel="noopener">Colab</a>',
 '[2] scikit-learn 문서: <a href="https://scikit-learn.org/stable/modules/model_evaluation.html" target="_blank" rel="noopener">Metrics and scoring</a> — confusion_matrix, precision_score, recall_score, f1_score, roc_curve, roc_auc_score.',
 '[3] Fawcett, T. (2006). An introduction to ROC analysis. Pattern Recognition Letters, 27(8), 861–874. — AUC의 순위 확률 해석.']
ILLUSTRATIVE = [
 '이 페이지의 고객 데이터(이용 감소율·불만 문의, 이탈 여부)는 모두 설명용으로 만든 예시 데이터입니다. 실제 기업 데이터가 아닙니다.',
 '④칸 앙상블은 개별 정확도 p인 가상의 모델들을 모의실험한 것입니다(문제 3,000개, 시드 77).',
 '대결의 쿠폰값(2만 원)·고객 가치(30만 원)·쿠폰 효과(절반 유지)는 설명용 가정입니다.']

GL = {
 '혼동행렬': ['혼동행렬(Confusion Matrix)', '평가', '행에 실제, 열에 예측을 놓고 맞힘·틀림을 네 칸(TP·TN·FP·FN)으로 센 표.', 'lab:concept/confusion-matrix'],
 '1종 오류': ['1종 오류(FP, 거짓 경보)', '평가', '실제로는 음성인데 양성으로 판정한 오류. 불필요한 조치·비용을 부른다.', None],
 '2종 오류': ['2종 오류(FN, 누락)', '평가', '실제로는 양성인데 음성으로 판정한 오류. 의료·보안에서 치명적일 수 있다.', None],
 '정밀도': ['정밀도(Precision)', '지표', 'TP ÷ (TP + FP). "양성이라고 한 것 중 실제 양성의 비율".', 'lab:metric/precision-recall'],
 '재현율': ['재현율(Recall, TPR)', '지표', 'TP ÷ (TP + FN). "실제 양성 중 찾아낸 비율".', None],
 'F1': ['F1-Score', '지표', '정밀도와 재현율의 조화평균. 2PR ÷ (P + R). 둘 중 하나라도 낮으면 낮아진다.', None],
 '임계값': ['임계값(Threshold)', '평가', '예측 확률이 이 값 이상이면 양성으로 판정하는 기준. 사람이 정한다.', None],
 'ROC 곡선': ['ROC 곡선', '평가', '임계값을 바꾸며 얻은 (FPR, TPR) 점을 이은 곡선. 왼쪽 위에 붙을수록 좋다.', 'lab:metric/roc-auc'],
 'AUC': ['AUC', '지표', 'ROC 곡선 아래 넓이. 0.5는 무작위, 1은 완벽. 양성이 음성보다 높은 점수를 받을 확률.', None],
 'FPR': ['FPR(위양성률)', '지표', 'FP ÷ (FP + TN). 실제 음성 중 양성으로 잘못 판정한 비율.', None],
 '앙상블': ['앙상블', '방법', '여러 모델을 결합해 단일 모델보다 나은 성능을 얻는 방법. 배깅·부스팅·스태킹·보팅.', 'lab:method/ensemble'],
 '배깅': ['배깅(Bagging)', '앙상블', '복원 추출로 만든 여러 데이터셋에 모델을 학습해 평균·다수결. 랜덤 포레스트.', None],
 '부스팅': ['부스팅(Boosting)', '앙상블', '앞 모델이 틀린 곳을 다음 모델이 집중 학습하는 순차 방식. AdaBoost, XGBoost, LightGBM.', None],
 '스태킹': ['스태킹(Stacking)', '앙상블', '여러 기본 모델의 예측을 메타 모델이 다시 학습해 종합하는 방식.', None],
 '에포크': ['에포크(Epoch)', '학습', '훈련 데이터 전체를 한 번 다 학습한 단위.', 'lab:concept/learning-rate-batch'],
 '배치': ['배치(Batch)', '학습', '한 번의 갱신에 쓰는 데이터 묶음. 풀 배치·미니 배치·SGD(1개).', None],
 '학습률': ['학습률(Learning Rate)', '학습', '한 번의 갱신에서 얼마나 크게 고칠지 정하는 값. 크면 헤매고 작으면 느리다.', None],
 '클래스 불균형': ['클래스 불균형', '데이터', '한 클래스가 다른 클래스보다 훨씬 많은 상태. 정확도를 부풀린다.', None],
 'RFM': ['RFM', '마케팅', 'Recency(최근성)·Frequency(빈도)·Monetary(금액). 고객 세분화 특성.', None],
 'CLV': ['CLV(고객 생애 가치)', '마케팅', '한 고객이 거래 기간 전체에 걸쳐 가져다줄 가치.', None],
}
CORE = ['혼동행렬', '1종 오류', '2종 오류', '정밀도', '재현율', 'F1', '임계값', 'ROC 곡선', 'AUC', '앙상블', '배깅', '부스팅', '에포크', '학습률', '클래스 불균형']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': 'Confusion Matrix에서 실제로는 양성인데 모델이 음성으로 잘못 예측한 경우는? (교안 연습문제 1)', 'o': ['TP', 'TN', 'FP', 'FN'], 'a': 3, 'why': 'FN(False Negative)은 2종 오류, 누락입니다.', 'hint': '①칸 표의 위 오른쪽 칸.', 'assess': 'lab:concept/confusion-matrix'},
  {'id': 'q2', 'q': '고객 1,000명 중 이탈 30명. "아무도 이탈 안 함"이라고만 답하는 모델의 정확도는?', 'o': ['3%', '50%', '97%'], 'a': 2, 'why': 'TN 970 ÷ 1,000 = 97%. 이탈은 한 명도 못 찾습니다.', 'hint': '(TP + TN) ÷ 전체', 'calc': True, 'assess': 'lab:concept/confusion-matrix'}],
 'lv2': [
  {'id': 'q3', 'q': 'TP 40, FP 60, FN 10일 때 정밀도와 재현율은?', 'o': ['정밀도 0.4 · 재현율 0.8', '정밀도 0.8 · 재현율 0.4', '정밀도 0.4 · 재현율 0.4'], 'a': 0, 'why': '정밀도 40 ÷ 100 = 0.4, 재현율 40 ÷ 50 = 0.8.', 'hint': '정밀도는 FP, 재현율은 FN과 짝.', 'calc': True, 'assess': 'lab:metric/precision-recall'},
  {'id': 'q4', 'q': '질병 진단·불량품 검출에서 보통 더 중시하는 지표는?', 'o': ['정밀도', '재현율', '정확도'], 'a': 1, 'why': '놓치는 오류(FN)가 더 치명적이라 재현율을 우선합니다(교안).', 'hint': '공항의 "엄격한 수하물 체크".', 'assess': 'lab:metric/precision-recall'}],
 'lv3': [
  {'id': 'q5', 'q': 'AUC = 0.5의 의미는?', 'o': ['완벽한 분류', '무작위 추측과 같은 수준', '절반을 맞힌 매우 좋은 모델'], 'a': 1, 'why': '45도 대각선 아래 넓이가 0.5입니다.', 'hint': '③칸 점선.', 'assess': 'lab:metric/roc-auc'},
  {'id': 'q6', 'q': '임계값을 0.5에서 0.1로 내리면 TPR과 FPR은?', 'o': ['둘 다 증가', '둘 다 감소', 'TPR 증가, FPR 감소'], 'a': 0, 'why': '더 많이 "양성"으로 판정하므로 맞힌 양성도, 잘못 걸린 음성도 늘어납니다(교안).', 'hint': '③칸 슬라이더를 왼쪽으로.', 'assess': 'lab:metric/roc-auc'}],
 'lv4': [
  {'id': 'q7', 'q': '앙상블 중 여러 모델을 순차적으로 학습해 이전 모델의 실수를 보완하는 방법은? (교안 연습문제 2)', 'o': ['배깅', '부스팅', '스태킹', '보팅'], 'a': 1, 'why': '부스팅은 틀린 부분에 집중해 다음 모델을 학습합니다.', 'hint': '틀린 문제를 다시 공부하는 학생.', 'assess': 'lab:method/ensemble'},
  {'id': 'q8', 'q': '같은 데이터·같은 설정으로 학습한 모델 21개를 다수결하면?', 'o': ['크게 좋아진다', '거의 같은 실수를 해 별로 나아지지 않는다', '반드시 나빠진다'], 'a': 1, 'why': '다양성이 없으면(ρ가 크면) 실수가 상쇄되지 않습니다.', 'hint': '④칸 ρ 슬라이더.', 'assess': 'lab:method/ensemble'}],
 'lv5': [
  {'id': 'q9', 'q': '훈련 데이터 1,000개, 미니 배치 100개면 1에포크의 갱신 횟수는?', 'o': ['1번', '10번', '100번'], 'a': 1, 'why': '1,000 ÷ 100 = 10번(교안).', 'hint': '데이터 수 ÷ 배치 크기', 'calc': True, 'assess': 'lab:concept/learning-rate-batch'},
  {'id': 'q10', 'q': '학습률이 너무 클 때 생기기 쉬운 일은?', 'o': ['학습이 매우 느려진다', '정답 주변을 헤매거나 손실이 튄다', '에포크 수가 줄어든다'], 'a': 1, 'why': '한 번에 너무 크게 고쳐 최적점을 지나칩니다.', 'hint': '⑤칸 학습률 30.', 'assess': 'lab:concept/learning-rate-batch'},
  {'id': 'q11', 'q': '고객 세분화에서 RFM 분석의 R이 뜻하는 것은? (교안 연습문제 3)', 'o': ['Revenue', 'Recency', 'Retention', 'Recommendation'], 'a': 1, 'why': 'R은 최근성, 마지막 구매일입니다.', 'hint': 'Recency · Frequency · Monetary', 'assess': 'lab:concept/rfm'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('dataset/churn-demo', 'Dataset', '이탈 예측 예시 고객', 'synthetic churn customers', '#lv1', '이용 감소율·불만 문의 두 특성과 이탈 여부. 설명용 예시.', level=1, family='basics'),
 N('task/churn-prediction', 'Task', '고객 이탈 예측', 'churn prediction', '#why', level=1, family='basics'),
 N('concept/class-imbalance', 'Concept', '클래스 불균형', 'class imbalance', '#lv1', level=1, family='data'),
 N('concept/confusion-matrix', 'Concept', '혼동행렬', 'confusion matrix', '#lv1', level=1, family='evaluation'),
 N('metric/accuracy', 'Metric', '정확도', 'accuracy', '#lv1', '(TP + TN) ÷ 전체.', level=1, family='evaluation'),
 N('metric/precision-recall', 'Metric', '정밀도·재현율·F1', 'precision, recall, F1', '#lv2', level=1, family='evaluation'),
 N('concept/threshold', 'Concept', '임계값', 'decision threshold', '#lv2', level=1, family='evaluation'),
 N('metric/roc-auc', 'Metric', 'ROC 곡선과 AUC', 'ROC and AUC', '#lv3', level=2, family='evaluation'),
 N('method/ensemble', 'Method', '앙상블(배깅·부스팅·스태킹)', 'ensembles', '#lv4', level=2, family='basics'),
 N('concept/diversity', 'Concept', '모델 다양성', 'model diversity', '#lv4', '앙상블의 개별 모델이 서로 다른 곳에서 틀려야 실수가 상쇄된다.', level=2, family='basics'),
 N('concept/learning-rate-batch', 'Concept', '배치·에포크·학습률', 'batch, epoch, learning rate', '#lv5', level=2, family='systems'),
 N('method/cost-threshold', 'Method', '비용 기반 임계값', 'cost-based threshold', '#duel', 'FP·FN에 값을 매겨 순이익이 최대인 임계값을 고른다.', level=2, family='evaluation'),
 N('concept/rfm', 'Concept', 'RFM 고객 세분화', 'RFM segmentation', '#lv5', level=1, family='basics'),
 N('limitation/no-alt-metric', 'Limitation', '정확도 대신 볼 지표가 없다', 'no alternative metric', '#lv1'),
 N('limitation/threshold-dependent', 'Limitation', '임계값마다 점수가 다르다', 'threshold-dependent scores', '#lv2'),
 N('limitation/eval-not-improve', 'Limitation', '평가만으로는 모델이 좋아지지 않는다', 'evaluation does not improve', '#lv3'),
 N('limitation/single-learner', 'Limitation', '개별 모델의 학습 방법은 그대로다', 'single learner training', '#lv4'),
 N('limitation/no-money', 'Limitation', '손실이 낮아도 돈이 되는 기준은 따로다', 'loss is not profit', '#lv5'),
 N('claim/type1-fp', 'Claim', 'FP = 1종 오류(거짓 경보), FN = 2종 오류(누락)', 'FP is type I, FN is type II', '#lv1', source=[{'cite': '교안 7주차', 'loc': '1교시 2'}]),
 N('claim/auc-scale', 'Claim', 'AUC 0.5 무작위, 0.7~0.8 적절, 0.8~0.9 좋음, 0.9 이상 매우 뛰어남', 'AUC interpretation scale', '#lv3', source=[{'cite': '교안 7주차', 'loc': '1교시 4'}]),
 N('question/core', 'Question', '이탈 고객을 못 찾는 모델이 정확도 1등을 할 수 있을까?', 'Can a useless model top accuracy?', '#hero'),
 N('question/duel', 'Question', '정확도로 고른 기준과 비용으로 고른 기준, 어느 쪽이 돈을 버나', 'accuracy or cost threshold?', '#duel'),
 N('analogy/airport', 'Analogy', '공항 수하물 검사 ↔ 정밀도·재현율', 'airport screening ↔ precision/recall', '#lv2', anchorType='D'),
 N('analogy/experts', 'Analogy', '여러 전문가의 의견 ↔ 앙상블', 'panel of experts ↔ ensemble', '#lv4', anchorType='D'),
 N('analogy/textbook', 'Analogy', '교과서 몇 쪽씩 읽고 정리 ↔ 배치·에포크', 'reading a textbook ↔ batch/epoch', '#lv5', anchorType='D'),
 N('sim/w07-cm', 'Simulation', '두 모델의 혼동행렬', 'confusion matrices', '#lv1'),
 N('sim/w07-pr', 'Simulation', '임계값과 정밀도·재현율', 'threshold vs P/R', '#lv2'),
 N('sim/w07-roc', 'Simulation', 'ROC와 쌍 뽑기', 'ROC and pair sampling', '#lv3'),
 N('sim/w07-ens', 'Simulation', '다수결 앙상블 모의실험', 'majority-vote ensemble', '#lv4'),
 N('sim/w07-sgd', 'Simulation', '학습률·배치 손실 곡선', 'learning-rate curves', '#lv5'),
 N('work/ahn-dsb-w07', 'Work', '안상선, 비즈니스를위한데이터과학 교안 7주차', 'Ahn, DSB lecture notes week 7', '#footer'),
 N('work/sklearn-metrics', 'Work', 'scikit-learn Metrics 문서', 'scikit-learn metrics docs', '#footer'),
 N('work/fawcett2006', 'Work', 'Fawcett (2006) ROC 분석 입문', 'Fawcett 2006', '#footer'),
]

EDGES = [
 ('lab:task/churn-prediction', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:concept/class-imbalance', 'lab:partOf', 'lab:task/churn-prediction', '#why'),
 ('lab:metric/accuracy', 'lab:hasLimitation', 'lab:concept/class-imbalance', '#lv1'),
 ('lab:concept/confusion-matrix', 'lab:evaluatedOn', 'lab:dataset/churn-demo', '#lv1'),
 ('lab:metric/accuracy', 'lab:partOf', 'lab:concept/confusion-matrix', '#lv1'),
 ('lab:concept/confusion-matrix', 'lab:hasLimitation', 'lab:limitation/no-alt-metric', '#lv1'),
 ('lab:limitation/no-alt-metric', 'lab:addressedBy', 'lab:metric/precision-recall', '#lv2'),
 ('lab:concept/confusion-matrix', 'lab:prerequisiteOf', 'lab:metric/precision-recall', '#lv2'),
 ('lab:concept/threshold', 'lab:partOf', 'lab:metric/precision-recall', '#lv2'),
 ('lab:metric/precision-recall', 'lab:hasLimitation', 'lab:limitation/threshold-dependent', '#lv2'),
 ('lab:limitation/threshold-dependent', 'lab:addressedBy', 'lab:metric/roc-auc', '#lv3'),
 ('lab:metric/roc-auc', 'lab:evaluatedOn', 'lab:dataset/churn-demo', '#lv3'),
 ('lab:metric/roc-auc', 'lab:hasLimitation', 'lab:limitation/eval-not-improve', '#lv3'),
 ('lab:limitation/eval-not-improve', 'lab:addressedBy', 'lab:method/ensemble', '#lv4'),
 ('lab:concept/diversity', 'lab:partOf', 'lab:method/ensemble', '#lv4'),
 ('lab:method/ensemble', 'lab:hasLimitation', 'lab:limitation/single-learner', '#lv4'),
 ('lab:limitation/single-learner', 'lab:addressedBy', 'lab:concept/learning-rate-batch', '#lv5'),
 ('lab:concept/learning-rate-batch', 'lab:hasLimitation', 'lab:limitation/no-money', '#lv5'),
 ('lab:limitation/no-money', 'lab:addressedBy', 'lab:method/cost-threshold', '#duel'),
 ('lab:method/cost-threshold', 'lab:solves', 'lab:task/churn-prediction', '#duel'),
 ('lab:concept/threshold', 'lab:prerequisiteOf', 'lab:method/cost-threshold', '#duel'),
 ('lab:method/cost-threshold', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:concept/rfm', 'lab:partOf', 'lab:task/churn-prediction', '#lv5'),
 ('lab:analogy/airport', 'lab:analogyOf', 'lab:metric/precision-recall', '#lv2'),
 ('lab:analogy/experts', 'lab:analogyOf', 'lab:method/ensemble', '#lv4'),
 ('lab:analogy/textbook', 'lab:analogyOf', 'lab:concept/learning-rate-batch', '#lv5'),
 ('lab:concept/confusion-matrix', 'lab:demonstratedBy', 'lab:sim/w07-cm', '#lv1'),
 ('lab:metric/precision-recall', 'lab:demonstratedBy', 'lab:sim/w07-pr', '#lv2'),
 ('lab:metric/roc-auc', 'lab:demonstratedBy', 'lab:sim/w07-roc', '#lv3'),
 ('lab:method/ensemble', 'lab:demonstratedBy', 'lab:sim/w07-ens', '#lv4'),
 ('lab:concept/learning-rate-batch', 'lab:demonstratedBy', 'lab:sim/w07-sgd', '#lv5'),
 ('lab:claim/type1-fp', 'lab:supports', 'lab:concept/confusion-matrix', '#lv1'), ('lab:claim/type1-fp', 'lab:assertedIn', 'lab:work/ahn-dsb-w07', '#lv1'),
 ('lab:claim/auc-scale', 'lab:supports', 'lab:metric/roc-auc', '#lv3'), ('lab:claim/auc-scale', 'lab:assertedIn', 'lab:work/ahn-dsb-w07', '#lv3'),
 ('lab:metric/precision-recall', 'lab:relatedTo', 'lab:work/sklearn-metrics', '#footer'),
 ('lab:metric/roc-auc', 'lab:relatedTo', 'lab:work/fawcett2006', '#footer'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w07', 'report', '비즈니스를위한데이터과학 강의 교안: 07. 비즈니스 데이터 분석 모델의 평가', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/type1-fp', 'lab:claim/auc-scale', 'lab:concept/confusion-matrix', 'lab:metric/precision-recall', 'lab:method/ensemble', 'lab:concept/learning-rate-batch'], 'lab:work/ahn-dsb-w07',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음. 5쪽 TN/FP 표기 확인 필요',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/type1-fp', 'loc': '1교시 2. Confusion Matrix'}, {'claim': 'lab:claim/auc-scale', 'loc': '1교시 4. ROC 곡선과 AUC'}]),
 R('sklearn_metrics', 'webpage', 'scikit-learn User Guide: Metrics and scoring', [{'literal': 'scikit-learn developers'}], None, 'background',
   ['lab:metric/precision-recall', 'lab:metric/roc-auc'], 'lab:work/sklearn-metrics',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '공식 문서 URL 확인', '', URL='https://scikit-learn.org/stable/modules/model_evaluation.html'),
 R('fawcett2006', 'article-journal', 'An introduction to ROC analysis', [{'family': 'Fawcett', 'given': 'Tom'}], 2006, 'background',
   ['lab:metric/roc-auc'], 'lab:work/fawcett2006',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '서지 기억 기반 — DOI 재확인 권장', '', **{'container-title': 'Pattern Recognition Letters', 'volume': '27', 'issue': '8', 'page': '861-874'}),
]
