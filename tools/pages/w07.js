/* 7주차 · 모델의 평가 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
var sig=function(z){return 1/(1+Math.exp(-z))};
/* 예시 고객: 특성 x1(이용 감소율), x2(불만 문의), 이탈 확률 = sigmoid(c + 1.6x1 + 1.0x2) */
var CC={};function cfor(rate){if(CC[rate]!=null)return CC[rate];var lo=-10,hi=5;for(var it=0;it<40;it++){var m=(lo+hi)/2,r=rng(1),s=0;for(var i=0;i<4000;i++)s+=sig(m+1.6*gauss(r)+1.0*gauss(r));if(s/4000<rate)lo=m;else hi=m;}return CC[rate]=(lo+hi)/2;}
function gen(n,rate,seed){var c=cfor(rate),r=rng(seed),a=[];for(var i=0;i<n;i++){var x1=gauss(r),x2=gauss(r),p=sig(c+1.6*x1+1.0*x2);a.push({x:[x1,x2],p:p,w:sig(c*0.9+0.9*x1),y:r()<p?1:0});}return a;}
function cm(D,t,k){var m={tp:0,fp:0,fn:0,tn:0};k=k||'p';D.forEach(function(d){if(d[k]>=t){if(d.y)m.tp++;else m.fp++;}else{if(d.y)m.fn++;else m.tn++;}});return m;}
function met(m){var n=m.tp+m.fp+m.fn+m.tn,P=m.tp+m.fp?m.tp/(m.tp+m.fp):0,R=m.tp+m.fn?m.tp/(m.tp+m.fn):0;return {acc:(m.tp+m.tn)/n,P:P,R:R,F:P+R?2*P*R/(P+R):0,fpr:m.fp+m.tn?m.fp/(m.fp+m.tn):0};}
function drawCM(x,X,Y,S,m,title,lazy){var c=S/2,cells=[[m.tp,'TP',C.gfp,0,0],[m.fn,'FN',C.eye,1,0],[m.fp,'FP',C.amber,0,1],[m.tn,'TN',C.info,1,1]],tot=m.tp+m.fp+m.fn+m.tn;
  txt(x,title,X,Y-30,C.text,12,'left',700);txt(x,'예측: 이탈',X+c/2,Y-12,C.muted,10,'center');txt(x,'예측: 유지',X+c*1.5,Y-12,C.muted,10,'center');
  txt(x,'실제 이탈',X-6,Y+c/2,C.muted,10,'right');txt(x,'실제 유지',X-6,Y+c*1.5,C.muted,10,'right');
  cells.forEach(function(e){var cx=X+e[3]*c,cy=Y+e[4]*c,a=Math.min(.55,.08+e[0]/tot*1.6);x.fillStyle=e[2];x.globalAlpha=a;x.fillRect(cx+1,cy+1,c-2,c-2);x.globalAlpha=1;x.strokeStyle=C.rule;x.strokeRect(cx,cy,c,c);
    txt(x,e[1],cx+8,cy+14,e[2],11,'left',700);txt(x,String(e[0]),cx+c/2,cy+c/2+4,C.text,Math.max(14,Math.min(22,c/5)),'center',700);});
  if(lazy){x.strokeStyle=C.eye;x.setLineDash([4,3]);x.lineWidth=2;x.strokeRect(X+2,Y+2,c-4,c-4);x.setLineDash([]);x.lineWidth=1;}}

/* ---------- 히어로 소품: 2×2 성적표 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var S=Math.min(W*.26,H*.42),X=W*.5-S/2,Y=H*.08,c=S/2,cols=[C.gfp,C.eye,C.amber,C.info];
  for(var i=0;i<4;i++){x.fillStyle=cols[i];x.globalAlpha=.25+.2*Math.sin(t*1.2+i*1.6)+.2;x.fillRect(X+(i%2)*c+2,Y+Math.floor(i/2)*c+2,c-4,c-4);}x.globalAlpha=1;x.strokeStyle='#4a6fa8';x.lineWidth=3;x.strokeRect(X,Y,S,S);x.lineWidth=1;
  var bx=W*.84,by=H*.22+Math.sin(t)*4;x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.moveTo(bx-W*.05,by);x.lineTo(bx+W*.05,by-Math.sin(t*.8)*6);x.stroke();x.beginPath();x.moveTo(bx,by-2);x.lineTo(bx,by+H*.12);x.stroke();x.lineWidth=1;});

/* ---------- ① 혼동행렬 ---------- */
var RATES=[.01,.03,.05,.1,.2,.3],D1C={};function d1(rate){return D1C[rate]||(D1C[rate]=gen(2000,rate,7));}
$('#heroLazy').textContent=pct(met(cm(d1(.05),2)).acc,1);
$('#rate').addEventListener('input',function(){$('#ratev').textContent=Math.round(RATES[+this.value]*100)+'%';draw1();});
function draw1(){var rate=RATES[+$('#rate').value],D=d1(rate),mL=cm(D,2),mM=cm(D,.5),aL=met(mL),aM=met(mM),c=$('#c1'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var S=Math.min((W-200)/2,200),X1=86,X2=X1+S+Math.max(100,(W-2*S-X1-40)/2+40);
  drawCM(x,X1,60,S,mL,'"아무도 이탈 안 함" 모델',true);drawCM(x,X2,60,S,mM,'학습한 모델 (임계값 0.5)');
  txt(x,'정확도 '+pct(aL.acc,1),X1+S/2,60+S+22,aL.acc>=aM.acc?C.amber:C.muted,13,'center',700);txt(x,'정확도 '+pct(aM.acc,1),X2+S/2,60+S+22,aM.acc>aL.acc?C.amber:C.muted,13,'center',700);
  stamp(x,W,'예시 데이터 · 고객 2,000명');
  var nPos=mM.tp+mM.fn;kpis($('#k1k'),[['i',nPos+'명','실제 이탈 고객'],['r',pct(aL.acc,1)+' · 찾은 이탈 0명','"아무도 이탈 안 함"'],['g',pct(aM.acc,1)+' · 찾은 이탈 '+mM.tp+'명','학습한 모델'],['a',mM.fn+'명','학습한 모델이 놓친 이탈(FN)']]);
  $('#ins1').innerHTML=aL.acc>=aM.acc?'<p class="r">이탈 '+Math.round(rate*100)+'%: 아무것도 찾지 못하는 모델의 정확도('+pct(aL.acc,1)+')가 학습한 모델('+pct(aM.acc,1)+')보다 높거나 같습니다. 정확도로 고르면 쓸모없는 모델이 뽑힙니다.</p>':'<p class="a">이탈 '+Math.round(rate*100)+'%: 이제 학습한 모델의 정확도가 더 높습니다. 클래스가 덜 기울면 정확도의 함정이 약해집니다. 그래도 놓친 이탈 '+mM.fn+'명은 정확도에 드러나지 않습니다.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 정밀도·재현율 ---------- */
var D2=gen(2000,.1,11),TS=[];for(var i=1;i<=49;i++)TS.push(i/50);
var CUR2=TS.map(function(t){var m=cm(D2,t),q=met(m);q.none=!(m.tp+m.fp);return q;});
$('#th').addEventListener('input',function(){$('#thv').textContent=(+this.value).toFixed(2);draw2();});
function draw2(){var t=+$('#th').value,m=cm(D2,t),M=met(m),c=$('#c2'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var X0=40,Y0=30,Wd=(W-110)/2,Hh=H-70,B=20,hp=new Array(B).fill(0),hn=new Array(B).fill(0);D2.forEach(function(d){var b=Math.min(B-1,Math.floor(d.p*B));if(d.y)hp[b]++;else hn[b]++;});
  var mx=Math.max.apply(0,hn.map(function(v,i){return Math.max(v,hp[i]*4)})),bw=Wd/B;
  for(var b=0;b<B;b++){var h1=hn[b]/mx*Hh,h2=hp[b]*4/mx*Hh;x.fillStyle='rgba(130,184,255,.55)';x.fillRect(X0+b*bw+1,Y0+Hh-h1,bw/2-1,h1);x.fillStyle='rgba(240,96,77,.8)';x.fillRect(X0+b*bw+bw/2,Y0+Hh-h2,bw/2-1,h2);}
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,.25,.5,.75,1].forEach(function(v){txt(x,v.toFixed(2),X0+v*Wd,Y0+Hh+12,C.muted,10,'center');});
  x.strokeStyle=C.gfp;x.lineWidth=2;x.beginPath();x.moveTo(X0+t*Wd,Y0-4);x.lineTo(X0+t*Wd,Y0+Hh);x.stroke();x.lineWidth=1;txt(x,'이 선 오른쪽 = "이탈" 판정',X0+t*Wd+(t>.6?-4:4),Y0-10,C.gfp,11,t>.6?'right':'left',700);
  x.fillStyle='rgba(130,184,255,.8)';x.fillRect(X0+6,Y0+8,8,8);txt(x,'유지',X0+18,Y0+12,C.muted,11);x.fillStyle=C.eye;x.fillRect(X0+52,Y0+8,8,8);txt(x,'이탈(막대 높이 ×4)',X0+64,Y0+12,C.muted,11);
  txt(x,'예측한 이탈 확률',X0+Wd/2,H-16,C.muted,11,'center');
  var X1=X0+Wd+50,tx=function(v){return X1+v*Wd},ty=function(v){return Y0+Hh-v*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,Wd,Hh);[0,.5,1].forEach(function(v){txt(x,v.toFixed(1),X1-4,ty(v),C.muted,10,'right');txt(x,v.toFixed(1),tx(v),Y0+Hh+12,C.muted,10,'center');});
  [['P',C.info,'정밀도'],['R',C.eye,'재현율'],['F',C.gfp,'F1']].forEach(function(s,j){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();var st=0;CUR2.forEach(function(q,i){if(s[0]==='P'&&q.none)return;var px=tx(TS[i]),py=ty(q[s[0]]);st?x.lineTo(px,py):x.moveTo(px,py);st=1;});x.stroke();x.lineWidth=1;txt(x,'— '+s[2],X1+24+j*62,Y0+12,s[1],11,'left',700);});
  x.setLineDash([3,3]);x.strokeStyle=C.text;x.beginPath();x.moveTo(tx(t),Y0);x.lineTo(tx(t),Y0+Hh);x.stroke();x.setLineDash([]);txt(x,'임계값',X1+Wd/2,H-16,C.muted,11,'center');
  stamp(x,W,'예시 데이터');
  kpis($('#k2k'),[['i',pct(M.P,1),'정밀도 · '+m.tp+' ÷ ('+m.tp+' + '+m.fp+')'],['r',pct(M.R,1),'재현율 · '+m.tp+' ÷ ('+m.tp+' + '+m.fn+')'],['g',M.F.toFixed(3),'F1'],['m',pct(M.acc,1),'정확도']]);
  $('#ins2').innerHTML=t<=.25?'<p class="a">관대한 기준: 이탈 고객의 '+pct(M.R,0)+'를 찾지만, "이탈" 판정의 '+pct(1-M.P,0)+'는 헛짚은 것입니다(FP '+m.fp+'명). 공항의 "엄격한 수하물 체크"와 같습니다.</p>':t>=.7?'<p class="a">엄격한 기준: "이탈" 판정은 '+pct(M.P,0)+'가 맞지만 이탈 고객의 '+pct(1-M.R,0)+'를 놓칩니다(FN '+m.fn+'명).</p>':'<p class="g">임계값 '+t.toFixed(2)+': 정밀도 '+pct(M.P,0)+', 재현율 '+pct(M.R,0)+'. 하나를 올리면 다른 하나가 내려갑니다.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ ROC·AUC ---------- */
function roc(D,k){var s=D.slice().sort(function(a,b){return b[k]-a[k]}),P=0,N=0,pts=[[0,0]],tp=0,fp=0;D.forEach(function(d){d.y?P++:N++;});s.forEach(function(d){d.y?tp++:fp++;pts.push([fp/N,tp/P]);});var a=0;for(var i=1;i<pts.length;i++)a+=(pts[i][0]-pts[i-1][0])*(pts[i][1]+pts[i-1][1])/2;return {pts:pts,auc:a};}
var RS=roc(D2,'p'),RW=roc(D2,'w'),PAIR=null;
LAB.radio('#pairBtns',[['none','끄기','pr0'],['pair','쌍 1,000개 뽑기','pr1']],'none',function(v){if(v==='pair'){var r=rng(5+Math.floor(Math.random()*1e4)),pos=D2.filter(function(d){return d.y}),neg=D2.filter(function(d){return !d.y}),w=0;for(var i=0;i<1000;i++){if(pos[Math.floor(r()*pos.length)].p>neg[Math.floor(r()*neg.length)].p)w++;}PAIR=w/1000;}else PAIR=null;draw3();});
$('#th3').addEventListener('input',function(){$('#th3v').textContent=(+this.value).toFixed(2);draw3();});
function draw3(){var t=+$('#th3').value,c=$('#c3'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var S=Math.min(W-220,H-60),X0=50,Y0=20,sx=function(v){return X0+v*S},sy=function(v){return Y0+S-v*S};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,S,S);[0,.5,1].forEach(function(v){txt(x,v.toFixed(1),X0-4,sy(v),C.muted,10,'right');txt(x,v.toFixed(1),sx(v),Y0+S+12,C.muted,10,'center');});
  txt(x,'FPR(유지 고객을 이탈로)',X0+S/2,Y0+S+28,C.muted,11,'center');
  x.setLineDash([4,4]);x.strokeStyle=C.muted;x.beginPath();x.moveTo(sx(0),sy(0));x.lineTo(sx(1),sy(1));x.stroke();x.setLineDash([]);
  [[RW,C.amber],[RS,C.gfp]].forEach(function(s){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();s[0].pts.forEach(function(p,i){i?x.lineTo(sx(p[0]),sy(p[1])):x.moveTo(sx(p[0]),sy(p[1]));});x.stroke();x.lineWidth=1;});
  var ms=met(cm(D2,t,'p')),mw=met(cm(D2,t,'w'));[[ms,C.gfp],[mw,C.amber]].forEach(function(s){x.fillStyle=s[1];x.beginPath();x.arc(sx(s[0].fpr),sy(s[0].R),6,0,7);x.fill();x.strokeStyle=C.text;x.stroke();});
  var lx=X0+S+18;txt(x,'— 강한 모델(특성 둘) AUC '+RS.auc.toFixed(3),lx,Y0+14,C.gfp,11,'left',700);txt(x,'— 약한 모델(특성 하나) AUC '+RW.auc.toFixed(3),lx,Y0+32,C.amber,11,'left',700);txt(x,'- - 랜덤 추측선 AUC 0.5',lx,Y0+50,C.muted,11);txt(x,'● 임계값 '+t.toFixed(2)+'의 위치',lx,Y0+68,C.text,11);txt(x,'세로: TPR(재현율)',lx,Y0+86,C.muted,11);
  stamp(x,W,'예시 데이터');
  kpis($('#k3k'),[['g',RS.auc.toFixed(3),'강한 모델 AUC'],['a',RW.auc.toFixed(3),'약한 모델 AUC'],['i','('+ms.fpr.toFixed(2)+', '+ms.R.toFixed(2)+')','강한 모델 (FPR, TPR)'],['m',PAIR==null?'—':pct(PAIR,1),'쌍 뽑기: 이탈 점수가 더 높은 비율']]);
  $('#ins3').innerHTML=PAIR!=null?'<p class="g">무작위 1,000쌍 중 '+pct(PAIR,1)+'에서 이탈 고객의 점수가 더 높았습니다. AUC '+RS.auc.toFixed(3)+'와 거의 같습니다. AUC는 "줄 세우기 실력"입니다.</p>':'<p class="g">강한 모델의 곡선이 약한 모델보다 왼쪽 위에 있습니다. 같은 FPR에서 더 많은 이탈 고객을 찾습니다. 두 곡선 모두 대각선 위라 동전 던지기보다 낫습니다.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 앙상블 ---------- */
var EC={};function ensAcc(N,p,rho){var key=N+'|'+p+'|'+rho;if(EC[key]!=null)return EC[key];var r=rng(77),ok=0,T=3000;for(var i=0;i<T;i++){var u0=r(),c=0;for(var j=0;j<N;j++){var u=r()<rho?u0:r();if(u<p)c++;}if(c>N/2)ok++;}return EC[key]=ok/T;}
['nm','pm','rho'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#nmv').textContent=$('#nm').value;$('#pmv').textContent=Math.round(+$('#pm').value*100)+'%';$('#rhov').textContent=(+$('#rho').value).toFixed(1);draw4();});});
var NS=[1,3,5,7,9,11,15,21,25,31,41,51];
function draw4(){var N=+$('#nm').value,p=+$('#pm').value,rho=+$('#rho').value,c=$('#c4'),W=fitC(c,280),H=280,x=c.getContext('2d');grid(x,W,H);var X0=50,Y0=24,Wd=W-80,Hh=H-60,sx=function(n){return X0+(n-1)/50*Wd},sy=function(v){return Y0+Hh-(v-.5)/.5*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[.5,.6,.7,.8,.9,1].forEach(function(v){txt(x,Math.round(v*100)+'%',X0-4,sy(v),C.muted,10,'right');});[1,11,21,31,41,51].forEach(function(n){txt(x,'N='+n,sx(n),Y0+Hh+12,C.muted,10,'center');});
  x.setLineDash([3,3]);x.strokeStyle=C.muted;x.beginPath();x.moveTo(sx(1),sy(p));x.lineTo(sx(51),sy(p));x.stroke();x.setLineDash([]);txt(x,'모델 하나 '+Math.round(p*100)+'%',sx(51)-4,sy(p)-8,C.muted,10,'right');
  [[0,C.info,'서로 독립(ρ = 0)'],[rho,C.gfp,'닮은 정도 ρ = '+rho.toFixed(1)]].forEach(function(s,j){if(j===1&&rho===0)return;x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();NS.forEach(function(n,i){var v=ensAcc(n,p,s[0]);i?x.lineTo(sx(n),sy(v)):x.moveTo(sx(n),sy(v));});x.stroke();x.lineWidth=1;txt(x,'— '+s[2],X0+8,Y0+14+j*18,s[1],11,'left',700);});
  var v=ensAcc(N,p,rho);x.fillStyle=C.gfp;x.beginPath();x.arc(sx(N),sy(v),6,0,7);x.fill();
  stamp(x,W,'모의실험 · 문제 3,000개');
  var v0=ensAcc(N,p,0);kpis($('#k4k'),[['m',pct(p,0),'모델 하나'],['g',pct(v,1),'N = '+N+' 다수결'],['i',pct(v0,1),'같은 N, 서로 독립이면'],['a','+'+((v-p)*100).toFixed(1)+'%p','앙상블로 얻은 몫']]);
  $('#ins4').innerHTML=rho>=.7?'<p class="r">ρ = '+rho.toFixed(1)+': 모델들이 같은 곳에서 같이 틀립니다. '+N+'개를 모아도 '+pct(v,1)+'. 다양성이 없으면 숫자만 많은 회의입니다.</p>':N===1?'<p class="a">모델 하나: 정확도 그대로 '+pct(p,0)+'. N을 늘려 보세요.</p>':'<p class="g">모델 '+N+'개의 다수결: '+pct(p,0)+' → '+pct(v,1)+'. 실수가 서로 다른 곳에서 나야 상쇄됩니다.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ 학습률·배치 ---------- */
var TR5=gen(800,.3,31),TE5=gen(800,.3,32),LRS=[.003,.03,.3,3,30],bs=32,LC={};
function lossW(w,D){var s=0;D.forEach(function(d){var q=sig(w[0]+w[1]*d.x[0]+w[2]*d.x[1]);q=Math.min(1-1e-9,Math.max(1e-9,q));s-=d.y*Math.log(q)+(1-d.y)*Math.log(1-q);});return s/D.length;}
function trainLR(lr,b){var key=lr+'|'+b;if(LC[key])return LC[key];var w=[0,0,0],r=rng(5),L=[lossW(w,TR5)],steps=0;
  for(var e=0;e<20;e++){var idx=TR5.map(function(_,i){return i});for(var i=idx.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),tt=idx[i];idx[i]=idx[j];idx[j]=tt;}
    for(var s=0;s<idx.length;s+=b){var g=[0,0,0],m=Math.min(b,idx.length-s);for(var k=s;k<s+m;k++){var d=TR5[idx[k]],er=sig(w[0]+w[1]*d.x[0]+w[2]*d.x[1])-d.y;g[0]+=er;g[1]+=er*d.x[0];g[2]+=er*d.x[1];}for(var q=0;q<3;q++)w[q]-=lr*g[q]/m;steps++;}L.push(lossW(w,TR5));}
  var ok=0;TE5.forEach(function(d){if((sig(w[0]+w[1]*d.x[0]+w[2]*d.x[1])>=.5?1:0)===d.y)ok++;});return LC[key]={w:w,L:L,steps:steps,acc:ok/TE5.length};}
LAB.radio('#bsBtns',[['1','1 (SGD)','b0'],['32','32 (미니 배치)','b1'],['800','800 (풀 배치)','b2']],'32',function(v){bs=+v;draw5();});
$('#lr').addEventListener('input',function(){$('#lrv').textContent=LRS[+this.value];draw5();});
function draw5(){var lr=LRS[+$('#lr').value],R=trainLR(lr,bs),c=$('#c5'),W=fitC(c,280),H=280,x=c.getContext('2d');grid(x,W,H);var X0=50,Y0=24,Wd=W-80,Hh=H-60,top=1.2,sx=function(e){return X0+e/20*Wd},sy=function(v){return Y0+Hh-Math.min(v,top)/top*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,.4,.8,1.2].forEach(function(v){txt(x,v.toFixed(1),X0-4,sy(v),C.muted,10,'right');});[0,5,10,15,20].forEach(function(e){txt(x,e+'에포크',sx(e),Y0+Hh+12,C.muted,10,'center');});
  LRS.forEach(function(l){if(l===lr)return;var Q=trainLR(l,bs);x.strokeStyle='rgba(157,155,184,.35)';x.beginPath();Q.L.forEach(function(v,e){e?x.lineTo(sx(e),sy(v)):x.moveTo(sx(e),sy(v));});x.stroke();txt(x,String(l),sx(20)+3,sy(Q.L[20]),C.muted,9);});
  x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();R.L.forEach(function(v,e){e?x.lineTo(sx(e),sy(v)):x.moveTo(sx(e),sy(v));});x.stroke();x.lineWidth=1;
  var best=trainLR(.3,32).L[20];x.setLineDash([3,3]);x.strokeStyle=C.info;x.beginPath();x.moveTo(X0,sy(best));x.lineTo(X0+Wd,sy(best));x.stroke();x.setLineDash([]);txt(x,'도달 가능한 손실 ≈ '+best.toFixed(3),X0+Wd-4,sy(best)-8,C.info,10,'right');
  txt(x,'— 학습률 '+lr+' · 배치 '+bs+' (흐린 선: 다른 학습률)',X0+8,Y0+14,C.gfp,11,'left',700);stamp(x,W,'예시 데이터 · 로지스틱 회귀');
  var fin=R.L[20],per=Math.ceil(800/bs);kpis($('#k5k'),[['i',per+'번','1에포크의 갱신 횟수(800 ÷ '+bs+')'],['a',R.steps+'번','20에포크 총 갱신'],[fin>best+.05?'r':'g',fin.toFixed(3),'20에포크 후 훈련 손실'],['m',pct(R.acc,1),'시험 정확도(임계값 0.5)']]);
  var jumpy=R.L.slice(10).some(function(v,i,a){return i&&v>a[i-1]+.02;});
  $('#ins5').innerHTML=fin>.6&&lr<=.03?'<p class="a">학습률 '+lr+' · 갱신 '+R.steps+'번: 너무 조금씩, 너무 드물게 고쳐 아직 시작점(0.693) 근처입니다.</p>':fin>best+.05||jumpy?'<p class="r">학습률 '+lr+': 한 번에 너무 크게 고쳐 손실이 '+(jumpy?'오르내립니다':'충분히 내려가지 못합니다')+'. 정답 주변을 헤매는 모습입니다.</p>':'<p class="g">학습률 '+lr+' · 배치 '+bs+': 손실이 '+fin.toFixed(3)+'까지 내려갔습니다. 도달 가능한 수준에 가깝습니다.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결: 비용 기반 임계값 ---------- */
var VD=gen(3000,.1,21),TD=gen(3000,.1,22),TT=[];for(var q=2;q<=98;q++)TT.push(q/100);
function profit(m){return m.tp*15-(m.tp+m.fp)*2;}
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:1,max:800,bigGap:1000,metric:'시험 고객 1,000명당 캠페인 순이익(만 원)',fmt:function(v){return Math.round(v).toLocaleString('ko-KR')+'만 원'},
  run:function(){var bA=TT.reduce(function(b,t){var a=met(cm(VD,t)).acc;return a>b[1]?[t,a]:b},[0,-1]),bP=TT.reduce(function(b,t){var p=profit(cm(VD,t));return p>b[1]?[t,p]:b},[0,-1e9]);
    var mA=cm(TD,bA[0]),mP=cm(TD,bP[0]);this.info={tA:bA[0],tP:bP[0],mA:mA,mP:mP,accA:met(mA).acc,accP:met(mP).acc};return {fly:profit(mA)/3,robo:profit(mP)/3};},
  report:function(r){var I=this.info;return '초파리 연구원의 임계값은 '+I.tA.toFixed(2)+'(시험 정확도 '+pct(I.accA,1)+'), 주판봇은 '+I.tP.toFixed(2)+'(정확도 '+pct(I.accP,1)+')예요. 주판봇은 쿠폰을 '+(I.mP.tp+I.mP.fp)+'장 뿌려 이탈 고객 '+I.mP.tp+'명에게 닿았고, 초파리는 '+(I.mA.tp+I.mA.fp)+'장으로 '+I.mA.tp+'명에게 닿았어요.';},
  verdict:function(r,res){return '정확도가 낮은 쪽이 돈을 더 벌었다. 임계값은 틀림의 값으로 정한다. '+(res==='R'?'주판봇 승.':res==='F'?'초파리 승.':'이번 판은 나눠 갖는다.');}});
