#!/usr/bin/env python3
"""8주차·15주차 연습(문제풀이) 페이지 조립 — practice_data.py의 문제를 단일 HTML로."""
import os, sys, html, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import REPO, SERIES, BASE_URL, DATE, VERSION, sprites, plain_box
from practice_data import PAGES, WEEKFILE

E = html.escape
CSS_EXTRA = '''
.qgrp{display:flex;flex-direction:column;gap:14px}
.qgrp h3 a{color:var(--seq);text-decoration:none;font-weight:500;font-size:14px;margin-left:8px}
.pq{background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:14px 16px}
.pq .stem{font-weight:500;margin:0 0 10px}
.pq .stem .no{color:var(--amber);font-weight:700;margin-right:6px}
.pq label{display:flex;gap:8px;align-items:flex-start;padding:6px 8px;border-radius:6px;cursor:pointer;line-height:1.5}
.pq label:hover{background:var(--panel2)}
.pq input[type=radio]{margin-top:5px;flex:none}
.pq label.ok{background:rgba(127,209,139,.16)}
.pq label.ng{background:rgba(240,96,77,.16)}
.fb{margin-top:8px;font-size:14px;line-height:1.6}
.fb .g{color:var(--gfp)}.fb .r{color:var(--eye)}
.pc{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--amber);border-radius:10px;padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.pc h3{margin:0}
.pc h3 small{display:block;color:var(--amber);font-weight:500;font-size:13px;margin-bottom:2px}
.pc p{margin:0}
.ptab{border-collapse:collapse;font-size:14px;margin:4px 0;max-width:100%;display:block;overflow-x:auto}
.ptab th,.ptab td{border:1px solid var(--rule);padding:6px 10px;text-align:center;white-space:nowrap}
.ptab th{background:var(--panel2);font-weight:500}
.inrow{display:flex;flex-wrap:wrap;align-items:center;gap:8px}
.inrow label{flex:1 1 240px;font-size:14px}
.inrow input{width:120px;background:var(--bg);color:var(--text);border:1px solid var(--rule);border-radius:6px;padding:6px 8px;font:inherit}
.inrow .unit{color:var(--muted);font-size:13px;min-width:40px}
.inrow .mk{width:22px;text-align:center;font-weight:700}
.mk.g{color:var(--gfp)}.mk.r{color:var(--eye)}
.pc details{border:1px solid var(--rule);border-radius:8px;padding:8px 12px;background:var(--bg)}
.pc details summary{cursor:pointer;color:var(--seq);font-weight:500}
.pc details ol{margin:8px 0 0;padding-left:20px;line-height:1.7}
.pc .work{font-size:14px;color:var(--muted)}.pc .work b{color:var(--text)}
.pc .fly{display:flex;gap:10px;align-items:flex-start;margin-top:8px}
.pc .fly img{width:40px;height:40px;image-rendering:pixelated;flex:none}
.scoreboard{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.scoreboard div{background:var(--panel);border:1px solid var(--rule);border-radius:8px;padding:10px 12px}
.scoreboard b{display:block;font-size:20px}
.scoreboard a{color:var(--seq);font-size:13px}
'''

def quiz_html(P):
    out, k = [], 0
    for w in P['weeks']:
        f, t = WEEKFILE[w]
        items = [q for q in P['quiz'] if q['week'] == w]
        qs = []
        for q in items:
            k += 1
            opts = ''.join('<label><input type="radio" name="q%d" value="%d"><span>%s %s</span></label>' % (k, i, '①②③④'[i], E(o)) for i, o in enumerate(q['opts']))
            qs.append('<div class="pq" data-k="%d" data-w="%d" data-ans="%d"><p class="stem"><span class="no">%d.</span>%s</p>%s<div class="fb" aria-live="polite"></div>'
                      '<template>%s</template></div>' % (k, w, q['ans'], k, E(q['q']), opts, E(q['exp'])))
        out.append('<div class="qgrp"><h3>%d주차 · %s<a href="%s">해설 다시 보기 →</a></h3>%s</div>' % (w, E(t), f, ''.join(qs)))
    return ''.join(out), k

def calc_html(P):
    out = []
    for j, c in enumerate(P['calc']):
        f, t = WEEKFILE[c['week']]
        ch = ''
        if c['choice']:
            opts, ans = c['choice']
            ch = '<div class="pq" data-k="c%d" data-w="%d" data-ans="%d" data-calc="1"><p class="stem">먼저 판단해 보세요</p>%s<div class="fb" aria-live="polite"></div><template>단계별 풀이를 펼쳐 이유를 확인해 보세요.</template></div>' % (
                j, c['week'], ans, ''.join('<label><input type="radio" name="c%d" value="%d"><span>%s</span></label>' % (j, i, E(o)) for i, o in enumerate(opts)))
        ins = ''.join('<div class="inrow"><label for="in%d_%d">%s</label><input id="in%d_%d" inputmode="decimal" autocomplete="off" data-ans="%s" data-tol="%s" data-w="%d"><span class="unit">%s</span><span class="mk" aria-live="polite"></span></div>' % (
            j, i, E(lab), j, i, a, tol, c['week'], E(u)) for i, (lab, a, tol, u) in enumerate(c['inputs']))
        btn = '<div><button class="bt primary" type="button" data-check="%d">채점하기</button> <span class="muted" style="font-size:13px">쉼표·단위는 빼고 숫자만 넣어도 됩니다.</span></div>' % j if c['inputs'] else ''
        out.append('<article class="pc" id="calc%d"><h3><small>%d주차 · %s</small>%s</h3><p>%s</p>%s%s%s%s'
                   '<details><summary>단계별 풀이 보기</summary><ol>%s</ol></details>'
                   '<details><summary>초파리의 흔한 실수 보기</summary><div class="fly"><img data-who="fly" data-mood="point" alt="" aria-hidden="true"><p>%s</p></div></details>'
                   '<p class="work"><b>업무에서는</b> — %s <a href="%s">%d주차 해설 →</a></p></article>' % (
            j, c['week'], E(t), E(c['title']), c['story'], c['table'], ch, ins, btn,
            ''.join('<li>%s</li>' % s for s in c['steps']), E(c['mistake']), E(c['work']), f, c['week']))
    return ''.join(out)

JS = r'''
(function(){
var S=window.SPRITE||{},A=window.SPRITE_ALIAS||{};
document.querySelectorAll('img[data-who]').forEach(function(i){var k=i.dataset.who+'_'+i.dataset.mood;var s=S[k]||S[A[k]];if(s)i.src=s;});
var c=document.querySelector('.cover[data-img]');if(c&&S[c.dataset.img]){var im=document.createElement('img');im.className='cv';im.alt=c.dataset.alt;im.width=1600;im.height=900;im.src=S[c.dataset.img];var fb=c.querySelector('.fallback');if(fb)fb.remove();c.insertBefore(im,c.firstChild);}
var WEEKS=__WEEKS__,FILES=__FILES__,st={};
function rec(key,w,ok){st[key]={w:w,ok:ok};score();}
document.querySelectorAll('.pq').forEach(function(q){
  q.addEventListener('change',function(e){
    var v=+e.target.value,a=+q.dataset.ans,fb=q.querySelector('.fb'),exp=q.querySelector('template').innerHTML;
    q.querySelectorAll('label').forEach(function(l,i){l.classList.remove('ok','ng');if(i===a)l.classList.add('ok');else if(i===v)l.classList.add('ng');});
    fb.innerHTML=(v===a?'<b class="g">정답입니다.</b> ':'<b class="r">아쉬워요. 정답은 '+'①②③④'.charAt(a)+'번입니다.</b> ')+exp;
    if(q.dataset.calc){fb.innerHTML=(v===a?'<b class="g">맞게 판단했어요.</b> ':'<b class="r">다시 생각해 볼 만해요.</b> ')+exp;}
    rec('q'+q.dataset.k,+q.dataset.w,v===a);
  });
});
function num(s){s=(s||'').replace(/[,\s%원만g년건백]/g,'').replace('−','-');if(s==='')return NaN;return parseFloat(s);}
document.querySelectorAll('[data-check]').forEach(function(b){
  b.addEventListener('click',function(){
    var j=b.dataset.check,all=true;
    document.querySelectorAll('#calc'+j+' input[data-ans]').forEach(function(inp){
      var v=num(inp.value),a=+inp.dataset.ans,t=+inp.dataset.tol,ok=!isNaN(v)&&Math.abs(v-a)<=t+1e-9,mk=inp.parentNode.querySelector('.mk');
      mk.textContent=isNaN(v)?'?':(ok?'○':'×');mk.className='mk '+(ok?'g':'r');if(!ok)all=false;
      rec(inp.id,+inp.dataset.w,ok);
    });
    if(!all){var d=document.querySelector('#calc'+j+' details');}
  });
});
function score(){
  var qa=0,qt=0,ca=0,ct=0,per={};
  WEEKS.forEach(function(w){per[w]=[0,0];});
  Object.keys(st).forEach(function(k){var r=st[k];per[r.w][1]++;if(r.ok)per[r.w][0]++;if(k.charAt(0)==='q'&&k.charAt(1)!=='c'){qt++;if(r.ok)qa++;}else{ct++;if(r.ok)ca++;}});
  document.getElementById('scQ').textContent=qa+' / '+qt;
  document.getElementById('scC').textContent=ca+' / '+ct;
  var weak=[],h='';
  WEEKS.forEach(function(w){var p=per[w];h+='<div><span class="muted">'+w+'주차</span><b>'+(p[1]?p[0]+' / '+p[1]:'–')+'</b><a href="'+FILES[w]+'">해설로 가기 →</a></div>';if(p[1]&&p[0]/p[1]<.7)weak.push(w+'주차');});
  document.getElementById('scW').innerHTML=h;
  document.getElementById('scSay').textContent=Object.keys(st).length===0?'문제를 풀면 여기에 주차별 점수가 쌓여요.':(weak.length?'정답률이 70%에 못 미친 곳: '+weak.join(', ')+'. 해설 페이지의 그 주차 실험을 한 번 더 돌려 보세요.':'지금까지 푼 문제는 모든 주차에서 70% 이상 맞혔어요.');
}
score();
})();
'''

def build(key):
    P = PAGES[key]
    css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'engine.css'), encoding='utf-8').read() + CSS_EXTRA
    spr = sprites(['doc_front', 'doc_think', 'asst_smile', 'asst_report', 'fly_point', 'fly_clip', 'robo_coin', 'robo_calc'])
    qh, nq = quiz_html(P)
    ch = calc_html(P)
    nc = len(P['calc'])
    url = BASE_URL + P['file']
    rng = P['range']
    hero = '''<header class="hero" id="hero"><div class="wrap hero-grid"><div class="hero-text">
  <span class="eyebrow">{series} · {no}주차 · 연습</span>
  <h1>{title}</h1>
  <p class="q">{q}</p>
  <p class="lead">{lead}</p>
  <div class="kpis k3" aria-label="숫자 요약"><div class="kpi i"><b>{nq}문</b><span>교안 연습문제({rng})<sup>[1]</sup></span></div><div class="kpi a"><b>{nc}문</b><span>계산·사례 문제(예시값)</span></div><div class="kpi g"><b>70%</b><span>주차별로 다시 볼 기준 정답률</span></div></div>
</div>
<div class="pixelart"><div class="cast" style="grid-template-columns:repeat(2,1fr)">
  <div><img data-who="doc" data-mood="think" alt="" aria-hidden="true"><b style="color:var(--c-doc)">박사</b><p class="muted">문제를 냅니다</p></div>
  <div><img data-who="asst" data-mood="report" alt="" aria-hidden="true"><b style="color:var(--c-asst)">조수(하루)</b><p class="muted">채점합니다</p></div>
  <div><img data-who="fly" data-mood="point" alt="" aria-hidden="true"><b style="color:var(--c-fly)">초파리 연구원</b><p class="muted">흔한 실수를 대신 저질러 줍니다</p></div>
  <div><img data-who="robo" data-mood="calc" alt="" aria-hidden="true"><b style="color:var(--c-robo)">주판봇</b><p class="muted">단계별로 계산합니다</p></div>
</div></div></div>
<div class="wrap" style="padding-block:0 40px"><div class="dialog">
  <div class="say" data-who="doc"><img class="who" data-who="doc" data-mood="think" alt="" aria-hidden="true"><div><b class="name">박사</b><p>{rng}를 지나왔으니 오늘은 새 내용 없이 문제만 풉니다. 틀린 곳이 곧 다시 볼 곳이에요.</p></div></div>
  <div class="say" data-who="fly"><img class="who" data-who="fly" data-mood="point" alt="" aria-hidden="true"><div><b class="name">초파리 연구원</b><p>내가 먼저 풀어 볼게. 틀리면… 그게 "흔한 실수" 칸에 들어가는 거지?</p></div></div>
  <div class="say" data-who="robo"><img class="who" data-who="robo" data-mood="calc" alt="" aria-hidden="true"><div><b class="name">주판봇</b><p>계산 문제는 엑셀이나 계산기로 따라 할 수 있는 숫자만 골랐어. 풀이는 한 줄씩 적어 둘게.</p></div></div>
</div></div></header>
'''.format(series=SERIES, no=P['no'], title=E(P['title']), q=E(P['q']), lead=E(P['lead']), nq=nq, nc=nc, rng=rng)
    cover = ('<!-- lab-cover -->\n<header class="cover" id="cover" data-img="cover_w%02d" data-alt="%s" role="img" aria-label="%s">'
             '<div class="fallback" aria-hidden="true"><img data-who="fly" data-mood="point" alt="" style="transform:scaleX(-1)"><img data-who="doc" data-mood="front" alt="">'
             '<span class="prop">✏️</span><img data-who="asst" data-mood="smile" alt=""><img data-who="robo" data-mood="coin" alt=""></div>'
             '<span class="cover-chip">%s · %d주차 연습</span></header>\n<!-- /lab-cover -->\n') % (P['no'], E(P['cover_alt']), E(P['cover_alt']), SERIES, P['no'], )
    body = cover + hero
    body = body + plain_box(key, hero + qh + ch)
    body += '''<section class="level" id="quiz"><div class="wrap stack">
  <div class="lvhead"><h2>1부 · 교안 연습문제 ({nq}문)</h2><p class="lead">교안 각 주차 끝의 연습문제입니다. 보기를 고르면 바로 정답과 해설이 나옵니다.</p></div>
  {qh}
</div></section>
<section class="level" id="calc"><div class="wrap stack">
  <div class="lvhead"><h2>2부 · 계산·사례 문제 ({nc}문)</h2><p class="lead">주차마다 하나씩, 업무 장면으로 만든 문제입니다. 숫자는 모두 설명을 위해 만든 예시값입니다. 답을 넣고 「채점하기」를 누르세요.</p></div>
  {ch}
</div></section>
<section class="level" id="score"><div class="wrap stack">
  <div class="lvhead"><h2>내 점수와 다시 볼 곳</h2></div>
  <section class="kpis k2"><div class="kpi i"><b id="scQ">0 / 0</b><span>교안 연습문제</span></div><div class="kpi a"><b id="scC">0 / 0</b><span>계산·사례 문제(판단 포함)</span></div></section>
  <div class="scoreboard" id="scW"></div>
  <div class="say" data-who="asst"><img class="who" data-who="asst" data-mood="report" alt="" aria-hidden="true"><div><b class="name">조수</b><p id="scSay"></p></div></div>
  <p class="muted" style="font-size:13px">점수는 이 화면에만 남고 어디에도 저장되지 않습니다. 새로고침하면 처음부터입니다.</p>
</div></section>
'''.format(nq=nq, nc=nc, qh=qh, ch=ch)
    pv, nx = P['prev'], P['next']
    prevnext = '<a href="%s"><small>← 이전 · %s</small>%s</a><a href="index.html"><small>목차</small>%s</a><a href="%s"><small>다음 · %s</small>%s →</a>' % (pv[0], pv[1], E(pv[2]), SERIES, nx[0], nx[1], E(nx[2]))
    if nx[0] == 'index.html':
        prevnext = '<a href="%s"><small>← 이전 · %s</small>%s</a><a href="index.html"><small>목차</small>%s</a>' % (pv[0], pv[1], E(pv[2]), SERIES)
    wk = ', '.join('%d' % w for w in P['weeks'])
    foot = '''<footer id="footer"><div class="wrap stack">
  <div class="serieslinks">{pn}</div>
  <div><h3>출처</h3><ol style="margin:0;padding-left:20px"><li>안상선. 「비즈니스를위한데이터과학」 강의 교안, {wk}주차 「연습문제」. 1부 문항·보기·정답·해설은 교안 원문이며, 해설은 읽기 쉽게 다듬었습니다.</li></ol></div>
  <div><h3>예시값·설명용 모형인 것</h3><ul style="margin:0;padding-left:20px"><li>2부 계산·사례 문제의 숫자(비용, 매출, 고객 수, 오차, 광고 실적 등)는 모두 설명을 위해 만든 예시값입니다. 실제 기업이나 교안 실습 데이터의 값이 아닙니다.</li></ul></div>
  <p>글 · 안상선 ((주)M-Robo 대표) · {series} {no}주차 연습 · v{ver} · {date}<br>캐릭터: 박사 · 조수(하루) · 초파리 연구원 · 주판봇 — 캐릭터 이름·설정·그림의 저작권은 안상선(개인)에게 있으며 허락 없이 쓸 수 없습니다. 그림: 캐릭터 팩 (fruitfly-lab-expressions @ 5269662).</p>
</div></footer>'''.format(pn=prevnext, wk=wk, series=SERIES, no=P['no'], ver=VERSION, date=DATE)
    files = {w: WEEKFILE[w][0] for w in P['weeks']}
    js = JS.replace('__WEEKS__', json.dumps(P['weeks'])).replace('__FILES__', json.dumps({str(k): v for k, v in files.items()}))
    out = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="article"><meta property="og:title" content="{title}"><meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap">
<style>
{css}
</style>
</head>
<body>
<nav class="top" aria-label="섹션 바로가기"><div class="wrap"><a class="logo" href="index.html"><i></i>연구실</a><div class="links"><a href="#hero">시작</a><a href="#plain">처음이라면</a><a href="#quiz">1부 연습문제</a><a href="#calc">2부 계산 문제</a><a href="#score">내 점수</a></div></div></nav>
{body}
{foot}
<script>
{spr}
{js}
</script>
</body>
</html>
'''.format(title=E('%d주차 연습 · %s' % (P['no'], P['title'])), desc=E(P['lead']), url=url, css=css, body=body, foot=foot, spr=spr, js=js)
    open(os.path.join(REPO, P['file']), 'w', encoding='utf-8').write(out)
    print('%s %.1f KB  교안 %d문 · 계산 %d문' % (P['file'], len(out.encode()) / 1024, nq, nc))

if __name__ == '__main__':
    for k in (sys.argv[1:] or ['08', '15']):
        build(k)
