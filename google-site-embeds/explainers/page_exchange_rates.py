def make(B):
    c, cd = "#0e8a8a", "#0a6666"
    ed = B.ed
    d = ed.Diagram("Price of AUD (US¢)", "Quantity of AUD", color=ed.TOPIC[2])
    d.line("D", (0.8, 9.2), (9.2, 0.8)); d.line("S1", (1.0, 1.4), (7.6, 8.0), "grey"); d.line("S2", (3.0, 1.0), (9.6, 7.6), "red")
    d.shift("S1", "S2"); d.point("D", "S1", "e1", "Q1"); d.point("D", "S2", "e2", "Q2", color="red")
    text = (
    "<h3>What an exchange rate is</h3>"
    "<p>An exchange rate is the price of one currency in terms of another. If the Australian dollar (AUD) is worth 68 United States (US) cents, then A$1 buys US$0.68. Exchange rates matter because every export, import and overseas investment needs one currency to be swapped for another.</p>"
    "<h3>How the exchange rate is measured</h3>"
    "<ul><li><b>Against individual currencies:</b> the rate most often quoted is against the US dollar, because most world trade and commodities are priced in it. The dollar is also quoted against the yen, the euro, the yuan and others. It can rise against one currency while it falls against another.</li>"
    "<li><b>Trade Weighted Index (TWI):</b> an index that measures the dollar against a basket of the currencies of Australia's trading partners. Each currency is weighted by its share of Australia's trade, so China has the largest weight. The TWI shows the overall movement of the dollar. Its base is May 1970 = 100.</li></ul>"
    "<p>To convert, multiply Australian dollars by the rate. At US$0.68, A$500 buys 500 &times; 0.68 = US$340. To go the other way, divide: US$340 &divide; 0.68 = A$500.</p>"
    "<h3>Demand for and supply of Australian dollars</h3>"
    "<p>Since December 1983 the value of the dollar has been set by demand and supply in the foreign exchange market.</p>"
    "<p><b>Demand</b> comes from people who need Australian dollars: foreigners buying Australian exports, foreign investors buying Australian assets or lending to Australians, and speculators who expect the dollar to rise.</p>"
    "<p><b>Supply</b> comes from people selling Australian dollars to buy other currencies: Australians buying imports, Australians investing overseas, payments of interest and dividends to foreign owners, and speculators who expect the dollar to fall.</p>"
    "<p>The main factors that shift these curves are listed in Figure 4.</p>"
    "<ul><li><b>Commodity prices and the terms of trade:</b> higher prices for iron ore, coal and gas raise export income and the demand for dollars.</li>"
    "<li><b>Interest rate differentials:</b> if Australian interest rates rise relative to those overseas, foreign savers buy dollars to invest here.</li>"
    "<li><b>Relative inflation:</b> higher inflation in Australia makes exports less competitive and imports more attractive, which lowers demand and raises supply.</li>"
    "<li><b>Economic growth:</b> strong growth overseas lifts demand for Australian exports. Strong growth at home draws in imports and raises supply.</li>"
    "<li><b>Expectations and sentiment:</b> speculators buy or sell on what they expect to happen. The dollar tends to fall when global investors become cautious.</li></ul>"
    "<h3>Appreciation and depreciation</h3>"
    "<p>An <b>appreciation</b> is a rise in the value of the dollar under a floating rate. It happens when demand increases or supply decreases (Figure 2). A <b>depreciation</b> is a fall in its value, when supply increases or demand decreases (Figure 3).</p>"
    "<p>The dollar was worth 68.04 US cents on 13 November 2026, up 3.8 per cent over the year. Rising Australian interest rates were one reason: the cash rate was raised five times in 2026. Over the longer term the dollar has ranged from about 48 US cents in 2001 to above US$1.10 in 2011, at the height of the mining boom.</p>"
    "<h3>How exchange rates are determined</h3>"
    "<p>There are three systems (Figure 5).</p>"
    "<ul><li><b>Floating:</b> market forces set the rate with no official target. Australia has had a floating rate since 1983.</li>"
    "<li><b>Fixed:</b> the government or central bank sets the rate and must buy or sell currency to hold it there. A rise in a fixed rate is a revaluation and a fall is a devaluation. Australia had a fixed rate until the 1970s.</li>"
    "<li><b>Managed:</b> the rate moves, but within limits set by the central bank. Australia used a managed rate, adjusted each day, from 1976 until the float.</li></ul>"
    "<h3>The influence of the Reserve Bank</h3>"
    "<p>The Reserve Bank of Australia (RBA) does not set the exchange rate, but it can influence it in two ways.</p>"
    "<ul><li><b>Direct intervention (dirtying the float):</b> the RBA buys Australian dollars with its reserves of foreign currency to support the rate, or sells dollars to lower it. It does this rarely, and mainly when the market is disorderly, as in the global financial crisis of 2008. Its reserves are small compared with the size of the market.</li>"
    "<li><b>Indirect influence through monetary policy:</b> a higher cash rate attracts foreign funds and tends to appreciate the dollar. The RBA sets the cash rate for inflation and employment, so this is a side effect and not a tool for managing the dollar.</li></ul>"
    "<h3>Effects of exchange rate changes</h3>"
    "<p>A <b>depreciation</b> has these effects (Figures 6 and 7).</p>"
    "<ul><li><b>Trade:</b> exports become cheaper for foreign buyers and imports dearer for Australians. Export and import-competing industries become more competitive, and the balance on goods and services should improve over time.</li>"
    "<li><b>Inflation:</b> import prices rise, which adds to imported inflation.</li>"
    "<li><b>Foreign debt:</b> debt owed in foreign currencies costs more to repay in Australian dollars. This is the valuation effect.</li>"
    "<li><b>Income:</b> interest payments on foreign-currency debt rise, which worsens net primary income.</li>"
    "<li><b>Growth:</b> higher net exports add to aggregate demand and employment.</li></ul>"
    "<p>An <b>appreciation</b> has the opposite effects. Imports and overseas travel become cheaper, which lowers inflation and helps consumers. Exporters and firms that compete with imports lose competitiveness, and the foreign debt is worth less in Australian dollars.</p>"
    "<p>A floating rate also works as a shock absorber. When commodity prices fall, the dollar usually depreciates, which makes other exports more competitive and softens the fall in national income.</p>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Balance of payments:</b> credits create demand for dollars and debits create supply.</li>"
    "<li><b>Inflation:</b> a depreciation is a source of imported inflation.</li>"
    "<li><b>Monetary policy:</b> the exchange rate is one channel through which the cash rate affects the economy.</li></ul>"
    "<p><b>Use it in an exam:</b> draw the market for Australian dollars, shift the correct curve and label the old and new rates. Name the factor that caused the shift, then trace the effects on exporters, importers, inflation and foreign debt.</p>"
    "<p>Sources: <a href=\"https://www.rba.gov.au/\">Reserve Bank of Australia</a>, exchange rate statistics and explainers.</p>")
    tiles, js = B.live([("audchg", "AUD/USD, change over the year", "+3.8%", "Year to 13 Nov 2026"), ("twi", "Trade Weighted Index", "63.3", "13 Nov 2026"),
                        ("cash", "Cash rate target", "4.85%", "4 Nov 2026"), ("tot", "Terms of trade, change in the quarter", "−1.6%", "Jun qtr 2026")])
    figs = [
      B.fig(1, "Latest figures", tiles, "These update by themselves from Economy at a Glance. The dollar was 68.04 US cents on 13 November 2026."),
      B.fig(2, "Appreciation: demand for dollars increases", ed.fx_market(ed.TOPIC[2], show_counterfactual=False).svg(), "D<sub>1</sub> to D<sub>2</sub> raises the exchange rate from e<sub>1</sub> to e<sub>2</sub>. Causes include higher commodity prices or higher Australian interest rates. Not to scale."),
      B.fig(3, "Depreciation: supply of dollars increases", d.svg(), "S<sub>1</sub> to S<sub>2</sub> lowers the exchange rate from e<sub>1</sub> to e<sub>2</sub>. Causes include higher spending on imports or more Australian investment overseas. Not to scale."),
      B.fig(4, "What shifts demand and supply", B.table(["Demand for dollars rises when", "Supply of dollars rises when"], [["Commodity prices rise", "Australians buy more imports"], ["Australian interest rates rise relative to overseas", "Overseas interest rates rise relative to Australia"], ["Trading partners grow faster", "The Australian economy grows faster"], ["Foreign investment in Australia rises", "Australians invest more overseas"], ["Speculators expect the dollar to rise", "Speculators expect the dollar to fall"]])),
      B.fig(5, "Three exchange rate systems", B.table(["System", "Who sets the rate", "In Australia"], [["Fixed", "Government or central bank", "Until the 1970s"], ["Managed", "Market, within official limits", "1976 to 1983"], ["Floating", "Demand and supply", "Since December 1983"]])),
      B.fig(6, "How a depreciation works through the economy", B.chain(["The Australian dollar depreciates", "Exports are cheaper overseas and imports are dearer here", "Export volumes rise and import volumes fall", "Net exports and aggregate demand rise", "Growth and employment rise", "Import prices add to inflation"])),
      B.fig(7, "Who gains and who loses from a depreciation", B.table(["Gains", "Loses"], [["Exporters, such as miners and farmers", "Consumers buying imports or travelling overseas"], ["Firms that compete with imports", "Firms that import inputs or equipment"], ["Tourism and education providers", "Borrowers with foreign-currency debt"], ["Australians with assets overseas", "Households, through higher inflation"]])),
      B.tools([("fx", "Shift demand and supply for the dollar"), ("glance", "Latest dollar, TWI and cash rate"), ("bop", "Link credits and debits to the dollar"), ("chain", "Build the chain from a depreciation"),
               ("calc", "Practise currency conversions"), ("qf", "Past HSC questions on exchange rates"), ("mcq", "Section I questions with explanations"), ("gloss", "TWI, appreciation, dirty float and more")]),
    ]
    B.build("exchange-rates", c, cd, text, figs, js)
