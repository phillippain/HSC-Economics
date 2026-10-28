import json
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-10-28-cpi-day-banks-expect-above-rba','2026-10-25-september-quarter-cpi-preview','2026-10-27-rba-melbourne-cup-live-hike','2026-10-27-aud-interest-rate-differential'}
before=len(d)
d=[x for x in d if x['id'] not in REMOVE]; removed=before-len(d); have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
def fl(i,pages=1,label='One-page digest'): return {'path':f'files/2026-10/{i}.pdf','label':label,'pages':pages}
recs=[]
def add(**k): recs.append(k)
CPI_U='https://theconversation.com/inflation-jumps-to-4-3-adding-to-pressure-for-rba-rate-rise-next-week-295162'
ABCM='https://www.abc.net.au/news/2026-10-28/asx-markets-business-live-news/107316614'
AAP='https://www.juneesoutherncross.com.au/story/9381176/november-rate-hike-a-lock-after-ugly-inflation-result/'
ALL='https://alloranews.com/economia/rba-sees-no-near-term-recession-as-michele-bullock-warns-inflation-is-far-too-high/'
ABSR='https://www.abs.gov.au/media-centre/media-releases/cpi-rose-43-year-september-2026'
ABSL='https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/consumer-price-index-australia/latest-release'
L_CPI=['Isaac Gross, Inflation jumps to 4.3%, adding to pressure for RBA rate rise next week, The Conversation, 28 Oct 2026',CPI_U]
L_ABC=['ABC News, ASX surrenders big gains as market puts chance of November hike near 90pc, 28 Oct 2026',ABCM]
L_AAP=['AAP via Junee Southern Cross, November rate hike a lock after ugly inflation result, 28 Oct 2026',AAP]
L_ALL=['Allora! News, RBA sees no near-term recession as Michele Bullock warns inflation is far too high, 28 Oct 2026',ALL]
GEN='Digest paraphrases its listed sources.'

i='2026-10-16-coal-mine-methane-safeguard-mechanism'
add(id=i,title='Coal mine methane: the emissions at home we are undercounting',date='2026-10-16',type='news',outlets=['The Conversation','Grattan Institute'],
 summary='A case study of the limits of a market-based environmental policy when emissions are poorly measured and baselines are set loosely.',
 lede='A Grattan Institute analyst argues methane from Australian coal mines, about 5% of national emissions, is badly measured: aircraft found open-cut mines released about 3.6 times what they reported. Because every mine moves to the same Safeguard target, low-reporting open-cut mines earned about 700,000 credits (around $26 million) in 2024-25.',
 about={'h09':['4G.2','4G.1'],'y12':['Y2f.3','Y2f.5','Y2f.8'],'y11':[]},also={'h09':['3F.2','3F.4','4G.3'],'y12':['Y1e.3','Y1e.5','Y2f.7'],'y11':['P5a.5']},
 issues=['environment'],levers=['environmental'],diagrams=['chart'],
 figures=[F('Share of Australia\'s emissions from coal-mine methane','about 5%','2026','environment','Pring, The Conversation'),F('Methane measured by aircraft vs reported (open-cut mines)','about 3.6 times','2026','environment','Pring, The Conversation'),F('Credits earned by low-reporting open-cut mines','about 700,000 (around $26m)','2024-25','environment','Pring, The Conversation'),F('Reported emissions per tonne of coal: open-cut Qld / shared target / underground','47 kg / 65 kg / 267 kg CO2-e','2026','environment','Pring, The Conversation'),F('Proposed cut to open-cut limits from separate limits','about 1.3 Mt a year','2026','environment','Pring, The Conversation')],
 terms=[T('Safeguard Mechanism','A federal baseline-and-credit scheme that sets a falling yearly emissions limit for big emitters; those that beat it earn credits and those that exceed it must buy them.'),T('Negative externality','A cost imposed on third parties that the producer does not pay.'),T('Scope 3 emissions','Emissions released when a product, such as exported coal, is burned elsewhere.')],
 links=[['Hayley Pring (Grattan Institute), The High Court looked at coal climate emissions overseas. But what about emissions at home?, The Conversation, 16 Oct 2026','https://theconversation.com/the-high-court-looked-at-coal-climate-emissions-overseas-but-what-about-emissions-at-home-294235']],
 file=fl(i),angle='Market-based environmental policy only works if emissions are measured accurately and baselines are set sensibly. If methane is undercounted, polluters also avoid paying the full external cost.',
 questions=[Q('Evaluate the effectiveness of the Safeguard Mechanism as a policy to reduce Australia\'s greenhouse gas emissions.',5)],
 note='An analyst\'s argument published by The Conversation, so the policy proposals are one view. The High Court ruling on Mount Pleasant is reported second-hand. Complements the 14 September climate targets article.')

i='2026-10-29-private-health-rebate-age-versus-need'
add(id=i,title='Who should get extra help with health insurance? Age versus need',date='2026-10-29',type='news',outlets=['The Conversation'],
 summary='Shows why income alone can mislead as a measure of wellbeing, using the rebate for over-65s and HILDA data on wealth and hardship by age.',
 lede='The government has reintroduced a bill to scrap the extra private health insurance rebate for over-65s. New analysis of HILDA 2022 data (not yet peer reviewed) argues a pensioner exemption would mostly protect comfortable part-pensioners and miss struggling younger families.',
 about={'h09':['3E.3','3E.5'],'y12':['Y1d.1','Y1d.2','Y2b.10'],'y11':[]},also={'h09':['3E.1','4C.2'],'y12':['Y1d.6','Y1d.9'],'y11':['P2h.8']},
 issues=['inequality','budget'],levers=['fiscal'],diagrams=['compare'],
 figures=[F('Private health rebate: lowest income tier under 65 / aged 65-69 / aged 70+','about 24% / 28% / 32%','2026','inequality','The Conversation'),F('Pensioners with cover: help from an exemption','about 560,000 full-rate and 540,000 part-rate','HILDA 2022 data','inequality','The Conversation'),F('Part-pensioners with more than $2 million in wealth (including home)','one in seven','HILDA 2022 data','inequality','The Conversation'),F('Share of disposable income full-rate pensioners spend on premiums','6.3%','HILDA 2022 data','inequality','The Conversation'),F('Median wealth of insured over-65s earning under $37,000','$1.18 million','HILDA 2022 data','inequality','The Conversation')],
 terms=[T('Vertical equity','Treating people with different abilities to pay differently.'),T('Intergenerational equity','Fairness between age groups.'),T('Means testing','Targeting a payment by income or assets.'),T('Community rating','Charging everyone the same premium regardless of age or health.')],
 links=[['The Conversation, Exempting pensioners from private health rebate changes won\'t make it fairer. Here\'s what would, 29 Oct 2026','https://theconversation.com/exempting-pensioners-from-private-health-rebate-changes-wont-make-it-fairerheres-what-would-294945']],
 file=fl(i),angle='Use this to show the difference between income and wealth inequality, and between targeting help by age and by need. The authors favour concessions for low-income people of any age.',
 questions=[Q('Explain why income alone may be a misleading measure of economic wellbeing, using evidence about older and younger Australians.',4)],
 note='The HILDA analysis is not yet peer reviewed and uses 2022 data. The authors argue for one position in a live policy debate.')

i='2026-10-28-eu-trade-deal-ratification'
add(id=i,title='Why the EU trade deal is about far more than beef',date='2026-10-28',type='news',outlets=['The Conversation'],
 summary='A current free trade agreement awaiting a divided Senate, with the tariff diagram and the case for diversifying trade partners.',
 lede='Australia and the EU agreed a free trade agreement in March after nearly eight years of talks, but the laws to bring it into force must still pass a divided Senate. Two trade economists argue rejecting it would cost far more than the beef access farmers say is too small.',
 about={'h09':['2D.2','2D.1'],'y12':['Y3a.13','Y3a.3'],'y11':[]},also={'h09':['1B.4','2D.3','1C.2'],'y12':['Y3a.16','Y3a.7'],'y11':[]},
 issues=['trade','global'],levers=['trade'],diagrams=['ds'],
 figures=[F('Australian goods exports covered by tariff cuts','98%','2026','trade','Gray and Draper, The Conversation'),F('EU beef quota for Australia','4,400 t rising to 35,000 t; 20% tariff removed from day one','2026','trade','Gray and Draper, The Conversation'),F('Value of new trade: industry wanted / deal delivers','A$3 billion / A$2 billion (Farrell)','2026','trade','Gray and Draper, The Conversation'),F('Labor Senate seats','30 of 76 (needs 9 more)','2026','trade','Gray and Draper, The Conversation')],
 terms=[T('Free trade agreement','An agreement removing tariffs and other barriers between member countries.'),T('Tariff-rate quota','A limit on the volume of imports that receive a lower tariff.'),T('Ratification','Formal approval by a country\'s legislature so an agreement takes effect.')],
 links=[['Gray and Draper, Failure to ratify the EU trade deal would cost Australia far more than beef, The Conversation, 28 Oct 2026','https://theconversation.com/failure-to-ratify-the-eu-trade-deal-would-cost-australia-far-more-than-beef-294855']],
 file=fl(i),angle='The authors\' wider argument is diversification: Australia is wedged between a protectionist ally (the US) and a coercive customer (China), and the EU deal adds options in trade, investment and critical minerals.',
 questions=[Q('Evaluate the potential impacts of the Australia-EU free trade agreement on the Australian economy.',5)],
 note='Argues for ratification, and the digest reports the authors\' case. The Senate vote is still to come, and EU ratification needs 15 of 27 states representing 65% of the population. UPDATE DUE: Senate decision.')

i='2026-10-29-inflation-4-3-perspectives-special'
add(id=i,title='Inflation at 4.3%: what is driving it, who says what, and what policy can do (six-page special)',date='2026-10-29',type='report',outlets=['ABS','ABC News','The Conversation','AAP'],
 summary='Sets the supply-shock, demand and wait-and-see views of inflation side by side with the AD/AS, transmission, Phillips curve and LRAS diagrams, plus a 20-mark extended response plan.',
 lede='September\'s CPI of 4.3% puts the RBA on track for a fifth rate rise on 3 November. The special compares what the Treasurer, RBA officials, the Opposition and commentators say about the causes of inflation, the cost of fighting it, and the roles of monetary policy, fiscal policy and productivity.',
 about={'h09':['3C.3','4D.3','3B.4','4B.1'],'y12':['Y1c.4','Y1c.6','Y2c.5','Y2c.8'],'y11':[]},also={'h09':['3C.1','4C.2','4E.1','4D.2','2C.6'],'y12':['Y1c.5','Y2b.14','Y2d.1','Y3c.5'],'y11':[]},
 issues=['inflation','rates','employment','productivity'],levers=['monetary','fiscal','micro'],diagrams=['adas','phillips','fx','flow','compare'],
 figures=[F('Annual CPI','4.3% (August 4.0%)','September 2026','inflation','ABS'),F('Trimmed mean','1.0% in the quarter (RBA forecast 0.8%); 3.6% annual (3.7% quarterly measure)','September quarter 2026','inflation','ABS'),F('Unemployment rate','4.7% (4.1% in January)','September 2026','employment','ABS'),F('Cash rate / expected after 3 November','4.60% / 4.85%; market odds about 80-90%','28 October 2026','rates','ABC News'),F('Automotive fuel / electricity, annual','+23.6% / +12.8%','September 2026','inflation','ABS')],
 terms=[T('Cost-push inflation','Inflation caused by rising production costs, such as oil.'),T('Demand-pull inflation','Inflation caused by spending outrunning the economy\'s capacity.'),T('NAIRU','The rate of unemployment below which inflation tends to accelerate.'),T('Policy mix','The combination of monetary, fiscal and microeconomic policy in use.')],
 links=[['ABS, CPI rose 4.3% in the year to September 2026',ABSR],['ABS, Consumer Price Index, Australia, September 2026',ABSL],L_CPI,['ABC News, Inflation rate rises to 4.3 per cent in September, raising rate hike expectations, 28 Oct 2026','https://abc.net.au/news/2026-10-28/inflation-september-cpi-ahead-of-november-interest-rate-call/107317382'],L_ABC,['ABC News, Jim Chalmers resists blame for another high inflation result, 28 Oct 2026','https://www.abc.net.au/news/2026-10-28/chalmers-downplays-further-fuel-discounts-amid-high-inflation/107319372'],['Tom Crowley, Bad inflation result lays bare the ugly truth: there is no easy way out, ABC News, 29 Oct 2026','https://www.abc.net.au/news/2026-10-29/bad-inflation-result-political-pressure/107318484'],L_AAP,L_ALL,['Trading Economics via TradingView, RBNZ holds cash rate at 2.75% in split decision, 28 Oct 2026','https://www.tradingview.com/news/te_news:595574:0-rbnz-holds-cash-rate-at-2-75-in-split-decision/'],['Fox Business, Federal Reserve holds rates steady, 28 Oct 2026','https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-october-28-2026']],
 file=fl(i,6,'Six-page special'),angle='Do not pick one cause. The strongest answers identify both cost-push and demand-pull pressures, use the trimmed mean to separate them, then explain why the mix matters for choosing a policy. Includes a 20-mark plan: evaluate the effectiveness of Australia\'s economic policies in managing inflation in 2026.',
 questions=[Q('Distinguish between headline and underlying inflation, using September 2026 data.',4),Q('Using an AD/AS diagram, explain how a rise in world oil prices affects inflation and economic growth in Australia.',4),Q('Using a Phillips curve, explain why rising inflation expectations make it harder to reduce inflation.',4)],
 extended='Evaluate the effectiveness of Australia\'s economic policies in managing inflation in 2026. (20 marks)',
 note='UPDATE DUE: RBA decision on 3 November with new forecasts. Includes positions of political figures, reported as the parties put them. Some sources are smaller outlets (AAP via a regional paper, Allora! News); the key figures are from the ABS.')

i='2026-10-28-aud-rises-on-rate-hike-bets'
add(id=i,title='Australian dollar climbs as markets bet on an RBA rate rise, reaching a 13-year high against the NZ dollar',date='2026-10-28',type='stats',outlets=['ABC News','Trading Economics'],
 summary='Shows how a widening interest rate differential lifts the AUD, using the AUD/NZD move after the RBNZ held and the CPI came in hot. Replaces the 27 October edition.',
 lede='After the CPI release the Australian dollar rose about 0.3% to around US70.45c, closing near US70.32c, and jumped about 2% to NZ$1.26, its highest since early 2013, after the RBNZ unexpectedly held rates. Australia\'s 10-year yield of 5.22% is above the US 5.02%.',
 about={'h09':['2C.4','2C.5'],'y12':['Y3c.1','Y3c.2'],'y11':['P6c.1']},also={'h09':['2C.3','4D.3','2C.6'],'y12':['Y3c.5'],'y11':[]},
 issues=['fx','rates'],levers=['monetary'],diagrams=['fx'],
 figures=[F('Australian dollar','about US70.45c after the CPI; closed near US70.32c','28 October 2026','fx','ABC News'),F('AUD against the NZ dollar','NZ$1.26 (about +2%; highest since early 2013)','28 October 2026','fx','Trading Economics via TradingView'),F('Australian / US 10-year bond yield','5.22% / 5.02%','28 October 2026','rates','ABC News'),F('Market odds of an RBA hike on 3 November','about 60% before the CPI, about 90% after','28 October 2026','rates','ABC News'),F('RBNZ official cash rate','held at 2.75% in a 4-3 vote (hike expected)','28 October 2026','rates','Trading Economics via TradingView')],
 terms=[T('Interest rate differential','The gap between Australian and overseas interest rates.'),T('Appreciation','A rise in the value of the AUD against another currency.'),T('Floating exchange rate','A rate set by the supply and demand for the currency in the market.')],
 links=[L_ABC,['Trading Economics via TradingView, RBNZ holds cash rate at 2.75% in split decision, 28 Oct 2026','https://www.tradingview.com/news/te_news:595574:0-rbnz-holds-cash-rate-at-2-75-in-split-decision/']],
 file=fl(i),angle='Appreciation is part of the RBA\'s exchange rate channel: it makes imports cheaper, which helps lower inflation, but reduces the competitiveness of exporters such as tourism, education and agriculture.',
 questions=[Q('Explain how a widening interest rate differential between Australia and New Zealand affects the value of the Australian dollar and Australia\'s external sector.',4)],
 note='Single-day figures, so update before quoting. UPDATE DUE: RBA decision on 3 November. Replaces the 27 October edition.')

i='2026-10-28-inflation-jumps-to-4-3-per-cent'
add(id=i,title='Inflation jumps to 4.3% as fuel and travel push prices higher',date='2026-10-28',type='stats',outlets=['ABS','The Conversation'],
 summary='The September 2026 CPI result: headline 4.3%, trimmed mean 1.0% for the quarter, with fuel and electricity the fastest rising. Replaces the earlier CPI previews.',
 lede='Annual CPI inflation rose to 4.3% in September from 4.0% in August. The trimmed mean rose 1.0% in the September quarter, in line with economists\' forecasts but above the RBA\'s August forecast of 0.8%, which strengthens the case for a fifth rate rise on 3 November.',
 about={'h09':['3C.1','3C.3','3C.2'],'y12':['Y1c.3','Y1c.4','Y1c.8'],'y11':[]},also={'h09':['3C.4','4D.2'],'y12':['Y1c.9','Y2c.4'],'y11':[]},
 issues=['inflation','rates'],levers=['monetary'],diagrams=['adas','chart'],
 figures=[F('Annual CPI','4.3% (August 4.0%)','September 2026','inflation','ABS'),F('Trimmed mean','1.0% in the quarter (RBA forecast 0.8%); 3.6% annual on the monthly measure, 3.7% on the quarterly','September quarter 2026','inflation','ABS via The Conversation'),F('Automotive fuel','+9.4% in the month; +23.6% over the year','September 2026','inflation','ABS'),F('Electricity','+12.8% over the year (federal energy rebates expired)','September 2026','inflation','ABS'),F('Transport group / housing group, annual','+8.7% / +5.2% (housing 5.7% in August)','September 2026','inflation','ABS')],
 terms=[T('Trimmed mean','The RBA\'s preferred underlying measure, which removes the largest price rises and falls each period.'),T('Cost-push inflation','Inflation caused by rising production costs such as fuel.'),T('Seasonal adjustment','Removing regular seasonal swings so data can be compared across periods.')],
 links=[L_CPI,['ABS, CPI rose 4.3% in the year to September 2026',ABSR],['ABS, Consumer Price Index, Australia, September 2026',ABSL]],
 file=fl(i),angle='As Gross puts it, a rate rise cannot produce more oil, but it can slow spending and make it harder for firms to pass higher costs on. The trimmed mean at 3.6% is still above the 2-3% target, which shows inflation is broad-based.',
 questions=[Q('Distinguish between headline and underlying inflation, using data from the September 2026 CPI release.',4)],
 note='The digest reports prices up 0.8% in September (0.6% seasonally adjusted, the figure The Conversation reports); check the ABS release before quoting the monthly figure. Card surcharges were banned from 1 October and the RBA estimates a one-off 0.1% lift to the price level. Replaces the 28 October CPI preview and the 25 October preview.')

i='2026-10-28-no-recession-but-unemployment-rising'
add(id=i,title='No recession in sight, but the jobless rate is heading up',date='2026-10-28',type='news',outlets=['Allora! News','AAP','The Conversation'],
 summary='The RBA\'s Senate estimates evidence on why unemployment must rise to bring down inflation, linking the NAIRU and the Phillips curve trade-off.',
 lede='At Senate estimates RBA officials said none of their indicators point to a recession, but they still expect unemployment, already 4.7%, to keep rising as higher interest rates slow the economy. NAB suggested unemployment may need to reach 5.5%, not 5%, to return inflation to target.',
 about={'h09':['3B.4','3B.2'],'y12':['Y1c.6','Y1b.11'],'y11':[]},also={'h09':['3B.6','4D.3','3C.3'],'y12':['Y1b.6','Y2c.8'],'y11':['P1e.5']},
 issues=['employment','inflation','rates'],levers=['monetary'],diagrams=['phillips','flow'],
 figures=[F('Unemployment rate','4.7% (4.1% at the start of 2026)','September 2026','employment','ABS via digest'),F('Change in employment','-39,300 in the month','September 2026','employment','ABS via digest'),F('Jobless rate NAB says may be needed','5.5% (not 5%)','28 October 2026','employment','NAB (Sally Auld) via digest')],
 terms=[T('NAIRU','The rate of unemployment below which inflation tends to accelerate.'),T('Spare capacity','Unused labour and other resources in the economy.')],
 links=[L_ALL,L_AAP,L_CPI],
 file=fl(i),angle='If the labour market is tighter than thought, the NAIRU is higher than estimated, so unemployment must rise further to bring inflation down. The cost of disinflation falls on workers who lose jobs or hours.',
 questions=[Q('Explain why the RBA may need unemployment to rise in order to reduce inflation.',4)],
 note='Relies partly on a smaller outlet (Allora! News) and AAP via a regional paper for the Senate estimates evidence. The unemployment figures should be checked against the ABS release.')

i='2026-10-28-melbourne-cup-rate-hike-expected'
add(id=i,title='Markets all but certain of a Melbourne Cup Day rate rise, with all four major banks tipping 4.85%',date='2026-10-28',type='news',outlets=['ABC News','AAP','The Conversation'],
 summary='After the hot CPI, markets price up to a 90% chance of a fifth rise on 3 November, with the case for hiking and for waiting. Replaces the 27 October edition.',
 lede='Market pricing for a 25 basis point rise on 3 November rose from about 60% before the CPI to up to 90% after it, and NAB and CBA have switched from expecting a hold to a hike, joining Westpac and ANZ. A rise would be the fifth of 2026 and take the cash rate to its highest level in 18 years.',
 about={'h09':['4D.2','4D.3'],'y12':['Y2c.4','Y2c.5','Y2c.8'],'y11':[]},also={'h09':['3C.3'],'y12':['Y2c.7'],'y11':[]},
 issues=['rates','inflation'],levers=['monetary'],diagrams=['flow','adas'],
 figures=[F('Cash rate / expected after 3 November','4.60% / 4.85% (18-year high)','28 October 2026','rates','ABC News'),F('Market odds of a hike','about 60% before the CPI, about 79% straight after, near 90% later','28 October 2026','rates','ABC News'),F('Rises so far in 2026','four, totalling 100 basis points (latest in September)','28 October 2026','rates','ABC News'),F('RBA decision','2:30pm AEDT, Tuesday 3 November, with new forecasts','3 November 2026','rates','ABC News')],
 terms=[T('Cash rate','The interest rate on overnight loans between banks, which the RBA targets.'),T('Transmission mechanism','The channels through which a change in the cash rate affects spending and inflation.'),T('Time lag','The delay between a policy change and its full effect.')],
 links=[L_ABC,L_AAP,L_CPI,L_ALL],
 file=fl(i),angle='Monetary policy works with time lags of up to 18 months, so part of earlier rises has not yet fed through: that is the main argument for a hold, while persistent underlying inflation is the main argument for a hike.',
 questions=[Q('Explain how an increase in the cash rate is transmitted through the economy to reduce inflation.',5)],
 note='Market odds change daily. UPDATE DUE: RBA decision on 3 November 2026. Replaces the 27 October edition.')

i='2026-10-28-bullock-supply-shocks-and-inflation'
add(id=i,title='Bullock: supply shocks make taming inflation harder',date='2026-10-28',type='news',outlets=['ABC News','Allora! News'],
 summary='The RBA Governor on why repeated negative supply shocks worsen the trade-off between inflation and jobs and risk lifting expectations.',
 lede='RBA Governor Michele Bullock told Senate estimates inflation is far too high and that repeated negative supply shocks worsen the trade-off the bank faces between bringing inflation down and protecting jobs. She said Australia\'s inflation problem began before the latest energy shock.',
 about={'h09':['3C.3','4D.2'],'y12':['Y1c.4','Y1c.6','Y2c.8'],'y11':[]},also={'h09':['3B.4','4B.1'],'y12':['Y2c.7'],'y11':[]},
 issues=['inflation','rates'],levers=['monetary'],diagrams=['adas'],
 figures=[F('Annual CPI','4.3%','September 2026','inflation','ABS via digest'),F('Cash rate','4.60% after four rises in 2026','28 October 2026','rates','ABC News'),F('House prices relative to early 2020','about 50% higher, although recently falling in most capitals','2026','housing','Bullock, Senate estimates')],
 terms=[T('Supply shock','A sudden change in production costs or capacity, such as an oil price rise.'),T('Stagflation','Rising inflation combined with weak growth.'),T('Inflation expectations','What households and firms expect inflation to be, which affects wage and price setting.')],
 links=[L_ABC,L_ALL],
 file=fl(i),angle='Monetary policy acts on demand, not supply, so it cannot fix the source of a supply shock: a key limitation to discuss in Topic 4 answers.',
 questions=[Q('Using an AD/AS diagram, explain why a negative supply shock creates a policy dilemma for the Reserve Bank.',5)],
 note='The Bullock and Hauser quotes come from a smaller outlet (Allora! News) and ABC live coverage rather than the Senate transcript.')

i='2026-10-28-chalmers-fiscal-response-to-inflation'
add(id=i,title='Chalmers rules out fuel relief as inflation bites',date='2026-10-28',type='news',outlets=['ABC News','AAP'],
 summary='The Treasurer\'s and the Opposition\'s competing views on whether fiscal policy is fuelling inflation, for answers on the policy mix.',
 lede='Treasurer Jim Chalmers called the 4.3% result too high but argued the budget is not the main cause of inflation, ruled out returning the fuel excise discount and flagged more savings in the December MYEFO. Shadow Treasurer Tim Wilson said the government is driving up underlying inflation and called for a fuel discount paid for by spending cuts.',
 about={'h09':['4C.2','4B.1'],'y12':['Y2b.3','Y2b.13','Y2b.14'],'y11':[]},also={'h09':['4C.1','4D.1'],'y12':['Y2b.9'],'y11':[]},
 issues=['budget','inflation'],levers=['fiscal'],diagrams=['compare'],
 figures=[F('Annual CPI','4.3%','September 2026','inflation','ABS via digest'),F('Cash rate','4.60%, with a rise to 4.85% expected','28 October 2026','rates','ABC News'),F('MYEFO','December 2026: more savings flagged','2026','budget','ABC News')],
 terms=[T('Fiscal stance','Whether the budget adds to (expansionary) or subtracts from (contractionary) aggregate demand.'),T('MYEFO','The Mid-Year Economic and Fiscal Outlook, the government\'s budget update.'),T('Policy mix','The combination of fiscal and monetary policy settings.')],
 links=[['ABC News, Jim Chalmers resists blame for another high inflation result, 28 Oct 2026','https://www.abc.net.au/news/2026-10-28/chalmers-downplays-further-fuel-discounts-amid-high-inflation/107319372'],L_AAP],
 file=fl(i),angle='If fiscal policy stays expansionary while the RBA tightens, rates must rise further for the same fall in demand. A fuel discount lowers measured CPI only temporarily while it adds to demand.',
 questions=[Q('Discuss whether fiscal policy should be tightened to support the Reserve Bank in reducing inflation.',5)],
 note='Government and Opposition positions reported as each put them. Complements the 26 October item on the Coalition\'s $31 billion savings plan.')

i='2026-10-29-no-easy-way-out-of-inflation'
add(id=i,title='Why there is no easy way out of high inflation',date='2026-10-29',type='news',outlets=['ABC News'],
 summary='An ABC analysis of why the soft landing has failed and why productivity growth is the only lasting fix, with the LRAS diagram.',
 lede='ABC analyst Tom Crowley argues the narrow path to a soft landing promised in 2022 has failed, with war-related supply constraints colliding with an AI and data-centre investment boom that is lifting demand. He expects policy to go harder for longer, holding back demand well into 2027, unless productivity improves.',
 about={'h09':['4E.1','3A.6'],'y12':['Y2d.1','Y2d.2','Y1a.10'],'y11':[]},also={'h09':['4D.2','3C.3'],'y12':['Y2c.8'],'y11':['P3c.4']},
 issues=['inflation','productivity','rates'],levers=['micro','monetary'],diagrams=['adas'],
 figures=[F('Expected cash rate after 3 November','4.85% (highest in 18 years)','29 October 2026','rates','ABC News analysis')],
 terms=[T('Soft landing','Slowing inflation without causing a recession.'),T('Productivity','Output per unit of input, such as per hour worked.'),T('Aggregate supply','The total output the economy can produce at each price level.')],
 links=[['Tom Crowley, Bad inflation result lays bare the ugly truth: there is no easy way out, ABC News (analysis), 29 Oct 2026','https://www.abc.net.au/news/2026-10-29/bad-inflation-result-political-pressure/107318484']],
 file=fl(i),angle='Microeconomic reform is slow and uncertain, so in the short run macroeconomic policy carries the load: a strong answer to any limitations-of-policy question.',
 questions=[Q('Assess the role of productivity growth in achieving sustained low inflation in Australia.',5)],
 note='An analysis piece, so treat it as one view. It also criticises EV and home-battery discounts, which is the author\'s judgement.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',removed,'added',n,'total',len(d))
