#!/usr/bin/env python3
"""Pull source links out of a handout/digest PDF's extracted text. Used when filing new items."""
import re, sys, json

URL = re.compile(r"https?://\S+")

def join_wrapped(lines):
    """Re-join URLs that pdftotext wrapped mid-token."""
    out, i = [], 0
    lines = [l.rstrip() for l in lines]
    while i < len(lines):
        cur = lines[i]
        while i + 1 < len(lines):
            toks = cur.split()
            nxt = lines[i + 1].strip()
            if not toks or not nxt:
                break
            last = toks[-1]
            if last.startswith("http") or (len(last) > 60 and "/" in last and " " not in last):
                first = nxt.split(" ")[0]
                if first in ("·", "—", "-") or re.match(r"^\d+\.$", first):
                    break
                cur = cur + nxt if len(nxt.split()) == 1 or True else cur
                i += 1
                continue
            break
        out.append(cur)
        i += 1
    return out

def numbered_sources(text):
    m = re.search(r"\n\s*SOURCES\s*\n(.*?)(\n\s*Note:|\n\s*HSC Economics ·|\Z)", text, re.S)
    if not m:
        return []
    block = [l.strip() for l in m.group(1).split("\n") if l.strip()]
    entries, cur = [], None
    for l in block:
        mm = re.match(r"^(\d+)\.\s+(.*)", l)
        if mm:
            cur = [mm.group(2)]; entries.append(cur)
        elif cur is not None:
            # URL wrapped across lines: glue without a space when the previous piece is inside a URL
            prev = cur[-1]
            if "http" in prev and not prev.endswith(" ") and " " not in prev.split("http", 1)[1]:
                cur[-1] = prev + l
            else:
                cur.append(l)
    res = []
    for e in entries:
        s = " ".join(e)
        u = URL.search(s)
        if not u:
            continue
        url = u.group(0)
        label = s[: u.start()].strip().rstrip(".").strip()
        res.append({"label": label, "url": url})
    return res

def digest_articles(text):
    m = re.search(r"\n\s*Articles:\s*(.*?)\n\s*HSC Economics ·", text, re.S)
    if not m:
        return []
    lines = join_wrapped(m.group(1).split("\n"))
    s = " ".join(l.strip() for l in lines)
    parts = [p.strip() for p in re.split(r"\s·\s(?=[A-Z])", s)]
    res = []
    for p in parts:
        p = re.sub(r"^Articles:\s*", "", p)
        u = URL.search(p)
        if not u:
            continue
        label = p[: u.start()].rstrip("— -").strip()
        res.append({"label": label, "url": u.group(0)})
    return res

if __name__ == "__main__":
    t = open(sys.argv[1], encoding="utf-8").read().replace("\f", "\n")
    r = numbered_sources(t) or digest_articles(t)
    print(json.dumps(r, indent=1, ensure_ascii=False))
