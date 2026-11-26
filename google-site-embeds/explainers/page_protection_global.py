def make(B):
    c, cd = "#2447d6", "#1a3399"
    ed = B.ed
    text = (
    "<h3>Protection in the global economy</h3>"
    "<p><b>Protection</b> is any government action that gives domestic producers an advantage over foreign competitors. It runs against the gains from free trade, so governments that use it need a reason. The syllabus asks for four: the infant industry argument, domestic employment, dumping and defence. Then it asks for the methods and their effects on the domestic and the global economy.</p>"
    "<h3>Reasons for protection</h3>"
    "<ul>"
    "<li><b>Infant industry argument.</b> A new industry may have high costs at first because it is too small to gain economies of scale. Temporary protection lets it grow until it can compete. The weakness is that protection is hard to remove, and the industry may never grow up.</li>"
    "<li><b>Domestic employment.</b> Protection saves jobs in industries facing import competition, which can ease the pain of structural change in regions such as steel towns. But the cost per job saved is usually high, and jobs are lost elsewhere, in exporters and in firms that use the protected product.</li>"
    "<li><b>Dumping.</b> Dumping is selling exports below their normal price at home, or below the cost of making them, often backed by government subsidies. Anti-dumping duties are allowed under WTO rules. Australia's Anti-Dumping Commission has placed duties on products such as Chinese steel and aluminium. Trade remedy investigations are rising: the WTO counted 218 new ones in the first half of 2026.</li>"
    "<li><b>Defence and national security.</b> Countries want to make goods essential in a war or a crisis, such as steel, ships, medicines and computer chips. Since COVID and the 2026 oil shock, this argument has widened to <b>supply-chain security</b>: China refines more than 90 per cent of several critical minerals, so the US, Australia and others are subsidising their own processing.</li>"
    "</ul>"
    "<p>Other reasons are sometimes given: retaliation against another country's barriers, raising government revenue, and protecting the environment or labour standards.</p>"
    "<h3>Methods of protection</h3>"
    "<p>The methods are <b>tariffs, subsidies, quotas, local content rules and export incentives</b>. Each is explained, with a diagram, on the <a href=\"https://sites.google.com/education.nsw.gov.au/hsceconomics-at-sscbwb/topic-1/protection/methods\"><b>Methods of protection</b></a> page. A tariff is the most common: it raises the domestic price from P<sub>w</sub> to P<sub>w+t</sub>, so local output rises, consumption falls and imports shrink (Figure 3).</p>"
    "<h3>Effects on the domestic economy</h3>"
    "<ul>"
    "<li>Consumers pay higher prices and have less choice.</li>"
    "<li>Protected firms gain sales and profits, but have less reason to become efficient, so resources are misallocated.</li>"
    "<li>Firms that use protected inputs face higher costs, which makes their own products less competitive.</li>"
    "<li>The government gains tariff revenue but pays for subsidies and export incentives.</li>"
    "</ul>"
    "<h3>Effects on the global economy</h3>"
    "<ul>"
    "<li>World trade and growth are lower, because countries no longer specialise according to comparative advantage.</li>"
    "<li>Protection invites <b>retaliation</b>. In 2025 the US raised tariffs on Chinese goods by up to 145 per cent and China replied with 125 per cent; both later pulled back, but average tariffs between them were still about 35 and 32 per cent in August 2026.</li>"
    "<li>Rich-country farm protection hurts developing economies, which lose export markets and face subsidised competition.</li>"
    "<li>Trade is diverted around barriers, and global value chains are reorganised.</li>"
    "</ul>"
    "<h3>Protection is rising again</h3>"
    "<p>The WTO recorded 333 new trade-restrictive measures in the first half of 2026, more than in the whole of 2025, and import restrictions in force since 2009 now cover a record US$5.4 trillion (21.3 per cent) of world imports. In February 2026 the US Supreme Court ruled the emergency-powers tariffs unlawful, but other tariffs replaced them, including a 12.5 per cent tariff on Australian goods from July 2026. On 25 November 2026 the US proposed new tariffs on 14 economies, including 20 per cent on China and Vietnam. Australia has gone the other way, abolishing more than 1,000 tariffs since 2022.</p>"
    "<p><b>Use it in an exam:</b> explain each reason, then judge it. Most economists accept that protection costs more than it saves, but the anti-dumping and security arguments are the strongest. Use the WTO data to show the current trend.</p>"
    "<p>Sources: WTO trade monitoring report (November 2026); PIIE via Fortune (October 2026); Al Jazeera and ABC News (November 2026); Prime Minister's office (November 2026).</p>"
    )
    tiles = ('<div class="k"><div><b>333</b><i>New trade restrictions</i><u>Jan&ndash;Jun 2026, WTO</u></div>'
             '<div><b>21.3%</b><i>World imports under restrictions</i><u>US$5.4tn, a record</u></div>'
             '<div><b>218</b><i>Trade remedy investigations</i><u>Jan&ndash;Jun 2026</u></div>'
             '<div><b>1,000+</b><i>Tariffs Australia has abolished</i><u>since 2022</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "New trade-restrictive measures (WTO)", B.bars([("All of 2025", 300), ("First half of 2026", 333)], vmax=360, fmt="%.0f"),
            "More restrictions in six months than in the whole previous year. Source: WTO, November 2026."),
      B.fig(3, "The effect of a tariff", ed.tariff(ed.TOPIC[1], good="steel").svg(),
            "The tariff lifts the price from P<sub>w</sub> to P<sub>w+t</sub>. Domestic output rises, consumption falls and imports shrink. Not to scale."),
      B.fig(4, "Reasons for protection, judged", B.table(["Reason", "Case for", "Case against"],
            [["Infant industry", "Time to reach economies of scale", "Hard to remove; may never mature"], ["Employment", "Saves jobs in exposed regions", "High cost per job; jobs lost elsewhere"],
             ["Dumping", "Counters unfair, subsidised prices", "Can be misused to block fair imports"], ["Defence", "Secure supply in a crisis", "Costly; 'security' is stretched to many goods"]])),
      B.fig(5, "How retaliation spreads", B.chain(["Country A raises tariffs", "Country B retaliates", "Trade between them falls", "Firms move supply chains", "World trade and growth slow", "Third countries like Australia are hit indirectly"])),
      B.tools([("explain", "See who wins and loses from protection"), ("lab", "Draw the tariff, quota and subsidy diagrams"), ("qf", "Past HSC questions on protection"), ("mcq", "Practise protection multiple choice")])]
    B.build("protection-global", c, cd, text, figs, "")
