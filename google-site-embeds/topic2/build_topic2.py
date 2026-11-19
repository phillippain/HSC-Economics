#!/usr/bin/env python3
"""Builds the Topic 2 'Charts and data' and 'Extension' pages (eight HTML files in this folder).

Run from this folder:  python3 build_topic2.py
The pages read data/series.json (refreshed every day by scripts/update_series.py through the
GitHub Action) and data/manual.json (checked by hand), so the charts update without a rebuild.
Rebuild only when the wording, the page numbers or the slide numbers change.
"""
import json, sys, os, html
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # always write the pages into this folder
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from icons import ICON

UPDATED = '19 November 2026'
SITE = 'https://sites.google.com/education.nsw.gov.au/hsceconomics-at-sscbwb'
GH = 'https://phillippain.github.io/HSC-Economics/'
HERE = GH + 'google-site-embeds/topic2/'
# Workbook pages and slide numbers (Topic 2 Workbook 2027 and Topic 2 Slides 2027)
SEC = {
 'trade': dict(n='2.1', name='Trade and financial flows', col='#0e8a8a', hub=SITE+'/topic-2/trade-financial-flows/vcd', hubname='Trade and finance overview', wb='pp. 4–12', sl='6–21', dp='2A', drill='2A', icon='Trade and financial flows', topic='Topic 2', topicurl=SITE+'/topic-2'),
 'bop': dict(n='2.2', name='Balance of payments', col='#0e8a8a', hub=SITE+'/topic-2/trade-financial-flows/balance-of-payments', hubname='Balance of payments', wb='pp. 13–22', sl='22–35', dp='2B', drill='2B', icon='Balance of payments', topic='Topic 2', topicurl=SITE+'/topic-2'),
 'exchange-rates': dict(n='2.3', name='Exchange rates', col='#0e8a8a', hub=SITE+'/topic-2/exchange-rates', hubname='Exchange rates', wb='pp. 23–33', sl='36–51', dp='2C', drill='2C', icon='Exchange rates', topic='Topic 2', topicurl=SITE+'/topic-2'),
 'external-stability': dict(n='2.4', name='External stability', col='#d9822b', hub=SITE+'/topic-3/external-stability', hubname='External stability', wb='pp. 34–44', sl='52–66', dp='3D', drill='3D', icon='External stability', topic='Topic 3', topicurl=SITE+'/topic-3'),
}
# Where the two child pages sit on the Google Site (filled in once the pages exist there)
CHILD = json.load(open('site_pages.json')) if os.path.exists('site_pages.json') else {}

def ic(kind): return '<span class="ic">%s</span>' % ICON[kind]
def esc(s): return html.escape(s, quote=True)

def head(key, page, title, lead):
    S = SEC[key]
    other = 'extension' if page == 'charts' else 'charts'
    other_label = 'Extension activities' if page == 'charts' else 'Charts and data'
    other_url = CHILD.get(key, {}).get(other) or (HERE + '%s-%s.html' % (other, key))
    links = [
        ('', S['hub'], 'Explainer', S['hubname'] + ' (explainer)'),
        ('', other_url, 'Extension' if other == 'extension' else 'Live chart', other_label),
        ('t', GH + 'multiple-choice-drill/#sec=' + S['drill'], 'Practice', 'HSC multiple choice'),
    ]
    if key == 'bop': links.append(('t', GH + 'bop-explorer/', 'Tool', 'BOP Explorer'))
    if key == 'exchange-rates': links.append(('t', GH + 'exchange-rate-explorer/', 'Tool', 'Exchange Rate Explorer'))
    if key in ('trade', 'external-stability'): links.append(('t', GH + 'economy-at-a-glance/', 'Tool', 'Economy at a Glance'))
    links.append(('', S['topicurl'], 'Topic page', 'All %s resources' % S['topic']))
    bar = ''.join('<a class="%s" target="_blank" rel="noopener" href="%s">%s%s</a>' % (c, u, ic(k), esc(t)) for c, u, k, t in links)
    return ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>%s</title><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&display=swap" rel="stylesheet">'
            '<link rel="stylesheet" href="t2.css"><style>:root{--acc:%s}.bar a .ic,.kind .ic{background:var(--acc)}.bar a .ic{width:22px;height:22px;border-radius:6px;display:inline-flex;align-items:center;justify-content:center}.bar a .ic svg{width:14px;height:14px}</style></head><body>'
            '<h1>%s</h1><p class="lead">%s</p>'
            '<div><span class="pill"><b>▸</b> Workbook %s · %s</span><span class="pill"><b>▸</b> Slides %s</span></div>'
            '<div class="bar">%s</div>') % (esc(title), S['col'], esc(title), lead, S['n'], S['wb'], S['sl'], bar)

def card(kind, title, what, body, src='', cid=''):
    return ('<section class="card"%s><div class="kind">%s%s</div><h2>%s</h2>%s%s%s</section>'
            % ((' id="%s"' % cid) if cid else '', ic(kind), esc(kind), title, ('<p class="what">%s</p>' % what) if what else '', body, ('<p class="src">%s</p>' % src) if src else ''))

def chart(cid): return '<div data-chart id="%s"></div><div class="notice" id="%s-n" style="display:none"></div>' % (cid, cid)
def foot(script):
    return ('<p class="upd" id="upd"></p><p class="upd">Page text updated %s. HSC Economics, Sydney Secondary College Blackwattle Bay.</p>'
            '<script src="t2.js"></script><script>%s</script></body></html>') % (UPDATED, script)
def tiles(n): return '<div class="tiles">%s</div>' % ''.join('<div class="tile" id="tile%d"><b>…</b><span></span><em></em></div>' % i for i in range(n))
RBA = 'Source: Reserve Bank of Australia statistical tables (ABS data). <b>Live</b>: redrawn when new figures are published.'
JS_COMMON = r'''
const {line,cols,bars,load,fyAvg,roll4,ratio,index100,from,fmt,last,lastIdx,qLabel,mLabel,dLabel,fyLabel,stamp,fail}=T2;
const tile=(i,big,label,sub)=>{const t=document.getElementById('tile'+i);if(!t)return;t.children[0].textContent=big;t.children[1].textContent=label;t.children[2].textContent=sub||'';};
const note=(id,htmlStr)=>{const e=document.getElementById(id+'-n');if(e){e.style.display='block';e.innerHTML='<b class="h">What to notice</b>'+htmlStr;}};
const yr=k=>k.slice(0,4); const sgn=v=>(v>0?'+':'')+fmt(v);
const ago=(a,i,n)=>a[i-n];
'''

# =====================================================================================================
# CHARTS AND DATA
# =====================================================================================================
def charts_trade():
    k='trade'
    b = head(k,'charts','Trade and financial flows: charts and data','The latest figures for the value, composition and direction of Australia\'s trade. Hover over (or tap) a chart to read the numbers.')
    b += tiles(3)
    b += card('Live chart','Exports and imports as a share of GDP','How open the economy is to trade. Each line is the value of exports or imports as a percentage of GDP in that quarter.',chart('c1'),RBA)
    b += card('Live chart','Export volumes by type','Quarterly export volumes in billions of dollars, with price changes removed, so the lines show how much is shipped, not what it earns.',chart('c2'),RBA+' Chain volume measures.')
    b += card('Live chart','Import volumes by type','Consumption goods (cars, clothing, electronics), capital goods (machinery), intermediate goods (parts and fuel) and services (mostly travel).',chart('c3'),RBA+' Chain volume measures.')
    b += card('Chart','Direction: top five export markets and import sources','Goods and services, in billions of dollars. Updated once a year when the ABS publishes the calendar-year figures.','<div class="legend"><span><i style="background:#0e8a8a"></i>Export markets</span></div><div data-chart id="c4"></div><div class="legend" style="margin-top:8px"><span><i style="background:#1c3fb0"></i>Import sources</span></div><div data-chart id="c5"></div><div class="notice" id="c4-n" style="display:none"></div>','<span id="psrc"></span>')
    b += card('Website','Composition: Australia\'s top 25 exports and imports','The Department of Foreign Affairs and Trade publishes a one-page factsheet listing the top 25 exports, top 25 imports and top 15 trading partners, with values and growth rates. Use it to complete the investigation table on workbook page 9.','<div class="bar" style="margin:4px 0 0"><a target="_blank" rel="noopener" href="https://www.dfat.gov.au/trade/trade-and-investment-data-information-and-publications/trade-statistics/trade-in-goods-and-services">'+ic('Website')+'DFAT: trade in goods and services factsheets</a><a target="_blank" rel="noopener" href="https://www.abs.gov.au/statistics/economy/international-trade/international-trade-goods/latest-release">'+ic('Website')+'ABS: international trade in goods, latest month</a></div>')
    js = JS_COMMON + r'''
load().then(({S,M})=>{ const q=S.q, n=q.t.length, i=n-1;
  tile(0,fmt(q.s.x_pct[i])+'%','Exports as a share of GDP',qLabel(q.t[i])+'; '+fmt(q.s.x_pct[i-4])+'% a year earlier');
  tile(1,fmt(q.s.m_pct[i])+'%','Imports as a share of GDP',qLabel(q.t[i])+'; '+fmt(q.s.m_pct[i-4])+'% a year earlier');
  tile(2,fmt(q.s.tb_pct[i])+'%','Trade balance, % of GDP',qLabel(q.t[i])+'; '+fmt(q.s.tb_pct[i-4])+'% a year earlier');
  line(document.getElementById('c1'),{x:q.t,label:qLabel,xTick:yr,unit:'% of GDP',suffix:'%',series:[{name:'Exports',color:'#0e8a8a',data:q.s.x_pct},{name:'Imports',color:'#1c3fb0',data:q.s.m_pct}],ranges:[['Since 1959',0],['30 years',120],['10 years',40]],zero:true});
  const i60=q.s.x_pct.findIndex(v=>v!=null); note('c1','Exports were '+fmt(q.s.x_pct[i60])+'% of GDP in '+yr(q.t[i60])+' and '+fmt(q.s.x_pct[i])+'% in the '+qLabel(q.t[i])+'. Trade has grown faster than the economy, most quickly after the dollar was floated in 1983 and tariffs were cut. When the teal line is above the blue line, the balance on goods and services is in surplus.');
  const f=q.s.x_res.findIndex((v,j)=>v!=null&&q.s.x_rural[j]!=null&&q.s.x_man[j]!=null&&q.s.x_serv[j]!=null); const qq=from(q,q.t[f]);
  line(document.getElementById('c2'),{x:qq.t,label:qLabel,xTick:yr,unit:'$ billion a quarter',series:[{name:'Resources',color:'#d9822b',data:qq.s.x_res},{name:'Services',color:'#1c3fb0',data:qq.s.x_serv},{name:'Rural',color:'#3b9a4c',data:qq.s.x_rural},{name:'Manufactures',color:'#8a3fb0',data:qq.s.x_man}],ranges:[['All',0],['20 years',80],['10 years',40]],zero:true});
  const m=qq.t.length-1, k20=Math.max(0,m-80); const g=key=>qq.s[key][k20]?((qq.s[key][m]/qq.s[key][k20]-1)*100):null;
  note('c2','Over the last 20 years resource export volumes have changed by '+sgn(g('x_res'))+'%, services '+sgn(g('x_serv'))+'%, rural '+sgn(g('x_rural'))+'% and manufactures '+sgn(g('x_man'))+'%. Look for the fall in services exports in 2020 and 2021, when borders were closed.');
  const f3=q.s.m_cons.findIndex((v,j)=>v!=null&&q.s.m_cap[j]!=null&&q.s.m_int[j]!=null&&q.s.m_serv[j]!=null); const q3=from(q,q.t[f3]);
  line(document.getElementById('c3'),{x:q3.t,label:qLabel,xTick:yr,unit:'$ billion a quarter',series:[{name:'Intermediate goods',color:'#d9822b',data:q3.s.m_int},{name:'Services',color:'#1c3fb0',data:q3.s.m_serv},{name:'Consumption goods',color:'#0e8a8a',data:q3.s.m_cons},{name:'Capital goods',color:'#8a3fb0',data:q3.s.m_cap}],ranges:[['All',0],['20 years',80],['10 years',40]],zero:true});
  note('c3','Imports rise when the economy grows quickly and when the dollar is high. Capital goods imports follow business investment, such as the mining boom.');
  const P=M.partners; bars(document.getElementById('c4'),{items:P.exports,color:'#0e8a8a',labelW:130}); bars(document.getElementById('c5'),{items:P.imports,color:'#1c3fb0',labelW:130});
  const sh=(v,t)=>fmt(v/t*100); note('c4',P.exports[0][0]+' took '+sh(P.exports[0][1],P.exports_total)+'% of exports and supplied '+sh(P.imports[0][1],P.imports_total)+'% of imports in '+P.period+'. Total exports were $'+fmt(P.exports_total)+' billion and total imports $'+fmt(P.imports_total)+' billion. Australia sells mainly to Asia but buys a large share of its imports from the United States.');
  document.getElementById('psrc').textContent='Source: '+P.source+'. Checked once a year.'; stamp(S);
}).catch(fail);'''
    return b + foot(js)

def charts_bop():
    k='bop'
    b = head(k,'charts','Balance of payments: charts and data','The current account since 1959, the trade balance and net income shown separately, and the latest quarterly figures.')
    b += tiles(3)
    b += card('Live chart','The current account, the trade balance and net income','All three as a percentage of GDP, each quarter. Net income here is the current account minus the trade balance: mostly net primary income, plus the small net secondary income.',chart('c1'),RBA)
    b += card('Live chart','The current account by financial year','The average of the four quarters in each financial year, with the balance on goods and services as a line. This is the same chart as Figure 2.9 in the workbook, kept up to date.',chart('c2'),RBA)
    b += card('Chart','The latest quarters','','<table class="t" id="tq"></table>',RBA+' Seasonally adjusted.')
    b += card('Notes','The latest ABS release in dollars','The dollar figures students need for the investigation table on workbook page 20. Checked by hand after each quarterly release.','<div id="abs"></div><div class="bar" style="margin:8px 0 0"><a target="_blank" rel="noopener" href="https://www.abs.gov.au/statistics/economy/international-trade/balance-payments-and-international-investment-position-australia/latest-release">'+ic('Website')+'ABS: balance of payments, latest release</a></div>')
    js = JS_COMMON + r'''
load().then(({S,M})=>{ const q=S.q, n=q.t.length, i=n-1; const gap=q.s.ca_pct.map((v,j)=>(v==null||q.s.tb_pct[j]==null)?null:+(v-q.s.tb_pct[j]).toFixed(1));
  tile(0,fmt(q.s.ca_pct[i])+'%','Current account, % of GDP',qLabel(q.t[i])+'; '+fmt(q.s.ca_pct[i-4])+'% a year earlier');
  tile(1,fmt(q.s.tb_pct[i])+'%','Balance on goods and services, % of GDP',qLabel(q.t[i])+'; '+fmt(q.s.tb_pct[i-4])+'% a year earlier');
  tile(2,fmt(gap[i])+'%','Net income, % of GDP',qLabel(q.t[i])+'; '+fmt(gap[i-4])+'% a year earlier');
  line(document.getElementById('c1'),{x:q.t,label:qLabel,xTick:yr,unit:'% of GDP',suffix:'%',series:[{name:'Current account',color:'#d43c33',data:q.s.ca_pct,width:2.6},{name:'Balance on goods and services',color:'#0e8a8a',data:q.s.tb_pct},{name:'Net income',color:'#1c3fb0',data:gap,dash:true}],ranges:[['Since 1959',0],['30 years',120],['10 years',40]],zero:true});
  let lo=0; q.s.ca_pct.forEach((v,j)=>{if(v!=null&&v<q.s.ca_pct[lo])lo=j;}); const pos=gap.filter(v=>v!=null&&v>0).length;
  note('c1','The largest quarterly deficit was '+fmt(q.s.ca_pct[lo])+'% of GDP in the '+qLabel(q.t[lo])+'. Net income has been '+(pos?'positive in only '+pos+' quarters':'negative in every quarter')+' since 1959: it is the structural part of the deficit. The trade balance swings with commodity prices and the exchange rate: it is the cyclical part.');
  const a=fyAvg(q,'ca_pct'), t=fyAvg(q,'tb_pct'); const k0=a.years.findIndex(y=>y>=1984); const ys=a.years.slice(k0);
  cols(document.getElementById('c2'),{x:ys.map(fyLabel),data:a.vals.slice(k0),name:'Current account',suffix:'% of GDP',unit:'% of GDP',pos:'#0e8a8a',neg:'#d43c33',lines:[{name:'Balance on goods and services',color:'#122a7a',data:ys.map(y=>t.vals[t.years.indexOf(y)])}]});
  const sur=ys.filter((y,j)=>a.vals[k0+j]>0); note('c2','Red columns are deficits and teal columns are surpluses; the navy line is the balance on goods and services. '+(sur.length?'Years with a surplus: '+sur.map(fyLabel).join(', ')+'. ':'')+'The latest full year is '+fyLabel(ys[ys.length-1])+': '+fmt(a.vals[a.vals.length-1])+'% of GDP. A yearly average of quarterly ratios can differ by 0.1 or 0.2 from the ABS annual figure.');
  let rows='<tr><th>Quarter</th><th class="n">Current account, % of GDP</th><th class="n">Balance on goods and services, % of GDP</th><th class="n">Net income, % of GDP</th></tr>'; for(let j=i;j>i-6;j--) rows+='<tr><td>'+qLabel(q.t[j])+'</td><td class="n">'+fmt(q.s.ca_pct[j])+'</td><td class="n">'+fmt(q.s.tb_pct[j])+'</td><td class="n">'+fmt(gap[j])+'</td></tr>'; document.getElementById('tq').innerHTML=rows;
  const L=M.bop_latest, Y=M.year; const tb=(title,r)=>'<table class="t"><tr><th colspan="2">'+title+'</th></tr>'+r.map(x=>'<tr><td>'+x[0]+'</td><td class="n">'+x[1]+'</td></tr>').join('')+'</table>';
  document.getElementById('abs').innerHTML=tb(L.quarter+' (released '+L.released+')',L.rows)+'<p class="src">Next release: '+L.next+'. Source: '+L.source+'.</p>'+tb('The year '+Y.period,Y.rows)+'<p class="src">Source: '+Y.source+'.</p>'; stamp(S);
}).catch(fail);'''
    return b + foot(js)

def charts_fx():
    k='exchange-rates'
    b = head(k,'charts','Exchange rates: charts and data','The dollar against the US dollar, the yen, the euro and the renminbi, the Trade Weighted Index and its weights.')
    b += tiles(4)
    b += card('Live chart','The Australian dollar against the US dollar','The bilateral rate quoted most often: how many US dollars one Australian dollar buys. Monthly since 2010.',chart('c1'),RBA)
    b += card('Live chart','Day by day: the last six months','The US dollar rate and the TWI each trading day. Use this to match a movement to a news event.',chart('c2'),RBA+' 4 pm Sydney rates.')
    b += card('Live chart','Against four currencies and the TWI','Each rate is set to 100 in January 2010, so the lines show the percentage change since then. A line above 100 means the A$ has appreciated against that currency.',chart('c3'),RBA+' Index calculated from monthly rates.')
    b += card('Chart','What is in the TWI basket?','The ten largest weights. The Reserve Bank resets the weights each year from Australia\'s trade with each partner.','<div data-chart id="c4"></div><div class="notice" id="c4-n" style="display:none"></div>','<span id="wsrc"></span>')
    b += card('Live chart','The dollar and commodity prices','The US dollar rate and the Reserve Bank\'s index of commodity prices (in US dollars), both set to 100 in January 2010. The A$ is often called a commodity currency: do the lines move together?',chart('c5'),RBA+' Index of Commodity Prices, all items, US$.')
    js = JS_COMMON + r'''
load().then(({S,M})=>{ const m=from(S.m,'2010-01'), n=m.t.length, i=n-1, d=S.d, j=d.t.length-1;
  tile(0,'US$'+d.s.usd[j].toFixed(4),'A$1 buys',dLabel(d.t[j]));
  tile(1,fmt(d.s.twi[j]),'Trade Weighted Index',dLabel(d.t[j])+' (May 1970 = 100)');
  const ch=(m.s.usd[i]/m.s.usd[i-12]-1)*100; tile(2,sgn(ch)+'%','Change against the US$ over 12 months','to '+mLabel(m.t[i]));
  const ct=(m.s.twi[i]/m.s.twi[i-12]-1)*100; tile(3,sgn(ct)+'%','Change in the TWI over 12 months','to '+mLabel(m.t[i]));
  line(document.getElementById('c1'),{x:m.t,label:mLabel,xTick:yr,unit:'US$ per A$',dp:4,series:[{name:'A$1 = US$',color:'#0e8a8a',data:m.s.usd,width:2.6}],ranges:[['Since 2010',0],['5 years',60],['2 years',24]]});
  let hi=0,lo=0; m.s.usd.forEach((v,k)=>{if(v!=null){if(v>m.s.usd[hi])hi=k;if(v<m.s.usd[lo])lo=k;}});
  note('c1','Since 2010 the monthly high was US$'+m.s.usd[hi].toFixed(2)+' ('+mLabel(m.t[hi])+', the peak of the mining boom) and the low was US$'+m.s.usd[lo].toFixed(2)+' ('+mLabel(m.t[lo])+'). The latest month is US$'+m.s.usd[i].toFixed(2)+'.');
  const base=d.s.usd[0], bt=d.s.twi[0];
  line(document.getElementById('c2'),{x:d.t,label:dLabel,xTick:k=>dLabel(k).replace(/ \d{4}$/,''),unit:'index: first day = 100',series:[{name:'US dollar rate',color:'#0e8a8a',data:d.s.usd.map(v=>v==null?null:+(v/base*100).toFixed(1))},{name:'TWI',color:'#1c3fb0',data:d.s.twi.map(v=>v==null?null:+(v/bt*100).toFixed(1))}]});
  note('c2','From '+dLabel(d.t[0])+' to '+dLabel(d.t[j])+' the dollar moved from US$'+d.s.usd[0].toFixed(4)+' to US$'+d.s.usd[j].toFixed(4)+' ('+sgn((d.s.usd[j]/base-1)*100)+'%), and the TWI from '+fmt(bt)+' to '+fmt(d.s.twi[j])+' ('+sgn((d.s.twi[j]/bt-1)*100)+'%). When the two lines move apart, the US dollar itself is changing against other currencies.');
  const ix=key=>index100(m.s[key],0);
  line(document.getElementById('c3'),{x:m.t,label:mLabel,xTick:yr,unit:'index: Jan 2010 = 100',series:[{name:'US dollar',color:'#0e8a8a',data:ix('usd')},{name:'Japanese yen',color:'#d43c33',data:ix('jpy')},{name:'Euro',color:'#1c3fb0',data:ix('eur')},{name:'Chinese renminbi',color:'#d9822b',data:ix('cny')},{name:'TWI',color:'#0b1330',data:ix('twi'),dash:true,width:2.6}],ranges:[['Since 2010',0],['5 years',60]],guides:[{y:100,label:'January 2010',color:'#55607a'}]});
  const p=key=>sgn(last(ix(key))-100)+'%'; note('c3','Since January 2010 the A$ has changed by '+p('usd')+' against the US dollar, '+p('jpy')+' against the yen, '+p('eur')+' against the euro and '+p('cny')+' against the renminbi. The TWI has changed by '+p('twi')+'. This is why one bilateral rate can mislead.');
  bars(document.getElementById('c4'),{items:M.twi.weights,color:'#0e8a8a',suffix:'%',labelW:150}); const top4=M.twi.weights.slice(0,4).reduce((a,b)=>a+b[1],0);
  note('c4','The top four currencies make up '+fmt(top4)+'% of the index. The US dollar has a weight of only '+fmt(M.twi.weights[1][1])+'%, although almost 90% of Australia\'s goods exports are priced in US dollars.'); document.getElementById('wsrc').textContent='Source: '+M.twi.source+', '+M.twi.period+'. Checked each January.';
  line(document.getElementById('c5'),{x:m.t,label:mLabel,xTick:yr,unit:'index: Jan 2010 = 100',series:[{name:'A$ against the US$',color:'#0e8a8a',data:ix('usd'),width:2.6},{name:'Commodity prices (US$)',color:'#d9822b',data:ix('com_usd')}],ranges:[['Since 2010',0],['5 years',60]]});
  const c12=(m.s.com_usd[i]/m.s.com_usd[i-12]-1)*100; note('c5','Over the 12 months to '+mLabel(m.t[i])+' commodity prices changed by '+sgn(c12)+'% and the dollar by '+sgn(ch)+'% against the US dollar. '+((c12>0)===(ch>0)?'They moved in the same direction.':'They moved in opposite directions, so another factor (such as interest rates or the US dollar itself) was stronger.')); stamp(S);
}).catch(fail);'''
    return b + foot(js)

def charts_ext():
    k='external-stability'
    b = head(k,'charts','External stability: charts and data','The measures of external stability: the current account deficit, net foreign debt and liabilities as a percentage of GDP, and the terms of trade.')
    b += tiles(4)
    b += card('Live chart','The current account deficit as a percentage of GDP','The average for each financial year. The dashed line is the International Monetary Fund\'s guide: a deficit above 4% of GDP in the medium to long term is too high.',chart('c1'),RBA)
    b += card('Live chart','Net foreign debt, net foreign equity and net foreign liabilities','Each as a percentage of GDP. Net foreign liabilities = net foreign debt + net foreign equity. A negative number for equity means Australians own more overseas than foreigners own here.',chart('c2'),RBA+' Levels at the end of each quarter, divided by nominal GDP over the previous four quarters.')
    b += card('Live chart','The terms of trade','Export prices compared with import prices, as an index. A rise means the same volume of exports buys more imports.',chart('c3'),RBA)
    b += card('Live chart','The terms of trade and the trade balance','Do they move together? The terms of trade index is on the first chart and the balance on goods and services, as a percentage of GDP, is on the second. They are drawn separately because they are measured in different units.','<div data-chart id="c4a"></div><div data-chart id="c4b" style="margin-top:6px"></div><div class="notice" id="c4-n" style="display:none"></div>',RBA)
    js = JS_COMMON + r'''
load().then(({S,M})=>{ const q=S.q, n=q.t.length, i=n-1; const g4=roll4(q.s.gdp_nom); const nfd=ratio(q.s.nfd,g4), nfe=ratio(q.s.nfe,g4), nfl=ratio(q.s.nfl,g4);
  const a=fyAvg(q,'ca_pct'), t=fyAvg(q,'tb_pct'); const ly=a.years.length-1;
  tile(0,fmt(a.vals[ly])+'%','Current account, % of GDP',fyLabel(a.years[ly])+' average; '+fmt(q.s.ca_pct[i])+'% in the '+qLabel(q.t[i]));
  const iN=lastIdx(nfd); tile(1,fmt(nfd[iN])+'%','Net foreign debt, % of GDP','end of '+qLabel(q.t[iN])+'; $'+fmt(q.s.nfd[iN],0)+' billion');
  tile(2,fmt(nfl[iN])+'%','Net foreign liabilities, % of GDP','end of '+qLabel(q.t[iN])+'; $'+fmt(q.s.nfl[iN],0)+' billion');
  const iT=lastIdx(q.s.tot); const ct=(q.s.tot[iT]/q.s.tot[iT-4]-1)*100; tile(3,sgn(ct)+'%','Terms of trade, change over the year','to the '+qLabel(q.t[iT])+' (index '+fmt(q.s.tot[iT])+')');
  const k0=a.years.findIndex(y=>y>=1960); const ys=a.years.slice(k0);
  cols(document.getElementById('c1'),{x:ys.map(fyLabel),data:a.vals.slice(k0),name:'Current account',suffix:'% of GDP',unit:'% of GDP',pos:'#0e8a8a',neg:'#d43c33',guides:[{y:-4,label:'IMF guide: −4% of GDP'}]});
  const dec=(a0,b0)=>{const v=ys.map((y,j)=>[y,a.vals[k0+j]]).filter(x=>x[0]>a0&&x[0]<=b0).map(x=>x[1]);return v.length?fmt(-v.reduce((p,c)=>p+c,0)/v.length):'–';};
  const over=ys.filter((y,j)=>a.vals[k0+j]<-4).length; note('c1','Average deficit by decade: 1980s '+dec(1980,1990)+'%, 1990s '+dec(1990,2000)+'%, 2000s '+dec(2000,2010)+'%, 2010s '+dec(2010,2020)+'% of GDP. The deficit was larger than the IMF guide in '+over+' of the '+ys.length+' years shown. The latest full year, '+fyLabel(ys[ys.length-1])+', is '+fmt(a.vals[ly])+'%.');
  const f=nfd.findIndex((v,j)=>v!=null&&nfl[j]!=null&&nfe[j]!=null); const tt=q.t.slice(f);
  line(document.getElementById('c2'),{x:tt,label:qLabel,xTick:yr,unit:'% of GDP',suffix:'%',series:[{name:'Net foreign debt',color:'#d43c33',data:nfd.slice(f)},{name:'Net foreign liabilities',color:'#0b1330',data:nfl.slice(f),width:2.6},{name:'Net foreign equity',color:'#0e8a8a',data:nfe.slice(f),dash:true}],ranges:[['All',0],['20 years',80],['10 years',40]],zero:true});
  let hi=f; nfl.forEach((v,j)=>{if(v!=null&&v>nfl[hi])hi=j;}); let e0=nfe.findIndex((v,j)=>j>f&&v!=null&&v<0&&nfe.slice(j).every(x=>x==null||x<0));
  note('c2','Net foreign liabilities peaked at '+fmt(nfl[hi])+'% of GDP at the end of the '+qLabel(q.t[hi])+' and are now '+fmt(nfl[iN])+'%. Net foreign equity has been negative since the '+(e0>0?qLabel(q.t[e0]):'mid-2010s')+', as superannuation funds bought overseas assets. Debt is serviced with interest; equity with dividends, paid only when there is a profit.');
  const f3=q.s.tot.findIndex(v=>v!=null); line(document.getElementById('c3'),{x:q.t.slice(f3),label:qLabel,xTick:yr,unit:'index',series:[{name:'Terms of trade',color:'#d9822b',data:q.s.tot.slice(f3),width:2.6}],ranges:[['Since 1959',0],['30 years',120],['10 years',40]]});
  let th=f3; q.s.tot.forEach((v,j)=>{if(v!=null&&v>q.s.tot[th])th=j;}); note('c3','The peak was '+fmt(q.s.tot[th])+' in the '+qLabel(q.t[th])+'. The latest figure, '+fmt(q.s.tot[iT])+', is '+fmt((1-q.s.tot[iT]/q.s.tot[th])*100)+'% below the peak. The long rise from 2003 was the commodity price boom driven by China.');
  const s40=Math.max(0,n-100); const tx=q.t.slice(s40);
  line(document.getElementById('c4a'),{x:tx,label:qLabel,xTick:yr,unit:'terms of trade index',series:[{name:'Terms of trade',color:'#d9822b',data:q.s.tot.slice(s40),width:2.6}]});
  line(document.getElementById('c4b'),{x:tx,label:qLabel,xTick:yr,unit:'% of GDP',suffix:'%',series:[{name:'Balance on goods and services',color:'#0e8a8a',data:q.s.tb_pct.slice(s40),width:2.6}],zero:true});
  note('c4','Compare the two shapes over the last 25 years. When commodity prices lift the terms of trade, export income rises and the trade balance usually improves a little later. The link is not exact: import volumes, the exchange rate and export volumes matter too.'); stamp(S);
}).catch(fail);'''
    return b + foot(js)

# =====================================================================================================
# EXTENSION
# =====================================================================================================
def qnum(n, text, a, show, tol=0.05, hint='', why=''):
    return ('<div class="q"><p><span class="n">%s</span>%s</p><input type="text" inputmode="decimal" aria-label="Your answer" data-a="%s" data-tol="%s" data-show="%s" data-hint="%s" data-why="%s"> '
            '<button class="btn" type="button" onclick="T2.check(this)">Check</button><p class="fb"></p></div>') % (n, text, a, tol, esc(show), esc(hint), esc(why))
def reveal(label, inner): return '<details><summary>%s</summary><div class="in">%s</div></details>' % (label, inner)
def qopen(n, text, ans): return '<div class="q"><p><span class="n">%s</span>%s</p>%s</div>' % (n, text, reveal('Show a model answer', ans))
def writing(question, marks, steps, points, sample_start, builder=True):
    b = '<p><b>%s</b> (%s marks)</p><p>Plan it with the scaffold, write it by hand in 35 minutes, then mark it against the points.</p><ol class="sc">%s</ol>' % (question, marks, ''.join('<li>%s</li>' % s for s in steps))
    b += reveal('Show the marking points', '<ul>%s</ul>' % ''.join('<li>%s</li>' % p for p in points))
    b += reveal('Show a Band 6 opening', '<p>%s</p>' % sample_start)
    if builder: b += '<div class="bar" style="margin:8px 0 0"><a class="t" target="_blank" rel="noopener" href="%sessay-builder/">%sExtended Response Builder</a></div>' % (GH, ic('Tool'))
    return b
def cases(dp):
    return ('<div id="cases" data-dp="%s"><p class="src">Loading the latest items…</p></div>'
            '<div class="bar" style="margin:8px 0 0"><a class="t" target="_blank" rel="noopener" href="%sevidence-finder/">%sOpen the Evidence Finder</a></div>') % (dp, GH, ic('Tool'))
JS_CASES = r'''
(function(){ const box=document.getElementById('cases'); if(!box) return; const dp=box.dataset.dp; const MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
 fetch(new URL('../../evidence-finder/data/evidence.json',document.baseURI).href,{cache:'no-cache'}).then(r=>r.json()).then(E=>{
  const hit=e=>((e.about&&e.about.h09)||[]).some(x=>x.indexOf(dp)===0); const L=E.filter(hit).sort((a,b)=>a.date<b.date?1:-1).slice(0,4);
  if(!L.length){box.innerHTML='<p class="src">No items yet for this section.</p>';return;}
  const esc=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  box.innerHTML=L.map(e=>{const d=e.date.split('-').map(Number);const q=(e.questions&&e.questions[0])?('<em><b>Try it:</b> '+esc(e.questions[0].q)+(e.questions[0].marks?' ('+e.questions[0].marks+' marks)':'')+'</em>'):'';
   return '<a class="case" target="_blank" rel="noopener" href="'+new URL('../../evidence-finder/#item='+encodeURIComponent(e.id),document.baseURI).href+'"><i>'+d[2]+' '+MON[d[1]-1]+' '+d[0]+' · Case study</i><b>'+esc(e.title)+'</b><span>'+esc(e.summary||e.lede||'')+'</span>'+q+'</a>';}).join('');
 }).catch(()=>{box.innerHTML='<p class="src">The Evidence Finder items could not be loaded. Use the button below.</p>';}); })();'''
def ext_head(k, lead): return head(k, 'extension', SEC[k]['name'] + ': extension', lead)
INTRO = '<p class="lead" style="margin-top:-4px">Four kinds of task: investigate live data, harder calculations that mark themselves, a Band 6 writing task, and current case studies. Do them after the matching workbook section.</p>'
def ext_foot(js): return foot(JS_COMMON + js + JS_CASES)
def span(i): return '<span id="%s">…</span>' % i

def ext_trade():
    k='trade'
    b = ext_head(k,'Go further than the workbook: how dependent is Australia on a few exports and a few markets?') + INTRO
    b += card('Live chart','Investigate: how dependent are we?','Use the live figures. Write your own answer first, then open the model answer, which is worked out from today\'s data.',
      qopen('1','How open is the Australian economy to trade, and how has that changed since 1960?','<p>'+span('a1')+'</p>')
      + qopen('2','Which type of export has grown fastest over the last 20 years, and which has grown slowest? What does this suggest about the structure of the economy?','<p>'+span('a2')+'</p>')
      + qnum('3','In calendar year 2025 Australia exported $665.2 billion of goods and services, of which $195.6 billion went to China. Calculate China\'s share of exports (%, one decimal place).','29.4','29.4%',0.06,'Divide exports to China by total exports and multiply by 100.','195.6 ÷ 665.2 × 100 = 29.4%.')
      + qnum('4','Imports from China were $130.2 billion out of total imports of $658.3 billion. Calculate China\'s share of imports (%, one decimal place).','19.8','19.8%',0.06,'130.2 ÷ 658.3 × 100.','China is a bigger share of what Australia sells than of what it buys.')
      + qopen('5','Use your answers to questions 3 and 4. Explain ONE risk and ONE benefit of the pattern you found.','<p><b>Risk:</b> almost three-tenths of export income depends on one buyer, so a slowdown in China or a trade dispute (as in 2020, when China restricted wine, barley and coal) cuts export income, the terms of trade and the dollar. <b>Benefit:</b> China\'s demand for iron ore, coal and gas lifted export income and the terms of trade for two decades, raising national income and funding the mining investment boom.</p>'),
      'Figures for questions 3 and 4: ABS, International Trade: Supplementary Information, calendar year 2025.')
    b += card('Calculate','Harder calculations','Each answer is checked when you press Check. Two tries, then the working is shown.',
      qnum('1','Exports rose 3.1% to $665.2 billion in 2025. What were exports in 2024 ($ billion, one decimal place)?','645.2','$645.2 billion',0.15,'Divide by 1.031: the 2025 figure is 103.1% of the 2024 figure.','665.2 ÷ 1.031 = 645.2. Do not subtract 3.1% of the new figure.')
      + qnum('2','Imports rose 6.9% to $658.3 billion in 2025. Using your answer to question 1, what was the balance on goods and services in 2024 ($ billion, one decimal place)?','29.4','+$29.4 billion',0.4,'Find 2024 imports (658.3 ÷ 1.069), then subtract them from 2024 exports.','658.3 ÷ 1.069 = 615.8; 645.2 − 615.8 = 29.4. The surplus shrank to $6.9 billion in 2025 because imports grew faster than exports.')
      + qnum('3','Foreign investment in Australia was $5,407.9 billion in 2026, of which direct investment was $1,419.7 billion. What percentage was direct investment (one decimal place)?','26.3','26.3%',0.06,'1,419.7 ÷ 5,407.9 × 100.','The rest (73.7%) is portfolio and other investment: mostly loans and small shareholdings.')
      + qnum('4','Iron ore exports were $118.8 billion, or 22.3% of goods exports. What were total goods exports ($ billion, to the nearest billion)?','533','$533 billion',1.0,'If 22.3% is 118.8, then 100% is 118.8 ÷ 0.223.','118.8 ÷ 0.223 = 532.7, about $533 billion.'))
    b += card('Write','Band 6 writing: commodity dependence',
      '', writing('Assess the risks and benefits for the Australian economy of its dependence on commodity exports.', '10',
        ['<b>Define and judge first.</b> Say what commodity dependence means (resources are over half of exports) and give your overall judgement in the first two sentences.','<b>Benefits (two paragraphs).</b> Higher terms of trade and national income; investment, jobs and tax revenue; a trade surplus in boom years.','<b>Risks (two paragraphs).</b> Volatile income; a high dollar in booms that squeezes other exporters; reliance on China; the energy transition.','<b>Evidence in every paragraph.</b> One statistic each, with its year.','<b>Conclude.</b> Weigh the two sides and say what would change your judgement (diversification, critical minerals).'],
        ['Resources are about 55% of exports (2026), up from about 32% in 1990; iron ore alone was $118.8 billion in 2025–26.','Benefit: the terms of trade peaked in mid-2022 at about double their 2003 level, giving a record trade surplus of 5.2% of GDP in 2021–22.','Benefit: mining investment, royalties and company tax; four current account surpluses from 2019–20 to 2022–23.','Risk: prices fall quickly. The terms of trade fell 18% in the three years after the peak and the balance on goods and services returned to deficit in 2025–26.','Risk: concentration. China takes 29.4% of exports; the 2020 trade restrictions showed the exposure.','Risk: a commodity currency. The dollar rises in booms, making manufacturing, tourism and education less competitive.','Risk: structural change as trading partners cut emissions; thermal coal declines in the long run.','Judgement supported by evidence, for example: the benefits have outweighed the risks so far, but diversification (critical minerals, services, new markets such as India) is needed to manage them.'],
        'Australia depends on commodities for more than half of its export income, and that dependence has made the country richer and more exposed at the same time. On balance the benefits have outweighed the risks over the past two decades, because high export prices lifted national income and paid for record investment; but the fall of 18% in the terms of trade after 2022 shows how quickly that income can be lost.'))
    b += card('Notes','Current case studies','The four newest items in the Evidence Finder tagged to trade and financial flows. Each opens with its statistics and an exam-style question.', cases('2A'))
    js = r'''
load().then(({S,M})=>{ const q=S.q,n=q.t.length,i=n-1; const i0=q.s.x_pct.findIndex(v=>v!=null);
  document.getElementById('a1').innerHTML='In the '+qLabel(q.t[i])+' exports were <b>'+fmt(q.s.x_pct[i])+'%</b> of GDP and imports <b>'+fmt(q.s.m_pct[i])+'%</b>, so trade (exports plus imports) was about '+fmt(q.s.x_pct[i]+q.s.m_pct[i])+'% of GDP. In '+q.t[i0].slice(0,4)+' the figures were '+fmt(q.s.x_pct[i0])+'% and '+fmt(q.s.m_pct[i0])+'%. Australia is a small open economy: trade has grown faster than output, especially since the float (1983), financial deregulation and tariff cuts, so changes in the world economy now reach Australia faster.';
  const k20=i-80; const names={x_res:'resources',x_serv:'services',x_rural:'rural goods',x_man:'manufactures'}; const g=Object.keys(names).map(key=>[names[key],(q.s[key][i]/q.s[key][k20]-1)*100]).sort((a,b)=>b[1]-a[1]);
  document.getElementById('a2').innerHTML='Over the 20 years to the '+qLabel(q.t[i])+', export volumes of <b>'+g[0][0]+'</b> grew fastest ('+sgn(g[0][1])+'%) and <b>'+g[3][0]+'</b> slowest ('+sgn(g[3][1])+'%). In between: '+g[1][0]+' '+sgn(g[1][1])+'% and '+g[2][0]+' '+sgn(g[2][1])+'%. The economy has become more specialised in what it has a comparative advantage in, and less in manufacturing, where large low-cost producers in Asia compete.'; stamp(S);
}).catch(fail);'''
    return b + ext_foot(js)

def ext_bop():
    k='bop'
    b = ext_head(k,'Go further than the workbook: why is net income always negative, and what would change it?') + INTRO
    b += card('Live chart','Investigate: the income deficit','Use the live figures on the Charts and data page. Write your own answer first; the model answers are worked out from today\'s data.',
      qopen('1','What are the latest figures for the current account, the balance on goods and services and net income, as percentages of GDP? Which part explains most of the deficit?','<p>'+span('a1')+'</p>')
      + qopen('2','In how many quarters since 1959 has net income been positive? What does this tell you about the cause of the income deficit?','<p>'+span('a2')+'</p>')
      + qopen('3','Compare the latest year with 2007–08, the year of the record deficit. What is different about the composition of the current account?','<p>'+span('a3')+'</p>')
      + qopen('4','Australian superannuation funds now hold very large investments overseas. Explain how this could change net primary income over the next decade.','<p>Income earned on overseas assets (dividends and interest) is a <b>credit</b> on net primary income. As Australian investment abroad grows ($4.8 trillion in 2026, 88% of foreign investment in Australia), those credits grow and offset more of the interest and dividends paid overseas. Net foreign equity is already negative (Australians own more equity overseas than foreigners own here). If the trend continues, the income deficit shrinks as a share of GDP. It will not disappear while net foreign debt remains about half of GDP, and it widens when world interest rates rise.</p>'))
    b += card('Calculate','Harder balance of payments calculations','An economy with a floating exchange rate has the data below ($ billion). Each answer is checked when you press Check.',
      '<table class="t"><tr><th>Item</th><th class="n">$b</th><th>Item</th><th class="n">$b</th></tr><tr><td>Goods credits</td><td class="n">510</td><td>Primary income debits</td><td class="n">195</td></tr><tr><td>Goods debits</td><td class="n">470</td><td>Net secondary income</td><td class="n">−3</td></tr><tr><td>Services credits</td><td class="n">120</td><td>Capital account balance</td><td class="n">−4</td></tr><tr><td>Services debits</td><td class="n">145</td><td>Net errors and omissions</td><td class="n">0</td></tr><tr><td>Primary income credits</td><td class="n">105</td><td>Nominal GDP</td><td class="n">2,900</td></tr></table>'
      + qnum('1','Calculate the balance on goods and services ($ billion).','15','+$15 billion',0.5,'Net goods plus net services.','(510 − 470) + (120 − 145) = 40 − 25 = 15.')
      + qnum('2','Calculate the current account balance ($ billion). Use a minus sign for a deficit.','-78','−$78 billion',0.5,'Balance on goods and services + net primary income + net secondary income.','15 + (105 − 195) + (−3) = 15 − 90 − 3 = −78.')
      + qnum('3','Calculate the financial account balance ($ billion).','82','+$82 billion',0.5,'The accounts sum to zero: current account + capital account + financial account + net errors and omissions = 0.','−78 + (−4) + financial account + 0 = 0, so the financial account is +82.')
      + qnum('4','Calculate the current account balance as a percentage of GDP (one decimal place; use a minus sign).','-2.7','−2.7%',0.06,'Current account ÷ GDP × 100.','−78 ÷ 2,900 × 100 = −2.7%.')
      + qnum('5','Next year world interest rates rise and primary income debits increase by 20%, with nothing else changing. What is the new current account balance ($ billion)?','-117','−$117 billion',0.5,'Find the new debits (195 × 1.2), then recalculate.','195 × 1.2 = 234, an extra 39 of debits: −78 − 39 = −117.')
      + qnum('6','In that case, what share of the current account deficit is explained by the net primary income deficit (%, to the nearest whole number)?','110','110%',1.0,'Net primary income is 105 − 234. Divide it by the current account balance.','−129 ÷ −117 × 100 = 110%. It is more than 100% because the trade surplus offsets part of the income deficit.'))
    b += card('Write','Band 6 writing: the savings–investment gap',
      '', writing('Explain how the gap between national saving and investment affects the size and composition of Australia\'s balance of payments.', '10',
        ['<b>Define.</b> National saving, investment and the gap between them; link it to the current account in one sentence.','<b>The financial account.</b> How the gap is filled: borrowing (debt) and foreign ownership (equity).','<b>Net primary income.</b> How past inflows become interest and dividends paid overseas every year.','<b>What changes the gap.</b> Superannuation, budget deficits, investment booms.','<b>Use the latest figures</b> and finish by linking size and composition back to the question.'],
        ['A current account deficit equals the excess of investment over national saving; overseas savings fill the gap.','The inflow is a surplus on the capital and financial account: $83.0 billion in 2025–26, matching a current account deficit of $94.9 billion (with net errors and omissions of $11.9 billion).','Composition: borrowing adds to net foreign debt ($1,486 billion, 50.8% of GDP); the servicing cost is the net primary income deficit ($85.5 billion), about nine-tenths of the current account deficit.','Size: the gap widens in investment booms (the mining boom: record deficit of 6.7% of GDP in 2007–08) and when the budget is in deficit; it narrows when saving rises (surpluses 2019–20 to 2022–23).','Superannuation (guarantee 12% from 2025) has lifted saving; super funds\' overseas assets earn income credits and made net foreign equity negative.','A clear cause-and-effect chain throughout: gap → inflow → liabilities → income outflow → larger deficit.'],
        'A country that invests more than it saves must use other countries\' savings, and the balance of payments is where that shows. Australia has done this for most of its history: a small population with large investment needs in mining, housing and infrastructure. The inflow appears as a surplus on the capital and financial account, and the cost of it appears every year afterwards as a deficit on net primary income.'))
    b += card('Notes','Current case studies','The four newest items in the Evidence Finder tagged to the balance of payments.', cases('2B'))
    js = r'''
load().then(({S,M})=>{ const q=S.q,n=q.t.length,i=n-1; const gap=q.s.ca_pct.map((v,j)=>(v==null||q.s.tb_pct[j]==null)?null:+(v-q.s.tb_pct[j]).toFixed(1));
  document.getElementById('a1').innerHTML='In the '+qLabel(q.t[i])+' the current account was <b>'+fmt(q.s.ca_pct[i])+'%</b> of GDP, the balance on goods and services <b>'+fmt(q.s.tb_pct[i])+'%</b> and net income <b>'+fmt(gap[i])+'%</b>. '+(Math.abs(gap[i])>Math.abs(q.s.tb_pct[i])?'Net income explains most of the deficit: '+fmt(gap[i]/q.s.ca_pct[i]*100,0)+'% of it.':'The trade balance explains most of it this quarter, which is unusual.')+' Net income here is the current account minus the trade balance, so it includes the small net secondary income.';
  const pos=gap.filter(v=>v!=null&&v>0).length, tot=gap.filter(v=>v!=null).length; document.getElementById('a2').innerHTML='Net income has been positive in <b>'+pos+'</b> of '+tot+' quarters. A deficit that never goes away is <b>structural</b>, not cyclical: it comes from decades of borrowing and foreign investment (the savings–investment gap), on which interest and dividends are paid every year whatever the stage of the business cycle.';
  const a=fyAvg(q,'ca_pct'),t=fyAvg(q,'tb_pct'); const y=a.years[a.years.length-1], k08=a.years.indexOf(2008); const g=(yy)=>+(a.vals[a.years.indexOf(yy)]-t.vals[t.years.indexOf(yy)]).toFixed(1);
  document.getElementById('a3').innerHTML='In 2007–08 the current account averaged '+fmt(a.vals[k08])+'% of GDP: a trade balance of '+fmt(t.vals[t.years.indexOf(2008)])+'% and net income of '+fmt(g(2008))+'%. In '+fyLabel(y)+' it averaged '+fmt(a.vals[a.vals.length-1])+'%: a trade balance of '+fmt(t.vals[t.years.indexOf(y)])+'% and net income of '+fmt(g(y))+'%. The trade balance is much stronger than in 2007–08 because mining investment turned into export volumes; the income deficit is the part that remains.'; stamp(S);
}).catch(fail);'''
    return b + ext_foot(js)

def ext_fx():
    k='exchange-rates'
    b = ext_head(k,'Go further than the workbook: commodity prices, managed rates in Asia, and the dollar as a shock absorber.') + INTRO
    b += card('Live chart','Investigate: the dollar and commodity prices','Use the last chart on the Charts and data page. Write your own answer first; the model answers are worked out from today\'s data.',
      qopen('1','Over the last 12 months, did the dollar and commodity prices move in the same direction? If not, suggest which other factor was stronger.','<p>'+span('a1')+'</p>')
      + qopen('2','The A$ has not changed by the same amount against every currency since 2010. Against which of the four major currencies has it fallen most, and against which least? Why does this matter for an exporter?','<p>'+span('a2')+'</p>')
      + qopen('3','Find the largest one-month fall in the dollar against the US dollar since 2010. What was happening?','<p>'+span('a3')+'</p>'))
    b += card('Notes','Fixed and managed rates in Asia','Australia floats, but several of its trading partners do not. Read the table, then answer.',
      '<table class="t"><tr><th>Economy</th><th>System</th><th>How it works</th></tr>'
      '<tr><td>Hong Kong</td><td>Fixed (a currency board)</td><td>The Hong Kong dollar has been linked to the US dollar since 1983 and is kept within a narrow band of HK$7.75 to HK$7.85. The monetary authority buys or sells US dollars to hold it there, so Hong Kong interest rates follow US rates.</td></tr>'
      '<tr><td>China</td><td>Managed (a daily band)</td><td>The central bank sets a reference rate each morning and the renminbi may move 2% either side of it.</td></tr>'
      '<tr><td>Singapore</td><td>Managed against a basket</td><td>The monetary authority steers the Singapore dollar against a trade-weighted basket inside a band it does not publish. It uses the exchange rate, not an interest rate, as its main tool against inflation.</td></tr>'
      '<tr><td>Japan</td><td>Floating, with occasional intervention</td><td>The yen floats, but the authorities have bought yen to slow sharp falls, as in 2022 and 2024.</td></tr></table>'
      + qopen('1','Explain why Hong Kong cannot run its own monetary policy.','<p>To hold the peg, the monetary authority must buy or sell Hong Kong dollars whenever the rate reaches the edge of the band. If Hong Kong interest rates were lower than US rates, savings would flow out, people would sell Hong Kong dollars and the peg would come under pressure. So interest rates have to follow US rates, whatever the state of Hong Kong\'s own economy. A fixed rate means giving up an independent monetary policy.</p>')
      + qopen('2','Outline ONE advantage and ONE disadvantage for an Australian exporter of a trading partner having a fixed or managed rate.','<p><b>Advantage:</b> less exchange rate risk against that currency, which makes prices and contracts easier to plan. <b>Disadvantage:</b> the partner\'s currency does not adjust to market forces, so it may be held lower than a market rate would be, making that country\'s goods more competitive against Australian producers; and all of the adjustment to a shock falls on the Australian dollar.</p>')
      + '<div class="bar" style="margin:8px 0 0"><a class="t" target="_blank" rel="noopener" href="'+GH+'exchange-rate-explorer/">'+ic('Tool')+'Try each system in the Exchange Rate Explorer</a></div>')
    b += card('Calculate','Harder calculations','Each answer is checked when you press Check.',
      qnum('1','A$1 = US$0.68 and US$1 = 155 yen. How many yen does A$1 buy (one decimal place)?','105.4','105.4 yen',0.06,'Multiply the two rates: this is a cross rate.','0.68 × 155 = 105.4 yen.')
      + qnum('2','An Australian exporter sells a tonne of wheat for US$250. The dollar moves from US$0.72 to US$0.66. By how much does the exporter\'s income per tonne rise in A$ (to the nearest dollar)?','32','A$32',0.6,'Convert US$250 at each rate (divide by the rate) and subtract.','250 ÷ 0.66 = 378.79; 250 ÷ 0.72 = 347.22; the difference is about A$32. A depreciation raises the A$ income of exporters paid in US dollars.')
      + qnum('3','A simplified TWI has three currencies with weights of 45%, 35% and 20%. The A$ changes by −6%, +2% and +4% against them. What is the change in the index (%, one decimal place; use a minus sign if it falls)?','-1.2','−1.2%',0.06,'Multiply each change by its weight and add.','0.45 × (−6) + 0.35 × 2 + 0.20 × 4 = −2.7 + 0.7 + 0.8 = −1.2%.')
      + qnum('4','The Reserve Bank estimates that a 2% fall in the TWI adds about 0.2 percentage points to inflation over two years. If the TWI falls from 65.0 to 59.8, about how much is added to inflation (percentage points, one decimal place)?','0.8','0.8 percentage points',0.06,'Find the percentage fall in the TWI first, then scale it.','(59.8 − 65.0) ÷ 65.0 = −8%. Four lots of 2%, so 4 × 0.2 = 0.8 percentage points.')
      + qnum('5','A firm owes US$40 million. The dollar falls from US$0.70 to US$0.64. By how much does the debt rise in A$ million (one decimal place)?','5.4','A$5.4 million',0.06,'Convert the debt at each rate and subtract.','40 ÷ 0.64 = 62.5; 40 ÷ 0.70 = 57.1; the difference is A$5.4 million. This is the valuation effect.'))
    b += card('Write','Band 6 writing: the dollar as a shock absorber',
      '', writing('Evaluate the view that a floating exchange rate protects the Australian economy from external shocks.', '10',
        ['<b>Define and judge.</b> A floating rate, an external shock, and your overall view in the opening.','<b>How it absorbs a negative shock.</b> Commodity prices fall → the dollar falls → other exports gain. Use a diagram of the market for A$.','<b>How it absorbs a positive shock.</b> In a boom the dollar rises, which holds down inflation.','<b>The limits.</b> Volatility, imported inflation, firms that lose in each case, and sentiment-driven swings.','<b>Conclude</b> with a judgement and one comparison with a fixed rate.'],
        ['A floating rate is set by demand and supply; Australia has floated since December 1983.','Negative shock: lower commodity prices reduce demand for A$; the depreciation makes exports cheaper and imports dearer, cushioning growth and jobs (2008–09: the dollar lost one-third of its value and Australia avoided recession).','Positive shock: during the mining boom the dollar rose to US$1.10 (2011), making imports cheaper and containing inflation while resources drew in labour and capital.','Monetary policy stays free to target inflation, unlike under a fixed rate, where interest rates must defend the currency.','Limits: a lower dollar raises import prices (a 2% fall in the TWI adds about 0.2 points to inflation); a high dollar hurt manufacturing, tourism and education; about 95% of trading is speculative, so the dollar can overshoot.','The Reserve Bank can smooth extreme moves but its reserves are small relative to daily trading.','Judgement: the float has protected output and jobs from external shocks better than a fixed rate would, at the cost of volatility and uneven effects across industries.'],
        'Since the float in December 1983 the Australian dollar has acted as the economy\'s first line of defence against changes in the rest of the world. When commodity prices fall the dollar falls with them, spreading the adjustment across exporters and import-competing firms instead of leaving it to output and jobs. The protection is real but incomplete: the same movements raise import prices, and they can be driven by sentiment as much as by trade.'))
    b += card('Notes','Current case studies','The four newest items in the Evidence Finder tagged to exchange rates.', cases('2C'))
    js = r'''
load().then(({S,M})=>{ const m=from(S.m,'2010-01'),n=m.t.length,i=n-1; const ch=(m.s.usd[i]/m.s.usd[i-12]-1)*100, cc=(m.s.com_usd[i]/m.s.com_usd[i-12]-1)*100;
  document.getElementById('a1').innerHTML='Over the 12 months to '+mLabel(m.t[i])+' commodity prices (in US$) changed by <b>'+sgn(cc)+'%</b> and the dollar by <b>'+sgn(ch)+'%</b> against the US dollar. '+((cc>0)===(ch>0)?'They moved in the same direction, as the commodity currency idea predicts: higher export prices raise demand for A$.':'They moved in opposite directions, so another factor was stronger: check the gap between Australian and US interest rates, the value of the US dollar against other currencies, and investor confidence.');
  const names={usd:'US dollar',jpy:'yen',eur:'euro',cny:'renminbi'}; const g=Object.keys(names).map(key=>[names[key],(m.s[key][i]/m.s[key][0]-1)*100]).sort((a,b)=>a[1]-b[1]);
  document.getElementById('a2').innerHTML='Since January 2010 the A$ has fallen most against the <b>'+g[0][0]+'</b> ('+sgn(g[0][1])+'%)'+(g[3][1]>0?', and it has risen against the <b>'+g[3][0]+'</b> ('+sgn(g[3][1])+'%)':', and least against the <b>'+g[3][0]+'</b> ('+sgn(g[3][1])+'%)')+'; the TWI changed by '+sgn((m.s.twi[i]/m.s.twi[0]-1)*100)+'%. An exporter\'s competitiveness depends on the currency of the market it sells to: a fall against one currency helps only exporters who sell there or are paid in it.';
  let w=1; for(let k=1;k<n;k++){ if(m.s.usd[k]/m.s.usd[k-1]<m.s.usd[w]/m.s.usd[w-1]) w=k; }
  const why={'2011-09':'the European debt crisis, when investors moved to the US dollar','2012-05':'worries about Europe and slower growth in China','2013-05':'the end of the mining investment boom and cuts to the cash rate','2013-06':'the end of the mining investment boom and talk of the US ending its stimulus','2015-01':'falling commodity prices and an expected cut in the cash rate','2015-07':'falling iron ore prices and turmoil in China\'s share market','2020-03':'the panic at the start of COVID-19, when investors moved to the US dollar','2022-09':'rapid rises in US interest rates'};
  document.getElementById('a3').innerHTML='The largest one-month fall was <b>'+sgn((m.s.usd[w]/m.s.usd[w-1]-1)*100)+'%</b> in '+mLabel(m.t[w])+' (from US$'+m.s.usd[w-1].toFixed(4)+' to US$'+m.s.usd[w].toFixed(4)+')'+(why[m.t[w]]?': '+why[m.t[w]]+'.':'. Look up what happened that month: sharp falls usually come from a loss of confidence, when investors sell riskier currencies for US dollars.'); stamp(S);
}).catch(fail);'''
    return b + ext_foot(js)

def ext_ext():
    k='external-stability'
    b = ext_head(k,'Go further than the workbook: is Australia\'s external position sustainable?') + INTRO
    b += card('Live chart','Investigate: the terms of trade and the trade balance','Use the charts on the Charts and data page. Write your own answer first; the model answers are worked out from today\'s data.',
      qopen('1','When did the terms of trade peak, and how far have they fallen since?','<p>'+span('a1')+'</p>')
      + qopen('2','What happened to the balance on goods and services between the year of the terms of trade peak and the latest year? Explain the link.','<p>'+span('a2')+'</p>')
      + qopen('3','Is net foreign debt growing faster than the economy? Use the latest figures.','<p>'+span('a3')+'</p>')
      + qopen('4','Using the IMF guide, is the current account deficit a concern right now?','<p>'+span('a4')+'</p>'))
    b += card('Calculate','Harder calculations','Each answer is checked when you press Check.',
      qnum('1','An economy pays $61 billion in interest on its foreign debt and earns $847 billion from exports. Calculate the debt servicing ratio (%, one decimal place).','7.2','7.2%',0.06,'Interest ÷ export income × 100.','61 ÷ 847 × 100 = 7.2%.')
      + qnum('2','Net foreign debt is $1,486.0 billion and net foreign liabilities are $638.9 billion. Calculate net foreign equity ($ billion, one decimal place; use a minus sign if negative).','-847.1','−$847.1 billion',0.15,'Liabilities = debt + equity, so equity = liabilities − debt.','638.9 − 1,486.0 = −847.1. Negative: Australians own more equity overseas than foreigners own here.')
      + qnum('3','The export price index rises from 120 to 126 and the import price index rises from 100 to 112. By what percentage do the terms of trade change (one decimal place; use a minus sign for a fall)?','-6.2','−6.2%',0.11,'Calculate the terms of trade index before and after, then the percentage change.','Before: 120 ÷ 100 × 100 = 120.0. After: 126 ÷ 112 × 100 = 112.5. Change: (112.5 − 120.0) ÷ 120.0 = −6.2%. Export prices rose, but import prices rose faster.')
      + qnum('4','GDP is $2,927 billion. What is the largest current account deficit, in $ billion, that stays within the IMF guide of 4% of GDP (to the nearest billion)?','117','$117 billion',1.0,'4% of GDP.','0.04 × 2,927 = 117.1. The 2025–26 deficit of $94.9 billion was inside the guide.')
      + qnum('5','Net foreign debt is $1,486 billion, of which 30% is in foreign currency and not hedged. If the dollar depreciates by 10%, by about how much does net foreign debt rise in A$ billion (to the nearest billion)?','50','about $50 billion',1.5,'Only the unhedged foreign-currency part changes. A 10% depreciation raises its A$ value by 1 ÷ 0.9 − 1, about 11.1%.','0.30 × 1,486 = 445.8; 445.8 × 0.111 = 49.5, about $50 billion. (Using a flat 10% gives $45 billion, which is close but understates it.) In practice most of Australia\'s foreign-currency debt is hedged, and overseas assets rise in value too.'))
    b += card('Exam question','Band 6 extended response with a scaffold',
      'This was Question 27 in the 2026 HSC (Section IV, 20 marks).', writing('Assess the influence of domestic and global factors on Australia\'s external stability.', '20',
        ['<b>Introduction.</b> Define external stability and name its measures. State your judgement: which group of factors matters more, and for which measure.','<b>Background.</b> The current position in three figures: the deficit, net foreign debt, net foreign liabilities.','<b>Global factor 1: the terms of trade and commodity prices.</b> Cyclical; affects the balance on goods and services and the dollar.','<b>Global factor 2: world interest rates and growth in trading partners.</b> Affects net primary income and export volumes.','<b>Domestic factor 1: the savings–investment gap.</b> Structural; drives net primary income and foreign liabilities. Include superannuation and the budget.','<b>Domestic factor 2: competitiveness and the structure of exports.</b> Narrow export base, productivity, inflation.','<b>Conclusion.</b> Weigh them: domestic factors set the long-run position; global factors explain the swings. Support it with a figure.'],
        ['Definition: the ability to meet financial obligations to the rest of the world over the medium to long term without sharp swings in the dollar; measured by the current account deficit, net foreign debt and liabilities as % of GDP, the terms of trade, the exchange rate and competitiveness.','Current position: deficit $94.9 billion, 3.2% of GDP (2025–26); net foreign debt 50.8% of GDP; net foreign liabilities 21.8% of GDP, down from over 60% in 2015–16.','Global: the terms of trade peaked in mid-2022 and fell 18% in three years; the balance on goods and services went from a record surplus (5.2% of GDP in 2021–22) to a deficit of $7.5 billion.','Global: higher world interest rates doubled net debt servicing costs to $38 billion in two years; the debt servicing ratio rose from 3.4% to 7.2%; China buys almost a third of exports; US tariffs of 12.5% from July 2026.','Domestic: investment exceeds national saving, so liabilities and the net primary income deficit ($85.5 billion) persist; super (12%) has raised saving and made net foreign equity negative; budget deficits widen the gap.','Domestic: resources about 57% of exports; competitiveness ranked 17th (IMD 2026); Future Made in Australia and microeconomic reform as responses.','The floating exchange rate links the two: it absorbs global shocks, and most debt is in A$.','A sustained judgement with current figures, for example: domestic structural factors determine the level of external liabilities, while global cyclical factors determine the year-to-year deficit; external stability is stronger than a decade ago but remains exposed to commodity prices and world interest rates.','A relevant diagram (the market for A$, or AD/AS) referred to in the text.'],
        'External stability is Australia\'s ability to meet its financial obligations to the rest of the world without sharp swings in the dollar or constraints on growth. Both domestic and global factors shape it, but in different ways: domestic factors, above all the gap between national saving and investment, set the long-run level of foreign liabilities, while global factors such as the terms of trade and world interest rates explain why the deficit moved from a surplus of 2% of GDP to a deficit of 3.2% in four years.'))
    b += card('Notes','Current case studies','The four newest items in the Evidence Finder tagged to external stability.', cases('3D'))
    js = r'''
load().then(({S,M})=>{ const q=S.q,n=q.t.length,i=n-1; const iT=lastIdx(q.s.tot); let th=q.s.tot.findIndex(v=>v!=null); q.s.tot.forEach((v,j)=>{if(v!=null&&v>q.s.tot[th])th=j;});
  document.getElementById('a1').innerHTML='The terms of trade peaked at an index of <b>'+fmt(q.s.tot[th])+'</b> in the '+qLabel(q.t[th])+'. The latest figure is '+fmt(q.s.tot[iT])+' ('+qLabel(q.t[iT])+'), which is <b>'+fmt((1-q.s.tot[iT]/q.s.tot[th])*100)+'%</b> below the peak. Over the last year they changed by '+sgn((q.s.tot[iT]/q.s.tot[iT-4]-1)*100)+'%.';
  const t=fyAvg(q,'tb_pct'), a=fyAvg(q,'ca_pct'); const [py,pm]=q.t[th].split('-').map(Number); const fy=pm>=9?py+1:py; const y=t.years[t.years.length-1]; const v0=t.vals[t.years.indexOf(fy)], v1=t.vals[t.vals.length-1];
  document.getElementById('a2').innerHTML='The balance on goods and services averaged <b>'+fmt(v0)+'%</b> of GDP in '+fyLabel(fy)+' (the year of the peak) and <b>'+fmt(v1)+'%</b> in '+fyLabel(y)+'. A fall in the terms of trade means export prices have fallen relative to import prices, so the same volume of exports earns less and the trade balance weakens. Import volumes also recovered after COVID-19, which added to the change.';
  const g4=roll4(q.s.gdp_nom), nfd=ratio(q.s.nfd,g4); const iN=lastIdx(nfd); const dg=(q.s.nfd[iN]/q.s.nfd[iN-4]-1)*100, gg=(g4[iN]/g4[iN-4]-1)*100;
  document.getElementById('a3').innerHTML='Over the year to the '+qLabel(q.t[iN])+' net foreign debt grew by <b>'+sgn(dg)+'%</b> (to $'+fmt(q.s.nfd[iN],0)+' billion) and nominal GDP by <b>'+sgn(gg)+'%</b>. '+(dg>gg+0.3?'Debt grew faster than the economy, so the ratio rose':(dg<gg-0.3?'Debt grew more slowly than the economy, so the ratio fell':'They grew at about the same rate, so the ratio was steady'))+': '+fmt(nfd[iN-4])+'% of GDP a year earlier and '+fmt(nfd[iN])+'% now. Debt that grows no faster than GDP is easier to sustain, because the income to service it is growing too.';
  const ly=a.vals[a.vals.length-1]; const l5=a.vals.slice(-5).reduce((p,c)=>p+c,0)/5;
  document.getElementById('a4').innerHTML='The deficit averaged <b>'+fmt(-ly)+'%</b> of GDP in '+fyLabel(a.years[a.years.length-1])+', and the average balance over the last five years was '+fmt(l5)+'% of GDP. The IMF guide is a concern above 4% in the medium to long term (or 6% in the short term), so on this measure '+((-l5)>4?'the deficit is above the guide.':'the deficit is inside the guide.')+' The latest quarter was '+fmt(q.s.ca_pct[i])+'%, so watch whether the yearly figure moves towards 4%.'; stamp(S);
}).catch(fail);'''
    return b + ext_foot(js)

PAGES = {'charts-trade.html':charts_trade,'charts-bop.html':charts_bop,'charts-exchange-rates.html':charts_fx,'charts-external-stability.html':charts_ext,
         'extension-trade.html':ext_trade,'extension-bop.html':ext_bop,'extension-exchange-rates.html':ext_fx,'extension-external-stability.html':ext_ext}
if __name__ == '__main__':
    for name, fn in PAGES.items():
        open(name, 'w', encoding='utf-8').write(fn()); print(name, os.path.getsize(name))
