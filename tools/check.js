const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const f=require('path').resolve(process.argv[2]);
for(const w of [390,1280]){const p=await b.newPage({viewport:{width:w,height:900}});const errs=[];
p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});p.on('pageerror',e=>errs.push('PAGEERR '+e.message));
await p.route(/fonts\.(googleapis|gstatic)/,r=>r.abort());
await p.goto('file://'+f);await p.waitForTimeout(1500);
const sw=await p.evaluate(()=>document.documentElement.scrollWidth);
console.log('width',w,'scrollWidth',sw,'errors',errs.filter(e=>!/font|ERR_FAILED/.test(e)));
if(w===1280){
 // click through
 const r=await p.evaluate(()=>{const o={};document.querySelectorAll('#k1 .kpi,#k2 .kpi,#k3 .kpi,#k4 .kpi').forEach((k,i)=>o[i]=k.innerText.replace(/\n/g,' '));return o});console.log(JSON.stringify(r));
 await p.click('#reveal');await p.waitForTimeout(800);console.log(await p.evaluate(()=>document.querySelector('#duelBox .say.asst p').textContent+' | '+document.querySelector('#duelBox .say.verdict p').textContent));
 for(const id of (process.argv[3]||'').split(',').filter(Boolean)){await p.evaluate(s=>{document.documentElement.style.scrollBehavior='auto';const e=document.querySelector(s);window.scrollTo(0,e.getBoundingClientRect().top+window.scrollY-60)},id);await p.waitForTimeout(300);await p.screenshot({path:'/tmp/claude-0/shots/'+id.replace('#','')+'.png'});}
 const q=await p.evaluate(()=>document.querySelectorAll('.jt').length);console.log('gloss underlines',q);
}
await p.close();}
await b.close();})();
