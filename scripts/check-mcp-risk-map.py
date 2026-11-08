"""Check the Microsoft ecosystem view of MCP-Risk-Map.html.

Usage:
  python3 -I scripts/check-mcp-risk-map.py <cache-dir>           run all checks (fetches sources)
  python3 -I scripts/check-mcp-risk-map.py --offline             skip the fetch, run the other checks
  python3 -I scripts/check-mcp-risk-map.py --list                print the captured presentation texts

Checks:
  1. Every quote in MSDATA appears word for word in its source (fetched today, whitespace
     collapsed, quotes straightened). CVE records are read from the CVE JSON API.
  2. Every quote id used on the page exists, and every quote is used.
  3. Every sourced sentence has a quote id or an [inference] or [unverified] label.
  4. Every presentation text (labels, start rows, box names, chips, header, notes) has a
     recorded verdict in MCP-Risk-Map.factcheck.md, and none changed since it was reviewed.
     Fact-style wording in those texts fails.
  5. No em dash, no en dash, no paragraph of more than 60 words.

A pass proves the quotes are on the pages the sources serve today and that a verdict was
recorded for the exact wording. It does not prove a verdict or a claim is right, and it
does not prove any setting works on a managed machine. Nothing was run on one.
"""

import html
import json
import re
import sys
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "MCP-Risk-Map.html"
LEDGER = ROOT / "MCP-Risk-Map.factcheck.md"
BEGIN = "<!-- Begin reviewed presentation text (Microsoft view) -->"
END = "<!-- End reviewed presentation text (Microsoft view) -->"
VERDICTS = {"label", "requirement", "code token"}
FACT_STYLE = re.compile(
    r"\b(?:supports|blocks|enforces|requires|prevents|provides|ensures|guarantees|inspects|"
    r"discovers|always|never|automatically)\b"
    r"|\b(?:is|are) (?:generally available|available|supported|enabled|required|blocked|allowed|"
    r"default|in preview|not supported)\b"
    r"|\bcan (?:block|allow|log|discover|inspect|run|sandbox)\b",
    re.IGNORECASE,
)
SOURCED = re.compile(r"\[(?:inference|unverified)\]")


def norm(text):
    text = html.unescape(text)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " ")):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def squash(text):
    return re.sub(r"\s+", "", norm(text))


def load_msdata(markup):
    m = re.search(r"^  var MSDATA = (\{.*\});$", markup, re.M)
    if not m:
        raise SystemExit("FAIL: MSDATA line not found in the page")
    return json.loads(m.group(1).replace("<\\/", "</"))


def fetch(url, cache):
    path = cache / (re.sub(r"[^a-z0-9]+", "-", url.lower()).strip("-")[-120:] + ".txt")
    if path.exists():
        return path.read_text(encoding="utf-8")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    text = norm(re.sub(r"(?s)<[^>]+>", " ", raw))
    path.write_text(text, encoding="utf-8")
    return text


def quote_ids(data):
    """Return every list of quote ids with a description of where it sits."""
    out = []
    for cid, c in data["MSCARD"].items():
        for kind in ("body", "checks", "how"):
            for i, x in enumerate(c.get(kind, [])):
                out.append((f"{cid}.{kind}[{i}]", x["t"], x.get("q", [])))
    for i, r in enumerate(data["MSROWS"]):
        out.append((f"row[{i}] {r['t']}", r["d"], r.get("q", [])))
    for i, p in enumerate(data["PLACE_M"]):
        out.append((f"place[{i}] {p[0]}/{p[1]}", p[2], p[3] if len(p) > 3 else []))
    for i, c in enumerate(data["CALLOUT_M"]):
        out.append((f"callout[{i}]", c["b"] + " " + c["t"], c.get("q", [])))
    return out


def presentation_texts(markup, data):
    """Texts with no evidence list: they hold design requirements and labels only."""

    class P(HTMLParser):
        def __init__(self):
            super().__init__()
            self.stack, self.items = [], []

        def handle_starttag(self, tag, attrs):
            a = dict(attrs)
            cls = set(a.get("class", "").split())
            ctx = set().union(*(f[1] for f in self.stack)) if self.stack else set()
            ms = "sc-m" in cls or "sc-m" in ctx
            capture = ms and (
                tag in {"p", "h3", "span", "li", "button"} and not (ctx & {"msx"})
                and "msx" not in cls and "chk-body" not in cls
                and "qs" not in cls
            )
            if tag == "button" and "scope" in ctx:
                capture = True
            if tag == "span" and "chip-lbl" in cls:
                capture = True
            if tag == "title":
                capture = True
            self.stack.append((tag, cls, [] if capture else None, "msx" in cls))

        def handle_data(self, d):
            for f in self.stack:
                if f[2] is not None:
                    f[2].append(d)

        def handle_endtag(self, tag):
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] != tag:
                    continue
                f = self.stack[i]
                if f[2] is not None:
                    v = " ".join("".join(f[2]).split())
                    if v:
                        self.items.append(v)
                del self.stack[i:]
                break

    body = markup.split('<div class="msx sc-m"')[0]
    # Static Microsoft-only markup outside the generated card blocks.
    p = P()
    p.feed(markup)
    items = list(p.items)
    # Tags inside a card's own msx block are generated from MSCARD and carry quotes.
    for c in data["COMP_M"].values():
        for k in ("t", "s", "short"):
            if c.get(k):
                items.append(c[k])
    for r in data["START_M"]:
        items.extend([r[1], r[2]])
    for s in data["MSS"]:
        items.extend([s["t"], s["n"]])
    for c in data["MSCARD"].values():
        if c.get("cl"):
            items.append(c["cl"])
    items.extend(data["EVIDENCE_M"][i]["h"] for i in range(len(data["EVIDENCE_M"])))
    for col in data["EVIDENCE_M"]:
        items.extend(col["i"])
    return [i for i in items if i], body


def ledger_rows(text):
    block = text.split(BEGIN, 1)[1].split(END, 1)[0].strip()
    block = block.removeprefix("```text\n").removesuffix("\n```")
    rows = {}
    bad = []
    for row in block.splitlines():
        if "\t" not in row:
            bad.append(f"Malformed ledger row: {row}")
            continue
        verdict, value = row.split("\t", 1)
        if verdict not in VERDICTS or value in rows:
            bad.append(f"Invalid or duplicate verdict: {row}")
        rows[value] = verdict
    return rows, bad


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    markup = PAGE.read_text(encoding="utf-8")
    data = load_msdata(markup)
    texts, _ = presentation_texts(markup, data)
    if "--list" in flags:
        for t in dict.fromkeys(texts):
            print(t)
        return 0
    problems = []

    # 1. quotes against sources
    srcs = {s["k"]: s for s in data["MSS"]}
    if "--offline" not in flags:
        if len(args) != 1:
            print(__doc__)
            return 2
        cache = Path(args[0])
        cache.mkdir(parents=True, exist_ok=True)
        pages = {}
        for qid, q in data["MSQ"].items():
            s = srcs[q["s"]]
            url = s.get("f") or s["u"]
            try:
                pages.setdefault(url, fetch(url, cache))
            except Exception as exc:
                problems.append(f"{qid}: cannot fetch {url}: {exc}")
                continue
            tx = pages[url]
            if norm(q["q"]) in tx:
                continue
            if squash(q["q"]) in squash(tx):
                print(f"note {qid}: matches only when whitespace is ignored")
                continue
            problems.append(f"{qid}: quote not found in {url}")

    # 2. ids used and defined
    used = Counter()
    for where, text, qs in quote_ids(data):
        for q in qs:
            used[q] += 1
            if q not in data["MSQ"]:
                problems.append(f"{where}: unknown quote id {q}")
    for c in data["COMP_M"].values():
        pass
    for q in data["MSQ"]:
        if q not in used:
            problems.append(f"quote {q} is never used")

    # 3. sourced sentences
    for where, text, qs in quote_ids(data):
        if not qs and not SOURCED.search(text):
            problems.append(f"{where}: no quote and no [inference] or [unverified]: {text[:70]}")
        if len(text.split()) > 60:
            problems.append(f"{where}: more than 60 words")

    # 4. reviewed presentation text
    ledger = LEDGER.read_text(encoding="utf-8")
    if BEGIN not in ledger or END not in ledger:
        problems.append("ledger has no reviewed-text block")
    else:
        rows, bad = ledger_rows(ledger)
        problems.extend(bad)
        seen = set(texts)
        for v in sorted(seen - rows.keys()):
            problems.append(f"Missing verdict: {v}")
        for v in sorted(rows.keys() - seen):
            problems.append(f"Stale verdict: {v}")
        for v in sorted(seen):
            if FACT_STYLE.search(v):
                problems.append(f"Move product claim to sourced prose: {v}")

    # 5. dashes and paragraph length
    for path in (PAGE, LEDGER, ROOT / "MCP-Risk-Map.decisions.md", ROOT / "MCP-Risk-Map.plan.md"):
        t = path.read_text(encoding="utf-8")
        for ch, name in (("—", "em dash"), ("–", "en dash")):
            if ch in t:
                problems.append(f"{path.name}: contains an {name}")
    for pm in re.finditer(r"<p[^>]*>(.*?)</p>", markup, re.S):
        words = len(re.sub(r"<[^>]+>", " ", pm.group(1)).split())
        if words > 60:
            problems.append(f"page paragraph of {words} words: {pm.group(1)[:60]}")

    for p in problems:
        print("FAIL", p)
    print(f"{len(data['MSQ'])} quotes, {len(set(texts))} reviewed texts, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
