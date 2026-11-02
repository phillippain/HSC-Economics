import json,os
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-10-22-house-price-falls','2026-10-30-oil-six-month-high-hormuz-attacks','2026-10-31-china-factories-slip-into-contraction','2026-10-29-aud-steady-iron-ore-flat-oil-high'}
os.makedirs('_to_delete/superseded',exist_ok=True)
for x in d:
    if x['id'] in REMOVE:
        src=x['file']['path']
        if os.path.exists(src): os.rename(src,'_to_delete/superseded/'+os.path.basename(src))
    if x['id']=='2026-10-25-record-quarterly-house-price-fall' and x.get('note'):
        x['note']=x['note'].replace('the monthly figures filed on 22 October','the monthly Cotality figures filed on 2 November')
d=[x for x in d if x['id'] not in REMOVE]; have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
def fl(i): return {'path':f'files/{i[:7]}/{i}.pdf','label':'One-page digest','pages':1}
recs=[]
def add(**k): recs.append(k)
BLOG='https://www.abc.net.au/news/2026-11-02/asx-markets-business-live-news-nov-2/107334212'
L_BLOG=['ABC News, ASX markets business live blog, 2 Nov 2026',BLOG]
PB='https://www.abc.net.au/news/2026-11-02/federal-politics-live-blog-albanese-chogm-nov-2/107334912'
RATE='https://abc.net.au/news/2026-11-03/rate-hikes-gather-pace-across-the-globe-as-deficits/107336008'

i='2026-11-01-myefo-no-promise-of-net-savings'
add(id=i,title='No promise of net savings in December\'s budget update',date='2026-11-01',type='news',outlets=['ABC News'],
 summary='Shows why structural spending pressures make a contractionary budget hard, and why that leaves the RBA carrying more of the load.',
 lede='Finance Minister Katy Gallagher would not commit to overall savings in December\'s Mid-Year Economic and Fiscal Outlook, citing rising costs in health, aged care and veterans\' services. Treasurer Jim Chalmers has warned higher borrowing costs will add billions, while the Opposition says spending restraint would ease pressure on the RBA.',
 about={'h09':['4C.1','4C.2','4B.1'],'y12':['Y2b.3','Y2b.5','Y2b.12','Y2b.14'],'y11':[]},also={'h09':['4C.3','4H.3','4D.1'],'y12':['Y2b.13','Y2c.7'],'y11':[]},
 issues=['budget','inflation'],levers=['fiscal'],diagrams=['adas','flow'],
 figures=[F('Government spending','26.8% of GDP','2026','budget','ABC News'),F('Budget deficit','about 1% of GDP','2026','budget','ABC News'),F('Annual CPI','4.3%','September 2026','inflation','ABS'),F('MYEFO release','December 2026','December 2026','budget','ABC News')],
 terms=[T('MYEFO','The Mid-Year Economic and Fiscal Outlook, the December update of the May budget.'),T('Structural balance','The budget balance after removing the effects of the economic cycle.'),T('Cyclical component','Budget changes caused by the business cycle.')],
 links=[['ABC News, Government will not promise net savings in budget update, 1 Nov 2026','https://abc.net.au/news/2026-11-01/katy-gallagher-wont-promise-myefo-net-savings/107333248'],['ABC News, Interest rate hikes gather pace across the globe, 3 Nov 2026',RATE]],
 file=fl(i),angle='Rising health, aged care and veterans\' costs are structural pressures, not cyclical ones, so they do not fade as the economy slows. If new spending is not offset by savings, the fiscal stance stays supportive and the RBA carries more of the load.',
 questions=[Q('Explain what MYEFO is and how the fiscal stance it reveals could influence monetary policy decisions.',4)],
 note='Government and Opposition positions are reported as each put them. UPDATE DUE: MYEFO in December. Follows the 29 October item on Chalmers ruling out a fuel discount.')

i='2026-11-02-oil-eases-hormuz-talks'
add(id=i,title='Oil eases on Hormuz talks, but the supply shock is not over',date='2026-11-02',type='news',outlets=['Euronews','ABC News'],
 summary='Shows how a possible reopening of the Strait of Hormuz shifts oil supply back, while a geopolitical risk premium keeps prices high. Replaces the 30 October edition.',
 lede='Brent crude fell about 2-3% on 2 November to around US$108-111 a barrel after rising 14-15% in October and peaking near US$118, as Iran held talks in Qatar on reopening the strait. Goldman Sachs estimates about US$27 a barrel is a geopolitical risk premium.',
 about={'h09':['3C.3','1A.1'],'y12':['Y1c.4','Y1c.5','Y3e.3'],'y11':[]},also={'h09':['3C.4','4D.3','1A.8'],'y12':['Y1c.1','Y1a.10','Y1a.13','Y2c.8'],'y11':[]},
 issues=['inflation','global','trade'],levers=['monetary'],diagrams=['ds','adas','flow'],
 figures=[F('Brent crude','about US$110 (range US$108-111; down 2-3%)','2 November 2026','global','Euronews; ABC News'),F('Brent rise over October','+14-15% (peak near US$118)','October 2026','global','Euronews; ABC News'),F('Risk premium in the oil price (Goldman Sachs)','about US$27 a barrel','2 November 2026','global','Goldman Sachs via Euronews'),F('Goldman Sachs end-of-year Brent forecast','US$105','2026','global','Goldman Sachs via Euronews'),F('Italy\'s inflation','5.4%','October 2026','inflation','Euronews'),F('Australian fuel prices','+9.4%','September 2026','inflation','ABS')],
 terms=[T('Supply shock','An unexpected event that cuts productive capacity or raises input costs.'),T('Cost-push inflation','Inflation driven by higher production costs rather than excess demand.'),T('Price-inelastic demand','Quantity demanded responds little to a price change, as for fuel in the short run.')],
 links=[['Euronews, Oil slides on Hormuz deal hopes but Trump keeps Iran strikes on the table, 2 Nov 2026','https://www.euronews.com/2026/11/02/oil-slides-on-hormuz-deal-hopes-but-trump-keeps-iran-strikes-on-the-table'],L_BLOG],
 file=fl(i),angle='Short-run oil demand is inelastic, so a supply cut raises the price a lot. A deal that reopens the strait would shift supply back right. On an AD/AS diagram the shock shifts SRAS left: higher prices and lower output, or stagflation.',
 questions=[Q('Explain how a disruption to oil supply in the Middle East can affect inflation and economic growth in Australia.',4)],
 note='Replaces the 30 October item, which reported Brent settling at US$117.64 and at least 35 attacks on shipping in October; that report put the Hormuz traffic about 70% below pre-war levels. Iran set conditions for reopening, including an end to the US naval blockade. UPDATE DUE: outcome of the talks.')

i='2026-10-31-china-factories-export-orders-fall'
add(id=i,title='China\'s factories slow as export orders fall',date='2026-10-31',type='stats',outlets=['AP','Reuters','National Bureau of Statistics','CGTN'],
 summary='China\'s official and private factory surveys diverge in October, with falling export orders and iron ore near US$91, a warning for Australia\'s biggest export market. Replaces the earlier PMI item.',
 lede='China\'s official manufacturing PMI fell to 49.3 in October from 50.1, with new export orders dropping to 48.7 from 50.0, while the private RatingDog PMI held at 52.0. China\'s trade surplus was about US$800 billion by August, on track to beat 2025\'s record of US$1.2 trillion.',
 about={'h09':['1A.8','2A.1','1E.1'],'y12':['Y3e.1','Y3e.3','Y1a.7'],'y11':['P6a.2']},also={'h09':['3D.3','4H.2'],'y12':['Y3a.15'],'y11':[]},
 issues=['global','growth','trade'],levers=['global'],diagrams=['ds','chart','flow'],
 figures=[F('Official manufacturing PMI','49.3 (September 50.1)','October 2026','global','National Bureau of Statistics via AP'),F('New export orders index','48.7 (September 50.0)','October 2026','global','National Bureau of Statistics via AP'),F('Production index','49.8','October 2026','global','National Bureau of Statistics via AP'),F('Non-manufacturing PMI','49.7 (September 50.2)','October 2026','global','National Bureau of Statistics via CGTN'),F('Private (RatingDog) PMI','52.0','October 2026','global','Reuters'),F('Iron ore','US$90.80 a tonne','31 October 2026','trade','AP'),F('China\'s trade surplus','about US$800b by August (2025 record US$1.2 trillion)','August 2026','global','AP')],
 terms=[T('Purchasing managers\' index (PMI)','A business survey where above 50 means expansion and below 50 means contraction.'),T('Trade surplus','Exports exceed imports in value.'),T('Terms of trade','Export prices relative to import prices.')],
 links=[['AP via WPXI, China factory activity contracts in October, 31 Oct 2026','https://www.wpxi.com/news/business/chinas-factory/UAWDXJV27M6LZNHTN2G2DMEGTQ/'],['Reuters, China private PMI, 1 Nov 2026','https://1027wbow.com/2026/11/01/china-factory-growth-slows-in-october-as-export-orders-ease-private-pmi-shows/'],['AP/PBS, US and China release product lists for tariff cuts, 28 Sep 2026','https://www.pbs.org/newshour/world/u-s-and-china-release-product-lists-for-tariff-cuts-after-trump-xi-meeting'],['China-Global South Project (AFP), China manufacturing PMI October 2026, 31 Oct 2026','https://chinaglobalsouth.com/2026/10/31/china-manufacturing-pmi-october-2026-factory-contraction/'],['CGTN, China\'s manufacturing PMI at 49.3, non-manufacturing PMI at 49.7, 31 Oct 2026','https://news.cgtn.com/news/2026-10-31/China-s-manufacturing-PMI-at-49-3-non-manufacturing-PMI-at-49-7-1RGwN3PBXpu/p.html']],
 file=fl(i),angle='If Chinese steel mills cut output, demand for iron ore shifts left, lowering Australia\'s export prices, terms of trade and national income. Link China\'s growth to Australia through export revenue, company tax receipts and the AUD. The two PMIs disagree, so avoid overstating one month.',
 questions=[Q('Explain how a slowdown in China\'s manufacturing sector could affect Australia\'s terms of trade and current account.',4)],
 note='Replaces the 31 October PMI item, whose figures are carried over. Official and private surveys sample different firms, which explains the gap. One month\'s data may reverse.')

i='2026-11-03-global-rates-government-debt'
add(id=i,title='Rates rise worldwide as government debt piles up',date='2026-11-03',type='news',outlets=['ABC News'],
 summary='Connects rising global bond yields to deficits and sovereign debt, and separates the level of spending from the budget balance when judging inflation.',
 lede='An ABC analysis argues investors are demanding higher returns to lend to governments, pushing up interest rates around the world, and that deficits, not just the size of spending, add to inflation. US interest payments on federal debt now exceed US$1 trillion a year and the Bank of England is tipped to raise its rate to 4.0%.',
 about={'h09':['1A.4','4C.3','4D.3'],'y12':['Y2b.6','Y2b.12','Y2c.5'],'y11':[]},also={'h09':['4C.1','4H.2'],'y12':['Y2b.13','Y3c.4','Y3b.3'],'y11':[]},
 issues=['global','rates','budget'],levers=['fiscal','monetary','global'],diagrams=['adas','flow'],
 figures=[F('US interest payments on federal debt','more than US$1 trillion a year','2026','global','ABC News'),F('Bank of England rate if Thursday\'s hike goes ahead','4.0%','5 November 2026','rates','ABC News'),F('Australian government spending','26.8% of GDP (pandemic peak 31.3%)','2026','budget','ABC News'),F('Australian budget deficit','about 1% of GDP','2026','budget','ABC News'),F('Australian 10-year bond yield','5.13%','2 November 2026','rates','ABC News'),F('Capital raised by data centre operators this year','record $35 billion','2026','investment','ABC News')],
 terms=[T('Budget deficit','Government spending exceeds revenue in a year.'),T('Sovereign debt','Borrowing by a national government, usually through bonds.'),T('Bond yield','The return investors earn on a bond; a higher yield means a higher cost of borrowing.')],
 links=[['ABC News, Interest rate hikes gather pace across the globe as deficits and debt pile up, 3 Nov 2026',RATE],L_BLOG],
 file=fl(i),angle='Higher global yields raise borrowing costs for households, firms and governments, shifting AD left and easing the price level but cutting real GDP. Separate the level of spending from the budget balance when judging whether fiscal policy adds to inflation.',
 questions=[Q('Discuss how rising global interest rates could affect Australia\'s economy and federal budget.',6)],
 note='An analysis piece, so the claim that deficits drive inflation is one view. UPDATE DUE: RBA decision (3 November) and the Bank of England decision (5 November). Private data centre investment is also cited as an inflation pressure.')

i='2026-11-02-uk-fta-backpacker-rules'
add(id=i,title='Albanese wants to rewrite part of the UK trade deal on backpackers',date='2026-11-02',type='news',outlets=['ABC News'],
 summary='Shows how a free trade agreement can cover labour mobility as well as tariffs, with winners and losers in the regional farm labour market.',
 lede='The Prime Minister will ask the UK to restore the regional work rule for British working holiday makers, which was waived under the Australia-UK free trade agreement. British backpackers rose from about 47,000 in 2024 to nearly 80,000 last financial year, and farmers warn of harvest labour shortages.',
 about={'h09':['2D.2','2D.3'],'y12':['Y3a.13','Y3a.16'],'y11':[]},also={'h09':['1B.4','2D.1'],'y12':['Y3a.3'],'y11':[]},
 issues=['trade','employment'],levers=['trade','labour'],diagrams=['ds','flow'],
 figures=[F('British working holiday makers','nearly 80,000 (about 47,000 in 2024)','last financial year','trade','ABC News'),F('Harvest workers who come from overseas','about 1 in 7','2026','employment','ABC News'),F('Proposed cap on second-year working holiday visas','45,000','2026','trade','ABC News'),F('Stay allowed without regional work (British working holiday makers)','up to three years','2026','trade','ABC News')],
 terms=[T('Free trade agreement','A treaty lowering trade barriers, often also covering services, investment and labour mobility.'),T('Working holiday maker','A visa allowing young travellers to work, often in seasonal jobs.'),T('Labour supply','The number of workers willing and able to work at each wage.')],
 links=[['ABC News, Albanese to discuss British backpacker changes with Burnham, 2 Nov 2026','https://www.abc.net.au/news/2026-11-02/albanese-to-discuss-british-backpacker-changes-with-burnham/107208084'],['ABC News, Federal politics live blog, 2 Nov 2026',PB]],
 file=fl(i),angle='Modern FTAs go beyond tariffs: services, investment and the movement of people all create winners and losers. The deal is already law, so changing it needs the UK\'s consent.',
 questions=[Q('Assess the costs and benefits of including labour-mobility provisions in Australia\'s free trade agreements.',6)],
 note='UPDATE DUE: outcome of the talks at CHOGM. The labour market diagram is the digest\'s illustration of a supply shift. The UK Prime Minister is named as Andy Burnham in the digest.')

i='2026-11-02-commodity-prices-aud-softens'
add(id=i,title='Commodity prices slip and the dollar softens before the RBA',date='2026-11-02',type='stats',outlets=['ABC News'],
 summary='Shows how falling export prices lower demand for the AUD while a wider interest rate differential supports it. Replaces the 29 October edition.',
 lede='The Australian dollar slipped 0.1% to 70.20 US cents on 2 November as iron ore held at US$90.80 a tonne and copper fell 1.5%, ahead of the expected RBA rate rise. Australia\'s 10-year bond yield of 5.13% is above the US 4.93%, which supports demand for AUD assets.',
 about={'h09':['2C.2','2C.3','2C.6'],'y12':['Y3c.2','Y3c.4','Y3c.5','Y1a.7'],'y11':['P6c.1']},also={'h09':['2A.1','2C.4','3D.3','4D.3'],'y12':['Y3c.1','Y3c.6','Y3e.3'],'y11':['P6a.2','P6c.2']},
 issues=['fx','trade','rates'],levers=['monetary'],diagrams=['fx','flow'],
 figures=[F('Australian dollar','70.20 US cents (-0.1%)','2 November 2026','fx','ABC News'),F('Iron ore','US$90.80 a tonne','2 November 2026','trade','ABC News'),F('Copper','-1.5%','2 November 2026','trade','ABC News'),F('Gold','near a one-year low (as reported)','2 November 2026','trade','ABC News'),F('ASX 200','-0.6% to about 8,857 (BHP -1.4%, Northern Star -4.8%)','2 November 2026','trade','ABC News'),F('Australian / US 10-year yield','5.13% / 4.93% (gap +0.20 points)','2 November 2026','rates','ABC News')],
 terms=[T('Exchange rate','The price of one currency in terms of another (AUD/USD).'),T('Interest rate differential','The gap between Australian and overseas interest rates, which drives capital flows.'),T('Terms of trade','Export prices relative to import prices.')],
 links=[L_BLOG],
 file=fl(i),angle='Lower commodity prices mean foreign buyers need fewer Australian dollars for our exports, shifting AUD demand left. An RBA hike works the other way: a wider differential attracts capital inflows and shifts demand right.',
 questions=[Q('Explain two factors that influence the value of the Australian dollar, and how a change in its value affects the current account.',5)],
 note='Single-day figures, so update before quoting. UPDATE DUE: RBA decision on 3 November. Replaces the 29 October edition; the 28 October item on the NZ dollar is kept.')

i='2026-11-02-house-prices-fastest-fall-40-years'
add(id=i,title='House prices fall at the fastest pace in 40 years',date='2026-11-02',type='stats',outlets=['Cotality','ABC News'],
 summary='The October Cotality result: a seventh monthly fall, with the wealth effect and transmission of higher rates. Replaces the sixth-month edition.',
 lede='National home values fell 1.2% in October, the seventh straight monthly fall, and are 6.7% below the March peak, about $63,400 off the median dwelling. Capital cities are down 8.1% in seven months and set to pass the 2017-19 record fall of 8.2%, and AMP now expects a 15% fall.',
 about={'h09':['3E.4','4D.3','3A.1'],'y12':['Y2c.5','Y1d.1','Y1d.6'],'y11':['P2d.1','P4c.7']},also={'h09':['3E.5','4H.1'],'y12':['Y1d.5','Y1a.14'],'y11':[]},
 issues=['housing','rates','inequality'],levers=['monetary'],diagrams=['ds','flow'],
 figures=[F('National home values, monthly change','-1.2% (seventh straight fall)','October 2026','housing','Cotality via ABC News'),F('Fall from the March peak','-6.7% (about $63,400 off the median dwelling)','October 2026','housing','Cotality via ABC News'),F('Median dwelling value','about $884,855','October 2026','housing','Cotality via ABC News'),F('Capital cities, fall over seven months','-8.1% (record 2017-19 fall was 8.2%)','October 2026','housing','Cotality via ABC News'),F('AMP expected fall','15%','2026','housing','AMP via ABC News')],
 terms=[T('Wealth effect','Spending changes as household wealth, such as house prices, changes.'),T('Transmission mechanism','The channels through which the cash rate affects spending and inflation.'),T('Distribution of wealth','How net worth is shared across households.')],
 links=[['ABC News, Largest property downturn in 40 years in sight, 2 Nov 2026','https://www.abc.net.au/news/2026-11-02/house-prices-fall-in-october-biggest-downturn-40-years-cotality/107325214'],L_BLOG],
 file=fl(i),angle='Higher rates cut borrowing capacity and investors have pulled back after property tax changes, shifting housing demand left. Falling prices hit recent buyers with small deposits hardest, which matters for wealth distribution as well as spending.',
 questions=[Q('Explain how rising interest rates affect house prices and consumer spending through the wealth effect.',4)],
 note='Replaces the sixth-month item, which reported HSBC\'s economist expecting falls of up to 13%. The AMP forecast is one institution\'s view. See also the 25 October Domain quarterly figures.')

i='2026-11-02-banks-cut-growth-forecasts-stagflation'
add(id=i,title='Banks see slower growth and higher unemployment, but still expect a hike',date='2026-11-02',type='news',outlets=['ABC News','NAB','CBA'],
 summary='A current stagflation example: NAB and CBA cut growth to about 1% and lifted unemployment forecasts while inflation stays above target.',
 lede='NAB cut its 2027 GDP growth forecast to 1.0% and expects unemployment to reach 5.4% by the end of 2027, while CBA cut growth to about 1% by mid-2027 from 1.8% and raised its unemployment forecast to 5.1% from 4.8%. CBA expects trimmed mean inflation to stay at or above 3.5% until at least mid-2027.',
 about={'h09':['4I.2','4I.3','3C.3'],'y12':['Y1c.1','Y1c.6','Y2c.8'],'y11':[]},also={'h09':['3A.7','3B.2','4D.3'],'y12':['Y1b.11','Y1a.14'],'y11':[]},
 issues=['growth','employment','inflation'],levers=['monetary'],diagrams=['adas','flow'],
 figures=[F('NAB GDP growth forecast','1.0% (2027)','2 November 2026','growth','NAB via ABC News'),F('NAB unemployment forecast','5.4% by end-2027','2 November 2026','employment','NAB via ABC News'),F('CBA growth forecast','about 1% by mid-2027 (was 1.8%)','2 November 2026','growth','CBA via ABC News'),F('CBA unemployment forecast','5.1% (was 4.8%)','2 November 2026','employment','CBA via ABC News'),F('CBA trimmed mean forecast','3.5% or more until at least mid-2027','2 November 2026','inflation','CBA via ABC News'),F('CBA wage growth forecast','2.9% by late 2028','2 November 2026','employment','CBA via ABC News')],
 terms=[T('Stagflation','High inflation combined with weak growth or rising unemployment.'),T('Internal balance','Sustainable growth with full employment and low, stable inflation.'),T('Trimmed mean','An underlying inflation measure that removes extreme price changes.')],
 links=[L_BLOG],
 file=fl(i),angle='Higher fuel and construction costs shift SRAS left, so prices rise while output falls. Raising rates to fight supply-driven inflation deepens the slowdown, a key limitation of monetary policy.',
 questions=[Q('Explain why policymakers find it difficult to achieve internal balance when inflation rises while growth slows.',5)],
 note='Bank forecasts are projections, not outcomes, and the digest relies on an ABC live blog summary. The "stagflation" label is the digest\'s description. UPDATE DUE: RBA forecasts on 3 November.')

i='2026-11-02-inflation-gauge-factories-contract'
add(id=i,title='Inflation pressures persist as factories contract',date='2026-11-02',type='stats',outlets=['ABC News','Melbourne Institute','ABS'],
 summary='A timely monthly inflation gauge and PMI, with the Phillips curve diagram showing why rising expectations make disinflation costlier.',
 lede='The Melbourne Institute Inflation Gauge rose 0.5% in October (September 0.3%), its fourth straight monthly rise, while the manufacturing PMI fell to 49.6, its second month of contraction. The ABS reported headline CPI of 4.3% and trimmed mean of 3.6% for the year to September.',
 about={'h09':['3C.1','3C.2','3C.3'],'y12':['Y1c.3','Y1c.8','Y1c.9'],'y11':[]},also={'h09':['3C.4','3A.7'],'y12':['Y1c.4','Y1c.6'],'y11':[]},
 issues=['inflation','growth'],levers=['monetary'],diagrams=['phillips','chart'],
 figures=[F('Melbourne Institute Inflation Gauge, monthly','+0.5% (September +0.3%; fourth straight rise)','October 2026','inflation','Melbourne Institute via ABC News'),F('Manufacturing PMI','49.6 (second month of contraction)','October 2026','growth','ABC News'),F('Dwelling approvals','+5.1% (apartments +16.6%, houses -5.3%)','September 2026','housing','ABS via ABC News'),F('Headline CPI, annual','4.3%','September 2026','inflation','ABS'),F('Trimmed mean, annual','3.6%','September 2026','inflation','ABS')],
 terms=[T('Headline CPI','The price change of the ABS\'s full basket of goods and services.'),T('Trimmed mean','Removes the largest price rises and falls; the RBA\'s preferred underlying measure.'),T('Inflation expectations','What people expect inflation to be, which feeds into wages and price-setting.')],
 links=[L_BLOG,['ABS, CPI rose 4.3% in the year to September 2026','https://www.abs.gov.au/media-centre/media-releases/cpi-rose-43-year-september-2026']],
 file=fl(i),angle='If people expect higher inflation, the short-run Phillips curve shifts out, so inflation rises even as unemployment rises and getting back to 2-3% becomes more costly. This is why the RBA targets underlying inflation and acts early to anchor expectations.',
 questions=[Q('Distinguish between headline and underlying inflation, and explain why the RBA focuses on the trimmed mean.',4)],
 note='The Melbourne Institute gauge is a private monthly estimate, not an official statistic. UPDATE DUE: RBA decision on 3 November.')

i='2026-11-02-spending-cuts-vs-rate-rises'
add(id=i,title='Could government spending cuts do the RBA\'s job?',date='2026-11-02',type='news',outlets=['ABC News'],
 summary='Compares contractionary fiscal policy with a rate rise as ways to reduce inflation, with Chris Richardson\'s rule of thumb.',
 lede='With a fifth rate rise for the year expected, economists and politicians are debating whether the budget should do more of the work of bringing inflation down. Chris Richardson estimates that $7-10 billion a year in spending cuts would have about the same effect as one rate rise.',
 about={'h09':['4B.1','4C.2','4D.2'],'y12':['Y2b.3','Y2b.13','Y2b.14'],'y11':[]},also={'h09':['4H.1','4H.3'],'y12':['Y2c.7','Y2c.8'],'y11':[]},
 issues=['budget','inflation','rates'],levers=['fiscal','monetary'],diagrams=['adas','compare'],
 figures=[F('Spending cuts equal to one rate rise (Chris Richardson)','$7-10 billion a year','2 November 2026','budget','ABC News'),F('Cash rate before the decision / if the hike is delivered','4.60% / 4.85%','3 November 2026','rates','ABC News'),F('Fuel tax credits','more than $10 billion a year','2026','budget','ABC News')],
 terms=[T('Fiscal policy','Using government spending and taxation to influence the economy.'),T('Contractionary policy','Settings that reduce aggregate demand.'),T('Policy mix','The combination of fiscal and monetary policy settings.')],
 links=[['ABC News, Could government spending cuts help fight inflation?, 2 Nov 2026','https://www.abc.net.au/news/2026-11-02/government-spending-cuts-to-control-inflation-explained/107337846'],['ABC News, Federal politics live blog, 2 Nov 2026',PB]],
 file=fl(i),angle='Evaluate both arms: fiscal policy can be targeted but is slow and political, while monetary policy is flexible but blunt and falls mainly on borrowers. If the budget does more, the RBA may need to do less.',
 questions=[Q('Evaluate the effectiveness of contractionary fiscal policy, compared with monetary policy, in reducing inflation.',6)],
 note='The Richardson estimate is a rule of thumb, not a precise forecast. The Opposition named the home battery program and EV discount as possible cuts; that is its proposal. UPDATE DUE: RBA decision on 3 November.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
