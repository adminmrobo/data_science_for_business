/* 11주차 · 시계열 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
function mean(a){return a.reduce(function(s,v){return s+v},0)/a.length}
function sd(a){var m=mean(a);return Math.sqrt(mean(a.map(function(v){return (v-m)*(v-m)})));}
function quant(a,q){var s=a.slice().sort(function(x,y){return x-y}),p=(s.length-1)*q,i=Math.floor(p);return s[i]+(s[Math.min(i+1,s.length-1)]-s[i])*(p-i);}
var SP=[-8,-10,-3,0,3,5,9,7,0,-2,3,14],MON=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'];
function sales(n,trend,amp,seed){var r=rng(seed),e=0,a=[];for(var t=0;t<n;t++){e=.5*e+gauss(r)*4;a.push(100+trend*t+amp/14*SP[t%12]+e);}return a;}
function acf(y,K){var m=mean(y),d=y.map(function(v){return v-m}),s0=d.reduce(function(s,v){return s+v*v},0),o=[];for(var k=1;k<=K;k++){var s=0;for(var t=k;t<y.length;t++)s+=d[t]*d[t-k];o.push(s/s0);}return o;}
function pacf(y,K){var r=[1].concat(acf(y,K)),phi=[],out=[];for(var k=1;k<=K;k++){var num=r[k],den=1;for(var j=1;j<k;j++){num-=phi[k-1][j]*r[k-j];den-=phi[k-1][j]*r[j];}var pk=num/den,row=[0];for(j=1;j<k;j++)row.push(phi[k-1][j]-pk*phi[k-1][k-j]);row.push(pk);phi[k]=row;out.push(pk);}return out;}
function line(x,ys,sx,sy,col,w){x.strokeStyle=col;x.lineWidth=w||2;x.beginPath();ys.forEach(function(v,i){i?x.lineTo(sx(i),sy(v)):x.moveTo(sx(i),sy(v));});x.stroke();x.lineWidth=1;}
function bars(x,vals,X0,Y0,W,H,n,title){var ci=1.96/Math.sqrt(n),bw=W/vals.length,zy=Y0+H/2,sy=function(v){return zy-v*(H/2)};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,W,H);x.beginPath();x.moveTo(X0,zy);x.lineTo(X0+W,zy);x.stroke();
  x.setLineDash([3,3]);x.strokeStyle=C.eye;[ci,-ci].forEach(function(c){x.beginPath();x.moveTo(X0,sy(c));x.lineTo(X0+W,sy(c));x.stroke();});x.setLineDash([]);
  vals.forEach(function(v,i){x.fillStyle=Math.abs(v)>ci?C.info:'rgba(157,155,184,.5)';x.fillRect(X0+i*bw+2,Math.min(zy,sy(v)),bw-4,Math.abs(sy(v)-zy)||1);if(i%3===0||vals.length<=12)txt(x,String(i+1),X0+(i+.5)*bw,Y0+H+11,C.muted,9,'center');});
  txt(x,title,X0,Y0-6,C.text,11,'left',700);txt(x,'+1',X0-4,sy(1),C.muted,9,'right');txt(x,'−1',X0-4,sy(-1),C.muted,9,'right');}
var Y72=sales(72,1.2,14,11);
var A0=acf(Y72,12);$('#heroAcf').textContent=A0[0].toFixed(2)+' · '+A0[11].toFixed(2);

/* ---------- 히어로 소품 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var X0=W*.3,Y0=H*.06,w=W*.46,h=H*.3;x.strokeStyle='#4a6fa8';x.lineWidth=2;x.strokeRect(X0,Y0,w,h);x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();for(var i=0;i<=36;i++){var u=i/36,v=.25+.35*u+.18*Math.sin(u*Math.PI*6+t*.5);i?x.lineTo(X0+u*w,Y0+h-v*h):x.moveTo(X0+u*w,Y0+h-v*h);}x.stroke();x.lineWidth=1;
  for(var k=0;k<3;k++){var px=X0+(k*12+11)/36*w;x.fillStyle=C.amber;x.beginPath();x.arc(px,Y0+h-(.25+.35*(k*12+11)/36+.18*Math.sin((k*12+11)/36*Math.PI*6+t*.5))*h,4,0,7);x.fill();}});

/* ---------- ① 차트·상자수염 ---------- */
var QS=[118,124,121,131,136,133,142,149],QL=['1Q','2Q','3Q','4Q','1Q','2Q','3Q','4Q'],DS=(function(){var r=rng(5),a=[];for(var i=0;i<90;i++)a.push(Math.round(300+gauss(r)*40));a[17]=520;a[44]=95;a[71]=470;return a;})(),ch='line';
LAB.radio('#chBtns',[['line','선','ch0'],['bar','막대','ch1'],['pie','파이','ch2']],'line',function(v){ch=v;draw1();});
$('#iq').addEventListener('input',function(){$('#iqv').textContent=this.value;draw1();});
function draw1(){var k=+$('#iq').value,c=$('#c1'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=46,Y0=30,Wd=(W-120)*.55,Hh=H-70;
  txt(x,'분기 매출(억 원, 2년)',X0,Y0-12,C.text,11,'left',700);var cols=[C.info,C.gfp,C.amber,C.eye,C.stain,'#82b8ff','#9ab8ff','#5ee39c'];
  if(ch==='pie'){var cx=X0+Wd/2,cy=Y0+Hh/2,R=Math.min(Wd,Hh)/2-6,tot=QS.reduce(function(a,b){return a+b}),a0=-Math.PI/2;QS.forEach(function(v,i){var a1=a0+v/tot*Math.PI*2;x.fillStyle=cols[i];x.globalAlpha=.75;x.beginPath();x.moveTo(cx,cy);x.arc(cx,cy,R,a0,a1);x.closePath();x.fill();x.globalAlpha=1;var am=(a0+a1)/2;txt(x,(i<4?'1년 ':'2년 ')+QL[i],cx+Math.cos(am)*R*.7,cy+Math.sin(am)*R*.7,C.bg||'#111',9,'center',700);a0=a1;});}
  else{var lo=100,hi=160,sx=function(i){return X0+(i+.5)/8*Wd},sy=function(v){return Y0+Hh-(v-lo)/(hi-lo)*Hh};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[100,130,160].forEach(function(v){txt(x,v,X0-4,sy(v),C.muted,10,'right');});QL.forEach(function(l,i){txt(x,l,sx(i),Y0+Hh+12,C.muted,9,'center');});
    if(ch==='bar')QS.forEach(function(v,i){x.fillStyle=C.info;x.fillRect(sx(i)-Wd/22,sy(v),Wd/11,Y0+Hh-sy(v));});else{line(x,QS,sx,sy,C.gfp,2.5);QS.forEach(function(v,i){x.fillStyle=C.gfp;x.beginPath();x.arc(sx(i),sy(v),3.5,0,7);x.fill();});}}
  var q1=quant(DS,.25),q2=quant(DS,.5),q3=quant(DS,.75),iqr=q3-q1,lw=q1-k*iqr,hw=q3+k*iqr,out=DS.filter(function(v){return v<lw||v>hw}),inn=DS.filter(function(v){return v>=lw&&v<=hw});
  var X1=X0+Wd+50,W1=W-X1-30,lo2=50,hi2=560,by=function(v){return Y0+Hh-(v-lo2)/(hi2-lo2)*Hh},bx=X1+W1/2,bw=Math.min(70,W1*.5);x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);[100,300,500].forEach(function(v){txt(x,v,X1-4,by(v),C.muted,10,'right');});
  x.fillStyle='rgba(130,184,255,.25)';x.fillRect(bx-bw/2,by(q3),bw,by(q1)-by(q3));x.strokeStyle=C.info;x.strokeRect(bx-bw/2,by(q3),bw,by(q1)-by(q3));x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.moveTo(bx-bw/2,by(q2));x.lineTo(bx+bw/2,by(q2));x.stroke();x.lineWidth=1;
  var wl=Math.min.apply(0,inn),wh=Math.max.apply(0,inn);x.strokeStyle=C.text;x.beginPath();x.moveTo(bx,by(q3));x.lineTo(bx,by(wh));x.moveTo(bx-bw/4,by(wh));x.lineTo(bx+bw/4,by(wh));x.moveTo(bx,by(q1));x.lineTo(bx,by(wl));x.moveTo(bx-bw/4,by(wl));x.lineTo(bx+bw/4,by(wl));x.stroke();
  out.forEach(function(v){x.fillStyle=C.eye;x.beginPath();x.arc(bx,by(v),5,0,7);x.fill();});txt(x,'일매출 90일(만 원)',X1,Y0-12,C.text,11,'left',700);
  stamp(x,W,'예시 데이터');
  kpis($('#k1k'),[['i',Math.round(q1)+' · '+Math.round(q2)+' · '+Math.round(q3),'Q1 · 중앙값 · Q3'],['a',Math.round(iqr),'가운데 50% 폭(IQR)'],['m',Math.round(lw)+' ~ '+Math.round(hw),'정상 범위(Q ± '+k+'·IQR)'],[out.length?'r':'g',out.length+'일','이상값으로 찍힌 날']]);
  $('#ins1').innerHTML=(ch==='pie'?'<p class="r">파이 차트: 8조각이 비슷한 크기라 성장 추세가 보이지 않고, 1년 1Q에서 2년 4Q로 가는 순서도 읽히지 않습니다.</p>':ch==='bar'?'<p class="a">막대: 분기별 값 비교는 정확하지만, 흐름은 선보다 덜 눈에 띕니다.</p>':'<p class="g">선: 2년 동안 꾸준히 오르고 매년 3Q에 살짝 꺾이는 흐름이 한눈에 보입니다.</p>')+'<p class="'+(out.length?'a':'g')+'">상자수염: '+k+'·IQR 기준으로 '+out.length+'일이 이상값 후보입니다'+(out.length?' ('+out.join(', ')+'만 원)':'')+'.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② ACF·PACF ---------- */
var E2=(function(){var r=rng(21),a=[];for(var i=0;i<260;i++)a.push(gauss(r));return a;})();
function ar2(p1,p2){var y=[0,0];for(var t=2;t<260;t++)y.push(p1*y[t-1]+p2*y[t-2]+E2[t]);return y.slice(60);}
['p1','p2'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#p1v').textContent=(+$('#p1').value).toFixed(1);$('#p2v').textContent=(+$('#p2').value).toFixed(1);draw2();});});
function draw2(){var p1=+$('#p1').value,p2=+$('#p2').value,c=$('#c2'),W=fitC(c,340),H=340,x=c.getContext('2d');grid(x,W,H);var st=Math.abs(p2)<1&&p1+p2<1&&p2-p1<1;
  var y=ar2(p1,p2),X0=40,Y0=20,Wd=W-60,h1=90,mx=Math.max.apply(0,y.map(Math.abs))||1,sx=function(i){return X0+i/199*Wd},sy=function(v){return Y0+h1/2-v/mx*(h1/2)};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,h1);line(x,y,sx,sy,C.gfp,1.5);txt(x,'시계열 200개 시점',X0,Y0-6,C.text,11,'left',700);
  var A=acf(y,12),P=pacf(y,12),Y1=Y0+h1+40,h2=H-Y1-30,w2=(Wd-40)/2;bars(x,A,X0,Y1,w2,h2,200,'ACF (시차 1~12)');bars(x,P,X0+w2+40,Y1,w2,h2,200,'PACF (시차 1~12)');
  stamp(x,W,'예시 데이터 · AR(2)');var ci=1.96/Math.sqrt(200),cut=0;P.forEach(function(v,i){if(Math.abs(v)>ci)cut=i+1;});
  kpis($('#k2k'),[['i',A[0].toFixed(2)+' · '+A[1].toFixed(2)+' · '+A[2].toFixed(2),'1·2·3달 전과 닮음(ACF)'],['g',P[0].toFixed(2)+' · '+P[1].toFixed(2)+' · '+P[2].toFixed(2),'1·2·3달 전과 직접 닮음(PACF)'],['a','±'+ci.toFixed(3),'우연 범위(95%)'],['m',cut?'시차 '+cut:'없음','직접 닮음이 끊기는 시차']]);
  $('#ins2').innerHTML=!st?'<p class="r">이 조합(φ₁ = '+p1+', φ₂ = '+p2+')은 정상 조건을 벗어나 값이 계속 커지거나 흔들립니다. 정상 AR(2)는 φ₁ + φ₂ &lt; 1, φ₂ − φ₁ &lt; 1, |φ₂| &lt; 1이어야 합니다.</p>':Math.abs(p1)<.05&&Math.abs(p2)<.05?'<p class="a">백색잡음: ACF·PACF 막대가 거의 모두 점선 안입니다. 과거로 미래를 맞힐 단서가 없습니다.</p>':'<p class="g">ACF는 서서히 줄고, PACF는 시차 '+(cut||'–')+' 뒤로 점선 안에 들어옵니다. AR('+(Math.abs(p2)>=.05?2:1)+')의 전형적인 모양입니다.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 분해 ---------- */
function decompose(y){var n=y.length,tr=new Array(n).fill(null);for(var t=6;t<n-6;t++){var s=.5*y[t-6]+.5*y[t+6];for(var k=-5;k<=5;k++)s+=y[t+k];tr[t]=s/12;}
  var se=new Array(12).fill(0),cn=new Array(12).fill(0);for(t=0;t<n;t++)if(tr[t]!=null){se[t%12]+=y[t]-tr[t];cn[t%12]++;}se=se.map(function(v,i){return v/cn[i]});var sm=mean(se);se=se.map(function(v){return v-sm});
  var S=y.map(function(_,t){return se[t%12]}),R=y.map(function(v,t){return tr[t]==null?null:v-tr[t]-S[t]});return {tr:tr,S:S,R:R,idx:se};}
['tr3','am3'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#tr3v').textContent=(+$('#tr3').value).toFixed(1);$('#am3v').textContent=$('#am3').value;draw3();});});
function draw3(){var y=sales(72,+$('#tr3').value,+$('#am3').value,11),D=decompose(y),c=$('#c3'),W=fitC(c,420),H=420,x=c.getContext('2d');grid(x,W,H);var X0=56,Wd=W-80,rows=[['원 시계열',y,C.text],['추세',D.tr,C.gfp],['계절성',D.S,C.amber],['불규칙성',D.R,C.eye]],rh=(H-40)/4;
  rows.forEach(function(r,j){var Y0=16+j*rh,h=rh-26,v=r[1].filter(function(q){return q!=null}),lo=Math.min.apply(0,v),hi=Math.max.apply(0,v);if(j>=2){var m=Math.max(Math.abs(lo),Math.abs(hi),5);lo=-m;hi=m;}if(hi-lo<1){hi+=1;lo-=1;}
    var sx=function(i){return X0+i/71*Wd},sy=function(q){return Y0+12+h-(q-lo)/(hi-lo)*h};x.strokeStyle=C.rule;x.strokeRect(X0,Y0+12,Wd,h);txt(x,r[0],X0,Y0+6,r[2],11,'left',700);txt(x,Math.round(hi),X0-4,sy(hi),C.muted,9,'right');txt(x,Math.round(lo),X0-4,sy(lo),C.muted,9,'right');
    x.strokeStyle=r[2];x.lineWidth=1.8;x.beginPath();var st=false;r[1].forEach(function(q,i){if(q==null){st=false;return;}st?x.lineTo(sx(i),sy(q)):x.moveTo(sx(i),sy(q));st=true;});x.stroke();x.lineWidth=1;});
  for(var yr=0;yr<=6;yr++)txt(x,(yr+1)+'년',X0+(yr*12+6)/71*Wd,H-8,C.muted,9,'center');stamp(x,W,'예시 데이터');
  var dec=D.idx[11],peak=D.idx.indexOf(Math.max.apply(0,D.idx)),low=D.idx.indexOf(Math.min.apply(0,D.idx)),tv=D.tr.filter(function(q){return q!=null});
  kpis($('#k3k'),[['g',((tv[tv.length-1]-tv[0])/(tv.length-1)).toFixed(2),'추정한 추세(월당)'],['a',MON[peak]+' +'+D.idx[peak].toFixed(1),'가장 잘 팔리는 달'],['i',MON[low]+' '+D.idx[low].toFixed(1),'가장 안 팔리는 달'],['m',sd(D.R.filter(function(q){return q!=null})).toFixed(1),'우연한 흔들림의 크기']]);
  $('#ins3').innerHTML=+$('#am3').value===0?'<p class="a">계절 진폭 0: 계절성 줄이 거의 평평합니다(잡음에서 나온 작은 흔들림만 남음).</p>':'<p class="g">분해 결과 '+MON[peak]+'이 평균보다 약 '+D.idx[peak].toFixed(1)+' 높고, '+MON[low]+'이 약 '+Math.abs(D.idx[low]).toFixed(1)+' 낮습니다. 추세는 월당 약 '+((tv[tv.length-1]-tv[0])/(tv.length-1)).toFixed(2)+'로 추정됐습니다(설정값 '+$('#tr3').value+').</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 차분 ---------- */
var srK='lin',dK=0,SER={lin:(function(){var r=rng(31),a=[];for(var t=0;t<160;t++)a.push(.8*t+gauss(r)*5);return a;})(),quad:(function(){var r=rng(32),a=[],v=0,s=0;for(var t=0;t<160;t++){s+=.04;v+=s+gauss(r)*1.2;a.push(v+gauss(r)*3);}return a;})(),stat:(function(){var r=rng(33),a=[],e=0;for(var t=0;t<160;t++){e=.4*e+gauss(r)*5;a.push(50+e);}return a;})()};
function diff(y,d){for(var k=0;k<d;k++)y=y.slice(1).map(function(v,i){return v-y[i]});return y;}
LAB.radio('#srBtns',[['lin','선형 추세','s0'],['quad','가속 추세','s1'],['stat','이미 정상','s2']],'lin',function(v){srK=v;draw4();});
LAB.radio('#dfBtns',[['0','0','d0'],['1','1','d1'],['2','2','d2']],'0',function(v){dK=+v;draw4();});
function draw4(){var y=diff(SER[srK],dK),c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=46,Y0=24,Wd=(W-110)*.62,Hh=H-60,lo=Math.min.apply(0,y),hi=Math.max.apply(0,y),sx=function(i){return X0+i/(y.length-1)*Wd},sy=function(v){return Y0+Hh-(v-lo)/(hi-lo||1)*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);line(x,y,sx,sy,C.gfp,1.5);var q=Math.floor(y.length/4),ms=[];for(var k=0;k<4;k++){var seg=y.slice(k*q,(k+1)*q),m=mean(seg);ms.push([m,sd(seg)]);x.strokeStyle=C.amber;x.lineWidth=2.5;x.beginPath();x.moveTo(sx(k*q),sy(m));x.lineTo(sx((k+1)*q-1),sy(m));x.stroke();x.lineWidth=1;}
  txt(x,(dK?dK+'차 차분':'원 시계열')+' · 주황 = 네 구간의 평균',X0,Y0-8,C.text,11,'left',700);txt(x,Math.round(hi),X0-4,sy(hi),C.muted,9,'right');txt(x,Math.round(lo),X0-4,sy(lo),C.muted,9,'right');
  var A=acf(y,10);bars(x,A,X0+Wd+40,Y0+10,W-X0-Wd-60,Hh-20,y.length,'ACF');stamp(x,W,'예시 데이터');
  var spread=Math.max.apply(0,ms.map(function(m){return m[0]}))-Math.min.apply(0,ms.map(function(m){return m[0]})),avgSd=mean(ms.map(function(m){return m[1]})),ok=spread<avgSd*.6;
  kpis($('#k4k'),[['i',ms.map(function(m){return m[0].toFixed(1)}).join(' · '),'네 구간 평균'],['a',ms.map(function(m){return m[1].toFixed(1)}).join(' · '),'네 구간 표준편차'],[A[0]<-.35?'r':ok?'g':'r',A[0].toFixed(2),'1달 전과 닮음(ACF)'],[ok?'g':'r',ok?'평균이 거의 일정':'평균이 움직임','잔잔한가(정상성)']]);
  $('#ins4').innerHTML=A[0]<-.35&&dK>0?'<p class="r">ACF 시차 1이 '+A[0].toFixed(2)+'로 크게 음수입니다. 필요 이상으로 차분해 오히려 새 패턴을 만들었습니다(과도한 차분).</p>':ok?'<p class="g">d = '+dK+': 네 구간 평균이 비슷하고 ACF가 빨리 줄어듭니다. 정상 시계열로 볼 만합니다.</p>':'<p class="a">d = '+dK+': 구간 평균이 '+ms[0][0].toFixed(1)+' → '+ms[3][0].toFixed(1)+'로 움직입니다. 아직 비정상입니다. 차분을 한 번 더 해 보세요.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ AR·ARIMA ---------- */
function solve(A,b){var n=b.length,M=A.map(function(r,i){return r.concat([b[i]])});for(var c=0;c<n;c++){var p=c;for(var r=c+1;r<n;r++)if(Math.abs(M[r][c])>Math.abs(M[p][c]))p=r;var t=M[c];M[c]=M[p];M[p]=t;for(r=0;r<n;r++){if(r===c)continue;var f=M[r][c]/M[c][c];for(var j=c;j<=n;j++)M[r][j]-=f*M[c][j];}}return M.map(function(r,i){return r[n]/r[i]});}
function fitAR(y,p){var X=[],Y=[];for(var t=p;t<y.length;t++){var row=[1];for(var k=1;k<=p;k++)row.push(y[t-k]);X.push(row);Y.push(y[t]);}var q=p+1,A=[],b=[];for(var i=0;i<q;i++){A.push([]);b.push(0);for(var j=0;j<q;j++){var s=0;X.forEach(function(r){s+=r[i]*r[j]});A[i].push(s);}X.forEach(function(r,k){b[i]+=r[i]*Y[k]});}
  var w=solve(A,b),sse=0;X.forEach(function(r,k){var e=Y[k]-r.reduce(function(s,v,j){return s+v*w[j]},0);sse+=e*e;});var n=Y.length;return {w:w,aic:n*Math.log(sse/n)+2*q};}
function fcAR(y,w,p,h){var z=y.slice();for(var i=0;i<h;i++){var t=z.length,v=w[0];for(var k=1;k<=p;k++)v+=w[k]*z[t-k];z.push(v);}return z.slice(y.length);}
function arima(y,p,d,h){if(!d){var F0=fitAR(y,p);return {f:fcAR(y,F0.w,p,h),aic:F0.aic};}var dd=y.slice(1).map(function(v,i){return v-y[i]}),F=fitAR(dd,p),fd=fcAR(dd,F.w,p,h),last=y[y.length-1],out=[];fd.forEach(function(v){last+=v;out.push(last);});return {f:out,aic:F.aic};}
function mape(a,f){return mean(a.map(function(v,i){return Math.abs((v-f[i])/v)}))*100;}
var TRN=Y72.slice(0,60),TST=Y72.slice(60),d5=1;
LAB.radio('#d5Btns',[['0','0','e0'],['1','1','e1']],'1',function(v){d5=+v;draw5();});
$('#pp').addEventListener('input',function(){$('#ppv').textContent=this.value;draw5();});
function draw5(){var p=+$('#pp').value,R=arima(TRN,p,d5,12),c=$('#c5'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=46,Y0=24,Wd=(W-110)*.68,Hh=H-60,lo=70,hi=210,sx=function(i){return X0+i/71*Wd},sy=function(v){return Y0+Hh-(v-lo)/(hi-lo)*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[100,150,200].forEach(function(v){txt(x,v,X0-4,sy(v),C.muted,9,'right');});x.fillStyle='rgba(241,182,70,.08)';x.fillRect(sx(60),Y0,sx(71)-sx(60),Hh);txt(x,'시험 12개월',sx(60)+4,Y0+12,C.amber,10);
  line(x,Y72,sx,sy,C.text,1.5);x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();x.moveTo(sx(59),sy(TRN[59]));R.f.forEach(function(v,i){x.lineTo(sx(60+i),sy(v));});x.stroke();x.lineWidth=1;
  for(var yr=0;yr<6;yr++)txt(x,(yr+1)+'년',sx(yr*12+6),Y0+Hh+12,C.muted,9,'center');txt(x,'— 실제  — ARIMA('+p+', '+d5+', 0) 예측',X0+6,Y0-8,C.muted,11);
  var X1=X0+Wd+40,W1=W-X1-14,aics=[];for(var q=1;q<=12;q++)aics.push(arima(TRN,q,d5,1).aic);var amin=Math.min.apply(0,aics),amax=Math.max.apply(0,aics),bw=W1/12;x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);
  aics.forEach(function(a,i){var h=8+(a-amin)/(amax-amin||1)*(Hh-16);x.fillStyle=i+1===p?C.amber:a===amin?C.gfp:'rgba(157,155,184,.45)';x.fillRect(X1+i*bw+1,Y0+Hh-h,bw-2,h);if(i%3===0||i===11)txt(x,String(i+1),X1+(i+.5)*bw,Y0+Hh+12,C.muted,9,'center');});txt(x,'p별 AIC(낮을수록 좋음)',X1,Y0-8,C.text,11,'left',700);
  stamp(x,W,'예시 데이터');var M=mape(TST,R.f),bestP=aics.indexOf(amin)+1;
  kpis($('#k5k'),[[M<3?'g':M<6?'a':'r',M.toFixed(2)+'%','12개월 예측이 빗나간 %(MAPE)'],['i',R.aic.toFixed(1),'AIC (p = '+p+')'],['m','p = '+bestP,'점수(AIC)가 가장 좋은 p'],['a',Math.round(R.f[11])+' / '+Math.round(TST[11]),'12월 예측 / 실제']]);
  $('#ins5').innerHTML=d5===0?'<p class="r">d = 0: 추세를 지우지 않고 AR을 맞춰, 예측이 평균 쪽으로 눌립니다. MAPE '+M.toFixed(2)+'%.</p>':p>=12?'<p class="g">p = 12: 12개월 전 값이 들어와 12월의 솟음을 따라갑니다. MAPE '+M.toFixed(2)+'%.</p>':'<p class="a">ARIMA('+p+', 1, 0): 추세는 따라가지만 12월 계절성은 '+(Math.abs(R.f[11]-TST[11])>8?'놓칩니다':'어느 정도 따라갑니다')+'. MAPE '+M.toFixed(2)+'%.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결 ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:false,drawMargin:.05,max:8,bigGap:100,metric:'시험 12개월 MAPE(%) — 작을수록 좋음',fmt:function(v){return v.toFixed(2)+'%'},
  run:function(){var best=null;for(var p=1;p<=6;p++){var R=arima(TRN,p,1,12);if(!best||R.aic<best.aic)best={p:p,f:R.f,aic:R.aic};}
    var g=(mean(TRN.slice(48))-mean(TRN.slice(36,48))),sn=TST.map(function(_,i){return TRN[48+i]+g});this.info={p:best.p,g:g,fDec:best.f[11],rDec:sn[11],aDec:TST[11]};return {fly:mape(TST,best.f),robo:mape(TST,sn)};},
  report:function(r){var I=this.info;return '초파리 연구원이 AIC로 고른 차수는 p = '+I.p+'이고, 주판봇은 작년 같은 달에 연간 증가분('+I.g.toFixed(1)+')을 더했어요. 마지막 12월(실제 '+Math.round(I.aDec)+')을 ARIMA는 '+Math.round(I.fDec)+', 주판봇은 '+Math.round(I.rDec)+'으로 예측했어요.';},
  verdict:function(r,res){return '계절성이 뚜렷하면 "작년 같은 달"이 강한 기준선이다. 복잡한 모델은 이 기준선부터 넘어야 한다. '+(res==='R'?'주판봇 승.':res==='F'?'초파리 승.':'이번 판은 나눠 갖는다.');}});
