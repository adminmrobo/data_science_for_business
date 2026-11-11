/* 13주차 · BI와 KPI — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
function mean(a){return a.reduce(function(s,v){return s+v},0)/a.length}
function fmt(v,d){return v.toLocaleString('ko-KR',{maximumFractionDigits:d||0,minimumFractionDigits:d||0});}
function won(v){var a=Math.abs(v);return a>=1e8?(v/1e8).toFixed(2)+'억 원':a>=1e4?fmt(v/1e4)+'만 원':fmt(v)+'원';}

/* ---------- 히어로 소품: 계기판 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){[[.38,.2,C.gfp],[.56,.2,C.amber],[.74,.2,C.eye]].forEach(function(g,i){var cx=W*g[0],cy=H*g[1],R=Math.min(W,H)*.075;x.strokeStyle='#4a6fa8';x.lineWidth=3;x.beginPath();x.arc(cx,cy,R,Math.PI,0);x.stroke();var a=Math.PI+Math.PI*(.3+.4*(.5+.5*Math.sin(t*.9+i*2)));x.strokeStyle=g[2];x.lineWidth=2.5;x.beginPath();x.moveTo(cx,cy);x.lineTo(cx+Math.cos(a)*R*.85,cy+Math.sin(a)*R*.85);x.stroke();});x.lineWidth=1;});

/* ---------- ① ETL ---------- */
var DAYS=['2026-10-01','2026-10-02','2026-10-03','2026-10-04','2026-10-05','2026-10-06','2026-10-07'];
var SRC=(function(){var r=rng(7),pos=[],onl=[],dlv=[];DAYS.forEach(function(d,i){for(var k=0;k<14;k++)pos.push({d:d,amt:Math.round((18000+r()*30000)/100)*100});for(k=0;k<10;k++)onl.push({d:d,amt:Math.round((25000+r()*40000)/1000)});for(k=0;k<9;k++){var o={id:'D'+i+'-'+k,d:d.slice(5).replace('-','/'),amt:Math.round((15000+r()*20000)/100)*100};dlv.push(o);if(r()<.22)dlv.push({id:o.id,d:o.d,amt:o.amt});}});return {pos:pos,onl:onl,dlv:dlv};})();
function etl(u,dt,dp){var inRange=function(d){return d>='2026-10-01'&&d<='2026-10-07'};var p=SRC.pos.filter(function(o){return inRange(o.d)}).reduce(function(s,o){return s+o.amt},0);
  var o=SRC.onl.filter(function(q){return inRange(q.d)}).reduce(function(s,q){return s+q.amt*(u?1000:1)},0);
  var dl=SRC.dlv.map(function(q){return {id:q.id,d:dt?'2026-'+q.d.replace('/','-'):q.d,amt:q.amt}});if(dp){var seen={};dl=dl.filter(function(q){if(seen[q.id])return false;seen[q.id]=1;return true;});}
  var d=dl.filter(function(q){return inRange(q.d)}).reduce(function(s,q){return s+q.amt},0);return {p:p,o:o,d:d,t:p+o+d,dups:SRC.dlv.length-Object.keys(SRC.dlv.reduce(function(m,q){m[q.id]=1;return m},{})).length};}
var TRUE1=etl(1,1,1);$('#heroEtl').textContent=pct(Math.abs(etl(0,0,0).t-TRUE1.t)/TRUE1.t,0)+' 적게';
['e1','e2','e3'].forEach(function(id){$('#'+id).addEventListener('change',draw1);});
function draw1(){var u=$('#e1').checked,dt=$('#e2').checked,dp=$('#e3').checked,R=etl(u,dt,dp),c=$('#c1'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);
  var bx=function(X,Y,w,h,t1,t2,col){x.fillStyle='rgba(130,184,255,.08)';x.fillRect(X,Y,w,h);x.strokeStyle=col;x.strokeRect(X,Y,w,h);txt(x,t1,X+8,Y+16,col,11,'left',700);if(t2)txt(x,t2,X+8,Y+32,C.muted,10);};
  var cw=Math.max(110,(W-120)/4.4),gap=(W-40-cw*4)/3;[['매장 POS','원 · 2026-10-01',C.info],['온라인몰','천 원 · 2026-10-01',C.amber],['배달앱','원 · 10/01 · 중복 있음',C.eye]].forEach(function(s,i){bx(20,24+i*58,cw,46,s[0],s[1],s[2]);});
  var ex=20+cw+gap;bx(ex,24,cw,162,'ETL','',C.gfp);[['단위 통일',u],['날짜 형식 통일',dt],['중복 제거',dp]].forEach(function(s,i){txt(x,(s[1]?'✔ ':'✘ ')+s[0],ex+10,24+48+i*30,s[1]?C.gfp:C.eye,11,'left',700);});
  bx(ex+cw+gap,24,cw,162,'웨어하우스','통합 테이블',C.text);var dx=ex+2*(cw+gap);bx(dx,24,cw,162,'대시보드','주간 매출',C.amber);txt(x,won(R.t),dx+cw/2,24+100,R.t===TRUE1.t?C.gfp:C.eye,16,'center',700);
  x.strokeStyle=C.muted;[0,1,2].forEach(function(i){x.beginPath();x.moveTo(20+cw,47+i*58);x.lineTo(ex,105);x.stroke();});x.beginPath();x.moveTo(ex+cw,105);x.lineTo(ex+cw+gap,105);x.moveTo(ex+2*cw+gap,105);x.lineTo(dx,105);x.stroke();
  var Y0=212,bh=16,mx=Math.max(TRUE1.p,TRUE1.o,TRUE1.d,R.p,R.o,R.d)*1.05,bw=W-200;[['POS',R.p,TRUE1.p,C.info],['온라인몰',R.o,TRUE1.o,C.amber],['배달앱',R.d,TRUE1.d,C.eye]].forEach(function(b,i){var y=Y0+i*(bh+8);txt(x,b[0],90,y+bh/2,C.muted,10,'right');x.fillStyle=b[3];x.fillRect(96,y,b[1]/mx*bw,bh);x.strokeStyle=C.text;x.setLineDash([3,3]);x.strokeRect(96,y,b[2]/mx*bw,bh);x.setLineDash([]);txt(x,won(b[1]),100+Math.max(b[1],b[2])/mx*bw,y+bh/2,C.text,10);});
  txt(x,'막대 = 지금 집계 · 점선 = 올바른 값',96,H-6,C.muted,10);stamp(x,W,'예시 데이터');
  var err=(R.t-TRUE1.t)/TRUE1.t;
  kpis($('#k1k'),[[Math.abs(err)<.001?'g':'r',won(R.t),'대시보드 주간 매출'],['i',won(TRUE1.t),'올바른 주간 매출'],[Math.abs(err)<.001?'g':'r',(err>=0?'+':'')+(err*100).toFixed(1)+'%','오차'],['a',R.dups+'건','배달앱 중복 기록']]);
  $('#ins1').innerHTML=Math.abs(err)<.001?'<p class="g">세 단계를 모두 거치자 대시보드 숫자가 올바른 값과 같아졌습니다.</p>':'<p class="r">대시보드가 '+won(R.t)+'를 보여 줍니다. 올바른 값보다 '+Math.abs(err*100).toFixed(1)+'% '+(err<0?'적습니다':'많습니다')+'. '+(!u?'온라인몰이 천 원 단위 그대로 더해졌습니다. ':'')+(!dt?'배달앱 주문이 날짜 필터에 걸리지 않았습니다. ':'')+(dt&&!dp?'배달앱 중복 '+R.dups+'건이 두 번 셌습니다.':'')+'</p>';}
draw1();addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 재고 ---------- */
function poisson(r,l){var L=Math.exp(-l),k=0,p=1;do{k++;p*=r();}while(p>L);return k-1;}
var DEM=(function(){var r=rng(12),a=[];for(var i=0;i<365;i++)a.push(poisson(r,20+6*Math.sin(i/365*Math.PI*2)));return a;})(),INV={};
function simInv(rp){if(INV[rp])return INV[rp];var inv=300,pipe=[],out=0,sold=0,lv=[],orders=0;for(var d=0;d<365;d++){pipe=pipe.filter(function(p){if(p.at===d){inv+=p.q;return false;}return true;});var dm=DEM[d],s=Math.min(inv,dm);if(inv<dm)out++;inv-=s;sold+=s;lv.push(inv);if(inv<=rp&&!pipe.length){pipe.push({at:d+5,q:300});orders++;}}
  var avg=mean(lv);return INV[rp]={lv:lv,out:out/365,turn:sold/avg,avg:avg,orders:orders,lost:DEM.reduce(function(a,b){return a+b},0)-sold};}
$('#rp').addEventListener('input',function(){$('#rpv').textContent=this.value;draw2();});
function draw2(){var rp=+$('#rp').value,S=simInv(rp),c=$('#c2'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=46,Y0=24,Wd=(W-110)*.55,Hh=H-60,sx=function(d){return X0+d/119*Wd},sy=function(v){return Y0+Hh-v/560*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,200,400].forEach(function(v){txt(x,v,X0-4,sy(v),C.muted,9,'right');});x.setLineDash([4,3]);x.strokeStyle=C.amber;x.beginPath();x.moveTo(X0,sy(rp));x.lineTo(X0+Wd,sy(rp));x.stroke();x.setLineDash([]);txt(x,'발주점 '+rp,X0+Wd-4,sy(rp)-8,C.amber,10,'right');
  x.strokeStyle=C.info;x.lineWidth=1.8;x.beginPath();for(var d=0;d<120;d++)d?x.lineTo(sx(d),sy(S.lv[d])):x.moveTo(sx(d),sy(S.lv[d]));x.stroke();x.lineWidth=1;for(d=0;d<120;d++)if(S.lv[d]===0){x.fillStyle=C.eye;x.fillRect(sx(d)-1.5,sy(0)-6,3,6);}
  txt(x,'재고 수준(처음 120일) · 빨강 = 품절일',X0,Y0-8,C.text,11,'left',700);[0,30,60,90].forEach(function(v){txt(x,v+'일',sx(v),Y0+Hh+12,C.muted,9,'center');});
  var X1=X0+Wd+50,W1=W-X1-30,RPS=[];for(var q=60;q<=240;q+=10)RPS.push(q);var tm=Math.max.apply(0,RPS.map(function(q){return simInv(q).turn})),rx=function(q){return X1+(q-60)/180*W1};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);
  [['turn',C.gfp,function(v){return Y0+Hh-v/tm*Hh},'재고회전율'],['out',C.eye,function(v){return Y0+Hh-v/.4*Hh},'품절률']].forEach(function(s,k){x.strokeStyle=s[1];x.lineWidth=2;x.beginPath();RPS.forEach(function(q,i){var v=simInv(q)[s[0]];i?x.lineTo(rx(q),s[2](v)):x.moveTo(rx(q),s[2](v));});x.stroke();x.lineWidth=1;txt(x,'— '+s[3],X1+6+k*80,Y0+12,s[1],10,'left',700);});
  x.setLineDash([3,3]);x.strokeStyle=C.text;x.beginPath();x.moveTo(rx(rp),Y0);x.lineTo(rx(rp),Y0+Hh);x.stroke();x.setLineDash([]);[60,150,240].forEach(function(q){txt(x,q,rx(q),Y0+Hh+12,C.muted,9,'center');});txt(x,'발주점',X1+W1/2,H-4,C.muted,10,'center');
  stamp(x,W,'예시 시뮬레이션');
  kpis($('#k2k'),[[S.out>.05?'r':S.out>0?'a':'g',pct(S.out,1),'품절률(품절일 ÷ 365)'],['g',S.turn.toFixed(1)+'회','재고회전율(연)'],['i',Math.round(S.avg)+'개','평균 재고'],['m',fmt(S.lost)+'개','못 판 수량(기회 손실)']]);
  $('#ins2').innerHTML=S.out>.05?'<p class="r">발주점 '+rp+': 리드타임 5일 동안 팔릴 양(평균 약 100개)보다 여유가 적어 1년 중 '+Math.round(S.out*365)+'일이 품절입니다. 회전율은 '+S.turn.toFixed(1)+'회로 높지만 고객은 빈 선반을 봅니다.</p>':S.out===0&&S.avg>220?'<p class="a">발주점 '+rp+': 품절은 없지만 평균 재고가 '+Math.round(S.avg)+'개로 쌓여 회전율이 '+S.turn.toFixed(1)+'회로 내려갔습니다. 과잉재고 비용이 커집니다.</p>':'<p class="g">발주점 '+rp+': 품절 '+Math.round(S.out*365)+'일, 회전율 '+S.turn.toFixed(1)+'회. 두 바늘이 모두 안전 구간 근처입니다.</p>';}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ 광고 퍼널 ---------- */
function funnel(budget,cpm,ctr,cvr,aov){var imp=budget/cpm*1000,clk=imp*ctr,cv=clk*cvr,rev=cv*aov;return {imp:imp,clk:clk,cv:cv,rev:rev,cpc:budget/clk,cpa:budget/cv,roas:rev/budget};}
['cpm','ctr','cvr','aov'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#cpmv').textContent=fmt(+$('#cpm').value);$('#ctrv').textContent=(+$('#ctr').value).toFixed(1);$('#cvrv').textContent=$('#cvr').value;$('#aovv').textContent=$('#aov').value;draw3();});});
function draw3(){var F=funnel(1e7,+$('#cpm').value,+$('#ctr').value/100,+$('#cvr').value/100,+$('#aov').value*1e4),c=$('#c3'),W=fitC(c,280),H=280,x=c.getContext('2d');grid(x,W,H);
  var rows=[['노출',F.imp,'회',C.info],['클릭',F.clk,'회',C.gfp],['전환(구매)',F.cv,'건',C.amber],['매출',F.rev,'',C.eye]],X0=W*.5,maxW=W-160,rh=(H-40)/4,lg=function(v){return Math.log10(Math.max(1,v))};
  var wPrev=0;rows.forEach(function(r,i){var w=i===3?wPrev:Math.max(30,lg(r[1])/lg(F.imp)*maxW*(1-i*.12));wPrev=w;var _=0,y=20+i*rh;x.fillStyle=r[3];x.globalAlpha=.75;x.fillRect(X0-w/2,y,w,rh-14);x.globalAlpha=1;txt(x,r[0]+' '+(r[2]?fmt(r[1])+r[2]:won(r[1])),X0,y+(rh-14)/2,'#111',12,'center',700);
    if(i<2)txt(x,i===0?'CTR '+$('#ctr').value+'%':'전환율 '+$('#cvr').value+'%',X0+maxW/2+8,y+rh-6,C.muted,10);});
  txt(x,'막대 너비는 로그 눈금(매출 막대는 전환과 같은 너비)',16,H-8,C.muted,10);stamp(x,W,'예시 가정');
  kpis($('#k3k'),[['i',fmt(F.cpc)+'원','CPC(클릭당 비용)'],['a',won(F.cpa),'CPA(전환당 비용)'],[F.roas>=1?'g':'r',pct(F.roas,0),'ROAS(매출 ÷ 광고비)'],['m',fmt(F.cv)+'건','전환 수']]);
  $('#ins3').innerHTML=F.roas<1?'<p class="r">ROAS '+pct(F.roas,0)+': 광고비 1,000만 원으로 매출 '+won(F.rev)+'. 광고비도 못 건졌습니다.</p>':'<p class="g">ROAS '+pct(F.roas,0)+': 광고비 1원당 매출 '+F.roas.toFixed(2)+'원. CPC '+fmt(F.cpc)+'원, CPA '+won(F.cpa)+'. 마진을 빼고도 남는지는 따로 확인합니다.</p>';}
addMod($('#c3'),function(dt){if(!dt)draw3();});

/* ---------- ④ 어트리뷰션 ---------- */
var CH=['SNS','디스플레이','이메일','검색'],CHC=[C.stain||'#d672d6',C.info,C.amber,C.gfp];
var JR=[[[0,1,3],12],[[0,3],8],[[1,2,3],15],[[0,2],6],[[1,3],10],[[0,1,2,3],20],[[2,3],9],[[0],5]],at='last';
LAB.radio('#atBtns',[['first','퍼스트 클릭','a0'],['last','라스트 클릭','a1'],['linear','선형 분배','a2']],'last',function(v){at=v;draw4();});
function credit(m){var c=[0,0,0,0];JR.forEach(function(j){var p=j[0],v=j[1];if(m==='first')c[p[0]]+=v;else if(m==='last')c[p[p.length-1]]+=v;else p.forEach(function(k){c[k]+=v/p.length;});});return c;}
function draw4(){var cr=credit(at),c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=20,Y0=26,Wd=(W-60)*.52,rh=(H-46)/JR.length;
  txt(x,'구매 고객 8명의 여정 → 구매액(만 원)',X0,Y0-10,C.text,11,'left',700);JR.forEach(function(j,i){var y=Y0+i*rh,sw=Math.min(70,(Wd-60)/4);j[0].forEach(function(k,s){var px=X0+s*(sw+8);x.fillStyle=CHC[k];x.globalAlpha=.8;x.fillRect(px,y+2,sw,rh-8);x.globalAlpha=1;txt(x,CH[k],px+sw/2,y+rh/2-2,'#111',9,'center',700);if(s<j[0].length-1)txt(x,'→',px+sw+4,y+rh/2-2,C.muted,9,'center');});txt(x,'🛒 '+j[1],X0+j[0].length*(sw+8)+4,y+rh/2-2,C.text,10);});
  var X1=X0+Wd+30,W1=W-X1-16,mx=Math.max.apply(0,['first','last','linear'].map(function(m){return Math.max.apply(0,credit(m))}))*1.05,bh=(H-80)/4;CH.forEach(function(n,k){var y=Y0+10+k*(bh+6),w=cr[k]/mx*(W1-90);txt(x,n,X1+60,y+bh/2,C.muted,10,'right');x.fillStyle=CHC[k];x.fillRect(X1+66,y,w,bh);txt(x,cr[k].toFixed(1)+'만',X1+70+w,y+bh/2,C.text,10);});
  txt(x,'채널별 매출 몫 · '+{first:'퍼스트 클릭',last:'라스트 클릭',linear:'선형 분배'}[at],X1,Y0-10,C.text,11,'left',700);stamp(x,W,'예시 데이터');
  var tot=cr.reduce(function(a,b){return a+b},0),best=cr.indexOf(Math.max.apply(0,cr)),cl=credit('last'),cf=credit('first');
  kpis($('#k4k'),[['g',CH[best]+' '+pct(cr[best]/tot,0),'가장 큰 몫'],['i',pct(cr[3]/tot,0),'검색의 몫'],['a',pct(cr[0]/tot,0),'SNS의 몫'],['m',fmt(tot)+'만 원','총매출(규칙과 무관)']]);
  $('#ins4').innerHTML=at==='last'?'<p class="a">라스트 클릭: 검색이 '+pct(cl[3]/tot,0)+'를 가져갑니다. SNS는 '+pct(cl[0]/tot,0)+'뿐이라 "SNS 예산을 줄이자"는 결론이 나오기 쉽습니다.</p>':at==='first'?'<p class="a">퍼스트 클릭: SNS가 '+pct(cf[0]/tot,0)+'로 뛰고 검색은 '+pct(cf[3]/tot,0)+'로 줄었습니다. 같은 매출, 다른 영웅.</p>':'<p class="g">선형 분배: 여정에 들른 채널마다 똑같이 나눕니다. 극단을 피하지만 "어느 접점이 결정적이었는지"는 말해 주지 않습니다.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ CLV:CAC ---------- */
var DISC=.10;function clv(m,r){return m+m*r/(1+DISC-r);}
['mg','rt','cac'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#mgv').textContent=$('#mg').value;$('#rtv').textContent=$('#rt').value;$('#cacv').textContent=$('#cac').value;draw5();});});
function draw5(){var m=+$('#mg').value,r=+$('#rt').value/100,cac=+$('#cac').value,V=clv(m,r),c=$('#c5'),W=fitC(c,280),H=280,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-90,Hh=H-60,yrs=10,cum=[],s=0;for(var t=0;t<yrs;t++){s+=m*Math.pow(r,t)/Math.pow(1+DISC,t);cum.push(s);}
  var ymax=Math.max(V,cac*3,10)*1.1,sx=function(t){return X0+t/(yrs-1)*Wd},sy=function(v){return Y0+Hh-v/ymax*Hh};x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,ymax/2,ymax].forEach(function(v){txt(x,Math.round(v)+'만',X0-4,sy(v),C.muted,9,'right');});
  [[cac,C.eye,'CAC'],[cac*3,C.amber,'CAC × 3'],[V,C.gfp,'CLV(무한 기간)']].forEach(function(l){x.setLineDash(l[2]==='CLV(무한 기간)'?[2,3]:[5,4]);x.strokeStyle=l[1];x.beginPath();x.moveTo(X0,sy(l[0]));x.lineTo(X0+Wd,sy(l[0]));x.stroke();x.setLineDash([]);txt(x,l[2]+' '+Math.round(l[0])+'만',X0+Wd-4,sy(l[0])-7,l[1],10,'right',700);});
  x.strokeStyle=C.info;x.lineWidth=2.5;x.beginPath();cum.forEach(function(v,t){t?x.lineTo(sx(t),sy(v)):x.moveTo(sx(t),sy(v));});x.stroke();x.lineWidth=1;cum.forEach(function(v,t){x.fillStyle=C.info;x.beginPath();x.arc(sx(t),sy(v),3,0,7);x.fill();txt(x,(t+1)+'년',sx(t),Y0+Hh+12,C.muted,9,'center');});
  txt(x,'— 고객 한 명의 기대 누적 이익(할인율 10%)',X0+6,Y0+12,C.info,11,'left',700);stamp(x,W,'예시 가정');
  var ratio=V/cac,pb=cum.findIndex(function(v){return v>=cac});
  kpis($('#k5k'),[['g',fmt(V,1)+'만 원','고객이 남길 이익(CLV)'],[ratio>=3?'g':ratio>=1?'a':'r',ratio.toFixed(1)+' : 1','CLV : CAC'],['i',pb<0?'10년 안에 못 함':(pb+1)+'년차','획득비 회수 시점'],['m',(1/(1-r)).toFixed(1)+'년','기대 거래 기간(1 ÷ (1 − 유지율))']]);
  $('#ins5').innerHTML=ratio>=3?'<p class="g">CLV : CAC = '+ratio.toFixed(1)+' : 1. 교안의 건강한 기준(3 : 1 이상)을 넘었습니다.</p>':ratio>=1?'<p class="a">CLV : CAC = '+ratio.toFixed(1)+' : 1. 본전은 찾지만 3 : 1에 못 미칩니다. 유지율을 올리거나 획득비를 줄여 보세요.</p>':'<p class="r">CLV가 CAC보다 작습니다. 고객 한 명을 데려올 때마다 손해입니다.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결: CPM vs CPC ---------- */
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.5,max:100,metric:'목표별 점수(두 캠페인 중 더 나은 쪽 = 100)',fmt:function(v){return Math.round(v)+'점'},
  run:function(){var B=1e7,AOV=5e4;var mImp=B/5000*1000,mReach=mImp/4,mRev=mImp*.004*.02*AOV;var cClk=B/500,cImp=cClk/.02,cReach=cImp/5,cRev=cClk*.03*AOV;
    var rM=Math.max(mReach,cReach),rR=Math.max(mRev,cRev);this.info={mReach:mReach,cReach:cReach,mRoas:mRev/B,cRoas:cRev/B};
    return {cond:true,fly:0,robo:0,condA:{label:'목표 A · 도달(신제품을 본 사람 수)',fly:mReach/rM*100,robo:cReach/rM*100},condB:{label:'목표 B · ROAS(광고비 대비 매출)',fly:mRev/rR*100,robo:cRev/rR*100}};},
  report:function(){var I=this.info;return '도달은 CPM '+fmt(I.mReach)+'명 대 CPC '+fmt(I.cReach)+'명으로 초파리 연구원, ROAS는 CPM '+pct(I.mRoas,0)+' 대 CPC '+pct(I.cRoas,0)+'로 주판봇이 앞섰어요.';},
  verdict:function(){return '조건부. 인지도가 목표면 CPM, 매출 효율이 목표면 CPC. KPI를 먼저 정해야 어떤 캠페인이 "좋은지" 말할 수 있다.';}});
