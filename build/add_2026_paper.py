#!/usr/bin/env python3
"""Add the 2026 HSC Economics paper to the Question Finder (run once).

The Question Finder has no build pipeline: its data lives in the `const DATA = {...}`
payload inside hsc-question-finder-site/index.html. This script loads that payload,
adds the 2026 questions, and writes it back in place. It refuses to run twice.

The 2026 marking guidelines were not published when this was written, so there are
no multiple-choice answers (DATA.key) and no marking criteria (DATA.crit) for 2026.
When NESA publishes them: add DATA.key['2026'], the criteria, mg-2026.pdf, and raise
the upper year in `mgLink`.
"""
import json, re, sys, pathlib
P = pathlib.Path(__file__).resolve().parent.parent / 'hsc-question-finder-site' / 'index.html'
h = P.read_text(encoding='utf-8')
A = 'const DATA = '
i = h.index(A) + len(A)
D, n = json.JSONDecoder().raw_decode(h[i:])
if any(it['y'] == 2026 for it in D['items']):
    sys.exit('2026 is already in the Question Finder; nothing done.')
Y = 2026
def mc(q, t, c, k=(), p=None):
    return {"s": "I", "y": Y, "q": q, "l": "Q%d" % q, "m": 1, "t": t, "c": list(c), "k": list(k), "p": p, "st": None, "ns": 0}
def s2(q, part, m, t, c, k, p=None, st="No stimulus material."):
    return {"s": "II", "y": Y, "q": q, "l": "Q%d(%s)" % (q, part), "m": m, "t": t, "c": list(c), "k": list(k), "p": p, "st": st, "ns": 0}
def er(s, q, t, c, k, p=None, st=None):
    return {"s": s, "y": Y, "q": q, "l": "Q%d" % q, "m": 20, "t": t, "c": list(c), "k": list(k), "p": p, "st": st, "ns": 0}

# Section I: the one-line notes say what each question tests, without naming an option,
# because no answer key has been published.
items = [
 mc(1, "Which international organisation assists a country that cannot repay its debt during a financial crisis.", ["1B.2"], ["define"], "S1.7"),
 mc(2, "The type of unemployment caused by a fall in demand for specific skills.", ["3B.3"], ["define"]),
 mc(3, "Classifying an agreement among four neighbouring economies to cut tariffs on each other's goods.", ["1B.4"], ["define"], "S1.7"),
 mc(4, "The likely effect of a rise in the Gini coefficient (greater inequality).", ["3E.6"]),
 mc(5, "Reading an AD/AS diagram: the cause and effect of a rightward shift of aggregate supply.", ["3A.6"], ["diagram", "graph"]),
 mc(6, "What could reduce a budget deficit: changes in revenue and spending items.", ["4C.1"]),
 mc(7, "Recording dividends paid to foreign investors on the balance of payments.", ["2B.1"], ["define"]),
 mc(8, "Market failure in the supply of a good with positive externalities.", ["3F.2"]),
 mc(9, "Explaining a fall in the participation rate from labour force data.", ["3B.1"], ["table"]),
 mc(10, "Calculating the unemployment rate from the working age population, employment and the participation rate.", ["3B.1"], ["calc", "table"]),
 mc(11, "The effect of tighter regulation of foreign investment on the balance of payments, the currency and globalisation.", ["2B.3"]),
 mc(12, "Using the balance of payments identity to calculate the balance on goods and services.", ["2B.3"], ["calc", "table"], "S2.6"),
 mc(13, "Methods of financing a budget deficit and their effect on price stability.", ["4C.3"]),
 mc(14, "The consequences of moving from a fixed to a floating exchange rate.", ["2C.4"], [], "S2.9"),
 mc(15, "How higher prices in a major trading partner affect Australia's terms of trade and import volumes.", ["2B.4"]),
 mc(16, "Deriving MPC and the multiplier from income and consumption data, then applying it to a fall in government spending.", ["3A.3"], ["calc", "table"], "S3.10"),
 mc(17, "The link between net foreign equity, net foreign liabilities and the net primary income balance.", ["2B.3"], [], "S2.7"),
 mc(18, "Factors that raise nominal GDP while real GDP is unchanged.", ["3A.4"]),
 mc(19, "Reading two exchange rate quotations and identifying factors that explain the change in the value of the Australian dollar.", ["2C.2"], ["table"]),
 mc(20, "Using a demand and supply diagram with a world price to compare the effect of tariffs and quotas on local production.", ["1C.2"], ["calc", "diagram", "graph"]),
 s2(21, "a", 2, "Calculate the total cost of this subsidy to the government in this economy. Show all working.", ["1C.2"], ["calc", "diagram", "graph"], None,
    "Diagram — domestic demand (D) and supply (S) for a particular good with a second supply curve (S + Subsidy) and a world price of $40; price in dollars, quantity in thousands."),
 s2(21, "b", 4, "Explain the disadvantages of providing protection for domestic industries.", ["1C.2"], ["explain"], "S1.5"),
 s2(21, "c", 4, "The government of a hypothetical economy is considering the implementation of tariffs in place of subsidies for all industries receiving protection. Compare the impacts of tariffs and subsidies on consumers of this economy.", ["1C.2"], ["compare"], "S1.5"),
 s2(22, "a", 3, "In a hypothetical economy, the level of GDP per capita has remained unchanged and the Human Development Index (HDI) has changed from 0.71 to 0.75. Explain ONE government policy that could have contributed to the change in the HDI.", ["1D.3"], ["explain"], "S1.8"),
 s2(22, "b", 3, "Consider an economy other than Australia. Explain ONE effect of globalisation on the quality of life in this economy.", ["1E.1"], ["explain", "case"], "S1.1"),
 s2(22, "c", 4, "Explain why increases in gross world product may not always lead to improvements in global economic development.", ["1D.1"], ["explain"]),
 s2(23, "a", 2, "Outline how this will affect the level of consumption in the Australian economy.", ["4D.3"], ["outline"]),
 s2(23, "b", 3, "Explain ONE possible reason why Australia’s Trade Weighted Index may increase after a decrease in its cash rate.", ["2C.2"], ["explain"]),
 s2(23, "c", 5, "Explain the limitations of using monetary policy to reduce unemployment in Australia.", ["4H.1"], ["explain"], "S4.7"),
 s2(24, "a", 2, "Distinguish between awards and minimum employment standards.", ["4F.2"], ["define"]),
 s2(24, "b", 3, "Explain ONE advantage of a centralised labour market policy.", ["4F.4"], ["explain"]),
 s2(24, "c", 5, "Discuss how increasing the minimum wage in Australia may cause potential conflicts in achieving the economic objectives of the government.", ["4A.7"], ["discuss"], "S4.5"),
 er("III", 25, "Discuss the impact of fiscal policy on inflation and the distribution of income in the Australian economy. In your answer, refer to the information provided.",
    ["4C.2", "4C.1", "3C.3", "3E.3", "4I.3", "4I.5"], ["extract", "discuss", "stimulus", "graph"], None,
    "Extract — AMP, February 2026: no slowdown in Federal spending growth; spending as a share of GDP has risen from 24.3% in 2022–23 to a forecast 26.9% this financial year (nominal spending growth of 7.2%, 8% and 8.2% over three years), with public spending settling at a much higher share of the economy than before 2020 and adding to capacity pressures as the private sector has sought to spend more. Plus RBA chart 'Contributions to GDP growth, year-ended', December 2025, showing GDP growth and the contributions of household consumption, dwelling investment, business investment, public consumption, public investment, change in inventories, exports and imports (Reserve Bank of Australia, March 2026)."),
 er("III", 26, "Discuss the impact of microeconomic policies on inflation and economic growth in the Australian economy. In your answer, refer to the information provided.",
    ["4E.1", "4E.2", "3A.6", "3C.3", "3A.5", "4I.1", "4I.3"], ["extract", "discuss", "stimulus", "graph"], None,
    "Extract — Reserve Bank of Australia, August 2025: productivity growth has slowed in Australia over recent decades, reflecting declining business dynamism and competition, slower technological diffusion and lower growth in capital per worker; this has weighed on supply capacity and on growth in wages, incomes and household spending. Plus chart 'Labour productivity' — GDP per hour worked as an index (December quarter 2019 = 100), June 2015 to June 2025 (adapted from the Australian Bureau of Statistics, September 2025)."),
 er("IV", 27, "Assess the influence of domestic and global factors on Australia’s external stability.",
    ["3D.3", "3D.1", "3D.2", "2B.4", "2A.2", "4A.4", "1A.8"], ["evaluate"]),
 er("IV", 28, "Assess the influence of domestic and global policies in promoting environmental sustainability in Australia.",
    ["4G.1", "4G.2", "4G.3", "4G.4", "4I.6", "4A.5", "3F.1"], ["evaluate"]),
]
codes = {d['c'] for t in D['syl'] for hh in t['h'] for d in hh['d']}
skills = {d['c'] for t in D['ssk'] for d in t['d']}
for it in items:
    assert set(it['c']) <= codes, it
    assert set(it['k']) <= {p['k'] for p in D['prac']}, it
    assert it['p'] is None or it['p'] in skills, it
D['items'].extend(items)

def Q(q, opts, v=False):
    return {"q": q, "o": [[L, t] for L, t in zip("ABCD", opts)], "v": v}
D['mcq'][str(Y)] = {str(k): v for k, v in {
 1: Q("A country is experiencing a financial crisis that is impacting its ability to repay its debt. Which of the following could assist in this situation?",
      ["World Bank", "World Trade Organization", "International Monetary Fund", "Organisation for Economic Co-operation and Development"]),
 2: Q("Data for a hypothetical economy shows increased unemployment due to a decrease in demand for specific skills. Which of the following is most likely to have increased?",
      ["Underemployment", "Hidden unemployment", "Frictional unemployment", "Structural unemployment"]),
 3: Q("Four neighbouring economies have joined to reduce tariffs on each other’s goods. What is this an example of?",
      ["Monetary union", "Regional business cycle", "Bilateral trade agreement", "Multilateral trade agreement"]),
 4: Q("A country’s Gini coefficient has increased. Which of the following is the most likely effect of this change in inequality?",
      ["Increased labour mobility", "Decreased level of national savings", "Decreased levels of relative poverty", "Increased consumption and utility levels"]),
 5: Q("The graph shows the changes in aggregate supply (AS) for a hypothetical economy. Which row of the table shows the most likely combination of the cause and effect of the shift of the aggregate supply curve?",
      ["Increased labour productivity Increased population", "Decreased labour productivity Increased productive capacity", "Increased regulation Increased population", "Decreased regulation Increased productive capacity"], True),
 6: Q("The budget deficit of an economy decreased from Year 1 to Year 2 due to measures taken by its government. The change is most likely to have been caused by a decrease in",
      ["the level of company profits.", "energy rebates for households.", "the number of jobs in the economy.", "tariffs imposed on overseas imports."]),
 7: Q("How are Australian company dividends paid to foreign investors recorded on Australia’s balance of payments?",
      ["Current account debit", "Current account credit", "Portfolio investment debit", "Portfolio investment credit"]),
 8: Q("Which of the following could account for market failure in the supply of a good with positive externalities?",
      ["Increased demand for the good", "Decreased cost of providing the good", "Decreased tax incentives for providing the good", "Increased government subsidies for using the good"]),
 9: Q("The following table shows selected economic data for a hypothetical economy. An increase in which of the following best accounts for the changes from Year 1 to Year 2 in this economy?",
      ["Increase in childcare subsidies", "Increase in number of jobs available", "Increase in level of economic activity", "Increase in the level of income tax rates"], True),
 10: Q("The following table shows selected economic data for a hypothetical economy. What is the rate of unemployment in Year 2?",
      ["10%", "20%", "40%", "60%"], True),
 11: Q("A government has increased the regulation of foreign investment into its domestic economy. Which of the following is the most likely to increase as a result of this change?",
      ["Levels of globalisation", "The country’s capital account balance", "The country’s current account balance", "The demand for the country’s currency"]),
 12: Q("The table shows selected information for the balance of payments for an economy with a floating exchange rate. What is the value of the balance of goods and services?",
      ["$0 billion", "$10 billion", "$15 billion", "$35 billion"], True),
 13: Q("A government is seeking to finance a budget deficit. Which of the following would have the least impact on price stability in this economy?",
      ["Increasing money supply", "Repaying government debt", "Borrowing from the central bank", "Issuing government securities in the domestic market"]),
 14: Q("An economy has moved from a fixed exchange rate to a floating exchange rate. Which of the following is the most likely outcome?",
      ["The exchange rate movements will be less volatile.", "The exchange rate will be less reactive to world shocks.", "The central bank will need to hold a greater volume of foreign reserves.", "The impact of changes in the balance of payments on the exchange rate will be greater."]),
 15: Q("Assume that prices rise in a major trading partner of Australia. All other things being equal, how are the terms of trade and volume of imports likely to be affected?",
      ["Decrease Increase", "Decrease Decrease", "Increase Increase", "Increase Decrease"], True),
 16: Q("The table shows selected data for a hypothetical economy. In Year 3, the economy experiences a decrease in its government spending by $2 billion. All other things being equal, what would be the national income in Year 3?",
      ["$90 billion", "$98 billion", "$110 billion", "$150 billion"], True),
 17: Q("An economy has experienced a decline in its net foreign equity and an increase in its net foreign liabilities. Which of the following is most likely for this economy?",
      ["Terms of trade have improved.", "Net foreign debt has decreased.", "Net primary income balance has worsened.", "Financial account balance has remained constant."]),
 18: Q("The Australian economy experiences an increase in nominal GDP but its real GDP has remained constant. Which row of the table shows the combination of factors most likely to account for this?",
      ["Lower domestic cash rate Higher labour costs", "Higher domestic cash rate Lower labour costs", "Increased government spending Appreciation of AUD", "Decreased government spending Depreciation of AUD"], True),
 19: Q("In Year 1, one Australian dollar buys 1.15 US dollars. In Year 2, one US dollar buys 1.15 Australian dollars. All other things being equal, which row of the table shows the combination of the most likely factors that have led to this change in Year 2?",
      ["Lower global commodity demand Increase in speculative investment into the US", "Higher global commodity demand Increase in foreign direct investment into Australia", "Increase in foreign investment by Australians US interest rates are relatively lower than the Australian interest rates", "Decrease in foreign investment by Australians US interest rates are relatively higher than the Australian interest rates"], True),
 20: Q("The graph shows the domestic demand and supply for a particular good in an economy. The world price is $40. The government of this economy is seeking the most effective method to increase local production of this good. Which of the following statements is true?",
      ["A tariff of $20 is less effective than a quota of 0.", "A tariff of $20 is more effective than a quota of 0.", "A tariff of $10 is less effective than a quota of 10.", "A tariff of $10 is more effective than a quota of 10."], True),
}.items()}

LF = {"t": "tbl", "rows": [["Year", "Working age population (million)", "Employed persons (million)", "Labour force participation rate"], ["1", "5", "2", "60%"], ["2", "5", "2", "50%"]]}
def opt(head, rows): return {"t": "opt", "head": head, "rows": [[L] + r for L, r in zip("ABCD", rows)]}
def img(f, px, **kw): return dict({"t": "img", "f": f, "w": round(px[0] / 3), "h": round(px[1] / 3)}, **kw)
D['figs'][str(Y)] = {
 "I": {
  "5": [img("2026-I-5-1.webp", (919, 777)), opt(["Cause", "Effect"], [["Increased labour productivity", "Increased population"], ["Decreased labour productivity", "Increased productive capacity"], ["Increased regulation", "Increased population"], ["Decreased regulation", "Increased productive capacity"]])],
  "9": [LF], "10": [LF],
  "12": [{"t": "tbl", "rows": [["Category", "Dollars (billion)"], ["Imports", "25"], ["Net primary income", "−15"], ["Net secondary income", "5"], ["Capital account", "20"], ["Financial account", "−20"], ["Net errors and omissions", "0"]]}],
  "15": [opt(["Terms of trade", "Volume of imports"], [["Decrease", "Increase"], ["Decrease", "Decrease"], ["Increase", "Increase"], ["Increase", "Decrease"]])],
  "16": [{"t": "tbl", "rows": [["Year", "Income ($ billion)", "Consumption ($ billion)"], ["1", "50", "50"], ["2", "100", "90"]]}],
  "18": [opt(["Factor causing an increase in nominal GDP", "Factor causing real GDP to remain constant"], [["Lower domestic cash rate", "Higher labour costs"], ["Higher domestic cash rate", "Lower labour costs"], ["Increased government spending", "Appreciation of AUD"], ["Decreased government spending", "Depreciation of AUD"]])],
  "19": [opt(["", ""], [["Lower global commodity demand", "Increase in speculative investment into the US"], ["Higher global commodity demand", "Increase in foreign direct investment into Australia"], ["Increase in foreign investment by Australians", "US interest rates are relatively lower than the Australian interest rates"], ["Decrease in foreign investment by Australians", "US interest rates are relatively higher than the Australian interest rates"]])],
  "20": [img("2026-I-20-1.webp", (889, 806))],
 },
 "II": {"21": [img("2026-II-Q21-1.webp", (1055, 758), show=["Q21(a)"])]},
 "III": {"25": [img("2026-III-Q25-1.webp", (1219, 1741))], "26": [img("2026-III-Q26-1.webp", (1421, 1364))]},
}
L21 = "In a hypothetical economy, a government has provided a subsidy to the domestic production of a particular good. This is shown below. The world price is $40."
L23 = "The Reserve Bank of Australia has decided to decrease the cash rate."
D['s2'][str(Y)] = {it['l']: {"t": it['t'], "m": it['m'], "lead": {"Q21(a)": L21, "Q23(a)": L23, "Q23(b)": L23, "Q23(c)": L23}.get(it['l'])} for it in items if it['s'] == 'II'}
figdir = P.parent / 'figs'
for sec in D['figs'][str(Y)].values():
    for bl in sec.values():
        for b in bl:
            if b['t'] == 'img': assert (figdir / b['f']).exists(), b['f']

out = h[:i] + json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + h[i + n:]
def sub(old, new):
    global out
    assert out.count(old) == 1, old
    out = out.replace(old, new)
sub("Section I covers 2009–2025 (17 papers); Sections II, III and IV cover 2002–2025.", "Section I covers 2009–2026 (18 papers); Sections II, III and IV cover 2002–2026.")
sub("Earlier years and 2025 have no criteria in the page; use\n  the link to the guidelines instead.",
    "Earlier years have no criteria in the page; use\n  the link to the guidelines instead. The 2026 marking guidelines had not been published when the 2026 paper was\n  added, so 2026 has no multiple-choice answers and no criteria yet.")
P.write_text(out, encoding='utf-8')
print('added', len(items), 'items for 2026; total', len(D['items']))
