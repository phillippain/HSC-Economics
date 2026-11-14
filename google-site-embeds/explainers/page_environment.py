def extern(ed, c):
    d = ed.Diagram("Price and cost ($)", "Quantity of electricity from coal", c)
    d.line("MPC", (0.8, 1.2), (9.0, 6.4), "grey")
    d.line("MSC", (0.8, 2.8), (8.0, 8.9), "red")
    d.line("D", (1.0, 8.8), (9.0, 1.4))
    d.shift("MPC", "MSC", .45)
    d.point("D", "MPC", "P1", "Q1", color="grey"); d.point("D", "MSC", "P2", "Q2", "red")
    return d.svg()

def make(B):
    c, cd = "#d9822b", "#a85a12"
    ed = B.ed
    text = (
    "<h3>What environmental sustainability means</h3>"
    "<p><b>Ecologically sustainable development (ESD)</b> means using, conserving and enhancing resources so that the ecological processes on which life depends are maintained and the total quality of life, now and in the future, can be increased. The key idea is <b>intergenerational equity</b>: the needs of future generations should not be sacrificed for the benefit of the present one. ESD does not rule out economic growth. It asks whether growth is achieved in a way that can be kept up over time.</p>"
    "<h3>Why markets fail to protect the environment</h3>"
    "<p>A market works well when the price paid by buyers and the price received by sellers reflect all the costs and benefits of a good. Environmental resources often fail this test, so the market produces too much or too little. This is <b>market failure</b>. Three causes are named in the syllabus.</p>"
    "<p><b>1. Private and social costs and benefits (externalities).</b> <b>Private costs</b> are the costs paid by the producer, such as wages and fuel. <b>Social costs</b> are private costs plus the <b>external costs</b> imposed on third parties, such as air pollution. A firm that does not pay for the pollution it causes produces where marginal private cost (MPC) meets demand (Figure 2). Because the marginal social cost (MSC) is higher than MPC, the market quantity (Q<sub>1</sub>) is greater than the socially best quantity (Q<sub>2</sub>), and the price (P<sub>1</sub>) is too low. A <b>positive externality</b>, such as the benefit to neighbours from a business that plants trees, works the other way: too little is produced.</p>"
    "<p><b>2. Public goods and free riders.</b> <b>Private goods</b> are rival (one person's use leaves less for others) and excludable (people who do not pay can be kept out). <b>Public goods</b>, such as a clean atmosphere, flood mitigation or national parks, are non-rival and non-excludable (Figure 7). Because people cannot be stopped from using them, many become <b>free riders</b>, who enjoy the benefit without paying. Private firms cannot earn a profit, so the good is under-provided unless government supplies it. <b>Common access resources</b>, such as fish stocks and groundwater, are rival but non-excludable. They tend to be overused because each user gains the full benefit of taking more while the cost of depletion is shared by all.</p>"
    "<p><b>3. Missing prices and property rights.</b> Where no one owns clean air or a coral reef, no one is charged for damaging it, so the price signal that normally limits use is absent.</p>"
    "<h3>The main environmental issues</h3>"
    "<ul><li><b>Pollution:</b> air, water and land pollution impose external costs on health and ecosystems. The cost falls on people who did not choose the activity.</li>"
    "<li><b>Climate change:</b> greenhouse gas emissions are a global negative externality. Australia has committed to cut emissions to 43 per cent below 2005 levels by 2030, 62 to 70 per cent below by 2035, and reach net zero by 2050 (Figure 3). The government's 2025 projections show a fall of only about 48 per cent by 2035 on current policies, which do not yet include the policies announced with the target.</li>"
    "<li><b>Preservation of natural environments:</b> reefs, forests and wetlands provide benefits that are not priced, such as tourism, water filtering and habitat. Land clearing or development gives a private gain but a social loss. The Australian Institute of Marine Science found that the Great Barrier Reef's coral cover recovered in the north and centre in 2026 after the recent bleaching, while the south slipped slightly (Figure 6).</li>"
    "<li><b>Depletion of resources:</b> <b>renewable</b> resources such as fish, forests and water can regenerate but are depleted if used faster than they replace themselves. <b>Non-renewable</b> resources such as coal, gas and iron ore are finite, so using them today leaves less for future generations.</li></ul>"
    "<h3>Trends in Australia</h3>"
    "<p>Australia's greenhouse gas emissions fell 1.6 per cent, or 7.5 million tonnes, in the year to March 2026 to about 455 million tonnes of carbon dioxide equivalent. Electricity emissions fell 3.7 per cent as renewable generation reached record levels (Figure 5). Emissions are about 25 per cent below 2005 levels when the land sector is included. The land sector is now a net carbon sink, so excluding it, emissions are only about 4 per cent below 2005. Electricity is still the largest source.</p>"
    "<p>Renewables supplied 44.3 per cent of generation in the National Electricity Market in the September quarter 2026, a record for that quarter, against a government target of 82 per cent by 2030 (Figure 4). Falling renewable costs, battery storage and consumer demand have helped lower wholesale prices, which shows that reducing emissions and economic goals can be consistent.</p>"
    "<h3>Policy responses</h3>"
    "<p>Governments can correct market failure by making the polluter bear the cost, or by providing the good themselves (Figure 8).</p>"
    "<ul><li><b>Market-based:</b> the Safeguard Mechanism sets a declining emissions baseline of 4.9 per cent a year to 2030 for about 220 large facilities, which cover around 30 per cent of national emissions. Facilities that exceed their baseline must buy carbon credits, so emissions now carry a price.</li>"
    "<li><b>Regulation:</b> standards and bans, such as vehicle efficiency standards and limits on pollutants, set a maximum.</li>"
    "<li><b>Taxes and subsidies:</b> a tax on a harmful activity raises its price. A subsidy for renewable energy or electric vehicles lowers the cost of activities with positive externalities.</li>"
    "<li><b>Direct provision and funding:</b> governments fund national parks, conservation and research, because free riders prevent private provision.</li></ul>"
    "<h3>Costs and trade-offs</h3>"
    "<p>Policies to protect the environment have costs. Higher costs for polluting firms can raise prices and reduce international competitiveness, and may cost jobs in coal and gas regions. Yet doing nothing also has costs in damaged health, lost tourism and farm output, and the risk of irreversible loss. The task for policy is to compare the costs and benefits and reach the lowest-cost way to achieve the goal.</p>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Economic growth:</b> GDP does not subtract environmental damage, so measured growth can overstate wellbeing.</li>"
    "<li><b>Fiscal and microeconomic policy:</b> taxes, subsidies, deregulation and competition policy in Topic 4 are the tools used to correct these failures.</li>"
    "<li><b>External stability:</b> exports of coal and gas depend on world demand, which may fall as other countries cut emissions.</li></ul>"
    "<p><b>Use it in an exam:</b> name the market failure, draw MPC and MSC with the quantities, use a current statistic such as the 1.6 per cent fall in emissions, and weigh the policy tools against their costs.</p>"
    "<p>Sources: <a href=\"https://www.dcceew.gov.au/climate-change/publications/national-greenhouse-gas-inventory-quarterly-updates\">DCCEEW, National Greenhouse Gas Inventory quarterly update</a>; <a href=\"https://www.aemo.com.au/\">AEMO, Quarterly Energy Dynamics</a>; <a href=\"https://aims.gov.au/monitoring-great-barrier-reef/gbr-condition-summary-2025-26\">AIMS, Great Barrier Reef condition summary 2025&ndash;26</a>; <a href=\"https://cer.gov.au/schemes/safeguard-mechanism\">Clean Energy Regulator, Safeguard Mechanism</a>.</p>")
    tiles = ('<div class="k"><div><b>455 Mt</b><i>Annual emissions</i><u>CO&#8322;-e, year to March 2026</u></div><div><b>&minus;1.6%</b><i>Change in emissions</i><u>Year to March 2026</u></div>'
             '<div><b>44.3%</b><i>Renewable share, NEM</i><u>September quarter 2026</u></div><div><b>62&ndash;70%</b><i>2035 target</i><u>Below 2005 levels</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "A negative externality: pollution from electricity", extern(ed, c), "MSC lies above MPC by the external cost. The market produces Q<sub>1</sub>, but the best level for society is Q<sub>2</sub>. Not to scale."),
      B.fig(3, "Australia's emissions targets", B.table(["Target or measure", "Level"], [["2030 target", "43% below 2005"], ["2035 target", "62&ndash;70% below 2005"], ["2050", "Net zero"], ["Projected 2035 cut (2025 projections)", "About 48%"], ["Cut so far (land sector included)", "About 25%"], ["Cut so far (land sector excluded)", "About 4%"]]), "Sources: DCCEEW, Climate Change Authority, as reported in the media."),
      B.fig(4, "Renewable share of National Electricity Market generation (%)", B.bars([("Sep qtr 2025", 41.8), ("Dec qtr 2025", 51.0), ("Mar qtr 2026", 46.5), ("Jun qtr 2026", 42.1), ("Sep qtr 2026", 44.3)], vmax=60, fmt="%.1f%%"), "The share varies with the season. Source: AEMO Quarterly Energy Dynamics."),
      B.fig(5, "Fall in emissions, year to March 2026 (%)", B.bars([("All sectors", 1.6), ("Electricity", 3.7), ("Fugitive emissions", 3.3), ("Agriculture", 1.0)], vmax=4, fmt="&minus;%.1f%%"), "Fugitive emissions are leaks from fuel production. Source: DCCEEW."),
      B.fig(6, "Great Barrier Reef hard coral cover (%)", B.bars2([("Central", 28.6, 31.6), ("Southern", 26.9, 26.4)], ("2025", "2026"), fmt="%.1f"), "Survey of 121 reefs by the Long-Term Monitoring Program. Source: AIMS, August 2026."),
      B.fig(7, "Types of goods", B.table(["Type", "Rival?", "Excludable?", "Example"], [["Private", "Yes", "Yes", "Takeaway meal"], ["Public", "No", "No", "Clean air, flood levee"], ["Common access", "Yes", "No", "Fish stocks"]]), "Free riding arises when people cannot be excluded."),
      B.fig(8, "Policy tools", B.table(["Tool", "How it works"], [["Carbon price or credits", "Makes polluters pay the external cost"], ["Regulation", "Sets a limit or standard"], ["Tax", "Raises the price of a harmful good"], ["Subsidy", "Lowers the price of a beneficial good"], ["Public provision", "Government funds the public good"]])),
      B.fig(9, "Chain: free riding", B.chain(["Clean air cannot be sold to individuals", "People enjoy it without paying (free riders)", "No private firm can earn a profit", "The market under-provides it", "Government funds or regulates"])),
      B.tools([("chain", "Build the chain from externality to policy"), ("macro", "Draw MPC and MSC diagrams"), ("glance", "Latest emissions and energy figures"), ("policy", "Test policy responses"),
               ("qf", "Past HSC questions on sustainability"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence on the environment"), ("gloss", "Externality, free rider and more")]),
    ]
    B.build("environmental-sustainability", c, cd, text, figs, "")
