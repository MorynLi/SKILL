#!/usr/bin/env python3
"""Check the X thread against the 280 limit, using X's own counting rule.

    python3 docs/launch/check-x.py

X does not count characters. It counts weighted code points: most of Latin,
Greek, Cyrillic and general punctuation weigh 1, everything else weighs 2. An
arrow costs two, an em dash costs one, and a post one glyph over the line is
simply refused at submit time — which is a bad moment to find out.

It also renders no Markdown, so asterisks meant as emphasis appear literally.
"""
from __future__ import annotations

import pathlib
import re
import sys

# the ranges X weighs as 1; everything outside them weighs 2
ONE = [(0, 4351), (8192, 8205), (8208, 8223), (8242, 8247),
       (8254, 8254), (8264, 8278), (8289, 8303)]


def xlen(s: str) -> int:
    return sum(1 if any(a <= ord(c) <= b for a, b in ONE) else 2 for c in s)


def main() -> int:
    src = (pathlib.Path(__file__).parent / "x-thread.md").read_text()
    body = src.split("---\n", 1)[1].split("## If someone pushes back")[0]
    bad = 0
    for chunk in re.split(r"\n---\n", body):
        m = re.match(r"\*\*(\d+)\*\*[^\n]*\n(.*)", chunk.strip(), re.S)
        if not m:
            continue
        n, txt = m.group(1), m.group(2).strip()
        note = ""
        if xlen(txt) > 280:
            note, bad = f"  OVER by {xlen(txt) - 280}", bad + 1
        if re.search(r"\*", txt):
            note, bad = note + "  has an asterisk — X shows it literally", bad + 1
        print(f"  post {n}: {xlen(txt):>3}/280{note}")
    print("\nall nine fit" if not bad else f"\n{bad} to fix")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
