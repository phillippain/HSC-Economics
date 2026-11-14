def make(B):
    c, cd = "#8a3fb0", "#6a2a8a"
    ed = B.ed
    text = (
    "<h3>What monetary policy is</h3>"
    "<p><b>Monetary policy</b> is the use of interest rates and the money supply by the central bank to influence the level of economic activity and achieve the objectives of price stability and full employment. In Australia it is set by the Reserve Bank of Australia (RBA). Its Monetary Policy Board, which has nine members, meets eight times a year to decide the <b>cash rate target</b>.</p>"
    "<h3>The objectives and the target</h3>"
    "<p>The RBA has two goals set out in law: price stability and full employment. It aims to keep consumer price inflation between <b>2 and 3 per cent</b> on average over time, and to support the highest level of employment that can be sustained without pushing inflation up. This is called <b>flexible inflation targeting</b>.</p>"
    "<h3>How the RBA carries out policy</h3>"
    "<p>The <b>cash rate</b> is the interest rate on overnight loans between banks. The RBA sets a target for it and makes it happen through <b>open market operations</b>: it buys or sells government securities and adjusts the supply of exchange settlement funds that banks hold with it. It also pays interest on those balances, which sets a floor for the cash rate. Banks then change their own lending and deposit rates (Figure 4).</p>"
    "<h3>Stance of monetary policy</h3>"
    "<ul><li><b>Expansionary (loose):</b> the RBA lowers the cash rate. Borrowing is cheaper, so consumption and investment rise and aggregate demand shifts to the right. It is used when growth is weak and unemployment is rising.</li>"
    "<li><b>Contractionary (tight):</b> the RBA raises the cash rate. Borrowing is dearer and saving is more attractive, so aggregate demand shifts to the left (Figure 3). It is used when inflation is above the target band.</li></ul>"
    "<h3>The transmission mechanism</h3>"
    "<p>A change in the cash rate affects the economy through several channels.</p>"
    "<ul><li><b>Interest rates:</b> a rise lifts mortgage and business loan rates, which cuts spending on housing and investment by households and firms.</li>"
    "<li><b>Asset prices and wealth:</b> higher rates reduce house and share prices, so households feel poorer and spend less.</li>"
    "<li><b>Exchange rate:</b> higher interest rates attract foreign capital, which raises the Australian dollar. Exports become dearer and imports cheaper, so net exports fall and imported inflation eases.</li>"
    "<li><b>Expectations:</b> a credible RBA helps keep inflation expectations anchored.</li></ul>"
    "<h3>Where policy stands</h3>"
    "<p>In 2026 the RBA moved from easing to tightening. It raised the cash rate five times, in February, March, May, September and November, by 25 basis points each time, from 3.60 to <b>4.85 per cent</b> on 3 November 2026 (Figure 2). It is the highest rate since 2008. The vote was 6 to 3, with three members preferring no change.</p>"
    "<p>The reason was inflation. Headline consumer price inflation reached 4.3 per cent in the year to September, and underlying inflation was 3.7 per cent, well above the target band (Figure 5). The RBA pointed to higher oil prices from the war in the Middle East and to capacity pressures in the economy. It expects inflation to remain above 3 per cent until late 2027.</p>"
    "<p>The tightening has a cost. The RBA acknowledged that the economy is slowing, house prices have fallen significantly and unemployment has risen to 4.7 per cent, the highest in five years. It forecasts that unemployment will rise to a little above 5 per cent by the end of 2028. This is the trade-off between the two objectives: lower inflation is being bought with slower growth and higher unemployment.</p>"
    "<h3>Limitations of monetary policy</h3>"
    "<ul><li><b>Time lags:</b> the full effect of a rate change takes 12 to 18 months or more, so policy must look ahead.</li>"
    "<li><b>Cost-push and imported inflation:</b> higher interest rates cannot lower the world price of oil. They work on demand, not supply.</li>"
    "<li><b>Uneven effects:</b> borrowers with large mortgages are hit harder than savers or those with no debt. Mortgage holders on variable rates feel changes quickly.</li>"
    "<li><b>Weak response in a downturn:</b> if confidence is low, cutting rates may not raise spending.</li>"
    "<li><b>Conflicting objectives:</b> a policy aimed at inflation may increase unemployment, as in 2026.</li></ul>"
    "<h3>Monetary and fiscal policy together</h3>"
    "<p>Monetary policy is flexible and independent of politics and can change at eight meetings a year, whereas fiscal policy changes mostly once a year at the Budget. When both are contractionary, as in 2026&ndash;27, they reinforce each other, but the risk of weaker growth is greater.</p>"
    "<p><b>Use it in an exam:</b> state the cash rate and the reason for the change, trace the transmission mechanism, draw the AD shift, then evaluate with lags, the trade-off with unemployment and the type of inflation.</p>"
    "<p>Sources: <a href=\"https://www.rba.gov.au/publications/smp/2026/nov/overview.html\">RBA, Statement on Monetary Policy, November 2026</a>; <a href=\"https://www.rba.gov.au/monetary-policy/\">RBA, Monetary Policy</a>; <a href=\"https://www.abs.gov.au/\">ABS, Consumer Price Index and Labour Force</a>; <a href=\"https://www.nab.com.au/news/economy-markets/nab-rba-watch--rba-hikes-25bps-as-expected\">NAB, RBA Watch, 3 November 2026</a>.</p>")
    tiles = ('<div class="k"><div><b>4.85%</b><i>Cash rate target</i><u>3 November 2026</u></div><div><b>5</b><i>Rate rises in 2026</i><u>+125 basis points</u></div>'
             '<div><b>4.3%</b><i>Headline inflation</i><u>Year to September 2026</u></div><div><b>4.7%</b><i>Unemployment rate</i><u>Highest in five years</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "RBA cash rate target (%)", B.bars([("Dec 2025", 3.60), ("Feb 2026", 3.85), ("Mar 2026", 4.10), ("May 2026", 4.35), ("Sep 2026", 4.60), ("Nov 2026", 4.85)], vmax=5.5, fmt="%.2f%%"), "Five rises of 25 basis points in 2026. Dates are the month of each decision. Source: RBA."),
      B.fig(3, "Contractionary monetary policy", ed.ad_as("AD left", ed.TOPIC[4]).svg(), "A higher cash rate shifts AD to the left: real GDP falls (Y<sub>1</sub> to Y<sub>2</sub>) and the price level is lower (P<sub>1</sub> to P<sub>2</sub>) than it would have been. Not to scale."),
      B.fig(4, "Chain: RBA raises the cash rate", B.chain(["RBA raises the cash rate target", "Banks raise mortgage and business rates", "Spending and investment fall; AUD may rise", "Aggregate demand slows", "Inflation falls, but unemployment may rise"])),
      B.fig(5, "Inflation and the target band", B.bars([("Target band top", 3.0), ("Underlying (Sep)", 3.7), ("Headline (Sep)", 4.3)], vmax=5, fmt="%.1f%%"), "Annual rates, September 2026. The RBA target is 2&ndash;3%. Source: ABS."),
      B.fig(6, "Stance of monetary policy", B.table(["", "Expansionary", "Contractionary"], [["Cash rate", "Lowered", "Raised"], ["Borrowing", "Cheaper", "Dearer"], ["Aggregate demand", "Rises", "Falls"], ["Used when", "Weak growth", "High inflation"]])),
      B.fig(7, "Monetary and fiscal policy compared", B.table(["", "Monetary", "Fiscal"], [["Decided by", "RBA Board", "Government"], ["Tools", "Cash rate", "Spending, tax"], ["Timing", "Eight meetings a year", "Budget, mainly once a year"], ["Main aim", "Inflation, jobs", "Growth, equity, jobs"]])),
      B.tools([("policy", "Change the cash rate and see the effects"), ("macro", "Draw AD shifts"), ("glance", "Latest cash rate, inflation and jobs"), ("chain", "Build the transmission chain"),
               ("qf", "Past HSC questions on monetary policy"), ("mcq", "Section I questions with explanations"), ("ef", "Find RBA evidence"), ("gloss", "Cash rate, open market operations")]),
    ]
    B.build("monetary-policy", c, cd, text, figs, "")
