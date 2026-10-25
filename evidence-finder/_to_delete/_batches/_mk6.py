R=[]
def rec(i,id,title,date,type,outlets,summary,lede,about,also,issues,levers,diagrams,figures,terms,questions,note,label,pages,angle=None,extended=None,dateText=None,links=None):
    h09a,y12a,y11a=about; h09b,y12b,y11b=also
    r={"id":id,"title":title,"date":date}
    if dateText: r["dateText"]=dateText
    r.update({"type":type,"outlets":outlets,"summary":summary,"lede":lede,
      "about":{"h09":h09a,"y12":y12a,"y11":y11a},"also":{"h09":h09b,"y12":y12b,"y11":y11b},
      "issues":issues,"levers":levers,"diagrams":diagrams,
      "figures":[dict(label=a,value=b,asAt=c,issue=d,source=e) for a,b,c,d,e in figures],
      "terms":[{"term":a,"def":b} for a,b in terms]})
    if angle: r["angle"]=angle
    r["questions"]=[{"q":q,"marks":m} for q,m in questions]
    if extended: r["extended"]=extended
    r["note"]=note
    ym=date[:7]
    r["file"]={"path":f"files/{ym}/{id}.pdf","label":label,"pages":pages}
    r["links"]=[{"label":a,"url":b} for a,b in (links or [])]
    r["_i"]=i
    R.append(r)

# 1 super tax opinion
rec(0,"2025-05-15-afr-chalmers-super-tax-opinion","Opinion: Chalmers' tax on unrealised super gains is clever, and cruel to the unadvised","2025-05-15","news",
 ["Australian Financial Review"],
 "A critical view of the proposed tax on high-balance super that shows how a tax on unrealised gains can fall on people who do not expect to be caught, which is useful for evaluating equity and efficiency.",
 "AFR wealth reporter Andrew Hobbs argues the proposed tax on unrealised gains in super balances above $3 million will initially hit hardly anyone, but will catch unsophisticated investors holding illiquid assets as property values rise. The government says fewer than 80,000 people (0.5 per cent of account holders) are affected, a figure the article notes dates from February 2023.",
 (["4C.2"],["Y2b.10"],["P5b.6","P5b.7"]),
 (["3E.3","3E.4","4I.5"],["Y1d.5","Y2b.11"],["P5b.3","P4a.3"]),
 ["budget","inequality"],["fiscal"],[],
 [("Super balance threshold for the proposed tax","$3 million (possibly $2 million)","May 2025 proposal","budget","AFR (Andrew Hobbs)"),
  ("Share of super account holders affected at start","0.5% (under 80,000 people)","Government figure from Feb 2023","inequality","AFR citing the Treasurer"),
  ("Share of account holders paying by 2053","about 10%","Government projection","inequality","AFR citing government numbers"),
  ("Super contribution rate used in author's example","12% of salary","May 2025","budget","AFR")],
 [("Unrealised gain","An increase in the value of an asset that has not yet been sold, so no cash has been received."),("Bracket creep / non-indexed threshold","A threshold that is not adjusted for inflation, so more people reach it over time."),("Vertical equity","Those with a greater capacity to pay contribute more tax.")],
 [("Explain why a tax on unrealised gains may be seen as less fair than a tax on realised gains.",3),("Outline why not indexing the $3 million threshold matters over time.",2)],
 "Older item (published May 2025): figures are as at that date; check for newer data before quoting. Opinion piece, not a news report; the proposal was a draft and design details may differ from what was legislated. Newspaper article reproduced for classroom use. A second copy of the same article in the folder was skipped as a duplicate.",
 "Original article",8,
 angle="Use as the opposing view when you evaluate the equity of taxing high-balance super: the policy is progressive in intent but the article argues it is poorly targeted at the unadvised.")

# 2 dashboard
rec(2,"2026-09-02-year11-economy-data-dashboard","Australian economy data dashboard for Year 11, September 2026","2026-09-02","stats",
 ["ABS","RBA","Fair Work Commission","Treasury (Budget Paper 1)"],
 "A single set of ten current indicators, each with its previous value and an exam hook, ready to quote with direction and source in any short answer or extended response.",
 "The dashboard collects the latest official figures at 2 September 2026: GDP growth of 0.4 per cent in the June quarter, headline inflation of 3.5 per cent, unemployment of 4.5 per cent and a cash rate of 4.35 per cent after three rises in 2026. It links them into a loop of prices, the RBA, borrowing and output, jobs and the federal Budget.",
 (["3A.4","3B.1","3C.1","4D.3","4C.1"],["Y1a.3","Y1b.9","Y1c.3","Y2c.5","Y2b.3"],["P1e.5","P4c.3","P5a.4","P3a.4"]),
 (["3A.7","3C.2","4A.7","4I.3","3B.2"],["Y1a.15","Y1b.8","Y2e.4","Y2b.9","Y2c.4"],["P1e.4","P1d.2","P5c.2"]),
 ["growth","inflation","employment","rates","budget"],["fiscal","monetary"],["flow","chart"],
 [("Real GDP growth, quarterly","0.4% (March qtr 0.3%; 2.1% through the year)","June qtr 2026","growth","ABS National Accounts"),
  ("Headline CPI inflation","3.5% (June 3.8%)","12 months to July 2026","inflation","ABS Monthly CPI Indicator"),
  ("Underlying inflation (trimmed mean)","3.6% (unchanged)","12 months to July 2026","inflation","ABS Monthly CPI Indicator"),
  ("Unemployment rate","4.5% (June 4.4%)","July 2026","employment","ABS Labour Force"),
  ("Underemployment rate","6.4% (unchanged; underutilisation 10.9%)","July 2026","employment","ABS Labour Force"),
  ("RBA cash rate target","4.35% (was 4.10%)","Held 11 Aug 2026","rates","RBA"),
  ("Household saving ratio","6.5% (March qtr 6.4%)","June qtr 2026","growth","ABS National Accounts"),
  ("Underlying cash balance","-$31.5b (-1.0% of GDP)","2026-27 Budget estimate","budget","2026-27 Budget, Budget Paper 1")],
 [("Trimmed mean","Underlying inflation that removes the 15% of items with the largest price rises and the 15% with the largest falls."),("Underutilisation rate","Unemployment plus underemployment as a share of the labour force."),("Fiscal stance","Whether the Budget is expansionary, contractionary or neutral, judged by the change in the balance as a share of GDP."),("Transmission mechanism","How a change in the cash rate reaches spending and prices.")],
 [("Distinguish between headline and underlying inflation, using the 3.5% and 3.6% figures.",3),("Explain how the three cash-rate rises in 2026 are expected to slow aggregate demand.",4),("Assess whether a deficit of 1.0% of GDP is an appropriate fiscal stance when growth is below trend.",6)],
 "Teacher revision handout for Year 11 compiling official releases as at 2 September 2026; figures are as at that date and later releases will have updated them, so check the ABS and RBA before quoting. Budget figures for 2025-26 onwards are estimates, not outcomes.",
 "Data sheet",8,
 angle="Quote direction as well as level (for example unemployment 4.5%, up from 4.4%) and link two indicators in each paragraph.")

# 3 petrol
rec(3,"2026-08-01-bocsar-petrol-thefts-price-elasticity","Petrol thefts and petrol prices: a BOCSAR study turned into an elasticity lesson","2026-08-01","report",
 ["NSW Bureau of Crime Statistics and Research (BOCSAR)"],
 "A real NSW dataset that applies price elasticity of demand, the total outlay method and supply shocks in the petrol market, and shows that cost of living matters more than price for theft.",
 "BOCSAR Bulletin No. 280 (August 2026) finds a 1 per cent rise in petrol prices raises petrol thefts by about 3 per cent over several months, around 37 extra incidents a month in NSW. The bigger driver is the general cost of living, with wages moving theft in the opposite direction.",
 ([],[],["P2e.1","P2e.3","P2e.4","P2d.1"]),
 ([],[],["P2c.4","P2e.5","P1e.5","P3a.8"]),
 ["inflation"],["micro"],["ds"],
 [("Increase in petrol thefts after a 1% rise in petrol prices","about 3% (peak 3.3%; 1.7% in month 0)","BOCSAR Bulletin 280, Aug 2026","inflation","NSW BOCSAR (Adams, 2026)"),
  ("Extra petrol thefts a month across NSW","37","From a 1% price rise","inflation","NSW BOCSAR"),
  ("Average petrol thefts a month in NSW","1,118","2025","inflation","NSW BOCSAR"),
  ("Elasticity of theft with respect to wages","-16.35%","Since 2016","inflation","NSW BOCSAR"),
  ("Elasticity of theft with respect to living costs","+6.51%","Since 2016","inflation","NSW BOCSAR"),
  ("Elasticity of theft with respect to petrol prices","+0.94%","Since 2016","inflation","NSW BOCSAR")],
 [("Price elasticity of demand","Responsiveness of quantity demanded to a change in price: %change in quantity demanded divided by %change in price."),("Total outlay method","Judging elasticity from whether total spending (price times quantity) rises or falls when price changes."),("Supply shock","A sudden change in the cost or availability of an input that shifts the supply curve."),("Correlation vs causation","Two series can move together because a third factor drives both.")],
 [("Explain why the demand for petrol is price inelastic.",4),("Using the worked example, apply the total outlay method to show demand is inelastic.",3),("With reference to the stimulus, explain what the findings show about the importance of income compared with price.",4)],
 "Year 11 teacher summary of a BOCSAR bulletin: the document gives August 2026 but no day, so the date is set to the first of the month. Figure B and the worked example (180c to 198c, 500m to 485m litres) are hypothetical teaching figures, not results from the bulletin. Check the original bulletin before quoting.",
 "Teacher handout",5,dateText="August 2026",
 angle="Use as a Year 11 stimulus for PED: inelastic demand means a supply shock lands on household budgets, which links to cost of living.")
# 4 income and wealth
rec(4,"2023-01-01-mccrindle-income-wealth-distribution","Australia's income and wealth distribution infographic (McCrindle, 2023)","2023-01-01","graph",
 ["McCrindle","ABS","Domain"],
 "A one-page picture of how unequally income and wealth are shared across household quintiles, states and generations, with ready-made ratios to quote.",
 "The top 20 per cent of households earn 48 per cent of all income and own 63 per cent of private wealth, while the lowest 20 per cent earn 4 per cent of income and own 1 per cent of wealth. The average household in the top quintile holds 93 times the wealth of the bottom quintile, and a median house costs 10.3 times average full-time earnings.",
 (["3E.4","3E.5","3E.6"],["Y1d.1","Y1d.2","Y1d.11"],["P2h.8"]),
 (["3E.1","4A.6"],["Y1d.5","Y1d.10"],["P3a.9"]),
 ["inequality","housing"],[],["chart","compare"],
 [("Share of all income earned by the top 20% of households","48% (lowest 20%: 4%)","2023","inequality","McCrindle, ABS"),
  ("Share of private wealth owned by the top 20% of households","63% (lowest 20%: 1%)","2023","inequality","McCrindle, ABS"),
  ("Average household net wealth","$1,042,000 (top 20%: $3,267,100; lowest 20%: $35,100)","2023","inequality","McCrindle, ABS"),
  ("Average household gross annual income","$121,108 (top 20%: $288,028; lowest 20%: $25,012)","2023","inequality","McCrindle, ABS"),
  ("Top 20% wealth compared with the lowest 20%","93 times average wealth","2023","inequality","McCrindle"),
  ("Median house price compared with average full-time earnings","$1,008,988 (10.3 times earnings of $97,510)","2023","housing","McCrindle, Domain House Price Report")],
 [("Income quintile","One fifth of households ranked by income."),("Net wealth","The value of assets minus debts."),("Income versus wealth","Income is a flow received over a period; wealth is a stock of assets owned at a point in time.")],
 [("Using the infographic, compare the distribution of income with the distribution of wealth.",3),("Explain one reason wealth is more unequally distributed than income.",3)],
 "Older item (published 2023): figures are as at that date; check for newer data before quoting. Only the year (2023) is given, so the date is set to 1 January. Infographic from a social research company drawing on ABS and Domain data; secondary source.",
 "Data sheet",2,
 angle="Pair the income and wealth quintile shares to show that wealth inequality is wider, then use the generational table for age differences.")

# 5 poverty
rec(5,"2024-02-01-senate-poverty-inquiry-final-report","Senate inquiry final report: The extent and nature of poverty in Australia","2024-02-01","report",
 ["Senate Community Affairs References Committee"],
 "The most authoritative recent source on Australian poverty rates, groups at risk and the role of income support, with 14 recommendations to cite in policy evaluation.",
 "The Senate committee's final report (February 2024) uses ACOSS and UNSW analysis to show 13.4 per cent of people, and 16.6 per cent of children, live below the poverty line after housing costs. It examines income support adequacy, employment services, First Nations poverty and child poverty and recommends urgent action to ensure no one lives in poverty.",
 (["3E.5","3E.6","3E.3"],["Y1d.4","Y1d.9","Y1d.8"],["P2h.8","P5a.1"]),
 (["4I.5","4F.5"],["Y1d.6","Y2b.10","Y2e.4"],["P5c.1"]),
 ["inequality","employment"],["fiscal","labour"],[],
 [("Share of people below the poverty line after housing costs","13.4% (over 3 million people)","2019-20 Census, ACOSS/UNSW","inequality","Senate Community Affairs References Committee, citing ACOSS and UNSW"),
  ("Share of children below the poverty line after housing costs","16.6% (over 760,000 children)","2019-20 Census, ACOSS/UNSW","inequality","Senate Community Affairs References Committee, citing ACOSS and UNSW"),
  ("Poverty line, single adult (50% of median income)","$489 a week (couple with two children $1,027)","2019-20","inequality","ACOSS/UNSW via Senate report"),
  ("Average poverty gap after housing costs","$304 a week","2019-20","inequality","ACOSS/UNSW via Senate report"),
  ("People lifted out of poverty by pandemic income support","646,000 (including 245,000 children)","2020","inequality","ACOSS/UNSW via Senate report"),
  ("People receiving income support payments","about 5 million (2.6 million on the Age Pension)","Sept 2022","inequality","Department of Social Services via Senate report")],
 [("Poverty line","A cut-off income below which a household is counted as poor; here half of median household income."),("Poverty gap","How far below the poverty line the average poor household's income falls."),("Income support","Government payments such as JobSeeker, the Age Pension and Youth Allowance.")],
 [("Outline what is meant by relative poverty, using the 50 per cent of median income measure.",2),("Explain how income support payments can reduce poverty.",4)],
 "Older item (published Feb 2024): figures are as at that date; check for newer data before quoting. Only the month is given, so the date is set to the first of the month. 206-page parliamentary report: poverty figures come from 2019-20 Census data cited via ACOSS and UNSW (chapter 1, paragraph 1.19), so check the original and newer ABS data before quoting.",
 "Report",206,dateText="February 2024",
 angle="Quote the 13.4 per cent and 16.6 per cent figures with 'after housing costs', then use the income support evidence to evaluate government redistribution.")

# 6 millionaire migration
rec(6,"2025-08-05-millionaire-migration-2025","Millionaire migration in 2025: projected net flows by country","2025-08-05","graph",
 ["Visual Capitalist","New World Wealth","Henley & Partners"],
 "A graph of where high-net-worth individuals are expected to move, showing how tax settings and residency rules can shift wealth and talent between economies.",
 "New World Wealth projects the UAE will gain 9.8 thousand millionaires in 2025 and the US 7.5 thousand, while the UK loses 16.5 thousand and China 7.8 thousand. Australia is projected to gain about 1.0 thousand.",
 (["1A.7"],[],[]),
 (["1A.4","3E.4"],["Y1d.5","Y3e.3"],[]),
 ["global","inequality"],["global"],["chart"],
 [("Projected net millionaire inflow, UAE","+9.8 thousand","2025 projection","global","New World Wealth via Visual Capitalist"),
  ("Projected net millionaire inflow, United States","+7.5 thousand","2025 projection","global","New World Wealth via Visual Capitalist"),
  ("Projected net millionaire inflow, Australia","+1.0 thousand","2025 projection","global","New World Wealth via Visual Capitalist"),
  ("Projected net millionaire outflow, United Kingdom","-16.5 thousand","2025 projection","global","New World Wealth via Visual Capitalist"),
  ("Projected net millionaire outflow, China","-7.8 thousand","2025 projection","global","New World Wealth via Visual Capitalist"),
  ("Projected net millionaire outflow, India","-3.5 thousand","2025 projection","global","New World Wealth via Visual Capitalist")],
 [("High-net-worth individual (millionaire)","A person with liquid investable wealth of US$1 million or more."),("Capital flight","Movement of money or wealthy people out of a country, often in response to tax or political settings.")],
 [("Explain one reason wealthy individuals may move to a different country.",2),("Discuss how tax policy could affect the movement of wealth between countries.",4)],
 "Older item (published 2025): figures are as at that date; check for newer data before quoting. No publication date appears on the graphic, so the file's modified date (5 Aug 2025) is used. Figures are projections (based on year-to-date movements) from New World Wealth, accessed via Henley & Partners, in a Visual Capitalist graphic; secondary source. Tagging is loose: it is not tied to one dot point.",
 "Original article",1,
 angle="A brief illustration of globalisation of people and capital, and a counterpoint to claims that higher taxes on the wealthy have no effect on behaviour.")

# 7 NAIRU
rec(7,"2021-04-29-treasury-estimating-the-nairu","Treasury working paper: Estimating the NAIRU in Australia","2021-04-29","report",
 ["The Treasury"],
 "Treasury's own estimate that unemployment consistent with stable inflation is about 4.75 per cent, which defines how much spare capacity exists in the labour market.",
 "The Treasury working paper (April 2021) re-estimates the NAIRU using a wage Phillips curve and finds it lay between 4.5 and 5 per cent in the years before the COVID-19 recession, with a point estimate of 4.75 per cent. It warns the NAIRU cannot be observed and estimates carry large confidence intervals.",
 (["3B.4","3C.3"],["Y1c.6","Y1b.11"],["P1e.5"]),
 (["3B.1","4I.2","3C.2"],["Y1b.9","Y2c.4","Y1c.4"],[]),
 ["employment","inflation"],["monetary","labour"],["phillips"],
 [("Treasury NAIRU estimate, point estimate","4.75%","Judgement for the years before COVID-19","employment","Treasury Working Paper 2021-01"),
  ("Treasury NAIRU estimate, range","4.5% to 5%","Five years before the COVID-19 recession","employment","Treasury Working Paper 2021-01"),
  ("Confidence interval around the NAIRU","plus or minus 0.5 points (0.75 at the endpoint)","68% interval","employment","Treasury Working Paper 2021-01"),
  ("Peak unemployment rate in the COVID-19 recession","7.5%","July 2020","employment","ABS via Treasury Working Paper"),
  ("Unemployment rate","5.6%","March 2021","employment","ABS via Treasury Working Paper")],
 [("NAIRU","The non-accelerating inflation rate of unemployment: the rate consistent with stable wage growth and inflation."),("Phillips curve","The relationship between inflation (or wage growth) and unemployment."),("Natural rate of unemployment","The medium to long-run rate reflecting frictional and structural unemployment.")],
 [("Outline what is meant by the NAIRU.",2),("Explain why the NAIRU is difficult to measure and what that means for policy.",4)],
 "Older item (published Apr 2021): figures are as at that date; check for newer data before quoting. Pre-dates the post-COVID inflation and labour market; the authors' views are not those of Treasury. Technical 43-page working paper, so use the abstract, introduction and conclusion for quotes.",
 "Report",43,
 angle="Use the 4.75 per cent estimate with the caveat that it is unobservable: when unemployment sits below it, wage and price pressure tend to rise.")

# 8 population map
rec(8,"2023-01-01-mccrindle-australia-population-map","Australia's population map and generational profile (McCrindle, 2023)","2023-01-01","stats",
 ["McCrindle","ABS"],
 "A snapshot of Australia's demographics (population, age, cities, workforce) that supports answers on ageing, participation and the size of the labour force.",
 "Australia's population is 26.3 million with a median age of 38, and Sydney and Melbourne are each above 5 million. The infographic also shows labour market figures (14 million employed, 3.5 per cent unemployment) and how each generation's share of the workforce is projected to change by 2033.",
 ([],["Y1b.4","Y1b.2"],[]),
 (["3A.5","3B.2"],["Y1a.15","Y1b.1"],["P3b.1"]),
 ["growth","employment"],[],["chart"],
 [("Total population","26.3 million (growth about 1% a year)","2023","growth","McCrindle, ABS"),
  ("Median age","38","2023","growth","McCrindle, ABS"),
  ("Total employed","14 million (9.6 million full time, 4.1 million part time)","2023","employment","McCrindle, ABS"),
  ("Unemployment rate","3.5%","2023","employment","McCrindle, ABS"),
  ("Population of Sydney","5.296 million (Melbourne 5.029 million)","2023","growth","McCrindle, ABS")],
 [("Dependency ratio","The number of people outside working age for every person of working age."),("Participation rate","The labour force as a share of the working-age population.")],
 [("Identify one economic effect of an ageing population.",2)],
 "Older item (published 2023): figures are as at that date; check for newer data before quoting. Only the year (2023) is given, so the date is set to 1 January. Dense infographic read from extracted text; check any specific number against the original before quoting. Secondary source drawing on ABS data.",
 "Data sheet",2,
 angle="Use for demographic context: a growing but ageing population affects labour supply, participation and public spending.")

# 9 Division 296
rec(9,"2025-08-04-division-296-microeconomic-reform","Division 296 super tax as a microeconomic reform case study","2025-08-04","case",
 ["Teacher notes (HSC Economics)"],
 "A ready-made case study applying the five economic objectives to a targeted tax reform on very large super balances.",
 "Division 296 applies an extra tax on earnings from super balances above $3 million, so earnings on that portion are taxed at 30 per cent instead of 15 per cent. The notes estimate it affects around 80,000 people (0.5 per cent of holders) and raises about $2.3 billion over four years, then assess its effects on growth, distribution, employment, price stability and the environment.",
 (["4E.1","4C.2","4A.6"],["Y2d.4","Y2b.10","Y2a.1"],["P5b.7"]),
 (["3E.3","4A.7","4I.5"],["Y1d.5","Y2d.5"],["P5b.6","P4a.3"]),
 ["budget","inequality"],["micro","fiscal"],[],
 [("Tax rate on earnings from super balances above $3 million","30% (standard concessional rate 15%)","From 1 July 2025","budget","Teacher notes, Division 296"),
  ("People affected","about 80,000 (0.5% of super holders)","Notes citing Treasury 2023","inequality","Teacher notes, Division 296"),
  ("Revenue expected over four years","about $2.3 billion","Treasury estimate as cited in the notes","budget","Teacher notes citing Treasury"),
  ("Super tax concessions a year","about $52 billion","Grattan Institute estimate as cited","budget","Teacher notes citing Grattan Institute"),
  ("Median super balance","$150,000 men, $130,000 women","APRA 2023 as cited","inequality","Teacher notes citing APRA")],
 [("Division 296","A tax on the earnings attributable to the part of a super balance above $3 million."),("Vertical equity","The principle that those with greater ability to pay should pay more tax."),("Microeconomic reform","Changes that alter incentives and the operation of markets to improve efficiency and equity.")],
 [("Explain how a higher tax on earnings of very large super balances may affect the distribution of income and wealth.",4),("Evaluate Division 296 as an example of microeconomic reform.",6)],
 "Older item (published Aug 2025): figures are as at that date; check for newer data before quoting. No date in the document, so the file's modified date (4 Aug 2025) is used. Teacher study notes, not an official source: the dollar figures are quoted from Treasury, Grattan, ABS and APRA as the notes cite them, and the policy details are as at mid-2025 and may have changed, so check the current legislated design before quoting.",
 "Teacher handout",2,
 angle="Use the five-objective structure to build an evaluation paragraph on a targeted reform, noting the equity benefit and the limited revenue.")

# 10 Ken Henry
rec(10,"2026-05-21-ken-henry-tax-reform-speech-article","Ken Henry's warning on tax reform, fairness and growth (student article)","2026-05-21","report",
 ["Teacher article (HSC Economics)","Dr Ken Henry (speech)"],
 "A long-form article on Australia's tax system that ties together incentives, intergenerational equity, housing, resource rents and carbon pricing for evaluation of tax policy.",
 "The article summarises a May 2026 speech by Dr Ken Henry arguing the tax system is 'more obviously broken' than at the time of the Henry Review, with too much reliance on personal income tax and favoured treatment of capital gains and resource rents. It uses reform history from the 1985 Tax Summit, the GST and the carbon price to explain why sound economics often fails politically.",
 (["4C.2","4E.1","4H.3"],["Y2b.10","Y2d.6","Y2b.14"],["P5b.6","P5b.7","P5b.5"]),
 (["3E.3","3F.2","4G.2"],["Y1d.5","Y1e.4","Y1e.5"],["P2h.3","P2i.2"]),
 ["budget","inequality","environment","productivity"],["fiscal","micro","environmental"],[],
 [("Top marginal personal income tax rate before the 1985 reforms","60%","1985","budget","Teacher article on Ken Henry speech"),
  ("GST rate when introduced","10%","1 July 2000","budget","Teacher article on Ken Henry speech"),
  ("Proposed GST rate in Fightback! package","15%","Early 1990s","budget","Teacher article on Ken Henry speech"),
  ("Capital gains tax discount for individuals","50% (for assets held over 12 months)","Since 1999","budget","Teacher article on Ken Henry speech"),
  ("Safeguard Mechanism threshold","facilities over 100,000 t CO2-e a year","May 2026","environment","Teacher article citing government sources")],
 [("Economic rent","A return above the normal return needed to keep a resource or factor in use."),("Incidence of a tax","Who actually bears the burden of a tax, not just who pays it legally."),("Intergenerational equity","Fairness between current and future generations."),("Excess burden","The loss of efficiency caused by a tax beyond the revenue it raises.")],
 [("Explain how the 50 per cent capital gains tax discount may affect investment decisions.",4),("Evaluate the economic and political difficulties of tax reform in Australia.",6)],
 "Teacher-prepared article summarising a speech (month stated as May 2026, day taken from the file's modified date); secondary source, so check the original speech before quoting Dr Henry directly. Policy details (for example Safeguard Mechanism) are as described in the article.",
 "Teacher handout",10,
 angle="Use the reform history to evaluate why tax changes face political limits, and the CGT and negative gearing discussion for equity and efficiency.",
 extended="Evaluate the effectiveness of tax reform as a tool for improving Australia's economic efficiency and equity.")
# 11 Reform aftershocks
rec(11,"2026-06-19-reform-aftershocks-budget-rollback","Reform aftershocks: how the 2026 federal Budget plans were rolled back","2026-06-19","case",
 ["Australian Financial Review (source pack)","Teacher zine (HSC Economics)"],
 "A case study of a microeconomic reform package that was softened under pressure, useful for weighing equity, dynamic efficiency and political feasibility.",
 "The classroom zine traces changes to the 2026 Budget tax package: concessions for small business, start-ups and testamentary trusts cost just $475 million over four years against an $8.1 billion revenue target. It also covers NDIS savings, a $3.6 billion childcare wage-subsidy extension, migration, housing, energy prices and bank resilience.",
 (["4E.1","4E.2","4C.2"],["Y2d.2","Y2d.4","Y2d.6"],["P5b.7","P5c.3"]),
 (["4H.3","3E.3","4E.3"],["Y2b.14","Y2d.3","Y1d.5"],["P2i.5","P5a.4"]),
 ["budget","housing","productivity"],["micro","fiscal"],["ds"],
 [("Revenue target of the capital gains, negative gearing and trust changes","$8.1 billion","Over forward estimates (AFR)","budget","AFR source pack"),
  ("Cost of concessions after the rollback","$475 million","Over four years","budget","AFR source pack"),
  ("Projected NDIS savings","$37.8 billion","Over four years","budget","Budget material cited in zine"),
  ("Childcare wage-subsidy extension","$3.6 billion (60,000 workers)","Added after the Budget","budget","AFR source pack"),
  ("Active-asset CGT relief turnover threshold","$10 million (was $2 million)","2026 revised package","budget","AFR source pack"),
  ("Start of CGT reform (discount replaced by CPI indexation)","1 July 2027","Budget material","budget","2026 Budget as cited in zine")],
 [("Dynamic efficiency","Improvement in productivity and innovation over time."),("Microeconomic reform","Policy changes that alter incentives and market operation to improve efficiency, productivity and competition."),("Testamentary trust","A trust set up under a will; the zine notes genuine ones were exempted from the 30% minimum tax floor.")],
 [("Explain how the CGT changes could affect incentives to invest in start-ups.",4),("Evaluate the extent to which the 2026 Budget rollback improved the design of microeconomic reform.",6)],
 "Classroom zine paraphrasing an AFR source pack and official Budget material; secondary source, check the Budget papers before quoting figures. No date in the document, so the file's modified date (19 Jun 2026) is used. Some policy details (for example the CGT start date) are as described in the zine.",
 "Teacher handout",15,
 angle="Use the policy trade-off lens (equity, fiscal sustainability, dynamic efficiency) to evaluate any reform that is later softened.")

# 12 age pension
rec(12,"2025-08-04-age-pension-to-self-funded-retirement","Age Pension means tests: from part pension to self-funded retirement","2025-08-04","stats",
 ["Teacher handout (HSC Economics)"],
 "The asset and income test thresholds that show how the Age Pension tapers and how the tax-transfer system targets support.",
 "The Age Pension is means tested, with the test giving the lower payment applying. The handout sets out the 1 July 2025 thresholds and shows that pension falls gradually through the assets and income tests until a retiree is self-funded.",
 (["3E.3"],["Y2b.10"],["P5c.1","P5a.4"]),
 (["4C.2","4I.5"],["Y1d.9","Y2b.11"],["P4a.3"]),
 ["budget","inequality"],["fiscal"],["compare"],
 [("Assets limit for full pension, single homeowner","$321,500 (part pension to $704,500)","1 July 2025","budget","Teacher handout"),
  ("Assets limit for full pension, single non-homeowner","$579,500 (part pension to $962,500)","1 July 2025","budget","Teacher handout"),
  ("Assets limit for full pension, homeowner couple","$481,500 combined (part pension to $1,059,000)","1 July 2025","budget","Teacher handout"),
  ("Income limit for full pension, single","$218 a fortnight (50c reduction per dollar above)","1 July 2025","budget","Teacher handout"),
  ("Pension reduction per $1,000 of assets over the limit","about $3 a fortnight","1 July 2025","budget","Teacher handout")],
 [("Means test","A test of income and assets used to decide eligibility for a payment."),("Transfer payment","A payment from government to households without a good or service being provided in return."),("Taper","A gradual reduction in a payment as income or assets rise.")],
 [("Explain how a means test targets government spending.",3)],
 "Older item (published Aug 2025): figures are as at that date; check for newer data before quoting. No date in the document, so the file's modified date (4 Aug 2025) is used. Teacher handout, not an official source: thresholds are as at 1 July 2025 and are indexed regularly, so check Services Australia before quoting.",
 "Teacher handout",1,
 angle="Use as a worked example of vertical equity and targeting in transfer payments, including the gradual taper.")

# 13 ample reserves
rec(13,"2025-04-02-rba-kent-ample-reserves-speech","RBA speech: monetary policy implementation and the move to ample reserves","2025-04-02","report",
 ["Reserve Bank of Australia"],
 "An RBA explanation of how the cash rate target is actually implemented through banks' reserves, which sits behind every 'RBA lowers the cash rate' headline.",
 "Assistant Governor Christopher Kent announced on 2 April 2025 that from 9 April the RBA would raise the price of new open market operation repos to 10 basis points above the cash rate target and add a seven-day term. He stressed these are operational changes, not a shift in the stance of monetary policy.",
 (["4D.2"],["Y2c.4"],["P4a.2"]),
 (["4D.1"],["Y2c.1","Y2c.6"],["P4c.3"]),
 ["rates"],["monetary"],["flow"],
 [("Reserves held by banks at the RBA","about $240 billion (down about $110 billion in a year)","Early 2025","rates","RBA (Christopher Kent)"),
  ("Price of new open market operation repos","10 basis points above the cash rate target (was 5)","From 9 April 2025","rates","RBA"),
  ("Activity at open market operations","about $7 billion a week (was about $3 billion)","2024 to early 2025","rates","RBA"),
  ("Estimated underlying demand for reserves","$100 billion to $200 billion","As at April 2025","rates","RBA")],
 [("Exchange Settlement balances (reserves)","Funds banks hold at the RBA to settle payments."),("Open market operations","The RBA's buying and selling of securities (repos) to influence the cash rate."),("Ample reserves","A system in which the RBA supplies as many reserves as banks demand at a price near the cash rate target.")],
 [("Outline how the RBA implements a change in the cash rate target.",3)],
 "Older item (published Apr 2025): figures are as at that date; check for newer data before quoting. Technical speech by an RBA official; useful for the implementation of monetary policy rather than for the transmission to the economy. Primary source.",
 "Report",7,
 angle="Use for the 'how' of implementation: the RBA sets the cash rate target and uses open market operations to keep the cash rate close to it.")

# 14 unconventional
rec(14,"2026-06-29-rba-additional-tools-framework-explainer","RBA's new framework for additional monetary policy tools: illustrated explainer","2026-06-29","report",
 ["Reserve Bank of Australia","Teacher explainer (HSC Economics)"],
 "A summary of how the RBA now plans to use unconventional monetary policy, including its own verdict on the pandemic-era tools, to evaluate effectiveness and limitations.",
 "Based on a 29 June 2026 speech and Q&A by Assistant Governor Christopher Kent, the explainer sets out four principles the RBA will apply before using additional tools and grades each of six tools. The pandemic term funding facility cost the RBA about $9 billion and bond purchases about $30 billion to date.",
 (["4D.2","4D.1"],["Y2c.6","Y2c.8","Y2c.7"],[]),
 (["4H.1","4I.3"],["Y2c.1","Y2c.3","Y2c.4"],["P4a.2"]),
 ["rates"],["monetary"],["flow"],
 [("Cost to the RBA of the Term Funding Facility","about $9 billion","As rates rose after the pandemic","rates","RBA (Kent), 29 June 2026"),
  ("Cost of the bond purchase program","about $30 billion","To date (June 2026)","rates","RBA (Kent), 29 June 2026"),
  ("Bond purchases in the first phase of the pandemic","about $40 billion","March to May 2020","rates","RBA (Kent), 29 June 2026"),
  ("Neutral cash rate mentioned by a questioner","about 3.6%","June 2026","rates","RBA Q&A, 29 June 2026"),
  ("Typical recession rate cut mentioned in the Q&A","about 400 basis points","June 2026","rates","RBA Q&A, 29 June 2026")],
 [("Unconventional monetary policy","Tools used when the cash rate is at or near its lower bound, such as bond purchases, term funding and forward guidance."),("Effective lower bound","The level near zero below which cutting the policy rate is no longer effective."),("Quantitative easing","Central bank purchases of government bonds to lower longer-term interest rates.")],
 [("Explain why a central bank might use unconventional monetary policy.",3),("Evaluate the effectiveness of unconventional monetary policy in Australia during the pandemic.",6)],
 "Teacher explainer based on an RBA speech and Q&A; the date used is the speech date (29 June 2026) and the file was last modified in July 2026. Secondary source; the risk and effectiveness heat-map is the explainer's own illustrative synthesis, not an RBA table. Check the RBA transcript before quoting.",
 "Teacher handout",8,
 angle="The cash rate is the first-choice tool; use the verdicts on each additional tool to support a balanced evaluation of its limits.")

# 15 IMF
rec(15,"2025-05-04-imf-gdp-growth-forecasts-2025","IMF real GDP growth projections for 2025, January versus April","2025-05-04","graph",
 ["Visual Capitalist","IMF"],
 "A graph showing how quickly the IMF downgraded 2025 growth forecasts amid tariffs and uncertainty, with country-by-country changes to quote.",
 "The IMF cut its 2025 world growth forecast from 3.3 per cent in January to 2.8 per cent in April, with the largest downgrades for Mexico (1.7 points) and the US (0.9 points). Russia was the only economy in the chart upgraded.",
 (["1A.2","1A.8"],["Y3e.3","Y3a.15"],[]),
 (["1B.2","3D.3"],["Y3b.4","Y3e.1"],["P6a.1"]),
 ["growth","global","trade"],["trade","global"],["chart","compare"],
 [("World real GDP growth forecast for 2025","2.8% (January forecast 3.3%)","IMF April 2025 WEO","growth","IMF via Visual Capitalist"),
  ("US growth forecast for 2025","1.8% (January 2.7%)","IMF April 2025 WEO","growth","IMF via Visual Capitalist"),
  ("China growth forecast for 2025","4.0% (January 4.6%)","IMF April 2025 WEO","growth","IMF via Visual Capitalist"),
  ("Euro area growth forecast for 2025","0.8% (January 1.0%)","IMF April 2025 WEO","growth","IMF via Visual Capitalist"),
  ("Japan growth forecast for 2025","0.6% (January 1.1%)","IMF April 2025 WEO","growth","IMF via Visual Capitalist"),
  ("Mexico growth forecast for 2025","-0.3% (January 1.4%)","IMF April 2025 WEO","growth","IMF via Visual Capitalist")],
 [("Gross world product","The total output of all economies in the world."),("Protectionism","Policies such as tariffs that restrict imports to protect domestic industry.")],
 [("Using the graph, describe the change in the IMF's forecast for world growth.",2),("Explain how tariffs could slow global economic growth.",4)],
 "Older item (published Apr 2025): figures are as at that date; check for newer data before quoting. The IMF has since revised these forecasts. No publication date on the graphic, so the file's modified date (4 May 2025) is used. Visual Capitalist graphic of IMF World Economic Outlook projections (January and April 2025); secondary source.",
 "Original article",1,
 angle="Use as quick evidence of a global slowdown caused by tariffs and uncertainty, then link to Australia's exports.")

# 16 financial markets
rec(16,"2025-05-25-world-financial-markets-graphics","World financial markets: centres, shareholders, exchanges and companies","2025-05-25","graph",
 ["Visual Capitalist","Z/Yen Group","HelloSafe","World Federation of Exchanges","BestBrokers"],
 "A set of five graphics on global financial centres, stock market participation and the biggest companies, with Australian comparisons to cite on financial markets.",
 "The graphics show New York, London, Hong Kong and Singapore as the top four financial centres, with Melbourne ranked 28th and Sydney 30th. Australia has 37 per cent of its population holding shares, the third highest among the countries shown, and 143 billion-dollar public companies.",
 (["1A.4","1A.5"],[],["P4b.1"]),
 (["1B.1"],["Y3b.1","Y3b.3"],["P4b.2","P4a.1"]),
 ["global","investment"],[],["chart"],
 [("Australia's stock market participation rate","37% (9.6 million shareholders; US 55%)","Latest 2023-24 figures, published April 2025","investment","HelloSafe via Visual Capitalist"),
  ("Billion-dollar public companies, United States","1,873","2025","investment","BestBrokers via Visual Capitalist"),
  ("Billion-dollar public companies, Australia","143 (China 216)","2025","investment","BestBrokers via Visual Capitalist"),
  ("Global Financial Centres Index rank, Melbourne","28 (Sydney 30)","March 2025, GFCI 37","investment","Z/Yen Group via Visual Capitalist"),
  ("Global Financial Centres Index rank, top three","New York 1, London 2, Hong Kong 3","March 2025, GFCI 37","investment","Z/Yen Group via Visual Capitalist")],
 [("Equity market","A market in which shares in companies are issued and traded."),("Market capitalisation","The total market value of a company's shares."),("Financial centre","A city where financial services and markets are concentrated.")],
 [("Identify two features of an equity market.",2)],
 "Older item (published May 2025): figures are as at that date; check for newer data before quoting. Compilation of five Visual Capitalist graphics, with no single publication date, so the file's modified date (25 May 2025) is used. Secondary source; the stock exchange and most-valuable-company graphics were not quoted. Tagging is loose.",
 "Original article",5,
 angle="Use the participation rate to show how widely Australians invest in equity markets, and the centres ranking for the global financial system.")

# 17 Budget speech
rec(17,"2025-03-25-budget-speech-2025-26","Treasurer's 2025-26 Budget Speech","2025-03-25","report",
 ["Treasury Ministers (Dr Jim Chalmers)"],
 "The government's own account of the 2025-26 Budget, showing its forecasts, its fiscal stance and the cost-of-living package in the Treasurer's words.",
 "Treasurer Jim Chalmers told Parliament on 25 March 2025 that inflation is down, unemployment is low and growth is picking up, with a $42 billion deficit forecast for 2025-26. The Budget includes $17 billion of new tax cuts, $1.8 billion more energy bill relief and a $33 billion plan to build 1.2 million homes.",
 (["4C.1","4C.2"],["Y2b.2","Y2b.3","Y2b.10"],["P5a.4","P5c.2"]),
 (["4A.7","4I.3","3A.7"],["Y2b.9","Y2b.12","Y1a.15"],["P5b.2"]),
 ["budget","growth","inflation"],["fiscal"],[],
 [("Forecast deficit next year","$42 billion","2025-26 Budget","budget","Treasurer's Budget Speech"),
  ("Gross debt","$940 billion","This financial year, 2024-25","budget","Treasurer's Budget Speech"),
  ("New tax cuts for taxpayers","$17 billion","2025-26 Budget","budget","Treasurer's Budget Speech"),
  ("Forecast economic growth","1.5% this year, rising to 2.5% in 2026-27","2025-26 Budget","growth","Treasurer's Budget Speech"),
  ("Projected peak unemployment rate","4.25%","2025-26 Budget","employment","Treasurer's Budget Speech"),
  ("Treasury global growth forecast","3.25% a year for 3 years","2025-26 Budget","global","Treasurer's Budget Speech")],
 [("Fiscal stance","Whether the Budget is expansionary, contractionary or neutral."),("Soft landing","Bringing inflation down without a sharp rise in unemployment."),("Cost-of-living relief","Budget measures that reduce household costs, such as tax cuts and energy rebates.")],
 [("Outline one way the 2025-26 Budget supports household incomes.",2),("Explain what a deficit of $42 billion suggests about the fiscal stance.",3)],
 "Older item (published Mar 2025): figures are as at that date; check for newer data before quoting. Primary source from the Treasurer's website, but a political speech: figures are forecasts, and later Budgets have revised them.",
 "Report",20,
 angle="Compare the government's framing with an independent analysis such as the Deloitte report.",
 links=[("Treasury Ministers, 2025-26 Budget Speech, 25 Mar 2025","https://ministers.treasury.gov.au/ministers/jim-chalmers-2022/speeches/2025-26-budget-speech-parliament-house-canberra")])

# 18 Deloitte
rec(18,"2025-03-25-deloitte-federal-budget-2025-26-report","Federal Budget 2025-26: A platform for the next election (Deloitte)","2025-03-25","report",
 ["Deloitte Access Economics"],
 "An independent professional analysis that gives the Budget deficits and debt in more than one measure, useful for a critical view of fiscal sustainability.",
 "Deloitte says the underlying cash deficit is forecast at $27.6 billion (1.0 per cent of GDP) in 2024-25 but off-budget spending takes the headline deficit to $46.7 billion (1.7 per cent). It argues government spending has become the driver of growth and the medium-term outlook is getting worse, with net debt rising to 23.1 per cent of GDP in 2028-29.",
 (["4C.1","4C.2","4C.3"],["Y2b.2","Y2b.5","Y2b.12"],["P5a.4"]),
 (["4H.3","4A.7"],["Y2b.14","Y2b.3"],["P5b.2","P5c.2"]),
 ["budget","growth"],["fiscal"],[],
 [("Underlying cash deficit","$27.6 billion (1.0% of GDP)","2024-25 forecast","budget","Deloitte Access Economics"),
  ("Headline cash deficit including off-budget spending","$46.7 billion (1.7% of GDP)","2024-25 forecast","budget","Deloitte Access Economics"),
  ("Fiscal balance deficit","$50.6 billion (1.8% of GDP)","2024-25 forecast","budget","Deloitte Access Economics"),
  ("Net debt","23.1% of GDP (19.9% in 2024-25)","2028-29 projection","budget","Deloitte Access Economics"),
  ("Lowest marginal tax rate","14% (was 16%)","Over two years from 1 July 2026","budget","Deloitte Access Economics"),
  ("Average-earner tax cut","$536 a year (from 2027-28)","Compared with 2024-25 tax settings","budget","Deloitte Access Economics")],
 [("Underlying cash balance","Receipts minus payments, excluding one-off items."),("Off-budget spending","Spending that is not counted in the headline Budget deficit."),("Structural deficit","The deficit that remains when the economy is at its normal level of activity.")],
 [("Explain why the underlying cash deficit may understate the true fiscal position.",3),("Assess the sustainability of the government's fiscal position using the data in the report.",6)],
 "Older item (published Mar 2025): figures are as at that date; check for newer data before quoting. Analysis by a private firm, and the document includes opinion; forecasts have been revised by later Budget updates.",
 "Report",16,
 angle="Use to show that headline deficits can hide off-budget spending, then assess sustainability using the debt projections.")

import json,subprocess,os
base=os.path.expanduser("~/mnt/2009 Resources/")
man=json.load(open("build/_batches/manifest6.json"))
for r in R:
    i=r.pop("_i")
    src=base+man[i]["path"]
    d=os.path.dirname(r["file"]["path"])
    os.makedirs(d,exist_ok=True)
    subprocess.run(["cp",src,r["file"]["path"]],check=True)
json.dump(R,open("build/_batches/batch6.json","w"),ensure_ascii=False,indent=1)
print(len(R),[r["id"] for r in R])
