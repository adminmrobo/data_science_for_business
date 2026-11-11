/* 3주차 · 데이터 분석을 위한 준비 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,F=LAB.FONT,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod,mean=LAB.mean,sd=LAB.sd,quantile=LAB.quantile,median=LAB.median;
function man(v){return Math.round(v).toLocaleString('ko-KR')+'만 원';}
function wonS(v){var a=Math.abs(v),s=v<0?'−':'';return s+(a>=1e4?Math.round(a/1e4).toLocaleString('ko-KR')+'만':Math.round(a).toLocaleString('ko-KR'))+'원';}

/* ---------- 히어로 소품: 고쳐지는 표 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var X=W*.34,Y=H*.12,cw=W*.075,ch=H*.06;
  for(var r=0;r<6;r++)for(var c=0;c<5;c++){var k=(r*5+c)%7,fixed=((t*.8)%6)>r;var col=k===2?(fixed?C.gfp:C.amber):k===5?(fixed?C.gfp:C.eye):'#2c2f4a';x.fillStyle=col;x.globalAlpha=k===2||k===5?.75:1;x.fillRect(X+c*cw,Y+r*ch,cw-3,ch-3);x.globalAlpha=1;}
  x.strokeStyle=C.seq;x.lineWidth=2;x.strokeRect(X-4,Y-4,cw*5+5,ch*6+5);x.lineWidth=1;});

/* ---------- ① SMART 조립기 ---------- */
var SM=[[['m0','고객 만족도를',0],['m1','고객 이탈률을',1]],[['a0','높인다',0],['a1','15%에서 10%로 낮춘다',1],['a2','15%에서 0%로 낮춘다',2]],[['s0','(측정 방법 없음)',0],['s1','월별 해지 고객 수 ÷ 월초 고객 수로 재며',1]],[['r0','(사업 목표 없음)',0],['r1','연간 매출 5% 증대를 위해',1]],[['t0','언젠가',0],['t1','3개월 안에',1]]];
var smV=[0,0,0,0,0];
SM.forEach(function(opts,i){LAB.radio('#sm'+i,opts.map(function(o){return [o[2],o[1],'sm'+i+'_'+o[2]]}),0,function(v){smV[i]=+v;smart();});});
function smart(){var s=[SM[3][smV[3]][1],SM[4][smV[4]][1],SM[0][smV[0]][1],SM[2][smV[2]][1],SM[1][smV[1]][1]].filter(function(w){return w.indexOf('(')!==0}).join(' ');
  var S=smV[0]===1&&smV[1]>0,M=smV[1]>0&&smV[2]===1,A=smV[1]!==2,R=smV[3]===1,T=smV[4]===1;
  $('#smOut').innerHTML='<b>목표:</b> '+s+'.';
  var L=[['S','Specific 구체성',S],['M','Measurable 측정 가능',M],['A','Achievable 달성 가능',A],['R','Relevant 관련성',R],['T','Time-bound 시한',T]];
  $('#smChk').innerHTML=L.map(function(l){return '<span class="'+(l[2]?'on':'off')+'">'+(l[2]?'✓ ':'✗ ')+l[1]+'</span>';}).join('');
  var n=L.filter(function(l){return l[2]}).length,why=[];
  if(!S)why.push('S: "만족도"나 "높인다"처럼 대상·방향만 있으면 구체적이지 않습니다. 교안 예처럼 "4.5점 달성", "15% → 10%"로 적습니다.');
  if(!M)why.push('M: 숫자 목표와 측정 방법(어떤 데이터로 재나)이 함께 있어야 합니다.');
  if(!A)why.push('A: 이탈률 0%는 현실적이지 않습니다. 필요한 자원과 함께 달성 가능한 수준을 정합니다.');
  if(!R)why.push('R: 매출·비용 같은 사업 목표와 연결해야 우선순위가 섭니다.');
  if(!T)why.push('T: 기한이 있어야 중간 점검과 성공 판정을 할 수 있습니다.');
  $('#ins1').innerHTML=n===5?'<p class="g">다섯 글자가 모두 켜졌습니다. 교안의 예시 목표와 같은 모양입니다. 이제 "월별 이탈률" 데이터가 필요하다는 것도 정해졌습니다.</p>':why.map(function(w){return '<p class="a">'+w+'</p>'}).join('');}
smart();
var TY=['분류','예측','최적화','탐색'];
var TQ=[['이 고객은 VIP·충성·신규·휴면 중 어디에 속할까?',0,'정해진 범주로 나누는 분류 문제(RFM 고객 세분화).'],['다음 달 매장별 우산 판매량은 몇 개일까?',1,'미래 값을 맞히는 예측(수요 예측) 문제.'],['배송 기사 10명이 120곳을 도는 가장 짧은 경로는?',2,'제약 안에서 목표(거리·시간)를 최소화하는 최적화 문제.'],['함께 자주 팔리는 상품 묶음에는 무엇이 있을까?',3,'정답 없이 패턴을 찾는 탐색 문제(연관 규칙).'],['이 보험금 청구는 사기일까, 정상일까?',0,'두 범주로 나누므로 분류. 사기 위험 "확률"을 내면 예측(리스크 예측)으로도 봅니다.'],['광고 예산 1억을 TV·온라인·모바일에 어떻게 나눌까?',2,'예산 제약 안에서 효과를 최대화하는 최적화(마케팅 믹스).']];
$('#typeBox').innerHTML=TQ.map(function(q,i){return '<div class="qi" style="background:rgba(94,227,156,.04);border-color:var(--rule)"><p>'+q[0]+'</p><div class="opts" id="ty'+i+'"></div><p class="fb" id="tyf'+i+'" aria-live="polite"></p></div>';}).join('');
TQ.forEach(function(q,i){TY.forEach(function(t,j){var b=document.createElement('button');b.className='bt';b.type='button';b.id='tq'+i+'_'+j;b.textContent=t;b.setAttribute('aria-pressed','false');
  b.addEventListener('click',function(){$$('#ty'+i+' .bt').forEach(function(z){z.setAttribute('aria-pressed',z===b)});var ok=j===q[1];$('#tyf'+i).className='fb '+(ok?'ok':'no');$('#tyf'+i).textContent=(ok?'맞습니다. ':'교안 기준으로는 '+TY[q[1]]+'. ')+q[2];});$('#ty'+i).appendChild(b);});});

/* ---------- ② 결측값 ---------- */
var POP=(function(){var r=rng(8),P=[];for(var i=0;i<200;i++){var age=20+r()*45,inc=2000+70*(age-20)+gauss(r)*500;P.push({age:age,inc:inc,u:r()});}return P;})();
var TM=mean(POP.map(function(p){return p.inc})),Q70=POP.map(function(p){return p.inc}).sort(function(a,b){return a-b})[140];
function missing(m){return POP.map(function(p){return {age:p.age,inc:p.inc,miss:m==='MCAR'?p.u<.3:m==='MAR'?p.u<(p.age<35?.65:.08):p.u<(p.inc>Q70?.7:.1)};});}
function impute(D,how,k){var obs=D.filter(function(d){return !d.miss});
  if(how==='del')return obs.map(function(d){return {age:d.age,v:d.inc,imp:false}});
  var mo=mean(obs.map(function(d){return d.inc}));
  return D.map(function(d){if(!d.miss)return {age:d.age,v:d.inc,imp:false};if(how==='mean')return {age:d.age,v:mo,imp:true,tru:d.inc};
    var nb=obs.slice().sort(function(a,b){return Math.abs(a.age-d.age)-Math.abs(b.age-d.age)}).slice(0,k);return {age:d.age,v:mean(nb.map(function(n){return n.inc})),imp:true,tru:d.inc};});}
var mech='MAR',how='del';
LAB.radio('#mechBtns',[['MCAR','MCAR · 아무나','me0'],['MAR','MAR · 젊은 층이','me1'],['MNAR','MNAR · 고소득자가','me2']],'MAR',function(v){mech=v;draw2();});
LAB.radio('#impBtns',[['del','결측 행 삭제','im0'],['mean','평균 대체','im1'],['knn','KNN 대체','im2']],'del',function(v){how=v;draw2();});
$('#kk').addEventListener('input',function(){$('#kkv').textContent=this.value;draw2();});
function draw2(){var k=+$('#kk').value,D=missing(mech),R=impute(D,how,k),est=mean(R.map(function(r){return r.v})),nMiss=D.filter(function(d){return d.miss}).length;
  var c=$('#c2'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);
  var X=56,Wd=W-260,Y0=H-40,sx=function(a){return X+(a-20)/45*Wd},sy=function(v){return Y0-(v-500)/6000*(H-70)};
  [1000,2000,3000,4000,5000,6000].forEach(function(v){txt(x,v.toLocaleString('ko-KR'),X-6,sy(v),C.muted,10,'right');});
  [20,30,40,50,60].forEach(function(a){txt(x,a+'세',sx(a),Y0+16,C.muted,10,'center');});
  txt(x,'연소득(만 원)',X,16,C.muted,11);
  D.forEach(function(d){if(d.miss){x.strokeStyle='rgba(157,155,184,.6)';x.beginPath();x.arc(sx(d.age),sy(d.inc),3.2,0,7);x.stroke();}else{x.fillStyle=C.seq;x.beginPath();x.arc(sx(d.age),sy(d.inc),2.8,0,7);x.fill();}});
  R.forEach(function(r){if(r.imp){x.fillStyle=C.amber;x.fillRect(sx(r.age)-3,sy(r.v)-3,6,6);}});
  if(mech==='MAR'){x.fillStyle='rgba(241,182,70,.07)';x.fillRect(sx(20),30,sx(35)-sx(20),Y0-30);txt(x,'35세 미만: 65%가 비움',sx(21),40,C.amber,11);}
  /* 오른쪽: 평균 비교 */
  var bx=W-180,mx=Math.max(TM,est)*1.15,bh=H-100;
  [[TM,'참값 평균',C.gfp],[est,'추정 평균',how==='del'?C.eye:how==='mean'?C.stain:C.info]].forEach(function(b,i){var h=b[0]/mx*bh,px=bx+i*80;x.fillStyle=b[2];x.fillRect(px,Y0-h,50,h);txt(x,Math.round(b[0]).toLocaleString('ko-KR'),px+25,Y0-h-10,C.text,11,'center',700);txt(x,b[1],px+25,Y0+16,C.muted,11,'center');});
  txt(x,'● 관측  ○ 빠진 값(진짜)  ■ 채운 값',X,H-8,C.muted,11);
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var sdv=sd(R.map(function(r){return r.v})),sdt=sd(POP.map(function(p){return p.inc})),err=est-TM;
  kpis($('#k2'),[['g',man(TM),'참값 평균(현실에선 모름)'],['i',man(est),'추정 평균'],[Math.abs(err)>150?'r':'g',(err>0?'+':'')+man(err),'오차'],['a',R.length+'줄 · 표준편차 '+Math.round(sdv/sdt*100)+'%','분석에 쓴 줄 · 퍼짐(참값 대비)']]);
  $('#eq2').innerHTML='빈칸 <i>'+nMiss+'</i>개 / 200 · 방법: <b>'+{del:'결측 행 삭제',mean:'평균 대체',knn:'KNN 대체(k = '+k+')'}[how]+'</b> · 추정 평균 − 참값 = <em>'+(err>0?'+':'')+Math.round(err)+'만 원</em>';
  var M={MCAR:'아무나 비웠으므로(MCAR) 관측된 줄도 전체를 잘 대표합니다. 어느 방법이든 평균은 크게 틀리지 않습니다.',MAR:'젊은 고객이 주로 비웠습니다(MAR). 남은 줄은 나이 든, 소득이 높은 쪽으로 기울어 있습니다.',MNAR:'고소득자가 소득을 숨겼습니다(MNAR). 빠진 이유가 빠진 값 자체라서, 남은 정보만으로는 완전히 되살릴 수 없습니다.'};
  var tail=how==='mean'?' 평균 대체는 빈칸에 같은 값을 넣어 퍼짐을 '+Math.round(sdv/sdt*100)+'%로 줄였습니다. 분산·상관 분석이 왜곡됩니다.':how==='knn'?' KNN은 나이가 비슷한 이웃의 소득으로 채웠습니다. 나이가 결측과 소득을 함께 설명할 때 강합니다.':' 삭제는 '+nMiss+'줄을 버렸습니다.';
  $('#ins2').innerHTML='<p class="'+(Math.abs(err)>150?'r':'g')+'">'+M[mech]+tail+'</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});
function errOf(m,h,k){var R=impute(missing(m),h,k||5);return mean(R.map(function(r){return r.v}))-TM;}
$('#heroMiss').textContent=(errOf('MAR','del')>0?'+':'')+man(errOf('MAR','del'));

/* ---------- ③ 이상값 ---------- */
var BUY=(function(){var r=rng(19),a=[];for(var i=0;i<115;i++)a.push({v:Math.round(Math.exp(Math.log(50000)+gauss(r)*.5)/100)*100,k:'n'});
  [1100000,1200000,1350000].forEach(function(v){a.push({v:v,k:'vip'})});a.push({v:9999999,k:'err'});a.push({v:-50000,k:'err'});return a;})();
var olR='iqr',olT='flag';
LAB.radio('#olBtns',[['z','Z-score |z|>3','ol0'],['iqr','IQR 1.5배','ol1'],['mz','수정 Z |z|>3.5','ol2']],'iqr',function(v){olR=v;draw3();});
LAB.radio('#otBtns',[['flag','표시만','ot0'],['drop','제거','ot1'],['cap','캡핑','ot2'],['dom','도메인 규칙','ot3']],'flag',function(v){olT=v;draw3();});
function rule(vals,r){var m=mean(vals),s=sd(vals),q1=quantile(vals,.25),q3=quantile(vals,.75),iq=q3-q1,md=median(vals),mad=median(vals.map(function(v){return Math.abs(v-md)}));
  var lo,hi;if(r==='z'){lo=m-3*s;hi=m+3*s;}else if(r==='iqr'){lo=q1-1.5*iq;hi=q3+1.5*iq;}else{lo=md-3.5*mad/.6745;hi=md+3.5*mad/.6745;}return {lo:lo,hi:hi,q1:q1,q3:q3,md:md,m:m,s:s};}
function tpos(v){return (v<0?-1:1)*Math.log10(1+Math.abs(v)/10000);}
function draw3(){var vals=BUY.map(function(b){return b.v}),R=rule(vals,olR),flag=BUY.map(function(b){return b.v<R.lo||b.v>R.hi});
  var used,vip=0;
  if(olT==='flag')used=vals.slice();
  else if(olT==='drop')used=vals.filter(function(v,i){return !flag[i]});
  else if(olT==='cap')used=vals.map(function(v){return Math.min(R.hi,Math.max(R.lo,v))});
  else{used=BUY.filter(function(b){return b.k==='n'}).map(function(b){return b.v});vip=3;}
  var c=$('#c3'),W=fitC(c,260),H=260,x=c.getContext('2d');grid(x,W,H);
  var X=40,Wd=W-80,pmin=tpos(-60000),pmax=tpos(1.2e7),sx=function(v){return X+(tpos(v)-pmin)/(pmax-pmin)*Wd};
  [-50000,0,10000,100000,1000000,10000000].forEach(function(v){x.strokeStyle='rgba(157,155,184,.15)';x.beginPath();x.moveTo(sx(v),40);x.lineTo(sx(v),H-40);x.stroke();txt(x,wonS(v),sx(v),H-24,C.muted,10,'center');});
  txt(x,'구매액(로그 비슷한 눈금) · 점 = 고객 한 명',X,18,C.muted,11);
  /* 박스플롯 (원자료 사분위) */
  var by=70;x.strokeStyle=C.text;x.fillStyle='rgba(154,184,255,.18)';x.fillRect(sx(R.q1),by-14,sx(R.q3)-sx(R.q1),28);x.strokeRect(sx(R.q1),by-14,sx(R.q3)-sx(R.q1),28);
  x.beginPath();x.moveTo(sx(R.md),by-14);x.lineTo(sx(R.md),by+14);x.stroke();
  [[R.lo,'하한'],[R.hi,'상한']].forEach(function(f){var px=sx(Math.max(-60000,Math.min(1.2e7,f[0])));x.setLineDash([4,3]);x.strokeStyle=C.amber;x.beginPath();x.moveTo(px,40);x.lineTo(px,H-40);x.stroke();x.setLineDash([]);txt(x,f[1],px+3,46,C.amber,10);});
  BUY.forEach(function(b,i){var jy=120+((i*37)%60),px=sx(b.v);x.fillStyle=flag[i]?C.eye:b.k==='vip'?C.gfp:C.seq;x.beginPath();x.arc(px,jy,flag[i]?4:3,0,7);x.fill();
    if(b.k!=='n'){txt(x,b.k==='vip'?'VIP':'오류',px,jy+14,b.k==='vip'?C.gfp:C.eye,10,'center',700);}});
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var nf=flag.filter(Boolean).length,vipF=BUY.filter(function(b,i){return b.k==='vip'&&flag[i]}).length,errF=BUY.filter(function(b,i){return b.k==='err'&&flag[i]}).length;
  kpis($('#k3'),[['r',nf+'건','규칙에 걸린 값'],['a','오류 '+errF+'/2 · VIP '+vipF+'/3','걸린 것 중 오류 · VIP'],['i',wonS(mean(used)),olT==='dom'?'일반 고객 평균':'처리 후 평균'],['g',wonS(median(used)),'처리 후 중앙값']]);
  var msg=[];
  if(olR==='z')msg.push('<p class="r">Z-score는 999만 원 오류 하나가 표준편차를 '+wonS(R.s)+'로 부풀려, '+nf+'건만 잡았습니다. −5만 원 오류와 VIP는 놓쳤습니다(가림 효과).</p>');
  else msg.push('<p class="a">'+(olR==='iqr'?'IQR':'수정 Z-score')+'는 극단값에 덜 흔들려 오류 '+errF+'건과 VIP '+vipF+'건을 포함해 '+nf+'건을 후보로 찾았습니다. 그러나 규칙은 오류와 VIP를 구분하지 못합니다.</p>');
  if(olT==='drop'&&vipF)msg.push('<p class="r">제거하면 진짜 VIP '+vipF+'명도 함께 사라집니다. 가장 중요한 고객이 분석에서 빠졌습니다.</p>');
  if(olT==='cap')msg.push('<p class="a">캡핑은 값을 경계로 눌러 영향을 줄이지만, −5만 원 같은 불가능한 값도 남겨 둡니다.</p>');
  if(olT==='dom')msg.push('<p class="g">도메인 규칙: 음수와 1회 한도(300만 원) 초과는 오류로 지우고, VIP 3명은 따로 분석합니다. 일반 고객의 평균 '+wonS(mean(used))+'과 중앙값 '+wonS(median(used))+'이 가까워졌습니다.</p>');
  $('#ins3').innerHTML=msg.join('');}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 중복과 품질 6차원 ---------- */
var COLS=['주문ID','고객ID','이름','나이','성별','이메일','도서번호','무게','갱신'];
var ROWS=[
 ['ORD001','12345','김철수','34','남','kim@mail.kr','B001','1.2kg','2026-10'],
 ['ORD001','12345','김철수','34','남','kim@mail.kr','B001','1.2kg','2026-10'],
 ['ORD001','12345','김철수','34','남','kim@mail.kr','B001','1.2kg','2026-10'],
 ['ORD002','12346','이영희','29','여','','B002','2.6lb','2026-10'],
 ['ORD003','12347','박민수','999','남','park@mail.kr','B003','0.8kg','2026-09'],
 ['ORD004','12348','최지은','41','외계인','choi@mail.kr','B001','1.2kg','2026-10'],
 ['ORD005','12349','정하늘','27','남','jung@mail.kr','B999','0.5kg','2026-10'],
 ['ORD006','12350','한소라','52','여','','B004','3.1lb','2024-02'],
 ['ORD007','12351','오세진','38','남','oh@mail','B002','1.2kg','2026-10'],
 ['ORD008','12352','윤가람','45','여','yoon@mail.kr','B005','1.0kg','2026-08'],
 ['ORD009','12345','김철수','34','남','kim2@mail.kr','B003','0.8kg','2026-10'],
 ['ORD010','12353','서다온','31','여','seo@mail.kr','B001','1.2kg','2025-01']];
var BOOKS=['B001','B002','B003','B004','B005'];
var FIXV={'4,3':'43','5,4':'여','6,6':'B005','8,5':'oh@mail.kr','3,5':'lee@mail.kr','7,5':'han@mail.kr','10,5':'kim@mail.kr'};
var FX={dup:false,fmt:false,rule:false,fill:false,fresh:false};
var FXL=[['dup','중복 제거'],['fmt','단위·형식 통일'],['rule','규칙 위반 고치기'],['fill','빈칸 보완'],['fresh','최신화']];
FXL.forEach(function(f){var b=document.createElement('button');b.className='bt';b.type='button';b.id='fx_'+f[0];b.textContent=f[1];b.setAttribute('aria-pressed','false');
  b.addEventListener('click',function(){FX[f[0]]=!FX[f[0]];b.setAttribute('aria-pressed',FX[f[0]]);draw4();});$('#fixBtns').appendChild(b);});
function cur(){return ROWS.map(function(r,i){var o=r.slice(),st=r.map(function(){return ''});
  if(FX.fmt){if(/lb$/.test(o[7])){o[7]=(parseFloat(o[7])*0.4536).toFixed(1)+'kg';st[7]='fix';}if(i===10){o[5]='kim@mail.kr';st[5]='fix';}}
  if(FX.rule){[[4,3],[5,4],[6,6],[8,5]].forEach(function(p){if(p[0]===i){o[p[1]]=FIXV[p[0]+','+p[1]];st[p[1]]='fix';}});}
  if(FX.fill){[[3,5],[7,5]].forEach(function(p){if(p[0]===i){o[p[1]]=FIXV[p[0]+','+p[1]];st[p[1]]='fix';}});}
  if(FX.fresh&&o[8]<'2025-11'){o[8]='2026-11';st[8]='fix';}
  return {o:o,st:st,dup:FX.dup&&(i===1||i===2)};});}
function valid(o){var a=+o[3];return a>=0&&a<=150&&(o[4]==='남'||o[4]==='여')&&(o[5]===''||/^[^@]+@[^@]+\.[a-z]{2,}$/.test(o[5]));}
function scores(rows){var R=rows.filter(function(r){return !r.dup}).map(function(r){return r.o}),n=R.length;
  var cells=n*COLS.length,nonNull=0;R.forEach(function(o){o.forEach(function(v){if(v!=='')nonNull++;});});
  var keys={};R.forEach(function(o){keys[o.join('|')]=1});var uniq=Object.keys(keys).length;
  var val=R.filter(valid).length;
  var em={};R.forEach(function(o){(em[o[1]]=em[o[1]]||{})[o[5]]=1;});
  var cons=R.filter(function(o){return /kg$/.test(o[7])&&BOOKS.indexOf(o[6])>=0&&Object.keys(em[o[1]]).filter(function(e){return e}).length<=1;}).length;
  var acc=R.filter(function(o){return o[3]!=='999'&&o[4]!=='외계인'&&o[6]!=='B999';}).length;
  var tim=R.filter(function(o){return o[8]>='2025-11'}).length;
  return [['정확성',acc/n],['완전성',nonNull/cells],['일관성',cons/n],['적시성',tim/n],['유효성',val/n],['유일성',uniq/n]];}
function draw4(){var rows=cur();
  $('#qTable').innerHTML='<thead><tr>'+COLS.map(function(c){return '<th>'+c+'</th>'}).join('')+'</tr></thead><tbody>'+rows.map(function(r,i){var o=r.o;
    return '<tr'+(r.dup?' class="dup"':'')+'>'+o.map(function(v,j){var cls=r.st[j];
      if(!cls){if(v==='')cls='miss';else if((j===3&&v==='999')||(j===4&&v==='외계인')||(j===6&&v==='B999')||(j===5&&v==='oh@mail')||(j===7&&/lb$/.test(v))||(j===8&&v<'2025-11')||(i===10&&j===5)||((i===1||i===2)&&!r.dup&&j===0))cls='bad';}
      return '<td'+(cls?' class="'+cls+'"':'')+'>'+(v===''?'(빈칸)':v)+'</td>';}).join('')+'</tr>';}).join('')+'</tbody>';
  var S=scores(rows),c=$('#c4'),W=fitC(c,220),H=220,x=c.getContext('2d');grid(x,W,H);
  var bw=(W-80)/6;S.forEach(function(s,i){var h=s[1]*(H-80),px=50+i*bw;x.fillStyle=C.panel2;x.fillRect(px,30,bw*.6,H-80);x.fillStyle=s[1]>=.99?C.gfp:s[1]>=.8?C.seq:C.eye;x.fillRect(px,30+(H-80)-h,bw*.6,h);
    txt(x,Math.round(s[1]*100)+'%',px+bw*.3,22,C.text,12,'center',700);txt(x,s[0],px+bw*.3,H-34,C.muted,12,'center');});
  stamp(x,W,'예시 데이터');
  var worst=S.slice().sort(function(a,b){return a[1]-b[1]})[0],on=Object.keys(FX).filter(function(k){return FX[k]}).length;
  $('#ins4').innerHTML=on===5?'<p class="g">다섯 단계를 모두 켜자 여섯 차원이 모두 100%가 되었습니다. 실제로는 원장(참조 데이터)과 대조할 수 있어야 정확성을 이렇게 고칠 수 있습니다.</p>':
    '<p class="a">지금 가장 낮은 차원은 <b>'+worst[0]+' '+Math.round(worst[1]*100)+'%</b>입니다. 빨간 칸은 규칙 위반, 노란 칸은 빈칸입니다. 정제 단계를 하나씩 켜 보세요.</p>';}
draw4();
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ EDA ---------- */
var ST=(function(){var r=rng(23),a=[];for(var i=0;i<60;i++){var ad=Math.exp(1.0+gauss(r)*.75);var s=12*Math.pow(ad,.55)*Math.exp(gauss(r)*.22);a.push({ad:ad,s:s});}return a;})();
var edaV='bi',withOut=false;
LAB.radio('#edaBtns',[['uni','단변량 · 매출 분포','ed0'],['bi','이변량 · 광고비와 매출','ed1']],'bi',function(v){edaV=v;draw5();});
$('#addOut').addEventListener('click',function(){withOut=!withOut;this.setAttribute('aria-pressed',withOut);draw5();});
function draw5(){var D=ST.slice();if(withOut)D.push({ad:2.0,s:140,out:true});
  var xs=D.map(function(d){return d.ad}),ys=D.map(function(d){return d.s}),pr=LAB.corr(xs,ys),sp=LAB.spearman(xs,ys),mu=mean(ys),md=median(ys);
  var c=$('#c5'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X=56,Wd=W-90,Y0=H-40;
  if(edaV==='bi'){var mxX=Math.max.apply(0,xs)*1.05,mxY=Math.max.apply(0,ys)*1.05,sx=function(v){return X+v/mxX*Wd},sy=function(v){return Y0-v/mxY*(H-70)};
    [0,.25,.5,.75,1].forEach(function(f){txt(x,(mxY*f).toFixed(0),X-6,sy(mxY*f),C.muted,10,'right');txt(x,(mxX*f).toFixed(1),sx(mxX*f),Y0+16,C.muted,10,'center');});
    txt(x,'세로: 월 매출(백만 원) · 가로: 월 광고비(백만 원)',X,16,C.muted,11);
    D.forEach(function(d){x.fillStyle=d.out?C.eye:C.seq;x.beginPath();x.arc(sx(d.ad),sy(d.s),d.out?5:3.2,0,7);x.fill();});
    var ord=ST.slice().sort(function(a,b){return a.ad-b.ad});x.strokeStyle=C.gfp;x.lineWidth=2;x.beginPath();for(var t=0;t<=40;t++){var v=mxX*t/40;var y=12*Math.pow(Math.max(v,.01),.55);t?x.lineTo(sx(v),sy(y)):x.moveTo(sx(v),sy(y));}x.stroke();x.lineWidth=1;
    txt(x,'만든 규칙: 매출 ∝ 광고비^0.55',sx(mxX*.55),sy(12*Math.pow(mxX*.55,.55))-14,C.gfp,11);}
  else{var lo=0,hi=Math.max.apply(0,ys)*1.02,nb=16,bins=new Array(nb).fill(0);ys.forEach(function(v){var i=Math.min(nb-1,Math.floor((v-lo)/(hi-lo)*nb));bins[i]++;});var mb=Math.max.apply(0,bins),bw=Wd/nb;
    bins.forEach(function(b,i){var h=b/mb*(H-80);x.fillStyle=C.seq;x.fillRect(X+i*bw,Y0-h,bw-2,h);});
    [[mu,'평균',C.eye],[md,'중앙값',C.gfp]].forEach(function(l,k){var px=X+(l[0]-lo)/(hi-lo)*Wd;x.strokeStyle=l[2];x.lineWidth=2;x.beginPath();x.moveTo(px,30);x.lineTo(px,Y0);x.stroke();x.lineWidth=1;txt(x,l[1]+' '+l[0].toFixed(1),px+4,36+k*16,l[2],11,'left',700);});
    for(var k=0;k<=4;k++){var v=lo+(hi-lo)*k/4;txt(x,v.toFixed(0),X+k/4*Wd,Y0+16,C.muted,10,'center');}
    txt(x,'월 매출(백만 원) 히스토그램',X,16,C.muted,11);}
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var sk=(function(){var m=mean(ys),s=sd(ys),t=0;ys.forEach(function(v){t+=Math.pow((v-m)/s,3)});return t/ys.length;})();
  kpis($('#k5'),[['i',pr.toFixed(2),'직선 관계의 세기(피어슨)'],['g',sp.toFixed(2),'순위 관계의 세기(스피어만)'],['a',mu.toFixed(1)+' / '+md.toFixed(1),'매출 평균 / 중앙값'],['m',sk.toFixed(2),'한쪽 쏠림(왜도, 0이면 대칭)']]);
  $('#ins5').innerHTML=edaV==='uni'?'<p class="a">오른쪽 꼬리가 깁니다(왜도 '+sk.toFixed(2)+'). 평균('+mu.toFixed(1)+')이 중앙값('+md.toFixed(1)+')보다 커서, "평균 매장"은 실제 보통 매장보다 커 보입니다.</p>':
    (withOut?'<p class="r">광고비는 적은데 매출이 큰 매장 하나를 넣자 피어슨이 '+pr.toFixed(2)+'로 흔들렸습니다. 순위만 보는 스피어만은 '+sp.toFixed(2)+'로 거의 그대로입니다.</p>':'<p class="g">광고비가 늘수록 매출도 늘지만 점점 완만해집니다(직선이 아님). 그래서 순위 기반 스피어만('+sp.toFixed(2)+')이 피어슨('+pr.toFixed(2)+')보다 큽니다.</p>');}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결 ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:false,drawMargin:5,metric:'평균 연소득 추정 오차(참값과의 차이, 만 원). 작을수록 좋음',fmt:function(v){return man(v)},
  run:function(){var f=Math.abs(errOf('MAR','del')),r=Math.abs(errOf('MAR','knn',5));this.max=Math.max(f,r)*1.1;this.bigGap=TM*.10;return {fly:f,robo:r};},
  report:function(r){return '참값 평균은 '+man(TM)+'이에요. 결측 행을 지운 초파리 쪽은 '+man(r.fly)+' 틀렸고(남은 줄이 나이 든 쪽으로 기울어서 높게 나옴), KNN으로 채운 주판봇 쪽은 '+man(r.robo)+' 틀렸어요.';},
  verdict:function(r,res){return '빈칸이 나이에 따라 생겼으면, 지우는 것도 편향을 만든다. '+(res==='R'?'주판봇 승.':res==='F'?'초파리 승.':'이번 판은 나눠 갖는다.');}});
