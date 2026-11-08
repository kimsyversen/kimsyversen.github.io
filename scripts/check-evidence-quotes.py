"""Confirm every evidence quote on a governance page appears word for word in its source.

Usage: python3 -I scripts/check-evidence-quotes.py <cache-dir> [evidence-module page.html]

Default: governance_evidence and the governance summary page. Pass a module name
and a page under wip/ to check another page, for example
  mcp_governance_evidence mcp-governance-microsoft.html

Fetches each source URL once into <cache-dir> (text, quotes straightened, whitespace
collapsed), then looks for each quote. Also checks that the built page lists every quote.
Exit code 1 if any quote is missing. A pass shows the words are on the page the
source URL serves today. It does not show the claim built on the quote is right.
"""

import html
import importlib
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

ROOT = Path(__file__).resolve().parents[1]
MODULE = sys.argv[2] if len(sys.argv) > 2 else "governance_evidence"
_ev = importlib.import_module(MODULE)
IDS, QUOTES, SOURCES = _ev.IDS, _ev.QUOTES, _ev.SOURCES
_name = sys.argv[3] if len(sys.argv) > 3 else "enterprise-ai-agent-governance-summary.html"
PAGE = ROOT / _name if (ROOT / _name).exists() else ROOT / "wip" / _name


def norm(text):
    text = html.unescape(text)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " ")):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def fetch(url, cache):
    path = cache / (re.sub(r"[^a-z0-9]+", "-", url.lower()).strip("-")[-120:] + ".txt")
    if path.exists():
        return path.read_text(encoding="utf-8")
    agent = "curl/8.7.1" if "releasecommunications" in url else "Mozilla/5.0"  # the feed refuses a browser name
    req = urllib.request.Request(url, headers={"User-Agent": agent})
    raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    if raw.lstrip().startswith("{"):  # JSON feed: keep the HTML in each description
        import json
        raw = " ".join(i.get("description", "") for i in json.loads(raw).get("value", []))
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    text = norm(re.sub(r"(?s)<[^>]+>", " ", raw))
    path.write_text(text, encoding="utf-8")
    return text


def main():
    if len(sys.argv) not in (2, 4):
        print(__doc__)
        return 2
    cache = Path(sys.argv[1])
    cache.mkdir(parents=True, exist_ok=True)
    texts = {}
    bad = 0
    for qid, key, quote in [(IDS[k], s, q) for k, s, q in QUOTES]:
        url = SOURCES[key][1]
        try:
            texts.setdefault(url, fetch(url, cache))
        except Exception as exc:  # report and keep going
            print(f"FAIL {qid}: cannot fetch {url}: {exc}")
            bad += 1
            continue
        if norm(quote) in texts[url]:
            print(f"ok   {qid} {key}")
        else:
            print(f"FAIL {qid} {key}: quote not found")
            bad += 1
    if PAGE.exists():
        page = PAGE.read_text(encoding="utf-8")
        for qid, quote in [(IDS[k], q) for k, _, q in QUOTES]:
            if f'id="ev-{qid}"' not in page or html.escape(quote, quote=False) not in page:
                print(f"FAIL {qid}: not listed word for word on the page")
                bad += 1
    print(f"{len(QUOTES)} quotes, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
