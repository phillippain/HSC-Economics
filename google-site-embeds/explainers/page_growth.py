def make(B):
    c, cd = "#d9822b", "#a85a12"
    ed = B.ed
    text = (
    "<h3>What economic growth is</h3>"
    "<p>Economic growth is an increase in the volume of goods and services an economy produces over time. It is measured by the percentage change in real gross domestic product (GDP). Real GDP removes the effect of inflation, so it shows the change in output and not the change in prices.</p>"
    "<p><b>Growth rate = (real GDP this year &minus; real GDP last year) &divide; real GDP last year &times; 100</b></p>"
    "<p>If real GDP rises from $2,500 billion to $2,560 billion, growth is 60 &divide; 2,500 &times; 100 = 2.4 per cent. GDP per person is a better guide to living standards, because it allows for population growth.</p>"
    "<h3>Aggregate demand and its components</h3>"
    "<p>In the short run, growth depends on aggregate demand (AD), the total spending on Australian goods and services:</p>"
    "<p><b>AD = C + I + G + (X &minus; M)</b></p>"
    "<ul><li><b>Consumption (C):</b> household spending, about half of GDP. It depends on income, interest rates, wealth and confidence.</li>"
    "<li><b>Investment (I):</b> business spending on capital. It is the most volatile component and depends on interest rates and expected profits.</li>"
    "<li><b>Government spending (G):</b> spending by all levels of government on goods and services.</li>"
    "<li><b>Net exports (X &minus; M):</b> export income minus import spending. It depends on world growth, commodity prices and the exchange rate.</li></ul>"
    "<h3>Injections, withdrawals and equilibrium</h3>"
    "<p>In the circular flow of income, <b>injections</b> add spending to the economy: investment (I), government spending (G) and exports (X). <b>Withdrawals</b> (leakages) remove it: saving (S), taxation (T) and imports (M). The economy is in equilibrium when:</p>"
    "<p><b>S + T + M = I + G + X</b></p>"
    "<p>If injections are greater than withdrawals, income and output rise. If withdrawals are greater, they fall.</p>"
    "<h3>The simple multiplier</h3>"
    "<p>A rise in spending raises national income by more than the first amount, because one person's spending becomes another person's income, and part of it is spent again (Figure 6). The size of this effect depends on the marginal propensity to consume (MPC), the share of each extra dollar of income that is spent. The share that is saved is the marginal propensity to save (MPS), and MPC + MPS = 1.</p>"
    "<p><b>Multiplier (k) = 1 &divide; (1 &minus; MPC) = 1 &divide; MPS</b></p>"
    "<p>If the MPC is 0.8, k = 1 &divide; 0.2 = 5. A $10 billion rise in investment then raises national income by 5 &times; 10 = $50 billion. A higher MPC gives a larger multiplier.</p>"
    "<h3>Aggregate supply and long-run growth</h3>"
    "<p>Demand can only raise output up to the economy's capacity. Sustained growth needs an increase in aggregate supply, the economy's ability to produce (Figure 4). The sources are:</p>"
    "<ul><li><b>More resources:</b> a larger labour force through population growth and participation, and more capital through investment.</li>"
    "<li><b>Higher productivity:</b> more output from each hour worked. It comes from better technology, skills and education, infrastructure and more efficient use of resources. Microeconomic reform aims to lift it.</li></ul>"
    "<h3>Recent trends and the business cycle</h3>"
    "<p>Growth moves in a cycle of upswings and downswings around its long-term trend. Australia went almost 30 years without a recession before the pandemic in 2020.</p>"
    "<p>Growth slowed to about 1 per cent in 2024 as high interest rates held back household spending. It recovered to 2.6 per cent by the end of 2025 as rates were cut and real incomes rose. It has slowed again in 2026, to 2.1 per cent over the year to June, as inflation and interest rates rose (Figure 2). In the June quarter GDP grew 0.4 per cent. Private investment was the fastest growing part of demand over the year, up 8.4 per cent.</p>"
    "<p>Two weaknesses stand out. GDP per person grew only 0.7 per cent over the year, because much of the growth came from a larger population. Productivity fell 0.2 per cent, which limits growth in real wages.</p>"
    "<h3>Effects of economic growth</h3>"
    "<ul><li><b>Living standards:</b> higher real incomes and more goods and services per person.</li>"
    "<li><b>Employment:</b> more output needs more workers, so unemployment falls.</li>"
    "<li><b>Government budget:</b> tax revenue rises and welfare spending falls.</li>"
    "<li><b>Inflation:</b> if demand grows faster than capacity, prices rise (Figure 3).</li>"
    "<li><b>External stability:</b> strong growth draws in imports and can widen the current account deficit.</li>"
    "<li><b>Income distribution:</b> the gains are not shared evenly, so inequality can widen.</li>"
    "<li><b>Environment:</b> more production can mean more pollution and faster use of resources.</li></ul>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Unemployment:</b> growth must be fast enough to absorb a growing labour force and rising productivity.</li>"
    "<li><b>Inflation:</b> growth above the economy's capacity causes demand inflation.</li>"
    "<li><b>Economic policy:</b> fiscal and monetary policy manage aggregate demand. Microeconomic policy lifts aggregate supply.</li></ul>"
    "<p><b>Use it in an exam:</b> quote the latest growth rate, name the component of aggregate demand that changed, use the multiplier to show the full effect, and draw an aggregate demand and supply diagram. Then weigh the benefits of growth against its costs.</p>"
    "<p>Sources: <a href=\"https://www.abs.gov.au/statistics/economy/national-accounts/australian-national-accounts-national-income-expenditure-and-product/latest-release\">ABS, Australian National Accounts, June 2026</a>; <a href=\"https://www.rba.gov.au/\">Reserve Bank of Australia</a>.</p>")
    tiles, js = B.live([("gdp", "GDP growth over the year", "2.1%", "Jun qtr 2026"), ("prod", "Productivity (GDP per hour worked)", "−0.2%", "Year to Jun qtr 2026"),
                        ("saving", "Household saving ratio", "6.5%", "Jun qtr 2026"), ("popn", "Population growth", "1.4%", "Year to Mar 2026")])
    pts = [("Jun 2024", 0, 0.9), ("", 1, 0.8), ("", 2, 1.2), ("", 3, 1.3), ("Jun 2025", 4, 1.9), ("", 5, 2.1), ("Dec 2025", 6, 2.6), ("", 7, 2.5), ("Jun 2026", 8, 2.1)]
    figs = [
      B.fig(1, "Latest figures", tiles, "These update by themselves from Economy at a Glance."),
      B.fig(2, "Real GDP growth over the year, 2024 to 2026 (%)", B.linechart(pts, c, 4), "Each point is growth over the year to that quarter. Source: ABS."),
      B.fig(3, "Higher aggregate demand: more output, higher prices", ed.ad_as("AD right", ed.TOPIC[3]).svg(), "AD<sub>1</sub> to AD<sub>2</sub> raises output from Y<sub>1</sub> to Y<sub>2</sub> and the price level from P<sub>1</sub> to P<sub>2</sub>. Not to scale."),
      B.fig(4, "Higher aggregate supply: growth without inflation", ed.lras_growth(ed.TOPIC[3]).svg(), "When capacity grows from LRAS<sub>1</sub> to LRAS<sub>2</sub>, output can rise from Y<sub>1</sub> to Y<sub>2</sub> without the same pressure on prices. Not to scale."),
      B.fig(5, "Growth in spending, year to June quarter 2026 (%)", B.bars([("Private investment", 8.4), ("Public investment", 2.4), ("Government spending", 2.0), ("Household consumption", 1.8)], fmt="%.1f"), "Real GDP grew 2.1% over the same period. Source: ABS."),
      B.fig(6, "How the multiplier works", B.chain(["Firms invest an extra $10 billion", "Workers and suppliers earn $10 billion more", "With an MPC of 0.8 they spend $8 billion of it", "That spending is income for others, who spend $6.4 billion", "The rounds continue, each smaller than the last", "National income rises by $50 billion in total"])),
      B.fig(7, "Multiplier values", B.table(["MPC", "MPS", "Multiplier"], [["0.5", "0.5", "2"], ["0.6", "0.4", "2.5"], ["0.75", "0.25", "4"], ["0.8", "0.2", "5"], ["0.9", "0.1", "10"]])),
      B.fig(8, "Benefits and costs of growth", B.table(["Benefits", "Costs"], [["Higher real incomes", "Inflation if demand outruns capacity"], ["More jobs, lower unemployment", "Imports rise, widening the current account deficit"], ["Higher tax revenue", "Gains are shared unevenly"], ["More to spend on services", "Pollution and resource depletion"]])),
      B.tools([("macro", "Shift AD and AS and see growth"), ("calc", "Practise growth and multiplier sums"), ("glance", "Latest GDP and productivity"), ("chain", "Build the multiplier chain"),
               ("policy", "Use policy to manage growth"), ("qf", "Past HSC questions on growth"), ("mcq", "Section I questions with explanations"), ("gloss", "Multiplier, MPC, real GDP and more")]),
    ]
    B.build("economic-growth", c, cd, text, figs, js)
