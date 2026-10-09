import re, sys, pathlib

def unwrap(lines):
    out, buf, quoted, fence = [], [], False, False
    def flush():
        nonlocal buf, quoted
        if buf:
            t = " ".join(x.strip() for x in buf)
            out.append(("> " + t) if quoted else t)
        buf, quoted = [], False
    for ln in lines:
        s = ln.rstrip()
        if fence:
            out.append(ln)
            if s.startswith("```") or s.startswith("~~~"): fence = False
            continue
        if s.startswith("```") or s.startswith("~~~"):
            flush(); out.append(ln); fence = True; continue
        if not s.strip():                       flush(); out.append(""); continue
        if s.startswith("|"):                   flush(); out.append(ln); continue
        if re.match(r"^#{1,6}\s", s):           flush(); out.append(ln); continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s.strip()): flush(); out.append(ln); continue
        if s.lstrip().startswith("<!--"):       flush(); out.append(ln); continue
        if re.match(r"^\s*([-*+]|\d+\.)\s", s): flush(); buf = [s]; continue
        if s.startswith("> "):
            if not quoted: flush(); quoted = True
            buf.append(s[2:]); continue
        if quoted: flush()
        buf.append(s)
    flush()
    return out

REGIONS = {
    "devto.md":    [(35, None)],
    "reddit.md":   [(24, 80)],
    "show-hn.md":  [(33, 88)],
    "x-thread.md": [(14, 113)],
    "threads.md":  [(55, 80), (105, 135)],
}
for fname, regions in REGIONS.items():
    p = pathlib.Path("docs/launch") / fname
    lines = p.read_text().split("\n")
    for start, end in sorted(regions, reverse=True):
        a = start - 1
        b = len(lines) if end is None else end
        lines[a:b] = unwrap(lines[a:b])
    p.write_text("\n".join(lines))
    print(f"{fname}: ok")
