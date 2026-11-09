#!/usr/bin/env python3
"""비즈니스를 위한 데이터 과학 연구실 — 주차 페이지 조립기.
pages/wNN.py(설정·지식 그래프·용어·퀴즈) + pages/wNN.html(본문) + pages/wNN.js(시뮬레이션)
+ engine.css/engine.js + 캐릭터 팩 그림  →  저장소/weekNN_*.html (단일 파일)"""
import importlib.util, json, os, re, subprocess, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.environ.get('REPO', os.path.dirname(HERE))
PACK = os.environ.get('PACK') or ([p for p in __import__('glob').glob('/root/.claude/skills/synced/*/ai-lab-explainer/packs/character/character_pack')] + [os.path.join(os.path.dirname(HERE), '..', 'ahnboat_lab_explainer', 'packs', 'character', 'character_pack')])[0]
SERIES = '비즈니스를 위한 데이터 과학 연구실'
BASE_URL = 'https://adminmrobo.github.io/data_science_for_business/'
DATE = '2026-11-09'
VERSION = '1.1'
sys.path.insert(0, HERE)
from abbr import ABBR
from plain import PLAIN
from easy import EASY, ASK
from talk import DLG

def load(n):
    spec = importlib.util.spec_from_file_location('w' + n, os.path.join(HERE, 'pages', 'w%s.py' % n))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def jdump(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

ART = os.path.join(HERE, 'art')

def sprites(keys):
    """캐릭터 표정(팩) + 이 시리즈의 표지·장면 그림(tools/art/*.webp)을 SPRITE에 함께 싣는다."""
    keys = set(keys)
    art = sorted(k for k in keys if k.startswith(('cover_', 'sc_')))
    face = sorted(keys - set(art))
    out = subprocess.run([sys.executable, os.path.join(PACK, 'build_character_pack.py'), '--pack', PACK, '--pick', ','.join(face), '--size', '96'],
                         capture_output=True, text=True, check=True).stdout
    have = {k: os.path.join(ART, k + '.webp') for k in art if os.path.exists(os.path.join(ART, k + '.webp'))}
    if have:
        import base64
        out += '\nwindow.SPRITE=window.SPRITE||{};Object.assign(window.SPRITE,{%s});\n' % ','.join(
            '"%s":"data:image/webp;base64,%s"' % (k, base64.b64encode(open(p, 'rb').read()).decode()) for k, p in have.items())
    return out

LD_TYPE = {'Concept': ['skos:Concept', 'schema:DefinedTerm'], 'Method': ['skos:Concept', 'schema:DefinedTerm'], 'Task': ['skos:Concept', 'schema:DefinedTerm'],
           'Term': ['skos:Concept', 'schema:DefinedTerm'], 'Framework': ['skos:Concept', 'schema:DefinedTerm'], 'Metric': ['skos:Concept', 'schema:DefinedTerm'],
           'Work': ['schema:CreativeWork'], 'Claim': ['schema:Claim'], 'Dataset': ['schema:Dataset'], 'QuizItem': ['schema:Question'],
           'Standard': ['schema:Legislation'], 'Question': ['schema:Question']}
LD_P = {'lab:broader': 'skos:broader', 'lab:partOf': 'schema:isPartOf', 'lab:relatedTo': 'skos:related', 'lab:assertedIn': 'schema:citation'}

def jsonld(kg, meta):
    g = []
    for n in kg['nodes']:
        o = {'@id': n['id'], '@type': ['lab:' + n['type']] + LD_TYPE.get(n['type'], []),
             'skos:prefLabel': [{'@value': n['label']['ko'], '@language': 'ko'}, {'@value': n['label']['en'], '@language': 'en'}]}
        if n.get('definition'): o['skos:definition'] = {'@value': n['definition']['ko'], '@language': 'ko'}
        g.append(o)
    for e in kg['edges']:
        for o in g:
            if o['@id'] == e['s']:
                o.setdefault(e['p'], []).append({'@id': e['o']})
                if e['p'] in LD_P: o.setdefault(LD_P[e['p']], []).append({'@id': e['o']})
    return {'@context': {'skos': 'http://www.w3.org/2004/02/skos/core#', 'schema': 'https://schema.org/', 'dct': 'http://purl.org/dc/terms/',
                         'prov': 'http://www.w3.org/ns/prov#', 'lab': 'urn:lab:'}, '@id': meta['url'] or ('urn:lab:page/' + kg['page']), '@graph': g}

def build_kg(m, slug):
    nodes, edges = [], []
    dom = m.DOMAIN
    def add(n):
        n.setdefault('page', slug); n.setdefault('domain', dom); n.setdefault('status', 'known'); n.setdefault('confidence', 'high'); n.setdefault('family', 'evaluation')
        if 'label' not in n: raise ValueError(n)
        nodes.append(n)
    for n in m.NODES: add(dict(n))
    ids = {n['id'] for n in nodes}
    # 용어 사전 → Term 노드 (이미 노드가 있으면 건너뜀)
    for k, v in m.GL.items():
        if len(v) > 3 and v[3]:
            nid = v[3]
            if nid not in ids:
                add({'id': nid, 'type': 'Term', 'label': {'ko': v[0], 'en': v[4] if len(v) > 4 else v[0]}, 'definition': {'ko': v[2]}, 'anchor': v[5] if len(v) > 5 else '#cast'}); ids.add(nid)
            else:
                for n in nodes:
                    if n['id'] == nid and 'definition' not in n: n['definition'] = {'ko': v[2]}
    for e in m.EDGES:
        s, p, o, a = e[:4]
        edges.append({'s': s, 'p': p, 'o': o, 'anchor': a, 'confidence': e[4] if len(e) > 4 else 'high'})
    # 퀴즈 → QuizItem
    qn = 0
    for sec, items in m.QZ.items():
        for it in items:
            qn += 1
            qid = 'lab:quiz/%s-%s' % (slug, it['id'])
            add({'id': qid, 'type': 'QuizItem', 'label': {'ko': '퀴즈 %d' % qn, 'en': 'Quiz %d' % qn}, 'anchor': '#' + sec, 'family': 'quiz'})
            edges.append({'s': qid, 'p': 'lab:assesses', 'o': it['assess'], 'anchor': '#' + sec, 'confidence': 'high'})
    ids = {n['id'] for n in nodes}
    for e in edges:
        for k in ('s', 'o'):
            if e[k] not in ids: raise SystemExit('끊긴 관계: %s in %s' % (e[k], e))
    deg = {i: 0 for i in ids}
    for e in edges: deg[e['s']] += 1; deg[e['o']] += 1
    iso = [i for i, d in deg.items() if d == 0]
    if iso: raise SystemExit('고립 노드: %s' % iso)
    rel = sum(1 for e in edges if e['p'] == 'lab:relatedTo')
    if rel > 0.15 * len(edges): raise SystemExit('relatedTo 비율 초과')
    return {'version': '1.0', 'page': slug, 'nodes': nodes, 'edges': edges}

NAVTPL = '''<nav class="top" aria-label="섹션 바로가기"><div class="wrap">
  <a class="logo" href="index.html"><i></i>연구실</a>
  <div class="links">{links}</div>
</div></nav>'''

KG_SECTION = '''<!-- 지식 색인 -->
<section class="level" id="kg"><div class="wrap stack">
  <div class="lvhead"><h2>지식 색인 — 이 페이지에서 찾아보기</h2><p class="lead" id="kgStat"></p></div>
  <div class="searchrow"><label class="glabel" for="kgq">검색</label><input class="search" id="kgq" type="search" placeholder="{ph}"></div>
  <div class="group" id="kgTypes"></div>
  <div class="kgl" id="kgList"></div>
  <h3>미니 그래프</h3>
  <div class="cwrap"><canvas id="kgG" class="wide" aria-label="개념 사이의 관계를 점과 선으로 보여 주는 그래프. 점을 누르면 목록에서 펼쳐진다"></canvas></div>
  <p class="muted" style="font-size:13px">점 색: <span style="color:var(--seq)">● 개념·방법</span> <span style="color:var(--eye)">● 한계</span> <span style="color:var(--amber)">● 질문·주장</span> <span style="color:var(--gfp)">● 지표·데이터·과제</span> <span style="color:var(--muted)">● 문헌·용어·비유</span> · 퀴즈와 시뮬레이션 노드는 숨김</p>
  <h3>사다리 경로</h3>
  <div class="flowchips" id="kgPath"></div>
  <h3>열린 질문</h3>
  <ul id="kgQ" style="margin:0;padding-left:20px"></ul>
  <div class="ctrl"><div class="group"><span class="glabel">빠른 내보내기</span><button class="bt" type="button" id="qJson">JSON 보기</button><button class="bt" type="button" id="qMer">Mermaid 보기</button></div><span class="muted" style="font-size:13px">전체 형식은 아래 꾸러미에서</span></div>
  <pre class="out" id="kgOut" hidden></pre>
</div></section>

<!-- 꾸러미 (마지막 섹션) -->
<section class="level" id="export"><div class="wrap stack">
  <div class="lvhead"><h2>온톨로지·서지 꾸러미 — 이 페이지의 지식을 가져가기</h2></div>
  <section class="kpis" id="exK"></section>
  <div class="say" data-who="asst"><img class="who" data-who="asst" data-mood="report" data-img="asst_report" alt="" aria-hidden="true"><div><b class="name">조수</b><p id="exSay"></p></div></div>
  <h3>이 페이지 인용하기</h3>
  <div class="group" id="citeFmt"></div>
  <pre class="out" id="citeOut"></pre>
  <div><button class="bt" type="button" id="citeCopy">복사</button> <span class="muted" id="citeMsg" style="font-size:13px"></span></div>
  <h3>참고문헌</h3>
  <ol class="reflist" id="refList"></ol>
  <h3>범위와 형식 고르기</h3>
  <div class="group" id="scopeG"><span class="glabel">범위</span></div>
  <div class="group" id="fileG"><span class="glabel">파일</span></div>
  <pre class="out" id="fileOut"></pre>
  <div class="ctrl"><div class="group"><button class="bt" type="button" id="fileCopy">이 파일 복사</button><button class="bt" type="button" id="fileDl">이 파일 내려받기</button><button class="bt primary" type="button" id="zipDl">꾸러미 ZIP 내려받기</button></div></div>
  <p class="muted" style="font-size:13px" id="dlMsg">ZIP 안에는 파일이 원래 이름으로 들어갑니다.</p>
  <h3>확인 필요 목록</h3>
  <ul id="todoList" style="margin:0;padding-left:20px"></ul>
  <p class="muted" style="font-size:13px" id="verLine"></p>
</div></section>'''

def plain_box(n, body):
    what, why, work, code = PLAIN[n]
    txt = re.sub(r'<script.*?</script>', ' ', body, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    found = sorted({t for t in re.findall(r'(?<![A-Za-z])([A-Z][A-Z0-9]{1,}(?:-[A-Z]+)?)(?![a-z])', txt) if t in ABBR})
    ab = ''.join('<div><dt>%s</dt><dd><b>%s</b> — %s</dd></div>' % (k, html.escape(ABBR[k][0]), html.escape(ABBR[k][1])) for k in found)
    codeline = '<p class="pnote">이 주에는 파이썬 코드가 조금 나옵니다. <b>코드를 몰라도 됩니다.</b> 버튼과 슬라이더만 움직여도 내용을 모두 따라올 수 있고, 코드는 접힌 상자 안에 넣어 두었습니다.</p>' if code else '<p class="pnote">코드나 수식을 몰라도 됩니다. 버튼과 슬라이더를 움직이며 결과가 어떻게 바뀌는지만 보면 됩니다.</p>'
    det = ('<details class="abbr"><summary>이 페이지에 나오는 영어 약어 풀이 (%d개)</summary><dl>%s</dl></details>' % (len(found), ab)) if found else ''
    return ('<section class="plain" id="plain" aria-label="처음 오신 분께"><div class="wrap"><div class="plainbox">'
            '<h2>처음 오신 분께 — 이 페이지를 3줄로</h2><dl class="p3">'
            '<div><dt>무엇을</dt><dd>%s</dd></div><div><dt>왜 중요한가</dt><dd>%s</dd></div><div><dt>업무에서는</dt><dd>%s</dd></div></dl>%s%s'
            '</div></div></section>\n') % (html.escape(what), html.escape(why), html.escape(work), codeline, det)

MODEL_LV = {('04', 'lv2'), ('05', 'lv4'), ('06', 'lv3'), ('07', 'lv4'), ('09', 'lv1'), ('09', 'lv2'), ('09', 'lv3'),
            ('10', 'lv1'), ('10', 'lv2'), ('10', 'lv3'), ('10', 'lv5'), ('11', 'lv2'), ('11', 'lv5'), ('14', 'lv1'), ('14', 'lv5')}

def easy_box(n, lv):
    e = EASY[(n, lv)]
    title = '왜 이 모델을 쓰나' if (n, lv) in MODEL_LV else '왜 이 방법을 쓰나'
    school = ('<p class="ez-school"><b>학교 수학으로 보면</b> %s</p>' % e['school']) if e['school'] else ''
    pieces = ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % (a, b) for a, b in e['pieces'])
    q, c = ASK[(n, lv)]
    say = lambda mood, t, cls: ('<div class="say ez-say %s" data-who="asst"><img class="who" data-who="asst" data-mood="%s" data-img="asst_%s" alt="" aria-hidden="true">'
                               '<div><b class="name">조수</b><p>%s</p></div></div>') % (cls, mood, mood, t)
    return ('<div class="easy" aria-label="쉽게 풀어 보기">'
            '<div class="ez-why"><h3 class="ez-h"><span class="ez-k">먼저</span>%s</h3><p>%s</p><p class="ez-like"><b>쉽게 말하면</b> %s</p></div>'
            '<div class="ez-math"><h3 class="ez-h"><span class="ez-k">수식</span>수학 수식을 어려워하는 조수가 대신 물어봅니다</h3>%s%s<dl class="ez-pieces">%s</dl>'
            '<div class="ez-try"><b>숫자로 한 번 해 보기</b><p>%s</p></div>%s</div></div>\n  ') % (title, e['why'], e['like'], say('shock', q, 'ez-q'), school, pieces, e['tryit'], say('spark', c, 'ez-c'))

def add_easy(n, body):
    for (wk, lv) in EASY:
        if wk != n:
            continue
        i = body.find('<section class="level" id="%s">' % lv)
        j = body.find('<div class="pair">', i)
        assert i >= 0 and j > i, (n, lv)
        body = body[:j] + easy_box(n, lv) + body[j:]
    return body

NAMES = {'doc': '박사', 'asst': '조수', 'fly': '초파리 연구원', 'robo': '주판봇'}

def add_talk(n, body):
    for (wk, lv), lines in DLG.items():
        if wk != n:
            continue
        i = body.find('<section class="level" id="%s">' % lv)
        end = body.find('<section class="level"', i + 10)
        j = body.find('<section class="panel"', i)
        if j < 0 or (end > 0 and j > end):
            j = body.find('<div class="explain">', i)
        assert i >= 0 and j > i, (n, lv)
        says = ''.join('<div class="say" data-who="%s"><img class="who" data-who="%s" data-mood="%s" data-img="%s_%s" alt="" aria-hidden="true"><div><b class="name">%s</b><p>%s</p></div></div>'
                       % (w, w, m, w, m, NAMES[w], t) for w, m, t in lines)
        body = body[:j] + '<div class="dialog lvtalk" aria-label="연구실 대화">' + says + '</div>\n  ' + body[j:]
    return body

def page(n):
    m = load(n)
    slug = m.SLUG
    fname = m.FILE
    url = BASE_URL + fname
    meta = {'title': m.TITLE, 'series': SERIES, 'number': n, 'creator': [{'name': '안상선', 'role': 'author', 'affiliation': '(주)M-Robo 대표', 'url': 'https://www.ahnboat.xyz'}],
            'date': DATE, 'version': VERSION, 'language': ['ko'], 'license': '', 'url': url, 'domain': m.DOMAIN,
            'about': m.ABOUT, 'educationalLevel': '입문~중급', 'learningResourceType': 'interactive explainer', 'basedOn': [r['id'] for r in m.REFS if r['lab']['role'] == 'primary'],
            'suggestedCitation': '안상선 (2026). %s. %s %s주차, v%s. %s' % (m.TITLE, SERIES, n, VERSION, url),
            'todo': ['페이지 서지: 라이선스 빈칸 (저자가 정할 것)'] + getattr(m, 'TODO', [])}
    kg = build_kg(m, slug)
    ld = jsonld(kg, meta)
    body = open(os.path.join(HERE, 'pages', 'w%s.html' % n), encoding='utf-8').read()
    pjs = open(os.path.join(HERE, 'pages', 'w%s.js' % n), encoding='utf-8').read()
    css = open(os.path.join(HERE, 'engine.css'), encoding='utf-8').read() + getattr(m, 'CSS', '')
    ejs = open(os.path.join(HERE, 'engine.js'), encoding='utf-8').read()
    keys = set(re.findall(r'data-img="((?:doc|asst|fly|robo)_[a-z]+)"', body)) | set(m.EXTRA_SPRITES) | {'asst_report', 'doc_front', 'asst_smile', 'fly_clip', 'robo_smile', 'fly_point', 'robo_coin', 'asst_shock', 'asst_spark'} | {'%s_%s' % (w, m) for (wk, lv), ls in DLG.items() if wk == n for w, m, t in ls}
    keys |= {'cover_w%s' % n, 'sc_w%s_hero' % n, 'sc_w%s_outro' % n}
    spr = sprites(keys)
    links = ''.join('<a href="%s">%s</a>' % (h, t) for h, t in m.NAV) + '<a href="#kg">지식 색인</a><a href="#export">꾸러미</a>'
    gl_js = {k: v[:3] for k, v in m.GL.items()}
    cover = ('<!-- lab-cover -->\n<header class="cover" id="cover" data-img="cover_w%s" data-alt="%s" role="img" aria-label="%s">'
             '<div class="fallback" aria-hidden="true"><img data-who="fly" data-mood="point" alt="" style="transform:scaleX(-1)"><img data-who="doc" data-mood="front" alt="">'
             '<span class="prop">%s</span><img data-who="asst" data-mood="smile" alt=""><img data-who="robo" data-mood="coin" alt=""></div>'
             '<span class="cover-chip">%s · %s주차</span></header>\n<!-- /lab-cover -->\n') % (n, html.escape(m.COVER_ALT), html.escape(m.COVER_ALT), m.COVER_PROP, SERIES, n)
    head = '''<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="citation_title" content="{title}">
<meta name="citation_author" content="안상선">
<meta name="citation_publication_date" content="2026/11/09">
<meta name="dc.title" content="{title}"><meta name="dc.creator" content="안상선"><meta name="dc.language" content="ko"><meta name="dc.date" content="{date}">
<meta property="og:type" content="article"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{ogimg}"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M8 0l7 4v8l-7 4-7-4V4z' fill='%239ab8ff'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+KR:wght@400;500;700&display=swap">
<style>
{css}
</style>
</head>
<body>
<div id="prog"></div>
<div id="tip" role="tooltip"></div>
'''.format(title=html.escape(m.TITLE), desc=html.escape(m.DESC), date=DATE, url=url, ogimg=BASE_URL + 'img/og_w%s.jpg' % n, css=css)
    foot = '''
<footer id="footer"><div class="wrap stack">
  <div class="serieslinks">{prevnext}</div>
  <div><h3>출처</h3><ol style="margin:0;padding-left:20px">{src}</ol></div>
  <div><h3>예시값·설명용 모형인 것</h3><ul style="margin:0;padding-left:20px">{ill}</ul></div>
  <p>글 · 안상선 (<a href="https://www.ahnboat.xyz" target="_blank" rel="noopener">www.ahnboat.xyz</a>) · (주)M-Robo 대표 · {series} {n}주차 · v{ver} · {date}<br>이 페이지는 저자의 강의 교안 「비즈니스를위한데이터과학」 {n}주차를 연구실 해설 형식으로 다시 쓴 것입니다. 교안에 나온 기업 사례는 교안이 인용한 기사·자료의 내용이며, 시점이 지난 사례일 수 있습니다.<br>캐릭터: 박사 · 조수(하루) · 초파리 연구원 · 주판봇 — 캐릭터 이름·설정·그림의 저작권은 안상선(개인)에게 있으며 허락 없이 쓸 수 없습니다. 그림: 캐릭터 팩 (fruitfly-lab-expressions @ 5269662).</p>
</div></footer>

<div id="study" aria-live="polite"><span id="stRead">읽은 곳 0%</span><span id="stQuiz">퀴즈 0/0</span><button class="bt" type="button" id="stGloss">밑줄: 핵심</button></div>
'''.format(prevnext=m.PREVNEXT, src=''.join('<li>%s</li>' % s for s in m.SOURCES), ill=''.join('<li>%s</li>' % s for s in m.ILLUSTRATIVE),
           series=SERIES, n=n, ver=VERSION, date=DATE)
    scripts = ('<script>\n' + spr + '\n</script>\n'
               '<script type="application/json" id="kg-raw">' + jdump(kg) + '</script>\n'
               '<script type="application/ld+json" id="kg-ld">' + jdump(ld) + '</script>\n'
               '<script type="application/json" id="refs-csl">' + jdump(m.REFS) + '</script>\n'
               '<script type="application/json" id="page-meta">' + jdump(meta) + '</script>\n'
               '<script>\n' + ejs + '\n</script>\n'
               '<script>\n(function(){\n"use strict";\nvar GL=' + jdump(gl_js) + ';\nvar CORE=' + jdump(m.CORE) + ';\nvar QZ=' + jdump({k: [{kk: vv for kk, vv in it.items() if kk != 'assess'} for it in v] for k, v in m.QZ.items()}) + ';\n'
               + pjs + '\nLAB.boot({GL:GL,CORE:CORE,QZ:QZ,kgPath:' + jdump(m.KGPATH) + '});\n})();\n</script>\n</body>\n</html>\n')
    body = body.replace('</header>', '</header>\n' + plain_box(n, body), 1)
    body = add_easy(n, body)
    body = add_talk(n, body)
    out = head + NAVTPL.format(links=links) + '\n' + cover + body + '\n' + KG_SECTION.replace('{ph}', m.SEARCH_PH) + foot + scripts
    p = os.path.join(REPO, fname)
    open(p, 'w', encoding='utf-8').write(out)
    # 등록부 갱신분
    reg = [{'id': x['id'], 'type': x['type'], 'label': x['label'], 'domain': x['domain'], 'page': slug} for x in kg['nodes'] if x['type'] not in ('QuizItem', 'Simulation')]
    print('%s  %.1f KB  노드 %d 관계 %d 퀴즈 %d' % (fname, len(out.encode()) / 1024, len(kg['nodes']), len(kg['edges']), sum(len(v) for v in m.QZ.values())))
    return reg, m

if __name__ == '__main__':
    regs = {}
    for n in sys.argv[1:]:
        reg, m = page(n)
        for r in reg:
            if r['id'] in regs:
                regs[r['id']]['pages'] = sorted(set(regs[r['id']]['pages'] + [r['page']]))
            else:
                r['pages'] = [r.pop('page')]; regs[r['id']] = r
    os.makedirs(os.path.join(REPO, 'data'), exist_ok=True)
    rp = os.path.join(REPO, 'data', 'KG_00_registry.json')
    old = json.load(open(rp, encoding='utf-8')) if os.path.exists(rp) else {'series': SERIES, 'version': '0', 'concepts': []}
    cur = {c['id']: c for c in old['concepts']}
    for k, v in regs.items():
        if k in cur:
            cur[k]['pages'] = sorted(set(cur[k]['pages']) | set(v['pages']))
        else:
            cur[k] = v
    old['concepts'] = sorted(cur.values(), key=lambda c: c['id']); old['updated'] = DATE; old['version'] = str(len(old['concepts']))
    json.dump(old, open(rp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
