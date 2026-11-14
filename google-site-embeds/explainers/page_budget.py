def make(B):
    c, cd = "#8a3fb0", "#6a2a8a"
    text = (
    "<h3>The Budget in context</h3>"
    "<p>The <b>Federal Budget</b> is the Government's annual statement of expected spending, revenue and borrowing, and the main tool of <b>fiscal policy</b>. The 2026&ndash;27 Budget was delivered by the Treasurer, Jim Chalmers, on 12 May 2026. It was delivered while inflation was rising because of the Middle East conflict and higher oil prices, and while growth was slowing. The Budget forecasts growth of 1&frac34; per cent in 2026&ndash;27. The Treasurer described it as one of the most ambitious budgets in decades, with three main themes: tax reform, restraint on spending growth, and national resilience.</p>"
    "<h3>The budget balance</h3>"
    "<p>The Budget is in deficit. The underlying cash deficit is forecast at $31.5 billion in 2026&ndash;27, about 1 per cent of GDP and $2.8 billion smaller than expected in the December update. Deficits are forecast through to 2029&ndash;30 (Figure 2), and a surplus is not expected until the mid-2030s. The headline deficit, which includes investment spending and other items, is forecast at $64.1 billion, or 2.1 per cent of GDP. Net debt is forecast at 19.9 per cent of GDP in 2026&ndash;27.</p>"
    "<p>In dollar terms the deficit widens slightly from 2025&ndash;26. Some economists argued that this is not a strong anti-inflation stance when the RBA is raising interest rates to slow demand. The Government replied that its spending restraint and savings measures help the RBA by limiting the growth of demand.</p>"
    "<h3>Spending and savings</h3>"
    "<p>The Budget contains large savings, including cuts of $37.8 billion in NDIS costs over five years, together with new spending on fuel and fertiliser security, defence, health and housing. The Government is therefore trying to slow spending growth while still responding to cost-of-living and supply concerns.</p>"
    "<h3>Tax changes</h3>"
    "<p>The Budget makes the largest changes to the tax system in many years (Figure 3). Supporters argue that they shift the tax system towards workers and make housing more affordable. Critics argue that the changes break an earlier commitment, may reduce investment in rental housing and increase uncertainty for investors.</p>"
    "<ul><li><b>Workers:</b> a $1,000 instant deduction for work expenses from 2026&ndash;27 and a $250 Working Australians Tax Offset from 1 July 2027. The lowest income tax rate also falls to 15 per cent in 2026&ndash;27 and 14 per cent in 2027&ndash;28.</li>"
    "<li><b>Capital gains tax:</b> from 1 July 2027 the 50 per cent discount is replaced by indexation of the cost base to inflation plus a 30 per cent minimum tax. The main residence is still exempt.</li>"
    "<li><b>Negative gearing:</b> from 1 July 2027, losses on established residential property can only be offset against rental income or residential capital gains. Earlier purchases are grandfathered and new builds are excluded.</li>"
    "<li><b>Trusts and business:</b> a 30 per cent minimum tax on discretionary trust income from 1 July 2028, and a permanent $20,000 instant asset write-off for small business.</li></ul>"
    "<h3>Cost of living and resilience</h3>"
    "<p>To reduce short-term price pressure the Government temporarily halved fuel excise for three months, from 52.6 to 20.6 cents a litre, and cut the heavy vehicle road user charge. It also committed billions of dollars to fuel and fertiliser security, which is a supply-side response to the oil price shock.</p>"
    "<h3>Linking the Budget to the objectives</h3>"
    "<p>The Budget is best analysed against the economic objectives (Figure 4).</p>"
    "<ul><li><b>Price stability:</b> spending restraint supports the RBA, but the fuel excise cut and tax offsets add to demand.</li>"
    "<li><b>Equity:</b> the changes to CGT, negative gearing and trusts target the tax advantages of asset owners, while the offset and deduction help workers.</li>"
    "<li><b>Growth:</b> the instant asset write-off and loss carry-back support business investment, while the deficit gives some support to demand.</li>"
    "<li><b>External stability and the environment:</b> fuel security spending reduces exposure to oil shocks, but critics noted less emphasis on climate programs.</li></ul>"
    "<p><b>Use it in an exam:</b> state the Budget balance and stance, link it to inflation and growth, then evaluate it using one objective it helps and one it conflicts with. Mention time lags and the role of monetary policy.</p>"
    "<p>Sources: <a href=\"https://budget.gov.au/\">Australian Government, Budget 2026&ndash;27</a>; <a href=\"https://www.pbo.gov.au/publications-and-data/publications/budget-charts/2026-27-Budget-Snapshot\">Parliamentary Budget Office, 2026&ndash;27 Budget Snapshot</a>; <a href=\"https://www.commbank.com.au/articles/newsroom/2026/05/2026-federal-budget-analysis-australian-economy.html\">CommBank, 2026&ndash;27 Federal Budget analysis</a>; <a href=\"https://www.hawkerbritton.com/blog/2026/05/13/2026-27-federal-budget/\">Hawker Britton, 2026&ndash;27 Federal Budget</a>.</p>"
    )
    tiles = ('<div class="k"><div><b>$31.5bn</b><i>Underlying cash deficit</i><u>2026&ndash;27, about 1% of GDP</u></div><div><b>19.9%</b><i>Net debt</i><u>Share of GDP, 2026&ndash;27</u></div>'
             '<div><b>1&frac34;%</b><i>GDP growth forecast</i><u>2026&ndash;27</u></div><div><b>$37.8bn</b><i>NDIS savings</i><u>Over five years</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "Underlying cash deficit ($ billion)", B.bars([("2025–26", 28.3), ("2026–27", 31.5), ("2027–28", 31.0), ("2028–29", 34.4), ("2029–30", 25.3)], vmax=40, fmt="$%.1fb"), "Budget forecasts, May 2026. Source: Budget 2026–27."),
      B.fig(3, "Main tax changes", B.table(["Change", "From"], [["$1,000 instant work deduction", "2026–27"], ["Lowest income tax rate 15%", "1 July 2026"], ["$250 Working Australians Tax Offset", "1 July 2027"], ["CGT discount replaced by indexation and 30% minimum tax", "1 July 2027"], ["Negative gearing limited for established homes", "1 July 2027"], ["30% minimum tax on discretionary trusts", "1 July 2028"]]), "Source: Budget 2026–27, as summarised by Mallesons."),
      B.fig(4, "The Budget and the objectives", B.table(["Objective", "Helped by", "Conflict"], [["Price stability", "Spending restraint", "Fuel excise cut, tax offsets"], ["Equity", "Asset tax changes, offsets", "Investor uncertainty"], ["Growth", "Business tax measures", "Slower demand growth"], ["External", "Fuel security", "Deficit persists"]])),
      B.fig(5, "Chain: why the Budget matters in 2026", B.chain(["Oil price shock lifts inflation", "RBA raises the cash rate", "Budget restrains spending growth", "Deficit stays near 1% of GDP", "Fiscal and monetary policy conflict is debated"])),
      B.tools([("policy", "Test fiscal and monetary settings"), ("calc", "Budget and multiplier calculations"), ("glance", "Latest Budget and economy data"), ("chain", "Build cause-and-effect chains"),
               ("qf", "Past HSC questions on fiscal policy"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence on the Budget"), ("map", "See how topics connect")]),
    ]
    B.build("budget-2026-27", c, cd, text, figs, "")
