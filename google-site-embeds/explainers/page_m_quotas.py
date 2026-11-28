import methods_common as M


def make(B):
    ed = B.ed
    text = (
    "<h3>What a quota is</h3>"
    "<p>An <b>import quota</b> is a physical limit on the quantity (or value) of a good that can be imported in a period, for example 30 million kilograms of cheese a year. Once the quota is filled, no more can come in. A <b>tariff-rate quota</b> mixes the two methods: imports up to the quota pay a low tariff, and anything above it pays a much higher one.</p>"
    "<h3>How a quota works</h3>"
    "<p>At the world price P<sub>w</sub>, local firms supply Q1 and consumers want Q4, so imports would be Q1 to Q4 (Figure 2). The quota allows only a smaller amount in. With fewer imports, the good becomes scarce and its domestic price rises until local supply plus the quota equals demand, at P1 (where the <b>S + quota</b> curve meets D).</p>"
    "<ul>"
    "<li><b>Price:</b> rises from P<sub>w</sub> to P1.</li>"
    "<li><b>Local production:</b> rises from Q1 to Q2, so local firms and jobs are protected.</li>"
    "<li><b>Consumption:</b> falls from Q4 to Q3.</li>"
    "<li><b>Revenue:</b> the government collects nothing (unless it sells the import licences). Importers who hold the right to bring in the quota buy at P<sub>w</sub> and sell at P1, so <b>the importers keep the extra revenue from the higher price</b> (the gold rectangle).</li>"
    "<li><b>Deadweight losses:</b> the two red triangles, as with a tariff.</li>"
    "</ul>"
    "<h3>Quota or tariff?</h3>"
    "<p>A quota gives local producers more certainty, because imports cannot rise however low the world price falls. But it is less transparent, it raises no revenue for the government, and if demand grows the whole increase goes into a higher price rather than more imports. That is why the WTO prefers tariffs, and why Australia phased out its import quotas on cars, clothing and footwear in the late 1980s and early 1990s in favour of tariffs, which were then cut over time.</p>"
    "<h3>Worked example: cheese</h3>"
    "<p>Domestic supply is Q = 10P &minus; 20 and demand Q = 130 &minus; 10P (millions of kilograms). At the world price of $4, local output is 20 million kg, demand 90 million and imports 70 million. A quota of 30 million kg raises the price to $6: local output rises to 40 million and demand falls to 70 million. Local producers' revenue rises from $80 million to $240 million. Importers' revenue falls from $280 million to $180 million, which includes $60 million of extra revenue from the higher price. Consumers lose $160 million of surplus: $60 million goes to producers, $60 million to importers, and $40 million is deadweight loss (Figure 3).</p>"
    "<h3>Quotas now</h3>"
    "<p>Quotas matter most to Australia as an exporter. The EU and the US limit imports of beef, sheepmeat and sugar with tariff-rate quotas. The Australia&ndash;EU free trade agreement, concluded in 2026, would lift Australia's beef access to about eight times, and sheepmeat to about four times, the current quota levels. In October 2026 US sheep farmers asked for a safeguard on imported lamb, which could take the form of a quota or a tariff.</p>"
    "<p><b>Use it in an exam:</b> draw the quota diagram and contrast it with a tariff: the same price, output and consumption effects, but no government revenue, because importers keep the extra revenue from the higher price.</p>"
    "<p>Sources: Pearson, <i>Australia in the Global Economy 2027</i>, ch. 6; Topic 1 workbook 2027 (cheese practice); Prime Minister's press conference (29 October 2026); <i>The Economy This Week</i>, 20 October 2026.</p>"
    + M.nav("quotas"))
    tiles = ('<div class="k"><div><b>$0</b><i>Government revenue from a quota</i><u>unless licences are sold</u></div>'
             '<div><b>~8&times;</b><i>EU beef access for Australia</i><u>Australia&ndash;EU FTA, 2026</u></div>'
             '<div><b>~4&times;</b><i>EU sheepmeat access</i><u>Australia&ndash;EU FTA, 2026</u></div>'
             '<div><b>$40m</b><i>Deadweight loss</i><u>cheese example</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "The effect of an import quota", M.quota_diagram(ed).svg(),
            "The quota (Q2 to Q3) is less than free-trade imports (Q1 to Q4), so the price rises to P1. Gold = extra revenue kept by importers; red = deadweight loss. Not to scale."),
      B.fig(3, "Worked example: a 30 million kg cheese quota", B.table(["", "Free trade", "With quota"],
            [["Price", "$4", "$6"], ["Local output", "20m kg", "40m kg"], ["Quantity demanded", "90m kg", "70m kg"], ["Imports", "70m kg", "30m kg"],
             ["Local producers' revenue", "$80m", "$240m"], ["Importers' revenue", "$280m", "$180m"]])),
      B.fig(4, "Where the lost consumer surplus goes ($m)", B.bars([("To local producers", 60), ("To importers", 60), ("Deadweight loss", 40)], vmax=70, fmt="$%gm"),
            "Total loss of consumer surplus: $160m."),
      B.fig(5, "Quota compared with a tariff", B.table(["", "Tariff", "Quota"],
            [["Price rises", "Yes", "Yes"], ["Imports limited", "Indirectly", "Exactly"], ["Government revenue", "Yes", "No"], ["Extra revenue goes to", "Government", "Importers"], ["If demand grows", "More imports", "Higher price"]])),
      B.tools([("lab", "Draw a quota and compare it with a tariff"), ("explain", "See who wins and loses from a quota"),
               ("mcq", "Multiple choice on methods of protection", "#point=1C.2"), ("qf", "Past HSC quota questions"), ("ef", "Latest trade news"), ("gloss", "Check key terms")])]
    B.build("method-quotas", M.C, M.CD, text, figs, "")
