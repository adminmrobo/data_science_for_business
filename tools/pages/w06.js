/* 6주차 · 분류모형(2) — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,F=LAB.FONT,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
var BL=[25.4,26.3,26.5,29.0,29.0,29.7,29.7,30.0,30.0,30.7,31.0,31.0,31.5,32.0,32.0,32.0,33.0,33.0,33.5,33.5,34.0,34.0,34.5,35.0,35.0,35.0,35.0,36.0,36.0,37.0,38.5,38.5,39.5,41.0,41.0];
var BW=[242,290,340,363,430,450,500,390,450,500,475,500,500,340,600,600,700,700,610,650,575,685,620,680,700,725,720,714,850,1000,920,955,925,975,950];
var SL=[9.8,10.5,10.6,11.0,11.2,11.3,11.8,11.8,12.0,12.2,12.4,13.0,14.3,15.0],SW=[6.7,7.5,7.0,9.7,9.8,8.7,10.0,9.9,9.8,12.2,13.4,12.2,19.7,19.9];
var PL=[15.2,16.8,17.5,18.3,19.1,20.4,21.7,22.3,23.6,24.1],PW=[52.3,68.7,74.2,85.6,92.4,108.5,125.3,132.8,145.2,158.7];
/* 2클래스(교안 5주차 라벨: 도미 1, 빙어 0) */
var X2=BL.map(function(l,i){return [l,BW[i]]}).concat(SL.map(function(l,i){return [l,SW[i]]})),Y2=BL.map(function(){return 1}).concat(SL.map(function(){return 0}));
var NAMES=['도미','농어','빙어'],COL3=[C.info,C.amber,C.eye];
function knnPred(X,Y,q,k,ncls){var d=X.map(function(p,i){var dx=p[0]-q[0],dy=p[1]-q[1];return [dx*dx+dy*dy,i]}).sort(function(a,b){return a[0]-b[0]}).slice(0,k);var v=new Array(ncls).fill(0);d.forEach(function(t){v[Y[t[1]]]++;});
  var best=0;for(var c=1;c<ncls;c++)if(v[c]>v[best])best=c;return {nb:d,votes:v,pred:best};}
function zfit(X){var m=[0,1].map(function(j){return LAB.mean(X.map(function(p){return p[j]}))}),s=[0,1].map(function(j){var mm=m[j];return Math.sqrt(LAB.mean(X.map(function(p){return (p[j]-mm)*(p[j]-mm)})))});return {m:m,s:s,t:function(p){return [(p[0]-m[0])/s[0],(p[1]-m[1])/s[1]]}};}
function mmfit(X){var lo=[0,1].map(function(j){return Math.min.apply(0,X.map(function(p){return p[j]}))}),hi=[0,1].map(function(j){return Math.max.apply(0,X.map(function(p){return p[j]}))});return {lo:lo,hi:hi,t:function(p){return [(p[0]-lo[0])/(hi[0]-lo[0]),(p[1]-lo[1])/(hi[1]-lo[1])]}};}
function rawAxes(x,X0,Y0,Wd,Hh,maxL,maxW){x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);for(var v=0;v<=maxW;v+=250)txt(x,v+'g',X0-4,Y0+Hh-v/1100*Hh,C.muted,10,'right');for(var l=0;l<=maxL;l+=10)txt(x,l+'cm',X0+l/45*Wd,Y0+Hh+12,C.muted,10,'center');}
function star(x,px,py,col){x.fillStyle=col||C.gfp;x.beginPath();for(var a=0;a<10;a++){var rr=a%2?4:10,an=-Math.PI/2+a*Math.PI/5;x.lineTo(px+rr*Math.cos(an),py+rr*Math.sin(an));}x.closePath();x.fill();}
function legend(x,items,X,Y){var cx=X;items.forEach(function(it){x.fillStyle=it[1];x.beginPath();x.arc(cx+4,Y,4,0,7);x.fill();txt(x,it[0],cx+12,Y,C.muted,11);cx+=x.measureText(it[0]).width+30;});}

/* ---------- 히어로 소품: 수조 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var tx=W*.34,ty=H*.14,tw=W*.4,th=H*.34;x.fillStyle='rgba(130,184,255,.12)';x.fillRect(tx,ty,tw,th);x.strokeStyle='#4a6fa8';x.lineWidth=3;x.strokeRect(tx,ty,tw,th);x.lineWidth=1;
  function fish(cx,cy,s,col,dir){x.fillStyle=col;x.beginPath();x.ellipse(cx,cy,s,s*.45,0,0,7);x.fill();x.beginPath();x.moveTo(cx-dir*s*.9,cy);x.lineTo(cx-dir*s*1.4,cy-s*.4);x.lineTo(cx-dir*s*1.4,cy+s*.4);x.fill();}
  fish(tx+tw*(.3+.1*Math.sin(t*.6)),ty+th*.35,W*.04,C.info,1);fish(tx+tw*(.65-.1*Math.sin(t*.8)),ty+th*.6,W*.025,C.amber,-1);fish(tx+tw*(.45+.15*Math.sin(t*1.1)),ty+th*.8,W*.012,C.eye,1);
  x.strokeStyle=C.gfp;x.lineWidth=2;x.beginPath();x.arc(W*.86,H*.25,W*.05,0,7);x.stroke();x.lineWidth=1;});

/* ---------- ① 3클래스 KNN ---------- */
var X3=BL.map(function(l,i){return [l,BW[i]]}).concat(PL.map(function(l,i){return [l,PW[i]]}),SL.map(function(l,i){return [l,SW[i]]})),Y3=BL.map(function(){return 0}).concat(PL.map(function(){return 1}),SL.map(function(){return 2}));
var Q1=[21,140],G1={};
$('#k1').addEventListener('input',function(){$('#k1v').textContent=this.value;draw1();});
$('#c1').addEventListener('click',function(e){var r=this.getBoundingClientRect();if(!G1.Wd)return;Q1=[Math.round(Math.max(5,Math.min(44,(e.clientX-r.left-G1.X0)/G1.Wd*45))*10)/10,Math.round(Math.max(0,Math.min(1100,(G1.Y0+G1.Hh-(e.clientY-r.top))/G1.Hh*1100)))];draw1();});
function draw1(){var k=+$('#k1').value,R=knnPred(X3,Y3,Q1,k,3),c=$('#c1'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-90,Hh=H-60;G1={X0:X0,Y0:Y0,Wd:Wd,Hh:Hh};
  var sx=function(v){return X0+v/45*Wd},sy=function(v){return Y0+Hh-v/1100*Hh};rawAxes(x,X0,Y0,Wd,Hh,40,1000);
  R.nb.forEach(function(t){var p=X3[t[1]];x.strokeStyle='rgba(241,182,70,.7)';x.beginPath();x.moveTo(sx(Q1[0]),sy(Q1[1]));x.lineTo(sx(p[0]),sy(p[1]));x.stroke();});
  X3.forEach(function(p,i){x.fillStyle=COL3[Y3[i]];x.beginPath();x.arc(sx(p[0]),sy(p[1]),3.5,0,7);x.fill();});
  star(x,sx(Q1[0]),sy(Q1[1]));txt(x,'['+Q1[0]+', '+Q1[1]+'] → '+NAMES[R.pred],sx(Q1[0])+12,sy(Q1[1])-12,C.gfp,12,'left',700);
  legend(x,[['도미(0)',C.info],['농어(1)',C.amber],['빙어(2)',C.eye]],X0+8,Y0+12);stamp(x,W,'교안 데이터 · 그림을 눌러 옮기기');
  kpis($('#k1k'),[['g',NAMES[R.pred],'판정'],['i',R.votes.join(' · '),'투표 (도미·농어·빙어)'],['a','['+R.votes.map(function(v){return (v/k).toFixed(2)}).join(', ')+']','확률'],['m',pct(1,0),'학습 데이터 정확도']]);
  var mx=Math.max.apply(0,R.votes);$('#ins1').innerHTML=mx===k?'<p class="g">이웃 '+k+'마리가 모두 '+NAMES[R.pred]+'입니다.</p>':'<p class="a">이웃이 갈렸습니다('+R.votes.map(function(v,i){return NAMES[i]+' '+v}).join(', ')+'). 가장 많은 '+NAMES[R.pred]+'로 정했지만 확신은 '+(mx/k*100).toFixed(0)+'%입니다.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② K 최적화 ---------- */
function blobs(n,seed){var r=rng(seed),a=[];for(var i=0;i<n;i++){var c=i%2;a.push({p:[(c?.5:-.5)+gauss(r),gauss(r)*1.0],c:c});}return a;}
var NTR=blobs(200,5),NTE=blobs(200,6),KC={};
function nAcc(k,S){var ok=0;S.forEach(function(s){var R=knnPred(NTR.map(function(t){return t.p}),NTR.map(function(t){return t.c}),s.p,k,2);if(R.pred===s.c)ok++;});return ok/S.length;}
function kAcc(k){if(!KC[k])KC[k]=[nAcc(k,NTR),nAcc(k,NTE)];return KC[k];}
var K2S=[1,3,5,7,9,11,15,19,25,31,41,51];
$('#k2').addEventListener('input',function(){$('#k2v').textContent=this.value;draw2();});
function draw2(){var k=+$('#k2').value,c=$('#c2'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=30,Y0=24,Wd=(W-100)/2,Hh=H-50,sx=function(v){return X0+(v+3.5)/7*Wd},sy=function(v){return Y0+Hh-(v+3)/6*Hh};
  var TP=NTR.map(function(t){return t.p}),TC=NTR.map(function(t){return t.c});
  for(var j=0;j<30;j++)for(var i=0;i<40;i++){var q=[-3.5+7*(i+.5)/40,-3+6*(j+.5)/30];x.fillStyle=knnPred(TP,TC,q,k,2).pred?'rgba(130,184,255,.16)':'rgba(240,96,77,.12)';x.fillRect(X0+i*Wd/40,Y0+Hh-(j+1)*Hh/30,Wd/40+.5,Hh/30+.5);}
  NTR.forEach(function(t){x.fillStyle=t.c?C.info:C.eye;x.beginPath();x.arc(sx(t.p[0]),sy(t.p[1]),2.5,0,7);x.fill();});x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);txt(x,'K = '+k+' 결정 영역 (훈련 200)',X0,14,C.info,12,'left',700);
  var X1=X0+Wd+50,W1=W-X1-20,kx=function(kk){return X1+(kk-1)/50*W1},ky=function(v){return Y0+Hh-(v-.5)/.5*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[.5,.6,.7,.8,.9,1].forEach(function(v){txt(x,Math.round(v*100)+'%',X1-4,ky(v),C.muted,10,'right');});
  [[0,C.amber],[1,C.gfp]].forEach(function(s){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();K2S.forEach(function(kk,i){var v=kAcc(kk)[s[0]];i?x.lineTo(kx(kk),ky(v)):x.moveTo(kx(kk),ky(v));});x.stroke();x.lineWidth=1;});
  txt(x,'— 훈련',X1+6,Y0+12,C.amber,11,'left',700);txt(x,'— 시험',X1+60,Y0+12,C.gfp,11,'left',700);x.setLineDash([3,3]);x.strokeStyle=C.text;x.beginPath();x.moveTo(kx(k),Y0);x.lineTo(kx(k),Y0+Hh);x.stroke();x.setLineDash([]);
  [1,11,21,31,41,51].forEach(function(v){txt(x,'K='+v,kx(v),Y0+Hh+12,C.muted,10,'center');});
  stamp(x,W,'예시 데이터 · 설명용 모형');
  var A=kAcc(k),best=K2S.slice().sort(function(a,b){return kAcc(b)[1]-kAcc(a)[1]})[0];
  kpis($('#k2k'),[['a',pct(A[0],1),'훈련 정확도'],['g',pct(A[1],1),'시험 정확도'],['i','K = '+best,'시험 곡선의 최고점'],['r',((A[0]-A[1])*100).toFixed(1)+'%p','공부 점수 − 시험 점수']]);
  $('#ins2').innerHTML=k===1?'<p class="r">K = 1: 훈련 100%, 시험 '+pct(A[1],1)+'. 교안의 "K = 1일 때 약 60%"와 같은 모습입니다.</p>':k>=31?'<p class="a">K가 크면 경계가 뭉개져 시험 정확도가 내려갑니다.</p>':'<p class="g">K = '+k+': 훈련과 시험의 차이가 '+((A[0]-A[1])*100).toFixed(1)+'%p로 줄었습니다.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ SVM (커널 Pegasos, 단순화) ---------- */
var ZF=zfit(X2),FISHZ=X2.map(function(p,i){return {p:ZF.t(p),y:Y2[i]?1:-1}});
var RING=(function(){var r=rng(31),a=[];for(var i=0;i<140;i++){var inner=i%2===0,rad=inner?Math.sqrt(r())*.55:.85+r()*.45,an=r()*Math.PI*2;a.push({p:[rad*Math.cos(an)*1.6,rad*Math.sin(an)*1.6],y:inner?1:-1});}return a;})();
var GAM=[.1,.3,1,3,10],svD='ring',svK='rbf',SVC={};
function kern(a,b,ker,g){if(ker==='lin')return a[0]*b[0]+a[1]*b[1]+1;var dx=a[0]-b[0],dy=a[1]-b[1];return Math.exp(-g*(dx*dx+dy*dy));}
function train(D,ker,g){var key=svD+ker+g;if(SVC[key])return SVC[key];var lam=.005,T=5000,al=new Array(D.length).fill(0),r=rng(9);
  for(var t=1;t<=T;t++){var i=Math.floor(r()*D.length),s=0;for(var j=0;j<D.length;j++)if(al[j])s+=al[j]*D[j].y*kern(D[j].p,D[i].p,ker,g);if(D[i].y*s/(lam*t)<1)al[i]++;}
  var M={al:al,c:1/(lam*T),f:function(q){var s=0;for(var j=0;j<D.length;j++)if(al[j])s+=al[j]*D[j].y*kern(D[j].p,q,ker,g);return s*M.c;}};SVC[key]=M;return M;}
LAB.radio('#svData',[['fish','도미·빙어(표준화)','sd0'],['ring','원형 데이터(예시)','sd1']],'ring',function(v){svD=v;draw3();});
LAB.radio('#svKer',[['lin','선형','sk0'],['rbf','RBF','sk1']],'rbf',function(v){svK=v;draw3();});
$('#gm').addEventListener('input',function(){$('#gmv').textContent=GAM[+this.value];draw3();});
function draw3(){var D=svD==='fish'?FISHZ:RING,g=GAM[+$('#gm').value],M=train(D,svK,g),c=$('#c3'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);
  var lim=svD==='fish'?[-2.2,2.2,-1.8,2.2]:[-2.4,2.4,-2.4,2.4],X0=40,Y0=20,Hh=H-40,Wd=Math.min(W-80,Hh*1.6),sx=function(v){return X0+(v-lim[0])/(lim[1]-lim[0])*Wd},sy=function(v){return Y0+Hh-(v-lim[2])/(lim[3]-lim[2])*Hh};
  var GX=56,GY=36;for(var j=0;j<GY;j++)for(var i=0;i<GX;i++){var q=[lim[0]+(lim[1]-lim[0])*(i+.5)/GX,lim[2]+(lim[3]-lim[2])*(j+.5)/GY],f=M.f(q);x.fillStyle=Math.abs(f)<1?'rgba(241,182,70,.18)':f>0?'rgba(130,184,255,.16)':'rgba(240,96,77,.12)';x.fillRect(X0+i*Wd/GX,Y0+Hh-(j+1)*Hh/GY,Wd/GX+.5,Hh/GY+.5);}
  var ok=0,sv=0;D.forEach(function(d,i){var f=M.f(d.p);if((f>0?1:-1)===d.y)ok++;var isSV=M.al[i]>0&&Math.abs(f)<=1.05;if(isSV)sv++;x.fillStyle=d.y>0?C.info:C.eye;x.beginPath();x.arc(sx(d.p[0]),sy(d.p[1]),3.3,0,7);x.fill();if(isSV){x.strokeStyle=C.text;x.lineWidth=1.5;x.beginPath();x.arc(sx(d.p[0]),sy(d.p[1]),6,0,7);x.stroke();x.lineWidth=1;}});
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);var lx=X0+Wd+16;
  legend(x,svD==='fish'?[['도미',C.info],['빙어',C.eye]]:[['안쪽 고객',C.info],['바깥 고객',C.eye]],lx,Y0+14);txt(x,'노란 띠 = 여백(|f| < 1)',lx,Y0+32,C.amber,11);txt(x,'흰 테두리 = 서포트 벡터',lx,Y0+50,C.text,11);txt(x,'가로·세로: 표준화한 값',lx,Y0+68,C.muted,11);
  stamp(x,W,'단순화한 학습 규칙(커널 Pegasos)');
  var acc=ok/D.length;kpis($('#k3k'),[['g',pct(acc,1),'학습 데이터 정확도'],['i',sv+'개','경계를 정한 점(서포트 벡터)'],['a',svK==='lin'?'선형':'RBF · γ = '+g,'커널'],['m',D.length+'개','점 수']]);
  var msg='';if(svD==='ring'&&svK==='lin')msg='<p class="r">직선으로는 원을 가를 수 없습니다. 정확도 '+pct(acc,1)+'. RBF로 바꿔 보세요.</p>';
  else if(svD==='ring'&&g>=10)msg='<p class="a">γ = 10: 경계가 점 가까이 붙어 구불구불해집니다. 학습 데이터는 잘 맞히지만 새 점에는 불안합니다(과적합 경향).</p>';
  else if(svD==='ring'&&g<=.1)msg='<p class="a">γ = 0.1: 경계가 직선에 가까워져 원을 잘 감싸지 못합니다(과소적합 경향).</p>';
  else if(svD==='ring')msg='<p class="g">RBF 커널이 안쪽 고객을 둘러싸는 원 모양 경계를 만들었습니다. 정확도 '+pct(acc,1)+'.</p>';
  else msg='<p class="g">도미와 빙어는 표준화하면 '+(svK==='lin'?'직선 하나로':'곡선 경계로도')+' 넓은 여백을 두고 갈립니다. 서포트 벡터는 '+sv+'마리뿐입니다.</p>';
  $('#ins3').innerHTML=msg;}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 데이터 분할 ---------- */
var spK='seq';
LAB.radio('#spBtns',[['seq','순서대로','sp0'],['rand','무작위','sp1'],['strat','층화(stratify)','sp2']],'seq',function(v){spK=v;draw4();});
$('#seed').addEventListener('input',function(){$('#seedv').textContent=this.value;draw4();});
function shuffle(a,seed){var r=rng(seed),b=a.slice();for(var i=b.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=b[i];b[i]=b[j];b[j]=t;}return b;}
function split(kind,seed){var idx=X2.map(function(_,i){return i}),te;
  if(kind==='seq')te=idx.slice(36);else if(kind==='rand')te=shuffle(idx,seed).slice(0,13);
  else{var b=shuffle(idx.filter(function(i){return Y2[i]===1}),seed),s=shuffle(idx.filter(function(i){return Y2[i]===0}),seed+1000);te=b.slice(0,9).concat(s.slice(0,4));}
  var tr=idx.filter(function(i){return te.indexOf(i)<0});return {tr:tr,te:te};}
function splitAcc(S){var X=S.tr.map(function(i){return X2[i]}),Y=S.tr.map(function(i){return Y2[i]}),ok=0;S.te.forEach(function(i){if(knnPred(X,Y,X2[i],5,2).pred===Y2[i])ok++;});return ok/S.te.length;}
function draw4(){var seed=+$('#seed').value,S=split(spK,seed),acc=splitAcc(S),c=$('#c4'),W=fitC(c,220),H=220,x=c.getContext('2d');grid(x,W,H);
  var cw=(W-60)/49;X2.forEach(function(p,i){var inTe=S.te.indexOf(i)>=0,px=30+i*cw,py=inTe?140:50;x.fillStyle=Y2[i]?C.info:C.eye;x.fillRect(px,py,cw-2,34);});
  txt(x,'훈련 '+S.tr.length+'마리 (위)',30,38,C.text,12,'left',700);txt(x,'시험 '+S.te.length+'마리 (아래)',30,128,C.text,12,'left',700);txt(x,'0번(왼쪽) → 48번(오른쪽): 원래 입력 순서 · 파랑 도미, 빨강 빙어',30,H-14,C.muted,11);
  stamp(x,W,'교안 데이터');
  var trS=S.tr.filter(function(i){return !Y2[i]}).length,teS=S.te.filter(function(i){return !Y2[i]}).length;
  kpis($('#k4k'),[['i',(S.tr.length-trS)+' : '+trS,'훈련 도미 : 빙어'],['a',(S.te.length-teS)+' : '+teS,'시험 도미 : 빙어'],['m',pct(teS/S.te.length,0)+' (원본 '+pct(14/49,0)+')','시험의 빙어 비율'],[acc<.5?'r':acc<1?'a':'g',pct(acc,1),'이웃 5마리 모델의 시험 정답률']]);
  $('#splitOut').textContent=spK==='seq'?'>>> train_input, test_input = fish_data[:36], fish_data[36:]\n>>> kn.fit(train_input, train_target).score(test_input, test_target)\n'+acc.toFixed(1):
    '>>> from sklearn.model_selection import train_test_split\n>>> train_test_split(fish_data, fish_target, test_size=13'+(spK==='strat'?', stratify=fish_target':'')+', random_state='+seed+')\n>>> kn.score(test_input, test_target)\n'+acc.toFixed(4).replace(/0+$/,'').replace(/\.$/,'.0');
  $('#ins4').innerHTML=spK==='seq'?'<p class="r">훈련에는 빙어가 '+trS+'마리뿐, 시험은 전부 빙어입니다. 모델은 빙어를 모두 도미로 판정해 정확도 '+pct(acc,0)+'입니다.</p>':spK==='rand'?'<p class="a">무작위로 섞으니 두 종류가 다 들어갔습니다. 하지만 섞는 순서 번호에 따라 시험의 빙어가 '+teS+'마리로 원본 비율(약 '+pct(14/49,0)+')과 다를 수 있습니다.</p>':'<p class="g">층화 분할: 훈련과 시험 모두 빙어 비율이 원본과 거의 같습니다. 시험 정확도 '+pct(acc,0)+'.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ 표준화 ---------- */
var scK='raw',NF=[25,150];
LAB.radio('#scBtns',[['raw','원자료','sc0'],['z','Z-점수','sc1'],['mm','Min-Max','sc2']],'raw',function(v){scK=v;draw5();});
var MM=mmfit(X2);function tf(kind){return kind==='z'?ZF.t:kind==='mm'?MM.t:function(p){return p};}
function nbOf(kind,q,k){var t=tf(kind),X=X2.map(t);return knnPred(X,Y2,t(q),k,2);}
function draw5(){var R=nbOf(scK,NF,5),t=tf(scK),c=$('#c5'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var pw=(W-90)/2,Hh=H-60,Y0=28;
  /* 왼쪽: 원래 눈금 */
  var X0=56,sx=function(v){return X0+v/45*(pw-20)},sy=function(v){return Y0+Hh-v/1100*Hh};rawAxes(x,X0,Y0,pw-20,Hh,40,1000);
  X2.forEach(function(p,i){x.fillStyle=Y2[i]?C.info:C.eye;x.beginPath();x.arc(sx(p[0]),sy(p[1]),3,0,7);x.fill();});
  R.nb.forEach(function(tt){var p=X2[tt[1]];x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.arc(sx(p[0]),sy(p[1]),6,0,7);x.stroke();x.lineWidth=1;});star(x,sx(NF[0]),sy(NF[1]));
  txt(x,'원래 눈금(cm, g)에서 본 이웃',X0,16,C.text,12,'left',700);
  /* 오른쪽: 바꾼 눈금(정사각 비율) */
  var T=X2.map(t),q=t(NF),xs=T.map(function(p){return p[0]}).concat([q[0]]),ys=T.map(function(p){return p[1]}).concat([q[1]]);
  var lo0=Math.min.apply(0,xs),hi0=Math.max.apply(0,xs),lo1=Math.min.apply(0,ys),hi1=Math.max.apply(0,ys),span=Math.max(hi0-lo0,hi1-lo1)*1.1,cx0=(lo0+hi0)/2,cy0=(lo1+hi1)/2;
  var X1=X0+pw+30,side=Math.min(pw-20,Hh),bx=function(v){return X1+(v-cx0+span/2)/span*side},by=function(v){return Y0+side-(v-cy0+span/2)/span*side};
  x.strokeStyle=C.rule;x.strokeRect(X1,Y0,side,side);
  R.nb.forEach(function(tt){var p=T[tt[1]];x.strokeStyle='rgba(241,182,70,.7)';x.beginPath();x.moveTo(bx(q[0]),by(q[1]));x.lineTo(bx(p[0]),by(p[1]));x.stroke();});
  T.forEach(function(p,i){x.fillStyle=Y2[i]?C.info:C.eye;x.beginPath();x.arc(bx(p[0]),by(p[1]),3,0,7);x.fill();});star(x,bx(q[0]),by(q[1]));
  txt(x,(scK==='raw'?'원자료: KNN이 실제로 재는 거리(가로·세로 같은 비율)':scK==='z'?'Z-점수 눈금(가로·세로 같은 비율)':'Min-Max 눈금(가로·세로 같은 비율)'),X1,Y0+side+14,C.text,12,'left',700);
  stamp(x,W,'교안 데이터');
  var nB=R.votes[1];kpis($('#k5k'),[[R.pred?'g':'r',R.pred?'도미 (1)':'빙어 (0)','새 생선(25cm·150g) 판정'],['i','도미 '+nB+' · 빙어 '+(5-nB),'이웃 5마리'],['a','['+q[0].toFixed(2)+', '+q[1].toFixed(2)+']','눈금을 맞춘 새 생선'],['m',scK==='z'?'평균 ['+ZF.m[0].toFixed(1)+', '+ZF.m[1].toFixed(1)+'] · 표준편차 ['+ZF.s[0].toFixed(1)+', '+ZF.s[1].toFixed(1)+']':scK==='mm'?'최솟값·최댓값 기준':'—','눈금 기준(공부용 데이터)']]);
  $('#eq5').innerHTML=scK==='z'?'z<sub>길이</sub> = (25 − '+ZF.m[0].toFixed(1)+') ÷ '+ZF.s[0].toFixed(1)+' = <b>'+q[0].toFixed(2)+'</b>,  z<sub>무게</sub> = (150 − '+ZF.m[1].toFixed(1)+') ÷ '+ZF.s[1].toFixed(1)+' = <em>'+q[1].toFixed(2)+'</em>':scK==='mm'?'(값 − 최솟값) ÷ (최댓값 − 최솟값): 길이 <b>'+q[0].toFixed(2)+'</b>, 무게 <em>'+q[1].toFixed(2)+'</em>':'길이 차이 10cm와 무게 차이 10g이 같은 거리로 계산됩니다. 무게의 범위(6.7~1,000g)가 길이(9.8~41cm)보다 약 30배 넓습니다.';
  $('#ins5').innerHTML=scK==='raw'?'<p class="r">오른쪽 그림이 KNN이 보는 세상입니다. 가로(길이)가 거의 한 점으로 눌려, 무게만 비슷한 빙어 4마리가 가장 가까운 이웃이 됩니다. → 빙어.</p>':'<p class="g">눈금을 맞추자 길이 차이도 무게 차이만큼 중요해졌습니다. 이웃 5마리 중 도미 '+nB+'마리 → '+(R.pred?'도미':'빙어')+'.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});
$('#heroStd').textContent=nbOf('z',NF,5).pred?'도미':'빙어';

/* ---------- 대결: 새로 잡힌 생선 30마리 ---------- */
var NEWF=(function(){var r=rng(17),a=[];for(var i=0;i<10;i++){var j=Math.floor(r()*35);a.push({p:[BL[j]*(1+(r()-.5)*.06),BW[j]*(1+(r()-.5)*.16)],y:1});}
  for(i=0;i<10;i++){j=Math.floor(r()*14);a.push({p:[SL[j]*(1+(r()-.5)*.08),SW[j]*(1+(r()-.5)*.2)],y:0});}
  for(i=0;i<10;i++)a.push({p:[24+r()*3,130+r()*100],y:1});return a;})();
function duelAcc(kind){var ok=0,young=0;NEWF.forEach(function(f,i){var R=nbOf(kind,f.p,5);if(R.pred===f.y){ok++;if(i>=20)young++;}});return {acc:ok/NEWF.length,young:young};}
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.001,max:1,metric:'새로 잡힌 생선 30마리를 맞힌 비율',fmt:function(v){return pct(v,1)},
  run:function(){var a=duelAcc('z'),b=duelAcc('raw');this.ya=a.young;this.yb=b.young;return {fly:a.acc,robo:b.acc};},
  report:function(r){return '표준화한 쪽은 30마리 중 '+Math.round(r.fly*30)+'마리, 원자료 쪽은 '+Math.round(r.robo*30)+'마리를 맞혔어요. 어린 도미 10마리만 보면 '+this.ya+'마리 대 '+this.yb+'마리예요.';},
  verdict:function(r,res){return '거리를 재는 모델은 눈금이 공정해야 한다. '+(res==='F'?'초파리 승.':res==='R'?'주판봇 승.':'이번 판은 나눠 갖는다.');}});
