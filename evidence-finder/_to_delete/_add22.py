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
      angle=angle,questions=questions,note=note,added='2026-11-18'))


ABC='ABC News'
RBAM='https://www.rba.gov.au/monetary-policy/rba-board-minutes/2026/2026-11-03.html'

R('2026-11-17-ai-investment-boom-wobbles','1','Is the AI investment boom running out of steam?','2026-11-17','news',['ABC News (Ian Verrender, analysis)'],
 "Uses AI share valuations to show how asset-price bubbles and global financial flows can spread instability to Australia.",
 "ABC analyst Ian Verrender compares today's rush of money into AI with the 1840s railway mania, 1920s radio shares and the dotcom crash. He notes Anthropic's planned float now aims to raise US$90 billion at about US$1.5 trillion, down from about US$2 trillion expected weeks earlier, and that APRA will stress-test banks, super funds and insurers against AI scenarios.",
 ['1A.4','1A.8','1D.9'],['Y3b.3','Y3e.1','Y3e.3'],['P4b.1','P4b.2'],
 ['1A.5','4H.2','3A.7'],['Y1a.14','Y2c.8'],['P1e.7','P4a.3'],
 ['global','investment'],[],['compare'],
 [F('Anthropic planned float','Raise US$90 billion at about US$1.5 trillion (from about US$2 trillion expected weeks earlier)','17 November 2026','investment','ABC News'),
  F('Share of US market in the 10 companies most exposed to AI','About 40%','17 November 2026','investment','ABC News')],
 [T('Asset bubble','Asset prices rising well above what their future earnings justify.'),T('Financial contagion','Financial stress spreading from one market or country to others.')],
 [['ABC News: Wheels falling off AI investment boom, 17 Nov 2026','https://www.abc.net.au/news/2026-11-17/wheels-falling-off-ai-investment-boom-nvidia-anthropic/107392122']],
 "A correction on Wall Street can hit Australian super funds and investment through global financial flows, as the dotcom crash and the global financial crisis did. Balance: history does not always repeat, and AI investment is lifting productivity and spending, including Australian data centres. Cheaper Chinese AI models such as Moonshot's Kimi threaten the earnings forecasts behind valuations.",
 [Q("Explain how a sharp fall in global share markets could affect the Australian economy.",4)],
 "ANALYSIS / OPINION piece by one commentator, not a news report: the valuation and market-share figures are as reported and were not checked. The float is planned, not completed. Related: 9 November (AI shares and household wealth) and the 16 November AI chips explainer.")

R('2026-11-17-china-october-slowdown-reuters','1','China\'s economy loses momentum in October','2026-11-17','stats',['Reuters','JournalArta'],
 "Gives October Chinese activity data and shows how weaker Chinese demand reaches Australia's terms of trade and income.",
 "Factory output, retail sales and investment in China all grew more slowly than expected in October, a worrying start to the final quarter for Australia's largest trading partner. ING blamed weak consumer confidence and ANZ does not expect new stimulus before year's end, though officials say AI-linked exports will keep supporting growth.",
 ['1A.8','1E.1','2B.4'],['Y3e.3','Y1a.7','Y3a.15'],['P6a.2'],
 ['2A.1','3D.3','1D.9'],['Y3c.4','Y3e.1'],['P1e.6'],
 ['global','growth','trade'],[],['adas','flow'],
 [F('China industrial output, year to October','+4.8% (September 5.5%; forecast 5.3%)','November 2026','growth','Reuters via MarketScreener'),
  F('China retail sales, year to October','+0.4% (September 1.1%; forecast 0.8%)','November 2026','growth','Reuters via MarketScreener'),
  F('China fixed asset investment, January-October','-8.1% (to September: -7.2%)','November 2026','investment','Reuters via MarketScreener'),
  F('China GDP, September quarter','4.5% (year on year)','September quarter 2026','growth','Reuters via MarketScreener')],
 [T('Fixed asset investment','Spending on buildings, infrastructure and equipment.'),T('Export-led growth','Growth driven mainly by foreign demand rather than domestic spending.')],
 [['Reuters via MarketScreener: China factory output, retail sales growth slow in October','https://www.marketscreener.com/news/china-s-factory-output-retail-sales-growth-slow-in-october-ce785ededf81fe2c'],['JournalArta: China economy falters, factory output and retail sales, October','https://journalarta.com/en/2026/11/16/china-economy-falters-factory-output-retail-sales-october/']],
 "Falling investment and weak consumption shift China's AD left; strong exports only partly offset it. Link to Australia through lower demand for iron ore and other commodities, which lowers the terms of trade and export income.",
 [Q("Explain how slower economic growth in China could affect Australia's current account and exchange rate.",4)],
 "Replaces the 16 November ABC version of this story (same October data; it also noted iron ore US$90.95 a tonne on Friday, BHP shares -2.8% on Monday and ANZ economist Zhaopeng Xing expecting no new stimulus this year). Related: 25 October, 31 October and 11 November China cards.")

R('2026-11-17-trade-deals-realign-asean-apec','1','Trade deals realign around the Asian summits','2026-11-17','news',['CTV News','The Nation (Thailand)'],
 "Gives a current example of bilateral deals struck under US tariff pressure and what that means for the multilateral system.",
 "Around the ASEAN and APEC summits countries are signing bilateral trade deals partly to protect themselves from US tariffs. Canada and China extended arrangements and cut some tariffs, while Thailand and the US were due to sign a joint statement on progress towards an Agreement on Reciprocal Trade.",
 ['1B.4','1C.2','1B.2'],['Y3a.13','Y3a.14','Y3a.7'],[],
 ['1B.1','2D.2','2D.4'],['Y3a.8','Y3a.15','Y3a.16'],[],
 ['trade','global'],['trade'],['ds','compare'],
 [F('New bilateral moves this week','2 (Canada-China, Thailand-US)','17 November 2026','trade','CTV News; The Nation')],
 [T('Bilateral agreement','A trade deal between two countries.'),T('Most-favoured-nation (MFN)','The WTO rule that a country must offer all WTO members the same tariff treatment.')],
 [['CTV News: Are U really threatening to play China off the US, Trump trade adviser asks PM Carney','https://ctvnews.ca/world/trumps-tariffs/article/are-u-really-threatening-to-play-china-off-the-us-trump-trade-adviser-asks-pm-carney'],['The Nation (Thailand)','https://www.nationthailand.com/business/trade/40073549']],
 "Bilateral deals made under tariff pressure can divert trade rather than create it and weaken the WTO's MFN principle. Cutting a tariff reverses the effects on the tariff diagram: lower prices and more trade. Australia also negotiates bilateral deals under US tariff pressure and competes with Canada in Chinese markets.",
 [Q("Evaluate the impact of bilateral trade agreements on the multilateral trading system.",6)],
 "The Thai deal still needs Cabinet approval, parliamentary scrutiny and public consultation, so it is not final. A senior Trump trade adviser criticised Canada over possible car trade with China. Related: 9 November (US-China truce) and 14 November (APEC meeting).")

R('2026-11-17-us-retail-sales-slow-october','1','US shoppers slow down as high prices bite','2026-11-17','stats',['AP via MPR News'],
 "Shows nominal versus real spending in the world's largest economy and how an oil shock spreads inflation between economies.",
 "US retail sales grew only 0.2% in October, down from 0.8% in September, while consumer prices rose 0.4% in the month, so Americans bought less in real terms. Petrol is still almost 20% dearer than a year ago and AI chip demand is lifting electronics prices.",
 ['1A.8','3C.3','3A.1'],['Y1c.4','Y1a.6','Y3e.3'],['P1e.5','P1e.6'],
 ['1D.9','3C.1'],['Y1a.1','Y1c.7'],['P1e.7'],
 ['inflation','growth','global'],[],['compare','flow'],
 [F('US retail sales, October','+0.2% m/m (September +0.8%)','October 2026','growth','US Commerce Department via AP'),
  F('US consumer prices, October','+0.4% m/m (faster than expected)','October 2026','inflation','AP'),
  F('Car dealer / online retailer sales','-1.6% / +1.2%','October 2026','growth','AP'),
  F('US petrol price, year on year','Almost +20%','October 2026','inflation','AP')],
 [T('Nominal vs real','Nominal values are in current dollars; real values remove the effect of inflation.'),T('Cost-push inflation','Rising input costs, such as oil and chips, passed on as higher prices.')],
 [['AP via MPR News: Spending growth slowed at retail stores in October as high prices give shoppers pause, 17 Nov 2026','https://mprnews.org/story/2026/11/17/spending-growth-slowed-at-retail-stores-in-october-as-high-prices-give-shoppers-pause']],
 "When prices rise faster than spending, volumes fall, so a small nominal rise can mean shrinking real consumption. The US is the world's largest economy, so slower consumption lowers global demand, and risk-off markets can weigh on the AUD and Australian super funds.",
 [Q("Distinguish between nominal and real growth in retail sales, using the October US data.",3)],
 "Month-on-month first estimates. The 'real spending was negative' comment is Navy Federal economist Heather Long's reading, not an official series. Related: 12 November card on US inflation and a Fed hike.")

R('2026-11-17-san-francisco-declaration-ai-supply-chain','2','Australia signs US-led AI supply chain pact','2026-11-17','news',[ABC],
 "Shows how security-driven trade policy could change the composition and direction of Australia's trade.",
 "Australia is one of 10 countries that signed the 'San Francisco Declaration', part of the Trump administration's Pax Silica initiative which Australia joined in 2025. It aims to cut reliance on unreliable suppliers of the minerals, energy and technology AI depends on, and is not a tariff-cutting trade agreement.",
 ['2A.1','2D.4','1C.2'],['Y3a.4','Y3a.5','Y3e.1','Y3e.3'],['P6a.2'],
 ['2D.2','1A.3','2D.1'],['Y3a.16','Y3a.13','Y3a.7'],[],
 ['trade','global','investment'],['trade'],['compare','flow'],
 [F('Countries signing the declaration','10 (including Australia, Japan, India, UK)','17 November 2026','trade','ABC News'),
  F("China's share of refining for several critical minerals",'More than 90% (rare earths, graphite, gallium)','17 November 2026','trade','ABC News'),
  F('Year Australia joined Pax Silica','2025','17 November 2026','trade','ABC News')],
 [T('Critical minerals','Minerals essential to modern technology that carry supply risk, such as rare earths and lithium.'),T('Value-adding','Processing raw materials further before export.')],
 [['ABC News: Australia signs US-led AI supply chain agreement, 17 Nov 2026','https://www.abc.net.au/news/2026-11-17/australia-signs-us-led-ai-supply-chain-agreement/107392252']],
 "Opportunities: demand for Australian critical minerals and processing, better access to US AI technology and more diverse export markets. Risks: China, the largest trading partner, may retaliate or restrict rare earth processing, and rebuilding supply chains outside China costs more. Balances the largest export market against security ties with the US.",
 [Q("Assess the economic risks and benefits for Australia of aligning its trade policy more closely with the United States.",6)],
 "Indonesia, Malaysia, Vietnam and Cambodia backed a rival China-led AI body. Pairs with the 13 November AI chips explainer (minerals page: Australia 7% of rare earths).")

R('2026-11-17-aud-iron-ore-oil-fall-wall-st-selloff','2','Dollar and commodity prices fall after a Wall Street sell-off','2026-11-17','news',['ABC News markets live blog'],
 "Shows how risk-off markets and weaker iron ore lower the AUD and the terms of trade.",
 "A sell-off in US technology shares on Monday spread to commodity and currency markets on Tuesday 17 November. The AUD fell 0.5% to US67.40c, iron ore fell 2.5% to US$88.15 a tonne and Brent crude fell 3.7% to US$92.32 a barrel; weak Chinese October data added to the pressure on iron ore.",
 ['2C.2','2C.3','2B.4','3D.1'],['Y3c.2','Y3c.4','Y1a.7'],['P6c.1','P6a.2'],
 ['2C.6','2A.1'],['Y3c.5','Y3e.3'],['P2d.1'],
 ['fx','trade','global'],[],['fx','flow'],
 [F('AUD / USD','US67.40c (-0.5%)','Tuesday 17 November 2026','fx','ABC News'),
  F('Iron ore','US$88.15 a tonne (-2.5%)','17 November 2026','trade','ABC News'),
  F('Brent crude / gold','US$92.32 a barrel (-3.7%) / US$3,865 an ounce (-0.4%)','17 November 2026','trade','ABC News'),
  F('Wall Street: Nasdaq / S&P 500','-2.5% / -2.0%','Monday 16 November 2026','global','ABC News')],
 [T('Commodity currency','A currency, like the AUD, that tends to move with commodity prices.'),T('Terms of trade','Index of export prices divided by index of import prices.')],
 [['ABC News live blog, Tuesday 17 November 2026','https://www.abc.net.au/news/2026-11-17/asx-markets-business-news-live-updates-tuesday-17-november/107393100']],
 "Lower iron ore prices mean foreign buyers need fewer Australian dollars, and risk-off investors leave the AUD, so demand shifts left and the AUD depreciates. Cheaper oil helps the import bill but cheaper iron ore hurts more, so the net terms of trade effect depends on which price falls further.",
 [Q("Explain how a fall in iron ore prices could affect Australia's exchange rate and current account.",4)],
 "Single-day market prices that move daily. Kept alongside (not replacing) the 16 November AUD card, which explains the interest-rate-gap driver, and the 16 November commodity card.")

R('2026-11-17-data-centres-inflation-local-disputes','3','Data centre boom adds to inflation and sparks local disputes','2026-11-17','news',[ABC],
 "Uses the data centre boom to distinguish demand-pull from cost-push inflation and to raise the environmental externalities.",
 "Record spending on data centres to power AI is pressuring building materials, skilled trades, electricity and water, and driving local opposition. RBA Governor Michele Bullock says construction is straining scarce materials and electricians, and about 70% of data centre technology is imported, so much of the spending leaks out of the economy.",
 ['3C.3','3A.1','3F.2','3F.4'],['Y1c.4','Y1c.5','Y1a.6','Y1e.5'],['P1e.6','P2h.3'],
 ['3A.7','4D.3','2B.4'],['Y1a.10','Y2c.4'],['P3c.4','P3c.5'],
 ['inflation','investment','environment','growth'],[],['adas'],
 [F('Capital raised by local data centre operators, 2026','At least $35 billion (+46% on 2025)','2026','investment','Internal RBA note, via ABC News'),
  F('Data centre capacity','About 2.3 GW across 79 sites; planned 23-67 GW','November 2026','investment','AEMO, via ABC News'),
  F('Data centre technology imported','About 70%','November 2026','trade','RBA Governor Bullock, via ABC News'),
  F('NEXTDC market value lost in one day (local dispute)','About $3 billion','November 2026','investment','ABC News')],
 [T('Demand-pull inflation','Prices rise because spending grows faster than the economy can supply.'),T('Cost-push inflation','Prices rise because input costs such as labour, materials and energy rise.')],
 [['ABC News: When community concerns collide in the fight over data centres, 16 Nov 2026','https://www.abc.net.au/news/2026-11-16/when-community-concerns-collide-in-data-centre-fight/107344810']],
 "Data centre construction lifts investment and shifts AD right; near capacity, much of the rise shows up as a higher price level (demand-pull). Competition for electricians and materials adds cost-push pressure. Mention energy and water use as a sustainability cost.",
 [Q("Is data centre investment mainly a demand-pull or a cost-push source of inflation? Justify your answer.",4)],
 "Replaces the 16 November card 'Data centre boom: billions in investment, rising community pushback' (same ABC article; it also gave 4.3% annual inflation, capacity enough for about 1.5 million homes per IBISWorld, Victoria making no decision on nine fast-tracked proposals before the caretaker period and two large NSW proposals stopped, plus a costs and benefits comparison).")

R('2026-11-17-rba-minutes-board-split-6-3','4','RBA board split 6-3 over the hike to 4.85%','2026-11-17','report',['Reserve Bank of Australia'],
 "Shows the inflation versus unemployment trade-off inside the RBA board, with policy lags and the limits of monetary policy.",
 "Minutes of the RBA's 2-3 November meeting, released on 17 November, show six members voted to raise the cash rate 25 basis points to 4.85% and three wanted to hold at 4.60%. The majority pointed to stronger September-quarter inflation, rising services inflation, higher oil prices and the risk that policy is not restrictive enough.",
 ['4D.1','4D.2','4D.3','4H.1'],['Y2c.4','Y2c.7','Y2c.8'],['P4c.3'],
 ['3C.3','3B.2','4A.7'],['Y1c.4','Y2a.2'],['P4c.7'],
 ['rates','inflation','employment'],['monetary'],['flow'],
 [F('RBA cash rate','4.85% (+25 basis points); board vote 6-3 (minority wanted to hold at 4.60%)','2-3 November 2026','rates','RBA minutes'),
  F('RBA inflation forecast','Above 3% until late 2027; back at the 2.5% midpoint by mid-2028','November 2026','inflation','RBA minutes'),
  F('Unemployment forecast, end-2028','5.1%','November 2026','employment','RBA minutes'),
  F('Rise in unemployment over six months (minority view)','0.5 percentage points','November 2026','employment','RBA minutes')],
 [T('Neutral rate','The cash rate that neither speeds up nor slows down the economy.'),T('Policy lag','The time before a rate change fully affects the economy.')],
 [['RBA: Minutes of the Monetary Policy Board meeting, 2-3 November 2026',RBAM]],
 "The disagreement is about timing and lags: the majority judged the risk of policy too loose greater than too tight, while the minority argued 100 basis points of earlier tightening is still working through. Use it for the inflation-unemployment trade-off and the limits of monetary policy (lags, neutral rate uncertainty, oil supply shocks).",
 [Q("Using the November RBA minutes, explain the trade-off the board faced between reducing inflation and supporting employment.",5)],
 "Replaces the 17 November preview 'A big week for the RBA: minutes, wages and jobs'. UPDATE DUE for what that preview still covered: Wage Price Index (Wed 18 Nov; CBA expected +0.9% for the quarter and 3.3% for the year, up from 3.2%), Labour Force (Thu 19 Nov; about +30,000 jobs and 4.7% unemployment expected after a fall of almost 40,000 in September), October CPI (24 Nov) and Q3 GDP (2 Dec). The RBA also expects October headline inflation to jump as household subsidies drop out of the annual figure.")

R('2026-11-17-cba-expects-rba-december-hold','4','CommBank expects the RBA to hold rates in December','2026-11-17','news',['CommBank Newsroom'],
 "Shows housing lending falling as evidence of the transmission mechanism and why a central bank may pause above target.",
 "Commonwealth Bank economists expect the RBA to keep the cash rate at 4.85% at its 7-8 December meeting. CBA's Belinda Allen says the meeting is unlikely to be 'live' and that February is the next meeting where a rise could be seriously considered if inflation surprises up.",
 ['4D.2','4D.3','4H.1'],['Y2c.4','Y2c.5','Y2c.8'],['P4c.7','P4c.3'],
 ['3C.3','4D.1'],['Y2a.2','Y1c.4'],['P4c.4'],
 ['rates','housing','inflation'],['monetary'],['chart','flow'],
 [F('New housing lending, September quarter','-15.5%','September quarter 2026','housing','CommBank Newsroom'),
  F('Investor housing lending, September quarter','-32.3%','September quarter 2026','housing','CommBank Newsroom'),
  F('CBA forecast','Hold at 4.85% in December; cuts in August and November 2027','17 November 2026','rates','CommBank Newsroom')],
 [T('Forward guidance','Signals about the likely future path of interest rates.'),T('Data-dependent','Policy decisions that respond to new economic data as it is released.')],
 [['CommBank Newsroom: RBA rate pause, split vote, December 2026','https://www.commbank.com.au/articles/newsroom/2026/11/rba-rate-pause-split-vote-december-2026.html']],
 "A sharp fall in housing lending shows the credit and asset-price channels working, so earlier rises are already slowing demand. Pausing while inflation is above target shows the RBA balancing price stability against rising unemployment; the 6-3 minutes show the uncertainty inside the board.",
 [Q("Explain why the RBA might keep the cash rate on hold even while inflation is above its target band.",4)],
 "FORECAST by one bank, filed as published: UPDATE DUE after the 7-8 December decision. Key data before then: October CPI (24 Nov) and September-quarter GDP (2 Dec). Related: 11 November card on whether the RBA has peaked.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-16-china-economy-loses-momentum-october','2026-11-16-data-centre-boom-investment-pushback','2026-11-17-rba-minutes-wages-jobs-week'}
d=[x for x in d if x['id'] not in REMOVE]
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
