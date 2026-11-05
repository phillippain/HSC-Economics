import json,os
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-11-04-oil-near-100-hormuz-blockade','2026-11-01-us-midterms-tariffs-likely-to-stay','2026-11-02-commodity-prices-aud-softens','2026-11-04-canva-david-jones-job-losses','2026-11-01-myefo-no-promise-of-net-savings'}
os.makedirs('_to_delete/superseded',exist_ok=True)
for x in d:
    if x['id'] in REMOVE:
        src=x['file']['path']
        if os.path.exists(src): os.rename(src,'_to_delete/superseded/'+os.path.basename(src))
ES=next(x for x in d if x['id']=='2026-10-26-external-stability-june-qtr-2026')
d=[x for x in d if x['id'] not in REMOVE]; have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
recs=[]
def R(i,title,date,type,outlets,summary,lede,about,also,issues,levers,diagrams,figures,terms,links,angle,questions,note,pages=1):
    recs.append(dict(id=i,title=title,date=date,type=type,outlets=outlets,summary=summary,lede=lede,
      about=about,also=also,issues=issues,levers=levers,diagrams=diagrams,figures=figures,terms=terms,links=links,
      file={'path':f'files/{i[:7]}/{i}.pdf','label':'One-page digest' if pages==1 else 'Two-page explainer','pages':pages},
      angle=angle,questions=questions,note=note))
def A(h,y,z=()): return {'h09':list(h),'y12':list(y),'y11':list(z)}
BLOG='https://www.abc.net.au/news/2026-11-05/asx-markets-business-live-news-november-5-2026/107347286'
L_BLOG=['ABC News, ASX markets business live blog, 5 Nov 2026',BLOG]
RBA=['RBA, media release 2026-30: decision on the cash rate target, 3 Nov 2026','https://www.rba.gov.au/media-releases/2026/mr-26-30.html']
def AFR(t): return ['AFR, '+t+' (article address not given in the digest; link goes to the AFR home page)','https://www.afr.com/']
S='ABC News live blog'

R('2026-11-05-oil-plunge-after-midterms','Oil falls almost 9% as markets bet on an end to the Iran war','2026-11-05','news',['ABC News'],
 'Shows how expected supply recovery moves the oil price before any extra barrels arrive, and who gains and loses in Australia. Replaces the 4 November edition.',
 'Brent crude fell US$8.98 (8.7%) to US$94.62 a barrel, its lowest since 31 August, after the US midterm result raised hopes of an earlier end to the war with Iran. Australian energy shares were sold off while the ASX 200 closed 2.6% higher at 9,065.',
 A(['3C.3','1A.1'],['Y1c.4','Y1c.5','Y3e.3']),A(['3C.4','4D.3','1A.8','2C.6'],['Y1c.1','Y1a.10','Y1a.13','Y2c.8','Y3c.5']),
 ['inflation','global','trade'],['monetary'],['ds','adas','flow'],
 [F('Brent crude','US$94.62 (-US$8.98, -8.7%; lowest since 31 August)','5 November 2026',  'global',S),F('US crude (WTI)','US$88.12 (-8.3%)','5 November 2026','global',S),F('Gulf crude and product exports','17.1m barrels a day in October (September 18.9m)','October 2026','global',S),F('ASX 200','+2.6% to 9,065 (Dow about +3%)','5 November 2026','global',S),F('Woodside / Viva / Santos / Ampol shares','-5.6% / -5.2% / -4.8% / -3.8%','5 November 2026','trade',S),F('Gold','about US$4,135 an ounce','5 November 2026','global',S)],
 [T('Supply shock','A sudden change in the cost or availability of a key input that shifts supply.'),T('Price-inelastic demand','Quantity demanded changes little when price changes, as with fuel in the short run.')],
 [L_BLOG],
 'For an oil importer like Australia, cheaper oil shifts SRAS right: lower cost-push inflation and a boost to real incomes. For energy exporters it means lower export income.',
 [Q('Explain how a sustained fall in world oil prices would affect Australia\'s inflation rate.',4),Q('Discuss why lower oil prices could hurt some parts of the Australian economy.',4)],
 'Replaces the 4 November item (Brent US$100.40, WTI US$93.08, ING expecting eurozone inflation near 4%, Australian fuel spending +5.4% in September). Traders\' expectation of an earlier end to the war is a market view, not an agreed deal. UPDATE DUE: any Hormuz agreement.')

R('2026-11-05-us-midterms-democrats-win-tariffs-stay','Democrats take Congress, but America\'s tariffs are likely to stay','2026-11-05','news',['Baker McKenzie','ABC News','AFR'],
 'The midterm result with the legal reasons tariffs survive, plus the tariff diagram. Replaces the 1 November pre-vote forecast.',
 'Voters punished President Trump over the cost of living, with Democrats winning both houses on 3 November, but trade lawyers say the tariff wall will not come down because the powers now used do not need Congress each year. A bill to roll tariffs back could be vetoed, and overriding a veto needs two-thirds of the Senate.',
 A(['1C.2','2D.4','1C.1'],['Y3a.7','Y3a.8','Y3a.11']),A(['1B.4','1B.1','4H.3'],['Y3a.5','Y3a.15','Y3a.13']),
 ['trade','global'],['trade'],['ds','flow'],
 [F('US House count (Democrats-Republicans), early','251-155','AFR tally, 6 November 2026','trade','AFR'),F('US Senate count (Democrats-Republicans), early','54-44, with 2 seats still to be called','5 November 2026','trade','Baker McKenzie; ABC News'),F('Senate majority needed to override a veto','two-thirds','2026','trade','Baker McKenzie'),F('Supreme Court ruling on IEEPA tariffs','February 2026: the emergency powers law does not allow tariffs','February 2026','trade','Baker McKenzie')],
 [T('Protection','Government measures that shield domestic producers from import competition.'),T('Tariff','A tax on imports that raises their domestic price.'),T('Deadweight loss','The efficiency loss when a tariff stops mutually beneficial trade.')],
 [['Baker McKenzie, 2026 US midterm election results: trade issues (article address not given; link goes to the Sanctions News home page)','https://sanctionsnews.bakermckenzie.com/'],AFR('early midterm count, 6 Nov 2026')],
 'Use the midterms as evidence that protection has political as well as economic costs, then explain why tariffs persist: legal authority (Sections 122, 232, 301 and, for the first time, 338), the veto and bipartisan support on China. Expect hearings and oversight rather than repeal.',
 [Q('Using a tariff diagram, explain who gains and who loses from a US tariff on imported goods.',6),Q('Explain why US protection could stay high even after the midterm result.',4)],
 'Replaces the 1 November forecast item, which gave the pre-election Congress as House 218-214 and Senate 53-47 (Republican majorities), a 10% temporary global tariff, about 20 trade deals claimed by the White House and a probe into 16 partners. The counts here are early and some seats were still to be called. Advisers say firms should plan for tariffs staying high and expect a push for tighter chip and AI export controls.')

R('2026-11-05-us-voters-reject-data-centres','US voters say no to data centres in their backyard','2026-11-05','news',['ABC News','AFR','NBC'],
 'A market failure example: the private benefits of data centres are counted but costs to neighbours and the grid often are not.',
 'About 41 data-centre ballot measures were held across 10 US states and all but one were heading for defeat, with an NBC exit poll finding three-quarters of voters opposed a data centre in their own community. In Australia on the same day, NextDC shares jumped about 48% after a Goodman-backed group bought a stake of up to 9.9%.',
 A(['3F.2','3F.4'],['Y1e.5','Y1a.10'],['P2h.3']),A(['1A.5','4G.1'],['Y1e.3','Y2f.5','Y3b.2'],['P2h.1','P5a.5']),
 ['environment','investment','global'],['environmental'],['compare'],
 [F('Data-centre ballot measures','about 41 in 10 US states; all but one heading for defeat','5 November 2026','investment',S),F('Voters opposed to a data centre in their community','3 in 4 (NBC exit poll)','November 2026','environment','NBC via '+S),F('NextDC share price','+48% (Goodman-backed group bought up to 9.9% at $9.50 a share)','5 November 2026','investment',S)],
 [T('Negative externality','A cost borne by third parties that is not reflected in the market price.'),T('Social licence','Community acceptance a project needs to proceed in practice.')],
 [L_BLOG,AFR('Wesfarmers, Telstra, BHP urge government to move fast on AI, 6 Nov 2026')],
 'The costs raised by voters are power prices, water, land use, noise and emissions; investors point to investment spending in AD, productivity gains that shift LRAS outward, and jobs. Link to policies such as pricing, regulation or renewable-supply conditions.',
 [Q('Identify one negative externality of data centres and explain a policy that could correct it.',4),Q('Explain how data-centre investment can affect both aggregate demand and aggregate supply.',4)],
 'Ballot results were still being counted when reported. The ABC framed the result as a warning for Australia; Meta\'s president said new US data centres will now be very hard to build. See the NSW data centre electricity item filed today.')

R('2026-11-05-aud-steady-near-70-cents','Dollar holds near 70 US cents as rates rise and commodities shift','2026-11-05','stats',['ABC News','RBA'],
 'Shows opposing forces on the AUD: a higher cash rate lifts it while falling energy prices and a narrow US rate gap hold it back. Replaces the 2 November edition.',
 'The Australian dollar was 70.12 US cents late on 5 November, up 0.1%, after the RBA lifted the cash rate to 4.85% on 3 November. Iron ore rose 0.9% to US$92.80 a tonne but oil fell almost 9%, and US 10-year bond yields near 4.95% limit the gap between Australian and US rates.',
 A(['2C.2','2C.3','2C.6'],['Y3c.2','Y3c.4','Y3c.5','Y1a.7'],['P6c.1']),A(['2A.1','2C.4','3D.3','4D.3'],['Y3c.1','Y3c.6','Y3e.3'],['P6a.2','P6c.2']),
 ['fx','trade','rates'],['monetary'],['fx','flow'],
 [F('Australian dollar','70.12 US cents (+0.1%)','late 5 November 2026','fx','ABC News'),F('RBA cash rate','4.85% (highest in 18 years)','3 November 2026','rates','RBA'),F('Iron ore','US$92.80 a tonne (+0.9%)','5 November 2026','trade','ABC News'),F('LME copper','near US$14,000 a tonne','5 November 2026','trade','ABC News'),F('US 10-year bond yield','near 4.95%','5 November 2026','rates','ABC News')],
 [T('Interest rate differential','The gap between domestic and foreign interest rates, which drives capital flows.'),T('Appreciation','A rise in the value of the AUD against other currencies.')],
 [L_BLOG,RBA],
 'When asked about the AUD, name at least two forces: the interest rate differential, commodity prices or terms of trade, and global risk sentiment, then explain which dominates. Here the forces largely offset.',
 [Q('Using a diagram, explain how an increase in the cash rate could affect the value of the AUD.',4),Q('Explain two factors pulling the AUD in opposite directions in November 2026.',4)],
 'Single-day figures, so update before quoting. Replaces the 2 November item (AUD 70.20 US cents, iron ore US$90.80, Australian 10-year yield 5.13% against 4.93% in the US). After the 6-3 vote the dollar reportedly slipped to about US69.8c and the 10-year yield fell to 5.10%, according to the AFR summary filed today.')

R('2026-11-05-diesel-import-dependence','Diesel squeeze: Australia pays more to find new suppliers','2026-11-05','news',['The Conversation','Macquarie University','Climate Council'],
 'A case of import dependence and imported cost-push inflation: Australia buys almost as much diesel but pays far more for it.',
 'Australia is the world\'s largest buyer of seaborne diesel, importing about 28 billion litres last year, and war in the Gulf and drone strikes on Russian refineries have reshaped the global diesel trade. Diesel peaked at A$3.20 a litre and is still about A$2.79, almost $1 higher than a year ago, with the Climate Council estimating an extra $9 billion paid for imports between March and August.',
 A(['2A.1','3C.3'],['Y3e.3','Y1c.4','Y3e.1'],['P6a.2']),A(['3D.3','2B.4','1A.1'],['Y1a.7','Y3e.2'],[]),
 ['trade','inflation','global'],['global'],['ds','flow'],
 [F('Diesel imported','about 28 billion litres (almost 8% of seaborne diesel)','last year','trade','Lurion De Mello, The Conversation'),F('Diesel price','A$2.79 a litre (peak A$3.20; almost $1 higher than a year ago)','November 2026','inflation','Lurion De Mello, The Conversation'),F('Extra paid for diesel imports','about $9 billion','March to August 2026','trade','Climate Council via The Conversation'),F('Russia\'s share of world diesel shipments','12% to 2%','2026','global','Lurion De Mello, The Conversation'),F('Share of Australia\'s diesel from South Korea','almost half (Indian supply stopped)','2026','trade','Lurion De Mello, The Conversation'),F('US diesel exports','49% above the 2025 average','2026','global','Lurion De Mello, The Conversation')],
 [T('Import dependence','Relying on foreign suppliers for an essential good.'),T('Fuel security','The ability to keep reliable fuel supplies flowing during disruptions.')],
 [['Lurion De Mello (Macquarie University), As diesel from the Gulf and Russia dried up, Australia had to find new suppliers at a cost, The Conversation, 5 Nov 2026','https://theconversation.com/as-diesel-from-the-gulf-and-russia-dried-up-australia-had-to-find-new-suppliers-at-a-cost-295461']],
 'Link to external stability: a higher fuel import bill widens the trade deficit on fuels and feeds imported cost-push inflation, part of why the RBA revised its inflation forecasts up. Korean refineries still depend on Middle East crude, so the diversification is partial.',
 [Q('Explain how a rise in world diesel prices affects Australia\'s balance on goods and its CPI.',4),Q('Does relying on fewer suppliers make Australia more vulnerable to global shocks? Discuss.',6)],
 'An analysis by an academic. The $9 billion is a Climate Council estimate. The Strait of Hormuz closure date (28 February) is as stated in the article.')

R('2026-11-05-farrell-midterms-vindicate-anti-tariff-stance','Farrell: Trump\'s defeat proves tariffs hurt consumers','2026-11-05','news',['Australian Financial Review'],
 'A current statement of the case against tariffs and a trade policy dispute over the Australia-EU FTA.',
 'Trade Minister Don Farrell will use the midterm result to press Washington to drop its tariffs on Australia, calling it a vindication of the view that tariffs mainly raise prices for ordinary consumers. The Coalition says it will vote against the Australia-EU FTA early next year, arguing it falls short on agriculture and ties Australia to climate commitments.',
 A(['2D.1','2D.2','2D.4'],['Y3a.16','Y3a.13','Y3a.7']),A(['1C.2','1B.4','2D.3'],['Y3a.8','Y3a.3']),
 ['trade','global'],['trade'],['ds'],
 [F('Existing US tariff on Australian imports','12.5%','5 November 2026','trade','AFR'),F('Australia-EU FTA','to parliament early next year; Coalition says it will vote against','5 November 2026','trade','AFR'),F('Summits Trump is due to attend that the PM may raise tariffs at','2','5 November 2026','trade','AFR')],
 [T('Free trade agreement (FTA)','A deal that lowers trade barriers between member countries.'),T('Trade liberalisation','Reducing tariffs and other barriers to trade.')],
 [AFR('Trump thrashing vindicates Australia\'s stance on tariffs: Farrell, 5 Nov 2026')],
 'The tariff diagram shows consumers losing more than producers and the government gain together, which is Farrell\'s argument. When evaluating an FTA, weigh gains from trade against adjustment costs and conditions attached, here the climate commitments.',
 [Q('Using a diagram, explain why tariffs raise prices for consumers.',4),Q('Assess the potential benefits and costs for Australia of a free trade agreement with the EU.',6)],
 'Positions are those of the Minister, the Coalition and Joe Hockey as reported. Both sides agree cost of living decided the US result, according to the report. Follows the 29 October items on the stalled EU deal. UPDATE DUE: the parliamentary vote.')

R('2026-11-05-goods-trade-surplus-september','Goods trade surplus jumps to $2.8 billion as imports fall','2026-11-05','stats',['ABS'],
 'The September goods balance: exports up, imports down led by gold, with a link to the current account.',
 'The seasonally adjusted goods surplus rose $2,642m to $2,826m in September, from a revised $184m in August. Exports rose 2.3% to $48.4b, led by other mineral fuels and metals, while imports fell 3.3% to $45.6b, with non-monetary gold making up $1,096m of the fall.',
 A(ES['about']['h09'],ES['about']['y12'],ES['about']['y11']),A(ES['also']['h09'],ES['also']['y12'],ES['also']['y11']),
 ['trade','global'],['global'],['chart'],
 [F('Goods surplus, seasonally adjusted','$2,826m (August revised $184m; July $1,515m)','September 2026','trade','ABS'),F('Goods exports','$48.4b (+$1,090m, +2.3%)','September 2026','trade','ABS'),F('Other mineral fuels / metals excluding gold exports','+$502m / +$382m','September 2026','trade','ABS'),F('Rural exports / meat exports','+3.6% / +11.3% (+$243m)','September 2026','trade','ABS'),F('Goods imports','$45.6b (-$1,551m, -3.3%)','September 2026','trade','ABS'),F('Non-monetary gold imports','-$1,096m','September 2026','trade','ABS')],
 [T('Balance on goods','Exports of goods minus imports of goods; part of the current account.'),T('Non-monetary gold','Gold traded as a commodity; volatile flows that can swing the monthly balance.')],
 [['ABS, International trade in goods, September 2026','https://www.abs.gov.au/statistics/economy/international-trade/international-trade-goods/sep-2026']],
 'A larger goods surplus narrows the current account deficit, but the primary income deficit is usually much bigger. Falling imports of capital and consumer goods may also signal weaker domestic demand as interest rates rise.',
 [Q('Outline the main factors behind the larger goods surplus in September 2026.',3),Q('Explain how a larger goods surplus affects Australia\'s current account deficit.',4)],
 'Monthly goods-only data swing with gold, so do not treat one month as a trend. UPDATE DUE: October figures on 3 December. The dot point tags follow the existing external stability item.')

R('2026-11-05-tech-giants-news-levy-ausfta','US tech giants push for trade retaliation over Australia\'s news levy','2026-11-05','news',['Australian Financial Review'],
 'Shows how a trade agreement can constrain domestic policy and how trade is used as leverage in digital and services disputes.',
 'Meta, Google and other platforms claim Australia\'s News Bargaining Incentive breaches the Australia-US Free Trade Agreement, and their lobby group CCIA has asked US Trade Representative Jamieson Greer to investigate. The incentive makes big platforms strike deals with publishers or pay a levy of 2.5% of their Australian digital advertising revenue.',
 A(['2D.2','2D.3'],['Y3a.13','Y3a.16']),A(['2D.4','1B.4'],['Y3a.15']),
 ['trade','global'],['trade','micro'],['compare'],
 [F('Levy rate if no deals are struck','2.5% of Australian digital advertising revenue','2026','trade','AFR'),F('Expected levy revenue','$1.85b over four years ($550m in 2026-27)','2026','budget','AFR'),F('Existing US tariff on Australian imports','12.5% (after a forced-labour imports investigation)','2026','trade','AFR')],
 [T('AUSFTA','The Australia-United States Free Trade Agreement, in force since 2005.'),T('Retaliation','Trade measures imposed in response to another country\'s policies.')],
 [AFR('Tech giants seek US trade retaliation over Australian media levy, 5 Nov 2026')],
 'Contrast the platforms\' view (a discriminatory tax that breaches AUSFTA) with the government\'s (it funds public-interest journalism, a merit good, and is a domestic policy choice). Canada dropped its digital tax last year under similar US pressure.',
 [Q('Explain how a trade agreement can constrain a country\'s domestic economic policy.',4),Q('Discuss the risks to the Australian economy of the US retaliating over the news levy.',6)],
 'The platforms\' claims are the lobby group\'s, and the government\'s revenue figure is its forecast. Meta, TikTok and Microsoft did not negotiate with publishers; Google had some deals to offset its bill, as reported. UPDATE DUE: any US investigation.')

R('2026-11-05-woodside-job-cuts-dividend-reset','Woodside cuts 500 jobs and its dividend as energy prices slide','2026-11-05','news',['ABC News','Discovery Alert','AFR'],
 'Shows how falling world energy prices flow through the terms of trade to Australian firms, jobs and export income.',
 'Woodside will cut at least 500 jobs, about 10% of its global workforce with around 80% in Australia and mostly in WA, and cut its dividend payout as energy prices slide. Its shares fell as much as 6.6% on the same day oil prices plunged.',
 A(['2A.1','2B.4'],['Y1a.7','Y3e.3','Y3e.1'],['P6a.2']),A(['3D.3','2C.6','3B.3'],['Y3c.5','Y1b.6','Y1a.14'],['P1e.7']),
 ['trade','employment','global'],['global'],['flow'],
 [F('Jobs to be cut','at least 500 (about 10% of the workforce)','5 November 2026','employment',S),F('Structural savings targeted from 2028','about US$400m a year (AFR: about A$570m)','5 November 2026','trade',S),F('Dividend policy','from 50-80% of underlying profit to 20-40% of adjusted operating cash flow (first 20% guaranteed)','5 November 2026','trade',S),F('Woodside share price','fell as much as 6.6%','5 November 2026','trade',S),F('Scarborough LNG / Louisiana LNG','99% complete (first gas Q4 2026) / 32% complete (due 2029)','5 November 2026','investment','Discovery Alert')],
 [T('Terms of trade','The ratio of export prices to import prices; it rises when commodity export prices rise.'),T('LNG','Liquefied natural gas, one of Australia\'s largest export earners.')],
 [L_BLOG,['Discovery Alert, Woodside capital markets day, dividend and job cuts, November 2026','https://discoveryalert.com/news/woodside-capital-markets-day-dividend-job-cuts-november-2026']],
 'A falling terms of trade reduces national income and usually weakens the AUD, but cheaper fuel imports also help households, so the net effect depends on Australia\'s mix of exports and imports.',
 [Q('Explain how a fall in world energy prices affects Australia\'s terms of trade.',4),Q('Discuss the effects of a declining terms of trade on Australian economic growth and employment.',6)],
 'The job cuts and dividend change are company announcements reported second-hand. The US and Australian dollar savings figures are from different outlets, so do not combine them.')

R('2026-11-05-cost-of-living-decided-us-midterms','Cost of living decided the US midterms. Is Labor next?','2026-11-05','news',['Australian Financial Review (opinion)'],
 'An opinion column on the politics of inflation and the regressive effect of price shocks, useful for the limits on economic policy.',
 'AFR political editor Phillip Coorey argues the Republican defeat was about prices, not ideology, with petrol prices from the Iran war and tariff-driven price rises hurting voters. He says the Albanese government, facing another rate rise, could face a similar backlash in 2028 unless conditions improve.',
 A(['3C.4','4H.3'],['Y1c.7','Y2b.14']),A(['3E.3','3C.3'],['Y1c.8','Y1d.9']),
 ['inflation','inequality'],['fiscal','monetary'],['flow'],
 [F('Diesel price cited by Joe Hockey','over US$6 a gallon (about A$2.27 a litre)','November 2026','inflation','AFR'),F('Australian cash rate','4.85%','3 November 2026','rates','RBA'),F('Next federal election','2028','2028','budget','AFR')],
 [T('Cost of living','The cost of the goods and services households need; it rises when prices outpace incomes.'),T('Real wages','Wages adjusted for inflation, which measure actual purchasing power.')],
 [AFR('It\'s the cost of living, stupid. And not even Trump is immune, 5 Nov 2026')],
 'Low-income households spend more of their budget on fuel and food, so price shocks are regressive. Pressure for quick fixes may clash with fighting inflation, a political limit on policy.',
 [Q('Explain why real wages fall when inflation exceeds nominal wage growth.',3),Q('Discuss how political pressures can limit governments\' ability to fight inflation.',5)],
 'An opinion column, so use it to show the politics of inflation, not as a data source. Labor, the Coalition and One Nation agreeing that cost of living decided the US result is the author\'s reading of their statements.')

R('2026-11-05-david-jones-collapse','David Jones collapses after 188 years as spending slows','2026-11-05','news',['ABC News','Sharecafe','AFR'],
 'Shows how higher interest rates and weaker spending reach retailers, and asks whether the job losses are cyclical or structural. Replaces the 4 November edition.',
 'Australia\'s oldest department store has gone into administration after rent talks with Scentre Group, the landlord of 17 of its 38 stores, broke down. All stores keep trading while a sale or recapitalisation is sought, and rival Myer\'s shares rose 10.9%.',
 A(['3B.3','3B.6','3A.7'],['Y1b.5','Y1b.6','Y1a.14'],['P1e.7','P1e.5']),A(['3B.2','4D.3'],['Y1b.10','Y1b.11'],[]),
 ['employment','growth','rates'],['monetary'],['adas','compare'],
 [F('David Jones stores','38, all still trading during administration','5 November 2026','employment',S),F('Stores leased from Scentre Group (Westfield)','17','5 November 2026','employment',S),F('Landlords\' bank guarantees','about $45m','5 November 2026','employment',S),F('Myer share price','+10.9%','5 November 2026','growth',S),F('Online searches for David Jones','about 30% below 2019 levels','2026','growth',S),F('Roles Canva is cutting (4 November report)','more than 1,200, about a fifth of its workforce','November 2026','employment',S)],
 [T('Voluntary administration','An insolvency process where an administrator takes control to try to save or sell the business.'),T('Cyclical unemployment','Joblessness caused by a downturn in aggregate demand.')],
 [L_BLOG,['Sharecafe, Retailer David Jones enters administration (article address not given; link goes to the Sharecafe home page)','https://www.sharecafe.com.au/']],
 'Weak spending is cyclical, but the long-run shift to online shopping is structural, and the best answers mention both. Five rate rises this year shifted AD left as more household income went to mortgage repayments.',
 [Q('Using an AD/AS diagram, explain how higher interest rates can lead to retail business failures.',4),Q('Assess whether job losses at department stores are mainly cyclical or structural.',5)],
 'Replaces the 4 November item, which reported speculation about David Jones and the Canva job cuts; the Canva figure is carried over (the Rates and tax hit households item reports 1,217 jobs, 22% of staff). The administrators are McGrathNicol and the receivers FTI Consulting, appointed by lender Hilco. ACCI\'s comment that retailers\' costs are rising faster than they can absorb is its view. UPDATE DUE: sale or recapitalisation.')

R('2026-11-05-home-grown-inflation','Home-grown inflation: the RBA says the problem is here, not just overseas','2026-11-05','news',['AFR','RBA'],
 'Tests whether inflation is imported or domestic using the four causes in the syllabus, with demand-pull and cost-push AD/AS diagrams and the RBA\'s outlook.',
 'The RBA raised the cash rate to 4.85% on 3 November by six votes to three, and Governor Bullock said Australia has a domestic home-grown inflation problem that was visible before oil prices jumped. The Treasurer points to the Middle East war while business, the RBA and AFR columnists point to demand the economy cannot supply and weak productivity.',
 A(['3C.3','4D.2','4D.3'],['Y1c.4','Y1c.5','Y2c.4','Y2c.7']),A(['3C.2','3C.4','4B.1','4H.1'],['Y1c.8','Y2c.8','Y1a.10','Y2d.1']),
 ['inflation','rates','productivity','investment'],['monetary','fiscal','micro'],['adas','compare','chart','flow'],
 [F('RBA cash rate','4.85% (fifth rise this year; board vote 6-3)','3 November 2026','rates','RBA'),F('Inflation that is domestic (Business Council analysis of ABS data)','3.0 of 4.3 percentage points (about 70% of the surge)','2026','inflation','Business Council via AFR'),F('Spending growth now / Business Council wants cut by more than half','about 4.5%','2026','budget','Business Council via AFR'),F('Construction pipeline in 2027 / mining boom peak (2012)','about $870b / $400b','2027','investment','Deloitte via AFR'),F('Data-centre projects','37 projects worth $141b (up 36% in a year)','2026','investment','Deloitte via AFR'),F('Share of data-centre components imported','about 70% (a leakage)','2026','investment','Governor Bullock via AFR'),F('Federal spending as a share of GDP','24.3% (2022-23) to 26.9% (2025-26)','2025-26','budget','John Kehoe, AFR (opinion)'),F('RBA forecasts','inflation back below 3% in late 2027; core at the 2.5% midpoint in 2028; unemployment 5.1% by late 2028; GDP growth 1.3%','2026','inflation','RBA via AFR'),F('Market odds of a further rise by February / economists tipping next move down','33% / 30 of 32','November 2026','rates','AFR'),F('AUD / 10-year bond yield after the 6-3 vote','about US69.8c / 5.10% (two-month low)','4 November 2026','fx','AFR')],
 [T('Capacity pressures','Demand pressing against what the economy can produce.'),T('Inflationary expectations','Expectations of higher inflation that feed into wage and price setting.'),T('Leakage','Spending that leaves the domestic economy, such as on imports.')],
 [AFR('RBA\'s ugly outlook spells tough times (J. Kehoe, 3 Nov, opinion)'),AFR('"Chickens coming home to roost" (P. Coorey, 4 Nov)'),AFR('Mega construction boom stirs RBA rate worries (M. Read, 4 Nov)'),AFR('RBA rates have peaked but relief still a year away (C. Lefort, 4 Nov)'),RBA],
 'The label matters because it decides which policy can work. If inflation is mostly imported, the RBA can do little about the cause and risks over-tightening; if it is mostly domestic demand and weak productivity, higher rates and tighter fiscal policy are aimed at the right target, but work with a lag. The test: the Fed, ECB and RBNZ held while Australia hiked.',
 [Q('Distinguish between demand inflation and cost inflation, using the RBA\'s November decision.',4),Q('Assess the view that Australia\'s inflation is mainly home-grown.',6)],
 'Several sources are AFR opinion columns (Kehoe, Thomson-style comment), and the Business Council has an interest in lower government spending. The 1.3 point imported share is calculated (4.3 minus 3.0). Economists Bassanese and Hogan still expect more rises (Hogan: a peak of 5.35%); Saul Eslake sees no loosening before early 2028. See also the RBA decision item filed on 3 November.',pages=2)

R('2026-11-05-nab-profit-fall-bad-debts','NAB profit falls as bad debts surge and 2,500 jobs go','2026-11-05','news',['ABC News','Sharecafe','AFR'],
 'Bad-debt charges as a leading indicator of a slowing economy, and the banks\' role in transmitting a cash rate change.',
 'NAB\'s net profit for the year to September fell 9.1% to $6.14b, short of the $6.45b analysts expected, and its bad and doubtful debts charge rose 86% to $1.55b. A restructure will cut up to 2,500 jobs by mid-2027.',
 A(['4D.3','4D.2'],['Y2c.5','Y1a.14'],['P4c.3','P4a.1']),A(['3A.7','3B.2'],['Y2c.8','Y1b.6'],[]),
 ['rates','employment','growth'],['monetary'],['flow'],
 [F('NAB net profit','$6.14b (-9.1%; analysts expected $6.45b)','year to September 2026','rates',S),F('NAB cash earnings','-13%','year to September 2026','rates',S),F('Bad and doubtful debts charge','$1.55b (+86%)','year to September 2026','rates',S),F('Jobs to be cut','up to 2,500 by mid-2027','2026','employment',S),F('NAB share price','fell about 7.5%','5 November 2026','rates',S)],
 [T('Credit impairment charge','Money a bank sets aside for loans it expects will not be repaid.'),T('Transmission mechanism','How a cash rate change flows through to lending, spending and inflation.')],
 [L_BLOG],
 'Banks raise bad-debt provisions when they expect unemployment and business failures to rise, and tighter bank lending can then amplify a slowdown. Bendigo Bank passed on the RBA\'s 0.25-point rise to variable home loans the same day.',
 [Q('Explain why rising bank bad-debt charges may signal a slowing economy.',3),Q('Outline the role of commercial banks in transmitting a change in the cash rate.',4)],
 'Company results as reported second-hand. Some non-voluntary exits were delayed until after Christmas, according to the report. Complements the 1 November item on banks and savers.')

R('2026-11-05-nsw-data-centre-electricity-demand','Data centres could use twice the power of every home in Sydney','2026-11-05','news',['Australian Financial Review'],
 'A negative externality and energy market pressure from the AI investment boom, with policy options from a NSW parliamentary inquiry.',
 'A NSW parliamentary inquiry warns the $50b of data centres planned in the state could use up to 25,719 GWh a year, about twice the 11,400 GWh used by Greater Sydney\'s 1.9 million households. It also found nobody knows the true demand because of phantom connection requests.',
 A(['3F.2','3F.4','4G.1'],['Y1e.5','Y1e.6','Y2f.5'],['P2h.3','P2h.4']),A(['3F.1','4G.2'],['Y1e.3','Y2f.2','Y2f.7'],['P5a.5']),
 ['environment','investment'],['environmental','micro'],['ds','compare'],
 [F('Possible annual use of planned NSW data centres','up to 25,719 GWh','2026','environment','AFR'),F('Greater Sydney households\' use (1.9 million households)','11,400 GWh','2026','environment','AFR'),F('Data centres\' share of NSW electricity','about 4% now; 17-30% by 2040','2026','environment','Ausgrid via AFR'),F('Speculative share of connection requests','six in every seven megawatts','2026','environment','Oxford Economics via AFR'),F('Connection applications that go ahead','about 20%','2026','environment','Oxford Economics via AFR')],
 [T('Phantom demand','Speculative grid-connection requests that will never be built and distort forecasts.'),T('Environmental sustainability','Meeting current needs without degrading resources for future generations.')],
 [AFR('Data centres could use twice the power of all the houses in Sydney, 5 Nov 2026')],
 'Evaluate the options: regulation (100% renewable supply on an hourly basis, a public register, less diesel backup) versus market-based approaches such as connection charges and carbon pricing, and note the risk of discouraging investment.',
 [Q('Using a diagram, explain how rapid data-centre growth could affect electricity prices.',4),Q('Evaluate a requirement for data centres to supply 100% renewable energy.',6)],
 'The upper-bound demand figure is a projection from the inquiry, not an outcome. Thirteen firms, including Amazon, Microsoft, Google and Anthropic, declined or did not respond to invitations to give evidence, as reported. The committee made more than two dozen recommendations, including an AI strategy.')

R('2026-11-05-rates-and-tax-hit-households','How the squeeze lands: mortgages, investors, shop floors and tech jobs','2026-11-05','news',['AFR','RBA'],
 'Traces the transmission mechanism through housing: repayments near a record share of income, falling prices, the wealth effect and job cuts, with a cyclical versus structural split.',
 'With the cash rate at 4.85% and average variable mortgage rates at 6.75%, repayments would take 37.4% of a typical household\'s income, just under the record 37.5% set in December 1989. New housing loan commitments are 27% below their November 2025 peak, with Bullock saying the May tax changes explain the extra drop in investor loans.',
 A(['4D.3','3E.4','3C.4'],['Y2c.5','Y1d.5','Y1d.6','Y2b.10'],['P4c.7','P5b.7']),A(['3E.3','3E.6','4H.1','3B.3'],['Y2c.8','Y1c.7','Y1b.6'],['P4c.3','P1e.7']),
 ['housing','rates','inequality','employment'],['monetary','fiscal'],['ds','adas','compare','flow','chart'],
 [F('Average variable mortgage rate','6.75%','November 2026','housing','REA Group via AFR'),F('Repayments as a share of typical household income','37.4% (record 37.5% in December 1989)','November 2026','housing','REA Group via AFR'),F('New housing loan commitments','27% below the November 2025 peak','2026','housing','AFR'),F('Forecast fall in Sydney prices','up to 16% (CBA); about 10% since February (AFR, 2 November)','2026','housing','CBA; AFR'),F('Real household disposable income per person','about -5% against its 2021 peak','2026','inequality','RBA via AFR'),F('RBA outlook','GDP growth 1.3% by late 2027; real wages fall until at least late 2027; unemployment 5.1% by late 2028','2026','employment','RBA via AFR'),F('Canva jobs to be restructured','1,217 (22% of its workforce)','2026','employment','AFR (Chanticleer)')],
 [T('Wealth effect','Spending changes as household wealth, such as house prices, changes.'),T('Negative gearing','Deducting investment property losses from other taxable income.'),T('Cyclical vs structural','Changes that reverse with the economic cycle compared with persistent changes.')],
 [AFR('Property investors have been sent packing (L. Slade, 5 Nov)'),AFR('Bullock\'s wrong. DJs and Canva show this may feel worse than recession (J. Thomson, Chanticleer, 4 Nov, opinion)'),AFR('RBA rates have peaked but relief still a year away (C. Lefort, 4 Nov)')],
 'Monetary policy works by shifting AD, and the May changes to negative gearing and the capital gains tax discount amplify the rate rises, so AD falls further than rates alone would cause. HSBC\'s Paul Bloxham calls the mix a double whammy: the rates and housing part is cyclical, the tax part structural.',
 [Q('Explain how rising interest rates and falling house prices can reduce consumer spending.',4),Q('Analyse the effects of high inflation and falling real wages on different groups of households.',6)],
 'Combines several AFR stories with different dates, so do not add the price-fall measures. Parts are opinion (Chanticleer on David Jones and Canva). The RBA is not forecasting a technical recession; Bullock says it will feel like one. See also the David Jones collapse item filed today.',pages=2)

R('2026-11-05-accc-sets-armaguard-cash-prices','ACCC steps in to set prices for Armaguard\'s cash transport','2026-11-05','news',['Australian Financial Review'],
 'A first use of new regulatory powers over a near-monopoly, showing the challenges of price regulation for a natural monopoly.',
 'The Cash Distribution Framework Act, passed in August, lets the ACCC regulate Armaguard, and talks with its eight biggest customers broke down. The ACCC has set interim prices for the first time, rejecting Armaguard\'s cost-plus proposal because its costs were not transparent.',
 A(['4E.3','4E.2'],['Y2d.2','Y2d.4'],['P2h.6']),A(['4E.1'],['Y2d.5'],['P5a.5']),
 ['productivity'],['micro'],['flow'],
 [F('Increase above CPI for the eight largest customers, until June 2027','29.55% (on their 30 June contract prices)','5 November 2026','productivity','AFR'),F('Smaller customers','10% above CPI, or CPI only','5 November 2026','productivity','AFR'),F('Losses Armaguard says it made on big-bank contracts since 2021','$207m','5 November 2026','productivity','AFR'),F('Extra funding banks and retailers have already contributed','$100m','5 November 2026','productivity','AFR')],
 [T('Natural monopoly','A market where one firm can supply at lower cost than several competitors.'),T('Price regulation','A regulator setting or capping prices where competition cannot.')],
 [AFR('ACCC forced to intervene after big banks, Armaguard relations unravel, 5 Nov 2026')],
 'Price regulation must balance viability (a price too low means the firm exits) against monopoly pricing (too high hurts customers). Mention information asymmetry: the ACCC could not verify Armaguard\'s costs. Armaguard must keep supplying services and must not favour its own ATM business over rivals.',
 [Q('Explain why cash distribution may be a natural monopoly.',3),Q('Discuss the challenges a regulator faces when setting prices for a monopoly.',5)],
 'The $207m loss is Armaguard\'s claim. The prices are interim, pending a long-term model. The customers include the big banks, Coles, Woolworths, Wesfarmers and Australia Post, and the near-monopoly is controlled by Lindsay Fox, as reported.')

R('2026-11-05-budget-versus-inflation','Budget versus inflation: when fiscal and monetary policy pull in different directions','2026-11-05','news',['AFR'],
 'Shows an interest-driven $11 billion budget hole, the policy mix, the savings menu and the case study of the home battery subsidy. Replaces the 1 November MYEFO item.',
 'The RBA is raising rates to cool demand while an estimated $11 billion hole has opened in the federal budget since May, largely because a surge in bond yields pushed up the interest bill. The Treasurer and Finance Minister will not promise net savings in December\'s mid-year update, and every minister has been told to find savings.',
 A(['4C.1','4C.2','4B.1','4C.3'],['Y2b.3','Y2b.6','Y2b.12','Y2b.14']),A(['4D.3','4H.1','4H.3','4I.3'],['Y2b.13','Y2g.1','Y2a.2','Y2c.7']),
 ['budget','inflation','rates'],['fiscal','monetary','micro'],['adas','compare','chart','flow'],
 [F('Estimated hole in the budget since May','$11b (about $6b extra debt interest over four years)','November 2026','budget','AFR (Coorey)'),F('Other named contributors','Senate carve-outs on capital gains and trust tax, refugee intake and veterans\' payment backdowns, a private health rebate compromise, a $680m charity wage subsidy','2026','budget','AFR'),F('Spending growth now / Business Council target','about 4.5% / 2%','2026','budget','Business Council via AFR'),F('Federal spending as a share of GDP','26.9% in 2025-26, up from 24.3% in 2022-23','2025-26','budget','AFR (Kehoe, opinion)'),F('Home battery subsidy cost: original / after loophole / after rebate cut','$2.3b / over $14b / about $7.2b (4 years)','2026','budget','AFR (Cropp)'),F('Batteries installed','35,000 a month; 550,000+ systems since July 2025','2026','environment','AFR (Cropp)'),F('Evening-peak grid power for homes with solar and a battery','74% less','2026','environment','AEMO via AFR')],
 [T('Net savings','More saved than spent in a budget update.'),T('Regressive','A policy whose benefits or costs fall more heavily on lower-income households.'),T('Stabilisation','Using policy to smooth the business cycle.')],
 [AFR('Budget black hole makes savings challenge harder (P. Coorey, 3 Nov)'),AFR('Shrinking subsidies haven\'t stifled the battery boom (R. Cropp, 3 Nov)'),AFR('"Chickens coming home to roost" (P. Coorey, 4 Nov)')],
 'A deficit is not only a government choice: persistent inflation lifts bond yields and interest costs, widening the hole. Price stability, a smaller deficit and low unemployment cannot all be won at once, and if fiscal policy does not tighten, monetary policy may have to do more and keep rates higher for longer.',
 [Q('Explain how higher interest rates can worsen the federal budget balance.',3),Q('Evaluate the effectiveness of fiscal policy in reducing inflation in the current context.',6)],
 'Replaces the 1 November ABC item on the MYEFO, which reported Finance Minister Gallagher citing health, aged care and veterans\' costs, a deficit of about 1% of GDP, spending of 26.8% of GDP (ABC) and the Opposition saying restraint would ease pressure on the RBA. The "so far" battery cost is an AFR estimate (certificates x $40); the net spending decisions figure ($3.7b to $51.2b) is from an opinion column citing Coalition analysis, so it is not given as a fact. UPDATE DUE: MYEFO in December.',pages=2)

R('2026-11-06-business-urges-fast-ai-policy','Wesfarmers, Telstra and BHP urge Canberra to move fast on AI','2026-11-06','news',['Australian Financial Review'],
 'Business argues rapid AI adoption is a productivity lever, while the digest sets this against externalities, structural unemployment and regulatory uncertainty.',
 'Business leaders want rules on AI, copyright and data centres settled before Christmas, warning that slow decisions will push investment to rival countries. Wesfarmers\' Rob Scott calls AI one of the few levers big enough to fix Australia\'s productivity problem.',
 A(['4E.1','3A.6'],['Y2d.1','Y2d.2','Y1a.10']),A(['4E.2'],['Y2d.6','Y3b.2'],['P3c.4','P3c.5']),
 ['productivity','investment'],['micro'],['adas','compare'],
 [F('Extra annual output at BHP in WA from AI computer vision','180,000 tonnes','2026','productivity','BHP via AFR'),F('Companies and CEOs represented by the BCA','more than 130','2026','productivity','AFR'),F('Share of data-centre power from renewables (industry claim)','70%','2026','environment','AFR')],
 [T('Productivity','Output per unit of input, such as per hour worked.'),T('Regulatory certainty','Clear, stable rules that let firms plan long-term investment.')],
 [AFR('Wesfarmers, Telstra, BHP urge government to move fast on AI, 6 Nov 2026')],
 'Balance the dynamic efficiency gains from new technology against externalities (energy, water) and structural unemployment risks. Investment is flowing to Singapore, India and Japan, and Meta says the midterms will make US data-centre building harder.',
 [Q('Explain how regulatory uncertainty can reduce business investment.',3),Q('Discuss the potential economic benefits and costs of rapid AI adoption in Australia.',6)],
 'The case for speed is made by business groups with an interest in the outcome; Assistant Minister Andrew Charlton\'s comment that falling AI share prices do not mean the technology has stalled is his view. Pairs with the Productivity Commission items filed today.')

R('2026-11-05-hauser-denies-pressuring-rba-board','RBA deputy denies pre-empting the board\'s rate decision','2026-11-05','news',['Australian Financial Review'],
 'Central bank communication, forward guidance and independence, with the 6-3 vote as evidence of real debate on the board.',
 'Some external members of the RBA\'s monetary policy board reportedly felt senior staff\'s public comments made November\'s rate rise look decided in advance, but Deputy Governor Andrew Hauser says he was only explaining the data. Market odds of a hike rose from about 20% to 60% after his 21 October speech and to 80% after the 28 October CPI.',
 A(['4D.1','4D.2'],['Y2c.3','Y2c.4','Y2c.7']),A(['4D.3','4H.3'],['Y2c.5'],[]),
 ['rates','inflation'],['monetary'],['flow'],
 [F('Market odds of a November hike','about 20% to 60% after Hauser\'s speech, then 80% after the CPI','October 2026','rates','AFR (Kehoe)'),F('Board vote to raise the cash rate to 4.85%','6-3','3 November 2026','rates','RBA'),F('Monetary policy board members','9 (3 internal and 6 external)','2026','rates','AFR (Kehoe)')],
 [T('Forward guidance','A central bank signalling the future path of interest rates.'),T('Inflation expectations','What people expect inflation to be; these feed into wages and prices.')],
 [AFR('Hauser denies pressuring RBA board with market-moving speech, 5 Nov 2026'),RBA],
 'Communication is part of the transmission mechanism, but it creates a tension with board independence. Hauser says he followed the 2023 RBA Review\'s advice to explain policy publicly and wants the RBA to explain how it would react to new data without promising a path for rates.',
 [Q('Explain how central bank communication can influence inflation expectations.',4),Q('Discuss one benefit and one risk of RBA officials commenting publicly before a board meeting.',4)],
 'The claim that board members felt pre-empted is reported, not confirmed by the RBA. Westpac\'s Luci Ellis and former board member Warwick McKibbin are quoted with opposing readings. Follows the 21 October Hauser and 26 October Hunter items.')

R('2026-11-06-pc-chair-calls-for-review-of-ir-laws','Productivity chief says Labor\'s workplace laws should be reviewed','2026-11-06','news',['Sydney Morning Herald'],
 'Frames industrial relations policy as a trade-off between equity and efficiency, and links wages, productivity and inflation.',
 'Productivity Commission chair Danielle Wood says the government should check whether its industrial relations changes, including multi-employer bargaining and same-job-same-pay, are holding back productivity. Meanwhile ABS data show federal public service wages rose 7% last financial year.',
 A(['4F.2','4F.4','4E.1'],['Y2e.7','Y2e.2','Y2d.1']),A(['3A.6','3E.6'],['Y2e.8','Y2d.6','Y1c.4'],['P3c.4']),
 ['employment','productivity','budget'],['labour','micro','fiscal'],['compare'],
 [F('Board time spent on compliance','55% (24% a decade ago)','2026','productivity','SMH'),F('Possible gain in a worker\'s income from small productivity improvements over a decade','about $14,000','2026','productivity','SMH'),F('Federal public service wages','+7%','last financial year','budget','ABS via SMH')],
 [T('Multi-employer bargaining','Enterprise agreements negotiated across several employers at once.'),T('Industrial relations','The laws and institutions that govern pay, conditions and bargaining.')],
 [['Paul Sakkal, Sydney Morning Herald, Labor\'s union-friendly laws under fire from its own productivity chief, 6 Nov 2026 (article address not given; link goes to the SMH home page)','https://www.smh.com.au/']],
 'Wages can only rise sustainably in line with productivity without adding to inflation. Critics (Coalition, business groups) say the reforms add cost and complexity; supporters (Labor, unions) say they lifted wages and improved bargaining power for the low paid.',
 [Q('Explain the link between wage growth, productivity growth and inflation.',4),Q('Evaluate the effects of recent industrial relations reforms on the Australian economy.',6)],
 'The compliance and $14,000 figures are the Commission chair\'s claims as reported. Economists also suggested cutting the EV tax concession and a road user charge, and Hauser warned of a fusillade of shocks. Pairs with the item on the inquiry being barred from examining tax and IR.')

R('2026-11-05-pc-barred-from-tax-and-ir','Productivity inquiry barred from looking at tax and workplace laws','2026-11-05','news',['Australian Financial Review'],
 'Shows what the Productivity Commission\'s business dynamism inquiry covers, why productivity matters for inflation, and the LRAS diagram.',
 'The Productivity Commission\'s interim report on business dynamism focuses on red tape, management and insolvency, but the Treasurer kept tax, industrial relations and mergers out of scope and business groups are angry. Red tape costs business about $160b a year.',
 A(['4E.1','4E.3','3A.6'],['Y2d.2','Y2d.1','Y2d.6']),A(['4E.2'],['Y1a.10','Y2d.5'],['P3c.5']),
 ['productivity'],['micro'],['adas'],
 [F('Annual cost of regulatory compliance to business','about $160b','2026','productivity','AFR'),F('Licences a typical business needs','14 (dairy farmers 46; scientific research firms 59)','2026','productivity','AFR'),F('Productivity gap between Australian and US management','almost 10%','2026','productivity','AFR'),F('Firms using an AI tool: Australia / US / UK','59% / 78% / 71%','December 2025','productivity','AFR')],
 [T('Business dynamism','How easily firms enter, grow and exit, which drives reallocation and productivity.'),T('Microeconomic reform','Policies that improve efficiency and productivity in particular markets.')],
 [AFR('Government gags PC from examining tax and IR impacts on business, 5 Nov 2026')],
 'Higher productivity raises the economy\'s speed limit: with LRAS shifted out, output can grow without extra price pressure, so the RBA does not have to hold rates as high. The limitation is that reforms take years to work.',
 [Q('Explain how reducing regulation could improve productivity.',4),Q('Using an AD/AS diagram, explain how productivity growth reduces inflationary pressure.',5)],
 'The BCA and ACCI criticisms are their views as reported. Proposals include a one-year bankruptcy option for people with debts under $50,000 and a government liquidator for insolvent companies with no assets.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
