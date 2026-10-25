#!/usr/bin/env python3
"""python3 build/_validate.py build/_batches/batchN.json  -- same checks as build_site.py, for one batch file."""
import json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
syl=json.load(open(f"{ROOT}/data/syllabus.json",encoding="utf-8"))
items=json.load(open(sys.argv[1],encoding="utf-8"))
ids={f["id"]:{p["id"] for t in f["topics"] for s in t["sections"] for p in s["points"]} for f in syl["frameworks"]}
vocab={k:{o["id"] for o in syl[k]} for k in("issues","levers","types","diagrams")}
err=[]
for it in items:
    n=it.get("id","?")
    for k in("id","title","date","type","outlets","summary","about","also","issues","levers","diagrams","figures","links","file","terms","lede"):
        if k not in it: err.append(f"{n}: missing {k}")
    for k in("about","also"):
        for fw in ids:
            for t in it.get(k,{}).get(fw,[]):
                if t not in ids[fw]: err.append(f"{n}: unknown {fw} tag {t}")
    for f_,k in(("issues","issues"),("levers","levers"),("diagrams","diagrams")):
        for v in it.get(f_,[]):
            if v not in vocab[k]: err.append(f"{n}: unknown {f_} {v}")
    if it.get("type") not in vocab["types"]: err.append(f"{n}: type {it.get('type')}")
    for f in it.get("figures",[]):
        if f.get("issue") not in vocab["issues"]: err.append(f"{n}: figure issue {f.get('issue')}")
        for k in("label","value","asAt","source"):
            if k not in f: err.append(f"{n}: figure missing {k}")
    if not os.path.exists(f"{ROOT}/{it['file']['path']}"): err.append(f"{n}: missing file {it['file']['path']}")
    if not str(it.get("date","")).startswith("20") or len(it["date"])!=10: err.append(f"{n}: bad date")
    if not it["id"].startswith(it["date"]): err.append(f"{n}: id must start with date")
print("\n".join(err) if err else f"OK {len(items)} records")
sys.exit(1 if err else 0)
