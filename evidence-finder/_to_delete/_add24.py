import json, os
p='data/evidence.json'; d=json.load(open(p)); have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
recs=[]
def R(i,topic,title,date,type,outlets,summary,lede,h,y,z,hh,yy,zz,issues,levers,diagrams,figures,terms,links,angle,questions,note,pages=1,label=None):
    recs.append(dict(id=i,title=title,date=date,type=type,outlets=outlets,summary=summary,lede=lede,
      about={'h09':h,'y12':y,'y11':z},also={'h09':hh,'y12':yy,'y11':zz},issues=issues,levers=levers,diagrams=diagrams,figures=figures,terms=terms,links=links,
      file={'path':f'files/{i[:7]}/{i}.pdf','label':label or f'Topic {topic} news summary','pages':pages},
      angle=angle,questions=questions,note=note,added='2026-11-19'))


ABC='ABC News'
def L(a,b): return [a,b]

R('2026-11-19-unemployment-rises-4-9-highest-since-2021','3','Unemployment rises to 4.9%, the highest since 2021','2026-11-19','stats',['ABS'],
 "Gives the October Labour Force result: rising unemployment, falling employment and participation, and a weak youth market.",
 "The ABS October Labour Force survey shows the seasonally adjusted unemployment rate rose to 4.9%, its highest since October 2021, as employment fell by 43,500 and the effects of five interest rate rises flow through to the jobs market.",
 ['3B.1','3B.2','3B.3','3B.6'],['Y1b.1','Y1b.3','Y1b.7','Y1b.11','Y1b.12'],['P1e.7','P3d.3'],
 ['3A.7','4D.3'],['Y1b.5','Y1b.10'],['P3b.1'],
 ['employment'],['monetary'],['ds','chart'],
 [F('Unemployment rate, seasonally adjusted','4.9% (September 4.7%; trend 4.8%), highest since October 2021','October 2026','employment','ABS Labour Force'),
  F('Change in employment','-43,500 to 14.74 million (part-time -40,600; full-time -2,900)','October 2026','employment','ABS Labour Force'),
  F('Number unemployed','753,700 (+17,800 in the month; +14.5% on a year ago)','October 2026','employment','ABS Labour Force'),
  F('Participation rate / employment-to-population ratio','66.6% (from 66.8%) / 63.3%','October 2026','employment','ABS Labour Force'),
  F('Youth unemployment (15-24)','11.3% (September 11.1%; post-COVID average 9.2%)','October 2026','employment','ABS Labour Force'),
  F('Hours worked / underemployment','-0.2% / 6.2% (eased slightly)','October 2026','employment','ABS Labour Force')],
 [T('Unemployment rate','The unemployed as a share of the labour force (employed plus unemployed).'),T('Participation rate','The share of the working-age population in the labour force.')],
 [L('ABS: Unemployment rate rises to 4.9%','https://www.abs.gov.au/'),L('ABS: Labour Force, Australia, October 2026','https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/')],
 "Labour is a derived demand: weaker spending lowers demand for labour, so more of the adjustment shows up as job losses and fewer hours than as lower wages. Look at participation as well as unemployment: it fell, so some people stopped looking and the unemployment rate would otherwise have risen further. Part-time jobs usually go first in a slowdown.",
 [Q("Using the October data, explain why the unemployment rate and the participation rate are both important for understanding labour market conditions.",4)],
 "Resolves the 18 November job-ads card's UPDATE DUE for the October Labour Force result. Next release 17 December 2026. Related: 15 November youth unemployment card and the 19 November recession-warnings analysis. The ABS links are to the ABS site; the digest names the releases only.")

R('2026-11-19-recession-warnings-quacking-like-a-recession','3','"Quacking like a recession": economists warn the downturn is deepening','2026-11-19','news',['ABC News (Jessica Irvine, analysis)'],
 "Gives economists' recession warnings after the jump in unemployment, with the rule of thumb and the demand-led downturn mechanism.",
 "After the jump in unemployment, leading economists warn Australia is showing the hallmarks of a recession. HSBC's Paul Bloxham says recession is 'clearly a concern' and Betashares' David Bassanese says the economy may already have 'one foot in recession'.",
 ['3A.7','3B.2','3B.3'],['Y1a.5','Y1a.12','Y1b.11'],['P1e.4','P1e.5','P1e.7'],
 ['3A.4','4H.1'],['Y1a.8','Y2c.8'],['P1e.6'],
 ['growth','employment'],['monetary'],['adas','flow'],
 [F('Rise in unemployment since Christmas 2025','0.8 percentage points (from 4.1%); rule of thumb: about 1 point signals recession','November 2026','employment','ABC News'),
  F('People available and looking for work who could not find it','More than 750,000 (first time since COVID)','October 2026','employment','ABC News'),
  F('RBA forecast unemployment','5.1% by next Christmas (as reported)','November 2026','employment','ABC News'),
  F('Westpac growth forecasts','1.4% in 2026; 1% in 2027','November 2026','growth','Westpac, via SMH')],
 [T('Technical recession','Two consecutive quarters of falling real GDP.'),T('Multiplier effect','An initial fall in spending leads to further falls as incomes drop.')],
 [L('ABC News: Australia\'s jobs market is quacking like a recession (Jessica Irvine), 19 Nov 2026','https://www.abc.net.au/news/'),L('SMH: Shrinking pay packets: real wages drop for fourth consecutive quarter, 18 Nov 2026 (Westpac forecast)','https://www.smh.com.au/')],
 "Rate rises, cost-of-living pressure and falling house prices cut consumption and investment, shifting AD left and lowering output; two quarters of falling GDP is a technical recession. Unemployment is usually a lagging indicator, but a sharp rise can signal a downturn is under way. Other risks: a falling AUD, elevated oil prices and global disruption.",
 [Q("Outline the definition of a technical recession and explain two indicators that suggest the Australian economy may be approaching one.",5)],
 "ANALYSIS and opinion: the quotes are two economists' views, not a call that a recession has begun. UPDATE DUE: September-quarter GDP on 2 December. CAUTION: the RBA 5.1% unemployment forecast is described here as 'by next Christmas', whereas the 17 November minutes card has it at end-2028; check the source before quoting. ABC and SMH links are site pages because the digest gives titles only.")

R('2026-11-19-rba-hike-bets-vanish-unemployment-outlook','4','Rate hike bets vanish as rising unemployment changes the RBA outlook','2026-11-19','news',[ABC,'RBA','CommBank'],
 "Shows the RBA's inflation-versus-unemployment dilemma and how markets repriced after the jump in unemployment.",
 "After the jump in unemployment, markets have dropped bets on another RBA rate rise at the 8 December meeting and now expect at least one cut, possibly two, by Christmas 2027. The RBA faces a classic dilemma: inflation is above target but the labour market is weakening quickly.",
 ['4D.1','4D.2','4D.3','4H.1'],['Y2c.2','Y2c.4','Y2c.7','Y2c.8'],['P4c.3'],
 ['4A.7','3B.4','3C.2'],['Y1c.6','Y2a.2'],['P4c.4'],
 ['rates','inflation','employment'],['monetary'],['phillips','chart'],
 [F('RBA cash rate','4.85% after five hikes this year (from 3.6%); November decision split 6-3','November 2026','rates','RBA; ABC News'),
  F('Market pricing for the 8 December meeting','No hike priced; at least one cut, possibly two, expected by Christmas 2027','19 November 2026','rates','ABC News'),
  F('Unemployment the RBA says may be needed to curb inflation','About 4.5-5% (now 4.9%)','November 2026','employment','RBA, via ABC News'),
  F('RBA staff inflation forecast','Above 3% until late 2027','November 2026','inflation','RBA')],
 [T('Dual mandate','The RBA\'s goals of price stability (2-3% inflation) and full employment.'),T('Market pricing','Expected future interest rates implied by financial market trading.')],
 [L('ABC News: Australia\'s jobs market is quacking like a recession (Jessica Irvine)','https://www.abc.net.au/news/'),L('ABC News: Federal politics live, 19 Nov 2026','https://www.abc.net.au/news/'),L('CommBank: RBA pause increasingly likely after November\'s vote','https://www.commbank.com.au/'),L('FINA: RBA minutes show board split six-three','https://www.fixedincomenews.com.au/')],
 "Rate rises have slowed demand, moving the economy along the short-run Phillips curve: inflation eases but unemployment rises. With unemployment at 4.9%, near the level the RBA said was needed, further hikes are less likely. Easing too early risks persistent inflation; holding too long risks recession; the full effect of 2026's hikes (a time lag) is still flowing through. Governor Bullock says the RBA does not intend to cause a recession.",
 [Q("With inflation above target but unemployment rising, discuss the policy dilemma facing the Reserve Bank of Australia.",6)],
 "Replaces the 17 November card 'CommBank expects the RBA to hold rates in December' (CBA's Belinda Allen: the 7-8 December meeting unlikely to be 'live'; February the next meeting where a rise could be seriously considered; cuts expected August and November 2027; new housing lending -15.5% and investor lending -32.3% in the September quarter). Market pricing and bank forecasts are not RBA decisions: UPDATE DUE after the 8 December meeting. Next data: October monthly CPI (24 Nov) and September-quarter GDP (2 Dec).")

R('2026-11-19-migrant-workers-underpaid-study','3','Two-thirds of surveyed migrant workers are underpaid, study finds','2026-11-19','report',['ABC News (federal politics live)','Migrant Justice Institute'],
 "Gives evidence on underpayment of a vulnerable group of workers and the bargaining power and enforcement issues behind it.",
 "A Migrant Justice Institute study of almost 10,000 migrants surveyed in 2024 found about two-thirds were underpaid. Very few tried to recover their wages, and many feared that complaining would put their visa at risk.",
 ['3E.5','3E.6','4F.2'],['Y1d.8','Y1d.5','Y2e.4'],['P3d.1','P2h.8'],
 ['4F.3','1A.7'],['Y2e.3','Y2e.8'],['P3d.3'],
 ['inequality','employment'],['labour'],['flow','compare'],
 [F('Surveyed migrants underpaid','About two-thirds (almost 10,000 surveyed in 2024)','2024','inequality','Migrant Justice Institute, via ABC News'),
  F('Underpaid workers who tried to recover wages','One in seven (about 14%)','2024','inequality','Migrant Justice Institute, via ABC News'),
  F('Feared that action would put their visa or residency pathway at risk','28%','2024','inequality','Migrant Justice Institute, via ABC News')],
 [T('Wage theft','Paying workers less than their legal entitlements under awards or the minimum wage.'),T('Bargaining power','A worker\'s ability to negotiate pay and conditions; weaker when a visa depends on the employer.')],
 [L('ABC News: Federal politics live, 19 Nov 2026','https://www.abc.net.au/news/')],
 "Visas that depend on the employer weaken bargaining power and discourage complaints, so underpayment goes unreported and law-abiding firms are undercut. Policy options: stronger Fair Work Ombudsman enforcement, visa protections for reporting and low-cost ways to recover wages; limits: enforcement is costly, small businesses are hard to monitor and policies cutting migration can increase insecurity.",
 [Q("Explain how underpayment of migrant workers affects the distribution of income, and outline one policy that could address it.",4)],
 "Survey data are from 2024, reported 19 November 2026; the survey sample is not necessarily representative of all migrant workers. The ABC link is the news home page because the digest cites a live blog only. Related: 18 November backpacker visa backtrack card.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-17-cba-expects-rba-december-hold'}
d=[x for x in d if x['id'] not in REMOVE]
for x in d:
    if x['id']=='2026-11-18-labour-market-cooling-job-ads-layoffs':
        x['note']=x['note'].replace("UPDATE DUE: October Labour Force data released Thursday 19 November.","The October Labour Force result is now filed (19 November card: unemployment 4.9%, employment -43,500).")
    if x['id']=='2026-11-17-rba-minutes-board-split-6-3':
        x['note']=x['note'].replace("Still UPDATE DUE: Labour Force (Thu 19 Nov), October CPI","Labour Force now filed (19 November card: unemployment 4.9%). Still UPDATE DUE: October CPI")
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
