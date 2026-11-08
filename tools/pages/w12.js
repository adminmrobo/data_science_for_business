/* 12주차 · 효과적인 비즈니스 데이터 시각화 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
function mean(a){return a.reduce(function(s,v){return s+v},0)/a.length}
function sdv(a){var m=mean(a);return Math.sqrt(mean(a.map(function(v){return (v-m)*(v-m)})));}
function median(a){var s=a.slice().sort(function(x,y){return x-y}),n=s.length;return n%2?s[(n-1)/2]:(s[n/2-1]+s[n/2])/2;}
function quant(a,q){var s=a.slice().sort(function(x,y){return x-y}),p=(s.length-1)*q,i=Math.floor(p);return s[i]+(s[Math.min(i+1,s.length-1)]-s[i])*(p-i);}
function mom(a,k){var m=mean(a),s=sdv(a);return mean(a.map(function(v){return Math.pow((v-m)/s,k)}));}
function fmt(v,d){return v.toLocaleString('ko-KR',{maximumFractionDigits:d==null?0:d,minimumFractionDigits:d==null?0:d});}
function hist(x,vals,X0,Y0,W,H,lo,hi,B,col){var c=new Array(B).fill(0);vals.forEach(function(v){var b=Math.floor((v-lo)/(hi-lo)*B);if(b>=0&&b<B)c[b]++;});var mx=Math.max.apply(0,c)||1,bw=W/B;c.forEach(function(n,i){var h=n/mx*H;x.fillStyle=col;x.fillRect(X0+i*bw+1,Y0+H-h,bw-2,h);});return mx;}
function vline(x,X,Y0,H,col,label,dy){x.strokeStyle=col;x.lineWidth=2;x.beginPath();x.moveTo(X,Y0);x.lineTo(X,Y0+H);x.stroke();x.lineWidth=1;txt(x,label,X+4,Y0+10+(dy||0),col,11,'left',700);}

/* ---------- 히어로 소품 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var X0=W*.3,Y0=H*.06,w=W*.46,h=H*.26,B=14;for(var i=0;i<B;i++){var u=(i+.5)/B,v=Math.pow(u*4,1.2)*Math.exp(-u*5)*1.9;x.fillStyle=i<3?C.gfp:'rgba(130,184,255,.7)';x.fillRect(X0+i*w/B+1,Y0+h-v*h,w/B-2,v*h);}
  var cx=X0+w*.5,cy=Y0+h+H*.06,tilt=.08+.04*Math.sin(t);x.strokeStyle='#d8c08a';x.lineWidth=3;x.beginPath();x.moveTo(cx-w*.4,cy+tilt*w*.4);x.lineTo(cx+w*.4,cy-tilt*w*.4);x.stroke();x.fillStyle='#d8c08a';x.beginPath();x.moveTo(cx,cy);x.lineTo(cx-8,cy+14);x.lineTo(cx+8,cy+14);x.fill();x.lineWidth=1;});

/* ---------- ① 대표값 ---------- */
var PAY=[['카드',46],['간편결제',61],['계좌이체',18],['현금',9]],pay=0;
$('#heroMean').textContent='450만 원';
LAB.radio('#mdBtns',[['0','온라인몰','m0'],['1','오프라인 매장','m1']],'0',function(v){pay=+v;draw1();});
$('#s5').addEventListener('input',function(){$('#s5v').textContent=fmt(+this.value);draw1();});
function draw1(){var s=[200,300,350,400,+$('#s5').value],m=mean(s),md=median(s),c=$('#c1'),W=fitC(c,260),H=260,x=c.getContext('2d');grid(x,W,H);var X0=40,Y0=40,Wd=(W-110)*.62,Hh=H-80,hi=3100,sx=function(v){return X0+v/hi*Wd};
  x.strokeStyle=C.rule;x.beginPath();x.moveTo(X0,Y0+Hh/2);x.lineTo(X0+Wd,Y0+Hh/2);x.stroke();[0,1000,2000,3000].forEach(function(v){txt(x,fmt(v),sx(v),Y0+Hh/2+18,C.muted,10,'center');});
  s.forEach(function(v,i){x.fillStyle=i===4?C.amber:C.info;x.beginPath();x.arc(sx(v),Y0+Hh/2,8,0,7);x.fill();});
  vline(x,sx(md),Y0,Hh/2-12,C.gfp,'중앙값 '+fmt(md),0);vline(x,sx(m),Y0+Hh/2+26,Hh/2-26,C.eye,'평균 '+fmt(m),-4);txt(x,'월급(만 원)',X0,Y0-14,C.text,11,'left',700);
  var P=pay===0?PAY:[['카드',58],['간편결제',22],['계좌이체',4],['현금',31]],X1=X0+Wd+40,W1=W-X1-14,mx=Math.max.apply(0,P.map(function(p){return p[1]})),bh=(Hh)/P.length;
  P.forEach(function(p,i){var w=p[1]/mx*(W1-70);x.fillStyle=p[1]===mx?C.gfp:'rgba(157,155,184,.5)';x.fillRect(X1+60,Y0+i*bh+4,w,bh-10);txt(x,p[0],X1+56,Y0+i*bh+bh/2,C.muted,10,'right');txt(x,p[1]+'',X1+64+w,Y0+i*bh+bh/2,C.text,10);});
  txt(x,'결제 방식(건, 예시) — 초록 = 최빈값',X1,Y0-14,C.text,11,'left',700);stamp(x,W,'교안 예 + 예시');
  var mode=P.filter(function(p){return p[1]===mx})[0][0];
  kpis($('#k1k'),[['r',fmt(m)+'만 원','평균'],['g',fmt(md)+'만 원','중앙값'],['a',s.filter(function(v){return v<m}).length+'명 / 5명','평균보다 적게 받는 사람'],['i',mode,'결제 방식의 최빈값']]);
  $('#ins1').innerHTML=m>md*1.2?'<p class="r">평균 '+fmt(m)+'만 원은 다섯 명 중 '+s.filter(function(v){return v<m}).length+'명보다 높습니다. 한 사람이 평균을 끌고 갔고, 중앙값('+fmt(md)+'만 원)은 꿈쩍하지 않았습니다.</p>':'<p class="g">다섯 번째 월급이 다른 사람과 비슷하면 평균('+fmt(m)+')과 중앙값('+fmt(md)+')이 가까워집니다.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 분산도 ---------- */
var SA=(function(){var r=rng(61),a=[];for(var i=0;i<400;i++)a.push(50000+gauss(r)*10000);return a;})(),SB=(function(){var r=rng(62),a=[];for(var i=0;i<400;i++)a.push(80000+gauss(r)*15000);return a;})(),un=1;
LAB.radio('#unBtns',[['1','달러','u0'],['1000','천 달러','u1']],'1',function(v){un=+v;draw2();});
function draw2(){var A=SA.map(function(v){return v/un}),B=SB.map(function(v){return v/un}),c=$('#c2'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=40,Y0=30,Wd=W-70,Hh=(H-80)/2,lo=0,hi=140000/un,sx=function(v){return X0+(v-lo)/(hi-lo)*Wd};
  [[A,C.info,'A 회사',0],[B,C.amber,'B 회사',1]].forEach(function(g){var y0=Y0+g[3]*(Hh+30),m=mean(g[0]),s=sdv(g[0]);hist(x,g[0],X0,y0,Wd,Hh,lo,hi,40,g[1]);x.strokeStyle=C.text;x.lineWidth=2;x.beginPath();x.moveTo(sx(m-s),y0+Hh+6);x.lineTo(sx(m+s),y0+Hh+6);x.stroke();x.lineWidth=1;x.fillStyle=C.text;x.beginPath();x.arc(sx(m),y0+Hh+6,4,0,7);x.fill();txt(x,g[2]+' · 평균 '+fmt(m,un>1?1:0)+' ± '+fmt(s,un>1?1:0),X0+4,y0+8,g[1],11,'left',700);});
  [0,35000,70000,105000,140000].forEach(function(v){txt(x,fmt(v/un),sx(v/un),H-6,C.muted,10,'center');});stamp(x,W,'예시 데이터 · 교안의 평균·표준편차');
  var vA=Math.pow(sdv(A),2),vB=Math.pow(sdv(B),2);
  kpis($('#k2k'),[['m',fmt(vA)+' · '+fmt(vB),'분산 A · B ('+(un>1?'천 달러':'달러')+'²)'],['i',fmt(sdv(A),un>1?1:0)+' · '+fmt(sdv(B),un>1?1:0),'표준편차 A · B'],['a',(sdv(A)/mean(A)).toFixed(3)+' · '+(sdv(B)/mean(B)).toFixed(3),'변동계수 A · B'],['g','0.200 · 0.188','교안 값으로 계산한 CV']]);
  $('#ins2').innerHTML='<p class="'+(un>1?'g':'a')+'">'+(un>1?'천 달러로 바꾸자 분산은 100만 분의 1로 줄었지만 변동계수는 그대로입니다.':'달러 단위의 분산은 억 단위라 읽기 어렵습니다. 단위를 바꿔 보세요.')+' 표준편차는 B가 크지만, 자기 평균에 비하면 A가 더 흩어져 있습니다(CV '+(sdv(A)/mean(A)).toFixed(3)+' &gt; '+(sdv(B)/mean(B)).toFixed(3)+').</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 왜도·첨도 ---------- */
var ZN=(function(){var r=rng(71),a=[];for(var i=0;i<1000;i++)a.push(gauss(r));return a;})(),lg=false;
function spend(sig,Z){return (Z||ZN).map(function(z){return 3*Math.exp(sig*z)});}
LAB.radio('#lgBtns',[['raw','원래','l0'],['log','로그','l1']],'raw',function(v){lg=v==='log';draw3();});
$('#sg').addEventListener('input',function(){$('#sgv').textContent=(+this.value).toFixed(1);draw3();});
function draw3(){var sig=+$('#sg').value,raw=spend(sig),v=lg?raw.map(Math.log):raw,c=$('#c3'),W=fitC(c,280),H=280,x=c.getContext('2d');grid(x,W,H);var X0=40,Y0=30,Wd=W-70,Hh=H-70,lo=lg?Math.min.apply(0,v):0,hi=lg?Math.max.apply(0,v):quant(v,.99)*1.05,sx=function(q){return X0+(q-lo)/(hi-lo)*Wd};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);hist(x,v,X0,Y0,Wd,Hh,lo,hi,40,'rgba(130,184,255,.6)');var m=mean(v),md=median(v);vline(x,sx(md),Y0,Hh,C.gfp,'중앙값',0);vline(x,sx(m),Y0,Hh,C.eye,'평균',16);
  [0,.25,.5,.75,1].forEach(function(f){var q=lo+f*(hi-lo);txt(x,lg?q.toFixed(1):fmt(q,1),sx(q),Y0+Hh+12,C.muted,10,'center');});txt(x,lg?'log(결제액)':'결제액(만 원, 상위 1% 밖은 잘림)',X0+Wd/2,H-10,C.muted,11,'center');stamp(x,W,'예시 데이터');
  var sk=mom(v,3),ku=mom(v,4);
  kpis($('#k3k'),[['r',fmt(mean(raw),1)+'만 원','평균 결제액'],['g',fmt(median(raw),1)+'만 원','중앙값 결제액'],[Math.abs(sk)<.3?'g':'a',sk.toFixed(2),'왜도 '+(lg?'(로그 후)':'')],[ku>4?'r':'i',ku.toFixed(2),'첨도(정규 = 3)']]);
  $('#ins3').innerHTML=lg?'<p class="g">로그로 바꾸자 왜도가 '+sk.toFixed(2)+'로 0 근처에 왔습니다. 평균과 중앙값이 겹칩니다.</p>':sig<=.2?'<p class="g">거의 대칭: 평균 ≈ 중앙값, 왜도 '+sk.toFixed(2)+', 첨도 '+ku.toFixed(2)+'.</p>':'<p class="a">오른쪽 꼬리: 평균('+fmt(mean(raw),1)+')이 중앙값('+fmt(median(raw),1)+')보다 '+pct(mean(raw)/median(raw)-1,0)+' 큽니다. 왜도 '+sk.toFixed(2)+', 첨도 '+ku.toFixed(2)+'.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 상관 ---------- */
var Z1=(function(){var r=rng(81),a=[];for(var i=0;i<120;i++)a.push([gauss(r),gauss(r)]);return a;})(),cu=1,ol=false;
LAB.radio('#cuBtns',[['1','원','c0'],['10000','만 원','c1']],'1',function(v){cu=+v;draw4();});
LAB.radio('#olBtns',[['off','없음','o0'],['on','큰손 1명','o1']],'off',function(v){ol=v==='on';draw4();});
$('#rr').addEventListener('input',function(){$('#rrv').textContent=(+this.value).toFixed(1);draw4();});
function corr(X,Y){var mx=mean(X),my=mean(Y),c=0;X.forEach(function(v,i){c+=(v-mx)*(Y[i]-my);});c/=X.length;return {cov:c,r:c/(sdv(X)*sdv(Y))};}
function draw4(){var r=+$('#rr').value,P=Z1.map(function(z){var u=z[0],v=r*z[0]+Math.sqrt(1-r*r)*z[1];return [Math.max(1,20+u*7),Math.max(10000,300000+v*90000)];});if(ol)P.push([62,2400000]);
  var X=P.map(function(p){return p[0]}),Y=P.map(function(p){return p[1]/cu}),R=corr(X,Y),c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=70,Y0=24,Wd=W-100,Hh=H-60,xh=66,yh=ol?2600000:800000,sx=function(v){return X0+v/xh*Wd},sy=function(v){return Y0+Hh-v*cu/yh*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,20,40,60].forEach(function(v){txt(x,v+'회',sx(v),Y0+Hh+12,C.muted,10,'center');});(ol?[0,1000000,2000000]:[0,200000,400000,600000,800000]).forEach(function(v){txt(x,fmt(v/cu),X0-4,Y0+Hh-v/yh*Hh,C.muted,10,'right');});
  P.forEach(function(p,i){x.fillStyle=ol&&i===P.length-1?C.eye:'rgba(130,184,255,.75)';x.beginPath();x.arc(sx(p[0]),sy(p[1]/cu),ol&&i===P.length-1?7:3.5,0,7);x.fill();});
  txt(x,'가로: 월 앱 사용 횟수 · 세로: 월 거래금액('+(cu>1?'만 원':'원')+')',X0+6,Y0+12,C.muted,11);stamp(x,W,'예시 데이터');
  var R0=corr(X.slice(0,120),Y.slice(0,120)),lab=Math.abs(R.r)>=.7?'강함':Math.abs(R.r)>=.3?'중간':'약함';
  kpis($('#k4k'),[['m',fmt(R.cov),'공분산('+(cu>1?'회·만 원':'회·원')+')'],[Math.abs(R.r)>=.3?'g':'a',R.r.toFixed(3),'상관계수 r'],['i',lab+(R.r<0?'(음)':R.r>0?'(양)':''),'교안 기준 해석'],[ol?'r':'g',ol?R0.r.toFixed(3)+' → '+R.r.toFixed(3):'—','큰손 1명의 영향']]);
  $('#ins4').innerHTML=ol?'<p class="r">점 하나(사용 62회, 240만 원)가 상관계수를 '+R0.r.toFixed(3)+' → '+R.r.toFixed(3)+'로 바꿨습니다. 이상치를 빼고 다시 계산해 보세요.</p>':'<p class="g">공분산은 '+fmt(R.cov)+'('+(cu>1?'만 원':'원')+' 단위). 단위를 바꾸면 이 숫자는 크게 달라지지만 r = '+R.r.toFixed(3)+'은 그대로입니다.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ 차트 선택 ---------- */
var DSETS={time:{n:'월별 매출(12개월)',v:[82,79,88,91,95,99,104,101,97,103,112,128],l:['1','2','3','4','5','6','7','8','9','10','11','12']},
  share:{n:'자산 배분(교안)',v:[40,30,15,10,5],l:['주식','채권','부동산','현금','원자재']},
  rel:{n:'광고비-매출(20개 지점)',pts:(function(){var r=rng(91),a=[];for(var i=0;i<20;i++){var ad=2+r()*8;a.push([ad,20+ad*6+gauss(r)*6]);}return a;})()},
  dist:{n:'부서별 급여(3개 부서)',g:(function(){var r=rng(92),o=[];[[320,40],[360,90],[300,30]].forEach(function(p,k){var a=[];for(var i=0;i<40;i++)a.push(p[0]+gauss(r)*p[1]);if(k===1){a.push(780);a.push(720);}o.push(a);});return o;})(),l:['영업','개발','지원']},
  mat:{n:'기술주 5종 상관(예시)',m:[[1,.7,.6,.5,.4],[.7,1,.8,.6,.5],[.6,.8,1,.7,.3],[.5,.6,.7,1,.2],[.4,.5,.3,.2,1]],l:['A','B','C','D','E']}};
var FIT={time:{line:['g','시간 흐름과 추세가 바로 보입니다. 교안이 권하는 시간 추이 차트.'],bar:['a','월별 값 비교는 되지만 흐름은 선보다 덜 보입니다.'],pie:['r','12조각이 비슷해 읽을 수 없고 순서 정보도 사라집니다.'],scatter:['a','점만 찍혀 흐름이 끊겨 보입니다. 선으로 잇는 편이 낫습니다.'],box:['r','12개월을 한 상자로 요약하면 추세가 사라집니다.'],heat:['r','1차원 시계열을 색으로만 보면 크기를 읽기 어렵습니다.']},
  share:{line:['r','항목 사이에 순서·시간이 없는데 선으로 이으면 추세처럼 오해됩니다.'],bar:['g','정확한 비교가 필요하면 막대가 가장 좋습니다(교안).'],pie:['g','5개 항목, 차이가 뚜렷해 전체 대비 비율이 한눈에 보입니다.'],scatter:['r','범주 하나에 숫자 하나뿐이라 산점도로는 관계가 없습니다.'],box:['r','5개 값의 분포는 이 데이터의 메시지가 아닙니다.'],heat:['a','색만으로 비율을 읽기 어렵습니다.']},
  rel:{line:['r','지점 사이에 순서가 없는데 선으로 이으면 엉뚱한 지그재그가 됩니다.'],bar:['a','지점별 막대 두 개로는 관계가 잘 보이지 않습니다.'],pie:['r','두 수치의 관계는 비율로 표현할 수 없습니다.'],scatter:['g','두 수치 변수의 관계와 이상치를 보는 기본 차트입니다(교안).'],box:['a','각 변수의 분포만 보이고 둘의 관계는 사라집니다.'],heat:['a','점이 적어 히트맵은 듬성듬성합니다.']},
  dist:{line:['r','부서 사이에 순서가 없어 선은 의미가 없습니다.'],bar:['a','평균만 보여 분포와 이상치(개발팀 고액 2명)가 숨습니다.'],pie:['r','급여 합계의 비율은 이 질문(분포 비교)과 맞지 않습니다.'],scatter:['a','점은 보이지만 사분위·이상치 기준이 없습니다.'],box:['g','여러 그룹의 분포·중앙값·이상치를 한 번에 비교합니다(교안).'],heat:['r','그룹 분포를 색 칸으로 바꾸면 정보가 줄어듭니다.']},
  mat:{line:['r','행렬을 선으로 그리면 25개 칸의 관계가 엉킵니다.'],bar:['a','25개 막대는 너무 많고 구조가 안 보입니다.'],pie:['r','상관계수는 비율이 아닙니다.'],scatter:['r','상관 행렬 자체는 산점도의 재료가 아닙니다.'],box:['r','행렬의 분포는 메시지가 아닙니다.'],heat:['g','변수 쌍마다의 상관을 색 강도로 한눈에. sns.heatmap(annot = True).']}};
var ds='time',ct='line',CNAME={line:'선',bar:'막대',pie:'파이',scatter:'산점도',box:'박스 플롯',heat:'히트맵'};
LAB.radio('#dsBtns',[['time','월별 매출','d0'],['share','자산 배분','d1'],['rel','광고비-매출','d2'],['dist','부서별 급여','d3'],['mat','상관 행렬','d4']],'time',function(v){ds=v;draw5();});
LAB.radio('#ctBtns',[['line','선','t0'],['bar','막대','t1'],['pie','파이','t2'],['scatter','산점도','t3'],['box','박스','t4'],['heat','히트맵','t5']],'line',function(v){ct=v;draw5();});
function series(){var D=DSETS[ds];if(D.v)return {v:D.v,l:D.l};if(D.pts)return {v:D.pts.map(function(p){return p[1]}),l:D.pts.map(function(_,i){return String(i+1)})};if(D.g)return {v:D.g.map(mean),l:D.l};var v=[],l=[];D.m.forEach(function(r,i){r.forEach(function(q,j){v.push(q);l.push(D.l[i]+D.l[j]);});});return {v:v,l:l};}
function draw5(){var c=$('#c5'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=50,Y0=30,Wd=W-80,Hh=H-70,D=DSETS[ds],S=series(),cols=[C.info,C.gfp,C.amber,C.eye,C.stain];
  txt(x,D.n+' → '+CNAME[ct],X0,Y0-12,C.text,12,'left',700);
  if(ct==='pie'){var cx=X0+Wd/2,cy=Y0+Hh/2,R=Math.min(Wd,Hh)/2-4,tot=S.v.reduce(function(a,b){return a+Math.max(0,b)},0),a0=-Math.PI/2;S.v.forEach(function(v,i){var a1=a0+Math.max(0,v)/tot*Math.PI*2;x.fillStyle=cols[i%5];x.globalAlpha=.75;x.beginPath();x.moveTo(cx,cy);x.arc(cx,cy,R,a0,a1);x.closePath();x.fill();x.globalAlpha=1;if(S.v.length<=6){var am=(a0+a1)/2;txt(x,S.l[i]+' '+v,cx+Math.cos(am)*R*.65,cy+Math.sin(am)*R*.65,'#111',11,'center',700);}a0=a1;});}
  else if(ct==='heat'){if(D.m){var n=D.m.length,cs=Math.min(Wd,Hh)/n;D.m.forEach(function(r,i){r.forEach(function(q,j){x.fillStyle='rgba(130,184,255,'+(.1+q*.85)+')';x.fillRect(X0+j*cs,Y0+i*cs,cs-2,cs-2);txt(x,q.toFixed(1),X0+(j+.5)*cs,Y0+(i+.5)*cs,'#111',11,'center',700);});txt(x,D.l[i],X0-6,Y0+(i+.5)*cs,C.muted,10,'right');txt(x,D.l[i],X0+(i+.5)*cs,Y0+n*cs+10,C.muted,10,'center');});}
    else{var mx=Math.max.apply(0,S.v),mn=Math.min.apply(0,S.v),cw=Wd/S.v.length;S.v.forEach(function(v,i){x.fillStyle='rgba(241,182,70,'+(.1+.85*(v-mn)/(mx-mn||1))+')';x.fillRect(X0+i*cw,Y0+Hh/2-20,cw-1,40);});}}
  else if(ct==='box'){var groups=D.g?D.g:[S.v],lab=D.g?D.l:['전체'],all=[].concat.apply([],groups),lo=Math.min.apply(0,all),hi=Math.max.apply(0,all),sy=function(v){return Y0+Hh-(v-lo)/(hi-lo||1)*Hh},gw=Wd/groups.length;
    groups.forEach(function(g,k){var q1=quant(g,.25),q2=quant(g,.5),q3=quant(g,.75),iq=q3-q1,inn=g.filter(function(v){return v>=q1-1.5*iq&&v<=q3+1.5*iq}),bx=X0+(k+.5)*gw,bw=Math.min(60,gw*.4);x.fillStyle='rgba(130,184,255,.25)';x.fillRect(bx-bw/2,sy(q3),bw,sy(q1)-sy(q3));x.strokeStyle=C.info;x.strokeRect(bx-bw/2,sy(q3),bw,sy(q1)-sy(q3));x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.moveTo(bx-bw/2,sy(q2));x.lineTo(bx+bw/2,sy(q2));x.stroke();x.lineWidth=1;
      x.strokeStyle=C.text;x.beginPath();x.moveTo(bx,sy(q3));x.lineTo(bx,sy(Math.max.apply(0,inn)));x.moveTo(bx,sy(q1));x.lineTo(bx,sy(Math.min.apply(0,inn)));x.stroke();g.filter(function(v){return inn.indexOf(v)<0}).forEach(function(v){x.fillStyle=C.eye;x.beginPath();x.arc(bx,sy(v),4,0,7);x.fill();});txt(x,lab[k],bx,Y0+Hh+12,C.muted,10,'center');});}
  else if(ct==='scatter'&&D.pts){var sx=function(v){return X0+v/11*Wd},sy2=function(v){return Y0+Hh-(v-10)/(90-10)*Hh};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);D.pts.forEach(function(p){x.fillStyle=C.info;x.beginPath();x.arc(sx(p[0]),sy2(p[1]),5,0,7);x.fill();});txt(x,'광고비(천만 원)',X0+Wd/2,Y0+Hh+12,C.muted,10,'center');txt(x,'매출(억 원)',X0+4,Y0+10,C.muted,10);}
  else{var mx2=Math.max.apply(0,S.v),mn2=Math.min(0,Math.min.apply(0,S.v)),n2=S.v.length,sx3=function(i){return X0+(i+.5)/n2*Wd},sy3=function(v){return Y0+Hh-(v-mn2)/(mx2-mn2||1)*Hh};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);
    if(ct==='bar')S.v.forEach(function(v,i){x.fillStyle=C.info;x.fillRect(sx3(i)-Wd/n2*.35,sy3(v),Wd/n2*.7,sy3(mn2)-sy3(v));});
    else if(ct==='line'){x.strokeStyle=C.gfp;x.lineWidth=2.5;x.beginPath();S.v.forEach(function(v,i){i?x.lineTo(sx3(i),sy3(v)):x.moveTo(sx3(i),sy3(v));});x.stroke();x.lineWidth=1;}
    else S.v.forEach(function(v,i){x.fillStyle=C.info;x.beginPath();x.arc(sx3(i),sy3(v),4,0,7);x.fill();});
    if(n2<=25)S.l.forEach(function(l,i){if(n2<=12||i%5===0)txt(x,l,sx3(i),Y0+Hh+12,C.muted,9,'center');});}
  var f=FIT[ds][ct],best=Object.keys(FIT[ds]).filter(function(k){return FIT[ds][k][0]==='g'}).map(function(k){return CNAME[k]}).join(' · ');
  x.fillStyle=f[0]==='g'?C.gfp:f[0]==='a'?C.amber:C.eye;x.font='700 13px '+(LAB.FONT||'sans-serif');x.textAlign='right';x.fillText(f[0]==='g'?'잘 어울림':f[0]==='a'?'쓸 수는 있음':'어울리지 않음',W-16,H-8);x.textAlign='left';
  stamp(x,W,ds==='share'?'교안 예':'예시 데이터');
  kpis($('#k5k'),[[f[0],f[0]==='g'?'잘 어울림':f[0]==='a'?'쓸 수는 있음':'어울리지 않음','판정'],['g',best,'이 데이터에 잘 맞는 차트'],['i',ds==='time'?'시간':ds==='share'?'범주 · 비율':ds==='rel'?'두 수치':ds==='dist'?'그룹 분포':'행렬','데이터의 모양'],['m',ds==='time'?'추세':ds==='share'?'구성비':ds==='rel'?'관계':ds==='dist'?'분포 비교':'쌍별 관계','전하려는 메시지']]);
  $('#ins5').innerHTML='<p class="'+f[0]+'">'+f[1]+'</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결 ---------- */
var ZA=(function(){var r=rng(51),a=[];for(var i=0;i<1000;i++)a.push(gauss(r));return a;})(),ZB=(function(){var r=rng(52),a=[];for(var i=0;i<1000;i++)a.push(gauss(r));return a;})();
LAB.Duel({el:'#duelBox',higherIsBetter:false,drawMargin:.01,max:6,bigGap:100,metric:'다음 달 결제 1,000건 MAE(만 원) — 작을수록 좋음',fmt:function(v){return v.toFixed(2)+'만 원'},
  run:function(){var tr=spend(.9,ZA),te=spend(.9,ZB),md=median(tr),mn=mean(tr),mae=function(c){return mean(te.map(function(v){return Math.abs(v-c)}))},rm=function(c){return Math.sqrt(mean(te.map(function(v){return (v-c)*(v-c)})))};
    this.info={md:md,mn:mn,rF:rm(md),rR:rm(mn),under:te.filter(function(v){return v<mn}).length};return {fly:mae(md),robo:mae(mn)};},
  report:function(r){var I=this.info;return '중앙값은 '+I.md.toFixed(2)+'만 원, 평균은 '+I.mn.toFixed(2)+'만 원이었어요. 다음 달 1,000건 중 '+I.under+'건이 평균보다 작았어요. 참고로 RMSE로 재면 중앙값 '+I.rF.toFixed(2)+', 평균 '+I.rR.toFixed(2)+'로 평균이 더 작아요.';},
  verdict:function(r,res){return '빗나간 거리를 그대로 세면(MAE) 중앙값이, 제곱해서 세면(RMSE) 평균이 강하다. 오늘의 질문은 "전형적인 고객 한 명"이었다. '+(res==='F'?'초파리 승.':res==='R'?'주판봇 승.':'이번 판은 나눠 갖는다.');}});
