/* 14주차 · 고급 분석 기법 — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
var sig=function(z){return 1/(1+Math.exp(-z))};
function mean(a){return a.reduce(function(s,v){return s+v},0)/a.length}
function sdv(a){var m=mean(a);return Math.sqrt(mean(a.map(function(v){return (v-m)*(v-m)})));}
var GC=[C.info,C.amber,C.gfp,C.eye,C.stain||'#d672d6','#9ab8ff'];

/* ---------- 신경망·로지스틱 (⑤·대결·히어로 공용) ---------- */
function mlp(D,H,it,seed){var r=rng(seed),W1=[],b1=[],W2=[],b2=0;for(var h=0;h<H;h++){W1.push([gauss(r)*.8,gauss(r)*.8]);b1.push(gauss(r)*.3);W2.push(gauss(r)*.5);}var lr=.3,n=D.length;
  for(var t=0;t<it;t++){var gW1=W1.map(function(){return [0,0]}),gb1=new Array(H).fill(0),gW2=new Array(H).fill(0),gb2=0;
    D.forEach(function(d){var a=W1.map(function(w,h){return Math.tanh(w[0]*d.x[0]+w[1]*d.x[1]+b1[h])}),z=b2;for(var h=0;h<H;h++)z+=a[h]*W2[h];var e=sig(z)-d.y;gb2+=e;for(h=0;h<H;h++){gW2[h]+=e*a[h];var dh=e*W2[h]*(1-a[h]*a[h]);gW1[h][0]+=dh*d.x[0];gW1[h][1]+=dh*d.x[1];gb1[h]+=dh;}});
    b2-=lr*gb2/n;for(var h=0;h<H;h++){W2[h]-=lr*gW2[h]/n;W1[h][0]-=lr*gW1[h][0]/n;W1[h][1]-=lr*gW1[h][1]/n;b1[h]-=lr*gb1[h]/n;}}
  return function(x){var z=b2;for(var h=0;h<H;h++)z+=Math.tanh(W1[h][0]*x[0]+W1[h][1]*x[1]+b1[h])*W2[h];return sig(z);};}
function logi(D,it){var w=[0,0,0];for(var t=0;t<it;t++){var g=[0,0,0];D.forEach(function(d){var e=sig(w[0]+w[1]*d.x[0]+w[2]*d.x[1])-d.y;g[0]+=e;g[1]+=e*d.x[0];g[2]+=e*d.x[1];});for(var k=0;k<3;k++)w[k]-=.5*g[k]/D.length;}var f=function(x){return sig(w[0]+w[1]*x[0]+w[2]*x[1])};f.w=w;return f;}
function acc(f,D){return D.filter(function(d){return (f(d.x)>=.5?1:0)===d.y}).length/D.length;}
var RING=(function(){var r=rng(4),a=[];for(var i=0;i<200;i++){var inn=i%2===0,rad=inn?Math.sqrt(r())*.9:1.3+r()*.9,an=r()*6.283;a.push({x:[rad*Math.cos(an),rad*Math.sin(an)],y:inn?1:0});}return a;})(),NN={};
function net(H){return NN[H]||(NN[H]=H?mlp(RING,H,2000,5):logi(RING,2000));}

/* ---------- 히어로 소품 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var cx=[W*.36,W*.48,W*.42],cy=[H*.12,H*.14,H*.28];for(var g=0;g<3;g++)for(var k=0;k<7;k++){var a=k*.9+t*.4+g,rr=12+(k%3)*6;x.fillStyle=GC[g];x.beginPath();x.arc(cx[g]+Math.cos(a)*rr,cy[g]+Math.sin(a)*rr*.6,3,0,7);x.fill();}
  var L=[[3,W*.66],[4,W*.74],[1,W*.82]];x.strokeStyle='rgba(130,184,255,.35)';for(var i=0;i<2;i++)for(var a2=0;a2<L[i][0];a2++)for(var b=0;b<L[i+1][0];b++){x.beginPath();x.moveTo(L[i][1],H*.06+(a2+1)*H*.3/(L[i][0]+1));x.lineTo(L[i+1][1],H*.06+(b+1)*H*.3/(L[i+1][0]+1));x.stroke();}
  L.forEach(function(l,i){for(var a3=0;a3<l[0];a3++){x.fillStyle=i===1?C.amber:C.gfp;x.beginPath();x.arc(l[1],H*.06+(a3+1)*H*.3/(l[0]+1),5+Math.sin(t*2+a3)*1,0,7);x.fill();}});});
$('#heroRing').textContent=pct(acc(net(0),RING),0)+' → '+pct(acc(net(4),RING),0);

/* ---------- ① K-means ---------- */
var CU=(function(){var r=rng(141),a=[];[[15,10,180,35],[70,25,80,25],[220,50,60,25]].forEach(function(p){for(var i=0;i<50;i++)a.push([Math.max(1,p[0]+gauss(r)*p[1]),Math.max(5,p[2]+gauss(r)*p[3])]);});return a;})();
var MU=[mean(CU.map(function(p){return p[0]})),mean(CU.map(function(p){return p[1]}))],SD=[sdv(CU.map(function(p){return p[0]})),sdv(CU.map(function(p){return p[1]}))],CZ=CU.map(function(p){return [(p[0]-MU[0])/SD[0],(p[1]-MU[1])/SD[1]]});
var INIT=(function(){var r=rng(7),idx=CZ.map(function(_,i){return i});for(var i=idx.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t;}return idx;})();
function d2(a,b){return (a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]);}
function kmeans(K,steps){var cen=INIT.slice(0,K).map(function(i){return CZ[i].slice()}),hist=[cen.map(function(c){return c.slice()})],lab;
  function assign(){return CZ.map(function(p){var b=0;for(var k=1;k<K;k++)if(d2(p,cen[k])<d2(p,cen[b]))b=k;return b;});}
  lab=assign();for(var s=0;s<steps;s++){for(var k=0;k<K;k++){var m=CZ.filter(function(_,i){return lab[i]===k});if(m.length)cen[k]=[mean(m.map(function(p){return p[0]})),mean(m.map(function(p){return p[1]}))];}hist.push(cen.map(function(c){return c.slice()}));lab=assign();}
  var inertia=CZ.reduce(function(s,p,i){return s+d2(p,cen[lab[i]])},0);return {cen:cen,lab:lab,hist:hist,inertia:inertia};}
['kk','it'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#kkv').textContent=$('#kk').value;$('#itv').textContent=$('#it').value;draw1();});});
function draw1(){var K=+$('#kk').value,S=+$('#it').value,R=kmeans(K,S),c=$('#c1'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=(W-120)*.62,Hh=H-60,sx=function(v){return X0+v/365*Wd},sy=function(v){return Y0+Hh-v/280*Hh},ux=function(z){return z*SD[0]+MU[0]},uy=function(z){return z*SD[1]+MU[1]};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,100,200,300].forEach(function(v){txt(x,v+'일',sx(v),Y0+Hh+12,C.muted,9,'center');});[0,100,200].forEach(function(v){txt(x,v+'만',X0-4,sy(v),C.muted,9,'right');});
  CU.forEach(function(p,i){x.fillStyle=S===0?'rgba(157,155,184,.6)':GC[R.lab[i]];x.beginPath();x.arc(sx(p[0]),sy(p[1]),3.2,0,7);x.fill();});
  R.hist.forEach(function(cs,s){cs.forEach(function(cz,k){if(s>0){var pr=R.hist[s-1][k];x.strokeStyle='rgba(236,234,243,.5)';x.beginPath();x.moveTo(sx(ux(pr[0])),sy(uy(pr[1])));x.lineTo(sx(ux(cz[0])),sy(uy(cz[1])));x.stroke();}});});
  R.cen.forEach(function(cz,k){var px=sx(ux(cz[0])),py=sy(uy(cz[1]));x.fillStyle=GC[k];x.strokeStyle=C.text;x.lineWidth=2;x.beginPath();for(var a=0;a<10;a++){var rr=a%2?5:12,an=-Math.PI/2+a*Math.PI/5;x.lineTo(px+rr*Math.cos(an),py+rr*Math.sin(an));}x.closePath();x.fill();x.stroke();x.lineWidth=1;});
  txt(x,'가로: 마지막 구매 후 지난 일수 · 세로: 연간 구매액(만 원)',X0+6,Y0+12,C.muted,10);
  var X1=X0+Wd+50,W1=W-X1-16,ins=[];for(var q=2;q<=6;q++)ins.push(kmeans(q,10).inertia);var mx=Math.max.apply(0,ins),ex=function(q){return X1+(q-2)/4*W1},ey=function(v){return Y0+Hh-v/mx*Hh};x.strokeStyle=C.rule;x.strokeRect(X1,Y0,W1,Hh);
  x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();ins.forEach(function(v,i){i?x.lineTo(ex(i+2),ey(v)):x.moveTo(ex(i+2),ey(v));});x.stroke();x.lineWidth=1;ins.forEach(function(v,i){x.fillStyle=i+2===K?C.gfp:C.amber;x.beginPath();x.arc(ex(i+2),ey(v),i+2===K?6:4,0,7);x.fill();txt(x,'K='+(i+2),ex(i+2),Y0+Hh+12,C.muted,9,'center');});
  txt(x,'엘보우: 군집 내 거리 제곱합',X1,Y0-8,C.text,11,'left',700);stamp(x,W,'예시 데이터');
  var sizes=[];for(var k=0;k<K;k++)sizes.push(R.lab.filter(function(l){return l===k}).length);var vip=R.cen.map(function(cz,k){return [uy(cz[1]),k]}).sort(function(a,b){return b[0]-a[0]})[0];
  kpis($('#k1k'),[['i',sizes.join(' · '),'군집별 고객 수'],['a',R.inertia.toFixed(1),'그룹 안 흩어짐(거리 제곱합)'],['g',Math.round(ux(R.cen[vip[1]][0]))+'일 · '+Math.round(vip[0])+'만','구매액이 가장 큰 군집의 중심'],['m',S+'회','반복']]);
  $('#ins1').innerHTML=S===0?'<p class="a">반복 0: 처음 고른 중심(별)만 있고 아직 배정 전입니다. 반복을 올려 보세요.</p>':K===3?'<p class="g">K = 3, 반복 '+S+': 최근에 많이 사는 고객, 중간 고객, 오래 안 온 고객으로 나뉘었습니다. 마케팅이라면 VIP 관리 · 일반 육성 · 이탈 방지 캠페인으로 이어집니다.</p>':'<p class="a">K = '+K+': '+(K<3?'서로 다른 고객이 한 무리에 섞였습니다.':'한 무리가 둘로 쪼개져 의미 차이가 작은 세그먼트가 생겼습니다.')+' 엘보우 그림의 꺾이는 점은 K = 3 근처입니다.</p>';}
addMod($('#c1'),function(dt){if(!dt)draw1();});

/* ---------- ② 연관 규칙 ---------- */
var IT=['라면','김치','계란','우유','빵','커피'],BASK=(function(){var r=rng(142),a=[];for(var i=0;i<400;i++){var b={};if(r()<.3)b[0]=1;if(b[0]&&r()<.65)b[1]=1;else if(r()<.08)b[1]=1;if(r()<.25)b[2]=1;if(b[0]&&r()<.3)b[2]=1;if(r()<.22)b[4]=1;if(b[4]&&r()<.6)b[3]=1;else if(r()<.15)b[3]=1;if(r()<.45)b[5]=1;var k=Object.keys(b).map(Number);if(!k.length)k=[5];a.push(k);}return a;})();
function supp(S){return BASK.filter(function(b){return S.every(function(i){return b.indexOf(i)>=0})}).length/BASK.length;}
var RULES=(function(){var o=[];for(var a=0;a<6;a++)for(var b=0;b<6;b++){if(a===b)continue;o.push([[a],b]);for(var c=a+1;c<6;c++){if(c===b)continue;o.push([[a,c],b]);}}return o.map(function(r){var sx=supp(r[0]),sxy=supp(r[0].concat([r[1]])),sy=supp([r[1]]);return {x:r[0],y:r[1],s:sxy,c:sx?sxy/sx:0,l:sx&&sy?sxy/sx/sy:0};});})();
['ms','mc'].forEach(function(id){$('#'+id).addEventListener('input',function(){$('#msv').textContent=$('#ms').value;$('#mcv').textContent=$('#mc').value;draw2();});});
function draw2(){var ms=+$('#ms').value/100,mc=+$('#mc').value/100,K=RULES.filter(function(r){return r.s>=ms&&r.c>=mc}).sort(function(a,b){return b.l-a.l});
  var rows=K.slice(0,10).map(function(r){return '<tr><td>'+r.x.map(function(i){return IT[i]}).join(' + ')+' → '+IT[r.y]+'</td><td>'+pct(r.s,1)+'</td><td>'+pct(r.c,0)+'</td><td class="'+(r.l>=1.5?'fix':r.l<1.1?'bad':'')+'">'+r.l.toFixed(2)+'</td></tr>'}).join('');
  $('#rules2').innerHTML='<thead><tr><th>규칙(향상도 순, 최대 10개)</th><th>지지도</th><th>신뢰도</th><th>향상도</th></tr></thead><tbody>'+(rows||'<tr><td colspan="4">조건을 만족하는 규칙이 없습니다.</td></tr>')+'</tbody>';
  var weak=K.filter(function(r){return r.l<1.1}).length;
  kpis($('#k2k'),[['i',RULES.length+'개','가능한 규칙(1·2개 → 1개)'],['g',K.length+'개','기준선을 통과한 규칙'],['a',weak+'개','통과했지만 향상도 1.1 미만'],['m',K.length?K[0].x.map(function(i){return IT[i]}).join('+')+'→'+IT[K[0].y]:'—','향상도 1위']]);
  $('#ins2').innerHTML=!K.length?'<p class="r">기준선이 너무 높아 규칙이 하나도 남지 않았습니다.</p>':weak?'<p class="a">통과한 '+K.length+'개 중 '+weak+'개는 향상도가 1.1 미만입니다. 대부분 "커피"처럼 원래 많이 팔리는 상품이 결과인 규칙입니다. 신뢰도만 보면 속습니다.</p>':'<p class="g">남은 '+K.length+'개 규칙이 모두 향상도 1.1 이상입니다. 진열·묶음 할인 후보로 볼 만합니다.</p>';}
draw2();

/* ---------- ③ 감성 분석 ---------- */
var POS={'좋다':1,'빠르다':1,'만족':1,'최고':1,'재구매':1,'친절':1,'자세하다':1,'믿다':1},NEG={'불친절':1,'실망':1,'나쁘다':1,'별로':1,'느리다':1,'아쉽다':1,'엉망':1,'최악':1},NOT_PREV={'않다':1},NOT_NEXT={'안':1,'못':1};
var REV=[['배송이 빠르고 포장도 좋아요',['배송','빠르다','포장','좋다'],1],['직원이 불친절해서 실망했어요',['직원','불친절','실망'],-1],['가격 대비 나쁘지 않아요',['가격','대비','나쁘다','않다'],1],['생각보다 별로였어요',['생각','별로'],-1],['최고예요 또 살게요',['최고','재구매'],1],['배송이 느려서 아쉬웠어요',['배송','느리다','아쉽다'],-1],
  ['맛은 좋은데 양이 너무 적어요',['맛','좋다','양','적다'],-1],['기대 안 했는데 만족스러워요',['기대','안','하다','만족'],1],['참 잘도 빠르네요 일주일 걸림',['참','잘','빠르다','일주일','걸리다'],-1],['친절하고 설명도 자세해요',['친절','설명','자세하다'],1],['포장이 엉망이라 최악',['포장','엉망','최악'],-1],['품질은 못 믿겠어요',['품질','못','믿다'],-1]],neg=false;
function score(tk,useNeg){var v=tk.map(function(t){return POS[t]?1:NEG[t]?-1:0});if(useNeg){tk.forEach(function(t,i){if(NOT_PREV[t]){for(var j=i-1;j>=0;j--)if(v[j]){v[j]=-v[j];break;}}if(NOT_NEXT[t]){for(j=i+1;j<tk.length;j++)if(v[j]){v[j]=-v[j];break;}}});}return {s:v.reduce(function(a,b){return a+b},0),v:v};}
LAB.radio('#ngBtns',[['off','끄기','n0'],['on','켜기','n1']],'off',function(v){neg=v==='on';draw3();});
function draw3(){var ok=0,rows=REV.map(function(r){var S=score(r[1],neg),p=S.s>0?1:S.s<0?-1:0,hit=p===r[2];if(hit)ok++;var tk=r[1].map(function(t,i){return S.v[i]>0?'<b style="color:var(--gfp)">'+t+'</b>':S.v[i]<0?'<b style="color:var(--eye)">'+t+'</b>':(NOT_PREV[t]||NOT_NEXT[t])&&neg?'<u>'+t+'</u>':t}).join(' · ');
    return '<tr><td>'+r[0]+'</td><td style="font-size:13px">'+tk+'</td><td>'+(S.s>0?'+':'')+S.s+'</td><td>'+(p>0?'긍정':p<0?'부정':'중립')+'</td><td>'+(r[2]>0?'긍정':'부정')+'</td><td class="'+(hit?'fix':'bad')+'">'+(hit?'맞음':'틀림')+'</td></tr>'}).join('');
  $('#sent3').innerHTML='<thead><tr><th>리뷰</th><th>토큰(초록 +1, 빨강 −1)</th><th>점수</th><th>판정</th><th>정답</th><th></th></tr></thead><tbody>'+rows+'</tbody>';
  var a0=REV.filter(function(r){var s=score(r[1],false).s;return (s>0?1:s<0?-1:0)===r[2]}).length,a1=REV.filter(function(r){var s=score(r[1],true).s;return (s>0?1:s<0?-1:0)===r[2]}).length;
  kpis($('#k3k'),[[ok>=10?'g':'a',ok+' / 12','지금 맞힌 리뷰'],['i',a0+' / 12','부정어 처리 끔'],['i',a1+' / 12','부정어 처리 켬'],['r','3개','사전으로 풀기 어려운 리뷰(비꼼·섞임·부정어 범위)']]);
  $('#ins3').innerHTML=neg?'<p class="a">부정어 처리를 켜자 "나쁘지 않아요"·"못 믿겠어요"는 맞혔지만, "기대 안 했는데 만족"의 "안"이 "만족"까지 뒤집었습니다. 12개 중 '+ok+'개.</p>':'<p class="a">사전만 쓰면 12개 중 '+ok+'개. "나쁘지 않아요"는 "나쁘다" 때문에 부정, "참 잘도 빠르네요"는 "빠르다" 때문에 긍정으로 판정됩니다.</p>';}
draw3();

/* ---------- ④ TF-IDF ---------- */
var DOCS=[['배송 늦다 배송 지연 문의','배송','늦다','배송','지연','문의'],['배송 빠르다 포장 꼼꼼 만족','배송','빠르다','포장','꼼꼼','만족'],['환불 요청 환불 지연 상담 연결 안되다','환불','요청','환불','지연','상담','연결','안되다'],['상담 친절 배송 빠르다','상담','친절','배송','빠르다'],['포장 파손 교환 요청 배송','포장','파손','교환','요청','배송'],['앱 오류 결제 실패 결제 다시','앱','오류','결제','실패','결제','다시']].map(function(d){return d.slice(1)}),dk=0;
var DF={};DOCS.forEach(function(d){var u={};d.forEach(function(t){u[t]=1;});Object.keys(u).forEach(function(t){DF[t]=(DF[t]||0)+1;});});
LAB.radio('#docBtns',DOCS.map(function(_,i){return [String(i),(i+1)+'번','dc'+i]}),'0',function(v){dk=+v;draw4();});
function draw4(){var d=DOCS[dk],cnt={};d.forEach(function(t){cnt[t]=(cnt[t]||0)+1;});var T=Object.keys(cnt).map(function(t){var tf=cnt[t]/d.length,idf=Math.log(DOCS.length/DF[t]);return {t:t,tf:tf,idf:idf,ti:tf*idf};}).sort(function(a,b){return b.ti-a.ti});
  var c=$('#c4'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);txt(x,(dk+1)+'번 문서: '+d.join(' '),20,20,C.text,12,'left',700);var X0=90,Y0=40,Wd=(W-140)/2,bh=Math.min(28,(H-60)/T.length-6),mxT=Math.max.apply(0,T.map(function(q){return q.tf})),mxI=Math.max.apply(0,T.map(function(q){return q.ti}))||1;
  txt(x,'TF(문서 안 빈도)',X0,Y0-4,C.info,11,'left',700);txt(x,'TF-IDF',X0+Wd+30,Y0-4,C.gfp,11,'left',700);
  T.forEach(function(q,i){var y=Y0+6+i*(bh+6);txt(x,q.t+' (df '+DF[q.t]+')',X0-6,y+bh/2,C.muted,10,'right');x.fillStyle=C.info;x.fillRect(X0,y,q.tf/mxT*(Wd-40),bh);txt(x,q.tf.toFixed(2),X0+q.tf/mxT*(Wd-40)+4,y+bh/2,C.text,10);x.fillStyle=C.gfp;x.fillRect(X0+Wd+30,y,q.ti/mxI*(Wd-40),bh);txt(x,q.ti.toFixed(3),X0+Wd+34+q.ti/mxI*(Wd-40),y+bh/2,C.text,10);});
  stamp(x,W,'예시 VOC');
  kpis($('#k4k'),[['g',T[0].t,'TF-IDF 1위'],['i',T.slice().sort(function(a,b){return b.tf-a.tf})[0].t,'TF 1위'],['a',DF['배송']+' / 6','"배송"이 나온 문서 수'],['m',Math.log(6/DF['배송']).toFixed(3),'"배송"의 희귀도(IDF)']]);
  var b=cnt['배송'];$('#ins4').innerHTML=b?'<p class="a">이 문서에도 "배송"이 '+b+'번 나오지만 6건 중 '+DF['배송']+'건에 나오는 흔한 단어라 TF-IDF가 낮습니다. 핵심어는 "'+T[0].t+'"입니다.</p>':'<p class="g">이 문서의 핵심어는 "'+T[0].t+'"(TF-IDF '+T[0].ti.toFixed(3)+'). 다른 문서에 거의 없는 단어일수록 위로 올라옵니다.</p>';}
addMod($('#c4'),function(dt){if(!dt)draw4();});

/* ---------- ⑤ 신경망 ---------- */
var hn=4;
LAB.radio('#hnBtns',[['0','0 (로지스틱)','h0'],['2','2','h1'],['4','4','h2'],['8','8','h3']],'4',function(v){hn=+v;draw5();});
function draw5(){var f=net(hn),c=$('#c5'),W=fitC(c,320),H=320,x=c.getContext('2d');grid(x,W,H);var S=Math.min(W*.55,H-40),X0=30,Y0=20,lim=2.4,sx=function(v){return X0+(v+lim)/(2*lim)*S},sy=function(v){return Y0+S-(v+lim)/(2*lim)*S},G=48;
  for(var j=0;j<G;j++)for(var i=0;i<G;i++){var p=f([-lim+(i+.5)/G*2*lim,-lim+(j+.5)/G*2*lim]);x.fillStyle=p>=.5?'rgba(130,184,255,'+(.08+.2*p)+')':'rgba(240,96,77,'+(.08+.2*(1-p))+')';x.fillRect(X0+i*S/G,Y0+S-(j+1)*S/G,S/G+.5,S/G+.5);}
  RING.forEach(function(d){x.fillStyle=d.y?C.info:C.eye;x.beginPath();x.arc(sx(d.x[0]),sy(d.x[1]),3,0,7);x.fill();});x.strokeStyle=C.rule;x.strokeRect(X0,Y0,S,S);
  var X1=X0+S+40,W1=W-X1-50,lay=[2,hn,1],cols=[C.text,C.amber,C.gfp],lx=function(k){return X1+k*(W1/2)};lay.forEach(function(n,k){if(!n)return;for(var a=0;a<n;a++){var y=Y0+(a+1)*S/(n+1);var nk=k+1<3&&lay[k+1]?k+1:k+2<3?k+2:-1;if(nk>0){for(var b=0;b<lay[nk];b++){x.strokeStyle='rgba(130,184,255,.35)';x.beginPath();x.moveTo(lx(k),y);x.lineTo(lx(nk),Y0+(b+1)*S/(lay[nk]+1));x.stroke();}}x.fillStyle=cols[k];x.beginPath();x.arc(lx(k),y,7,0,7);x.fill();}});
  txt(x,'입력 2',lx(0),Y0+S+14,C.muted,10,'center');if(hn)txt(x,'은닉 '+hn+' (tanh)',lx(1),Y0+S+14,C.amber,10,'center');txt(x,'출력 1',lx(2),Y0+S+14,C.gfp,10,'center');stamp(x,W,'예시 데이터');
  var a=acc(f,RING),nP=hn?hn*3+hn+1:3;
  kpis($('#k5k'),[[a>.95?'g':a>.7?'a':'r',pct(a,1),'학습 데이터 정확도'],['i',nP+'개','배운 숫자 개수'],['m',hn?hn+'개':'없음','은닉 뉴런'],['a','2,000회','고친 횟수(경사 하강)']]);
  $('#ins5').innerHTML=hn===0?'<p class="r">은닉층이 없으면 로지스틱 회귀입니다. 직선 하나로는 원을 가를 수 없어 '+pct(a,1)+'.</p>':hn===2?'<p class="a">뉴런 2개: 직선 두 개를 조합해 띠 모양 경계를 만들었습니다. '+pct(a,1)+'.</p>':'<p class="g">뉴런 '+hn+'개: 원을 감싸는 경계를 스스로 배웠습니다. '+pct(a,1)+'. 가중치 '+nP+'개를 학습했습니다.</p>';}
addMod($('#c5'),function(dt){if(!dt)draw5();});

/* ---------- 대결 ---------- */
function linData(n,seed){var r=rng(seed),a=[];for(var i=0;i<n;i++){var x=[gauss(r),gauss(r)],y=(.9*x[0]-.6*x[1]+.2+gauss(r)*.5)>0?1:0;a.push({x:x,y:y});}return a;}
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.01,max:1,metric:'처음 보는 대출 신청 400명 정확도',fmt:function(v){return pct(v,2)},
  run:function(){var tr=linData(400,1),te=linData(400,2),L=logi(tr,2000),M=mlp(tr,8,2000,3);this.info={w:L.w,trL:acc(L,tr),trM:acc(M,tr)};return {fly:acc(M,te),robo:acc(L,te)};},
  report:function(r){var I=this.info;return '신경망은 가중치 33개로 '+pct(r.fly,2)+', 로지스틱 회귀는 계수 3개로 '+pct(r.robo,2)+'를 맞혔어요. 로지스틱의 식은 z = '+I.w[0].toFixed(2)+' + '+I.w[1].toFixed(2)+'×소득 '+(I.w[2]<0?'− ':'+ ')+Math.abs(I.w[2]).toFixed(2)+'×부채예요.';},
  verdict:function(r,res){return res==='D'?'무승부. 경계가 직선이면 층을 쌓아도 정확도는 거의 같다. 같다면 설명할 수 있는 쪽이 현장에서 이긴다.':res==='F'?'초파리 승.':'주판봇 승.';}});
