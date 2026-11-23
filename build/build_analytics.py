#!/usr/bin/env python3
"""Put the Google Analytics tag on every HSC Economics tool page.

    python3 build/build_analytics.py           # write the tag into every page and template
    python3 build/build_analytics.py --check   # change nothing; fail if any page is missing it

The tag is written between the GA:START and GA:END markers at the top of <head>. Templates
and the pages built from them both carry it, so rebuilding a tool keeps the tag. The list of
pages is the same one the "Other tools" menu uses (PAGES in build_sitemenu.py), so a new tool
added there is picked up here too: run this script after adding it.

To change the measurement ID, edit GA_ID and run the script. To remove the tag everywhere,
set GA_ID to "" and run it.

Not tagged on purpose: the small card strips in google-site-embeds/ (they sit inside pages of
the Google Site, which has its own Analytics setting, so tagging them would count one visit
several times), the teacher review sheets in review/, and working copies.
"""
import re, sys
from pathlib import Path
from build_sitemenu import PAGES

ROOT = Path(__file__).resolve().parent.parent
CHECK = "--check" in sys.argv
GA_ID = "G-11YGV11ZES"

MARKED = re.compile(r"[ \t]*<!-- GA:START.*?<!-- GA:END -->\n", re.S)
HEAD = re.compile(r"<head[^>]*>\n?")
TITLE = re.compile(r"<title\b")   # the Topic Map has no <head> tag


def block():
    if not GA_ID:
        return ""
    return ("<!-- GA:START (Google Analytics; written by build/build_analytics.py, do not edit here) -->\n"
            f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}"
            f"gtag('js',new Date());gtag('config','{GA_ID}');</script>\n"
            "<!-- GA:END -->\n")


def patch(p):
    old = p.read_text(encoding="utf-8")
    s = MARKED.sub("", old)
    b = block()
    if b:
        m = HEAD.search(s[:5000])
        if m:
            at = m.end()
            if not s[:at].endswith("\n"):
                b = "\n" + b
        else:
            m = TITLE.search(s[:5000])
            at = m.start() if m else 0
        s = s[:at] + b + s[at:]
    return old, s


def main():
    stale, n = [], 0
    for files in PAGES.values():
        for f in files:
            p = ROOT / f
            if not p.exists():
                print(f"skipped (not found): {f}")
                continue
            old, new = patch(p)
            assert new.count("GA:START") == (1 if GA_ID else 0), f
            n += 1
            if old != new:
                stale.append(f)
                if not CHECK:
                    p.write_text(new, encoding="utf-8")
    print(f"analytics: tag {GA_ID or '(none)'} on {n} files")
    if CHECK:
        if stale:
            print("OUT OF DATE: " + ", ".join(stale) + ". Run python3 build/build_analytics.py")
            sys.exit(1)
        print("up to date")
        return
    print("wrote: " + (", ".join(stale) if stale else "nothing, already up to date"))


if __name__ == "__main__":
    main()
