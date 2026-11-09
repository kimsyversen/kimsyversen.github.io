"""Make every section of a page linkable.

Rule (see AGENTS.md): every <section>, <article> that holds a heading, and every
<h2> and <h3> has a stable id, and every h2/h3 is a link to that id so a reader
can copy the address of that part of the page.

Usage:
  python3 -I scripts/section_anchors.py            add missing ids and links to all pages
  python3 -I scripts/section_anchors.py --check    change nothing, exit 1 if anything is missing
  python3 -I scripts/section_anchors.py page.html  limit to the given pages

Builders import add_anchors() and run it on the page text before writing it.

The function is idempotent and never changes an id that exists. Existing ids are
public anchors. New ids come from the heading text. Tab ids on tabbed pages are
reserved, because the page script reads them from the address.
"""

import html as htmllib
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARK = "/* section links */"

CSS = (
    MARK + "\n"
    "h2 a.sec-link,h3 a.sec-link{color:inherit;text-decoration:none;font:inherit;letter-spacing:inherit;text-transform:inherit}\n"
    "h2 a.sec-link::after,h3 a.sec-link::after{content:\"#\";margin-left:.45em;font-weight:400;opacity:0;transition:opacity .12s}\n"
    "h2:hover a.sec-link::after,h3:hover a.sec-link::after,a.sec-link:focus-visible::after{opacity:.5}\n"
    "a.sec-link:focus-visible{outline:2px solid currentColor;outline-offset:3px;border-radius:2px}\n"
    "@media (hover:none){h2 a.sec-link::after,h3 a.sec-link::after{opacity:.35}}\n"
    "@media print{h2 a.sec-link::after,h3 a.sec-link::after{display:none}}\n"
)
CSS_OFFSET = ":is(section,article,h2,h3)[id]{scroll-margin-top:64px}\n"

TOKEN = re.compile(
    r"<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->"
    r"|<(?P<open>section|article)\b(?P<oattrs>[^>]*)>"
    r"|</(?P<close>section|article)\s*>"
    r"|<(?P<h>h[23])\b(?P<hattrs>[^>]*)>(?P<inner>.*?)</(?P=h)\s*>",
    re.S | re.I,
)
ID_ATTR = re.compile(r"""\sid\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s>"']+))""", re.I)
DATA_ID = re.compile(r"""\sdata-id\s*=\s*"([^"]*)"|\sdata-id\s*=\s*'([^']*)'""", re.I)


def _get_id(attrs):
    m = ID_ATTR.search(attrs)
    return next((g for g in m.groups() if g), None) if m else None


def _slug(text):
    text = unicodedata.normalize("NFKD", htmllib.unescape(text))
    text = text.encode("ascii", "ignore").decode().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    if len(text) > 48:
        text = text[:48].rsplit("-", 1)[0] or text[:48]
    return text or "section"


def _plain(inner):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", inner)).strip()


def _reserved(src):
    r = {"more"}
    r.update(re.findall(r"""data-tab\s*=\s*["']([^"']+)["']""", src))
    return r


def add_anchors(src):
    """Return src with ids and heading links added. Raises ValueError if a
    section has no heading and no id (it cannot be named automatically)."""
    taken = set(re.findall(r"""\sid\s*=\s*"([^"]*)\"""", src))
    taken.update(re.findall(r"""\sid\s*=\s*'([^']*)'""", src))
    taken |= _reserved(src)

    def fresh(base):
        i, cand = 2, base
        while cand in taken:
            cand = f"{base}-{i}"
            i += 1
        taken.add(cand)
        return cand

    edits = []  # (start, end, replacement)
    stack = []  # open containers: dicts
    problems = []

    def finish(c):
        if not c["claimed"] and not c["id"]:
            problems.append(f"<{c['tag']}> at char {c['start']} has no heading and no id")

    for m in TOKEN.finditer(src):
        if m.group("open"):
            attrs = m.group("oattrs")
            c = {"tag": m.group("open").lower(), "start": m.start(), "tagend": m.start() + 1 + len(m.group("open")),
                 "id": _get_id(attrs), "claimed": False, "attrs": attrs}
            stack.append(c)
        elif m.group("close"):
            tag = m.group("close").lower()
            for i in range(len(stack) - 1, -1, -1):
                if stack[i]["tag"] == tag:
                    finish(stack.pop(i))
                    break
        elif m.group("h"):
            tag, hattrs, inner = m.group("h"), m.group("hattrs"), m.group("inner")
            hid = _get_id(hattrs)
            c = stack[-1] if stack else None
            new_hattrs = hattrs
            if c is not None and not c["claimed"]:
                c["claimed"] = True
                if c["id"]:
                    target = c["id"]
                elif hid:
                    target = hid
                else:
                    pref = None
                    d = DATA_ID.search(c["attrs"])
                    if d and "risk" in c["attrs"]:
                        pref = "risk-" + _slug(next(g for g in d.groups() if g))
                    target = fresh(pref or _slug(_plain(inner)))
                    c["id"] = target
                    edits.append((c["tagend"], c["tagend"], f' id="{target}"'))
            else:
                if "<a " in inner.lower():
                    continue  # a heading that is itself a link to another page
                if hid:
                    target = hid
                else:
                    target = fresh(_slug(_plain(inner)))
                    new_hattrs = hattrs + f' id="{target}"'
            new_inner = inner
            if "<a " not in inner.lower() and "<a>" not in inner.lower():
                new_inner = f'<a class="sec-link" href="#{target}">{inner}</a>'
            if new_hattrs != hattrs or new_inner != inner:
                edits.append((m.start(), m.end(), f"<{tag}{new_hattrs}>{new_inner}</{tag}>"))
    for c in stack:
        finish(c)
    if problems:
        raise ValueError("; ".join(problems))

    out, pos = [], 0
    for s, e, r in sorted(edits, key=lambda x: (x[0], x[1])):
        out.append(src[pos:s])
        out.append(r)
        pos = e
    out.append(src[pos:])
    res = "".join(out)

    if MARK not in res and "sec-link" in res and "</style>" in res:
        add = CSS
        if re.search(r"\.tabs\{[^}]*position:sticky", res):
            add += CSS_OFFSET
        i = res.index("</style>")
        res = res[:i] + add + res[i:]
    return res


def pages():
    skip = {"node_modules", ".git"}
    return sorted(p for p in ROOT.rglob("*.html") if not skip & set(p.relative_to(ROOT).parts))


def main(argv):
    check = "--check" in argv
    files = [Path(a) for a in argv if not a.startswith("--")] or pages()
    bad = 0
    for p in files:
        src = p.read_text(encoding="utf-8")
        try:
            new = add_anchors(src)
        except ValueError as e:
            print(f"{p}: {e}")
            bad += 1
            continue
        if new != src:
            if check:
                print(f"{p}: sections missing an id or link")
                bad += 1
            else:
                p.write_text(new, encoding="utf-8")
                print(f"{p}: updated")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
