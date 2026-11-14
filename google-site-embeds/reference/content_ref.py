# Text and data for the reference-note embeds. Figures and their sources are listed on each page.
def PAGES(hbar, line, exam, T1, T2, T4):
    P = []
    # ---------- Topic 1 ----------
    P.append(("technology", T1, "Reference notes: technology, transport and communication",
      [("6 billion", "people online in 2025, about 74% of the world"), ("94% v 23%", "online in high-income v low-income countries"), ("2.2 billion", "people still offline, mostly in poorer countries")],
      "<h3>Why it matters</h3><p>Technology is a main driver of globalisation. It cuts the cost and time of moving goods, services, money and information between countries, so more things can be traded.</p>"
      "<h3>How each one drives globalisation</h3><ul><li><b>Transport:</b> container ships, bulk carriers and air freight lower the cost per unit of moving goods. Australia can sell iron ore to Asia and buy cars from Japan at a low freight cost.</li>"
      "<li><b>Communication:</b> the internet, mobile phones and video calls let firms run global supply chains and sell services such as education, finance and software across borders.</li>"
      "<li><b>Finance:</b> electronic payments and trading move money between countries in seconds. This has grown financial flows faster than trade in goods.</li>"
      "<li><b>Production:</b> automation and artificial intelligence raise productivity, but they also change which jobs are needed and where.</li></ul>"
      "<h3>The digital divide</h3><p>Access is not equal. Almost everyone in high-income countries is online, but fewer than one in four people in low-income countries are. Countries without access miss out on the gains from trade in services. This widens the gap in living standards between nations.</p>"
      + exam("Link technology to lower costs, then to higher trade and financial flows. Use the digital divide as evidence that the gains from globalisation are shared unequally."),
      line("Share of the world's population using the internet (%)", [("2005", 2005, 16), ("2010", 2010, 29), ("2015", 2015, 40), ("2020", 2020, 59), ("2025", 2025, 74)], T1, "ITU estimates, rounded. 5G networks covered about 55% of people in 2025.", "%", ymax=100)
      + hbar("People online in 2025, by country income group (%)", [("High income", 94), ("World", 74, "#5a6580"), ("Low income", 23, "#d9822b")], T1, "", "%", vmax=100),
      [("ITU, Facts and Figures 2025", "https://www.itu.int/")]))

    P.append(("division-of-labour", T1, "Reference notes: international division of labour and migration",
      [("304 million", "international migrants in 2024, 3.7% of the world"), ("167.7 million", "migrant workers worldwide (2022)"), ("US$685 billion", "sent home to low and middle-income countries in 2024")],
      "<h3>What it means</h3><p>The international division of labour is how the world's jobs are shared between countries. Each stage of production moves to where it can be done at the lowest cost or with the best skills. A phone may be designed in the United States, use parts made in South Korea and be put together in China or India.</p>"
      "<h3>Two ways labour is used globally</h3><ul><li><b>People move to the jobs (migration):</b> skilled workers move to high-wage countries. Low-skilled workers fill shortages in jobs such as farm work, building and aged care.</li>"
      "<li><b>Jobs move to the people (offshoring):</b> firms shift factories and services such as call centres to countries with lower labour costs.</li></ul>"
      "<h3>Effects</h3><ul><li><b>Receiving countries</b> fill skill shortages and slow the ageing of their workforce. Australia relies on skilled migration for this.</li>"
      "<li><b>Sending countries</b> gain remittances, which is money workers send home. They can also lose skilled workers. This is called the brain drain.</li>"
      "<li><b>Workers:</b> labour moves far less freely than money or goods because of visa rules, language and the cost of moving. Wages still differ widely between countries.</li></ul>"
      + exam("Contrast labour with finance: capital moves in seconds, but only about 1 in 27 people live outside their country of birth. Use remittances to show a benefit for developing economies."),
      line("International migrants worldwide (millions)", [("1990", 1990, 153.9), ("2020", 2020, 275), ("2024", 2024, 304)], T1, "The number has almost doubled since 1990.", "", ymax=350, fmt="%.0f")
      + hbar("Top destination countries, 2024 (millions of migrants)", [("United States", 52.4), ("Germany", 16.8), ("Saudi Arabia", 13.7), ("United Kingdom", 11.8), ("France", 9.2)], T1),
      [("UN DESA, International Migrant Stock 2024", "https://www.un.org/development/desa/pd/"), ("ILO, Global Estimates on International Migrant Workers", "https://www.ilo.org/"), ("World Bank, Migration and Development Brief", "https://www.worldbank.org/")]))

    orgs = [("WTO", "World Trade Organization", "1995", "Sets the rules for world trade and settles trade disputes between members."),
            ("IMF", "International Monetary Fund", "1944", "Keeps the global financial system stable. Lends to countries in a balance of payments crisis, with conditions."),
            ("World Bank", "World Bank Group", "1944", "Lends to developing countries for projects that reduce poverty, such as roads, schools and health."),
            ("UN", "United Nations", "1945", "Covers peace, health, development and the environment. Runs the Sustainable Development Goals."),
            ("OECD", "Organisation for Economic Co-operation and Development", "1961", "A forum of mostly high-income economies. Researches and compares economic policy, such as tax rules.")]
    tbl = "<table><tr><th>Body</th><th>Since</th><th>Main role</th></tr>" + "".join("<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>" % (a, y, r) for a, _, y, r in orgs) + "</table>"
    P.append(("international-organisations", T1, "Reference notes: international organisations and government forums",
      [("166", "members of the WTO, covering about 98% of world trade"), ("G20", "19 countries plus the European Union and African Union"), ("G7", "seven large advanced economies")],
      "<h3>International organisations</h3>" + tbl +
      "<h3>Government economic forums</h3><ul><li><b>G20:</b> leaders of the largest advanced and emerging economies. Australia is a member. It coordinates responses to global problems, as it did in the 2008 global financial crisis.</li>"
      "<li><b>G7:</b> the United States, Japan, Germany, the United Kingdom, France, Italy and Canada. Australia is not a member but is often invited.</li></ul>",
      hbar("Number of member countries", [("United Nations", 193), ("IMF", 191), ("World Bank", 189), ("WTO", 166), ("OECD", 38)], T1, "Australia is a member of all five.")
      + "<h3>How well do they work?</h3><ul><li><b>Strengths:</b> shared rules lower trade barriers, crisis loans stop problems spreading, and forums let countries act together.</li>"
      "<li><b>Limits:</b> decisions need agreement, so progress is slow. The WTO's Doha Round of talks stalled, and its appeals body has not been able to hear cases since 2019. Large economies can act alone, as the United States has with tariffs.</li>"
      "<li><b>Criticism:</b> IMF loan conditions can force spending cuts that hurt the poor. Voting power in the IMF and World Bank favours rich countries.</li></ul>"
      + exam("Name the body, state its role, give one example of it acting, then judge it. A top answer weighs a strength against a limit."),
      [("WTO", "https://www.wto.org/"), ("IMF", "https://www.imf.org/"), ("World Bank", "https://www.worldbank.org/"), ("OECD", "https://www.oecd.org/"), ("G20", "https://g20.org/")]))

    P.append(("local-content", T1, "Reference notes: local content rules",
      [("10%", "of Australian program spending that large streaming services must put into new Australian content"), ("7.5%", "of Australian revenue, the other way to meet the streaming rule"), ("55%", "Australian content required on commercial free-to-air main channels, 6 am to midnight")],
      "<h3>What they are</h3><p>A local content rule says that a set share of a good or service must be made in the home country. It is a form of protection. It does not tax imports as a tariff does. It guarantees local producers a share of the market.</p>"
      "<h3>How they work</h3><ul><li>A firm must use a minimum share of local parts, workers or programs to sell in the market or to win a government contract.</li>"
      "<li>Demand for the local product rises, so local output and jobs are higher than they would be under free trade.</li>"
      "<li>The government collects no revenue, unlike a tariff. The cost is hidden in higher prices or less choice.</li></ul>"
      "<h3>Australian example: streaming services</h3><p>A law passed in November 2025 applies from 1 January 2026. Streaming services with more than one million Australian subscribers must invest in new Australian drama, children's, documentary, arts and educational programs. They can spend 10 per cent of what they spend on programs for Australia, or 7.5 per cent of their Australian revenue. The rule is phased in over three years and will be reviewed after four.</p>"
      + exam("Treat local content rules like a quota. Explain who gains (local producers and workers) and who pays (consumers and firms that face higher costs), then judge the effect on efficiency."),
      "<h3>Who gains and who loses</h3><table><tr><th>Gains</th><th>Costs</th></tr>"
      "<tr><td>Local producers get a guaranteed share of sales.</td><td>Firms must buy local inputs even when imports are cheaper or better.</td></tr>"
      "<tr><td>Jobs and skills are kept in the protected industry.</td><td>Costs can be passed on to consumers as higher prices.</td></tr>"
      "<tr><td>Cultural goals are met, such as Australian stories on screen.</td><td>Resources stay in industries where Australia may lack comparative advantage.</td></tr>"
      "<tr><td>No cost to the budget.</td><td>Trading partners may object or retaliate. Rules can breach trade agreements.</td></tr></table>"
      "<h3>Other examples</h3><ul><li>Local content quotas for Australian music on commercial radio.</li><li>Government purchasing rules that favour local suppliers.</li><li>Rules of origin in free trade agreements, which set how much of a good must be made in a member country to get the lower tariff.</li></ul>",
      [("Office for the Arts, Australian content on streaming services", "https://www.arts.gov.au/"), ("ACMA, Australian content rules", "https://www.acma.gov.au/")]))

    # ---------- Topic 2 ----------
    P.append(("trade-financial-flows", T2, "Reference notes: value, composition and direction of trade and financial flows",
      [("30.4%", "of Australia's exports went to China in 2024"), ("$638.9 billion", "net foreign liabilities, June quarter 2026"), ("$27.2 billion", "current account deficit, June quarter 2026")],
      "<h3>Value</h3><p>Trade is worth close to half of Australia's GDP when exports and imports are added. Export values swing with commodity prices. When iron ore and coal prices fall, export income falls even if volumes hold.</p>"
      "<h3>Composition: what Australia trades</h3><ul><li><b>Exports</b> are led by minerals and energy. Iron ore, coal and natural gas are the three largest. Services such as education and tourism come next, then farm goods.</li>"
      "<li><b>Imports</b> are mostly manufactured goods and fuel: refined petroleum, cars, phones and computers. Refined petroleum imports rose 25.5 per cent to $55.1 billion in 2025-26 as fuel prices climbed.</li>"
      "<li>This pattern reflects comparative advantage. Australia is rich in resources and land, and has a small manufacturing base.</li></ul>"
      "<h3>Direction: who Australia trades with</h3><p>Trade has shifted from Europe to Asia. China is the largest partner by a wide margin, then Japan, South Korea, the United States and India. Relying on one buyer is a risk, as China's trade restrictions in 2020 showed.</p>"
      "<h3>Financial flows</h3><ul><li>Australia saves less than it invests, so it borrows from and sells assets to the rest of the world. This is a financial account surplus that matches the current account deficit.</li>"
      "<li>The United States and the United Kingdom are the largest sources of foreign investment. Most is portfolio investment (shares and debt), not direct investment.</li>"
      "<li>Australia owes more than it owns overseas, so net income flows out each quarter.</li></ul>"
      + exam("Give one figure for each of value, composition and direction, then explain a trend. Link the export mix to the terms of trade and the current account."),
      hbar("Australia's three largest exports ($ billion)", [("Iron ore (2025)", 120.8), ("Natural gas (2024)", 67.5), ("Coal (2025)", 64.1)], T2, "Iron ore was 18.1% and coal 9.6% of all exports in 2025.")
      + hbar("China's share of Australia's trade, 2024 (%)", [("Exports to China", 30.4), ("Imports from China", 18.8, "#5a6580")], T2, "No other partner takes more than about half this share of exports.", "%", vmax=40),
      [("DFAT, Trade and investment at a glance", "https://www.dfat.gov.au/"), ("ABS, Balance of Payments and International Investment Position", "https://www.abs.gov.au/"), ("ABS, International Trade in Goods", "https://www.abs.gov.au/")]))

    P.append(("protection-policy", T2, "Reference notes: Australia's free trade and protection policies",
      [("Over 90%", "of imports by value now enter Australia duty free"), ("5%", "the highest general tariff rate today, down from as much as 125% in 1985"), ("$16.8 billion", "budgetary assistance to industry in 2024-25")],
      "<h3>From protection to free trade</h3><p>Until the 1970s Australia protected its factories with some of the highest tariffs in the developed world. Governments then cut protection in steps: a 25 per cent across-the-board cut in 1973, phased cuts from 1988 and 1991, and the end of import quotas. The aim was to force firms to compete and to shift resources to industries where Australia has a comparative advantage.</p>"
      "<h3>Where protection stands now</h3><ul><li>Tariffs are low. From 1 July 2024 the government removed 457 nuisance tariffs that raised little revenue.</li>"
      "<li>Tariffs raised $1.9 billion, but cost firms between $1.4 billion and $4.1 billion to comply with. The Productivity Commission argues the rest should go.</li>"
      "<li>Help for industry has moved from tariffs to the budget: grants, tax concessions and subsidies, such as support for local manufacturing and clean energy.</li>"
      "<li>The effective rate of assistance to manufacturing is about 4 per cent, far below past levels.</li></ul>"
      "<h3>Effects on the economy</h3><ul><li><b>Gains:</b> lower prices and more choice for consumers, cheaper inputs for firms, higher productivity, and stronger export industries.</li>"
      "<li><b>Costs:</b> structural unemployment as protected industries shrank. Car making ended in 2017. Job losses fell on particular regions and workers.</li></ul>"
      + exam("Explain the reasons for cutting protection, then weigh the long-run efficiency gains against the short-run structural costs. Note that industry help is now mostly paid through the budget."),
      line("Tariff on imported passenger cars (%)", [("1987", 1987, 57.5), ("", 1988, 45), ("1992", 1992, 35), ("", 1996, 25), ("2000", 2000, 15), ("", 2005, 10), ("2010", 2010, 5)], T2, "Rates fell in yearly steps between the dates shown. The rate has been 5% since 2010.", "%", ymax=70)
      + hbar("Tariffs: revenue raised v cost to firms ($ billion)", [("Revenue raised", 1.9), ("Compliance cost (low)", 1.4, "#d9822b"), ("Compliance cost (high)", 4.1, "#d9822b")], T2, "Productivity Commission estimates. The cost of complying may be larger than the revenue."),
      [("Productivity Commission, Trade and Assistance Review 2024-25", "https://www.pc.gov.au/"), ("DFAT, About free trade agreements", "https://www.dfat.gov.au/")]))

    ftas = [(1983, "New Zealand"), (2003, "Singapore"), (2005, "United States, Thailand"), (2009, "Chile"), (2010, "ASEAN and New Zealand (AANZFTA)"), (2013, "Malaysia"), (2014, "South Korea"),
            (2015, "Japan, China"), (2018, "CPTPP (11 Pacific Rim partners)"), (2020, "Hong Kong, Peru, Indonesia, PACER Plus"), (2022, "RCEP, India"), (2023, "United Kingdom"), (2025, "United Arab Emirates")]
    counts = {1983: 1, 2003: 2, 2005: 4, 2009: 5, 2010: 6, 2013: 7, 2014: 8, 2015: 10, 2018: 11, 2020: 15, 2022: 17, 2023: 18, 2025: 19}
    lab = {1983: "1983", 2005: "2005", 2015: "2015", 2025: "2025"}
    pts = [(lab.get(y, ""), y, n) for y, n in sorted(counts.items())]
    tbl2 = "<table><tr><th>In force</th><th>Partner</th></tr>" + "".join("<tr><td>%d</td><td>%s</td></tr>" % f for f in ftas) + "</table>"
    P.append(("free-trade-agreements", T2, "Reference notes: Australia's free trade agreements",
      [("19", "free trade agreements in force: 15 bilateral and 4 with groups of countries"), ("78%", "of Australia's trade is with free trade agreement partners"), ("88%", "the share once the agreement with the European Union starts")],
      "<h3>What they do</h3><p>A free trade agreement (FTA) removes or lowers tariffs and other barriers between the countries that sign it. A <b>bilateral</b> agreement has two members. A <b>multilateral</b> or regional agreement has many.</p>"
      "<h3>Why Australia signs them</h3><ul><li>World Trade Organization talks have stalled, so deals with single partners or regions are the faster way to open markets.</li>"
      "<li>Exporters of beef, wine, minerals and services gain lower tariffs in large markets.</li><li>Consumers and firms pay less for imports.</li>"
      "<li>Deals with many partners spread risk. The government has pushed to diversify trade away from reliance on China.</li></ul>"
      "<h3>The newest deals</h3><ul><li><b>United Arab Emirates:</b> in force from 1 October 2025. It is Australia's first agreement in the Middle East.</li>"
      "<li><b>European Union:</b> talks concluded on 24 March 2026 after years of dispute over farm access. It starts once both sides have signed and ratified it.</li></ul>"
      "<h3>Limits</h3><ul><li><b>Trade diversion:</b> buying from a partner because its goods are tariff free, even when another country makes them more cheaply.</li>"
      "<li>Rules of origin add paperwork, so some firms do not use the lower rates.</li><li>Sensitive sectors, such as farm goods, are often left out or opened slowly.</li></ul>"
      + exam("Name two agreements with dates, explain trade creation and trade diversion, and judge whether bilateral deals are a good substitute for global free trade."),
      line("Number of Australia's free trade agreements in force", pts, T2, "Most have been signed since 2003, and most partners are in Asia and the Pacific.", "", ymax=20, step=True, fmt="%d")
      + tbl2,
      [("DFAT, Free trade agreements in force", "https://www.dfat.gov.au/"), ("DFAT, Australia-European Union FTA", "https://www.dfat.gov.au/")]))

    # ---------- Topic 4 ----------
    P.append(("environment-context", T4, "Reference notes: environmental management in a national and global context",
      [("23.3%", "fall in Australia's emissions from 2005 to 2024"), ("43%", "cut on 2005 levels by 2030, the target set in law"), ("62 to 70%", "cut by 2035, the target announced in September 2025")],
      "<h3>Why governments act</h3><p>Pollution is a negative externality. Firms and households do not pay the full cost of the damage they cause, so the market produces too much of it. This is market failure. Governments step in so that growth today does not reduce living standards for future generations. This goal is called ecologically sustainable development.</p>"
      "<h3>National context: Australia's main tools</h3><ul><li><b>Targets:</b> 43 per cent below 2005 levels by 2030, 62 to 70 per cent by 2035 and net zero by 2050.</li>"
      "<li><b>Safeguard Mechanism:</b> the largest industrial sites must cut emissions each year or buy credits. This puts a price on their pollution.</li>"
      "<li><b>Renewable energy:</b> a goal of 82 per cent renewable electricity by 2030, backed by government underwriting of new wind, solar and storage.</li>"
      "<li><b>Regulation and spending:</b> vehicle emission standards, and rebates for home batteries and efficient appliances.</li></ul>"
      "<h3>Global context</h3><ul><li>Climate change is a global problem, so one country acting alone cannot fix it. Each has an incentive to let others bear the cost. This is the free rider problem.</li>"
      "<li><b>Paris Agreement (2015):</b> countries agreed to hold warming well below 2 degrees and to aim for 1.5 degrees. Each sets its own target and updates it every five years.</li>"
      "<li>Trade partners are acting too. The European Union now charges for the carbon in some imports, which affects exporters.</li></ul>"
      "<h3>The trade-off</h3><p>Australia earns large export income from coal and gas. Cutting emissions means structural change: some regions lose jobs while new industries grow. Official projections in 2025 showed a 48 per cent cut by 2035 on current policies, so more action is needed to reach the target.</p>"
      + exam("Define the market failure, name a policy and how it changes incentives, then weigh the environmental gain against the short-run cost to growth, jobs and prices."),
      line("Australia's greenhouse gas emissions (million tonnes CO2-e)", [("2005", 2005, 607.7), ("2015", 2015, 537.5), ("2020", 2020, 476.6), ("2024", 2024, 466.4)], T4,
           "Solid line is actual. Dashed line shows the targets: 43% below 2005 by 2030 and 62% (upper end of the 2035 range). A 70% cut would be about 182 million tonnes.", "", ymax=700, fmt="%.0f",
           extra=[("2030", 2030, 346.4, "346"), ("2035", 2035, 230.9, "231")])
      + hbar("Cut in emissions from 2005 levels (%)", [("Achieved by 2024", 23.3), ("Projected for 2035", 48, "#5a6580"), ("2030 target", 43, "#b8860b"), ("2035 target (low)", 62, "#b8860b"), ("2035 target (high)", 70, "#b8860b")], T4, "Emissions fell a further 1.6% in the year to March 2026.", "%", vmax=80),
      [("DCCEEW, National Greenhouse Gas Inventory", "https://www.dcceew.gov.au/"), ("DCCEEW, Australia's emissions projections 2025", "https://www.dcceew.gov.au/"), ("UNFCCC, The Paris Agreement", "https://unfccc.int/")]))
    return P
