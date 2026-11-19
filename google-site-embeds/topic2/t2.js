/* Topic 2 chart pages: loads data/series.json (refreshed daily from Reserve Bank tables) and data/manual.json,
   and draws plain SVG charts with a hover read-out. No libraries. */
(function(){
const NS='http://www.w3.org/2000/svg';
const el=(t,a={},p)=>{const e=document.createElementNS(NS,t);for(const k in a)e.setAttribute(k,a[k]);if(p)p.appendChild(e);return e;};
const h=(t,c,html)=>{const e=document.createElement(t);if(c)e.className=c;if(html!=null)e.innerHTML=html;return e;};
const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const fmt=(v,dp=1)=>v==null?'–':(v<0?'−':'')+Math.abs(v).toLocaleString('en-AU',{minimumFractionDigits:dp,maximumFractionDigits:dp});
const qLabel=k=>{const [y,m]=k.split('-').map(Number);return MON[m-1]+' qtr '+y;};
const mLabel=k=>{const [y,m]=k.split('-').map(Number);return MON[m-1]+' '+y;};
const dLabel=k=>{const [y,m,d]=k.split('-').map(Number);return d+' '+MON[m-1]+' '+y;};
const fyLabel=y=>(y-1)+'–'+String(y).slice(2);
const lastIdx=a=>{for(let i=a.length-1;i>=0;i--)if(a[i]!=null)return i;return -1;};
const last=a=>a[lastIdx(a)];
function nice(lo,hi,n=5){const span=(hi-lo)||1;const raw=span/n;const p=Math.pow(10,Math.floor(Math.log10(raw)));const m=raw/p;const step=(m<1.5?1:m<3?2:m<7?5:10)*p;const a=Math.floor(lo/step)*step,b=Math.ceil(hi/step)*step;const t=[];for(let v=a;v<=b+step/2;v+=step)t.push(+v.toFixed(10));return t;}

/* ---------- line chart ----------
   o: {x:[keys], label:fn(key), series:[{name,color,data,dash,width}], unit:'%', dp:1, ranges:[['All',0],['20 years',80]...] (points to show),
       zero:true, guides:[{y,label,color}], yMin, yMax, tickEvery:fn(key)->bool for x labels} */
function line(host,o){
  host.innerHTML='';const W=720,H=312,L=46,R=14,T=24,B=28;
  let from=0; const n=o.x.length;
  const leg=h('div','legend'); o.series.forEach(s=>leg.appendChild(h('span',null,'<i style="background:'+s.color+(s.dash?';background:repeating-linear-gradient(90deg,'+s.color+' 0 5px,transparent 5px 8px)':'')+'"></i>'+s.name)));
  const rg=h('div','ranges'); const wrap=h('div','chart'); const tip=h('div','tip');
  if(o.ranges&&o.ranges.length>1){ o.ranges.forEach((r,i)=>{const b=h('button',i===(o.rangeDefault||0)?'on':'',r[0]);b.type='button';b.onclick=()=>{[...rg.children].forEach(c=>c.className='');b.className='on';from=r[1]?Math.max(0,n-r[1]):0;draw();};rg.appendChild(b);}); const d=o.ranges[o.rangeDefault||0]; from=d[1]?Math.max(0,n-d[1]):0; host.appendChild(rg); }
  host.appendChild(leg); host.appendChild(wrap);
  function draw(){
    wrap.innerHTML='';wrap.appendChild(tip);tip.style.display='none';
    const svg=el('svg',{viewBox:'0 0 '+W+' '+H,role:'img','aria-label':o.title||'chart'});wrap.appendChild(svg);
    const idx=[];for(let i=from;i<n;i++)idx.push(i);
    let lo=Infinity,hi=-Infinity; o.series.forEach(s=>idx.forEach(i=>{const v=s.data[i];if(v!=null){lo=Math.min(lo,v);hi=Math.max(hi,v);}}));
    (o.guides||[]).forEach(g=>{lo=Math.min(lo,g.y);hi=Math.max(hi,g.y);});
    if(o.zero){lo=Math.min(lo,0);hi=Math.max(hi,0);} if(o.yMin!=null)lo=o.yMin; if(o.yMax!=null)hi=o.yMax;
    const ticks=nice(lo,hi);lo=ticks[0];hi=ticks[ticks.length-1];
    const X=k=>L+(idx.length<2?0:(k/(idx.length-1))*(W-L-R)),Y=v=>T+(1-(v-lo)/(hi-lo))*(H-T-B);
    ticks.forEach(t=>{el('line',{x1:L,x2:W-R,y1:Y(t),y2:Y(t),stroke:t===0?'#55607a':'#e3e8f2','stroke-width':t===0?1.2:1},svg);const tx=el('text',{x:L-6,y:Y(t)+4,'text-anchor':'end','font-size':11,fill:'#55607a'},svg);tx.textContent=fmt(t,(Math.abs(ticks[1]-ticks[0])<1)?(Math.abs(ticks[1]-ticks[0])<0.1?2:1):0);});
    if(o.unit){const u=el('text',{x:4,y:11,'font-size':10.5,fill:'#55607a'},svg);u.textContent=o.unit;}
    // x labels: about 7 evenly spaced
    const step=Math.max(1,Math.round(idx.length/7));for(let k=0;k<idx.length;k+=step){const t=el('text',{x:X(k),y:H-8,'text-anchor':k===0?'start':'middle','font-size':11,fill:'#55607a'},svg);t.textContent=(o.xTick||o.label)(o.x[idx[k]]);}
    (o.guides||[]).forEach(g=>{el('line',{x1:L,x2:W-R,y1:Y(g.y),y2:Y(g.y),stroke:g.color||'#b07d00','stroke-width':1.3,'stroke-dasharray':'6 4'},svg);const t=el('text',{x:W-R-4,y:Y(g.y)-4,'text-anchor':'end','font-size':11,'font-weight':700,fill:g.color||'#8a6a00'},svg);t.textContent=g.label;});
    o.series.forEach(s=>{let d='',pen=false;idx.forEach((i,k)=>{const v=s.data[i];if(v==null){pen=false;return;}d+=(pen?'L':'M')+X(k).toFixed(1)+' '+Y(v).toFixed(1);pen=true;});const pa=el('path',{d,fill:'none',stroke:s.color,'stroke-width':s.width||2.2,'stroke-linejoin':'round','stroke-linecap':'round'},svg);if(s.dash)pa.setAttribute('stroke-dasharray','6 4');});
    const cur=el('line',{y1:T,y2:H-B,stroke:'#0b1330','stroke-width':1,visibility:'hidden'},svg);
    const dots=o.series.map(s=>el('circle',{r:3.5,fill:s.color,stroke:'#fff','stroke-width':1.5,visibility:'hidden'},svg));
    const ov=el('rect',{x:L,y:T,width:W-L-R,height:H-T-B,fill:'transparent'},svg);
    const move=ev=>{const r=svg.getBoundingClientRect();const px=(ev.clientX-r.left)/r.width*W;let k=Math.round((px-L)/(W-L-R)*(idx.length-1));k=Math.max(0,Math.min(idx.length-1,k));const i=idx[k];cur.setAttribute('x1',X(k));cur.setAttribute('x2',X(k));cur.setAttribute('visibility','visible');
      let html='<b>'+o.label(o.x[i])+'</b>';o.series.forEach((s,j)=>{const v=s.data[i];if(v==null){dots[j].setAttribute('visibility','hidden');return;}dots[j].setAttribute('cx',X(k));dots[j].setAttribute('cy',Y(v));dots[j].setAttribute('visibility','visible');html+='<br>'+s.name+': '+fmt(v,s.dp!=null?s.dp:(o.dp!=null?o.dp:1))+(o.suffix||'');});
      tip.innerHTML=html;tip.style.display='block';const wr=wrap.getBoundingClientRect();let lx=(X(k)/W)*wr.width+12;if(lx+tip.offsetWidth>wr.width)lx=(X(k)/W)*wr.width-tip.offsetWidth-12;tip.style.left=Math.max(0,lx)+'px';tip.style.top='8px';};
    ov.addEventListener('pointermove',move);ov.addEventListener('pointerdown',move);ov.addEventListener('pointerleave',()=>{tip.style.display='none';cur.setAttribute('visibility','hidden');dots.forEach(d=>d.setAttribute('visibility','hidden'));});
  }
  draw();
}

/* ---------- column chart (one series, positive and negative colours) ---------- */
function cols(host,o){
  host.innerHTML='';const W=720,H=312,L=46,R=14,T=24,B=28;const wrap=h('div','chart');const tip=h('div','tip');host.appendChild(wrap);wrap.appendChild(tip);
  const svg=el('svg',{viewBox:'0 0 '+W+' '+H,role:'img','aria-label':o.title||'chart'});wrap.appendChild(svg);const n=o.x.length;
  let lo=Math.min(0,...o.data.filter(v=>v!=null)),hi=Math.max(0,...o.data.filter(v=>v!=null));(o.guides||[]).forEach(g=>{lo=Math.min(lo,g.y);hi=Math.max(hi,g.y);});(o.lines||[]).forEach(s=>s.data.forEach(v=>{if(v!=null){lo=Math.min(lo,v);hi=Math.max(hi,v);}}));
  const ticks=nice(lo,hi);lo=ticks[0];hi=ticks[ticks.length-1];const bw=(W-L-R)/n;const X=k=>L+k*bw+bw/2,Y=v=>T+(1-(v-lo)/(hi-lo))*(H-T-B);
  ticks.forEach(t=>{el('line',{x1:L,x2:W-R,y1:Y(t),y2:Y(t),stroke:t===0?'#55607a':'#e3e8f2','stroke-width':t===0?1.2:1},svg);const tx=el('text',{x:L-6,y:Y(t)+4,'text-anchor':'end','font-size':11,fill:'#55607a'},svg);tx.textContent=fmt(t,0);});
  if(o.unit){const u=el('text',{x:4,y:11,'font-size':10.5,fill:'#55607a'},svg);u.textContent=o.unit;}
  const step=Math.max(1,Math.round(n/8));for(let k=0;k<n;k+=step){const t=el('text',{x:X(k),y:H-8,'text-anchor':'middle','font-size':11,fill:'#55607a'},svg);t.textContent=o.x[k];}
  const rects=o.data.map((v,k)=>v==null?null:el('rect',{x:X(k)-bw*0.36,width:bw*0.72,y:Math.min(Y(0),Y(v)),height:Math.max(0.5,Math.abs(Y(v)-Y(0))),fill:v<0?(o.neg||'#d43c33'):(o.pos||'#0e8a8a')},svg));
  (o.lines||[]).forEach(s=>{let d='',pen=false;s.data.forEach((v,k)=>{if(v==null){pen=false;return;}d+=(pen?'L':'M')+X(k).toFixed(1)+' '+Y(v).toFixed(1);pen=true;});el('path',{d,fill:'none',stroke:s.color,'stroke-width':2.2,'stroke-linejoin':'round'},svg);});
  (o.guides||[]).forEach(g=>{el('line',{x1:L,x2:W-R,y1:Y(g.y),y2:Y(g.y),stroke:g.color||'#b07d00','stroke-width':1.3,'stroke-dasharray':'6 4'},svg);const t=el('text',{x:L+6,y:Y(g.y)+13,'font-size':11,'font-weight':700,fill:g.color||'#8a6a00'},svg);t.textContent=g.label;});
  const ov=el('rect',{x:L,y:T,width:W-L-R,height:H-T-B,fill:'transparent'},svg);
  const move=ev=>{const r=svg.getBoundingClientRect();const px=(ev.clientX-r.left)/r.width*W;let k=Math.floor((px-L)/bw);k=Math.max(0,Math.min(n-1,k));rects.forEach((q,j)=>q&&q.setAttribute('opacity',j===k?1:0.55));let html='<b>'+o.x[k]+'</b><br>'+(o.name||'Value')+': '+fmt(o.data[k],1)+(o.suffix||'');(o.lines||[]).forEach(s=>{html+='<br>'+s.name+': '+fmt(s.data[k],1)+(o.suffix||'');});tip.innerHTML=html;tip.style.display='block';const wr=wrap.getBoundingClientRect();let lx=(X(k)/W)*wr.width+12;if(lx+tip.offsetWidth>wr.width)lx=(X(k)/W)*wr.width-tip.offsetWidth-12;tip.style.left=Math.max(0,lx)+'px';tip.style.top='8px';};
  ov.addEventListener('pointermove',move);ov.addEventListener('pointerdown',move);ov.addEventListener('pointerleave',()=>{tip.style.display='none';rects.forEach(q=>q&&q.setAttribute('opacity',1));});
}

/* ---------- horizontal bars (a few labelled values) ---------- */
function bars(host,o){
  host.innerHTML='';const rowH=30,W=720,L=o.labelW||150,R=70,H=o.items.length*rowH+8;const svg=el('svg',{viewBox:'0 0 '+W+' '+H,role:'img','aria-label':o.title||'chart'});const wrap=h('div','chart');wrap.appendChild(svg);host.appendChild(wrap);
  const max=Math.max(...o.items.map(i=>i[1]));o.items.forEach((it,k)=>{const y=4+k*rowH;const t=el('text',{x:L-8,y:y+rowH/2+4,'text-anchor':'end','font-size':13,fill:'#0b1330','font-weight':700},svg);t.textContent=it[0];const w=(it[1]/max)*(W-L-R);el('rect',{x:L,y:y+5,width:w,height:rowH-10,rx:3,fill:o.color||'#0e8a8a'},svg);const v=el('text',{x:L+w+6,y:y+rowH/2+4,'font-size':13,fill:'#0b1330'},svg);v.textContent=fmt(it[1],1)+(o.suffix||'');});
}

/* ---------- data helpers ---------- */
// financial-year average of a quarterly series (year ending June); needs all four quarters
function fyAvg(q,key){const out={};q.t.forEach((k,i)=>{const [y,m]=k.split('-').map(Number);const fy=m>=9?y+1:y;const v=q.s[key][i];(out[fy]=out[fy]||[]).push(v);});const ys=Object.keys(out).map(Number).sort((a,b)=>a-b).filter(y=>out[y].length===4&&out[y].every(v=>v!=null));return {years:ys,vals:ys.map(y=>+(out[y].reduce((a,b)=>a+b,0)/4).toFixed(1))};}
// rolling four-quarter sum
function roll4(a){return a.map((v,i)=>{if(i<3)return null;const w=a.slice(i-3,i+1);return w.some(x=>x==null)?null:+(w.reduce((p,c)=>p+c,0)).toFixed(1);});}
const ratio=(a,b)=>a.map((v,i)=>(v==null||b[i]==null||b[i]===0)?null:+(v/b[i]*100).toFixed(1));
const index100=(a,base)=>{const b=a[base];return a.map(v=>(v==null||b==null)?null:+(v/b*100).toFixed(1));};
function from(block,firstKey){const i=block.t.findIndex(k=>k>=firstKey);const s={};for(const k in block.s)s[k]=block.s[k].slice(i);return {t:block.t.slice(i),s};}
let cache=null;
function load(){ if(!cache){ const base=(document.currentScript&&document.currentScript.src)||''; const u=p=>new URL(p,document.baseURI).href; cache=Promise.all([fetch(u('data/series.json'),{cache:'no-cache'}).then(r=>r.json()),fetch(u('data/manual.json'),{cache:'no-cache'}).then(r=>r.json())]).then(([S,M])=>({S,M})); } return cache; }
function stamp(S){const d=new Date(S.updated);const e=document.getElementById('upd');if(e)e.innerHTML='Charts marked <b>live</b> are redrawn from Reserve Bank statistical tables (ABS and RBA data). The data file was last refreshed on '+d.getDate()+' '+MON[d.getMonth()]+' '+d.getFullYear()+'; latest quarter '+qLabel(S.q.t[S.q.t.length-1])+', latest month '+mLabel(S.m.t[S.m.t.length-1])+', latest day '+dLabel(S.d.t[S.d.t.length-1])+'.';}
function fail(e){document.querySelectorAll('[data-chart]').forEach(c=>c.innerHTML='<p class="src">The data could not be loaded. Reload the page, or try again later.</p>');console.error(e);}
/* ---------- self-marking questions ---------- */
function check(btn){const q=btn.closest('.q');const inp=q.querySelector('input');const fb=q.querySelector('.fb');const want=parseFloat(inp.dataset.a),tol=parseFloat(inp.dataset.tol||'0.05');const got=parseFloat(String(inp.value).replace(/[, $%]/g,'').replace('−','-'));const ok=!isNaN(got)&&Math.abs(got-want)<=tol;inp.className=ok?'ok':'no';fb.className='fb '+(ok?'ok':'no');fb.innerHTML=ok?('Correct. '+(inp.dataset.why||'')):(isNaN(got)?'Type a number.':(q.dataset.tries?('Not yet. '+(inp.dataset.hint||'')+' Answer: '+inp.dataset.show+'. '+(inp.dataset.why||'')):('Not yet. '+(inp.dataset.hint||'Check your working and try again.'))));if(!ok&&!isNaN(got))q.dataset.tries=1;}
window.T2={line,cols,bars,load,fyAvg,roll4,ratio,index100,from,fmt,last,lastIdx,qLabel,mLabel,dLabel,fyLabel,stamp,fail,check,h};
})();
