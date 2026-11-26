"""Check mcp-intake.html and its content.

Usage:
  python3 -I scripts/check-mcp-intake.py <cache-dir>   all checks, fetching sources into the folder
  python3 -I scripts/check-mcp-intake.py --offline     all checks except the source quotes

Checks:
  1. Every quote appears word for word in its source (PDF quotes on the page they cite).
  2. Every id used exists, every quote is used, every OWASP MCP Top 10 item is mapped.
  3. Every sourced statement has a quote or a tag.
  4. The page equals the builder output, has no em or en dash, and its links to this site resolve.
  5. Every statement on the page has a verdict in mcp-intake.factcheck.md for its exact wording.

A pass proves that the quotes are on the pages served on the day of the run and that a verdict
was recorded for each wording. It does not prove a verdict is right.
"""

import html
import importlib.util
import json
import re
import subprocess
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mcp_intake_data as D  # noqa: E402
from section_anchors import add_anchors  # noqa: E402

spec = importlib.util.spec_from_file_location("builder", ROOT / "scripts" / "build-mcp-intake.py")
B = importlib.util.module_from_spec(spec)
spec.loader.exec_module(B)

DASHES = ("\u2013", "\u2014")


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "nav", "svg", "noscript"):
            self.skip += 1
        if tag in ("p", "li", "tr", "div", "h1", "h2", "h3", "h4", "pre", "br", "table", "td", "th"):
            self.out.append(" ")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "svg", "noscript") and self.skip:
            self.skip -= 1
        if tag in ("p", "li", "h1", "h2", "h3", "h4"):
            self.out.append(" ")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def norm(text):
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = re.sub(r"\[([^\]\n]*)\]\((?:[^()\n]|\([^()\n]*\))*\)", r"\1", text)
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\\([*_#\[\]()])", r"\1", text)
    text = html.unescape(text)
    for a, b in (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u00a0", " ")):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def fetch(key, url, cache):
    """Return the source as a list of normalised pages (one item unless it is a PDF)."""
    path = cache / f"{key}.raw"
    kind = cache / f"{key}.type"
    if not path.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; quote-check)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            path.write_bytes(r.read())
            kind.write_text(r.headers.get("content-type", ""))
    ctype = kind.read_text()
    if url.endswith(".pdf") or "pdf" in ctype:
        out = subprocess.run(["pdftotext", str(path), "-"], capture_output=True, text=True, check=True).stdout
        return [norm(p) for p in out.split("\f")]
    raw = path.read_bytes().decode("utf-8", "replace")
    if "services.nvd.nist.gov" in url:
        cve = json.loads(raw)["vulnerabilities"][0]["cve"]
        return [norm(" ".join(d["value"] for d in cve["descriptions"] if d["lang"] == "en"))]
    if "html" in ctype:
        parser = Text()
        parser.feed(raw)
        raw = "".join(parser.out)
    return [norm(raw)]


def check_quotes(cache):
    errors, texts = [], {}
    for qid, entry in D.Q.items():
        key, quote = entry[0], entry[1]
        if key not in texts:
            try:
                texts[key] = fetch(key, D.SOURCES[key][2], cache)
            except Exception as exc:  # a source that cannot be read is a failure
                texts[key] = []
                errors.append(f"source {key}: cannot fetch ({exc})")
        found = [i + 1 for i, page in enumerate(texts[key]) if norm(quote) in page]
        if not found:
            errors.append(f"quote {qid}: not found in {key}: {quote[:70]}")
        elif len(texts[key]) > 1 and (len(entry) < 3 or entry[2] not in found):
            errors.append(f"quote {qid}: is on page {found}, data says {entry[2] if len(entry) > 2 else 'nothing'}")
    return errors


def all_facts():
    for s in D.STAGES:
        yield from ((f"stage {s['key']}", f) for f in s["facts"])
    for c in D.CHECKS:
        if c["note"]:
            yield f"check {c['id']}", c["note"]
    for t in D.TRIGGERS:
        yield from ((f"trigger {t['id']}", f) for f in t["facts"])
    for s in D.SCENARIOS:
        yield from ((f"case {s['id']}", f) for f in s["facts"])
    for e in D.ENFORCE:
        yield from ((f"enforce {e['name']}", f) for f in e["facts"])
    yield "enforce gap", D.ENFORCE_GAP


def check_data():
    errors, used = [], set()
    stages = {s["key"] for s in D.STAGES}
    ids = [c["id"] for c in D.CHECKS]
    errors += [f"check id {i} is used twice" for i in set(ids) if ids.count(i) > 1]

    def need(where, check_ids):
        errors.extend(f"{where}: unknown check {i}" for i in check_ids if i not in ids)

    for c in D.CHECKS:
        used.update(c["why"])
        if c["stage"] not in stages:
            errors.append(f"check {c['id']}: unknown stage")
    for where, f in all_facts():
        used.update(f["q"])
        if not f["q"] and not f["tag"] and not f["text"].startswith("Get "):
            errors.append(f"{where}: statement has no quote and no tag: {f['text'][:60]}")
    need("minimum", D.MINIMUM)
    for t in D.TRIGGERS:
        need(f"trigger {t['id']}", t["checks"])
        errors += [f"trigger {t['id']}: unknown stage {s}" for s in t["rerun"] if s not in stages]
    for _, check_ids in D.FORCE_REVIEW:
        need("force review", check_ids)
    for s in D.SCENARIOS:
        for step in s["steps"]:
            need(f"case {s['id']}", step["checks"])
            if step["stage"] not in stages or step["result"] not in D.RESULTS:
                errors.append(f"case {s['id']}: bad step {step['stage']}")
    mapped, covered = set(), set()
    for _, classes in D.COVERAGE:
        for v in classes:
            need(f"coverage {v['name']}", v["checks"])
            used.update(v["q"])
            mapped.update(v["owasp"])
            covered.update(v["checks"])
            if not v["q"] and not v["tag"]:
                errors.append(f"coverage {v['name']}: gap has no quote and no tag")
    errors += [f"OWASP {c} is not mapped" for c in D.OWASP if c not in mapped]
    for _, _, quote_ids in D.SCANNERS:
        used.update(quote_ids)
    errors += [f"unknown quote id {q}" for q in sorted(used - set(D.Q))]
    errors += [f"quote {q} is not used" for q in sorted(set(D.Q) - used)]
    errors += [f"quote {q}: unknown source" for q, e in D.Q.items() if e[0] not in D.SOURCES]
    return errors


def check_page():
    errors = []
    page = ROOT / "mcp-intake.html"
    text = page.read_text(encoding="utf-8")
    built, statements = B.build()
    if add_anchors(built) != text:
        errors.append("mcp-intake.html differs from the builder output: run the builder")
    ids = re.findall(r'\sid="([^"]+)"', text)
    errors += [f"id {i} is used twice" for i in sorted({i for i in ids if ids.count(i) > 1})]
    for href in re.findall(r'href="([^"]+)"', text):
        if href.startswith("#"):
            if href[1:] not in ids:
                errors.append(f"link {href}: no such id")
        elif not href.startswith("http"):
            name, _, anchor = href.partition("#")
            target = ROOT / name
            if not target.exists():
                errors.append(f"link {href}: no such file")
            elif anchor and f'id="{anchor}"' not in target.read_text(encoding="utf-8"):
                errors.append(f"link {href}: no such anchor")
    files = [page, ROOT / "scripts" / "mcp_intake_data.py", ROOT / "scripts" / "build-mcp-intake.py"]
    files += sorted(ROOT.glob("mcp-intake.*.md"))
    for f in files:
        if any(d in f.read_text(encoding="utf-8") for d in DASHES):
            errors.append(f"{f.name}: has an em or en dash")
    return errors, statements


def check_ledger(statements):
    ledger = B.read_ledger()
    errors = [f"no verdict for: [{b}] {t[:70]}" for b, t in statements if not ledger.get((b, t))]
    errors += [f"ledger row no longer on the page: {t[:70]}" for b, t in ledger if (b, t) not in statements]
    errors += [f"verdict is not OK: {t[:70]}" for (b, t), v in ledger.items() if v and not v.startswith("OK")]
    return errors


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    errors = check_data()
    if argv[0] != "--offline":
        cache = Path(argv[0])
        cache.mkdir(parents=True, exist_ok=True)
        errors += check_quotes(cache)
    page_errors, statements = check_page()
    errors += page_errors + check_ledger(statements)
    for e in errors:
        print("FAIL:", e)
    print(f"{len(D.Q)} quotes{' (not fetched)' if argv[0] == '--offline' else ''}, {len(D.CHECKS)} checks, "
          f"{len(statements)} statements, {len(errors)} failures")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
