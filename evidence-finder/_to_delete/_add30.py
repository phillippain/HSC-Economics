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
      angle=angle,questions=questions,note=note,added='2026-11-27'))

ABC='ABC News'
def L(a,b): return [a,b]
H='https://www.abc.net.au/news/'
ETW='The Economy This Week'

R('2026-11-27-rba-expected-to-hold-4-85-despite-inflation-surprise','4','RBA expected to hold at 4.85% despite inflation surprise','2026-11-27','news',[ABC,'CommBank'],
 "Shows the RBA's 'worst nightmare' of rising inflation and unemployment together, with the Phillips curve shift and market pricing for 8 December.",
 "After five rate rises in 2026, markets and most economists expect the Reserve Bank to keep the cash rate on hold at its 8 December meeting. It faces the 'worst nightmare' of rising inflation and rising unemployment.",
 ['4D.1','4D.2','4D.3'],['Y2c.1','Y2c.2','Y2c.4','Y2c.5'],['P4c.3'],
 ['3C.3','4H.1'],['Y1c.6','Y2c.3'],['P4c.4'],
 ['rates','inflation','employment'],['monetary'],['phillips','flow','compare'],
 [F('Cash rate','4.85% (raised 0.25 percentage points on 3 November, 6-3 vote); highest since 2008','November 2026','rates','RBA'),
  F('Market-implied chance of a hold on 8 December','96.7% after the October CPI','November 2026','rates','ABC News'),
  F('RBA forecast for inflation back at the 2-3% target midpoint','About mid-2028','November 2026','inflation','RBA'),
  F('CommBank expectation','Cuts from August 2027; UBS and Betashares see a risk of a February hike','November 2026','rates','CommBank')],
 [T('Inflation expectations','What people expect prices to do, which shapes wages and prices.'),T('Time lags','The delay of up to 1-2 years before rate changes fully affect the economy.')],
 [L('ABC News: Inflation rises to 4.9pc, 25 Nov 2026',H),L('ABC News: markets blog, 25 Nov 2026',H),L('CommBank: RBA analysis, Nov 2026','https://www.commbank.com.au/')],
 "When inflation expectations rise, the short-run Phillips curve shifts up, so both inflation and unemployment rise: raising rates fights inflation but pushes unemployment higher still. The split vote shows the policy trade-off and is evidence of the limitations of monetary policy.",
 [Q("Explain the monetary policy transmission mechanism.",4),Q("Using a Phillips curve, explain the dilemma the RBA faces when inflation and unemployment rise together.",5)],
 "UPDATE DUE: RBA decision on 7-8 December. Market pricing and economist views, not decisions. Oxford Economics called rising inflation and unemployment together the RBA's 'worst nightmare'. Replaces the 25 November 'hold, hike or cut?' card (retained facts are in the figures above): that card also had 97% hold pricing, first cut pushed back from June to August 2027, Bullock's 'sustainably back to target' test and the cases for hiking and holding.")

R('2026-11-27-chalmers-promises-substantial-savings-december-update','4','Chalmers promises "substantial savings" in December budget update','2026-11-27','news',['Guardian (via CathNews)',ABC],
 "Shows fiscal policy being used to support the RBA when inflation is cost-push, and the limits of that approach.",
 "With inflation at 4.9%, the Treasurer says savings will be at the core of next month's MYEFO, with the aim that fiscal policy supports the RBA rather than adds to demand. He called the result 'a very serious moment' and said no amount of relief or savings would make it go away overnight.",
 ['4C.1','4C.2','4B.1'],['Y2b.3','Y2b.9','Y2b.13','Y2b.14'],['P5a.4','P5c.3'],
 ['4D.3','4H.3'],['Y2c.5'],['P5b.7'],
 ['budget','inflation'],['fiscal'],['adas','flow'],
 [F('Headline inflation','4.9% (the Treasurer\'s "very serious moment")','November 2026','inflation','ABS'),
  F('Minimum tax on discretionary trust distributions','30%, passed by Parliament after a Labor-Greens deal','November 2026','budget','Guardian, via CathNews'),
  F('Private health insurance rebate for over-65s','Deal exempts pensioners, forgoing about A$1.5 billion of the planned A$3 billion saving','November 2026','budget','ABC News')],
 [T('Contractionary fiscal policy','Cutting spending or raising taxes to slow aggregate demand.'),T('Policy mix','How fiscal and monetary policy work together.')],
 [L('CathNews (Guardian): Chalmers promises substantial savings','https://cathnews.com/'),L('ABC News: David Speers analysis, Nov 2026',H),L('ABC News: Federal politics blog, 26 Nov 2026',H)],
 "Today's inflation is largely cost-push (fuel, electricity), but fiscal tightening cuts demand-pull pressure, so it may do little to the CPI while hurting growth: a limitation of fiscal policy. ABC's David Speers argues spending cuts are unlikely to fix inflation and could risk recession as unemployment rises (analysis, not fact).",
 [Q("Explain how contractionary fiscal policy can complement monetary policy in reducing inflation.",4),Q("Assess whether fiscal tightening is appropriate when inflation is high but unemployment is rising.",6)],
 "UPDATE DUE: the MYEFO itself (December, after the RBA's 8 December meeting). Infrastructure spending is a possible target. Replaces the 24 November MYEFO savings card (lower tax receipts and bigger deficits in later years; net saving with savings exceeding new spending; EV and home-battery subsidies could be means-tested; Chalmers said no realistic savings will make inflation go away; Wilson's spending 'speed limit'; $25 PBS script price frozen). The 25 November critics card (mostly AFR opinion) is kept. The trust tax card has been updated to say the tax has now passed.")

R('2026-11-27-gas-reservation-scheme-set-to-become-law','4','Gas reservation scheme set to become law','2026-11-27','news',['AAP (Yahoo News)',ABC,'World Today Journal'],
 "Shows the final shape of the gas reservation policy, including amendments, and the trade-off between domestic energy costs and export income.",
 "Parliament is set to pass a national scheme forcing east-coast LNG exporters to keep up to 20% of their gas for Australian users, aiming to drive 'a permanent wedge' between export and domestic prices.",
 ['4E.1','4E.2'],['Y2d.1','Y2d.4','Y2d.5'],['P2i.2','P2i.3','P2i.4'],
 ['4H.3','2A.1'],['Y2d.6'],['P2d.1'],
 ['investment','inflation','trade'],['micro'],['ds','flow'],
 [F('Share of gas to be reserved for domestic users','Up to 20% for the largest LNG exporters from 1 January 2028','November 2026','investment','AAP'),
  F('East-coast wholesale gas prices versus WA','About double','November 2026','inflation','AAP'),
  F('Amendments','An "up to" 10% oversupply buffer and a review of the investment impact after five years','November 2026','investment','AAP'),
  F('Greens\' alternative: 25% gas export tax','Said to raise $17 billion a year','November 2026','budget','AAP')],
 [T('Export parity pricing','Domestic prices that track higher world (LNG) prices.'),T('Market intervention','Government action to change market outcomes.')],
 [L('Yahoo News (AAP): Gas reserve gets green light','https://au.news.yahoo.com/'),L('World Today Journal: Gas reservation from 2028','https://world-today-journal.com/'),L('ABC News: Federal politics blog, 26 Nov 2026',H)],
 "Reservation shifts domestic supply right (S1 to S2): domestic price falls and quantity rises, helping manufacturers and households, but exporters earn less than world prices and long-run investment in new supply may weaken.",
 [Q("Using a supply and demand diagram, explain the intended effect of the gas reservation scheme on domestic gas prices.",4),Q("Evaluate the scheme as a policy to reduce energy costs in Australia.",6)],
 "UPDATE DUE: confirm the House passed the amended bill (due Friday 27 November) and the start date. The Coalition agreed not to block the bill in the Senate on Thursday night but warned it could deter investment. WA is exempt because it has run its own reservation policy for two decades. Replaces the 25 November AFR card on the Coalition backing the scheme (Resources Minister Madeleine King on 'must sell' rules; Amplitude Energy's sovereign risk warning; Rod Sims' view). The 18 November WA carve-out card is kept.")

R('2026-11-27-rba-bulletin-small-businesses-squeezed','3','RBA: small businesses squeezed by weak demand and rising costs','2026-11-27','report',['RBA Bulletin'],
 "Gives official RBA evidence on how tight monetary policy reaches small businesses, with a bright spot in AI adoption.",
 "A new RBA Bulletin finds small business conditions have deteriorated over the past year. Higher interest rates are working through to the firms that employ a large share of Australians.",
 ['4D.3','3A.7','3C.3'],['Y2c.5','Y1a.14','Y1a.10'],['P4c.3','P1e.7'],
 ['3A.6'],['Y1c.4'],['P3c.5'],
 ['rates','growth','productivity','employment'],['monetary'],['flow','chart'],
 [F('Small businesses reporting difficulty getting finance','About 1 in 5','November 2026','rates','RBA Bulletin'),
  F('Extra borrowing cost for small businesses over large firms','About 75 basis points (historic low)','November 2026','rates','RBA Bulletin'),
  F('Small business credit secured by residential property','About 50%','November 2026','housing','RBA Bulletin'),
  F('SMEs reporting material efficiency gains from AI','About 20% already; about 40% expect gains within a year','November 2026','productivity','Macquarie BOSS survey, cited in RBA Bulletin')],
 [T('Profit margin squeeze','Costs rise faster than the prices firms can charge.'),T('Insolvency','When a business cannot pay its debts as they fall due.')],
 [L('RBA Bulletin: Small business conditions, 26 Nov 2026','https://www.rba.gov.au/publications/bulletin/')],
 "Small businesses feel tight monetary policy through the cash-flow channel (higher loan repayments) and weaker household spending; with about half of small business credit secured on housing, a weak housing market can also restrict finance. Financial stress is expected to rise most in construction, hospitality and retail (hospitality has the highest insolvency rate).",
 [Q("Explain how tight monetary policy affects small businesses.",4),Q("Assess the potential of AI adoption to improve productivity in Australia.",5)],
 "Official RBA analysis (a Bulletin article), so a strong source; AI shares quoted are from a Macquarie BOSS survey cited in it (approximate: 20% already, 40% expect, 23% no material change, 16% too early to say). Related earlier small business cards in this series are kept. The link goes to the RBA Bulletin index because the digest gives the title only.")

R('2026-11-27-home-building-lifts-construction-ahead-of-gdp','3','Home building lifts construction activity ahead of next week\'s GDP','2026-11-27','news',['ABS',ABC],
 "Shows how partial indicators are used to forecast GDP, and links residential investment to growth, capacity and housing costs.",
 "Construction work done rose 0.9% in the September quarter, above the 0.7% consensus, led by residential building. It is one of the partial indicators economists use to forecast GDP before the National Accounts are released next week.",
 ['3A.4','3A.5','3A.1'],['Y1a.3','Y1a.6','Y1a.10'],['P1e.1'],
 ['4E.1','3C.3'],['Y2d.3','Y1c.4'],[],
 ['growth','housing','investment','inflation'],[],['chart','flow','adas'],
 [F('Total construction work done, September quarter','+0.9% (consensus +0.7%): building +2.4%, residential +3.1%, engineering -0.9%','September quarter 2026','growth','ABS, via ABC News'),
  F('Q3 GDP forecast','JP Morgan 0.4% q/q; NAB estimates residential building adds about 0.1 percentage points to GDP growth','September quarter 2026','growth','ABC News')],
 [T('Partial indicator','Data on one part of the economy used to forecast GDP.'),T('Residential investment','Spending on new homes and renovations (part of I).')],
 [L('ABC News: markets blog, 25 Nov 2026',H)],
 "Construction feeds into GDP through investment (I). More dwellings over time should ease rent and price pressures, though housing and data centres are meanwhile competing for scarce tradespeople and materials (adding to inflation now but expanding capacity later).",
 [Q("Explain how economists use partial indicators such as construction work done to forecast GDP.",3),Q("Explain how increased housing construction could affect inflation over time.",4)],
 "UPDATE DUE: Q3 GDP (National Accounts, 2 December). Replaces the 25 November 'Record home building as the AI boom stretches capacity' card: the figures and dot points are carried over, including the record real residential building of about $30.4 billion, non-residential construction +10.2% over the year, new home building costs +5.1% over the year (SMH/AFR/ABS) and Shane Wright's point that data centres and homes need the same electricians and plumbers. Housing costs rose 6.4% over the year in the CPI.")

R('2026-11-27-data-centre-boom-biggest-investment-jump-since-2011','3','Data centre boom drives the biggest investment jump since 2011','2026-11-27','news',['ABS','TechTimes'],
 "Shows why a large investment boom adds less to GDP than the headline suggests, because the equipment is imported.",
 "Business investment surged in the September quarter as firms poured money into data centre equipment. But because most of that equipment is imported, the boost to Australia's GDP is much smaller than the headline.",
 ['3A.1','3A.5','2B.1'],['Y1a.6','Y1a.10','Y3b.1'],['P3c.4','P3c.5'],
 ['2B.4','3D.1'],['Y1a.12'],['P6b.1'],
 ['investment','growth','productivity','trade'],[],['adas','flow'],
 [F('Private new capital expenditure, September quarter','+12.2% (+18.6% over the year): largest quarterly rise since the 2011 mining boom','September quarter 2026','investment','ABS'),
  F('Equipment investment','Record, +23.1%; information media and telecommunications equipment +183.5%','September quarter 2026','investment','ABS'),
  F('Buildings and structures','+1.7%','September quarter 2026','investment','ABS'),
  F('Expected 2026-27 capex revised','Up 11.8%','2026-27','investment','ABS'),
  F('Share of data centre equipment that is imported','About 70% (RBA Governor Bullock estimate)','November 2026','trade','TechTimes')],
 [T('Capital expenditure','Business spending on buildings, machinery and equipment.'),T('Leakage','Spending that flows to imports rather than domestic production.')],
 [L('ABS: Data centre investment drives new capex, 26 Nov 2026','https://www.abs.gov.au/'),L('TechTimes: Capex jumps 12%','https://www.techtimes.com/')],
 "Remember AD = C + I + G + (X - M): investment financed by imports raises I and M together, so the real shift in AD is smaller than a 12% rise in capex suggests, and the current account deficit widens. Over time the data centre build-out expands productive capacity.",
 [Q("Explain why a large rise in business investment may add relatively little to GDP growth.",4),Q("Discuss how the data centre boom could affect Australia's long-term productive capacity.",5)],
 "The 70% imported share is attributed to Governor Bullock via TechTimes (second-hand). Victoria (+31.0%) and NSW (+9.6%) led. Related 17 November data centre cards and 25 November record home building card (now replaced by the 27 November construction card). UPDATE DUE: Q3 GDP, 2 December. Links to home pages where the digest gives titles only.")

R('2026-11-27-october-inflation-jumps-4-9-highest-in-three-years','3','Inflation jumps to 4.9%, its highest in three years','2026-11-27','news',['ABS',ABC,'Guardian (via CathNews)'],
 "Gives the October CPI with headline and underlying measures and shows the unequal burden of non-discretionary price rises.",
 "The October CPI showed inflation rising faster than expected, driven by fuel and the end of electricity rebates. The Treasurer called it 'a very serious moment' for the economy.",
 ['3C.1','3C.2','3C.3','3C.4'],['Y1c.2','Y1c.3','Y1c.4','Y1c.7'],['P2c.4'],
 ['4D.3'],['Y1c.5','Y1c.9'],[],
 ['inflation'],['monetary'],['adas','chart','flow'],
 [F('Non-discretionary versus discretionary prices','+6.1% versus +3.2% over the year','October 2026','inflation','ABS'),
  F('Headline CPI and trimmed mean','4.9% (September 4.3%) and 3.8% (September 3.6%), against a 2-3% target','October 2026','inflation','ABS'),
  F('Electricity, fuel, housing over the year','+25.2%, +32.5%, +6.4%','October 2026','inflation','ABS')],
 [T('Trimmed mean','An underlying inflation measure that removes the largest price rises and falls.'),T('Non-discretionary','Essentials households cannot easily cut, such as fuel and power.')],
 [L('ABS: Consumer Price Index, October 2026','https://www.abs.gov.au/'),L('ABC News: Inflation rises to 4.9pc, 25 Nov 2026',H),L('CathNews (Guardian): Chalmers','https://cathnews.com/')],
 "The RBA looks through one-off shocks such as rebates ending, but the rising trimmed mean and inflation expectations suggest more persistent pressure. Rising non-discretionary prices hit low-income households hardest, linking inflation to the distribution of income.",
 [Q("Distinguish between headline and underlying inflation, using October 2026 data.",3),Q("Explain why rising non-discretionary prices affect low-income households most.",4)],
 "Replaces the 25 November CPI card on the same release: its details are carried over in the figures, dot points and links (including tradables +5.3% and non-tradables +4.7%, rents +3.5%, toys and games +13%, and the home-grown versus imported debate from the AFR and SMH). UPDATE DUE: November CPI and the RBA decision on 8 December. The 4.9% inflation rate coincides with the 4.9% unemployment rate.")

R('2026-11-27-aud-weakest-since-december-despite-hot-cpi','2','Australian dollar slides to its weakest level since December','2026-11-27','news',[ABC],
 "Shows why the AUD fell despite high inflation, with commodity prices and risk-off selling outweighing interest rates.",
 "Even though inflation came in high, the dollar fell rather than rose. Weaker commodity prices and global risk-off selling outweighed the pull of higher Australian interest rates.",
 ['2C.2','2C.3','2C.6'],['Y3c.2','Y3c.4','Y3c.5','Y3c.6'],['P6c.1'],
 ['4D.3','2B.4'],['Y1a.7','Y2c.5'],['P4c.3'],
 ['fx','rates','trade','inflation'],['monetary'],['fx','flow'],
 [F('AUD / USD on Wednesday 25 November','About 65.9 US cents (-0.7%), lowest since December; briefly towards 66.7c on the CPI release; steady at 66.25c on Thursday morning','25-26 November 2026','fx','ABC News'),
  F('Copper and iron ore','Copper -4.8% on Wednesday; iron ore near four-year lows (about US$88 a tonne)','25 November 2026','trade','ABC News'),
  F('Chance the RBA holds on 8 December','96.7%','November 2026','rates','ABC News')],
 [T('Risk-off','Investors sell riskier assets, often including the AUD.'),T('Interest rate differential','The gap between Australian and overseas rates, which drives capital flows.')],
 [L('ABC News: markets blog, 25 Nov 2026',H),L('ABC News: markets blog, 26 Nov 2026',H)],
 "Lower commodity prices mean foreign buyers need fewer Australian dollars, and risk-off investors sell AUD assets, so demand shifts left and the AUD depreciates. A lower AUD makes exports more competitive but raises import prices including fuel, adding to imported inflation when the CPI is already 4.9%.",
 [Q("Explain two reasons the AUD fell this week despite high Australian inflation.",4),Q("Using a diagram, explain the effect of a depreciation on Australia's inflation rate.",4)],
 "Replaces the 25 November card on the 11-month low (CommBank/AAP, ABC, AFR): carried over in the merged figures and links. The two cards give slightly different details of the same day (CPI-day spike to about 66.6c versus 66.7c; copper -5% versus -4.8%): single-day market prices. The 'weakest since December' framing agrees with the 'lowest in 11 months'.")

R('2026-11-27-iron-ore-below-us90-china-buying-bloc','2','Iron ore stuck below US$90 as China\'s buying bloc flexes its muscle','2026-11-27','news',['Reuters (via Investing.com)',ABC],
 "Shows China's buyer power in iron ore price talks and what falling prices mean for terms of trade, income and government revenue.",
 "Australia's biggest export is trading near four-year lows. China's state-run buyer is using its market power in annual supply talks with BHP, Rio Tinto and Fortescue, which threatens Australian export income and tax revenue.",
 ['2B.4','2A.1','2D.4','2C.6'],['Y1a.7','Y3e.1','Y3c.6'],['P6a.2'],
 ['3D.1'],['Y3a.15','Y3c.4'],[],
 ['trade','fx','budget'],['trade'],['ds','flow'],
 [F('Iron ore','US$88.30 a tonne on Thursday 26 November (-0.5%); SGX benchmark below US$90 for the first time in four years','26 November 2026','trade','Reuters; ABC News'),
  F('Australian iron ore exports','About A$107 billion in 2026-27 (estimate)','2026-27','trade','ABC News'),
  F('Goldman Sachs cut to miners\' earnings forecasts','Up to US$9 billion over a decade','November 2026','trade','Goldman Sachs, via Reuters')],
 [T('Market power','The ability of a buyer or seller to influence price.'),T('Commodity dependence','Reliance on a few raw-material exports for income.')],
 [L('Reuters via Investing.com: BHP, Rio meet China leaders','https://www.investing.com/'),L('ABC News: markets blog, 26 Nov 2026',H)],
 "Weaker Chinese demand shifts the iron ore demand curve left, lowering price and quantity. Lower iron ore prices cut the terms of trade, export income, company tax and royalty revenue and put downward pressure on the AUD. Assess the risks of dependence on China as an export market.",
 [Q("Explain how a fall in iron ore prices affects Australia's terms of trade and current account balance.",4),Q("Assess the risks of Australia's dependence on China as an export market.",6)],
 "China Mineral Resources Group (CMRG), the state's central iron ore buyer, has banned steelmakers from buying certain products from BHP, Rio and Fortescue during supply talks (reported second-hand by Reuters); Resources Minister Madeleine King warned price manipulation would breach international rules. BHP and Rio executives joined a CEO roundtable with Premier Li Qiang in Beijing. Related: 18 November CMRG haggling analysis and the 23 November iron ore card (kept; iron ore prices there are US$88.50 and US$90.6 on other dates). Link 1 goes to the Investing.com home page because the digest gives the title only.")

R('2026-11-27-oil-climbs-again-hormuz-disruption-drags-on','1','Oil climbs again as Strait of Hormuz disruption drags on','2026-11-27','news',[ABC,'ABS','CommBank'],
 "Shows an oil supply shock transmitted to Australian petrol prices and inflation, with the price-inelastic demand diagram.",
 "Brent crude jumped 3.7% on Thursday as shipping through the Strait of Hormuz stayed disrupted. A supply shock in the Middle East is now showing up directly in Australian petrol prices and inflation.",
 ['3C.3','1A.1','1A.8'],['Y1c.4','Y1c.5','Y3e.3'],['P2c.4','P2d.1','P2d.2'],
 ['2B.4','3F.4'],['Y1c.8'],['P1e.6'],
 ['inflation','global'],[],['ds','adas','flow'],
 [F('Brent crude on Thursday 26 November','US$94.76 a barrel (+3.7%), after slipping 1.4% to US$90.10 the day before','26 November 2026','inflation','ABC News'),
  F('Australian automotive fuel prices','+6.3% in October and +32.5% on a year ago','October 2026','inflation','ABS'),
  F('Fuel\'s contribution to the rise in annual inflation to 4.9%','About 0.3 of the 0.6 percentage point rise','October 2026','inflation','Treasurer, via ABC News')],
 [T('Supply shock','A sudden event that cuts (or raises) supply and shifts the supply curve.'),T('Price-inelastic demand','Quantity demanded changes little when the price changes.')],
 [L('ABC News: markets blog, 26 Nov 2026',H),L('ABS: Consumer Price Index, October 2026','https://www.abs.gov.au/'),L('CommBank: RBA analysis','https://www.commbank.com.au/')],
 "In the short run demand for oil is price-inelastic, so a supply cut (S1 to S2) lowers quantity only slightly but lifts the price sharply. On an AD/AS diagram the same shock shifts SRAS left, raising prices and reducing output: stagflation.",
 [Q("With the aid of a diagram, explain why oil prices rise sharply when supply is disrupted.",4),Q("Explain how a global oil price shock affects Australia's inflation and economic growth.",4)],
 "Replaces the 19 November oil card, whose figures and dot points are carried over (Brent about US$91-93; Goldman Sachs 2027 surplus forecast of about 2 million barrels a day with Brent averaging US$88 is a forecast). Brent moves daily: US$88.97 on 24 November (lowest close since 31 August), US$90.10 on 25 November and US$94.76 on 26 November. The 24 November Russian oil flows card is kept. CommBank economists list Middle East-linked fuel and commodity prices among the RBA's main inflation concerns.")

R('2026-11-27-us-excess-capacity-tariffs-14-economies','1','US targets 14 economies with new "excess capacity" tariffs','2026-11-27','news',['Al Jazeera','Reuters',ABC],
 "Gives a live case of protectionism under Section 301 and shows how Australia can be affected through China and Asia even though it is not targeted.",
 "Washington has proposed a fresh round of Section 301 tariffs on 14 economies it says produce far more manufactured goods than their own markets can absorb. China faces the steepest rate. Australia was not on the list.",
 ['1C.2','1C.1','2D.4','1B.2'],['Y3a.6','Y3a.7','Y3a.8','Y3a.11','Y3a.14'],['P6a.1'],
 ['2A.1'],['Y3a.15','Y3e.3'],['P6a.2'],
 ['trade','global'],['trade'],['ds','flow'],
 [F('Proposed tariff on China','An extra 20% on top of about 25% from Trump\'s first term','25 November 2026','trade','Al Jazeera / Reuters'),
  F('Rate caps under existing deals','15% for the EU, Japan and Korea; 19% for Malaysia','November 2026','trade','Al Jazeera / Reuters'),
  F('China\'s 2026 trade surplus','On track for a record, above US$1 trillion','2026','trade','Al Jazeera / Reuters'),
  F('Nasdaq on the day','Ended 0.6% lower after falling more than 4% early in the session','25 November 2026','global','Reuters')],
 [T('Section 301','US trade law letting the President act against unfair foreign trade practices.'),T('Trade diversion','Trade shifting to untaxed suppliers when tariffs hit others.')],
 [L('Al Jazeera: Which countries are affected?, 25 Nov 2026','https://www.aljazeera.com/'),L('Al Jazeera/Reuters: World reacts, 25 Nov 2026','https://www.aljazeera.com/'),L('ABC News: markets blog, 26 Nov 2026',H)],
 "Apply the tariff diagram (price rises to Pw+t, imports shrink, revenue and deadweight loss). Tariffs on China and ASEAN can divert their surplus goods to other markets including Australia (lower import prices but competition for local manufacturers), and slower Asian growth means weaker demand for Australian resources and a lower terms of trade.",
 [Q("Using a tariff diagram, explain how the proposed US tariffs affect US consumers, producers and government.",5),Q("Discuss how Australia could be affected even though it is not targeted.",4)],
 "PROPOSED, not in force; China called overcapacity a 'false issue' and the EU rejected the premise. Replaces the 25 November card on the same announcement. NOTE a discrepancy: the 25 November digest reported US shares falling sharply (Nasdaq -3.9%, S&P 500 -2.8%), while this digest says the Nasdaq ended 0.6% lower after an early fall of more than 4%; check the sources. This digest also says Australia 'still faces the separate 12.5% tariff the US imposed in July': that figure has been reported elsewhere as the Philippines' rate (July tariffs of 10-12.5% on 60 economies), so check before quoting. UPDATE DUE: final rates and start date; G20 meetings in mid-December.")

recs=[r for r in recs if r['id'] not in have]
MERGE={
 '2026-11-27-rba-expected-to-hold-4-85-despite-inflation-surprise':'2026-11-25-rba-december-dilemma-hold-hike-or-cut',
 '2026-11-27-chalmers-promises-substantial-savings-december-update':'2026-11-24-myefo-substantial-savings-budget-weakens',
 '2026-11-27-gas-reservation-scheme-set-to-become-law':'2026-11-25-coalition-backs-labor-20-per-cent-gas-reservation',
 '2026-11-27-home-building-lifts-construction-ahead-of-gdp':'2026-11-25-record-home-building-ai-boom-capacity',
 '2026-11-27-october-inflation-jumps-4-9-highest-in-three-years':'2026-11-25-inflation-hits-4-9-per-cent-october-cpi',
 '2026-11-27-aud-weakest-since-december-despite-hot-cpi':'2026-11-25-aud-slides-11-month-low-hot-cpi',
 '2026-11-27-oil-climbs-again-hormuz-disruption-drags-on':'2026-11-19-oil-holds-above-us90-middle-east-surplus',
 '2026-11-27-us-excess-capacity-tariffs-14-economies':'2026-11-25-us-overcapacity-tariffs-14-economies',
}
byid={x['id']:x for x in d}
def uni(a,b):
    out=list(a)
    for v in b:
        if v not in out: out.append(v)
    return out
for r in recs:
    o=byid.get(MERGE.get(r['id']))
    if not o: continue
    for k in ('h09','y12','y11'):
        r['about'][k]=uni(r['about'][k],o['about'].get(k,[]))
        r['also'][k]=[c for c in uni(r['also'][k],o['also'].get(k,[])) if c not in r['about'][k]]
    for k in ('issues','levers','diagrams'): r[k]=uni(r[k],o.get(k,[]))
    labels={f['label'] for f in r['figures']}
    r['figures']+= [f for f in o['figures'] if f['label'] not in labels]
    tn={t['term'] for t in r['terms']}
    r['terms']+= [t for t in o['terms'] if t['term'] not in tn]
    ul={l[1] for l in r['links']}
    r['links']+= [l for l in o['links'] if l[1] not in ul]
    qs={q['q'] for q in r['questions']}
    r['questions']+= [q for q in o['questions'] if q['q'] not in qs]
REMOVE=set(MERGE.values())
d=[x for x in d if x['id'] not in REMOVE]
for x in d:
    if x['id']=='2026-11-25-trust-tax-passes-greens-private-jet-levy' and 'PASSED' not in x['note']:
        x['note']='UPDATE (27 November digest): Parliament has now PASSED the 30% minimum tax on discretionary trust distributions after the Labor-Greens deal. '+x['note']
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(REMOVE),'replaced',len(d),'total')
