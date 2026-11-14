def make(B):
    c, cd = "#d9822b", "#a85a12"
    ed = B.ed
    text = (
    "<h3>Measuring unemployment</h3>"
    "<p>A person is <b>unemployed</b> if they are aged 15 or over, are not working, are actively looking for work and are available to start. A person who works one hour or more a week for pay is counted as <b>employed</b>. The Australian Bureau of Statistics (ABS) measures both in its monthly Labour Force Survey.</p>"
    "<ul><li><b>Labour force</b> = employed + unemployed</li>"
    "<li><b>Unemployment rate</b> = unemployed &divide; labour force &times; 100</li>"
    "<li><b>Participation rate</b> = labour force &divide; working-age population (15 and over) &times; 100</li></ul>"
    "<p>In September 2026 there were 732,000 unemployed people and 14.78 million employed, so the labour force was 15.51 million. The unemployment rate was 732,000 &divide; 15.51 million &times; 100 = 4.7 per cent (Figure 3).</p>"
    "<h3>Recent trends</h3>"
    "<p>Unemployment fell to about 3.5 per cent in 2022, the lowest rate in almost 50 years, as the economy recovered from the pandemic. It has risen slowly since. In September 2026 it was 4.7 per cent, the highest since late 2021 (Figure 2). Employment fell by 39,000 in the month. Economic growth has slowed and higher interest rates are reducing the demand for labour.</p>"
    "<p>The participation rate is 66.8 per cent, close to a record high. More women and older workers are in the labour force than in the past.</p>"
    "<h3>Types of unemployment</h3>"
    "<ul><li><b>Cyclical:</b> caused by a downturn in the business cycle. When aggregate demand falls, firms cut output and need fewer workers (Figure 5).</li>"
    "<li><b>Structural:</b> caused by a mismatch between the skills workers have and the skills employers need. It follows changes in technology, the decline of an industry or a cut in protection. It lasts longer than cyclical unemployment.</li>"
    "<li><b>Frictional:</b> people who are between jobs. It is short term and exists even in a strong economy.</li>"
    "<li><b>Seasonal:</b> caused by jobs that exist only at certain times of year, such as fruit picking and holiday retail work.</li>"
    "<li><b>Hidden:</b> people who would like to work but have given up looking. They are not counted as unemployed, so the official rate understates the problem.</li>"
    "<li><b>Long-term:</b> people unemployed for 12 months or more. They lose skills and contacts, which makes it harder to find work.</li>"
    "<li><b>Underemployment:</b> people who have a job but want more hours. The underemployment rate is 6.3 per cent. Adding it to the unemployment rate gives the <b>underutilisation rate</b> of 11.0 per cent, the widest measure of spare capacity in the labour market.</li></ul>"
    "<h3>The non-accelerating inflation rate of unemployment</h3>"
    "<p>The non-accelerating inflation rate of unemployment (NAIRU) is the lowest rate of unemployment that can be sustained without causing inflation to rise. It is made up of structural and frictional unemployment. This is what economists mean by full employment.</p>"
    "<p>If unemployment falls below the NAIRU, firms compete for scarce workers, wages rise faster and inflation increases (Figure 6). The Reserve Bank of Australia (RBA) estimates the NAIRU at about 4.5 per cent. Demand management policies can reduce cyclical unemployment, but only policies that improve skills and the working of the labour market can lower the NAIRU.</p>"
    "<h3>Main groups affected</h3>"
    "<ul><li><b>Young people (15 to 24):</b> their unemployment rate is 11.1 per cent, more than twice the national rate. They have less experience and are more likely to work in casual jobs (Figure 7).</li>"
    "<li><b>Aboriginal and Torres Strait Islander people:</b> unemployment is much higher than the national rate, reflecting gaps in education, health and location.</li>"
    "<li><b>People with low skills or education:</b> they are the most exposed to structural change.</li>"
    "<li><b>Regional areas:</b> regions that depend on one industry are hit hard when it declines.</li>"
    "<li><b>Older workers and recent migrants:</b> older workers who lose a job take longer to find another, and migrants can face language barriers or unrecognised qualifications.</li></ul>"
    "<h3>Effects of unemployment</h3>"
    "<p><b>Economic costs</b></p>"
    "<ul><li><b>Lost output:</b> the economy produces less than it could, so it operates inside its production possibility frontier.</li>"
    "<li><b>Lower living standards:</b> unemployed people lose income and spend less, which reduces demand further.</li>"
    "<li><b>Loss of skills:</b> long periods without work reduce a person's skills, which lowers productivity.</li>"
    "<li><b>Cost to the budget:</b> income tax revenue falls and spending on welfare payments rises.</li>"
    "<li><b>Lower wage growth:</b> spare labour reduces the bargaining power of workers.</li></ul>"
    "<p><b>Social costs</b></p>"
    "<ul><li><b>Inequality:</b> unemployment is the largest single cause of poverty in Australia.</li>"
    "<li><b>Health and family:</b> it is linked to poor mental and physical health and family breakdown.</li>"
    "<li><b>Community:</b> areas of high unemployment have higher rates of crime and social isolation.</li></ul>"
    "<h3>Links to other parts of the course</h3>"
    "<ul><li><b>Economic growth:</b> the economy must grow fast enough to create jobs for a growing labour force.</li>"
    "<li><b>Inflation:</b> the NAIRU links the unemployment rate to wage and price pressure.</li>"
    "<li><b>Labour market policy:</b> training, education and wage-setting rules aim to reduce structural unemployment.</li></ul>"
    "<p><b>Use it in an exam:</b> quote the unemployment, participation and underemployment rates, name the type of unemployment and its cause, and explain the economic and social costs. Use the NAIRU to link unemployment to inflation.</p>"
    "<p>Sources: <a href=\"https://www.abs.gov.au/statistics/labour/employment-and-unemployment/labour-force-australia/latest-release\">ABS, Labour Force, Australia, September 2026</a>; <a href=\"https://www.rba.gov.au/\">Reserve Bank of Australia</a>.</p>")
    tiles, js = B.live([("unemp", "Unemployment rate", "4.7%", "Sep 2026"), ("underut", "Underutilisation rate", "11.0%", "Sep 2026"),
                        ("partic", "Participation rate", "66.8%", "Sep 2026"), ("wpi", "Wages growth (WPI)", "3.2%", "Jun qtr 2026")])
    pts = [("Sep 2025", 0, 4.4), ("Jan 2026", 4, 4.1), ("", 5, 4.3), ("", 10, 4.5), ("", 11, 4.7), ("Sep 2026", 12, 4.7)]
    figs = [
      B.fig(1, "Latest figures", tiles, "These update by themselves from Economy at a Glance."),
      B.fig(2, "Unemployment rate, September 2025 to September 2026 (%)", B.linechart(pts, c, 6), "Selected months, seasonally adjusted. Source: ABS."),
      B.fig(3, "Worked example: September 2026", B.table(["Measure", "Figure"], [["Employed", "14.78 million"], ["Unemployed", "0.73 million"], ["Labour force", "14.78 + 0.73 = 15.51 million"], ["Unemployment rate", "0.73 &divide; 15.51 &times; 100 = 4.7%"], ["Working-age population", "23.2 million"], ["Participation rate", "15.51 &divide; 23.2 &times; 100 = 66.8%"]]), "Source: ABS, rounded."),
      B.fig(4, "Types of unemployment", B.table(["Type", "Cause"], [["Cyclical", "Fall in aggregate demand"], ["Structural", "Skills do not match the jobs available"], ["Frictional", "Moving between jobs"], ["Seasonal", "Work available only part of the year"], ["Hidden", "Gave up looking, so not counted"], ["Long-term", "Out of work for 12 months or more"]])),
      B.fig(5, "Cyclical unemployment: aggregate demand falls", ed.ad_as("AD left", ed.TOPIC[3]).svg(), "AD<sub>1</sub> to AD<sub>2</sub> lowers output from Y<sub>1</sub> to Y<sub>2</sub>. Firms need fewer workers, so unemployment rises. Not to scale."),
      B.fig(6, "Unemployment and inflation: the Phillips curve", ed.phillips(expectations_shift=False).svg(), "The Phillips curve (PC) slopes down: lower unemployment is associated with higher inflation, and the shaded band marks the 2&ndash;3% target. Not to scale."),
      B.fig(7, "Young people are hit hardest, September 2026 (%)", B.bars2([("Unemployment rate", 11.1, 4.7), ("Underemployment rate", 16.0, 6.3)], ("Aged 15 to 24", "All ages"), fmt="%.1f"), "Source: ABS; Department of Employment and Workplace Relations."),
      B.fig(8, "How unemployment costs the economy", B.chain(["Workers lose their jobs", "Household income and spending fall", "Firms sell less and cut more jobs", "Tax revenue falls and welfare spending rises", "Skills are lost the longer people are out of work", "The economy's future capacity is lower"])),
      B.tools([("glance", "Latest labour market figures"), ("calc", "Practise labour force calculations"), ("macro", "Shift AD and see unemployment change"), ("chain", "Build the chain from downturn to job losses"),
               ("policy", "Use policy to lower unemployment"), ("qf", "Past HSC questions on unemployment"), ("mcq", "Section I questions with explanations"), ("gloss", "NAIRU, participation rate and more")]),
    ]
    B.build("unemployment", c, cd, text, figs, js)
