"""Check Developer-WS2.html.

Usage: python3 -I scripts/check-developer-ws2.py <cache-dir> [--offline-page]

1. Fetches each source URL once into <cache-dir> and confirms each quote appears
   in it word for word (quotes straightened, whitespace collapsed).
2. Confirms the page lists every quote as id="ev-V<n>" with the same words.
3. Confirms every evidence chip on the page points at a listed quote.
4. Confirms the reviewed-text ledger in Developer-WS2.factcheck.md matches the
   presentation texts on the page exactly (nothing missing, nothing changed).
5. Confirms the text each link points at sits inside one HTML block (a browser
   cannot highlight a text fragment that crosses table cells or code lines).
6. Fails on fact-style wording in ledger texts, paragraphs over 60 words,
   and em or en dashes anywhere on the page.

A pass shows the quotes are on the source pages today and that every
recorded verdict is for the exact wording. It does not show that a verdict
or a claim built on a quote is right.
"""

import html
import re
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from developer_ws2_evidence import BLOCK_FRAGS, IDS, QUOTES, SOURCES  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wip" / "Developer-WS2.html"
LEDGER = ROOT / "wip" / "Developer-WS2.factcheck.md"
BEGIN = "<!-- Begin reviewed presentation text -->"
END = "<!-- End reviewed presentation text -->"
VERDICTS = {"label", "requirement", "code token"}
REQ_WORD = re.compile(r"\b(must|should)\b", re.I)

# Wording that states what a product does. Allowed only in evidence-backed claim text.
FACT_STYLE = re.compile(
    r"\b(supports?|enforces?|blocks?|allows?|denies|deny|disables?|enables?|ships?|reads?|"
    r"applies|applied|overrides?|includes?|requires?|runs?|checks?|discovers?|inspects?|"
    r"logs?|can|cannot|can't|does|doesn't|is|are|was|were|has|have|will|always|never)\b",
    re.I,
)
DASH = re.compile("[–—]")


def norm(text):
    text = html.unescape(text)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), (" ", " ")):
        text = text.replace(a, b)
    return re.sub(r"\s+", " ", text).strip()


def fetch(url, cache):
    path = cache / (re.sub(r"[^a-z0-9]+", "-", url.lower()).strip("-")[-120:] + ".txt")
    if path.exists():
        return path.read_text(encoding="utf-8")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    text = norm(re.sub(r"(?s)<[^>]+>", " ", raw))
    path.write_text(text, encoding="utf-8")
    return text


def check_quotes(cache):
    texts, bad = {}, 0
    for k, key, quote in QUOTES:
        qid, url = IDS[k], SOURCES[key][1]
        if DASH.search(quote):
            print(f"FAIL {qid}: quote contains an en or em dash")
            bad += 1
        try:
            texts.setdefault(url, fetch(url, cache))
        except Exception as exc:
            print(f"FAIL {qid}: cannot fetch {url}: {exc}")
            bad += 1
            continue
        if norm(quote) in texts[url]:
            print(f"ok   {qid} {k}")
        else:
            print(f"FAIL {qid} {k}: quote not found in {key}")
            bad += 1
    return bad


BLK = r"</?(?:p|div|li|ul|ol|tr|td|th|table|tbody|thead|h[1-6]|br|pre|section|article|blockquote|dt|dd|details|summary)\\b[^>]*>"


def blocks_of(url, cache):
    """Source text split at block tags, so a text fragment can be tested against one block."""
    path = cache / ("raw-" + re.sub(r"[^a-z0-9]+", "-", url.lower()).strip("-")[-110:] + ".html")
    if path.exists():
        raw = path.read_text(encoding="utf-8")
    else:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        raw = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
        path.write_text(raw, encoding="utf-8")
    raw = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", raw)
    raw = re.sub(BLK, "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", "", raw)
    return [norm(b) for b in raw.split("\n") if b.strip()]


def check_blocks(cache):
    """The text the link points at must sit inside one block, or the browser cannot highlight it."""
    bad, seen = 0, {}
    for k, key, quote in QUOTES:
        url = SOURCES[key][1]
        if url not in seen:
            try:
                seen[url] = blocks_of(url, cache)
            except Exception as exc:
                print(f"FAIL {IDS[k]}: cannot fetch {url} for block check: {exc}")
                bad += 1
                seen[url] = []
        target = norm(BLOCK_FRAGS.get(k, quote))
        if not any(target in b for b in seen[url]):
            print(f"FAIL {IDS[k]} {k}: link target is not inside one block of {key}")
            bad += 1
    print(f"link targets: {len(QUOTES)} checked, {bad} problems")
    return bad


def ledger_texts(md):
    """Return {text: verdict} from the reviewed block: lines '| verdict | text |'."""
    if BEGIN not in md or END not in md:
        return None
    block = md.split(BEGIN, 1)[1].split(END, 1)[0]
    out = {}
    for line in block.splitlines():
        m = re.match(r"^\|\s*([a-z ]+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if m and m.group(1) in VERDICTS:
            out[html.unescape(m.group(2))] = m.group(1)
    return out


def page_texts(page):
    """Presentation texts are elements marked data-rt (one text each)."""
    return [norm(re.sub(r"<[^>]+>", "", m[1])) for m in re.findall(r"<(\w+)\b[^>]*\bdata-rt\b[^>]*>(.*?)</\1>", page, re.S)]


def check_page():
    bad = 0
    page = PAGE.read_text(encoding="utf-8")
    for k, _, quote in QUOTES:
        qid = IDS[k]
        if f'id="ev-{qid}"' not in page or html.escape(quote, quote=False) not in page:
            print(f"FAIL {qid}: not listed word for word on the page")
            bad += 1
    ids = {f"V{i}" for i in range(1, len(QUOTES) + 1)}
    for chip in set(re.findall(r'href="#ev-(V\d+)"', page)):
        if chip not in ids:
            print(f"FAIL chip {chip} has no quote")
            bad += 1
    if DASH.search(page):
        print("FAIL page contains an en or em dash")
        bad += 1
    for p in re.findall(r"<p\b[^>]*>(.*?)</p>", page, re.S):
        words = len(norm(re.sub(r"<[^>]+>", " ", p)).split())
        if words > 60:
            print(f"FAIL paragraph over 60 words ({words}): {norm(re.sub(r'<[^>]+>', ' ', p))[:60]}")
            bad += 1
    if "Made with AI" not in page or "This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human." not in page:
        print("FAIL Made with AI note missing or changed")
        bad += 1
    for name in ("Developer-WS2.plan", "Developer-WS2.decisions", "Developer-WS2.factcheck"):
        if name in page:
            print(f"FAIL page names a note file: {name}")
            bad += 1
    led = ledger_texts(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else None
    if led is None:
        print("FAIL ledger block missing in Developer-WS2.factcheck.md")
        return bad + 1
    texts = page_texts(page)
    for t in texts:
        if t not in led:
            print(f"FAIL text not in ledger or changed: {t[:70]}")
            bad += 1
    for t in led:
        if t not in texts:
            print(f"FAIL ledger text not on page: {t[:70]}")
            bad += 1
    for t, v in led.items():
        if v == "label":
            hit = FACT_STYLE.search(t)
            if hit:
                print(f"FAIL label uses fact-style word '{hit.group(0)}': {t[:70]}")
                bad += 1
        elif v == "requirement":
            if not REQ_WORD.search(t):
                print(f"FAIL requirement without must/should: {t[:70]}")
                bad += 1
        else:
            print(f"FAIL unknown verdict '{v}': {t[:70]}")
            bad += 1
    for c in re.findall(r'<p class="claim">(.*?)</p>', page, re.S):
        if 'class="ev"' not in c and 'class="tg' not in c:
            print(f"FAIL claim without chip or tag: {norm(re.sub(r'<[^>]+>', ' ', c))[:70]}")
            bad += 1
    print(f"page: {len(texts)} reviewed texts, {len(led)} ledger rows, {bad} problems")
    return bad


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cache = Path(sys.argv[1])
    cache.mkdir(parents=True, exist_ok=True)
    bad = check_quotes(cache) + check_blocks(cache)
    if PAGE.exists() and "--quotes-only" not in sys.argv:
        bad += check_page()
    print(f"{len(QUOTES)} quotes, {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
