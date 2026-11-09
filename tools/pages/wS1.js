/* 특강 ① · 이상 탐지 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod,mean=LAB.mean,sdv=LAB.sd,median=LAB.median;

/* ---------- 공용 계산 ---------- */
function cov2(P){var mx=mean(P.map(function(p){return p[0]})),my=mean(P.map(function(p){return p[1]})),sxx=0,syy=0,sxy=0,n=P.length;P.forEach(function(p){var a=p[0]-mx,b=p[1]-my;sxx+=a*a;syy+=b*b;sxy+=a*b;});return {m:[mx,my],S:[[sxx/(n-1),sxy/(n-1)],[sxy/(n-1),syy/(n-1)]]};}
function maha2(p,cv){var a=p[0]-cv.m[0],b=p[1]-cv.m[1],S=cv.S,det=S[0][0]*S[1][1]-S[0][1]*S[0][1];return (a*a*S[1][1]-2*a*b*S[0][1]+b*b*S[0][0])/det;}
function cfun(n){if(n<=1)return 0;if(n===2)return 1;return 2*(Math.log(n-1)+0.5772156649)-2*(n-1)/n;}
function iTree(P,depth,lim,r){if(depth>=lim||P.length<=1)return {n:P.length};var f=r()<.5?0:1,lo=Infinity,hi=-Infinity;P.forEach(function(p){if(p[f]<lo)lo=p[f];if(p[f]>hi)hi=p[f];});if(hi<=lo)return {n:P.length};var t=lo+r()*(hi-lo);
  return {f:f,t:t,L:iTree(P.filter(function(p){return p[f]<t}),depth+1,lim,r),R:iTree(P.filter(function(p){return p[f]>=t}),depth+1,lim,r)};}
function pathLen(x,T,d){if(T.n!==undefined)return d+cfun(T.n);return pathLen(x,x[T.f]<T.t?T.L:T.R,d+1);}
function iForest(X,nT,psi,seed){var r=rng(seed);psi=Math.min(psi,X.length);var lim=Math.ceil(Math.log(psi)/Math.LN2),trees=[];
  for(var k=0;k<nT;k++){var idx=X.map(function(_,i){return i});for(var i=idx.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t;}trees.push(iTree(idx.slice(0,psi).map(function(q){return X[q]}),0,lim,r));}
  var c=cfun(psi);return {c:c,psi:psi,score:function(x){var h=0;trees.forEach(function(T){h+=pathLen(x,T,0)});h/=trees.length;return {h:h,s:Math.pow(2,-h/c)};}};}
function topHits(score,D,k){return score.map(function(s,i){return [s,i]}).sort(function(a,b){return b[0]-a[0]}).slice(0,k).filter(function(o){return D[o[1]].y}).length;}
function zmax(X){var m=[0,1].map(function(f){return mean(X.map(function(x){return x[f]}))}),s=[0,1].map(function(f){return sdv(X.map(function(x){return x[f]}))});return X.map(function(x){return Math.max(Math.abs((x[0]-m[0])/s[0]),Math.abs((x[1]-m[1])/s[1]))});}
function payData(seed,nA,nB,nBad){var r=rng(seed),a=[];
  for(var i=0;i<nA;i++)a.push({x:[Math.max(.2,1.2+gauss(r)*.45),Math.max(1,9+gauss(r)*1.5)],y:0});
  for(i=0;i<nB;i++)a.push({x:[Math.max(2,8.5+gauss(r)*1.0),Math.max(.3,2.2+gauss(r)*.7)],y:0});
  for(i=0;i<nBad;i++){var k=r();a.push({x:k<.75?[3.4+r()*3.2,3.8+r()*3.8]:[11+r()*3,9+r()*4],y:1});}
  return a;}

/* ---------- 히어로 소품 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var r=rng(77);for(var i=0;i<46;i++){var px=W*.3+r()*W*.5,py=H*.06+r()*H*.34;x.fillStyle='rgba(94,227,156,'+(.35+r()*.4)+')';x.beginPath();x.arc(px,py,2.6,0,7);x.fill();}
  var ax=W*.7,ay=H*.13,pu=.5+.5*Math.sin(t*3);x.fillStyle=C.eye;x.beginPath();x.arc(ax,ay,4,0,7);x.fill();x.strokeStyle='rgba(240,96,77,'+(.4+.6*pu)+')';x.lineWidth=2;x.beginPath();x.arc(ax,ay,9+pu*4,0,7);x.stroke();x.lineWidth=1;});

/* ---------- ① Z 점수 ---------- */
var MEAL=(function(){var r=rng(101),a=[];for(var i=0;i<197;i++)a.push(Math.max(.8,+(4.5+gauss(r)*1.1).toFixed(1)));a.splice(40,0,11.8);a.splice(120,0,9.6);a.splice(170,0,48.0);return a;})(),MEAL_BAD=[40,120,170],zMode='ms';
function zs(a,robust){var c,s;if(robust){c=median(a);s=1.4826*median(a.map(function(v){return Math.abs(v-c)}));}else{c=mean(a);s=sdv(a);}return {c:c,s:s,z:a.map(function(v){return (v-c)/s})};}
LAB.radio('#zMode',[['ms','평균·표준편차','zm0'],['rb','중앙값·MAD','zm1']],'ms',function(v){zMode=v;draw1();});
$('#zt').addEventListener('input',function(){$('#ztv').textContent=$('#zt').value;draw1();});
function draw1(){var tau=+$('#zt').value,R=zs(MEAL,zMode==='rb'),c=$('#c1'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var X0=44,X1=W-60,Y0=36,Hh=H-80,lo=0,hi=16,sx=function(v){return X0+(Math.min(v,hi)-lo)/(hi-lo)*(X1-X0)};
  var bins=new Array(32).fill(0);MEAL.forEach(function(v){if(v<hi)bins[Math.floor(v/.5)]++;});var mx=Math.max.apply(0,bins);
  var L=R.c-tau*R.s,U=R.c+tau*R.s;x.fillStyle='rgba(240,96,77,.12)';x.fillRect(X0,Y0,Math.max(0,sx(Math.max(lo,L))-X0),Hh);x.fillRect(sx(U),Y0,Math.max(0,X1-sx(U)),Hh);
  bins.forEach(function(b,i){if(!b)return;var h=b/mx*(Hh-30);x.fillStyle='rgba(130,184,255,.55)';x.fillRect(sx(i*.5)+1,Y0+Hh-h,(X1-X0)/32-2,h);});
  x.strokeStyle=C.rule;x.beginPath();x.moveTo(X0,Y0+Hh);x.lineTo(X1,Y0+Hh);x.stroke();for(var v=0;v<=16;v+=2)txt(x,v+'만',sx(v),Y0+Hh+14,C.muted,10,'center');
  [[R.c,C.gfp,zMode==='rb'?'중앙값':'평균'],[L,C.amber,'−'+tau+'×퍼짐'],[U,C.amber,'+'+tau+'×퍼짐']].forEach(function(q){if(q[0]<lo||q[0]>hi)return;x.strokeStyle=q[1];x.setLineDash(q[1]===C.gfp?[]:[5,4]);x.beginPath();x.moveTo(sx(q[0]),Y0);x.lineTo(sx(q[0]),Y0+Hh);x.stroke();x.setLineDash([]);txt(x,q[2],sx(q[0]),Y0-8,q[1],10,'center',700);});
  var flag=0,hit=0;MEAL.forEach(function(v,i){var f=Math.abs(R.z[i])>tau;if(f)flag++;if(f&&MEAL_BAD.indexOf(i)>=0)hit++;if(f||MEAL_BAD.indexOf(i)>=0){var px=v>=hi?X1+18:sx(v);x.fillStyle=f?C.eye:'rgba(236,234,243,.55)';x.beginPath();x.arc(px,Y0+Hh-10,5,0,7);x.fill();if(!f){x.strokeStyle=C.eye;x.beginPath();x.arc(px,Y0+Hh-10,8,0,7);x.stroke();}}});
  txt(x,'48만 →',X1+18,Y0+Hh-26,C.muted,10,'center');txt(x,'빨간 점: 문턱을 넘은 결제 · 빈 고리: 숨긴 이상인데 통과한 결제',X0,Y0+Hh+30,C.muted,10);stamp(x,W,'예시 데이터');
  kpis($('#k1k'),[['i',R.c.toFixed(2)+'만',zMode==='rb'?'가운데(중앙값)':'가운데(평균)'],['m',R.s.toFixed(2)+'만',zMode==='rb'?'퍼짐(1.4826 × MAD)':'퍼짐(표준편차)'],['a',flag+'건','문턱을 넘은 결제'],[hit===3?'g':'r',hit+' / 3','숨긴 이상 중 잡은 수']]);
  $('#ins1').innerHTML=zMode==='ms'?(hit<3?'<p class="r">표준편차가 '+R.s.toFixed(2)+'만 원으로 부풀어 τ = '+tau+'에서 숨긴 3건 중 '+hit+'건만 잡았습니다. 48만 원 한 건이 나머지를 가렸습니다(가림 효과).</p>':'<p class="a">τ = '+tau+'로 낮추니 숨긴 3건을 모두 잡았지만, 평범한 결제도 '+(flag-hit)+'건 함께 걸렸습니다.</p>'):'<p class="g">중앙값 '+R.c.toFixed(2)+'만 원, 퍼짐 '+R.s.toFixed(2)+'만 원. 극단값에 흔들리지 않아 τ = '+tau+'에서 숨긴 3건 중 '+hit+'건을 잡았고, 평범한 결제는 '+(flag-hit)+'건 걸렸습니다.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 마할라노비스 ---------- */
var TRIP=(function(){var r=rng(202),a=[];for(var i=0;i<146;i++){var d=1+Math.floor(r()*5);a.push({x:[d,Math.round(18+d*22+gauss(r)*7)],k:0,j:(r()-.5)*.36});}
  a.push({x:[1,108],k:1,j:0});a.push({x:[5,46],k:1,j:0});a.push({x:[2,121],k:1,j:0});a.push({x:[7,190],k:2,j:0});return a;})();
var TCV=cov2(TRIP.map(function(t){return t.x})),TM=[0,1].map(function(f){return mean(TRIP.map(function(t){return t.x[f]}))}),TS=[0,1].map(function(f){return sdv(TRIP.map(function(t){return t.x[f]}))}),mView='both';
LAB.radio('#mView',[['z','Z 상자','mv0'],['m','마할라노비스 타원','mv1'],['both','둘 다','mv2']],'both',function(v){mView=v;draw2();});
$('#mt').addEventListener('input',function(){$('#mtv').textContent=$('#mt').value;draw2();});
function draw2(){var tau=+$('#mt').value,c=$('#c2'),W=fitC(c,330),H=330,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-80,Hh=H-64,sx=function(v){return X0+(v-0)/8*Wd},sy=function(v){return Y0+Hh-(v-0)/220*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);for(var d=1;d<=7;d++)txt(x,d+'일',sx(d),Y0+Hh+12,C.muted,10,'center');[0,50,100,150,200].forEach(function(v){txt(x,v+'만',X0-6,sy(v),C.muted,10,'right');});
  x.save();x.beginPath();x.rect(X0,Y0,Wd,Hh);x.clip();
  if(mView!=='m'){x.strokeStyle=C.amber;x.setLineDash([6,4]);x.strokeRect(sx(TM[0]-tau*TS[0]),sy(TM[1]+tau*TS[1]),sx(TM[0]+tau*TS[0])-sx(TM[0]-tau*TS[0]),sy(TM[1]-tau*TS[1])-sy(TM[1]+tau*TS[1]));x.setLineDash([]);txt(x,'Z 상자',sx(TM[0]+tau*TS[0])-4,sy(TM[1]+tau*TS[1])+12,C.amber,11,'right',700);}
  if(mView!=='z'){var S=TCV.S,a=S[0][0],b=S[0][1],dd=S[1][1],tr=a+dd,det=a*dd-b*b,l1=tr/2+Math.sqrt(tr*tr/4-det),l2=tr/2-Math.sqrt(tr*tr/4-det),v1=Math.abs(b)>1e-9?[l1-dd,b]:[1,0],n1=Math.hypot(v1[0],v1[1]);v1=[v1[0]/n1,v1[1]/n1];var v2=[-v1[1],v1[0]];
    x.strokeStyle=C.gfp;x.lineWidth=2;x.beginPath();for(var k=0;k<=72;k++){var th=k/72*2*Math.PI,px=TCV.m[0]+tau*(Math.sqrt(l1)*Math.cos(th)*v1[0]+Math.sqrt(l2)*Math.sin(th)*v2[0]),py=TCV.m[1]+tau*(Math.sqrt(l1)*Math.cos(th)*v1[1]+Math.sqrt(l2)*Math.sin(th)*v2[1]);k?x.lineTo(sx(px),sy(py)):x.moveTo(sx(px),sy(py));}x.closePath();x.stroke();x.lineWidth=1;}
  x.restore();
  var zf=0,mf=0,zh=0,mh=0,longZ=false,longM=false;TRIP.forEach(function(t){var zz=Math.max(Math.abs((t.x[0]-TM[0])/TS[0]),Math.abs((t.x[1]-TM[1])/TS[1])),D=Math.sqrt(maha2(t.x,TCV)),fz=zz>tau,fm=D>tau;if(fz)zf++;if(fm)mf++;if(t.k===1){if(fz)zh++;if(fm)mh++;}if(t.k===2){longZ=fz;longM=fm;}
    var on=mView==='z'?fz:mView==='m'?fm:(fz||fm);x.fillStyle=t.k===1?C.eye:t.k===2?C.amber:'rgba(130,184,255,.65)';x.beginPath();x.arc(sx(t.x[0]+t.j),sy(t.x[1]),t.k?5:3,0,7);x.fill();if(on){x.strokeStyle=C.text;x.beginPath();x.arc(sx(t.x[0]+t.j),sy(t.x[1]),8,0,7);x.stroke();}
    if(t.k)txt(x,'D='+D.toFixed(1),sx(t.x[0])+9,sy(t.x[1])-8,C.text,10);});
  txt(x,'가로: 출장 일수 · 세로: 출장비 · 흰 고리: 경보',X0+6,Y0+12,C.muted,10);stamp(x,W,'예시 데이터');
  var r=TCV.S[0][1]/Math.sqrt(TCV.S[0][0]*TCV.S[1][1]);
  kpis($('#k2k'),[['i',r.toFixed(2),'일수와 출장비의 상관계수'],['a',zh+' / 3 · 경보 '+zf,'Z 상자: 숨긴 3건 중 · 전체 경보'],['g',mh+' / 3 · 경보 '+mf,'타원: 숨긴 3건 중 · 전체 경보'],['m',(Math.exp(-tau*tau/2)*100).toFixed(1)+'%','평범한 기록이 타원 밖일 확률(정규분포 가정)']]);
  $('#ins2').innerHTML='<p class="'+(mh>zh?'g':'a')+'">문턱 '+tau+'에서 Z 상자는 숨긴 3건 중 '+zh+'건을 잡고 7일 출장에는 '+(longZ?'경보를 울렸습니다':'울리지 않았습니다')+'. 마할라노비스 타원은 '+mh+'건을 잡고 7일 출장에는 '+(longM?'경보를 울렸습니다(경계 근처)':'울리지 않았습니다')+'.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 고립 숲 ---------- */
var PAY=payData(306,170,110,12),PX=PAY.map(function(d){return d.x}),IF3=iForest(PX,100,256,9),S3=PX.map(function(p){return IF3.score(p)}),M3cv=cov2(PX),M3=PX.map(function(p){return Math.sqrt(maha2(p,M3cv))}),Z3=zmax(PX);
var normalIdx=(function(){var b=0,bd=1e9;PAY.forEach(function(d,i){if(d.y)return;var q=Math.hypot(d.x[0]-1.2,(d.x[1]-9)/3);if(q<bd){bd=q;b=i;}});return b;})(),badIdx=(function(){var b=0,bs=-1;PAY.forEach(function(d,i){if(d.y&&d.x[0]<7&&S3[i].s>bs){bs=S3[i].s;b=i;}});return b;})();
var ifTarget=normalIdx,ifMapMode='if',cutSeed=1,cutHist=[],GRID3=null,GRIDM=null;
LAB.radio('#ifPt',[['n','무리 한가운데 점','ip0'],['b','두 무리 사이 점','ip1']],'n',function(v){ifTarget=v==='n'?normalIdx:badIdx;cutHist=[];cutSeed=1;draw3();});
LAB.radio('#ifMap',[['if','고립 숲 점수','im0'],['m','마할라노비스 거리','im1']],'if',function(v){ifMapMode=v;draw3();});
$('#ifTree').addEventListener('click',function(){cutSeed++;draw3(true);});
function isolate(target,seed){var r=rng(seed*7919+13),P=PX.slice(),box=[[0,15],[0,17]],cuts=[];while(P.length>1&&cuts.length<30){var f=r()<.5?0:1,lo=Infinity,hi=-Infinity;P.forEach(function(p){if(p[f]<lo)lo=p[f];if(p[f]>hi)hi=p[f];});if(hi<=lo)break;var t=lo+r()*(hi-lo);cuts.push({f:f,t:t,box:[box[0].slice(),box[1].slice()]});
  if(target[f]<t){P=P.filter(function(p){return p[f]<t});box[f][1]=t;}else{P=P.filter(function(p){return p[f]>=t});box[f][0]=t;}}return cuts;}
function draw3(newTree){var c=$('#c3'),W=fitC(c,340),H=340,x=c.getContext('2d');grid(x,W,H);var X0=50,Y0=20,Wd=Math.min(W-70,620),Hh=H-56,sx=function(v){return X0+v/15*Wd},sy=function(v){return Y0+Hh-v/17*Hh},G=40;
  if(ifMapMode==='if'&&!GRID3){GRID3=[];for(var j=0;j<G;j++)for(var i=0;i<G;i++)GRID3.push(IF3.score([(i+.5)/G*15,(j+.5)/G*17]).s);}
  if(ifMapMode==='m'&&!GRIDM){GRIDM=[];for(j=0;j<G;j++)for(i=0;i<G;i++)GRIDM.push(Math.sqrt(maha2([(i+.5)/G*15,(j+.5)/G*17],M3cv)));}
  var GG=ifMapMode==='if'?GRID3:GRIDM,gs=GG.slice().sort(function(a,b){return a-b}),rk=function(q){var lo=0,hi=gs.length;while(lo<hi){var md=(lo+hi)>>1;if(gs[md]<q)lo=md+1;else hi=md;}return lo/gs.length;};
  for(j=0;j<G;j++)for(i=0;i<G;i++){var v=rk(GG[j*G+i]);x.fillStyle='rgba(214,114,214,'+(.03+.55*v*v)+')';x.fillRect(X0+i*Wd/G,Y0+Hh-(j+1)*Hh/G,Wd/G+.5,Hh/G+.5);}
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,3,6,9,12,15].forEach(function(v){txt(x,v+'만',sx(v),Y0+Hh+12,C.muted,10,'center');});[0,4,8,12,16].forEach(function(v){txt(x,v+'회',X0-6,sy(v),C.muted,10,'right');});
  PAY.forEach(function(d,i){x.fillStyle=d.y?C.eye:i<170?'rgba(130,184,255,.75)':'rgba(94,227,156,.75)';x.beginPath();x.arc(sx(d.x[0]),sy(d.x[1]),d.y?4.5:3,0,7);x.fill();});
  var sc=ifMapMode==='if'?S3.map(function(q){return q.s}):M3,top=sc.map(function(v,i){return [v,i]}).sort(function(a,b){return b[0]-a[0]}).slice(0,12);x.strokeStyle=C.text;x.lineWidth=1.5;top.forEach(function(o){var d=PAY[o[1]];x.beginPath();x.arc(sx(d.x[0]),sy(d.x[1]),8,0,7);x.stroke();});x.lineWidth=1;
  var tg=PX[ifTarget],cuts=isolate(tg,cutSeed);x.strokeStyle='rgba(241,182,70,.85)';cuts.forEach(function(q){var b=q.box;x.beginPath();if(q.f===0){x.moveTo(sx(q.t),sy(b[1][0]));x.lineTo(sx(q.t),sy(b[1][1]));}else{x.moveTo(sx(b[0][0]),sy(q.t));x.lineTo(sx(b[0][1]),sy(q.t));}x.stroke();});
  x.fillStyle=C.amber;x.strokeStyle=C.text;x.lineWidth=2;x.beginPath();x.arc(sx(tg[0]),sy(tg[1]),7,0,7);x.fill();x.stroke();x.lineWidth=1;
  txt(x,'흰 고리: '+(ifMapMode==='if'?'고립 숲':'마할라노비스')+' 점수 상위 12건 · 배경이 밝을수록 '+(ifMapMode==='if'?'고립 숲 점수가 높음':'평균에서 마할라노비스 거리가 멂'),X0+6,Y0+12,C.muted,10);stamp(x,W,'예시 데이터');
  if(newTree)cutHist.push(cuts.length);if(!cutHist.length)cutHist.push(cuts.length);
  var sN=mean(S3.filter(function(_,i){return !PAY[i].y}).map(function(q){return q.s})),sB=mean(S3.filter(function(_,i){return PAY[i].y}).map(function(q){return q.s}));
  var hIF=topHits(S3.map(function(q){return q.s}),PAY,12),hM=topHits(M3,PAY,12);
  kpis($('#k3k'),[['a',cuts.length+'번','이번 나무에서 혼자 남기까지 자른 횟수'],['i',S3[ifTarget].h.toFixed(2)+' → s = '+S3[ifTarget].s.toFixed(2),'나무 100그루 평균 경로 E[h] → 점수 (c(256) = '+IF3.c.toFixed(1)+')'],['m',sN.toFixed(2)+' / '+sB.toFixed(2),'점수 평균: 평범한 280건 / 이상 12건'],['g',hIF+' · '+hM+' / 12','상위 12건 중 진짜 이상: 고립 숲 · 마할라노비스']]);
  $('#ins3').innerHTML=(ifTarget===normalIdx?'<p class="a">무리 한가운데 점: 이번 나무에서 '+cuts.length+'번 잘라야 혼자 남았습니다.':'<p class="r">두 무리 사이 점: 이번 나무에서 '+cuts.length+'번 만에 혼자 남았습니다.')+(cutHist.length>1?' 지금까지 '+cutHist.length+'그루 평균 '+(mean(cutHist)).toFixed(1)+'번.':'')+' 이 점의 100그루 평균 경로는 '+S3[ifTarget].h.toFixed(2)+', 점수는 '+S3[ifTarget].s.toFixed(2)+'입니다.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});
$('#heroHit').textContent=topHits(Z3,PAY,12)+' → '+topHits(S3.map(function(q){return q.s}),PAY,12)+'건';

/* ---------- ④ 복원 오차 (직선 오토인코더 = 주성분) ---------- */
function bump(h,c,w){return Math.exp(-(h-c)*(h-c)/(2*w*w));}
function openH(h){return h>=9&&h<=21?1:0;}
function shape(t,h,sh){var hh=h-(sh||0);if(!(hh>=9&&hh<=21))return 0;return t===0?12+38*bump(hh,12.3,1.1)+30*bump(hh,18.5,1.4):14+34*bump(hh,15,2.6);}
var DAYS=(function(){var r=rng(404),a=[],h,v;for(var d=0;d<140;d++){var t=(d%7)>=5?1:0,amp=.75+r()*.5;v=[];for(h=0;h<24;h++)v.push(Math.max(0,shape(t,h)*amp+(shape(t,h)>0?gauss(r)*2.2:Math.abs(gauss(r))*.4)));a.push({v:v,y:0,t:t,name:t?'주말(정상)':'평일(정상)'});}
  var bad=[],cl=function(v){return v.map(function(q){return Math.max(0,q)})};
  v=[];for(h=0;h<24;h++)v.push(shape(0,h,3)+gauss(r)*1.5*(shape(0,h,3)>0?1:0));bad.push({v:cl(v),y:1,name:'개점 3시간 늦음'});
  v=[];for(h=0;h<24;h++)v.push(openH(h)?30:0);bad.push({v:v,y:1,name:'센서 고정'});
  v=[];for(h=0;h<24;h++)v.push(h>=9&&h<=15?shape(0,h)*1.05+gauss(r)*1.5:0);bad.push({v:cl(v),y:1,name:'저녁 휴업'});
  v=[];for(h=0;h<24;h++)v.push(openH(h)?(14+34*bump(h,15,2.6))*.6+30*bump(h,18.5,1.4)*.9+gauss(r)*1.5:0);bad.push({v:cl(v),y:1,name:'평일·주말 섞임'});
  v=[];for(h=0;h<24;h++)v.push(openH(h)?12+45*bump(h,10,1.0)+10*bump(h,18.5,1.4)+gauss(r)*1.5:0);bad.push({v:cl(v),y:1,name:'오전 행사'});
  v=[];for(h=0;h<24;h++)v.push(openH(h)?12+30*bump(h,12.3,1.1)+38*bump(h,18.5,1.4)+gauss(r)*1.5:0);bad.push({v:cl(v),y:1,name:'정점 뒤바뀜'});
  [17,41,66,88,103,127].forEach(function(p,i){a.splice(p,0,bad[i]);});return a;})();
function jacobi(A){var n=A.length,V=A.map(function(_,i){return A.map(function(_,j){return i===j?1:0})}),a=A.map(function(r){return r.slice()}),p,q,k;
  for(var sw=0;sw<60;sw++){var off=0;for(p=0;p<n;p++)for(q=p+1;q<n;q++)off+=a[p][q]*a[p][q];if(off<1e-10)break;
    for(p=0;p<n;p++)for(q=p+1;q<n;q++){if(Math.abs(a[p][q])<1e-12)continue;var th=(a[q][q]-a[p][p])/(2*a[p][q]),t=(th>=0?1:-1)/(Math.abs(th)+Math.sqrt(th*th+1)),c=1/Math.sqrt(t*t+1),s=t*c;
      for(k=0;k<n;k++){var akp=a[k][p],akq=a[k][q];a[k][p]=c*akp-s*akq;a[k][q]=s*akp+c*akq;}
      for(k=0;k<n;k++){var apk=a[p][k],aqk=a[q][k];a[p][k]=c*apk-s*aqk;a[q][k]=s*apk+c*aqk;}
      for(k=0;k<n;k++){var vkp=V[k][p],vkq=V[k][q];V[k][p]=c*vkp-s*vkq;V[k][q]=s*vkp+c*vkq;}}}
  var ev=a.map(function(r,i){return r[i]}),idx=ev.map(function(_,i){return i}).sort(function(i,j){return ev[j]-ev[i]});return {val:idx.map(function(i){return ev[i]}),vec:idx.map(function(i){return V.map(function(r){return r[i]})})};}
var PCA=(function(){var X=DAYS.filter(function(d){return !d.y}).map(function(d){return d.v}),n=X.length,m=[],a,b,j;for(j=0;j<24;j++)m.push(mean(X.map(function(x){return x[j]})));var Cv=[];for(a=0;a<24;a++){Cv.push([]);for(b=0;b<24;b++){var s=0;X.forEach(function(x){s+=(x[a]-m[a])*(x[b]-m[b])});Cv[a].push(s/(n-1));}}var E=jacobi(Cv),tot=E.val.reduce(function(p,q){return p+Math.max(0,q)},0);
  return {m:m,E:E,tot:tot,rec:function(x,k){if(k>=24)return x.slice();var out=m.slice(),i,jj;for(i=0;i<k;i++){var z=0;for(jj=0;jj<24;jj++)z+=(x[jj]-m[jj])*E.vec[i][jj];for(jj=0;jj<24;jj++)out[jj]+=z*E.vec[i][jj];}return out;}};})();
function aeErr(d,k){var r=PCA.rec(d.v,k),e=0;for(var j=0;j<24;j++)e+=(d.v[j]-r[j])*(d.v[j]-r[j]);return e;}
var aeK=2,aeDay=127,ERRC={};function errs(k){return ERRC[k]||(ERRC[k]=DAYS.map(function(d){return aeErr(d,k)}));}
var dayChoices=[['0','평일(정상)','ad0'],['5','주말(정상)','ad1']].concat([17,41,66,88,103,127].map(function(p,i){return [String(p),DAYS[p].name,'ad'+(i+2)]}));
LAB.radio('#aeK',[['1','1','ak1'],['2','2','ak2'],['3','3','ak3'],['6','6','ak6'],['24','24 (병목 없음)','ak24']],'2',function(v){aeK=+v;draw4();});
LAB.radio('#aeDay',dayChoices,'127',function(v){aeDay=+v;draw4();});
function draw4(){var c=$('#c4'),W=fitC(c,360),H=360,x=c.getContext('2d');grid(x,W,H);var d=DAYS[aeDay],rc=PCA.rec(d.v,aeK),E=errs(aeK);
  var X0=48,X1=W-20,Y0=24,Hh=170,sx=function(h){return X0+h/23*(X1-X0)},sy=function(v){return Y0+Hh-v/80*Hh};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,X1-X0,Hh);[0,6,9,12,15,18,21,23].forEach(function(h){txt(x,h+'시',sx(h),Y0+Hh+12,C.muted,10,'center');});[0,20,40,60,80].forEach(function(v){txt(x,v,X0-6,sy(v),C.muted,10,'right');});
  x.fillStyle='rgba(240,96,77,.18)';for(var h=0;h<23;h++){x.beginPath();x.moveTo(sx(h),sy(d.v[h]));x.lineTo(sx(h+1),sy(d.v[h+1]));x.lineTo(sx(h+1),sy(rc[h+1]));x.lineTo(sx(h),sy(rc[h]));x.closePath();x.fill();}
  [[d.v,C.text,2.5],[rc,C.gfp,2]].forEach(function(L){x.strokeStyle=L[1];x.lineWidth=L[2];x.beginPath();L[0].forEach(function(v,h){h?x.lineTo(sx(h),sy(v)):x.moveTo(sx(h),sy(v));});x.stroke();});x.lineWidth=1;
  txt(x,'흰 선: '+d.name+' 실제 방문객 · 초록 선: 병목 '+aeK+'로 복원 · 빨간 면적: 차이',X0+6,Y0+12,C.muted,10);
  var B0=Y0+Hh+34,Bh=H-B0-26,mx=Math.max.apply(0,E.filter(function(_,i){return !DAYS[i].y}))*1.3||1,bw=(X1-X0)/DAYS.length,lg=function(v){return Math.min(1,Math.log(1+v)/Math.log(1+Math.max.apply(0,E)||2))};
  E.forEach(function(e,i){var hh=lg(e)*Bh;x.fillStyle=i===aeDay?C.amber:DAYS[i].y?C.eye:'rgba(130,184,255,.55)';x.fillRect(X0+i*bw,B0+Bh-hh,Math.max(1,bw-1),hh);});
  txt(x,'146일의 복원 오차(로그 눈금) · 빨강: 숨긴 이상 6일 · 노랑: 지금 보는 날',X0,B0-8,C.muted,10);stamp(x,W,'예시 데이터');
  var ord=E.map(function(e,i){return [e,i]}).sort(function(a,b){return b[0]-a[0]}),rank=ord.map(function(o){return o[1]}).indexOf(aeDay)+1,hits=ord.slice(0,6).filter(function(o){return DAYS[o[1]].y}).length;
  var ex=aeK>=24?1:PCA.E.val.slice(0,aeK).reduce(function(p,q){return p+q},0)/PCA.tot;
  kpis($('#k4k'),[['a',E[aeDay].toFixed(0),'이 날의 복원 오차 e(x)'],['i',rank+'위 / 146','오차 순위'],[hits===6?'g':hits>=4?'a':'r',hits+' / 6','오차 상위 6일 중 숨긴 이상'],['m',pct(ex,1),'병목 '+aeK+'이 담는 정상 패턴의 퍼짐 비율']]);
  $('#ins4').innerHTML=aeK>=24?'<p class="r">병목이 입력과 같은 24칸이면 모든 날을 그대로 베낍니다. 복원 오차가 모두 0이라 아무것도 찾지 못합니다.</p>':aeK===1?'<p class="a">병목 1: 숫자 하나로는 평일 모양과 주말 모양을 함께 담지 못해 평범한 날도 오차가 큽니다. 상위 6일 중 숨긴 이상은 '+hits+'일.</p>':'<p class="'+(hits===6?'g':'a')+'">병목 '+aeK+': 정상 패턴 퍼짐의 '+pct(ex,1)+'를 담습니다. "'+d.name+'"의 오차는 146일 중 '+rank+'위이고, 상위 6일 중 숨긴 이상은 '+hits+'일입니다.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ 문턱값 ---------- */
var TH=(function(){var seed=509,A=payData(seed,330,220,14),r=rng(seed+50);
  for(var i=0;i<10;i++){var g=r()<.5,ang=r()*6.283,rad=2.1+r()*1.2;A.push({x:g?[1.2+Math.cos(ang)*rad*.45,9+Math.sin(ang)*rad*1.5]:[8.5+Math.cos(ang)*rad,2.2+Math.sin(ang)*rad*.7],y:1});}
  A.forEach(function(d){d.x[0]=Math.max(.2,d.x[0]);d.x[1]=Math.max(.3,d.x[1]);});
  var F=iForest(A.map(function(d){return d.x}),100,256,seed+7),S=A.map(function(d){return F.score(d.x).s}),o={A:A,S:S,k:0};
  o.split=function(k){var q=rng(seed+99+k*1000),B=[],Nn=[];A.forEach(function(d,i){(d.y?B:Nn).push(i);});[B,Nn].forEach(function(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(q()*(i+1)),t=a[i];a[i]=a[j];a[j]=t;}});o.k=k;o.V=B.slice(0,12).concat(Nn.slice(0,275));o.T=B.slice(12).concat(Nn.slice(275));};
  o.split(0);return o;})(),thMode='p';
function ev(set,tau){var tp=0,fp=0,fn=0;set.forEach(function(i){var p=TH.S[i]>=tau;if(p&&TH.A[i].y)tp++;else if(p)fp++;else if(TH.A[i].y)fn++;});var pr=tp+fp?tp/(tp+fp):0,rc=tp+fn?tp/(tp+fn):0;return {tp:tp,fp:fp,fn:fn,pr:pr,rc:rc,f1:pr+rc?2*pr*rc/(pr+rc):0,n:tp+fp};}
function costOf(e,miss){return e.n*2+e.fn*miss;}
function pickTau(){var vs=TH.V.map(function(i){return TH.S[i]}).sort(function(a,b){return b-a}),P=+$('#thP').value,miss=+$('#thC').value;
  if(thMode==='p')return vs[Math.max(0,Math.ceil(P/100*vs.length)-1)];
  if(thMode==='k'){var m=mean(vs),s=sdv(vs);return m+P*s;}
  var best=null;vs.forEach(function(t){var e=ev(TH.V,t),sc=thMode==='f1'?e.f1:-costOf(e,miss);if(!best||sc>best[0])best=[sc,t];});return best[1];}
LAB.radio('#thM',[['p','상위 p%','tm0'],['k','평균 + kσ','tm1'],['f1','검증 F1 최대','tm2'],['cost','검증 비용 최소','tm3']],'p',function(v){thMode=v;var sl=$('#thP');if(v==='k'){sl.min=1;sl.max=4;sl.step=.5;sl.value=3;}else{sl.min=1;sl.max=10;sl.step=1;sl.value=5;}sl.disabled=(v==='f1'||v==='cost');$('#thPv').textContent=sl.value;$('#thPl').textContent=v==='k'?'k (표준편차 몇 개)':'상위 p(%)';draw5();});
$('#thSplit').addEventListener('click',function(){TH.split((TH.k+1)%8);draw5();});
['thP','thC'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#thPv').textContent=$('#thP').value;$('#thCv').textContent=$('#thC').value;draw5();});});
function draw5(){var tau=pickTau(),e=ev(TH.T,tau),miss=+$('#thC').value,c=$('#c5'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=50,X1=W-20,Y0=24,Hh=H-60,lo=.35,hi=.8,sy=function(v){return Y0+Hh-(Math.max(lo,Math.min(hi,v))-lo)/(hi-lo)*Hh},sx=function(i){return X0+(i+.5)/TH.T.length*(X1-X0)};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,X1-X0,Hh);[.4,.5,.6,.7,.8].forEach(function(v){txt(x,v.toFixed(1),X0-6,sy(v),C.muted,10,'right');});
  x.fillStyle='rgba(240,96,77,.08)';x.fillRect(X0,Y0,X1-X0,sy(tau)-Y0);
  TH.T.forEach(function(i,k){var a=TH.S[i]>=tau,y=TH.A[i].y;x.fillStyle=y?C.eye:'rgba(130,184,255,.7)';x.beginPath();x.arc(sx(k),sy(TH.S[i]),y?4.5:3,0,7);x.fill();if(a){x.strokeStyle=C.text;x.beginPath();x.arc(sx(k),sy(TH.S[i]),7,0,7);x.stroke();}});
  x.strokeStyle=C.amber;x.setLineDash([6,4]);x.lineWidth=2;x.beginPath();x.moveTo(X0,sy(tau));x.lineTo(X1,sy(tau));x.stroke();x.setLineDash([]);x.lineWidth=1;txt(x,'τ = '+tau.toFixed(3),X1-4,sy(tau)-9,C.amber,11,'right',700);
  txt(x,'시험 데이터 287건의 고립 숲 점수 s(x) · 빨강: 진짜 이상 · 흰 고리: 경보',X0+6,Y0+12,C.muted,10);txt(x,'기록(순서 무관)',(X0+X1)/2,Y0+Hh+14,C.muted,10,'center');stamp(x,W,'예시 데이터');
  var nb=TH.T.filter(function(i){return TH.A[i].y}).length;
  kpis($('#k5k'),[['i',e.n+'건','경보 수(점검 비용 '+(e.n*2)+'만 원)'],[e.rc>=.9?'g':e.rc>=.6?'a':'r',e.tp+' / '+nb,'잡은 진짜 이상(재현율 '+pct(e.rc,0)+')'],[e.pr>=.6?'g':e.pr>=.35?'a':'r',pct(e.pr,0),'정밀도 · F1 '+e.f1.toFixed(2)],['m',(costOf(e,miss)).toLocaleString('ko-KR')+'만 원','총비용 = 점검 + 놓친 '+e.fn+'건 × '+miss+'만 원']]);
  var lab={p:'상위 '+$('#thP').value+'%',k:'평균 + '+$('#thP').value+'σ',f1:'검증 F1 최대',cost:'검증 비용 최소'}[thMode];
  $('#ins5').innerHTML='<p class="'+(e.rc>=.9&&e.pr>=.5?'g':'a')+'">'+lab+' → τ = '+tau.toFixed(3)+'. 시험 데이터에서 경보 '+e.n+'건, 진짜 이상 '+nb+'건 중 '+e.tp+'건을 잡고 '+e.fn+'건을 놓쳤습니다. 오경보는 '+e.fp+'건.</p><p class="i">검증·시험 나누기 '+(TH.k+1)+'번째 / 8. 진짜 이상이 12건뿐이라 한 건 차이로 재현율이 8%p씩 움직입니다. 다시 나누어 숫자가 얼마나 흔들리는지 보세요.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결 ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.5,bigGap:3,max:15,metric:'점수 상위 15건 가운데 진짜 이상(숨긴 12건 중)',fmt:function(v){return v+'건'},
  run:function(){var D=payData(305,170,110,12),X=D.map(function(d){return d.x}),F=iForest(X,100,256,11),S=X.map(function(p){return F.score(p).s}),Z=zmax(X);this.info={between:D.filter(function(d){return d.y&&d.x[0]<7}).length};return {fly:topHits(Z,D,15),robo:topHits(S,D,15)};},
  report:function(r){return '경보 15건 가운데 진짜 이상은 칸별 Z 점수가 '+r.fly+'건, 고립 숲이 '+r.robo+'건이에요. 숨긴 12건 중 '+this.info.between+'건이 두 무리 사이에 있었어요.';},
  verdict:function(r,res){return res==='R'?'평균이 두 무리 사이 빈 곳에 있으면, 평균에서 재는 자는 그 빈 곳의 이상을 평범하게 본다. 주판봇 승.':res==='F'?'칸별 Z 점수로 충분했다. 초파리 승.':'이번 판은 나눠 갖는다.';}});
