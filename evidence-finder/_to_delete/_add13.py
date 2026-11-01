import json
p='data/evidence.json'; d=json.load(open(p)); have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
def fl(i): return {'path':f'files/{i[:7]}/{i}.pdf','label':'One-page digest','pages':1}
recs=[]
def add(**k): recs.append(k)

i='2026-11-01-banks-zero-interest-savings'
add(id=i,title='Big banks hold about $332 billion that earns savers no interest as rates rise',date='2026-11-01',type='news',outlets=['ABC News','Canstar','ACCC'],
 summary='Shows how weak competition in banking can leak the savings channel of monetary policy, linking microeconomic and macroeconomic policy.',
 lede='The RBA has raised the cash rate four times this year to 4.60%, but the big four banks lifted their top savings rates by only 0.20-0.25 percentage points and only on products with strict conditions. Savers who miss the conditions earn a base rate of 0.10%, and the four banks hold about $332 billion in deposits that earn no interest.',
 about={'h09':['4D.3','4D.2','4E.3'],'y12':['Y2c.5','Y2c.8','Y2d.2'],'y11':['P2h.6']},also={'h09':['4H.1','4E.2','3E.3'],'y12':['Y2c.7','Y2d.4'],'y11':['P2h.1']},
 issues=['rates','inflation'],levers=['monetary','micro'],diagrams=['flow','chart'],
 figures=[F('Big-four deposits earning no interest','about $332b (CBA $122b, Westpac $82b, NAB $67b, ANZ $61b)','latest annual reports (CBA June; others March)','rates','ABC News'),F('Rise in big-four top savings rates after the September hike','0.20-0.25 percentage points','September 2026','rates','Canstar via ABC News'),F('Base savings rate if conditions are missed','0.10% (unchanged)','2026','rates','ABC News'),F('Customers who never meet bonus conditions','more than 70%','2023 inquiry','rates','ACCC via ABC News'),F('Consumers who switched savings accounts in three years','16%','2026','rates','ABC News'),F('Interest paid to depositors last financial year (industry claim)','more than $120b','2025-26','rates','Australian Banking Association'),F('Cash rate after four rises in 2026','4.60%','September 2026','rates','RBA')],
 terms=[T('Interest rate pass-through','How much of a change in the cash rate banks pass on to their savers and borrowers.'),T('Savings channel','The way higher interest rates reward saving and discourage spending.'),T('Competition policy','Laws and regulators (the ACCC) that promote rivalry between firms.'),T('Market power','The ability of firms to set prices or conditions without losing customers.')],
 links=[['ABC News, Big banks hold about $330 billion that earns savers no interest, 1 Nov 2026','https://www.abc.net.au/news/2026-11-01/rba-interest-hike-impact-on-high-interest-savings-accounts/107197290']],
 file=fl(i),angle='If banks pass on only small rises, much of the incentive to save is lost and their interest margins widen instead, so transmission is weaker. Stronger competition, easier switching and ACCC scrutiny could make monetary policy work better.',
 questions=[Q('Explain how weak competition in banking can reduce the effectiveness of cash rate rises in curbing spending.',4),Q('Evaluate whether stronger competition policy in banking could improve both consumer outcomes and the transmission of monetary policy.',6)],
 note='The $120 billion interest figure is the banking industry\'s claim, and the $330 billion headline is the sum of the four banks\' reported figures at different dates. UPDATE DUE: RBA decision on 3 November.')

i='2026-11-01-us-midterms-tariffs-likely-to-stay'
add(id=i,title='US midterms could shift Congress, but Trump\'s tariffs are likely to stay',date='2026-11-01',type='news',outlets=['Reuters'],
 summary='Explains why a change of Congress is unlikely to remove US tariffs, with the tariff diagram showing who gains and loses from protection.',
 lede='Democrats are favoured to win the House on 3 November and want to repeal the laws behind the Canada tariffs and the temporary 10% global tariff. Analysts say neither party will win the two-thirds majority needed to override a presidential veto, so tariffs are very likely to survive.',
 about={'h09':['1C.2','2D.4','1C.1'],'y12':['Y3a.7','Y3a.8','Y3a.11'],'y11':[]},also={'h09':['1B.4','1B.1','4H.3'],'y12':['Y3a.5','Y3a.15','Y3a.13'],'y11':[]},
 issues=['trade','global'],levers=['trade'],diagrams=['ds','flow'],
 figures=[F('US House of Representatives (Republican-Democrat)','218-214','1 November 2026','trade','Reuters via GV Wire'),F('US Senate (Republican-Democrat)','53-47','1 November 2026','trade','Reuters via GV Wire'),F('Net seats Democrats need in each chamber','4','1 November 2026','trade','Reuters via GV Wire'),F('Temporary US global tariff','10%','2026','trade','Reuters via GV Wire'),F('Trade deals the White House says it has signed','nearly 20','1 November 2026','trade','Reuters via GV Wire'),F('Partners facing a planned "excess industrial capacity" probe','16','1 November 2026','trade','Reuters via GV Wire')],
 terms=[T('Tariff','A tax on imports.'),T('Deadweight loss','The efficiency loss when a tariff or other distortion stops mutually beneficial trade.'),T('Trade diversion','Trade shifting from one source to another because of a tariff or agreement.'),T('Veto','The president\'s power to reject a bill passed by Congress.')],
 links=[['Reuters via GV Wire, Democratic wins would shift Congress trade debate but fall short of US tariff rollbacks, 1 Nov 2026','https://gvwire.com/2026/11/01/democratic-wins-would-shift-congress-trade-debate-but-fall-short-of-us-tariff-rollbacks/']],
 file=fl(i),angle='Use the tariff diagram to show consumers losing, domestic producers and government gaining, and deadweight losses. Then explain the political economy: a veto and no two-thirds majority mean tariffs persist, which matters for trade-exposed economies such as Australia.',
 questions=[Q('Using a diagram, explain the effects of a tariff on consumers, domestic producers and the government in the importing country.',6),Q('Explain why US tariffs may continue even if the Democrats win control of Congress.',3)],
 note='A forecast made before the vote. UPDATE DUE: results of the 3 November midterms. The "End Trump\'s Tariff Tax Act" has 28 co-sponsors.')

i='2026-10-31-china-factories-slip-into-contraction'
add(id=i,title='China\'s factories slip back into contraction as demand weakens',date='2026-10-31',type='stats',outlets=['National Bureau of Statistics','AFP','CGTN'],
 summary='A leading indicator for Australia\'s biggest export market: both Chinese PMIs fell below 50 in October, with new orders weaker at home and abroad.',
 lede='China\'s official manufacturing PMI fell to 49.3 in October from 50.1 in September, below forecasts of 49.9, and the non-manufacturing PMI fell to 49.7 from 50.2. The new orders index fell to 49.4, though high-tech and AI-related manufacturing kept growing.',
 about={'h09':['1A.8','2A.1'],'y12':['Y3e.1','Y3e.3','Y1a.7'],'y11':['P6a.2']},also={'h09':['1E.1','3D.3','4H.2'],'y12':['Y3a.15'],'y11':[]},
 issues=['global','growth','trade'],levers=['global'],diagrams=['chart','flow'],
 figures=[F('Official manufacturing PMI','49.3 (September 50.1; forecast 49.9)','October 2026','global','National Bureau of Statistics via AFP'),F('Non-manufacturing PMI (services and construction)','49.7 (September 50.2)','October 2026','global','National Bureau of Statistics via CGTN'),F('New orders index','49.4 (September about 50.5)','October 2026','global','National Bureau of Statistics via AFP'),F('Consumer goods PMI','-1.9 points','October 2026','global','National Bureau of Statistics via AFP')],
 terms=[T('Purchasing managers\' index (PMI)','A survey of purchasing managers about output, orders and jobs; above 50 means expansion and below 50 means contraction.'),T('Terms of trade','Export prices divided by import prices, times 100.'),T('Leading indicator','A statistic that tends to change before the wider economy does.')],
 links=[['China-Global South Project (AFP), China manufacturing PMI October 2026: factory contraction, 31 Oct 2026','https://chinaglobalsouth.com/2026/10/31/china-manufacturing-pmi-october-2026-factory-contraction/'],['CGTN, China\'s manufacturing PMI at 49.3, non-manufacturing PMI at 49.7, 31 Oct 2026','https://news.cgtn.com/news/2026-10-31/China-s-manufacturing-PMI-at-49-3-non-manufacturing-PMI-at-49-7-1RGwN3PBXpu/p.html']],
 file=fl(i),angle='Slower Chinese growth reduces demand for iron ore, coal and LNG, which can lower Australia\'s export prices and volumes, worsen the terms of trade and weaken the current account and the AUD. The 25 October and 27 October items give the earlier, stronger growth picture.',
 questions=[Q('China buys about a third of Australia\'s goods exports. Explain how a slowdown in Chinese manufacturing could affect Australia\'s terms of trade and current account balance.',5),Q('What does a fall in China\'s new orders index suggest about the likely direction of Chinese output?',2)],
 note='One month\'s survey data, so it may reverse. The "about a third" share of Australia\'s goods exports is the digest\'s statement; check it against DFAT or the ABS before quoting. Contrasts with the earlier 4.5% growth figure for the third quarter.')

i='2026-11-01-opec-holds-december-output'
add(id=i,title='OPEC+ holds December output targets steady while the Iran war keeps supply tight',date='2026-11-01',type='news',outlets=['Reuters'],
 summary='Shows why a cartel\'s quotas matter little when physical supply is already disrupted, and what an oversupply in 2027 could mean for Australia.',
 lede='Seven core OPEC+ members agreed on 1 November to leave December production targets unchanged. The decision makes little difference because war disruptions have already pushed most producers well below their quotas, and the IEA warns of possible oversupply in 2027 if Gulf flows return to normal.',
 about={'h09':['1A.1'],'y12':['Y3e.3','Y1a.7'],'y11':[]},also={'h09':['3C.3','2A.1','1A.8'],'y12':['Y1c.4','Y1c.1'],'y11':[]},
 issues=['global','inflation','trade'],levers=['global'],diagrams=['ds','flow'],
 figures=[F('Core OPEC+ members in the decision','7','1 November 2026','global','Reuters via GV Wire'),F('2023 production cut','1.65m barrels a day, fully unwound','September 2026','global','Reuters via GV Wire'),F('Other cuts still in place to end-2026','about 2m barrels a day','2026','global','Reuters via GV Wire'),F('Full OPEC+ meeting on 2027 quotas','29 November (21 members)','November 2026','global','Reuters via GV Wire')],
 terms=[T('Cartel','A group of producers that coordinates output to influence price.'),T('Production quota','A limit on the amount a member may produce.'),T('Supply-side shock','A sudden change in production costs or capacity.'),T('Oversupply','Supply exceeding demand, which pushes prices down.')],
 links=[['Reuters via GV Wire, OPEC keeps December oil output targets steady ahead of tougher call for 2027, 1 Nov 2026','https://gvwire.com/2026/11/01/opec-keeps-december-oil-output-targets-steady-ahead-of-tougher-call-for-2027/']],
 file=fl(i),angle='Quotas only matter when members can produce up to them. With Gulf exports disrupted, the price is set by the physical shock in Hormuz, not OPEC+. If the strait reopens, prices could fall sharply in 2027, easing Australian fuel inflation but lowering LNG export prices.',
 questions=[Q('Explain why an OPEC+ decision to hold output steady may have little effect on oil prices when members are already producing below quota.',3),Q('Discuss how a world oil oversupply in 2027 could affect Australia\'s inflation rate and terms of trade.',5)],
 note='UPDATE DUE: OPEC+ meeting on 29 November and the mid-November capacity review. The UAE left OPEC in May, according to the report. Related to the 30 October Hormuz oil price item.')

i='2026-10-30-oil-six-month-high-hormuz-attacks'
add(id=i,title='Oil hits a six-month high as attacks in the Strait of Hormuz escalate',date='2026-10-30',type='news',outlets=['Investing.com','ABC News'],
 summary='A live supply shock: Brent rose 13.6% in October on shipping attacks, shown with the inelastic demand diagram and the AD/AS stagflation effect on Australia.',
 lede='Brent crude settled at US$117.64 on 30 October, up 13.6% across the month, as attacks on tankers in the Strait of Hormuz reached the highest monthly level since the war with Iran began in February. Traffic through the strait is still about 70% below pre-war levels.',
 about={'h09':['3C.3','1A.1'],'y12':['Y1c.4','Y1c.5','Y3e.3'],'y11':[]},also={'h09':['3C.4','4D.3','1A.8'],'y12':['Y1c.1','Y1a.10','Y1a.13','Y2c.8'],'y11':[]},
 issues=['inflation','global','trade','rates'],levers=['monetary'],diagrams=['ds','adas','flow'],
 figures=[F('Brent crude','US$117.64 (+2.4% on the day; six-month high)','30 October 2026','global','Investing.com via Yahoo Finance'),F('Brent crude rise over October','+13.6%','October 2026','global','Investing.com via Yahoo Finance'),F('WTI crude','US$104.12','30 October 2026','global','Investing.com via Yahoo Finance'),F('Attacks on shipping','at least 35 (the most in any month of the conflict)','October 2026','global','Investing.com via Yahoo Finance'),F('Hormuz traffic compared with pre-war','about 70% lower','October 2026','global','Investing.com via Yahoo Finance'),F('Australian fuel prices','+9.4%','September 2026','inflation','ABS via digest'),F('Annual CPI','4.3%','September 2026','inflation','ABS')],
 terms=[T('Supply shock','An unexpected change in the supply of a key input that shifts costs across the economy.'),T('Price-inelastic demand','Demand that changes little when the price changes.'),T('Cost-push inflation','Inflation caused by rising production costs.'),T('Stagflation','Rising inflation combined with weak growth.')],
 links=[['Investing.com via Yahoo Finance, Oil hits six-month highs','https://au.finance.yahoo.com/news/oil-hits-six-month-highs-064011112.html'],['ABC News, Attacks on Iran should be met without restraint, Khamenei orders, 31 Oct 2026','https://www.abc.net.au/news/2026-10-31/attacks-on-iran-should-be-met-without-restraint-khamenei-orders/107332392']],
 file=fl(i),angle='Short-run oil demand is inelastic, so a small fall in quantity brings a large rise in price. For an oil importer the shock shifts SRAS left: higher prices and lower output. The RBA may not "look through" the shock in 2026 because inflation is already high.',
 questions=[Q('Using an AD/AS diagram, explain how a sustained rise in world oil prices affects inflation, output and unemployment in Australia.',6),Q('Explain why the RBA might "look through" an oil price shock, and why it may not in 2026.',4)],
 note='Iran\'s claim that four tankers hit mines, including a supertanker, was not independently verified. Overlaps with the 19 October and 28 October oil items; this one has the latest price. Qatar-mediated talks on reopening the strait were continuing.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('added',n,'total',len(d))
