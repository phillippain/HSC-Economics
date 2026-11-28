import methods_common as M


def make(B):
    ed = B.ed
    text = (
    "<h3>What export incentives are</h3>"
    "<p><b>Export incentives</b> are government measures that help local firms sell overseas. They range from <b>export subsidies</b>, which pay producers for each unit they export, to <b>non-price assistance</b> such as marketing grants, trade missions, information about foreign markets and help with finance and insurance. They protect local industry indirectly, by giving it a larger market than it could win on its own.</p>"
    "<h3>How an export subsidy works</h3>"
    "<p>When the world price P<sub>w</sub> is above the local equilibrium, a country exports the gap between what its firms supply and what its consumers buy (Q2 to Q3 in Figure 2). An export subsidy of s per unit means producers earn P<sub>w+s</sub> on every unit they export, so they will not sell locally for less. The local price rises, local consumers buy less (Q1), producers supply more (Q4), and exports grow to Q1&ndash;Q4. Taxpayers pay the subsidy on every exported unit (the gold rectangle).</p>"
    "<p>If the exporting country is large, the extra supply pushes the <b>world price down</b>. That hurts efficient, unsubsidised exporters in other countries. This is why Australian farmers have long opposed the export subsidies of the EU and the US.</p>"
    "<h3>Export incentives in Australia</h3>"
    "<ul>"
    "<li>The <b>Export Market Development Grants</b> (EMDG) scheme reimburses part of small firms' overseas marketing costs. It has about $105 million in 2026&ndash;27 and has helped more than 51,000 exporters since 1974.</li>"
    "<li><b>Austrade</b> gives market information and trade missions, and <b>Export Finance Australia</b>, a government agency, provides loans, guarantees and insurance when banks will not.</li>"
    "<li>These are non-price incentives: they do not cut the price of exports, so they are allowed under WTO rules and distort trade far less than export subsidies.</li>"
    "</ul>"
    "<h3>Export subsidies in the world</h3>"
    "<p>At the WTO's Nairobi meeting in 2015, members agreed to abolish export subsidies on farm goods, a long-standing aim of the Cairns Group led by Australia. But farm support continues through other channels: the EU's Common Agricultural Policy still takes more than a third of the EU budget, and ABARES estimates that rich-country farm support costs Australia $8 to $10 billion a year in lost farm exports.</p>"
    "<h3>Evaluating export incentives</h3>"
    "<ul>"
    "<li><b>For:</b> they help small firms overcome the cost of entering new markets, lift export income and jobs, and can help diversify exports away from one or two buyers.</li>"
    "<li><b>Against:</b> export subsidies cost taxpayers, raise local prices, misallocate resources and lower world prices for other exporters, and they can provoke countervailing duties.</li>"
    "</ul>"
    "<p><b>Use it in an exam:</b> distinguish export subsidies (price support, WTO-banned for farm goods) from non-price assistance such as the EMDG. Explain how foreign export subsidies harm Australia through lower world prices for its farm exports.</p>"
    "<p>Sources: Pearson, <i>Australia in the Global Economy 2027</i>, ch. 6; Austrade, EMDG; WTO, Nairobi Ministerial Decision on Export Competition (2015).</p>"
    + M.nav("export-incentives"))
    tiles = ('<div class="k"><div><b>$105m</b><i>EMDG funding</i><u>2026&ndash;27</u></div>'
             '<div><b>51,000+</b><i>Exporters helped by EMDG</i><u>since 1974</u></div>'
             '<div><b>2015</b><i>WTO agrees to end farm export subsidies</i><u>Nairobi</u></div>'
             '<div><b>$8&ndash;10b</b><i>Australian farm exports lost each year</i><u>to other countries\' farm support (ABARES)</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "The effect of an export subsidy", M.export_subsidy_diagram(ed).svg(),
            "Producers earn Pw+s on exports, so the local price rises: consumption falls Q2 to Q1, output rises Q3 to Q4, exports grow. Gold = cost to taxpayers. Not to scale."),
      B.fig(3, "Types of export incentive", B.table(["Type", "Example", "WTO rules"],
            [["Export subsidy", "Payment per unit exported", "Banned for farm goods since 2015"], ["Marketing grants", "EMDG", "Allowed"], ["Finance and insurance", "Export Finance Australia", "Allowed within limits"], ["Information and promotion", "Austrade, trade missions", "Allowed"]])),
      B.fig(4, "Who gains and who loses from an export subsidy", B.table(["Group", "Effect"],
            [["Local exporters", "Gain: higher price, more sales"], ["Local consumers", "Lose: higher local price"], ["Taxpayers", "Pay the subsidy"], ["Other exporters (e.g. Australian farmers)", "Lose: lower world price"]])),
      B.fig(5, "Chain: how EU farm support hurts Australia", B.chain(["EU supports its farmers", "EU farm output and exports rise", "World prices fall", "Australian farm export income falls", "Australia's terms of trade and current account weaken"])),
      B.tools([("explain", "See who wins and loses from protection"), ("mcq", "Multiple choice on methods of protection", "#point=1C.2"),
               ("qf", "Past HSC questions on export incentives"), ("ef", "Latest evidence on exports"), ("bop", "Link exports to the current account"), ("chain", "Build the export subsidy chain")])]
    B.build("method-export-incentives", M.C, M.CD, text, figs, "")
