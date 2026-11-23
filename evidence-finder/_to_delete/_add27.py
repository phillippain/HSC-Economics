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
      angle=angle,questions=questions,note=note,added='2026-11-24'))

ABC='ABC News'
def L(a,b): return [a,b]

R('2026-11-23-chalmers-weaker-growth-net-spending-cuts','4','Chalmers flags weaker growth and net spending cuts in the budget update','2026-11-23','news',[ABC,'The Conversation'],
 "Gives the official forecast downgrade and the contractionary fiscal stance planned for MYEFO, with the policy mix and automatic stabiliser trade-offs.",
 "In a statement to parliament on 23 November, Treasurer Jim Chalmers warned that growth will slow, unemployment will rise above 5% and inflation will stay high. The mid-year update (MYEFO) will deliver a net saving, with cuts outweighing new spending, so the budget does not add to inflation.",
 ['4C.1','4C.2','4B.1'],['Y2b.2','Y2b.3','Y2b.6','Y2b.14'],['P5a.4'],
 ['4D.3','3C.3'],['Y2b.13'],['P5c.3'],
 ['budget','growth','inflation'],['fiscal'],['adas','flow'],
 [F('Real GDP growth','2.3% last financial year, slowing to well below 2% for the next two years','November 2026','growth','Treasurer, via ABC News'),
  F('Unemployment peak','Above 5% (higher than the budget-time forecast)','November 2026','employment','Treasurer, via ABC News'),
  F('Inflation back in the 2-3% target band','Not until late 2027','November 2026','inflation','Treasurer, via ABC News'),
  F('PBS co-payment','Frozen at $25 until 2030 ($242 million over three years)','November 2026','budget','ABC News'),
  F('Private health insurance rebate for people aged 65+: proposed cut','$3 billion over four years','November 2026','budget','ABC News')],
 [T('MYEFO','The Mid-Year Economic and Fiscal Outlook, which updates the Budget forecasts.'),T('Contractionary fiscal policy','Lower spending or higher taxes that reduce aggregate demand.'),T('Automatic stabilisers','Budget items such as tax receipts and benefits that change with the economy and dampen the cycle without new decisions.')],
 [L('ABC News: Chalmers flags net spending cuts in mid-year budget, 23 Nov 2026','https://www.abc.net.au/news/2026-11-23/chalmers-flags-net-spending-cuts-in-mid-year-budget/107417628'),L('Yahoo News (The Conversation): Chalmers flags slowing growth, warns...','https://au.news.yahoo.com/chalmers-flags-slowing-growth-warns-043053500.html'),L('ABC News: Federal politics live blog, parliament, 23 Nov 2026','https://abc.net.au/news/2026-11-23/federal-politics-live-blog-parliament-nov-23/107415266')],
 "Discuss the policy mix: tight fiscal policy can share the load with monetary policy (cash rate 4.85%) but cuts G and shifts AD left when unemployment is already rising. Automatic stabilisers (lower tax receipts, higher benefits) push the other way.",
 [Q("Evaluate the appropriateness of a contractionary fiscal stance when unemployment is rising and inflation is above target.",8)],
 "UPDATE DUE: the MYEFO itself, which comes after the RBA's 8 December meeting so September-quarter GDP can be included. Forecasts, not outcomes. Positives noted: business investment growing faster than forecast, wages growing above 3% and no recession forecast. Chalmers said tax receipts will be substantially lower than forecast. Replaces the 22 November pre-statement card (Chalmers said MYEFO would cut 'enough, but not too much'; no cuts confirmed; Gallagher flagged 'belt tightening'; calls to means-test EV and home battery subsidies; Chalmers rejected that spending drives inflation while the Opposition alleged an 'active inflation agenda'; two deregulation tax changes save business $52 million a year; government spending 26.8% of GDP in 2026-27 against 31.3% in the pandemic era per ABC's Verrender, 3 Nov) and, through it, the 18 November AFR/AAP survey card (JWS Research poll of 1,000 voters, an opinion poll: 83% concerned about the deficit, 54% mainly cut spending; deficit $31.5 billion in 2026-27).")

R('2026-11-23-job-losses-house-prices-slide-seven-months','3','Job losses mount and house prices slide as the slowdown bites','2026-11-23','news',[ABC],
 "Joins the labour market and housing market to show how a downturn's costs fall unevenly, with a house price demand diagram.",
 "Behind October's jump in unemployment to 4.9% are thousands of redundancies across retail, banking and tech, and some households are being forced to sell their homes. Cotality reports national house prices have now fallen for seven consecutive months.",
 ['3B.1','3B.3','3E.4'],['Y1b.1','Y1d.1'],['P3b.1'],
 ['4D.3','3A.7'],['Y2c.5'],['P4c.3'],
 ['employment','housing','rates'],['monetary'],['ds','flow'],
 [F('Unemployment rate','4.9% in October (from 4.7%), highest since 2021','October 2026','employment','ABS, via ABC News'),
  F('Employment change','About -43,500','October 2026','employment','ABS, via ABC News'),
  F('National house prices','Fallen seven months in a row','November 2026','housing','Cotality, via ABC News'),
  F('Job cuts','About 1,500 roles at David Jones; 500 jobs in doubt at General Pants (in administration)','November 2026','employment','ABC News')],
 [T('Cyclical unemployment','Unemployment caused by a lack of aggregate demand in a downturn.'),T('Wealth inequality','The uneven distribution of assets such as housing and shares.')],
 [L('ABC News: Australians lose jobs, recession fears, some forced to sell homes, 21 Nov 2026','https://www.abc.net.au/news/2026-11-21/australians-lose-jobs-recession-fears-some-forced-to-sell-homes/107408374'),L('ABC News: Federal politics live blog, recession concerns, 20 Nov 2026','https://www.abc.net.au/news/2026-11-20/federal-politics-live-blog-recession-concerns/107407116')],
 "Use for the economic and social costs of unemployment (lost income, skills and assets) and for how a downturn affects the distribution of wealth. Five rate rises this year (cash rate 4.85%) plus job insecurity shift housing demand left, lowering prices and sales.",
 [Q("Discuss the economic and social costs of rising unemployment in Australia.",6)],
 "Betashares' David Bassanese says the economy has 'one foot in a recession', and economists warn unemployment could pass 5%: opinions, not forecasts by the RBA or Treasury. Overlaps the 22 November human cost card (kept: this one adds housing) and 19 November house prices card. NAB, ANZ, Canva, Qantas and Bunnings have also announced cuts.")

R('2026-11-23-business-activity-contracts-pmi-stagflation-risk','3','Business activity shrinks at its fastest pace in five years while inflation stays high','2026-11-23','news',[ABC,'S&P Global','UBS'],
 "Provides the November PMI and UBS forecasts as evidence of stagflation risk, with a cost-push AD/AS diagram.",
 "Australia's private sector contracted further in November, with the S&P Global flash composite PMI falling to 48.7 from 49.6. UBS expects headline inflation to rise to 4.5% in the December quarter, pointing to a risk of stagflation: weak growth and high inflation together.",
 ['3C.3','3A.4','3A.7'],['Y1c.1','Y1c.5'],['P2c.4'],
 ['3B.2','4D.3'],['Y1a.5'],['P1e.4'],
 ['inflation','growth','employment'],['monetary'],['adas','flow'],
 [F('S&P Global flash composite PMI','48.7 (previous 49.6); below 50 means activity is shrinking','November 2026','growth','S&P Global, via ABC News'),
  F('New orders','Sharpest fall in five years; firms resumed shedding jobs','November 2026','growth','S&P Global, via ABC News'),
  F('UBS headline CPI forecast','4.5% in the December quarter 2026 (September: 4.3%)','Q4 2026 forecast','inflation','UBS, via ABC News'),
  F('UBS real GDP growth forecast','About 2.0% in 2026, 1.4% in 2027; unemployment above 5%','2026-27 forecast','growth','UBS, via ABC News'),
  F('Brent crude','About US$92.65 a barrel','23 November 2026','inflation','ABC News')],
 [T('PMI','Purchasing Managers\' Index: a survey-based measure of business activity where 50 separates expansion from contraction.'),T('Stagflation','Slow or negative growth combined with high inflation.')],
 [L('ABC News: ASX and business live news, 23 Nov 2026','https://www.abc.net.au/news/2026-11-23/asx-markets-business-live-news-november-23/107414602')],
 "High oil and input costs shift SRAS left: output falls and the price level rises. Stagflation is a policy dilemma: tightening to fight inflation deepens the downturn, while easing risks embedding inflation.",
 [Q("Explain why stagflation makes it difficult for policymakers to achieve both low inflation and low unemployment.",5)],
 "A survey and a bank's forecasts, not official outcomes. UPDATE DUE: October CPI (due the week of 23 November). Y1a.5 and P1e.4 are carried from the earlier recession card; check them against the syllabus text. The digest gives September headline inflation as 4.3%; an earlier card cites 3.9% for the year to September, so confirm against the ABS.")

R('2026-11-23-iron-ore-slides-steel-mills-struggle-aud-66-cents','2','Iron ore slides as China\'s steel mills struggle; the dollar sits near 66 US cents','2026-11-23','news',[ABC],
 "Links weaker Chinese steel demand to iron ore prices, the terms of trade and the AUD, with a demand-shift diagram.",
 "Iron ore, Australia's biggest export, finished last week at about US$88.50 a tonne and slipped again on Monday as Chinese steel demand weakened. Oil remains high, squeezing Australia's terms of trade from both sides, and the AUD is about 66 US cents.",
 ['2B.4','2C.6','2A.1'],['Y1a.7','Y3c.4','Y3c.6'],['P6a.2'],
 ['2C.5'],['Y3c.5'],['P6c.1'],
 ['trade','fx'],[],['ds','flow'],
 [F('Iron ore','US$88.50 a tonne (Friday), lower again Monday','20-23 November 2026','trade','ABC News'),
  F('Chinese steelmakers that are profitable','About 10% (38% a year ago)','November 2026','trade','Mysteel, cited by ABC News'),
  F('Brent / WTI crude','About US$92.65 / US$83.55 a barrel','23 November 2026','inflation','ABC News'),
  F('AUD / USD','About 66 US cents','23 November 2026','fx','ABC News'),
  F('10-year bond yield: Australia / US','4.91% / 4.95%','23 November 2026','rates','ABC News'),
  F('BHP South Australian copper plan','Double output to 650,000 tonnes by 2040 (US$14.2-18.1 billion); decision due first half of 2027','November 2026','investment','ABC News')],
 [T('Terms of trade','The index of export prices divided by import prices, times 100.'),T('Commodity dependence','Reliance on a narrow range of resource exports whose prices swing widely.')],
 [L('ABC News: ASX and business live news, 23 Nov 2026','https://www.abc.net.au/news/2026-11-23/asx-markets-business-live-news-november-23/107414602')],
 "Weaker Chinese steel demand shifts the iron ore demand curve left, lowering price and quantity. With oil import prices high, the terms of trade worsen, reducing export income and pressuring the AUD; link to the current account and to company tax receipts in MYEFO.",
 [Q("Explain how a fall in iron ore prices affects Australia's terms of trade and current account balance.",4)],
 "Market prices that move daily. The 22 November miners card gives iron ore at about US$90.6 a tonne (a different date and source): both are kept. Related 18 November China iron ore haggling card. AUD about 66 US cents, consistent with the 22 November 11-month low.")

R('2026-11-21-albanese-xi-li-qiang-full-turnaround-ai-talks','2','Xi hails a "full turnaround" with Australia as AI talks are agreed','2026-11-21','news',[ABC],
 "Shows the state of Australia-China trade relations, what business wants from the relationship, and the risk of export concentration.",
 "Anthony Albanese met Xi Jinping at APEC in Shenzhen and Premier Li Qiang in Beijing. Business leaders used the visit to press for better access for Australian food exports, years after Beijing's trade restrictions hit Australian goods, and the two governments agreed to hold talks on artificial intelligence.",
 ['2D.4','1C.2','2A.1'],['Y3a.6','Y3a.7','Y3a.13','Y3a.15'],['P6a.2'],
 ['1B.1','2B.4'],['Y3e.3'],['P6a.1'],
 ['trade','global'],['trade'],['ds','flow'],
 [F('Albanese-Xi meetings since 2022','Fifth','20 November 2026','trade','ABC News'),
  F('Australian jobs that depend on trade','One in four','November 2026','employment','PM Albanese, via ABC News'),
  F('Australia-China CEO Roundtable','Ninth','November 2026','trade','ABC News')],
 [T('Market access','The ability of exporters to sell into a foreign market without tariffs or other barriers.'),T('Export concentration','Reliance on a small number of markets, which raises vulnerability to shocks.')],
 [L('ABC News: Albanese to meet Xi for trade, 20 Nov 2026','https://www.abc.net.au/news/2026-11-20/albanese-to-meet-xi-for-trade/107406222'),L('ABC News: Australia strikes deal on AI talks with China after APEC, 21 Nov 2026','https://www.abc.net.au/news/2026-11-21/australia-strikes-deal-on-ai-talks-with-china-after-apec/107411592'),L('ABC News: Federal politics live blog, recession concerns, 20 Nov 2026','https://www.abc.net.au/news/2026-11-20/federal-politics-live-blog-recession-concerns/107407116')],
 "Weigh the gains from China trade against the risk of export concentration: earlier restrictions on barley, wine and beef show the downside. Easing barriers on beef shifts Chinese demand right, lifting export income. The Business Council pushed for access for beef and rice, medical devices and recognition of professional qualifications.",
 [Q("Assess the benefits and risks for the Australian economy of its trade relationship with China.",6)],
 "Replaces the 22 November card on the same meeting, which carried: China takes more than a quarter of Australia's exports; the Darwin Port (99-year lease from 2015 to Landbridge) remains a source of tension and Landbridge flagged possible legal action. The digest does not say whether the beef quota or tariff was resolved (earlier previews: 205,000 tonne 2026 quota used up in June, extra 55% tariff above it, about $1 billion of beef exports at risk per an AMIC industry estimate). Australia also signed a US-led declaration on reducing reliance on China for critical technologies; Trade Minister Don Farrell urged the Coalition to back the Australia-EU FTA. Albanese's Beijing visit was about six hours.")

R('2026-11-23-wall-street-correction-ai-share-boom-unwinds','1','Wall Street plunges into correction as the AI share boom unwinds','2026-11-23','news',['Reuters',ABC],
 "Gives the daily detail of the US correction and its spread to the ASX as evidence of financial globalisation and the wealth effect.",
 "US shares fell sharply on Friday 20 November, pushing the S&P 500 and Dow more than 10% below their record highs. The sell-off was led by AI and chip stocks and spread to the ASX, which has now lost eight sessions in a row.",
 ['1A.4','1D.1'],['Y3e.3','Y3c.4'],['P4b.2','P6c.1'],
 ['4D.3'],['Y1a.8'],['P6b.1'],
 ['global','growth'],[],['adas','flow'],
 [F('S&P 500 on Friday 20 November','-3.7% to 6,910 (seventh straight daily fall); Dow -1.9%','20 November 2026','global','Reuters'),
  F('Nasdaq','-5.3% on the day, about -10% on the week (biggest weekly fall since March 2020)','Week to 20 November 2026','global','Reuters'),
  F('Nvidia','-13.8% on the day','20 November 2026','global','Reuters'),
  F('ASX 200','-1.6% on Friday and lower again Monday: eight losing sessions in a row','20-23 November 2026','global','ABC News'),
  F('Fed pricing','Near-certain 25 basis point hike in December','November 2026','rates','Reuters')],
 [T('Correction','A fall of 10% or more from a recent market peak.'),T('Wealth effect','Households spend less when the value of their assets (shares, super, housing) falls.')],
 [L('Yahoo Finance (Reuters): Wall St futures slip as Anthropic...','https://finance.yahoo.com/markets/stocks/articles/wall-st-futures-slip-anthropic-104746137.html'),L('ABC News: ASX and business live news, 23 Nov 2026','https://www.abc.net.au/news/2026-11-23/asx-markets-business-live-news-november-23/107414602')],
 "Falling share prices cut household wealth (including super) and business confidence, so AD shifts left. A US shock moved the ASX within hours: integrated capital markets.",
 [Q("Explain how a sharp fall in US share prices can affect economic growth in Australia.",4)],
 "Daily and weekly market moves. The digest reports newly listed AI developer Anthropic falling 9.1% on its second trading day, a Goldman Sachs AI share index about 37% below its June peak, and Fed Governor Lisa Cook saying US rates are not high enough: reported, not independently checked. Related 22 November global share sell-off card (kept: it has the weekly table across markets and weekly falls by index) and 19 November Fed card.")

R('2026-11-23-philippines-seeks-us-tariff-cut-new-trade-deals','1','Philippines pushes to cut US tariffs while signing new trade deals','2026-11-23','news',['Daily Tribune (Philippines)'],
 "Shows how a developing economy responds to US protectionism by negotiating and diversifying, with a tariff diagram.",
 "The Philippines is negotiating with the United States to lower the tariff on its exports from 12.5% to 10%. At the same time it is spreading its risk with new agreements with Chile, Canada and the EU.",
 ['1C.2','1B.1','2D.4'],['Y3a.6','Y3a.7','Y3a.13'],['P6a.1'],
 ['1B.4'],['Y3a.14','Y3a.15'],[],
 ['trade','global'],['trade'],['ds','flow'],
 [F('US tariff on covered Philippine goods','12.5% (imposed July 2026, replacing an earlier 10%); Manila seeks 10%','November 2026','trade','Daily Tribune'),
  F('Philippine exports, September 2026','+35.6% (fastest growth in 35 years, per Trade Secretary Roque)','September 2026','trade','Daily Tribune'),
  F('New deals','Chile (signed 19 Nov at APEC); Canada FTA talks concluded 14 Nov; EU FTA targeted for end-2026 or early 2027','November 2026','trade','Daily Tribune')],
 [T('Tariff','A tax on imports that raises their domestic price.'),T('Trade diversification','Spreading exports across more markets to reduce dependence on any one.')],
 [L('Daily Tribune: Philippines seeks to cut US tariffs to 10% as trade talks continue, 23 Nov 2026','https://tribune.net.ph/2026/11/23/philippines-seeks-to-cut-us-tariffs-to-10-as-trade-talks-continue')],
 "Apply the tariff diagram (price rises to Pw+t, imports shrink, deadweight loss) and link to the WTO and the rise of bilateral and regional deals as countries route around protectionism.",
 [Q("With the aid of a diagram, explain the effects of a tariff on consumers, domestic producers and the government in the importing country.",6)],
 "Foreign-outlet report of ongoing talks, not a deal. The US rate followed a trade investigation into forced-labour enforcement, per the digest. Trump claimed the Philippines would buy all its farm and energy needs from the US; President Marcos said talks were about diversifying supply, not exclusive deals. Related 17 November trade deals card and 22 November Xi APEC card. Y3a.14 carried from the 17 November card.")

R('2026-11-22-cop31-collapses-no-deal-bowen-co-president','1','COP31 collapses without a climate deal','2026-11-22','news',['UN News',ABC],
 "Shows why international environmental agreements are hard to reach, using the externality and free-rider problems, with Australia as co-president.",
 "The UN climate summit in Antalya, Türkiye, ended on Sunday 22 November without a final agreement. It was the longest-running climate summit on record and broke down over whether the text should mention fossil fuels. Australia's Chris Bowen was co-president.",
 ['4G.4','3F.4','1D.8'],['Y1e.5','Y2f.6','Y1e.4'],['P2h.3'],
 ['3F.2','4I.6'],['Y2f.8'],['P2h.4'],
 ['environment','global'],['environmental','global'],['ds','flow'],
 [F('Length of talks','Two weeks plus two days of overtime; longest summit on record','22 November 2026','environment','UN News'),
  F('Formal objectors to the final text','EU, Panama and the Marshall Islands','22 November 2026','environment','UN News'),
  F('Final agreed text','None','22 November 2026','environment','UN News'),
  F('Next summit','COP32, Addis Ababa, Ethiopia','2027','environment','UN News')],
 [T('Negative externality','A cost imposed on third parties that is not included in the market price.'),T('Free-rider problem','Each country benefits from others\' cuts in emissions without paying the cost itself.')],
 [L('UN News: COP31 ends without agreement','https://news.un.org/en/story/2026/11/1168855'),L('ABC News: Federal politics live blog, parliament, 23 Nov 2026','https://abc.net.au/news/2026-11-23/federal-politics-live-blog-parliament-nov-23/107415266')],
 "Use the MSC/MPC diagram: the market produces Q1 at P1, more than the socially optimal Q*, with a deadweight loss. Agreements need consensus, and nations with fossil-fuel exports can block it, so COP31 is evidence of the limits of international environmental management.",
 [Q("Using a negative externality diagram, explain why international cooperation is needed to reduce greenhouse gas emissions.",5)],
 "Replaces the earlier 22 November COP31 card (UN News, CBS) and, through it, the 16 November first-draft card. Carried facts: about 200 countries negotiated; early draft called for faster action to phase out fossil fuels but later drafts dropped mention of coal, oil and gas; the last draft kept a goal for electricity to supply about 35% of world energy by 2035, a carbon-capture target and a pledge to 'at least triple' adaptation finance; US sent no official delegation for the second year; about 2.5 degrees of warming on current national plans against the 1.5 degree Paris goal; Guterres called it deeply disappointing. New here: co-presidents Murat Kurum (Türkiye) and Chris Bowen (Australia); Saudi Arabia defended references to carbon capture and storage; Opposition Leader Angus Taylor called on Bowen to resign as Climate Minister (a political claim). Link 3 date: the live blog is 23 November.")

recs=[r for r in recs if r['id'] not in have]
REMOVE={'2026-11-22-myefo-chalmers-cuts-enough-not-too-much','2026-11-22-albanese-xi-shenzhen-full-turnaround','2026-11-22-cop31-ends-no-deal-fossil-fuels'}
d=[x for x in d if x['id'] not in REMOVE]
d+=recs
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
os.makedirs('_to_delete/superseded',exist_ok=True)
for i in REMOVE:
    src=f'files/{i[:7]}/{i}.pdf'
    if os.path.exists(src): os.rename(src,f'_to_delete/superseded/{i}.pdf')
print(len(recs),'added',len(d),'total')
