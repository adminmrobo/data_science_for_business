/* 2주차 · 비즈니스 데이터의 수집 및 처리 기술 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,F=LAB.FONT,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
function won(v){return v>=1e8?(v/1e8).toFixed(2).replace(/\.?0+$/,'')+'억 원':v>=1e4?Math.round(v/1e4).toLocaleString('ko-KR')+'만 원':Math.round(v).toLocaleString('ko-KR')+'원';}

/* ---------- 히어로 소품: 출처 → 서버 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){
  var src=[[.36,.2,C.eye],[.36,.36,C.amber],[.36,.52,C.seq],[.5,.12,C.stain]],sx=W*.74,sy=H*.22;
  x.fillStyle='#2a2d48';x.fillRect(sx,sy,W*.12,H*.42);for(var i=0;i<6;i++){x.fillStyle='#14152a';x.fillRect(sx+W*.012,sy+H*.02+i*H*.066,W*.096,H*.045);x.fillStyle=i%2?C.gfp:C.info;x.fillRect(sx+W*.09,sy+H*.035+i*H*.066,4,4);}
  src.forEach(function(s,k){var px=W*s[0],py=H*s[1];x.fillStyle=s[2];x.fillRect(px-8,py-8,16,16);
    for(var j=0;j<4;j++){var u=((t*.35+j/4+k*.13)%1);x.fillStyle=s[2];x.beginPath();x.arc(px+(sx-px)*u,py+(sy+H*.2-py)*u,2.5,0,7);x.fill();}});
});

/* ---------- ① 산업별 데이터 지도 ---------- */
var IND={
 fin:{n:'금융(은행·결제·증권)',spd:1.4,src:['계좌·거래','대출·신용','앱 접속 로그','상담 기록','결제(카드·간편결제)'],use:['고객 세분화·타깃 마케팅','신용 평가 모델','이상 거래 탐지','상품 추천·로보어드바이저'],
  rows:[['인구통계 정보','연령·성별·거주지·직업','고객 세분화, 타깃 마케팅'],['계좌 정보','계좌 유형, 잔액, 입출금 패턴, 이체·결제 내역','금융 상품 추천, 이상 거래 탐지'],['대출·신용 정보','대출 종류·금액·이율·상환·연체, 신용점수, 카드 사용','신용 평가 모델, 리스크 관리'],['서비스 이용·상담','로그인 기록, 이용 시간대, 클릭, 문의·불만 내역','서비스 개선, 이상 행동 탐지'],['결제·투자','결제 수단·금액·채널(금융결제원 Datop), 투자 목표·위험 허용도','소비 패턴 분석, 포트폴리오 최적화']],
  warn:'신용정보법·마이데이터 규제, 실시간 보안 감시(③칸), 투자성향 설문의 신뢰성'},
 mfg:{n:'제조(스마트팩토리·IoT)',spd:3.2,src:['온도·압력·진동 센서','전력 소비','설비 가동·고장 이력','품질 검사 결과'],use:['예측 정비','품질 예측·불량률 저감','생산 계획 최적화','디지털 트윈 시뮬레이션'],
  rows:[['공정 데이터','온도, 압력, 진동, 전력 소비(센서, 실시간)','이상 징후 감지, 예측 정비'],['설비 운영 데이터','가동률, 고장 이력, 유지보수 주기','다운타임 최소화, 설비 수명 예측'],['품질 검사 데이터','검사 결과, 불량률, 재작업 현황','AI 품질 예측, 불량 저감'],['통합 플랫폼','SCADA·MES·ERP 연계, 원자재~완제품 품질 이력','생산 계획, 품질 이력 추적']],
  warn:'초당 수백 건 → 대용량 실시간 인프라(엣지·클라우드), 산업보안법·영업비밀'},
 ret:{n:'소매(일반·편의점)',spd:2,src:['POS 영수증','매장 동선·체류(센서·CCTV)','재고·납기(RFID)','무인 계산대','에너지 사용'],use:['매출 패턴·프로모션','RFM 고객 세분화','ABC 분석·자동 발주','PB 상품 개발'],
  rows:[['POS 데이터','매장·시간대·상품별 판매(실시간)','재고 관리, 매출 분석, 인기 상품'],['고객 행동','출입·동선·체류 시간, 영상 분석 연령대·성별 추정','고객 세분화, 맞춤 마케팅'],['재고·공급망','실시간 재고, 공급업체 납기, 물류(RFID·스마트 선반)','적정 재고, 품절 방지'],['편의점 운영','시간대별 매출, 날씨·요일, 단골/신규, 계산대 대기 시간','진열 전략, PB 상품(라면·스낵) 개발']],
  warn:'POS에도 구매 이력 등 개인정보가 들어갈 수 있음(교안 연습문제 2) → 개인정보보호법'},
 plat:{n:'플랫폼(앱·배달)',spd:2.4,src:['앱 사용 로그','주문·배송 기록','리뷰·평점','라이더 위치','파트너 식당 정보'],use:['UI/UX A/B 테스트','개인화 메뉴 추천','수요 예측·동적 배송비','이탈 예측·파트너 관리'],
  rows:[['앱 사용성','화면별 체류 시간, 클릭률, 이탈률','A/B 테스트로 UI/UX 개선'],['고객 피드백','리뷰, 평점, 고객센터 문의, 앱스토어 피드백','텍스트 마이닝·감정 분석'],['주문·배송','주문 시간, 음식 종류, 지역, 배달 시간, 라이더 위치','배송 경로 최적화, 수요 예측'],['파트너 데이터','메뉴, 가격, 평점, 리뷰, 운영 시간','성과 관리, 매출 증진 협업']],
  warn:'모든 활동을 추적하는 만큼 동의·최소 수집 원칙, 동적 가격의 공정성 논란'}};
var indK='fin';
LAB.radio('#indBtns',[['fin','금융','in_fin'],['mfg','제조','in_mfg'],['ret','소매','in_ret'],['plat','플랫폼','in_plat']],'fin',function(v){indK=v;showInd();});
function showInd(){var d=IND[indK];
  $('#indTable').innerHTML='<thead><tr><th>데이터 유형</th><th>수집 항목</th><th>활용 목적</th></tr></thead><tbody>'+d.rows.map(function(r){return '<tr><td><b>'+r[0]+'</b></td><td>'+r[1]+'</td><td>'+r[2]+'</td></tr>';}).join('')+'</tbody>';
  $('#ins1').innerHTML='<p class="a"><b>'+d.n+' · 조심할 점:</b> '+d.warn+'</p>';}
showInd();
var T1=0;
function draw1(dt){T1+=dt||0;var c=$('#c1'),W=fitC(c,260),H=260,x=c.getContext('2d'),d=IND[indK];grid(x,W,H);
  var n=d.src.length,m=d.use.length,lx=24,rx=W-200,mx=W/2;
  x.fillStyle=C.panel2;x.fillRect(mx-60,H/2-36,120,72);x.strokeStyle=C.seq;x.strokeRect(mx-60,H/2-36,120,72);txt(x,'저장·처리',mx,H/2-10,C.seq,13,'center',700);txt(x,'레이크·웨어하우스',mx,H/2+12,C.muted,11,'center');
  d.src.forEach(function(s,i){var y=30+i*(H-50)/(n-1||1);x.fillStyle=C.panel;x.fillRect(lx,y-13,170,26);x.strokeStyle=C.eye;x.strokeRect(lx,y-13,170,26);txt(x,s,lx+8,y,C.text,12);
    for(var j=0;j<3;j++){var u=(T1*d.spd*.25+j/3+i*.17)%1,px=lx+170+(mx-60-lx-170)*u,py=y+(H/2-y)*u;x.fillStyle=C.eye;x.beginPath();x.arc(px,py,2.6,0,7);x.fill();}});
  d.use.forEach(function(s,i){var y=40+i*(H-80)/(m-1||1);x.fillStyle=C.panel;x.fillRect(rx,y-13,180,26);x.strokeStyle=C.gfp;x.strokeRect(rx,y-13,180,26);txt(x,s,rx+8,y,C.text,12);
    for(var j=0;j<2;j++){var u=(T1*.3+j/2+i*.2)%1,px=mx+60+(rx-mx-60)*u,py=H/2+(y-H/2)*u;x.fillStyle=C.gfp;x.beginPath();x.arc(px,py,2.4,0,7);x.fill();}});
  stamp(x,W,'도식 · 흐름 속도는 설명용');}
addMod($('#c1'),function(dt){if(!dt||!LAB.reduce)draw1(dt);});

/* ---------- ② 수집 방법 고르기 ---------- */
var MET=['API','웹 크롤링','설문','센서','RPA'];
var SCN=[['우리 동네 상권의 업소 수와 유동인구를 매달 받아 입지 분석에 쓰고 싶다.',0,'소상공인시장진흥공단의 상권정보 API가 있습니다. 공식 API가 있으면 API가 가장 안정적입니다.'],
 ['경쟁 쇼핑몰 10곳의 같은 상품 가격을 매일 비교하고 싶다(공개 페이지, 공식 API 없음).',1,'공개 웹페이지의 정보는 스크래핑·크롤링으로 모읍니다. 이용약관 확인과 속도 제한이 함께 필요합니다.'],
 ['고객의 투자 위험 허용도와 투자 경험을 알아야 상품을 권할 수 있다.',2,'위험 성향은 행동 기록에 남지 않는 생각입니다. 교안의 투자성향진단 설문이 이 경우입니다.'],
 ['양식장 수조의 수질(온도·용존산소)을 24시간 감시하고 싶다.',3,'물리적 상태의 실시간 측정은 센서(IoT)의 일입니다. 교안의 스마트 양식장 사례입니다.'],
 ['20년 된 사내 재고 시스템에서 매일 숫자를 옮겨 적고 있다. API는 없다.',4,'API가 없는 레거시 시스템은 RPA 봇이 화면을 조작해 데이터를 꺼낼 수 있습니다.'],
 ['상장기업 300곳의 재무제표를 분기마다 모아 신용평가 모델에 넣고 싶다.',0,'금융감독원 DART의 기업공시 API로 받습니다. 공시 페이지를 크롤링하는 것보다 안정적입니다.']];
var picks={};
$('#pickBox').innerHTML=SCN.map(function(s,i){return '<div class="qi" style="background:rgba(94,227,156,.04);border-color:var(--rule)"><span class="qh" style="color:var(--muted)">상황 '+(i+1)+'</span><p>'+s[0]+'</p><div class="opts" id="pk'+i+'"></div><p class="fb" id="pf'+i+'" aria-live="polite"></p></div>';}).join('');
SCN.forEach(function(s,i){MET.forEach(function(m,j){var b=document.createElement('button');b.className='bt';b.type='button';b.id='pk'+i+'_'+j;b.textContent=m;b.setAttribute('aria-pressed','false');
  b.addEventListener('click',function(){picks[i]=j;$$('#pk'+i+' .bt').forEach(function(z){z.setAttribute('aria-pressed',z===b)});var ok=j===s[1];$('#pf'+i).className='fb '+(ok?'ok':'no');$('#pf'+i).textContent=(ok?'알맞습니다. ':'추천은 '+MET[s[1]]+'. ')+s[2];score2();});$('#pk'+i).appendChild(b);});});
function score2(){var n=Object.keys(picks).length,ok=Object.keys(picks).filter(function(i){return picks[i]===SCN[i][1]}).length;
  kpis($('#k2'),[['i',n+'/6','고른 상황'],['g',ok+'개','알맞은 선택'],['a',(n?Math.round(ok/n*100):0)+'%','적중률']]);
  $('#ins2').innerHTML=n<6?'<p class="a">여섯 상황에 모두 답해 보세요. 버튼은 다시 눌러 바꿀 수 있습니다.</p>':(ok===6?'<p class="g">여섯 개 모두 알맞습니다. 목적 → 출처 → 방법 순서로 생각했군요.</p>':'<p class="r">'+(6-ok)+'개가 다릅니다. 각 상황 아래 설명을 읽어 보세요. "공식 API가 있는가"를 먼저 묻는 습관이 핵심입니다.</p>');}
score2();

/* ---------- ③ 적시성: 배치 vs 스트림 ---------- */
var EV=20,RUN=20000,STREAM=500000,HS=[1,2,4,6,12,24];
var EVT=(function(){var r=rng(5),a=[];for(var d=0;d<30;d++)for(var e=0;e<EV;e++)a.push(r()*24);return a;})();
function cost(h,loss){var delay=0;EVT.forEach(function(t){delay+=h===0?0.05:(Math.ceil(t/h)*h-t);});var avg=delay/EVT.length,ld=avg*loss*EV,run=h===0?STREAM:(24/h)*RUN;return {avg:avg,loss:ld,run:run,tot:ld+run};}
var hCur=24;
LAB.radio('#hBtns',[[0,'스트림(실시간)','h0']].concat(HS.map(function(h){return [h,h+'시간','h'+h]})),24,function(v){hCur=+v;draw3();});
$('#lossH').addEventListener('input',function(){$('#lossHv').textContent=won(+this.value);draw3();});
function draw3(){var loss=+$('#lossH').value,c=$('#c3'),W=fitC(c,330),H=330,x=c.getContext('2d');grid(x,W,H);
  var X=40,Wd=W-70,y0=56,cur=cost(hCur,loss);
  txt(x,'첫째 날 의심 거래 '+EV+'건 · 발생(●) → 처리(|) 까지 기다린 시간',X,22,C.text,13,'left',700);
  x.strokeStyle=C.rule;x.beginPath();x.moveTo(X,y0+40.5);x.lineTo(X+Wd,y0+40.5);x.stroke();
  for(var hh=0;hh<=24;hh+=6)txt(x,hh+'시',X+hh/24*Wd,y0+56,C.muted,10,'center');
  if(hCur>0)for(var k=hCur;k<=24;k+=hCur){var px=X+k/24*Wd;x.strokeStyle=C.gfp;x.lineWidth=2;x.beginPath();x.moveTo(px,y0-6);x.lineTo(px,y0+46);x.stroke();x.lineWidth=1;}
  EVT.slice(0,EV).forEach(function(t,i){var px=X+t/24*Wd,py=y0+(i%5)*8,pe=hCur===0?t+.05:Math.ceil(t/hCur)*hCur;x.strokeStyle='rgba(240,96,77,.6)';x.beginPath();x.moveTo(px,py);x.lineTo(X+pe/24*Wd,py);x.stroke();x.fillStyle=C.eye;x.beginPath();x.arc(px,py,3,0,7);x.fill();});
  /* 아래: 주기별 하루 총비용 막대 */
  var opts=[0].concat(HS),cs=opts.map(function(h){return cost(h,loss)}),mx=Math.max.apply(0,cs.map(function(c){return c.tot}))||1,by=H-34,bh=H-170,bw=Wd/opts.length;
  txt(x,'처리 주기별 하루 총비용 (진한 색 = 처리 비용, 연한 색 = 지연 손실)',X,y0+84,C.muted,12);
  cs.forEach(function(cc,i){var px=X+i*bw+bw*.2,w=bw*.6,h1=cc.run/mx*bh,h2=cc.loss/mx*bh,on=opts[i]===hCur;x.fillStyle=on?C.seq:'#5a6190';x.fillRect(px,by-h1,w,h1);x.fillStyle=on?'rgba(240,96,77,.85)':'rgba(240,96,77,.4)';x.fillRect(px,by-h1-h2,w,h2);
    txt(x,won(cc.tot),px+w/2,by-h1-h2-10,on?C.text:C.muted,10,'center',on?700:500);txt(x,opts[i]===0?'스트림':opts[i]+'h',px+w/2,by+14,on?C.text:C.muted,11,'center');});
  stamp(x,W,'예시값 · 설명용 모형');
  var best=opts[cs.map(function(c){return c.tot}).indexOf(Math.min.apply(0,cs.map(function(c){return c.tot})))];
  kpis($('#k3'),[['i',hCur===0?'약 3분':cur.avg.toFixed(1)+'시간','평균 대기 시간'],['r',won(cur.loss),'하루 지연 손실'],['a',won(cur.run),'하루 처리 비용'],['g',won(cur.tot),'하루 총비용']]);
  $('#eq3').innerHTML='총비용 = 처리 <i>'+won(cur.run)+'</i> + 손실 '+EV+'건 × '+(hCur===0?'0.05':cur.avg.toFixed(2))+'시간 × '+won(loss)+' = <b>'+won(cur.tot)+'</b>';
  $('#ins3').innerHTML='<p class="'+(best===hCur?'g':'a')+'">이 손실 수준에서 가장 싼 선택은 <b>'+(best===0?'스트림':best+'시간 배치')+'</b>입니다.'+(best===hCur?' 지금 고른 주기가 최적입니다.':'')+'</p>'+(loss===0?'<p class="g">손실이 0이면 기다려도 손해가 없으니, 처리 횟수가 적은 하루 배치가 가장 쌉니다. 월간 매출 보고 같은 업무입니다.</p>':'');}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ TCO ---------- */
var ON0=1.2e8,ONM=3e6,ONCAP=80,ONADD=6e7,CLB=5e5,CLTB=1.2e5;
function tco(tb0,g){var on=[ON0],cl=[0],cap=ONCAP,adds=[],tb=tb0,a=ON0,b=0;
  for(var m=1;m<=36;m++){if(tb>cap){a+=ONADD;cap+=ONCAP;adds.push(m);}a+=ONM;b+=CLB+CLTB*tb;on.push(a);cl.push(b);tb*=1+g;}
  var be=null;for(var i=1;i<=36;i++)if(cl[i]>=on[i]){be=i;break;}return {on:on,cl:cl,adds:adds,be:be};}
$('#tb').addEventListener('input',function(){$('#tbv').textContent=this.value+'TB';draw4();});
$('#gr').addEventListener('input',function(){$('#grv').textContent=this.value+'%';draw4();});
function draw4(){var tb=+$('#tb').value,g=+$('#gr').value/100,R=tco(tb,g),c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var X=70,Wd=W-100,base=H-40,mx=Math.max(R.on[36],R.cl[36])*1.05,sx=function(m){return X+m/36*Wd},sy=function(v){return base-v/mx*(H-80)};
  for(var k=0;k<=4;k++){var v=mx*k/4;txt(x,won(v),X-6,sy(v),C.muted,10,'right');x.strokeStyle='rgba(157,155,184,.12)';x.beginPath();x.moveTo(X,sy(v));x.lineTo(X+Wd,sy(v));x.stroke();}
  [0,6,12,18,24,30,36].forEach(function(m){txt(x,m+'개월',sx(m),base+16,C.muted,10,'center');});
  [[R.on,C.amber,'온프레미스'],[R.cl,C.info,'클라우드']].forEach(function(s){x.strokeStyle=s[1];x.lineWidth=2.5;x.beginPath();s[0].forEach(function(v,m){m?x.lineTo(sx(m),sy(v)):x.moveTo(sx(m),sy(v));});x.stroke();x.lineWidth=1;txt(x,s[2],sx(36)-4,sy(s[0][36])-12,s[1],12,'right',700);});
  R.adds.forEach(function(m){x.fillStyle=C.eye;x.beginPath();x.arc(sx(m),sy(R.on[m]),5,0,7);x.fill();});
  if(R.be){x.setLineDash([4,4]);x.strokeStyle=C.gfp;x.beginPath();x.moveTo(sx(R.be),40);x.lineTo(sx(R.be),base);x.stroke();x.setLineDash([]);txt(x,'손익분기 '+R.be+'개월',sx(R.be)+4,46,C.gfp,12,'left',700);}
  stamp(x,W,'예시값 · 실제 단가 아님');
  kpis($('#k4'),[['a',won(R.on[36]),'온프레미스 36개월'],['i',won(R.cl[36]),'클라우드 36개월'],['g',R.be?R.be+'개월':'36개월 안에 없음','손익분기'],['r',R.adds.length+'번','온프레미스 증설']]);
  $('#ins4').innerHTML=R.be?'<p class="a">'+R.be+'개월째부터 클라우드 누적 비용이 온프레미스를 넘습니다. 그 이후까지 쓸 계획이면 온프레미스가 쌉니다.</p>':'<p class="g">36개월 동안 클라우드가 계속 쌉니다. 데이터가 적거나 사업 기간이 짧으면 빌려 쓰는 쪽이 유리합니다.</p>';
  if(R.adds.length)$('#ins4').innerHTML+='<p class="r">데이터가 늘어 온프레미스 용량(80TB)을 넘을 때마다 서버를 더 사야 합니다(빨간 점).</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ k-익명성 ---------- */
var ZIPS=['06236','06237','06611','06614','04524','04525','13529','13530'];
var CUS=(function(){var r=rng(77),a=[];for(var i=0;i<40;i++){a.push({id:'P'+(i<9?'0':'')+(i+1),age:22+Math.floor(r()*44),sex:r()<.5?'여':'남',zip:ZIPS[Math.floor(r()*ZIPS.length)],buy:Math.round(5+r()*45)*1e4});}return a;})();
var gA=0,gZ=0,gS=0;
LAB.radio('#ageBtns',[[0,'그대로','ag0'],[1,'5세 구간','ag1'],[2,'10세 구간','ag2']],0,function(v){gA=+v;draw5();});
LAB.radio('#zipBtns',[[0,'5자리','zp0'],[1,'앞 3자리','zp1'],[2,'앞 2자리','zp2']],0,function(v){gZ=+v;draw5();});
LAB.radio('#sexBtns',[[0,'그대로','sx0'],[1,'삭제','sx1']],0,function(v){gS=+v;draw5();});
function gen(c,a,z,s){var age=a===0?String(c.age):a===1?(Math.floor(c.age/5)*5)+'~'+(Math.floor(c.age/5)*5+4):(Math.floor(c.age/10)*10)+'대';
  var zip=z===0?c.zip:z===1?c.zip.slice(0,3)+'**':c.zip.slice(0,2)+'***';return {age:age,zip:zip,sex:s?'*':c.sex};}
function kStats(a,z,s){var G={};CUS.forEach(function(c){var g=gen(c,a,z,s),k=g.age+'|'+g.sex+'|'+g.zip;(G[k]=G[k]||[]).push(c.id);});var sizes=Object.keys(G).map(function(k){return G[k].length});
  var uniq=0;Object.keys(G).forEach(function(k){if(G[k].length===1)uniq++;});return {G:G,k:Math.min.apply(0,sizes),groups:sizes.length,uniq:uniq};}
function draw5(){var S=kStats(gA,gZ,gS),rows=CUS.map(function(c){var g=gen(c,gA,gZ,gS),key=g.age+'|'+g.sex+'|'+g.zip;return {c:c,g:g,n:S.G[key].length};});
  rows.sort(function(p,q){return p.n-q.n||(p.g.age+p.g.zip).localeCompare(q.g.age+q.g.zip)});
  $('#kTable').innerHTML='<thead><tr><th>가명 ID</th><th>나이</th><th>성별</th><th>우편번호</th><th>월 구매액</th><th>같은 조합 인원</th></tr></thead><tbody>'+rows.map(function(r){var bad=r.n===1;
    return '<tr><td>'+r.c.id+'</td><td'+(gA?' class="fix"':'')+'>'+r.g.age+'</td><td'+(gS?' class="fix"':'')+'>'+r.g.sex+'</td><td'+(gZ?' class="fix"':'')+'>'+r.g.zip+'</td><td>'+r.c.buy.toLocaleString('ko-KR')+'</td><td class="'+(bad?'bad':r.n<3?'miss':'')+'">'+r.n+'명'+(bad?' · 특정 가능':'')+'</td></tr>';}).join('')+'</tbody>';
  kpis($('#k5'),[['r',S.uniq+'명','같은 조합이 혼자뿐인 고객(k = 1)'],['a','k = '+S.k,'가장 작은 묶음'],['i',S.groups+'개','남은 묶음 수(정보량)'],['g',pct((40-S.uniq)/40),'특정되지 않는 고객']]);
  $('#ins5').innerHTML=S.k>=3?'<p class="g">모든 묶음이 '+S.k+'명 이상입니다. 다만 묶음이 '+S.groups+'개로 줄어 지역·나이별 분석은 그만큼 거칠어졌습니다.</p>':
    (S.uniq?'<p class="r">이름을 지웠는데도 '+S.uniq+'명은 같은 조합이 혼자뿐입니다. 다른 데이터와 맞춰 보면 누구인지 알 수 있습니다.</p>':'<p class="a">혼자인 고객은 없지만 k = '+S.k+'입니다. 두 명 중 한 명으로 좁혀지는 것도 위험할 수 있습니다.</p>');}
draw5();
$('#heroK').textContent=kStats(0,0,0).uniq+'명 / 40명';

/* ---------- 대결 (조건부) ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:false,drawMargin:0,metric:'하루 총비용(처리 비용 + 지연 손실). 짧을수록 좋음',fmt:won,
  run:function(){var A0=cost(24,20000),A1=cost(0,20000),B0=cost(24,0),B1=cost(0,0);var mx=Math.max(A0.tot,A1.tot,B0.tot,B1.tot);this.max=mx;
    return {cond:true,fly:A0.tot,robo:A1.tot,condA:{label:'업무 A · 카드 사기 의심 거래 감시 (탐지 전 건당 시간당 2만 원 손실)',fly:A0.tot,robo:A1.tot},condB:{label:'업무 B · 월간 매출 보고 (기다려도 손실 없음)',fly:B0.tot,robo:B1.tot}};},
  report:function(r){return '사기 감시에서는 하루 배치가 '+won(r.condA.fly)+', 스트림이 '+won(r.condA.robo)+'이에요. 월간 보고에서는 하루 배치가 '+won(r.condB.fly)+', 스트림이 '+won(r.condB.robo)+'이에요.';},
  verdict:function(){return '기다리는 동안 손실이 크면 스트림, 손실이 없으면 배치가 싸다. 어느 쪽이 맞는지는 업무의 지연 손실이 정한다. 이 판은 판정하지 않는다.';}});
