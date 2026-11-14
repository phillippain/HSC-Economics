def make(B):
    c, cd = "#8a3fb0", "#6a2a8a"
    ed = B.ed
    text = (
    "<h3>The goals of economic policy</h3>"
    "<p>Governments and the Reserve Bank use <b>macroeconomic policies</b> to influence the whole economy. They aim to achieve a set of <b>economic objectives</b>. The syllabus names six, and each can be measured with an indicator (Figure 2).</p>"
    "<ul><li><b>Strong and sustainable economic growth:</b> a steady rise in real GDP that can be kept up without causing inflation or damaging the environment. The Budget forecasts growth of 1&frac34; per cent in 2026&ndash;27.</li>"
    "<li><b>Full employment:</b> a low rate of unemployment that does not cause inflation to rise. The unemployment rate was 4.7 per cent in the latest figures, the highest in five years.</li>"
    "<li><b>Price stability:</b> low and stable inflation. The RBA target is 2 to 3 per cent on average. Headline inflation was 4.3 per cent in the year to September 2026.</li>"
    "<li><b>External stability:</b> a current account deficit and foreign liabilities at levels that are sustainable. The deficit was $27.2 billion in the June quarter 2026.</li>"
    "<li><b>Equitable distribution of income:</b> a fair sharing of the gains from growth, measured by the Gini coefficient and the Lorenz curve.</li>"
    "<li><b>Ecologically sustainable development:</b> use of resources that protects the environment for future generations, for example by cutting greenhouse gas emissions.</li></ul>"
    "<h3>The policy tools</h3>"
    "<p>Three groups of policies are used (Figure 4).</p>"
    "<ul><li><b>Fiscal policy:</b> government spending and taxation, mainly aimed at the level of aggregate demand. It is set in the Federal Budget.</li>"
    "<li><b>Monetary policy:</b> the Reserve Bank's cash rate, aimed at inflation and employment.</li>"
    "<li><b>Microeconomic policies:</b> reforms of markets to raise efficiency and productivity, such as competition policy, deregulation, labour market reform and reduction of protection. These policies work on aggregate supply, so their effects are slower but longer lasting.</li></ul>"
    "<p>Fiscal and monetary policies are <b>demand-side</b> policies and are used to manage the business cycle. Micro policies are <b>supply-side</b> policies and aim to raise the productive capacity of the economy.</p>"
    "<h3>The business cycle</h3>"
    "<p>Output does not grow smoothly. The economy moves through a <b>business cycle</b> of expansion, peak, contraction and trough. During an expansion real GDP rises, unemployment falls and inflation tends to rise. During a contraction the opposite occurs. Demand-side policies try to smooth these swings, while supply-side policies try to lift the long-run trend of growth. The difference matters in an exam: use fiscal or monetary policy for a cyclical problem, and micro reform for a structural one such as low productivity.</p>"
    "<h3>Policy in practice</h3>"
    "<p>The policy mix depends on where the economy is in the business cycle. When growth is weak and unemployment is rising, policy is expansionary. When demand is too strong and inflation is rising, policy is contractionary (Figure 5). In 2026 the RBA raised the cash rate from 3.60 to 4.85 per cent because inflation was well above target, even though unemployment was rising. The Budget set out restraint in spending growth at the same time.</p>"
    "<h3>Conflicts between objectives</h3>"
    "<p>Policies that improve one objective may harm another, so governments must make trade-offs.</p>"
    "<ul><li><b>Inflation and unemployment:</b> a short-run trade-off is shown by the Phillips curve (Figure 3). Moving down the curve lowers unemployment but raises inflation, and the reverse. In 2026 higher interest rates were being used to reduce inflation at the cost of higher unemployment.</li>"
    "<li><b>Growth and the current account:</b> faster growth raises imports and widens the current account deficit.</li>"
    "<li><b>Growth and the environment:</b> more output can mean more emissions and resource use, unless the economy shifts to cleaner production.</li>"
    "<li><b>Efficiency and equity:</b> a more equal distribution through taxes and transfers may reduce incentives, and microeconomic reforms that raise efficiency may leave some groups worse off.</li></ul>"
    "<h3>Limits on policy</h3>"
    "<p>Policies take time to work (time lags), the economy is affected by world events such as the oil price shock caused by the Middle East war, and forecasts are uncertain. Governments also face political constraints, and the effect of a policy depends on how households and firms respond.</p>"
    "<p><b>Use it in an exam:</b> name the objective, give a current indicator, say which policy is being used and why, then explain the trade-off with another objective.</p>"
    "<p>Sources: <a href=\"https://www.abs.gov.au/\">Australian Bureau of Statistics</a>; <a href=\"https://www.rba.gov.au/publications/smp/2026/nov/overview.html\">RBA, Statement on Monetary Policy, November 2026</a>; <a href=\"https://budget.gov.au/\">Australian Government, Budget 2026&ndash;27</a>; <a href=\"https://educationstandards.nsw.edu.au/\">NESA, Economics Stage 6 Syllabus</a>.</p>")
    tiles = ('<div class="k"><div><b>1&frac34;%</b><i>GDP growth forecast</i><u>2026&ndash;27 Budget</u></div><div><b>4.7%</b><i>Unemployment</i><u>Highest in five years</u></div>'
             '<div><b>4.3%</b><i>Headline inflation</i><u>Year to September 2026</u></div><div><b>$27.2bn</b><i>Current account deficit</i><u>June quarter 2026</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "The six objectives and how to measure them", B.table(["Objective", "Indicator"], [["Strong, sustainable growth", "Real GDP growth"], ["Full employment", "Unemployment rate"], ["Price stability", "CPI, 2&ndash;3% target"], ["External stability", "CAD, net foreign liabilities, % of GDP"], ["Equitable distribution", "Gini coefficient"], ["Ecological sustainability", "Emissions, resource use"]])),
      B.fig(3, "The Phillips curve: inflation and unemployment trade-off", ed.phillips(expectations_shift=False).svg(), "The curve slopes downward: lower unemployment is associated with higher inflation, and the reverse. The green band is the 2&ndash;3% target. Not to scale."),
      B.fig(4, "Policy tools", B.table(["Policy", "Who", "Tools", "Works on"], [["Fiscal", "Government", "Spending, tax", "Demand"], ["Monetary", "RBA", "Cash rate", "Demand"], ["Micro", "Government", "Competition, labour, trade reforms", "Supply"]])),
      B.fig(5, "Choosing the policy stance", B.table(["Economy", "Problem", "Stance"], [["Weak growth, rising unemployment", "Low demand", "Expansionary"], ["Strong demand, high inflation", "Excess demand", "Contractionary"], ["Low productivity", "Low supply", "Micro reform"]])),
      B.fig(6, "Chain: a trade-off in 2026", B.chain(["Inflation above 2&ndash;3% target", "RBA raises the cash rate", "Demand and growth slow", "Unemployment rises", "Objectives conflict: price stability vs jobs"])),
      B.tools([("policy", "Test fiscal and monetary settings"), ("macro", "Draw AD/AS and Phillips curves"), ("glance", "Latest indicators for each objective"), ("chain", "Build trade-off chains"),
               ("qf", "Past HSC questions on objectives"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence for each objective"), ("map", "See how topics connect")]),
    ]
    B.build("macroeconomic-policies", c, cd, text, figs, "")
