#!/usr/bin/env python3
"""File new evidence from the Drive inbox into the Evidence Finder, and rebuild.

    python3 build/ingest.py status
        What is waiting in  Evidence Finder/inbox  on the shared drive: size,
        pages, any web address inside a dropped link or note, and whether the
        site already holds the same file.

    python3 build/ingest.py file "<inbox path>" <id> [--label "Original article"] [--as year11]
        Copy one inbox file to  files/YYYY-MM/<id>.<ext>  in the repo (YYYY-MM
        comes from the id), move the original to  Evidence Finder/filed/YYYY-MM/
        so the inbox empties, and print the "file" block for the record.
        --as year11 files it as the card's SECOND document (the Year 11 version
        of a story whose card already has, or is about to get, an HSC summary):
        it goes to  files/YYYY-MM/<id>-year11.<ext>  and the block printed is
        "file11". One story is one card, however many summaries it has.

    python3 build/ingest.py archive "<inbox path>" [--note "why"]
        Move an inbox item to  filed/  without copying it into the repo: a
        dropped link or note once its story is filed, a duplicate, or something
        that does not belong on the site.

    python3 build/ingest.py refresh [--commit "<message>"]
        Rebuild index.html (build_site.py checks every tag and file), report
        what is still in the inbox, and with --commit make a git commit of
        data/, files/ and index.html. Pushing is left to GitHub Desktop.

The daily news task drops an index beside its PDFs,  _index-YYYY-MM-DD.json ,
listing each story's number, title, source link, HSC and Year 11 links and the
names of its PDFs. `status` uses it to show which PDFs belong to the same story
and which existing cards look like the same story; `refresh` moves an index to
filed/ once none of its PDFs is left in the inbox.

Between `status` and `refresh` come the judgement calls, made by a person or by
Claude through the add-economics-evidence skill: the id, the record in
data/evidence.json and its syllabus tags (see ADDING.md).
"""

import datetime, hashlib, json, os, re, shutil, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(ROOT)

EF_CANDIDATES = [
    os.environ.get("ECON_EVIDENCE_FINDER", ""),
    "/Users/phillip/Library/CloudStorage/GoogleDrive-phillip.pain@education.nsw.gov.au/"
    "Shared drives/HSC_Economics_SSCBWB/Evidence Finder",
    os.path.expanduser("~/mnt/HSC_Economics_SSCBWB/Evidence Finder"),
]
EF = next((c for c in EF_CANDIDATES if c and os.path.isdir(os.path.join(c, "inbox"))), None)
if not EF:
    sys.exit("Cannot find the Evidence Finder folder on the shared drive (one containing "
             "`inbox`). Connect HSC_Economics_SSCBWB, or set ECON_EVIDENCE_FINDER to its path.")
INBOX = os.path.join(EF, "inbox")
FILED = os.path.join(EF, "filed")
LOG = os.path.join(ROOT, "data", "ingest-log.jsonl")
SKIP = {".DS_Store", "Icon\r", "Thumbs.db", "desktop.ini"}
LINKY = {".txt", ".url", ".webloc", ".md", ".html", ".htm", ".eml", ".gdoc", ".rtf"}
ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")


# --------------------------------------------------------------------- bits

def retry(fn, what):
    """Drive for desktop sometimes refuses a file it has only just synced
    (EDEADLK, 'Resource deadlock avoided'). Try a few times before giving up."""
    last = None
    for _ in range(6):
        try:
            return fn()
        except PermissionError:
            raise
        except OSError as e:
            last = e
            time.sleep(1.5)
    raise OSError(f"could not {what}: {last}. Drive may still be syncing it; wait a "
                  "minute and run again, or stage the file and copy it across by hand.")


def walk(base):
    out = []
    for d, dirs, names in os.walk(base):
        dirs[:] = sorted(x for x in dirs if not x.startswith("."))
        for n in sorted(names):
            if n in SKIP or n.startswith(".") or n.startswith("_"):
                continue
            out.append(os.path.relpath(os.path.join(d, n), base).replace(os.sep, "/"))
    return out


def md5(path):
    def go():
        h = hashlib.md5()
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()
    return retry(go, f"read {os.path.basename(path)}")


def pages(path):
    if not path.lower().endswith(".pdf"):
        return None
    try:
        out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
        m = re.search(r"^Pages:\s+(\d+)", out, re.M)
        return int(m.group(1)) if m else None
    except OSError:
        return None


def urls_in(path):
    try:
        text = retry(lambda: open(path, "rb").read(200000), "read it").decode("utf-8", "ignore")
    except OSError:
        return []
    seen = []
    for u in re.findall(r"https?://[^\s\"'<>\\)]+", text):
        u = u.rstrip(".,;")
        if u not in seen:
            seen.append(u)
    return seen[:8]


def inbox_rel(path):
    """An inbox file's path relative to the inbox, however it was given: the bare
    name, inbox/<name>, or a full path on this machine or on the Mac."""
    p = os.path.expanduser(path.strip()).replace("\\", "/")
    parts = p.split("/")
    for i in range(len(parts) - 1, -1, -1):
        if parts[i].lower() == "inbox":
            return "/".join(parts[i + 1:])
    return p.lstrip("/")


def log(entry):
    entry["at"] = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


def load_indexes():
    """The daily task's index files -> {pdf name: (story, index date)} and the list of files."""
    by_pdf, files = {}, []
    for n in sorted(os.listdir(INBOX)):
        if not (n.startswith("_index-") and n.endswith(".json")):
            continue
        full = os.path.join(INBOX, n)
        try:
            idx = retry(lambda: json.load(open(full, encoding="utf-8")), f"read {n}")
        except (OSError, ValueError) as e:
            print(f"  !! {n}: {e}")
            continue
        files.append((n, idx))
        for st in idx.get("stories", []):
            for key in ("hsc_pdf", "year11_pdf"):
                if st.get(key):
                    by_pdf[st[key]] = (st, idx.get("date", ""))
    return by_pdf, files


STOP = set("the a an and of to in on for as at by with from is are its it after amid over into new says say "
           "australia australian economy economic per cent percent year".split())


def words(t):
    return {w for w in re.findall(r"[a-z0-9.%]+", t.lower()) if len(w) > 2 and w not in STOP}


def similar_cards(story, date, items):
    """Existing cards that look like the same story: same source link, or a close date and shared title words."""
    out, url, w = [], (story.get("url") or "").rstrip("/"), words(story.get("title", ""))
    try:
        d0 = datetime.date.fromisoformat(date)
    except ValueError:
        d0 = None
    for it in items:
        hit = url and any(((l.get("url") if isinstance(l, dict) else l[-1]) or "").rstrip("/") == url
                          for l in it.get("links", []) if l)
        if not hit and d0 and w:
            try:
                near = abs((datetime.date.fromisoformat(it["date"]) - d0).days) <= 4
            except ValueError:
                near = False
            hit = near and len(w & words(it["title"])) >= max(3, len(w) // 2)
        if hit:
            out.append(it)
    return out[:4]


def move_to_filed(src, month, name):
    dest_dir = os.path.join(FILED, month)
    os.makedirs(dest_dir, exist_ok=True)
    dest, stem, ext, n = os.path.join(dest_dir, name), *os.path.splitext(name), 2
    while os.path.exists(dest):
        dest = os.path.join(dest_dir, f"{stem} ({n}){ext}")
        n += 1
    try:
        retry(lambda: os.rename(src, dest), "move it out of the inbox")
    except PermissionError as e:
        sys.exit(f"Could not move the file out of the inbox ({e}). That needs delete "
                 "permission on the HSC_Economics_SSCBWB folder; allow it and run again.")
    parent = os.path.dirname(src)                      # tidy an emptied dropped folder
    while os.path.realpath(parent) != os.path.realpath(INBOX):
        try:
            os.rmdir(parent)
        except OSError:
            break
        parent = os.path.dirname(parent)
    return os.path.relpath(dest, EF).replace(os.sep, "/")


# ------------------------------------------------------------------- status

def status():
    inbox = walk(INBOX)
    items = json.load(open(os.path.join(ROOT, "data", "evidence.json"), encoding="utf-8"))
    by_size = {}
    for d, _, names in os.walk(os.path.join(ROOT, "files")):
        for n in names:
            p = os.path.join(d, n)
            by_size.setdefault(os.path.getsize(p), []).append(p)

    by_pdf, index_files = load_indexes()
    print(f"INBOX  {len(inbox)} item(s)   ({INBOX})")
    for rel in inbox:
        full = os.path.join(INBOX, rel)
        size = os.path.getsize(full)
        ext = os.path.splitext(rel)[1].lower()
        pg = pages(full)
        dropped = datetime.date.fromtimestamp(os.path.getmtime(full)).isoformat()
        print(f"  - {rel}   [{size/1024:.0f} KB{f', {pg} page(s)' if pg else ''}, dropped {dropped}]")
        if ext in LINKY:
            for u in urls_in(full):
                print(f"      link: {u}")
        if os.path.basename(rel) in by_pdf:
            st, idate = by_pdf[os.path.basename(rel)]
            kind = "Year 11 version" if st.get("year11_pdf") == os.path.basename(rel) else "HSC summary"
            print(f"      story {st.get('number', '?')} of {idate}: {st.get('title', '')}   [{kind}]")
            if st.get("url"):
                print(f"      source: {st.get('source', '')} {st['url']}")
            if st.get("syllabus_link"):
                print(f"      HSC link: {st['syllabus_link']}")
            if st.get("year11_link"):
                print(f"      Year 11 link: {st['year11_link']}")
            other = st.get("hsc_pdf") if kind == "Year 11 version" else st.get("year11_pdf")
            if other:
                where = "also in the inbox" if other in inbox else "not in the inbox"
                print(f"      SAME STORY as: {other}  ({where})  -> one card: HSC summary as `file`, "
                      "Year 11 version with `--as year11`")
            for it in similar_cards(st, idate, items):
                has11 = " (already has a Year 11 version)" if it.get("file11") else ""
                print(f"      possible existing card: {it['id']}  \"{it['title']}\"{has11}")
        same = []
        if size in by_size:
            try:
                h = md5(full)
                same = [os.path.relpath(p, ROOT) for p in by_size[size] if md5(p) == h]
            except OSError as e:
                print(f"      !! {e}")
        if same:
            print(f"      ALREADY ON THE SITE as: {'; '.join(same)}  (archive it rather than file it twice)")
    if not inbox:
        print("  nothing waiting")
    for n, idx in index_files:
        left = [st.get(k) for st in idx.get("stories", []) for k in ("hsc_pdf", "year11_pdf") if st.get(k) in inbox]
        print(f"  index {n}: {len(idx.get('stories', []))} stories, {len(left)} PDF(s) still to file")
    print(f"\nSITE   {len(items)} items in data/evidence.json; latest added "
          f"{max((i.get('added', '') for i in items), default='-')}")


# --------------------------------------------------------------------- file

def file_one(src_rel, new_id, label=None, as_year11=False):
    src_rel = inbox_rel(src_rel)
    src = os.path.join(INBOX, src_rel)
    if not os.path.isfile(src):
        sys.exit(f"Not in the inbox: {src_rel}")
    if not ID_RE.match(new_id):
        sys.exit(f"Refused: `{new_id}` is not an id of the form YYYY-MM-DD-short-slug.")
    items = json.load(open(os.path.join(ROOT, "data", "evidence.json"), encoding="utf-8"))
    month = new_id[:7]
    ext = os.path.splitext(src_rel)[1].lower() or ".pdf"
    rel = f"files/{month}/{new_id}{'-year11' if as_year11 else ''}{ext}"
    dest = os.path.join(ROOT, rel)
    if os.path.exists(dest):
        sys.exit(f"Refused: {rel} already exists. Choose another id, or `archive` the inbox copy.")
    existing = next((i for i in items if i["id"] == new_id), None)
    if existing and not as_year11:
        print(f"note    a record with id {new_id} already exists; this file will be its document")
    if existing and as_year11 and existing.get("file11"):
        sys.exit(f"Refused: the card {new_id} already has a Year 11 version ({existing['file11']['path']}).")
    if ext != ".pdf":
        print(f"note    {ext} file: the card's button says \"(PDF)\", so convert it to a PDF where you can")

    os.makedirs(os.path.dirname(dest), exist_ok=True)
    retry(lambda: shutil.copyfile(src, dest), "copy it into the repo")
    if md5(dest) != md5(src):
        os.replace(dest, dest + ".partial")
        sys.exit("Refused: the copy does not match the original (Drive still syncing?). "
                 "Nothing was moved; run again in a minute.")
    print(f"copied  inbox/{src_rel}  ->  evidence-finder/{rel}")
    pg = pages(dest)
    kept = move_to_filed(src, month, f"{new_id} - {os.path.basename(src_rel)}")
    print(f"moved   inbox/{src_rel}  ->  {kept}")
    log({"action": "file", "from": f"inbox/{src_rel}", "to": rel, "original": kept})

    block = {"path": rel, "label": label or ("Year 11 version" if as_year11 else "Original article")}
    if pg:
        block["pages"] = pg
    if as_year11:
        print(f"\nAdd to the record {new_id} in data/evidence.json" +
              ("" if existing else " (no such record yet: write it, with the HSC summary or this file as `file`)") + ":")
        print(f'  "file11": {json.dumps(block, ensure_ascii=False)}')
        print("and check the card has Year 11 (y11) tags.")
        return
    print("\nFor the record in data/evidence.json:")
    print(f'  "id": "{new_id}",')
    print(f'  "file": {json.dumps(block, ensure_ascii=False)},')
    print(f'  "added": "{datetime.date.today().isoformat()}"')


def archive(src_rel, note=None):
    src_rel = inbox_rel(src_rel)
    src = os.path.join(INBOX, src_rel)
    if not os.path.isfile(src):
        sys.exit(f"Not in the inbox: {src_rel}")
    month = datetime.date.today().strftime("%Y-%m")
    kept = move_to_filed(src, month, os.path.basename(src_rel))
    print(f"moved   inbox/{src_rel}  ->  {kept}   (not copied to the site)")
    log({"action": "archive", "from": f"inbox/{src_rel}", "original": kept, "note": note or ""})


# ------------------------------------------------------------------ refresh

def git(*args, **kw):
    return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True, **kw)


def clear_locks():
    """In a device shell git cannot delete its own lock files; move them aside."""
    gd = os.path.join(REPO, ".git")
    for rel in ("HEAD.lock", "index.lock", "objects/maintenance.lock"):
        p = os.path.join(gd, rel)
        if os.path.exists(p):
            try:
                os.remove(p)
            except OSError:
                try:
                    os.rename(p, f"{p}.stale-{int(time.time() * 1000)}")
                except OSError:
                    pass


def refresh(commit_msg=None):
    r = subprocess.run([sys.executable, "build/build_site.py"], cwd=ROOT, capture_output=True, text=True)
    print((r.stdout + r.stderr).rstrip())
    if r.returncode:
        sys.exit("\nFAILED: build_site.py found problems. Nothing was committed.")

    items = json.load(open(os.path.join(ROOT, "data", "evidence.json"), encoding="utf-8"))
    used = {i["file"]["path"] for i in items} | {i["file11"]["path"] for i in items if i.get("file11")}
    orphans = []
    for d, _, names in os.walk(os.path.join(ROOT, "files")):
        for n in names:
            rel = os.path.relpath(os.path.join(d, n), ROOT).replace(os.sep, "/")
            if rel not in used and not n.startswith(".") and not n.endswith(".partial"):
                orphans.append(rel)
    waiting = walk(INBOX)
    for n, idx in load_indexes()[1]:                       # an index whose PDFs are all dealt with is finished
        if not any(st.get(k) in waiting for st in idx.get("stories", []) for k in ("hsc_pdf", "year11_pdf")):
            month = (idx.get("date") or datetime.date.today().isoformat())[:7]
            print(f"index   {n} is finished  ->  {move_to_filed(os.path.join(INBOX, n), month, n)}")
    print("\nREPORT")
    if orphans:
        print(f"  in files/ with no record ({len(orphans)}): write the record, or remove the file:")
        for p in sorted(orphans)[:15]:
            print("    " + p)
    print(f"  still in the inbox ({len(waiting)})" + (": " + "; ".join(waiting) if waiting else ""))

    if not commit_msg:
        print("\nBuilt. Commit and push (GitHub Desktop) to publish.")
        return
    clear_locks()
    who = git("log", "-1", "--format=%an%n%ae").stdout.split("\n")
    git("add", "evidence-finder/data", "evidence-finder/files", "evidence-finder/index.html")
    c = git("-c", f"user.name={who[0]}", "-c", f"user.email={who[1]}", "commit", "-m", commit_msg)
    print("\n" + (c.stdout + c.stderr).strip())
    clear_locks()
    if c.returncode == 0:
        print("Committed. Push it with GitHub Desktop (Push origin) to publish.")


# --------------------------------------------------------------------- main

def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd, rest = argv[0], argv[1:]

    def opt(flag):
        if flag in rest:
            i = rest.index(flag)
            val = rest[i + 1]
            del rest[i:i + 2]
            return val
        return None

    if cmd == "status":
        status()
    elif cmd == "file":
        label, kind = opt("--label"), opt("--as")
        if kind not in (None, "year11"):
            sys.exit("--as takes only: year11")
        if len(rest) != 2:
            sys.exit('usage: ingest.py file "<inbox path>" <id> [--label "Original article"] [--as year11]')
        file_one(rest[0], rest[1], label, kind == "year11")
    elif cmd == "archive":
        note = opt("--note")
        if len(rest) != 1:
            sys.exit('usage: ingest.py archive "<inbox path>" [--note "why"]')
        archive(rest[0], note)
    elif cmd == "refresh":
        refresh(opt("--commit"))
    else:
        sys.exit(f"unknown command `{cmd}` (status, file, archive, refresh)")


if __name__ == "__main__":
    main(sys.argv[1:])
