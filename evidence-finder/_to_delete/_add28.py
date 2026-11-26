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
      angle=angle,questions=questions,note=note,added='2026-11-25'))

ABC='ABC News'
def L(a,b): return [a,b]

R('2026-11-24-senate-showdown-gas-reservation-lng-2028','4','Senate showdown over plan to reserve gas for Australians','2026-11-24','news',['Region Canberra','Argus Media'],
 "Gives the detail and politics of the gas reservation bill, the competing 25% export tax idea and a supply and demand view of who gains and loses.",
 "The government wants the Senate to pass a scheme forcing LNG exporters to reserve up to 20% of their exports for the domestic market from 2028. The bill has passed the House, and a Labor-chaired Senate committee has recommended it be passed.",
 ['4E.1','4E.2'],['Y2d.1','Y2d.4','Y2d.5'],['P2i.2','P2i.3','P2i.4'],
 ['4H.3','2A.1'],['Y2d.6'],['P2d.1'],
 ['investment','inflation','trade'],['micro'],['ds','compare'],
 [F('Maximum share of LNG exports to be reserved','Up to 20% of annual export volumes, from 1 January 2028','November 2026','investment','Region Canberra'),
  F('Gladstone LNG netback price','A$35.48/GJ on 10 November (A$15.40 a year earlier)','10 November 2026','inflation','Argus Media'),
  F('East-coast December gas price','About A$12.20/GJ','November 2026','inflation','Argus Media'),
  F('Gas export tax proposed by the Greens and David Pocock','25% (rejected by the government)','November 2026','investment','Region Canberra'),
  F('Existing WA reservation policy','15%','November 2026','investment','Region Canberra')],
 [T('Gas reservation','A requirement that a share of gas production be sold domestically rather than exported.'),T('Netback price','The export price minus the costs of liquefying and shipping the gas.')],
 [L('Region Canberra: All eyes on Senate over gas reservation scheme, 24 Nov 2026','https://regioncanberra.com.au/'),L('Argus Media: Senate panel backs gas reservation bill, Nov 2026','https://www.argusmedia.com/')],
 "Reservation shifts domestic supply right: price falls and quantity used rises, helping manufacturers and households while exporters lose some higher-priced sales. Weigh short-run price relief against the risk that lower expected returns reduce future gas investment and supply.",
 [Q("Evaluate the effectiveness of a domestic gas reservation scheme in lowering energy prices for Australian households and businesses.",5)],
 "UPDATE DUE: the Senate vote. Industry warned the planned 110% oversupply target for the east coast could distort the market and deter investment. The Coalition wants Western Australia excluded; the government says WA must stay in for constitutional reasons. Jacqui Lambie, unions, the Ai Group and Manufacturing Australia back the bill. Replaces the 19 November card (Acting PM Richard Marles urging the Coalition to back the scheme; at least 20% of output reserved; Shadow Resources Minister Susan McDonald said gas sells at 'about $10' and called for a 'fair level' of pricing). The 18 November WA carve-out opinion card is kept. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-24-myefo-substantial-savings-budget-weakens','4','MYEFO to bring "substantial" savings as the budget weakens','2026-11-24','news',[ABC,'CathNews','Fixed Income News'],
 "Shows what is moving the budget (lower receipts, rising welfare costs) and how savings aim to avoid adding to inflation.",
 "The government's mid-year budget update (MYEFO) will show lower tax receipts and bigger deficits in later years. The Treasurer has promised savings that more than cover any new spending, so as not to add to inflation, though final dollar figures have not been released.",
 ['4C.1','4C.2','4B.1'],['Y2b.2','Y2b.3','Y2b.14'],['P5a.4'],
 ['4D.3'],['Y2b.13'],['P5c.3'],
 ['budget','inflation'],['fiscal'],['adas','flow','compare'],
 [F('Unemployment peak driving welfare costs','Above 5%','November 2026','budget','ABC News'),
  F('PBS script price','$25, frozen to the end of the decade','November 2026','budget','ABC News'),
  F('MYEFO timing','December, after the RBA\'s 8 December decision','November 2026','budget','ABC News')],
 [T('MYEFO','The Mid-Year Economic and Fiscal Outlook, the update to the May Budget.'),T('Automatic stabilisers','Tax receipts fall and welfare spending rises automatically as the economy slows.')],
 [L('ABC News: Federal politics live, 24 Nov 2026','https://www.abc.net.au/news/'),L('CathNews (ABC): Chalmers economic statement','https://cathnews.com/'),L('Fixed Income News: Chalmers flags jobless rate above 5%','https://www.fixedincomenews.com.au/')],
 "A contractionary (or less expansionary) fiscal stance supports the RBA by not adding to demand, but cutting too hard in a slowdown risks deepening it. Explain cyclical versus structural components: a slowing economy cuts receipts and lifts welfare spending, widening the cyclical deficit.",
 [Q("Distinguish between the cyclical and structural components of the budget, and explain why the government is seeking savings in MYEFO.",5)],
 "UPDATE DUE: the MYEFO itself. EV and home-battery subsidies, whose costs have blown out, could be targeted; Labor's Andrew Charlton did not rule out means-testing. Chalmers argued that no realistic level of savings will make inflation go away but too much new spending can make it worse. Shadow Treasurer Tim Wilson proposed a 'speed limit' on government spending. Replaces the 23 November card on Chalmers' statement to parliament (growth from 2.3% last financial year to well below 2% for the next two years; unemployment to peak above 5%; inflation not back in the 2-3% band until late 2027; PBS co-payment frozen at $25 until 2030, $242 million over three years; $3 billion over four years from cutting the private health insurance rebate for people aged 65+; positives: business investment growing faster than forecast, wages above 3%, no recession forecast) and, through it, the 22 November and 18 November MYEFO cards (JWS survey: 83% concerned about the deficit; deficit $31.5 billion in 2026-27; government spending 26.8% of GDP against 31.3% in the pandemic era). The forecast numbers are also on the 24 November Chalmers jobless warning card. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-24-rba-tipped-to-hold-4-85-economy-cools','4','RBA tipped to hold at 4.85% as the economy cools','2026-11-24','news',['CommBank',ABC,'Fixed Income News'],
 "Shows the cash rate path, evidence that policy is working on housing, and what markets expect next.",
 "After five rate rises in 2026, economists expect the Reserve Bank to pause at its 7-8 December meeting, and bond markets are starting to bet on cuts in 2027. The cash rate is 4.85% after a 25 basis point rise in November, the fifth this year and the second in a row.",
 ['4D.1','4D.2','4D.3'],['Y2c.1','Y2c.2','Y2c.4','Y2c.5'],['P4c.3'],
 ['3C.1','3C.3'],['Y2c.3'],['P4c.4'],
 ['rates','inflation','housing'],['monetary'],['flow','adas'],
 [F('Cash rate','4.85% after five rises in 2026; November rise decided 6-3','November 2026','rates','RBA'),
  F('New housing lending, September quarter','-15.5%','September quarter 2026','housing','ABC News'),
  F('Investor housing lending, September quarter','-32.3%','September quarter 2026','housing','ABC News'),
  F('Market pricing','A full 25 basis point cut by about August 2027; 10-year bond yield about 4.9%','24 November 2026','rates','Fixed Income News'),
  F('RBA inflation expectation','Above 3% until late 2027','November 2026','inflation','RBA, via ABC News')],
 [T('Cash rate','The RBA\'s target interest rate on overnight loans between banks.'),T('Transmission mechanism','The channels through which a change in the cash rate affects spending, output and inflation.')],
 [L('CommBank: RBA pause increasingly likely, Nov 2026','https://www.commbank.com.au/'),L('ABC News: markets live, 24 Nov 2026','https://www.abc.net.au/news/'),L('Fixed Income News, 24 Nov 2026','https://www.fixedincomenews.com.au/')],
 "Higher rates raise mortgage repayments and borrowing costs, cutting consumption and investment so AD shifts left: inflation pressure eases but real GDP falls and unemployment rises. Policy works with lags of 12-18 months, which explains the split vote: some board members feared overtightening.",
 [Q("Explain how the RBA's interest rate rises in 2026 are affecting economic activity, and discuss one limitation of monetary policy.",6)],
 "UPDATE DUE: RBA decision 7-8 December. Economist views and market pricing, not decisions. CommBank's Belinda Allen says December won't be a 'live' meeting; Pitcher Partners expects a hold until February 2027. Replaces the 22 November CBA outlook card (cash rate highest since 2008 after the 6-3 vote; dissenters warned of a 'materially sharper downturn' while the majority saw upward inflation risks; RBA headline CPI forecast 4.5% in December 2026 and back to 2.5% by mid-2028; CBA had cuts pencilled for August and November 2027). The 17 November minutes card and 19 November jobs shock card are kept. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-24-business-activity-fastest-fall-five-years-pmi','3','Business activity shrinks at its fastest pace in more than five years','2026-11-24','news',[ABC,'S&P Global'],
 "Uses the November flash PMI as a leading indicator, with the link from higher interest rates to weaker activity.",
 "The S&P Global flash composite PMI for November fell to 48.7 from 49.6 in October, pointing to a contraction across manufacturing and services as higher interest rates bite. Activity fell at the sharpest pace in more than five years.",
 ['3A.4','3A.7','3B.2'],['Y1a.5','Y1a.12'],['P1e.4','P1e.5'],
 ['4D.3'],['Y2c.5'],['P1e.7'],
 ['growth','employment','inflation'],['monetary'],['adas','flow','chart'],
 [F('S&P Global flash composite PMI','48.7 in November (October: 49.6); below 50 means activity is shrinking','November 2026','growth','S&P Global, via ABC News'),
  F('Unemployment rate','4.9% in October (43,500 jobs lost)','October 2026','employment','ABS, via ABC News'),
  F('UBS real GDP growth forecast','1.4% in 2027','2027 forecast','growth','UBS, via ABC News')],
 [T('PMI','Purchasing Managers\' Index, a monthly business survey; above 50 means expansion, below 50 contraction.'),T('Leading indicator','Data that tends to change before the wider economy does.')],
 [L('ABC News: markets live, 23 Nov 2026','https://www.abc.net.au/news/'),L('ABC News: Sahm rule recession indicator','https://www.abc.net.au/news/')],
 "Falling demand shifts AD left: output and employment fall while price pressures ease, the intended effect of tighter monetary policy. S&P Global's Jingyi Pan blamed higher interest rates. Price rises eased for both input costs and prices charged.",
 [Q("Explain why the PMI is a useful leading indicator of economic growth, using November's result as evidence.",4)],
 "A survey, not official GDP data. Replaces the 23 November card on the same release, which framed it as stagflation risk: UBS forecast headline CPI of 4.5% in the December quarter (September 4.3%); UBS real GDP growth about 2.0% in 2026 and 1.4% in 2027 with unemployment above 5%; new orders fell at the sharpest rate in five years; firms resumed shedding jobs; Brent about US$92.65. NOTE: the two digests read the price signals differently (survey prices easing here; UBS expecting headline CPI to rise). UPDATE DUE: October CPI and Q3 GDP (2 December). Y1a.5, Y1a.12, P1e.4 and P1e.5 are carried from the earlier recession card. Links are to the ABC home page because the digest gives titles only.")

R('2026-11-24-chalmers-unemployment-top-5-things-harder','3','Chalmers: unemployment to top 5% as "things might get a bit harder"','2026-11-24','news',[ABC,'CathNews','Fixed Income News'],
 "Gives the Treasurer's official forecasts and the cost-push explanation for rising inflation and unemployment together.",
 "In a ministerial statement on the economy, Treasurer Jim Chalmers warned of higher unemployment, slower growth and stubborn inflation. He insisted Treasury is not forecasting a recession.",
 ['3B.2','3B.3','3C.3'],['Y1b.1','Y1c.1','Y1c.5'],['P1e.7','P2c.4'],
 ['3A.7','4B.1'],['Y2a.2'],['P1e.4'],
 ['employment','inflation','growth'],['monetary'],['adas','flow'],
 [F('Unemployment peak forecast','Above 5% (May Budget forecast: 4.5%; October: 4.9%)','November 2026','employment','Treasurer, via ABC News'),
  F('Growth forecast','"Well below" 2% in each of the next two years (2.3% last financial year)','November 2026','growth','Treasurer, via ABC News'),
  F('Inflation back in the RBA 2-3% band','End of 2027','November 2026','inflation','Treasurer, via ABC News'),
  F('AMP estimate of risk of a more severe downturn','40% (growth below 1%)','November 2026','growth','AMP (Shane Oliver), via Fixed Income News')],
 [T('Stagflation','Rising inflation and rising unemployment at the same time.'),T('Cost-push inflation','Inflation caused by higher production costs, such as fuel.')],
 [L('CathNews (ABC): No recession but things might get a bit harder','https://cathnews.com/'),L('Fixed Income News: Chalmers flags jobless rate above 5%','https://www.fixedincomenews.com.au/'),L('ABC News: markets live, 23 Nov 2026','https://www.abc.net.au/news/')],
 "A fuel-price spike shifts SRAS left: the price level rises while output and employment fall, a mild stagflation. This is a classic conflict between objectives: fighting inflation with higher rates deepens the rise in unemployment.",
 [Q("Using an AD/AS diagram, explain why Australia is experiencing rising inflation and rising unemployment at the same time.",6)],
 "Forecasts, not outcomes; the AMP 40% figure is one economist's estimate. Positives: business investment growing about twice as fast as forecast in May, and real wages expected to recover in 2027. Overlaps the 23 November Chalmers statement figures, now carried on the 24 November MYEFO savings card. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-24-albanese-hosts-singapore-wong-supply-chains','2','Albanese hosts Singapore\'s Prime Minister as supply-chain security tops the agenda','2026-11-24','news',[ABC,'PM&C','Singapore MFA'],
 "Illustrates a bilateral trade relationship built on complementary resources and supply security, with the benefits and limits of bilateral agreements.",
 "Prime Minister Anthony Albanese hosted Singapore's Lawrence Wong for trade talks under the two countries' Comprehensive Strategic Partnership 2.0. No new trade measures had been announced at the time of writing, so the digest also covers the background to the relationship.",
 ['2D.2','1B.4','2A.1'],['Y3a.13','Y3a.16','Y3a.4'],['P6a.1','P6a.2'],
 ['1A.1','2D.1'],['Y3e.2'],[],
 ['trade','global'],['trade'],['flow','compare'],
 [F('CSP 2.0 initiatives (launched October 2025)','80, including 20 new agreements','October 2025','trade','Singapore MFA'),
  F('Australian companies using Singapore as a regional base','More than 5,000','2025','trade','PM Wong, 2025'),
  F('Australia\'s contribution to Singapore\'s FAST-P climate finance fund','A$175 million','2025','environment','PM&C')],
 [T('SAFTA','The Singapore-Australia Free Trade Agreement, a bilateral trade agreement.'),T('Supply-chain resilience','The ability to keep essential imports flowing through disruptions.')],
 [L('ABC News: Federal politics live, 24 Nov 2026','https://www.abc.net.au/news/'),L('Singapore MFA: 10th Leaders\' Meeting (2025)','https://www.mfa.gov.sg/'),L('PM: Joint statement on essential supplies, Apr 2026','https://www.pm.gov.au/')],
 "Australia exports LNG and Singapore refines fuels such as diesel that Australia imports: comparative advantage in action. Both want a binding protocol to keep essentials moving in a crisis such as the Iran war. Bilateral agreements lower barriers but have smaller reach than WTO deals and can divert trade.",
 [Q("Outline two benefits for Australia of bilateral trade agreements such as SAFTA, and one limitation.",4)],
 "MEETING OUTCOMES NOT YET PUBLISHED when the ABC reported: most facts here are background from October 2025 and April 2026 (when the leaders agreed during the energy crisis to keep essentials such as diesel and LNG flowing and to finalise a legally binding SAFTA protocol on essential supplies). UPDATE DUE: add the outcome of the meeting. Links are to home pages because the digest gives titles only.")

R('2026-11-24-aud-11-month-low-iron-ore-copper-slide','2','Dollar sinks to an 11-month low as iron ore and copper slide','2026-11-24','news',['Westpac IQ','MMI',ABC],
 "Explains the AUD's fall through commodity prices, risk aversion and a narrowing interest rate gap, with the shock-absorber effect of depreciation.",
 "The Australian dollar has wiped out all its 2026 gains, falling to US$0.6609 on 23 November, an 11-month low, and was the weakest G10 currency over the week. Prices for the commodities that underpin Australia's export income are falling and global investors are avoiding risk.",
 ['2C.2','2C.3','2C.6','2B.4'],['Y3c.2','Y3c.4','Y3c.5','Y3c.6','Y1a.7'],['P6c.1'],
 ['2A.1'],['Y3e.3'],['P6a.2'],
 ['fx','trade','rates'],['monetary'],['fx','flow'],
 [F('AUD / USD','US$0.6609 on 23 November (11-month low); about 66.3 US cents on Tuesday','23-24 November 2026','fx','Westpac IQ'),
  F('Iron ore (61% fines)','US$89.30 a tonne on 24 November; SGX futures below US$90 for five sessions','24 November 2026','trade','MMI Daily Iron Ore Index'),
  F('Chinese steelmakers in profit','About 10% (38% a year earlier)','19 November 2026','trade','Mysteel'),
  F('Copper / gold','Copper down about 14-16% this month; gold near 15-month lows','November 2026','trade','ABC News')],
 [T('Terms of trade','The ratio of export prices to import prices.'),T('Depreciation','A fall in the value of the AUD against other currencies in a floating exchange rate system.')],
 [L('Westpac IQ: The Australian Dollar: Losing Its Anchors','https://www.westpaciq.com.au/'),L('MMI: Daily Iron Ore Index, 24 Nov 2026','https://www.mmiprices.com/'),L('ABC News: markets live, 23 and 24 Nov 2026','https://www.abc.net.au/news/')],
 "Lower export earnings shift AUD demand left, and global risk aversion and a narrowing interest rate gap (markets pricing Fed rises but possible RBA cuts in 2027) reduce capital inflows. A lower AUD is a shock absorber: it makes exports more competitive but raises import prices, so mention current account and inflation effects.",
 [Q("Explain how a fall in commodity prices affects Australia's terms of trade, exchange rate and current account balance.",5)],
 "Market prices that move daily. Overlaps the 22 November miners and 23 November iron ore cards (both kept: this one adds the Westpac currency analysis and copper and gold). Iron ore here is the MMI 61% fines index (US$89.30), which differs from the US$88.50 and US$90.6 quoted on earlier cards. Links are to home pages because the digest gives titles only.")

R('2026-11-24-ai-stock-rout-record-rebound','1','AI-stock rout, then a record one-day rebound','2026-11-24','news',[ABC,'Reuters'],
 "Shows financial contagion in both directions, with Australia's smaller exposure and super fund links.",
 "An AI-led sell-off pushed Wall Street into a correction, then a single announcement (Nvidia reinstating Jensen Huang) sparked a huge rebound that spread to Asia and the ASX within hours. Last week the S&P 500 fell 8.6% and the Nasdaq about 10%, its worst week since March 2020.",
 ['1A.4','1A.8'],['Y3e.3','Y3b.3'],['P4b.2','P6c.1'],
 ['1A.1'],['Y3b.1'],['P6b.1'],
 ['global','growth'],[],['flow','compare'],
 [F('S&P 500, last week / Monday','-8.6% / +4.7% (nearly 12% below its October high)','20-23 November 2026','global','ABC News'),
  F('Nasdaq, last week / Monday','About -10% / +6.5%; Nvidia more than +30% on Monday','20-23 November 2026','global','ABC News'),
  F('Asia on Tuesday','Taiwan +9.1%, South Korea +7.5%, Japan +4.5%','24 November 2026','global','ABC News'),
  F('ASX 200 on Tuesday','+1.8% to 8,726, ending an eight-session losing streak','24 November 2026','global','ABC News'),
  F('Australian ETF buying on Monday','Record A$391 million, more than 70% into international shares','23 November 2026','investment','ABC News')],
 [T('Correction','A fall of 10% or more from a recent peak.'),T('Financial contagion','Shocks spreading rapidly across countries\' financial markets.')],
 [L('ABC News: markets live, 24 Nov 2026','https://www.abc.net.au/news/'),L('ABC News: markets live, 23 Nov 2026','https://www.abc.net.au/news/')],
 "Capital and sentiment move across borders within hours. Exposure: super funds hold large offshore share portfolios, and falling share wealth can dent confidence and spending. Cushions: the ASX has a smaller tech weighting, and a lower AUD lifts the AUD value of offshore assets.",
 [Q("Explain two ways volatility in global financial markets can affect the Australian economy.",4)],
 "The trigger of the rebound (Nvidia reinstating CEO Jensen Huang, with Donald Trump taking credit) is as reported by the digest and was not independently checked; economist Gerard Minack estimates a broad AI share index is 37% below its June peak. Replaces the 23 November Wall Street correction card (S&P 500 -3.7% to 6,910 on Friday 20 November, its seventh straight daily fall; Dow -1.9%; Nasdaq -5.3% on the day; Nvidia -13.8%; ASX 200 -1.6% Friday and eight losing sessions; Fed Governor Lisa Cook said US rates are not high enough; near-certain 25 basis point Fed hike priced for December). The 22 November weekly market table card (S&P 500 -8.3% for the week) is kept; the S&P weekly fall is quoted as -8.3% there and -8.6% here, so check the source. Links are to the ABC home page because the digest gives titles only.")

R('2026-11-24-iran-war-russian-oil-india-china-record','1','Iran war redraws the oil map as India and China buy record Russian crude','2026-11-24','news',['Reuters (via Business Standard)',ABC],
 "Shows how a geopolitical shock redirects trade flows and feeds into world oil prices and Australian fuel inflation.",
 "As the Iran war and a US naval blockade cut Middle Eastern supply, India and China are taking record volumes of Russian oil. Brent is up nearly a third since the war began but eased to US$88.97 on Tuesday as inventories built up.",
 ['1A.1','1A.8','3C.3'],['Y1c.5','Y3e.3','Y3a.4'],['P2d.1','P2d.2','P2c.4'],
 ['2B.4'],['Y1c.4'],['P6a.2'],
 ['global','inflation','trade'],[],['ds','adas','flow'],
 [F('Seaborne Russian oil to India and China','3.4 million barrels a day through mid-November (up about 530,000 a year earlier)','November 2026','trade','Vortexa'),
  F('China\'s Russian crude imports, January-October','+17% to 2.34 million barrels a day (US$59.6 billion), while total crude imports fell 15%','January-October 2026','trade','Reuters'),
  F('India\'s Russian crude imports','1.99 million barrels a day through early November (about 38% of imports)','November 2026','trade','Reuters'),
  F('Brent close on 24 November','US$88.97, the lowest close since 31 August','24 November 2026','inflation','Reuters')],
 [T('Trade diversion','Trade flows redirected towards different partners because of policy or conflict.'),T('Price-inelastic demand','Quantity demanded changes little when the price changes.')],
 [L('Business Standard (Reuters): India, China set for record Russian oil imports','https://www.business-standard.com/'),L('ABC News: markets live, 24 Nov 2026','https://www.abc.net.au/news/')],
 "Supply cut by conflict (S shifts left) raises price while quantity falls little because short-run demand is inelastic. On an AD/AS diagram an oil price shock shifts SRAS left, raising inflation and cutting output, which is how fuel prices feed into Australia's CPI.",
 [Q("Explain how a conflict in the Middle East can affect inflation and economic growth in Australia.",4)],
 "Together India and China buy more than 80% of Russia's crude exports. Drivers listed: temporary US sanctions waivers, the Iran war, a US naval blockade on Iranian flows and Ukrainian drone strikes on Russian refineries. Brent is lower here (US$88.97) than on the 19 November oil card (about US$91-93) and the 23 November iron ore card (about US$92.65): single-day prices. Links are to home pages because the digest gives titles only.")

R('2026-11-24-us-readies-sweeping-new-tariffs-subsidies-probe','1','Washington readies a sweeping new round of tariffs','2026-11-24','news',['Investing.com (citing WSJ)'],
 "Gives a live case of protectionism, the role of courts and how US tariffs could reach Australia through China.",
 "The US is preparing new tariffs on China, the EU and dozens of other economies, arguing that their industrial subsidies have created excess global capacity. The move would revive levies the US Supreme Court struck down in February.",
 ['1C.2','1C.1','2D.4'],['Y3a.6','Y3a.7','Y3a.8','Y3a.11','Y3a.14'],['P6a.1'],
 ['1B.2','2A.1'],['Y3a.15','Y3e.3'],['P6a.2'],
 ['trade','global'],['trade'],['ds','flow'],
 [F('Expected cap for partners with deals (EU, Japan, South Korea)','15% or lower; China slated for the steepest rates','November 2026','trade','WSJ, via Investing.com'),
  F('July tariffs on 60 economies (under court challenge)','10-12.5%; the new duties would stack on top','July 2026','trade','WSJ, via Investing.com'),
  F('Supreme Court ruling on the 2025 tariffs','Struck down in February 2026','February 2026','trade','WSJ, via Investing.com')],
 [T('Protectionism','Government measures that shield domestic industries from import competition.'),T('Excess capacity','Productive capacity well beyond what a market can absorb at normal prices.')],
 [L('Investing.com: White House prepares sweeping new tariffs, 24 Nov 2026','https://www.investing.com/')],
 "Apply the tariff diagram (price rises to Pw+t, imports shrink, revenue and deadweight loss). Link to Australia: higher US barriers on China weaken Chinese output and demand for Australian resources, hurting the terms of trade and the AUD.",
 [Q("Using a diagram, explain the effects of a US tariff on imports on US consumers, US producers and the US government.",4)],
 "PROSPECTIVE and second-hand: a report of what the US Trade Representative (Jamieson Greer) may release 'as soon as this week', citing the WSJ via Investing.com; nothing has been announced. UPDATE DUE: add USTR's findings and the actual rates. Steel, aluminium and cars are excluded (separate national security tariffs). Related 18 November WTO restrictions card and 23 November Philippines tariff card. Link is to the Investing.com home page because the digest gives the article title only.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-19-labor-presses-coalition-gas-reservation','2026-11-23-chalmers-weaker-growth-net-spending-cuts','2026-11-22-rba-pause-after-split-vote-cba-outlook','2026-11-23-business-activity-contracts-pmi-stagflation-risk','2026-11-23-wall-street-correction-ai-share-boom-unwinds'}
d=[x for x in d if x['id'] not in REMOVE]
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
