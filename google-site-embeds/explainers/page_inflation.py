def make(B):
    c, cd = "#d9822b", "#a85a12"   # Topic 3 amber; darker shade for text
    T = B.tool
    text = (
    "<h3>What inflation is</h3>"
    "<p>Inflation is a sustained increase in the general level of prices in an economy. It means that each dollar buys fewer goods and services than before, so the purchasing power of money falls. Inflation is not a rise in the price of one good. It is a rise in the average price of the many goods and services that households buy. A fall in the general price level is called deflation. A fall in the rate of inflation, where prices still rise but more slowly, is called disinflation.</p>"
    "<h3>How inflation is measured</h3>"
    "<p>The Australian Bureau of Statistics (ABS) measures inflation with the Consumer Price Index (CPI). The CPI tracks the price of a fixed basket of goods and services bought by households in the capital cities. Each item is weighted by its share of household spending, so a rise in rent affects the index more than a rise in the price of pepper. The ABS has published a full monthly CPI since late 2025.</p>"
    "<p>The inflation rate is the percentage change in the CPI over a year:</p>"
    "<p><b>Inflation rate = (CPI this year &minus; CPI last year) &divide; CPI last year &times; 100</b></p>"
    "<p>If the CPI rises from 140.0 to 146.0, inflation is 6.0 &divide; 140.0 &times; 100 = 4.3 per cent.</p>"
    "<ul><li><b>Headline inflation</b> is the change in the whole CPI. It includes every item, so one-off price changes such as a jump in petrol prices can move it sharply.</li>"
    "<li><b>Underlying inflation</b> removes the most volatile price changes to show the trend. The main measure is the trimmed mean, which leaves out the items with the largest price rises and falls. The Reserve Bank of Australia (RBA) watches underlying inflation closely when it sets the cash rate.</li></ul>"
    "<p>The RBA's inflation target is 2 to 3 per cent a year, and it aims for the middle of that range. Figure 1 shows the latest readings.</p>"
    "<h3>Recent trends</h3>"
    "<p>Inflation was below the target band for several years before 2020. It then rose quickly after the pandemic, as supply chains were disrupted, government stimulus lifted spending and energy prices jumped. It peaked at 7.8 per cent at the end of 2022, the highest rate in more than 30 years. The RBA raised the cash rate 13 times and inflation fell back into the target band by late 2024.</p>"
    "<p>Inflation has risen again since mid-2025. In the year to September 2026 the CPI rose 4.3 per cent and the trimmed mean rose 3.6 per cent. Housing was the largest contributor, up 5.2 per cent, and transport costs rose 8.7 per cent as fuel prices climbed. The RBA has responded by raising the cash rate five times in 2026 (Figure 2).</p>"
    "<h3>Causes of inflation</h3>"
    "<ul><li><b>Demand inflation (demand-pull):</b> aggregate demand grows faster than the economy's capacity to produce. With the economy near full employment, firms cannot raise output easily, so they raise prices. Strong consumer spending, government spending or export income can all cause it. In Figure 3, aggregate demand shifts right and the price level rises.</li>"
    "<li><b>Cost inflation (cost-push):</b> the costs of production rise and firms pass them on as higher prices. Causes include wage rises that are larger than productivity growth, and higher prices for inputs such as energy. In Figure 4, aggregate supply shifts left. Prices rise while output falls, which is the worst mix for policy makers.</li>"
    "<li><b>Imported inflation:</b> the prices of imports rise. This happens when world prices rise, as with oil, or when the Australian dollar depreciates and makes every import dearer. Figure 5 traces the chain.</li>"
    "<li><b>Inflationary expectations:</b> if people expect prices to rise, they act in ways that make it happen. Workers ask for higher wages and firms raise prices in advance. This can create a wage-price spiral that keeps inflation high after the first cause has passed.</li></ul>"
    "<h3>Effects of inflation</h3>"
    "<p>Low and stable inflation is healthy. High or unpredictable inflation is costly, and the costs fall unevenly (Figure 6).</p>"
    "<p><b>Negative effects of high inflation</b></p>"
    "<ul><li><b>Lower real incomes:</b> if wages rise more slowly than prices, real wages fall. In mid-2026 wages were growing by 3.2 per cent while prices rose faster, so living standards were falling for many workers.</li>"
    "<li><b>Loss of international competitiveness:</b> if Australia's inflation is higher than its trading partners', exports become dearer and imports relatively cheaper. This worsens the current account deficit.</li>"
    "<li><b>Higher interest rates:</b> the RBA tightens monetary policy to bring inflation down. Lenders also raise nominal rates to protect their real return. Higher rates slow investment and economic growth and can raise unemployment.</li>"
    "<li><b>Redistribution of income and wealth:</b> inflation hurts people on fixed incomes and savers, because the real value of their money falls. It helps borrowers, because the real value of their debt falls, and owners of assets such as property.</li>"
    "<li><b>Uncertainty:</b> firms find it harder to plan, so they delay investment. Resources shift from productive investment into speculation in assets.</li></ul>"
    "<p><b>Positive effects of low inflation</b></p>"
    "<ul><li>Mild inflation encourages spending and investment now, not later, which supports growth.</li>"
    "<li>It lets real wages adjust without cuts to money wages, which helps the labour market work.</li>"
    "<li>It keeps the economy away from deflation, which raises the real burden of debt and leads consumers to delay spending.</li></ul>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Unemployment:</b> in the short run there is a trade-off. When unemployment falls below the non-accelerating inflation rate of unemployment (NAIRU), wage pressure builds and inflation rises.</li>"
    "<li><b>Monetary policy:</b> price stability is the RBA's main objective, and the cash rate is its main tool.</li>"
    "<li><b>Exchange rates:</b> a depreciation causes imported inflation. Higher interest rates can attract capital and lift the dollar.</li></ul>"
    "<p><b>Use it in an exam:</b> define inflation, quote the latest headline and underlying rates against the 2 to 3 per cent target, name the type of inflation and explain its cause with a diagram, then weigh the effects on households, firms and the wider economy.</p>"
    "<p>Sources: <a href=\"https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/consumer-price-index-australia/latest-release\">ABS, Consumer Price Index, Australia</a>; <a href=\"https://www.rba.gov.au/inflation/\">Reserve Bank of Australia, inflation</a>.</p>")
    tiles, js = B.live([("cpi", "Headline CPI, annual", "4.3%", "Sep 2026"), ("tmean", "Trimmed mean, annual", "3.6%", "Sep 2026"),
                        ("cash", "Cash rate target", "4.85%", "4 Nov 2026"), ("wpi", "Wages growth (WPI)", "3.2%", "Jun qtr 2026")])
    pts = [("Dec 2019", 2019.9, 1.8), ("", 2020.9, 0.9), ("", 2021.9, 3.5), ("Dec 2022", 2022.9, 7.8), ("", 2023.9, 4.1), ("Dec 2024", 2024.9, 2.4), ("", 2025.9, 3.8), ("Sep 2026", 2026.7, 4.3)]
    figs = [
      B.fig(1, "Latest figures", tiles, "These update by themselves from Economy at a Glance. The RBA's target is 2 to 3%."),
      B.fig(2, "Annual CPI inflation, 2019 to 2026 (%)", B.linechart(pts, c, 8, band=(2, 3, "RBA target 2 to 3%")), "Year to December each year, and year to September 2026. Source: ABS."),
      B.fig(3, "Demand inflation: aggregate demand shifts right", B.ed.ad_as("AD right", B.ed.TOPIC[3]).svg(), "AD<sub>1</sub> to AD<sub>2</sub> lifts the price level from P<sub>1</sub> to P<sub>2</sub> and output from Y<sub>1</sub> to Y<sub>2</sub>. Not to scale."),
      B.fig(4, "Cost inflation: aggregate supply shifts left", B.ed.ad_as("SRAS left", B.ed.TOPIC[3]).svg(), "SRAS<sub>1</sub> to SRAS<sub>2</sub> lifts the price level from P<sub>1</sub> to P<sub>2</sub> while output falls from Y<sub>1</sub> to Y<sub>2</sub>. Not to scale."),
      B.fig(5, "How imported inflation spreads", B.chain(["World oil price rises, or the Australian dollar falls", "Imports cost more in Australian dollars", "Fuel and input costs rise for firms", "Firms pass costs on as higher prices", "Headline CPI rises", "Workers seek higher wages, so expectations rise"])),
      B.fig(6, "Who gains and who loses from high inflation", B.table(["Loses", "Gains"], [["Workers whose wages rise more slowly than prices", "Borrowers with fixed-rate debt"], ["Savers and people on fixed incomes", "Owners of property and other real assets"], ["Exporters and firms that compete with imports", "Firms that can raise prices faster than their costs"], ["Lenders repaid in money that buys less", "Governments, as tax receipts rise with prices"]])),
      B.tools([("glance", "Latest inflation, wages and cash rate"), ("macro", "Shift AD and AS and watch prices"), ("chain", "Build the chain from cost shock to prices"), ("qf", "Past HSC questions on inflation"),
               ("mcq", "Section I questions with explanations"), ("ef", "News and statistics for essays"), ("gloss", "CPI, trimmed mean, NAIRU and more"), ("policy", "Set the cash rate and see inflation respond")]),
    ]
    B.build("inflation", c, cd, text, figs, js)
