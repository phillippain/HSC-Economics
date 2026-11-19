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
      angle=angle,questions=questions,note=note,added='2026-11-20'))


ABC='ABC News'
def L(a,b): return [a,b]

R('2026-11-18-super-investment-rules-loosened-chalmers','4','Chalmers loosens the rules on where super funds can invest','2026-11-18','news',[ABC,'The Nightly (opinion)'],
 "Shows a structural reform that frees part of super from the performance test to back housing and renewables, with a returns-versus-steering trade-off.",
 "The Treasurer announced changes to superannuation investment rules at a conference in Melbourne on 18 November. Media reports say about 5% of fund investments would be exempt from APRA's annual performance test, giving funds more room to invest in subsidised housing and renewable energy.",
 ['4E.1','4E.2','3A.6'],['Y2d.1','Y2d.2','Y2d.6'],['P4a.3','P4a.1','P4a.2'],
 ['2A.2','3E.4','4I.1'],['Y2d.4','Y2d.5'],['P3c.4'],
 ['investment','housing','productivity'],['micro'],['flow','compare'],
 [F('Share of fund investments exempt from the performance test (reported)','About 5% (about $170 billion of roughly $3.4 trillion APRA-regulated super)','November 2026','investment','The Nightly (opinion), citing AFR reporting'),
  F('Performance test consequence','Funds that fail twice in a row must tell members to consider moving their money','November 2026','investment','APRA, via digest')],
 [T('Performance test','APRA\'s annual check comparing each super fund\'s returns against a benchmark.'),T('Structural reform','A policy that changes how markets and institutions work to lift efficiency or productivity.')],
 [L('ABC News: Federal politics live blog, 19 Nov 2026','https://www.abc.net.au/news/'),L('The Nightly: Chalmers\' changes will allow superannuation to be invested in subsidised housing and wind and solar farms (opinion), 17 Nov 2026','https://www.thenightly.com.au/')],
 "Possible benefits: more capital for housing supply and wind and solar, long-term investment that suits retirement savings. Possible risks: lower or riskier member returns, less pressure on poorly performing funds and government steering of private savings. Shadow Treasurer Tim Wilson revived the idea of first home buyers using super; Chalmers said the Coalition wanted a 'wrecking ball' for super.",
 [Q("Discuss the possible economic benefits and costs of encouraging super funds to invest more in housing and renewable energy.",6)],
 "DETAIL IS UNOFFICIAL: the figures come from media reporting (an opinion column citing AFR); the government has not released the official rules or a start date. Replaces the earlier ABC-based card on the same proposal (filed 18 November) (Treasurer's estimate that it could unlock up to $90 billion; up to 5% of a portfolio in 'emerging assets' judged against an inflation-plus-premium benchmark set on Government Actuary advice; voluntary; best-interests duty unchanged; members in underperforming funds fell from about 1 million in 2021 to about 8,500 in 2025; super savings almost $5 trillion). The $90 billion (unlocked) and $170 billion (exempt) are different measures; and the announcement is dated 17 November in the ABC card and 18 November here, so check the source.")

R('2026-11-19-labor-presses-coalition-gas-reservation','4','Labor presses the Coalition to back domestic gas reservation','2026-11-19','news',[ABC],
 "Gives the political contest over the gas reservation scheme and a supply and demand view of who gains and loses.",
 "The government is pressing the Coalition to support its gas reservation scheme, which would require producers to set aside at least 20% of their output for Australian users rather than exporting it. Acting Prime Minister Richard Marles urged Coalition support while Shadow Resources Minister Susan McDonald said gas is selling at about $10.",
 ['4E.1','4E.2'],['Y2d.1','Y2d.4'],['P2i.2','P2i.3','P2i.4'],
 ['4H.3','2A.1'],['Y2d.6'],['P5a.5'],
 ['investment','inflation'],['micro'],['ds','compare'],
 [F('Share of output to be reserved for domestic users','At least 20%','19 November 2026','investment','ABC News'),
  F('Gas price cited by the Coalition','About $10 a gigajoule','19 November 2026','inflation','ABC News')],
 [T('Gas reservation','A requirement that a share of gas production be sold in the domestic market.'),T('Market intervention','Government action that changes how a market allocates resources.')],
 [L('ABC News: Federal politics live blog (Marles; McDonald), 19 Nov 2026','https://www.abc.net.au/news/')],
 "Reserving gas shifts domestic supply right, lowering the domestic price and raising quantity used, which helps households and manufacturers. Costs: producers earn less than at export prices, export income and the current account may fall, and long-run investment in new fields may be lower. Weigh these in a 6-mark assess question.",
 [Q("Assess the likely impact of a domestic gas reservation scheme on Australia's energy market and its export income.",6)],
 "UPDATE DUE: the Senate vote. The $10 figure is described as 'about' and the unit (per gigajoule) is the digest's. Kept alongside the 18 November opinion card on the WA carve-out, which has the investment and sovereign risk detail (WA permanently at 0%, Hancock's $2 billion project paused).")

R('2026-11-19-jobs-shock-december-rate-rise-off-the-table','4','Jobs shock takes a December rate rise off the table','2026-11-19','news',['RBA',ABC,'CommBank','Newsquawk'],
 "Shows the RBA's policy dilemma after October's jobs data, with its inflation forecasts, NAIRU estimate and time lags.",
 "The RBA raised the cash rate to 4.85% on 3 November, its fifth rise of 2026, in a split 6-3 vote. After October's jobs data, economists now expect it to hold rates until at least February; Moody's said the data 'all but closes the door' on a December rise.",
 ['4D.1','4D.2','4D.3','4H.1'],['Y2c.4','Y2c.7','Y2c.8','Y1c.6'],['P4c.3'],
 ['3B.4','3C.2','3C.1'],['Y1c.3','Y2c.3'],['P4c.4'],
 ['rates','inflation','employment'],['monetary'],['phillips','flow'],
 [F('RBA cash rate','4.85% (+25 basis points on 3 November; highest since 2008; board vote 6-3)','3 November 2026','rates','RBA'),
  F('RBA headline inflation forecast','Peak 4.5% in the December quarter; above 3% until late 2027; 2.5% by mid-2028','November 2026','inflation','RBA, Statement on Monetary Policy'),
  F('Inflation, year to September','Headline 3.9%; trimmed mean 3.7%','September 2026','inflation','ABS, via digest'),
  F('Unemployment rate / RBA NAIRU estimate','4.9% / about 4.75% (raised)','November 2026','employment','RBA; ABC News'),
  F('Next RBA meeting','7-8 December 2026 (CommBank expects a hold)','November 2026','rates','CommBank')],
 [T('NAIRU','The unemployment rate consistent with stable inflation; the RBA raised its estimate to about 4.75%.'),T('Cash rate','The interest rate on overnight loans between banks, which the RBA sets.')],
 [L('RBA: Statement on Monetary Policy, November 2026','https://www.rba.gov.au/'),L('ABC News: Unemployment rate surges to 4.9pc, 19 Nov 2026','https://www.abc.net.au/news/'),L('CommBank: RBA pause increasingly likely, 17 Nov 2026','https://www.commbank.com.au/'),L('investinglive: RBA lifts cash rate to 4.85% in split 6-3 vote','https://investinglive.com/'),L('Newsquawk: Bullock headlines, 17 Nov 2026','https://newsquawk.com/')],
 "Rate rises move the economy along the short-run Phillips curve: inflation eases but unemployment rises. With inflation still well above target and unemployment at 4.9%, the board must weigh the cost of any further rise. Monetary policy works with long and variable lags, so earlier 2026 rises are still flowing through (a key limitation). Bullock said inflation risks are still tilted upward.",
 [Q("Assess the policy dilemma facing the RBA when inflation is around 3.9% and unemployment has risen to 4.9%.",6)],
 "Replaces the earlier 19 November card 'Rate hike bets vanish as rising unemployment changes the RBA outlook' (markets removed all bets on a December hike and expected at least one cut, possibly two, by Christmas 2027; the RBA says unemployment of about 4.5-5% may be needed to return inflation to target; Governor Bullock says the RBA does not intend to cause a recession; cash rate from 3.6% at the start of 2026). Forecasts and market pricing are not RBA decisions: UPDATE DUE after 8 December (the RBA's final 2026 meeting). CAUTION: this card gives headline inflation of 3.9% for the year to September; other cards use 4.3%, so check the measure and period before quoting.")

R('2026-11-19-economists-warn-edging-towards-recession','3','Economists warn Australia is edging towards recession','2026-11-19','news',[ABC,'AAP'],
 "Gives economists' recession-risk estimates after the jobs shock and introduces the Sahm rule.",
 "After October's jobs shock, leading economists warned the risk of recession is rising. AMP's Shane Oliver puts it at 'around 40 per cent' and BetaShares' David Bassanese says the economy may already have 'one foot in recession'.",
 ['3A.7','3B.2','3B.3'],['Y1a.5','Y1a.12','Y1b.11'],['P1e.4','P1e.5','P1e.7'],
 ['3A.4','4H.1'],['Y1a.8','Y2c.8'],['P1e.6'],
 ['growth','employment'],['monetary'],['adas','flow'],
 [F('Recession risk (AMP, Shane Oliver)','Around 40%','19 November 2026','growth','AAP'),
  F('Unemployment rate','4.9% in October; Eslake: 5% could come by early 2027, not 2028 as the RBA forecasts','19 November 2026','employment','ABC News; AAP'),
  F('RBA rate rises in 2026','5','2026','rates','ABC News')],
 [T('Sahm rule','A recession signal triggered when the 3-month average unemployment rate rises 0.5 points above its low of the past year.'),T('Recession','Commonly defined as two consecutive quarters of negative real GDP growth.')],
 [L('ABC News: Unemployment rate surges to 4.9pc in October, 19 Nov 2026','https://www.abc.net.au/news/'),L('AAP via Yahoo News: Risk is high: recession warning after jobless spike, 19 Nov 2026','https://au.news.yahoo.com/')],
 "Higher rates and weak confidence cut consumption and investment, shifting AD left, lowering output and raising cyclical unemployment. GDP data come after jobs data, so the labour market can signal a slowdown first. Big job cuts at NAB, David Jones and General Pants are not yet in the official data (AAP).",
 [Q("Explain how a fall in aggregate demand could lead to a recession and higher unemployment in Australia.",5)],
 "FORECASTS and views of individual economists, not an official call that a recession has begun. UPDATE DUE: September-quarter GDP on 2 December. Filed alongside the 19 November ABC analysis 'Quacking like a recession' (different quotes and figures: HSBC's Bloxham, 750,000 job seekers, Westpac forecasts).")

R('2026-11-19-unemployment-jumps-4-9-43500-jobs-lost','3','Unemployment jumps to 4.9% as 43,500 jobs are lost','2026-11-19','stats',['ABS','ABC News'],
 "Gives the October Labour Force result against market expectations and explains why unemployment rose by less than jobs fell.",
 "The ABS Labour Force survey showed unemployment rising from 4.7% in September to 4.9% in October, the highest since 2021, while markets had expected no change and about 25,000 new jobs. Employment fell 43,500, almost all in part-time work.",
 ['3B.1','3B.2','3B.3','3B.6'],['Y1b.1','Y1b.3','Y1b.7','Y1b.11','Y1b.12'],['P1e.7','P3d.3'],
 ['3A.7','4D.3'],['Y1b.5','Y1b.8','Y1b.10'],['P3b.1'],
 ['employment'],['monetary'],['chart','flow'],
 [F('Unemployment rate, seasonally adjusted','4.9% (September 4.7%; trend 4.8%)','October 2026','employment','ABS Labour Force'),
  F('Change in employment','-43,500 (part-time -40,600; full-time -2,900); market expected about +25,000','October 2026','employment','ABS Labour Force'),
  F('Number unemployed','753,700 (+17,800)','October 2026','employment','ABS Labour Force'),
  F('Participation rate','66.6% (-0.2 points); hours worked -0.2%','October 2026','employment','ABS Labour Force'),
  F('Youth unemployment / underemployment','11.3% / 6.2% (eased slightly)','October 2026','employment','ABS Labour Force'),
  F('RBA unemployment forecast, end-2028','5.1%','November 2026','employment','RBA')],
 [T('Participation rate','The labour force (employed plus unemployed) as a share of the working-age population.'),T('Cyclical unemployment','Unemployment caused by a downturn in the business cycle.')],
 [L('ABS: Labour Force, Australia, October 2026','https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/'),L('ABC News: Unemployment rate surges to 4.9pc in October, taking analysts by surprise, 19 Nov 2026','https://www.abc.net.au/news/'),L('investinglive: Australian jobs report preview, 18 Nov 2026','https://investinglive.com/')],
 "Unemployment rose by only 17,800 while 43,500 jobs disappeared because many people left the labour force, so participation fell; people who stop looking are not counted as unemployed ('hidden unemployment'), so 4.9% may understate the weakening. Quote both the unemployment rate and the participation rate. Five rate rises slow household spending, firms cut hours and part-time staff, and cyclical unemployment rises.",
 [Q("Explain why the unemployment rate rose by only 0.2 percentage points even though 43,500 jobs were lost in October.",3)],
 "Replaces the earlier 19 November card 'Unemployment rises to 4.9%, the highest since 2021' (same ABS release; it also gave unemployed +14.5% on a year ago, employment 14.74 million, employment-to-population ratio 63.3%, September youth rate 11.1% against a post-COVID average of 9.2%, and the next release on 17 December 2026). The ABS trend rate (4.8%) is the best guide to underlying conditions.")

R('2026-11-19-aud-slides-towards-67-cents-sixth-day','2','Australian dollar slides towards 67 US cents','2026-11-19','news',[ABC,'Saxo Markets'],
 "Shows two causes of an AUD depreciation, commodity prices and a narrowing US rate gap, and its effects.",
 "The Australian dollar fell for a sixth straight day to about 67 US cents. Commodity prices are weaker, US interest rates look set to rise further, and Thursday's jobs data reduced the chance of more RBA rate rises.",
 ['2C.2','2C.3','2C.6','2B.4'],['Y3c.2','Y3c.4','Y3c.5','Y3c.6'],['P6c.1'],
 ['3D.1','4D.3'],['Y1a.7','Y2c.5'],['P6a.2'],
 ['fx','trade','rates'],['monetary'],['fx','flow'],
 [F('AUD / USD','US67.12c early Thursday (-0.3%); sixth straight daily fall to Tuesday','19 November 2026','fx','ABC News; Saxo Markets'),
  F('Iron ore / gold','US$88.05 a tonne (-1.2%) / US$3,724 an ounce (-3.3%)','19 November 2026','trade','ABC News'),
  F('10-year bond yield: Australia / US','5.09% / 5.07%','19 November 2026','rates','ABC News')],
 [T('Depreciation','A fall in the value of the AUD against other currencies when the market sets the rate.'),T('Terms of trade','The ratio of export prices to import prices.')],
 [L('ABC News: ASX and business live blog, 19 Nov 2026','https://www.abc.net.au/news/'),L('Saxo: Asia Market Quick Take, 18 Nov 2026','https://www.home.saxo/'),L('ABC News: Unemployment rate surges to 4.9pc, 19 Nov 2026','https://www.abc.net.au/news/')],
 "Lower commodity prices mean foreign buyers need fewer AUD, and a smaller interest rate gap with the US makes Australian assets less attractive, so demand shifts left and the AUD depreciates. A lower AUD cheapens exports and improves international competitiveness but raises import prices, adding to inflation. The dollar kept falling even though Governor Bullock sounded hawkish.",
 [Q("Discuss two factors behind the recent depreciation of the AUD and one likely effect on the Australian economy.",5)],
 "Replaces the 18 November card 'Aussie dollar slips to 67 US cents as commodities and shares fall' (AUD US67.18c, -0.19%; iron ore US$89.85 a tonne, +0.16%; Brent US$92.50 a barrel, -0.69%; gold US$3,788, -1.6%; ASX 200 -0.69% to 8,821.8, Dow -1.6%, S&P 500 -1%; cash rate 4.85%). Single-day market prices that move daily.")

R('2026-11-19-beef-tariffs-albanese-xi-apec','2','Beef tariffs on the table as Albanese meets Xi at APEC','2026-11-19','news',['AAP',ABC],
 "Gives a current example of another country's tariff-rate quota on an Australian export, with the tariff diagram and trade-relationship context.",
 "Anthony Albanese meets Xi Jinping in Shenzhen on Friday at the APEC summit, and Australian beef exporters want relief from China's import quota, which triggered an extra 55% tariff once Australia's share was used up.",
 ['1C.2','2D.4','2A.1'],['Y3a.6','Y3a.7','Y3a.8','Y3a.11'],['P6a.2'],
 ['1C.1','2B.4'],['Y3a.15','Y3e.3'],[],
 ['trade'],['trade'],['ds','flow'],
 [F("Australia's 2026 beef quota in China",'205,000 tonnes, used up in June (three-year quota from 2026)','June 2026','trade','AAP'),
  F('Extra tariff on beef above the quota','55%','2026','trade','AAP'),
  F('Beef exports to China at risk each year (AMIC estimate)','About $1 billion','November 2026','trade','Australian Meat Industry Council, via AAP'),
  F('Rabobank expectation for the 2027 quota','Could be used up by May','November 2026','trade','Rabobank, via AAP')],
 [T('Tariff-rate quota','A low tariff applies up to a set volume of imports, and a higher tariff above it.'),T('Safeguard measure','Temporary protection for a domestic industry facing a surge in imports.')],
 [L('Michael West Media (AAP): Tough act to follow: PM\'s Xi meeting overshadowed, 19 Nov 2026','https://www.michaelwest.com.au/'),L('ABC News: Federal politics live blog, 19 Nov 2026','https://www.abc.net.au/news/')],
 "The tariff raises China's domestic beef price, lifts Chinese production, cuts consumption and imports, raises government revenue and creates deadweight losses; Australian exporters lose sales and look for other markets. Protection shifts resources to less efficient producers, reducing global welfare.",
 [Q("Explain the effects of China's beef import quota and tariff on Australian beef producers and on Chinese consumers.",4)],
 "UPDATE DUE: the outcome of the Albanese-Xi meeting (Friday 20 November) and the APEC summit; Acting PM Richard Marles says beef tariffs are a key goal of the trip. The AMIC $1 billion figure is an industry estimate. Related: 18 November Albanese at APEC card.")

R('2026-11-19-oil-holds-above-us90-middle-east-surplus','1','Oil holds above US$90 as Middle East tension offsets surplus fears','2026-11-19','news',['Saxo Markets',ABC,'Newsquawk'],
 "Shows how a supply shock raises oil prices when demand is price-inelastic, and how oil drives cost-push inflation.",
 "Oil prices stayed above US$90 a barrel this week as Middle East flare-ups held prices up, even though some analysts expect a supply glut in 2027. Oil has been a major driver of inflation around the world in 2026, including in Australia.",
 ['3C.3','1A.1','1A.8'],['Y1c.4','Y1c.5','Y3e.3'],['P2c.4','P2d.1','P2d.2'],
 ['2B.4','3F.4'],['Y1a.10','Y1c.8'],['P1e.6'],
 ['inflation','global'],[],['ds','adas','chart'],
 [F('Brent crude','US$93.14 settle on Tuesday; about US$91.59 early Thursday (-1.7% overnight)','19 November 2026','inflation','Saxo Markets; ABC News'),
  F('Goldman Sachs 2027 outlook','Possible surplus of about 2 million barrels a day; Brent averaging US$88','2027 forecast','inflation','Goldman Sachs, via digest'),
  F('US petrol price','Eight-month low of US$3.78 a gallon','November 2026','inflation','digest')],
 [T('Supply shock','A sudden change in supply that shifts the supply curve, such as a war disrupting oil production.'),T('Price-inelastic demand','Quantity demanded changes little when price changes.')],
 [L('Saxo: Asia Market Quick Take, 18 Nov 2026','https://www.home.saxo/'),L('ABC News: ASX and business live blog, 19 Nov 2026','https://www.abc.net.au/news/'),L('Newsquawk: Bullock on inflation risks, 17 Nov 2026','https://newsquawk.com/')],
 "In the short run demand for oil is price-inelastic, so when conflict threatens supply (S shifts left) quantity falls a little but price jumps. On an AD/AS diagram, an oil price rise shifts SRAS left, causing cost-push inflation and slower growth together (stagflation). RBA Governor Bullock flagged the risk that oil prices stay high.",
 [Q("Using an AD/AS diagram, explain how higher world oil prices affect inflation and economic growth in Australia.",6)],
 "Market prices and a 2027 forecast: the Goldman surplus is a forecast, not an outcome. Single-day figures move daily. Related: 10 November oil and the bowser card and 28 October Saudi refinery card. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-19-us-fed-signals-more-rate-rises','1','US Fed signals more rate rises as global shares slide','2026-11-19','news',['Saxo Markets',ABC],
 "Shows how expected US rate rises pull funds away from other currencies and link Australian markets to the US.",
 "St Louis Fed President Alberto Musalem said 'several' rate rises are likely to be needed before spring 2027, and global share markets have fallen. Higher US interest rates draw investment towards the US, putting downward pressure on other currencies including the AUD.",
 ['1A.4','2C.2','4H.2'],['Y3c.4','Y3e.3','Y3b.3'],['P6c.1','P4c.2'],
 ['4D.3','2A.2'],['Y3c.5','Y2c.8'],['P4c.3'],
 ['rates','fx','global'],['monetary','global'],['fx','flow'],
 [F('Fed view (St Louis Fed President Musalem)','"Several" rate rises likely before spring 2027; real policy rate may need to rise about 1 percentage point','18 November 2026','rates','Saxo Markets'),
  F('US import prices, October','+1.1% (expected +0.7%); US retail sales +0.2%','October 2026','inflation','Saxo Markets'),
  F('S&P 500 / Stoxx 600','-1.0% (lowest since July) / -1.8%','18 November 2026','global','Saxo Markets'),
  F('10-year yield: US / Australia','About 5.1% / 5.09%','19 November 2026','rates','ABC News')],
 [T('Real interest rate','The nominal interest rate minus inflation.'),T('Capital flows','Money moving between countries to buy financial assets such as shares and bonds.')],
 [L('Saxo: Asia Market Quick Take, 18 Nov 2026','https://www.home.saxo/'),L('ABC News: ASX and business live blog, 19 Nov 2026','https://www.abc.net.au/news/')],
 "When US rates rise relative to Australia's, investors switch funds into US assets, demand for AUD falls and the AUD depreciates: a key channel linking the global economy to Australia's exchange rate through the financial account. Weak Australian jobs data makes further RBA rises less likely, which could widen the rate gap with the US.",
 [Q("Explain how rising US interest rates could affect Australia's exchange rate and financial account.",4)],
 "One Fed official's view, not a Fed decision. Replaces the 13 November card 'US bond yields jump as markets bet on a Fed rate hike' (US 10-year 5.152%, +29.4 basis points on the week, the largest since April 2025; US 2-year 4.872%, +35.2 basis points; about 88% chance of a 0.25 point December Fed hike and 12% for 0.50; Australian 10-year 5.14%; Fed Chair Kevin Warsh due to speak and the Fed's October minutes due 18 November). The 12 November card on hot US inflation is kept. UPDATE DUE: the Fed's December decision.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-18-super-funds-emerging-assets-chalmers','2026-11-19-unemployment-rises-4-9-highest-since-2021','2026-11-18-aud-iron-ore-slip-wall-st','2026-11-19-rba-hike-bets-vanish-unemployment-outlook','2026-11-13-us-bond-yields-jump-fed-hike-bets'}
d=[x for x in d if x['id'] not in REMOVE]
for x in d:
    for key,old,new in [('2026-11-18-labour-market-cooling-job-ads-layoffs','2026-11-19 card','19 November card')]:
        pass
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
