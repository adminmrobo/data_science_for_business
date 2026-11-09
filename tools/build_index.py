#!/usr/bin/env python3
"""목차(index.html) 조립 — 주차 카드는 WEEKS 표를 고치면 된다 (ready=True면 링크가 켜짐)."""
import os, sys, subprocess, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import PACK, REPO, SERIES, BASE_URL, DATE, sprites

WEEKS = [
 (1, '비즈니스 데이터 과학의 이해', '데이터는 많은데, 결정은 왜 틀릴까', 'DIKW 계단 · 생존자 편향 · 상관과 인과 · A/B 테스트', '📊', 'week01_business_data_science.html', True, '초파리 승'),
 (2, '비즈니스 데이터의 수집 및 처리 기술', '데이터는 어디서 오는가', '산업별 데이터 · 수집 방법 · 배치와 스트림 · TCO · k-익명성', '📡', 'week02_data_collection.html', True, '조건부'),
 (3, '데이터 분석을 위한 준비', '분석 전에 데이터를 손보다', 'SMART · 결측값 · 이상값 · 품질 6차원 · EDA', '🧹', 'week03_analysis_prep.html', True, '주판봇 승'),
 (4, '데이터 분석 개념의 이해', '도구와 알고리즘의 지도', '도구 고르기 · 규칙 vs KNN · K와 교차 검증 · 장바구니 연관 규칙', '🧰', 'week04_analysis_concepts.html', True, '주판봇 승'),
 (5, '데이터 분석 모형: 분류모형(1)', '도미와 빙어', '파이썬 데이터 구조 · 입력 점검 · zip과 라벨 · KNN 예측', '🐟', 'week05_classification_1.html', True, '무승부'),
 (6, '데이터 분석 모형: 분류모형(2)', '농어가 끼어들자', '3클래스 KNN · K 고르기 · SVM과 커널 · 층화 분할 · 표준화', '🎣', 'week06_classification_2.html', True, '초파리 승'),
 (7, '비즈니스 데이터 분석 모델의 평가', '정확도 95%의 함정', '혼동행렬 · 정밀도·재현율 · ROC·AUC · 앙상블 · 학습률', '⚖️', 'week07_model_evaluation.html', True, '주판봇 승'),
 (8, '연습 ①', '1~7주차 문제풀이', '교안 연습문제 21문 · 계산·사례 문제 7문 · 주차별 점수', '✏️', 'week08_practice_1.html', True, ''),
 (9, '데이터 분석 모형: 회귀모형(1)', '숫자를 맞히는 선', 'KNN 회귀 · 최소제곱 · 다항 회귀 · MSE·RMSE·MAE · R²', '🎯', 'week09_regression_1.html', True, '조건부'),
 (10, '데이터 분석 모형: 회귀모형(2)', 'S자 곡선과 스무고개', '로지스틱 회귀 · 지니 불순도 · 나무 깊이 · 특성공학 · 릿지·라쏘', '🌳', 'week10_regression_2.html', True, '초파리 승'),
 (11, '데이터 모델 최적화와 시계열 모형', '시간이 기억하는 숫자', '차트 선택 · ACF·PACF · 시계열 분해 · 차분 · ARIMA', '📅', 'week11_time_series.html', True, '주판봇 승'),
 (12, '효과적인 비즈니스 데이터 시각화', '숫자의 얼굴', '대표값 · 분산도·변동계수 · 왜도·첨도 · 상관 · 차트 선택', '📊', 'week12_visualization.html', True, '초파리 승'),
 (13, '비즈니스 인텔리전스와 KPI 설계', '계기판을 설계하다', 'ETL · 재고 KPI · 광고 퍼널 · 어트리뷰션 · CLV : CAC', '🧭', 'week13_bi_kpi.html', True, '조건부'),
 (14, '비즈니스를 위한 고급 분석 기법', '정답 없이, 글 속에서, 층을 쌓아', 'K-means · 연관 규칙 · 감성 분석 · TF-IDF · 신경망', '🧠', 'week14_advanced_analytics.html', True, '무승부'),
 (15, '연습 ②', '9~14주차 문제풀이', '교안 연습문제 18문 · 계산·사례 문제 6문 · 주차별 점수', '✏️', 'week15_practice_2.html', True, ''),
]

def card(w):
    n, t, sub, desc, ico, f, ready, duel = w
    if ready is None:
        return '<div class="wk exam"><span class="no">%02d주차</span><b>%s</b><p class="muted">시험 주간</p></div>' % (n, t)
    inner = '<span class="no">%02d주차</span><span class="ico" aria-hidden="true">%s</span><b>%s</b>%s<p class="muted">%s</p>%s' % (
        n, ico, html.escape(sub or t), ('<small>교안: %s</small>' % html.escape(t)) if sub else '', html.escape(desc),
        ('<span class="lvtag g">대결: %s</span>' % duel) if duel else '<span class="lvtag">연습 · 문제풀이</span>')
    return ('<a class="wk" href="%s">%s</a>' % (f, inner)) if ready else '<div class="wk soon">%s</div>' % inner

def main():
    css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'engine.css'), encoding='utf-8').read()
    spr = sprites(['doc_front', 'asst_smile', 'fly_point', 'robo_coin'])
    cards = ''.join(card(w) for w in WEEKS)
    out = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>비즈니스를 위한 데이터 과학 연구실</title>
<meta name="description" content="안상선의 강의 교안 「비즈니스를위한데이터과학」을 박사·조수·초파리 연구원·주판봇이 진행하는 연구실 해설 대시보드로 다시 쓴 시리즈. 주차별 시뮬레이션과 대결, 실습 사례.">
<meta property="og:title" content="비즈니스를 위한 데이터 과학 연구실"><meta property="og:url" content="{url}">
<meta name="citation_title" content="비즈니스를 위한 데이터 과학 연구실"><meta name="citation_author" content="안상선"><meta name="dc.language" content="ko">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M8 0l7 4v8l-7 4-7-4V4z' fill='%239ab8ff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap">
<style>
{css}
.weeks{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}}
.wk{{background:var(--panel);border:1px solid var(--rule);border-radius:12px;padding:16px;display:flex;flex-direction:column;gap:6px;text-decoration:none;color:var(--text);min-width:0;position:relative}}
a.wk:hover{{border-color:var(--seq)}}
.wk .no{{font-size:12px;color:var(--seq);font-weight:700;letter-spacing:.06em}}
.wk .ico{{position:absolute;right:14px;top:12px;font-size:26px}}
.wk b{{font-size:17px}}
.wk small{{color:var(--muted);font-size:12px}}
.wk .lvtag{{align-self:flex-start;margin-top:auto}}
.wk.soon{{opacity:.6}}
.wk.exam{{background:transparent;border-style:dashed;justify-content:center}}
@media (max-width:860px){{.weeks{{grid-template-columns:repeat(2,minmax(0,1fr))}}}}
@media (max-width:520px){{.weeks{{grid-template-columns:1fr}}}}
</style>
</head>
<body>
<nav class="top" aria-label="바로가기"><div class="wrap"><a class="logo" href="#top"><i></i>연구실</a><div class="links"><a href="#start">처음이라면</a><a href="#weeks">주차</a><a href="#practice">실습 사례</a><a href="#how">보는 법</a><a href="#about">저자·출처</a></div></div></nav>
<!-- lab-cover -->
<header class="cover" id="top" data-img="cover_index" data-alt="밤의 연구실 복도. 주차마다 다른 색 빛이 새는 문들 앞에 박사·조수·초파리 연구원·주판봇이 서 있는 표지" role="img" aria-label="밤의 연구실 복도 앞에 선 네 캐릭터 표지"><div class="fallback" aria-hidden="true"><img data-who="fly" data-mood="point" alt="" style="transform:scaleX(-1)"><img data-who="doc" data-mood="front" alt=""><span class="prop">📚</span><img data-who="asst" data-mood="smile" alt=""><img data-who="robo" data-mood="coin" alt=""></div><span class="cover-chip">{series}</span></header>
<!-- /lab-cover -->
<header class="hero"><div class="wrap" style="padding-block:40px 32px"><div class="stack">
  <span class="eyebrow">강의 교안 · 연구실 해설 대시보드 시리즈</span>
  <h1>비즈니스를 위한 데이터 과학 연구실</h1>
  <p class="q">데이터로 더 나은 비즈니스 결정을 내리려면, 무엇을 알고 무엇을 의심해야 할까?</p>
  <p class="lead">강의 교안 「비즈니스를위한데이터과학」(전 15주)의 13개 주차와 8·15주차 연습(문제풀이)을 박사 · 조수(하루) · 초파리 연구원 · 주판봇이 진행하는 해설 페이지로 다시 썼습니다. 페이지마다 직접 돌려 보는 장난감 실험, 초파리 연구원과 주판봇의 대결, 확인 퀴즈, 지식 색인과 온톨로지·서지 꾸러미가 들어 있습니다. 교안의 실습 사례는 아래 '실습 사례'에 차례로 더합니다.</p>
  <div class="kpis k4"><div class="kpi i"><b>15</b><span>강의 주차(해설 13 · 연습 2)</span></div><div class="kpi g"><b>{ready}</b><span>공개한 주차</span></div><div class="kpi a"><b>2</b><span>연습 주차(8·15주차 문제풀이)</span></div><div class="kpi m"><b>추가 예정</b><span>실습 사례</span></div></div>
</div></div></header>
<section class="plain" id="start" aria-label="AI를 처음 접하는 분께"><div class="wrap"><div class="plainbox">
  <h2>AI를 처음 접하는 분께 — 이렇게 읽으세요</h2>
  <dl class="p3">
    <div><dt>누구를 위해</dt><dd>AI·통계를 배운 적 없는 경영·사무직을 기준으로 썼습니다. 코드나 수식을 몰라도 됩니다.</dd></div>
    <div><dt>먼저 볼 곳</dt><dd>각 페이지 첫 화면 아래 <b>「처음 오신 분께 — 이 페이지를 3줄로」</b> 상자입니다. 무엇을 배우는지, 왜 중요한지, 업무에서 어떻게 쓰는지가 있습니다. 영어 약어 풀이도 그 상자에 모아 두었습니다.</dd></div>
    <div><dt>읽는 순서</dt><dd>1~4주차(데이터·문제 정의) → 12~13주차(숫자 읽기·대시보드) → 7주차(모델 성적표 읽기) → 나머지 순으로 읽어도 됩니다. 다 읽었으면 8·15주차 연습에서 문제를 풀어 다시 볼 곳을 찾습니다. 5·6·9·10주차는 파이썬 실습을 따라가는 주라 코드가 조금 나오지만, 코드는 접힌 상자 안에 있습니다.</dd></div>
    <div><dt>바로 쓰는 법</dt><dd>각 실험에서 버튼·슬라이더를 움직여 결과가 어떻게 바뀌는지 봅니다. 밑줄 낱말에 마우스를 올리면 뜻이 나옵니다. 대결 끝의 판정이 그 주의 업무 결론입니다.</dd></div>
  </dl>
</div></div></section>
<section class="level" id="weeks"><div class="wrap stack">
  <h2>주차별 해설</h2>
  <div class="weeks">{cards}</div>
  <p class="muted" style="font-size:14px">대결 결과는 시리즈 전체에서 한쪽으로 쏠리지 않게 설계합니다. 전체 13편: 초파리 승 4 · 주판봇 승 4 · 무승부 2 · 조건부 3.</p>
</div></section>
<section class="level" id="practice"><div class="wrap stack">
  <h2>실습 사례 <span class="lvtag">추가 예정</span></h2>
  <p class="lead">교안의 실습(Google Colab 등) 사례를 같은 연구실 형식으로 이 자리에 더합니다. 파일은 저장소의 <code>practice/</code> 폴더에 들어갑니다.</p>
</div></section>
<section class="level" id="how"><div class="wrap stack">
  <h2>이 시리즈를 보는 법</h2>
  <div class="steps">
    <div><b>사다리를 오른다</b><p>각 주차는 3~5칸의 사다리입니다. 칸마다 앞 칸이 못 푼 문제를 풀고, 자기 한계로 끝나 다음 칸을 부릅니다.</p></div>
    <div><b>직접 돌려 본다</b><p>모든 실험은 브라우저에서 돌아가고, 데이터는 시드를 고정한 장난감 데이터입니다. 캔버스의 노란 도장이 그 표시입니다.</p></div>
    <div><b>지식을 가져간다</b><p>페이지 끝의 지식 색인에서 개념을 찾고, 꾸러미에서 온톨로지(JSON-LD·Turtle·CSV)와 서지(BibTeX·RIS)를 내려받습니다.</p></div>
  </div>
  <div class="cast">
    <div><img data-who="doc" data-mood="front" alt="" aria-hidden="true"><b style="color:var(--c-doc)">박사</b><p class="muted">해설과 판정</p></div>
    <div><img data-who="asst" data-mood="smile" alt="" aria-hidden="true"><b style="color:var(--c-asst)">조수(하루)</b><p class="muted">실험과 숫자 발표</p></div>
    <div><img data-who="fly" data-mood="point" alt="" aria-hidden="true"><b style="color:var(--c-fly)">초파리 연구원</b><p class="muted">의심하는 쪽</p></div>
    <div><img data-who="robo" data-mood="coin" alt="" aria-hidden="true"><b style="color:var(--c-robo)">주판봇</b><p class="muted">확신하는 쪽</p></div>
  </div>
</div></section>
<footer id="about"><div class="wrap stack">
  <div><h3>저자·출처</h3><p>교안 저자: 안상선. 이 시리즈의 모든 페이지는 저자의 강의 교안 「비즈니스를위한데이터과학」을 바탕으로 하며, 교안이 인용한 자료의 출처는 각 페이지 바닥글에 적었습니다. 교안의 기업 사례는 인용 자료의 시점 기준입니다.</p></div>
  <p>글 · 안상선 ((주)M-Robo 대표) · <a href="https://adminmrobo.github.io/who_am_i/who_am_i.html" target="_blank" rel="noopener">저자 소개</a> · {date}<br>캐릭터: 박사 · 조수(하루) · 초파리 연구원 · 주판봇 — 캐릭터 이름·설정·그림의 저작권은 안상선(개인)에게 있으며 허락 없이 쓸 수 없습니다. 그림: 캐릭터 팩 (fruitfly-lab-expressions @ 5269662).</p>
</div></footer>
<script>
{spr}
(function(){{var S=window.SPRITE||{{}},A=window.SPRITE_ALIAS||{{}};document.querySelectorAll('img[data-who]').forEach(function(i){{var k=i.dataset.who+'_'+i.dataset.mood;var s=S[k]||S[A[k]];if(s)i.src=s;}});
var c=document.querySelector('.cover[data-img]');if(c&&S[c.dataset.img]){{var im=document.createElement('img');im.className='cv';im.alt=c.dataset.alt;im.width=1600;im.height=900;im.src=S[c.dataset.img];var fb=c.querySelector('.fallback');if(fb)fb.remove();c.insertBefore(im,c.firstChild);}}}})();
</script>
</body>
</html>
'''.format(css=css, spr=spr, cards=cards, series=SERIES, url=BASE_URL, date=DATE, ready=sum(1 for w in WEEKS if w[6]))
    open(os.path.join(REPO, 'index.html'), 'w', encoding='utf-8').write(out)
    print('index.html %.1f KB' % (len(out.encode()) / 1024))

if __name__ == '__main__':
    main()
