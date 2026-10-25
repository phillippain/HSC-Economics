#!/usr/bin/env python3
"""Assemble index.html from data/syllabus.json + data/evidence.json + build/template.html.

Run from anywhere:  python3 build/build_site.py
Also checks every tag, issue, lever, diagram and file path, and refuses to build if anything is unknown.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
syl = json.load(open(f"{ROOT}/data/syllabus.json", encoding="utf-8"))
items = json.load(open(f"{ROOT}/data/evidence.json", encoding="utf-8"))

# ---------------------------------------------------------------- validation
ids = {f["id"]: {p["id"] for t in f["topics"] for s in t["sections"] for p in s["points"]} for f in syl["frameworks"]}
vocab = {k: {o["id"] for o in syl[k]} for k in ("issues", "levers", "types", "diagrams")}
errors, seen = [], set()
for it in items:
    n = it.get("id", "?")
    if n in seen: errors.append(f"{n}: duplicate id")
    seen.add(n)
    for k in ("id", "title", "date", "type", "outlets", "summary", "about", "also", "issues", "levers", "diagrams", "figures", "links", "file", "terms", "lede"):
        if k not in it: errors.append(f"{n}: missing {k}")
    for k in ("about", "also"):
        for fw in ids:
            it.setdefault(k, {}).setdefault(fw, [])
            for t in it[k][fw]:
                if t not in ids[fw]: errors.append(f"{n}: unknown {fw} tag {t}")
    for field, key in (("issues", "issues"), ("levers", "levers"), ("diagrams", "diagrams")):
        for v in it.get(field, []):
            if v not in vocab[key]: errors.append(f"{n}: unknown {field[:-1]} {v}")
    if it.get("type") not in vocab["types"]: errors.append(f"{n}: unknown type {it.get('type')}")
    for f in it.get("figures", []):
        if f["issue"] not in vocab["issues"]: errors.append(f"{n}: figure issue {f['issue']}")
    if not os.path.exists(f"{ROOT}/{it['file']['path']}"): errors.append(f"{n}: missing file {it['file']['path']}")
if errors:
    print("\n".join(errors)); sys.exit(1)

# ---------------------------------------------------------------- build
fonts = open(f"{ROOT}/build/fonts.css", encoding="utf-8").read()
tpl = open(f"{ROOT}/build/template.html", encoding="utf-8").read()
data = json.dumps({"syl": syl, "items": items}, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
out = tpl.replace("__FONTS__", fonts).replace("__DATA__", data)
open(f"{ROOT}/index.html", "w", encoding="utf-8").write(out)

n_pts = {fw: len(v) for fw, v in ids.items()}
print(f"index.html  {len(out)/1024:,.0f} KB  ·  {len(items)} items  ·  {sum(len(i['figures']) for i in items)} figures")
for fw in ids:
    cov = {t for i in items for t in i["about"][fw]}
    print(f"  {fw}: {len(cov)} of {n_pts[fw]} dot points have 'about' evidence")
print("placeholders left:", [p for p in ("__DATA__", "__FONTS__") if p in out] or "none")
