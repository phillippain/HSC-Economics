def make(B):
    c, cd = "#d9822b", "#a85a12"
    ed = B.ed
    m = "&minus;"
    text = (
    "<h3>Income and wealth</h3>"
    "<p><b>Income</b> is a flow: what a household earns over a period from wages, business profits, rent, interest, dividends and government payments. <b>Wealth</b> (net worth) is a stock: the value of a household's assets, such as housing, superannuation, shares and savings, minus its debts. The distribution of each shows how they are shared across households.</p>"
    "<h3>Measuring the distribution</h3>"
    "<p>The <b>Lorenz curve</b> plots the cumulative share of income (or wealth) against the cumulative share of households, ranked from poorest to richest (Figure 3). If every household had the same income the curve would follow the line of equality. The more it bows away from that line, the less equal the distribution.</p>"
    "<p>The <b>Gini coefficient</b> summarises the curve as a single number: Gini = A &divide; (A + B), where A is the area between the line of equality and the Lorenz curve and B is the area below the Lorenz curve. It runs from 0 (perfect equality) to 1 (one household has everything). A rising Gini means greater inequality.</p>"
    "<p>The Australian Bureau of Statistics (ABS) found in its 2019&ndash;20 Survey of Income and Housing that the Gini coefficient for equivalised disposable household income was 0.324, and the Gini for household net worth was 0.611 (Figure 2). Wealth is always more unequally distributed than income. ABS data from other sources put the income Gini at 0.307 and the wealth Gini at 0.606 in 2022&ndash;23. The ABS wealth and income survey has not been updated since 2019&ndash;20, so the quintile figures below come from that survey.</p>"
    "<h3>Income</h3>"
    "<ul><li><b>Wages and salaries</b> are the main source of income for most households.</li>"
    "<li><b>Income from capital</b> (rent, interest, dividends and profits) is more important for higher income and older households.</li>"
    "<li><b>Government payments</b> (pensions, family payments and unemployment benefits) are the main source for lower income households.</li></ul>"
    "<p>In 2019&ndash;20 the highest 20 per cent of households had a disposable income of $4,306 a week, about twice that of the middle 20 per cent ($1,989) and over five times that of the lowest 20 per cent ($794) (Figure 4).</p>"
    "<h3>Wealth</h3>"
    "<p>Wealth is far more concentrated than income. In the ABS surveys the wealthiest 20 per cent of households hold about 62 per cent of all household wealth, while the lowest 20 per cent hold less than 1 per cent. The main sources of wealth are the family home, superannuation, investment property and shares. Rising house prices have increased the wealth of owners and raised the barrier for those trying to buy.</p>"
    "<h3>Government redistribution</h3>"
    "<ul><li><b>Progressive income tax:</b> the rate rises with income, so high earners pay a larger share of income in tax (Figure 5). For 2026&ndash;27 the rates are 15 per cent on $18,201 to $45,000, 30 per cent to $135,000, 37 per cent to $190,000 and 45 per cent above that, with the first $18,200 tax free.</li>"
    "<li><b>Transfer payments:</b> cash payments such as the Age Pension, JobSeeker and Family Tax Benefit are means tested, so they go to lower income households.</li>"
    "<li><b>The social wage:</b> government-provided services such as Medicare, public schools and subsidised child care give benefits in kind to all households and are worth more to low income households as a share of income.</li></ul>"
    "<p>A report by the Australian Council of Social Service and the University of NSW released in 2026 found that social security payments and income tax together reduce income inequality by about a third.</p>"
    "<h3>Dimensions of inequality</h3>"
    "<ul><li><b>Gender:</b> the gender pay gap for full-time adults was 11.3 per cent in May 2026, the lowest on record. Men earned $2,181.00 a week on average and women $1,934.50. When part-time work is included the gap is much larger, and women retire with lower superannuation balances.</li>"
    "<li><b>Age:</b> wealth rises with age as people repay mortgages and build super, so older households hold the most wealth. Younger households face high housing costs.</li>"
    "<li><b>Occupation:</b> pay differs between occupations and industries, because of skills, qualifications and the level of union coverage.</li>"
    "<li><b>Ethnic background:</b> Aboriginal and Torres Strait Islander people have lower average incomes and wealth than other Australians, because of gaps in education, health, employment and location. Some migrant groups face barriers such as language and unrecognised qualifications.</li>"
    "<li><b>Family structure:</b> single-parent families, most of them headed by women, face the highest risk of poverty, while couples with two incomes and no children have the highest income.</li></ul>"
    "<h3>Costs and benefits of inequality</h3>"
    "<p><b>Benefits</b></p>"
    "<ul><li>Differences in reward give people an incentive to work, save, invest and take risks, which supports growth.</li>"
    "<li>Higher rewards for skills encourage people to undertake education and training.</li></ul>"
    "<p><b>Costs</b></p>"
    "<ul><li><b>Lower consumption and aggregate demand:</b> low income households spend a larger share of any extra income than high income households, so a more equal distribution tends to raise consumption.</li>"
    "<li><b>Lost human capital:</b> poverty limits access to education and health, so potential output is not reached.</li>"
    "<li><b>Poverty and social cohesion:</b> high inequality is linked to poorer health, crime and weaker trust in society.</li>"
    "<li><b>Housing and generational gaps:</b> wealth passes between generations, so inequality of opportunity can persist.</li></ul>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Economic growth:</b> growth raises average income but does not guarantee it is shared.</li>"
    "<li><b>Unemployment:</b> job loss is a leading cause of low income.</li>"
    "<li><b>Fiscal policy:</b> tax and transfers are the main tools for redistribution, and the budget must balance equity against efficiency.</li></ul>"
    "<p><b>Use it in an exam:</b> state the Gini coefficient and what it measures, use the quintile shares, name the group affected, and explain the trade-off between the incentive benefits and the social costs of inequality.</p>"
    "<p>Sources: <a href=\"https://www.abs.gov.au/media-centre/media-releases/stable-household-income-and-wealth-inequality-leading-pandemic\">ABS, Household Income and Wealth, Australia, 2019&ndash;20</a>; <a href=\"https://www.abs.gov.au/statistics/measuring-what-matters/measuring-what-matters-themes-and-indicators/prosperous/income-and-wealth-inequality\">ABS, Measuring What Matters, income and wealth inequality</a>; <a href=\"https://www.abs.gov.au/media-centre/media-releases/average-weekly-earnings-growth-lowest-2022\">ABS, Average Weekly Earnings, May 2026</a>; <a href=\"https://povertyandinequality.acoss.org.au/\">ACOSS and UNSW, Poverty and Inequality in Australia</a>; <a href=\"https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents\">Australian Taxation Office</a>.</p>")
    tiles = ('<div class="k"><div><b>0.324</b><i>Income Gini</i><u>2019&ndash;20, ABS</u></div><div><b>0.611</b><i>Wealth Gini</i><u>2019&ndash;20, ABS</u></div>'
             '<div><b>11.3%</b><i>Gender pay gap</i><u>Full-time adults, May 2026</u></div><div><b>62%</b><i>of wealth held by top 20%</i><u>ABS household surveys</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "Wealth is far less equal than income (Gini coefficient)", B.bars2([("2019–20", 0.324, 0.611), ("2022–23", 0.307, 0.606)], ("Income", "Wealth"), fmt="%.3f"), "Income is equivalised disposable household income. Source: ABS."),
      B.fig(3, "The Lorenz curve and Gini coefficient", ed.lorenz(ed.TOPIC[3], second=True).svg(), "The amber Lorenz curve lies below the line of equality. The red curve (L<sub>2</sub>) is further away, so area A is larger and the Gini coefficient is higher. Not to scale."),
      B.fig(4, "Disposable income per week, 2019–20 ($)", B.bars([("Lowest 20%", 794), ("Middle 20%", 1989), ("Highest 20%", 4306)], fmt="$%.0f"), "Equivalised disposable household income. Source: ABS, as reported by ACOSS."),
      B.fig(5, "Income tax rates, 2026–27", B.table(["Taxable income", "Rate"], [["$0 &ndash; $18,200", "Nil"], ["$18,201 &ndash; $45,000", "15%"], ["$45,001 &ndash; $135,000", "30%"], ["$135,001 &ndash; $190,000", "37%"], ["Over $190,000", "45%"]]) + "<small>Plus the 2% Medicare levy. A higher rate on higher income makes the system <b>progressive</b>.</small>", "Source: Australian Taxation Office."),
      B.fig(6, "Worked example: finding the Gini coefficient", B.table(["Item", "Value"], [["Area A (between the two lines)", "20"], ["Area B (below the Lorenz curve)", "30"], ["<b>Gini = A &divide; (A + B)</b>", "<b>20 &divide; 50 = 0.40</b>"]]), "Made-up figures for practice."),
      B.fig(7, "Gender pay gap, full-time adults, May 2026", B.bars([("Men", 2181.0), ("Women", 1934.5)], fmt="$%.2f"), "Average weekly ordinary time earnings. The gap is 11.3%. Source: ABS."),
      B.fig(8, "Equity and efficiency", B.table(["Benefit of inequality", "Cost of inequality"], [["Incentive to work and invest", "Lower consumption and demand"], ["Rewards skills and effort", "Lost human capital"], ["Supports growth", "Poverty and weak social cohesion"]]), ""),
      B.tools([("calc", "Practise Gini and Lorenz calculations"), ("glance", "Latest wages and income figures"), ("policy", "Use tax and transfers to change inequality"), ("chain", "Build the chain from inequality to demand"),
               ("qf", "Past HSC questions on distribution"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence on inequality"), ("gloss", "Gini coefficient, progressive tax and more")]),
    ]
    B.build("distribution-of-income-wealth", c, cd, text, figs, "")
