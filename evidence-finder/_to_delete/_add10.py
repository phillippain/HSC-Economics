import json
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-10-26-aud-interest-rate-differential','2026-10-26-september-quarter-cpi-expectations'}
d=[x for x in d if x['id'] not in REMOVE]; have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
def fl(i): return {'path':f'files/2026-10/{i}.pdf','label':'One-page digest','pages':1}
recs=[]
def add(**k): recs.append(k)

i='2026-10-27-china-growth-despite-us-tariffs'
add(id=i,title='China grows 4.5% as exports surge 36.3% despite US tariffs averaging 35%',date='2026-10-27',type='news',outlets=['Fortune'],
 summary='A case of tariffs and trade flows between the two largest economies, with the tariff diagram and a development contrast (GDP per capita of US$15,370 against over US$95,000).',
 lede='China\'s real GDP grew 4.5% over the year to the September quarter and September exports jumped 36.3%, even though about nine in ten Chinese exports to the US face tariffs averaging 35.2%. The source does not say where the extra exports went.',
 about={'h09':['1C.2','1E.1'],'y12':['Y3a.7','Y3a.8'],'y11':[]},also={'h09':['1D.1','1D.9'],'y12':['Y3d.2','Y3a.15'],'y11':[]},
 issues=['trade','growth','global'],levers=['trade','global'],diagrams=['ds'],
 figures=[F('China real GDP growth','4.5% year on year (consensus 4.4%)','September quarter 2026','growth','Fortune'),F('China exports','+36.3% year on year (fastest since February)','September 2026','trade','Fortune'),F('Average US tariff on Chinese goods / Chinese tariff on US goods','35.2% / 31.9%','August 2026','trade','PIIE via Fortune'),F('Chinese exports to the US facing tariffs','88.8%','August 2026','trade','PIIE via Fortune'),F('GDP per capita: China / US','US$15,370 / over US$95,000','2026','growth','IMF via Fortune'),F('Augmented fiscal deficit','9.4% of GDP (12-month average; Goldman estimates 10.0% for 2026)','2026','budget','Goldman Sachs via Fortune')],
 terms=[T('Tariff','A tax on imports, which raises their domestic price.'),T('Augmented deficit','A broad fiscal measure that includes off-budget local government borrowing.')],
 links=[['Fortune, China growth, tariffs and deficit, 26 Oct 2026','https://fortune.com/2026/10/26/trump-china-economy-tariffs-growth-goldman-sachs-deficit/']],
 file=fl(i),angle='The tariff diagram shows imports into the US shrinking, yet China\'s total exports are surging. Check customs data on where tariffed goods are being redirected before claiming an explanation.',
 questions=[Q('Using a diagram, explain the effects of a tariff on consumers, producers and the government in the importing country.',5)],
 note='Complements the 25 October item on China\'s growth and property slump. The flow chart on the digest is a hypothesis for students to test, not a finding.')

i='2026-10-27-us-china-port-fee-truce'
add(id=i,title='The US moves to extend its port-fee truce with China to 9 January',date='2026-10-27',type='news',outlets=['Bloomberg','gCaptain','Splash247'],
 summary='A current example of a non-tariff barrier, retaliation and how a trade dispute raises freight costs for countries outside it.',
 lede='The US Trade Representative has proposed a two-month extension, to 9 January, of the pause on port charges the US and China placed on each other\'s ships. The proposal is in a notice of 26 October and is not yet final.',
 about={'h09':['1C.2'],'y12':['Y3a.6','Y3a.7'],'y11':[]},also={'h09':['1A.6','2D.4'],'y12':['Y3a.15'],'y11':[]},
 issues=['trade','global'],levers=['trade','global'],diagrams=['ds','flow'],
 figures=[F('Proposed extension of the port-fee pause','2 months, to 9 January','USTR notice 26 October 2026','trade','Bloomberg via gCaptain'),F('Wider US-China trade truce announced','September 2026 (Xi\'s first US visit in 11 years)','September 2026','trade','Bloomberg via gCaptain')],
 terms=[T('Non-tariff barrier','A restriction on trade other than a tariff, such as fees, quotas or regulations.'),T('Retaliation','One country answering another\'s protection with its own.')],
 links=[['gCaptain (Bloomberg), US plans two-month extension to shipping fee truce with China','https://gcaptain.com/us-plans-two-month-extension-to-shipping-fee-truce-with-china/'],['Splash247, US moves to extend China ship fee truce into 2027','https://splash247.com/us-moves-to-extend-china-ship-fee-truce-into-2027/']],
 file=fl(i),angle='Port fees work like a tariff on transport, not on the goods themselves, so they raise trade costs for everyone using affected ships, including countries outside the dispute such as Australia.',
 questions=[Q('Explain how port fees on foreign ships act as a form of protection. Outline the likely effects of suspending them on global trade.',4)],
 note='The extension is proposed, not final. The new end date is 9 January (the Splash247 headline places it in 2027). UPDATE DUE: USTR decision before the pause ends in early November.')

i='2026-10-27-aud-interest-rate-differential'
add(id=i,title='The dollar sits near 70 US cents as Australian bond yields stay above US yields (27 October)',date='2026-10-27',type='stats',outlets=['ABC News'],
 summary='Shows the interest rate differential and commodity prices pulling on the Australian dollar, with a demand and supply diagram. Replaces the 26 October edition.',
 lede='The Australian dollar traded at about 70 US cents at Tuesday\'s close. Australia\'s 10-year bond yield was 5.16% against 4.99% in the US, iron ore was soft at US$90.60 and Brent oil stayed near US$115.',
 about={'h09':['2C.4','2C.5'],'y12':['Y3c.1','Y3c.2'],'y11':['P6c.1']},also={'h09':['2C.3','4D.3','2C.6'],'y12':['Y3c.5','Y1a.7'],'y11':[]},
 issues=['fx','rates'],levers=['monetary'],diagrams=['fx','flow'],
 figures=[F('Australian dollar','about US70c','close Tuesday 27 October 2026','fx','ABC News'),F('Australian / US 10-year bond yield','5.16% / 4.99%','27 October 2026','rates','ABC News'),F('Iron ore price','US$90.60 a tonne','27 October 2026','trade','ABC News'),F('Brent crude oil','about US$115 a barrel','27 October 2026','global','ABC News'),F('RBA cash rate / US Fed funds target','4.60% (four rises in 2026) / 3.75-4.00% (hold expected)','27 October 2026','rates','ABC News')],
 terms=[T('Interest rate differential','The gap between Australian and overseas interest rates.'),T('Terms of trade','The index of export prices divided by the index of import prices, multiplied by 100.')],
 links=[['ABC News markets blog, 27 Oct 2026','https://www.abc.net.au/news/2026-10-27/asx-markets-business-live-news-anthropic/107312526'],['ABS, Release calendar','https://www.abs.gov.au/release-calendar/future-releases']],
 file=fl(i),angle='Interest rates are only one influence. Weak iron ore reduces demand for the AUD from buyers of exports and can offset the support from higher yields, which helps explain a high-rate AUD of only about 70 cents.',
 questions=[Q('Explain two factors that influence the value of the Australian dollar. Refer to recent data in your answer.',4)],
 note='A single close, so update before quoting. The ABS releases International Trade Price Indexes on 29 October. Replaces the 26 October edition of this item.')

i='2026-10-28-cpi-day-banks-expect-above-rba'
add(id=i,title='CPI day: banks expect underlying inflation of 0.9 to 1.0%, above the RBA\'s 0.8% forecast',date='2026-10-28',type='news',outlets=['CommBank','InvestingLive','ABS'],
 summary='The bank forecasts for the September quarter CPI, written before the release, with the headline versus underlying distinction and a cost-push diagram. Replaces the 26 October preview.',
 lede='The ABS releases the September quarter CPI at 11:30am on 28 October. All four major banks expect trimmed mean inflation of 0.9 to 1.0% against the RBA\'s 0.8% forecast, and headline CPI of 1.2 to 1.3% for the quarter, about 3.9% for the year.',
 about={'h09':['3C.1','3C.3'],'y12':['Y1c.3','Y1c.4','Y1c.5'],'y11':[]},also={'h09':['4D.2'],'y12':['Y1c.1','Y2c.4'],'y11':[]},
 issues=['inflation','rates'],levers=['monetary'],diagrams=['adas'],
 figures=[F('Expected trimmed mean (CBA, NAB, ANZ / Westpac)','1.0% / 0.9% in the quarter','September quarter 2026 (due 28 October)','inflation','InvestingLive / CommBank'),F('RBA forecast for the trimmed mean','0.8% in the quarter','August 2026','inflation','InvestingLive / CommBank'),F('Expected headline CPI','+1.2% to 1.3% in the quarter, about 3.9% over the year','September quarter 2026 (due 28 October)','inflation','CommBank'),F('Fuel prices (CBA)','+14.8% in August; +9.8% expected in September','2026','inflation','CommBank'),F('Market services inflation (CBA)','4.1% rising to 4.3%','September quarter 2026','inflation','CommBank'),F('New dwelling price inflation (annual, CBA)','5.4% easing to 4.9%; rents about 3.5%','September quarter 2026','housing','CommBank')],
 terms=[T('Trimmed mean','CPI with the largest and smallest price changes removed, used as a measure of underlying inflation.'),T('Cost-push inflation','Higher production costs passed on as higher prices.'),T('Stagflation','Rising inflation combined with weak growth.')],
 links=[['CommBank, September data will keep inflation pressure on RBA','https://www.commbank.com.au/articles/newsroom/2026/10/inflation-cpi-rba-interest-rates-november.html'],['InvestingLive, Australia CPI preview: banks see 1.0% core rise above the RBA\'s 0.8% forecast','https://investinglive.com/news/australia-cpi-preview-banks-see-1-0-core-rise-above-the-rba-s-0-8-forecast/'],['ABS, Consumer Price Index, Australia','https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/consumer-price-index-australia']],
 file=fl(i),angle='Fuel is volatile, so it mostly affects headline CPI. If the trimmed mean also comes in high, inflation is broad-based (second-round effects through market services), which is what the RBA watches most closely.',
 questions=[Q('Distinguish between headline and underlying inflation. Explain why the RBA focuses on underlying measures when setting the cash rate.',4)],
 note='A preview with forecasts, not the result. UPDATE DUE: add the actual September quarter CPI released at 11:30am on 28 October, then the RBA decision on 3 November. Replaces the 26 October expectations item; the earlier 25 October preview from a different source set is still on the site.')

i='2026-10-27-price-gouging-abs-profits'
add(id=i,title='Price gouging? ABS figures point to housing, transport and mining',date='2026-10-27',type='news',outlets=['Katherine Times (ACM)'],
 summary='An opinion column weighing demand-pull, cost-push and profit-push explanations of high prices against ABS data on prices and company profits.',
 lede='Consumer prices have risen almost 30% since 2020 and company gross operating profits by about the same, but the column argues ABS data do not show widespread gouging: housing and transport drove prices and mining accounts for most of the profit rise.',
 about={'h09':['3C.3','4E.3'],'y12':['Y1c.4','Y1c.8'],'y11':['P2g.3']},also={'h09':['3C.4','3C.1'],'y12':['Y2d.2'],'y11':[]},
 issues=['inflation','productivity'],levers=['micro'],diagrams=['adas','compare'],
 figures=[F('Consumer prices','up almost 30%','since 2020','inflation','Katherine Times (ACM) citing ABS'),F('Company gross operating profits','up about 30%','since 2020','inflation','Katherine Times (ACM) citing ABS'),F('Cumulative rise in markups','6% (2003 to 2016, mostly digital firms)','2003-2016','productivity','Hambur study cited by Katherine Times')],
 terms=[T('Markup','The gap between a firm\'s price and its cost of production.'),T('Profit-push inflation','Prices rising because firms widen their margins.')],
 links=[['Katherine Times (ACM), ABS data counters price gouging claims across Australia','https://www.katherinetimes.com.au/story/9380526/abs-data-counters-price-gouging-claims-across-australia/']],
 file=fl(i),angle='Mining profits mostly reflect world commodity prices (the terms of trade), so aggregate profits can look like gouging even when domestic retail margins have barely moved.',
 questions=[Q('Assess the extent to which rising business profits have contributed to inflation in Australia since 2020.',6)],
 note='An opinion column, so treat it as one side of the debate and compare it with ACCC findings. The figures are as cited by the columnist and not checked against the ABS.')

i='2026-10-27-small-business-squeeze'
add(id=i,title='Small businesses squeezed between rising costs and weaker sales',date='2026-10-27',type='news',outlets=['ABC News'],
 summary='Shows how higher fuel costs, interest rates and regulatory changes combine to squeeze small business, with late payments at their worst since 2018.',
 lede='Australia\'s roughly 2.7 million small business owners face higher fuel costs, higher interest rates and slower sales. CreditorWatch says serious arrears reached an 8.5-year high in September, and more than half of invoices were paid late.',
 about={'h09':['3A.7','4D.3'],'y12':['Y1a.14','Y2d.6'],'y11':['P3c.1']},also={'h09':['3B.3'],'y12':['Y2c.5'],'y11':['P1e.7']},
 issues=['growth','employment','rates'],levers=['monetary','micro'],diagrams=['ds','flow'],
 figures=[F('Serious arrears (CreditorWatch)','8.5-year high; more than half of invoices paid late, 1 in 10 over 60 days overdue','September 2026','growth','CreditorWatch via ABC News'),F('Small businesses with lower revenue than a year earlier (MYOB)','38%','2026','growth','MYOB via ABC News'),F('Small businesses worried about cashflow / finding new customers','65% / 69%','2026','growth','MYOB via ABC News'),F('Estimated cost saving from payment reforms (RBA)','$910m a year','2026','productivity','RBA via ABC News')],
 terms=[T('Insolvency','When a business cannot pay its debts as they fall due.'),T('Compliance cost','The time and money spent meeting regulations.')],
 links=[['ABC News, Economic pain collides with regulatory changes for small business','https://www.abc.net.au/news/2026-10-27/economic-pain-collides-with-regulatory-changes-small-business/107286660']],
 file=fl(i),angle='Industry groups say each reform is assessed in a policy silo. The cumulative burden of many small changes at once is a limitation of policy, even when each change has merit alone.',
 questions=[Q('Explain how rising interest rates and higher input costs can affect small businesses and the wider economy.',4)],
 note='Survey and credit-agency figures, not official statistics.')

i='2026-10-27-greens-tax-free-threshold'
add(id=i,title='The Greens pitch a $26,000 tax-free threshold and a matching welfare boost',date='2026-10-27',type='news',outlets=['ABC News'],
 summary='A current proposal on tax design and redistribution, costed by the PBO at $22 billion a year, with a Lorenz curve diagram.',
 lede='Greens leader David Shoebridge would lift the tax-free threshold from $18,200 to $26,000, worth up to $1,092 a year, and add the same amount to income support payments. The PBO puts the cost at $22 billion a year.',
 about={'h09':['3E.3','4C.2'],'y12':['Y2b.10','Y1d.3'],'y11':['P5b.6','P5b.7']},also={'h09':['3E.1'],'y12':['Y1d.9'],'y11':['P5b.1']},
 issues=['inequality','budget'],levers=['fiscal'],diagrams=['chart','compare'],
 figures=[F('Proposed tax-free threshold','$26,000 (from $18,200)','27 October 2026','inequality','ABC News'),F('Maximum gain per year','$1,092 ($21 a week), not means-tested','27 October 2026','inequality','ABC News'),F('PBO cost per year','$22b','27 October 2026','budget','ABC News'),F('Proposed funding: gas export tax / mining royalties','25% (about $17b a year, Australia Institute) / about $28b (ballpark); neither costed by the PBO','27 October 2026','budget','ABC News'),F('Coalition proposed cuts, for comparison','$31.3b over four years','26 October 2026','budget','ABC News')],
 terms=[T('Progressive tax','A tax where the average rate rises with income.'),T('Effective marginal tax rate','The share of an extra dollar earned that is lost to tax and to withdrawn benefits.')],
 links=[['ABC News, Greens leader proposes tax cut and welfare boost','https://abc.net.au/news/2026-10-27/greens-leader-proposes-tax-cut-and-welfare-boost/107315572'],['ABC News, Coalition says cuts to climate, housing and more would save $31b','https://www.abc.net.au/news/2026-10-26/coalition-says-cuts-to-save-budget-31-billion/107310512']],
 file=fl(i),angle='Equity versus efficiency: the plan improves equity but costs $22b a year, rests on taxes the PBO has not costed and may weaken work incentives at payment cut-offs. Compare with the Coalition\'s plan to fund bracket indexation by cutting climate programs.',
 questions=[Q('Evaluate the effects of raising the tax-free threshold on equity and efficiency in the Australian economy.',6)],
 note='A party proposal, filed as reported. The Lorenz curve on the digest is illustrative only.')

i='2026-10-27-rba-melbourne-cup-live-hike'
add(id=i,title='The RBA\'s Melbourne Cup meeting becomes a live chance for a fifth hike',date='2026-10-27',type='news',outlets=['ABC News','CommBank'],
 summary='Explains why the 3 November RBA decision is live, the market odds, and the limits of monetary policy against a fuel-driven price shock.',
 lede='The cash rate is 4.60% after four rises this year. Market odds of a November hike rose from about 24% to 56% after Deputy Governor Hauser warned the inflation outlook is materially worse, and were above 60% by 26 October; CBA\'s base case is still a hold.',
 about={'h09':['4D.2','4D.3'],'y12':['Y2c.4','Y2c.5','Y2c.8'],'y11':[]},also={'h09':['3C.3'],'y12':['Y2c.7','Y1c.4'],'y11':[]},
 issues=['rates','inflation'],levers=['monetary'],diagrams=['adas','flow'],
 figures=[F('RBA cash rate','4.60% after four rises in 2026','27 October 2026','rates','ABC News / CommBank'),F('Market odds of a November hike','about 24% to 56% after Hauser\'s speech (CBA); above 60% by 26 October (ABC)','21-26 October 2026','rates','CommBank / ABC News'),F('RBA forecast vs bank forecasts for trimmed mean, September quarter','0.8% vs 0.9-1.0%','September quarter 2026','inflation','CommBank')],
 terms=[T('Cash rate','The interest rate on overnight loans between banks, which the RBA targets.'),T('Transmission mechanism','The channels through which a change in the cash rate affects spending and inflation.')],
 links=[['CommBank, September data will keep inflation pressure on RBA','https://www.commbank.com.au/articles/newsroom/2026/10/inflation-cpi-rba-interest-rates-november.html'],['ABC News markets blog, 26 Oct 2026','https://www.abc.net.au/news/2026-10-26/asx-markets-business-live-news-october-26/107306820'],['ABC News, RBA deputy warns the inflation outlook is materially worse, 21 Oct 2026','https://www.abc.net.au/news/2026-10-21/reserve-bank-hauser-warns-inflation-outlook-materially-worse/107288574']],
 file=fl(i),angle='Much of today\'s inflation is supply-side (fuel). Monetary policy works on demand, so it can only stop the price shock spreading by slowing the whole economy, and it acts with long lags.',
 questions=[Q('Discuss the limitations of monetary policy in responding to inflation driven by a rise in fuel prices.',6)],
 note='Market odds change daily. UPDATE DUE: RBA decision on 3 November 2026 and the September quarter CPI released 28 October.')

i='2026-10-27-startup-cgt-rnd-reform'
add(id=i,title='New tax break for startup investors and a refocused R&D incentive',date='2026-10-27',type='news',outlets=['Treasurer','ABC News'],
 summary='A current microeconomic reform using tax incentives to raise innovation and productivity, with the positive externality case for R&D support.',
 lede='The Treasurer introduced the Treasury Laws Amendment (Tax Reform No. 4) Bill 2026, which creates an Innovative Business CGT Concession for early investors in young innovative firms and redesigns the R&D Tax Incentive from 1 July 2028 to reward core research.',
 about={'h09':['4E.1','3A.6'],'y12':['Y2d.2','Y2d.4'],'y11':['P3c.5']},also={'h09':['4E.3'],'y12':['Y1a.10','Y2d.1'],'y11':['P5b.7']},
 issues=['productivity','investment'],levers=['micro','fiscal'],diagrams=['adas','flow'],
 figures=[F('Refundable R&D offset turnover threshold','$20m to $50m (from 1 July 2028)','27 October 2026','productivity','ABC News'),F('Core R&D offset rates','up by as much as 50% (from 1 July 2028)','27 October 2026','productivity','ABC News'),F('Wider business and start-up tax relief package','$3.8b','27 October 2026','budget','Treasurer')],
 terms=[T('Capital gains tax (CGT)','Tax on the profit from selling an asset.'),T('Positive externality','A benefit to third parties; R&D spillovers are the classic example.')],
 links=[['Treasurer, media release: tax reforms support innovation and investment','https://ministers.treasury.gov.au/ministers/jim-chalmers-2022/media-releases/tax-reforms-support-innovation-and-investment'],['ABC News markets blog, 27 Oct 2026','https://www.abc.net.au/news/2026-10-27/asx-markets-business-live-news-anthropic/107312526']],
 file=fl(i),angle='R&D creates positive externalities so the market under-provides it, which is the efficiency case for a tax incentive. The costs are lost revenue and the risk that firms relabel ordinary activity as R&D.',
 questions=[Q('Explain how microeconomic reforms that encourage innovation can improve Australia\'s long-run economic growth.',4)],
 note='A bill that has been introduced, not law. Safe-harbour rules for eligibility are still being finalised. The benefits to productivity take years to arrive.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
