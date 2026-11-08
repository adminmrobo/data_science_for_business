/* 5주차 · 분류모형(1) — 페이지 스크립트 */
var $=LAB.$,$$=LAB.$$,C=LAB.C,F=LAB.FONT,fitC=LAB.fitC,grid=LAB.grid,stamp=LAB.stamp,txt=LAB.txt,pct=LAB.pct,kpis=LAB.kpis,addMod=LAB.addMod;
function lg5(x,X,Y,tail){[['도미',C.info],['빙어',C.eye]].forEach(function(it,i){x.fillStyle=it[1];x.beginPath();x.arc(X+4+i*52,Y,4,0,7);x.fill();txt(x,it[0],X+12+i*52,Y,C.muted,11);});if(tail)txt(x,tail,X+108,Y,C.muted,11);}
/* Fish Market 실측값 (교안 실습 데이터) */
var BL=[25.4,26.3,26.5,29.0,29.0,29.7,29.7,30.0,30.0,30.7,31.0,31.0,31.5,32.0,32.0,32.0,33.0,33.0,33.5,33.5,34.0,34.0,34.5,35.0,35.0,35.0,35.0,36.0,36.0,37.0,38.5,38.5,39.5,41.0,41.0];
var BW=[242,290,340,363,430,450,500,390,450,500,475,500,500,340,600,600,700,700,610,650,575,685,620,680,700,725,720,714,850,1000,920,955,925,975,950];
var SL=[9.8,10.5,10.6,11.0,11.2,11.3,11.8,11.8,12.0,12.2,12.4,13.0,14.3,15.0];
var SW=[6.7,7.5,7.0,9.7,9.8,8.7,10.0,9.9,9.8,12.2,13.4,12.2,19.7,19.9];
var FL=BL.concat(SL),FW=BW.concat(SW),FT=BL.map(function(){return 1}).concat(SL.map(function(){return 0}));
function nf(v){return Number.isInteger(v)?v.toFixed(1):String(v);}

/* ---------- 히어로 소품: 노트북 산점도 + 물고기 ---------- */
LAB.heroStage($('#heroArt'),function(x,W,H,t){var mx=W*.34,my=H*.12,mw=W*.36,mh=H*.3;x.fillStyle='#0f1020';x.fillRect(mx,my,mw,mh);x.strokeStyle='#4a4f72';x.lineWidth=3;x.strokeRect(mx,my,mw,mh);x.lineWidth=1;
  FL.forEach(function(l,i){x.fillStyle=FT[i]?C.info:C.eye;x.fillRect(mx+6+l/45*(mw-12),my+mh-6-FW[i]/1100*(mh-12),3,3);});
  function fish(cx,cy,s,col){x.fillStyle=col;x.beginPath();x.ellipse(cx,cy,s,s*.45,0,0,7);x.fill();x.beginPath();x.moveTo(cx+s*.9,cy);x.lineTo(cx+s*1.4,cy-s*.4);x.lineTo(cx+s*1.4,cy+s*.4);x.fill();x.fillStyle='#11121a';x.fillRect(cx-s*.6,cy-s*.12,3,3);}
  fish(W*.82,H*.22+Math.sin(t*1.5)*3,W*.045,C.info);fish(W*.86,H*.4+Math.sin(t*1.9+1)*3,W*.02,C.eye);});

/* ---------- ① 데이터 구조 ---------- */
var DS=[['list','List'],['tuple','Tuple'],['dict','Dictionary'],['set','Set'],['array','Array'],['df','DataFrame']];
var OP=[['make','만들기'],['add','"도미" 하나 더 넣기'],['change','첫 값 바꾸기'],['mul','× 2 하기']];
var dsK='list',opK='make';
var OUT={
 list:{make:["fish = ['도미', '빙어']","print(fish)","['도미', '빙어']"],add:["fish.append('도미')","print(fish)","['도미', '빙어', '도미']   # 순서 있음 · 중복 허용"],change:["fish[0] = '농어'","print(fish)","['농어', '빙어']   # 바꿀 수 있음(mutable)"],mul:["length = [25.4, 26.3]","print(length * 2)","[25.4, 26.3, 25.4, 26.3]   # 곱셈이 아니라 반복!"]},
 tuple:{make:["fish = ('도미', '빙어')","print(fish)","('도미', '빙어')"],add:["fish = fish + ('도미',)","print(fish)","('도미', '빙어', '도미')   # 새 튜플을 만든 것"],change:["fish[0] = '농어'","","TypeError: 'tuple' object does not support item assignment"],mul:["length = (25.4, 26.3)","print(length * 2)","(25.4, 26.3, 25.4, 26.3)   # 역시 반복"]},
 dict:{make:["count = {'도미': 35, '빙어': 14}","print(count)","{'도미': 35, '빙어': 14}"],add:["count['도미'] = 36","print(count)","{'도미': 36, '빙어': 14}   # 같은 키 → 나중 값으로 덮어씀"],change:["count['빙어'] = 15","print(count['빙어'])","15   # 키로 찾아 바꿈"],mul:["count * 2","","TypeError: unsupported operand type(s) for *: 'dict' and 'int'"]},
 set:{make:["kinds = {'도미', '빙어'}","print(kinds)","{'도미', '빙어'}"],add:["kinds.add('도미')","print(kinds)","{'도미', '빙어'}   # 중복 허용 안 함, 그대로"],change:["kinds[0]","","TypeError: 'set' object is not subscriptable   # 순서·위치가 없음"],mul:["kinds * 2","","TypeError: unsupported operand type(s) for *: 'set' and 'int'"]},
 array:{make:["import numpy as np","length = np.array([25.4, 26.3])","array([25.4, 26.3])"],add:["np.append(length, 29.0)","","array([25.4, 26.3, 29. ])   # 같은 타입(숫자)끼리"],change:["length[0] = 30.0","print(length)","[30.  26.3]"],mul:["print(length * 2)","","[50.8 52.6]   # 원소마다 곱셈"]},
 df:{make:["import pandas as pd","df = pd.DataFrame({'length': [25.4, 26.3], 'weight': [242.0, 290.0]})","   length  weight\n0    25.4   242.0\n1    26.3   290.0"],add:["df.loc[2] = [29.0, 363.0]","print(df)","   length  weight\n0    25.4   242.0\n1    26.3   290.0\n2    29.0   363.0"],change:["df.loc[0, 'weight'] = 250.0","print(df.loc[0])","length     25.4\nweight    250.0"],mul:["print(df['length'] * 2)","","0    50.8\n1    52.6   # 열 단위 원소 곱셈"]}};
var TIP={list:'순서가 있고 바꿀 수 있는 가장 기본 그릇입니다. 교안 실습은 리스트로 생선 데이터를 입력합니다.',tuple:'바꿀 수 없는 그릇입니다. 실수로 바뀌면 안 되는 값에 씁니다.',dict:'키로 값을 찾습니다. 같은 키에는 값 하나만 저장됩니다(덮어쓰기).',set:'중복이 없는 그릇입니다. 종류가 몇 가지인지 셀 때 씁니다(교안 연습문제: 중복을 허용하지 않는 것은 Set).',array:'같은 타입의 숫자를 빠르게 계산합니다. 리스트 × 2(반복)와 배열 × 2(곱셈)를 비교해 보세요.',df:'행·열에 이름이 붙은 표입니다. 엑셀처럼 보이지만 코드로 다룹니다.'};
LAB.radio('#dsBtns',DS.map(function(d){return [d[0],d[1],'ds_'+d[0]]}),'list',function(v){dsK=v;show1();});
LAB.radio('#opBtns',OP.map(function(o){return [o[0],o[1],'op_'+o[0]]}),'make',function(v){opK=v;show1();});
function show1(){var o=OUT[dsK][opK],err=/Error/.test(o[2]);$('#dsOut').innerHTML='<span style="color:var(--muted)">&gt;&gt;&gt; </span>'+o[0]+(o[1]?'\n<span style="color:var(--muted)">&gt;&gt;&gt; </span>'+o[1]:'')+'\n<span style="color:'+(err?'var(--eye)':'var(--gfp)')+'">'+o[2].replace(/</g,'&lt;')+'</span>';
  $('#ins1').innerHTML='<p class="'+(err?'r':'g')+'">'+TIP[dsK]+'</p>';}
show1();

/* ---------- ② 입력·점검 ---------- */
var errK='none';
LAB.radio('#errBtns',[['none','실수 없음','er0'],['len','무게 하나 빠뜨림','er1'],['neg','음수 무게','er2'],['kg','한 마리만 kg','er3']],'none',function(v){errK=v;draw2();});
function bad(){var L=BL.slice(),W=BW.slice(),mark=-1;if(errK==='len')W.pop();if(errK==='neg'){W[7]=-390;mark=7;}if(errK==='kg'){W[15]=0.6;mark=15;}return {L:L,W:W,mark:mark};}
function stats(a){return [Math.min.apply(0,a),Math.max.apply(0,a),LAB.mean(a)];}
function draw2(){var B=bad(),c=$('#c2'),W=fitC(c,300),H=300,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-90,Hh=H-60,sx=function(v){return X0+v/45*Wd},sy=function(v){return Y0+Hh-(v+60)/1160*Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,250,500,750,1000].forEach(function(v){txt(x,v+'g',X0-4,sy(v),C.muted,10,'right');});[0,10,20,30,40].forEach(function(v){txt(x,v+'cm',sx(v),Y0+Hh+14,C.muted,10,'center');});
  if(errK==='neg'){x.strokeStyle='rgba(240,96,77,.5)';x.beginPath();x.moveTo(X0,sy(0));x.lineTo(X0+Wd,sy(0));x.stroke();}
  var n=Math.min(B.L.length,B.W.length);for(var i=0;i<n;i++){x.fillStyle=C.info;x.beginPath();x.arc(sx(B.L[i]),sy(B.W[i]),3.5,0,7);x.fill();if(i===B.mark){x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.arc(sx(B.L[i]),sy(B.W[i]),8,0,7);x.stroke();x.lineWidth=1;}}
  SL.forEach(function(l,i){x.fillStyle=C.eye;x.beginPath();x.arc(sx(l),sy(SW[i]),3.5,0,7);x.fill();});
  lg5(x,X0+8,Y0+12);stamp(x,W,'Fish Market 실측값 · 실수는 일부러 넣은 것');
  var sL=stats(B.L),sW=stats(B.W);
  $('#chkOut').textContent='>>> len(bream_length), len(bream_weight)\n('+B.L.length+', '+B.W.length+')'+(B.L.length!==B.W.length?'   ← 개수가 다릅니다!':'')+
    '\n>>> min(bream_weight), max(bream_weight), sum(bream_weight)/len(bream_weight)\n('+nf(sW[0])+', '+nf(sW[1])+', '+sW[2].toFixed(1)+')'+(sW[0]<0?'   ← 음수 무게!':'')+
    '\n>>> min(bream_length), max(bream_length)\n('+nf(sL[0])+', '+nf(sL[1])+')'+
    '\n>>> len(smelt_length), len(smelt_weight)\n('+SL.length+', '+SW.length+')';
  var M={none:'<p class="g">도미 35개·빙어 14개, 길이와 무게 개수가 맞고 범위도 상식 안입니다. 도미(오른쪽 위)와 빙어(왼쪽 아래)가 뚜렷이 갈립니다.</p>',
    len:'<p class="r">len()이 35와 34로 다릅니다. 이대로 zip()하면 마지막 도미 한 마리가 조용히 사라집니다.</p>',
    neg:'<p class="r">최솟값이 −390g입니다. 무게는 음수일 수 없으니 입력 오류입니다(노란 원).</p>',
    kg:'<p class="a">0.6이 최솟값이지만 빙어도 6.7g이라 숫자만 보면 그럴듯합니다. 산점도에서는 32cm인데 빙어 높이에 있는 점(노란 원)이 튀어나옵니다. kg으로 적은 600g입니다.</p>'};
  $('#ins2').innerHTML=M[errK];}
addMod($('#c2'),function(dt){if(!dt)draw2();});

/* ---------- ③ zip·라벨 ---------- */
var lbK='ok';
LAB.radio('#lbBtns',[['ok','올바른 순서','lb0'],['swap','빙어 먼저 입력(라벨은 그대로)','lb1']],'ok',function(v){lbK=v;show3();});
function rows3(){var L=lbK==='ok'?FL:SL.concat(BL),Wt=lbK==='ok'?FW:SW.concat(BW),truth=lbK==='ok'?FT:SL.map(function(){return 0}).concat(BL.map(function(){return 1}));
  return L.map(function(l,i){return {l:l,w:Wt[i],lab:FT[i],tru:truth[i]};});}
function show3(){var R=rows3(),wrong=R.filter(function(r){return r.lab!==r.tru}).length;
  $('#zipTable').innerHTML='<thead><tr><th>#</th><th>fish_data[i]</th><th>fish_target[i]</th><th>실제 종류</th></tr></thead><tbody>'+R.map(function(r,i){var bad=r.lab!==r.tru;return '<tr><td>'+i+'</td><td>['+nf(r.l)+', '+nf(r.w)+']</td><td class="'+(bad?'bad':'')+'">'+r.lab+'</td><td>'+(r.tru?'도미':'빙어')+'</td></tr>';}).join('')+'</tbody>';
  kpis($('#k3'),[['i',R.length+'개','fish_data 샘플'],['g',FT.filter(function(v){return v}).length+' : '+FT.filter(function(v){return !v}).length,'라벨 1 : 0'],[wrong?'r':'g',wrong+'개','틀린 라벨'],['a',pct(14/49,1),'빙어 비율(불균형 확인)']]);
  $('#ins3').innerHTML=wrong?'<p class="r">49개 중 '+wrong+'개의 이름표가 틀렸습니다. 모델은 "작은 생선 = 도미"라고 배우게 됩니다. 라벨은 데이터를 넣은 순서와 똑같이 만들어야 합니다.</p>':'<p class="g">특성과 라벨이 같은 순서로 맞았습니다. 도미 35(라벨 1), 빙어 14(라벨 0)로 빙어가 약 29%라 약간 불균형합니다.</p>';}
show3();

/* ---------- ④ KNN ---------- */
var NEW={l:30,w:600},PRE=[[30,600,'30cm·600g'],[13,15,'13cm·15g'],[25,150,'25cm·150g'],[20,250,'20cm·250g']];
function knn(q,k,feat){feat=feat||[0,1];var d=FL.map(function(l,i){var dx=feat.indexOf(0)>=0?l-q.l:0,dy=feat.indexOf(1)>=0?FW[i]-q.w:0;return [Math.sqrt(dx*dx+dy*dy),i];}).sort(function(a,b){return a[0]-b[0]}).slice(0,k);
  var v=d.reduce(function(s,t){return s+FT[t[1]]},0);return {nb:d,p1:v/k,pred:v*2>k?1:0};}
$('#kk').addEventListener('input',function(){$('#kkv').textContent=this.value;draw4();});
LAB.radio('#preBtns',PRE.map(function(p,i){return [i,p[2],'pre'+i]}),0,function(v){NEW={l:PRE[v][0],w:PRE[v][1]};draw4();});
var G4={};
$('#c4').addEventListener('click',function(e){var r=this.getBoundingClientRect(),px=e.clientX-r.left,py=e.clientY-r.top;if(!G4.sx)return;
  NEW={l:Math.max(5,Math.min(44,(px-G4.X0)/G4.Wd*45)),w:Math.max(0,Math.min(1100,(G4.Y0+G4.Hh-py)/G4.Hh*1100))};NEW.l=Math.round(NEW.l*10)/10;NEW.w=Math.round(NEW.w);$$('#preBtns .bt').forEach(function(z){z.setAttribute('aria-pressed','false')});draw4();});
function draw4(){var k=+$('#kk').value,R=knn(NEW,k),c=$('#c4'),W=fitC(c,330),H=330,x=c.getContext('2d');grid(x,W,H);var X0=56,Y0=24,Wd=W-90,Hh=H-60;
  var sx=function(v){return X0+v/45*Wd},sy=function(v){return Y0+Hh-v/1100*Hh};G4={sx:sx,X0:X0,Y0:Y0,Wd:Wd,Hh:Hh};
  x.strokeStyle=C.rule;x.strokeRect(X0,Y0,Wd,Hh);[0,250,500,750,1000].forEach(function(v){txt(x,v+'g',X0-4,sy(v),C.muted,10,'right');});[0,10,20,30,40].forEach(function(v){txt(x,v+'cm',sx(v),Y0+Hh+14,C.muted,10,'center');});
  R.nb.forEach(function(t){var i=t[1];x.strokeStyle='rgba(241,182,70,.75)';x.beginPath();x.moveTo(sx(NEW.l),sy(NEW.w));x.lineTo(sx(FL[i]),sy(FW[i]));x.stroke();});
  FL.forEach(function(l,i){x.fillStyle=FT[i]?C.info:C.eye;x.beginPath();x.arc(sx(l),sy(FW[i]),3.5,0,7);x.fill();});
  R.nb.forEach(function(t){var i=t[1];x.strokeStyle=C.amber;x.lineWidth=2;x.beginPath();x.arc(sx(FL[i]),sy(FW[i]),6,0,7);x.stroke();x.lineWidth=1;});
  var px=sx(NEW.l),py=sy(NEW.w);x.fillStyle=C.gfp;x.beginPath();for(var a=0;a<10;a++){var rr=a%2?4:10,an=-Math.PI/2+a*Math.PI/5;x.lineTo(px+rr*Math.cos(an),py+rr*Math.sin(an));}x.closePath();x.fill();
  txt(x,'새 생선 ['+NEW.l+', '+NEW.w+'] → '+(R.pred?'도미(1)':'빙어(0)'),px+12,py-12,C.gfp,12,'left',700);
  lg5(x,X0+8,Y0+12,'★ 새 생선 · 노란 선 = 가까운 '+k+'마리 · 그림을 눌러 옮기기');stamp(x,W,'Fish Market 실측값');
  var nB=R.nb.filter(function(t){return FT[t[1]]}).length;
  kpis($('#k4'),[['g',R.pred?'도미 (1)':'빙어 (0)','predict 결과'],['i','도미 '+nB+' · 빙어 '+(k-nB),'이웃 '+k+'마리의 투표'],['a','['+(1-R.p1).toFixed(1)+', '+R.p1.toFixed(1)+']','predict_proba [빙어, 도미]'],['r','1.0','score(학습 데이터 그대로)']]);
  $('#pyOut').textContent='>>> from sklearn.neighbors import KNeighborsClassifier\n>>> kn = KNeighborsClassifier(n_neighbors='+k+')\n>>> kn.fit(fish_data, fish_target)\n>>> kn.score(fish_data, fish_target)\n1.0\n>>> kn.predict([['+NEW.l+', '+NEW.w+']])\narray(['+R.pred+'])\n>>> kn.predict_proba([['+NEW.l+', '+NEW.w+']])\narray([['+(1-R.p1).toFixed(1)+', '+R.p1.toFixed(1)+']])';
  var far=R.nb[R.nb.length-1][0];
  $('#ins4').innerHTML=(NEW.l===25&&NEW.w===150)?'<p class="r">25cm·150g: 그림에서는 도미 쪽에 가까워 보이는데, 이웃 5마리 중 '+(5-nB)+'마리가 빙어입니다. 무게 눈금(g)이 길이 눈금(cm)보다 훨씬 커서, 거리가 거의 무게로만 정해지기 때문입니다. 6주차 표준화에서 다시 봅니다.</p>':
    (R.p1>0&&R.p1<1?'<p class="a">이웃이 갈렸습니다(도미 '+nB+' 대 빙어 '+(k-nB)+'). 경계 근처는 불확실합니다. 확률을 함께 보고 판단합니다.</p>':'<p class="g">이웃 '+k+'마리가 모두 '+(R.pred?'도미':'빙어')+'입니다. 가장 먼 이웃까지 거리 '+far.toFixed(1)+'.</p>');}
addMod($('#c4'),function(dt){if(!dt)draw4();});
$('#heroPred').textContent=knn({l:30,w:600},5).pred?'도미':'빙어';

/* ---------- 대결: Leave-One-Out ---------- */
function loo(feat,k){var ok=0;FL.forEach(function(l,i){var d=FL.map(function(m,j){if(j===i)return [Infinity,j];var dx=feat.indexOf(0)>=0?m-l:0,dy=feat.indexOf(1)>=0?FW[j]-FW[i]:0;return [dx*dx+dy*dy,j];}).sort(function(a,b){return a[0]-b[0]}).slice(0,k);
  var v=d.reduce(function(s,t){return s+FT[t[1]]},0)*2>k?1:0;if(v===FT[i])ok++;});return ok/FL.length;}
LAB.Duel({el:'#duelBox',higherIsBetter:true,drawMargin:.001,max:1,metric:'한 마리씩 빼놓고 맞힌 비율 (Leave-One-Out, 49번)',fmt:function(v){return pct(v,1)},
  run:function(){return {fly:loo([0,1],5),robo:loo([1],5)};},
  report:function(r){return '길이+무게는 49마리 중 '+Math.round(r.fly*49)+'마리, 무게 하나도 '+Math.round(r.robo*49)+'마리를 맞혔어요. 둘 다 '+pct(r.fly,0)+'예요.';},
  verdict:function(r,res){return '도미와 빙어는 크기가 겹치지 않아 어느 특성으로도 갈린다. '+(res==='D'?'이번 판은 나눠 갖는다.':res==='F'?'초파리 승.':'주판봇 승.');}});
