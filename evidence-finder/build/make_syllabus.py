#!/usr/bin/env python3
"""Combine the three syllabus trees, the vocabularies and the 2009<->2025 crosswalk into data/syllabus.json.

Inputs : data/qf_taxonomy.json   (2009 HSC tree, taken from the Question Finder so dot point codes match)
         data/syl2025.json       (parsed by build/parse_syl2025.py from the NESA PDF)
Output : data/syllabus.json
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
qf = json.load(open(f"{ROOT}/data/qf_taxonomy.json", encoding="utf-8"))
s25 = json.load(open(f"{ROOT}/data/syl2025.json", encoding="utf-8"))

# ---------------------------------------------------------------- 2009 HSC
COL09 = {"T1": "#2447d6", "T2": "#0e8a8a", "T3": "#d9822b", "T4": "#8a3fb0"}
topics09 = []
for t in qf["syl"]:
    tid = t["c"]
    short = re.sub(r"^Topic \d — ", "", t["n"])
    secs = []
    for h in t["h"]:
        sid = h["d"][0]["c"].split(".")[0]
        secs.append({"id": sid, "name": h["n"], "points": [{"id": d["c"], "t": d["t"]} for d in h["d"]]})
    skills = next((s for s in qf["ssk"] if s["c"] == tid), None)
    if skills:
        sid = skills["d"][0]["c"].split(".")[0]
        secs.append({"id": sid, "name": "Skills: students learn to", "skills": True, "points": [{"id": d["c"], "t": d["t"]} for d in skills["d"]]})
    topics09.append({"id": tid, "name": short, "label": t["n"].split(" — ")[0], "color": COL09[tid], "sections": secs})

# ---------------------------------------------------------------- 2025
COL25 = {"P1": "#5b6472", "P2": "#2f9e5b", "P3": "#d9528a", "P4": "#0e8a8a", "P5": "#8a3fb0", "P6": "#2447d6",
         "Y1": "#d9822b", "Y2": "#8a3fb0", "Y3": "#2447d6"}
def tree25(year):
    out = []
    for a in s25:
        if a["year"] != year:
            continue
        out.append({"id": a["id"], "name": a["name"], "label": ("Focus area " + a["id"][1:]),
                    "color": COL25[a["id"]],
                    "sections": [{"id": s["id"], "name": s["name"],
                                  "points": [{"id": p["id"], "t": p["t"], **({"eg": p["eg"]} if p.get("eg") else {})} for p in s["points"]]}
                                 for s in a["sections"]]})
    return out

frameworks = [
    {"id": "h09", "label": "HSC", "sub": "2009 syllabus", "full": "HSC (2009 syllabus)",
     "note": "Year 12 until the HSC in 2027.", "topics": topics09},
    {"id": "y12", "label": "HSC", "sub": "2025 syllabus", "full": "HSC (2025 syllabus)",
     "note": "Year 12 from Term 4 2027; first examined in 2028.", "topics": tree25(12)},
    {"id": "y11", "label": "Year 11", "sub": "2025 syllabus", "full": "Year 11 (2025 syllabus)",
     "note": "Year 11 from Term 1 2027.", "topics": tree25(11)},
]

# ---------------------------------------------------------------- crosswalk (section level)
# Each pair says: evidence filed under a section on the left is also useful under the sections on the right.
XWALK = [
    ("1A", ["Y3a", "Y3b", "Y3e"]),
    ("1B", ["Y3a", "Y3b"]),
    ("1C", ["Y3a"]),
    ("1D", ["Y3d", "Y3e"]),
    ("1E", ["Y3e"]),
    ("2A", ["Y3a", "Y3b", "P6a", "P6b"]),
    ("2B", ["Y3e", "P6d"]),
    ("2C", ["Y3c", "P6c"]),
    ("2D", ["Y3a"]),
    ("3A", ["Y1a", "P1e"]),
    ("3B", ["Y1b"]),
    ("3C", ["Y1c"]),
    ("3D", ["Y3e", "P6d"]),
    ("3E", ["Y1d"]),
    ("3F", ["Y1e", "P2h"]),
    ("4A", ["Y2a"]),
    ("4B", ["Y2a", "Y2g"]),
    ("4C", ["Y2b", "P5b", "P5c"]),
    ("4D", ["Y2c", "P4c"]),
    ("4E", ["Y2d"]),
    ("4F", ["Y2e"]),
    ("4G", ["Y2f"]),
    ("4H", ["Y2g"]),
    ("4I", ["Y2g"]),
]

# ---------------------------------------------------------------- vocabularies
issues = [
    {"id": "growth", "label": "Economic growth and GDP"},
    {"id": "employment", "label": "Employment and unemployment"},
    {"id": "inflation", "label": "Inflation and cost of living"},
    {"id": "rates", "label": "Interest rates and the cash rate"},
    {"id": "fx", "label": "The Australian dollar"},
    {"id": "trade", "label": "Trade and commodity prices"},
    {"id": "investment", "label": "Investment and foreign capital"},
    {"id": "housing", "label": "Housing and household wealth"},
    {"id": "budget", "label": "Budget, tax and debt"},
    {"id": "inequality", "label": "Income and wealth distribution"},
    {"id": "environment", "label": "Environment and energy"},
    {"id": "productivity", "label": "Productivity and supply side"},
    {"id": "global", "label": "Global economy and institutions"},
]
levers = [
    {"id": "fiscal", "label": "Fiscal policy"},
    {"id": "monetary", "label": "Monetary policy"},
    {"id": "micro", "label": "Microeconomic policy"},
    {"id": "labour", "label": "Labour market policy"},
    {"id": "environmental", "label": "Environmental policy"},
    {"id": "trade", "label": "Trade and investment policy"},
    {"id": "global", "label": "International co-operation"},
]
types = [
    {"id": "news", "label": "News", "plural": "News articles"},
    {"id": "stats", "label": "Statistics", "plural": "Statistics and data"},
    {"id": "report", "label": "Report", "plural": "Reports and documents"},
    {"id": "graph", "label": "Graph", "plural": "Graphs and diagrams"},
    {"id": "case", "label": "Case study", "plural": "Case studies"},
]
diagrams = [
    {"id": "adas", "label": "AD–AS"},
    {"id": "ds", "label": "Demand and supply"},
    {"id": "phillips", "label": "Phillips curve"},
    {"id": "fx", "label": "AUD market"},
    {"id": "flow", "label": "Flow chart"},
    {"id": "chart", "label": "Data chart"},
    {"id": "compare", "label": "Compare table"},
]

out = {
    "meta": {"title": "HSC Economics Evidence Finder",
             "syllabi": ["Economics Stage 6 Syllabus (Board of Studies NSW, 2009)", "Economics 11–12 (2025) (NSW Education Standards Authority)"]},
    "frameworks": frameworks, "xwalk": XWALK,
    "issues": issues, "levers": levers, "types": types, "diagrams": diagrams,
}
json.dump(out, open(f"{ROOT}/data/syllabus.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for f in frameworks:
    n = sum(len(s["points"]) for t in f["topics"] for s in t["sections"])
    print(f["id"], f["full"], len(f["topics"]), "topics", n, "points")
