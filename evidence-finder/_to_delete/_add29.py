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
      angle=angle,questions=questions,note=note,added='2026-11-26'))

ABC='ABC News'
def L(a,b): return [a,b]
AFR='https://www.afr.com/'
H='https://www.abc.net.au/news/'

R('2026-11-25-us-overcapacity-tariffs-14-economies','1','US targets 14 economies with new "overcapacity" tariffs','2026-11-25','news',['Al Jazeera','ABC News (US)'],
 "Gives a live case of protectionism under Section 301, the role of courts in trade policy and the indirect risks for Australia, which is not targeted.",
 "The US Trade Representative has proposed new tariffs on 14 trading partners, including China, the EU and Japan, arguing that subsidised excess capacity in their manufacturing sectors gives them an unfair advantage. Australia is not on the list.",
 ['1C.2','1C.1','2D.4','1B.2'],['Y3a.6','Y3a.7','Y3a.8','Y3a.11','Y3a.14'],['P6a.1'],
 ['2A.1'],['Y3a.15','Y3e.3'],['P6a.2'],
 ['trade','global'],['trade'],['ds','flow'],
 [F('Economies named in the proposed tariffs','14: China, EU, India, Japan, South Korea, Indonesia, Bangladesh, Cambodia, Malaysia, Singapore, Switzerland, Taiwan, Thailand, Vietnam (Mexico and Norway investigated but left out)','25 November 2026','trade','ABC News (US) / Al Jazeera'),
  F('Proposed rate on China and Vietnam','20% (China on top of about 25% in duties from Trump\'s first term)','November 2026','trade','Al Jazeera'),
  F('Reported rate caps in earlier trade deals','15% for the EU, Japan and Korea; 19% for Malaysia','November 2026','trade','Al Jazeera'),
  F('US share market reaction','Nasdaq -3.9%, S&P 500 -2.8%','25 November 2026','global','Al Jazeera')],
 [T('Section 301','US trade law used to impose tariffs on countries found to trade unfairly.'),T('Excess capacity','More production than domestic demand can absorb, often supported by subsidies and then exported cheaply.'),T('Trade diversion','Goods blocked from one market are redirected to other markets.')],
 [L('Al Jazeera: World reacts to Trump\'s new tariffs as US stocks tumble, 25 Nov 2026','https://www.aljazeera.com/'),L('Al Jazeera: Trump announces new trade tariffs: which countries will they target?, 25 Nov 2026','https://www.aljazeera.com/'),L('ABC News (US): Trump admin proposes new tariffs on China, EU and 12 other trading partners, 25 Nov 2026','https://abcnews.go.com/')],
 "Apply the tariff diagram (price rises to Pw+t, imports shrink, revenue and deadweight loss). Indirect effects on Australia: weaker Chinese manufacturing could cut demand for iron ore and coal (terms of trade), while goods diverted from the US could flow into Australia more cheaply, helping consumers but pressuring import-competing firms.",
 [Q("Using a tariff diagram, explain the effects of a US tariff on US consumers, US producers and the US government.",6),Q("Explain how US tariffs on China could indirectly affect the Australian economy.",4)],
 "PROPOSED, from preliminary findings of an eight-month Section 301 investigation: not yet in force. The US used Section 301 after the Supreme Court struck down its broad emergency-powers (IEEPA) tariffs in February 2026. The EU said it 'strongly rejects' the overcapacity premise and China called it a 'false issue'; analysts see the mid-December G20 meetings as a chance to negotiate. Replaces the 24 November preview card (WSJ via Investing.com: USTR Jamieson Greer could release findings 'as soon as this week'; 27 EU members in scope; July tariffs of 10-12.5% on 60 economies under court challenge; steel, aluminium and cars excluded as separate national security tariffs apply). UPDATE DUE: final rates and start date. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-25-aud-slides-11-month-low-hot-cpi','2','Aussie dollar slides to an 11-month low','2026-11-25','news',['CommBank (AAP)',ABC,'AFR'],
 "Explains the AUD's fall through commodity prices and diverging interest rate expectations, and the inflation cost of depreciation.",
 "The Australian dollar fell to about US65.9 cents on 25 November, its lowest level in 11 months. Metal prices slumped and investors are betting that US and Australian interest rates will move in opposite directions next year.",
 ['2C.2','2C.3','2C.6'],['Y3c.2','Y3c.4','Y3c.5','Y3c.6'],['P6c.1'],
 ['4D.3','3C.3','2B.4'],['Y2c.5','Y1c.4','Y1a.7'],['P4c.3'],
 ['fx','rates','trade','inflation'],['monetary'],['fx','flow'],
 [F('AUD / USD','About US65.9c, down about 0.7% on the day (briefly US66.6c when the hot CPI came out)','25 November 2026','fx','ABC News; CommBank/AAP'),
  F('Copper on the LME','-5% to about US$11,900 a tonne','25 November 2026','trade','CommBank/AAP'),
  F('ASX 200','-0.4% to 8,692','25 November 2026','global','CommBank/AAP'),
  F('10-year bond yield: Australia / US','4.84% / 4.90%','25 November 2026','rates','ABC News'),
  F('First RBA cut priced','August 2027','25 November 2026','rates','AFR')],
 [T('Depreciation','A fall in the value of the AUD under a floating exchange rate.'),T('Interest rate differential','The gap between Australian and overseas rates, which influences capital flows.'),T('Imported inflation','Higher domestic prices caused by more expensive imports.')],
 [L('CommBank Newsroom (AAP): Aussie shares slip as hot inflation pushes back rate cut hopes, 25 Nov 2026','https://www.commbank.com.au/'),L('ABC News: markets blog, 25 Nov 2026',H),L('AFR: Hot inflation dashes market\'s hopes of an early RBA cut (Cécile Lefort), 25 Nov 2026',AFR)],
 "Lower commodity prices cut the demand for AUD, and expectations that US rates rise while Australian rates fall make AUD assets less attractive, so D shifts left and the AUD depreciates. A depreciation is two-edged: exporters become more competitive, but imports (especially fuel) cost more and the AUD value of foreign-currency debt rises, complicating the RBA's job.",
 [Q("Explain two factors that contributed to the depreciation of the Australian dollar in November 2026.",4),Q("Discuss the effects of a depreciation on Australia's external stability and inflation.",6)],
 "Market prices that move daily. Replaces the 24 November card (Westpac IQ: AUD US$0.6609 on 23 November, an 11-month low and weakest G10 currency of the week; iron ore 61% fines US$89.30 a tonne; only about 10% of Chinese steelmakers profitable per Mysteel, against 38% a year earlier; copper down about 14-16% in November; gold near 15-month lows; AUD had wiped out all its 2026 gains). The 16 November low was US67.6c (a 10-month low). The 22 November miners and 23 November iron ore cards are kept. Links are to the outlets' home pages because the digest gives titles only.")

R('2026-11-25-inflation-hits-4-9-per-cent-october-cpi','3','Inflation hits 4.9%: fuel, power and a home-grown problem','2026-11-25','news',['ABS',ABC,'SBS','AFR','SMH','The Conversation'],
 "Gives the October CPI with headline and trimmed mean figures and the split between supply shocks and domestic pressure.",
 "Headline CPI rose 4.9% in the year to October, up from 4.3% in September and the highest in three years. The RBA's preferred trimmed mean measure rose from 3.6% to 3.8%. Both are well above the 2-3% target.",
 ['3C.1','3C.2','3C.3'],['Y1c.2','Y1c.3','Y1c.4','Y1c.8','Y1c.9'],['P2c.4'],
 ['3C.4','4D.3'],['Y1c.7','Y2c.5'],['P4c.3'],
 ['inflation'],['monetary'],['chart','adas','flow'],
 [F('Headline CPI, year to October','4.9% (September: 4.3%); highest in three years','October 2026','inflation','ABS'),
  F('Trimmed mean, year to October','3.8% (September: 3.6%)','October 2026','inflation','ABS'),
  F('Automotive fuel, year to October','+32.5% (petrol +6.3% in the month)','October 2026','inflation','ABS, via SMH'),
  F('Electricity, year to October','+25.2% (federal rebates ended last October: partly a base effect)','October 2026','inflation','ABS'),
  F('Housing group','+6.4%, the largest contributor (new dwellings +5.1%); rents +3.5%, lowest annual rate since the pandemic','October 2026','inflation','ABS'),
  F('Tradables / non-tradables','+5.3% / +4.7% (non-tradables about 65% of the CPI)','October 2026','inflation','ABS, via AFR')],
 [T('Headline vs trimmed mean','Headline is the whole CPI basket; the trimmed mean strips out the biggest price rises and falls each month to show underlying inflation.'),T('Base effect','A change in the annual rate caused by what happened 12 months earlier.'),T('Tradables and non-tradables','Goods exposed to world prices versus mainly domestic services and housing.')],
 [L('ABC News: Inflation rises more than expected to 4.9pc in year to October, 25 Nov 2026',H),L('SBS News, 25 Nov 2026','https://www.sbs.com.au/news/'),L('AFR: Domestic cost increases fuel surprise inflation jump (Grace Lagan)',AFR),L('SMH: Stagflation fears grip Canberra (Shane Wright)','https://www.smh.com.au/'),L('The Conversation: Inflation jumps to 4.9% as fuel prices surge (Stella Huangfu)','https://theconversation.com/au')],
 "Separate temporary supply shocks (fuel, rebates ending) from persistent domestic pressure (housing, services), the core of the debate over whether the RBA needs to raise rates again. The Business Council says most of the problem is home-grown (AFR); many economists think October is the peak because petrol has fallen about 20% in four weeks (AMP via SMH).",
 [Q("Distinguish between headline and underlying inflation, using the October 2026 data.",4),Q("Explain whether Australia's inflation in 2026 is mainly imported or home-grown.",6)],
 "This is the October CPI release (flagged UPDATE DUE on earlier cards). Australia's headline rate is now above the US, UK, Canada and NZ (AFR). The AI boom is competing for resources and chips: toy and game prices +13% (SMH). Other items: fruit +10.9%, transport group +10.6%, meals out +4.1%. Headline inflation and the unemployment rate are both 4.9% (coincidence). This confirms September headline CPI of 4.3%, resolving the earlier 3.9% discrepancy. UPDATE DUE: November CPI and the RBA decision on 8 December. Links to home pages where the digest gives titles only.")

R('2026-11-25-record-home-building-ai-boom-capacity','3','Record home building as the AI boom stretches capacity','2026-11-25','news',['ABS',ABC,'AFR','SMH'],
 "Shows investment as both a demand-side and supply-side force, with competition for scarce labour and materials adding to inflation.",
 "Construction work done rose 0.9% in the September quarter and residential building reached a record of about $30.4 billion. But data centres and housing are competing for the same scarce tradespeople and materials, adding to inflation even as it supports growth.",
 ['3A.5','3A.6','3C.3'],['Y1a.6','Y1a.10','Y1a.12','Y1c.4'],['P1e.6'],
 ['3A.1','4E.1'],['Y1c.5','Y2d.3'],[],
 ['growth','inflation','housing','investment'],[],['adas','flow'],
 [F('Construction work done, September quarter','+0.9% (building +2.4%, engineering -0.9%)','September quarter 2026','growth','ABS, via ABC News'),
  F('Real residential building','Record about $30.4 billion, up roughly 9% on a year earlier','September quarter 2026','housing','ABS, via SMH and AFR'),
  F('Non-residential construction','+10.2% over the year (much of it data centres and renewable energy)','September quarter 2026','investment','SMH'),
  F('Cost of building new homes','+0.8% in October, +5.1% over the year','October 2026','inflation','ABS'),
  F('Expected Q3 GDP growth','About 0.4% (due next week)','September quarter 2026','growth','SMH')],
 [T('Productive capacity','The maximum sustainable output of the economy (LRAS).'),T('Capacity constraints','Shortages of labour or materials that push up prices when demand grows faster than supply.')],
 [L('ABC News: markets blog, 25 Nov 2026',H),L('AFR: Domestic cost increases fuel surprise inflation jump (Grace Lagan)',AFR),L('SMH: Stagflation fears grip Canberra; Chalmers cannot spin a silver lining out of this grim story (Shane Wright)','https://www.smh.com.au/')],
 "In the short run the investment boom shifts AD right against a near-fixed LRAS, so the main effect is a higher price level; over time finished homes, data centres and energy projects expand productive capacity (LRAS shifts right). Investment is both a demand-side and a supply-side force.",
 [Q("Explain how the AI and data-centre investment boom can add to inflation in the short run but raise economic growth in the long run.",5)],
 "Shane Wright (SMH): data centres need 'electricians and plumbers just as much as' new homes do. The SMH reports that strong construction may help Australia avoid a recession. UPDATE DUE: Q3 GDP (due 2 December). Related 17 November data centres and inflation card. Links to home pages where the digest gives titles only.")

R('2026-11-25-stagflation-fears-shoppers-retreat','3','Stagflation fears grow as shoppers retreat','2026-11-25','news',['SBS','The Conversation','SMH','AFR'],
 "Shows rising unemployment and inflation together, with retail evidence of how rate rises cut household spending.",
 "Inflation and unemployment are both 4.9%. Economists at HSBC, BDO and AMP warn that Australia is drifting into stagflation, and retailers say customers have already stopped spending.",
 ['3C.3','3B.2','3A.7'],['Y1c.1','Y1c.5','Y1c.6','Y1a.5'],['P1e.5','P1e.7'],
 ['4D.3','4I.2','4I.3'],['Y2c.5','Y2a.2'],['P4c.3'],
 ['inflation','employment','growth'],['monetary'],['adas','flow'],
 [F('Unemployment rate','4.9% in October, a five-year high; unemployed people +17,800 to about 753,700','October 2026','employment','The Conversation'),
  F('Harvey Norman pre-tax profit, July-October','-47% (analysts expected -13%); same-store sales -3.7%','July-October 2026','growth','AFR; SMH'),
  F('Mortgage holders who have cut spending','72% (62% of renters; a fifth of outright owners have cut essentials)','November 2026','growth','RBA research, via SMH'),
  F('Recession odds','About 50-50 (Macquarie, HSBC)','November 2026','growth','SMH')],
 [T('Stagflation','High inflation together with stagnant growth and rising unemployment.'),T('Supply shock','A sudden rise in costs, such as oil, that shifts short-run aggregate supply left.'),T('Discretionary spending','Non-essential purchases, which households cut first.')],
 [L('SBS News: Australia\'s inflation problem is growing again, 25 Nov 2026','https://www.sbs.com.au/news/'),L('The Conversation (Stella Huangfu)','https://theconversation.com/au'),L('SMH: Stagflation fears grip Canberra; Only going to get worse: Harvey Norman','https://www.smh.com.au/'),L('AFR (Campbell Kwan): Gerry Harvey warns of recession as retail disaster...',AFR)],
 "An oil shock shifts SRAS left (higher prices, lower output) while five rate rises pull AD left as households cut back. Policy conflict: measures that bring inflation down (higher rates, budget cuts) also raise unemployment, a short-run trade-off along the Phillips curve.",
 [Q("Using an AD/AS diagram, explain how an oil price shock can lead to stagflation.",5),Q("Explain how rising interest rates affect household consumption, using evidence from the retail sector.",4)],
 "Retail claims are those of businesses (Gerry Harvey says 'there's no one in the shop' and expects bankruptcies from February to June; he warned another rate rise could tip the economy into a 'bad recession'): treat as opinion. Treasury expects growth well below 2% for two years and unemployment peaking above 5%; Chalmers rejects recession talk. David Jones, General Pants and Cue have collapsed. Related 24 November Chalmers jobless warning and 22 November Sahm rule cards. Links to home pages where the digest gives titles only.")

R('2026-11-25-accc-clears-calvary-healthscope-hospitals','4','ACCC clears Calvary\'s takeover of 14 Healthscope hospitals','2026-11-25','news',[ABC,'Real Estate Source','The Urban Developer'],
 "Gives a current merger review case for competition policy, including the failing-firm trade-off.",
 "The ACCC has cleared not-for-profit Calvary's purchase of 14 private hospitals from collapsed operator Healthscope, a key step in breaking up what was Australia's second-largest private hospital group.",
 ['4E.3','4E.2'],['Y2d.2','Y2d.4'],['P2g.1','P2g.3'],
 ['4E.1'],['Y2d.5'],['P5a.5'],
 ['investment','employment'],['micro'],['compare'],
 [F('Hospitals cleared for Calvary','14 (of 25 split between four buyers)','25 November 2026','investment','ABC News'),
  F('Healthscope debt at collapse','More than $1.6 billion (receivership May 2025)','May 2025','investment','Healthscope receivership statement'),
  F('Jobs reported protected by the sale','About 14,000 (completion expected by 30 November; lenders expected to recover about 40 cents in the dollar)','November 2026','employment','Real Estate Source; The Urban Developer')],
 [T('Substantial lessening of competition','The legal test the ACCC applies to mergers and acquisitions.'),T('Receivership','An insolvency process where a receiver sells assets to repay lenders.')],
 [L('ABC News: markets blog, 25 Nov 2026',H),L('Real Estate Source: Calvary wins control of Healthscope, Sep 2026','https://www.realestatesource.com.au/'),L('The Urban Developer: Calvary-Healthscope hospital deal, 28 Sep 2026','https://www.theurbandeveloper.com/')],
 "Competition policy keeps markets contestable so firms face pressure to keep prices down and quality up. Use the case to explain why the ACCC reviews mergers and why a failing-firm situation can change the balance of costs and benefits: risks are less competition and more bargaining power over insurers, benefits are keeping hospitals open and protecting jobs.",
 [Q("Explain the role of the ACCC in promoting competition, using the Calvary-Healthscope deal.",4)],
 "The sources reviewed did not report the ACCC's detailed reasons, so the card cannot explain why it cleared the deal. Timeline: Healthscope receivership May 2025; first four hospitals sold December 2025 (including Hobart and Holmesglen to Calvary); remaining 25 split in September 2026 (Calvary 14, Healthe Care 6, Acurio Health 3, KnG Group 2). Links to home pages where the digest gives titles only.")

R('2026-11-25-can-the-budget-help-fight-inflation-critics','4','Can the budget help fight inflation? Critics say it\'s late','2026-11-25','news',['AFR (opinion)','SMH',ABC],
 "Sets out the debate over whether fiscal restraint can support the RBA, with lags, credibility and the policy mix.",
 "Treasurer Jim Chalmers promises 'substantial savings' in December's mid-year update (MYEFO). AFR columnists argue that after years of fast spending growth it is 'too little, too late', and others warn that cuts could land just as the economy is weakest.",
 ['4C.1','4C.2','4H.1','4H.3','4B.1'],['Y2b.3','Y2b.9','Y2b.13','Y2b.14'],['P5c.3'],
 ['4D.3'],['Y2c.5'],['P5a.4'],
 ['budget','inflation'],['fiscal','monetary'],['adas','compare'],
 [F('Growth in federal payments','8% in 2024-25 and 8.2% in 2025-26, about 17% over two years','2024-26','budget','AFR (John Kehoe, opinion)'),
  F('Estimated effect of an $8 billion net spending cut over 12 months','About 0.25 percentage points off the cash rate','November 2026','rates','Chris Richardson, cited by AFR'),
  F('Lag before spending cuts affect demand','6-18 months','November 2026','budget','AFR (John Kehoe, opinion)')],
 [T('Fiscal stance','Whether the budget is adding to (expansionary) or subtracting from (contractionary) demand.'),T('Policy mix','How fiscal and monetary policy work together or against each other.'),T('Fiscal credibility','Public belief that deficits will eventually be repaid.')],
 [L('AFR: It\'s too late for Jim Chalmers to fix inflation (John Kehoe, opinion), 25 Nov 2026',AFR),L('AFR: Inflation spells trouble for everyone (Jennifer Hewett, opinion), 25 Nov 2026',AFR),L('SMH: Chalmers cannot spin a silver lining out of this grim story (Shane Wright)','https://www.smh.com.au/'),L('ABC News: Federal politics blog, 25 Nov 2026',H)],
 "Contractionary fiscal policy cuts G and shifts AD left: the price level is lower than it would be, helping the RBA, but real output falls and unemployment rises. Compare critics (inflation largely home-grown; the budget should have run surpluses during the revenue boom) with the government (the war and oil prices are the primary driver; savings must not threaten growth).",
 [Q("Discuss the role of fiscal policy in supporting the RBA to reduce inflation in 2026-27.",6)],
 "MOSTLY OPINION: the AFR pieces are columns by John Kehoe and Jennifer Hewett, and the Nobel laureate Michael Woodford point (a central bank cannot defeat inflation alone if fiscal policy lacks credibility) is cited by Kehoe. Chalmers called the CPI 'unwelcome but unsurprising' and the budget 'not the primary driver of prices'; infrastructure projects may be delayed or 're-profiled'. HSBC's Paul Bloxham says growth needs supply-side reform rather than more redistribution. Shane Wright (SMH): the MYEFO 'has to deliver' real cuts. UPDATE DUE: the MYEFO. Related 24 November MYEFO savings card. Links to home pages where the digest gives titles only.")

R('2026-11-25-coalition-backs-labor-20-per-cent-gas-reservation','4','Coalition to back Labor\'s 20% gas reservation','2026-11-25','news',['AFR'],
 "Shows how a contested market intervention was settled by political compromise, with the costs and benefits of reserving gas.",
 "Labor and the Coalition are set to pass laws forcing gas producers to set aside up to 20% of their supply for domestic users, after agreeing minor technical changes. The scheme is due to start in January 2028.",
 ['4E.1','4E.2'],['Y2d.1','Y2d.4','Y2d.5'],['P2i.2','P2i.3','P2i.4'],
 ['4H.3','2A.1'],['Y2d.6'],['P2d.1'],
 ['investment','inflation','trade'],['micro'],['ds','compare'],
 [F('Share of supply to be reserved for domestic users','Up to 20%, from January 2028','November 2026','investment','AFR'),
  F('Disputed "oversupply" requirement','10%','November 2026','investment','AFR'),
  F('Expected passage','Thursday 26 November, before parliament rises for summer','26 November 2026','investment','AFR')],
 [T('Domestic gas reservation','Requiring a share of gas production to be sold locally rather than exported.'),T('Sovereign risk','The risk that a government changes rules in ways that reduce the value of investments.'),T('Marginal cost','The cost of producing one more unit.')],
 [L('AFR: Coalition to back Labor\'s 20pc gas reservation (Ryan Cropp and Angela Macdonald-Smith), 25 Nov 2026',AFR)],
 "Reservation shifts domestic supply right: price falls and quantity used rises, helping manufacturers and households. Costs: lower export volumes and revenue (terms of trade, tax receipts) and possibly less future investment. A trade-off between domestic energy costs and export income, linked to Topic 2.",
 [Q("Discuss the economic costs and benefits of a domestic gas reservation policy for Australia.",6)],
 "UPDATE DUE: confirm that the Senate passed the laws on 26 November. The sticking point was a 'must sell' rule and a requirement to oversupply the market by 10%, which the Coalition said would push prices so low it would destroy future investment (producers say they would be forced to sell below marginal cost); Resources Minister Madeleine King says the must-sell rules are fundamental. The Coalition won a stronger carve-out for WA producers and limits on the minister's powers; Andrew Hastie says the goal is to keep advanced manufacturing and heavy industry in Australia; Amplitude Energy warns of sovereign risk; former ACCC chair Rod Sims says it is not tenable to export so much gas while local industry cannot secure supply. Replaces the 24 November Senate showdown card (from 2028; Labor-chaired Senate committee recommended the bill; Gladstone LNG netback A$35.48/GJ on 10 November against A$15.40 a year earlier; east-coast December gas about A$12.20/GJ; Greens and David Pocock proposed a 25% gas export tax, rejected by the government; WA already has a 15% reservation; industry warned the 110% east-coast oversupply target could distort the market). The 18 November WA carve-out card is kept. Link to the AFR home page because the digest gives the title only.")

R('2026-11-25-google-ends-news-deals-news-bargaining-incentive','4','Google walks away from news deals under the new digital levy','2026-11-25','news',['AFR'],
 "Shows government failure and the limits of microeconomic policy, with a multinational responding to incentives in an unintended way.",
 "Google has ended a $15 million-a-year deal with the ABC as it dismantles dozens of agreements with Australian newsrooms. It is choosing to pay the government's new News Bargaining Incentive (NBI) charge rather than sign enough deals to offset it.",
 ['4E.2','4E.3'],['Y2d.4','Y2d.5','Y2d.6'],['P2h.3','P2i.2','P2i.4','P2i.5'],
 ['4H.3'],['Y3b.2'],[],
 ['global','budget'],['micro'],['flow','compare'],
 [F('NBI charge','2.75% of the Australian ad revenue of Google, Meta, TikTok and LinkedIn, backdated to the start of 2025','November 2026','budget','AFR'),
  F('News deals needed to fully offset the charge','At least 8 news businesses','November 2026','budget','AFR'),
  F('Expected NBI revenue','At least $550m in 2026-27 (first 18 months), $400m in 2027-28, $450m in each of the next two years','2026-27 onward','budget','AFR'),
  F('Google-ABC deal ended','$15 million a year (worth up to $75 million over five years); about $3 million a year to the Public Interest Publishers Alliance ends in December','November 2026','global','AFR')],
 [T('Positive externality','A benefit to society (such as informed citizens) that the producer is not paid for.'),T('Government failure','When an intervention produces outcomes different from those intended.'),T('Multinational corporation','A firm operating across many countries.')],
 [L('AFR: Google cancels ABC\'s $15m deal as it turns off publisher funding (Sam Buckingham-Jones), 25 Nov 2026',AFR)],
 "The NBI was meant to encourage commercial deals (and fund journalism, a positive externality the market under-provides); Google is instead paying the charge, so publishers lose direct deals and compete for tax proceeds paid out via a News Journalism Payments Scheme. Firms respond to incentives in ways governments may not expect. Topic 1 link: how governments tax and regulate global digital firms, and the trade tensions with the US.",
 [Q("Explain why a policy designed to encourage commercial deals may instead lead firms to pay the charge.",4)],
 "Single-source report (AFR). The ABC says the 60 regional journalist jobs it funded will be kept. Google says the NBI was 'not providing incentives to reach commercial deals'; its contracts with Nine and Seven West Media have lapsed, and the charge has angered US tech lobby groups. Background: the News Media Bargaining Code put about $250 million into local news over three years from 2021. Related 5 November card on US tech giants pushing for trade retaliation over the levy. Link to the AFR home page because the digest gives the title only.")

R('2026-11-25-rba-december-dilemma-hold-hike-or-cut','4','The RBA\'s dilemma: hold, hike or cut?','2026-11-25','news',[ABC,'The Conversation','AFR','SBS'],
 "Sets out the case for holding or hiking after the hot CPI and shows why monetary policy is limited against a supply shock.",
 "The cash rate is 4.85%, its highest level in 18 years, after five rate rises in 2026. Hot inflation and a weakening labour market now pull the Reserve Bank in opposite directions before its 8 December meeting.",
 ['4D.1','4D.2','4D.3'],['Y2c.1','Y2c.2','Y2c.4','Y2c.5'],['P4c.3'],
 ['3C.1','3C.3','4H.1'],['Y2c.3','Y1c.4'],['P4c.4'],
 ['rates','inflation','employment'],['monetary'],['flow','compare'],
 [F('Cash rate','4.85% after five rises in 2026 (+1.25 percentage points from 3.60%); November vote 6-3','November 2026','rates','RBA'),
  F('Market pricing for December','About 97% chance of no change','25 November 2026','rates','ABC News'),
  F('First cut priced','Pushed back from June to August 2027; chance of a March cut fell from 33% to 23%','25 November 2026','rates','AFR'),
  F('Oil','Down from a US$125 peak to about US$91; petrol down about 20%','November 2026','inflation','digest')],
 [T('Cash rate','The RBA\'s target interest rate on overnight loans between banks.'),T('Time lags','The 12-18 months it takes for monetary policy to have its full effect.')],
 [L('ABC News: markets blog, 25 Nov 2026',H),L('The Conversation: Inflation jumps to 4.9% as fuel prices surge, but the RBA should hold rates steady (Stella Huangfu)','https://theconversation.com/au'),L('AFR: Rate hike calls grow even as inflation tipped for three-year high (Lea Jurkovic), 24 Nov 2026',AFR),L('AFR: Hot inflation dashes market\'s hopes of an early RBA cut (Cécile Lefort), 25 Nov 2026',AFR),L('SBS News, Nov 2026','https://www.sbs.com.au/news/')],
 "Case for hiking: trimmed mean (3.8%) above the RBA's own 3.6% forecast, a weaker AUD adds imported inflation, and some board members may lean hawkish. Case for holding: unemployment (4.9%) already at the RBA's late-2027 forecast, oil and petrol falling, five rises still working through with 12-18 month lags. Much of the inflation is a supply shock, so higher rates cut it only by cutting demand and jobs: a key limitation of monetary policy.",
 [Q("Evaluate the effectiveness of monetary policy in responding to inflation caused by a global oil price shock.",6)],
 "UPDATE DUE: RBA decision on 7-8 December. Market pricing and economist views, not decisions. Governor Bullock has said inflation must be moving sustainably back to target before cuts are considered; former RBA official Jonathan Kearns says no cut is likely in the first half of 2027 without a 'major catastrophe'; Kapstream and UBS warn markets are underpricing a hike; Schroders warns of a possible 'policy mistake' if rates stay too high. Before the CPI, ANZ had brought its first-cut forecast forward to June 2027. Replaces the 24 November 'RBA tipped to hold' card (new housing lending -15.5% and investor lending -32.3% in the September quarter; CommBank's Belinda Allen said December would not be 'live'; Pitcher Partners expected a hold until February 2027; the RBA expected inflation above 3% until late 2027). The 17 November minutes and 19 November jobs shock cards are kept. Links to home pages where the digest gives titles only.")

R('2026-11-25-trust-tax-passes-greens-private-jet-levy','4','Trust tax passes as Greens win a private-jet levy','2026-11-25','news',['AFR','The Nightly',ABC],
 "Gives a current tax reform with equity and efficiency trade-offs, compliance costs and winners and losers.",
 "Labor has secured Greens support to pass a minimum 30% tax on discretionary trust distributions. In return, owners of private jets will face a new registration fee that closes the gap between their fuel tax and what motorists pay.",
 ['4C.2','3E.3','3E.6'],['Y2b.10','Y1d.5','Y1d.9'],['P5b.1','P5b.6','P5b.7'],
 ['4I.5'],['Y1d.10'],['P5a.4'],
 ['inequality','budget'],['fiscal'],['compare'],
 [F('Minimum tax on discretionary trust distributions','30%; about 800,000 people use discretionary trusts','November 2026','inequality','AFR'),
  F('Start date','1 July 2028 (three-year window to restructure opens 1 July 2027)','2027-28','budget','AFR'),
  F('Compliance cost estimates','CPA Australia: $2-2.8 billion up front and $221-595 million a year; Treasury: $48 million a year','November 2026','budget','AFR'),
  F('Fuel excise per litre','Private jets 3.556c versus about 53c for petrol; new fee about $3,000 per full refill','November 2026','budget','AFR; The Nightly'),
  F('PBO costing of aligning jet fuel rate','About $1.2-1.5 billion over the forward estimates','Earlier 2026','budget','The Nightly')],
 [T('Vertical equity','People with higher incomes should pay a greater share of tax.'),T('Compliance costs','The cost to taxpayers of understanding and meeting tax rules.'),T('Tax concession','A lower rate or exemption that reduces tax for particular activities or groups.')],
 [L('AFR: The trust tax deal is done: here\'s what it means for you (Andrew Hobbs), 25 Nov 2026',AFR),L('AFR: Billionaires brace for private jet tax after Labor backs Greens (Ayesha de Kretser), 25 Nov 2026',AFR),L('The Nightly: Greens demand change as Aussie motorists pay 15 times higher fuel tax, 15 Nov 2026','https://www.thenightly.com.au/')],
 "A classic equity versus efficiency trade-off: the reforms reduce tax advantages for wealthier households (vertical equity, revenue) but add compliance costs and may discourage some small-business investment. A trust's options: accept the minimum tax, make an 'excluded election trust' election, or restructure into a company.",
 [Q("Assess the equity and efficiency effects of the minimum tax on discretionary trusts.",6),Q("Explain why fuel tax concessions for private aircraft might be considered inequitable.",3)],
 "The Coalition promises to contest the laws at the next election; critics warn families face irreversible decisions and Grant Thornton warns some small businesses may fail. Testamentary trusts can still distribute to minors at adult rates; charities and not-for-profits stay excluded (an estimated $1.3 billion over five years); medical, agricultural, charter and hobby flying are exempt from the jet fee. Compliance cost estimates differ widely between CPA Australia and Treasury. Links to home pages where the digest gives titles only.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-24-us-readies-sweeping-new-tariffs-subsidies-probe','2026-11-24-aud-11-month-low-iron-ore-copper-slide','2026-11-24-senate-showdown-gas-reservation-lng-2028','2026-11-24-rba-tipped-to-hold-4-85-economy-cools'}
d=[x for x in d if x['id'] not in REMOVE]
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
