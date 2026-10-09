#!/usr/bin/env python3
"""Generate the header image for every language.

    python3 assets/generate_heroes.py

## The layout

Two Claude Code sessions, the same problem, side by side. Both assistants diagnose
correctly, both propose the same fix, and both stop to ask permission — because that is
what these tools actually do. The difference is whether you can answer honestly.

    ┌──────────────────────────────────────────────────────────────────────┐
    │ › my checkout page won't load the orders. it just fails.             │
    └──────────────────────────────────────────────────────────────────────┘

    ┌────────────────────────────────┐  ┌────────────────────────────────┐
    │ ● ● ●  without feynman-technique│  │ ● ● ●     with feynman-technique│
    │                                 │  │                                 │
    │ The request is blocked by the   │  │ Your code didn't fail. The      │
    │ browser's same-origin policy…   │  │ browser stopped it…             │
    │                                 │  │                                 │
    │ Apply this patch to server.js?  │  │ Want me to add you to its list? │
    │ ❯ Yes   No                      │  │ ❯ Yes   No                      │
    └────────────────────────────────┘  └────────────────────────────────┘

The question is asked once, above both. Printing it inside each frame spent four rows
saying the inputs matched and still left the reader comparing two strings to be sure.

Both panels end on the same decision. On the left you approve something you cannot
picture; on the right you can actually answer. That contrast is the whole image — it
needs no caption, and there are no arrows.

## Things that must not be "simplified" back

* Wrapping happens here, by character budget per script. Never hand-wrap the JSON: a
  translation that grows three characters would overflow a panel silently. The English
  entry was hand-wrapped once and drifted eight rows shorter than its neighbour, which
  is how the empty half-panel got into the published image.
* Panel height comes from whichever session is longer; the shorter one is padded so the
  frames stay level. Keep the two answers within a few rows of each other in every
  language, or that padding becomes a visible hole.
* The verdict is carried by colour, not by wording: red frame for the session without
  the skill, green for the one with it, and the WITHOUT / WITH is upper-cased so it is
  read before the identifier. This image is met as a thumbnail in a feed, where brighter
  body text alone did not distinguish the two before reading. The orange stays reserved
  for interaction — the chevrons and the selected option — so the two systems never
  compete for the same meaning.
* Arabic and Urdu mirror wholesale — panels swap sides so "without" is still met first in
  reading order, text anchors right, and the Latin-script prompt is forced back to LTR.

## Adding or editing a language

Edit `hero-strings.json` and re-run. **Compose in the target language — do not translate
the English.** The English entry is a content spec, not a source text. An earlier version
was translated nine ways and a native speaker rejected it on sight. See
`skills/feynman-technique/references/other-languages.md`.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
STRINGS_FILE = HERE / "hero-strings.json"

W = 1200
MARGIN = 72
GAP = 30
PANEL_W = (W - 2 * MARGIN - GAP) // 2
PAD = 22
BAR_H = 36

QUOTE = "“There is a difference between the name of the thing and what goes on.”"
BYLINE = "R. P. Feynman, 1966"

MONO = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace'
STACKS = {
    "zh-CN": '"PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Noto Sans SC", sans-serif',
    "hi": '"Noto Sans Devanagari", "Nirmala UI", "Kohinoor Devanagari", Mangal, sans-serif',
    "bn": '"Noto Sans Bengali", "Nirmala UI", "Kohinoor Bangla", Vrinda, sans-serif',
    "ar": '"Noto Sans Arabic", "Geeza Pro", "Segoe UI", Tahoma, sans-serif',
    "ur": '"Noto Nastaliq Urdu", "Noto Sans Arabic", Tahoma, sans-serif',
}

METRICS = {
    "default": dict(size=13, cols=56, lead=23),
    "zh-CN":   dict(size=14, cols=52, lead=25),  # 26 glyphs, 2 columns each
    "hi":      dict(size=13, cols=44, lead=25),
    "bn":      dict(size=12, cols=52, lead=24),
    "ar":      dict(size=14, cols=50, lead=25),
    "ur":      dict(size=13, cols=50, lead=26),
}

CAPTIONS = {
    "en":    ("without feynman-technique", "with feynman-technique"),
    "pt-BR": ("sem feynman-technique",     "com feynman-technique"),
    "es":    ("sin feynman-technique",     "con feynman-technique"),
    "fr":    ("sans feynman-technique",    "avec feynman-technique"),
    "zh-CN": ("未加载 feynman-technique",   "已加载 feynman-technique"),
    "ru":    ("feynman-technique выключен", "feynman-technique включён"),
    "hi":    ("feynman-technique के बिना",   "feynman-technique के साथ"),
    "bn":    ("feynman-technique বন্ধ",     "feynman-technique চালু"),
    "ar":    ("بلا feynman-technique",     "مع feynman-technique"),
    "ur":    ("skill کے بغیر",              "skill کے ساتھ"),
}

INK = dict(
    page="#171614", win="#262624", bar="#1e1d1b", edge="#37352f",
    text="#e9e6df", dim="#9a968d", faint="#5b5850", ask="#e9e6df",
    accent="#d97757", hair="#2a2823",
    # Which panel is which has to survive being a thumbnail in a feed. Red and
    # green carry that at any size, and in either reading direction, without a
    # word of caption being read. The orange stays the interaction colour —
    # chevrons and the selected option — so the two systems never compete.
    bad="#e5484d", good="#4cc38a", bad_bar="#241b1a", good_bar="#1a241e",
)


def width(s: str) -> int:
    """Display width, not codepoints.

    Devanagari, Bengali and Arabic carry vowel signs as separate codepoints that
    occupy no column of their own. Counting codepoints over-measures them by 20%
    and folds lines a native writer deliberately kept whole — which is exactly
    what the composers were told never to do.
    """
    n = 0
    for c in s:
        if unicodedata.category(c) in ("Mn", "Me", "Cf"):
            continue
        n += 2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
    return n


def wrap(text: str, cols: int, cjk: bool) -> list[str]:
    """Break to the panel width. Terminals wrap; so does this."""
    if not text:
        return [""]
    if width(text) <= cols:
        return [text]
    if cjk:
        out, line = [], ""
        for c in text:
            if width(line + c) > cols:
                out.append(line)
                line = c
            else:
                line += c
        if line:
            out.append(line)
        return out
    out, line = [], ""
    for word in text.split(" "):
        candidate = f"{line} {word}".strip()
        if width(candidate) <= cols or not line:
            line = candidate
        else:
            out.append(line)
            line = word
    if line:
        out.append(line)
    return out or [""]


def emphasise(caption: str) -> str:
    """Upper-case the verdict, leave the identifier alone.

    "without feynman-technique" reads as one grey phrase. "WITHOUT
    feynman-technique" puts the verdict first. Scripts without letter case —
    Chinese, Arabic, Devanagari, Bengali — pass through untouched.
    """
    parts = re.split(r"(feynman-technique|skill)", caption)
    return "".join(p if p in ("feynman-technique", "skill") else p.upper()
                   for p in parts)


def build(lang: str, s: dict) -> str:
    rtl = s.get("rtl", False)
    cjk = lang == "zh-CN"
    m = METRICS.get(lang, METRICS["default"])
    stack = STACKS.get(lang, MONO)
    e = html.escape
    cap_off, cap_on = (emphasise(c) for c in CAPTIONS[lang])

    # The question sits in a bar as wide as both panels, so it gets twice the
    # budget. Wrapping it to a panel's width left it broken in half across a
    # bar that was mostly empty.
    prompt = wrap(s["prompt"], m["cols"] * 2 + 5, cjk)
    left = [l for line in s["left"] for l in wrap(line, m["cols"], cjk)]
    right = [l for line in s["right"] for l in wrap(line, m["cols"], cjk)]
    left_ask = wrap(s["left_ask"], m["cols"], cjk)
    right_ask = wrap(s["right_ask"], m["cols"], cjk)

    # both sessions end on the same decision, so the frames must end level
    rows = max(len(left) + len(left_ask), len(right) + len(right_ask))
    panel_h = BAR_H + PAD + rows * m["lead"] + m["lead"] + m["lead"] + PAD
    ask_y = 92
    ask_h = PAD + len(prompt) * m["lead"] + PAD - 6
    top = ask_y + ask_h + 26
    out: list[str] = []

    def t(x, y, size, fill, txt, *, weight=None, anchor="start", mono=False,
          italic=False, spacing=None, force_ltr=False):
        a = [f'x="{x}"', f'y="{y}"', f'font-size="{size}"', f'fill="{fill}"',
             f'text-anchor="{anchor}"', f'class="{"mono" if mono else "body"}"']
        if weight:  a.append(f'font-weight="{weight}"')
        if italic:  a.append('font-style="italic"')
        if spacing: a.append(f'letter-spacing="{spacing}"')
        if rtl and not force_ltr: a.append('direction="rtl"')
        out.append(f'  <text {" ".join(a)}>{e(txt)}</text>')

    # ── masthead ─────────────────────────────────────────────────────────
    t(W - MARGIN if rtl else MARGIN, 46, 19, INK["text"], s["title"],
      weight="700")
    t(MARGIN if rtl else W - MARGIN, 46, 12, INK["faint"], s["eyebrow"],
      spacing=3.2, mono=True, anchor="start" if rtl else "end", force_ltr=True)
    out.append(f'  <line x1="{MARGIN}" y1="70" x2="{W - MARGIN}" y2="70" '
               f'stroke="{INK["hair"]}" stroke-width="1"/>')

    # ── the question, asked once ─────────────────────────────────────────
    # Both sessions answer the same sentence. Printing it twice, once inside
    # each frame, spent four rows saying so and still left the reader to
    # compare the two strings to be sure. One bar above both says it outright.
    out.append(f'  <rect x="{MARGIN}" y="{ask_y}" width="{W - 2 * MARGIN}" '
               f'height="{ask_h}" rx="10" fill="{INK["win"]}" '
               f'stroke="{INK["edge"]}" stroke-width="1"/>')
    py = ask_y + PAD + m["size"]
    for i, line in enumerate(prompt):
        if i == 0:
            t((W - MARGIN - PAD) if rtl else (MARGIN + PAD), py, m["size"] + 2,
              INK["accent"], "›", weight="700", mono=True,
              anchor="end" if rtl else "start", force_ltr=True)
        t((W - MARGIN - PAD - 18) if rtl else (MARGIN + PAD + 18), py, m["size"],
          INK["text"], line)
        py += m["lead"]

    def panel(x, caption, body, ask, lit):
        # The lit panel carries a warm edge and a warmer title bar. At the size
        # this image is actually seen — a thumbnail in a feed — the brighter
        # body text alone was not enough to tell the two apart before reading.
        hue = INK["good" if lit else "bad"]
        stroke = f'stroke="{hue}" stroke-opacity="{0.55 if lit else 0.4}"'
        out.append(f'  <rect x="{x}" y="{top}" width="{PANEL_W}" height="{panel_h}" '
                   f'rx="10" fill="{INK["win"]}" {stroke} stroke-width="1"/>')
        out.append(f'  <path d="M{x} {top + BAR_H} V{top + 10} a10 10 0 0 1 10 -10 '
                   f'H{x + PANEL_W - 10} a10 10 0 0 1 10 10 V{top + BAR_H} Z" '
                   f'fill="{INK["good_bar" if lit else "bad_bar"]}"/>')
        out.append(f'  <line x1="{x}" y1="{top + BAR_H}" x2="{x + PANEL_W}" '
                   f'y2="{top + BAR_H}" stroke="{INK["edge"]}" stroke-width="1"/>')
        for i in range(3):
            out.append(f'  <circle cx="{x + 20 + i * 15}" cy="{top + BAR_H // 2}" '
                       f'r="4" fill="#4a4741"/>')
        # The caption is the one string in an RTL panel that must NOT be forced
        # LTR: with force_ltr the particle renders left of the Latin identifier,
        # so an Arabic reader meets "feynman-technique" first and the "without"
        # second. In RTL, text-anchor="start" is the right edge, which is where
        # the caption belongs.
        t(x + PANEL_W - 16, top + BAR_H // 2 + 4, 12, hue, caption,
          weight="700",
          anchor="start" if rtl else "end", mono=not rtl)

        tx = x + PAD
        rx_ = x + PANEL_W - PAD
        anchor = "start"          # see the note on the masthead
        glyph = "end" if rtl else "start"
        y = top + BAR_H + PAD + m["size"] + 4

        # the assistant answering
        for line in body:
            if line:
                t(rx_ if rtl else tx, y, m["size"],
                  INK["text"] if lit else INK["dim"], line, anchor=anchor)
            y += m["lead"]

        # pad so both frames end level
        y += (rows - len(body) - len(ask)) * m["lead"] + m["lead"]

        for line in ask:
            t(rx_ if rtl else tx, y, m["size"], INK["ask"], line,
              weight="600", anchor=anchor)
            y += m["lead"]

        # the decision
        y += 4
        t(rx_ if rtl else tx, y, m["size"], INK["accent"], "❯", anchor=glyph,
          mono=True, force_ltr=True)
        off = 20 + len(s["yes"]) * 9 + 16
        t((rx_ - 20) if rtl else (tx + 20), y, m["size"], INK["text"], s["yes"],
          weight="600", anchor=anchor)
        t((rx_ - off) if rtl else (tx + off), y, m["size"], INK["faint"], s["no"],
          anchor=anchor)

    lx, rx = MARGIN, MARGIN + PANEL_W + GAP
    if rtl:
        panel(rx, cap_off, left, left_ask, False)
        panel(lx, cap_on, right, right_ask, True)
    else:
        panel(lx, cap_off, left, left_ask, False)
        panel(rx, cap_on, right, right_ask, True)

    fy = top + panel_h + 44
    t(MARGIN, fy, 13, INK["faint"], QUOTE, italic=True, force_ltr=True)
    t(W - MARGIN, fy, 13, INK["faint"], BYLINE, anchor="end", force_ltr=True)
    H = fy + 26

    alt = (f'feynman-technique — {cap_off}: {" ".join(s["left"])} {s["left_ask"]} — '
           f'{cap_on}: {" ".join(s["right"])} {s["right_ask"]}')

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{e(alt)}">
  <defs>
    <style>
      .body {{ font-family: {stack}; }}
      .mono {{ font-family: {MONO}; }}
    </style>
  </defs>
  <rect width="{W}" height="{H}" fill="{INK["page"]}"/>
{chr(10).join(out)}
</svg>
'''


if __name__ == "__main__":
    strings = json.loads(STRINGS_FILE.read_text(encoding="utf-8"))
    for lang, s in strings.items():
        if lang.startswith("_"):
            continue
        if "prompt" not in s:
            print(f"  skip assets/hero.{lang}.svg — awaiting composition")
            continue
        name = "hero.svg" if lang == "en" else f"hero.{lang}.svg"
        (HERE / name).write_text(build(lang, s), encoding="utf-8")
        print(f"  wrote assets/{name}")
