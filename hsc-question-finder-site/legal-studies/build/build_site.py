#!/usr/bin/env python3
"""Assemble index.html from syllabus.json + the extracted item sets."""

import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
syl = json.load(open(f"{ROOT}/data/syllabus.json"))
items = json.load(open(f"{ROOT}/data/items-extended.json"))

# Human Rights and Section I come later; the topic still appears so the coverage
# heatmap shows its elements as unexamined-so-far rather than hiding them.
ORDER = ["crime", "humanrights", "family", "shelter"]
topics = []
for k in ORDER:
    t = syl["topics"][k]
    topics.append({
        "k": k, "label": t["label"], "part": t["part"],
        "themes": t["themes"], "sections": t["sections"],
    })

data = {
    "meta": {
        "firstYear": min(i["y"] for i in items),
        "lastYear": max(i["y"] for i in items),
        "syllabus": syl["meta"]["syllabus"],
    },
    "bands": syl["demandBands"],
    "topics": topics,
    "items": items,
}

tpl = open(f"{ROOT}/build/template.html").read()
out = tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
with open(f"{ROOT}/index.html", "w") as f:
    f.write(out)

print(f"index.html  {len(out):,} bytes  ·  {len(items)} items  ·  {len(topics)} topics")

# ------------------------------------------------------------ sanity checks --
tagids = set()
for t in topics:
    for th in t["themes"]:
        tagids.add(th["id"])
    for s in t["sections"]:
        tagids.add(s["id"])
        for p in s["points"]:
            tagids.add(p["id"])

bad = set()
for it in items:
    for c in it["core"] + it["support"]:
        if c not in tagids:
            bad.add(c)
print("unknown tag ids:", sorted(bad) or "none")
print("items with no core:", sum(1 for i in items if not i["core"]))
print("placeholder left in html:", "__DATA__" in out)
