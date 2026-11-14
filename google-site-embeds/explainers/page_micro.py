def make(B):
    c, cd = "#8a3fb0", "#6a2a8a"
    ed = B.ed
    text = (
    "<h3>What microeconomic policies do</h3>"
    "<p><b>Microeconomic policies</b> are reforms to particular markets and industries. They aim to make resources move to their most productive uses, so that the economy produces more output from the same inputs. They are <b>supply-side</b> policies: they act on aggregate supply and the productive capacity of the economy, not on aggregate demand. Their main objectives are higher <b>productivity</b>, stronger competitiveness, and sustained growth in living standards.</p>"
    "<h3>The main policy tools</h3>"
    "<ul><li><b>Competition policy:</b> rules that stop firms from misusing market power. From 1 January 2026 acquisitions above set thresholds must be notified to the ACCC and cannot be completed until cleared. Large deals are caught when the combined Australian revenue is at least $200 million.</li>"
    "<li><b>Deregulation:</b> removing or simplifying rules that raise costs without a clear benefit, such as planning and licensing rules. The Productivity Commission has argued that planning barriers hold back housing supply.</li>"
    "<li><b>Privatisation:</b> selling government-owned businesses so that they face competitive pressure and the profit motive.</li>"
    "<li><b>Trade liberalisation:</b> reducing tariffs and other barriers so that domestic firms face competition from imports and can sell to larger export markets.</li>"
    "<li><b>Labour market reform:</b> changes to wage setting, work rules and skills so that labour is used more efficiently. The move from centralised wage setting to enterprise bargaining is an example.</li>"
    "<li><b>Tax reform and investment incentives:</b> tax settings that encourage business investment and innovation, such as the $20,000 instant asset write-off, which the 2026&ndash;27 Budget made permanent for small business, and a higher R&amp;D offset from 1 July 2028.</li></ul>"
    "<h3>How they raise productivity</h3>"
    "<p>Competition forces firms to cut costs and innovate. Removing barriers lets capital and labour move to the firms and industries where they are most productive. Lower costs of production shift the aggregate supply curve to the right and raise the long-run aggregate supply (LRAS) curve, so that output can grow without adding to inflation (Figure 3). The effects are long-term, because reforms take time to change how firms behave.</p>"
    "<h3>Productivity in Australia now</h3>"
    "<p>Australia has a productivity problem. Between 2010 and 2020 it recorded its weakest productivity growth in 60 years, mainly because multifactor productivity weakened. Labour productivity rose by only 1 per cent over the year to December 2025, which only recovered a fall of 1 per cent over the previous year. Capital productivity has fallen by about 18.6 per cent since 1995. The Productivity Commission and the RBA point to declining competition and business dynamism, weak investment and a slowdown in major reform.</p>"
    "<p>The reforms of the 1980s and 1990s show what is possible. Lower tariffs, greater competition, changes to government-owned businesses and more flexible markets added about half a percentage point to the acceleration in annual labour productivity growth. The Government now has a five-pillar productivity agenda, which includes a revitalised National Competition Policy, tax reform, and the new merger rules.</p>"
    "<h3>Evaluating microeconomic policies</h3>"
    "<ul><li><b>Strengths:</b> they raise the productive capacity of the economy, support real wage growth, and improve competitiveness without raising inflation.</li>"
    "<li><b>Limitations:</b> the benefits come slowly and are hard to measure, while the costs, such as job losses in protected industries, are felt quickly and by particular groups. Workers who lose jobs may need retraining, and there are trade-offs with equity and the environment.</li>"
    "<li><b>Policy mix:</b> micro reform does not manage the business cycle, so it works alongside fiscal and monetary policy.</li></ul>"
    "<p><b>Use it in an exam:</b> name the policy, explain the mechanism that raises productivity, show the shift in LRAS, then weigh the long-run benefits against the short-run costs and time lags.</p>"
    "<p>Sources: <a href=\"https://www.aph.gov.au/About_Parliament/Parliamentary_departments/Parliamentary_Library/Research/Policy_Briefs/2025-26/Australiasflaggingproductivitygrowth\">Parliamentary Library, Australia's flagging productivity growth</a>; <a href=\"https://www.accountingtimes.com.au/economy/lacklustre-december-productivity-growth-spurs-pc-to-double-down-on-reform-calls\">Accounting Times, Productivity Commission March 2026 bulletin</a>; <a href=\"https://www.cornwalls.com.au/?p=30502\">Cornwalls, ACCC merger regime</a>; <a href=\"https://www.commbank.com.au/articles/newsroom/2026/08/explainer-australia-productivity-living-standards.html\">CommBank, What is productivity</a>; <a href=\"https://www.mallesons.com/content/dam/mallesons/insights/download-publication/australia/2026/05/Mallesons-Australian-Federal-Budget-2026-27.pdf\">Mallesons, Budget 2026&ndash;27</a>.</p>"
    )
    tiles = ('<div class="k"><div><b>1%</b><i>Labour productivity growth</i><u>Year to December 2025</u></div><div><b>&minus;18.6%</b><i>Capital productivity</i><u>Change 1995 to 2025</u></div>'
             '<div><b>1 Jan 2026</b><i>Mandatory merger notification</i><u>ACCC clearance required</u></div><div><b>$20,000</b><i>Instant asset write-off</i><u>Permanent for small business</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "Micro policy tools", B.table(["Tool", "Aim", "Example"], [["Competition", "Limit market power", "ACCC merger regime"], ["Deregulation", "Cut compliance costs", "Planning reform"], ["Privatisation", "Efficiency", "Sale of public assets"], ["Trade liberalisation", "Import competition", "Lower tariffs"], ["Labour market", "Flexible wages", "Enterprise bargaining"], ["Tax incentives", "Boost investment", "Asset write-off"]])),
      B.fig(3, "Micro reform raises long-run aggregate supply", ed.lras_growth(ed.TOPIC[4]).svg(), "AD outruns a fixed LRAS and pushes up prices (P<sub>1</sub> to P<sub>2</sub>); a shift of LRAS to the right lets output grow (Y<sub>1</sub> to Y<sub>2</sub>) without more inflation. Not to scale."),
      B.fig(4, "Chain: how competition lifts productivity", B.chain(["Stronger competition", "Firms cut costs and innovate", "Resources move to productive uses", "Productivity and LRAS rise", "Higher output, real wages and living standards"])),
      B.fig(5, "Evaluating micro policy", B.table(["Strength", "Limitation"], [["Raises productive capacity", "Slow to take effect"], ["No extra inflation pressure", "Costs fall on specific groups"], ["Improves competitiveness", "Equity and environmental trade-offs"]])),
      B.tools([("policy", "Test fiscal and monetary settings"), ("macro", "Draw AD/AS and LRAS shifts"), ("glance", "Latest productivity data"), ("chain", "Build cause-and-effect chains"),
               ("qf", "Past HSC questions on micro policy"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence on reform"), ("map", "See how topics connect")]),
    ]
    B.build("microeconomic-policies", c, cd, text, figs, "")
