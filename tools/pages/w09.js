/* 9주차 · 회귀모형(1) — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
var PL=[8.4,13.7,15.0,16.2,17.4,18.0,18.7,19.0,19.6,20.0,21.0,21.0,21.0,21.3,22.0,22.0,22.0,22.0,22.0,22.5,22.5,22.7,23.0,23.5,24.0,24.0,24.6,25.0,25.6,26.5,27.3,27.5,27.5,27.5,28.0,28.7,30.0,32.8,34.5,35.0,36.5,36.0,37.0,37.0,39.0,39.0,39.0,40.0,40.0,40.0,40.0,42.0,43.0,43.0,43.5,44.0];
var PW=[5.9,32.0,40.0,51.5,70.0,100.0,78.0,80.0,85.0,85.0,110.0,115.0,125.0,130.0,120.0,120.0,130.0,135.0,110.0,130.0,150.0,145.0,150.0,170.0,225.0,145.0,188.0,180.0,197.0,218.0,300.0,260.0,265.0,250.0,250.0,300.0,320.0,514.0,556.0,840.0,685.0,700.0,700.0,690.0,900.0,650.0,820.0,850.0,900.0,1015.0,820.0,1100.0,1000.0,1100.0,1000.0,1000.0];
/* train_test_split(random_state=42)의 시험 인덱스(np.random.RandomState(42).permutation(56)의 앞 14개) */
var TEI=[0,5,33,13,19,50,36,26,44,12,54,3,34,30],TRI=[];for(var i=0;i<56;i++)if(TEI.indexOf(i)<0)TRI.push(i);
var XTR=TRI.map(function(i){return PL[i]}),YTR=TRI.map(function(i){return PW[i]}),XTE=TEI.map(function(i){return PL[i]}),YTE=TEI.map(function(i){return PW[i]});
function mean(a){return a.reduce(function(s,v){return s+v},0)/a.length}
function r2(y,p){var m=mean(y),sse=0,sst=0;y.forEach(function(v,i){sse+=(v-p[i])*(v-p[i]);sst+=(v-m)*(v-m);});return 1-sse/sst;}
function rmse(y,p){return Math.sqrt(mean(y.map(function(v,i){return (v-p[i])*(v-p[i])})));}
function knnR(x,k){var d=XTR.map(function(v,i){return [Math.abs(v-x),i]}).sort(function(a,b){return a[0]-b[0]||a[1]-b[1]}).slice(0,k);return {pred:mean(d.map(function(t){return YTR[t[1]]})),nb:d.map(function(t){return t[1]})};}
function solve(A,b){var n=b.length,M=A.map(function(r,i){return r.concat([b[i]])});for(var c=0;c<n;c++){var p=c;for(var r=c+1;r<n;r++)if(Math.abs(M[r][c])>Math.abs(M[p][c]))p=r;var t=M[c];M[c]=M[p];M[p]=t;for(r=0;r<n;r++){if(r===c)continue;var f=M[r][c]/M[c][c];for(var j=c;j<=n;j++)M[r][j]-=f*M[c][j];}}return M.map(function(r,i){return r[n]/r[i]});}
function ols(X,y,ridge){var p=X[0].length,A=[],b=[];for(var i=0;i<p;i++){A.push([]);b.push(0);for(var j=0;j<p;j++){var s=0;for(var r=0;r<X.length;r++)s+=X[r][i]*X[r][j];A[i].push(s+(i===j?(ridge||0):0));}for(r=0;r<X.length;r++)b[i]+=X[r][i]*y[r];}return solve(A,b);}
var MX=mean(XTR),SX=Math.sqrt(mean(XTR.map(function(v){return (v-MX)*(v-MX)})));
function polyFit(d){var row=function(x){var z=(x-MX)/SX,r=[];for(var q=0;q<=d;q++)r.push(Math.pow(z,q));return r;},w=ols(XTR.map(row),YTR,1e-9);return function(x){var r=row(x),s=0;for(var q=0;q<=d;q++)s+=w[q]*r[q];return s;};}
var LIN=ols(XTR.map(function(x){return [1,x]}),YTR),linF=function(x){return LIN[0]+LIN[1]*x},POLY2=polyFit(2);
function axes(x,X0,Y0,Wd,Hh,xmax,ymin,ymax){x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);for(var v=Math.ceil(ymin/500)*500;v<=ymax;v+=500)txt(x,v+'g',X0-4,Y0+Hh-(v-ymin)/(ymax-ymin)*Hh,C.muted,10,'right');for(var l=0;l<=xmax;l+=10)txt(x,l+'cm',X0+l/xmax*Wd,Y0+Hh+12,C.muted,10,'center');}
function dots(x,sx,sy){XTR.forEach(function(v,i){x.fillStyle=C.info;x.beginPath();x.arc(sx(v),sy(YTR[i]),3.2,0,7);x.fill();});XTE.forEach(function(v,i){x.fillStyle=C.amber;x.beginPath();x.arc(sx(v),sy(YTE[i]),3.6,0,7);x.fill();});}
function legend(x,X,Y,items){var cx=X;items.forEach(function(it){x.fillStyle=it[1];x.beginPath();x.arc(cx+4,Y,4,0,7);x.fill();txt(x,it[0],cx+12,Y,C.muted,11);cx+=x.measureText(it[0]).width+30;});}

/* ---------- 히어로 소품: 과녁 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var cx=W*.55,cy=H*.24,R=Math.min(W,H)*.14;[[1,'#f0604d'],[.75,'#eceaf3'],[.5,'#82b8ff'],[.25,'#f1b646']].forEach(function(r){x.fillStyle=r[1];x.globalAlpha=.75;x.beginPath();x.arc(cx,cy,R*r[0],0,7);x.fill();});x.globalAlpha=1;
  [[.1,.05],[-.3,.2],[.45,-.35]].forEach(function(a,i){var ax=cx+a[0]*R,ay=cy+a[1]*R+Math.sin(t*1.3+i)*1.5;x.strokeStyle='#d8c08a';x.lineWidth=2;x.beginPath();x.moveTo(ax,ay);x.lineTo(ax+R*.5,ay-R*.25);x.stroke();});x.lineWidth=1;});

/* ---------- ① KNN 회귀 ---------- */
$('#heroKnn50').textContent=Math.round(knnR(50,5).pred).toLocaleString('ko-KR')+'g';
['k1','q1'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#k1v').textContent=$('#k1').value;$('#q1v').textContent=$('#q1').value+'cm';draw1();});});
function draw1(){var k=+$('#k1').value,q=+$('#q1').value,c=$('#c1'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-80,Hh=H-60,sx=function(v){return X0+v/60*Wd},sy=function(v){return Y0+Hh-v/1600*Hh};axes(x,X0,Y0,Wd,Hh,60,0,1600);
  x.strokeStyle=C.eye;x.lineWidth=2;x.beginPath();for(var l=5;l<=60;l+=.25){var p=knnR(l,k).pred;l>5?x.lineTo(sx(l),sy(p)):x.moveTo(sx(l),sy(p));}x.stroke();x.lineWidth=1;
  dots(x,sx,sy);var R=knnR(q,k);R.nb.forEach(function(i){x.strokeStyle=C.gfp;x.lineWidth=2;x.beginPath();x.arc(sx(XTR[i]),sy(YTR[i]),7,0,7);x.stroke();x.lineWidth=1;});
  x.setLineDash([3,3]);x.strokeStyle=C.gfp;x.beginPath();x.moveTo(sx(q),Y0+Hh);x.lineTo(sx(q),sy(R.pred));x.stroke();x.setLineDash([]);x.fillStyle=C.gfp;x.beginPath();x.arc(sx(q),sy(R.pred),6,0,7);x.fill();
  txt(x,q+'cm → '+Math.round(R.pred)+'g',sx(q)+(q>45?-10:10),sy(R.pred)-12,C.gfp,12,q>45?'right':'left',700);
  legend(x,X0+8,Y0+12,[['훈련 42',C.info],['시험 14',C.amber],['예측선',C.eye]]);stamp(x,W,'교안 데이터');
  var ptr=XTR.map(function(v){return knnR(v,k).pred}),pte=XTE.map(function(v){return knnR(v,k).pred});
  kpis($('#k1k'),[['i',r2(YTR,ptr).toFixed(4),'공부 데이터 설명력(R²)'],['g',r2(YTE,pte).toFixed(4),'시험 데이터 설명력(R²)'],['a',Math.round(R.pred)+'g',q+'cm 농어 예측'],['m',Math.round(knnR(44,k).pred)+'g','44cm 농어 예측(비교)']]);
  $('#ins1').innerHTML=q>44?'<p class="r">'+q+'cm 농어도 '+Math.round(R.pred)+'g. 훈련 데이터의 가장 긴 농어(44cm) 근처 '+k+'마리 평균에서 멈춥니다. 이웃이 바뀌지 않으니 예측도 바뀌지 않습니다.</p>':k===1?'<p class="a">K = 1: 예측선이 훈련 점마다 꺾입니다. 노이즈까지 따라가는 과적합 모습입니다.</p>':'<p class="g">K = '+k+', '+q+'cm → '+Math.round(R.pred)+'g. 가장 가까운 '+k+'마리(초록 테두리)의 무게 평균입니다.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 최소제곱 ---------- */
LAB.radio('#lsBtns',[['hand','손으로','ls0'],['ls','최소제곱으로','ls1']],'hand',function(v){if(v==='ls'){$('#b1').value=Math.round(LIN[1]);$('#b0').value=Math.round(LIN[0]/20)*20;}draw2(v==='ls');});
['b1','b0'].forEach(function(id){$('#'+id).addEventListener('input',function(){var b=$('#lsBtns .bt[aria-pressed="true"]');draw2(false);});});
function draw2(exact){var b1=exact?LIN[1]:+$('#b1').value,b0=exact?LIN[0]:+$('#b0').value;$('#b1v').textContent=exact?b1.toFixed(1):b1;$('#b0v').textContent=exact?Math.round(b0):b0;
  var c=$('#c2'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-80,Hh=H-60,ymin=-500,ymax=1300,sx=function(v){return X0+v/50*Wd},sy=function(v){return Y0+Hh-(v-ymin)/(ymax-ymin)*Hh};axes(x,X0,Y0,Wd,Hh,50,ymin,ymax);
  x.strokeStyle='rgba(157,155,184,.4)';x.beginPath();x.moveTo(X0,sy(0));x.lineTo(X0+Wd,sy(0));x.stroke();
  var sse=0;XTR.forEach(function(v,i){var p=b0+b1*v,e=YTR[i]-p;sse+=e*e;var px=sx(v),py=sy(YTR[i]),pp=sy(p),s=Math.abs(py-pp);x.fillStyle=e>0?'rgba(130,184,255,.12)':'rgba(240,96,77,.12)';x.fillRect(px,Math.min(py,pp),Math.min(s,60),s);x.strokeStyle=e>0?C.info:C.eye;x.beginPath();x.moveTo(px,py);x.lineTo(px,pp);x.stroke();});
  XTR.forEach(function(v,i){x.fillStyle=C.text;x.beginPath();x.arc(sx(v),sy(YTR[i]),3,0,7);x.fill();});
  x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();x.moveTo(sx(0),sy(b0));x.lineTo(sx(50),sy(b0+b1*50));x.stroke();x.lineWidth=1;
  x.setLineDash([4,4]);x.strokeStyle=C.amber;x.beginPath();x.moveTo(sx(0),sy(LIN[0]));x.lineTo(sx(50),sy(LIN[0]+LIN[1]*50));x.stroke();x.setLineDash([]);
  txt(x,'— 지금 직선  - - 최소제곱 직선  ▮ 잔차²',X0+8,Y0+12,C.muted,11);stamp(x,W,'교안 데이터 · 훈련 42마리');
  var best=0;XTR.forEach(function(v,i){var e=YTR[i]-(LIN[0]+LIN[1]*v);best+=e*e;});
  kpis($('#k2k'),[['g','무게 = '+b1.toFixed(1)+' × 길이 '+(b0<0?'− ':'+ ')+Math.abs(Math.round(b0)),'지금 직선'],[sse<=best*1.001?'g':'r',Math.round(sse).toLocaleString('ko-KR'),'빗나간 거리 제곱의 합(SSE)'],['a',Math.round(best).toLocaleString('ko-KR'),'가장 잘 맞는 직선의 SSE'],['i',Math.round(b0+b1*8.4)+'g','8.4cm 농어 예측']]);
  $('#ins2').innerHTML=sse<=best*1.001?'<p class="g">최소제곱 직선입니다. 어떤 직선도 SSE를 '+Math.round(best).toLocaleString('ko-KR')+'보다 작게 만들 수 없습니다. 그런데 8.4cm 농어는 '+Math.round(b0+b1*8.4)+'g으로 예측됩니다.</p>':'<p class="a">지금 SSE는 최소제곱의 '+(sse/best).toFixed(2)+'배입니다. 슬라이더로 줄여 보거나 "최소제곱으로"를 누르세요.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2(false);});

/* ---------- ③ 다항 회귀 ---------- */
var PF={};function pf(d){return PF[d]||(PF[d]=polyFit(d));}
function polyScores(d){var f=pf(d);return [r2(YTR,XTR.map(f)),r2(YTE,XTE.map(f))];}
$('#dg').addEventListener('input',function(){$('#dgv').textContent=this.value;draw3();});
function draw3(){var d=+$('#dg').value,f=pf(d),S=polyScores(d),c=$('#c3'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=(W-120)*.62,Hh=H-60,ymin=-300,ymax=1500,sx=function(v){return X0+v/50*Wd},sy=function(v){return Y0+Hh-(v-ymin)/(ymax-ymin)*Hh};
  axes(x,X0,Y0,Wd,Hh,50,ymin,ymax);x.save();x.beginPath();x.rect(X0,Y0,Wd,Hh);x.clip();x.strokeStyle=C.eye;x.lineWidth=2;x.beginPath();for(var l=5;l<=50;l+=.25){var p=f(l);l>5?x.lineTo(sx(l),sy(p)):x.moveTo(sx(l),sy(p));}x.stroke();x.lineWidth=1;dots(x,sx,sy);x.restore();
  x.fillStyle='rgba(241,182,70,.15)';x.fillRect(X0,Y0,sx(13.7)-X0,Hh);txt(x,'훈련 범위 밖',X0+4,Y0+Hh-8,C.amber,10);
  legend(x,X0+8,Y0+12,[['훈련',C.info],['시험',C.amber],['곡선',C.eye]]);
  var X1=X0+Wd+50,W1=W-X1-16,bw=W1/8,by=function(v){return Y0+Hh-Math.max(0,v)*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[0,.5,1].forEach(function(v){txt(x,v.toFixed(1),X1-4,by(v),C.muted,10,'right');});
  for(var q=1;q<=8;q++){var s=polyScores(q);x.fillStyle=q===d?C.info:'rgba(130,184,255,.4)';x.fillRect(X1+(q-1)*bw+2,by(s[0]),bw/2-2,Y0+Hh-by(s[0]));x.fillStyle=q===d?C.amber:'rgba(241,182,70,.4)';x.fillRect(X1+(q-1)*bw+bw/2,by(s[1]),bw/2-2,Y0+Hh-by(s[1]));if(s[1]<0)txt(x,'↓',X1+(q-.25)*bw,Y0+Hh-6,C.eye,12,'center',700);txt(x,String(q),X1+(q-.5)*bw,Y0+Hh+12,C.muted,10,'center');}
  txt(x,'차수별 R² (파랑 훈련 · 주황 시험)',X1,Y0-8,C.text,11,'left',700);stamp(x,W,'교안 데이터');
  kpis($('#k3k'),[['i',S[0].toFixed(4),'공부 데이터 설명력(R²)'],[S[1]<.9?'r':'g',S[1].toFixed(4),'시험 데이터 설명력(R²)'],['a',Math.round(f(8.4))+'g','8.4cm 농어 예측(실제 5.9g)'],['m',Math.round(f(50))+'g','50cm 농어 예측']]);
  $('#ins3').innerHTML=d===1?'<p class="a">차수 1은 ②칸의 직선과 같습니다. 시험 R² '+S[1].toFixed(3)+'.</p>':d>=6?'<p class="r">차수 '+d+': 훈련 R² '+S[0].toFixed(3)+'로 더 올랐지만 시험 R²는 '+S[1].toFixed(2)+'. 곡선이 훈련 점 사이를 억지로 지나가며 범위 끝에서 크게 휘었습니다.</p>':'<p class="g">차수 '+d+': 훈련 '+S[0].toFixed(3)+', 시험 '+S[1].toFixed(3)+'. 직선보다 작은 농어와 큰 농어를 함께 잘 따라갑니다.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 오차 지표 ---------- */
var md='knn',ol='off',MODELS={knn:function(v){return knnR(v,5).pred},lin:linF,poly:POLY2};
LAB.radio('#mdBtns',[['knn','KNN','m0'],['lin','선형','m1'],['poly','2차','m2']],'knn',function(v){md=v;draw4();});
LAB.radio('#olBtns',[['off','없음','o0'],['on','한 마리 +600g 오기','o1']],'off',function(v){ol=v;draw4();});
function draw4(){var f=MODELS[md],Y=YTE.slice();if(ol==='on')Y[8]+=600;var P=XTE.map(f),E=Y.map(function(v,i){return v-P[i]}),c=$('#c4'),W=fitC(c,260),H=260,x=c.getContext('2d');grid(x,W,H);
  var X0=56,Y0=24,Wd=W-80,Hh=H-60,mx=ol==='on'?700:200,zy=Y0+Hh/2,bw=Wd/14,sy=function(v){return zy-v/mx*(Hh/2)};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);x.beginPath();x.moveTo(X0,zy);x.lineTo(X0+Wd,zy);x.stroke();[mx,mx/2,0,-mx/2,-mx].forEach(function(v){txt(x,(v>0?'+':'')+v+'g',X0-4,sy(v),C.muted,10,'right');});
  var ord=XTE.map(function(v,i){return i}).sort(function(a,b){return XTE[a]-XTE[b]});
  ord.forEach(function(i,j){var e=E[i];x.fillStyle=e>=0?C.info:C.eye;x.fillRect(X0+j*bw+3,Math.min(zy,sy(e)),bw-6,Math.abs(sy(e)-zy)||1);txt(x,XTE[i]+'',X0+j*bw+bw/2,Y0+Hh+12,C.muted,9,'center');if(ol==='on'&&i===8)txt(x,'오기',X0+j*bw+bw/2,sy(e)-8,C.amber,10,'center',700);});
  txt(x,'시험 농어 14마리 (가로: 길이 cm 순) · 위 = 실제가 더 무거움',X0+6,Y0+12,C.muted,11);stamp(x,W,ol==='on'?'오기는 일부러 넣은 값':'교안 데이터');
  var mse=mean(E.map(function(e){return e*e})),mae=mean(E.map(Math.abs));
  kpis($('#k4k'),[['r',Math.round(mse).toLocaleString('ko-KR'),'빗나간 거리 제곱의 평균(MSE, g²)'],['a',Math.round(Math.sqrt(mse))+'g','평균적으로 빗나간 g(RMSE)'],['g',Math.round(mae)+'g','빗나간 g의 평균(MAE)'],['m',Math.round(mean(E))+'g','오차를 그냥 평균하면']]);
  $('#ins4').innerHTML=ol==='on'?'<p class="r">오기 한 마리로 MSE는 '+Math.round(mse).toLocaleString('ko-KR')+'까지 뛰었고, RMSE('+Math.round(Math.sqrt(mse))+'g)와 MAE('+Math.round(mae)+'g)의 차이가 크게 벌어졌습니다. 큰 오차 하나에 MSE가 가장 민감합니다.</p>':'<p class="g">'+{knn:'KNN',lin:'선형',poly:'2차'}[md]+' 모델: 시험 농어 한 마리당 평균 '+Math.round(mae)+'g(MAE), 제곱 평균의 제곱근으로는 '+Math.round(Math.sqrt(mse))+'g(RMSE) 빗나갑니다. 오차를 그냥 평균하면 '+Math.round(mean(E))+'g — 부호가 상쇄됩니다.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ R²와 수정 R² ---------- */
var NOISE=(function(){var r=rng(13),a=[];for(var i=0;i<42;i++){var row=[];for(var j=0;j<20;j++)row.push(gauss(r));a.push(row);}return a;})(),RC={};
function r2k(k){if(RC[k])return RC[k];var X=XTR.map(function(v,i){return [1,v].concat(NOISE[i].slice(0,k))}),w=ols(X,YTR,1e-9),P=X.map(function(r){return r.reduce(function(s,v,j){return s+v*w[j]},0)}),R=r2(YTR,P),n=42,A=1-(1-R)*(n-1)/(n-k-1-1);
  var m=mean(YTR),sst=0,ssr=0,sse=0;YTR.forEach(function(v,i){sst+=(v-m)*(v-m);ssr+=(P[i]-m)*(P[i]-m);sse+=(v-P[i])*(v-P[i]);});return RC[k]={R:R,A:A,sst:sst,ssr:ssr,sse:sse};}
$('#kn').addEventListener('input',function(){$('#knv').textContent=this.value;draw5();});
function draw5(){var k=+$('#kn').value,S=r2k(k),c=$('#c5'),W=fitC(c,280),H=280,x=c.getContext('2d');grid(x,W,H);var X0=30,Y0=34,Wd=Math.max(140,(W-100)*.35),bh=34;
  txt(x,'SST = SSR + SSE',X0,Y0-12,C.text,12,'left',700);var f=S.ssr/S.sst;x.fillStyle=C.gfp;x.fillRect(X0,Y0+10,Wd*f,bh);x.fillStyle=C.eye;x.fillRect(X0+Wd*f,Y0+10,Wd*(1-f)+1,bh);x.strokeStyle=C.rule;x.strokeRect(X0,Y0+10,Wd,bh);
  txt(x,'SSR '+pct(f,1),X0,Y0+bh+28,C.gfp,11,'left',700);txt(x,'SSE '+pct(1-f,1),X0+Wd,Y0+bh+28,C.eye,11,'right',700);txt(x,'SST = '+Math.round(S.sst/1000).toLocaleString('ko-KR')+'천 g²',X0,Y0+bh+50,C.muted,11);
  var X1=X0+Wd+60,W1=W-X1-20,Hh=H-70,lo=.90,hi=.96,sx=function(q){return X1+q/12*W1},sy=function(v){return Y0+Hh-(Math.max(lo,Math.min(hi,v))-lo)/(hi-lo)*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[.90,.92,.94,.96].forEach(function(v){txt(x,v.toFixed(2),X1-4,sy(v),C.muted,10,'right');});[0,3,6,9,12].forEach(function(q){txt(x,'+'+q,sx(q),Y0+Hh+12,C.muted,10,'center');});
  [['R',C.info,'설명력(R²)'],['A',C.amber,'칸 수만큼 깎은 설명력(수정 R²)']].forEach(function(s,j){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();for(var q=0;q<=12;q++){var v=r2k(q)[s[0]];q?x.lineTo(sx(q),sy(v)):x.moveTo(sx(q),sy(v));}x.stroke();x.lineWidth=1;x.fillStyle=s[1];x.beginPath();x.arc(sx(k),sy(S[s[0]]),5,0,7);x.fill();txt(x,'— '+s[2],X1+8+j*60,Y0+12,s[1],11,'left',700);});
  txt(x,'난수 변수 개수',X1+W1/2,H-14,C.muted,11,'center');stamp(x,W,'교안 데이터 + 난수 열');
  kpis($('#k5k'),[['i',S.R.toFixed(4),'설명력(R²)'],['a',S.A.toFixed(4),'칸 수만큼 깎은 설명력(수정 R²)'],['m',(k+1)+'개','독립변수 수(길이 + 난수 '+k+')'],[S.A<r2k(0).A?'r':'g',(S.A-r2k(0).A>=0?'+':'')+((S.A-r2k(0).A)*100).toFixed(2)+'%p','길이만 쓸 때보다 달라진 수정 R²']]);
  $('#eq5').innerHTML='Adj. R² = 1 − (1 − <b>'+S.R.toFixed(4)+'</b>) × (42 − 1) ÷ (42 − '+(k+1)+' − 1) = <em>'+S.A.toFixed(4)+'</em>';
  $('#ins5').innerHTML=k===0?'<p class="g">길이 하나로 무게 변동의 '+pct(S.R,1)+'를 설명합니다(훈련 데이터). 난수 변수를 더해 보세요.</p>':'<p class="'+(S.A<r2k(0).A?'r':'a')+'">쓸모없는 변수 '+k+'개를 더하자 R²는 '+r2k(0).R.toFixed(4)+' → '+S.R.toFixed(4)+'로 올랐지만, 수정 R²는 '+r2k(0).A.toFixed(4)+' → '+S.A.toFixed(4)+'. 겉보기 성능에 속지 않게 해 줍니다.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결: 범위 안 vs 범위 밖 ---------- */
var BL=[45.1,47.5,47.5,45.7,45.7,46.1,47.1,46.2,45.4,46.7],BW=[1338,1722,1534,1403,1534,1411,1650,1277,1285,1575];
LAB.Duel({el:'#duelBox',higherIsBetter:false,drawMargin:1,max:500,metric:'RMSE(g) — 작을수록 좋음',fmt:function(v){return Math.round(v)+'g'},
  run:function(){var kA=rmse(YTE,XTE.map(function(v){return knnR(v,5).pred})),pA=rmse(YTE,XTE.map(POLY2)),kB=rmse(BW,BL.map(function(v){return knnR(v,5).pred})),pB=rmse(BW,BL.map(POLY2));
    this.v={kA:kA,pA:pA,kB:kB,pB:pB,knn47:knnR(47.5,5).pred,poly47:POLY2(47.5)};
    return {cond:(kA<pA)!==(kB<pB),fly:pA,robo:kA,condA:{label:'시험 A · 교안 시험 농어 14마리(훈련 범위 안)',fly:pA,robo:kA},condB:{label:'시험 B · 큰 농어 10마리(45~48cm, 훈련 범위 밖)',fly:pB,robo:kB}};},
  report:function(r){var v=this.v;return '범위 안에서는 KNN '+Math.round(v.kA)+'g 대 곡선 '+Math.round(v.pA)+'g로 주판봇, 범위 밖에서는 KNN '+Math.round(v.kB)+'g 대 곡선 '+Math.round(v.pB)+'g로 초파리 연구원이 덜 빗나갔어요. 47.5cm 농어를 KNN은 '+Math.round(v.knn47)+'g, 곡선은 '+Math.round(v.poly47)+'g으로 예측했어요.';},
  verdict:function(r,res){return res==='C'?'조건부. 데이터 범위 안이면 이웃 평균, 범위 밖이면 곡선. 예측할 대상이 어디에 있는지부터 확인한다.':'이번 판은 '+(res==='F'?'초파리 승.':res==='R'?'주판봇 승.':'무승부.');}});
