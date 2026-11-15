import json
p='data/evidence.json'; d=json.load(open(p)); have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
recs=[]
def R(i,topic,title,date,type,outlets,summary,lede,h,y,z,hh,yy,zz,issues,levers,diagrams,figures,terms,links,angle,questions,note):
    recs.append(dict(id=i,title=title,date=date,type=type,outlets=outlets,summary=summary,lede=lede,
      about={'h09':h,'y12':y,'y11':z},also={'h09':hh,'y12':yy,'y11':zz},issues=issues,levers=levers,diagrams=diagrams,figures=figures,terms=terms,links=links,
      file={'path':f'files/{i[:7]}/{i}.pdf','label':f'Topic {topic} news summary','pages':1},
      angle=angle,questions=questions,note=note,added='2026-11-16'))

R('2026-11-14-political-limits-on-economic-policy',4,'Rate rises and tax backlash put the government\'s economic management under pressure','2026-11-14','news',['ABC News (analysis)'],
 'A current example of political constraints on policy: five rate rises and unpopular housing tax changes, and the inflation-unemployment trade-off voters feel.',
 'An ABC analysis by Jacob Greber argues the Albanese government is struggling after five RBA rate rises this year and broken election promises on housing tax concessions. It is a reminder that economic policy runs into political limits.',
 ['4H.3','4I.1'],['Y2b.14','Y2c.8','Y2g.1'],[],['4C.1','3B.4'],['Y2d.6','Y2f.8'],['P5a.1'],
 ['rates','inflation','housing','budget'],['monetary','fiscal'],['phillips','flow'],
 [F('RBA rate rises in 2026','5 since February, to 4.85% (18-year high)','3 November 2026','rates','ABC News'),F('Budget changes in May','negative gearing and capital gains tax concessions wound back, despite earlier promises not to','May 2026','budget','ABC News (Jacob Greber)'),F('Next dates','MYEFO in December; trusts legislation due in the Senate the week of 16 November; next federal election due 2028','2026-2028','budget','ABC News (Jacob Greber)')],
 [T('Policy trade-off','Achieving one goal, such as lower inflation, at the cost of another, such as jobs.'),T('Political constraint','When a policy is economically sound but unpopular, making it harder to implement.')],
 [['ABC News, The government is floundering and Albanese\'s salad days have wilted into woe (analysis), 14 Nov 2026','https://abc.net.au/news/2026-11-14/government-floundering-albanese-salad-days-wilted/107382680'],['ABC News, RBA hikes cash rate to 18-year high of 4.85 per cent, 3 Nov 2026','https://abc.net.au/news/2026-11-03/rba-interest-rates-markets-live-coverage/107338216']],
 'To bring inflation back toward the 2-3% target the RBA tightens policy and the economy moves along the Phillips curve: inflation falls but unemployment rises. Higher mortgage repayments and job losses are felt by voters, which creates political pressure on governments even though the RBA is independent. Reforms with long-run benefits, such as the housing tax changes, often have short-run costs that make them hard to sustain.',
 [Q('Discuss the political constraints that limit the effectiveness of economic policy in Australia.',6)],
 'An opinion piece: it reflects the writer\'s political judgement, not official data, and the description of polling as bleak is the author\'s. Use it to illustrate political limits on policy, not as a statistic. See the 4 November inflation politics item and the 11 November Albanese at COP31 item.')

R('2026-11-14-regional-airfares-competition',4,'Regional flights cost far more than city routes, Productivity Commission finds','2026-11-14','news',['ABC News','Productivity Commission'],
 'Market concentration and thin routes explain high regional fares, and show the limits of competition policy.',
 'A Productivity Commission interim report found regional and remote Australians pay much higher airfares than people flying between major cities: long regional flights cost 67% more on average, and short regional flights cost 173% more per kilometre. Several airlines have cut Northern Territory services, so Darwin\'s flights to Sydney, Adelaide and Canberra are served only by Qantas and Jetstar.',
 ['4E.3','4E.2'],['Y2d.2','Y2d.5','Y2d.6'],['P2g.1','P2g.2','P2h.6'],['4E.1'],['Y2d.1'],['P5a.5'],
 ['productivity','inequality'],['micro'],['ds','flow'],
 [F('Long regional and remote flights compared with major-city routes','67% dearer on average','2026','productivity','Productivity Commission interim report via ABC News'),F('Short regional flights, per kilometre','173% dearer','2026','productivity','Productivity Commission interim report via ABC News'),F('Return fare, Gove to Brisbane','about $5,200','2026','productivity','ABC News'),F('Airlines left on several Darwin routes','2 (Qantas and Jetstar)','2026','productivity','ABC News')],
 [T('Market concentration','When a few firms supply most of a market, reducing competition.'),T('Microeconomic reform','Policies that improve efficiency and competition in particular industries.')],
 [['ABC News, Touring Australia no longer tenable for internationally-renowned local bands as regional airfares soar, 14 Nov 2026','https://abc.net.au/news/2026-11-14/remote-flight-prices-nt-bands-yothu-yindi-king-stingray-touring/107381634'],['Productivity Commission, Determinants of regional airfares (interim report)','https://pc.gov.au/inquiries-and-research/regional-airfares/interim']],
 'If reforms encourage new airlines to enter regional routes, or lower costs such as airport charges, supply shifts right: fares fall and more people fly, which improves allocative efficiency. But thin regional routes may be natural monopolies where only one or two airlines can operate profitably, which limits what competition policy can achieve.',
 [Q('Using the example of regional airfares, explain how a lack of competition affects prices and economic efficiency.',4)],
 'An interim report, so the findings may change. Qantas says aviation costs such as labour, airport charges and air traffic control fees are rising faster than inflation, which is its view, not a finding. The Yothu Yindi manager\'s comment that a London gig is cheaper than one in an Australian capital is an anecdote. UPDATE DUE: the Commission\'s final report.')

R('2026-11-13-ministers-net-budget-savings',4,'Only four ministers saved money this year, as spending outruns savings','2026-11-13','news',['ABC News'],
 'Shows discretionary fiscal policy pulling against monetary policy: new spending exceeds savings by $8.7 billion while the RBA raises rates.',
 'An ABC analysis of the May budget papers found that new government spending in 2026-27 exceeded savings by $8.7 billion, and revenue measures added $2.2 billion, leaving the budget $6.5 billion worse off this year. Only four of more than 20 ministers achieved net savings: Catherine King, Jason Clare, Julie Collins and Jim Chalmers.',
 ['4C.1','4C.2','4B.1'],['Y2b.3','Y2b.5','Y2b.13'],['P5a.4'],['4H.3','4D.3'],['Y2g.1','Y2b.12'],[],
 ['budget','inflation','rates'],['fiscal','monetary'],['adas','chart'],
 [F('New spending in excess of savings, 2026-27','$8.7 billion','2026-27','budget','ABC News analysis of budget papers'),F('Revenue measures','+$2.2 billion','2026-27','budget','ABC News analysis of budget papers'),F('Net impact on the budget this year','-$6.5 billion','2026-27','budget','ABC News analysis of budget papers'),F('Ministers with net savings','4 of more than 20','2026-27','budget','ABC News'),F('Public service staff in May','217,256 (173,558 before Labor took office)','May 2026','budget','ABC News')],
 [T('Discretionary fiscal policy','Deliberate changes to spending and tax decisions by the government.'),T('MYEFO','Mid-Year Economic and Fiscal Outlook: the December budget update.')],
 [['ABC News, Only four ministers have achieved net savings this year, budget papers show, 13 Nov 2026','https://abc.net.au/news/2026-11-13/which-ministers-have-achieved-net-savings-this-year/107377958']],
 'Net new government spending shifts AD right, lifting output and the price level. With inflation above target and the cash rate at 4.85% that works against the RBA, which is trying to slow demand, so the RBA may need to raise rates further when fiscal policy is expansionary and monetary policy is contractionary.',
 [Q('Explain how expansionary fiscal policy can limit the effectiveness of monetary policy in reducing inflation.',4)],
 'Health had the largest net spend, and Defence and Finance each spent more than $1 billion, as reported. Finance Minister Katy Gallagher is looking for savings before MYEFO in December but has not committed to a net saving. The measure is the ABC\'s own analysis of the budget papers. Extends the 5 November budget versus inflation item. UPDATE DUE: December MYEFO.')

R('2026-11-14-housing-market-turns-to-buyers',3,'Housing turns into a buyers\' market as tax changes and rate rises bite','2026-11-14','news',['ABC News','realestate.com.au','Property Buzz'],
 'House prices, auction clearance rates and investor lending show the combined effect of the May tax changes and five rate rises.',
 'After the government wound back negative gearing and capital gains tax concessions and the RBA lifted rates five times, the national median house price is 5.6% below its March peak, auction clearance rates have dropped below 50%, and realestate.com.au says buyers hold the upper hand in 72% of markets. The government says the shift from investors to first home buyers is the point of the reforms, while critics say the 1.2 million new homes target is now likely out of reach.',
 ['3E.4','4D.3'],['Y1d.5','Y2d.3'],['P4c.7','P2h.8'],['3A.7','4C.2'],['Y2b.13','Y2c.5'],['P5a.4','P4c.3'],
 ['housing','inequality','budget'],['fiscal','monetary'],['ds','chart'],
 [F('National median house price against March peak','-5.6% (apartments -3.9%)','November 2026','housing','ABC News; REA data'),F('Auction clearance rate','below 50% (long-run average about 60%)','November 2026','housing','ABC News'),F('Share of markets where buyers have the edge','72%','November 2026','housing','realestate.com.au via Property Buzz'),F('Fall in new home loans by type, September quarter (rounded)','investors -31%; first home buyers -8%; owner-occupiers -5%; all loans -15%','September quarter 2026','housing','ABS via ABC News'),F('Value of new home loans','-15.5% (largest fall since the series began in 2002)','September quarter 2026','housing','ABS via ABC News')],
 [T('Negative gearing','Deducting losses on an investment property from other income to cut tax.'),T('Wealth effect','People spend less when the value of their assets, such as housing, falls.')],
 [['ABC News, Do Australians actually want cheaper housing? We\'re finding out fast, 14 Nov 2026','https://abc.net.au/news/2026-11-14/do-australians-actually-want-cheaper-housing/107378812'],['Property Buzz daily brief (REA data), 15 Nov 2026','https://propertybuzz.com.au/daily-brief/property-brief-15-November-2026'],['ABC News, markets live blog (ABS lending data), 11 Nov 2026','https://abc.net.au/news/2026-11-11/asx-markets-business-live-news-nov-11/107370848']],
 'Lower tax concessions and higher rates reduce investor demand, so prices fall and fewer homes change hands. Lower prices help first home buyers but reduce existing owners\' wealth, which cuts spending through the wealth effect, and falling prices can also reduce new housing supply because builders start fewer projects.',
 [Q('Evaluate whether falling house prices are good or bad for the Australian economy.',6)],
 'The 5.6% peak-to-now figure is the digest\'s and differs from the 6% fall since March in the APRA item and the quarterly falls in other items, because the series and dates differ, so quote the source. The loan percentages are rounded. Complements the 11 November record fall in new home loans and budget tax changes items.')

R('2026-11-15-youth-unemployment-rising',3,'Young workers in the firing line as the economy slows','2026-11-15','news',['ABC News','ABS','CBA'],
 'Youth unemployment is more than double the overall rate and is expected to rise as higher rates slow the economy.',
 'ABS data for September put youth unemployment at 11.1%, compared with 4.7% overall, and economists warn it could rise further as the economy softens after five rate rises. CBA economist Harry Ottley says youth unemployment is rising faster than for other groups, though the youth employment-to-population ratio is still above its 2019 level.',
 ['3B.1','3B.3','3B.5'],['Y1b.5','Y1b.6','Y1b.10','Y1b.11'],[],['3B.2'],['Y1b.9','Y1b.7'],['P3b.1'],
 ['employment','growth'],['monetary'],['adas','chart'],
 [F('Youth unemployment rate','11.1%','September 2026','employment','ABS'),F('Overall unemployment rate','4.7%','September 2026','employment','ABS'),F('Youth employment-to-population ratio','63.6% (peak 66.7% in November 2022; 2019 average 59.7%)','2026','employment','ABS and CBA via ABC News'),F('Youth participation rate','71.4% (67.7% in 2019)','2026','employment','ABS and CBA via ABC News')],
 [T('Cyclical unemployment','Unemployment caused by a fall in aggregate demand during a downturn.'),T('Employment-to-population ratio','The share of a group\'s population that has a job.')],
 [['ABC News, Economists are watching for higher youth unemployment as economy softens, 15 Nov 2026','https://abc.net.au/news/2026-11-15/youth-unemployment-could-rise-as-economy-softens/107382888']],
 'Higher interest rates and weaker household spending shift AD left, real GDP falls and firms need fewer workers, so cyclical unemployment rises. Young workers, who are often casual and have less experience, are usually the first to lose hours or miss out on jobs, and SEEK says graduate job ads have trended down since their post-pandemic highs. A July DEWR study found AI is not yet causing broad disruption.',
 [Q('Explain why young people are more likely than other groups to become unemployed during an economic slowdown.',4)],
 'The forecast that youth unemployment will rise further is economists\' expectation, not an outcome. The Qantas 850 job cuts are mentioned as context. The same 11.1% figure appears in the 26 October item on who is affected by unemployment; the 4.7% rate is the national figure for September.')

R('2026-11-14-microsoft-outage-cloud-dependence',2,'Microsoft outage exposes Australia\'s reliance on a few foreign cloud giants','2026-11-14','news',['ABC News','University of Melbourne'],
 'A globalisation risk: cheaper imported digital services concentrate risk in a few foreign suppliers, and resilience has an opportunity cost.',
 'A global Microsoft outage on 13 November knocked out Outlook, SharePoint and Copilot for Australian users. University of Melbourne experts say most Australian email runs through Microsoft or Google and most websites sit on Amazon or other big cloud platforms, and that building resilience will cost money.',
 ['1A.3','1A.6','2A.1'],['Y3e.3','Y3b.2'],[],['1D.6','2B.3'],['Y1a.10'],[],
 ['global','trade','investment'],['global','micro'],['compare','flow'],
 [F('Microsoft services hit','3 (Outlook, SharePoint, Copilot)','13 November 2026','global','ABC News'),F('Firms carrying most Australian email','2 (Microsoft and Google)','2026','global','University of Melbourne via ABC News'),F('France moved government operating systems from Microsoft to Linux','April 2026 (Germany and Austria also reassessing)','April 2026','global','ABC News')],
 [T('Services imports','Payments to overseas firms for services such as cloud computing and software, recorded in the current account.'),T('Opportunity cost','The next best alternative given up when resources go to one use.')],
 [['ABC News, Microsoft outage shows Australia must develop digital resilience, experts warn, but it will cost, 14 Nov 2026','https://abc.net.au/news/2026-11-14/microsoft-outage-and-cloud-providers-tech-risk-in-australia/107383316']],
 'Relying on global cloud providers is cheaper because of economies of scale and gives access to frontier tools, but one outage hits millions of users and adds to services imports. Building local or regulated back-ups gives more control and resilience, as Toby Murray argues governments could regulate these firms like banks, but it needs significant investment and gives up some benefit of specialisation. On a production possibility frontier, more digital resilience means giving up other goods and services.',
 [Q('Explain one benefit and one cost for Australia of relying on overseas providers for digital services.',4)],
 'Microsoft said just after 9am AEST on 13 November that access was recovering, but servers were unresponsive again about an hour later, as reported. The experts\' views are their own, and the cost of building resilience is not quantified in the digest.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('added',n,'total',len(d))
