import json,os
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-11-10-cop31-electrification-push','2026-11-10-china-exports-surge-tariff-truce','2026-11-10-aud-steadies-rates-peaked','2026-11-11-rba-finished-hiking'}
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
      angle=angle,questions=questions,note=note,added='2026-11-12'))
AFR=lambda t:['AFR, '+t+' (subscriber article; link goes to the AFR home page)','https://www.afr.com/']
BLOG11=['ABC News, markets live blog, 11 Nov 2026','https://www.abc.net.au/news/2026-11-11/asx-markets-business-live-news-nov-11/107370848']
INDAILY=['AAP/InDaily, Tax changes spur record fall in investor home loans','https://indailyqld.com.au/news/just-in/2026/11/11/tax-changes-spur-record-fall-in-investor-home-loans']
PLUNGE=['ABC News, Plunge in new home loans a result of property investors','https://abc.net.au/news/2026-11-11/plunge-in-new-home-loans-result-of-property-investors/107373668']
WEST=['Westpac IQ, Consumer sentiment, November 2026','https://westpaciq.com.au/economics/2026/11/consumer-sentiment-november-2026']

R('2026-11-09-chalmers-productivity-plan-myefo',4,'Chalmers asks Treasury for a productivity plan before the mid-year update','2026-11-09','news',['MacroBusiness','The Australian'],
 'Shows the government turning to supply-side reform as the RBA fights inflation, and why productivity sets the economy\'s speed limit.',
 'The Treasurer has reportedly asked Treasury\'s structural reform officials to develop new productivity policies for December\'s Mid-Year Economic and Fiscal Outlook. Australia\'s productivity growth over the past decade has been among the weakest in the OECD.',
 ['4E.1','3A.6'],['Y2d.1','Y2d.2','Y1a.10'],['P3c.4'],['4H.3','4D.3','4B.1'],['Y2g.1','Y2c.8','Y2d.6'],['P3c.5'],
 ['productivity','inflation','budget'],['micro'],['adas','flow'],
 [F('Next budget update','MYEFO, December 2026','December 2026','budget','MacroBusiness, citing The Australian'),F('Australia\'s productivity growth over the past decade','among the weakest in the OECD','2016-2026','productivity','MacroBusiness, citing The Australian'),F('RBA cash rate','4.85%','November 2026','rates','MacroBusiness')],
 [T('Productivity','Output per unit of input, such as output per hour worked.'),T('Microeconomic reform','Policies that improve how efficiently individual markets and industries work.')],
 [['MacroBusiness, Jim Chalmers pretends to care about productivity growth (opinion piece citing The Australian, 9 Nov 2026)','https://macrobusiness.com.au/2026/11/jim-chalmers-pretends-to-care-about-productivity-growth/']],
 'When demand grows against fixed capacity (LRAS1) the result is only a higher price level. Productivity-raising reform shifts capacity out to LRAS2, so real GDP can grow with less price pressure. Supply-side policy complements monetary policy, since the RBA manages only demand, but reform takes years to pay off.',
 [Q('Explain how microeconomic reform can lift productivity and reduce inflationary pressure in the Australian economy.',4)],
 'Secondhand and thin: the source is a MacroBusiness opinion piece citing The Australian, and no policy details or costings have been released. UPDATE DUE: the December MYEFO. Pairs with the 5 November Productivity Commission and budget items.')

R('2026-11-11-budget-tax-changes-hit-investors',4,'Budget tax changes push investors out of the housing market','2026-11-11','news',['AAP','InDaily','ABC News'],
 'A policy test: investor tax changes cut investor lending by almost a third, shifting the market to owner-occupiers, with the rent-supply limit as the counter-argument.',
 'Investor home loans fell by almost a third in the first full quarter after the May budget\'s tax changes: the number of new investor loans fell 30.6% to 35,301 and their value fell 32.3%. Owner-occupiers\' share of new home loans rose to 68%, from 59% before the budget.',
 ['4C.1','4C.2'],['Y2d.3','Y2b.13'],['P4c.7','P5b.1'],['3E.4','4H.3'],['Y2b.14','Y1d.5'],['P5a.4'],
 ['housing','budget','inequality'],['fiscal','micro'],['ds','chart'],
 [F('New investor loans, number','-30.6% to 35,301 (value -32.3%)','September quarter 2026','housing','AAP/InDaily'),F('Owner-occupiers\' share of new home loans','68% (59% before the May budget)','September quarter 2026','housing','AAP/InDaily'),F('Brisbane median dwelling value','-2% in October (steepest fall in the country)','October 2026','housing','ABC News')],
 [T('Fiscal policy','The use of government spending and taxation to influence the economy.'),T('Housing affordability','How easily households can buy or rent a home relative to their income.')],
 [INDAILY,PLUNGE],
 'Reducing tax concessions lowers investors\' after-tax return, so demand for investment property falls and the price falls, improving affordability. The limitation: if fewer investors buy, fewer homes may be offered for rent, which could push rents up, and lasting affordability needs more housing supply.',
 [Q('Evaluate the use of tax policy to improve housing affordability in Australia.',6)],
 'Housing Minister Clare O\'Neil credits the budget changes; the ABS says higher borrowing costs and expectations of lower prices also played a part, so the fall is not all policy. Same ABS release as the record fall in new home loans item filed today.')

R('2026-11-11-rba-rate-peak-debate',4,'Has the RBA reached its peak? Economists weigh up the fifth hike','2026-11-11','news',['ABC News','Westpac IQ'],
 'A week after the fifth rise, evidence of the transmission mechanism at work and a split view on whether another hike is needed. Replaces the 11 November "finished hiking" item.',
 'The RBA raised the cash rate by 0.25 points to 4.85% on 3 November, the fifth hike of 2026 and the highest since late 2008. A week later, ANZ expects a pause but warns another rise in December cannot be ruled out, and the RBA does not expect inflation below 3% until late 2027.',
 ['4D.1','4D.2','4D.3','4H.1'],['Y2c.4','Y2c.5','Y2c.7','Y2c.8'],['P4c.3'],['3A.7','3C.3'],['Y2c.3','Y1a.14'],['P4c.4'],
 ['rates','inflation','housing'],['monetary'],['adas','flow'],
 [F('RBA cash rate','4.85% (highest since late 2008; fifth hike of 2026; board vote 6-3, three members wanted to hold at 4.60%)','3 November 2026','rates','ABC News'),F('When the RBA expects inflation below 3%','late 2027 (about three quarters later than previously forecast)','2027','inflation','ABC News'),F('Consumer sentiment','78.2 (from 80.4; four-year low)','November 2026','growth','Westpac IQ'),F('New home loans, value','-15.5% in the September quarter (record fall)','September quarter 2026','housing','ABS via ABC News')],
 [T('Cash rate','The interest rate on overnight loans between banks, set by the RBA as its main policy tool.'),T('Transmission mechanism','The channels through which a cash-rate change affects spending, output and inflation.')],
 [['ABC News, RBA lifts interest rates (3 Nov 2026)','https://abc.net.au/news/2026-11-03/rba-lifts-interest-rates-november-2026-highest-rate-in-18-years/107340050'],BLOG11,WEST,INDAILY],
 'Higher rates raise mortgage repayments and reduce borrowing, shifting AD left: the price level eases but output falls. The 6-3 split shows the board is divided over how much tightening is already in the pipeline, a key limitation given time lags of up to two years.',
 [Q('Analyse the transmission mechanism of monetary policy, using recent data on lending and consumer sentiment.',6)],
 'Replaces the 11 November item "Has the RBA finished raising rates?", which cited Bullock\'s reasons (excess domestic demand, capacity pressures, weak productivity, data-centre boom; monetary policy cannot change oil prices), swaps putting an 82% chance on a peak, Westpac expecting a pause on 7-8 December, AMP seeing the surveys as early signs the rises are working, and a six-year low in business conditions. ANZ (December, or less likely February hike possible) and Cotality (no cuts before the second half of 2027) are forecasts, not RBA decisions. UPDATE DUE: the 7-8 December RBA meeting.')

R('2026-11-11-cba-arrears-rise-as-rates-bite',3,'CBA\'s profit is up, but more borrowers are falling behind','2026-11-11','news',['ABC News'],
 'Shows the uneven effect of higher rates: bank profits and savers gain while recent buyers with big mortgages fall behind.',
 'Commonwealth Bank lifted its first-quarter cash profit about 8% to roughly A$2.8bn, but home loan arrears rose 7 basis points to 0.8% and home loan applications fell 16% over the year. CEO Matt Comyn said higher inflation and interest rates are hitting some households and businesses much harder than others.',
 ['4D.3','3E.4'],['Y2c.5','Y1d.5'],['P4c.3','P2h.8'],['3A.7','3E.3'],['Y1c.7','Y1d.3'],['P1e.7'],
 ['rates','housing','inequality'],['monetary'],['chart','compare'],
 [F('CBA unaudited first-quarter cash profit','about A$2.8bn (+8% on a year earlier)','first quarter 2026-27','rates','ABC News'),F('Home loans in arrears (90+ days)','0.8% (+7 basis points)','first quarter 2026-27','housing','ABC News'),F('Home loan applications','-16% over the year (home lending still +6.6%, business lending +13.6%)','first quarter 2026-27','housing','ABC News'),F('Loan impairment expense','A$300m (more than analysts expected)','first quarter 2026-27','rates','ABC News')],
 [T('Arrears','Loan repayments that are overdue (here, 90+ days).'),T('Basis point','One-hundredth of a percentage point; 7 basis points is 0.07 percentage points.')],
 [BLOG11],
 'Rising rates redistribute income from borrowers to lenders and savers, which is one reason monetary policy is described as a blunt instrument. Existing loan books are still growing but new demand is falling fast, a leading sign that credit growth will slow.',
 [Q('Discuss how rising interest rates affect the distribution of income and wealth in Australia.',6)],
 'An unaudited quarterly update reported in a live blog. Pairs with the record fall in new home loans item filed today and the 5 November NAB results item.')

R('2026-11-11-record-fall-in-new-home-loans',3,'New home lending suffers its biggest fall on record','2026-11-11','stats',['ABS','ABC News','AAP'],
 'The September quarter lending data: the steepest drop since the series began in 2002, led by investors, with the wealth effect and a GFC/COVID comparison.',
 'The value of new home loans fell 15.5% in the September quarter, the steepest drop since the ABS series began in 2002, and investors led the retreat. It was bigger than the falls during the GFC (-13.3% in 2008) and COVID (-12.9%).',
 ['3A.1','3E.4','4D.3'],['Y1a.8','Y2c.5','Y1d.5'],['P4c.7','P4c.3'],['3A.7','3A.3'],['Y1a.14','Y2b.13'],['P5a.4'],
 ['housing','growth','rates'],['monetary','fiscal'],['chart','flow'],
 [F('Value of new housing loan commitments','-15.5% (number -15%)','September quarter 2026','housing','ABS Lending Indicators'),F('Investor loans','-30.6% in number, -32.3% in value','September quarter 2026','housing','ABS Lending Indicators'),F('Owner-occupier lending','-5.3%','September quarter 2026','housing','ABS Lending Indicators'),F('First home buyer loans','-8.6% in number (-12.3% over the year)','September quarter 2026','housing','ABS via ABC News'),F('Previous largest falls','GFC -13.3% (2008); COVID -12.9% (2020)','2008, 2020','housing','ABC News')],
 [T('Lending Indicators','An ABS release measuring new loan commitments for housing, personal and business finance.'),T('Wealth effect','When asset values such as house prices fall, households feel poorer and spend less.')],
 [BLOG11,PLUNGE,INDAILY],
 'Two forces are at work: higher interest rates reduce how much people can borrow, and the sharper investor fall points to the budget\'s tax changes and falling-price expectations. J.P. Morgan calls the investor decline a structural drag steeper than in past hiking cycles. Falling lending and prices can cut spending through the wealth effect and slow dwelling investment.',
 [Q('Explain how a fall in housing lending can affect economic growth and the distribution of wealth in Australia.',4)],
 'The digest gives first home buyer loans as -8.6% in number in the text and -8.0% in its chart, which may be a different measure (value), so check the ABS release before quoting one. The ABS says falls were broad-based across states and investors were influenced by more than borrowing costs. Same data as the budget tax changes item filed today.')

R('2026-11-11-oil-aud-commodities-shipping-attacks',2,'Oil swings and the dollar firms: what it means for Australia','2026-11-11','news',['ABC News','Westpac IQ'],
 'Links Gulf shipping attacks, oil and iron ore prices to the terms of trade and the AUD.',
 'Brent crude hit two-month lows after US officials played down further military action against Iran, then rose about 1% to US$92.43 a barrel as attacks on Gulf shipping continued, while the Australian dollar edged up 0.2% to 68.78 US cents. Iron ore slipped 0.4% to US$92.40 a tonne.',
 ['2B.4','2A.1','3C.3'],['Y3e.3','Y3c.5','Y1c.4'],['P6a.2'],['2C.2','1A.1'],['Y3c.4','Y1a.7'],['P6c.1'],
 ['trade','fx','inflation','global'],['global'],['ds','flow'],
 [F('Brent crude / WTI','US$92.43 (about +1%) / US$86.60','11 November 2026','global','ABC News'),F('Australian dollar','68.78 US cents (+0.2%)','11 November 2026','fx','ABC News'),F('Iron ore','US$92.40 a tonne (-0.4%); copper -1.2%; gold about +0.5%','11 November 2026','trade','ABC News'),F('Ships attacked in the Gulf','37 in October (the most in any month since the war began); 10 so far in November','to 11 November 2026','global','ABC News'),F('Petrol price','near $2.40 a litre','November 2026','inflation','Westpac IQ')],
 [T('Terms of trade','The ratio of export prices to import prices; it rises when export prices rise relative to import prices.'),T('Price-inelastic demand','Quantity demanded changes little when price changes, such as fuel in the short run.')],
 [BLOG11,WEST],
 'Attacks on tankers shift oil supply left and, because short-run demand is inelastic, the price jumps while quantity barely falls. Australia imports most of its refined fuel, so dearer oil raises import prices, but it also exports LNG and coal, so whether the terms of trade improve depends on which prices move more.',
 [Q('Explain how changes in global commodity prices affect Australia\'s terms of trade and current account balance.',4)],
 'Single-day market prices. Complements the 10 November oil and petrol item and the AUD item filed today.')

R('2026-11-11-cop31-electrification-target-row',1,'COP31: arguments over a global electricity target','2026-11-11','news',['ABC News'],
 'The sticking point in the 35-by-35 pledge: whether the electricity must be clean, and what that means for voluntary agreements and externalities. Replaces the 10 November COP31 item.',
 'At the UN climate talks in Antalya, a push to lift electricity\'s share of world energy use from about 23% to 35% by 2035 has divided countries over whether that power must be clean. The draft wording does not require clean electricity, and analysts estimate a clean-only version could cut projected warming by 0.3°C from at least 2.6°C.',
 ['3F.4','1D.8','4G.1'],['Y1e.5','Y2f.6','Y2f.8','Y3d.6'],['P2h.3'],['4I.6','4G.2'],['Y2f.7','Y1e.7'],['P2h.4'],
 ['environment','global'],['environmental','global'],['ds','chart'],
 [F('Electricity\'s share of world energy use, now / proposed by 2035','23% / 35% (about four times the current pace of electrification)','2035 target','environment','ABC News'),F('Projected warming on the current path','2.6°C or more (clean-only version could cut about 0.3°C)','2026','environment','ABC News'),F('Rooftop-solar households targeted by 2030 (Australia-backed voluntary pledge)','300 million (as reported)','2030','environment','ABC News')],
 [T('Negative externality','A cost imposed on third parties that is not reflected in the market price.'),T('Voluntary pledge','A non-binding commitment with no penalty for missing it.')],
 [['ABC News, COP31 electric power target sparks row over cutting fossil fuel use','https://abc.net.au/news/2026-11-11/cop31-electrification-turkiye-australia/107371196']],
 'Firms set output on private costs, but burning fossil fuels imposes climate costs on others, so the market overproduces. Clean electrification shifts energy use away from that market, but if the power comes from coal or gas much of the climate benefit is lost. Because each country can free-ride, the strength of the wording (binding or voluntary, clean or any electricity) matters.',
 [Q('Assess the effectiveness of voluntary international agreements in addressing global environmental problems.',6)],
 'Replaces the 10 November ABC item, which reported COP31 accepting for the first time that warming will exceed 1.5°C, Chris Bowen saying projected warming fell from nearly 4°C before Paris to about 2.6°C, Türkiye getting 55% of its electricity from coal and gas, fossil fuel cuts not formally on the agenda, and criticism of Australia over coal expansion and extending the North West Shelf gas project. The digest gives the solar pledge as 300 million households, which should be checked against the ABC article before quoting. Partners with Australia on that pledge include Bangladesh, Kenya, Nigeria, Palau and Vanuatu. See also the Conversation explainer filed on 11 November.')

R('2026-11-11-us-inflation-fed-hike-expected',1,'Hot US inflation puts a Fed rate hike on the table','2026-11-11','news',['ABC News'],
 'Shows how US inflation and interest rate expectations reach Australia through the exchange rate and imported inflation.',
 'US consumer prices rose 0.4% in October, above the 0.3% expected and the third month in a row at 0.4% or higher, and markets now fully price a Federal Reserve rate hike at its December meeting. The US 10-year bond yield rose to about 5%, the US dollar strengthened and the Australian dollar dipped overnight before recovering to 68.78 US cents.',
 ['1A.1','2C.2','3C.3'],['Y3c.4','Y1c.4'],['P6c.1'],['2C.6','4D.3'],['Y3c.5','Y3e.3'],['P4c.3'],
 ['inflation','rates','fx','global'],['monetary','global'],['adas','flow'],
 [F('US CPI, October (month on month)','+0.4% (0.3% expected; September 0.6%)','October 2026','inflation','ABC News'),F('Market pricing for a Fed hike in December','fully priced','11 November 2026','rates','ABC News'),F('US 10-year bond yield','about 5%','11 November 2026','rates','ABC News'),F('Australian dollar','68.78 US cents (Wednesday afternoon)','11 November 2026','fx','ABC News')],
 [T('CPI','The Consumer Price Index, which measures changes in the prices of a basket of household goods and services.'),T('Interest rate differential','The gap between interest rates in two countries, which influences capital flows and exchange rates.')],
 [BLOG11],
 'A Fed rate rise widens the gap between US and Australian rates, drawing capital to the US, which tends to depreciate the AUD, raise import prices and add to Australian inflation. A Fed hike also aims to shift US AD left, slowing inflation at the cost of real GDP.',
 [Q('Explain how a rise in US interest rates could affect the Australian dollar and inflation in Australia.',4)],
 'US figures as reported in an ABC live blog. "Fully priced" is a market expectation, not a Fed decision. See the AFR weak-dollar item filed today.')

R('2026-11-09-us-china-trade-truce-extended',1,'China extends its trade truce with the US to January','2026-11-09','news',['Reuters','BusinessDay'],
 'Details of the US-China truce: the 24% tariff stays suspended, with export-control waivers and a proposed US$60bn reciprocal tariff cut, ahead of the APEC meeting.',
 'China will keep its extra 24% tariff on US goods suspended for another two months, while a 10% tariff remains, buying time before Xi Jinping and Donald Trump meet at APEC on 18-19 November. Waivers on some critical mineral export controls are extended to 10 January 2027.',
 ['1C.2','1B.1','2D.4'],['Y3a.7','Y3a.8','Y3a.11','Y3a.15'],[],['1A.3','1C.1'],['Y3a.5','Y3a.13','Y3e.3'],[],
 ['trade','global'],['trade'],['ds','flow'],
 [F('Extra tariff on US goods, suspended / tariff still in place','24% (two more months) / 10%','9 November 2026','trade','Reuters via BusinessDay'),F('Suspended penalties and export-control waivers extended to','10 January 2027 (11 US firms on the unreliable entities list; 16 on the export control list; port fees on US-linked ships)','10 January 2027','trade','Reuters via BusinessDay'),F('Proposed reciprocal tariff cuts (not finalised)','US$60bn, including about US$17bn of US farm goods','November 2026','trade','Reuters via BusinessDay'),F('Xi-Trump meeting','APEC, 18-19 November 2026','18-19 November 2026','trade','Reuters via BusinessDay')],
 [T('Tariff','A tax on imported goods that raises their domestic price.'),T('Trade truce','A temporary pause in retaliatory trade barriers while negotiations continue.')],
 [['Reuters via BusinessDay, China extends US trade truce by two months','https://businessday.co.za/world/2026-11-09-china-extends-us-trade-truce-by-two-months/']],
 'A tariff raises the domestic price to Pw+t, so farmers supply more, consumers buy less, imports shrink, the government collects revenue and deadweight loss appears. Suspending the extra 24% keeps the price wedge smaller. A US-China farm deal could also cause trade diversion: if China buys more US farm goods it may buy less from other suppliers, such as Australia.',
 [Q('Using a tariff diagram, explain the effects on Chinese consumers and US exporters if the suspended 24% tariff were reimposed.',6)],
 'The proposed US$60bn package is not final. The diagram in the digest uses US soybeans in China as the example. Replaces nothing directly: it expands the truce element of the China exports item filed on 10 November (now replaced, see the China trade surplus item filed today). UPDATE DUE: outcome of the APEC meeting. See also the 27 October US-China port-fee truce item.')

R('2026-11-11-china-trade-surplus-tops-1-trillion',1,'China\'s trade surplus tops US$1 trillion, again','2026-11-11','stats',['ABC News'],
 'Export-led growth and weak household demand produce a record surplus, with rising protectionist pressure on trading partners. Replaces the 10 November China exports item.',
 'China\'s trade surplus for the first ten months of 2026 reached US$1.04 trillion, a month earlier than last year, as Beijing relies on exports to reach its growth target. October exports rose 35.2% year on year to US$412.3bn, and exports to the US rose 32.9% despite US tariffs.',
 ['1A.3','1A.1','1D.6'],['Y3a.15','Y3e.3'],[],['1C.2','2B.4'],['Y3a.7','Y3a.5'],[],
 ['trade','global','growth'],['trade'],['chart','flow'],
 [F('China trade surplus, January-October 2026','US$1.04 trillion (2025 full-year record: US$1.2 trillion)','January-October 2026','trade','ABC News'),F('Exports, October (year on year)','+35.2% to US$412.3bn','October 2026','trade','ABC News'),F('Imports, October (year on year)','+41.6% to US$307.1bn','October 2026','trade','ABC News'),F('Exports to the US, October','+32.9%','October 2026','trade','ABC News'),F('China\'s surplus with the EU, January-October','US$310.7bn (US$241.6bn a year earlier)','January-October 2026','trade','ABC News'),F('China\'s 2026 GDP growth target','4.5-5%','2026','growth','ABC News')],
 [T('Trade surplus','The value of exports is greater than the value of imports.'),T('Export-led growth','A strategy that relies on selling to foreign markets, not domestic demand, to drive GDP.')],
 [['ABC News, China\'s trade surplus surpasses $US1 trillion for second straight year','https://abc.net.au/news/2026-11-11/china-trade-surpasses-1-trillion-for-second-straight-year/107372090']],
 'A surplus means China produces more than it spends at home. With weak household demand and low inflation, Chinese firms push output into world markets, which helps China\'s GDP but squeezes import-competing industries elsewhere and raises protectionist pressure in the US and EU. For Australia, Chinese industrial output underpins iron ore demand, but a growth model built on exports is more exposed to tariffs.',
 [Q('Explain how China\'s reliance on export-led growth could increase protectionism in the global economy.',4)],
 'Replaces the 10 November item "China\'s exports boom as its shoppers hold back", which reported China\'s consumer prices up just 0.7% in the year to October (September 0.9%, forecast 0.8%), exports +35.2% (September +36.3%), and the extra 24% tariff on US goods kept suspended for two months from 10 November with the 10% tariff staying. China\'s domestic inflation is well below its roughly 2% goal, according to analysts quoted. The Xi-Trump APEC meeting is in Shenzhen on 18-19 November. See the US-China truce item filed today.')

R('2026-11-10-spender-cgt-alternative',4,'Business groups back a simpler capital gains tax model','2026-11-10','news',['Australian Financial Review'],
 'The equity-efficiency trade-off in capital gains tax reform, with three models compared.',
 'Peak industry groups, economists and business leaders are urging the government to adopt independent MP Allegra Spender\'s alternative to the May budget\'s capital gains tax changes, which they say would raise as much revenue with far less complexity. The budget replaced the 50% CGT discount with an inflation-based discount on all assets and a minimum 30% CGT rate.',
 ['4C.1','4C.2','3E.3'],['Y2b.3','Y2b.13','Y1d.5'],['P5b.1','P5b.3'],['3E.4','4B.1'],['Y2b.14','Y1d.3'],['P2h.8','P5a.1'],
 ['budget','inequality','investment'],['fiscal'],['chart','compare'],
 [F('Old CGT discount (abolished in May)','50% on assets held over 12 months','before May 2026','budget','AFR (Phillip Coorey)'),F('Budget model','inflation-based discount on all assets; minimum 30% CGT rate','May 2026 budget','budget','AFR (Phillip Coorey)'),F('Spender model','inflation-based discount for passive assets; flat 40% discount for active assets; scraps the start-up carve-out (IBCC)','2026','budget','AFR (Phillip Coorey)'),F('Business owners backing the Spender model','more than 350','November 2026','budget','AFR (Phillip Coorey)'),F('Taxable gain on a $1m gain from a zero-cost stake: old 50% / Spender 40% / budget indexation','$500k / $600k / $1,000k (simplified example)','November 2026','budget','AFR (Phillip Coorey)')],
 [T('Capital gains tax (CGT)','Tax on the profit made when an asset is sold for more than it cost.'),T('Active vs passive assets','Active assets are businesses, shares and options; passive assets are such as investment property.')],
 [AFR('Business, economists urge Chalmers to adopt Spender\'s CGT model, Phillip Coorey, 10-11 Nov 2026')],
 'Taxing gains more like wages improves vertical equity, since capital gains flow mainly to high-wealth households, but critics say it reduces the incentive to take risks and invest, which matters for productivity. A start-up founder with a zero-cost stake has nothing to index, so the whole gain is taxable.',
 [Q('Evaluate the trade-off between equity and efficiency in recent changes to Australia\'s capital gains tax.',6)],
 'The chart example is simplified and ignores the start-up carve-out and personal tax rates. Supporters say the PBO has costed the Spender model as raising as much revenue as the budget version; that is their claim, so check the PBO costing before quoting. Backers include Ai Group\'s Innes Willox, ACCI\'s Andrew McKellar and economist Robert Breunig. The remaining budget bills are due to pass within a fortnight. UPDATE DUE: Senate vote on the budget bills.')

R('2026-11-11-albanese-at-cop31',1,'Albanese at COP31: climate policy meets political reality','2026-11-11','news',['Australian Financial Review'],
 'The free-rider problem applied to COP31, with the US absent, and the costs and benefits Australia claims from its role.',
 'Anthony Albanese has arrived at the COP31 climate summit in Antalya, Türkiye, the first Australian prime minister at a COP since 2021, as Australia oversees the negotiations without the United States at the table. The US has withdrawn from the UN climate process under President Trump.',
 ['1D.8','3F.4','1D.6'],['Y2f.6','Y3d.6','Y2f.8'],['P2h.3'],['4I.6','1A.1'],['Y1e.7','Y3a.13'],[],
 ['environment','global'],['environmental','global'],['compare'],
 [F('Countries in the COP31 negotiations','200 or more','November 2026','environment','AFR (Ryan Cropp)'),F('Electrification goal by 2035','35%','2035','environment','AFR (Ryan Cropp)'),F('Estimated cost of hosting COP31 in Adelaide','well over $1 billion on government estimates (Türkiye pays most under the deal)','2026','budget','AFR (Ryan Cropp)'),F('Paris warming goal','1.5°C, already exceeded','2026','environment','AFR (Ryan Cropp)')],
 [T('Free-rider problem','Countries benefit from others\' emissions cuts without paying the cost themselves.'),T('Global public good','A benefit, such as a stable climate, that no country can be excluded from enjoying.')],
 [AFR('COP is a political headache Albanese can\'t dodge, Ryan Cropp, 11 Nov 2026')],
 'Both countries are better off if both cut emissions, but each does even better by free-riding, so the likely outcome is that neither acts. When a large emitter such as the US leaves, the gains from cooperation shrink and others have less reason to keep their own pledges. International agreements are hard to enforce because pledges are largely voluntary.',
 [Q('Explain why the withdrawal of a major economy weakens international cooperation on climate change.',4)],
 'The pay-offs in the decision table are illustrative, not data. The costs and benefits of Australia\'s role are the arguments reported, not findings: backlash over spending while rates are high against Pacific leadership, national security and economic interest in the energy transition. Bowen is focusing on getting countries to implement existing pledges.')

R('2026-11-11-aukus-workforce-skills-strategy',4,'$88m to train an AUKUS workforce amid a skills shortage','2026-11-11','news',['Australian Financial Review'],
 'A labour market policy case: training places for a big defence project against a national shortage of skilled trades.',
 'The federal government will spend $88 million over six years to train workers for nuclear-powered submarines under the 2026 Nuclear-Powered Submarine Workforce Strategy, targeting up to 275 apprentices and trainees in WA and SA. ASPI, citing BuildSkills Australia, estimates a shortfall of about 110,000 skilled trades workers, with AUKUS competing against infrastructure and energy projects.',
 ['3B.3'],['Y2e.6','Y2e.7','Y1b.6'],['P3b.1'],['3B.2','4E.1'],['Y2e.8','Y1b.11'],['P3d.1'],
 ['employment','productivity','investment'],['labour','micro'],['ds','flow'],
 [F('Nuclear-Powered Submarine Workforce Strategy','$88 million over six years; up to 275 apprentices and trainees','2026','employment','AFR (Nicola Smith)'),F('Estimated shortfall of skilled trades workers','about 110,000','2026','employment','ASPI, citing BuildSkills Australia'),F('Investment in HMAS Stirling','$8 billion (hosts one UK and up to four US nuclear subs from 2027)','from 2027','investment','AFR (Nicola Smith)')],
 [T('Skills shortage','Employers cannot find enough workers with the required skills at current wages.'),T('Structural unemployment','Joblessness caused by a mismatch between workers\' skills and the jobs available.')],
 [AFR('$88m boost for AUKUS workforce amid skills shortage, Nicola Smith, 11 Nov 2026')],
 'Big projects lift demand for tradespeople and, with supply fixed in the short run, wages jump, a source of cost inflation. Training and skilled migration shift supply right and ease wage pressure, but 275 places over six years is small next to a 110,000-worker shortfall, so migration and fewer competing projects also matter.',
 [Q('Assess the effectiveness of education and training policies in addressing skills shortages in Australia.',6)],
 'The shortfall estimate is ASPI\'s, using BuildSkills data. ASPI recommends an AUKUS-specific skilled visa and industry leaders warn of a maritime skills crisis and slow security clearances. The strategy also helps tradespeople move into welding, mechanical and electrical roles.')

R('2026-11-11-weak-aud-threatens-rba-inflation-fight',2,'A weaker Australian dollar complicates the RBA\'s inflation fight','2026-11-11','news',['Australian Financial Review'],
 'Shows the exchange rate channel working against the RBA: a falling AUD raises import prices, and weakens the transmission of rate rises. Replaces the 10 November AUD item.',
 'The Australian dollar fell to a seven-month low of 68.42 US cents after hotter-than-expected US inflation data, making imports dearer just as the Reserve Bank is trying to bring inflation down. RBA modelling suggests exchange-rate moves account for up to two-thirds of the effect of rate changes on inflation, so a weaker dollar weakens that channel.',
 ['2C.2','2C.3','2C.6','4D.3'],['Y3c.2','Y3c.4','Y3c.5','Y2c.5'],['P6c.1'],['3C.3','2A.1'],['Y1c.4','Y2c.7'],['P4c.3'],
 ['fx','inflation','rates'],['monetary'],['fx','flow'],
 [F('Australian dollar','68.42 US cents low in New York (seven-month low); about 68.78 on Wednesday','11 November 2026','fx','AFR (Lea Jurkovic)'),F('US 2-year bond yield / 10-year yield','+18 basis points / towards 5%','11 November 2026','rates','AFR (Lea Jurkovic)'),F('Share of the effect of rate changes on inflation that works through the exchange rate','up to two-thirds (RBA modelling)','2026','rates','AFR (Lea Jurkovic)'),F('Market odds of a sixth RBA hike by early 2027','about 1 in 4 (would take the cash rate above 5%)','11 November 2026','rates','AFR (Lea Jurkovic)'),F('CBA AUD forecasts','68 US cents by year-end; 66 by March 2027','2026-2027','fx','CBA via AFR')],
 [T('Depreciation','A fall in the value of a currency against another under a floating exchange rate.'),T('Imported inflation','Rising domestic prices caused by dearer imports, for example after a depreciation.')],
 [AFR('A weak $A starting to threaten RBA\'s inflation fight, Lea Jurkovic, 11 Nov 2026')],
 'Higher expected US rates make US assets more attractive, so demand for AUD falls and the exchange rate depreciates, and imports cost more in AUD. A full answer shows both sides: a depreciation helps export competitiveness and the trade balance but adds to imported inflation, which matters most when inflation is already above the 2-3% target.',
 [Q('Explain how a depreciation of the Australian dollar could affect inflation and the RBA\'s monetary policy decisions.',4)],
 'Replaces the 10 November item (AUD about 69.2 US cents; swaps giving an 82% chance of an RBA peak at 4.85% with a quarter-point cut fully priced by end-2027; 10-year yield about 4.99%, lowest since late August; iron ore about US$93; support near the June low of 0.6867). The Fed official\'s suggestion of a 0.5-point hike (Christopher Waller) and the market odds are as reported by the AFR. See the US inflation item filed today.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
