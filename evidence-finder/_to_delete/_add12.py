import json,os
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-10-28-chalmers-fiscal-response-to-inflation','2026-10-29-no-easy-way-out-of-inflation','2026-10-23-aud-commodity-prices','2026-10-25-global-central-bank-week','2026-10-25-saudi-oil-attacks'}
os.makedirs('_to_delete/superseded',exist_ok=True)
for x in d:
    if x['id'] in REMOVE:
        src=x['file']['path']
        if os.path.exists(src): os.rename(src,'_to_delete/superseded/'+os.path.basename(src))
d=[x for x in d if x['id'] not in REMOVE]; have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
def fl(i): return {'path':f'files/2026-10/{i}.pdf','label':'One-page digest','pages':1}
recs=[]
def add(**k): recs.append(k)
MK='https://www.abc.net.au/news/2026-10-29/asx-markets-business-live-news-29-october-2026/107321622'
PB='https://www.abc.net.au/news/2026-10-29/federal-politics-live-blog-oct-29/107320104'
PM='https://miragenews.com/australian-prime-minister-press-conference-1768488/'
L_MK=['ABC News, ASX markets business live blog, 29 Oct 2026',MK]
L_PB=['ABC News, Federal politics live blog, 29 Oct 2026',PB]
L_PM=['Prime Minister\'s press conference, 29 Oct 2026 (via Mirage News)',PM]
CH='https://www.abc.net.au/news/2026-10-28/chalmers-downplays-further-fuel-discounts-amid-high-inflation/107319372'

i='2026-10-29-fair-work-ombudsman-record-recoveries'
add(id=i,title='Wage watchdog recovers a record $453m for underpaid workers',date='2026-10-29',type='news',outlets=['Fair Work Ombudsman','HRD Australia','ABC News'],
 summary='Shows that labour market rules only work if they are enforced, and how underpayment shifts income from workers to employers.',
 lede='The Fair Work Ombudsman recovered about $453 million for more than 181,000 workers in 2025-26, up 27% on the year before, and received a record 31,596 anonymous reports. Large corporates made up nearly half of recoveries, including a Westpac underpayment of more than $50 million affecting about 47,000 staff.',
 about={'h09':['4F.1','4F.2','4F.3'],'y12':['Y2d.1','Y2d.4'],'y11':[]},also={'h09':['3E.6','4F.4','3E.5'],'y12':['Y1d.5','Y1d.9'],'y11':['P2h.8']},
 issues=['employment','inequality'],levers=['labour','micro'],diagrams=['flow','chart'],
 figures=[F('Wages and entitlements recovered by the FWO','about $453m (+27%, about $95m more)','2025-26','employment','Fair Work Ombudsman via HRD Australia'),F('Workers helped','more than 181,000','2025-26','employment','Fair Work Ombudsman via HRD Australia'),F('Anonymous reports received','31,596 (record)','2025-26','employment','Fair Work Ombudsman via HRD Australia'),F('Proactive investigations','more than 2,860 (nearly doubled)','2025-26','employment','Fair Work Ombudsman via HRD Australia'),F('Recovered over six years','about $2.5 billion','2020-21 to 2025-26','employment','Fair Work Ombudsman via HRD Australia'),F('Westpac underpayment','more than $50m, about 47,000 staff','2025-26','employment','Fair Work Ombudsman via HRD Australia')],
 terms=[T('Fair Work Ombudsman','The regulator that enforces workplace laws and awards.'),T('Award wage','The legal minimum pay and conditions for an industry or occupation.'),T('Labour market policy','Government rules and programs that affect wages, conditions and employment.')],
 links=[['HRD Australia, FWO recovered $453 million in unpaid wages and entitlements in FY26','https://hcamag.com/au/specialisation/employment-law/fwo-recovered-453-million-in-unpaid-wages-and-entitlements-in-fy26/589729'],L_MK],
 file=fl(i),angle='Setting a minimum wage is not enough: enforcement decides whether the floor is real. Weak enforcement lets non-compliant firms undercut compliant rivals and shifts income from workers to employers.',
 questions=[Q('Explain the role of the Fair Work Ombudsman in Australia\'s industrial relations system.',3),Q('Discuss how widespread underpayment of wages affects the distribution of income and labour market outcomes.',6)],
 note='The 2024-25 figure of about $358m on the digest chart is derived from the reported $95m increase, so check the FWO annual report before quoting it. The Star Entertainment $260m anti-money-laundering penalty in the same digest is unrelated to wages.')

i='2026-10-29-trusts-housing-grocery-price-caps'
add(id=i,title='Trust tax, housing claims and talk of grocery price caps',date='2026-10-29',type='news',outlets=['ABC News'],
 summary='Contrasts direct price controls with competition policy, with a price ceiling diagram, and links trust and housing tax changes to the distribution of income and wealth.',
 lede='The ACTU backed the planned 30% minimum tax on discretionary trusts, due from 1 July 2028. Assistant Treasurer Daniel Mulino said negative gearing and capital gains tax changes will help 75,000 more Australians buy a home, and Ed Husic floated price caps on bread, milk and eggs, which the government resisted in favour of the Grocery Code and ACCC enforcement.',
 about={'h09':['4E.3','3E.3','4C.2'],'y12':['Y2d.2','Y2b.10','Y2d.4'],'y11':['P2h.6','P5b.6','P5b.7']},also={'h09':['3E.6','3E.4','4E.1'],'y12':['Y1d.6','Y2b.13','Y2d.5'],'y11':['P5b.3']},
 issues=['inequality','housing','budget'],levers=['fiscal','micro'],diagrams=['ds','compare'],
 figures=[F('Minimum tax on discretionary trusts','30% from 1 July 2028','2026','inequality','ABC News'),F('Additional home buyers the government says changes will help','75,000 (government claim)','2026','housing','ABC News'),F('Staples floated for price caps','3 (bread, milk, eggs)','29 October 2026','inflation','ABC News')],
 terms=[T('Price ceiling','A legal maximum price set below the equilibrium price.'),T('Competition policy','Laws and regulators (the ACCC) that promote rivalry between firms.'),T('Progressive tax','A tax that takes a higher share from higher incomes.')],
 links=[L_PB,L_MK],
 file=fl(i),angle='A cap below equilibrium creates a shortage, since producers supply less than consumers want. Competition policy aims to lower prices by increasing rivalry without cutting supply. Use the trust tax and the housing claim to discuss equity.',
 questions=[Q('Explain how a minimum tax on trusts could affect the distribution of income.',3),Q('Compare price caps with competition policy as ways to reduce grocery prices.',6)],
 note='A roundup of live-blog items, so claims are reported as made: the 75,000 figure is the government\'s and was not checked. The price cap was a backbench idea, not government policy. The ATO extended credit-card tax payments to mid-2027 after a small-business backlash, and Peter Costello opposed any GST rise.')

i='2026-10-29-gas-reservation-bill-passes-house'
add(id=i,title='Gas reservation bill passes the House: up to 20% of exports for local users',date='2026-10-29',type='news',outlets=['ABC News','Business News WA','Prime Minister\'s office'],
 summary='A current microeconomic intervention in an energy market, with a supply and demand diagram and the trade-off with export earnings and investment.',
 lede='The Domestic Gas Reservation Bill, allowing up to 20% of gas exports to be reserved for the domestic market, passed the House of Representatives on 29 October and goes to the Senate. The Prime Minister says more local supply will put downward pressure on gas prices, which is particularly important for manufacturing.',
 about={'h09':['4E.1','4E.2'],'y12':['Y2d.1','Y2d.4','Y2d.5'],'y11':[]},also={'h09':['3C.3','4E.3','2B.4'],'y12':['Y2d.6','Y1c.4','Y3a.16'],'y11':['P2h.1']},
 issues=['inflation','trade','environment'],levers=['micro'],diagrams=['ds','flow'],
 figures=[F('Maximum share of gas exports that can be reserved','20%','29 October 2026','trade','ABC News; Prime Minister'),F('Electricity prices, annual','+13% (September CPI)','September 2026','inflation','ABS via digest'),F('Physical energy exports','ten-year low (as reported)','2024-25','trade','ABS via digest')],
 terms=[T('Gas reservation','Requiring a share of production to be sold on the domestic market.'),T('Microeconomic reform','Policies that change how individual markets work to improve efficiency or outcomes.'),T('Sovereign risk','The risk that a government changes the rules and harms investors.')],
 links=[L_PB,L_PM,['Business News, Gas reservation scheme passes House hurdle','https://businessnews.com.au/article/Gas-reservation-scheme-passes-House-hurdle']],
 file=fl(i),angle='Shows the policy as a supply shift in the domestic market (S1 to S2) lowering price. Evaluate with both sides: lower input costs and energy security against export earnings, investment certainty and sovereign risk.',
 questions=[Q('Use a supply and demand diagram to explain how a gas reservation policy is expected to affect domestic gas prices.',4),Q('Evaluate a domestic gas reservation scheme as a microeconomic policy.',6)],
 note='UPDATE DUE: Senate vote. The exporter objections are the digest\'s expectation of the argument, not quoted positions. Check the ABS source for the energy exports figure before quoting it.')

i='2026-10-29-chalmers-rules-out-fuel-discount'
add(id=i,title='Chalmers rules out a new fuel discount and promises budget savings',date='2026-10-29',type='news',outlets=['ABC News'],
 summary='Shows how a fuel excise cut would work against the RBA, with an AD/AS diagram, for answers on the policy mix. Replaces the 28 October edition.',
 lede='After inflation jumped to 4.3%, Treasurer Jim Chalmers said a new fuel excise discount is unlikely because the budget cannot afford it forever, and flagged savings in the mid-December MYEFO. The Prime Minister ruled out cuts to hospitals and schools, and the Coalition wants a discount funded by spending cuts.',
 about={'h09':['4C.1','4C.2','4B.1'],'y12':['Y2b.3','Y2b.13','Y2b.14'],'y11':[]},also={'h09':['4D.1','3C.3'],'y12':['Y2b.9','Y2c.7','Y1c.4'],'y11':[]},
 issues=['budget','inflation','rates'],levers=['fiscal','monetary'],diagrams=['adas','flow'],
 figures=[F('Fuel prices','+9.4% in September; almost 24% over the year','September 2026','inflation','ABS via ABC News'),F('Annual CPI','4.3%','September 2026','inflation','ABS'),F('MYEFO','mid-December 2026, with savings','December 2026','budget','ABC News'),F('Cash rate expected after Tuesday','4.85%','3 November 2026','rates','ABC News')],
 terms=[T('Fuel excise','A per-litre tax on fuel.'),T('MYEFO','The Mid-Year Economic and Fiscal Outlook, which updates the budget.'),T('Fiscal stance','Whether the budget adds to (expansionary) or subtracts from (contractionary) aggregate demand.')],
 links=[['ABC News, Jim Chalmers resists blame for another high inflation result, 28 Oct 2026',CH],L_PB],
 file=fl(i),angle='A fuel excise cut lowers measured CPI briefly, but households spend the savings elsewhere, shifting AD right and pushing prices up, so fiscal and monetary policy would pull in opposite directions. A contractionary stance supports the RBA.',
 questions=[Q('Explain how a fuel excise cut could reduce measured inflation in the short term but work against the RBA over time.',4),Q('Assess whether a contractionary fiscal stance would support monetary policy in the current economic conditions.',6)],
 note='Replaces the 28 October record from the same story. The government and Coalition positions are reported as each put them. UPDATE DUE: MYEFO in December.')

i='2026-10-29-small-business-slowdown-nairu'
add(id=i,title='Small business sales slow as banks debate how tight the labour market is',date='2026-10-29',type='stats',outlets=['Xero Small Business Insights','ABC News','CBA'],
 summary='Links evidence of a demand slowdown to the NAIRU, using CBA\'s 4.8% estimate against the RBA\'s 4.6%.',
 lede='Xero data show small business sales growth slowed to 5.2% a year in the September quarter from 7.3%, and small business wage growth halved to 1.2%. CBA estimates the NAIRU at 4.8%, above the RBA\'s 4.6%, which would mean unemployment must rise further before inflation returns to target.',
 about={'h09':['3B.4','3B.2'],'y12':['Y1c.6','Y2c.5'],'y11':['P1e.7']},also={'h09':['4D.3','3C.3'],'y12':['Y1b.11','Y2c.8'],'y11':['P1e.5']},
 issues=['employment','inflation','rates','growth'],levers=['monetary'],diagrams=['phillips','flow'],
 figures=[F('Small business sales growth, annual','5.2% (from 7.3%)','September quarter 2026','growth','Xero Small Business Insights'),F('Small business wage growth','1.2% (from 2.3%)','September quarter 2026','employment','Xero Small Business Insights'),F('Retail / hospitality sales growth','+2.4% / +2.7%','September quarter 2026','growth','Xero Small Business Insights'),F('NAIRU estimate: CBA / RBA','4.8% / 4.6%','October 2026','employment','CBA; RBA via ABC News')],
 terms=[T('NAIRU','The lowest unemployment rate consistent with stable inflation.'),T('Discretionary spending','Non-essential purchases households can delay.'),T('Phillips curve','The relationship between inflation and unemployment.')],
 links=[L_MK],
 file=fl(i),angle='The NAIRU cannot be observed, only estimated, and different estimates explain why economists disagree on how much tightening is needed. A higher NAIRU means the RBA must slow the economy further.',
 questions=[Q('Define the NAIRU and explain why a higher estimate implies tighter monetary policy.',3),Q('Explain why monetary policy may affect small businesses and some sectors more than others.',4)],
 note='Xero figures are sample data from its customers, reported second-hand through an ABC live blog. Complements the 27 October small business squeeze item (CreditorWatch and MYOB).')

i='2026-10-29-no-painless-way-out-on-inflation'
add(id=i,title='Inflation at 4.3%: why there is no painless way out',date='2026-10-29',type='news',outlets=['ABC News','ABS'],
 summary='Why cutting demand is the reliable cure for inflation and what it costs, with an AD/AS diagram and the case for productivity growth. Replaces the earlier edition of the same analysis.',
 lede='An ABC analysis argues the narrow path to a soft landing promised in 2022 has failed, with a Middle East energy shock and an AI-driven investment boom keeping prices high. The RBA is expected to lift the cash rate to 4.85% on Tuesday; spending cuts and tax rises are politically hard and productivity growth is the root fix that no one knows how to engineer.',
 about={'h09':['3C.3','4B.1','4E.1','3A.6'],'y12':['Y2d.1','Y2d.2','Y1a.10'],'y11':[]},also={'h09':['4D.2','4D.3'],'y12':['Y1c.4','Y2c.8'],'y11':['P3c.4']},
 issues=['inflation','productivity','rates'],levers=['monetary','fiscal','micro'],diagrams=['adas','flow'],
 figures=[F('Annual CPI','4.3% (August 4.0%)','September 2026','inflation','ABS'),F('Trimmed mean','about 3.6-3.7%','September 2026','inflation','ABS via ABC News'),F('RBA inflation target','2-3%','2026','inflation','RBA'),F('Cash rate expected after Tuesday','4.85% (highest in about 18 years)','3 November 2026','rates','ABC News analysis')],
 terms=[T('Soft landing','Slowing inflation without causing a recession.'),T('Demand-pull inflation','Prices rise because spending outpaces the economy\'s capacity.'),T('Productivity','Output per unit of input, such as per hour worked.')],
 links=[['Tom Crowley, Bad inflation result lays bare the ugly truth: there is no easy way out, ABC News (analysis), 29 Oct 2026','https://www.abc.net.au/news/2026-10-29/bad-inflation-result-political-pressure/107318484'],['ABS, CPI rose 4.3% in the year to September 2026','https://www.abs.gov.au/media-centre/media-releases/cpi-rose-43-year-september-2026']],
 file=fl(i),angle='Lower demand reduces the price level but also real GDP and jobs, a conflict between price stability and growth. Only a rightward shift of supply (productivity) could lower prices and raise output. Economist Chris Richardson urges governments at least not to add stimulus.',
 questions=[Q('Explain why reducing aggregate demand is described as the most reliable cure for inflation, and identify its costs.',4),Q('Discuss the role of productivity growth in achieving both low inflation and sustainable growth.',6)],
 note='An analysis piece, so treat it as one view. Replaces the earlier record from the same article. UPDATE DUE: RBA decision on 3 November.')

i='2026-10-29-australia-eu-fta-stalls-in-parliament'
add(id=i,title='Australia-EU free trade deal stalls in Parliament',date='2026-10-29',type='news',outlets=['ABC News','Prime Minister\'s press conference'],
 summary='Shows the political stalemate over a bilateral FTA and why agricultural access is the hardest part of trade liberalisation, with a tariff diagram.',
 lede='The Prime Minister says the deal makes 98% of Australian exports to the EU tariff-free and would add about $10 billion to the economy, but the Coalition will not support it in its current form, so there is no vote this week. The Nationals want better access for farmers and the Greens are leaning towards support.',
 about={'h09':['2D.2','2D.1','1B.4'],'y12':['Y3a.13','Y3a.16','Y3a.8'],'y11':[]},also={'h09':['1C.2','2D.3'],'y12':['Y3a.5','Y3a.7','Y3a.11'],'y11':['P6a.1']},
 issues=['trade','global'],levers=['trade'],diagrams=['ds'],
 figures=[F('Australian exports to the EU that would be tariff-free','98% (Prime Minister)','29 October 2026','trade','Prime Minister\'s press conference'),F('EU market','450 million people','2026','trade','Prime Minister\'s press conference'),F('Claimed boost to the economy','about $10 billion','2026','trade','Prime Minister\'s press conference'),F('Beef / sheepmeat access','about 8 times / 4 times current levels; review after five years','2026','trade','Prime Minister\'s press conference')],
 terms=[T('Tariff','A tax on imports.'),T('Tariff-rate quota','A volume that can enter at a low tariff; imports above it pay a much higher rate.'),T('Bilateral FTA','An agreement between two parties to reduce trade barriers.')],
 links=[L_PB,L_PM],
 file=fl(i),angle='The tariff diagram shows who wins and loses from protection: EU farmers and the government gain; consumers and efficient foreign exporters lose. Agricultural quotas also stalled negotiations in 2023.',
 questions=[Q('Explain why agricultural market access is often the hardest part of negotiating a free trade agreement.',4),Q('Assess the likely costs and benefits of the Australia-EU FTA for Australian producers and consumers.',6)],
 note='The $10 billion figure is the Prime Minister\'s claim and differs from the A$2 billion of new trade quoted in the 28 October Conversation article; compare the two when evaluating claims. UPDATE DUE: parliamentary vote.')

i='2026-10-29-aud-steady-iron-ore-flat-oil-high'
add(id=i,title='Dollar steady near 70.5 US cents as iron ore flatlines and oil stays high',date='2026-10-29',type='stats',outlets=['ABC News'],
 summary='Combines terms of trade with the interest rate differential, showing why the AUD moves less when the Fed is also expected to hike. Replaces the 23 October edition.',
 lede='The Australian dollar closed flat at 70.52 US cents on 29 October, iron ore was unchanged at US$90.70 a tonne and Brent crude stayed near US$114. Markets price about an 85% chance of an RBA rise on Tuesday and about an 80% chance of a US Fed hike in December, which pull the dollar in opposite directions.',
 about={'h09':['2C.2','2C.3','2C.6'],'y12':['Y3c.2','Y3c.4','Y3c.5','Y1a.7'],'y11':['P6c.1']},also={'h09':['2A.1','2C.4','3D.3','4D.3'],'y12':['Y3c.1','Y3c.6','Y3e.3'],'y11':['P6a.2','P6c.2']},
 issues=['fx','trade','rates'],levers=['monetary'],diagrams=['fx','flow'],
 figures=[F('Australian dollar','70.52 US cents (high about 70.70)','close, 29 October 2026','fx','ABC News'),F('Iron ore','US$90.70 a tonne (unchanged)','29 October 2026','trade','ABC News'),F('Gold','US$4,039 an ounce (-0.7%)','29 October 2026','trade','ABC News'),F('Brent crude','near US$114','29 October 2026','trade','ABC News'),F('Market odds: RBA hike Tuesday / US Fed hike in December','about 85% / about 80%','29 October 2026','rates','ABC News'),F('RBA cash rate before Tuesday','4.60%','29 October 2026','rates','RBA')],
 terms=[T('Terms of trade','Export prices divided by import prices, times 100.'),T('Interest rate differential','The gap between Australian and overseas rates, which drives short-term capital flows.'),T('Commodity prices','The prices of raw materials such as iron ore and oil.')],
 links=[L_MK],
 file=fl(i),angle='Exchange rates depend on relative, not absolute, interest rates, so combine the differential with commodity prices. Flat iron ore receipts and expensive oil imports put downward pressure on the terms of trade.',
 questions=[Q('Explain how an increase in the RBA cash rate, with US rates unchanged, would be expected to affect the value of the AUD.',3),Q('Explain how high oil prices combined with flat iron ore prices affect Australia\'s terms of trade.',4)],
 note='Single-day figures, so update before quoting. UPDATE DUE: RBA decision on 3 November. Overlaps with the 28 October item on the AUD and rate hike bets, which is kept because it covers the NZ dollar move.')

i='2026-10-29-central-banks-split-on-oil-shock'
add(id=i,title='One oil shock, three answers: Canada hikes while Europe and New Zealand hold',date='2026-10-29',type='news',outlets=['Bank of Canada','ECB','ABC News'],
 summary='Why central banks respond differently to the same supply shock, with the SRAS dilemma diagram. Replaces the 25 October preview with the actual decisions.',
 lede='The Bank of Canada raised its rate 25 basis points to 2.50%, its first hike in three years, while the ECB held its deposit rate at 2.50% and the RBNZ held at 2.75%, surprising markets that expected a hike. The US Fed held its range at 3.75-4% in a 10-2 vote.',
 about={'h09':['1A.4','3C.3','4D.2','4D.3'],'y12':['Y2c.8','Y1c.4','Y2c.7'],'y11':[]},also={'h09':['2C.2','4H.2','2C.6'],'y12':['Y3c.4','Y3c.5','Y3e.3'],'y11':['P4c.3']},
 issues=['global','inflation','rates'],levers=['monetary','global'],diagrams=['adas','flow'],
 figures=[F('Bank of Canada rate','2.50% (+25 basis points; first hike in three years)','28 October 2026','rates','Rio Times'),F('Canada: inflation / petrol / inflation excluding petrol','3.1% / +27.8% / 2.2%','28 October 2026','inflation','Rio Times'),F('Canada expects inflation near 3.5% by year-end and growth of','1% in 2026','28 October 2026','inflation','Rio Times'),F('ECB deposit rate','2.50% (held, after a September hike)','29 October 2026','rates','Cyprus Mail'),F('RBNZ cash rate','2.75% (held; NZ dollar fell 1.2%)','28 October 2026','rates','ABC News'),F('US Fed target range','3.75-4% (held, 10-2 vote)','28 October 2026','rates','ABC News')],
 terms=[T('Second-round effects','When an initial price shock flows into wage claims and other prices, making inflation persistent.'),T('Basis point','0.01 percentage points.'),T('Supply shock','An unexpected change in the supply of a key input that shifts costs across the economy.')],
 links=[['Rio Times, Bank of Canada rate decision, 28 October 2026','https://riotimesonline.com/bank-of-canada-rate-decision-28-october-2026/'],['Cyprus Mail, ECB holds interest rates steady as energy shock threatens inflation and growth, 29 Oct 2026','https://cyprus-mail.com/2026/10/29/ecb-holds-interest-rates-steady-as-energy-shock-threatens-inflation-and-growth'],L_MK],
 file=fl(i),angle='Monetary policy cannot fix a supply shock; it can only stop the first-round price rise turning into persistent inflation. Canada judged the inflation risk larger, while the ECB and RBNZ weighted weak growth more heavily.',
 questions=[Q('Explain why central banks might respond differently to the same rise in world oil prices.',4),Q('Distinguish between first-round and second-round effects of an oil price shock.',3)],
 note='Replaces the 25 October preview with the actual decisions. Christine Lagarde will leave the ECB early in February 2027, according to the digest. Figures are as reported by smaller outlets (Rio Times, Cyprus Mail) and were not checked against the central banks.')

i='2026-10-28-saudi-refinery-strike-oil-near-115'
add(id=i,title='Missile strike on Saudi refinery keeps oil near US$115',date='2026-10-28',type='news',outlets=['Reuters via RTE','ABC News'],
 summary='A live supply shock: why a small fall in supply causes a large price rise when demand is inelastic, and how it reaches Australian fuel prices. Replaces the 25 October item.',
 lede='Yemen\'s Houthis claimed a missile hit Saudi Arabia\'s biggest refinery, which can process 550,000 barrels a day; Saudi authorities had not immediately confirmed the strike. Brent crude rose about 1% to US$115.02 a barrel on 28 October and eased to about US$113.90 on Thursday.',
 about={'h09':['3C.3','1A.1'],'y12':['Y1c.4','Y1c.5','Y3e.3'],'y11':[]},also={'h09':['3C.4','1A.8','4D.3','4B.1'],'y12':['Y1c.1','Y1a.10','Y2c.4','Y2c.8'],'y11':[]},
 issues=['inflation','global','trade'],levers=['monetary'],diagrams=['ds','adas','flow'],
 figures=[F('Brent crude','US$115.02 a barrel (+1%)','28 October 2026','global','Reuters via RTE'),F('US crude (WTI)','US$101.61 (+1.7%)','28 October 2026','global','Reuters via RTE'),F('Refinery capacity hit','550,000 barrels a day','28 October 2026','global','Reuters via RTE'),F('US crude stockpiles','fell about 2 million barrels','28 October 2026','global','Reuters via RTE'),F('Australian fuel prices','+9.4% in September','September 2026','inflation','ABS')],
 terms=[T('Supply shock','An unexpected change in the supply of a key input that shifts costs across the economy.'),T('Risk premium','The extra price traders pay because of the chance of future disruption.'),T('Price-inelastic demand','Demand that changes little when the price changes.')],
 links=[['Reuters via RTE, World oil prices, 28 Oct 2026','https://www.rte.ie/news/business/2026/1028/1597079-world-oil-prices/'],L_MK],
 file=fl(i),angle='In the short run oil demand is inelastic, so a small fall in quantity brings a big rise in price. For an oil-importing economy the shock shifts SRAS left: higher prices and lower output, leaving central banks with a policy dilemma.',
 questions=[Q('Draw an AD/AS diagram to show how a sustained rise in world oil prices affects output and the price level in an oil-importing economy.',4),Q('Explain why a supply shock creates a policy dilemma for central banks.',3)],
 note='The strike was claimed by the Houthis and not confirmed by Saudi authorities when reported. ING analysts expect a risk premium to remain until US policy towards Iran is clearer, possibly after the 3 November US midterms. OPEC+ meets on Sunday and is expected to hold output targets. Replaces the 25 October record on earlier Houthi attacks.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
