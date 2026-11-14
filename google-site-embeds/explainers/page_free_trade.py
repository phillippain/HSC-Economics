def make(B):
    c, cd = "#0e8a8a", "#0a6666"
    ed = B.ed
    text = (
    "<h3>Free trade and protection</h3>"
    "<p><b>Free trade</b> means goods and services move between countries without barriers imposed by governments. <b>Protection</b> is any government action that gives local producers an advantage over foreign competitors. The main methods are tariffs (a tax on imports), subsidies (payments to local producers), quotas (limits on the volume of imports) and local content rules.</p>"
    "<h3>Australia's policies: from protection to free trade</h3>"
    "<p>Until the 1970s Australia protected its manufacturers with some of the highest tariffs in the developed world. The aim was to build local industry and jobs. The cost was high prices for consumers and firms that had little reason to become efficient.</p>"
    "<p>Governments then cut protection in steps. Tariffs were cut by 25 per cent across the board in 1973, and phased cuts followed from 1988 and 1991. Import quotas were removed. The tariff on imported cars fell from 57.5 per cent in 1987 to 5 per cent in 2010 (Figure 3).</p>"
    "<p>Protection is now very low.</p>"
    "<ul><li>The highest general tariff is 5 per cent, and more than 90 per cent of imports by value enter duty free.</li>"
    "<li>From 1 July 2024 the government removed 457 nuisance tariffs that raised little revenue.</li>"
    "<li>Tariffs raise about $1.9 billion a year, but cost firms between $1.4 billion and $4.1 billion to comply with (Figure 5). The Productivity Commission argues the rest should go.</li>"
    "<li>Help for industry has moved from tariffs to the budget. Grants, tax concessions and subsidies were worth $16.8 billion in 2024-25, including support for local manufacturing and clean energy.</li></ul>"
    "<h3>Why Australia reduced protection</h3>"
    "<p>A tariff raises the price of imports, so consumers pay more and buy less, and resources are held in industries that cannot compete (Figure 2). Removing it reverses these effects. Firms must compete with imports, so they lift productivity or close. Resources then move to industries where Australia has a comparative advantage, such as mining, agriculture and services (Figure 6).</p>"
    "<h3>Free trade agreements</h3>"
    "<p>A free trade agreement (FTA) removes or lowers barriers between the countries that sign it. Australia is a member of the World Trade Organization (WTO), which sets global trade rules, but WTO talks have stalled. Australia has turned to agreements with single partners and regions. It has 19 in force, covering about 78 per cent of its trade.</p>"
    "<p><b>Bilateral agreements</b> have two members.</p>"
    "<ul><li><b>China-Australia Free Trade Agreement (2015):</b> removed tariffs on most Australian exports to its largest market, including beef, dairy, wine and resources.</li>"
    "<li><b>Australia-United States Free Trade Agreement (2005):</b> removed most tariffs on trade between the two countries.</li></ul>"
    "<p><b>Multilateral (regional) agreements</b> have many members.</p>"
    "<ul><li><b>Comprehensive and Progressive Agreement for Trans-Pacific Partnership (CPTPP, 2018):</b> links Australia with Japan, Canada, Mexico, Vietnam and other Pacific economies. The United Kingdom has since joined.</li>"
    "<li><b>Regional Comprehensive Economic Partnership (RCEP, 2022):</b> fifteen members, including China, Japan, South Korea and the ten ASEAN countries. It is the world's largest trade agreement by the size of its members' economies.</li></ul>"
    "<p>FTAs open markets for exporters and lower import prices. Their main weakness is <b>trade diversion</b>: buying from a partner because its goods are tariff free, even when another country produces them more cheaply. The Free Trade Agreements page has more detail.</p>"
    "<h3>Implications for individuals, firms and governments</h3>"
    "<ul><li><b>Individuals:</b> consumers gain lower prices and more choice, which raises real incomes. Workers in industries that lose protection can face structural unemployment. Car making in Australia ended in 2017, and the job losses fell on particular regions.</li>"
    "<li><b>Firms:</b> exporters gain access to larger markets and cheaper inputs. Import-competing firms face more competition and must become more efficient, change what they make or close.</li>"
    "<li><b>Governments:</b> tariff revenue falls, and governments face pressure to help the workers and regions affected. In the long run a more productive economy raises growth and tax revenue.</li></ul>"
    "<h3>Protection by other countries and trading blocs</h3>"
    "<p>Australia gains little if its trading partners keep their own barriers (Figure 8).</p>"
    "<ul><li><b>United States:</b> since 2025 the United States has placed tariffs on almost all trading partners. In August 2026 most Australian goods faced a 12.5 per cent tariff, and steel and aluminium faced rates of up to 50 per cent. Beef and gold were exempt. This is despite the free trade agreement between the two countries.</li>"
    "<li><b>China:</b> from 2020 China placed tariffs and bans on Australian barley, wine, coal, beef and lobster during a political dispute. The restrictions were lifted by the end of 2024. They showed the risk of relying on one market.</li>"
    "<li><b>European Union:</b> a trading bloc that subsidises and protects its farmers, which limits Australian farm exports. It now also charges for the carbon content of some imports. Australia and the European Union concluded talks on a free trade agreement in March 2026.</li></ul>"
    "<p>The direct effect of foreign protection is lower export income for the industries targeted. The indirect effect can be larger. Trade wars slow world growth and reduce the demand of Australia's main customers, especially China, for commodities.</p>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Topic 1:</b> the methods of protection and their diagrams are covered in The Global Economy.</li>"
    "<li><b>Trade flows:</b> lower protection and FTAs have shaped the direction of Australia's trade.</li>"
    "<li><b>Microeconomic policy:</b> cutting protection is a microeconomic reform that raises productivity.</li></ul>"
    "<p><b>Use it in an exam:</b> describe how protection has fallen, name two bilateral and two multilateral agreements with dates, then weigh the long-run efficiency gains against the short-run structural costs for individuals, firms and governments.</p>"
    "<p>Sources: <a href=\"https://www.pc.gov.au/\">Productivity Commission</a>, Trade and Assistance Review; <a href=\"https://www.dfat.gov.au/\">Department of Foreign Affairs and Trade</a>, free trade agreements; <a href=\"https://export.business.gov.au/pricing-costs-and-finance/tariffs-taxes-and-duties/us-tariff-rates-and-exemptions\">Australian Government, US tariff rates and exemptions</a>.</p>")
    tiles = ('<div class="k"><div><b>5%</b><i>Highest general tariff</i><u>Down from 57.5% on cars in 1987</u></div><div><b>Over 90%</b><i>of imports enter duty free</i><u>By value</u></div>'
             '<div><b>19</b><i>Free trade agreements in force</i><u>About 78% of trade</u></div><div><b>12.5%</b><i>US tariff on most Australian goods</i><u>From 24 July 2026</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "The effect of a tariff", ed.tariff(ed.TOPIC[2], good="cars").svg(), "A tariff lifts the price from P<sub>w</sub> to P<sub>w+t</sub>. Local output rises from Q<sub>1</sub> to Q<sub>2</sub>, demand falls from Q<sub>4</sub> to Q<sub>3</sub> and imports shrink. Removing the tariff reverses this. Not to scale."),
      B.fig(3, "Tariff on imported passenger cars (%)", B.linechart([("1987", 1987, 57.5), ("", 1988, 45), ("1992", 1992, 35), ("", 1996, 25), ("2000", 2000, 15), ("", 2005, 10), ("2010", 2010, 5)], c, 60), "Rates fell in yearly steps between the dates shown. The rate has been 5% since 2010."),
      B.fig(4, "Four agreements to know", B.table(["Agreement", "Type", "In force"], [["China (ChAFTA)", "Bilateral", "2015"], ["United States (AUSFTA)", "Bilateral", "2005"], ["CPTPP", "Multilateral", "2018"], ["RCEP", "Multilateral", "2022"]])),
      B.fig(5, "Tariffs: revenue raised and cost to firms ($ billion)", B.bars([("Revenue raised", 1.9), ("Compliance cost, low", 1.4), ("Compliance cost, high", 4.1)], fmt="%.1f"), "Productivity Commission estimates. The cost of complying may be larger than the revenue."),
      B.fig(6, "How lower protection raises living standards", B.chain(["Tariffs are cut", "Imports become cheaper for consumers and firms", "Local firms must compete or close", "Resources move to more efficient industries", "Productivity and exports rise", "Real incomes rise, but some workers lose jobs in the short run"])),
      B.fig(7, "Who is affected by lower protection", B.table(["Group", "Gains", "Costs"], [["Individuals", "Lower prices, more choice", "Job losses in protected industries"], ["Firms", "Cheaper inputs, larger markets", "More competition from imports"], ["Governments", "Higher growth in the long run", "Less tariff revenue, adjustment costs"]])),
      B.fig(8, "Protection by other countries", B.table(["Who", "Measure", "Effect on Australia"], [["United States", "Tariffs of 12.5%, and up to 50% on steel and aluminium", "Exports to the US cost more; world growth slows"], ["China", "Tariffs and bans on barley, wine, coal and more, 2020 to 2024", "Exporters lost their main market and had to find others"], ["European Union", "Farm subsidies and a carbon charge on imports", "Limits farm exports; raises costs for some exporters"]])),
      B.tools([("explain", "See who gains and loses from a tariff"), ("lab", "Draw tariff, quota and subsidy diagrams"), ("chain", "Build the chain from tariff cut to living standards"), ("ef", "News on tariffs and trade deals"),
               ("qf", "Past HSC questions on protection"), ("mcq", "Section I questions with explanations"), ("glance", "Latest trade figures"), ("gloss", "Tariff, quota, trade diversion and more")]),
    ]
    B.build("free-trade-protection", c, cd, text, figs, "")
