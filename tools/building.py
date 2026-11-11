# 가상 다국적 기업 본사 — 층 = 주차, 방 = 칸.
# 문구만 고치면 목차의 3D 건물과 주차별 「이번 주의 층」이 함께 바뀐다.
# prop: desk(책상) · meet(회의 탁자) · server(서버 랙) · lab(검사대·생선 상자) · screen(모니터 벽) · board(화이트보드) · shelf(서가)

COMPANY = {
    'name': '오션마켓 글로벌',
    'en': 'OCEANMARKET GLOBAL',
    'tag': '12개국에서 수산물·식품을 사고팔고 온라인몰을 운영하는 가상 다국적 기업',
    'note': '교육용 가상 기업입니다. 회사 이름·부서·숫자는 모두 설명을 위해 만든 것이며 실제 기업과 관계없습니다.',
}

# 층 묶음 색 (3D 유리 색 · 목록 점 색)
GROUPS = {
    'base': ('#5b8def', '데이터 기초 (1~4층)'),
    'cls':  ('#3fbf8f', '분류 (5~7층)'),
    'prac': ('#f0b44c', '연수원 · 연습 (8·15층)'),
    'reg':  ('#a07de0', '회귀 · 시계열 (9~11층)'),
    'bi':   ('#2fb5c4', '보고 · BI · 고급 분석 (12~14층)'),
}

DUEL = ('duel', '대결 회의실', 'meet')

FLOORS = {
 1: dict(group='base', dept='경영전략실', ask='숫자는 많은데 왜 결정은 틀릴까?',
         story='임원 회의에 올라온 숫자가 결정이 되기까지 어떤 계단을 오르고, 어디서 함정에 빠지는지 따져 보는 층입니다.',
         rooms=[('lv1', '전략 회의실 · 네 계단', 'board'), ('lv2', '해지 고객 기록실', 'shelf'), ('lv3', '시장 조사실', 'desk'), ('lv4', 'A/B 실험실', 'screen'), DUEL]),
 2: dict(group='base', dept='데이터 수집센터', ask='데이터는 어디서, 얼마에, 얼마나 빨리 들어오나?',
         story='12개국 매장·온라인몰·협력사의 데이터가 들어오는 입구입니다. 수집 방법, 처리 속도, 서버 비용, 개인정보를 정합니다.',
         rooms=[('lv1', '산업별 데이터 지도실', 'board'), ('lv2', '수집 창구', 'desk'), ('lv3', '실시간 처리실', 'screen'), ('lv4', '서버실', 'server'), ('lv5', '개인정보 보호실', 'shelf'), DUEL]),
 3: dict(group='base', dept='데이터 품질관리팀', ask='분석 전에 무엇을 손봐야 하나?',
         story='들어온 데이터의 빈칸·튀는 값·중복을 고치고 품질 점수를 매깁니다. 분석 시간의 대부분이 이 층에서 쓰입니다.',
         rooms=[('lv1', '목표 설정실', 'board'), ('lv2', '빈칸 복구실', 'desk'), ('lv3', '이상값 검사대', 'lab'), ('lv4', '품질 점수판', 'screen'), ('lv5', '탐색 분석실', 'desk'), DUEL]),
 4: dict(group='base', dept='분석 기획실', ask='어떤 도구와 어떤 모델로 풀까?',
         story='문제를 받으면 도구를 고르고, 사람이 쓴 규칙과 데이터에서 배운 규칙 중 무엇을 쓸지, 어떻게 시험할지 정합니다.',
         rooms=[('lv1', '도구실', 'shelf'), ('lv2', '대출 심사 데스크', 'desk'), ('lv3', '시험 출제실', 'board'), ('lv4', '장바구니 분석실', 'screen'), DUEL]),
 5: dict(group='cls', dept='수산 품질연구소 A · 선별 라인', ask='들어온 생선이 도미인지 빙어인지 기계가 가릴 수 있나?',
         story='길이와 무게를 재서 기록하고, 정답을 붙여, 처음으로 자동 선별 모델(KNN)을 가르치는 층입니다.',
         rooms=[('lv1', '용기 보관실', 'shelf'), ('lv2', '계측대', 'lab'), ('lv3', '정답 붙이는 데스크', 'desk'), ('lv4', '자동 선별기', 'lab'), DUEL]),
 6: dict(group='cls', dept='수산 품질연구소 B · 3종 선별', ask='농어까지 섞이면 어떻게 가리나?',
         story='종류가 셋으로 늘어난 선별 라인입니다. 이웃 수를 고르고, 경계선을 긋고, 시험 데이터를 떼고, cm와 g의 눈금을 맞춥니다.',
         rooms=[('lv1', '3종 선별대', 'lab'), ('lv2', '이웃 수 조정실', 'desk'), ('lv3', '경계선 설계실', 'board'), ('lv4', '시험 샘플실', 'shelf'), ('lv5', '눈금 맞춤실', 'lab'), DUEL]),
 7: dict(group='cls', dept='고객관리 · 이탈방지팀', ask='정확도 95%짜리 이탈 예측, 믿어도 되나?',
         story='떠날 고객에게 쿠폰을 보내는 팀입니다. 모델의 성적표를 네 칸으로 나눠 읽고, 쿠폰을 보낼 기준선을 돈으로 정합니다.',
         rooms=[('lv1', '성적표실', 'screen'), ('lv2', '쿠폰 기준선 회의실', 'meet'), ('lv3', '모델 비교실', 'screen'), ('lv4', '모델 위원회실', 'meet'), ('lv5', '학습 조정실', 'desk'), DUEL]),
 8: dict(group='prac', dept='사내 연수원 · 연습 ①', ask='1~7층에서 배운 것, 문제로 확인하기',
         story='새 내용 없이 문제만 푸는 층입니다. 틀린 문제는 해당 층으로 돌아가 다시 봅니다.',
         rooms=[('quiz', '교안 문제 풀이실', 'desk'), ('calc', '계산·사례 문제실', 'desk'), ('score', '성적표 게시판', 'board')]),
 9: dict(group='reg', dept='상품 계량 · 가격팀', ask='길이만 보고 무게(값)를 맞힐 수 있나?',
         story='생선 무게를 예측해 가격을 매기는 팀입니다. 이웃 평균, 직선, 곡선으로 맞혀 보고 얼마나 빗나갔는지 잽니다.',
         rooms=[('lv1', '이웃 평균 저울', 'lab'), ('lv2', '직선 예측실', 'board'), ('lv3', '곡선 예측실', 'board'), ('lv4', '오차 측정실', 'desk'), ('lv5', '설명력 보고실', 'screen'), DUEL]),
 10: dict(group='reg', dept='신사업 심사실', ask='예/아니오를 확률로, 판단을 규칙으로 바꿀 수 있나?',
         story='합격 여부와 와인 등급을 가리는 심사실입니다. 확률로 판정하고, 스무고개 규칙을 만들고, 재료를 늘리되 벌점을 줍니다.',
         rooms=[('lv1', '확률 판정실', 'desk'), ('lv2', '스무고개실', 'board'), ('lv3', '깊이 조정실', 'desk'), ('lv4', '재료 실험실', 'lab'), ('lv5', '계수 다이어트실', 'screen'), DUEL]),
 11: dict(group='reg', dept='수요예측 · 재무실', ask='다음 달 매출은 지난 매출에서 얼마나 읽히나?',
         story='월매출을 시간 순서대로 읽는 층입니다. 지난달과 얼마나 닮았는지, 계절 반복이 있는지 보고 다음 달을 예측합니다.',
         rooms=[('lv1', '차트실', 'screen'), ('lv2', '닮음 분석실', 'desk'), ('lv3', '추세·계절 분해실', 'board'), ('lv4', '변화 측정실', 'desk'), ('lv5', '예측실', 'screen'), DUEL]),
 12: dict(group='bi', dept='경영보고 · 시각화실', ask='숫자 하나와 차트 한 장으로 어떻게 말하나?',
         story='임원 보고서를 만드는 층입니다. 대표값·흩어짐·기울어짐·함께 움직임을 읽고, 목적에 맞는 차트를 고릅니다.',
         rooms=[('lv1', '대표값 데스크', 'desk'), ('lv2', '흩어짐 측정실', 'desk'), ('lv3', '결제액 꼬리 분석실', 'screen'), ('lv4', '관계 분석실', 'board'), ('lv5', '차트 갤러리', 'screen'), DUEL]),
 13: dict(group='bi', dept='마케팅 · BI 상황실', ask='경영 계기판에는 무엇을 올리나?',
         story='12개국 데이터를 하나로 모아 계기판을 만드는 상황실입니다. 재고, 광고, 채널별 성과, 고객 가치를 한 화면에서 봅니다.',
         rooms=[('lv1', '데이터 파이프라인실', 'server'), ('lv2', '재고 관제실', 'screen'), ('lv3', '광고 퍼널실', 'screen'), ('lv4', '성과 분배 회의실', 'meet'), ('lv5', '고객 가치 분석실', 'desk'), DUEL]),
 14: dict(group='bi', dept='AI 연구소', ask='정답이 없을 때, 글일 때, 경계가 휘었을 때는?',
         story='고급 분석을 맡는 연구소입니다. 고객을 묶고, 함께 팔리는 상품을 찾고, 고객의 글을 읽고, 신경망을 시험합니다.',
         rooms=[('lv1', '고객 세분화실', 'board'), ('lv2', '장바구니 규칙실', 'desk'), ('lv3', '고객의 소리 센터', 'screen'), ('lv4', '핵심 단어실', 'desk'), ('lv5', '신경망실', 'server'), DUEL]),
 15: dict(group='prac', dept='임원 연수실 · 연습 ②', ask='9~14층에서 배운 것, 문제로 확인하기',
         story='꼭대기 층 연수실입니다. 회귀·시계열·시각화·BI·고급 분석 문제를 풀고, 틀린 곳의 층으로 내려가 다시 봅니다.',
         rooms=[('quiz', '교안 문제 풀이실', 'desk'), ('calc', '계산·사례 문제실', 'desk'), ('score', '성적표 게시판', 'board')]),
}

FILES = {
 1: 'week01_business_data_science.html', 2: 'week02_data_collection.html', 3: 'week03_analysis_prep.html',
 4: 'week04_analysis_concepts.html', 5: 'week05_classification_1.html', 6: 'week06_classification_2.html',
 7: 'week07_model_evaluation.html', 8: 'week08_practice_1.html', 9: 'week09_regression_1.html',
 10: 'week10_regression_2.html', 11: 'week11_time_series.html', 12: 'week12_visualization.html',
 13: 'week13_bi_kpi.html', 14: 'week14_advanced_analytics.html', 15: 'week15_practice_2.html',
}


def data(cur=None):
    """페이지에 심을 JSON (cur = 지금 층, 목차면 None)."""
    fl = []
    for n in range(1, 16):
        f = FLOORS[n]
        fl.append({'n': n, 'dept': f['dept'], 'ask': f['ask'], 'story': f['story'], 'color': GROUPS[f['group']][0],
                   'file': FILES[n], 'rooms': [{'id': a, 'name': b, 'prop': c} for a, b, c in f['rooms']]})
    return {'company': COMPANY, 'groups': [{'color': c, 'label': l} for c, l in GROUPS.values()], 'floors': fl, 'cur': cur}


import html as _h, json as _j, os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
NUMS = '①②③④⑤'


def _room_no(rid, i):
    if rid == 'duel': return '⚔'
    if rid.startswith('lv'): return NUMS[int(rid[2:]) - 1]
    return NUMS[i]


def assets(cur=None):
    """페이지 끝에 넣을 데이터 + 스크립트, <style>에 넣을 CSS."""
    js = open(_os.path.join(_HERE, 'building.js'), encoding='utf-8').read()
    css = open(_os.path.join(_HERE, 'building.css'), encoding='utf-8').read()
    tag = '<script type="application/json" id="bld-data">%s</script>\n<script>\n%s\n</script>\n' % (
        _j.dumps(data(cur), ensure_ascii=False).replace('</', '<\\/'), js)
    return css, tag


def _stack(cur):
    rows = []
    for n in range(15, 0, -1):
        f = FLOORS[n]; c = GROUPS[f['group']][0]
        here = ' <em>지금 여기</em>' if n == cur else ''
        rows.append('<a class="lv%s" href="%s" data-fl="%d" style="--c:%s"><b>%dF</b><span>%s</span>%s</a>' % (
            ' cur' if n == cur else '', FILES[n], n, c, n, _h.escape(f['dept']), here))
    return ('<nav class="bld-stack" aria-label="본사 건물 층 안내"><div class="roof">%s</div>%s<div class="lobby">로비 · 광장</div></nav>'
            % (_h.escape(COMPANY['en']), ''.join(rows)))


def floor_html(cur):
    f = FLOORS[cur]; c = GROUPS[f['group']][0]
    lis = []
    for i, (rid, name, _p) in enumerate(f['rooms']):
        no = _room_no(rid, i)
        sub = '이번 주의 대결' if rid == 'duel' else ''
        lis.append('<li><a href="#%s" data-room="%s"><span class="no">%s</span><b>%s</b><small>%s</small></a></li>' % (rid, rid, no, _h.escape(name), sub))
    dn = '<a href="%s">▼ %dF · %s</a>' % (FILES[cur - 1], cur - 1, _h.escape(FLOORS[cur - 1]['dept'])) if cur > 1 else '<span></span>'
    up = '<a href="%s">▲ %dF · %s</a>' % (FILES[cur + 1], cur + 1, _h.escape(FLOORS[cur + 1]['dept'])) if cur < 15 else '<span></span>'
    return '''<section class="bld-floor" id="floor" style="--c:{c}" aria-label="이번 주의 층"><div class="wrap">
  <div class="bld-grid">
    {stack}
    <div class="bld-main">
      <span class="eyebrow">{co} 본사 · 엘리베이터 안내</span>
      <h2>🛗 {n}층에 도착했습니다 — {dept}</h2>
      <p class="bld-ask"><b>이 층의 질문</b>{ask}</p>
      <p class="lead">{story}</p>
      <div class="bld-3d" id="floor3d"><button class="bt bld-reset" type="button" id="bldReset">시점 처음으로</button></div>
      <ol class="bld-rooms">{lis}</ol>
      <p class="muted bld-note">방(3D 바닥이나 아래 목록)을 누르면 그 칸으로 내려갑니다. 화면을 끌면 층을 돌려 볼 수 있습니다. {note}</p>
      <div class="bld-lift">{dn}<a href="index.html#tower">건물 전체 보기</a>{up}</div>
    </div>
  </div>
</div></section>
'''.format(c=c, stack=_stack(cur), co=_h.escape(COMPANY['name']), n=cur, dept=_h.escape(f['dept']), ask=_h.escape(f['ask']),
           story=_h.escape(f['story']), lis=''.join(lis), note=_h.escape(COMPANY['note']), dn=dn, up=up)


def tower_html(title, sub):
    lis = []
    for n in range(15, 0, -1):
        f = FLOORS[n]; c = GROUPS[f['group']][0]
        lis.append('<li><a href="%s" data-fl="%d" style="--c:%s"><b>%dF</b><span>%s<small>%s</small></span></a></li>' % (
            FILES[n], n, c, n, _h.escape(f['dept']), _h.escape(f['ask'])))
    leg = ''.join('<span style="--c:%s">%s</span>' % (c, _h.escape(l)) for c, l in GROUPS.values())
    return '''<header class="bld-tower" id="tower"><div class="wrap">
  <div class="tw-grid">
    <div class="bld-3d tall" id="tower3d"><button class="bt bld-reset" type="button" id="bldReset">시점 처음으로</button></div>
    <div class="tw-side">
      <span class="eyebrow">{sub}</span>
      <h1>{title}</h1>
      <p class="lead"><b>{co}</b> 본사에 오신 것을 환영합니다. {tag}입니다. 15층 건물의 층마다 한 부서가 있고, 그 부서가 한 주차의 데이터 문제를 풉니다. 층을 누르면 그 주차로 올라갑니다.</p>
      <div class="bld-legend">{leg}</div>
      <ol class="tw-list">{lis}</ol>
      <p class="muted bld-note">{note}</p>
    </div>
  </div>
</div></header>
'''.format(title=_h.escape(title), sub=_h.escape(sub), co=_h.escape(COMPANY['name']), tag=_h.escape(COMPANY['tag']), leg=leg, lis=''.join(lis), note=_h.escape(COMPANY['note']))
