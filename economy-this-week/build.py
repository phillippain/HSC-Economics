#!/usr/bin/env python3
"""The Economy This Week archive page.

Reads every edition PDF in editions/, pulls out the date, cover summary, big exam idea and each story
(number, topic, headline, lead, page, key terms, 'Try this' question), renders the pages as JPEGs for
the in-page reader, looks up each file's Google Drive ID, and writes index.html from template.html.

Needs only python3 and poppler (pdftotext, pdftoppm). Runs in the device shell.

  python3 build.py                      rebuild from editions/
  python3 build.py --import DIR         first copy new editions from DIR (the Friday output folder)
  python3 build.py --drive DIR          shared-drive folder that holds the student copies
                                        (default: ~/mnt/HSC_Economics_SSCBWB/The Economy This Week)
  python3 build.py --check              rebuild and fail if any edition has no stories or no Drive ID

Corrections that the parser cannot work out go in overrides.json, keyed by edition id (YYYY-MM-DD).
"""
import json, os, re, shutil, subprocess, sys, glob, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ED, PG = os.path.join(HERE, "editions"), os.path.join(HERE, "pages")
NAME = re.compile(r"^12Eco[ _]The[ _]Economy[ _]This[ _]Week[ _](\d{1,2})([A-Z][a-z]{2})(\d{4})(.*)\.pdf$")
MON = {m: i for i, m in enumerate("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), 1)}
TOPICS = {1: "The Global Economy", 2: "Australia's Place in the Global Economy", 3: "Economic Issues", 4: "Economic Policies and Management"}


def arg(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default


def ed_id(fname):
    m = NAME.match(fname)
    if not m:
        return None
    d, mon, y, _ = m.groups()
    return "%s-%02d-%02d" % (y, MON[mon], int(d))


def import_from(src):
    """Copy one PDF per edition date: the plain name if it exists, otherwise the newest variant (_auto, _updated...)."""
    best = {}
    for p in glob.glob(os.path.join(src, "*.pdf")):
        f = os.path.basename(p); m = NAME.match(f)
        if not m:
            continue
        i = ed_id(f); plain = m.group(4) == ""
        key = (plain, os.path.getmtime(p))
        if i not in best or key > best[i][0]:
            best[i] = (key, p)
    added = []
    for i, (_, p) in sorted(best.items()):
        d, mon, y = NAME.match(os.path.basename(p)).groups()[:3]
        dst = os.path.join(ED, "12Eco_The_Economy_This_Week_%s%s%s.pdf" % (int(d), mon, y))
        if not os.path.exists(dst):
            shutil.copy2(p, dst); added.append(os.path.basename(dst))
    return added


def ind(l):
    return len(l) - len(l.lstrip())


def column_text(lines, col):
    return " ".join(x[col:].strip() for x in lines if len(x) > col and x[col:].strip())


def parse(path):
    t = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True, text=True).stdout
    pages = t.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    m = re.search(r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) (\d{1,2} \w+ \d{4})", t)
    long_date = m.group(0) if m else ""
    p0 = pages[0].split("\n"); summ = []
    k = next((i for i, l in enumerate(p0) if m and m.group(2) in l), 0) + 1
    while k < len(p0) and "Topic 1 ·" not in p0[k]:
        if p0[k].strip():
            summ.append(p0[k].strip())
        k += 1
    big = re.search(r"The big exam idea:\s*(.+?)(?:\n\s*\n)", pages[0], re.S)
    focus = re.search(r"Focus: (Topic \d|Balanced)", pages[0])
    stories = []
    for pi, p in enumerate(pages):
        L = p.split("\n")
        for i, l in enumerate(L):
            mm = re.match(r"^\s{0,4}(\d\d)\s{2,}TOPIC (\d)", l)
            if not mm:
                continue
            j = i + 1
            while j < len(L) and (not L[j].strip() or ind(L[j]) > 40):
                j += 1
            title = []
            while j < len(L) and L[j].strip() and ind(L[j]) == 0 and not L[j].startswith(("WHAT", "W H AT")):
                title.append(re.split(r"\s{3,}", L[j].strip())[0]); j += 1
            stand = []
            while j < len(L) and L[j].strip() and not re.match(r"\s*(W\s?H\s?AT|WHAT|Source)", L[j]):
                stand.append(re.split(r"\s{3,}", L[j].strip())[0]); j += 1
            blk = L[i + 1:i + 95]
            nxt = next((n for n, x in enumerate(blk) if re.match(r"^\s{0,4}\d\d\s{2,}TOPIC \d", x)), None)
            if nxt is not None:
                blk = blk[:nxt]
            text = "\n".join(blk)
            # key terms: 'Key terms: a · b · c' (Nov format) or a KEY TERMS box of 'Term: definition' (Oct format)
            terms = []
            kt = re.search(r"Key terms:\s*(.+?)(?:\n\s*\n|$)", text, re.S)
            if kt:
                raw = " ".join(re.split(r"\s{3,}", x.strip())[0] for x in kt.group(1).split("\n") if x.strip())
                raw = re.split(r"ALSO THIS WEEK|\(\d marks\)|The Economy This Week", raw)[0]
                terms = [x.strip(" .") for x in raw.split("·") if x.strip(" .")]
            else:
                kb = re.search(r"KEY TERMS\s*\n(.+?)(?:\n\s*\n\s*\n|[A-Z ]{8,}\s{3,})", text, re.S)
                if kb:
                    terms = list(dict.fromkeys(x.strip() for x in re.findall(r"(?:^|\s{2,})([A-Z][A-Za-z'\- ]{2,40}):", kb.group(1), re.M)))
            # 'Try this': take the text in the column under the heading, up to the first '(n marks)'
            q = ""
            for n, x in enumerate(blk):
                h = re.search(r"T\s?R\s?Y\s+T\s?H\s?I\s?S", x)
                if h:
                    rest = column_text(blk[n + 1:n + 9], h.start() - 1)
                    rest = re.sub(r"^\s*1\.\s*", "", rest)
                    mq = re.search(r"^(.+?\(\d+ marks?\))", rest)
                    q = (mq.group(1) if mq else rest[:260]).strip()
                    break
            stories.append(dict(n=mm.group(1), topic=int(mm.group(2)), title=" ".join(title), lead=" ".join(stand), page=pi + 1, terms=terms, q=q))
    return dict(date=long_date, pages=len(pages), summary=" ".join(summ), big=" ".join(big.group(1).split()) if big else "",
                focus=focus.group(1) if focus else "", stories=stories)


def drive_id(path):
    for attr in ("com.google.drivefs.item-id#S", "user.drive.id"):
        try:
            return os.getxattr(path, attr).decode()
        except Exception:
            pass
    return None


def main():
    os.makedirs(ED, exist_ok=True); os.makedirs(PG, exist_ok=True)
    src = arg("--import")
    if src:
        print("imported:", import_from(src) or "nothing new")
    drive_dir = os.path.expanduser(arg("--drive", "~/mnt/HSC_Economics_SSCBWB/The Economy This Week"))
    ids_path = os.path.join(HERE, "drive.json")
    ids = json.load(open(ids_path)) if os.path.exists(ids_path) else {}
    over = json.load(open(os.path.join(HERE, "overrides.json"))) if os.path.exists(os.path.join(HERE, "overrides.json")) else {}
    eds = []
    for path in glob.glob(os.path.join(ED, "*.pdf")):
        f = os.path.basename(path); i = ed_id(f)
        if not i:
            continue
        e = parse(path)
        # student copy on the shared drive: copy it there if missing, then read its Drive ID
        if os.path.isdir(drive_dir):
            dst = os.path.join(drive_dir, f)
            if not os.path.exists(dst):
                shutil.copy2(path, dst)
            got = drive_id(dst)
            if got:
                ids[f] = got
        # page images for the reader (rebuilt only when missing)
        imgs = []
        for n in range(1, e["pages"] + 1):
            out = os.path.join(PG, "%s-%d.jpg" % (i, n))
            if not os.path.exists(out):
                subprocess.run(["pdftoppm", "-jpeg", "-jpegopt", "quality=82", "-r", "110", "-f", str(n), "-l", str(n), "-singlefile", path, out[:-4]], check=True)
            imgs.append("pages/%s-%d.jpg" % (i, n))
        e.update(id=i, file=f, pdf="editions/" + f, drive=ids.get(f), images=imgs)
        o = over.get(i, {})
        for s in e["stories"]:
            s.update(o.get("stories", {}).get(s["n"], {}))
        for k, v in o.items():
            if k != "stories":
                e[k] = v
        eds.append(e)
    eds.sort(key=lambda e: e["id"], reverse=True)
    json.dump(ids, open(ids_path, "w"), indent=1, sort_keys=True)
    data = dict(built=datetime.date.today().isoformat(), topics=TOPICS, editions=eds)
    json.dump(data, open(os.path.join(HERE, "editions.json"), "w"), indent=1, ensure_ascii=False)
    tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
    js = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(tpl.replace("/*__DATA__*/null", js))
    bad = []
    for e in eds:
        print("%s  %2d pages  %2d stories  drive %s  %s" % (e["id"], e["pages"], len(e["stories"]), "yes" if e["drive"] else "NO ", e["date"]))
        if not e["stories"] or (not e["drive"] and "--check" in sys.argv):
            bad.append(e["id"])
        for s in e["stories"]:
            if not s["title"] or not s["q"]:
                print("   check story", s["n"], "title" if not s["title"] else "", "question" if not s["q"] else "")
    if "--check" in sys.argv and bad:
        sys.exit("problem editions: %s" % bad)


if __name__ == "__main__":
    main()
