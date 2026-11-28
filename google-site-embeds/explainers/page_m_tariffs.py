import methods_common as M


def make(B):
    ed = B.ed
    text = (
    "<h3>What a tariff is</h3>"
    "<p>A <b>tariff</b> is a tax on imported goods. It is the most common method of protection. An <b>ad valorem</b> tariff is a percentage of the import's value (for example 5 per cent); a <b>specific</b> tariff is a fixed amount per unit (for example $2 a kilogram). The tariff is collected at the border, so imports cost more than locally made goods.</p>"
    "<h3>How a tariff works</h3>"
    "<p>In a small economy like Australia, imports are available at the <b>world price</b> (P<sub>w</sub>). Local firms supply Q1, consumers buy Q4, and imports fill the gap (Figure 2). A tariff raises the price of imports to P<sub>w+t</sub>, and local producers can then charge the same higher price. The effects are often remembered as five:</p>"
    "<ul>"
    "<li><b>Price effect:</b> the domestic price rises from P<sub>w</sub> to P<sub>w+t</sub>.</li>"
    "<li><b>Production (protection) effect:</b> local firms expand output from Q1 to Q2.</li>"
    "<li><b>Consumption effect:</b> consumers buy less, Q3 instead of Q4.</li>"
    "<li><b>Revenue effect:</b> the government collects the tariff on the imports that remain (Q2 to Q3), the gold rectangle.</li>"
    "<li><b>Redistribution effect:</b> income moves from consumers to local producers and the government. The two red triangles are <b>deadweight losses</b>: inefficient local production and consumption that no longer happens.</li>"
    "</ul>"
    "<h3>Worked example</h3>"
    "<p>Suppose S is Q = P and D is Q = 100 &minus; P, with a world price of $20. Local output is 20 and demand 80, so imports are 60. A $15 tariff lifts the price to $35: local output rises to 35, demand falls to 65 and imports fall to 30. Tariff revenue is $15 &times; 30 = $450, and the deadweight loss is two triangles of $112.50, or $225 in total (Figure 3).</p>"
    "<h3>Tariffs in Australia and the world</h3>"
    "<p>Australia's average tariff fell from about 36 per cent in 1968&ndash;69 to about 0.4 per cent in 2025. About 90 per cent of imports now enter tariff-free, the general tariff is 5 per cent or less, and tariff revenue is about $1.9 billion, only 0.2 per cent of Commonwealth revenue. The government removed about 500 &ldquo;nuisance&rdquo; tariffs in 2024 and more than 1,000 since 2022. The world has gone the other way: the US placed a 12.5 per cent tariff on Australian goods from July 2026, and the WTO counted a record share of world imports under restrictions in 2026.</p>"
    "<p><b>Use it in an exam:</b> draw the diagram, label P<sub>w</sub>, P<sub>w+t</sub> and Q1 to Q4, and walk through the five effects. Then judge: who gains (local producers, government), who loses (consumers, firms using imported inputs, exporters if other countries retaliate), and the net loss to the economy.</p>"
    "<p>Sources: Pearson, <i>Australia in the Global Economy 2027</i>, ch. 6; WTO trade monitoring report (November 2026); Prime Minister's office (November 2026).</p>"
    + M.nav("tariffs"))
    tiles = ('<div class="k"><div><b>0.4%</b><i>Australia\'s average tariff</i><u>2025 (36% in 1968&ndash;69)</u></div>'
             '<div><b>~90%</b><i>Imports that are tariff-free</i><u>Pearson 2027</u></div>'
             '<div><b>$1.9b</b><i>Tariff revenue</i><u>0.2% of revenue</u></div>'
             '<div><b>12.5%</b><i>US tariff on Australian goods</i><u>from July 2026</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "The effect of a tariff", ed.tariff(ed.TOPIC[1], good="imports").svg(),
            "P<sub>w</sub> to P<sub>w+t</sub>: local output Q1 to Q2, consumption Q4 to Q3, imports shrink. Gold = revenue; red = deadweight loss. Not to scale."),
      B.fig(3, "Worked example: a $15 tariff", B.table(["", "Free trade", "With tariff"],
            [["Price", "$20", "$35"], ["Local output", "20", "35"], ["Quantity demanded", "80", "65"], ["Imports", "60", "30"], ["Tariff revenue", "&ndash;", "$450"], ["Deadweight loss", "&ndash;", "$225"]])),
      B.fig(4, "Australia's average tariff (%)", B.bars([("1968\u201369", 36), ("2025", 0.4)], vmax=40, fmt="%.1f%%"),
            "Average tariff on imports. Source: Pearson 2027, Figure 6.1."),
      B.fig(5, "Who gains and who loses", B.table(["Group", "Effect"],
            [["Local producers", "Gain: higher price and sales"], ["Government", "Gains revenue"], ["Consumers", "Lose: pay more, buy less"], ["Exporters", "Lose if partners retaliate"], ["Economy", "Deadweight loss"]])),
      B.tools([("lab", "Shift the tariff and watch Q1 to Q4"), ("calc", "Practise tariff revenue sums", "#skill=tariff"), ("explain", "See who wins and loses"),
               ("mcq", "Multiple choice on methods of protection", "#point=1C.2"), ("qf", "Past HSC tariff questions"), ("ef", "Latest tariff news")])]
    B.build("method-tariffs", M.C, M.CD, text, figs, "")
