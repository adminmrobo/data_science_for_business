# 2주차 · 비즈니스 데이터의 수집 및 처리 기술
SLUG = 'dsb_w02_data_collection'
FILE = 'week02_data_collection.html'
TITLE = '데이터는 어디서 오는가 — 비즈니스 데이터의 수집과 처리'
DESC = '비즈니스를 위한 데이터 과학 2주차 연구실 해설. 산업별 데이터 지도, 수집 방법 고르기, 배치와 스트림, TCO, 가명처리와 k-익명성을 직접 돌려 본다.'
DOMAIN = ['ai', 'stats', 'biz']
COVER_ALT = '네 캐릭터가 은행 창구, 공장 센서, 편의점 계산대, 스마트폰에서 연구실 서버로 흘러드는 빛줄기를 지켜보는 표지'
COVER_PROP = '📡'
SEARCH_PH = '예: API, 스트림, TCO, k-익명성'
NAV = [('#why', '왜'), ('#big', '큰 그림'), ('#lv1', '① 산업별 지도'), ('#lv2', '② 수집 방법'), ('#lv3', '③ 적시성'), ('#lv4', '④ 비용'), ('#lv5', '⑤ 가명처리'), ('#duel', '대결'), ('#sum', '정리')]
PREVNEXT = '<a href="week01_business_data_science.html"><small>← 이전 · 1주차</small>데이터는 많은데, 결정은 왜 틀릴까</a><a href="index.html"><small>목차</small>비즈니스를 위한 데이터 과학 연구실</a><a href="week03_analysis_prep.html"><small>다음 · 3주차</small>분석 전에 데이터를 손보다 →</a>'
EXTRA_SPRITES = ['fly_arms', 'robo_sigh', 'doc_judge', 'asst_spark', 'fly_cry', 'fly_coffee', 'robo_happy', 'asst_firm', 'doc_think', 'robo_meh', 'robo_calc', 'robo_blush', 'asst_shock', 'asst_report', 'fly_magnify']
ABOUT = ['lab:concept/data-collection-method', 'lab:method/api', 'lab:concept/batch-vs-stream', 'lab:concept/tco', 'lab:concept/k-anonymity']
KGPATH = ['concept/industry-data', 'limitation/method-unknown', 'concept/data-collection-method', 'limitation/frequency-unknown', 'concept/batch-vs-stream', 'limitation/ownership-cost', 'concept/tco', 'limitation/personal-data', 'concept/k-anonymity', 'limitation/quality-remains']
TODO = ['교안 [1]의 발행 연도·학기 표기 확인', '개인정보보호법 등 법령 내용은 교안 기준 — 최신 개정 여부 확인 필요']

SOURCES = [
 '[1] 안상선. 「비즈니스를위한데이터과학」 강의 교안, 02. 비즈니스 데이터의 수집 및 처리 기술. 인공지능융합학과. — 산업별 데이터, 수집 방법, 데이터 레이크·웨어하우스, RPA, 품질·보안·적시성·TCO·신뢰성, 국내외 규제와 가명처리 내용은 교안 본문을 옮김. 법·규제 내용은 교안 기준이며 이후 개정 여부는 확인하지 않음.',
 '[2] 한국기술교육대학교 온라인평생교육원 (2025). 「핀테크데이터분석」. — 교안이 인터넷 전문은행 데이터 표의 출처와 참고문헌으로 인용.',
 '[3] 한국지능정보사회진흥원 (2021). 『데이터 품질관리 가이드』. — 교안이 품질 관리 프레임워크의 참고로 인용.',
 '[4] Sweeney, L. (2002). k-anonymity: A model for protecting privacy. International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10(5), 557–570. — k-익명성 개념의 출처(배경 문헌). 서지는 <a href="https://dataprivacylab.org/projects/kanonymity/" target="_blank" rel="noopener">Data Privacy Lab</a>에서 확인(2026-11-09).']
ILLUSTRATIVE = [
 '①칸 흐름도의 알갱이 속도는 데이터가 생기는 빠르기를 느낌으로 보여 주는 설명용 도식입니다.',
 '③칸과 대결: 하루 의심 거래 20건(30일, 시드 5), 탐지 전 건당 시간당 손실 2만 원, 배치 처리 1회 2만 원, 스트림 하루 50만 원은 예시값입니다.',
 '④칸: 온프레미스 초기 1억 2,000만 원·월 300만 원·용량 80TB·증설 6,000만 원, 클라우드 기본료 월 50만 원·TB당 월 12만 원은 비교를 보여 주기 위한 예시값이며 실제 단가가 아닙니다.',
 '⑤칸 고객 40명(시드 77)의 나이·성별·우편번호·구매액은 만든 데이터이며 실제 인물이 아닙니다.']

GL = {
 '비즈니스 데이터': ['비즈니스 데이터', '개념', '기업 운영 과정에서 생기는 모든 형태의 정보. 고객 행동, 거래 내역, 운영 데이터, 외부 환경 정보.', 'lab:concept/industry-data'],
 'API': ['API (응용 프로그램 인터페이스)', '방법', '소프트웨어 시스템끼리 통신하고 데이터를 주고받기 위한 규칙. 공공·금융 기관이 Open API로 데이터를 제공한다.', 'lab:method/api'],
 '웹 스크래핑': ['웹 스크래핑', '방법', '특정 웹페이지에서 구조화된 데이터를 뽑아내는 기술.', 'lab:method/web-scraping'],
 '크롤링': ['웹 크롤링', '방법', '여러 페이지를 돌아다니며 넓게 데이터를 모으는 방법. 저작권·개인정보·약관·서버 부하를 함께 따진다.', None],
 'RPA': ['RPA (로봇 프로세스 자동화)', '방법', '사람의 화면 조작을 흉내 내는 소프트웨어 봇으로 반복 업무를 자동화한다. API가 없는 옛 시스템에서도 데이터를 꺼낼 수 있다.', 'lab:method/rpa'],
 'IoT': ['IoT (사물인터넷)', '용어', '센서가 달린 사물이 네트워크로 데이터를 주고받는 기술.', 'lab:method/sensor-iot'],
 'MES': ['MES (제조실행시스템)', '용어', '작업지시·자원·품질·성과 등 생산 전 과정의 데이터를 실시간으로 모으는 시스템.', None],
 '디지털 트윈': ['디지털 트윈', '용어', '실제 공장과 똑같은 가상 모델을 만들어 시뮬레이션하는 기술.', None],
 'POS': ['POS (판매시점 정보관리)', '용어', '계산대에서 매장·시간대·상품별 판매를 실시간으로 기록하는 장비·시스템.', None],
 'RFM': ['RFM 분석', '방법', '최근 구매일(Recency)·구매 빈도(Frequency)·구매 금액(Monetary)으로 고객 가치를 숫자로 나타내는 방법.', None],
 'RFID': ['RFID', '용어', '전파로 태그를 읽는 기술. 스마트 선반과 함께 실시간 재고를 파악한다.', None],
 '데이터 레이크': ['데이터 레이크', '개념', '정형·반정형·비정형 데이터를 원본 그대로 저장하는 중앙 저장소.', 'lab:concept/data-lake'],
 '데이터 웨어하우스': ['데이터 웨어하우스', '개념', '비즈니스 목적에 맞게 정제·구조화한 데이터를 저장하고 OLAP 분석을 지원하는 시스템.', 'lab:concept/data-warehouse'],
 '데이터 거버넌스': ['데이터 거버넌스', '개념', '데이터 품질·보안·접근 권한을 체계적으로 관리하는 체계. 메타데이터와 데이터 계보를 추적한다.', 'lab:concept/data-governance'],
 '데이터 계보': ['데이터 계보(lineage)', '개념', '데이터가 어디서 생겨 어떤 변환을 거쳐 쓰였는지의 기록.', None],
 '배치 처리': ['배치 처리', '방법', '데이터를 모아 두었다가 정해진 주기에 한꺼번에 처리하는 방식.', 'lab:concept/batch-vs-stream'],
 '스트림 처리': ['스트림 처리', '방법', '데이터가 생기는 즉시 계속 처리하는 방식. 실시간 의사결정에 쓴다.', None],
 '데이터 신선도': ['데이터 신선도', '개념', '데이터가 생긴 시점과 쓰이는 시점의 차이. 작을수록 신선하다.', None],
 'TCO': ['TCO (총소유비용)', '경영', '하드웨어·소프트웨어·인력·운영비를 모두 더한 소유 비용.', 'lab:concept/tco'],
 'ROI': ['ROI (투자 수익률)', '경영', '투자로 얻은 이익을 투자 비용으로 나눈 비율.', None],
 'FinOps': ['FinOps', '경영', '클라우드 비용을 계속 감시하고 최적화하는 운영 관행.', None],
 '가명정보': ['가명정보', '기준·법령', '추가 정보 없이는 특정 개인을 알아볼 수 없게 처리한 정보. 교안 기준 2020년 개정 개인정보보호법으로 통계·연구·공익적 기록보존 목적의 활용 근거가 생겼다.', 'lab:standard/pipa-2020'],
 'k-익명성': ['k-익명성', '방법', '준식별자(나이·성별·우편번호 등)의 조합이 같은 사람이 언제나 최소 k명 이상이 되도록 데이터를 일반화하는 기준.', 'lab:concept/k-anonymity'],
 '준식별자': ['준식별자', '개념', '하나만으로는 사람을 가리키지 않지만, 조합하면 특정 개인을 가리킬 수 있는 속성.', 'lab:concept/quasi-identifier'],
 'GDPR': ['GDPR', '기준·법령', '유럽연합의 일반 데이터 보호 규정. 정보주체 권리 강화와 기업 책임을 규정한다.', 'lab:standard/gdpr'],
 'CCPA': ['CCPA', '기준·법령', '미국 캘리포니아주 소비자 프라이버시법. 판매 거부권·삭제권·알 권리를 규정한다.', 'lab:standard/ccpa'],
}
CORE = ['API', '웹 스크래핑', 'RPA', '데이터 레이크', '데이터 웨어하우스', '배치 처리', '스트림 처리', 'TCO', '가명정보', 'k-익명성', '준식별자', 'GDPR']

QZ = {
 'lv1': [
  {'id': 'q1', 'q': '스마트팩토리 데이터 활용에 대한 설명으로 가장 거리가 먼 것은? (교안 연습문제 1)', 'o': ['AI 품질 예측으로 사전 품질 관리가 가능하다', '품질 검사 데이터는 생산 완료 후에만 수집할 수 있다', '설비 가동률·고장 이력으로 예측 정비가 가능하다'], 'a': 1, 'why': '품질 데이터는 생산 과정 중에도 실시간으로 수집됩니다.', 'hint': '제조 지도의 품질 검사 데이터 줄을 보세요.', 'assess': 'lab:concept/industry-data'},
  {'id': 'q2', 'q': 'POS 데이터 활용에 대한 설명으로 틀린 것은? (교안 연습문제 2)', 'o': ['RFM 분석으로 고객 가치를 정량화한다', '개인정보를 수집하지 않으므로 개인정보보호법 준수가 불필요하다', '시간대·요일·계절별 매출 패턴을 분석한다'], 'a': 1, 'why': 'POS 데이터에도 구매 이력 등 개인정보가 들어갈 수 있으므로 법을 지켜야 합니다.', 'hint': '소매 지도의 조심할 점을 보세요.', 'assess': 'lab:standard/pipa-2020'}],
 'lv2': [
  {'id': 'q3', 'q': 'API로 받는 수집이 웹 스크래핑보다 대체로 나은 점은?', 'o': ['더 많은 항목을 마음대로 받을 수 있다', '표준화된 인터페이스라 안정적이고 효율적이다', '법적 검토가 전혀 필요 없다'], 'a': 1, 'why': '교안 복습 문제 그대로입니다. API는 표준화된 규칙으로 데이터를 줍니다.', 'hint': '수집 방법 비교표의 강점 열.', 'assess': 'lab:method/api'},
  {'id': 'q4', 'q': 'API가 없는 20년 된 사내 시스템에서 데이터를 꺼낼 때 알맞은 방법은?', 'o': ['RPA', '설문', 'IoT 센서'], 'a': 0, 'why': 'RPA는 화면 조작을 흉내 내 레거시 시스템에서도 데이터를 꺼냅니다.', 'hint': '상황 5를 보세요.', 'assess': 'lab:method/rpa'}],
 'lv3': [
  {'id': 'q5', 'q': '처리 주기가 6시간이면 의심 거래의 평균 대기 시간은 대략?', 'o': ['약 1시간', '약 3시간', '약 6시간'], 'a': 1, 'why': '거래가 아무 때나 생기면 다음 처리까지 평균 주기의 절반, 약 3시간을 기다립니다.', 'hint': '평균 대기 ≈ h / 2', 'calc': True, 'assess': 'lab:concept/batch-vs-stream'},
  {'id': 'q6', 'q': '기다려도 손실이 거의 없는 월간 매출 보고에 알맞은 처리 방식은?', 'o': ['실시간 스트림', '하루 한 번 배치', '1시간마다 배치'], 'a': 1, 'why': '지연 손실이 0이면 처리 횟수가 적을수록 쌉니다.', 'hint': '③칸 슬라이더를 0으로 내려 보세요.', 'assess': 'lab:concept/batch-vs-stream'}],
 'lv4': [
  {'id': 'q7', 'q': '온프레미스가 클라우드보다 유리해지기 쉬운 경우는?', 'o': ['데이터가 적고 6개월만 쓸 때', '데이터가 많고 몇 년 동안 꾸준히 쓸 때', '데이터 양이 매달 크게 바뀔 때'], 'a': 1, 'why': '초기 투자를 오래, 많이 쓰며 나눠 갚을수록 손익분기 이후의 이득이 커집니다.', 'hint': '월 데이터 양을 높여 손익분기 월을 보세요.', 'assess': 'lab:concept/tco'}],
 'lv5': [
  {'id': 'q8', 'q': '이름을 지운 고객 표에서 "나이 34, 여, 06236" 조합이 한 명뿐이다. 이 고객의 k는?', 'o': ['0', '1', '34'], 'a': 1, 'why': '같은 조합을 가진 사람이 자기 혼자이므로 k = 1, 특정될 수 있습니다.', 'hint': 'k = 같은 조합을 가진 인원.', 'calc': True, 'assess': 'lab:concept/k-anonymity'},
  {'id': 'q9', 'q': '나이를 10세 구간, 우편번호를 앞 2자리로 일반화했을 때 생기는 대가는?', 'o': ['재식별 위험이 커진다', '남은 묶음 수가 줄어 분석이 거칠어진다', '데이터가 늘어난다'], 'a': 1, 'why': '보호가 강해지는 만큼 정보가 뭉개집니다. 보호와 활용의 균형입니다.', 'hint': '남은 묶음 수(정보량) 칸을 보세요.', 'assess': 'lab:concept/quasi-identifier'},
  {'id': 'q10', 'q': '교안 기준, 2020년 개정 개인정보보호법이 가명정보 활용을 허용한 목적이 아닌 것은?', 'o': ['통계 작성', '과학적 연구', '본인 동의 없는 타깃 광고'], 'a': 2, 'why': '교안은 통계 작성, 과학적 연구, 공익적 기록 보존을 듭니다. 법령 세부는 최신 조문으로 확인해야 합니다.', 'hint': '⑤칸 규제 지도.', 'assess': 'lab:standard/pipa-2020'}],
}

def N(i, t, ko, en, a, d=None, **k):
    n = {'id': 'lab:' + i, 'type': t, 'label': {'ko': ko, 'en': en}, 'anchor': a}
    if d: n['definition'] = {'ko': d}
    n.update(k); return n

NODES = [
 N('concept/industry-data', 'Concept', '산업별 비즈니스 데이터', 'business data by industry', '#lv1', level=1, family='data'),
 N('concept/data-collection-process', 'Framework', '데이터 수집 프로세스', 'data collection process', '#big', '목적 설정 → 소스 선정 → 방법 결정 → 수집 → 저장, 그리고 품질 검증.', level=1, family='data'),
 N('concept/data-collection-method', 'Concept', '데이터 수집 방법', 'data collection methods', '#lv2', '설문, API, 웹 스크래핑, 센서, RPA 등 데이터를 모으는 방법. 목적에 맞게 고른다.', level=1, family='data'),
 N('method/api', 'Method', 'Open API', 'open API', '#lv2', level=1, family='data'),
 N('method/web-scraping', 'Method', '웹 스크래핑·크롤링', 'web scraping and crawling', '#lv2', level=1, family='data'),
 N('method/survey', 'Method', '설문조사', 'survey', '#lv2', '사람에게 직접 물어 태도·성향·만족도를 모으는 방법.', level=1, family='data', domain=['stats', 'biz']),
 N('method/sensor-iot', 'Method', '센서(IoT) 수집', 'sensor / IoT collection', '#lv2', level=1, family='data'),
 N('method/rpa', 'Method', 'RPA', 'robotic process automation', '#lv2', level=1, family='data'),
 N('concept/data-lake', 'Concept', '데이터 레이크', 'data lake', '#big', level=2, family='data'),
 N('concept/data-warehouse', 'Concept', '데이터 웨어하우스', 'data warehouse', '#big', level=2, family='data'),
 N('concept/data-governance', 'Concept', '데이터 거버넌스', 'data governance', '#big', level=2, family='data'),
 N('concept/data-quality-3', 'Concept', '데이터 품질(정확성·완전성·일관성)', 'data quality (accuracy, completeness, consistency)', '#big', '수집한 데이터가 정확하고, 빠짐없고, 서로 모순 없는 정도.', level=1, family='data'),
 N('concept/batch-vs-stream', 'Concept', '배치 처리와 스트림 처리', 'batch vs stream processing', '#lv3', level=2, family='data'),
 N('concept/data-freshness', 'Concept', '적시성·데이터 신선도', 'timeliness / data freshness', '#lv3', '데이터가 생긴 시점과 쓰이는 시점의 차이를 비즈니스 요구에 맞게 관리하는 것.', level=2, family='data'),
 N('concept/tco', 'Concept', 'TCO(총소유비용)', 'total cost of ownership', '#lv4', level=2, family='data', domain=['biz']),
 N('concept/cloud-vs-onprem', 'Concept', '클라우드 대 온프레미스', 'cloud vs on-premises', '#lv4', '빌려 쓰는 인프라와 직접 사서 운영하는 인프라의 비교.', level=2, family='data', domain=['biz']),
 N('metric/roi', 'Metric', 'ROI(투자 수익률)', 'return on investment', '#lv4', '수집 투자로 얻은 가치를 비용으로 나눈 비율.', level=1, family='data', domain=['biz']),
 N('concept/k-anonymity', 'Method', 'k-익명성', 'k-anonymity', '#lv5', level=3, family='ethics', domain=['stats', 'ai']),
 N('concept/quasi-identifier', 'Concept', '준식별자', 'quasi-identifier', '#lv5', level=2, family='ethics'),
 N('concept/pseudonymization', 'Method', '가명처리·익명화', 'pseudonymization and anonymization', '#lv5', '식별자 제거, 일반화, 마스킹, 해시·토큰화 등으로 개인을 알아볼 수 없게 처리하는 것.', level=2, family='ethics'),
 N('concept/reidentification', 'Concept', '재식별 위험', 're-identification risk', '#lv5', '가명 처리된 정보가 다른 정보와 결합해 특정 개인이 드러날 위험.', level=2, family='ethics'),
 N('standard/pipa-2020', 'Standard', '개인정보보호법(2020 개정, 가명정보)', 'Personal Information Protection Act (2020 amendment)', '#lv5', asOf='교안 기준', jurisdiction='KR', domain=['biz'], confidence='mid'),
 N('standard/gdpr', 'Standard', 'GDPR', 'General Data Protection Regulation', '#lv5', asOf='교안 기준', jurisdiction='EU', domain=['biz']),
 N('standard/ccpa', 'Standard', 'CCPA', 'California Consumer Privacy Act', '#lv5', asOf='교안 기준', jurisdiction='US-CA', domain=['biz']),
 N('task/fraud-monitoring', 'Task', '사기 의심 거래 감시', 'fraud monitoring', '#lv3', level=2, family='data'),
 N('task/monthly-report', 'Task', '월간 매출 보고', 'monthly sales reporting', '#duel', level=1, family='data'),
 N('metric/daily-total-cost', 'Metric', '하루 총비용(처리 + 지연 손실)', 'daily total cost', '#lv3', level=2, family='data'),
 N('limitation/method-unknown', 'Limitation', '무엇을 모을지만 알고 방법은 모름', 'method not chosen', '#lv1'),
 N('limitation/frequency-unknown', 'Limitation', '얼마나 자주 처리할지 모름', 'processing frequency undecided', '#lv2'),
 N('limitation/ownership-cost', 'Limitation', '소유 비용 전체가 빠짐', 'ownership cost missing', '#lv3'),
 N('limitation/personal-data', 'Limitation', '사람이 담긴 데이터의 법적 문제', 'personal data legal issues', '#lv4'),
 N('limitation/quality-remains', 'Limitation', '결측·이상값·중복은 그대로', 'quality issues remain', '#lv5'),
 N('limitation/l-diversity', 'Limitation', '묶음 안 정보 누출(l-다양성 문제)', 'homogeneity leakage', '#lv5', '한 묶음의 민감 속성이 모두 같으면 k가 커도 정보가 샌다.'),
 N('claim/api-more-stable', 'Claim', 'API 수집은 웹 스크래핑보다 안정적이고 효율적', 'API is more stable than scraping', '#lv2', source=[{'cite': '교안 2주차', 'loc': '2교시 2, 3주차 복습점검'}]),
 N('claim/pipa-2020-pseudonym', 'Claim', '2020년 개정 개인정보보호법으로 가명정보 처리 근거 마련', '2020 PIPA amendment enabled pseudonymized data', '#lv5', source=[{'cite': '교안 2주차', 'loc': '3교시 7'}], confidence='mid'),
 N('claim/factory-sensor-rate', 'Claim', '스마트팩토리 센서는 초당 수백~수천 건의 데이터를 만든다', 'factory sensors generate hundreds+ records per second', '#lv1', source=[{'cite': '교안 2주차', 'loc': '1교시 6, 2교시 5'}], confidence='mid'),
 N('question/core', 'Question', '어디서, 어떻게, 얼마나 빨리 모은 데이터라야 믿고 쓸 수 있을까?', 'What makes collected data trustworthy?', '#hero'),
 N('question/duel', 'Question', '하루 한 번 배치냐, 실시간 스트림이냐?', 'Daily batch or real-time stream?', '#duel'),
 N('question/k-enough', 'Question', 'k는 얼마면 충분할까? 정보 손실과의 균형은?', 'How large should k be?', '#lv5'),
 N('analogy/lab-instruments', 'Analogy', '실험 장비 고르기 ↔ 수집 방법 고르기', 'choosing lab instruments ↔ collection methods', '#lv2', anchorType='B'),
 N('analogy/buy-vs-rent', 'Analogy', '차를 살까 빌릴까 ↔ 온프레미스 대 클라우드', 'buy vs rent ↔ on-prem vs cloud', '#lv4', anchorType='C'),
 N('sim/w02-flow', 'Simulation', '산업별 데이터 흐름도', 'industry data flow', '#lv1'),
 N('sim/w02-pick', 'Simulation', '상황 여섯 개 수집 방법 고르기', 'method picking game', '#lv2'),
 N('sim/w02-batch', 'Simulation', '30일 사기 감시 처리 주기 실험', 'batch vs stream simulation', '#lv3'),
 N('sim/w02-tco', 'Simulation', '36개월 TCO 비교', 'TCO comparison', '#lv4'),
 N('sim/w02-kanon', 'Simulation', '고객 40명 k-익명성 실험', 'k-anonymity table', '#lv5'),
 N('work/ahn-dsb-w02', 'Work', '안상선, 비즈니스를위한데이터과학 교안 2주차', 'Ahn, DSB lecture notes week 2', '#footer'),
 N('work/koreatech2025', 'Work', '한국기술교육대학교(2025) 핀테크데이터분석', 'KOREATECH (2025) Fintech Data Analysis', '#footer'),
 N('work/nia2021', 'Work', '한국지능정보사회진흥원(2021) 데이터 품질관리 가이드', 'NIA (2021) Data Quality Guide', '#footer'),
 N('work/sweeney2002', 'Work', 'Sweeney(2002) k-anonymity', 'Sweeney (2002)', '#footer'),
]

EDGES = [
 ('lab:concept/industry-data', 'lab:prerequisiteOf', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:concept/industry-data', 'lab:hasLimitation', 'lab:limitation/method-unknown', '#lv1'),
 ('lab:limitation/method-unknown', 'lab:addressedBy', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:method/api', 'lab:broader', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:method/web-scraping', 'lab:broader', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:method/survey', 'lab:broader', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:method/sensor-iot', 'lab:broader', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:method/rpa', 'lab:broader', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:method/api', 'lab:contrastsWith', 'lab:method/web-scraping', '#lv2'),
 ('lab:concept/data-collection-method', 'lab:partOf', 'lab:concept/data-collection-process', '#big'),
 ('lab:concept/data-lake', 'lab:partOf', 'lab:concept/data-collection-process', '#big'),
 ('lab:concept/data-warehouse', 'lab:partOf', 'lab:concept/data-collection-process', '#big'),
 ('lab:concept/data-lake', 'lab:contrastsWith', 'lab:concept/data-warehouse', '#big'),
 ('lab:concept/data-governance', 'lab:relatedTo', 'lab:concept/data-quality-3', '#big'),
 ('lab:concept/data-quality-3', 'lab:partOf', 'lab:concept/data-collection-process', '#big'),
 ('lab:concept/data-collection-method', 'lab:hasLimitation', 'lab:limitation/frequency-unknown', '#lv2'),
 ('lab:limitation/frequency-unknown', 'lab:addressedBy', 'lab:concept/batch-vs-stream', '#lv3'),
 ('lab:concept/data-collection-method', 'lab:prerequisiteOf', 'lab:concept/batch-vs-stream', '#lv3'),
 ('lab:concept/data-freshness', 'lab:relatedTo', 'lab:concept/batch-vs-stream', '#lv3'),
 ('lab:concept/batch-vs-stream', 'lab:solves', 'lab:task/fraud-monitoring', '#lv3'),
 ('lab:concept/batch-vs-stream', 'lab:solves', 'lab:task/monthly-report', '#duel'),
 ('lab:concept/batch-vs-stream', 'lab:evaluatedBy', 'lab:metric/daily-total-cost', '#lv3'),
 ('lab:concept/batch-vs-stream', 'lab:hasLimitation', 'lab:limitation/ownership-cost', '#lv3'),
 ('lab:limitation/ownership-cost', 'lab:addressedBy', 'lab:concept/tco', '#lv4'),
 ('lab:concept/batch-vs-stream', 'lab:prerequisiteOf', 'lab:concept/tco', '#lv4'),
 ('lab:concept/cloud-vs-onprem', 'lab:evaluatedBy', 'lab:concept/tco', '#lv4'),
 ('lab:concept/tco', 'lab:relatedTo', 'lab:metric/roi', '#lv4'),
 ('lab:concept/tco', 'lab:hasLimitation', 'lab:limitation/personal-data', '#lv4'),
 ('lab:limitation/personal-data', 'lab:addressedBy', 'lab:concept/pseudonymization', '#lv5'),
 ('lab:concept/tco', 'lab:prerequisiteOf', 'lab:concept/k-anonymity', '#lv5'),
 ('lab:concept/k-anonymity', 'lab:broader', 'lab:concept/pseudonymization', '#lv5'),
 ('lab:concept/quasi-identifier', 'lab:partOf', 'lab:concept/k-anonymity', '#lv5'),
 ('lab:concept/k-anonymity', 'lab:evaluatedBy', 'lab:concept/reidentification', '#lv5'),
 ('lab:concept/k-anonymity', 'lab:hasLimitation', 'lab:limitation/l-diversity', '#lv5'),
 ('lab:concept/k-anonymity', 'lab:hasLimitation', 'lab:limitation/quality-remains', '#lv5'),
 ('lab:limitation/l-diversity', 'lab:raises', 'lab:question/k-enough', '#lv5'),
 ('lab:concept/pseudonymization', 'lab:governedBy', 'lab:standard/pipa-2020', '#lv5'),
 ('lab:concept/pseudonymization', 'lab:governedBy', 'lab:standard/gdpr', '#lv5'),
 ('lab:concept/pseudonymization', 'lab:governedBy', 'lab:standard/ccpa', '#lv5'),
 ('lab:method/web-scraping', 'lab:governedBy', 'lab:standard/pipa-2020', '#lv2'),
 ('lab:concept/data-collection-process', 'lab:raises', 'lab:question/core', '#hero'),
 ('lab:metric/daily-total-cost', 'lab:raises', 'lab:question/duel', '#duel'),
 ('lab:analogy/lab-instruments', 'lab:analogyOf', 'lab:concept/data-collection-method', '#lv2'),
 ('lab:analogy/buy-vs-rent', 'lab:analogyOf', 'lab:concept/cloud-vs-onprem', '#lv4'),
 ('lab:concept/industry-data', 'lab:demonstratedBy', 'lab:sim/w02-flow', '#lv1'),
 ('lab:concept/data-collection-method', 'lab:demonstratedBy', 'lab:sim/w02-pick', '#lv2'),
 ('lab:concept/batch-vs-stream', 'lab:demonstratedBy', 'lab:sim/w02-batch', '#lv3'),
 ('lab:concept/tco', 'lab:demonstratedBy', 'lab:sim/w02-tco', '#lv4'),
 ('lab:concept/k-anonymity', 'lab:demonstratedBy', 'lab:sim/w02-kanon', '#lv5'),
 ('lab:claim/api-more-stable', 'lab:supports', 'lab:method/api', '#lv2'), ('lab:claim/api-more-stable', 'lab:assertedIn', 'lab:work/ahn-dsb-w02', '#lv2'),
 ('lab:claim/pipa-2020-pseudonym', 'lab:supports', 'lab:standard/pipa-2020', '#lv5', 'mid'), ('lab:claim/pipa-2020-pseudonym', 'lab:assertedIn', 'lab:work/ahn-dsb-w02', '#lv5', 'mid'),
 ('lab:claim/factory-sensor-rate', 'lab:supports', 'lab:method/sensor-iot', '#lv1', 'mid'), ('lab:claim/factory-sensor-rate', 'lab:assertedIn', 'lab:work/ahn-dsb-w02', '#lv1', 'mid'),
 ('lab:work/koreatech2025', 'lab:relatedTo', 'lab:concept/industry-data', '#lv1'),
 ('lab:work/nia2021', 'lab:relatedTo', 'lab:concept/data-quality-3', '#big'),
 ('lab:work/sweeney2002', 'lab:relatedTo', 'lab:concept/k-anonymity', '#lv5'),
]

def R(id, typ, title, author, year, role, supports, work, verified, checked, note='', **k):
    r = {'id': id, 'type': typ, 'title': title, 'author': author, 'lab': {'work': work, 'role': role, 'supports': supports, 'locs': k.pop('locs', []), 'verified': verified, 'checkedBy': checked, 'note': note}}
    if year: r['issued'] = {'date-parts': [[year]]}
    r.update(k); return r

REFS = [
 R('ahn_dsb_w02', 'report', '비즈니스를위한데이터과학 강의 교안: 02. 비즈니스 데이터의 수집 및 처리 기술', [{'family': '안', 'given': '상선'}], None, 'primary',
   ['lab:claim/api-more-stable', 'lab:claim/pipa-2020-pseudonym', 'lab:claim/factory-sensor-rate', 'lab:concept/industry-data', 'lab:concept/data-collection-method'], 'lab:work/ahn-dsb-w02',
   {'title': True, 'authors': True, 'year': False, 'venue': True, 'doi': False, 'pages': False}, '저자 원고(교안 PDF)로 확인 2026-11-09', '연도 표기 없음',
   publisher='인공지능융합학과 강의자료', locs=[{'claim': 'lab:claim/api-more-stable', 'loc': '2교시 2'}, {'claim': 'lab:claim/pipa-2020-pseudonym', 'loc': '3교시 7'}, {'claim': 'lab:claim/factory-sensor-rate', 'loc': '1교시 6'}]),
 R('koreatech2025fintech', 'report', '핀테크데이터분석', [{'literal': '한국기술교육대학교 온라인평생교육원'}], 2025, 'background', ['lab:concept/industry-data'], 'lab:work/koreatech2025',
   {'title': True, 'authors': True, 'year': True, 'venue': False, 'doi': False, 'pages': False}, '교안의 인용 서지로 확인', 'STEP 온라인평생교육원 강좌'),
 R('nia2021quality', 'report', '데이터 품질관리 가이드', [{'literal': '한국지능정보사회진흥원'}], 2021, 'background', ['lab:concept/data-quality-3'], 'lab:work/nia2021',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': False}, '교안의 인용 서지로 확인', publisher='한국지능정보사회진흥원'),
 R('sweeney2002k', 'article-journal', 'k-anonymity: A model for protecting privacy', [{'family': 'Sweeney', 'given': 'Latanya'}], 2002, 'background', ['lab:concept/k-anonymity'], 'lab:work/sweeney2002',
   {'title': True, 'authors': True, 'year': True, 'venue': True, 'doi': False, 'pages': True}, '웹 검색으로 서지 확인 2026-11-09 (dataprivacylab.org, Harvard HKS 목록)', 'DOI 미확인',
   volume='10', issue='5', page='557-570', **{'container-title': 'International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems'}),
]
