def make(B):
    c, cd = "#8a3fb0", "#6a2a8a"
    text = (
    "<h3>What a tax model is</h3>"
    "<p>A <b>tax</b> is a compulsory payment to government that does not give the payer a specific good or service in return. A <b>tax model</b> describes how a tax is designed: who pays it, what it is charged on, and how the rate changes as the tax base changes. Taxation is the main source of revenue for the Australian Government and a key tool of fiscal policy.</p>"
    "<h3>Direct and indirect taxes</h3>"
    "<ul><li><b>Direct taxes</b> are paid straight to the government by the person or business that bears them. Examples are income tax, company tax and capital gains tax.</li>"
    "<li><b>Indirect taxes</b> are charged on spending and collected by a seller, who passes them on to consumers in the price. Examples are the GST and excise on fuel, alcohol and tobacco.</li></ul>"
    "<h3>Progressive, proportional and regressive taxes</h3>"
    "<p>Taxes are classified by what happens to the <b>average tax rate</b> (tax paid divided by income) as income rises (Figure 3).</p>"
    "<ul><li><b>Progressive:</b> the average rate rises with income. Personal income tax is progressive because higher <b>marginal rates</b> apply to each extra slice of income.</li>"
    "<li><b>Proportional:</b> the same rate applies at every income. Company tax, which is charged at a flat rate on profits, is an example.</li>"
    "<li><b>Regressive:</b> the average rate falls as income rises, so low-income households pay a bigger share of their income. A flat tax on spending, such as the GST or a cigarette excise, is regressive because lower-income households spend more of their income.</li></ul>"
    "<h3>The 2026&ndash;27 income tax scale</h3>"
    "<p>Australian residents pay no tax on the first $18,200, then 15 per cent up to $45,000, 30 per cent up to $135,000, 37 per cent up to $190,000 and 45 per cent above that, plus the 2 per cent Medicare levy. The lowest rate fell from 16 to 15 per cent on 1 July 2026 and is legislated to fall to 14 per cent from 1 July 2027 (Figure 2).</p>"
    "<p>Marginal rates apply only to the income inside each bracket. A person earning $100,000 pays $20,520 in income tax, an average rate of 20.5 per cent, even though their marginal rate is 30 per cent. This is why the system is progressive (Figure 4).</p>"
    "<h3>Principles of a good tax</h3>"
    "<p>Economists judge a tax model against several principles (Figure 5).</p>"
    "<ul><li><b>Equity:</b> fairness. <b>Vertical equity</b> means people with a greater ability to pay contribute more. <b>Horizontal equity</b> means people in similar circumstances pay similar amounts.</li>"
    "<li><b>Efficiency:</b> a tax should not distort decisions to work, save, invest or spend more than necessary. High marginal rates may reduce the incentive to work extra hours.</li>"
    "<li><b>Simplicity and certainty:</b> a tax should be easy to understand, cheap to collect and hard to avoid.</li>"
    "<li><b>Revenue adequacy:</b> a tax should raise enough revenue and keep up with the growth of the economy.</li></ul>"
    "<p>These principles often conflict. A more progressive scale improves equity but can weaken incentives, and the many deductions and concessions that make a tax fairer for some taxpayers also make it more complex.</p>"
    "<h3>The tax mix</h3>"
    "<p>Australia relies mainly on direct taxes, and above all on personal income tax. In the 2026&ndash;27 Budget, individuals and withholding taxes are projected at about 12.6 per cent of GDP and company tax at about 5.1 per cent of GDP, with company tax forecast to fall to 4.4 per cent by 2029&ndash;30. The GST goes to the states and territories.</p>"
    "<h3>Tax changes in the 2026&ndash;27 Budget</h3>"
    "<p>The Budget made changes in several parts of the tax system (Figure 6). A $1,000 instant deduction for work expenses starts in 2026&ndash;27, and a $250 Working Australians Tax Offset starts from 1 July 2027. From 1 July 2027 the 50 per cent capital gains tax discount is replaced by indexation of the cost base plus a 30 per cent minimum tax, and negative gearing is limited for established residential property bought after 12 May 2026. A 30 per cent minimum tax on discretionary trust income starts from 1 July 2028. Supporters say the changes improve equity and raise revenue, while critics argue they may reduce investment.</p>"
    "<p><b>Use it in an exam:</b> name the tax, say whether it is direct or indirect and progressive, proportional or regressive, then judge it against equity and efficiency.</p>"
    "<p>Sources: <a href=\"https://www.ato.gov.au/tax-rates-and-codes/tax-rates-australian-residents\">ATO, tax rates for Australian residents</a>; <a href=\"https://budget.gov.au/\">Australian Government, Budget 2026&ndash;27</a>; <a href=\"https://www.pbo.gov.au/publications-and-data/publications/budget-charts/2026-27-Budget-Snapshot\">Parliamentary Budget Office, 2026&ndash;27 Budget Snapshot</a>; <a href=\"https://educationstandards.nsw.edu.au/\">NESA, Economics Stage 6 Syllabus</a>.</p>"
    )
    tiles = ('<div class="k"><div><b>$18,200</b><i>Tax-free threshold</i><u>Residents, 2026&ndash;27</u></div><div><b>15%</b><i>Lowest rate</i><u>Down from 16%; 14% from July 2027</u></div>'
             '<div><b>45%</b><i>Top marginal rate</i><u>Income over $190,000</u></div><div><b>$1,000</b><i>Instant deduction</i><u>New from 2026&ndash;27</u></div></div>')
    figs = [
      B.fig(1, "Key numbers", tiles),
      B.fig(2, "Resident income tax scale, 2026–27", B.table(["Taxable income", "Marginal rate"], [["$0 &ndash; $18,200", "0%"], ["$18,201 &ndash; $45,000", "15%"], ["$45,001 &ndash; $135,000", "30%"], ["$135,001 &ndash; $190,000", "37%"], ["Over $190,000", "45%"]]), "Plus the 2% Medicare levy. Source: ATO."),
      B.fig(3, "Types of tax", B.table(["Type", "Average rate as income rises", "Example"], [["Progressive", "Rises", "Income tax"], ["Proportional", "Stays the same", "Company tax"], ["Regressive", "Falls", "GST, excise"]])),
      B.fig(4, "Average tax rate rises with income", B.bars([("$30,000", 5.9), ("$60,000", 14.2), ("$100,000", 20.5), ("$150,000", 24.4), ("$250,000", 31.3)], vmax=35, fmt="%.1f%%"), "Income tax only, before the Medicare levy, 2026&ndash;27 scale. Calculated from ATO rates."),
      B.fig(5, "Judging a tax", B.table(["Principle", "Question to ask"], [["Equity", "Do those with more ability pay more?"], ["Efficiency", "Does it distort work or investment?"], ["Simplicity", "Is it easy and cheap to collect?"], ["Revenue", "Does it raise enough?"]])),
      B.fig(6, "2026–27 Budget tax changes", B.table(["Change", "From"], [["$1,000 instant work deduction", "2026&ndash;27"], ["Lowest rate 16% to 15%", "1 July 2026"], ["$250 Working Australians Tax Offset", "1 July 2027"], ["CGT discount replaced by indexation and 30% minimum tax", "1 July 2027"], ["Negative gearing limited (established homes)", "1 July 2027"], ["30% minimum tax on discretionary trusts", "1 July 2028"]]), "Source: Budget 2026&ndash;27, as summarised by Mallesons."),
      B.tools([("policy", "Test fiscal and monetary settings"), ("calc", "Tax calculation skills"), ("glance", "Latest tax statistics"), ("chain", "Build cause-and-effect chains"),
               ("qf", "Past HSC questions on taxation"), ("mcq", "Section I questions with explanations"), ("ef", "Find evidence on tax reform"), ("map", "See how topics connect")]),
    ]
    B.build("tax-models", c, cd, text, figs, "")
