import json,os
p='data/evidence.json'; d=json.load(open(p))
REMOVE={'2026-11-02-oil-eases-hormuz-talks','2026-11-02-uk-fta-backpacker-rules'}
os.makedirs('_to_delete/superseded',exist_ok=True)
for x in d:
    if x['id'] in REMOVE:
        src=x['file']['path']
        if os.path.exists(src): os.rename(src,'_to_delete/superseded/'+os.path.basename(src))
d=[x for x in d if x['id'] not in REMOVE]; have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
def fl(i): return {'path':f'files/{i[:7]}/{i}.pdf','label':'One-page digest','pages':1}
recs=[]
def add(**k): recs.append(k)
BLOG='https://www.abc.net.au/news/2026-11-04/asx-markets-business-live-news-nov-4/107343406'
L_BLOG=['ABC News, ASX markets business live blog, 4 Nov 2026',BLOG]
SMP=['RBA, Statement on Monetary Policy, November 2026','https://www.rba.gov.au/publications/smp/2026/nov/']
POL='https://www.abc.net.au/news/2026-11-04/federal-politics-live-blog-angus-taylor-rates/107342840'
L_POL=['ABC News, Federal politics live blog, 4 Nov 2026',POL]

i='2026-11-04-oil-near-100-hormuz-blockade'
add(id=i,title='Oil slips about 3% but stays near US$100 as the Hormuz blockade keeps energy prices high',date='2026-11-04',type='news',outlets=['Al Jazeera','ABC News','Reuters','Euronews','RBA'],
 summary='Shows why oil stays high after a small fall when supply is blockaded and demand is price-inelastic, and how the shock reaches inflation. Replaces the 2 November edition.',
 lede='Brent crude fell US$3.20 (about 3.1%) to US$100.40 a barrel on 4 November, after the US midterm elections and reports of peace talks, but the effective blockade of the Strait of Hormuz keeps prices high. The RBA lists energy prices and the Middle East conflict as key upside risks to inflation, with the cash rate now 4.85%.',
 about={'h09':['3C.3','1A.1'],'y12':['Y1c.4','Y1c.5','Y3e.3'],'y11':[]},also={'h09':['3C.4','4D.3','1A.8'],'y12':['Y1c.1','Y1a.10','Y1a.13','Y2c.8'],'y11':[]},
 issues=['inflation','global','trade'],levers=['monetary'],diagrams=['ds','adas','flow'],
 figures=[F('Brent crude','US$100.40 (-US$3.20, about -3.1%)','4 November 2026','global','Al Jazeera'),F('US crude (WTI)','US$93.08 (about -3.1%)','4 November 2026','global','Al Jazeera'),F('Brent crude in Australian trading','choppy, around US$103-104','4 November 2026','global','ABC News'),F('Eurozone inflation expected by ING','near 4%','2026','inflation','ING via Euronews'),F('Australian fuel spending','+5.4%','September 2026','inflation','ABS via ABC News'),F('RBA cash rate','4.85%','3 November 2026','rates','RBA')],
 terms=[T('Supply-side shock','A sudden change in production costs or supply that shifts aggregate supply.'),T('Price-inelastic demand','Quantity demanded changes proportionally less than price; oil has few short-run substitutes.'),T('Stagflation','Rising inflation combined with weak growth.')],
 links=[['Al Jazeera, US markets rise as Democrats sweep midterm elections, 4 Nov 2026','https://www.aljazeera.com/economy/2026/11/4/us-markets-rise-as-democrats-sweep-midterm-elections'],L_BLOG,['Euronews, US midterms: what Trump\'s defeat means for Europe and global markets, 4 Nov 2026','https://www.euronews.com/2026/11/04/us-midterms-what-trumps-defeat-means-for-europe-and-global-markets'],SMP],
 file=fl(i),angle='A blockade shifts supply left and, with inelastic short-run demand, the price rises a lot even if quantity falls only a little. On an AD/AS diagram higher oil prices shift SRAS left: higher prices and lower output, a challenge for central banks.',
 questions=[Q('Explain how a supply disruption in the Middle East can raise inflation in economies that import little oil directly from the region. Use a diagram.',4)],
 note='Replaces the 2 November item, which reported Brent around US$110 (range US$108-111), a peak near US$118 in October, and Goldman Sachs estimating a US$27 a barrel risk premium. The digest attributes the fall to the midterm elections and peace talk reports; the election result is given only in the Al Jazeera link title, so check that article. UPDATE DUE: further oil price moves and any Hormuz agreement.')

i='2026-11-04-uk-fta-backpacker-rules-migration'
add(id=i,title='Albanese wants backpacker rules in the UK free trade deal changed to help cut migration',date='2026-11-04',type='news',outlets=['ABC News'],
 summary='Shows how a free trade agreement can cover the movement of people, and the trade-offs of tighter working holiday rules for demand, housing and farm labour. Replaces the 2 November edition.',
 lede='Prime Minister Anthony Albanese said the working holiday arrangements in the Australia-UK Free Trade Agreement should change so that fewer people arrive and net overseas migration falls. British backpackers can currently stay up to three years without doing the specified work, such as regional farm work, that other working holiday makers must do.',
 about={'h09':['2D.2','2D.3'],'y12':['Y3a.13','Y3a.16'],'y11':[]},also={'h09':['1B.4','2D.1'],'y12':['Y3a.3'],'y11':[]},
 issues=['trade','employment','housing'],levers=['trade','labour'],diagrams=['ds','compare'],
 figures=[F('Maximum stay for British backpackers without specified work','3 years','2026','trade','ABC News'),F('British working holiday makers','nearly 80,000 (about 47,000 in 2024)','last financial year','trade','ABC News (2 November report)'),F('Harvest workers who come from overseas','about 1 in 7','2026','employment','ABC News (2 November report)'),F('Proposed cap on second-year working holiday visas','45,000','2026','trade','ABC News (2 November report)')],
 terms=[T('Free trade agreement (FTA)','A deal that lowers barriers to trade in goods and services between countries and can also cover the movement of people.'),T('Net overseas migration (NOM)','Arrivals minus departures of people staying 12 months or more.'),T('Labour supply','The number of workers willing and able to work at each wage.')],
 links=[L_POL,['ABC News, Albanese to discuss British backpacker changes with Burnham, 2 Nov 2026','https://www.abc.net.au/news/2026-11-02/albanese-to-discuss-british-backpacker-changes-with-burnham/107208084']],
 file=fl(i),angle='Migration affects both sides of the economy: it adds to aggregate demand (housing, consumption) and aggregate supply (labour). Cutting it may ease demand pressure but worsen labour shortages in farming, tourism and hospitality.',
 questions=[Q('Assess the economic costs and benefits of including labour-mobility provisions, such as working holiday visas, in a free trade agreement.',6)],
 note='Replaces the 2 November item, whose figures are carried over. Any change needs the UK\'s agreement because the rules are part of a bilateral agreement. The Prime Minister described UK Prime Minister Andy Burnham as "very constructive". The diagram is the digest\'s illustration. UPDATE DUE: outcome of the talks.')

i='2026-11-04-canva-david-jones-job-losses'
add(id=i,title='Canva cuts more than 1,200 jobs, and questions grow over David Jones before Christmas',date='2026-11-04',type='news',outlets=['ABC News'],
 summary='A current case for classifying job losses as cyclical or structural, with weak demand shown on the AD/AS diagram.',
 lede='Design company Canva is cutting more than 1,200 roles, about a fifth of its workforce, and says they are not being replaced by AI. David Jones faces speculation about its finances after Scentre told the ASX it had paid rent only up to 30 September 2026 for its 17 stores in Westfield centres.',
 about={'h09':['3B.3','3B.6','3A.7'],'y12':['Y1b.5','Y1b.6','Y1a.14'],'y11':['P1e.7','P1e.5']},also={'h09':['3B.2','4D.3'],'y12':['Y1b.10','Y1b.11'],'y11':[]},
 issues=['employment','growth','rates'],levers=['monetary'],diagrams=['adas','compare'],
 figures=[F('Roles Canva is cutting','more than 1,200 (about a fifth of the workforce)','November 2026','employment','ABC News'),F('David Jones stores in Westfield centres','17 (rent paid to 30 September 2026)','November 2026','employment','Scentre via ABC News'),F('Myer share price','+4.7%','4 November 2026','growth','ABC News'),F('RBA rate rises in 2026','5, with the cash rate at 4.85%','3 November 2026','rates','RBA')],
 terms=[T('Cyclical unemployment','Unemployment caused by a downturn in the economic cycle and weak aggregate demand.'),T('Structural unemployment','Unemployment caused by long-term changes in the economy, such as new technology or shifts in consumer tastes.'),T('Discretionary spending','Non-essential purchases households can delay.')],
 links=[L_BLOG,['ABC News, David Jones future in doubt as debt and loan questions grow, 3 Nov 2026','https://www.abc.net.au/news/2026-11-03/david-jones-future-debt-loan-stores/107339924'],['ABC News, Australian banks lift interest rates after RBA cash rate hike, 4 Nov 2026','https://www.abc.net.au/news/2026-11-04/australian-banks-lift-interest-rates-after-rba-cash-rate-hike/107341858']],
 file=fl(i),angle='Real-world job losses often mix causes: a retailer losing customers to online shopping is structural, but losing them because of high rates is cyclical. Governor Bullock warned that with incomes not growing quickly it may feel like a recession for many households.',
 questions=[Q('Classify the job losses at Canva and David Jones as cyclical or structural. Justify your answer with evidence from the news.',4)],
 note='The reports on David Jones are speculation, not confirmed insolvency; Scentre only confirmed rent paid to 30 September. Canva says the roles are not being replaced by AI, which is the company\'s statement. Black Milk also entered voluntary administration, per the digest. UPDATE DUE: David Jones.')

i='2026-11-04-household-spending-nominal-vs-real'
add(id=i,title='Household spending rose 0.6% in September, but much of it was higher prices rather than more goods',date='2026-11-04',type='stats',outlets=['ABS','ABC News','Capital Economics','KPMG'],
 summary='Shows the difference between nominal and real spending growth: 2.1% in dollars against 0.7% in volume, with fuel driving cost-push inflation.',
 lede='ABS data show household spending rose 0.6% in September, led by fuel (+5.4%), transport and health, after a revised -0.1% in August. Capital Economics says nominal spending rose 2.1% over the September quarter but volumes rose only 0.7%, and KPMG notes inflation is above 3% in 45% of the 87 items in the CPI basket.',
 about={'h09':['3C.1','3C.3','3A.4'],'y12':['Y1c.4','Y1c.8','Y1a.1'],'y11':[]},also={'h09':['3A.1','3C.2'],'y12':['Y1a.3','Y1c.2'],'y11':[]},
 issues=['inflation','growth'],levers=['monetary'],diagrams=['adas','chart'],
 figures=[F('Household spending, monthly','+0.6% (August revised -0.1%; July +1.0%)','September 2026','inflation','ABS Monthly Household Spending Indicator via ABC News'),F('Fuel spending','+5.4% (excise relief ended 3 August)','September 2026','inflation','ABS via ABC News'),F('Transport and health / recreation and culture','+1.5% / +0.8%','September 2026','inflation','ABS via ABC News'),F('Nominal / real (volume) spending growth','2.1% / 0.7%','September quarter 2026','growth','Capital Economics via ABC News'),F('CPI items with inflation above 3%','45% of 87 items','2026','inflation','KPMG via ABC News'),F('RBA forecast headline CPI','4.5%','December 2026','inflation','RBA')],
 terms=[T('Nominal vs real','Nominal values are in current dollars; real values remove the effect of price rises and measure volume.'),T('Cost-push inflation','Inflation caused by rising production costs, such as fuel, shifting SRAS left.'),T('Broad-based inflation','Price rises spread across many items rather than a few.')],
 links=[L_BLOG,SMP],
 file=fl(i),angle='Rising nominal spending is not the same as rising living standards, so use real figures when discussing growth. Link fuel prices to cost-push inflation: households pay more at the bowser, so spending rises in dollars while real consumption barely grows.',
 questions=[Q('Distinguish between nominal and real growth in household spending, using the September quarter figures. Explain why the difference matters for the RBA.',4)],
 note='The nominal and real quarterly growth figures are Capital Economics\' estimates, not ABS publications. Capital Economics thinks inflation may peak near 4.5% this quarter, which is its forecast.')

i='2026-11-04-job-vacancies-fall-ai'
add(id=i,title='Job vacancies fall to 325,000, now 31% below their peak, and few businesses blame AI',date='2026-11-04',type='stats',outlets=['ABS','ABC News','RBA'],
 summary='Uses vacancies as a leading indicator of unemployment and shows that falling labour demand is cyclical rather than caused by AI.',
 lede='ABS data show job vacancies fell 0.9% in the three months to August 2026 to 325,000, which is 31.2% below the May 2022 peak, with the fall concentrated in the private sector. About 82% of businesses said AI did not affect their vacancies and 4% said it reduced them.',
 about={'h09':['3B.2','3B.3'],'y12':['Y1b.5','Y1b.6','Y1b.11'],'y11':['P1e.5']},also={'h09':['3B.4','4D.3'],'y12':['Y1b.12','Y2c.5'],'y11':[]},
 issues=['employment','rates','productivity'],levers=['monetary'],diagrams=['ds','chart'],
 figures=[F('Job vacancies','325,000 (-0.9%)','three months to August 2026','employment','ABS Job Vacancies via ABC News'),F('Fall from the May 2022 peak','-31.2%','August 2026','employment','ABS via ABC News'),F('Private / public sector vacancies','286,300 (-2%) / 38,700 (+7.8%)','three months to August 2026','employment','ABS via ABC News'),F('Businesses saying AI did not affect vacancies','82%','2026','employment','ABS via ABC News'),F('Businesses saying AI reduced / increased vacancies','4% / fewer than 1%','2026','employment','ABS via ABC News'),F('Information media and telecommunications citing AI for fewer vacancies','16%','2026','employment','ABS via ABC News'),F('Unemployment rate, average / RBA forecast','4.6% / about 5.1% by end-2028','September quarter 2026','employment','RBA')],
 terms=[T('Job vacancy','An unfilled job that an employer is actively trying to fill; a leading indicator of unemployment.'),T('Structural unemployment','Unemployment caused by a mismatch between workers\' skills and available jobs, for example from technological change.'),T('Cyclical unemployment','Unemployment caused by a downturn in the economic cycle.')],
 links=[L_BLOG,SMP],
 file=fl(i),angle='Vacancies falling while unemployment rises signals cyclical weakness: higher rates shift labour demand left. The AI survey suggests technology is not yet a major source of structural unemployment.',
 questions=[Q('Explain why job vacancies are a useful leading indicator of unemployment. Refer to the August 2026 data.',3)],
 note='The ABS release covers the three months to August, so it is older than the other November items. The 5.1% unemployment forecast is the RBA\'s, from its November Statement on Monetary Policy.')

i='2026-11-04-inflation-politics-fiscal-reset'
add(id=i,title='Analysis: after years of inflation pain, the political debate over the economy needs a reset',date='2026-11-04',type='news',outlets=['ABC News'],
 summary='Sets the Treasurer\'s supply-shock argument against the Opposition\'s demand-pull argument, for answers on the policy mix and the political limits of fiscal policy.',
 lede='After the RBA\'s fifth rate hike of 2026, Labor and the Coalition returned to familiar arguments about who is to blame for inflation. ABC economics reporter Tom Crowley argues both scripts are worn out and that only a bold policy shift may break the cycle.',
 about={'h09':['4B.1','4C.2','4H.3'],'y12':['Y2b.3','Y2b.13','Y2b.14'],'y11':[]},also={'h09':['4C.1','4D.1','3C.3'],'y12':['Y2c.7','Y1c.4','Y2b.10'],'y11':['P5b.7']},
 issues=['inflation','budget','rates'],levers=['fiscal','monetary'],diagrams=['adas','chart'],
 figures=[F('Cash rate after the 3 November hike','4.85% (18-year high)','3 November 2026','rates','RBA'),F('Government spending','26.9% of GDP (Final Budget Outcome, cited by the Prime Minister)','2025-26','budget','ABC News'),F('Chalmers\' press conferences after RBA decisions','41 (17 hikes, 21 holds, 3 cuts)','2026','rates','ABC News analysis')],
 terms=[T('Demand-pull inflation','Inflation caused by aggregate demand growing faster than the economy\'s capacity.'),T('Policy mix','How fiscal and monetary policy work together; if the Budget adds to demand, the RBA may need higher rates.'),T('Political limitation','A constraint on policy because of voter and party pressures.')],
 links=[['Tom Crowley, Can anything break politics out of its inflation doom loop?, ABC News (analysis), 4 Nov 2026','https://www.abc.net.au/news/2026-11-04/can-anything-break-politics-out-of-its-inflation-doom-loop/107343140'],L_POL,['RBA, media release 2026-30: decision on the cash rate target, 3 Nov 2026','https://www.rba.gov.au/media-releases/2026/mr-26-30.html']],
 file=fl(i),angle='A strong answer weighs both causes: the Government points to supply shocks (the Middle East war and an AI investment boom) while the Opposition says government spending is driving demand. If fiscal policy adds to demand, monetary policy has to work harder.',
 questions=[Q('Evaluate the claim that fiscal policy is "working against" monetary policy in 2026. Explain one political and one economic limitation on using the Budget to fight inflation.',6)],
 note='An analysis piece, so it is one view. The positions of Chalmers, the Prime Minister and Angus Taylor are reported as each put them. The 26.9% spending figure is the Prime Minister\'s citation of the Final Budget Outcome; the 2 November item reported 26.8% (ABC), so check the Budget papers before quoting. Savings are promised in December\'s MYEFO; the Coalition backs indexing tax brackets and has ruled out raising the GST. UPDATE DUE: MYEFO.')

n=0
for r in recs:
    if r['id'] in have: continue
    d.append(r); n+=1
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('removed',len(REMOVE),'added',n,'total',len(d))
