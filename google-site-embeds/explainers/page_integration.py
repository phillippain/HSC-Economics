def make(B):
    c, cd = "#2447d6", "#1a3399"
    text = (
    "<h3>The global economy</h3>"
    "<p>The <b>global economy</b> is the sum of all the world's national economies and the links between them: trade in goods and services, flows of money, investment by firms, the spread of technology and the movement of people. <b>International economic integration</b> describes how closely those economies are tied together. The more integrated they are, the faster a shock in one country spreads to the others.</p>"
    "<h3>Gross World Product</h3>"
    "<p><b>Gross World Product (GWP)</b> is the total value of goods and services produced by every economy in a year. The IMF measured it at about US$126 trillion in 2026, with Australia the 12th largest economy at about US$2.1 trillion. World growth was 3.5 per cent in 2025 and is forecast at 3.1 per cent in 2026 and 3.4 per cent in 2027 (Figure 2).</p>"
    "<p>GWP is compared in two ways. <b>Market exchange rates</b> convert each country's output into US dollars. <b>Purchasing power parity (PPP)</b> adjusts for the lower prices of goods and services in poorer countries. PPP makes emerging and developing economies look larger, which is why China's share of world output is bigger on a PPP basis.</p>"
    "<h3>The dimensions of globalisation</h3>"
    "<p><b>Globalisation</b> is the increasing integration of the world's economies. Remember its parts with <b>FITT MITTC</b>: finance, investment, trade, technology, migration, international division of labour, transport and communication, and culture.</p>"
    "<ul>"
    "<li><b>Trade in goods and services.</b> World trade passed US$35 trillion in 2025 (UNCTAD). Goods trade volumes rose 4.2 per cent in 2025, and the WTO raised its 2026 forecast to 3.9 per cent in November, helped by trade in goods that power artificial intelligence.</li>"
    "<li><b>Financial flows.</b> Money moves between countries as portfolio investment, loans and currency trading. Financial markets are now so closely linked that a sell-off in one spreads within hours: when US shares fell 8 to 10 per cent in the week to 20 November 2026, Japan, Germany, Hong Kong and the ASX 200 all fell by 5 to 8 per cent.</li>"
    "<li><b>Investment and transnational corporations (TNCs).</b> Foreign direct investment (FDI) is investment that gives a firm a lasting stake in a business overseas. It rose 6 per cent to about US$1.6 trillion in UNCTAD's 2026 report. TNCs, which produce in more than one country, carry most of it. 17 of the 20 largest digital TNCs are based in the US.</li>"
    "<li><b>Technology, transport and communication.</b> Cheap shipping, the internet and now AI cut the cost of doing business across borders. About 74 per cent of the world's people use the internet, but use is far lower in the poorest countries (the digital divide).</li>"
    "<li><b>International division of labour and migration.</b> Production is split into stages, each done where it is cheapest or most skilled, forming <b>global value chains</b>. About 304 million people live outside their country of birth, and migrants sent home about US$905 billion in remittances (IOM).</li>"
    "</ul>"
    "<h3>The international and regional business cycles</h3>"
    "<p>The <b>international business cycle</b> is the pattern of booms and downturns in world output. Because economies are linked, the cycle is transmitted through trade (falling demand for exports), finance (share and bond markets), confidence and commodity prices. The 2026 oil shock is an example: the closure of the Strait of Hormuz pushed Brent crude near US$118 a barrel, lifting inflation worldwide and leading central banks, including the RBA, to raise interest rates.</p>"
    "<p><b>Regional business cycles</b> matter too. Australia's cycle is closely tied to East Asia, especially China, which buys most of its iron ore. Slower Chinese growth in 2026 (4.5 per cent in the September quarter) kept iron ore near US$90 a tonne.</p>"
    "<p><b>Use it in an exam:</b> define globalisation, then pick two or three dimensions and give a current statistic for each. Link the business cycle to transmission channels (trade, finance, confidence) and to a current event such as the 2026 oil shock.</p>"
    "<p>Sources: IMF World Economic Outlook (October 2026); WTO trade forecast (November 2026); UNCTAD World Investment Report 2026; IOM World Migration Report; ABS; Evidence Finder news items, November 2026.</p>"
    )
    tiles = ('<div class="k"><div><b>US$126tn</b><i>Gross World Product</i><u>2026, IMF</u></div>'
             '<div><b>3.1%</b><i>World growth forecast</i><u>2026, IMF</u></div>'
             '<div><b>US$1.6tn</b><i>Global FDI flows</i><u>UNCTAD 2026</u></div>'
             '<div><b>304m</b><i>International migrants</i><u>IOM</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "World growth (% a year)", B.colchart([("2019", 2.9), ("2020", -2.7), ("2021", 6.6), ("2022", 3.6), ("2023", 3.5), ("2024", 3.3), ("2025", 3.5), ("2026f", 3.1), ("2027f", 3.4)], c, -4, 8),
             "Real GWP growth at PPP. 2026 and 2027 are forecasts. Source: IMF World Economic Outlook, October 2026."),
      B.fig(3, "FITT MITTC: the dimensions of globalisation", B.table(["Dimension", "Measure to quote"],
             [["Finance", "Daily currency trading; share markets moving together"], ["Investment", "FDI about US$1.6 trillion (2025)"], ["Trade", "World trade above US$35 trillion (2025)"],
              ["Technology", "74% of people online; AI adoption"], ["Migration", "304m migrants; US$905bn remittances"], ["Int. division of labour", "Global value chains"],
              ["Transport and communication", "Container shipping, undersea cables"], ["Culture", "Global brands and media"]])),
      B.fig(4, "Share markets fell together, week to 20 November 2026 (%)", B.bars([("Nasdaq", 9.8), ("S&P 500", 8.3), ("Nikkei", 7.7), ("DAX", 7.3), ("ASX 200", 5.4), ("Hang Seng", 5.2)], vmax=12, fmt="−%.1f%%"),
             "Financial integration transmits shocks within days. Source: FNArena."),
      B.fig(5, "How a shock travels through the international business cycle", B.chain(["Oil supply shock: Strait of Hormuz closed", "Energy and transport costs rise worldwide", "Inflation rises in most economies", "Central banks raise interest rates", "Spending and world growth slow", "Demand for Australia's exports softens"])),
      B.tools([("mcq", "Test yourself on Topic 1 multiple choice"), ("qf", "Past HSC questions on globalisation"), ("ef", "Latest evidence on trade, FDI and migration"), ("essay", "Plan an essay on globalisation")])]
    B.build("international-economic-integration", c, cd, text, figs, "")
