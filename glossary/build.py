#!/usr/bin/env python3
"""Build glossary/index.html from glossary/template.html and glossary/data/glossary.json.

    python3 glossary/build.py           # write index.html
    python3 glossary/build.py --check   # change nothing; fail if index.html is out of date

data/glossary.json is the one list: edit a term or definition there, then run this.
data/suggested.json holds draft terms that are not on the site until moved into glossary.json.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SYL = REPO / "evidence-finder" / "data" / "syllabus.json"
FONTS = REPO / "evidence-finder" / "build" / "fonts.css"


def build():
    g = json.loads((HERE / "data" / "glossary.json").read_text(encoding="utf8"))
    syl = json.loads(SYL.read_text(encoding="utf8"))
    h09 = next(f for f in syl["frameworks"] if f["id"] == "h09")
    topics = [{"id": t["id"], "label": t["label"], "name": t["name"], "color": t["color"]} for t in h09["topics"]]
    ids, seen = {t["id"] for t in topics}, set()
    for t in g["terms"]:
        assert t.get("id") and t.get("term") and t.get("def"), f"incomplete entry: {t}"
        assert re.fullmatch(r"[a-z0-9-]+", t["id"]), f'bad id: {t["id"]}'
        assert t["id"] not in seen, f'duplicate id: {t["id"]}'
        assert t.get("topics") and set(t["topics"]) <= ids, f'{t["term"]}: topics must be from {sorted(ids)}'
        seen.add(t["id"])
    g["terms"].sort(key=lambda t: t["term"].lower())
    data = {"source": g["source"], "updated": g["updated"], "topics": topics, "terms": g["terms"]}
    html = (HERE / "template.html").read_text(encoding="utf8")
    html = html.replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
    html = html.replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
    return html, data


if __name__ == "__main__":
    html, data = build()
    target = HERE / "index.html"
    if "--check" in sys.argv:
        ok = target.exists() and target.read_text(encoding="utf8") == html
        print("glossary/index.html is up to date" if ok else "glossary/index.html is OUT OF DATE: run glossary/build.py")
        sys.exit(0 if ok else 1)
    target.write_text(html, encoding="utf8")
    per = {t["label"]: sum(1 for x in data["terms"] if t["id"] in x["topics"]) for t in data["topics"]}
    print(f'Wrote {target} ({len(html)//1024} KB): {len(data["terms"])} terms ({", ".join(f"{k} {v}" for k, v in per.items())}).')
