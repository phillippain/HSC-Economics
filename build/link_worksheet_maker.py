#!/usr/bin/env python3
"""Put a "Make a PDF worksheet" button in the Question Finder's toolbar, beside "Print worksheet".

    python3 build/link_worksheet_maker.py           # add (or refresh) the button
    python3 build/link_worksheet_maker.py --check   # change nothing; fail if the button is missing

The button opens the Worksheet Maker in a new tab with the ticked questions in the address
(?qf=I2019Q1,II2019Q21(a),...). Passing them in the address matters on the Google Site: an embedded
Question Finder keeps its ticks in storage that a new tab cannot read.
Written between WM:START and WM:END markers, so running it again replaces the old copy.
"""
import re, sys
from pathlib import Path

QF = Path(__file__).resolve().parent.parent / "hsc-question-finder-site" / "index.html"
ANCHOR = '<button class="tool primary" id="sheet" type="button">Print worksheet</button>'
BLOCK = ('<!-- WM:START (written by build/link_worksheet_maker.py) -->'
         '<a class="tool" id="toWM" href="../worksheet-maker/" target="_blank" rel="noopener" style="text-decoration:none" '
         'title="Open the ticked questions in the Worksheet Maker: add other question types, set the page layout and download a PDF with an answer copy">'
         'Make a PDF worksheet ↗</a>'
         '<script>(function(){var a=document.getElementById("toWM");if(!a)return;a.addEventListener("click",function(){var ids=[];'
         'try{ids=JSON.parse(localStorage.getItem("hsc-qf-done")||"[]")}catch(e){}'
         'a.href="../worksheet-maker/"+(ids.length?"?qf="+encodeURIComponent(ids.join(",")):"");});})();</script>'
         '<!-- WM:END -->')

s = QF.read_text(encoding="utf8")
new = re.sub(r"\n[ \t]*<!-- WM:START.*?<!-- WM:END -->", "", s, flags=re.S)
assert ANCHOR in new, "the Print worksheet button was not found in the Question Finder"
new = new.replace(ANCHOR, ANCHOR + "\n      " + BLOCK, 1)
if "--check" in sys.argv:
    ok = s == new
    print("Question Finder has the Worksheet Maker button" if ok else "Question Finder button is MISSING or out of date: run build/link_worksheet_maker.py")
    sys.exit(0 if ok else 1)
QF.write_text(new, encoding="utf8")
print("Added the Make a PDF worksheet button to the Question Finder")
