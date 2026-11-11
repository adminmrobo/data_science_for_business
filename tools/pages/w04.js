/* 4주차 · 데이터 분석 개념의 이해 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,F=LAB.FONT,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;

/* ---------- 히어로 소품: 연장통 + 나무 그림 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var bx=W*.36,by=H*.38;x.fillStyle='#5a4636';x.fillRect(bx,by,W*.3,H*.2);x.fillStyle='#7a5c44';x.fillRect(bx,by-6,W*.3,8);
  [[C.gfp,'▦'],[C.info,'▮'],[C.stain,'{ }'],[C.amber,'◔']].forEach(function(o,i){var px=bx+W*.03+i*W*.065,py=by-H*.12+Math.sin(t*1.4+i)*2;x.fillStyle=o[0];x.fillRect(px,py,W*.045,H*.12);});
  var tx=W*.82,ty=H*.1;x.strokeStyle=C.seq;x.lineWidth=2;x.beginPath();x.moveTo(tx,ty);x.lineTo(tx-W*.05,ty+H*.1);x.moveTo(tx,ty);x.lineTo(tx+W*.05,ty+H*.1);x.moveTo(tx-W*.05,ty+H*.1);x.lineTo(tx-W*.08,ty+H*.2);x.moveTo(tx-W*.05,ty+H*.1);x.lineTo(tx-W*.02,ty+H*.2);x.stroke();x.lineWidth=1;
  [[tx,ty],[tx-W*.05,ty+H*.1],[tx+W*.05,ty+H*.1],[tx-W*.08,ty+H*.2],[tx-W*.02,ty+H*.2]].forEach(function(p,i){x.fillStyle=i>2?C.gfp:C.amber;x.beginPath();x.arc(p[0],p[1],4,0,7);x.fill();});});

/* ---------- ① 도구 추천 ---------- */
var TQ=[[['s','수천 행 이하'],['m','수십만 행'],['l','수백만 행 이상']],[['b','합계·피벗·차트'],['t','통계 검정·회귀'],['ml','머신러닝·딥러닝']],[['me','나 혼자 본다'],['team','팀이 함께 편집'],['exec','경영진 대시보드']],[['once','한 번 하고 끝'],['rep','매달 반복·재현 필요']]];
var tv=['s','b','me','once'];
TQ.forEach(function(q,i){LAB.radio('#tq'+i,q.map(function(o){return [o[0],o[1],'tq'+i+'_'+o[0]]}),q[0][0],function(v){tv[i]=v;draw1();});});
var TOOLS=[['스프레드시트','엑셀·구글 시트'],['시각화·BI','Tableau·Power BI'],['상용 통계','SAS·SPSS·STATA'],['오픈소스','Python·R']];
function tscore(){var s=[5,3,3,3],why=[];
  if(tv[0]==='m'){s[0]-=1;s[2]+=1;s[3]+=1;}if(tv[0]==='l'){s[0]-=4;s[2]+=2;s[3]+=3;why.push('수백만 행 이상은 스프레드시트의 처리 한계를 넘습니다.');}
  if(tv[1]==='t'){s[2]+=2;s[3]+=1;s[0]-=1;}if(tv[1]==='ml'){s[3]+=3;s[2]+=1;s[0]-=3;s[1]-=1;why.push('머신러닝·딥러닝은 Python·R의 라이브러리(scikit-learn 등)가 강합니다.');}
  if(tv[2]==='team'){s[0]+=1;why.push('구글 시트는 클라우드에서 실시간 협업이 됩니다.');}if(tv[2]==='exec'){s[1]+=3;why.push('대시보드 공유는 Tableau·Power BI의 강점입니다.');}
  if(tv[3]==='rep'){s[3]+=2;s[0]-=1;why.push('반복·재현은 코드로 남기는 쪽(스크립트, Git 버전 관리)이 쉽습니다.');}
  if(tv[0]==='s'&&tv[1]==='b')why.push('작고 단순한 분석은 스프레드시트가 가장 빠릅니다. 교안의 초보자 경로도 여기서 시작합니다.');
  return {s:s.map(function(v){return Math.max(0,Math.min(10,v))}),why:why};}
function draw1(){var R=tscore(),c=$('#c1'),W=fitC(c,200),H=200,x=c.getContext('2d');grid(x,W,H);var best=R.s.indexOf(Math.max.apply(0,R.s));
  R.s.forEach(function(v,i){var y=24+i*42,bw=(W-260)*v/10;txt(x,TOOLS[i][0],20,y+14,C.text,13,'left',700);txt(x,TOOLS[i][1],20,y+30,C.muted,11);x.fillStyle=C.panel2;x.fillRect(160,y+4,W-260,24);x.fillStyle=i===best?C.gfp:C.seq;x.fillRect(160,y+4,bw,24);txt(x,v+'/10',160+bw+8,y+16,C.text,12,'left',700);});
  stamp(x,W,'도식 · 교안 비교표를 규칙으로 옮김');
  $('#ins1').innerHTML='<p class="g">가장 어울리는 묶음: <b>'+TOOLS[best][0]+'</b> ('+TOOLS[best][1]+')</p>'+R.why.map(function(w){return '<p class="a">'+w+'</p>'}).join('');}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- 대출 데이터 ---------- */
function gen(n,seed){var r=rng(seed),a=[];for(var i=0;i<n;i++){var inc=2+r()*6,debt=r();var good=debt<0.18+0.09*(inc-2)+0.04*Math.sin(inc*1.3);if(r()<.08)good=!good;a.push({x:inc,y:debt,c:good?1:0});}return a;}
var TR=gen(600,3),TE=gen(400,99);
function d2(p,q){var dx=(p.x-q.x)/6,dy=p.y-q.y;return dx*dx+dy*dy;}
function order(q,S){return S.map(function(p,i){return [d2(p,q),i]}).sort(function(a,b){return a[0]-b[0]}).map(function(v){return v[1]});}
var ORD_TR=null,ORD_TE=null,GRID=null,GX=60,GY=36;
function ordTr(){if(!ORD_TR)ORD_TR=TR.map(function(p){return order(p,TR)});return ORD_TR;}
function ordTe(){if(!ORD_TE)ORD_TE=TE.map(function(p){return order(p,TR)});return ORD_TE;}
function ordGrid(){if(!GRID){GRID=[];for(var j=0;j<GY;j++)for(var i=0;i<GX;i++)GRID.push(order({x:2+6*(i+.5)/GX,y:(j+.5)/GY},TR));}return GRID;}
function vote(ord,k,skip){var s=0,n=0;for(var t=0;t<ord.length&&n<k;t++){var j=ord[t];if(skip&&skip(j))continue;s+=TR[j].c;n++;}return s*2>n?1:0;}
function accTr(k){var o=ordTr(),ok=0;TR.forEach(function(p,i){if(vote(o[i],k)===p.c)ok++;});return ok/TR.length;}
function accTe(k){var o=ordTe(),ok=0;TE.forEach(function(p,i){if(vote(o[i],k)===p.c)ok++;});return ok/TE.length;}
var FOLD=TR.map(function(p,i){return i%5});
function cv(k){var o=ordTr(),sc=[];for(var f=0;f<5;f++){var ok=0,n=0;TR.forEach(function(p,i){if(FOLD[i]!==f)return;n++;if(vote(o[i],k,function(j){return FOLD[j]===f})===p.c)ok++;});sc.push(ok/n);}return sc;}
function ruleAcc(I,D,S){return S.filter(function(p){return ((p.x>=I&&p.y<=D)?1:0)===p.c}).length/S.length;}
function plotPts(x,S,X0,Y0,Wd,Hh,lim){S.slice(0,lim||S.length).forEach(function(p){var px=X0+(p.x-2)/6*Wd,py=Y0+Hh-p.y*Hh;x.fillStyle=p.c?C.gfp:C.eye;x.beginPath();x.arc(px,py,2.3,0,7);x.fill();});}
function axes(x,X0,Y0,Wd,Hh){x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[2,4,6,8].forEach(function(v){txt(x,v+'천만',X0+(v-2)/6*Wd,Y0+Hh+12,C.muted,10,'center');});[0,.5,1].forEach(function(v){txt(x,Math.round(v*100)+'%',X0-4,Y0+Hh-v*Hh,C.muted,10,'right');});}
function knnMap(x,k,X0,Y0,Wd,Hh){var G=ordGrid();for(var j=0;j<GY;j++)for(var i=0;i<GX;i++){var v=vote(G[j*GX+i],k);x.fillStyle=v?'rgba(94,227,156,.16)':'rgba(240,96,77,.12)';x.fillRect(X0+i*Wd/GX,Y0+Hh-(j+1)*Hh/GY,Wd/GX+.5,Hh/GY+.5);}}

/* ---------- ② 규칙 vs 머신러닝 ---------- */
var vw='both';
LAB.radio('#vw2',[['both','둘 다','vw0'],['rule','규칙만','vw1'],['ml','머신러닝만','vw2']],'both',function(v){vw=v;draw2();});
$('#rI').addEventListener('input',function(){$('#rIv').textContent=(+this.value*1000).toLocaleString('ko-KR')+'만';draw2();});
$('#rD').addEventListener('input',function(){$('#rDv').textContent=this.value+'%';draw2();});
function draw2(){var I=+$('#rI').value,D=+$('#rD').value/100,c=$('#c2'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);
  var panels=vw==='both'?['rule','ml']:[vw],pw=(W-60)/panels.length;
  panels.forEach(function(pn,i){var X0=40+i*pw,Y0=34,Wd=pw-30,Hh=H-70;
    if(pn==='rule'){x.fillStyle='rgba(94,227,156,.16)';var rx=X0+(I-2)/6*Wd;x.fillRect(rx,Y0+Hh-D*Hh,X0+Wd-rx,D*Hh);x.fillStyle='rgba(240,96,77,.12)';x.fillRect(X0,Y0,Wd,Hh);x.fillStyle='rgba(94,227,156,.16)';x.fillRect(rx,Y0+Hh-D*Hh,X0+Wd-rx,D*Hh);
      x.strokeStyle=C.amber;x.lineWidth=2;x.strokeRect(rx,Y0+Hh-D*Hh,X0+Wd-rx,D*Hh);x.lineWidth=1;txt(x,'규칙: 네모 안 = 승인',X0,20,C.amber,12,'left',700);}
    else{knnMap(x,15,X0,Y0,Wd,Hh);txt(x,'머신러닝(KNN, K = 15): 배운 승인 영역',X0,20,C.info,12,'left',700);}
    plotPts(x,TE,X0,Y0,Wd,Hh,250);axes(x,X0,Y0,Wd,Hh);});
  txt(x,'가로: 연소득 · 세로: 부채비율 · ● 정상 상환 ● 연체 (시험 기록 250건 표시)',40,H-6,C.muted,10);
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var ra=ruleAcc(I,D,TE),ma=accTe(15),rtr=ruleAcc(I,D,TR);
  kpis($('#k2'),[['a',pct(rtr,1),'규칙의 과거 600건 정확도'],['r',pct(ra,1),'규칙의 시험 400건 정확도'],['i',pct(accTr(15),1),'머신러닝 과거 600건'],['g',pct(ma,1),'머신러닝 시험 400건']]);
  $('#ins2').innerHTML=(ra<ma?'<p class="a">이 규칙은 시험에서 '+pct(ra,1)+'로 머신러닝('+pct(ma,1)+')보다 '+((ma-ra)*100).toFixed(1)+'%p 낮습니다. 슬라이더로 더 좋은 네모를 찾아보세요. 네모의 한계는 비스듬한 경계에서 옵니다.</p>':'<p class="g">이 규칙이 시험에서 머신러닝과 비슷하거나 높습니다('+pct(ra,1)+'). 좋은 네모를 찾았네요.</p>')+'<p class="m">규칙은 "연소득 '+(I*1000).toLocaleString('ko-KR')+'만 원 미만이라 거절"처럼 이유를 말할 수 있습니다. KNN은 "비슷한 과거 15건 중 다수가 연체"라고만 말합니다.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 과적합·교차 검증 ---------- */
var KS=[1,3,5,7,9,11,15,21,27,35,43,51],CVC={};function cvK(k){if(!CVC[k])CVC[k]=cv(k);return CVC[k];}
$('#kk').addEventListener('input',function(){$('#kkv').textContent=this.value;draw3();});
function draw3(){var k=+$('#kk').value,c=$('#c3'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);
  var X0=40,Y0=34,Wd=(W-110)/2,Hh=H-70;knnMap(x,k,X0,Y0,Wd,Hh);plotPts(x,TR,X0,Y0,Wd,Hh,300);axes(x,X0,Y0,Wd,Hh);txt(x,'K = '+k+'로 배운 승인 영역 (훈련 기록 300건 표시)',X0,20,C.info,12,'left',700);
  var X1=X0+Wd+50,W1=W-X1-20,sx=function(kk){return X1+(kk-1)/50*W1},sy=function(v){return Y0+Hh-(v-.7)/.3*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[.7,.8,.9,1].forEach(function(v){txt(x,Math.round(v*100)+'%',X1-4,sy(v),C.muted,10,'right');});[1,11,21,31,41,51].forEach(function(v){txt(x,'K='+v,sx(v),Y0+Hh+12,C.muted,10,'center');});
  [[function(kk){return accTr(kk)},C.amber,'훈련'],[function(kk){return LAB.mean(cvK(kk))},C.gfp,'다섯 번 돌아가며 시험']].forEach(function(s){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();KS.forEach(function(kk,i){var v=s[0](kk);i?x.lineTo(sx(kk),sy(v)):x.moveTo(sx(kk),sy(v));});x.stroke();x.lineWidth=1;});
  txt(x,'— 훈련 정확도',X1+6,Y0+12,C.amber,11,'left',700);txt(x,'— 다섯 번 돌아가며 시험 평균',X1+6,Y0+28,C.gfp,11,'left',700);
  var cs=cvK(k);x.strokeStyle=C.text;x.setLineDash([3,3]);x.beginPath();x.moveTo(sx(k),Y0);x.lineTo(sx(k),Y0+Hh);x.stroke();x.setLineDash([]);
  cs.forEach(function(v){x.fillStyle='rgba(94,227,156,.7)';x.beginPath();x.arc(sx(k),sy(v),3,0,7);x.fill();});
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var best=KS.slice().sort(function(a,b){return LAB.mean(cvK(b))-LAB.mean(cvK(a))})[0],m=LAB.mean(cs);
  kpis($('#k3'),[['a',pct(accTr(k),1),'훈련 정확도'],['g',pct(m,1),'돌아가며 시험 평균'],['i','±'+(LAB.sd(cs)*100).toFixed(1)+'%p','다섯 겹의 흩어짐'],['m','K = '+best,'돌아가며 시험이 고른 K']]);
  $('#eq3').innerHTML='5겹 점수: '+cs.map(function(v){return '<b>'+pct(v,1)+'</b>'}).join(' · ')+' → 평균 <em>'+pct(m,1)+'</em> · 봉인한 시험 400건(마지막에만): <i>'+pct(accTe(k),1)+'</i>';
  $('#ins3').innerHTML=k===1?'<p class="r">K = 1: 훈련 100%인데 돌아가며 시험은 '+pct(m,1)+'. 예외까지 외운 과적합입니다.</p>':k>=35?'<p class="a">K가 크면 경계가 뭉개져 훈련·검증 모두 내려갑니다(과소적합).</p>':'<p class="g">훈련과 돌아가며 시험의 차이가 줄었습니다. 돌아가며 시험이 가장 높은 K는 '+best+'입니다.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 장바구니 ---------- */
var ITEMS=['라면','달걀','우유','커피','케이크'],CUS=['A','B','C','D','E'];
var BASE=[[1,1,0,1,0],[1,1,1,0,0],[0,0,1,1,1],[1,1,0,0,1],[0,1,1,1,1]],BK=BASE.map(function(r){return r.slice()});
var RULES=[[0,1],[3,4],[2,1],[1,0]],rI=0;
LAB.radio('#ruleBtns',RULES.map(function(r,i){return [i,ITEMS[r[0]]+' → '+ITEMS[r[1]],'ru'+i]}),0,function(v){rI=+v;draw4();});
$('#bkReset').addEventListener('click',function(){BK=BASE.map(function(r){return r.slice()});draw4();});
function draw4(){var r=RULES[rI],a=r[0],b=r[1],n=CUS.length,nA=0,nB=0,nAB=0;BK.forEach(function(row){if(row[a])nA++;if(row[b])nB++;if(row[a]&&row[b])nAB++;});
  var sup=nAB/n,conf=nA?nAB/nA:0,lift=nB?conf/(nB/n):0;
  $('#bkTable').innerHTML='<thead><tr><th>손님</th>'+ITEMS.map(function(it,i){return '<th'+(i===a||i===b?' style="color:var(--amber)"':'')+'>'+it+'</th>'}).join('')+'</tr></thead><tbody>'+BK.map(function(row,ci){return '<tr><td>'+CUS[ci]+'</td>'+row.map(function(v,ii){return '<td class="'+(v?((ii===a||ii===b)&&row[a]&&row[b]?'fix':''):'')+'"><button class="bt" type="button" id="bk'+ci+'_'+ii+'" style="padding:1px 10px" aria-pressed="'+(v?'true':'false')+'" data-c="'+ci+'" data-i="'+ii+'">'+(v?'✓':'·')+'</button></td>'}).join('')+'</tr>';}).join('')+'</tbody>';
  $$('#bkTable button').forEach(function(bt){bt.addEventListener('click',function(){var ci=+bt.dataset.c,ii=+bt.dataset.i;BK[ci][ii]=BK[ci][ii]?0:1;draw4();});});
  kpis($('#k4'),[['i',nAB+'/'+n+' = '+sup.toFixed(2),'지지도'],['g',nA?nAB+'/'+nA+' = '+conf.toFixed(2):'–','신뢰도'],[lift>1?'g':lift<1?'r':'a',nB?lift.toFixed(2):'–','향상도'],['a',nB+'/'+n,ITEMS[b]+' 전체 구매 비율']]);
  $('#eq4').innerHTML='향상도 = 신뢰도 ÷ P('+ITEMS[b]+') = <b>'+conf.toFixed(2)+'</b> ÷ '+(nB/n).toFixed(2)+' = <em>'+(nB?lift.toFixed(2):'–')+'</em>';
  $('#ins4').innerHTML=!nA?'<p class="a">'+ITEMS[a]+'를 산 손님이 없어 신뢰도를 계산할 수 없습니다.</p>':lift>1.001?'<p class="g">향상도 '+lift.toFixed(2)+' &gt; 1: '+ITEMS[a]+'를 산 손님은 '+ITEMS[b]+'도 우연보다 '+Math.round((lift-1)*100)+'% 더 삽니다. 교차 판매 후보입니다.</p>':lift<0.999?'<p class="r">향상도 '+lift.toFixed(2)+' &lt; 1: 함께 사는 경향이 오히려 약합니다(음의 연관).</p>':'<p class="a">향상도 1: 서로 독립입니다. 신뢰도가 높아 보여도 '+ITEMS[b]+'는 원래 그만큼 팔립니다.</p>';}
draw4();

$('#heroAcc').textContent=pct(accTe(15),1);

/* ---------- 대결 ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.005,max:1,metric:'처음 보는 대출 400건의 결과를 맞힌 비율',fmt:function(v){return pct(v,1)},
  run:function(){return {fly:ruleAcc(4,.4,TE),robo:accTe(15)};},
  report:function(r){return '심사역 규칙은 '+pct(r.fly,1)+', 머신러닝은 '+pct(r.robo,1)+' 맞혔어요. 400건 기준으로 '+Math.round((r.robo-r.fly)*400)+'건 차이예요.';},
  verdict:function(r,res){return '경계가 비스듬하면 데이터에서 배운 쪽이 더 잘 따라간다. '+(res==='R'?'주판봇 승.':res==='F'?'초파리 승.':'이번 판은 나눠 갖는다.');}});
