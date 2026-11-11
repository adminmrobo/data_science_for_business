/* 10주차 · 회귀모형(2) — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
var sig=function(z){return 1/(1+Math.exp(-z))};
function mean(a){return a.reduce(function(s,v){return s+v},0)/a.length}
function fmtN(v){var a=Math.abs(v);return a>=1e6?(v/1e6).toFixed(1)+'백만':a>=1e4?Math.round(v/1e4)+'만':Math.round(v).toLocaleString('ko-KR');}

/* ---------- 히어로 소품: S자 + 나무 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var X0=W*.3,Y0=H*.08,w=W*.22,h=H*.26;x.strokeStyle='#4a6fa8';x.lineWidth=2;x.strokeRect(X0,Y0,w,h);x.strokeStyle=C.gfp;x.lineWidth=3;x.beginPath();for(var i=0;i<=40;i++){var u=i/40,px=X0+u*w,py=Y0+h-sig((u-.5)*(10+2*Math.sin(t)))*h*.9-h*.05;i?x.lineTo(px,py):x.moveTo(px,py);}x.stroke();
  var tx=W*.78,ty=H*.08;x.strokeStyle='#d8c08a';x.lineWidth=3;x.beginPath();x.moveTo(tx,ty+h);x.lineTo(tx,ty+h*.45);x.moveTo(tx,ty+h*.45);x.lineTo(tx-w*.25,ty+h*.15);x.moveTo(tx,ty+h*.45);x.lineTo(tx+w*.25,ty+h*.15);x.stroke();
  [[-.25,.15],[.25,.15],[0,.45]].forEach(function(p,i){x.fillStyle=i===2?C.amber:i?C.eye:C.info;x.beginPath();x.arc(tx+p[0]*w,ty+p[1]*h,6+Math.sin(t*1.5+i)*1.2,0,7);x.fill();});x.lineWidth=1;});

/* ---------- ① 로지스틱 회귀 ---------- */
var ST=(function(){var r=rng(3),a=[];for(var i=0;i<40;i++){var h=Math.round(r()*100)/10;a.push({h:h,y:r()<sig(-5+1.0*h)?1:0});}return a;})();
function lossL(w0,w1){var s=0;ST.forEach(function(d){var p=Math.min(1-1e-9,Math.max(1e-9,sig(w0+w1*d.h)));s-=d.y*Math.log(p)+(1-d.y)*Math.log(1-p);});return s/ST.length;}
var BEST1=(function(){var w0=0,w1=0;for(var it=0;it<20000;it++){var g0=0,g1=0;ST.forEach(function(d){var e=sig(w0+w1*d.h)-d.y;g0+=e;g1+=e*d.h;});w0-=.05*g0/ST.length;w1-=.05*g1/ST.length;}return [w0,w1];})(),fit1=false;
LAB.radio('#fitBtns',[['hand','손으로','f0'],['fit','비용 최소화','f1']],'hand',function(v){fit1=v==='fit';if(fit1){$('#w1').value=BEST1[1].toFixed(1);$('#w0').value=(Math.round(BEST1[0]*2)/2);}draw1();});
['w1','w0'].forEach(function(id){$('#'+id).addEventListener('input',function(){fit1=false;draw1();});});
function draw1(){var w1=fit1?BEST1[1]:+$('#w1').value,w0=fit1?BEST1[0]:+$('#w0').value;$('#w1v').textContent=w1.toFixed(fit1?2:1);$('#w0v').textContent=fit1?w0.toFixed(2):w0;
  var c=$('#c1'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=50,Y0=30,Wd=(W-110)*.6,Hh=H-66,sx=function(v){return X0+v/10*Wd},sy=function(v){return Y0+Hh-v*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,.5,1].forEach(function(v){txt(x,v.toFixed(1),X0-4,sy(v),C.muted,10,'right');});[0,2,4,6,8,10].forEach(function(v){txt(x,v+'시간',sx(v),Y0+Hh+12,C.muted,10,'center');});
  x.setLineDash([3,3]);x.strokeStyle=C.muted;x.beginPath();x.moveTo(X0,sy(.5));x.lineTo(X0+Wd,sy(.5));x.stroke();x.setLineDash([]);
  var r=rng(8);ST.forEach(function(d){var jy=(r()-.5)*.06;x.fillStyle=d.y?C.gfp:C.eye;x.beginPath();x.arc(sx(d.h),sy(d.y?.97+jy:.03+jy),4,0,7);x.fill();});
  x.strokeStyle=C.info;x.lineWidth=2.5;x.beginPath();for(var i=0;i<=100;i++){var h=i/10;i?x.lineTo(sx(h),sy(sig(w0+w1*h))):x.moveTo(sx(h),sy(sig(w0+w1*h)));}x.stroke();x.lineWidth=1;
  var bnd=w1>0?-w0/w1:null;if(bnd!=null&&bnd>=0&&bnd<=10){x.strokeStyle=C.amber;x.beginPath();x.moveTo(sx(bnd),Y0);x.lineTo(sx(bnd),Y0+Hh);x.stroke();txt(x,'경계 '+bnd.toFixed(1)+'시간',sx(bnd)+4,Y0+12,C.amber,11,'left',700);}
  [['합격(1)',C.gfp],['불합격(0)',C.eye],['p = σ(z)',C.info]].forEach(function(it,k){x.fillStyle=it[1];x.beginPath();x.arc(X0+6+k*78,Y0-10,4,0,7);x.fill();txt(x,it[0],X0+14+k*78,Y0-10,C.muted,10);});
  var X1=X0+Wd+50,W1=W-X1-16,zs=function(v){return Y0+Hh/2-Math.max(-12,Math.min(12,v))/12*(Hh/2)},hx=function(v){return X1+v/10*W1};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);x.beginPath();x.moveTo(X1,zs(0));x.lineTo(X1+W1,zs(0));x.stroke();[-10,0,10].forEach(function(v){txt(x,'z='+v,X1-4,zs(v),C.muted,10,'right');});
  x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.moveTo(hx(0),zs(w0));x.lineTo(hx(10),zs(w0+w1*10));x.stroke();x.lineWidth=1;txt(x,'z = w₀ + w₁·시간 (직선, −∞~+∞)',X1,Y0-8,C.amber,11,'left',700);
  stamp(x,W,'예시 데이터 · 40명');
  var acc=mean(ST.map(function(d){return (sig(w0+w1*d.h)>=.5?1:0)===d.y?1:0})),L=lossL(w0,w1),Lb=lossL(BEST1[0],BEST1[1]);
  kpis($('#k1k'),[[L<=Lb+.005?'g':'a',L.toFixed(3),'틀린 정도(비용)'],['i',Lb.toFixed(3),'가장 작은 틀린 정도'],['m',pct(acc,1),'정확도(0.5 기준)'],['a',pct(sig(w0+w1*6),0),'6시간 공부한 학생의 합격 확률']]);
  $('#ins1').innerHTML=L<=Lb+.005?'<p class="g">비용이 가장 작은 곡선입니다: p = σ('+w0.toFixed(2)+' + '+w1.toFixed(2)+' × 시간). 결정 경계는 약 '+(bnd!=null?bnd.toFixed(1):'–')+'시간.</p>':w1<.3?'<p class="a">w₁이 작아 곡선이 거의 평평합니다. 공부시간이 확률을 거의 바꾸지 못하는 모델입니다.</p>':'<p class="a">비용 '+L.toFixed(3)+' (최소 '+Lb.toFixed(3)+'). 슬라이더로 줄여 보거나 "비용 최소화"를 누르세요.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- 와인 모양 예시 데이터 ---------- */
var FN=['잔당(g/L)','알코올(%)'],FR=[[0,20],[8,14.5]];
function wine(n,seed){var r=rng(seed),a=[];for(var i=0;i<n;i++){var red=r()<.45,s,al;if(red){s=Math.max(.6,2.4+gauss(r)*1.1);al=10.3+gauss(r)*.8;}else if(r()<.5){s=Math.min(19.5,Math.max(1,8+gauss(r)*3.5));al=10+gauss(r)*.9;}else{s=Math.max(.6,2.2+gauss(r)*1);al=11.9+gauss(r)*.8;}
  al=Math.max(8.2,Math.min(14.3,al));var y=red?1:0;if(r()<.08)y=1-y;a.push({x:[s,al],y:y});}return a;}
var WTR=wine(300,41),WTE=wine(300,42);
function gini(c){var n=c[0]+c[1];if(!n)return 0;var p=c[0]/n,q=c[1]/n;return 1-p*p-q*q;}
function counts(D){var c=[0,0];D.forEach(function(d){c[d.y]++;});return c;}
function bestSplit(D){var best={g:-1};[0,1].forEach(function(f){var s=D.slice().sort(function(a,b){return a.x[f]-b.x[f]}),L=[0,0],R=counts(D),n=D.length,g0=gini(R);for(var i=0;i<n-1;i++){L[s[i].y]++;R[s[i].y]--;if(s[i].x[f]===s[i+1].x[f])continue;var gl=gini(L),gr=gini(R),ig=g0-((i+1)*gl+(n-i-1)*gr)/n;if(ig>best.g)best={g:ig,f:f,t:(s[i].x[f]+s[i+1].x[f])/2};}});return best;}
function build(D,d,maxD,imp){var c=counts(D),node={c:c,n:D.length,cls:c[1]>c[0]?1:0};if(d>=maxD||D.length<2||!c[0]||!c[1])return node;var b=bestSplit(D);if(b.g<=0)return node;
  var L=D.filter(function(q){return q.x[b.f]<=b.t}),R=D.filter(function(q){return q.x[b.f]>b.t});imp[b.f]+=D.length*b.g;node.f=b.f;node.t=b.t;node.l=build(L,d+1,maxD,imp);node.r=build(R,d+1,maxD,imp);return node;}
function pred(nd,p){while(nd.l)nd=p[nd.f]<=nd.t?nd.l:nd.r;return nd.cls;}
function nLeaves(nd){return nd.l?nLeaves(nd.l)+nLeaves(nd.r):1;}
function scat(x,D,X0,Y0,Wd,Hh){var sx=function(v){return X0+(v-FR[0][0])/(FR[0][1]-FR[0][0])*Wd},sy=function(v){return Y0+Hh-(v-FR[1][0])/(FR[1][1]-FR[1][0])*Hh};D.forEach(function(d){x.fillStyle=d.y?C.eye:C.amber;x.beginPath();x.arc(sx(d.x[0]),sy(d.x[1]),2.8,0,7);x.fill();});
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,5,10,15,20].forEach(function(v){txt(x,v+'',sx(v),Y0+Hh+12,C.muted,10,'center');});[8,10,12,14].forEach(function(v){txt(x,v+'%',X0-4,sy(v),C.muted,10,'right');});txt(x,FN[0],X0+Wd/2,Y0+Hh+26,C.muted,11,'center');return {sx:sx,sy:sy};}

/* ---------- ② 지니 ---------- */
var f2=0,auto2=false;
LAB.radio('#ftBtns',[['0','잔당','ft0'],['1','알코올','ft1']],'0',function(v){f2=+v;auto2=false;draw2();});
LAB.radio('#bestBtns',[['hand','손으로','b0'],['best','최적 분할 찾기','b1']],'hand',function(v){if(v==='best'){var b=bestSplit(WTR);f2=b.f;$('#ft'+b.f).click();$('#th2').value=Math.round((b.t-FR[f2][0])/(FR[f2][1]-FR[f2][0])*100);auto2=b;}else auto2=false;draw2();});
$('#th2').addEventListener('input',function(){auto2=false;draw2();});
function draw2(){var t=auto2?auto2.t:FR[f2][0]+(+$('#th2').value)/100*(FR[f2][1]-FR[f2][0]);$('#th2v').textContent=t.toFixed(f2?1:1)+(f2?'%':'g/L');
  var L=WTR.filter(function(d){return d.x[f2]<=t}),R=WTR.filter(function(d){return d.x[f2]>t}),cA=counts(WTR),cL=counts(L),cR=counts(R),g0=gini(cA),gl=gini(cL),gr=gini(cR),gw=(L.length*gl+R.length*gr)/WTR.length;
  var c=$('#c2'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=46,Y0=20,Wd=(W-90)*.6,Hh=H-60,S=scat(x,WTR,X0,Y0,Wd,Hh);
  x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();if(f2===0){x.moveTo(S.sx(t),Y0);x.lineTo(S.sx(t),Y0+Hh);}else{x.moveTo(X0,S.sy(t));x.lineTo(X0+Wd,S.sy(t));}x.stroke();x.lineWidth=1;
  var X1=X0+Wd+30,W1=W-X1-14;function box(yy,lab,cc,g){var n=cc[0]+cc[1],bw=W1;txt(x,lab+' · '+n+'병 · 지니 '+g.toFixed(3),X1,yy,C.text,11,'left',700);if(n){x.fillStyle=C.eye;x.fillRect(X1,yy+8,bw*cc[1]/n,16);x.fillStyle=C.amber;x.fillRect(X1+bw*cc[1]/n,yy+8,bw*cc[0]/n,16);}txt(x,'레드 '+cc[1]+' · 화이트 '+cc[0],X1,yy+38,C.muted,10);}
  box(Y0+12,'분할 전',cA,g0);box(Y0+82,(f2?'알코올':'잔당')+' ≤ '+t.toFixed(1),cL,gl);box(Y0+152,(f2?'알코올':'잔당')+' > '+t.toFixed(1),cR,gr);
  txt(x,'● 레드(1)  ● 화이트(0)',X1,Y0+222,C.muted,11);stamp(x,W,'예시 데이터 · 300병');
  kpis($('#k2k'),[['m',g0.toFixed(3),'나누기 전 섞임(지니)'],['i',gw.toFixed(3),'나눈 뒤 섞임(지니)'],[auto2?'g':'a',(g0-gw).toFixed(3),'줄어든 섞임(정보 이득)'],['a',L.length+' : '+R.length,'왼쪽 : 오른쪽 병 수']]);
  $('#ins2').innerHTML=auto2?'<p class="g">최적 분할: '+FN[auto2.f]+' ≤ '+auto2.t.toFixed(2)+'. 불순도를 '+(g0-gw).toFixed(3)+'만큼 줄여, 두 특성의 어떤 기준값보다 큽니다. 이것이 나무의 뿌리 질문입니다.</p>':(g0-gw)<.02?'<p class="a">거의 줄지 않았습니다. 이 칸막이로는 양쪽이 여전히 섞여 있습니다.</p>':'<p class="g">불순도가 '+g0.toFixed(3)+' → '+gw.toFixed(3)+'로 줄었습니다. 더 큰 이득을 주는 자리가 있을까요?</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 깊이 ---------- */
var TREES={};function tree(d){if(TREES[d])return TREES[d];var imp=[0,0],t=build(WTR,0,d,imp);var tr=mean(WTR.map(function(q){return pred(t,q.x)===q.y?1:0})),te=mean(WTE.map(function(q){return pred(t,q.x)===q.y?1:0}));var s=imp[0]+imp[1]||1;return TREES[d]={t:t,tr:tr,te:te,imp:[imp[0]/s,imp[1]/s]};}
function rules(nd,pre,out,dep){if(!nd.l){out.push(pre.join(' 이고 ')+' → '+(nd.cls?'레드':'화이트')+' ('+nd.c[1]+':'+nd.c[0]+')');return;}var nm=nd.f?'알코올':'잔당',u=nd.f?'%':'g/L';rules(nd.l,pre.concat([nm+' ≤ '+nd.t.toFixed(1)+u]),out,dep+1);rules(nd.r,pre.concat([nm+' > '+nd.t.toFixed(1)+u]),out,dep+1);}
$('#dp').addEventListener('input',function(){$('#dpv').textContent=this.value;draw3();});
function draw3(){var d=+$('#dp').value,T=tree(d),c=$('#c3'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=46,Y0=20,Wd=(W-110)*.58,Hh=H-60;
  var GX=80,GY=50;for(var j=0;j<GY;j++)for(var i=0;i<GX;i++){var p=[FR[0][0]+(i+.5)/GX*(FR[0][1]-FR[0][0]),FR[1][0]+(j+.5)/GY*(FR[1][1]-FR[1][0])];x.fillStyle=pred(T.t,p)?'rgba(240,96,77,.18)':'rgba(241,182,70,.12)';x.fillRect(X0+i*Wd/GX,Y0+Hh-(j+1)*Hh/GY,Wd/GX+.5,Hh/GY+.5);}
  scat(x,WTE,X0,Y0,Wd,Hh);txt(x,'시험 300병 위에 그린 결정 영역',X0,Y0-6,C.text,11,'left',700);
  var X1=X0+Wd+50,W1=W-X1-16,sx=function(q){return X1+(q-1)/9*W1},sy=function(v){return Y0+Hh-(v-.6)/.4*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[.6,.8,1].forEach(function(v){txt(x,Math.round(v*100)+'%',X1-4,sy(v),C.muted,10,'right');});
  [['tr',C.info,'훈련'],['te',C.gfp,'시험']].forEach(function(s,k){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();for(var q=1;q<=10;q++){var v=tree(q)[s[0]];q>1?x.lineTo(sx(q),sy(v)):x.moveTo(sx(q),sy(v));}x.stroke();x.lineWidth=1;txt(x,'— '+s[2],X1+6+k*50,Y0+12,s[1],11,'left',700);});
  for(var q=1;q<=10;q+=3)txt(x,'깊이 '+q,sx(q),Y0+Hh+12,C.muted,10,'center');x.setLineDash([3,3]);x.strokeStyle=C.text;x.beginPath();x.moveTo(sx(d),Y0);x.lineTo(sx(d),Y0+Hh);x.stroke();x.setLineDash([]);
  stamp(x,W,'예시 데이터');var bestD=1;for(q=2;q<=10;q++)if(tree(q).te>tree(bestD).te)bestD=q;
  kpis($('#k3k'),[['i',pct(T.tr,1),'훈련 정확도'],[T.te<tree(bestD).te-.02?'r':'g',pct(T.te,1),'시험 정확도'],['a',nLeaves(T.t)+'개','마지막 칸 수(잎)'],['m','잔당 '+pct(T.imp[0],0)+' · 알코올 '+pct(T.imp[1],0),'재료별 중요도']]);
  var R=[];rules(T.t,[],R,0);$('#rules3').textContent=d<=3?R.map(function(r){return 'if '+r}).join('\n'):'(깊이 '+d+': 규칙 '+R.length+'개 — 사람이 읽기에는 너무 많습니다)';
  $('#ins3').innerHTML=d>=7?'<p class="r">깊이 '+d+': 훈련 '+pct(T.tr,1)+', 시험 '+pct(T.te,1)+'. 일부러 섞어 둔 라벨 잡음(약 8%)까지 외우느라 잎이 '+nLeaves(T.t)+'개로 늘었습니다.</p>':d===bestD?'<p class="g">깊이 '+d+'에서 시험 정확도가 가장 높습니다('+pct(T.te,1)+'). 이 근처가 가지치기의 균형점입니다.</p>':'<p class="a">깊이 '+d+': 훈련 '+pct(T.tr,1)+', 시험 '+pct(T.te,1)+'. 시험 곡선의 꼭대기는 깊이 '+bestD+'입니다.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- 농어: 다항 특성 + 규제 ---------- */
var PL=[8.4,13.7,15.0,16.2,17.4,18.0,18.7,19.0,19.6,20.0,21.0,21.0,21.0,21.3,22.0,22.0,22.0,22.0,22.0,22.5,22.5,22.7,23.0,23.5,24.0,24.0,24.6,25.0,25.6,26.5,27.3,27.5,27.5,27.5,28.0,28.7,30.0,32.8,34.5,35.0,36.5,36.0,37.0,37.0,39.0,39.0,39.0,40.0,40.0,40.0,40.0,42.0,43.0,43.0,43.5,44.0];
var PW=[5.9,32.0,40.0,51.5,70.0,100.0,78.0,80.0,85.0,85.0,110.0,115.0,125.0,130.0,120.0,120.0,130.0,135.0,110.0,130.0,150.0,145.0,150.0,170.0,225.0,145.0,188.0,180.0,197.0,218.0,300.0,260.0,265.0,250.0,250.0,300.0,320.0,514.0,556.0,840.0,685.0,700.0,700.0,690.0,900.0,650.0,820.0,850.0,900.0,1015.0,820.0,1100.0,1000.0,1100.0,1000.0,1000.0];
var TEI=[0,5,33,13,19,50,36,26,44,12,54,3,34,30],TRI=[];for(var i=0;i<56;i++)if(TEI.indexOf(i)<0)TRI.push(i);
var XTR=TRI.map(function(i){return PL[i]}),YTR=TRI.map(function(i){return PW[i]}),XTE=TEI.map(function(i){return PL[i]}),YTE=TEI.map(function(i){return PW[i]});
function r2(y,p){var m=mean(y),a=0,b=0;y.forEach(function(v,i){a+=(v-p[i])*(v-p[i]);b+=(v-m)*(v-m);});return 1-a/b;}
function rmse(y,p){return Math.sqrt(mean(y.map(function(v,i){return (v-p[i])*(v-p[i])})));}
/* PolynomialFeatures(include_bias=False) → StandardScaler(훈련 기준) */
function polyPrep(d){var raw=function(x){var r=[];for(var q=1;q<=d;q++)r.push(Math.pow(x,q));return r;},R=XTR.map(raw),mu=[],sd=[];for(var j=0;j<d;j++){var col=R.map(function(r){return r[j]}),m=mean(col);mu.push(m);sd.push(Math.sqrt(mean(col.map(function(v){return (v-m)*(v-m)}))));}
  var tf=function(x){return raw(x).map(function(v,j){return (v-mu[j])/sd[j]})};return {tf:tf,X:XTR.map(tf)};}
/* 하우스홀더 QR 최소제곱 */
function lstsq(A,b){var m=A.length,n=A[0].length,Q=A.map(function(r){return r.slice()}),y=b.slice();for(var k=0;k<n;k++){var s=0;for(var i=k;i<m;i++)s+=Q[i][k]*Q[i][k];var nrm=Math.sqrt(s),a=Q[k][k]>0?-nrm:nrm,v=[];for(i=0;i<m;i++)v.push(i<k?0:Q[i][k]);v[k]-=a;var vv=0;for(i=k;i<m;i++)vv+=v[i]*v[i];if(vv<1e-300)continue;
  for(var j=k;j<n;j++){var d=0;for(i=k;i<m;i++)d+=v[i]*Q[i][j];d=2*d/vv;for(i=k;i<m;i++)Q[i][j]-=d*v[i];}var dy=0;for(i=k;i<m;i++)dy+=v[i]*y[i];dy=2*dy/vv;for(i=k;i<m;i++)y[i]-=dy*v[i];}
  var w=new Array(n).fill(0);for(k=n-1;k>=0;k--){var s2=y[k];for(j=k+1;j<n;j++)s2-=Q[k][j]*w[j];w[k]=s2/Q[k][k];}return w;}
var YM=mean(YTR),YC=YTR.map(function(v){return v-YM});
function fitPlain(P){var w=lstsq(P.X,YC);return {w:w,b:YM,f:function(x){var z=P.tf(x);return YM+z.reduce(function(s,v,j){return s+v*w[j]},0)}};}
function fitRidge(P,al,X,Y){X=X||P.X;Y=Y||YTR;var ym=mean(Y),xm=X[0].map(function(_,j){return mean(X.map(function(r){return r[j]}))}),Xc=X.map(function(r){return r.map(function(v,j){return v-xm[j]})}),yc=Y.map(function(v){return v-ym}),p=xm.length,sq=Math.sqrt(al);
  var A=Xc.concat(xm.map(function(_,j){var r=new Array(p).fill(0);r[j]=sq;return r;})),bb=yc.concat(new Array(p).fill(0)),w=lstsq(A,bb),b=ym-xm.reduce(function(s,v,j){return s+v*w[j]},0);return {w:w,b:b,f:function(x){var z=P.tf(x);return b+z.reduce(function(s,v,j){return s+v*w[j]},0)}};}
function fitLasso(P,al){var X=P.X,n=X.length,p=X[0].length,w=new Array(p).fill(0),r=YC.slice(),nn=X[0].map(function(_,j){return X.reduce(function(s,row){return s+row[j]*row[j]},0)/n});
  for(var it=0;it<60000;it++){var mx=0;for(var j=0;j<p;j++){var rho=0;for(var i=0;i<n;i++)rho+=X[i][j]*(r[i]+X[i][j]*w[j]);rho/=n;var nw=Math.sign(rho)*Math.max(0,Math.abs(rho)-al)/nn[j],dw=nw-w[j];if(dw){for(i=0;i<n;i++)r[i]-=X[i][j]*dw;w[j]=nw;mx=Math.max(mx,Math.abs(dw));}}if(mx<1e-7)break;}
  return {w:w,b:YM,f:function(x){var z=P.tf(x);return YM+z.reduce(function(s,v,j){return s+v*w[j]},0)}};}
var PP={};function prep(d){return PP[d]||(PP[d]=polyPrep(d));}
var PLN={};function plain(d){return PLN[d]||(PLN[d]=fitPlain(prep(d)));}
function maxAbs(w){return Math.max.apply(0,w.map(Math.abs));}
function sens(f){var m=0,at=0;for(var x=13.7;x<=44;x+=.1){var d=Math.abs(f(x+.1)-f(x));if(d>m){m=d;at=x;}}return {d:m,at:at};}
$('#heroCoef').textContent=fmtN(maxAbs(plain(8).w));

/* ---------- ④ 특성공학 ---------- */
function binom(n,k){var r=1;for(var i=1;i<=k;i++)r=r*(n-k+i)/i;return Math.round(r);}
['nf','dg4'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#nfv').textContent=$('#nf').value;$('#dg4v').textContent=$('#dg4').value;draw4();});});
function draw4(){var n=+$('#nf').value,d=+$('#dg4').value,cnt=binom(n+d,d)-1,c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=40,Y0=24,Wd=(W-110)*.38,Hh=H-60,bw=Wd/8,lg=function(v){return Y0+Hh-Math.log10(Math.max(1,v))/4*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[1,10,100,1000,10000].forEach(function(v){txt(x,v.toLocaleString('ko-KR'),X0-4,lg(v),C.muted,9,'right');});
  for(var q=1;q<=8;q++){var v=binom(n+q,q)-1;x.fillStyle=q===d?C.amber:'rgba(241,182,70,.35)';x.fillRect(X0+(q-1)*bw+2,lg(v),bw-4,Y0+Hh-lg(v));txt(x,String(q),X0+(q-.5)*bw,Y0+Hh+12,C.muted,10,'center');}
  txt(x,'특성 '+n+'개의 degree별 특성 수(로그 눈금)',X0,Y0-8,C.text,11,'left',700);
  var M=plain(d),X1=X0+Wd+56,W1=W-X1-16,ymin=-400,ymax=1400,sx=function(v){return X1+v/50*W1},sy=function(v){return Y0+Hh-(v-ymin)/(ymax-ymin)*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[0,500,1000].forEach(function(v){txt(x,v+'g',X1-4,sy(v),C.muted,9,'right');});[10,20,30,40].forEach(function(v){txt(x,v+'cm',sx(v),Y0+Hh+12,C.muted,9,'center');});
  x.save();x.beginPath();x.rect(X1,Y0,W1,Hh);x.clip();x.strokeStyle=C.eye;x.lineWidth=2;x.beginPath();for(var l=6;l<=48;l+=.2){var p=M.f(l);l>6?x.lineTo(sx(l),sy(p)):x.moveTo(sx(l),sy(p));}x.stroke();x.lineWidth=1;
  XTR.forEach(function(v,i){x.fillStyle=C.info;x.beginPath();x.arc(sx(v),sy(YTR[i]),2.8,0,7);x.fill();});XTE.forEach(function(v,i){x.fillStyle=C.amber;x.beginPath();x.arc(sx(v),sy(YTE[i]),3.2,0,7);x.fill();});x.restore();
  txt(x,'농어 길이 '+d+'차 · 규제 없음',X1,Y0-8,C.text,11,'left',700);stamp(x,W,'교안 데이터');
  var S=sens(M.f),te=r2(YTE,XTE.map(M.f));
  kpis($('#k4k'),[['a',cnt.toLocaleString('ko-KR')+'개','특성 '+n+'개 · '+d+'차 → 새 특성 수'],['r',fmtN(maxAbs(M.w)),'가장 큰 계수 |w|(농어 '+d+'차)'],['m',S.d.toFixed(1)+'g','0.1cm 차이에 예측이 가장 크게 변하는 폭'],[te<.9?'r':'g',te.toFixed(3),'시험 데이터 설명력(R²)']]);
  $('#ins4').innerHTML=d>=6?'<p class="r">'+d+'차: 계수 절댓값이 '+fmtN(maxAbs(M.w))+'까지 커졌고, 시험 R²는 '+te.toFixed(2)+'입니다. 계수들이 서로 거대한 값으로 상쇄하며 겨우 균형을 맞추고 있어, 범위 끝에서 곡선이 튑니다.</p>':'<p class="g">특성 '+n+'개를 '+d+'차로 늘리면 '+cnt.toLocaleString('ko-KR')+'개. 농어 '+d+'차 회귀의 가장 큰 계수는 '+fmtN(maxAbs(M.w))+', 시험 R² '+te.toFixed(3)+'.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ 릿지·라쏘 ---------- */
var ALS=[.001,.01,.1,1,10,100],rg='ridge',RG={};
function reg(kind,a){var k=kind+a;if(RG[k])return RG[k];var P=prep(8);return RG[k]=kind==='none'?plain(8):kind==='ridge'?fitRidge(P,a):fitLasso(P,a);}
LAB.radio('#rgBtns',[['none','없음','g0'],['ridge','릿지','g1'],['lasso','라쏘','g2']],'ridge',function(v){rg=v;draw5();});
$('#al').addEventListener('input',function(){$('#alv').textContent=ALS[+this.value];draw5();});
function draw5(){var a=ALS[+$('#al').value],M=reg(rg,a),c=$('#c5'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=50,Y0=24,Wd=(W-110)*.55,Hh=H-60,ymin=-400,ymax=1400,sx=function(v){return X0+v/50*Wd},sy=function(v){return Y0+Hh-(v-ymin)/(ymax-ymin)*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,500,1000].forEach(function(v){txt(x,v+'g',X0-4,sy(v),C.muted,9,'right');});[10,20,30,40].forEach(function(v){txt(x,v+'cm',sx(v),Y0+Hh+12,C.muted,9,'center');});
  x.save();x.beginPath();x.rect(X0,Y0,Wd,Hh);x.clip();x.strokeStyle=rg==='none'?C.eye:C.gfp;x.lineWidth=2;x.beginPath();for(var l=6;l<=48;l+=.2){var p=M.f(l);l>6?x.lineTo(sx(l),sy(p)):x.moveTo(sx(l),sy(p));}x.stroke();x.lineWidth=1;
  XTR.forEach(function(v,i){x.fillStyle=C.info;x.beginPath();x.arc(sx(v),sy(YTR[i]),2.8,0,7);x.fill();});XTE.forEach(function(v,i){x.fillStyle=C.amber;x.beginPath();x.arc(sx(v),sy(YTE[i]),3.2,0,7);x.fill();});x.restore();
  var X1=X0+Wd+40,W1=W-X1-16,zy=Y0+Hh/2,mx=rg==='none'?maxAbs(M.w):Math.max(400,maxAbs(M.w)),bw=W1/8;x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);x.beginPath();x.moveTo(X1,zy);x.lineTo(X1+W1,zy);x.stroke();
  M.w.forEach(function(w,j){var h=w/mx*(Hh/2-6);x.fillStyle=Math.abs(w)<1e-6?C.muted:w>0?C.info:C.eye;x.fillRect(X1+j*bw+3,Math.min(zy,zy-h),bw-6,Math.abs(h)||1);txt(x,'x'+(j?'^'+(j+1):''),X1+(j+.5)*bw,Y0+Hh+12,C.muted,9,'center');if(Math.abs(w)<1e-6)txt(x,'0',X1+(j+.5)*bw,zy-8,C.muted,10,'center',700);});
  txt(x,'계수 8개 (막대 높이 기준 ±'+fmtN(mx)+')',X1,Y0-8,C.text,11,'left',700);stamp(x,W,'교안 데이터');
  var tr=r2(YTR,XTR.map(M.f)),te=r2(YTE,XTE.map(M.f)),nz=M.w.filter(function(w){return Math.abs(w)>1e-6}).length;
  kpis($('#k5k'),[['i',tr.toFixed(4),'공부 데이터 설명력(R²)'],[te<.9?'r':'g',te.toFixed(4),'시험 데이터 설명력(R²)'],['a',fmtN(maxAbs(M.w)),'가장 큰 계수 크기'],['m',nz+' / 8','남은 재료(0이 아닌 계수)']]);
  $('#ins5').innerHTML=rg==='none'?'<p class="r">규제 없음: 훈련 R² '+tr.toFixed(4)+'로 가장 높지만 시험 R²는 '+te.toFixed(2)+'. 계수 '+fmtN(maxAbs(M.w))+'짜리 곡선이 8.4cm 농어에서 크게 빗나갑니다.</p>':a>=100?'<p class="a">α = '+a+': 고삐가 너무 셉니다. 훈련 '+tr.toFixed(3)+', 시험 '+te.toFixed(3)+'로 둘 다 내려갔습니다(과소적합).</p>':rg==='lasso'?'<p class="g">라쏘 α = '+a+': 계수 '+(8-nz)+'개가 정확히 0이 되어 특성 '+nz+'개만 남았습니다. 시험 R² '+te.toFixed(3)+'.</p>':'<p class="g">릿지 α = '+a+': 특성 8개를 모두 쓰되 가장 큰 계수가 '+fmtN(maxAbs(M.w))+'로 줄었습니다. 시험 R² '+te.toFixed(3)+'.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결: 교차 검증으로 고른 릿지 vs 규제 없음 ---------- */
function cvRidge(){var P=prep(8),idx=XTR.map(function(_,i){return i}),r=rng(0);for(var i=idx.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t;}
  var best=null;ALS.forEach(function(a){var sc=[];for(var k=0;k<5;k++){var va=idx.filter(function(_,q){return q%5===k}),tr=idx.filter(function(_,q){return q%5!==k}),M=fitRidge(P,a,tr.map(function(q){return P.X[q]}),tr.map(function(q){return YTR[q]}));sc.push(r2(va.map(function(q){return YTR[q]}),va.map(function(q){return M.f(XTR[q])})));}var m=mean(sc);if(!best||m>best.cv)best={a:a,cv:m};});return best;}
LAB.Duel({el:'#duelBox',higherIsBetter:false,drawMargin:1,metric:'시험 농어 14마리 RMSE(g) — 작을수록 좋음',fmt:function(v){return Math.round(v).toLocaleString('ko-KR')+'g'},
  run:function(){var b=cvRidge(),F=fitRidge(prep(8),b.a),R=plain(8),fr=rmse(YTE,XTE.map(F.f)),rr=rmse(YTE,XTE.map(R.f));this.max=Math.max(fr,rr)*1.05;this.bigGap=1e9;this.info={a:b.a,cv:b.cv,trF:r2(YTR,XTR.map(F.f)),trR:r2(YTR,XTR.map(R.f)),p84F:F.f(8.4),p84R:R.f(8.4)};return {fly:fr,robo:rr};},
  report:function(r){var I=this.info;return '교차 검증이 고른 α는 '+I.a+'(검증 R² 평균 '+I.cv.toFixed(3)+')예요. 훈련 R²는 주판봇 '+I.trR.toFixed(4)+', 초파리 '+I.trF.toFixed(4)+'로 주판봇이 조금 높았지만, 8.4cm 농어(실제 5.9g)를 초파리는 '+Math.round(I.p84F)+'g, 주판봇은 '+fmtN(I.p84R)+'g으로 예측했어요.';},
  verdict:function(r,res){return '훈련 점수는 시험 점수가 아니다. 특성을 늘렸으면 계수에 고삐를. '+(res==='F'?'초파리 승.':res==='R'?'주판봇 승.':'이번 판은 나눠 갖는다.');}});
