#!/usr/bin/env python3
"""Parse the NESA Economics 11-12 (2025) syllabus text into data/syl2025.json.

Input : pdftotext -layout output of the syllabus PDF (path in argv[1])
Output: JSON written to argv[2]

Shape: [ {id, year, name, sections:[ {id, name, points:[ {id, t, eg} ]} ]} ]
IDs: P<n> for Year 11 focus areas, Y<n> for Year 12 ones; dot points  P1a.3 etc.
"""
import json, re, sys

src, dst = sys.argv[1], sys.argv[2]
lines = open(src, encoding="utf-8").read().replace("\f", "").split("\n")

start = next(i for i, l in enumerate(lines) if l.strip() == "Outcomes and content for Year 11" and i > 150)
end = next(i for i, l in enumerate(lines) if l.strip() == "Assessment" and i > start)
body = lines[start:end]

FOOT = re.compile(r"^Economics 11–12 \(2025\)\s+Page \d+ of 38")
Y11 = ["Introduction to economics", "Markets", "Household and business sector",
       "Financial sector", "Government sector", "International sector"]
Y12 = ["Economic issues in the Australian economy",
       "Economic management of the Australian economy", "Australia and the global economy"]

areas, cur_area, cur_sec, cur_pt, in_eg = [], None, None, None, False
year = 11
i = 0
state = "pre"  # pre | outcomes | content

def clean(t):
    t = re.sub(r"\s+", " ", t).strip()
    t = t.replace(" ,", ",")
    return t

for raw in body:
    l = raw.rstrip()
    if FOOT.match(l.strip()):
        continue
    s = l.strip()
    if s == "Outcomes and content for Year 12":
        year = 12; continue
    if s == "Outcomes and content for Year 11":
        continue
    names = Y11 if year == 11 else Y12
    nxt = next((x.strip() for x in body[body.index(raw) + 1:] if x.strip()), "")
    if s in names and not l.startswith(" ") and nxt == "Outcomes":
        cur_area = {"name": s, "year": year, "sections": []}
        areas.append(cur_area); cur_sec = None; cur_pt = None; state = "outcomes"; in_eg = False
        continue
    if s == "Outcomes" and state == "outcomes":
        continue
    if s == "Content":
        state = "content"; continue
    if state != "content" or not s:
        if not s:
            continue
        continue
    # content state
    if l.startswith("§"):
        txt = clean(l[1:])
        cur_pt = {"t": txt, "eg": ""}
        cur_sec["points"].append(cur_pt); in_eg = False
        continue
    if s.startswith("Example(s):"):
        in_eg = True; continue
    if not l.startswith(" "):
        # a new section heading (or the next focus area header handled above)
        cur_sec = {"name": clean(s), "points": []}
        cur_area["sections"].append(cur_sec); cur_pt = None; in_eg = False
        continue
    # indented line: continuation of bullet, example, or formula fragment
    indent = len(l) - len(l.lstrip())
    if in_eg and cur_pt is not None:
        cur_pt["eg"] = clean(cur_pt["eg"] + " " + s)
    elif cur_pt is not None and indent <= 6:
        cur_pt["t"] = clean(cur_pt["t"] + " " + s)
    # else: formula fragment, dropped (flagged later)

# ---- ids
out = []
letters = "abcdefghijklmnopqrstuvwxyz"
p = y = 0
for a in areas:
    if a["year"] == 11:
        p += 1; aid = f"P{p}"
    else:
        y += 1; aid = f"Y{y}"
    sec_out = []
    for si, sec in enumerate(a["sections"]):
        sid = f"{aid}{letters[si]}"
        pts = [{"id": f"{sid}.{pi+1}", "t": pt["t"], **({"eg": pt["eg"]} if pt["eg"] else {})}
               for pi, pt in enumerate(sec["points"])]
        sec_out.append({"id": sid, "name": sec["name"], "points": pts})
    out.append({"id": aid, "year": a["year"], "name": a["name"], "sections": sec_out})

# ---- formula dot points: the PDF's equation objects extract as fragments, so these are
# restated in plain text (checked against the layout of the syllabus pages).
FIX = {
 "P2e.3": "Calculate price elasticity of demand using the percentage method formula: PED = % change in quantity demanded ÷ % change in price",
 "P3a.5": "Determine the marginal propensity to consume (MPC = change in consumption ÷ change in income)",
 "Y1a.2": "Calculate real GDP using the formula: real GDP = nominal GDP × (CPI base ÷ CPI current)",
 "Y1a.3": "Relationship between GDP and economic growth, including the growth rate: (real GDP current − real GDP previous) ÷ real GDP previous × 100",
 "Y1a.7": "Effect of changes in the terms of trade (export price index ÷ import price index × 100) on net exports and aggregate demand",
 "Y1a.9": "Calculate and interpret the simple expenditure multiplier (k) using the formula k = 1 ÷ (1 − MPC), and its effect on national income using the formula ΔY = k × ΔAE",
 "Y1b.3": "Calculate and interpret the rate of labour force participation using the formula: labour force ÷ working-age population × 100",
 "Y1b.7": "Calculate and interpret the rate of unemployment using the formula: unemployed ÷ labour force × 100",
 "Y1b.9": "Relationship between the labour force, labour force participation rate, unemployment rate and labour force underutilisation rate ((unemployed + underemployed) ÷ labour force × 100)",
 "Y1c.2": "Measurement of inflation from the consumer price index (CPI) using the formula: (CPI current − CPI previous) ÷ CPI previous × 100",
}
for a in out:
    for sec in a["sections"]:
        for pt in sec["points"]:
            if pt["id"] in FIX:
                pt["t"] = FIX[pt["id"]]
            pt["t"] = pt["t"].replace("Co- operation", "Co-operation")

json.dump(out, open(dst, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
tot = sum(len(s["points"]) for a in out for s in a["sections"])
print(f"{len(out)} focus areas · {sum(len(a['sections']) for a in out)} sections · {tot} dot points")
for a in out:
    print(a["id"], a["name"], [len(s["points"]) for s in a["sections"]])
