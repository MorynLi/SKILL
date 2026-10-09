#!/usr/bin/env python3
"""Find live Hacker News threads where this project has something to contribute.

    python3 docs/launch/find-threads.py            # last 7 days
    python3 docs/launch/find-threads.py --days 21
    python3 docs/launch/find-threads.py --min-points 100

Hacker News only. Reddit and Stack Overflow block automated reading, and Reddit is
where most of this audience actually is — those threads have to be found by hand.

## What it is looking for

Not "people with a CORS bug". Someone debugging their own middleware wants the bug
fixed, and a skill about explanation quality is off-topic there by Stack Overflow's own
rules.

The fit is threads *about* whether an explanation landed: the illusion of explanatory
depth, documentation that defines instead of explaining, whether working with an
assistant leaves you understanding anything.

## Before you post anything it finds

Delete the link. Does the comment still help the person? If not, it was an advert.
And when a comment passes that test comfortably, the link usually makes it worse.
"""

from __future__ import annotations

import argparse
import html
import json
import time
import urllib.parse
import urllib.request

API = "https://hn.algolia.com/api/v1/search"

# each: (query, why it might fit)
QUERIES = [
    ("illusion of explanatory depth", "the exact mechanism this project is built on"),
    ("vibe coding", "shipping code you cannot explain"),
    ("learning to code with AI", "whether the understanding arrives with the output"),
    ("technical writing", "explanation quality as a craft"),
    ("documentation", "docs that define instead of explaining"),
    ("Feynman", "on topic by name"),
    ("explain like", "how explanation gets done"),
    ("understanding code", "reading what you did not write"),
    ("agent skills", "the format itself"),
    ("prompt engineering", "adjacent, often drifts into explanation quality"),
]

# threads with these in the title are almost never a fit, whatever they match on
NOISE = ("hiring", "who is hiring", "yc ", "launch hn", "funding", "raises", "acquire")


def search(query: str, since: int, min_points: int, limit: int = 5) -> list[dict]:
    params = urllib.parse.urlencode({
        "query": query,
        "tags": "story",
        "numericFilters": f"created_at_i>{since},points>{min_points}",
        "hitsPerPage": limit,
    })
    req = urllib.request.Request(f"{API}?{params}",
                                 headers={"User-Agent": "feynman-technique/find-threads"})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r).get("hits", [])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=7)
    ap.add_argument("--min-points", type=int, default=30)
    args = ap.parse_args()

    since = int(time.time()) - 86400 * args.days
    now = time.time()
    seen: set[str] = set()
    found = 0

    print(f"Hacker News, last {args.days} days, above {args.min_points} points.\n")

    for query, why in QUERIES:
        try:
            hits = search(query, since, args.min_points)
        except Exception as exc:                       # network, rate limit, anything
            print(f"  {query}: {exc}")
            continue

        rows = []
        for h in hits:
            oid = h["objectID"]
            title = html.unescape(h.get("title") or "")
            if oid in seen or any(n in title.lower() for n in NOISE):
                continue
            seen.add(oid)
            age_h = (now - h["created_at_i"]) / 3600
            # HN comments past ~72h are read by almost nobody
            heat = "LIVE " if age_h < 36 else ("cooling" if age_h < 96 else "cold")
            rows.append((heat, age_h, h.get("points", 0),
                         h.get("num_comments") or 0, title, oid))

        if not rows:
            continue
        print(f"── {query}  ({why})")
        for heat, age_h, pts, cs, title, oid in sorted(rows, key=lambda r: r[1]):
            found += 1
            print(f"   {heat:8} {age_h:5.0f}h  {pts:>4}pts {cs:>4}c  {title[:60]}")
            print(f"            https://news.ycombinator.com/item?id={oid}")
        print()

    if not found:
        print("Nothing live. That is the normal result — this conversation surfaces")
        print("every few weeks, not every day. Try again in a week, or --days 30 to")
        print("see what the recurring threads look like.")
        return 0

    print("Anything marked LIVE is worth reading. Anything cold is not worth a comment:")
    print("HN threads stop being read after about three days.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
