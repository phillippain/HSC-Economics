#!/usr/bin/env python3
"""Build macro-diagram-lab/index.html from template.html (inlines the shared fonts).

    python3 macro-diagram-lab/build.py           # write index.html
    python3 macro-diagram-lab/build.py --check   # change nothing; fail if index.html is out of date

All diagrams, scenarios and wording are in template.html (the DG object).
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = HERE.parent / "evidence-finder" / "build" / "fonts.css"

html = (HERE / "template.html").read_text(encoding="utf8").replace("/*__FONTS__*/", FONTS.read_text(encoding="utf8") if FONTS.exists() else "")
target = HERE / "index.html"
if "--check" in sys.argv:
    ok = target.exists() and target.read_text(encoding="utf8") == html
    print("macro-diagram-lab/index.html is up to date" if ok else "macro-diagram-lab/index.html is OUT OF DATE: run macro-diagram-lab/build.py")
    sys.exit(0 if ok else 1)
target.write_text(html, encoding="utf8")
print(f"Wrote {target} ({len(html)//1024} KB)")
