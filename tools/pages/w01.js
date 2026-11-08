/* 1주차 · 비즈니스 데이터 과학의 이해 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,F=LAB.FONT,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;

/* ---------- 히어로 소품: 모니터 막대 + DIKW 계단 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){
  var mx=W*.33,my=H*.14,mw=W*.36,mh=H*.3;x.fillStyle='#0f1020';x.fillRect(mx,my,mw,mh);x.strokeStyle='#4a4f72';x.lineWidth=3;x.strokeRect(mx,my,mw,mh);
  var hs=[.3,.55,.4,.8,.65,.9,.5];hs.forEach(function(h,i){var bw=mw/9,bx=mx+bw*(i+1)-bw*.3,bh=(mh-16)*h*(0.85+0.15*Math.sin(t*1.2+i));x.fillStyle=i===5?C.gfp:C.seq;x.fillRect(bx,my+mh-8-bh,bw*.6,bh);});
  x.fillStyle='#4a4f72';x.fillRect(mx+mw/2-6,my+mh,12,H*.05);
  var cols=['#4a4f72',C.info,C.stain,C.amber];for(var k=0;k<4;k++){var sw=W*.07,sx=W*.74+k*sw*.0,sy=H*.68-(k+1)*H*.065;x.fillStyle=cols[k];x.fillRect(W*.73+k*W*.045,sy,W*.2-k*W*.045,H*.06);}
});

/* ---------- 큰 그림: 의사결정 5단계 ---------- */
var PROC=[['문제 정의','해결하려는 비즈니스 문제를 명확히 하고, SMART 원칙으로 범위·목표·성공 지표를 정합니다. 예: 3개월 안에 고객 이탈률 10% 감소.','3주차에서 자세히'],
  ['데이터 수집','내부(매출·고객·로그)와 외부(공공 데이터·소셜 미디어·시장 조사), 정성(설문·인터뷰·리뷰)과 정량(숫자·통계·로그) 데이터를 모으고 품질을 관리합니다.','2주차에서 자세히'],
  ['분석','기술통계, 상관분석, 회귀분석, 시계열 분석, 분류·군집 분석을 상황에 맞게 씁니다.','①칸 · 4주차 이후'],
  ['해석','통계적 유의성(우연이 아닌지), 상관과 인과의 구분, 편향을 확인하고 인사이트를 끌어냅니다.','②·③칸'],
  ['실행','실행 계획 → 파일럿 테스트 → 지속적 개선 → 성공 사례 공유. 결과를 모니터링해 다시 문제 정의로 돌아갑니다(피드백 루프).','④칸 A/B 테스트']];
var procI=0;
function showProc(i){procI=+i;var p=PROC[procI];$('#procOut').innerHTML='<p class="g"><b>'+(procI+1)+'단계 · '+p[0]+'</b> — '+p[1]+' <span class="muted">('+p[2]+')</span></p>';}
LAB.radio('#procBtns',PROC.map(function(p,i){return [i,(i+1)+'. '+p[0],'proc'+i]}),0,showProc);showProc(0);

/* ---------- ① DIKW ---------- */
var D1=(function(){var r=rng(21),days=[];for(var i=0;i<30;i++){var rain=r()<.35;var s=rain?Math.round(18+gauss(r)*4):Math.max(0,Math.round(3+gauss(r)*2));days.push({d:i+1,rain:rain,s:Math.max(0,s)});}
  var R=days.filter(function(d){return d.rain}).map(function(d){return d.s}),S=days.filter(function(d){return !d.rain}).map(function(d){return d.s});
  return {days:days,mr:LAB.mean(R),ms:LAB.mean(S),nr:R.length,ns:S.length,all:LAB.mean(days.map(function(d){return d.s}))};})();
var stage=0;
LAB.radio('#dikwBtns',[[0,'데이터','dk0'],[1,'정보','dk1'],[2,'지식','dk2'],[3,'지혜','dk3']],0,function(v){stage=+v;draw1();});
$('#rainP').addEventListener('input',function(){$('#rainPv').textContent=this.value+'%';draw1();});
function draw1(){var c=$('#c1'),W=fitC(c,300),x=c.getContext('2d'),H=300;grid(x,W,H);
  var p=+$('#rainP').value/100,exp=p*D1.mr+(1-p)*D1.ms,order=Math.ceil(exp*1.2);
  $('#wisdomCtrl').style.opacity=stage===3?1:.45;
  if(stage===0){x.font='500 13px '+F;x.textBaseline='middle';
    D1.days.forEach(function(d,i){var col=i%10,row=Math.floor(i/10),px=30+col*((W-60)/10),py=60+row*70;x.fillStyle=C.panel2;x.fillRect(px,py-18,(W-60)/10-8,36);x.fillStyle=C.text;x.textAlign='center';x.fillText(String(d.s),px+((W-60)/10-8)/2,py);});
    txt(x,'우산 판매량 30개 (날짜 순서). 아직 아무 의미도 붙지 않았다',20,26,C.muted,13);}
  else{var bw=(W-80)/30,base=H-50,mxv=30;
    x.strokeStyle=C.rule;x.beginPath();x.moveTo(50,base+.5);x.lineTo(W-20,base+.5);x.stroke();
    [0,10,20,30].forEach(function(v){var y=base-v/mxv*(H-110);txt(x,String(v),40,y,C.muted,11,'right');});
    D1.days.forEach(function(d,i){var h=d.s/mxv*(H-110),px=55+i*bw;x.fillStyle=stage>=2?(d.rain?C.info:'#6b6f92'):C.seq;x.fillRect(px,base-h,bw-3,h);
      if(stage>=2&&d.rain){x.fillStyle=C.info;x.fillRect(px+bw/2-3,base+8,4,6);}
      if(i%5===0)txt(x,(i+1)+'일',px,base+24,C.muted,10);});
    if(stage>=2){[[D1.mr,C.info,'비 온 날 평균 '+D1.mr.toFixed(1)],[D1.ms,'#9d9bb8','맑은 날 평균 '+D1.ms.toFixed(1)]].forEach(function(a){var y=base-a[0]/mxv*(H-110);x.setLineDash([6,4]);x.strokeStyle=a[1];x.beginPath();x.moveTo(55,y);x.lineTo(W-20,y);x.stroke();x.setLineDash([]);txt(x,a[2],W-24,y-10,a[1],12,'right',700);});
      txt(x,'파란 막대 = 비 온 날, 회색 = 맑은 날',55,24,C.muted,12);}
    else txt(x,'날짜별 막대그래프: 들쭉날쭉하다는 것까지는 보인다',55,24,C.muted,12);
    if(stage===3){var y=base-exp/mxv*(H-110);x.fillStyle='rgba(94,227,156,.15)';x.fillRect(W-150,40,130,52);x.strokeStyle=C.gfp;x.strokeRect(W-150,40,130,52);txt(x,'내일 발주',W-140,56,C.gfp,12,'left',700);txt(x,order+'개',W-140,78,C.gfp,18,'left',700);}}
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  kpis($('#k1'),[['i',D1.nr+'일 / '+D1.ns+'일','비 온 날 / 맑은 날'],['g',D1.mr.toFixed(1)+'개','비 온 날 평균'],['a',D1.ms.toFixed(1)+'개','맑은 날 평균'],['m',stage===3?order+'개':'–','내일 발주량(지혜)']]);
  $('#eq1').innerHTML=stage<3?'전체 평균 <b>'+D1.all.toFixed(1)+'</b>개 — 평균 하나로는 비 오는 날 품절, 맑은 날 재고가 남는다':'기대 판매 = <i>'+p.toFixed(1)+'</i> × <b>'+D1.mr.toFixed(1)+'</b> + '+(1-p).toFixed(1)+' × '+D1.ms.toFixed(1)+' = <em>'+exp.toFixed(1)+'</em>개 → 안전재고 20% 더해 <b>'+order+'</b>개';
  var M=['<p class="a">데이터 단계: 숫자 30개. 평균을 내도 '+D1.all.toFixed(1)+'개라는 숫자 하나뿐입니다.</p>','<p class="g">정보 단계: 그래프로 그리니 판매량이 크게 오르내린다는 사실이 보입니다. 왜 그런지는 아직 모릅니다.</p>',
    '<p class="g">지식 단계: 날씨를 붙이니 비 온 날 평균('+D1.mr.toFixed(1)+'개)이 맑은 날('+D1.ms.toFixed(1)+'개)의 약 '+(D1.mr/D1.ms).toFixed(0)+'배입니다. 패턴을 찾았습니다.</p>',
    '<p class="m">지혜 단계: 비 올 확률 '+Math.round(p*100)+'%면 기대 판매 '+exp.toFixed(1)+'개, 발주 '+order+'개. 숫자가 행동이 되었습니다. 슬라이더를 움직여 보세요.</p>'];
  $('#ins1').innerHTML=M[stage];}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 생존자 편향 ---------- */
var ZONES=[{k:'엔진',a:.15,p:.3},{k:'조종석',a:.10,p:.5},{k:'동체',a:.45,p:.95},{k:'날개',a:.30,p:.9}];
var showLost=false;
function sim2(engP){var r=rng(42),planes=[];for(var i=0;i<400;i++){var nh=1+Math.floor(r()*5),hits=[],alive=true;
    for(var h=0;h<nh;h++){var u=r(),z=0,acc=0;for(var k=0;k<4;k++){acc+=ZONES[k].a;if(u<acc){z=k;break;}}var pz=k===0?engP:ZONES[z].p;if(z===0)pz=engP;hits.push({z:z,u:r(),v:r()});if(r()>pz)alive=false;}
    planes.push({hits:hits,alive:alive});}
  var res={n:planes.filter(function(p){return p.alive}).length,ret:[0,0,0,0],all:[0,0,0,0],planes:planes};
  planes.forEach(function(p){p.hits.forEach(function(h){res.all[h.z]++;if(p.alive)res.ret[h.z]++;});});return res;}
$('#engP').addEventListener('input',function(){$('#engPv').textContent=this.value+'%';draw2();});
$('#showLost').addEventListener('click',function(){showLost=!showLost;this.setAttribute('aria-pressed',showLost);draw2();});
function zoneRect(z,X,Y,S){/* 비행기 위에서 본 도식: 상대 좌표 */return [[X+S*.42,Y+S*.30,S*.16,S*.12],[X+S*.44,Y+S*.04,S*.12,S*.14],[X+S*.44,Y+S*.18,S*.12,S*.62],[X+S*.06,Y+S*.42,S*.88,S*.14]][z];}
function draw2(){var engP=+$('#engP').value/100,R=sim2(engP),c=$('#c2'),W=fitC(c,330),H=330,x=c.getContext('2d');grid(x,W,H);
  var S=Math.min(280,W*.36),X=20,Y=30;
  /* 도식: 날개 → 동체 → 조종석 → 엔진 순서로 그림 */
  [3,2,1,0].forEach(function(z){var q=zoneRect(z,X,Y,S);x.fillStyle=['rgba(240,96,77,.25)','rgba(130,184,255,.25)','rgba(157,155,184,.22)','rgba(94,227,156,.18)'][z];x.fillRect(q[0],q[1],q[2],q[3]);
    if(z===0){var q2=[X+S*.2,Y+S*.38,S*.1,S*.1];x.fillRect(q2[0],q2[1],q2[2],q2[3]);var q3=[X+S*.7,Y+S*.38,S*.1,S*.1];x.fillRect(q3[0],q3[1],q3[2],q3[3]);}
    txt(x,ZONES[z].k,q[0]+q[2]/2,q[1]-6,C.muted,10,'center');});
  var drawn=0;R.planes.forEach(function(p){if(drawn>140)return;if(!p.alive&&!showLost)return;drawn++;p.hits.forEach(function(h){var q=zoneRect(h.z,X,Y,S);if(h.z===0&&h.u<.66){q=h.u<.33?[X+S*.2,Y+S*.38,S*.1,S*.1]:[X+S*.7,Y+S*.38,S*.1,S*.1];}
    x.fillStyle=p.alive?C.text:C.eye;x.fillRect(q[0]+((h.u*3)%1)*(q[2]-3),q[1]+h.v*(q[3]-3),2.5,2.5);});});
  txt(x,showLost?'흰 점 = 돌아온 비행기, 빨간 점 = 돌아오지 못한 비행기':'흰 점 = 돌아온 비행기의 자국',X,H-14,C.muted,11);
  /* 막대: 부위별 자국 밀도(면적당) — 평균 대비 */
  var src=showLost?R.all:R.ret,tot=src.reduce(function(a,b){return a+b},0),dens=src.map(function(v,i){return v/ZONES[i].a/tot});
  var bx=X+S+50,bw=W-bx-30,mx=Math.max(1.6,Math.max.apply(0,dens));
  txt(x,(showLost?'전체 400대':'돌아온 '+R.n+'대')+' · 부위별 자국 밀도 (평균 = 1)',bx,24,C.text,13,'left',700);
  dens.forEach(function(d,i){var y=50+i*62,w=d/mx*bw;x.fillStyle=C.panel2;x.fillRect(bx,y,bw,30);x.fillStyle=d<0.8?C.eye:C.seq;x.fillRect(bx,y,w,30);txt(x,ZONES[i].k,bx+6,y+15,'#11121a',12,'left',700);txt(x,d.toFixed(2),bx+w+6,y+15,C.text,12,'left',700);});
  var one=bx+bw/mx;x.setLineDash([4,4]);x.strokeStyle=C.amber;x.beginPath();x.moveTo(one,44);x.lineTo(one,300);x.stroke();x.setLineDash([]);
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var dr=R.ret.map(function(v,i){return v/ZONES[i].a/R.ret.reduce(function(a,b){return a+b},0)});
  var minZ=dr.indexOf(Math.min.apply(0,dr));
  kpis($('#k2'),[['i','400대','출격'],['g',R.n+'대','돌아옴'],['r',dr[0].toFixed(2),'돌아온 비행기의 엔진 자국 밀도'],['a',ZONES[minZ].k,'자국이 가장 적은 곳 = 장갑이 필요한 곳']]);
  $('#ins2').innerHTML=showLost?'<p class="g">전체 비행기로 보면 네 부위의 자국 밀도가 모두 1 근처입니다. 총알은 고르게 맞았습니다.</p>':
    (engP>=1?'<p class="g">엔진에 맞아도 모두 돌아오면 걸러지는 비행기가 없으니, 엔진 자국 밀도도 평균 근처('+dr[0].toFixed(2)+')입니다. 편향은 걸러짐에서 생깁니다.</p>':
    '<p class="r">돌아온 비행기만 보면 엔진 자국 밀도가 '+dr[0].toFixed(2)+'로 가장 낮습니다. "엔진은 잘 안 맞는다"가 아니라 "엔진에 맞은 비행기는 돌아오지 못했다"입니다.</p><p class="a">\'돌아오지 못한 비행기도 보기\'를 눌러 확인해 보세요.</p>');}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 상관과 인과 ---------- */
var POP=(function(){var r=rng(283),P=[];for(var i=0;i<2000;i++){var sm=r()<.30,li=r()<(sm?.85:.10),ca=r()<(sm?.15:.02);P.push({sm:sm,li:li,ca:ca});}return P;})();
function rate(f){var a=POP.filter(f);return {n:a.length,k:a.filter(function(p){return p.ca}).length,r:a.filter(function(p){return p.ca}).length/Math.max(1,a.length)};}
var split=false;
LAB.radio('#splitBtns',[[0,'전체로 보기','sp0'],[1,'흡연 여부로 나눠 보기','sp1']],0,function(v){split=v==1;draw3();});
function pp(d){var v=(d*100).toFixed(1);return (v==='-0.0'?'0.0':v)+'%p';}
function phi(){var a=0,b=0,c=0,d=0;POP.forEach(function(p){if(p.li&&p.ca)a++;else if(p.li)b++;else if(p.ca)c++;else d++;});return (a*d-b*c)/Math.sqrt((a+b)*(c+d)*(a+c)*(b+d));}
function draw3(){var c=$('#c3'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var groups=split?[['흡연자',function(p){return p.sm}],['비흡연자',function(p){return !p.sm}]]:[['전체 2,000명',function(){return true}]];
  var gw=(W-60)/groups.length,mx=.25;
  groups.forEach(function(g,gi){var X=40+gi*gw,yes=rate(function(p){return g[1](p)&&p.li}),no=rate(function(p){return g[1](p)&&!p.li});
    txt(x,g[0],X+gw/2-10,26,C.text,14,'center',700);
    [[yes,'라이터 있음',C.eye],[no,'라이터 없음',C.seq]].forEach(function(b,bi){var bh=b[0].r/mx*(H-120),bx=X+gw*.18+bi*gw*.32,bw=gw*.24;x.fillStyle=b[2];x.fillRect(bx,H-60-bh,bw,bh);
      txt(x,pct(b[0].r,1),bx+bw/2,H-72-bh,C.text,13,'center',700);txt(x,b[1],bx+bw/2,H-44,C.muted,12,'center');txt(x,'('+b[0].k+'/'+b[0].n+'명)',bx+bw/2,H-26,C.muted,11,'center');});});
  x.strokeStyle=C.rule;x.beginPath();x.moveTo(30,H-59.5);x.lineTo(W-20,H-59.5);x.stroke();
  stamp(x,W,'예시값 · 실제 의학 통계 아님');
  var Y=rate(function(p){return p.li}),N=rate(function(p){return !p.li});
  var sY=rate(function(p){return p.sm&&p.li}),sN=rate(function(p){return p.sm&&!p.li}),nY=rate(function(p){return !p.sm&&p.li}),nN=rate(function(p){return !p.sm&&!p.li});
  kpis($('#k3'),[['r',(Y.r/N.r).toFixed(1)+'배','전체: 라이터 소지자의 폐암 비율'],['i',phi().toFixed(2),'라이터–폐암 상관(φ)'],['g',pp(sY.r-sN.r),'흡연자 안의 차이'],['g',pp(nY.r-nN.r),'비흡연자 안의 차이']]);
  $('#eq3').innerHTML=split?'흡연자: '+pct(sY.r,1)+' vs '+pct(sN.r,1)+' · 비흡연자: '+pct(nY.r,1)+' vs '+pct(nN.r,1)+' → 층 안에서는 <b>차이가 거의 없다</b>':'P(폐암 | 라이터 있음) = <em>'+pct(Y.r,1)+'</em>,  P(폐암 | 라이터 없음) = <b>'+pct(N.r,1)+'</b>';
  $('#ins3').innerHTML=split?'<p class="g">흡연 여부를 고정하니 라이터 유무에 따른 차이가 흡연자 '+pp(sY.r-sN.r)+', 비흡연자 '+pp(nY.r-nN.r)+'로 거의 0이 되었습니다. 전체에서 보인 '+(Y.r/N.r).toFixed(1)+'배 차이는 흡연이 만든 것입니다.</p>':
    '<p class="r">전체로 보면 라이터 소지자의 폐암 비율이 '+(Y.r/N.r).toFixed(1)+'배 높습니다. 이 표만 보면 "라이터가 위험하다"는 결론이 그럴듯해 보입니다.</p><p class="a">\'흡연 여부로 나눠 보기\'를 눌러 보세요.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ A/B 테스트 ---------- */
var PA=.05,PB=.06,REP=1000,ABC={};
function binom(r,n,p){var k=0;for(var i=0;i<n;i++)if(r()<p)k++;return k;}
function ab(n){if(ABC[n])return ABC[n];var r=rng(11),d=[],okB=0;for(var t=0;t<REP;t++){var a=binom(r,n,PA),b=binom(r,n,PB);d.push((b-a)/n);if(b>a)okB++;}ABC[n]={d:d,okB:okB/REP,mean:LAB.mean(d)};return ABC[n];}
var nCur=100;
LAB.radio('#nBtns',[100,200,500,1000,2000,5000].map(function(n){return [n,n.toLocaleString('ko-KR')+'명','n'+n]}),100,function(v){nCur=+v;draw4();});
function draw4(){var R=ab(nCur),c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var lo=-.06,hi=.08,nb=56,bins=new Array(nb).fill(0);R.d.forEach(function(v){var i=Math.floor((v-lo)/(hi-lo)*nb);if(i<0)i=0;if(i>=nb)i=nb-1;bins[i]++;});
  var mx=Math.max.apply(0,bins),X=40,Wd=W-70,base=H-46,bw=Wd/nb;
  bins.forEach(function(b,i){var v=lo+(i+.5)/nb*(hi-lo),h=b/mx*(H-100);x.fillStyle=v<0?C.eye:C.gfp;x.fillRect(X+i*bw,base-h,bw-1,h);});
  var zx=X+(0-lo)/(hi-lo)*Wd,tx=X+(PB-PA-lo)/(hi-lo)*Wd;
  x.strokeStyle=C.text;x.beginPath();x.moveTo(zx+.5,40);x.lineTo(zx+.5,base);x.stroke();txt(x,'0 (차이 없음)',zx+4,44,C.text,11);
  x.setLineDash([5,4]);x.strokeStyle=C.amber;x.beginPath();x.moveTo(tx+.5,60);x.lineTo(tx+.5,base);x.stroke();x.setLineDash([]);txt(x,'진짜 차이 +1%p',tx+4,64,C.amber,11);
  [-.05,-.025,0,.025,.05,.075].forEach(function(v){var px=X+(v-lo)/(hi-lo)*Wd;txt(x,(v*100).toFixed(1)+'%p',px,base+18,C.muted,10,'center');});
  txt(x,'관측 차이(B − A)의 분포 · 실험 1,000번 · 집단당 '+nCur.toLocaleString('ko-KR')+'명',X,22,C.text,13,'left',700);
  stamp(x,W,'설명용 모형 · 실제 데이터 아님');
  var se=Math.sqrt(PA*(1-PA)/nCur+PB*(1-PB)/nCur);
  kpis($('#k4'),[['g',pct(R.okB,1),'B(정답)를 고른 비율'],['r',pct(1-R.okB,1),'A를 고르거나 비김(틀림)'],['i',(R.mean*100).toFixed(2)+'%p','관측 차이 평균'],['a',(se*100).toFixed(2)+'%p','차이의 표준오차(이론)']]);
  $('#eq4').innerHTML='표준오차 = √(0.05×0.95/<i>'+nCur+'</i> + 0.06×0.94/<i>'+nCur+'</i>) = <b>'+(se*100).toFixed(2)+'%p</b>  vs  진짜 차이 <em>1.00%p</em>';
  $('#ins4').innerHTML=R.okB<.7?'<p class="r">집단당 '+nCur+'명이면 표준오차('+(se*100).toFixed(2)+'%p)가 진짜 차이(1%p)보다 큽니다. 실험 '+Math.round((1-R.okB)*1000)+'번이 틀린 쪽을 골랐습니다.</p>':
    (R.okB<.9?'<p class="a">정답률 '+pct(R.okB,1)+'. 나아졌지만 열 번 중 한두 번은 여전히 틀립니다.</p>':'<p class="g">집단당 '+nCur.toLocaleString('ko-KR')+'명이면 정답률 '+pct(R.okB,1)+'. 분포가 0의 오른쪽으로 거의 다 넘어갔습니다.</p>');}
addMod($('#c4'),function(dt){if(!dt)draw4();});
$('#heroAB').textContent=pct(ab(2000).okB,1);

/* ---------- 대결 ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.01,max:1,metric:'1,000번 반복 실험에서 더 좋은 B를 고른 비율',fmt:function(v){return pct(v,1)},
  run:function(){return {fly:ab(2000).okB,robo:ab(100).okB};},
  report:function(r){return '1,000번 반복해서, 집단당 2,000명으로 정한 초파리 쪽은 '+pct(r.fly,1)+', 첫날 100명으로 정한 주판봇 쪽은 '+pct(r.robo,1)+' 맞게 골랐어요. 주판봇 쪽은 동전 던지기(50%)보다 조금 나은 수준이에요.';},
  verdict:function(r,res){return '표본이 작으면 우연이 결정을 내린다. '+(res==='F'?'초파리 승.':res==='R'?'주판봇 승.':'이번 판은 나눠 갖는다.');}});

/* ---------- 사례 지도 ---------- */
var CASES=[
 ['mining','월마트 · 맥주와 기저귀','고객 구매 데이터를 분석해 함께 팔리는 상품을 찾고 진열을 바꿨다는 사례.','구매 영수증','예상 밖 연관성은 우연일 수 있다. 널리 회자되는 이야기라 세부는 출처마다 다르다.'],
 ['mining','구글 · 독감 트렌드','독감 관련 검색량으로 독감 유행을 예측했다.','검색어','교안이 짚은 한계: 검색 데이터의 신뢰성, 과적합 위험.'],
 ['mining','타깃 · 임신 예측','구매 패턴으로 임신 가능성을 예측해 타깃 광고에 썼다.','구매 이력','효과적이지만 프라이버시 논란이 함께 왔다.'],
 ['mining','링크드인 · 인맥 추천','연결망 데이터로 인맥을 추천하고 영향력 있는 사용자를 찾는다.','소셜 네트워크','네트워크 분석은 관계가 많은 사람 쪽으로 기울기 쉽다.'],
 ['reco','넷플릭스 · 추천','시청 이력과 평점으로 비슷한 취향의 사용자 그룹을 찾아 추천한다.','시청 이력, 평점','교안: 이탈률 감소, 시청 시간 증가. 추천이 취향을 좁힐 수도 있다.'],
 ['reco','스포티파이 · 음악 추천','청취 이력과 플레이리스트로 개인화 음악을 추천한다.','청취 이력','아티스트 발견과 장르 다양화라는 산업 영향도 있다.'],
 ['reco','에어비앤비 · 스마트 프라이싱','위치·리뷰·수요 데이터로 호스트에게 가격을 제안한다.','위치, 리뷰, 수요','가격 제안은 호스트 수익과 고객 만족의 균형 문제다.'],
 ['live','우버 · 동적 요금','시간대·위치·날씨 등 실시간 수요와 공급으로 요금을 정한다.','시간대, 위치, 날씨, 이벤트','공급 부족 때 과도한 요금 인상 논란.'],
 ['live','X(옛 트위터) · 트렌드','전 세계 게시물을 실시간으로 보며 트렌드 키워드를 뽑는다.','실시간 게시물','가짜 뉴스와 봇 계정이 트렌드를 만들 수 있다.'],
 ['ai','지메일 · 스팸 차단','내용·발신자·첨부파일과 사용자의 스팸 표시 행동으로 학습한다.','이메일, 사용자 행동','스팸·피싱·멀웨어 차단 생태계.'],
 ['ai','페이스북(메타) · 이미지 태깅','딥러닝 얼굴 인식으로 사진에 자동 태그를 붙였다.','사진','편리함과 프라이버시가 충돌했고, 잘못된 분류 논란도 있었다.'],
 ['ai','쿠팡 · 개인화','추천과 개인화에 머신러닝을 쓴다. 교안은 "가격이 없는 페이지"를 왜 만들었는지 묻는다.','검색·구매 이력','개인화된 화면은 사람마다 다르게 보인다.'],
 ['ai','아마존 · DASH와 예측 배송','버튼 한 번 주문과 예측 배송. 데이터 기반 의사결정의 성공 사례로 교안이 소개.','주문 이력','교안 시점의 서비스 사례다.']];
var CG={all:'전체',mining:'데이터마이닝·빅데이터',reco:'개인화·추천',live:'실시간 분석',ai:'AI 모델'};
function showCases(g){$('#caseGrid').innerHTML=CASES.filter(function(c){return g==='all'||c[0]===g}).map(function(c){return '<div><b>'+c[1]+'</b><span class="lvtag" style="align-self:flex-start">'+CG[c[0]]+'</span><p>'+c[2]+'</p><p class="muted" style="font-size:14px">데이터: '+c[3]+'</p><p class="warn">조심할 점: '+c[4]+'</p></div>';}).join('');}
LAB.radio('#caseBtns',Object.keys(CG).map(function(k){return [k,CG[k],'cg_'+k]}),'all',showCases);showCases('all');
