import json
p='data/evidence.json'; d=json.load(open(p)); have={x['id'] for x in d}
def F(l,v,a,i,s): return {"label":l,"value":v,"asAt":a,"issue":i,"source":s}
def T(t,x): return {"term":t,"def":x}
def Q(q,m): return {"q":q,"marks":m}
S='AFR (Michael Read), from ABS CPI data'
i='2026-10-27-afr-everyday-price-rises-rba-test'
r=dict(id=i,title='Six everyday items are up more than 40% since the pandemic as the CPI tests the RBA',date='2026-10-27',type='news',outlets=['Australian Financial Review','ABS'],
 summary='Shows how prices have outrun wages since late 2021 (a fall of about 4% in real wages) and sets out the supply-side and domestic demand views of what drives inflation.',
 lede='AFR analysis of ABS data finds consumer prices rose 21.5% from December 2021 to June 2026 while nominal wages rose 16.8%, and six CPI items (tobacco, insurance, gas, postal services, eggs, oils and fats) rose more than 40%. Wednesday\'s September quarter CPI is expected to decide whether the RBA lifts the cash rate to 4.85%.',
 about={'h09':['3C.1','3C.3','3C.4'],'y12':['Y1c.3','Y1c.4','Y1c.8'],'y11':[]},also={'h09':['3E.2','4D.2'],'y12':['Y1c.7','Y2c.4','Y2b.14'],'y11':[]},
 issues=['inflation','rates','inequality'],levers=['monetary','fiscal'],diagrams=['chart','compare'],
 figures=[F('Consumer prices (all items)','+21.5%','December 2021 to June 2026','inflation',S),F('Nominal wages','+16.8% (real wages about -4%)','December 2021 to June 2026','employment',S),F('Tobacco / insurance / gas and household fuels','+49.4% / +45.4% / +44.3%','December 2021 to June 2026','inflation',S),F('Electricity','+36.9%','December 2021 to June 2026','inflation',S),F('Expected trimmed mean, September quarter','1.0% (RBA forecast 0.8%); 3.6% annual','due 28 October 2026','inflation',S),F('Cash rate if the RBA raises again','4.85%','November 2026','rates',S)],
 terms=[T('Underlying (trimmed mean) inflation','Inflation excluding the most extreme price changes; the RBA\'s key gauge.'),T('Real wages','Wages adjusted for inflation; they fall when prices rise faster than pay.'),T('Cost-push inflation','Inflation caused by rising production costs such as fuel.')],
 links=[['AFR, The six everyday items that have risen in price the most, 27 Oct 2026 (subscriber copy)','https://www.afr.com/policy/economy'],['RBA, Sarah Hunter, Interview on 60 Minutes, 25 Oct 2026','https://www.rba.gov.au/speeches/2026/sp-ag-2026-10-25.html']],
 file={'path':f'files/2026-10/{i}.pdf','label':'One-page digest','pages':1},
 angle='Real wage change is about (1.168 / 1.215) - 1, roughly -4%. Contrast the supply-side view (Middle East conflict, imported cost-push) with the domestic demand view (RBA, Coalition, market services inflation), and note that the RBA acts when inflation becomes broad-based and domestic.',
 questions=[Q('Using the figures, calculate the approximate change in real wages from December 2021 to June 2026 and explain its effect on living standards.',3),Q('"Australia\'s inflation problem is mainly domestic." Assess this statement using evidence from the article.',6)],
 note='The link goes to the AFR economy page because the article is subscriber-only; the figures are as reported by the AFR from ABS data and were not checked against the ABS. UPDATE DUE: add the September quarter CPI result (ABS, 28 October) and the RBA decision on 3 November.')
if i not in have: d.append(r)
d.sort(key=lambda x:x['date'],reverse=True)
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1); print(len(d))
