import json,os
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-11-09-oil-steepest-weekly-fall-since-covid','2026-11-09-china-us-tariff-truce-extended','2026-11-05-aud-steady-near-70-cents','2026-11-06-consumer-sentiment-job-fears'}
os.makedirs('_to_delete/superseded',exist_ok=True)
for x in d:
    if x['id'] in REMOVE:
        src=x['file']['path']
        if os.path.exists(src): os.rename(src,'_to_delete/superseded/'+os.path.basename(src))
d=[x for x in d if x['id'] not in REMOVE]; have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
recs=[]
def R(i,topic,title,date,type,outlets,summary,lede,h,y,z,hh,yy,zz,issues,levers,diagrams,figures,terms,links,angle,questions,note):
    recs.append(dict(id=i,title=title,date=date,type=type,outlets=outlets,summary=summary,lede=lede,
      about={'h09':h,'y12':y,'y11':z},also={'h09':hh,'y12':yy,'y11':zz},issues=issues,levers=levers,diagrams=diagrams,figures=figures,terms=terms,links=links,
      file={'path':f'files/{i[:7]}/{i}.pdf','label':f'Topic {topic} news summary','pages':1},
      angle=angle,questions=questions,note=note,added='2026-11-11'))
TC=lambda t:['The Conversation, '+t+' (article address not given in the digest; link goes to The Conversation Australia home page)','https://theconversation.com/au']
BLOG10=['ABC News, markets live blog, 10 Nov 2026','https://www.abc.net.au/news/2026-11-10/asx-markets-business-live-news-november-10-2026/107363300']
INV=['investingLive, Australian consumer sentiment sinks to four-year low as rates and living costs bite','https://investinglive.com/news/australian-consumer-sentiment-sinks-to-four-year-low-as-rates-and-living-costs-bite/']
BR=['Business Recorder (Reuters), Aussie steadies as oil-fuelled risk rally offsets weak domestic surveys','https://www.brecorder.com/news/40448242/aussie-steadies-as-oil-fuelled-risk-rally-offsets-weak-domestic-surveys']

R('2026-11-11-electrification-35-by-35-pledge',1,'Why COP31 wants 35% of the world\'s energy to be electric by 2035','2026-11-11','news',['The Conversation','University of Melbourne'],
 'Explains where the 35% electrification target comes from, why current policies fall short, and how subsidies could close the gap.',
 'COP31\'s "35-by-35" pledge, led by Chris Bowen and Türkiye\'s Murat Kurum, asks countries to get 35% of global final energy from electricity by 2035, up from 23% today. Analyst Anita Talberg says the figure is the median across the ten lowest-warming climate scenarios, and the IEA projects current policies deliver just under 30%.',
 ['3F.4','1D.8'],['Y2f.3','Y2f.6','Y1e.5'],['P2h.3'],['4G.2','1A.1','4I.6'],['Y3d.6','Y2f.8','Y1e.8','Y3a.15'],['P2h.4','P5a.5'],
 ['environment','global'],['environmental','global'],['ds','chart'],
 [F('Electricity share of global final energy','23% (2025) to 28% (2030) to 35% (2035 pledge)','2025-2035','environment','Climate Resource (2026) analysis of climate scenarios'),F('Share on current policies in 2035','just under 30%','2035 projection','environment','IEA'),F('Share of new cars sold globally in 2025 that were electric','1 in 4','2025','environment','The Conversation'),F('Best-case peak warming','about 1.7°C in the 2040s, back to 1.5°C by 2100','2040s','environment','The Conversation'),F('Energy demand that could be electrified with existing technology','up to three-quarters','2026','environment','The Conversation')],
 [T('Final energy','Energy reaching users such as households and factories.'),T('Overshoot','Warming temporarily exceeding 1.5°C before being brought back down.'),T('Subsidy','A government payment that lowers producers\' costs.')],
 [TC('The world needs to get serious about electrification – here\'s why, Anita Talberg, 11 Nov 2026')],
 'A subsidy on heat pumps or electric vehicles shifts supply right, lowering the price and raising take-up, so it displaces gas appliances. It has a budget cost and an opportunity cost, so it is justified only if climate and energy-security gains are larger. Cheaper finance helps developing economies electrify, which links environmental goals with development.',
 [Q('Explain how government policies could speed up electrification, and assess one economic cost of doing so.',4)],
 'Disclosure in the source: the author\'s organisation, Climate Resource, received Australian Government funding for analysis on electrification as a COP31 priority. The 35% figure is a pledge and is voluntary. Barriers named are grid and storage investment, incentives to switch from gas and affordable finance. See the ABC COP31 item filed today.')

R('2026-11-10-cop31-electrification-push',1,'COP31 admits 1.5°C will be missed and bets on electrification','2026-11-10','news',['ABC News'],
 'Shows why voluntary climate pledges struggle with a global negative externality and free riders.',
 'The COP31 climate summit, co-hosted by Türkiye and Australia, has accepted for the first time that warming will exceed 1.5°C. Its main proposal is a voluntary push for electricity to supply 35% of the world\'s energy by 2035, from about 23% now and about 30% on existing policies.',
 ['3F.4','1D.8','1D.6'],['Y1e.5','Y2f.6','Y3d.6'],['P2h.3'],['4G.1','4I.6','1A.1'],['Y2f.8','Y1e.7','Y1e.4'],['P2h.4','P5a.5'],
 ['environment','global'],['environmental','global'],['ds','compare'],
 [F('Target electricity share of world energy by 2035','35% (about 23% now; about 30% on current policies, IEA)','2035','environment','ABC News'),F('Projected warming, down from about 4°C before Paris','about 2.6°C','2026','environment','Chris Bowen, via ABC News'),F('Türkiye\'s electricity from coal and gas','55%','2026','environment','ABC News')],
 [T('Negative externality','A cost borne by third parties, not the buyer or seller.'),T('Global public good','A benefit (a stable climate) that no country can be excluded from.'),T('Free rider','A country that benefits from others\' action without acting itself.')],
 [['ABC News, COP31 summit targets major electrification push as 1.5C goal slips away','https://www.abc.net.au/news/2026-11-10/cop31-tingle-global-temperature-1-5c/107366402']],
 'Producers set output on private cost, but burning fossil fuels also imposes climate costs on third parties, so marginal social cost lies above marginal private cost and the market overproduces, creating a deadweight loss. Voluntary pledges are hard to enforce because each country gains from others\' cuts while bearing its own costs.',
 [Q('Explain why voluntary international climate pledges may fail to correct a global negative externality.',4)],
 'Fossil fuel cuts are not formally on the COP31 agenda, as reported, and Australia faces criticism over coal expansion and extending the North West Shelf gas project. The warming figures are Bowen\'s statement. Pairs with the Conversation explainer on the 35% target filed today.')

R('2026-11-10-china-exports-surge-tariff-truce',1,'China\'s exports boom as its shoppers hold back','2026-11-10','news',['Xinhua','TMGM','ABC News'],
 'A lopsided recovery: weak household demand at home, a record trade surplus and a tariff truce, with the tariff diagram. Replaces the 9 November headline-only item.',
 'China\'s consumer prices rose just 0.7% over the year to October, yet its exports jumped 35.2%. Beijing also extended its pause on an extra 24% tariff on US goods for two more months from 10 November, ahead of an expected Trump–Xi meeting at APEC.',
 ['1C.2','1B.1','1D.6'],['Y3a.7','Y3a.8','Y3a.15','Y3a.11'],[],['1A.3','2D.4','2A.1'],['Y3a.5','Y3a.13','Y3e.3'],[],
 ['trade','global','growth'],['trade'],['ds','flow'],
 [F('China consumer prices (CPI), year to October','0.7% (September 0.9%; forecast 0.8%)','October 2026','global','Xinhua'),F('China exports, year on year in US dollars','+35.2% (September +36.3%)','October 2026','trade','Xinhua; TMGM'),F('China trade surplus, first ten months of 2026','about US$1.04 trillion','January-October 2026','trade','TMGM'),F('Extra tariff on US goods kept suspended / tariff that stays','24% (two months from 10 November) / 10%','10 November 2026','trade','China Finance Ministry via ABC News')],
 [T('Trade surplus','Exports greater than imports.'),T('Trade truce','A temporary pause in retaliatory tariffs.'),T('Tariff','A tax on imports that raises their domestic price.')],
 [['Xinhua, China\'s CPI up 0.7% in October','https://english.news.cn/20261109/8cba51c016304f11a089bb1d290bf020/c.html'],['TMGM, morning brief, 9-10 Nov 2026','https://www.tmgm.com/en/analysis/market-insight/morning-brief-2026-11-08'],BLOG10],
 'A tariff on US goods lifts their domestic price from Pw to Pw+t, so Chinese consumers buy less, producers sell more and the government collects revenue, with deadweight losses. Keeping the extra 24% suspended means only the 10% applies: a smaller t, more trade and smaller losses. Link China\'s weak consumer prices and rising surplus to the risk that trading partners respond with protection.',
 [Q('Using a tariff diagram, explain the effects on Chinese consumers, producers and the government of keeping only the 10% tariff on US goods.',4)],
 'Replaces the 9 November record, which was based only on a paywalled Bloomberg headline and web address (24% tariff pause to January, 10% rate kept; it also noted the US cut its extra tariff on Chinese goods from 20% to 10% in the 2025 truce). The "cautious households lead to exports" chain is one common reading, not a finding. The Trump–Xi meeting at APEC was expected the following week. UPDATE DUE: the Trump–Xi meeting. See also the 27 October US-China port-fee truce item.')

R('2026-11-10-cost-of-living-politics-australia',2,'Cost-of-living anger reshapes politics, with spillovers for Australia','2026-11-10','news',['ABC News (analysis)'],
 'Links overseas politics to Australia through super fund exposure to Wall Street, government debt comparisons and trans-Tasman migration.',
 'ABC analysis by Ian Verrender argues the US midterm result and New Zealand\'s too-close-to-call election matter for Australia through financial flows and migration. US government debt is about 126% of GDP against about 33% for Australia, and Australian super funds have up to 20% of their investments on Wall Street, mostly in tech.',
 ['1A.4','1A.7','2A.1'],['Y3b.3','Y3e.3','Y1b.11'],['P6b.1'],['3B.2','3A.7','1D.6'],['Y2b.12','Y3b.1','Y1b.9'],['P3b.1'],
 ['global','employment','budget'],['global'],['ds','chart'],
 [F('US government debt, share of GDP','about 126%','2026','budget','ABC News (Ian Verrender)'),F('Australian government debt, share of GDP','about 33%','2026','budget','ABC News (Ian Verrender)'),F('US share of the world\'s US$112 trillion of government debt','about 38%','2026','global','ABC News (Ian Verrender)'),F('Share of Australian super fund investments on Wall Street','up to 20%','2026','investment','ABC News (Ian Verrender)'),F('New Zealanders who moved to Australia, three years to mid-2026','about 120,000','to mid-2026','employment','ABC News (Ian Verrender)'),F('New Zealand cash rate / inflation / unemployment','2.75% / 3.7% / 5.7%','2026','global','ABC News (Ian Verrender)')],
 [T('Portfolio investment','Buying shares or bonds overseas, such as super funds on Wall Street.'),T('Labour supply','The number of people willing and able to work.'),T('Public debt','The stock of government borrowing, often shown as a % of GDP.')],
 [['ABC News, Why cost-of-living concerns are up-ending global politics','https://www.abc.net.au/news/2026-11-10/why-cost-of-living-concerns-are-up-ending-global-politics-us-nz/107365544']],
 'An inflow of New Zealand workers shifts labour supply right: employment rises but, if wages are sticky and labour demand is weakening, the extra workers show up as higher unemployment in the short run. Migrants also spend, which lifts demand later. Link migration to both aggregate supply and aggregate demand.',
 [Q('Explain how an increase in migration from New Zealand could affect Australia\'s labour market.',4)],
 'An analysis column, so the claim that trans-Tasman migration will add pressure to Australia\'s unemployment rate is the author\'s view, not a forecast. US tech shares fell about 6% on fears of tighter data-centre rules after markets first welcomed the midterm result. Follows the 5 November midterms items.')

R('2026-11-10-aud-steadies-rates-peaked',2,'Markets bet the RBA is done, and the dollar steadies','2026-11-10','stats',['Reuters','Business Recorder','ABC News'],
 'Shows expectations moving the exchange rate before the RBA acts: weak surveys, a likely rate peak and cheaper oil. Replaces the 5 November AUD item.',
 'The Australian dollar held at about US69.2c on Tuesday, recovering part of last week\'s 2.5% slide. After weak consumer and business surveys, swap markets put an 82% chance on the RBA\'s cash rate having peaked at 4.85%.',
 ['2C.2','2C.3','4D.3'],['Y3c.2','Y3c.4','Y3c.5'],['P6c.1'],['2C.6','2A.1','3C.3'],['Y3c.1','Y2c.5'],['P4c.3'],
 ['fx','rates','trade'],['monetary'],['fx','flow'],
 [F('Australian dollar','about 69.2 US cents (-2.5% the previous week; support near June low of 0.6867)','10 November 2026','fx','Reuters via Business Recorder'),F('Market chance the cash rate has peaked at 4.85%','82% (a quarter-point cut fully priced by end-2027)','10 November 2026','rates','Reuters via Business Recorder'),F('10-year bond yield','about 4.99% (lowest since late August)','10 November 2026','rates','Reuters via Business Recorder'),F('Iron ore','about US$93 a tonne','10 November 2026','trade','ABC News')],
 [T('Depreciation','A fall in the AUD\'s value against another currency.'),T('Interest rate differential','The gap between Australian and overseas interest rates.'),T('Swap pricing','What financial markets expect rates to do.')],
 [BR,BLOG10],
 'Foreign investors buy AUD to invest in Australian assets. When they expect no more rate rises, and eventual cuts, those assets look less attractive, demand for AUD falls and the dollar depreciates. A lower AUD helps exporters but raises import prices such as fuel, adding to inflation.',
 [Q('Explain how a change in expected interest rates can affect the value of the Australian dollar.',3)],
 'Single-day market prices and market-implied probabilities, not forecasts by the RBA. Replaces the 5 November item (AUD 70.12 US cents on 5 November, iron ore US$92.80, cash rate 4.85%). Cheaper oil also helped a global rally in riskier assets.')

R('2026-11-10-consumer-sentiment-four-year-low',3,'Consumer mood sinks to a four-year low','2026-11-10','stats',['Westpac-Melbourne Institute','Reuters','investingLive'],
 'Confidence data as evidence the transmission mechanism is working, and a trigger for the multiplier. Replaces the 6 November sentiment item.',
 'The Westpac–Melbourne Institute index of consumer sentiment fell 2.7% to 78.2 in November, its third monthly fall in a row and the lowest since late 2022. High petrol prices, 4.3% inflation and the RBA\'s fifth rate rise this year are weighing on households.',
 ['3A.1','3A.3','4D.3'],['Y1a.8','Y1a.13','Y2c.5'],['P4c.4','P1e.7'],['3A.7','3B.2'],['Y1a.14','Y1b.11','Y1c.7'],['P4c.3'],
 ['growth','rates','employment'],['monetary'],['adas','chart'],
 [F('Westpac–Melbourne Institute consumer sentiment index','78.2 (-2.7%; previous 80.4)','November 2026','growth','Westpac-Melbourne Institute via Reuters'),F('Sentiment compared with a year earlier','almost 25% lower','November 2026','growth','investingLive'),F('Expectations for the economy over the next 12 months','-10.2%','November 2026','growth','investingLive'),F('Consumers expecting mortgage rates to rise further','more than 70%','November 2026','rates','investingLive'),F('Petrol price near / cash rate','A$2.40 a litre / 4.85% (18-year high)','November 2026','inflation','Reuters')],
 [T('Consumer sentiment','An index of how households feel about finances and the economy; below 100 means pessimists outnumber optimists.'),T('Multiplier','An initial cut in spending leads to further falls in income and spending.')],
 [INV,['Reuters via Investing.com, Australian consumer sentiment hits four-year low in November as rates rise (article address not given in full; link goes to Investing.com economy news)','https://www.investing.com/news/economy-news/']],
 'Consumption is about half of aggregate demand. When households feel worse off and expect higher mortgage repayments they save more and spend less, shifting AD left, and the multiplier amplifies the fall. Falling confidence shows the transmission mechanism working, but raises the risk of slower growth and higher unemployment.',
 [Q('Explain how a fall in consumer confidence could affect economic growth and unemployment in Australia.',4)],
 'Replaces the 6 November item (index 80.4 in October, down 4.2% over three months; unemployment expectations index 142.2, up 9.3%; mortgage rate expectations 179; house price expectations 115.6; CommBank forecasting GDP growth of 1% by mid-2027, down from 1.8%, and unemployment peaking at 5.1% at the end of 2027). Mortgage-holder sentiment was a record low (data back to 1994). The August and September bars in the digest are derived from reported monthly falls and are approximate. Westpac expects the RBA to pause at its 7-8 December meeting.')

R('2026-11-10-nab-business-conditions-six-year-low',3,'Business conditions slump to a six-year low as costs keep rising','2026-11-10','stats',['NAB','Reuters','investingLive'],
 'The October business survey shows weak demand and rising costs together, the stagflation risk that makes the RBA\'s job harder.',
 'NAB\'s October survey shows business conditions at their weakest since August 2020 and forward orders falling sharply, yet purchase costs are still rising. Underlying inflation was 3.6% in September, above the RBA\'s 2-3% target.',
 ['3A.7','3C.3'],['Y1c.1','Y1c.4','Y1a.13'],['P1e.7'],['4D.3','4H.3','4I.1'],['Y2c.8','Y1a.14'],['P4c.4'],
 ['growth','inflation','productivity'],['monetary'],['adas','compare'],
 [F('NAB business conditions index','-2 (down 1 point; lowest since August 2020)','October 2026','growth','NAB Monthly Business Survey'),F('Business confidence','-15 (down 1 point; long-run average +5)','October 2026','growth','NAB Monthly Business Survey'),F('Purchase cost growth','2.4% a quarter','October 2026','inflation','NAB Monthly Business Survey'),F('Underlying inflation','3.6%','September 2026','inflation','NAB via investingLive')],
 [T('Forward orders','A leading indicator of future demand.'),T('Stagflation','Rising prices combined with weak growth.')],
 [['investingLive, Australia business conditions hit six-year low as forward orders slide: NAB','https://investinglive.com/news/australia-business-conditions-hit-six-year-low-as-forward-orders-slide-nab/'],['The Star (Reuters/Bloomberg), Australia business conditions fall to six-year low in October, NAB survey shows','https://www.thestar.com.my/business/business-news/2026/11/10/australia-business-conditions-fall-to-six-year-low-in-october-nab-survey-shows']],
 'Higher input costs shift SRAS left, raising the price level and cutting output, while weak orders point to falling demand. That creates a policy conflict: raising rates fights inflation but deepens the slowdown in growth and jobs. Retail was weakest and construction is softening.',
 [Q('Using an AD/AS diagram, explain why rising business costs make the RBA\'s job harder.',4)],
 'A business survey measures opinion and is not an official statistic. NAB says cost pressure remains a serious inflation risk even as growth slows. Pairs with the consumer sentiment item filed today and the 3 November NAB profit item.')

R('2026-11-10-oil-slide-reaches-petrol-bowser',3,'Oil\'s slide starts to reach the bowser, slowly','2026-11-10','news',['ABC News','Reuters','Australian Institute of Petroleum'],
 'Shows oil supply, inelastic demand and how long cost falls take to reach petrol prices. Replaces the 9 November oil item.',
 'Brent crude fell about 16% last week, its steepest weekly drop since COVID hit, after President Trump signalled a pause in strikes on Iran, and was about US$93 a barrel on 10 November. Australian petrol prices are only starting to follow: the national average unleaded fell 2.9c to 234.5c a litre, well above its 12-month average of 196.4c.',
 ['3C.3','3C.4'],['Y1c.4','Y1a.13','Y3e.3'],['P2h.4'],['1A.1','4E.3'],['Y1c.7','Y2d.2'],['P2g.1'],
 ['inflation','global'],['micro'],['ds','adas'],
 [F('Brent crude, week to Friday','about -16% (previous week US$111.9)','week to 6 November 2026','global','Reuters via Business Standard'),F('Brent crude','about US$93 a barrel (30 October high US$118)','10 November 2026','global','ABC News'),F('National average unleaded petrol','234.5c a litre (-2.9c; 12-month average 196.4c)','10 November 2026','inflation','AIP via ABC News'),F('OPEC output rise in October','1.38 million barrels a day','October 2026','global','Reuters survey'),F('Market surplus estimated by JPMorgan','about 1.4 million barrels a day','2026','global','JPMorgan via Reuters')],
 [T('Price inelastic demand','Quantity barely responds to price, so supply shifts cause big price swings.'),T('Pass-through','How quickly cost changes reach retail prices.')],
 [['ABC News, Global oil prices have dropped. Here\'s what that means for drivers','https://abc.net.au/news/2026-11-10/fuel-update-oil-prices-drop-midterms-iran-ukraine/107364786'],['Business Standard (Reuters), Oil prices fall as Trump signals pause in military action against Iran','https://www.business-standard.com/amp/markets/commodities/oil-prices-fall-as-trump-signals-pause-in-military-action-against-iran-126111000067_1.html'],BLOG10],
 'More OPEC supply and a smaller war-risk premium shift crude supply right; because short-run demand for oil is inelastic, modest supply changes produce large price swings. On an AD/AS diagram cheaper oil shifts SRAS right, lowering inflation and raising output, the reverse of a supply shock. Cuts should reach capital cities in days but regional areas in weeks.',
 [Q('Explain why petrol prices in regional areas may take longer to fall than prices in capital cities.',3)],
 'Replaces the 9 November item (Brent Friday close US$98.32, WTI about US$88, global oil surplus 1.1-1.4 million barrels a day, about 20% of oil and LNG shipments passing through Hormuz before the war began on 28 February). That item reported Qatar-brokered terms, unconfirmed by either government: Iran reopening the strait while the US lifts its blockade and releases about US$8 billion of frozen funds; Rubio played down a breakthrough. This digest says the US blockade in the Strait of Hormuz continues, and an expert says prices in the US$90s are the "new normal". City averages in the digest bar chart run from Adelaide A$2.25 to Darwin A$2.65. UPDATE DUE: Hormuz outcome.')

R('2026-11-11-wage-growth-slows-cba',3,'Wage growth cools to its slowest pace this year','2026-11-11','stats',['CommBank'],
 'Wage growth below inflation means falling real wages, with no sign yet of a wage-price spiral; includes a Phillips curve diagram.',
 'CommBank\'s monthly measure of wage growth slowed to 3.1% (annualised) in October, down from 3.5% in August, and annual wage growth was 3.2%. CBA says there is no sign yet that higher inflation is feeding into a wage-price spiral, and expects unemployment to peak at 5.1% by the end of 2027.',
 ['3B.4','3C.3','3E.2'],['Y1c.7','Y1b.11','Y2e.1'],['P3d.1'],['3B.2','3E.3'],['Y1d.5','Y2e.7'],['P1b.2'],
 ['employment','inflation','inequality'],['labour','monetary'],['phillips','chart'],
 [F('CBA monthly wage growth, annualised','3.1% (August 3.5%; 3.2-3.3% held January-July)','October 2026','employment','CommBank'),F('Annual wage growth','3.2%','October 2026','employment','CommBank'),F('Fair Work award rise described as "short and sharp"','4.75%','2026','employment','CommBank'),F('Jobs added','about 18,000','October 2026','employment','CommBank'),F('Unemployment rate / CBA forecast peak','4.7% (September) / 5.1% by end-2027','2026-2027','employment','CommBank'),F('Annual wage growth by state: SA / WA / NT / Tas / Vic','3.8% / 3.7% / 3.7% / 3.5% / 2.9%','October 2026','employment','CommBank')],
 [T('Nominal wages','Pay in dollars.'),T('Real wages','Nominal wage growth minus inflation (about 3.2% - 4.3%, which is negative now).'),T('Wage-price spiral','Higher prices lead to higher wages, which lead to higher prices.')],
 [['CommBank, Monthly wage growth slows to weakest pace seen this year','https://www.commbank.com.au/articles/newsroom/2026/11/monthly-wage-growth-slows-october.html']],
 'With inflation at 4.3% and wages growing about 3.2%, real wages are falling, which squeezes household spending and affects the distribution of income. A softer labour market moves the economy along the short-run Phillips curve: unemployment rises and wage and price pressure eases, which is what the RBA\'s rate rises aim for, at the cost of jobs.',
 [Q('Distinguish between nominal and real wage growth, and explain what it means for households when inflation is 4.3%.',3)],
 'This is CBA account data, not the ABS Wage Price Index, so treat it as an early signal. Victoria has had the slowest wage growth for five months, according to CBA. Jobs growth of about 18,000 is slightly below the pace needed to stop unemployment rising.')

R('2026-11-10-qantas-offshores-850-jobs',3,'Qantas sends 850 corporate jobs offshore','2026-11-10','news',['ABC News'],
 'A current case of offshoring services: winners, losers and structural unemployment.',
 'Qantas will cut about 850 corporate roles over the next few years under an outsourcing deal with Accenture, with most of the work moving to India. Its shares rose about 5.6% on the news, and Coles announced a similar plan in August to move up to 1,000 roles to India via Accenture.',
 ['3B.3','1A.7','1A.3'],['Y1b.5','Y1b.6','Y1b.11'],[],['1D.6','3B.5','4F.2'],['Y2e.7','Y3e.3','Y1a.10'],[],
 ['employment','global','productivity'],['labour','global'],['ds','compare'],
 [F('Qantas corporate roles to go','about 850','over the next few years','employment','ABC News'),F('First changes due','mid-2027 (finance, procurement, marketing)','mid-2027','employment','ABC News'),F('Qantas share price on the day','+5.6%','10 November 2026','employment','ABC News'),F('Roles Coles plans to move offshore via Accenture (August plan)','up to 1,000','August 2026','employment','ABC News'),F('Qantas annual technology spending','over A$1bn','2026','productivity','ABC News')],
 [T('Offshoring','Moving work to another country to cut costs.'),T('Structural unemployment','Job losses caused by long-term change in the economy, not the business cycle.'),T('Trade in services','Services bought from abroad count as imports.')],
 [['ABC News, Qantas to cut 850 corporate jobs as it moves roles overseas in Accenture deal','https://www.abc.net.au/news/2026-11-10/850-jobs-to-go-from-qantas-as-airline-moves-roles-overseas/107368120'],BLOG10],
 'When firms can buy the same services more cheaply from overseas, demand for local back-office workers falls and wage pressure eases. Winners include shareholders and workers in India; losers include displaced staff, communities and the government through lower tax receipts. It is a case for labour market policies such as retraining and redeployment.',
 [Q('Evaluate the impact on the Australian economy of firms offshoring service jobs.',6)],
 'Qantas says it will redeploy as many staff as possible, and cites more than 1,000 legacy IT applications and a push to move faster on AI. The Australian Services Union opposes the move. Whether the work is structural or cyclical is argued from the digest, not stated by Qantas.')

R('2026-11-11-rba-finished-hiking',4,'Has the RBA finished raising rates?','2026-11-11','news',['RBA','Westpac','Reuters','AMP'],
 'Weighs the effectiveness and limits of monetary policy a week after the November rise, using the transmission mechanism and the weak surveys.',
 'The RBA raised the cash rate to 4.85% on 3 November, an 18-year high and its fifth rise this year, with three of nine members preferring to hold. A week later, weak consumer and business surveys have markets betting that it is done.',
 ['4D.1','4D.2','4D.3','4H.1'],['Y2c.4','Y2c.5','Y2c.7','Y2c.8'],['P4c.3'],['3C.3','4I.1'],['Y2c.3','Y2g.1'],['P4c.4'],
 ['rates','inflation','growth'],['monetary'],['adas','flow'],
 [F('RBA cash rate target','4.85% (18-year high; fifth rise since February; three members preferred to hold)','3 November 2026','rates','RBA'),F('Market chance rates have peaked','82%','10 November 2026','rates','Reuters via Business Recorder'),F('Next RBA board meeting','7-8 December 2026 (Westpac expects a pause)','December 2026','rates','Westpac')],
 [T('Contractionary policy','Higher rates to slow demand and inflation.'),T('Time lags','Rate changes take many months to affect spending and prices.')],
 [['RBA, Media conference, monetary policy decision, 3 Nov 2026','https://rba.gov.au/speeches/2026/mc-gov-2026-11-03.html'],INV,BR],
 'Higher rates raise mortgage and business loan rates, shifting AD left: the price level falls or rises more slowly but real output also falls. Bullock pointed to excess domestic demand, capacity pressures, weak productivity and the data-centre investment boom, and said monetary policy cannot change oil prices. Policy works with long lags, so the RBA risks overshooting.',
 [Q('Using evidence from November 2026, assess the effectiveness of monetary policy in reducing inflation in Australia.',6)],
 'A synthesis of the RBA decision, Westpac, Reuters and AMP, with the weak surveys read as early signs the rises are working (AMP). The 82% figure is a market-implied probability, not an RBA forecast. UPDATE DUE: the 7-8 December RBA meeting.')

R('2026-11-09-rba-ai-boom-higher-rates',4,'RBA: the AI boom could keep interest rates higher for longer','2026-11-09','news',['Sydney Morning Herald'],
 'Explains how a global AI investment boom lifts interest rates and inflation now, while any productivity gain comes later (the J-curve).',
 'RBA chief economist Sarah Hunter told a UBS conference that the global rush to invest in AI and data centres may keep interest rates higher, that productivity gains are likely to come later, and that the technology has so far had little effect on overall jobs. Data-centre investment is up tenfold in three years and the RBA expects $115 billion of it by 2028.',
 ['4D.2','3A.6','4E.1'],['Y2c.4','Y1a.10','Y1a.13','Y2d.1'],['P4c.5'],['3A.1','4H.1','3E.4'],['Y1d.5','Y3b.1','Y2c.7'],['P4c.4'],
 ['investment','productivity','rates','inequality'],['monetary','micro'],['adas','flow'],
 [F('Expected data-centre investment by 2028 (excluding energy infrastructure)','$115 billion (about 2% of GDP a year)','by 2028','investment','RBA via SMH'),F('RBA forecast for business investment growth this year','12% (May forecast 0.8%)','2026','investment','RBA via SMH'),F('Rise in data-centre investment over three years','tenfold','three years to 2026','investment','RBA via SMH'),F('Share of households\' roughly $9 trillion of financial wealth in AI-related companies','5.3% (about 2% in late 2022)','2026','inequality','RBA via SMH')],
 [T('Neutral interest rate','The rate that neither stimulates nor restrains the economy.'),T('General-purpose technology','An innovation, like electricity, that transforms many industries.'),T('Productivity J-curve','Productivity dips or stalls before rising as firms adapt.')],
 [['Shane Wright, Sydney Morning Herald, The Reserve Bank says AI could supercharge your workplace. Right now, it\'s inflating cost of living, 9 Nov 2026 (article address not given; link goes to the SMH home page)','https://www.smh.com.au/']],
 'The same investment is inflationary now and potentially disinflationary later. In the short run data-centre construction shifts AD right against fixed capacity (LRAS1), lifting the price level so the RBA keeps rates higher; in the long run, if AI lifts productivity, LRAS shifts right and output can grow with less inflation pressure. Firms worldwide compete for scarce savings, so the RBA\'s neutral rate estimate has risen, as in the late-1990s internet boom.',
 [Q('Explain how a surge in data-centre investment could affect inflation and interest rates in Australia in the short run and the long run.',4)],
 'Reported speech from an RBA speech to a conference. RBA business contacts do not expect AI to cut headcount in the next year, but hiring of young workers in AI-exposed jobs is lower. Data centres compete with construction for tradies, and their power demand may lift wholesale electricity prices for a time. Pairs with the 9 November AI household-wealth item and the Hunter item from 26 October.')

R('2026-11-11-stubborn-inflation-limits-monetary-policy',4,'Why Australia\'s inflation is so stubborn, and why rates can\'t fix it alone','2026-11-11','news',['The Conversation','Australian Catholic University'],
 'Compares Australia with the US, UK and Canada and argues inflation is now mainly a supply-constraint problem that monetary policy can only partly address.',
 'Underlying inflation in Australia is stuck around 3.5-3.6%, while in the US, UK and Canada it has fallen towards 2-2.5%. Finance academic Jak Kakhkharov argues the cause is now mainly supply constraints, such as housing, energy and skilled labour shortages, which interest rates can only partly address.',
 ['3C.3','4D.3','4H.1','S4.7'],['Y1c.4','Y2c.7','Y2c.8','Y2d.1'],[],['1A.1','4E.2','4C.1'],['Y2g.1','Y2g.2','Y2b.13'],[],
 ['inflation','rates','productivity','housing'],['monetary','micro','fiscal'],['adas','chart'],
 [F('Australia\'s trimmed mean inflation (US, UK, Canada about 2-2.5%)','3.5-3.6%','November 2026','inflation','The Conversation (Jak Kakhkharov)'),F('RBA rate rises in 2026 against one rise in the past two years in each of the US and UK','5','2026','rates','The Conversation (Jak Kakhkharov)'),F('Policy rates: RBA / Bank of England / US Fed / Bank of Canada','4.85% / 4.00% / 3.75-4.00% / 2.50%','November 2026','rates','The Conversation, using BIS data'),F('When the RBA expects inflation back in its 2-3% band','late 2027','2027','inflation','RBA via The Conversation')],
 [T('Trimmed mean','The RBA\'s preferred underlying inflation measure.'),T('Supply constraint','Costs or shortages that stop output keeping up with demand.'),T('Cost-push inflation','Prices rise because production costs rise.')],
 [TC('Inflation is proving more stubborn in Australia than elsewhere, making the RBA\'s job harder, Jak Kakhkharov, 11 Nov 2026')],
 'Shortages and higher input costs shift SRAS left, raising prices and cutting output. Rate rises work on demand, lowering the price level but cutting output further and raising unemployment. Rates cannot build houses, generate electricity or train workers, so supply-side (microeconomic) reform and fiscal restraint are needed alongside them. Most Australian home loans are variable, so rate rises hit households faster than where fixed rates dominate.',
 [Q('Discuss the limitations of monetary policy in reducing inflation caused by supply constraints, and identify other policies that could help.',6)],
 'An academic\'s argument. Australia has not always had the highest headline inflation (the UK and US were higher at times in 2025) but its inflation has been more persistent. The Fed rate bar is drawn at the midpoint of its target range. Some economists also blame high government spending, as reported. See the Burshtein opinion item filed today for the opposing demand-side argument.')

R('2026-11-10-burshtein-blame-canberra-rba-not-oil',4,'Opinion: "Blame Canberra and the RBA, not oil, for inflation"','2026-11-10','news',['Australian Financial Review (opinion)'],
 'The demand-side case that government spending and early rate cuts, not oil, caused inflation, with the critics\' replies to weigh it against.',
 'In the AFR, economist Dimitri Burshtein (Eminence Advisory) argues that the oil shock is a convenient excuse: underlying inflation has been rising since mid-2025, before the Strait of Hormuz was closed in late February 2026. He blames heavy government spending, made worse by an RBA that cut rates too early in 2025.',
 ['3C.3','4D.1','4C.1','4B.1'],['Y1c.4','Y2b.3','Y2b.14','Y2c.7'],[],['4H.3','4I.1','4G.2'],['Y2g.1','Y2c.8','Y2b.13'],[],
 ['inflation','budget','rates'],['fiscal','monetary','micro'],['adas','compare'],
 [F('Underlying (trimmed mean) inflation / headline','3.6% / 4.3%','2026','inflation','AFR (Dimitri Burshtein)'),F('Cash rate','4.85% after the fifth rise in 2026 (three cuts in 2025 to 3.6%)','2026','rates','AFR (Dimitri Burshtein)'),F('Broad money growth, year to June 2026 / by September / "needed" rate','8% / 6.2% / about 4.6%','2026','inflation','AFR (Dimitri Burshtein)'),F('Federal spending as a share of GDP','26.9% in 2025-26 (24.3% in 2022-23)','2025-26','budget','AFR (Dimitri Burshtein)'),F('Author\'s measure of the real cash rate','about 1.25% (4.85% - 3.6%)','2026','rates','AFR (Dimitri Burshtein)')],
 [T('Underlying (trimmed mean) inflation','Inflation with the most extreme price moves removed.'),T('Broad money','The RBA\'s widest measure of the money supply.'),T('Real cash rate','The cash rate minus inflation.')],
 [['Dimitri Burshtein, AFR (opinion), That \'recession feeling\' is caused by Canberra and the RBA, 10 Nov 2026 (article address not given; link goes to the AFR home page)','https://www.afr.com/']],
 'His argument is about demand: spending, cost-of-living payments and cheap credit push AD right, a demand-pull inflation that persists however oil moves, while oil is a supply (SRAS) shift. Critics would say the RBA sets interest rates, not money, the money-to-prices link is loose when velocity is unstable, private demand such as the data-centre boom matters, and oil feeds into second-round costs and expectations.',
 [Q('Evaluate the claim that Australia\'s high inflation in 2026 is caused mainly by government policy rather than global oil prices.',6)],
 'An opinion piece, so treat it as an argument, not evidence. The "needed money growth" figure (2.5% inflation plus 2.1% real growth) uses Friedman\'s quantity theory and is the author\'s calculation. On Warren Hogan\'s benchmark policy is restrictive only above a real rate of about 2%. The 24.3% and 26.9% spending figures also appear in the 5 November items. Credit growth of 8.4% and public demand of about 28.5% of GDP against a 23.5% pre-COVID average are the author\'s claims.')

R('2026-11-10-accc-dodgy-discounts-asic-private-credit',4,'Regulators target dodgy discounts and opaque private credit','2026-11-10','news',['ABC News'],
 'Information asymmetry as a market failure, and how the ACCC and ASIC use competition and financial regulation to fix it.',
 'With Black Friday to Cyber Monday spending forecast to hit a record A$7.2 billion, the ACCC is watching for fake "discounts". Separately, ASIC\'s second review of the A$250 billion private credit sector found poor disclosure to investors and firms resisting its instructions.',
 ['4E.3','4G.1','4E.2'],['Y2d.2','Y2d.5','Y2d.1'],['P2h.7','P5a.5'],['4E.1'],['Y2d.6'],['P2g.1','P5a.1'],
 ['productivity','investment'],['micro'],['ds','compare'],
 [F('Forecast Black Friday to Cyber Monday spending (27-30 November)','A$7.2 billion (+5.5%)','November 2026','growth','ABC News'),F('Average planned spend per shopper','A$920 (+14.4%)','November 2026','growth','ABC News'),F('Combined fines on six retailers for misleading discounts, over two years','A$217,800','2024-2026','productivity','ABC News'),F('Size of the private credit sector','A$250 billion','2026','investment','ASIC via ABC News')],
 [T('Information asymmetry','One side of a deal (the seller) knows more than the other.'),T('ACCC','The regulator that enforces competition and consumer law.'),T('ASIC','The regulator of financial markets and products.')],
 [['ABC News, Pre-Christmas shoppers warned of dodgy discounts in Black Friday sales','https://www.abc.net.au/news/2026-11-10/shoppers-warned-dodgy-discounts-black-friday-sales/107365588'],['ABC News, ASIC slams $250 billion private credit sector','https://www.abc.net.au/news/2026-11-10/asic-slam-250-billion-dollar-private-credit-sector/107365226'],BLOG10],
 'A fake "was" price inflates demand from D1 to D2, so consumers buy more at a higher price than they would with accurate information and resources go to goods people would not have chosen. Consumer law aims to keep demand at D1 by keeping price claims honest. Competition and consumer protection is part of microeconomic reform that improves allocative efficiency.',
 [Q('Explain how regulators such as the ACCC can improve the efficiency of markets.',3)],
 'The spending forecast is a forecast by the source cited. The digest draws on two separate ABC stories. Follows the ACCC Armaguard item filed on 5 November.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
