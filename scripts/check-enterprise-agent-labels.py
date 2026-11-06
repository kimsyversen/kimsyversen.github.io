"""Check the reviewed wording of non-evidence text on the agent security page."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "enterprise-ai-agent-security-recommendation.html"
LEDGER = PAGE.with_suffix(".factcheck.md")
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
            or "tg" in classes or "lead" in classes or "rl" in classes
            or bool(classes & {"what", "ex", "apt"})
            or tag in {"a", "p"} and "routes" in context
            or tag == "p" and bool(context & {"path", "flow", "ans", "decision", "returns"})
            or tag in {"dt", "dd"} and "route-notes" in context
            or tag == "li" and bool(context & {"chk", "key"})
            or tag == "li" and "layer" in context and "layer" not in classes
        )
        self.stack.append((tag, classes, [] if capture else None))
        if "gantt" in classes:
            self.items.append(attrs["aria-label"])

    def handle_data(self, data):
        for _, _, parts in self.stack:
            if parts is not None:
                parts.append(data)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] != tag:
                continue
            for _, _, parts in self.stack[i:]:
                if parts is not None:
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
    counts, failures = check(PAGE.read_text(), LEDGER.read_text())
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Checked {len(counts)} distinct presentation texts.")
