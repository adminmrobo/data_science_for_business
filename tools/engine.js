/* 연구실 공용 엔진 — 비즈니스를 위한 데이터 과학 연구실 (ai-lab-explainer v1.9 규격)
   페이지 스크립트가 LAB.* 도우미를 쓰고, 마지막에 LAB.boot(cfg)를 부른다. */
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);
  t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gauss(r){var u=0;while(!u)u=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*r())}
var LAB=(function(){
'use strict';
var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var CSS=getComputedStyle(document.documentElement);
function cv(n){return CSS.getPropertyValue(n).trim()}
var C={bg:cv('--bg'),panel:cv('--panel'),panel2:cv('--panel2'),rule:cv('--rule'),text:cv('--text'),muted:cv('--muted'),gfp:cv('--gfp'),stain:cv('--stain'),eye:cv('--eye'),amber:cv('--amber'),info:cv('--info'),seq:cv('--seq'),fly:cv('--c-fly'),robo:cv('--c-robo'),doc:cv('--c-doc'),asst:cv('--c-asst')};
var FONT='"IBM Plex Sans KR",system-ui,sans-serif';
function fitC(c,h){var d=window.devicePixelRatio||1, w=c.clientWidth||c.parentElement.clientWidth||600;
  if(c.width!==Math.round(w*d)||c.height!==Math.round(h*d)){c.width=Math.round(w*d);c.height=Math.round(h*d);c.style.height=h+'px';}
  var x=c.getContext('2d');x.setTransform(d,0,0,d,0,0);return w;}
function grid(x,W,H){x.fillStyle=C.bg;x.fillRect(0,0,W,H);x.strokeStyle='rgba(157,155,184,.06)';x.lineWidth=1;
  for(var i=0;i<W;i+=24){x.beginPath();x.moveTo(i+.5,0);x.lineTo(i+.5,H);x.stroke();}for(var j=0;j<H;j+=24){x.beginPath();x.moveTo(0,j+.5);x.lineTo(W,j+.5);x.stroke();}}
function stamp(ctx,W,txt){ctx.save();ctx.font='700 11px '+FONT;var tw=ctx.measureText(txt).width+16,x=W-tw-8,y=8;
  ctx.fillStyle='rgba(241,182,70,.14)';ctx.strokeStyle='rgba(241,182,70,.7)';ctx.beginPath();if(ctx.roundRect)ctx.roundRect(x,y,tw,20,10);else ctx.rect(x,y,tw,20);ctx.fill();ctx.stroke();
  ctx.fillStyle=C.amber;ctx.textAlign='left';ctx.textBaseline='alphabetic';ctx.fillText(txt,x+8,y+14);ctx.restore();}
function txt(x,s,px,py,col,size,align,weight){x.fillStyle=col||C.text;x.font=(weight||500)+' '+(size||12)+'px '+FONT;x.textAlign=align||'left';x.textBaseline='middle';x.fillText(s,px,py);}
function pct(v,d){return (v*100).toFixed(d||0)+'%'}
function fmt(v,d){return Number(v).toLocaleString('ko-KR',{minimumFractionDigits:d||0,maximumFractionDigits:d||0})}
function kpis(el,items){el.innerHTML=items.map(function(it){return '<div class="kpi '+it[0]+'"><b>'+it[1]+'</b><span>'+it[2]+'</span></div>';}).join('');}
function mean(a){var s=0;for(var i=0;i<a.length;i++)s+=a[i];return a.length?s/a.length:NaN;}
function sd(a){var m=mean(a),s=0;for(var i=0;i<a.length;i++)s+=(a[i]-m)*(a[i]-m);return Math.sqrt(s/Math.max(1,a.length-1));}
function quantile(a,q){var b=a.slice().sort(function(p,r){return p-r}),pos=(b.length-1)*q,lo=Math.floor(pos),hi=Math.ceil(pos);return b[lo]+(b[hi]-b[lo])*(pos-lo);}
function median(a){return quantile(a,.5)}
function corr(x,y){var mx=mean(x),my=mean(y),sxy=0,sx=0,sy=0;for(var i=0;i<x.length;i++){sxy+=(x[i]-mx)*(y[i]-my);sx+=(x[i]-mx)*(x[i]-mx);sy+=(y[i]-my)*(y[i]-my);}return sxy/Math.sqrt(sx*sy);}
function ranks(a){var idx=a.map(function(v,i){return i}).sort(function(p,q){return a[p]-a[q]}),r=new Array(a.length);
  for(var i=0;i<idx.length;){var j=i;while(j+1<idx.length&&a[idx[j+1]]===a[idx[i]])j++;var av=(i+j)/2+1;for(var k=i;k<=j;k++)r[idx[k]]=av;i=j+1;}return r;}
function spearman(x,y){return corr(ranks(x),ranks(y));}
/* 버튼 묶음: 하나만 눌리는 토글 */
function radio(el,items,cur,on){var box=typeof el==='string'?$(el):el;items.forEach(function(it){var b=document.createElement('button');b.className='bt';b.type='button';b.textContent=it[1];b.dataset.v=it[0];
  if(it[2])b.id=it[2];b.setAttribute('aria-pressed',String(it[0])===String(cur));b.addEventListener('click',function(){$$('.bt',box).forEach(function(z){z.setAttribute('aria-pressed',z===b)});on(it[0]);});box.appendChild(b);});}

/* ---------- 캐릭터 (캐릭터 팩 그림 → 기본 표정 → 픽셀 지도) ---------- */
var PAL={K:'#1d1a22',W:'#eceaf3',R:'#e04a3a',r:'#a8281c',U:'#3a6fd8',Y:'#f1c84a',L:'#5a4636',S:'rgba(0,0,0,.35)',B:'#4aa3ff',F:'#f2c9a0',G:'#9fb4d0',P:'#ff86b8',N:'#2b3a7a',V:'#b9a6e8',O:'#d4a54a',
  E:'#eadfc6',D:'#17352c',M:'#5befa5',A:'#8b5a2b',Q:'#d2603c',H:'#9c978c'};
var MAPS={
fly:['....K......K....','.....K....K.....','....UUUUUUUU....','...UUYUUUUYUU...','..RRRUUUUUURRR..','.RRrRRKKKKRRrRR.','.RRRRKKKKKKRRRR.','..RRKKKKKKKKRR..','WW..WKKKKKKW..WW','WWW.WWKKKKWW.WWW','.WWWWWKKKKWWWWW.','..L.WWKKKKWW.L..','.L...WKKKKW...L.','L.....KKKK.....L','.......KK.......','................'],
robo:['.......Q........','.......K........','..KKKKKKKKKKKK..','..KEEEEEEEEEEK..','..KEDDDDDDDDEK..','..KEDMDDDDMDEK..','..KEDDDDDDDDEK..','..KEDMDDDDMDEK..','..KEDDMMMMDDEK..','.HKEEEEEEEEEEKH.','HHAAAAAAAAAAAAHH','HHAEQEQEEQEQEAHH','..AAAAAAAAAAAA..','..AEQEQEEQEQEA..','..AAAAAAAAAAAA..','.KKKK......KKKK.'],
doc:['....KKKKKKK.....','...KKKWKKKKK....','..KKKWWKKKKKK...','..KFFFFFFFFFK...','..FGGFFFFGGFF...','..FGKFFFFGKFF...','..FFFFFFFFFFF...','...FFFRRRFFF....','....FFFFFFF.....','...WWWKKKWWW....','..WWWWKRKWWWW...','..WWWWKRKWWWW...','..WFWWKKKWWFW...','..WWWWKKKWWWW...','...LL.....LL....','...KK.....KK....'],
asst:['.PP..........PP.','.PP..PPPPPP..PP.','PPPPPPPPPPNPPPPP','.PPPPFFFFFFPPPP.','..PPFFFFFFFFPP..','..PFFBFFFFBFFP..','..PFFBFFFFBFFP..','..PFFFFFFFFFFP..','...FFFFRRFFFF...','....FFFFFFFF....','...WWVVVVVVWW...','..WWWVVVVVVWWW..','..WWWVVVVVVWWW..','..WFWVVVVVVWFW..','...NN......NN...','...NN......NN...']};
var DEFAULT={doc:'doc_front',asst:'asst_smile',fly:'fly_clip',robo:'robo_smile'};
function packSrc(key){var S=window.SPRITE||{},AL=window.SPRITE_ALIAS||{};return S[key]||S[AL[key]]||null;}
var PIX={};
function pixelSrc(who){if(PIX[who])return PIX[who];var c=document.createElement('canvas');c.width=64;c.height=64;var x=c.getContext('2d');x.imageSmoothingEnabled=false;
  MAPS[who].forEach(function(r,y){r.split('').forEach(function(ch,i){if(ch==='.')return;x.fillStyle=PAL[ch];x.fillRect(i*4,y*4,4,4);});});PIX[who]=c.toDataURL();return PIX[who];}
function src(who,mood){return packSrc(who+'_'+mood)||packSrc(DEFAULT[who])||pixelSrc(who);}
var Cast={fill:function(){$$('img[data-who]').forEach(function(i){i.src=src(i.dataset.who,i.dataset.mood||'');});},
  set:function(img,who,mood){if(!img)return;img.dataset.mood=mood;img.style.transition=reduce?'none':'opacity .2s';img.style.opacity=0;
    setTimeout(function(){img.src=src(who,mood);img.style.opacity=1;},reduce?0:200);}};
/* 받은 장면 그림(SPRITE의 표지·장면 키)이 있으면 그 자리만 켠다 */
function scenes(){var S=window.SPRITE||{};
  $$('[data-scene]').forEach(function(el){var k=el.dataset.scene;if(!S[k])return;var img=el.tagName==='IMG'?el:$('img',el);img.src=S[k];el.hidden=false;});
  $$('.cover[data-img]').forEach(function(el){var k=el.dataset.img;if(!S[k])return;var im=document.createElement('img');im.className='cv';im.alt=el.dataset.alt||'';im.width=1600;im.height=900;im.src=S[k];
    var fb=$('.fallback',el);if(fb)fb.remove();el.insertBefore(im,el.firstChild);});}

/* ---------- 루프: 보이는 캔버스만 ---------- */
var mods=[],vis=new Set(),io=('IntersectionObserver' in window)?new IntersectionObserver(function(es){es.forEach(function(e){e.isIntersecting?vis.add(e.target):vis.delete(e.target);});},{rootMargin:'100px'}):null;
function addMod(el,fn){mods.push({el:el,fn:fn});if(io)io.observe(el);else vis.add(el);}
var last=0;function loop(ts){var dt=last?Math.min(.05,(ts-last)/1000):.016;last=ts;mods.forEach(function(m){if(vis.has(m.el))m.fn(dt);});requestAnimationFrame(loop);}

/* ---------- 대결 (SKILL 6장, 부록 B-5) ---------- */
function Duel(o){var root=$(o.el),shown=false,guess=null;
  var flyImg=$('.side.fly img',root),roboImg=$('.side.robo img',root),asstImg=$('.say.asst img',root),docImg=$('.say.verdict img',root),btn=$('.reveal',root);
  $$('[data-guess]',root).forEach(function(b){b.addEventListener('click',function(){guess=b.dataset.guess;$$('[data-guess]',root).forEach(function(z){z.setAttribute('aria-pressed',z===b)});});});
  function bar(name,v,col,f){var mx=o.max||1;return '<div class="barrow"><span>'+name+'</span><div class="track"><div class="fill" style="width:0;background:'+col+'" data-w="'+Math.max(2,Math.min(100,v/mx*100))+'"></div></div><b class="num">'+f(v)+'</b></div>';}
  btn.addEventListener('click',function(){if(shown){reset();return;}
    var r=o.run(),res,f=o.fmt||function(v){return v.toFixed(2)};
    if(r.foul)res='X';else if(r.cond)res='C';else if(Math.abs(r.fly-r.robo)<=(o.drawMargin||0))res='D';else res=((o.higherIsBetter?r.fly-r.robo:r.robo-r.fly)>0)?'F':'R';
    var big=Math.abs(r.fly-r.robo)>=(o.bigGap||0.10);
    var M={F:['arms','sigh','judge','spark'],R:[big?'cry':'coffee','happy','judge','spark'],D:['coffee','meh','think','smile'],X:['arms','blush','judge','shock'],C:['coffee','calc','think','report']}[res];
    Cast.set(flyImg,'fly',M[0]);Cast.set(roboImg,'robo',M[1]);Cast.set(docImg,'doc',M[2]);Cast.set(asstImg,'asst',M[3]);
    var html='';
    if(res==='C'){[r.condA,r.condB].forEach(function(c){html+='<p class="muted" style="font-size:14px;margin-top:4px">'+c.label+'</p>'+bar('초파리 연구원',c.fly,C.fly,f)+bar('주판봇',c.robo,C.robo,f);});}
    else html=bar('초파리 연구원',r.fly,C.fly,f)+bar('주판봇',r.robo,C.robo,f);
    if(o.metric)html='<p class="muted" style="font-size:14px">'+o.metric+'</p>'+html;
    $('.bars',root).innerHTML=html;
    requestAnimationFrame(function(){$$('.fill',root).forEach(function(el){el.style.width=el.dataset.w+'%';});});
    $('.say.asst p',root).textContent=o.report(r,res);
    $('.say.verdict p',root).textContent=o.verdict(r,res);
    var gfb=$('.guessfb',root);if(gfb)gfb.textContent=guess?((guess===res||(res==='C'))?'예상한 쪽: '+(guess==='F'?'초파리':'주판봇')+(res==='C'?' — 이 판은 조건에 따라 갈립니다.':' — 맞혔습니다.'):'예상한 쪽: '+(guess==='F'?'초파리':'주판봇')+' — 결과는 반대였습니다.'):'';
    if(o.after)o.after(r,res);
    root.classList.add('open');shown=true;btn.textContent='다시 닫기';});
  function reset(){Cast.set(flyImg,'fly','point');Cast.set(roboImg,'robo','coin');Cast.set(docImg,'doc','judge');Cast.set(asstImg,'asst','firm');root.classList.remove('open');shown=false;btn.textContent='결과 보기';}
}

/* ---------- 용어 ---------- */
var GL={},CORE_T=[],glossMode='core';
function applyGloss(){$$('span.jt').forEach(function(s){s.replaceWith(document.createTextNode(s.textContent));});
  $$('section.level .wrap, header.hero .wrap').forEach(function(w){w.normalize();});
  if(glossMode==='off')return;var terms=(glossMode==='core'?CORE_T:Object.keys(GL)).slice().sort(function(a,b){return b.length-a.length});
  $$('section.level').forEach(function(sec){if(sec.id==='kg'||sec.id==='export')return;var used={};
    var walker=document.createTreeWalker(sec,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentElement;if(!p||p.closest('button,h1,h2,h3,nav,canvas,svg,.kpis,.eq,.jt,label,summary,script,.chip,.lvtag,th,.dt,.tag,.name'))return NodeFilter.FILTER_REJECT;return NodeFilter.FILTER_ACCEPT;}});
    var nodes=[],n;while((n=walker.nextNode()))nodes.push(n);
    nodes.forEach(function(tn){for(var t=0;t<terms.length;t++){var term=terms[t];if(used[term])continue;var i=tn.nodeValue.indexOf(term);if(i<0)continue;
      used[term]=1;var after=tn.splitText(i);after.splitText(term.length);var sp=document.createElement('span');sp.className='jt';sp.tabIndex=0;sp.dataset.t=term;sp.textContent=term;after.replaceWith(sp);tn=sp.nextSibling;if(!tn||tn.nodeType!==3)break;t=-1;}});});}
function initGloss(){var tip=$('#tip');
  function showTip(el){var d=GL[el.dataset.t];if(!d)return;tip.innerHTML='<b>'+d[0]+'</b><small>'+d[1]+'</small><div>'+d[2]+'</div>';tip.style.display='block';
    var r=el.getBoundingClientRect(),tw=Math.min(300,window.innerWidth-24);tip.style.maxWidth=tw+'px';var left=Math.max(12,Math.min(r.left,window.innerWidth-tw-12));tip.style.left=left+'px';
    var top=r.bottom+8;if(top+tip.offsetHeight>window.innerHeight-10)top=r.top-tip.offsetHeight-8;tip.style.top=top+'px';}
  function hideTip(){tip.style.display='none';}
  document.addEventListener('pointerover',function(e){var t=e.target.closest&&e.target.closest('.jt');if(t)showTip(t);else if(!e.target.closest('#tip'))hideTip();});
  document.addEventListener('focusin',function(e){if(e.target.classList&&e.target.classList.contains('jt'))showTip(e.target);});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')hideTip();});
  window.addEventListener('scroll',hideTip,{passive:true});
  applyGloss();
  $('#stGloss').addEventListener('click',function(){glossMode={core:'all',all:'off',off:'core'}[glossMode];this.textContent='밑줄: '+{core:'핵심',all:'전체',off:'끄기'}[glossMode];applyGloss();});}

/* ---------- 퀴즈 ---------- */
function initQuiz(QZ){var qDone={},qN=0;Object.keys(QZ).forEach(function(k){qN+=QZ[k].length;});
  function upd(){$('#stQuiz').textContent='퀴즈 '+Object.keys(qDone).length+'/'+qN;}
  $$('.quiz[data-quiz]').forEach(function(box){(QZ[box.dataset.quiz]||[]).forEach(function(it){var d=document.createElement('div');d.className='qi';
    d.innerHTML='<span class="qh">확인 퀴즈'+(it.calc?' · 계산':'')+'</span><p>'+it.q+'</p><div class="opts"></div><p class="fb" aria-live="polite"></p>';
    it.o.forEach(function(o,oi){var b=document.createElement('button');b.className='bt';b.type='button';b.id=it.id+'_'+oi;b.textContent=o;b.addEventListener('click',function(){var fb=$('.fb',d);
      if(oi===it.a){fb.className='fb ok';fb.textContent='정답. '+it.why;qDone[it.id]=1;upd();}else{fb.className='fb no';fb.textContent='다시 보기: '+it.hint;}});$('.opts',d).appendChild(b);});box.appendChild(d);});});
  upd();}

/* ---------- 진행률 ---------- */
function initProgress(){function onScroll(){var h=document.documentElement,max=h.scrollHeight-h.clientHeight,p=max>0?h.scrollTop/max:0;$('#prog').style.width=(p*100)+'%';$('#stRead').textContent='읽은 곳 '+Math.round(p*100)+'%';}
  window.addEventListener('scroll',onScroll,{passive:true});onScroll();}

/* ---------- 지식 색인 (O1) ---------- */
var KG,REF,META,byId={},tyOn={},renderList;
var TYKO={Concept:'개념',Method:'방법',Task:'문제',Metric:'지표',Dataset:'데이터',Claim:'주장',Work:'문헌',Term:'용어',Analogy:'비유',Question:'질문',Limitation:'한계',Simulation:'시뮬레이션',QuizItem:'퀴즈',Framework:'분석 틀',Standard:'기준·법령',Assumption:'가정',Theory:'이론',Indicator:'지표(공식)',Distribution:'분포'};
var PKO={broader:'더 넓은 개념',partOf:'부분',prerequisiteOf:'먼저 알아야 함',hasLimitation:'한계',addressedBy:'해결',contrastsWith:'대비',analogyOf:'비유',solves:'푼다',evaluatedBy:'지표',evaluatedOn:'데이터',supports:'근거',assertedIn:'출처',demonstratedBy:'시뮬레이션',assesses:'퀴즈가 확인',explainedIn:'설명',raises:'질문을 낳음',relatedTo:'관련',governedBy:'기준·법령',assumes:'가정',measuredBy:'잰다'};
/* 지식 색인 표시용: 번역판(<html lang>)이면 그 언어 라벨을 쓴다 */
var UIL=(document.documentElement.lang||'ko').slice(0,2);
function LB(n){return (n.label&&n.label[UIL])||n.label.ko;}
function DF(n){return (n.definition&&(n.definition[UIL]||n.definition.ko))||'';}
function initKG(path){KG=JSON.parse($('#kg-raw').textContent);REF=JSON.parse($('#refs-csl').textContent);META=JSON.parse($('#page-meta').textContent);
  KG.nodes.forEach(function(n){byId[n.id]=n;});
  var types=[];KG.nodes.forEach(function(n){if(n.type!=='QuizItem'&&n.type!=='Simulation'&&types.indexOf(n.type)<0)types.push(n.type);});
  types.forEach(function(t){tyOn[t]=true;});
  var tg=$('#kgTypes');types.forEach(function(t){var b=document.createElement('button');b.className='bt';b.type='button';b.id='ty_'+t;b.textContent=TYKO[t]||t;b.setAttribute('aria-pressed','true');
    b.addEventListener('click',function(){tyOn[t]=!tyOn[t];b.setAttribute('aria-pressed',tyOn[t]);renderList();});tg.appendChild(b);});
  renderList=function(){var q=$('#kgq').value.trim().toLowerCase();
    var list=KG.nodes.filter(function(n){if(!tyOn[n.type])return false;if(!q)return true;
      var hay=[LB(n),n.label.en,(n.altLabel&&n.altLabel.ko||[]).join(' '),n.definition?DF(n):''].join(' ').toLowerCase();return hay.indexOf(q)>=0;});
    $('#kgList').innerHTML=list.map(function(n){var out=KG.edges.filter(function(e){return e.s===n.id||e.o===n.id}).map(function(e){var other=e.s===n.id?e.o:e.s;return (PKO[e.p.slice(4)]||e.p)+': '+LB(byId[other]);});
      return '<details id="kgi_'+n.id.replace(/[^a-z0-9]/gi,'_')+'"><summary><b>'+LB(n)+'</b><span class="ty">'+(TYKO[n.type]||n.type)+'</span><span class="muted" style="font-size:13px">'+n.label.en+'</span></summary>'+
        (n.definition?'<p>'+DF(n)+'</p>':'')+'<p class="muted">'+out.slice(0,6).join(' · ')+'</p><p><a href="'+n.anchor+'">설명 보러 가기 →</a>'+(n.evidence?' <span class="muted">근거 '+n.evidence.length+'</span>':'')+'</p></details>';}).join('')||'<p class="muted">찾는 항목이 없습니다.</p>';};
  $('#kgq').addEventListener('input',renderList);renderList();
  var cnt={};KG.nodes.forEach(function(n){cnt[n.type]=(cnt[n.type]||0)+1;});
  $('#kgStat').textContent='노드 '+KG.nodes.length+'개 · 관계 '+KG.edges.length+'개 · '+Object.keys(cnt).map(function(t){return (TYKO[t]||t)+' '+cnt[t]}).join(', ')+' · 외부 매핑 확인 0건';
  $('#kgPath').innerHTML=path.map(function(id,i){var n=byId['lab:'+id];return (i?'<i>→</i>':'')+'<span class="'+(n.type==='Limitation'?'lim':'')+'">'+LB(n)+'</span>';}).join('');
  $('#kgQ').innerHTML=KG.nodes.filter(function(n){return n.type==='Question'}).map(function(n){return '<li><a href="'+n.anchor+'">'+LB(n)+'</a></li>';}).join('');
  (function(){var c=$('#kgG');var nodes=KG.nodes.filter(function(n){return n.type!=='QuizItem'&&n.type!=='Simulation'});if(nodes.length>80)nodes=nodes.slice(0,80);var idx={};nodes.forEach(function(n,i){idx[n.id]=i;});
    var edges=KG.edges.filter(function(e){return idx[e.s]!==undefined&&idx[e.o]!==undefined});
    var r=rng(5),P=nodes.map(function(){return {x:r(),y:r(),vx:0,vy:0}});
    for(var it=0;it<200;it++){for(var i=0;i<P.length;i++)for(var j=i+1;j<P.length;j++){var dx=P[i].x-P[j].x,dy=P[i].y-P[j].y,d2=dx*dx+dy*dy+1e-4,f=.0009/d2;P[i].vx+=dx*f;P[i].vy+=dy*f;P[j].vx-=dx*f;P[j].vy-=dy*f;}
      edges.forEach(function(e){var a=P[idx[e.s]],b=P[idx[e.o]],dx=b.x-a.x,dy=b.y-a.y,d=Math.sqrt(dx*dx+dy*dy)+1e-4,f=(d-.12)*.04;a.vx+=dx/d*f;a.vy+=dy/d*f;b.vx-=dx/d*f;b.vy-=dy/d*f;});
      P.forEach(function(p){p.vx+=(.5-p.x)*.004;p.vy+=(.5-p.y)*.004;p.x+=p.vx;p.y+=p.vy;p.vx*=.6;p.vy*=.6;});}
    var xs=P.map(function(p){return p.x}),ys=P.map(function(p){return p.y}),mx=Math.min.apply(0,xs),Mx=Math.max.apply(0,xs),my=Math.min.apply(0,ys),My=Math.max.apply(0,ys);
    function col(t){return {Concept:C.seq,Method:C.seq,Framework:C.seq,Limitation:C.eye,Question:C.amber,Claim:C.amber,Metric:C.gfp,Dataset:C.gfp,Task:C.gfp,Standard:C.stain}[t]||C.muted;}
    var scr=[];
    function draw(){var W=fitC(c,420),x=c.getContext('2d');grid(x,W,420);scr=P.map(function(p){return {x:30+(p.x-mx)/(Mx-mx||1)*(W-160),y:30+(p.y-my)/(My-my||1)*360};});
      edges.forEach(function(e){var a=scr[idx[e.s]],b=scr[idx[e.o]];x.strokeStyle=e.p==='lab:hasLimitation'||e.p==='lab:addressedBy'?'rgba(240,96,77,.45)':e.p==='lab:prerequisiteOf'?'rgba(94,227,156,.5)':'rgba(157,155,184,.22)';x.lineWidth=1.2;x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b.x,b.y);x.stroke();});
      x.font='500 11px '+FONT;x.textBaseline='middle';
      nodes.forEach(function(n,i){var s=scr[i];x.fillStyle=col(n.type);x.beginPath();x.arc(s.x,s.y,n.type==='Method'?6:4.5,0,7);x.fill();x.fillStyle=C.text;x.textAlign='left';x.fillText(LB(n).length>14?LB(n).slice(0,13)+'…':LB(n),s.x+8,s.y);});
      stamp(x,W,'배치는 의미 축이 아님');}
    c.addEventListener('click',function(e){var rc=c.getBoundingClientRect(),px=e.clientX-rc.left,py=e.clientY-rc.top,best=-1,bd=400;
      scr.forEach(function(s,i){var d=(s.x-px)*(s.x-px)+(s.y-py)*(s.y-py);if(d<bd){bd=d;best=i;}});
      if(best>=0){var n=nodes[best];tyOn[n.type]=true;var tb=$('#ty_'+n.type);if(tb)tb.setAttribute('aria-pressed','true');$('#kgq').value=LB(n);renderList();var d=$('#kgList details');if(d){d.open=true;d.scrollIntoView({block:'nearest',behavior:reduce?'auto':'smooth'});}}});
    addMod(c,draw);})();
  $('#qJson').addEventListener('click',function(){var o=$('#kgOut');o.hidden=false;o.textContent=JSON.stringify(KG,null,2);});
  $('#qMer').addEventListener('click',function(){var o=$('#kgOut');o.hidden=false;o.textContent=toMermaid(KG);});
}

/* ---------- 내보내기 변환 (O2, 부록 O-B) ---------- */
function esc(s){return String(s==null?'':s).replace(/"/g,'""');}
function filterScope(kg,scope){if(scope==='all')return kg;var keep;
  if(scope==='concepts')keep=function(n){return ['Concept','Method','Term','Task','Metric','Framework'].indexOf(n.type)>=0};
  else if(scope==='claims')keep=function(n){return n.type==='Claim'||n.type==='Work'};
  else keep=function(n){return ['Concept','Method','Limitation','Framework'].indexOf(n.type)>=0};
  var nodes=kg.nodes.filter(keep),ids={};nodes.forEach(function(n){ids[n.id]=1});
  var edges=kg.edges.filter(function(e){if(!ids[e.s]||!ids[e.o])return false;if(scope==='path')return ['lab:prerequisiteOf','lab:hasLimitation','lab:addressedBy'].indexOf(e.p)>=0;return true;});
  return {version:kg.version,page:kg.page,scope:scope,nodes:nodes,edges:edges};}
function toNodesCsv(g){return 'id,type,label_ko,label_en,status,level,family,page,anchor\n'+g.nodes.map(function(n){return [n.id,n.type,n.label.ko,n.label.en,n.status,n.level,n.family,n.page,n.anchor].map(function(v){return '"'+esc(v)+'"'}).join(',');}).join('\n');}
function toEdgesCsv(g){return 'source,predicate,target,anchor,confidence\n'+g.edges.map(function(e){return [e.s,e.p,e.o,e.anchor,e.confidence].map(function(v){return '"'+esc(v)+'"'}).join(',');}).join('\n');}
function ttlStr(s){return '"'+String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"')+'"';}
function toTurtle(g){var L=['@prefix lab: <urn:lab:> .','@prefix skos: <http://www.w3.org/2004/02/skos/core#> .','@prefix schema: <https://schema.org/> .',''];
  g.nodes.forEach(function(n){var id='<'+n.id.replace(/^lab:/,'urn:lab:')+'>';var t=['lab:'+n.type];if(['Concept','Method','Task','Term','Framework'].indexOf(n.type)>=0)t.push('skos:Concept');
    L.push(id+' a '+t.join(', ')+' ;');L.push('  skos:prefLabel '+ttlStr(n.label.ko)+'@ko, '+ttlStr(n.label.en)+'@en'+(n.definition?' ;':' .'));if(n.definition)L.push('  skos:definition '+ttlStr(n.definition.ko)+'@ko .');});
  L.push('');g.edges.forEach(function(e){L.push('<'+e.s.replace(/^lab:/,'urn:lab:')+'> '+e.p+' <'+e.o.replace(/^lab:/,'urn:lab:')+'> .');});return L.join('\n');}
function toJsonLd(g){var ld=JSON.parse($('#kg-ld').textContent);if(g.scope&&g.scope!=='all'){var ids={};g.nodes.forEach(function(n){ids[n.id]=1});ld['@graph']=ld['@graph'].filter(function(o){return ids[o['@id']]});}return ld;}
function toMermaid(g){var nodes=g.nodes.filter(function(n){return n.type!=='QuizItem'&&n.type!=='Simulation'}).slice(0,40),ids={};nodes.forEach(function(n,i){ids[n.id]='n'+i});
  var L=['graph LR'];nodes.forEach(function(n){L.push('  '+ids[n.id]+'["'+n.label.ko.replace(/"/g,"'")+'"]');});
  g.edges.forEach(function(e){if(ids[e.s]&&ids[e.o])L.push('  '+ids[e.s]+' -->|'+(PKO[e.p.slice(4)]||e.p)+'| '+ids[e.o]);});return L.join('\n');}
var BIBT={'article-journal':'article','paper-conference':'inproceedings','book':'book','chapter':'incollection','webpage':'misc','dataset':'misc','report':'techreport','thesis':'phdthesis','software':'misc'};
var RIST={'article-journal':'JOUR','paper-conference':'CPAPER','book':'BOOK','chapter':'CHAP','webpage':'ELEC','dataset':'DATA','report':'RPRT','thesis':'THES','software':'COMP'};
function names(a){return (a||[]).map(function(p){return p.literal||(p.family+(p.given?', '+p.given:''));});}
function yr(r){return r.issued&&r.issued['date-parts']&&r.issued['date-parts'][0][0];}
function toBib(r){var f=[],add=function(k,v){if(v!==undefined&&v!==null&&v!=='')f.push('  '+k+' = {'+v+'}');};
  add('title',r.title);add('author',names(r.author).map(function(n){return n==='et al.'?'others':n;}).join(' and '));add('year',yr(r));
  add(r.type==='article-journal'?'journal':'booktitle',r.type==='webpage'||r.type==='book'?'':r['container-title']);add('publisher',r.publisher);add('volume',r.volume);add('number',r.issue);add('pages',r.page);add('doi',r.DOI);add('url',r.URL);
  if(r.lab&&r.lab.note)add('note',r.lab.note);return '@'+(BIBT[r.type]||'misc')+'{'+r.id+',\n'+f.join(',\n')+'\n}';}
function toRis(r){var L=['TY  - '+(RIST[r.type]||'GEN')],add=function(t,v){if(v)L.push(t+'  - '+v);};
  add('TI',r.title);names(r.author).forEach(function(n){add('AU',n);});add('PY',yr(r));add('T2',r['container-title']);add('PB',r.publisher);add('VL',r.volume);add('IS',r.issue);add('DO',r.DOI);add('UR',r.URL);
  if(r.lab&&r.lab.note)add('N1',r.lab.note);L.push('ER  - ');return L.join('\r\n');}
function toProvCsv(g,refs){var rows=['item,kind,work,loc,factCard,confidence,verified,pageAnchor'];var ids={};g.nodes.forEach(function(n){ids[n.id]=1});
  refs.forEach(function(r){(r.lab.supports||[]).forEach(function(s){if(!ids[s])return;var n=byId[s];var loc=(r.lab.locs||[]).filter(function(l){return l.claim===s}).map(function(l){return l.loc}).join(';');
    rows.push(['"'+s+'"','node','"'+r.id+'"','"'+loc+'"','"'+((n.evidence||[]).join(';'))+'"',n.confidence,loc?'true':'false','"'+n.anchor+'"'].join(','));});});
  g.edges.filter(function(e){return e.p==='lab:assertedIn'}).forEach(function(e){var w=REF.filter(function(r){return r.lab.work===e.o})[0];rows.push(['"'+e.s+' assertedIn '+e.o+'"','edge','"'+(w?w.id:'')+'"','""','""',e.confidence,'false','"'+e.anchor+'"'].join(','));});return rows.join('\n');}
function todoItems(){var t=[];REF.forEach(function(r){var v=r.lab.verified;Object.keys(v).forEach(function(k){if(!v[k])t.push(r.id+': '+{title:'원제',authors:'저자',year:'연도',venue:'게재지·출판사',doi:'DOI',pages:'쪽수'}[k]+' 미확인');});});
  t.push('외부 온톨로지 대응(Wikidata 등) '+KG.nodes.filter(function(n){return n.match&&n.match.length}).length+'건 미확인');(META.todo||[]).forEach(function(x){t.push(x)});return t;}
function readme(meta,g){var todo=todoItems();return ['꾸러미: '+meta.title,'버전 '+meta.version+' · '+meta.date+' · 범위 '+(g.scope||'all'),'','권장 인용:',meta.suggestedCitation,'',
  '파일: manifest.json, page_meta.json, kg.json, kg.jsonld, kg.ttl, nodes.csv, edges.csv, references.csl.json, references.bib, references.ris, provenance.csv, README.txt','',
  '확인 필요:'].concat(todo.map(function(t){return '- '+t})).concat(['','시뮬레이션 수치는 모두 설명용 장난감 데이터에서 계산한 값입니다.']).join('\n');}
function buildPackage(scope){var g=filterScope(KG,scope);var BOM='﻿';
  var files=[{name:'page_meta.json',text:JSON.stringify(META,null,2)},{name:'kg.json',text:JSON.stringify(g,null,2)},{name:'kg.jsonld',text:JSON.stringify(toJsonLd(g),null,2)},{name:'kg.ttl',text:toTurtle(g)},
    {name:'nodes.csv',text:BOM+toNodesCsv(g)},{name:'edges.csv',text:BOM+toEdgesCsv(g)},{name:'references.csl.json',text:JSON.stringify(REF,null,2)},{name:'references.bib',text:REF.map(toBib).join('\n\n')},
    {name:'references.ris',text:REF.map(toRis).join('\r\n')},{name:'provenance.csv',text:BOM+toProvCsv(g,REF)},{name:'README.txt',text:readme(META,g)}];
  files.unshift({name:'manifest.json',text:JSON.stringify({package:'lab-kg',version:META.version,page:META.number,created:META.date,scope:scope,counts:{nodes:g.nodes.length,edges:g.edges.length,refs:REF.length},files:files.map(function(f){return f.name})},null,2)});
  return files;}
var CRC=(function(){var t=[],c;for(var n=0;n<256;n++){c=n;for(var k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0;}return function(u8){var x=0xFFFFFFFF;for(var i=0;i<u8.length;i++)x=t[(x^u8[i])&255]^(x>>>8);return (x^0xFFFFFFFF)>>>0;};})();
function makeZip(files){var enc=new TextEncoder(),parts=[],central=[],off=0;function u16(v){return [v&255,(v>>8)&255]}function u32(v){return [v&255,(v>>8)&255,(v>>16)&255,(v>>>24)&255]}
  files.forEach(function(f){var name=enc.encode(f.name),data=enc.encode(f.text),crc=CRC(data);
    var head=[].concat(u32(0x04034b50),u16(20),u16(0x0800),u16(0),u16(0),u16(0),u32(crc),u32(data.length),u32(data.length),u16(name.length),u16(0));
    parts.push(new Uint8Array(head),name,data);
    central.push(new Uint8Array([].concat(u32(0x02014b50),u16(20),u16(20),u16(0x0800),u16(0),u16(0),u16(0),u32(crc),u32(data.length),u32(data.length),u16(name.length),u16(0),u16(0),u16(0),u16(0),u32(0),u32(off))),name);
    off+=head.length+name.length+data.length;});
  var cdStart=off,cdLen=0;central.forEach(function(c){parts.push(c);cdLen+=c.length;});
  parts.push(new Uint8Array([].concat(u32(0x06054b50),u16(0),u16(0),u16(files.length),u16(files.length),u32(cdLen),u32(cdStart),u16(0))));
  return new Blob(parts,{type:'application/zip'});}
function download(blob,name){try{var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove();},500);}catch(e){}
  $('#dlMsg').textContent=name+' 내려받기를 시도했습니다. 받아지지 않았다면 위 텍스트를 복사해 주세요.';}
function copyText(txt,pre,msgEl){function fb(){var r=document.createRange();r.selectNodeContents(pre);var s=window.getSelection();s.removeAllRanges();s.addRange(r);if(msgEl)msgEl.textContent='복사가 막혀 있어 텍스트를 선택해 두었습니다. 직접 복사해 주세요.';}
  try{navigator.clipboard.writeText(txt).then(function(){if(msgEl)msgEl.textContent='복사했습니다.';},fb);}catch(e){fb();}}
function initExport(){var claims=KG.nodes.filter(function(n){return n.type==='Claim'}),withSrc=claims.filter(function(n){return KG.edges.some(function(e){return e.s===n.id&&e.p==='lab:assertedIn'})});
  var vref=REF.filter(function(r){var v=r.lab.verified;return v.title&&v.authors&&v.year;}).length;
  kpis($('#exK'),[['i',KG.nodes.length,'노드'],['i',KG.edges.length,'관계'],['a',REF.length,'문헌'],['g',pct(vref/REF.length),'핵심 서지 확인'],['g',pct(withSrc.length/Math.max(1,claims.length)),'출처 있는 주장'],['r',todoItems().length,'확인 필요']]);
  $('#exSay').textContent='출처 없는 주장은 꾸러미에 넣지 않았어요. 확인할 항목 '+todoItems().length+'개는 아래에 있어요.';
  var key='ahn2026dsb'+META.number;
  var citeF={'일반 문장':META.suggestedCitation,'BibTeX':'@misc{'+key+',\n  title = {'+META.title+'},\n  author = {안상선},\n  year = {2026},\n  note = {'+META.series+' '+META.number+', v'+META.version+'}'+(META.url?',\n  url = {'+META.url+'}':'')+'\n}','RIS':'TY  - ELEC\r\nTI  - '+META.title+'\r\nAU  - 안상선\r\nPY  - 2026\r\nN1  - '+META.series+' '+META.number+', v'+META.version+(META.url?'\r\nUR  - '+META.url:'')+'\r\nER  - '};
  var cf=$('#citeFmt'),curC='일반 문장';Object.keys(citeF).forEach(function(k,i){var b=document.createElement('button');b.className='bt';b.type='button';b.id='cite_'+i;b.textContent=k;b.setAttribute('aria-pressed',k===curC);
    b.addEventListener('click',function(){curC=k;$$('#citeFmt .bt').forEach(function(z){z.setAttribute('aria-pressed',z===b)});$('#citeOut').textContent=citeF[k];});cf.appendChild(b);});
  $('#citeOut').textContent=citeF[curC];$('#citeCopy').addEventListener('click',function(){copyText(citeF[curC],$('#citeOut'),$('#citeMsg'));});
  var ROLE={primary:'주 자료',background:'배경',data:'수치',figure:'그림',software:'소프트웨어'};
  $('#refList').innerHTML=REF.map(function(r){var v=r.lab.verified,ok=v.title&&v.authors&&v.year&&v.venue;var au=names(r.author).join(', ');
    var sup=r.lab.supports.map(function(s){return byId[s]?'<a href="#kg" data-kg="'+s+'">'+LB(byId[s])+'</a>':'';}).join(', ');
    return '<li>'+(au?au+(yr(r)?' ('+yr(r)+')':'')+'. ':'')+'<i>'+r.title+'</i>'+(r['container-title']?'. '+r['container-title']:'')+(r.publisher?'. '+r.publisher:'')+(r.URL?'. <a href="'+r.URL+'" target="_blank" rel="noopener">'+r.URL+'</a>':'')+
      ' <span class="lvtag">'+ROLE[r.lab.role]+'</span><span class="badge '+(ok?'ok':'no')+'">'+(ok?'확인됨':'확인 필요')+'</span><details style="margin-top:4px"><summary class="muted" style="font-size:13px">뒷받침하는 개념 '+r.lab.supports.length+'개</summary><p style="font-size:14px">'+sup+'</p><p class="muted" style="font-size:13px">'+r.lab.checkedBy+(r.lab.note?' · '+r.lab.note:'')+'</p></details></li>';}).join('');
  $$('#refList a[data-kg]').forEach(function(a){a.addEventListener('click',function(){var n=byId[a.dataset.kg];$('#kgq').value=LB(n);tyOn[n.type]=true;renderList();var d=$('#kgList details');if(d)d.open=true;});});
  var SC={all:'전체',concepts:'개념·방법만',claims:'주장 + 출처만',path:'선수 관계만'},scope='all',fileI=0,files=buildPackage(scope);
  var sg=$('#scopeG');Object.keys(SC).forEach(function(k){var b=document.createElement('button');b.className='bt';b.type='button';b.id='sc_'+k;b.textContent=SC[k];b.setAttribute('aria-pressed',k===scope);
    b.addEventListener('click',function(){scope=k;$$('#scopeG .bt').forEach(function(z){z.setAttribute('aria-pressed',z===b)});files=buildPackage(scope);showFile();});sg.appendChild(b);});
  var fg=$('#fileG');files.forEach(function(f,i){var b=document.createElement('button');b.className='bt';b.type='button';b.id='file_'+i;b.textContent=f.name;b.setAttribute('aria-pressed',i===0);
    b.addEventListener('click',function(){fileI=i;$$('#fileG .bt').forEach(function(z){z.setAttribute('aria-pressed',z===b)});showFile();});fg.appendChild(b);});
  function showFile(){$('#fileOut').textContent=files[fileI].text.replace(/^﻿/,'');}
  showFile();
  $('#fileCopy').addEventListener('click',function(){copyText(files[fileI].text.replace(/^﻿/,''),$('#fileOut'),$('#dlMsg'));});
  $('#fileDl').addEventListener('click',function(){download(new Blob([files[fileI].text],{type:'text/plain;charset=utf-8'}),files[fileI].name);});
  $('#zipDl').addEventListener('click',function(){download(makeZip(files),'kg_dsb_'+META.number+'_'+scope+'.zip');});
  $('#todoList').innerHTML=todoItems().map(function(t){return '<li>'+t+'</li>';}).join('');
  $('#verLine').textContent='꾸러미 v'+META.version+' · '+META.date+' · 등록부: data/KG_00_registry.json (이 시리즈 공용)';}

/* ---------- 히어로 무대: 밤의 연구실 배경 + 페이지 소품 ---------- */
function heroStage(c,prop){function draw(t){var W=fitC(c,c.parentElement.clientHeight||300),H=c.parentElement.clientHeight||300,x=c.getContext('2d');
    var g=x.createLinearGradient(0,0,0,H);g.addColorStop(0,'#1b1533');g.addColorStop(.72,'#191a2b');g.addColorStop(1,'#25283a');x.fillStyle=g;x.fillRect(0,0,W,H);
    x.fillStyle='rgba(154,184,255,.07)';for(var i=0;i<W;i+=16)for(var j=0;j<H*.7;j+=14)if(((i*7+j*13)%5)===0)x.fillRect(i,j,2,2);
    x.fillStyle='#2c2f4a';x.fillRect(0,H*.72,W,3);
    /* 창문과 달 */
    x.fillStyle='#232a4d';x.fillRect(W*.06,H*.08,W*.18,H*.24);x.fillStyle='#f1e6b8';x.beginPath();x.arc(W*.18,H*.15,Math.max(4,W*.025),0,7);x.fill();
    x.strokeStyle='#363a52';x.lineWidth=3;x.strokeRect(W*.06,H*.08,W*.18,H*.24);x.beginPath();x.moveTo(W*.15,H*.08);x.lineTo(W*.15,H*.32);x.stroke();
    /* 형광 시험관 */
    [[.84,'#5ee39c'],[.88,'#d672d6'],[.92,'#82b8ff']].forEach(function(p,k){var h=H*.12,y=H*.2+Math.sin((t||0)*1.5+k)*1.5;x.fillStyle='rgba(236,234,243,.18)';x.fillRect(W*p[0],y,W*.022,h);x.fillStyle=p[1];x.fillRect(W*p[0],y+h*.45,W*.022,h*.55);});
    x.fillStyle='#363a52';x.fillRect(W*.82,H*.2+H*.12,W*.13,4);
    if(prop)prop(x,W,H,t||0);}
  var T=0;addMod(c,function(dt){T+=dt;if(!reduce||!dt)draw(T);});}

/* ---------- 시작 ---------- */
function boot(cfg){GL=cfg.GL;CORE_T=cfg.CORE;
  Cast.fill();scenes();initGloss();initQuiz(cfg.QZ);initProgress();initKG(cfg.kgPath);initExport();
  if(reduce)mods.forEach(function(m){m.fn(0);});else mods.forEach(function(m){m.fn(0);});
  var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(function(){mods.forEach(function(m){m.fn(0);});},120);});
  requestAnimationFrame(loop);}

return {$:$,$$:$$,C:C,FONT:FONT,reduce:reduce,fitC:fitC,grid:grid,stamp:stamp,txt:txt,pct:pct,fmt:fmt,kpis:kpis,mean:mean,sd:sd,quantile:quantile,median:median,corr:corr,spearman:spearman,radio:radio,
  Cast:Cast,addMod:addMod,Duel:Duel,heroStage:heroStage,boot:boot};
})();
