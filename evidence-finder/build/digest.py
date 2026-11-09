#!/usr/bin/env python3
"""Collect what was added to (or changed in) the HSC Economics Evidence Finder since the last digest.

    python3 build/digest.py collect [--since YYYY-MM-DD] [--out PATH] [--site URL]
        Reads data/evidence.json and data/syllabus.json and writes a JSON file of the new and
        updated records, grouped by syllabus topic. Prints a readable listing. Read-only: it
        does not touch the saved state, so it can be re-run safely.

    python3 build/digest.py mark PATH_TO_DIGEST.json
        Record the digest as reported, so the next collect starts after it. Run it once the
        email page has been made.

    python3 build/digest.py status
        Show the saved state.

    python3 build/digest.py stamp [--date YYYY-MM-DD] [--write]
        One-off: give every record that has no `added` date one (the date of the git commit that
        introduced it, else --date, else the record's own `date`). Dry run unless --write.

"Added" is the `added` field on a record: the day it was FILED into the Finder (not the date of
the news story, which is `date`). New = `added` on or after the day before the last run and not
yet reported. A record with no `added` is dated from git history when it looks recent.
Updated = a record already reported or present at the last run whose content (summary, lede,
figures, terms, links, file, note and so on) has changed since. Changes to tags only are ignored.

State lives in data/digest-state.json (git-ignored). Dates are Sydney dates. Python 3 standard
library only.
"""

import argparse, datetime, json, os, re, subprocess, sys, time
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))      # .../evidence-finder
DATA = os.path.join(ROOT, "data", "evidence.json")
STATE = os.path.join(ROOT, "data", "digest-state.json")
OUT_DIR = os.path.join(ROOT, ".digest")
DEFAULT_SITE = "https://phillippain.github.io/HSC-Economics/evidence-finder/"

os.environ["TZ"] = "Australia/Sydney"
try:
    time.tzset()
except AttributeError:
    pass

# Fields whose change is news. Tag fields (about, also, issues, levers, diagrams) and `added` are not.
CONTENT = ["title", "type", "date", "dateText", "outlets", "summary", "lede", "figures", "terms",
           "links", "file", "angle", "questions", "extended", "note"]
TEXT_FIELDS = ["title", "summary", "lede", "angle", "note", "extended"]
TYPE_LABEL = {"news": "News", "stats": "Statistics", "report": "Report", "graph": "Graph", "case": "Case study"}
FW_ORDER = ["h09", "y12", "y11"]
FW_NAME = {"h09": "HSC · 2009 syllabus", "y12": "HSC · 2025 syllabus", "y11": "Year 11 · 2025 syllabus"}
FW_SHORT = {"h09": "HSC 2009", "y12": "HSC 2025", "y11": "Year 11"}
FW_COURSE = {"h09": "hsc", "y12": "hsc25", "y11": "prelim"}


# ----------------------------------------------------------------- helpers ----
def today():
    return datetime.datetime.now().date()


def prev_school_day(d):
    d -= datetime.timedelta(days=1)
    while d.weekday() >= 5:
        d -= datetime.timedelta(days=1)
    return d


def git(*args):
    r = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def content_of(rec):
    return {k: rec.get(k) for k in CONTENT if rec.get(k) not in (None, "", [], {})}


def link_pair(l):
    if isinstance(l, dict):
        return l.get("label", ""), l.get("url", "")
    return (l[0], l[1]) if len(l) > 1 else ("", l[0])


# ------------------------------------------------------------------ syllabus --
def load_syllabus():
    """Return topics {(fw, topic id): {...}} in syllabus order, and points {(fw, code): text}."""
    syl = load_json(os.path.join(ROOT, "data", "syllabus.json"), {})
    topics, points = {}, {}
    for fw in syl.get("frameworks", []):
        for t in fw["topics"]:
            topics[(fw["id"], t["id"])] = {"fw": fw["id"], "id": t["id"], "label": t["name"],
                                           "part": t.get("label", ""), "color": t.get("color", "#2447d6")}
            for s in t.get("sections", []):
                for p in s.get("points", []):
                    points[(fw["id"], p["id"])] = p["t"]
    return topics, points


def topic_id(fw, code):
    """h09 '3C.3' -> 'T3'; y12 'Y2b.6' -> 'Y2'; y11 'P2d.1' -> 'P2'."""
    m = re.match(r"^(\d)", code) if fw == "h09" else re.match(r"^([YP]\d)", code)
    return ("T" + m.group(1)) if (m and fw == "h09") else (m.group(1) if m else None)


def place(rec, topics):
    """One home for each record: HSC 2009 topic, else HSC 2025 focus area, else Year 11 focus area."""
    tg = lambda fw, kind: (rec.get(kind) or {}).get(fw) or []
    for fw in FW_ORDER:                              # about tags first, across frameworks
        for code in tg(fw, "about"):
            t = topic_id(fw, code)
            if (fw, t) in topics:
                return (fw, t)
    for fw in FW_ORDER:                              # then supporting tags
        for code in tg(fw, "also"):
            t = topic_id(fw, code)
            if (fw, t) in topics:
                return (fw, t)
    return None


# ------------------------------------------------------------------- records --
def build_item(rec, status, topics, points, base, added, added_from):
    rid = rec["id"]
    home = place(rec, topics)
    tags = {}
    for fw in FW_ORDER:
        about = (rec.get("about") or {}).get(fw) or []
        also = (rec.get("also") or {}).get(fw) or []
        tags[fw] = {"about": [{"code": c, "text": points.get((fw, c), "")} for c in about],
                    "also": [{"code": c, "text": points.get((fw, c), "")} for c in also]}
    also_topics = []                       # other topics in the same syllabus that the record touches
    if home:
        fw0 = home[0]
        for code in ((rec.get("about") or {}).get(fw0) or []) + ((rec.get("also") or {}).get(fw0) or []):
            k = (fw0, topic_id(fw0, code))
            if k in topics and k != home and f"{k[0]}:{k[1]}" not in also_topics:
                also_topics.append(f"{k[0]}:{k[1]}")
    f = rec.get("file") or {}
    pdf = (base + quote(f["path"])) if f.get("path") else ""
    links = [link_pair(l) for l in rec.get("links", [])]
    figs = [{"i": i, **fg} for i, fg in enumerate(rec.get("figures", []))]
    hsc_fw = "y11" if (home and home[0] == "y11") else "h09" if (home and home[0] == "h09") else "y12"
    return {
        "id": rid, "status": status, "type": rec.get("type", ""),
        "type_label": TYPE_LABEL.get(rec.get("type", ""), rec.get("type", "").title()),
        "title": rec.get("title", rid), "added": added, "added_from": added_from,
        "date": rec.get("date", ""), "date_text": rec.get("dateText", ""),
        "outlets": rec.get("outlets", []), "summary": rec.get("summary", ""), "lede": rec.get("lede", ""),
        "angle": rec.get("angle", ""), "note": rec.get("note", ""),
        "questions": rec.get("questions", []), "figures": figs, "terms": rec.get("terms", []),
        "tags": tags, "home": list(home) if home else None, "also_topics": also_topics,
        "card_url": f"{base}#item={quote(rid)}&fw={hsc_fw}" if base else "",
        "pdf_url": pdf, "pdf_label": f.get("label", "PDF"), "pdf_pages": f.get("pages"),
        "pdf_path": f.get("path", ""), "source_label": links[0][0] if links else "",
        "source_url": links[0][1] if links else "", "n_links": len(links),
    }


def snapshot_of(recs):
    return {r["id"]: content_of(r) for r in recs}


def describe_change(before, after):
    """Plain-language facts about what changed, for the summary writer."""
    out = {"fields": [], "text": {}, "figures_added": [], "figures_changed": [], "links_added": []}
    for k in CONTENT:
        b, a = before.get(k), after.get(k)
        if b == a:
            continue
        out["fields"].append(k)
        if k in TEXT_FIELDS:
            out["text"][k] = {"before": (b or "")[:400], "after": (a or "")[:600]}
    bf = {fg.get("label"): fg for fg in before.get("figures", [])}
    for fg in after.get("figures", []):
        old = bf.get(fg.get("label"))
        if old is None:
            out["figures_added"].append(fg)
        elif old != fg:
            out["figures_changed"].append({"label": fg.get("label"), "before": old.get("value"),
                                           "after": fg.get("value"), "asAt": fg.get("asAt")})
    bl = {link_pair(l)[1] for l in before.get("links", [])}
    out["links_added"] = [link_pair(l)[0] for l in after.get("links", []) if link_pair(l)[1] not in bl]
    return out


def git_added_dates(ids, path_rel):
    """Date of the commit that first introduced each id into evidence.json (needs real history)."""
    out = {}
    for rid in ids:
        r = git("log", "-S" + f'"id": "{rid}"', "--format=%cs", "--reverse", "--", path_rel)
        first = r.strip().split("\n")[0] if r.strip() else ""
        if first:
            out[rid] = first
    return out


# ------------------------------------------------------------------ commands --
def cmd_collect(a):
    recs = load_json(DATA, [])
    topics, points = load_syllabus()
    state = load_json(STATE, {}) or {}
    reported = state.get("reported", {})
    t = today()
    prefix = git("rev-parse", "--show-prefix").strip()
    path_rel = prefix + "data/evidence.json"          # repo-root path, for `git show <sha>:<path>`
    log_path = "data/evidence.json"                    # path relative to evidence-finder, for `git -C ROOT log`
    base = a.site or os.environ.get("EVIDENCE_SITE_URL") or DEFAULT_SITE
    if not base.endswith("/"):
        base += "/"

    if a.since:
        start, basis = datetime.date.fromisoformat(a.since), f"--since {a.since}"
    elif state.get("last_run"):
        last = datetime.datetime.fromisoformat(state["last_run"]).date()
        start = last - datetime.timedelta(days=1)
        basis = f"the last digest ({state['last_run'][:16].replace('T', ' ')}), looking back a day"
    else:
        start = prev_school_day(t)
        basis = f"first run: from the last school day, {start.strftime('%A %-d %B')}"

    # --- when was each record filed? `added`, else git history for recent-looking records
    notes, added, added_from = [], {}, {}
    missing = [r for r in recs if not r.get("added")]
    for r in recs:
        if r.get("added"):
            added[r["id"]], added_from[r["id"]] = r["added"], "record"
    probe_from = (start - datetime.timedelta(days=45)).isoformat()
    probe = [r["id"] for r in missing if r.get("date", "") >= probe_from]
    gd = git_added_dates(probe, log_path) if probe else {}
    for rid, d in gd.items():
        added[rid], added_from[rid] = d, "git"
    if missing:
        n_git = len(gd)
        notes.append(f"{len(missing)} record(s) have no `added` date" +
                     (f"; {n_git} recent one(s) were dated from git history" if n_git else "") +
                     ". Run `python3 build/digest.py stamp --write` once to stamp them all, and add "
                     "`\"added\": \"YYYY-MM-DD\"` when filing new items.")
        if probe and not gd:
            notes.append("Git history gave no dates (shallow clone or file not committed yet), so these "
                         "could not be treated as new: " + ", ".join(probe[:8]) + ("…" if len(probe) > 8 else ""))

    by_id = {r["id"]: r for r in recs}
    new_ids = [rid for rid, d in added.items()
               if start.isoformat() <= d <= t.isoformat() and rid not in reported]
    future = sorted(rid for rid, d in added.items() if d > t.isoformat())

    # --- updated: compare with the snapshot taken at the last `mark`
    before = state.get("snapshot")
    if before is None:
        sha = git("rev-list", "-1", f"--before={start.isoformat()}T00:00:00", "HEAD").strip()
        blob = git("show", f"{sha}:{path_rel}") if sha else ""
        try:
            before = snapshot_of(json.loads(blob)) if blob else None
        except json.JSONDecodeError:
            before = None
        if before is None:
            notes.append("No saved snapshot and no earlier git version, so updated records cannot be "
                         "detected on this run (new ones are unaffected).")
    updated = {}
    for r in recs:
        rid = r["id"]
        if before and rid in before and rid not in new_ids:
            now_c = content_of(r)
            if now_c != before[rid]:
                ch = describe_change(before[rid], now_c)
                if ch["fields"]:
                    updated[rid] = ch
    # --- items
    items = [build_item(by_id[rid], "new", topics, points, base, added[rid], added_from[rid]) for rid in new_ids]
    for rid, ch in updated.items():
        it = build_item(by_id[rid], "updated", topics, points, base, added.get(rid, ""), added_from.get(rid, ""))
        it["update"] = ch
        items.append(it)

    # --- groups: HSC 2009 topics, HSC 2025 focus areas, Year 11 focus areas, then anything untagged
    groups = []
    for key, meta in topics.items():
        its = [i for i in items if i["home"] == list(key)]
        if its:
            its.sort(key=lambda i: (i["status"] != "new", i["added"], i["title"]))
            groups.append({"key": f"{key[0]}:{key[1]}", "fw": key[0], "course": FW_COURSE[key[0]],
                           "course_label": FW_NAME[key[0]], **{k: meta[k] for k in ("label", "part", "color")},
                           "items": its})
    other = [i for i in items if i["home"] is None]
    if other:
        groups.append({"key": "other", "fw": "", "course": "other", "course_label": "Not yet tagged",
                       "label": "Not yet tagged to the syllabus", "part": "", "color": "#4a5468", "items": other})
    order = {"hsc": 0, "hsc25": 1, "prelim": 2, "other": 3}
    fwpos = {k: n for n, k in enumerate(topics)}
    groups.sort(key=lambda g: (order[g["course"]], fwpos.get(tuple(g["key"].split(":")), 99)))
    labels = {f"{k[0]}:{k[1]}": f"{FW_SHORT[k[0]]} · {v['part']}: {v['label']}" for k, v in topics.items()}

    # --- notes for the teacher
    ahead = git("rev-list", "--count", "@{u}..HEAD").strip()
    if ahead.isdigit() and int(ahead) > 0:
        notes.append(f"{ahead} commit(s) have not been pushed: links to those items will not work until "
                     "you push to main.")
    if git("status", "--porcelain", "--", "data/evidence.json").strip():
        notes.append("data/evidence.json has uncommitted changes: commit and push before sending, or the "
                     "card and PDF links will not exist on the site yet.")
    try:
        site_text = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    except OSError:
        site_text = ""
    if site_text and "linkedItem" not in site_text:
        notes.append("index.html has no #item=<id> deep-link code, so 'Open the card' links open the Finder "
                     "at the top, not the card. See references/deeplink-patch.md in the skill.")
    if site_text:
        miss = [i["id"] for i in items if f'"id":"{i["id"]}"' not in site_text]
        if miss:
            notes.append("Not in the current index.html build (run build/build_site.py): " + ", ".join(miss))
    nopdf = [i["id"] for i in items if i["pdf_path"] and not os.path.exists(os.path.join(ROOT, i["pdf_path"]))]
    if nopdf:
        notes.append("PDF file is missing on disk: " + ", ".join(nopdf))
    due = [i["id"] for i in items if "UPDATE DUE" in (i["note"] or "").upper()]
    if due:
        notes.append("These items say an update is due (see their note): " + ", ".join(due))
    if future:
        notes.append("Records with an `added` date after today were left out: " + ", ".join(future))

    digest = {"generated": datetime.datetime.now().isoformat(timespec="seconds"), "today": t.isoformat(),
              "window_start": start.isoformat(), "basis": basis, "site_url": base,
              "counts": {"new": sum(i["status"] == "new" for i in items),
                         "updated": sum(i["status"] == "updated" for i in items)},
              "topic_labels": labels, "groups": groups, "notes": notes}
    out = a.out or os.path.join(OUT_DIR, f"digest-{t.isoformat()}.json")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(digest, f, indent=1, ensure_ascii=False)

    print(f"Digest window: {basis}")
    print(f"{digest['counts']['new']} new, {digest['counts']['updated']} updated  ->  {out}\n")
    for g in groups:
        print(f"== {g['course_label']} · {g['part']} {g['label']}")
        for i in g["items"]:
            print(f"  [{i['status'].upper()}] {i['id']}  ·  {i['type_label']}  ·  filed {i['added']}"
                  f"{' (from git)' if i['added_from'] == 'git' else ''}  ·  {', '.join(i['outlets'])}")
            print(f"    title: {i['title']}")
            print(f"    summary: {i['summary']}")
            print(f"    lede: {i['lede'][:700]}")
            if i["angle"]:
                print(f"    use it for: {i['angle'][:450]}")
            if i["note"]:
                print(f"    caution: {i['note'][:450]}")
            for fg in i["figures"]:
                print(f"    figure [{fg['i']}]: {fg.get('label')} = {fg.get('value')}  "
                      f"(as at {fg.get('asAt')}; {fg.get('source')})")
            for fw in FW_ORDER:
                ab = i["tags"][fw]["about"]
                if ab:
                    print(f"    {FW_SHORT[fw]} about: " + "; ".join(f"{x['code']} {x['text']}" for x in ab))
            if i["status"] == "updated":
                u = i["update"]
                print(f"    CHANGED: {', '.join(u['fields'])}")
                for k, v in u["text"].items():
                    print(f"      {k} before: {v['before'][:200]}\n      {k} after:  {v['after'][:300]}")
                for fg in u["figures_added"]:
                    print(f"      figure added: {fg.get('label')} = {fg.get('value')} ({fg.get('asAt')})")
                for fg in u["figures_changed"]:
                    print(f"      figure changed: {fg['label']}: {fg['before']} -> {fg['after']}")
                if u["links_added"]:
                    print(f"      links added: {'; '.join(u['links_added'])}")
        print()
    for n in notes:
        print("NOTE:", n)


def cmd_mark(a):
    digest = load_json(a.digest)
    if not digest:
        sys.exit(f"Cannot read {a.digest}")
    recs = load_json(DATA, [])
    state = load_json(STATE, {}) or {}
    reported = state.setdefault("reported", {})
    for g in digest["groups"]:
        for i in g["items"]:
            if i["status"] == "new":
                reported[i["id"]] = digest["today"]
    cutoff = (today() - datetime.timedelta(days=90)).isoformat()
    state["reported"] = {k: v for k, v in reported.items() if v >= cutoff}
    state["snapshot"] = snapshot_of(recs)
    state["last_run"] = datetime.datetime.now().isoformat(timespec="seconds")
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    with open(STATE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False)
    print(f"Marked {digest['counts']['new']} new and {digest['counts']['updated']} updated item(s) as reported. "
          f"Last run: {state['last_run']}")


def cmd_status(a):
    s = load_json(STATE)
    if not s:
        print("No digest has been marked yet: the next collect starts from the last school day "
              f"({prev_school_day(today()).strftime('%A %-d %B')}).")
        return
    print(f"Last run: {s.get('last_run')}\nReported items (90 days): {len(s.get('reported', {}))}"
          f"\nSnapshot records: {len(s.get('snapshot', {}))}")


def cmd_stamp(a):
    """Insert `"added": "..."` after the `date` line of records that lack it, editing the file as text
    so nothing else in evidence.json changes."""
    text = open(DATA, encoding="utf-8").read()
    recs = json.loads(text)
    prefix = git("rev-parse", "--show-prefix").strip()
    missing = [r for r in recs if not r.get("added")]
    gd = git_added_dates([r["id"] for r in missing], "data/evidence.json")
    plan = {}
    for r in missing:
        plan[r["id"]] = gd.get(r["id"]) or a.date or r.get("date")
    print(f"{len(missing)} record(s) lack `added`; {len(gd)} dated from git history, "
          f"{len(missing) - len(gd)} from {'--date' if a.date else 'their own date'}.")
    if not a.write:
        for rid, d in list(plan.items())[:10]:
            print(f"  {rid} -> {d}")
        print("Dry run. Add --write to edit data/evidence.json.")
        return
    indent = re.search(r'\n( +)"date":', text)
    ind = indent.group(1) if indent else "  "
    n = 0
    for rid, d in plan.items():
        pat = re.compile(r'("id":\s*"' + re.escape(rid) + r'",\s*\n(?:.*\n)*?)(\s*)("date":\s*"[^"]*",?)')
        m = pat.search(text)
        if not m:
            print(f"  could not place `added` for {rid}; skipped")
            continue
        line = m.group(3)
        comma = "," if line.endswith(",") else ""
        new = f'{m.group(1)}{m.group(2)}{line if comma else line + ","}\n{ind}"added": "{d}"{comma}'
        text = text[:m.start()] + new + text[m.end():]
        n += 1
    json.loads(text)                                           # must still be valid JSON
    open(DATA, "w", encoding="utf-8").write(text)
    print(f"Stamped {n} record(s). Now run python3 build/build_site.py and commit.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("collect")
    c.add_argument("--since")
    c.add_argument("--out")
    c.add_argument("--site")
    c.set_defaults(fn=cmd_collect)
    m = sub.add_parser("mark")
    m.add_argument("digest")
    m.set_defaults(fn=cmd_mark)
    sub.add_parser("status").set_defaults(fn=cmd_status)
    s = sub.add_parser("stamp")
    s.add_argument("--date")
    s.add_argument("--write", action="store_true")
    s.set_defaults(fn=cmd_stamp)
    args = ap.parse_args()
    args.fn(args)
