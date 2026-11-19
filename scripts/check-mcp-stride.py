"""Check reviewed STRIDE wording, exported data, public anchors and source quotes.

  python3 -I scripts/check-mcp-stride.py
  python3 -I scripts/check-mcp-stride.py --quotes /tmp/fresh-source-cache

The optional cache contains freshly fetched source text, using the filenames from
check-evidence-quotes.py. This check reads the complete interactive evidence
inventory, including its Purview and architecture-review additions. Checks prove
consistency and quote presence, not semantic correctness or mitigation efficacy.
"""

import argparse
import csv
import html
import importlib.util
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from mcp_stride_data import ELEMENTS, OBSERVED, STRIDE, THREATS, adjust, dread_score, level_of, rating  # noqa: E402


def norm(text):
    text = html.unescape(text)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"')):
        text = text.replace(a, b)
    return re.sub(r"\s+:", ":", " ".join(text.split()))


class DiagramLabels(HTMLParser):
    """Read visible DFD labels, excluding separately reviewed threat-id chips."""

    def __init__(self):
        super().__init__()
        self.in_dfd = False
        self.parts = None
        self.labels = set()

    def handle_starttag(self, tag, attrs):
        if tag == "svg" and dict(attrs).get("class") == "dfd":
            self.in_dfd = True
        if tag == "text" and self.in_dfd:
            self.parts = []

    def handle_data(self, text):
        if self.parts is not None:
            self.parts.append(text)

    def handle_endtag(self, tag):
        if tag == "text" and self.parts is not None:
            text = norm(" ".join(self.parts))
            if not re.fullmatch(r"[STRIDE]\d+", text):
                self.labels.add(text)
            self.parts = None
        if tag == "svg":
            self.in_dfd = False


def check(cache=None):
    spec = importlib.util.spec_from_file_location("stride_builder", HERE / "build-mcp-stride.py")
    build = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(build)
    build.check()
    rows = build.numbered()
    notes = (ROOT / "mcp-governance-stride.factcheck.md").read_text()
    page = (ROOT / "mcp-governance-stride.html").read_text()
    blob = re.search(r'<script type="application/json" id="data">(.*?)</script>', page, re.S)
    assert blob, "page model data not found"
    model = json.loads(blob[1])
    indexed = {t["id"]: t for t in model["threats"]}
    with (ROOT / "mcp-governance-stride.threats.tsv").open() as stream:
        exported = {t["id"]: t for t in csv.DictReader(stream, delimiter="\t")}
    assert set(indexed) == set(exported) == {r[0] for r in rows}, "exported threat IDs differ"
    source_notes = (ROOT / "mcp-governance-microsoft-interactive.factcheck.md").read_text()
    quotes = re.findall(r'^\| <a id="ev-(V\d+)"></a>V\d+ \| (.*?) \| \[[^\]]+\]\((https://.*?)\) \|', source_notes, re.M)
    quote_ids = {qid for qid, _, _ in quotes}
    for tid, el, cat, text, controls, _skills, scores, basis in rows:
        web, tsv = indexed[tid], exported[tid]
        score = dread_score(scores)
        assert f"| {tid} | {el} | {text} |" in notes, f"{tid}: wording has no review verdict"
        assert web["text"] == tsv["threat"] == text, f"{tid}: stale export"
        assert web["el"] == tsv["element"] == el, f"{tid}: element drift"
        assert web["cat"] == cat and tsv["stride"] == STRIDE[cat], f"{tid}: category drift"
        assert web["dr"] == [int(tsv[k]) for k in ("D", "R", "E", "A", "Di")] == list(scores), f"{tid}: factor drift"
        assert web["score"] == float(tsv["dread"]) == score, f"{tid}: score drift"
        assert web["rating"] == tsv["rating"] == rating(score), f"{tid}: rating drift"
        assert f'id="t-{tid}"' in page, f"{tid}: public anchor missing"
        assert web["ctrls"] == tsv["page_controls"].split() == controls, f"{tid}: controls differ"
        assert web["basis"] == basis.replace("AI inference", "interpretation by AI") and tsv["basis"] == basis, f"{tid}: basis drift"
        assert set(re.findall(r"\bV\d+\b", basis)) <= quote_ids, f"{tid}: missing architecture evidence"
        records = OBSERVED.get(tid, [])
        assert web["refs"] == [list(r) for r in records], f"{tid}: page evidence drift"
        assert tsv["evidence_refs"] == " | ".join(f"{title} <{url}>" for _, title, url in records), f"{tid}: TSV evidence drift"
        assert web["level"] == tsv["evidence"] == level_of(tid), f"{tid}: evidence level drift"
    for tid, t in zip((r[0] for r in rows), THREATS):
        assert adjust(tid, t[5]) == t[5], f"{tid}: evidence changed scenario score"
    assert set(model["elements"]) == set(ELEMENTS), "element IDs differ"
    for eid in ELEMENTS:
        assert f"#el-{eid}" in notes, f"{eid}: stable deep link not recorded"
    assert "Raised by the evidence rule" not in page, "obsolete score rule remains"
    assert "<dt>Evidence rule</dt>" not in page, "obsolete method remains"
    assert "direct call: blocked" not in page, "untested bypass block is asserted"
    for classes, tid in re.findall(r'<span class="(sw [^"]+)">([STRIDE]\d+)</span>', page):
        threat = indexed[tid]
        assert "r-" + threat["rating"].lower() in classes.split(), f"legend rating wrong: {tid}"
        assert ("pub" in classes.split()) == bool(threat["refs"]), f"legend evidence wrong: {tid}"
    labels = DiagramLabels()
    labels.feed(page)
    label_block = notes.split("<!-- Begin reviewed diagram labels -->\n", 1)[1].split("<!-- End reviewed diagram labels -->", 1)[0]
    reviewed_labels = set()
    for line in label_block.strip().splitlines():
        verdict, text = line.split("\t", 1)
        assert verdict in {"label", "requirement"}, f"invalid diagram verdict: {line}"
        reviewed_labels.add(text)
    assert labels.labels == reviewed_labels, f"DFD label review drift: {labels.labels ^ reviewed_labels}"
    for term in ("local choices", "uncalibrated AI estimates", "not completeness"):
        assert term in page, f"model limit missing: {term}"
    ids = re.findall(r'\bid="([^"]+)"', page)
    assert not [k for k, n in Counter(ids).items() if n > 1], "duplicate HTML IDs"
    print(f"{len(rows)} reviewed rows, matching page/TSV scores and evidence; stable public anchors")
    print(f"{len(labels.labels)} reviewed DFD labels and design requirements")
    if cache:
        from mcp_governance_interactive_evidence import QUOTES, IDS, UNAVAILABLE
        assert len(quotes) == len(QUOTES), "source quote inventory differs from the interactive evidence module"
        unavailable_ids = {IDS[key] for key in UNAVAILABLE}
        urls = set()
        for qid, quote, link in quotes:
            if qid in unavailable_ids:
                assert qid not in page, f"{qid}: unresolved quote used on STRIDE page"
                print(f"UNVERIFIED {qid}: source unavailable, historical quote only")
                continue
            url = urldefrag(link)[0]
            name = re.sub(r"[^a-z0-9]+", "-", url.lower()).strip("-")[-120:] + ".txt"
            file = cache / name
            assert file.exists(), f"{qid}: missing fresh source cache: {url}"
            assert norm(quote) in norm(file.read_text()), f"{qid}: quote absent from {url}"
            urls.add(url)
        print(f"{len(quotes) - len(unavailable_ids)} quotes present across {len(urls)} source URLs; {len(unavailable_ids)} explicitly unverified")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--quotes", type=Path)
    args = parser.parse_args()
    check(args.quotes)
