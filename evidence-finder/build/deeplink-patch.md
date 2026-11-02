# Card deep-link patch (Economics Evidence Finder)

The daily summary links each item to `.../evidence-finder/#item=<record id>&fw=h09|y12|y11`. The
Finder opens that card only if `build/template.html` contains the code in `deeplink-template.diff`
(apply with `git apply`, or make the three edits by hand: add `linkedItem()` and `openLinked()` above
the `hashchange` listener, call `openLinked` from that listener, and call it once at the end of boot).
Then run `python3 build/build_site.py` and push to `main`.

Check: open `index.html#item=<any record id>&fw=h09`; the card should be expanded at the top of the
page. An unknown id, or no hash, behaves exactly as before. Tested in Chromium on 3 Nov 2026 for
HSC 2009, HSC 2025 and Year 11 links, on first load and on hash change.

If a rebuild or an older template copy loses the code, the collector's NOTE says "no #item=<id>
deep-link code" until it is restored.
