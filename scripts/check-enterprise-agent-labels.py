"""Check the reviewed wording of non-evidence text on an agent governance page.

Usage:
  python3 -I scripts/check-enterprise-agent-labels.py [page.html]          check one page (default: the long page)
  python3 -I scripts/check-enterprise-agent-labels.py page.html --list     print the captured texts, one per line

The ledger is the page's own .factcheck.md. A pass proves a verdict was recorded for the
exact wording, not that the verdict is right.
"""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PAGE = "enterprise-ai-agent-security-recommendation.html"
BEGIN = "<!-- Begin reviewed presentation text -->"
END = "<!-- End reviewed presentation text -->"
VOID = set("area base br col embed hr img input link meta param source track wbr".split())
VERDICTS = {"label", "requirement", "code token"}
FACT_STYLE = re.compile(
    r"\b(?:is|are) (?:generally available|in preview|always allowed|not supported)"
    r"|\b(?:automatically discovers|automatically publishes|supports only|"
    r"can block|can discover|does not inspect|does not support)\b",
    re.IGNORECASE,
)


# An ASCII figure holds boxes, arrows and words. Each run of words is one text to review.
ASCII_SPLIT = re.compile(r"\s-+X-+>\s|[|+]|\s{2,}|(?:\s-)+\s|\sX\s")


def ascii_texts(raw):
    found = []
    for line in raw.splitlines():
        for seg in ASCII_SPLIT.split(line):
            seg = re.sub(r"^X\s+", "", seg.strip(" -=.:<>^"))
            if seg and seg not in {"v", "X"}:
                found.append(seg)
    return found


class PresentationText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.items = []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        attrs = dict(attrs)
        classes = set(attrs.get("class", "").split())
        context = set().union(*(frame[1] for frame in self.stack))
        in_figure = any(frame[0] == "figure" for frame in self.stack)
        capture = (
            tag in {"title", "h1", "h2", "h3", "h4"}
            or in_figure and tag in {"text", "desc", "figcaption"}
            or in_figure and tag == "pre" and "ascii" in classes
            or "tg" in classes or "lead" in classes or "rl" in classes
            or bool(classes & {"what", "ex", "apt"})
            or tag in {"a", "p"} and "routes" in context
            or tag == "p" and bool(context & {"path", "flow", "ans", "decision", "returns"})
            or tag in {"dt", "dd"} and "route-notes" in context
            or tag == "li" and bool(context & {"chk", "key"})
            or tag == "li" and "layer" in context and "layer" not in classes
        )
        self.stack.append((tag, classes, [] if capture else None))
        if "gantt" in classes or tag == "pre" and "ascii" in classes:
            self.items.append(attrs["aria-label"])

    def handle_data(self, data):
        for _, _, parts in self.stack:
            if parts is not None:
                parts.append(data)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] != tag:
                continue
            for frame in self.stack[i:]:
                parts = frame[2]
                if parts is None:
                    continue
                if frame[0] == "pre" and "ascii" in frame[1]:
                    self.items.extend(ascii_texts("".join(parts)))
                    continue
                value = " ".join("".join(parts).split())
                if value:
                    self.items.append(value)
            del self.stack[i:]
            break


def check(markup, ledger):
    parser = PresentationText()
    parser.feed(markup)
    block = ledger.split(BEGIN, 1)[1].split(END, 1)[0].strip()
    rows = block.removeprefix("```text\n").removesuffix("\n```").splitlines()
    reviewed = {}
    failures = []
    for row in rows:
        verdict, value = row.split("\t", 1)
        if verdict not in VERDICTS or value in reviewed:
            failures.append(f"Invalid or duplicate verdict: {row}")
        reviewed[value] = verdict

    counts = Counter(parser.items)
    for value in sorted(counts.keys() - reviewed.keys()):
        failures.append(f"Missing verdict: {value}")
    for value in sorted(reviewed.keys() - counts.keys()):
        failures.append(f"Stale verdict: {value}")
    for value in sorted(counts):
        if FACT_STYLE.search(value):
            failures.append(f"Move product claim to sourced prose: {value}")
    return counts, failures


if __name__ == "__main__":
    import sys

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    name = args[0] if args else DEFAULT_PAGE
    page = ROOT / name if (ROOT / name).exists() else ROOT / "wip" / name
    ledger = page.with_suffix(".factcheck.md")
    if "--list" in sys.argv:
        parser = PresentationText()
        parser.feed(page.read_text())
        for value in dict.fromkeys(parser.items):
            print(value)
        raise SystemExit(0)
    counts, failures = check(page.read_text(), ledger.read_text())
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Checked {len(counts)} distinct presentation texts on {page.name}.")
