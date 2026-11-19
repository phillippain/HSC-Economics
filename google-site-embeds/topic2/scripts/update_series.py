#!/usr/bin/env python3
"""
Daily updater for the Topic 2 "Charts and data" pages.

Reads Reserve Bank of Australia statistical tables (which republish ABS data) and rewrites
google-site-embeds/topic2/data/series.json. The chart pages read that file every time they load,
so the charts stay current without anyone editing a page.

Tables and series
  I1   trade balance and current account (% of GDP), exports and imports as a share of GDP,
       export and import volumes by type (chain volumes, quarterly)
  H1   nominal GDP and the terms of trade index (quarterly)
  I5   net foreign debt, net foreign equity and net foreign liabilities (quarterly)
  F11  monthly exchange rates (US dollar, TWI, renminbi, yen, euro)
  I2   Reserve Bank index of commodity prices (monthly, A$ and US$)
  F11.1 daily US dollar rate and TWI (last 130 trading days)

Safety rules (the same as the Economy at a Glance updater)
  * If a table cannot be downloaded, the block that needs it is left exactly as it was.
  * A block is never replaced by one that ends earlier or is much shorter than the one on file.
  * The file is rewritten only when a figure has changed.

Usage:  python3 google-site-embeds/topic2/scripts/update_series.py
        python3 google-site-embeds/topic2/scripts/update_series.py --fixtures DIR [--out FILE]
"""
import argparse
import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "series.json"
REPO = HERE.parents[2]

# Reuse the table reader that the Economy at a Glance job already runs every day.
_spec = importlib.util.spec_from_file_location("update_rba", REPO / "economy-at-a-glance" / "scripts" / "update_rba.py")
rba = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rba)

SOURCE = "Reserve Bank of Australia statistical tables I1, H1, I5, F11, F11.1 and I2 (ABS and RBA data)"


def bn(v):      # $ million -> $ billion, one decimal
    return round(v / 1000, 1)


def r1(v):
    return round(v, 1)


def r2(v):
    return round(v, 2)


def r4(v):
    return round(v, 4)


# block -> (date key, first key kept, [(table, series id, name, transform)])
QUARTERLY = [
    ("i1", "HCAGSCPGDP", "ca_pct", r1), ("i1", "HTBGSCPGDP", "tb_pct", r1),
    ("i1", "HXEGSCPGDP", "x_pct", r1), ("i1", "HMIGSCPGDP", "m_pct", r1),
    ("h1", "GOPITT", "tot", r1), ("h1", "GGDPECCPGDP", "gdp_nom", bn),
    ("i5", "HANFLSFDT", "nfd", bn), ("i5", "HANFLSEL", "nfe", bn), ("i5", "HANFLST", "nfl", bn),
    ("i1", "HXEGSCVGR", "x_rural", bn), ("i1", "HXEGSCVGRE", "x_res", bn),
    ("i1", "HXEGSCVGM", "x_man", bn), ("i1", "HXEGSCVS", "x_serv", bn),
    ("i1", "HMIGSCVGCO", "m_cons", bn), ("i1", "HMIGSCVGCA", "m_cap", bn),
    ("i1", "HMIGSCVGI", "m_int", bn), ("i1", "HMIGSCVS", "m_serv", bn),
]
MONTHLY = [
    ("f11", "FXRUSD", "usd", r4), ("f11", "FXRTWI", "twi", r1), ("f11", "FXRCR", "cny", r4),
    ("f11", "FXRJY", "jpy", r2), ("f11", "FXREUR", "eur", r4),
    ("i2", "GRCPAIAD", "com_aud", r1), ("i2", "GRCPAIUSD", "com_usd", r1),
]
DAILY = [("f11.1", "FXRUSD", "usd", r4), ("f11.1", "FXRTWI", "twi", r1)]


def ym(d):
    return f"{d.year}-{d.month:02d}"


def ymd(d):
    return d.isoformat()


def build(tables, spec, key, first, keep_last=None):
    """Align the series on one sorted list of date keys. Returns None if a table is missing."""
    for t, sid, _, _ in spec:
        if not tables.get(t) or not tables[t].get(sid):
            return None
    keys = sorted({key(d) for t, sid, _, _ in spec for d, _ in tables[t][sid] if key(d) >= first})
    if keep_last:
        keys = keys[-keep_last:]
    pos = {k: i for i, k in enumerate(keys)}
    out = {}
    for t, sid, name, f in spec:
        a = [None] * len(keys)
        for d, v in tables[t][sid]:
            k = key(d)
            if k in pos:
                a[pos[k]] = f(v)
        out[name] = a
    return {"t": keys, "s": out}


def acceptable(new, old):
    """Never go backwards: the new block must end no earlier and be about as long as the old one."""
    if not old or not old.get("t"):
        return True
    return new["t"][-1] >= old["t"][-1] and len(new["t"]) >= 0.9 * len(old["t"])


def run(fixtures=None, out=OUT):
    needed = sorted({t for spec in (QUARTERLY, MONTHLY, DAILY) for t, *_ in spec})
    tables = {t: rba.load_table(t, fixtures) for t in needed}
    old = json.loads(out.read_text(encoding="utf-8")) if out.exists() else {}
    new = dict(old)
    for name, spec, key, first, keep in (("q", QUARTERLY, ym, "1959-09", None), ("m", MONTHLY, ym, "2000-01", None), ("d", DAILY, ymd, "2000-01-01", 130)):
        block = build(tables, spec, key, first, keep)
        if block is None:
            rba.warn(f"Topic 2 charts: block '{name}' left as it was (a table could not be read)")
        elif not acceptable(block, old.get(name)):
            rba.warn(f"Topic 2 charts: block '{name}' left as it was (the new data ends earlier or is shorter)")
        else:
            new[name] = block
    changed = any(new.get(k) != old.get(k) for k in ("q", "m", "d"))
    if not changed and old:
        print("Topic 2 charts: no new figures.")
        return False
    new["updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    new["source"] = SOURCE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(new, separators=(",", ":")) + "\n", encoding="utf-8")
    ends = {k: new[k]["t"][-1] for k in ("q", "m", "d") if k in new}
    print(f"Topic 2 charts: series.json updated; latest quarter, month and day: {ends}")
    return True


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixtures", help="read <table>-data.csv files from this folder instead of rba.gov.au")
    ap.add_argument("--out", help="write to this file instead of data/series.json")
    a = ap.parse_args()
    run(a.fixtures, Path(a.out) if a.out else OUT)
    sys.exit(0)
