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
      angle=angle,questions=questions,note=note,added='2026-11-23'))

ABC='ABC News'
def L(a,b): return [a,b]
H='https://www.abc.net.au/news/'

R('2026-11-22-myefo-chalmers-cuts-enough-not-too-much','4','Chalmers: MYEFO will cut "enough, but not too much"','2026-11-22','news',[ABC],
 "Shows the contractionary fiscal stance debate before the December MYEFO and the argument over whether government spending drives inflation.",
 "Treasurer Jim Chalmers says December's mid-year update will cut spending 'enough, but not too much'. No cuts are confirmed, Finance Minister Katy Gallagher has flagged 'belt tightening', and there are calls to means-test EV and home battery subsidies. Chalmers rejects the claim that spending drives inflation; the Opposition says the government has an 'active inflation agenda'.",
 ['4C.1','4C.2','4B.1'],['Y2b.2','Y2b.3','Y2b.6'],['P5a.4'],
 ['3C.3','4D.3'],['Y2b.14','Y2b.13'],['P5c.3'],
 ['budget','inflation'],['fiscal'],['adas','compare'],
 [F('Government spending as a share of GDP','26.8% (2026-27 estimate) versus 31.3% in the pandemic era','November 2026','budget','ABC News (Verrender analysis, 3 Nov 2026)'),
  F('Business savings from two deregulation tax changes','$52 million a year','November 2026','budget','ABC News')],
 [T('Contractionary fiscal policy','Lower government spending or higher taxes that reduce aggregate demand.'),T('Means test','Limiting a payment or subsidy to people below an income or asset level.')],
 [L('ABC News: Chalmers says MYEFO cuts will be "enough, but not too much", 22 Nov 2026',H),L('ABC News: Federal politics, 17 and 20 Nov 2026',H),L('ABC News: Verrender analysis of government spending, 3 Nov 2026',H)],
 "Cutting spending shifts AD left, easing demand inflation but also slowing growth and employment, a hard trade-off when unemployment is rising. Compare the case for cuts (lower deficit, less pressure on the RBA) with the case against (weaker growth, worse jobs outlook).",
 [Q("Assess the likely effects of a contractionary fiscal stance on inflation and employment in Australia.",6)],
 "UPDATE DUE: add the December MYEFO. Replaces the 18 November AFR/AAP card (JWS Research survey of 1,000 voters, an opinion poll: 83% concerned about the deficit; 54% mainly cut spending, 28% a mix, 7% mainly raise taxes, 2% borrow; deficit $31.5 billion in 2026-27 and deficits for at least a decade; Chalmers said capital gains tax changes will go ahead). Links are to the ABC home page because the digest gives titles and dates only.")

R('2026-11-22-rba-pause-after-split-vote-cba-outlook','4','RBA pauses at 4.85% after a 6-3 split: what happens next?','2026-11-22','news',['Commonwealth Bank','RBA'],
 "Gives the cash rate, the vote split and the forecast path so students can explain the RBA's decision and the transmission mechanism.",
 "The cash rate sits at 4.85% after a 25 basis point rise, the highest since 2008, decided 6-3. The three dissenters warned of a 'materially sharper downturn', while the majority worried inflation risks were upward. CBA says a December move is 'not live' and has cuts pencilled in for August and November 2027.",
 ['4D.1','4D.2','4D.3'],['Y2c.1','Y2c.2','Y2c.4','Y2c.5'],['P4c.3'],
 ['3C.1','3C.3'],['Y2c.3'],['P4c.4'],
 ['rates','inflation'],['monetary'],['flow','chart'],
 [F('Cash rate target','4.85% (+25 basis points; highest since 2008; 6-3 vote)','November 2026','rates','RBA'),
  F('RBA headline CPI forecast','4.5% in December 2026, back to 2.5% by mid-2028','November 2026','inflation','RBA Statement on Monetary Policy'),
  F('CBA expectation','December "not live"; cuts in August and November 2027','November 2026','rates','Commonwealth Bank')],
 [T('Transmission mechanism','The channels through which a change in the cash rate affects spending, saving, the exchange rate and inflation.'),T('Basis point','One hundredth of a percentage point.')],
 [L('Commonwealth Bank newsroom, November 2026','https://www.commbank.com.au/'),L('RBA: Statement on Monetary Policy, November 2026 overview','https://www.rba.gov.au/')],
 "Explain the board's trade-off: inflation still above target versus a weakening labour market. Higher rates reduce consumption and investment through the cash-flow, saving and asset-price channels, shifting AD left.",
 [Q("Explain how the RBA's most recent interest rate decision aims to achieve price stability, and outline one cost.",6)],
 "A bank forecast (CBA) and RBA projections, not outcomes. UPDATE DUE: RBA decision on 7-8 December. Overlaps the 17 November minutes card (6-3 split) and 19 November jobs shock card, which are kept: this card adds the forecast path. Links are to the outlets' sites because the digest gives titles only.")

R('2026-11-22-rising-unemployment-human-cost','3','Behind the 4.9%: the human cost of rising unemployment','2026-11-22','news',[ABC,'ABS'],
 "Puts real cases and the latest labour force figures together to show who bears the costs of unemployment.",
 "Unemployment has risen to 4.9% with about 44,000 jobs lost. One worker has been made redundant four times since 2019 and made over 100 applications; General Pants is in administration with 500 jobs in doubt and about 1,500 jobs were lost at David Jones. Cuts have also been reported at NAB, ANZ, Canva, Qantas and Bunnings.",
 ['3B.1','3B.2','3B.3'],['Y1b.1','Y1b.2'],['P3b.1'],
 ['3C.4'],['Y2a.2'],[],
 ['employment'],[],['chart'],
 [F('Unemployment rate','4.9%','October 2026','employment','ABS'),
  F('Jobs lost','About 44,000 (43,500 per ABS)','October 2026','employment','ABS'),
  F('Youth unemployment','11.3% (previously 11.1%)','October 2026','employment','ABS'),
  F('Participation rate','66.6% (previously 66.8%)','October 2026','employment','ABS')],
 [T('Cyclical unemployment','Unemployment caused by a downturn in economic activity.'),T('Participation rate','The labour force as a share of the working-age population.')],
 [L('ABC News: human cost of rising unemployment, 21 Nov 2026',H),L('ABS: Labour Force, Australia media release, October 2026','https://www.abs.gov.au/')],
 "Use the personal cases to discuss the costs of unemployment (lost income, lower output, social costs) and who bears them: young workers and those in retail and corporate roles.",
 [Q("Discuss the economic and social costs of rising unemployment.",6)],
 "Anecdotes illustrate the statistics but are not representative. Related 19 November unemployment and recession cards are kept. Links are to the outlets' sites because the digest gives titles only.")

R('2026-11-22-sahm-rule-recession-australia-entirely-possible','3','Sahm rule: a recession in Australia is "entirely possible"','2026-11-22','news',[ABC],
 "Introduces the Sahm rule as a way to read unemployment as a recession signal, with Australian numbers.",
 "Economist Claudia Sahm says a recession in Australia is 'entirely possible', though she is not forecasting one. The Sahm rule compares the three-month average unemployment rate with its lowest level over the prior 12 months; Australia is now 0.6 percentage points above. Saul Eslake says it could trigger in December, while the RBA and Treasury are not forecasting a recession.",
 ['3B.2','3B.3','1A.2'],['Y1b.1','Y1b.2'],['P3b.1'],
 ['3C.4'],['Y2a.2'],[],
 ['employment','growth'],[],['chart','compare'],
 [F('Australia\'s Sahm rule gap','0.6 percentage points','November 2026','employment','ABC News'),
  F('Trigger thresholds','0.5 points in the US; RBA research suggests 0.75 points for Australia','November 2026','employment','ABC News'),
  F('People unemployed','More than 750,000','October 2026','employment','ABC News')],
 [T('Sahm rule','A recession signal triggered when the three-month average unemployment rate rises by a set margin above its 12-month low.'),T('Recession','A sustained fall in economic activity, commonly two consecutive quarters of negative real GDP growth.')],
 [L('ABC News: Sahm rule and recession risk, 23 Nov 2026',H)],
 "Use as evidence on how unemployment relates to the business cycle. Note the caution: the rule was built for the US, and Governor Bullock says people may feel a recession before GDP shows one.",
 [Q("Assess whether rising unemployment is a reliable indicator of a recession in Australia.",6)],
 "Commentary and a rule of thumb, not a forecast. The RBA and Treasury are not forecasting a recession. Related 19 November recession cards (kept). The link is dated 23 November and goes to the ABC home page. UPDATE DUE: October CPI (24 Nov) and Q3 GDP (2 Dec). Check dot point 1A.2 against the course map.")

R('2026-11-22-albanese-xi-shenzhen-full-turnaround','2','Albanese meets Xi in Shenzhen: Xi hails a "full turnaround"','2026-11-22','news',["PM's office",ABC,'The Nightly'],
 "Shows the state of Australia-China trade relations after the APEC meeting and the risks of reliance on one market.",
 "In their fifth meeting, in Shenzhen, Xi Jinping hailed a 'full turnaround' in relations. China takes more than a quarter of Australia's exports. Tension remains over the Darwin Port, leased for 99 years from 2015 to Landbridge, which has flagged possible legal action.",
 ['2D.4','1C.2','2A.1'],['Y3a.6','Y3a.7','Y3a.13'],['P6a.2'],
 ['1B.1','2B.4'],['Y3a.15'],[],
 ['trade','global'],['trade'],['flow'],
 [F("China's share of Australian exports","More than a quarter",'November 2026','trade','PM\'s office / ABC News'),
  F('Albanese-Xi meetings','Fifth meeting','20 November 2026','trade','The Nightly')],
 [T('Trade diversification','Spreading exports across many markets to reduce reliance on one buyer.')],
 [L("PM's office: 33rd APEC Leaders' Summit",'https://www.pm.gov.au/media/33rd-apec-leaders-summit'),L('ABC News: APEC live blog, 20 Nov 2026',H),L('The Nightly: Albanese and Xi in Shenzhen','https://www.thenightly.com.au/')],
 "Balance the benefits of stronger China ties (export revenue, stable trade) against the risks of concentration and political tension.",
 [Q("Evaluate the implications for Australia of its trade relationship with China.",6)],
 "Replaces two preview cards: 19 November 'Beef tariffs on the table as Albanese meets Xi at APEC' (beef quota 205,000 tonnes, used up in June; extra 55% tariff above the quota; about $1 billion of beef exports at risk per an AMIC industry estimate; Rabobank said 2027 quota could be used up by May) and 18 November 'Albanese heads to APEC in Shenzhen as Xi calls for lower trade barriers' (APEC has 21 economies; WTO reported a surge in trade restrictions). The digest does not say whether the beef tariff was resolved: check the sources. The 14 November Trump-Xi-Putin preview is kept. Links to the outlets' sites where the digest gives titles only.")

R('2026-11-22-miners-slump-aud-11-month-low','2','Miners slump drags the ASX and pushes the AUD to an 11-month low','2026-11-22','news',['Motley Fool',ABC],
 "Links commodity prices, the terms of trade and the exchange rate in one week of market data.",
 "The ASX 200 fell 5.4% in the week to 8,592.6, its worst since 2022, led by materials (-12.3%). BHP (-12.7%) was overtaken by CBA as the largest ASX company, Rio Tinto fell 12.8%, copper about 10% and gold about 9%. The AUD fell from about 70 US cents in late October to about 66.5 cents, an 11-month low.",
 ['2C.2','2C.3','2B.4'],['Y3c.2','Y3c.4','Y3c.5'],['P6c.1'],
 ['2A.1'],['Y3c.6'],[],
 ['fx','trade'],[],['fx','ds'],
 [F('ASX 200 weekly fall','-5.4% to 8,592.6 (worst week since 2022)','Week to 20 November 2026','fx','Motley Fool'),
  F('ASX materials sector','-12.3%','Week to 20 November 2026','trade','Motley Fool'),
  F('AUD / USD','About US66.5c (11-month low), from about US70c in late October','November 2026','fx','Motley Fool / ABC News'),
  F('Iron ore','About US$90.6 a tonne','November 2026','trade','Motley Fool')],
 [T('Terms of trade','The ratio of export prices to import prices.'),T('Depreciation','A fall in the value of a currency in a floating exchange rate system.')],
 [L('Motley Fool: ASX 200 week in review, 22 Nov 2026','https://www.fool.com.au/'),L('ABC News: ASX and business live blog, 20 Nov 2026',H)],
 "Falling commodity export prices lower demand for AUD (D shifts left), so the AUD depreciates and the terms of trade fall. Falling export incomes also reduce national income.",
 [Q("Using a diagram, explain how lower commodity prices could affect the Australian dollar.",4)],
 "Weekly market figures; they move daily. Replaces the 19 November card 'Australian dollar slides towards 67 US cents' (AUD US67.12c, sixth straight daily fall; iron ore US$88.05 a tonne; gold US$3,724 an ounce; 10-year bond yield 5.09% Australia / 5.07% US). The 16 November commodity prices card is kept. Links to outlets' sites because the digest gives titles only.")

R('2026-11-22-xi-pitches-free-trade-apec-shenzhen','1','Xi pitches free trade at APEC as tariff tensions linger','2026-11-22','news',['Al Jazeera',"PM's office"],
 "Gives the free trade versus protection debate a current example, with a tariff diagram and Australia's position.",
 "At the APEC leaders' meeting in Shenzhen, Xi Jinping promised lower tariffs and wider market access and pledged to resist unilateralism and protectionism, read by commentators as criticism of US tariffs. Albanese said Australia has abolished more than 1,000 tariffs since 2022 and backs paperless trade and the WTO.",
 ['1B.1','1C.2','1B.3'],['Y3a.3','Y3a.6','Y3a.7','Y3a.13'],['P6a.1'],
 ['2D.4'],[],[],
 ['trade','global'],['trade','global'],['ds','flow'],
 [F('Tariffs abolished by Australia since 2022','More than 1,000','November 2026','trade',"PM's office"),
  F("Australia's annual trade with APEC economies",'About $1 trillion','November 2026','trade',"PM's office"),
  F('Australian business investment in APEC economies','About $2.5 trillion','November 2026','investment',"PM's office"),
  F('APEC members','21 economies','November 2026','trade','APEC')],
 [T('Protectionism','Measures such as tariffs, quotas and subsidies that shield domestic industries from imports.'),T('APEC','Asia-Pacific Economic Cooperation, a forum of 21 economies promoting freer trade and investment.')],
 [L('Al Jazeera: Xi\'s pitch for free trade amid Trump\'s global trade disruptions, 18 Nov 2026','https://aljazeera.com/news/2026/11/18/xis-pitch-for-free-trade-amid-trumps-global-trade-disruptions'),L("PM's office: 33rd APEC Leaders' Summit",'https://www.pm.gov.au/media/33rd-apec-leaders-summit')],
 "Apply the tariff diagram (price rises, imports fall, deadweight loss) and link the pledges to the gains from trade, noting China's own trade practices are often criticised.",
 [Q("Using a tariff diagram, explain the effects of protection on consumers and domestic producers.",5),Q("Assess the effect of rising global protectionism on a small open economy like Australia.",6)],
 "Statements of intent at a summit, not binding commitments. Check P6a.1 against the Year 11 syllabus text. Related 17 November trade deals card and 18 November WTO restrictions card.")

R('2026-11-22-global-share-sell-off-ai-stocks-crack','1','AI stocks crack and global share markets tumble','2026-11-22','news',['Rio Times','FNArena'],
 "Illustrates financial contagion and the wealth effect with a week of falls across major share markets.",
 "Share markets had one of their worst weeks in years. On Friday the S&P 500 fell 3.7% and the Nasdaq more than 5%, linked to profit-taking in AI stocks after Anthropic's record listing, and Fed minutes showed some officials think more rate rises may be needed. Copper lost about 9% and silver about 12%.",
 ['1A.4','1D.1'],['Y3e.3','Y3c.4'],['P4b.2','P6c.1'],
 ['4D.3'],[],['P6b.1'],
 ['global','growth'],[],['adas','chart'],
 [F('Nasdaq, week to 20 Nov','-9.8%','20 November 2026','global','FNArena'),
  F('S&P 500, week','-8.3%','20 November 2026','global','FNArena'),
  F('Nikkei, week','-7.7%','20 November 2026','global','FNArena'),
  F('DAX / ASX 200 / Hang Seng, week','-7.3% / -5.4% / -5.2%','20 November 2026','global','FNArena')],
 [T('Wealth effect','When asset prices fall, households feel poorer and cut spending.'),T('Financial contagion','Shocks in one market spread quickly to others through global financial flows.')],
 [L('Rio Times: Global economy briefing, 21 Nov 2026','https://www.riotimesonline.com/global-economy-briefing-november-21-2026/'),L('FNArena: The Market in Numbers, 21 Nov 2026','https://fnarena.com/2026/11/21/the-market-in-numbers-21-nov-2026/')],
 "Falling share prices cut wealth and confidence, shifting AD left. Explain the transmission to the ASX and superannuation balances.",
 [Q("Explain how a fall in global share prices can affect Australia's economic growth.",4),Q("Outline one benefit and one risk of global financial integration.",4)],
 "The digest links the sell-off to Anthropic's record listing; this detail is as reported by the digest and was not independently checked. Related 9 November AI shares and household wealth card and 19 November US Fed card (both kept). Syllabus codes 1D.1 and P4b.2 should be checked.")

R('2026-11-22-cop31-ends-no-deal-fossil-fuels','1','COP31 climate talks end with no deal on fossil fuels','2026-11-22','news',['UN News','CBS News'],
 "Shows why international environmental agreements are hard to reach, using the externality and free-rider problems.",
 "After two weeks and two days of overtime in Antalya, nearly 200 countries failed to adopt a final text; the EU and Panama formally objected. Later drafts dropped every mention of coal, oil and gas, but kept a goal for electricity to supply about 35% of world energy by 2035, a carbon-capture target and a pledge to 'at least triple' adaptation finance. The US sent no official delegation for a second year.",
 ['4G.4','3F.4','1D.8'],['Y1e.5','Y2f.6','Y1e.4'],['P2h.3'],
 ['3F.2','4I.6'],['Y2f.8'],['P2h.4'],
 ['environment','global'],['environmental','global'],['ds','flow'],
 [F('Countries negotiating','About 200','November 2026','environment','UN News'),
  F('Warming on current national plans','About 2.5°C (Paris goal of 1.5°C at risk)','November 2026','environment','UN News'),
  F('Electricity share of energy by 2035 (kept in the last draft)','About 35%','November 2026','environment','CBS News')],
 [T('Negative externality','A cost imposed on third parties that is not reflected in the market price.'),T('Free-rider problem','Each country gains from others\' emission cuts without bearing the cost itself.')],
 [L('UN News: COP31 ends without agreement, Nov 2026','https://news.un.org/en/story/2026/11/1168855'),L('CBS News: UN COP31 climate conference ends with no agreement','https://www.cbsnews.com/news/un-cop31-climate-conference-ends-no-agreement-fossil-fuel-debate-standstill/')],
 "Use the MSC/MPC diagram to show over-production of fossil-fuel energy, and discuss why consensus among about 200 countries is difficult.",
 [Q("Using a diagram, explain why fossil-fuel energy is over-produced in a free market.",4),Q("Discuss the difficulties of reaching global agreement on environmental sustainability.",6)],
 "Replaces the 16 November card on the first COP31 draft, which Australia tabled as co-host (35% electricity share by 2035; developing countries wanted at least US$120 billion in adaptation funding, triple current levels; final text was due Friday 20 November). The 11 November COP31 electrification and Albanese cards are kept. Final text status may change: check the UN site. Codes 1D.8 and 4I.6 are carried from the earlier card.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-18-myefo-deficit-spending-cuts-cgt','2026-11-16-cop31-first-draft-deal-final-week','2026-11-19-aud-slides-towards-67-cents-sixth-day','2026-11-19-beef-tariffs-albanese-xi-apec','2026-11-18-albanese-apec-shenzhen-xi-barriers'}
d=[x for x in d if x['id'] not in REMOVE]
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
