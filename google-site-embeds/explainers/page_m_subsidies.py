import methods_common as M


def make(B):
    ed = B.ed
    text = (
    "<h3>What a subsidy is</h3>"
    "<p>A <b>subsidy</b> (or bounty) is a payment or tax concession from the government to local producers. It lowers their costs, so they can sell more at the world price and compete with imports. Subsidies can be cash grants, tax credits, cheap loans or guaranteed purchases.</p>"
    "<h3>How a subsidy works</h3>"
    "<p>Because the subsidy cuts costs, local firms are willing to supply more at every price: the supply curve shifts right from S1 to <b>S2</b> (Figure 2). Imports are still available at the world price, so the price consumers pay does not change.</p>"
    "<ul>"
    "<li><b>Price:</b> stays at P<sub>w</sub>, so consumers are not directly affected.</li>"
    "<li><b>Local production:</b> rises from Q1 to Q2, protecting local firms and jobs.</li>"
    "<li><b>Consumption:</b> stays at Q3.</li>"
    "<li><b>Imports:</b> fall from Q1&ndash;Q3 to Q2&ndash;Q3.</li>"
    "<li><b>Cost:</b> taxpayers pay the subsidy on every unit produced (the subsidy per unit times Q2). The money has an opportunity cost: it could have funded schools or hospitals, or lower taxes.</li>"
    "</ul>"
    "<h3>Subsidy or tariff?</h3>"
    "<p>A subsidy protects local producers without raising prices to consumers, so it causes less deadweight loss than a tariff: there is no loss from reduced consumption, only from inefficient production. It is also transparent, because its cost appears in the Budget. But it must be paid for, and it is hard to remove once firms depend on it. Other countries may also treat subsidised exports as unfair and impose <b>countervailing duties</b>.</p>"
    "<h3>Subsidies now</h3>"
    "<ul>"
    "<li><b>Australia:</b> the Whyalla steelworks received $2.4 billion in support plus $223 million more. Under Future Made in Australia, production tax incentives pay 10 per cent of the cost of processing critical minerals and $2 for each kilogram of green hydrogen.</li>"
    "<li><b>Farm support:</b> government support is under 3 per cent of farm income in Australia, against about 7 per cent in the US, 16 per cent in the EU and 41 per cent in South Korea. The EU's Common Agricultural Policy takes more than a third of the EU budget.</li>"
    "<li><b>Industry policy:</b> the US, the EU and China all subsidise electric vehicles, batteries, chips and clean energy, which has started subsidy races and trade disputes over &ldquo;overcapacity&rdquo;.</li>"
    "</ul>"
    "<p><b>Use it in an exam:</b> show the supply curve shifting right at an unchanged world price, then compare with a tariff: same protection for local producers, no rise in consumer prices, but a direct cost to the Budget.</p>"
    "<p>Sources: Pearson, <i>Australia in the Global Economy 2027</i>, ch. 6; Australian Government, Future Made in Australia; <i>The Economy This Week</i>, 27 November 2026.</p>"
    + M.nav("subsidies"))
    tiles = ('<div class="k"><div><b>$2.4b</b><i>Support for Whyalla steelworks</i><u>plus $223m</u></div>'
             '<div><b>&lt;3%</b><i>Farm support in Australia</i><u>EU 16%, South Korea 41%</u></div>'
             '<div><b>&gt;&#8531;</b><i>EU budget spent on the CAP</i><u>Pearson 2027</u></div>'
             '<div><b>$2/kg</b><i>Green hydrogen tax incentive</i><u>Future Made in Australia</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "The effect of a production subsidy", M.subsidy_diagram(ed).svg(),
            "Supply shifts right from S1 to S2 (S2 includes the subsidy); at the unchanged world price local output rises from Q1 to Q2 and imports shrink. Consumption stays at Q3. Not to scale."),
      B.fig(3, "Farm support as a share of farm income (%)", B.bars([("Australia", 3), ("United States", 7), ("European Union", 16), ("South Korea", 41)], vmax=45, fmt="%g%%"),
            "Australia's figure is 'under 3%'. Source: Pearson 2027, ch. 6 (OECD producer support estimates)."),
      B.fig(4, "Subsidy compared with a tariff", B.table(["", "Tariff", "Subsidy"],
            [["Consumer price", "Rises", "Unchanged"], ["Local output", "Rises", "Rises"], ["Consumption", "Falls", "Unchanged"], ["Budget", "Revenue in", "Cost out"], ["Deadweight loss", "Production and consumption", "Production only"]])),
      B.fig(5, "Chain: how a subsidy protects local jobs", B.chain(["Government pays producers per unit", "Costs fall; supply shifts right", "Local output rises at the world price", "Imports fall; local jobs kept", "Taxpayers bear the cost"])),
      B.tools([("lab", "Shift supply with a subsidy"), ("explain", "See who wins and loses from a subsidy"),
               ("mcq", "Multiple choice on methods of protection", "#point=1C.2"), ("qf", "Past HSC subsidy questions"), ("ef", "Latest evidence on industry support"), ("chain", "Build the subsidy chain")])]
    B.build("method-subsidies", M.C, M.CD, text, figs, "")
