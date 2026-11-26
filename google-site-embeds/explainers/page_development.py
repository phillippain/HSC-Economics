def make(B):
    c, cd = "#2447d6", "#1a3399"
    text = (
    "<h3>Economic growth and economic development</h3>"
    "<p><b>Economic growth</b> is an increase in the volume of goods and services an economy produces, measured by the change in real GDP. <b>Economic development</b> is broader: it is an improvement in people's quality of life, including health, education, freedom, equality and a clean environment. Growth can pay for development (schools, hospitals, clean water), but it does not guarantee it. A country can grow fast while inequality widens or pollution worsens.</p>"
    "<h3>Income and quality of life indicators</h3>"
    "<ul>"
    "<li><b>GDP or GNI per capita</b> measures average income. Converting at purchasing power parity (PPP) allows for lower prices in poorer countries.</li>"
    "<li>The <b>Human Development Index (HDI)</b> combines life expectancy, years of schooling and GNI per capita into a score from 0 to 1. Australia ranks 7th (0.958), China 78th (0.797), India 130th (0.685) and Nigeria 164th (0.560) (Figure 2).</li>"
    "<li>Other indicators include the inequality-adjusted HDI, the Gender Inequality Index, poverty rates, literacy, infant mortality and access to clean water.</li>"
    "</ul>"
    "<h3>Distribution of income and wealth</h3>"
    "<p>Income and wealth are unequal both between and within countries. The <b>Lorenz curve</b> and <b>Gini coefficient</b> measure inequality within a country: Australia's income Gini is about 0.33, while South Africa's is about 0.63. Between countries, the gap is shown by poverty: in 2025 about <b>831 million people</b> lived in extreme poverty, on less than US$3 a day, down from about 2.3 billion in 1990. Extreme poverty is now concentrated in Sub-Saharan Africa and in countries affected by conflict (World Bank).</p>"
    "<h3>Developing, emerging and advanced economies</h3>"
    "<p>Economies are grouped by their stage of development. These are three separate categories, not two.</p>"
    "<ul>"
    "<li><b>Advanced economies</b> (Australia, the US, Japan, Germany) have high incomes, large service sectors and strong institutions.</li>"
    "<li><b>Emerging economies</b> (China, India, Brazil, Indonesia) are industrialising fast, attract large FDI inflows and are becoming more integrated with the world economy.</li>"
    "<li><b>Developing economies</b> (Nigeria, Bangladesh, many Pacific and African nations) have low incomes, large farm sectors, weak infrastructure and often depend on a few commodity exports.</li>"
    "</ul>"
    "<h3>Reasons for differences between nations</h3>"
    "<p>Differences come from natural resources, the quality of human capital (health and education), physical capital and infrastructure, the strength of institutions and the rule of law, political stability and conflict, population growth, geography and access to markets, foreign debt, and how open the economy is to trade and investment.</p>"
    "<h3>Effects of globalisation</h3>"
    "<ul>"
    "<li><b>Trade, investment and TNCs.</b> Openness has raised growth in emerging economies such as China and Vietnam by giving them access to large markets, technology and FDI. But many developing economies still export raw commodities, face rich-country farm protection and gain little from global value chains. TNCs bring jobs and skills, but can shift profits offshore and use their bargaining power over small economies.</li>"
    "<li><b>Inequality.</b> Inequality between countries has narrowed as Asia caught up, but inequality within many countries has widened, as gains went to skilled workers and owners of capital.</li>"
    "<li><b>Environmental sustainability.</b> Growth in production and transport has raised greenhouse emissions and pressure on resources. Pollution is a negative externality that crosses borders, so it needs international agreement. Warming has already passed the Paris goal of 1.5&deg;C. In November 2026 the COP31 climate summit became the longest on record, and the EU, Panama and the Marshall Islands formally objected to its final text.</li>"
    "<li><b>The international business cycle.</b> Integration spreads downturns. The 2026 oil shock raised inflation and interest rates worldwide, and developing economies that import fuel and food were hit hardest.</li>"
    "</ul>"
    "<p><b>Use it in an exam:</b> show you know that growth is not development. Use an indicator (HDI, poverty, Gini) for an advanced, an emerging and a developing economy, then judge whether globalisation helped or hurt each.</p>"
    "<p>Sources: UNDP Human Development Report 2025; World Bank Poverty and Inequality Platform (2025); IMF; UN News on COP31 (November 2026).</p>"
    )
    tiles = ('<div class="k"><div><b>831m</b><i>People in extreme poverty</i><u>2025, under US$3 a day</u></div>'
             '<div><b>2.3bn</b><i>Extreme poverty in 1990</i><u>World Bank</u></div>'
             '<div><b>0.958</b><i>Australia HDI, ranked 7th</i><u>HDR 2025</u></div>'
             '<div><b>0.560</b><i>Nigeria HDI, ranked 164th</i><u>HDR 2025</u></div></div>')
    figs = [B.fig(1, "Key numbers", tiles),
      B.fig(2, "Human Development Index, 2023", B.bars([("Australia (7th)", 0.958), ("China (78th)", 0.797), ("India (130th)", 0.685), ("Nigeria (164th)", 0.560)], vmax=1, fmt="%.3f"),
            "An advanced, two emerging and a developing economy. Source: UNDP Human Development Report 2025."),
      B.fig(3, "GNI per capita, 2023 (US$ thousand, PPP)", B.bars([("Australia", 58.3), ("China", 22.0), ("India", 9.0), ("Nigeria", 5.6)], fmt="$%.1fk"),
            "Average income adjusted for price differences. Source: UNDP HDR 2025."),
      B.fig(4, "China's HDI rose as it opened up", B.linechart([("1990", 1990, 0.491), ("2000", 2000, 0.598), ("2010", 2010, 0.710), ("2015", 2015, 0.750), ("2023", 2023, 0.797)], c, 1, unit=""),
            "Source: UNDP HDR 2025, Table 2."),
      B.fig(5, "Growth versus development", B.table(["", "Economic growth", "Economic development"],
            [["Meaning", "More output", "Better quality of life"], ["Measure", "Real GDP growth", "HDI, poverty, Gini, life expectancy"], ["Example", "China grew about 10% a year 1980&ndash;2010", "China's HDI rose from 0.491 to 0.797"]])),
      B.fig(6, "Three groups, three stages", B.table(["", "Advanced", "Emerging", "Developing"],
            [["Income", "High", "Middle, rising fast", "Low"], ["Main sector", "Services", "Manufacturing", "Agriculture, commodities"], ["Example", "Australia", "China, India", "Nigeria, Bangladesh"]])),
      B.tools([("ef", "Evidence on poverty, inequality and climate"), ("qf", "Past HSC questions on development"), ("essay", "Plan a globalisation and development essay"), ("gloss", "Check key terms")])]
    B.build("globalisation-and-development", c, cd, text, figs, "")
