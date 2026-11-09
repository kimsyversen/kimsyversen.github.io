"""Check both views of MCP-Risk-Map.html.

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
  6. Framework mapping (FW): every OWASP and CoSAI entry name appears in its source, every
     entry has one home risk that has a card, and each card is the home of at least one entry.
     CoSAI quotes are matched on the PDF page they cite (needs pdftotext).

A pass proves the quotes are on the pages the sources serve today and that a verdict was
recorded for the exact wording. It does not prove a verdict or a claim is right, and it
does not prove any setting works on a managed machine. Nothing was run on one.
"""

import html
import json
import re
import subprocess
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


def fetch_pdf(url, cache):
    """Return the PDF text, one normalised string per page (index 0 is page 1)."""
    path = cache / (re.sub(r"[^a-z0-9]+", "-", url.lower()).strip("-")[-120:] + ".pdf")
    if not path.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        path.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    out = subprocess.run(["/opt/homebrew/bin/pdftotext", str(path), "-"],
                         capture_output=True, text=True, check=True).stdout
    pages = out.split("\f")
    if pages and not pages[-1].strip():
        pages.pop()
    return [norm(p) for p in pages]


def load_fw(markup):
    m = re.search(r"^  var FW = (.*);$", markup, re.M)
    if not m:
        raise SystemExit("FAIL: FW line not found in the page")
    return json.loads(m.group(1))


def quote_ids(data, general_places=()):
    """Return every list of quote ids with a description of where it sits."""
    out = [(f"general place[{i}] {p[0]}/{p[1]}", p[2], p[3] if len(p) > 3 else [])
           for i, p in enumerate(general_places)]
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
    general_places = json.loads(re.search(r"^  var PLACE = (.*);$", markup, re.M)[1])
    texts, _ = presentation_texts(markup, data)
    if "--list" in flags:
        for t in dict.fromkeys(texts):
            print(t)
        return 0
    problems = []
    # Distinct evidence namespaces prevent valid but unrelated quotes from passing.
    for qid, q in data['MSQ'].items():
        if re.fullmatch(r'cs\d+', qid) and q['s'] != 'cosai':
            problems.append(f'{qid}: CoSAI quote uses another source')
        if qid.startswith('studio') and q['s'] not in {'csadd', 'csdlp'}:
            problems.append(f'{qid}: Copilot Studio quote uses another source')
    for where, text, qs in quote_ids(data):
        if 'Copilot Studio' in text and any(re.fullmatch(r'cs\d+', q) for q in qs):
            problems.append(f'{where}: Copilot Studio claim cites CoSAI evidence')

    # 1. quotes against sources
    srcs = {s["k"]: s for s in data["MSS"]}
    if "--offline" not in flags:
        if len(args) != 1:
            print(__doc__)
            return 2
        cache = Path(args[0])
        cache.mkdir(parents=True, exist_ok=True)
        pages = {}
        pdf_pages = {}
        for qid, q in data["MSQ"].items():
            s = srcs[q["s"]]
            url = s.get("f") or s["u"]
            if s.get("pdf"):
                try:
                    pdf_pages.setdefault(url, fetch_pdf(url, cache))
                except Exception as exc:
                    problems.append(f"{qid}: cannot read PDF {url}: {exc}")
                    continue
                pg = pdf_pages[url]
                n = q.get("pg", 0)
                if not 1 <= n <= len(pg):
                    problems.append(f"{qid}: page {n} not in PDF ({len(pg)} pages)")
                elif norm(q["q"]) in pg[n - 1]:
                    pass
                elif squash(q["q"]) in squash(pg[n - 1]):
                    print(f"note {qid}: matches only when whitespace is ignored")
                else:
                    problems.append(f"{qid}: quote not found on page {n} of {url}")
                continue
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

    # 6. framework mapping
    fw = load_fw(markup)
    cards = set(re.findall(r'<article id="risk-m\d+" class="risk" data-id="(M\d+)"', markup))
    homes = Counter()
    for key in ("o", "c"):
        ids = [e[0] for e in fw[key]]
        if len(ids) != len(set(ids)):
            problems.append(f"FW {key}: duplicate entry id")
        expected = ({f'MCP{i:02}' for i in range(1, 11)} if key == 'o'
                    else {str(i) for i in range(1, 35)})
        if set(ids) != expected:
            problems.append(f'FW {key}: missing or unexpected entry IDs')
        if key == 'o' and len({e[2] for e in fw[key]}) != 10:
            problems.append('OWASP entries must have ten distinct homes')
        for eid, name, home, also in fw[key]:
            homes[home] += 1
            for r in [home] + also:
                if r not in cards:
                    problems.append(f"FW {key} {eid}: risk {r} has no card")
            if home in also:
                problems.append(f"FW {key} {eid}: home risk repeated under also")
    for r in sorted(cards - set(homes)):
        problems.append(f"card {r} is not the home of any framework entry")
    for article in re.findall(r'<article\b.*?</article>', markup, re.S):
        rid = re.search(r'data-id="(M\d+)"', article)
        label = re.search(r'<p class="en">(.*?)</p>', article)
        if not rid or not label:
            continue
        expected = {e[0] for e in fw['o'] if e[2] == rid[1]}
        if set(re.findall(r'MCP\d+', label[1])) != expected:
            problems.append(f'{rid[1]}: card OWASP label differs from home mapping')
        expected = {e[0] for e in fw['c'] if e[2] == rid[1]}
        if set(re.findall(r'#(\d+)', label[1])) != expected:
            problems.append(f'{rid[1]}: card CoSAI label differs from home mapping')
    if len(fw["o"]) != 10:
        problems.append(f"FW o: {len(fw['o'])} OWASP entries, expected 10")
    if "--offline" not in flags:
        own = srcs["owasp"]
        try:
            otext = fetch(own.get("f") or own["u"], cache)
            for eid, name, _, _ in fw["o"]:
                if squash(eid + " " + name) not in squash(otext) and squash(name) not in squash(otext):
                    problems.append(f"FW OWASP {eid}: name not found on the OWASP page: {name}")
        except Exception as exc:
            problems.append(f"cannot fetch OWASP page: {exc}")
        cs = srcs["cosai"]
        ctext = squash(" ".join(pdf_pages.get(cs["u"]) or fetch_pdf(cs["u"], cache)))
        for eid, name, _, _ in fw["c"]:
            if squash(name) not in ctext:
                problems.append(f"FW CoSAI #{eid}: name not found in the PDF: {name}")
        if len(fw["c"]) != 34:
            problems.append(f"FW c: {len(fw['c'])} CoSAI entries, expected 34")

    # 2. ids used and defined
    used = Counter()
    for where, text, qs in quote_ids(data, general_places):
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
    for where, text, qs in quote_ids(data, general_places):
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
