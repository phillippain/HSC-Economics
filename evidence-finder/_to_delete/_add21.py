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
      angle=angle,questions=questions,note=note,added='2026-11-17'))

ABC='ABC News'
MK='https://www.abc.net.au/news/2026-11-16/asx-markets-business-live-news-nov-16/107388134'
FI='https://www.fixedincomenews.com.au/wages-jobs-and-rba-minutes-put-australian-bonds-to-the-test-as-yields-match-treasuries/'

R('2026-11-17-rba-minutes-wages-jobs-week','4','A big week for the RBA: minutes, wages and jobs','2026-11-17','news',['ABC News','Fixed Income News Australia','RBA'],
 "Preview of the data that will test the RBA's fifth hike this year: the minutes, the Wage Price Index and October jobs.",
 "After lifting the cash rate to an 18-year high of 4.85% on 3 November (a 6-3 split), the RBA releases its minutes on Tuesday 17 November, followed by the Wage Price Index (Wednesday) and October jobs (Thursday). The RBA expects inflation to stay above 3% for the coming year and to reach the 2-3% target band only in late 2027.",
 ['4D.1','4D.2','4D.3'],['Y2c.4','Y2c.5','Y2c.7'],['P4c.3'],
 ['3C.3','3B.2','3A.4'],['Y1c.4','Y1c.6','Y1b.11'],['P4c.4'],
 ['rates','inflation','employment'],['monetary'],['phillips','flow'],
 [F('RBA cash rate','4.85% (18-year high; fifth rise this year; board split 6-3)','3 November 2026','rates','RBA'),
  F('Expected wage growth (CBA)','+0.9% for the quarter; 3.3% for the year (up from 3.2%)','Week of 17 November 2026','employment','Fixed Income News Australia'),
  F('Expected unemployment rate, October','4.7%; about +30,000 jobs expected after a fall of almost 40,000 in September','Week of 17 November 2026','employment','ABC News'),
  F('Annual inflation','4.3%','November 2026','inflation','ABC News'),
  F('New housing lending, September quarter','-15.5%','September quarter 2026','housing','ABC News')],
 [T('Real wages','Wage growth minus inflation; a measure of changes in purchasing power.'),T('Inflation expectations','What households and firms expect inflation to be; if they rise the short-run Phillips curve shifts up.')],
 [['ABC News: ASX falls as miners drag, 16 Nov 2026',MK],['Fixed Income News Australia: Wages, jobs and RBA minutes put Australian bonds to the test, 16 Nov 2026',FI],['RBA: Statement by the Monetary Policy Board, 3 Nov 2026','https://www.rba.gov.au/media-releases/2026/mr-26-30.html']],
 "Use the week as a monetary policy case: the RBA raised rates because inflation (4.3%) sits above the 2-3% target and it worries about expectations; real wages of about -1% (3.3% minus 4.3%) and weak lending show the transmission mechanism working through falling spending. A rise in inflation expectations shifts the short-run Phillips curve up, so the same unemployment comes with higher inflation.",
 [Q("Wages are expected to grow about 3.3% while inflation is 4.3%. Calculate approximate real wage growth and explain what it means for consumer spending and the RBA's next decision.",4)],
 "PREVIEW filed as published: UPDATE DUE. Add the minutes (Tue 17 Nov), Wage Price Index (Wed 18 Nov) and October jobs (Thu 19 Nov) when released. Forecast figures (3.3%, 4.7%, +30,000) are CBA and economist expectations, not outcomes. Related: the 11 November item on whether the RBA has peaked.")

R('2026-11-16-cost-of-essentials-price-controls','3','Rising cost of essentials puts affordability on the policy agenda','2026-11-16','news',[ABC],
 "Gives the arguments for and against temporary price controls on essentials, using the textbook price ceiling diagram.",
 "Economist Isabella Weber argues that rapidly rising costs of housing, food, energy, water, health care and transport are testing democracies, and that governments should put affordability at the centre of policy. She is open to targeted, temporary price controls, limits on market concentration and changes to how essentials are supplied.",
 ['3C.4','3E.6','4E.2'],['Y1c.7','Y1d.9','Y2d.3'],['P2i.2','P2i.3','P2i.4'],
 ['3C.3','4E.3','4I.3'],['Y1c.8','Y2d.6','Y1d.5'],['P2h.6','P2h.8'],
 ['inflation','inequality'],['micro'],['ds','compare'],
 [F('Australia annual inflation rate','4.3%','November 2026','inflation','ABC News'),
  F('Essentials Weber targets','6: housing, food, energy, water, health, transport','16 November 2026','inflation','ABC News'),
  F('Earnings calls analysed in cited research','138,962','16 November 2026','inflation','ABC News'),
  F('US data cited (2000-2022)','Essentials rose faster than non-essentials such as TVs and electronics','2000-2022','inflation','ABC News')],
 [T('Price ceiling','A legal maximum price set below the market equilibrium, which creates a shortage.'),T('Market concentration','When a few large firms dominate an industry and have pricing power.')],
 [["ABC News: The cost of basics keeps rising but 'anti-fascist economics' could lower them, 16 Nov 2026",'https://www.abc.net.au/news/2026-11-16/anti-fascist-economics-isabella-weber-cost-of-living-essentials/107382064'],['ABC News: When community concerns collide in the fight over data centres, 16 Nov 2026 (4.3% inflation)','https://www.abc.net.au/news/2026-11-16/when-community-concerns-collide-in-data-centre-fight/107344810']],
 "For an evaluate question weigh quick relief for low-income households and a break in price spikes against shortages (quantity demanded above quantity supplied at the ceiling), rationing, weaker incentives to invest and the difficulty of removing controls. Weber's case rests on temporary, targeted use plus action on market concentration.",
 [Q("Evaluate the effectiveness of price controls as a response to rising living costs in Australia.",6)],
 "Interview-based opinion piece: Weber's views are one economist's position and her 2021 article drew a strong backlash from other economists. The digest's data are US figures (2000-2022), not Australian. Use the 4.3% inflation figure from the second source only.")

R('2026-11-16-superannuation-nears-5-trillion','3','Super nears $5 trillion. Who is it serving?','2026-11-16','news',[ABC],
 "Shows how compulsory super shapes the distribution of wealth, retirement income and the role of the age pension.",
 "Australians' compulsory superannuation savings are about to pass $5 trillion, roughly $178,571 for each of 28 million people and about 20 months of GDP. Yet two-thirds of retirees still draw a full or part age pension, and fees and marketing spending are under scrutiny.",
 ['3E.4','3E.1','3E.3'],['Y1d.1','Y1d.3','Y1d.9'],['P4a.3','P2h.8'],
 ['3E.6','4I.5','2A.2'],['Y1d.2','Y1d.10'],['P4a.1'],
 ['inequality'],['micro'],['chart','compare'],
 [F('Total super savings','About $5 trillion (about 20 months of GDP; about $178,571 per person)','November 2026','inequality','ABC News'),
  F('Compulsory employer contribution rate','12% of wages','November 2026','inequality','ABC News'),
  F('Retirees drawing a full or part age pension','Two-thirds','November 2026','inequality','ABC News'),
  F('Marketing vs complaints spend, 10 largest funds, FY25','$388 million vs $45 million','FY25','inequality','APRA, via ABC News'),
  F('Fees: index option vs active default','As low as 0.03% vs about 0.5-1%','November 2026','inequality','ABC News'),
  F('Projected super pool by 2045','$12 trillion','2045 projection','inequality','Deloitte, via ABC News')],
 [T('Defined contribution','Retirement balance depends on what is paid in and the returns earned, not on a promised payout.'),T('Gini coefficient','A measure of inequality from 0 (perfect equality) to 1; A/(A+B) on a Lorenz curve.')],
 [["ABC News: Australians' superannuation to hit $5 trillion. How well is it serving us?, 16 Nov 2026",'https://www.abc.net.au/news/2026-11-16/is-super-serving-its-members-in-retirement/107387284']],
 "Because contributions are a fixed share of wages, higher earners build larger balances, so super can widen wealth gaps while the age pension acts as a safety net. Link to national saving and to reliance on foreign capital in Topic 2. High fees compound over decades, so fee differences matter for final balances.",
 [Q("Explain how Australia's superannuation system affects the distribution of wealth.",4)],
 "The $5 trillion figure is 'about to pass' rather than passed. The 20 months of GDP, $178,571 per person and Deloitte $12 trillion projection are as reported in the source and were not independently checked. FY25 marketing figures are APRA data via ABC.")

R('2026-11-16-data-centre-boom-investment-pushback','3','Data centre boom: billions in investment, rising community pushback','2026-11-16','news',[ABC],
 "Uses data centre investment to show how a demand boom near full capacity adds inflation now and capacity later.",
 "Local data centre operators have raised at least $35 billion this year, 46% more than in 2025, according to an internal RBA note. With inflation at 4.3%, the building boom adds to demand for materials, labour, power and water, while community opposition is growing and Victoria and NSW have stalled several proposals.",
 ['3A.1','3A.6','3C.3'],['Y1a.6','Y1a.10','Y1c.5'],['P1e.6','P3c.4'],
 ['3A.7','3F.4','4D.3'],['Y1c.4','Y1e.5','Y2c.4'],['P3c.5','P1e.7'],
 ['investment','inflation','growth','environment'],['monetary'],['adas','compare'],
 [F('Raised by data centre operators in 2026','$35 billion+ (46% more than 2025)','2026','investment','Internal RBA note, via ABC News'),
  F('Australian data centre capacity','About 2.3 GW across 79 data centres (about 1.5 million homes)','November 2026','investment','IBISWorld, via ABC News'),
  F('Planned projects (AEMO estimate)','23-67 GW','November 2026','environment','AEMO, via ABC News'),
  F('Data centre technology that is imported','About 70%','November 2026','trade','RBA Governor Bullock, via ABC News'),
  F('Annual inflation','4.3%','November 2026','inflation','ABC News')],
 [T('Capacity constraint','When the economy is near its productive limit, so extra demand raises prices more than output.'),T('Import leakage','Spending on imports that flows out of the domestic economy.')],
 [['ABC News: When community concerns collide in the fight over data centres, 16 Nov 2026','https://www.abc.net.au/news/2026-11-16/when-community-concerns-collide-in-data-centre-fight/107344810']],
 "In the short run construction raises I and shifts AD right; near LRAS the price level rises. In the long run finished data centres lift capacity (LRAS right). About 70% imported technology means part of the spending leaks to imports. The RBA cited AI-related investment as one reason for its November rate rise.",
 [Q("Assess the impact of rising business investment on economic growth and inflation in Australia.",6)],
 "Capacity (2.3 GW) and the 23-67 GW planned range come from different bodies (IBISWorld, AEMO). Related earlier cards: 8 November (opportunity or problem), 5 November (NSW electricity demand) and 9 November (RBA and the AI boom).")

R('2026-11-16-commodity-prices-miners-drag-asx','2','Miners drag the ASX lower as commodity prices soften','2026-11-16','news',[ABC],
 "Shows how weaker Chinese demand lowers commodity prices, the terms of trade and Australian export income.",
 "Weaker Chinese demand weighed on Australia's key commodity exports and the ASX 200 fell 0.4% to about 9,045 on Monday 16 November. Iron ore fell to US$90.95 a tonne, copper is near a four-month low and port stockpiles in China are rising.",
 ['2A.1','2B.4','3D.1'],['Y1a.7','Y3e.1','Y3e.3'],['P6a.2','P2d.1'],
 ['3D.3','1A.8','4C.1'],['Y3c.4','Y3a.15'],['P2d.2'],
 ['trade','global'],[],['ds','flow'],
 [F('ASX 200','-0.4% to about 9,045','16 November 2026','trade','ABC News'),
  F('BHP share price','-2.8%','16 November 2026','trade','ABC News'),
  F('New Hope share price','-5.9% (quarterly coal production -10%)','16 November 2026','trade','ABC News'),
  F('Iron ore','US$90.95 a tonne (-0.4%)','13 November 2026','trade','ABC News'),
  F('LME copper','US$13,467 a tonne (-1.3%; fifth straight weekly fall)','13 November 2026','trade','ABC News'),
  F('Iron ore stockpiles at 10 Chinese ports','108 million tonnes (+3.3 million)','13 November 2026','trade','ABC News')],
 [T('Terms of trade','An index of export prices divided by import prices, multiplied by 100.'),T('Stockpile','Unsold inventory; rising stockpiles suggest supply is running ahead of demand.')],
 [['ABC News: ASX falls as miners drag, Coles investigates cybersecurity incident, 16 Nov 2026',MK]],
 "Australia is a price taker in world commodity markets, so falling iron ore, coal and copper prices flow straight into export prices and the terms of trade, lowering mining profits, company tax and the current account. Pair with the China October slowdown card for the cause.",
 [Q("Explain the relationship between commodity prices, the terms of trade and Australia's current account balance.",4)],
 "Single-day and single-week market moves. The AUD figures are on a separate card (Australian dollar slide) from the same live blog. Supersedes nothing: earlier commodity items remain relevant for the trend.")

R('2026-11-16-aud-slides-as-rate-gap-narrows','2','The dollar slides as the gap with US interest rates narrows','2026-11-16','news',[ABC,'Fixed Income News Australia'],
 "Shows how a narrowing interest rate gap with the US lowers demand for the AUD and what a depreciation does to winners and losers.",
 "The Australian dollar lost 1.4% last week, closing Friday at 67.71 US cents and falling to 67.57 US cents on Monday afternoon. Rising US yields and fading expectations of another RBA hike have narrowed the interest rate gap that supported it, and Australian and US 10-year yields are now almost level.",
 ['2C.2','2C.3','2C.6'],['Y3c.2','Y3c.4','Y3c.5'],['P6c.1'],
 ['4D.3','3C.3','2B.4'],['Y2c.5','Y1c.4','Y3c.6'],['P4c.3'],
 ['fx','rates'],['monetary'],['fx','flow'],
 [F('AUD / USD','67.71 US cents on Friday (-0.5%; -1.4% for the week); 67.57 at 4:15pm Monday','16 November 2026','fx','ABC News'),
  F('Market chance of an RBA hike in December','About 6% (cash rate 4.85%)','16 November 2026','rates','Fixed Income News Australia'),
  F('10-year bond yield: Australia / US','About 5.14% / 5.15%','16 November 2026','rates','Fixed Income News Australia')],
 [T('Depreciation','A fall in the value of a floating currency against another currency.'),T('Interest rate differential','The gap between Australian and overseas interest rates, which drives capital flows.')],
 [['ABC News: ASX falls as miners drag, 16 Nov 2026',MK],['Fixed Income News Australia: Wages, jobs and RBA minutes put Australian bonds to the test as yields match Treasuries, 16 Nov 2026',FI]],
 "A narrower yield gap means foreign investors want fewer Australian assets, so demand for AUD shifts left and the exchange rate depreciates. Exporters, tourism and import-competing firms gain; importers, travellers and foreign-currency borrowers lose. Higher import prices add to inflation, which the RBA watches closely.",
 [Q("Using a diagram, explain how a narrowing interest rate gap with the US affects the AUD. Then analyse the effects on the current account.",6)],
 "Replaces the 12 November item 'Aussie dollar slips as the US dollar hits a 19-month high' (US dollar index +0.7% to its highest since April 2025 after hot US inflation; AUD 68.31 US cents, -0.2%, opening just under 69; iron ore US$92 a tonne, -0.6%; Brent US$91.67 a barrel, -1.2%; 10-year yields Australia 5.04% and US 4.99%). Market prices; moves daily.")

R('2026-11-13-us-bond-yields-jump-fed-hike-bets','1','US bond yields jump as markets bet on a Fed rate hike','2026-11-13','news',['Fixed Income News Australia',ABC],
 "Shows how US interest rate expectations spread to Australia through bond yields, capital flows and the exchange rate.",
 "US government bond yields had their biggest weekly rise since April 2025 as markets priced in a likely Fed rate hike in December. The US 10-year closed Friday at 5.152% and Australian long-term yields rose to match it.",
 ['1A.4','2C.2','4D.3','4H.2'],['Y3c.4','Y3e.3','Y2c.8'],['P4c.2','P4c.3'],
 ['2A.2','3C.3','4H.2'],['Y3c.5','Y3b.3'],['P6c.1'],
 ['rates','fx','global'],['monetary','global'],['chart','flow'],
 [F('US 10-year yield','5.152% (+29.4 basis points on the week, the largest since April 2025)','Friday 13 November 2026','rates','Fixed Income News Australia'),
  F('US 2-year yield','4.872% (+35.2 basis points)','Friday 13 November 2026','rates','Fixed Income News Australia'),
  F('Market odds of a December Fed hike','About 88% for 0.25 points; 12% for 0.50 points','13 November 2026','rates','Fixed Income News Australia'),
  F('Australian 10-year yield','5.14% (US 10-year also 5.14% early Monday)','16 November 2026','rates','Fixed Income News Australia')],
 [T('Basis point','One-hundredth of a percentage point; 29 basis points is 0.29 percentage points.'),T('Bond yield','The return on a government bond, which moves with expected interest rates.')],
 [['Fixed Income News Australia: Wages, jobs and RBA minutes put Australian bonds to the test as yields match Treasuries, 16 Nov 2026',FI],['ABC News: ASX falls as miners drag, 16 Nov 2026',MK]],
 "Evidence that Australia is closely tied to global financial markets: US rates help set Australian borrowing costs, and similar yields reduce the reason to hold Australian assets, lowering capital inflows and the AUD. It also shows the limits on a small open economy's monetary independence (limitation: global influences).",
 [Q("Explain how a rise in US interest rates can affect Australia's exchange rate and financial flows.",4)],
 "Fed Chair Kevin Warsh was due to speak Monday US time and the Fed's October minutes are due Wednesday 18 November: UPDATE DUE if the December hike odds change. Market odds are as reported by Fixed Income News Australia. Related: 12 November card on hot US inflation and a Fed hike.")

R('2026-11-16-japan-gdp-contracts-september-quarter','1','Japan\'s economy shrinks in the September quarter','2026-11-16','stats',[ABC],
 "Gives a current example of a surprise fall in a major trading partner's GDP, separating a slowdown from a recession.",
 "Japan's real GDP fell at an annualised 0.1% in the September quarter, against a forecast of +0.3%, as private consumption dropped 0.3%. The June quarter was revised up to +1.7% annualised, so Japan is not in a technical recession.",
 ['1A.8','1D.9','3A.4'],['Y1a.5','Y1a.3','Y3e.3'],['P1e.4','P1e.5','P1e.7'],
 ['2A.1','3A.7'],['Y1a.6','Y1a.16'],['P1e.1'],
 ['growth','global'],[],['chart','flow'],
 [F('Japan real GDP, September quarter (annualised)','-0.1% (forecast +0.3%)','16 November 2026','growth','ABC News'),
  F('Japan real GDP, June quarter (revised, annualised)','+1.7%','16 November 2026','growth','ABC News'),
  F('Japan private consumption','-0.3%','September quarter 2026','growth','ABC News')],
 [T('Annualised rate','A quarterly change scaled up to show what it would be over a full year.'),T('Technical recession','Two consecutive quarters of negative growth.')],
 [['ABC News: ASX falls as miners drag, 16 Nov 2026',MK]],
 "One negative quarter is a slowdown, not a technical recession. Consumption is the largest part of aggregate demand, so a fall in household spending pulls GDP down directly. Japan is one of Australia's largest export markets, so weaker demand is a risk to exports such as energy and food.",
 [Q("Using Japan's GDP figures, distinguish between an economic slowdown and a recession.",3)],
 "Single quarter, first estimate: later revision is possible. Daiwa's Kento Minami is quoted saying the economy is probably still growing at a moderate pace.")

R('2026-11-16-cop31-first-draft-deal-final-week','1','Australia tables the first COP31 draft deal as talks enter their final week','2026-11-16','news',['AFP via Yahoo News','UN News','Nature World News'],
 "Updates the COP31 story with the first draft cover decision and the open disputes over fossil fuels and finance.",
 "As co-host and lead negotiator of COP31 in Antalya, Türkiye, Australia released the first draft of the summit's overall cover decision. It calls for faster action to move away from fossil fuels, and about 200 countries must agree on a final text by Friday 20 November.",
 ['1D.8','3F.4','3F.2','4G.4'],['Y1e.5','Y2f.6','Y2f.8'],['P2h.3','P2h.4'],
 ['4G.3','4I.6','3F.1'],['Y1e.7','Y1e.4'],['P2i.1'],
 ['environment','global'],['environmental','global'],['ds','flow'],
 [F('Proposed electricity share of final energy demand by 2035','35%','16 November 2026','environment','AFP via Yahoo News'),
  F('Minimum adaptation funding developing countries want','US$120 billion (triple current levels)','16 November 2026','environment','AFP via Yahoo News'),
  F('Countries that must agree a final text','About 200, by Friday 20 November 2026','16 November 2026','global','UN News')],
 [T('Negative externality','A cost imposed on third parties that is not reflected in the market price, such as emissions.'),T('Adaptation finance','Funding that helps countries cope with climate impacts.')],
 [["AFP via Yahoo News: COP31 draft deal calls for 'accelerated action' to exit fossil fuels, 16 Nov 2026",'https://www.yahoo.com/news/science/articles/cop31-draft-deal-calls-accelerated-130134626.html'],['UN News: COP31 enters decisive week as climate talks face political test, 16 Nov 2026','https://news.un.org/en/story/2026/11/1168812'],['Nature World News: COP31 enters its final week with fossil fuels and climate finance still unresolved, 16 Nov 2026','https://www.natureworldnews.com/articles/73864/20261116/cop31-enters-its-final-week-with-fossil-fuels-and-climate-finance-still-unresolved.htm']],
 "Climate change is a negative externality: producers count only private costs, so output is above the socially efficient level. Emissions cross borders, so one country acting alone invites free riding, which is why international agreements matter. Saudi Arabia and Russia have long opposed firm targets and the US skipped the talks for a second year.",
 [Q("Explain why international cooperation is needed to address climate change. Refer to market failure in your answer.",4)],
 "UPDATE DUE: add the final COP31 outcome after Friday 20 November. Draft text only; not agreed. Climate minister Chris Bowen chairs the negotiations. Related earlier cards: 11 November (electrification target row, 35% by 2035 pledge, Albanese at COP31).")

R('2026-11-14-trump-xi-putin-apec-shenzhen','1','Trump, Xi and Putin to meet at APEC in Shenzhen','2026-11-14','news',['Al Jazeera','Bloomberg'],
 "Previews the first US-China-Russia leaders' meeting at APEC against the background of the US-China tariff war.",
 "The White House has confirmed the first meeting between the US, Chinese and Russian leaders, on the sidelines of APEC in Shenzhen on 18-19 November. It follows a tariff war that pushed US-China tariffs into triple digits before both sides cut them.",
 ['1C.2','1B.3','2D.4'],['Y3a.7','Y3a.8','Y3a.11'],[],
 ['1B.1','1C.1','1A.3'],['Y3a.13','Y3a.15','Y3e.3'],[],
 ['trade','global'],['trade'],['ds','compare'],
 [F('US tariff increase on Chinese goods last year','145%','2025','trade','Al Jazeera'),
  F("China's retaliatory levies on US imports",'125%','2025','trade','Al Jazeera'),
  F('APEC leaders summit','18-19 November 2026, Shenzhen','14 November 2026','trade','Al Jazeera'),
  F('Strait of Hormuz closure','More than 100 days; about a third of China\'s crude oil used to pass through','14 November 2026','trade','Al Jazeera')],
 [T('Tariff','A tax on imported goods.'),T('APEC','Asia-Pacific Economic Cooperation, a 21-member regional forum that promotes trade and investment; Australia is a member.')],
 [['Al Jazeera: Trump-Xi-Putin trilateral meeting at APEC: what to expect, 14 Nov 2026','https://www.aljazeera.com/news/2026/11/14/trump-xi-putin-trilateral-meeting-at-apec-what-to-expect'],['Bloomberg: China, US discuss tariffs in first meeting of trade council, 14 Nov 2026 (headline only)','https://www.bloomberg.com/news/articles/2026-11-14/china-the-us-discuss-tariffs-in-first-meeting-of-trade-council']],
 "Tariff diagram: the tariff lifts the price to Pw+t, cuts consumption and imports, raises domestic output and government revenue and creates deadweight losses; cutting tariffs reverses this. Australia benefits from stronger Chinese growth and calmer trade but is exposed if protectionism returns (2D.4).",
 [Q("Using a diagram, explain the effects of a tariff on domestic consumers, domestic producers and government revenue.",6)],
 "PREVIEW filed as published: UPDATE DUE after the 18-19 November summit. Bloomberg is cited by headline only. A US official said no arms control agreement is expected. Related: 9 November card on China extending the trade truce to January.")

R('2026-11-16-china-economy-loses-momentum-october','1','China\'s economy loses momentum in October','2026-11-16','stats',[ABC],
 "Gives October Chinese activity data that explain the fall in iron ore and miners' shares and show how China's slowdown reaches Australia.",
 "Factory output, retail sales and investment in China all came in weaker than expected in October, and ANZ's China economist does not expect new stimulus before the end of the year. That is bad news for Australia's biggest export market.",
 ['1A.8','1E.1','2B.4'],['Y3e.3','Y1a.7','Y3a.15'],['P6a.2'],
 ['2A.1','3D.3','1D.9'],['Y3c.4','Y3e.1'],['P1e.6'],
 ['global','growth','trade'],[],['adas','flow'],
 [F('China industrial output, year to October','+4.8% (forecast 5.3%; September 5.5%)','16 November 2026','growth','ABC News'),
  F('China retail sales, year to October','+0.4% (September 1.1%)','16 November 2026','growth','ABC News'),
  F('China fixed-asset investment, January-October','-8.1%','16 November 2026','investment','ABC News'),
  F('Iron ore / BHP shares','US$90.95 a tonne (Friday) / -2.8% (Monday)','16 November 2026','trade','ABC News')],
 [T('Fixed-asset investment','Spending on buildings, infrastructure and machinery.'),T('Stimulus','Expansionary fiscal or monetary policy used to lift aggregate demand.')],
 [['ABC News: ASX falls as miners drag, 16 Nov 2026',MK]],
 "Weak consumption and investment shift China's AD left, lowering output and slowing growth. China buys much of Australia's iron ore, coal and LNG, so weaker Chinese AD lowers Australian export prices, the terms of trade and national income; a lower AUD can partly cushion the effect.",
 [Q("Explain how a slowdown in China's economy could affect Australia's terms of trade and current account balance.",4)],
 "Related earlier cards: 25 October (China beats growth forecasts but property slump weighs on iron ore), 31 October (China factories) and 11 November (trade surplus above US$1 trillion). Pairs with the commodity prices card filed today.")

R('2026-11-13-ai-chips-arms-race-explainer','1','The chips powering the AI arms race: an HSC Economics explainer','2026-11-13','report',['Visual Capitalist'],
 "Follows the AI supply chain from minerals to chips, memory, profits, costs, models and adoption, with an evidence bank for all four topics.",
 "An eight-page explainer built on Visual Capitalist's 13 November 2026 'The Chips Powering the AI Arms Race' graphics. Nvidia shipped 2.96 million H100-equivalents in Q4 2025, far more than Google, AMD, Amazon and Huawei combined, and each stage of the chain shows its own concentration of power.",
 ['1A.5','1A.6','1D.7','3A.6'],['Y3a.4','Y3b.2','Y1a.10','Y2d.1'],['P2g.2','P2g.3','P2g.4','P3c.6'],
 ['2A.1','1D.4','3E.4','4E.1'],['Y3d.4','Y3d.5','Y3e.1','Y1d.1'],['P3c.4','P3c.5','P1b.2'],
 ['global','productivity','investment','trade'],['micro','trade'],['ds','adas','chart','compare'],
 [F('Nvidia shipments, Q4 2025 (H100-equivalents)','2.96 million (Google 976K; AMD 226K; Amazon 221K; Huawei 132K)','Q4 2025','global','Epoch AI, via Visual Capitalist'),
  F('Samsung, SK hynix and Micron share of listed memory market value','About 86% of US$2.18 trillion (calculated)','13 April 2026','global','CompaniesMarketCap, via Visual Capitalist'),
  F('China share of gallium; Australia share of rare earths','99% (refined, low-purity) ; 7% (mined)','2025 estimates','trade','USGS, World Bank WDR 2026'),
  F('Profit per $100 revenue','Nvidia $55.60; Microsoft $36.10; Alphabet $32.80; Amazon $10.80; Toyota $7.60','Fiscal years to 31 March 2026','investment','Fortune Global 500, via Visual Capitalist'),
  F('Share of AI models by country','US 50%; China 24%; UK 5.2%','May 2026','global','Epoch AI via World Bank WDR 2026'),
  F('Generative AI adoption, working-age population, Q1 2026','UAE 70%; Australia 40%; US 31% (21st); global 17.8%','Q1 2026','global','Microsoft AI Diffusion Report')],
 [T('Market power','The ability of a firm to influence price or output because it has few rivals.'),T('Economies of scale','Average cost per unit falls as output rises, because fixed costs are spread over more output.'),T('Supply shock','A sudden change in supply, such as an outage or export restriction, that moves the price.')],
 [['Visual Capitalist, VC+ Special Dispatch: The Chips Powering the AI Arms Race, 13 Nov 2026','https://www.visualcapitalist.com/']],
 "Use one data point per stage: gallium and rare earths (Topic 2, supply risk and terms of trade), Nvidia versus Google shipments (Topic 1, concentration), profit margins (Topic 3, distribution), compute costs falling from 172% to 57% of revenue (economies of scale) and the US and China building 74% of models (Topic 4, supply-side policy). Adoption is not productivity: test the link before claiming growth.",
 [Q("'Control of chips, memory and minerals gives some countries and firms an economic advantage in the global economy.' Discuss this statement with reference to the global economy and the Australian economy.",15)],
 "Eight-page booklet with a 15-mark practice question. Data are dated: shipments Q4 2025, market values 13 April 2026, adoption Q1 2026. Figures cover whole companies, not AI alone; compute-cost data mix periods and definitions. The booklet also reports that Nvidia CEO Jensen Huang has resigned and that an AI lab IPO filing was made on 10 November; these were taken as printed and not checked. The Visual Capitalist link is the site home page because the source gives no article URL.",pages=8,label='AI chips explainer (8 pages)')

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-12-aud-falls-strong-us-dollar'}
d=[x for x in d if x['id'] not in REMOVE]
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
