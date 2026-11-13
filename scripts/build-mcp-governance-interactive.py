#!/usr/bin/env python3
"""Build mcp-governance-microsoft-interactive.html.

Reuses definitions from scripts/build-mcp-governance.py without writing its page.
Interactive-only wording corrections and evidence live in the companion modules.
Each control has one home box.

Usage: python3 -I scripts/build-mcp-governance-interactive.py
"""

import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote as urlquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OLD_PATH = HERE / "build-mcp-governance.py"
PAGE = "mcp-governance-microsoft-interactive"
OUT = ROOT / f"{PAGE}.html"
NOTES = ROOT / f"{PAGE}.factcheck.md"
OLD_FACT = "mcp-governance-microsoft.factcheck.md"

# ---- shared content ------------------------------------------------------
_src = OLD_PATH.read_text(encoding="utf-8")
_src = _src[:_src.index("for ch in (chr(0x2014)")]
_url_line = 'blob/master/mcp-governance-microsoft.factcheck.md"'
if _src.count(_url_line) != 1:
    sys.exit("fact check url not found exactly once in the shared builder")
_src = _src.replace(_url_line, f'blob/master/{PAGE}.factcheck.md"')
_src = _src.replace('NOTES = ROOT / "mcp-governance-microsoft.factcheck.md"', f'NOTES = ROOT / "{PAGE}.factcheck.md"')
sys.path.insert(0, str(HERE))
ns = {"__file__": str(OLD_PATH), "__name__": "shared_content"}
exec(compile(_src, str(OLD_PATH), "exec"), ns)
import mcp_governance_interactive_evidence as interactive_evidence
ns.update({name: getattr(interactive_evidence, name) for name in
           ("QUOTES", "IDS", "SOURCES", "PREVIEW_ONLY", "CHECKED")})

from section_anchors import add_anchors  # noqa: E402

HEAD, STYLE, MARKERS, AI_NOTE = ns["HEAD"], ns["STYLE"], ns["MARKERS"], ns["AI_NOTE"]
EXTRA_CSS_OLD = ns["EXTRA_CSS"]
FACTCHECK_URL = ns["FACTCHECK_URL"]
REC, UNV, INF, PRE = ns["REC"], ns["UNV"], ns["INF"], ns["PRE"]
LAYER_ROWS, DESIGN_ROWS, GR_PREV_RAW = ns["LAYER_ROWS"], ns["DESIGN_ROWS"], ns["GR_PREV_RAW"]
GR_PREV_FY = ns["GR_PREV"][0]
PREVIEW_HTML, ROLLOUT, GAPS = ns["PREVIEW"], ns["ROLLOUT"], ns["GAPS"]
QUOTES, IDS, SOURCES, PREVIEW_ONLY, CHECKED = ns["QUOTES"], ns["IDS"], ns["SOURCES"], ns["PREVIEW_ONLY"], ns["CHECKED"]
frag, ev, evp, anchors = ns["frag"], ns["ev"], ns["evp"], ns["anchors"]

_shared_frag = frag


def frag(quote):
    """Keep published fragments unless the shared helper produces an empty range."""
    fragment = _shared_frag(quote)
    if fragment.startswith('#:~:text=,') or fragment.endswith(','):
        return '#:~:text=' + urlquote(quote, safe='').replace('-', '%2D')
    return fragment

# The Foundry tool call and tool response intervention points are labelled Preview in their source,
# so they back the preview design here. The shared list still counts them as released.
PREVIEW_ONLY = set(PREVIEW_ONLY) | {k for k, v in IDS.items() if v in ("V102", "V103")}

# Tag key block, placed after the AI note rules. The shared style from the first page has none.
_AI_NOTE_CSS = "@media (max-width:560px){.ai-note{grid-template-columns:1fr}}\n"
_TAG_KEY_CSS = (
    ".tag-key{margin:6px 0 0;padding-top:12px;border-top:1px solid var(--line);display:grid;grid-template-columns:9rem 1fr;gap:2px 16px;font-size:0.78rem;line-height:1.5}\n"
    ".tag-key h2{font-size:0.68rem;font-weight:600;letter-spacing:0.09em;text-transform:uppercase;color:var(--ink);line-height:1.5;padding-top:1px}\n"
    ".tag-key dl{margin:0;display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;align-items:baseline}\n"
    ".tag-key dt{margin:0}\n"
    ".tag-key dd{margin:0}\n"
    "@media (max-width:560px){.tag-key{grid-template-columns:1fr}.tag-key dl{grid-template-columns:1fr;gap:2px 0}.tag-key dd{margin-bottom:8px}}\n")
if STYLE.count(_AI_NOTE_CSS) != 1:
    sys.exit("ai-note style rule not found exactly once in the shared style")
STYLE = STYLE.replace(_AI_NOTE_CSS, _AI_NOTE_CSS + _TAG_KEY_CSS)


TITLE = "A proposed design for MCP Governance in a Microsoft ecosystem"
DESC = ("The MCP governance design as one interactive diagram: select a box to see its controls, "
        "and filter by objective or call layer.")
HEAD = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", HEAD, flags=re.S)
HEAD = re.sub(r'(<meta name="description" content=")[^"]*(")', rf"\g<1>{DESC}\2", HEAD)


def strip_anchors(text):
    """Drop the empty spans that kept old ids alive on the first page. Gap ids stay."""
    return re.sub(r'<span id="(?!gap-)[^"]+"></span>', "", text)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", html.unescape(text).lower()).strip("-")


# ---- controls: parse the shared rows -------------------------------------
LAYER_NAMES = ["Whole path", "Which server", "Person approves", "Call content",
               "Network and gateway", "Company server", "Tool response"]
LAYER_OF_GRP = []  # layer number per group row, in order: 0 whole path, 1 to 6
LABEL = re.compile(r'(?:<span id="ctrl-([^"]+)">(.*?)</span>|(.*?))<span class="rt">(.*?)</span>', re.S)

CONTROLS = []  # dicts: id, title, meta, applies, req, doc, layers, objs, preview, guardrail


def objs_of(meta):
    found = []
    if re.search(r"\bObjectives? A\b|\bA and B\b", meta):
        found.append("A")
    if re.search(r"\bObjectives? B\b|\bA and B\b", meta):
        found.append("B")
    return found


layer_no = -1
for row in LAYER_ROWS:
    if isinstance(row, tuple):
        layer_no += 1
        continue
    label, applies, req, doc = row
    m = LABEL.fullmatch(label)
    if not m:
        sys.exit(f"cannot read control label: {label[:60]!r}")
    cid, t1, t2, meta = m.groups()
    guardrail = cid is None
    title = t1 if cid else t2
    CONTROLS.append(dict(
        id=cid or ("g-" + slug(title)), title=title, meta=meta, applies=applies,
        req=None if req == ns["NONE_ADDED"] else req, doc=doc, layers=[layer_no],
        objs=objs_of(meta), preview=False, guardrail=guardrail))

pv_block = PREVIEW_HTML[PREVIEW_HTML.index('<div class="sub3" id="preview-controls">'):PREVIEW_HTML.index('<span id="preview-env">')]
PV_ROW = re.compile(r'<tr><td><span id="ctrl-([^"]+)">(.*?)</span><span class="rt">(.*?)</span></td><td>(.*?)</td><td>(.*?)</td></tr>', re.S)
PV_LAYER = {"a365": [4], "a365-consent": [4], "ai-resource": [4], "ai-limits": [4], "ai-publish": [4],
            "ttp-users": [4], "ttp-modes": [4], "byo": [4], "foundry-routing": [4], "outbound-filter": [4]}
# The first page names layer 4 only for tool threat protection. The other layer 4 tags are an AI estimate
# and say so on the page, the way the first page marks its own layer guess for the prompt attack block.
PV_LAYER_EST = {"a365", "a365-consent", "ai-resource", "ai-limits", "ai-publish", "byo", "foundry-routing", "outbound-filter"}
for cid, title, meta, req, doc in PV_ROW.findall(pv_block):
    CONTROLS.append(dict(id=cid, title=title, meta=meta, applies=None, req=req, doc=doc,
                         layers=PV_LAYER[cid], objs=objs_of(meta), preview=True, guardrail=False))

PV_GR_LAYERS = {"Tool call and tool response guardrails": [3, 6], "Threat detection": [3],
                "Defender real-time protection": [3, 6], "Defender on the Agent 365 path": [3],
                "Defender rules and scope": [3, 6], "Defender for Endpoint runtime protection": []}
for name, product, layer, text in [GR_PREV_FY] + [r[1] for r in GR_PREV_RAW]:
    CONTROLS.append(dict(id="g-" + slug(name), title=name, meta="Guardrail", applies=product, req=None,
                         doc=text, layers=PV_GR_LAYERS[name], objs=[], preview=True, guardrail=True,
                         layer_text=layer))

# The Network guardrail is preview (guardrails overview); toolbox network isolation is separate.
for _c in CONTROLS:
    if _c["id"] == "foundry-network":
        _c["doc"] = (f"For a Foundry toolbox, its hosting project governs network access {ev('fy-gov')}. "
                     f"Downstream connectivity depends on the tool and its hosting {ev('fy-tool')}. "
                     f"Configure egress separately from inbound private access. {REC}")
CONTROLS.append(dict(
    id="foundry-egress", title="Foundry Network guardrail", meta="Objective B",
    applies="Hosted agents and prompt agents on the Copilot harness", layers=[4], objs=["B"],
    preview=True, guardrail=False,
    req=f"Pilot explicit destination rules; do not count this guardrail as part of the released-only baseline. {REC}",
    doc=(f"The Network control covers hosted agents and prompt agents on the Copilot harness, not other prompt agents {ev('gr-fy-net')}. "
         f"Agent guardrails are preview {evp('gr-fy-agprev')}; hosted agents use per-session VM sandboxes {ev('gr-fy-sandbox')}.")))

# Page-only control. The first page has no Purview row; this one adds what Purview records about agent tool calls.
CONTROLS.append(dict(
    id="purview-audit", title="Purview audit of agent tool calls", meta="Objectives A and B",
    applies="Agent 365 agent instances", layers=[0], objs=["A", "B"], preview=False, guardrail=False,
    req=(f"Add the Purview audit log for Agent 365 activities to the log review. Look for tool calls to servers that are not on the approved list. {REC} "
         f"{INF} Interpretation by AI: MCP tool calls count as agent-to-tools interactions. The Purview pages do not name MCP."),
    doc=(f"Agent 365 agent instances are audited from creation {ev('purview-audit-on')}, including agent-to-tools interactions "
         f"{ev('purview-audit-tools')}, in a searchable audit log {ev('purview-audit-search')}. "
         f"Agent 365 DLP lists only agent-to-human and human-to-agent traffic {ev('purview-dlp-scope')}. "
         f"DSPM lists agents active in the last 30 days {ev('purview-dspm-inventory')}. "
         f"For Foundry, Purview audits prompts and responses {ev('purview-foundry-audit')}; its page does not mention tool calls.")))

CTRL = {c["id"]: c for c in CONTROLS}
if len(CTRL) != len(CONTROLS):
    sys.exit("duplicate control id")

# ---- parts: shared design rows -------------------------------------------
PART = {}
for name_html, does, where, use in DESIGN_ROWS:
    name = re.sub(r"<span class=\"rt\">.*?</span>", "", name_html)
    PART[name] = (does, where, use)


def clean_use(use, here=()):
    """The control links in the shared rows are replaced by the controls on the box itself.
    A link to a control that sits in another box stays, so the reader can still reach it."""
    use = re.sub(r'<a href="#ctrl-([^"]+)">[^<]*</a>', lambda m: "" if m.group(1) in here else m.group(0), use)
    use = re.sub(r"(;\s*)+;", ";", use)
    use = re.sub(r";\s*\.", ".", use)
    return re.sub(r"^[;.\s]+|[;\s]+$", "", use).strip()


# ---- nodes ---------------------------------------------------------------
# One CSS grid holds the whole map. Columns: 1 trunk line, 2 policy target, 3 gap, 4 client, 5 gap,
# 6 what sits before the gateway, 7 rail line into the gateway. place = (col start, col end, row start, row end).
# Rows: 1 label, 2 Git and pipeline, 3 column heads, 4 to 7 the four client lanes, 8 label,
# 9 and 10 gateway, logging and the preview route, 11 label, 12 company server.
# role sets the color: pol = policy plane, call = call path, gw = gateway, be = server, log = monitoring, pv = preview.
# The list order is the reading order: tab order, panel order and Previous and Next follow it.
NODES = [
    dict(id="git", kind="Source of truth", role="pol", place=(2, 3, 2, 3), title=["Approved list", "in Git"], sub="Approved and denied",
         parts=["Approved list in Git"], ctl=["inventory"], applies=True),
    dict(id="pipeline", kind="Source of truth", role="pol", place=(4, 5, 2, 3), title=["Sync pipeline"], sub="Proposed automation",
         parts=["Sync pipeline"], ctl=["pipeline"], applies=True),
    dict(id="ghe", kind="Policy target", role="pol", place=(2, 3, 4, 5), title=["GitHub Enterprise"], sub="Managed settings file",
         parts=["GitHub Enterprise"], ctl=[]),
    dict(id="vs", kind="Client", role="call", place=(4, 5, 4, 5), title=["VS Code,", "GitHub Copilot"], sub="",
         parts=[], ctl=["client", "g-server-trust-prompt", "stdio", "g-confirmation-dialog", "g-approval-lock",
                        "g-tool-call-hook", "g-result-review", "g-defender-for-endpoint-runtime-protection"]),
    dict(id="device", kind="Device", role="call", place=(6, 7, 4, 5), title=["Managed", "Windows device"], sub="Intune",
         parts=["Client and device controls"], ctl=["windows", "outbound-filter"]),
    dict(id="m365admin", kind="Policy target", role="pol", place=(2, 3, 5, 6), title=["Microsoft 365", "admin center"], sub="Set by hand",
         parts=["Microsoft 365 admin center"], ctl=["m365"]),
    dict(id="m365", kind="Client", role="call", place=(4, 5, 5, 6), title=["Microsoft 365", "Copilot"], sub="",
         parts=[], ctl=["g-write-approval", "m365-network"]),
    dict(id="fypolicy", kind="Policy target", role="pol", place=(2, 3, 6, 7), title=["Microsoft Foundry"], sub="Allowed tool lists",
         parts=["Microsoft Foundry"], ctl=["foundry"]),
    dict(id="fy", kind="Client", role="call", place=(4, 5, 6, 7), title=["Foundry agents"], sub="",
         parts=[], ctl=["g-approval", "g-untrusted-results", "foundry-network", "foundry-routing",
                        "g-tool-call-and-tool-response-guardrails", "foundry-egress"]),
    dict(id="defender", kind="Preview guardrail product", role="pv", place=(6, 7, 6, 8), title=["Microsoft", "Defender"], sub="Checks tool calls",
         parts=[], ctl=["g-defender-real-time-protection", "g-defender-on-the-agent-365-path", "g-defender-rules-and-scope"],
         preview=True, applies=True),
    dict(id="pp", kind="Policy target", role="pol", place=(2, 3, 7, 8), title=["Power Platform"], sub="Manual until API verified",
         parts=["Power Platform"], ctl=["power-platform"]),
    dict(id="cs", kind="Client", role="call", place=(4, 5, 7, 8), title=["Copilot Studio"], sub="",
         parts=[], ctl=["g-ask-before-running", "g-prompt-attack-block", "g-threat-detection"]),
    dict(id="log", kind="Monitoring", role="log", place=(2, 3, 9, 10), title=["Logging, checks", "and Purview"], sub="All clients",
         parts=[], ctl=["logging", "purview-audit"], applies=True),
    dict(id="gw", kind="Control point", role="gw", place=(4, 7, 9, 11), title=["Gateway"], sub="",
         parts=["Azure API Management", "AI Gateway integrated with Foundry"],
         ctl=["gateway", "identity", "a365", "a365-consent", "ai-resource", "ai-limits", "ai-publish", "ttp-users", "ttp-modes"],
         applies=True),
    dict(id="byo", kind="Separate preview route", role="pv", place=(2, 3, 10, 11), title=["Agent 365 BYO route"], sub="Alternative; excluded",
         parts=[], ctl=["byo"], preview=True),
    dict(id="be", kind="Backend", role="be", place=(2, 8, 11, 12), title=["Company MCP server"], sub="Gateway-only access",
         parts=["Company MCP server"], ctl=["backend"]),
]
NODE = {n["id"]: n for n in NODES}

used = [c for n in NODES for c in n["ctl"]]
missing = [c["id"] for c in CONTROLS if c["id"] not in used]
dupes = sorted({c for c in used if used.count(c) > 1})
unknown = [c for c in used if c not in CTRL]
if missing or dupes or unknown:
    sys.exit(f"control mapping broken: missing={missing} duplicate={dupes} unknown={unknown}")
if len(PART) != 10:
    sys.exit("expected 10 shared parts")
used_parts = [p for n in NODES for p in n["parts"]]
for p in PART:
    if p not in used_parts:
        sys.exit(f"part without a box: {p}")
for p in used_parts:
    if p not in PART:
        sys.exit(f"unknown part: {p}")

for n in NODES:
    n["n_safe"] = sum(1 for c in n["ctl"] if not CTRL[c]["preview"])
    n["n_all"] = len(n["ctl"])
    n.setdefault("preview", False)
    n.setdefault("applies", False)


# ---- lines between boxes -------------------------------------------------
# The script draws these from the box positions, so they follow the layout at every width.
# r is the route: h = side to side, v = bottom to top, trunk = pipeline down the left edge,
# branch = trunk into a policy target, rail = out to the right edge and down into the gateway,
# blocked = the direct call that the server refuses. k is the line style. paths lists the
# Follow a path buttons that light the line. view limits a line to one design.
EDGES = [
    dict(id="git-pipeline", a="git", b="pipeline", k="pol", r="h", paths=["policy"]),
    dict(id="trunk", a="pipeline", b="pp", k="pol", r="trunk", paths=["policy"]),
    dict(id="to-ghe", a="pipeline", b="ghe", k="pol", r="branch", paths=["policy"]),
    dict(id="to-m365admin", a="pipeline", b="m365admin", k="pol dash", r="branch", paths=["policy"]),
    dict(id="to-fypolicy", a="pipeline", b="fypolicy", k="pol", r="branch", paths=["policy"]),
    dict(id="to-pp", a="pipeline", b="pp", k="pol dash", r="branch", paths=["policy"]),
    dict(id="ghe-vs", a="ghe", b="vs", k="pol", r="h", paths=["policy"]),
    dict(id="m365admin-m365", a="m365admin", b="m365", k="pol", r="h", paths=["policy"]),
    dict(id="fypolicy-fy", a="fypolicy", b="fy", k="pol", r="h", paths=["policy"]),
    dict(id="pp-cs", a="pp", b="cs", k="pol", r="h", paths=["policy"]),
    dict(id="vs-device", a="vs", b="device", k="call", r="h", paths=["vs"]),
    dict(id="device-gw", a="device", b="gw", k="call", r="rail", paths=["vs"]),
    dict(id="m365-gw", a="m365", b="gw", k="call", r="rail", paths=["m365"]),
    dict(id="fy-gw", a="fy", b="gw", k="call", r="rail", paths=["fy"], view="safe"),
    dict(id="cs-gw", a="cs", b="gw", k="call", r="rail", paths=["cs"], view="safe"),
    dict(id="fy-defender", a="fy", b="defender", k="call", r="h", paths=["fy"], view="preview"),
    dict(id="cs-defender", a="cs", b="defender", k="call", r="h", paths=["cs"], view="preview"),
    dict(id="defender-gw", a="defender", b="gw", k="call", r="rail", paths=["fy", "cs"], view="preview"),
    dict(id="gw-be", a="gw", b="be", k="call", r="v", paths=["vs", "m365", "fy", "cs"]),
    dict(id="log-gw", a="log", b="gw", k="log", r="h", paths=[]),
    dict(id="direct", a="vs", b="be", k="red", r="blocked", paths=["direct"]),
    dict(id="byo-be", a="byo", b="be", k="red", r="blocked", paths=["byo"], view="preview"),
]
for e in EDGES:
    for end in (e["a"], e["b"]):
        if end not in NODE:
            sys.exit(f"line {e['id']} names an unknown box {end}")

# Follow a path. Each note restates the figure description below; nothing new is claimed.
PATHS = [
    dict(id="policy", label="Approved list", k="pol",
         nodes=["git", "pipeline", "ghe", "m365admin", "fypolicy", "pp", "vs", "m365", "fy", "cs"],
         note="The proposed pipeline maps Git decisions to GitHub settings and Foundry connection tool lists. "
              "Power Platform stays manual until its MCP API path is verified; Microsoft 365 connector access is manual. "
              "These are separate policy scopes, not interchangeable server allowlists."),
    dict(id="vs", label="VS Code", k="call", nodes=["vs", "device", "gw", "be"],
         note="VS Code and local GitHub Copilot run on the managed Windows device and call the gateway. "
              "The gateway calls the company MCP server. Remote and cloud sessions need their own controls."),
    dict(id="m365", label="Microsoft 365 Copilot", k="call", nodes=["m365", "gw", "be"],
         note="Microsoft 365 Copilot calls the gateway from the Microsoft cloud, from fixed outbound addresses. No device is on this path."),
    dict(id="fy", label="Foundry agents", k="call", nodes=["fy", "gw", "be"], nodes_pv=["defender"],
         note="Foundry agents call the gateway, which calls the company MCP server.",
         note_pv=f"Foundry agents call the gateway, which calls the company MCP server. Microsoft Defender checks the tool call before it runs. "
                 f"{INF} Interpretation by AI: the sources do not say where Defender runs."),
    dict(id="cs", label="Copilot Studio", k="call", nodes=["cs", "gw", "be"], nodes_pv=["defender"],
         note="Copilot Studio calls the gateway, which calls the company MCP server.",
         note_pv=f"Copilot Studio calls the gateway, which calls the company MCP server. Microsoft Defender checks the tool call before it runs. "
                 f"{INF} Interpretation by AI: the sources do not say where Defender runs."),
    dict(id="direct", label="Direct call", k="red", nodes=["vs", "m365", "fy", "cs", "be"],
         note="Design requirement: reject direct client access to the company MCP server. Verify every bypass route in the acceptance tests."),
    dict(id="byo", label="Agent 365 route", k="red", nodes=["byo", "be"], preview=True,
         note="Alternative preview route, excluded from this topology: BYO needs a public endpoint through the Agent 365 Tooling Gateway. "
              "Direct access to the private company backend must fail. Registering the company gateway URL instead requires a separate compatibility test."),
]
for p in PATHS:
    for nid in p["nodes"] + p.get("nodes_pv", []):
        if nid not in NODE:
            sys.exit(f"path {p['id']} names an unknown box {nid}")
    if not any(p["id"] in e["paths"] for e in EDGES):
        sys.exit(f"path {p['id']} lights no line")


# ---- map -----------------------------------------------------------------
def esc(t):
    return html.escape(t, quote=False)


def count_text(n, preview):
    k = n["n_all"] if preview else n["n_safe"]
    return f"{k} control{'s' if k != 1 else ''}" if k else ""


def box(n):
    c1, c2, r1, r2 = n["place"]
    cls = f'bx {n["role"]}' + (" view-preview" if n["preview"] else "")
    out = [f'<a class="{cls}" id="b-{n["id"]}" href="#n-{n["id"]}" data-node="{n["id"]}" '
           f'style="grid-area:{r1}/{c1}/{r2}/{c2}">']
    if n["preview"]:
        out.append('<span class="bp">Preview</span>')
    out.append(f'<span class="bt">{esc(" ".join(n["title"]))}</span>')
    if n["id"] == "gw":
        out.append('<span class="bs view-safe">Azure API Management</span><span class="bs view-preview">API Management or AI Gateway</span>')
    elif n["sub"]:
        out.append(f'<span class="bs">{esc(n["sub"])}</span>')
    if n["n_all"] != n["n_safe"] and not n["preview"]:
        out.append(f'<span class="bc view-safe">{count_text(n, False)}</span><span class="bc view-preview">{count_text(n, True)}</span>')
    else:
        ct = count_text(n, True)
        if ct:
            out.append(f'<span class="bc">{ct}</span>')
    out.append('<span class="bf" aria-live="off"></span></a>')
    return "".join(out)


def map_html():
    out = ['<div class="map" id="mapGrid">',
           '<p class="zl z-pol" style="grid-area:1/2/2/-1">Source of truth</p>',
           '<p class="ch z-pol" style="grid-area:3/2/4/3">Policy target</p>',
           '<p class="ch z-call" style="grid-area:3/4/4/5">Client</p>',
           '<p class="ch z-call" style="grid-area:3/6/4/7">Before the gateway</p>',
           '<span class="g-trunk" aria-hidden="true" style="grid-area:4/1/8/2"></span>',
           '<span class="g-rail" aria-hidden="true" style="grid-area:4/7/11/8"></span>',
           '<p class="wl" style="grid-area:5/6/6/7">Microsoft cloud, fixed addresses</p>',
           '<p class="zl z-gw" style="grid-area:8/2/9/4">Control point</p>',
           '<p class="xl" style="grid-area:8/4/9/7">Direct call: must be blocked</p>']
    out += [box(n) for n in NODES]
    out.append("</div>")
    return "\n".join(out)


def path_buttons():
    b = []
    for p in PATHS:
        cls = "chip pk" + (" view-preview" if p.get("preview") else "")
        b.append(f'<button type="button" class="{cls}" data-path="{p["id"]}" data-k="{p["k"]}" aria-pressed="false">'
                 f'<span class="sw sw-{p["k"]}" aria-hidden="true"></span>{p["label"]}</button>')
    return "".join(b)


DESC_FIG = ("Design requirements, not a deployed or tested topology. Git holds approval decisions. "
            "The proposed pipeline updates GitHub settings and Foundry connection tool lists. Power Platform is manual until MCP API support is verified; Microsoft 365 connector access is manual. "
            "Approved clients call the gateway; only the gateway reaches the private company MCP backend. VS Code runs on the managed Windows device. "
            "Microsoft 365 Copilot calls from the Microsoft cloud; its documented egress addresses do not replace authentication. "
            "Logging joins gateway and client records; Purview coverage depends on the agent integration. "
            "Preview adds optional detection and an optional dedicated AI Gateway. The alternative Agent 365 BYO route is excluded from direct backend access.")


# ---- panels --------------------------------------------------------------
def dl(rows):
    return "<dl>" + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rows if v) + "</dl>"


def control_html(n, cid):
    c = CTRL[cid]
    meta = c["meta"] if not c["guardrail"] or c["preview"] else "Product guardrail"
    if c["guardrail"] and c["preview"]:
        meta = "Product guardrail"
    layers = c["layers"]
    ltxt = ""
    if c["guardrail"] and c.get("layer_text"):
        lt = c["layer_text"]
        ltxt = ("layer not stated" if lt == "Not stated" else "layers as the other Defender controls"
                if lt.startswith("Same as") else "layer " + lt if lt[0].isdigit() else "layers: " + lt)
    elif layers and layers != [0]:
        ltxt = "layer " + " and ".join(str(x) for x in layers)
        if c["id"] in PV_LAYER_EST:
            ltxt += ", AI estimate"
    elif layers == [0]:
        ltxt = "whole path"
    head_meta = " · ".join(x for x in (meta, ltxt) if x)
    rows = []
    if (n["applies"] or c["preview"] and c["guardrail"]) and c["applies"] and not (c["guardrail"] and not n["applies"]):
        rows.append(("Applies to", c["applies"]))
    if not c["guardrail"] and n["applies"] and c["applies"]:
        pass
    rows.append(("Design requirement", c["req"]) if c["req"] else ("", ""))
    rows.append(("What Microsoft and GitHub document" if not c["preview"] else "What Microsoft documents", c["doc"]))
    # de-duplicate Applies to
    seen, out = set(), []
    for k, v in rows:
        if k and k not in seen:
            out.append((k, v))
            seen.add(k)
    classes = "ctl" + (" view-preview" if c["preview"] else "")
    objs = " ".join(c["objs"]) or "-"
    lay = " ".join(str(x) for x in layers) or "-"
    tag = f" {PRE}" if c["preview"] else ""
    return (f'<div class="{classes}" id="ctrl-{c["id"]}" data-obj="{objs}" data-layer="{lay}">'
            f'<h4>{c["title"]}{tag} <span class="rt">{head_meta}</span></h4>{dl(out)}</div>')


def panel(n):
    parts = []
    for pn in n["parts"]:
        does, where, use = PART[pn]
        parts.append(f'<div class="part" id="part-{slug(pn)}"><h4>{pn}</h4>'
                     + dl([("What it does", does), ("Where it is set or run", where),
                           ("Use in this design", clean_use(use, n["ctl"]))]) + "</div>")
    ctls = "".join(control_html(n, cid) for cid in n["ctl"])
    cls = "np" + (" view-preview" if n["preview"] else "")
    extra = ""
    if n["id"] == "defender":
        extra = ('<p class="q-note">' + INF + ' Interpretation by AI: Defender is drawn between the agents and the gateway because the sources say it checks tool calls before they run. They do not say where it runs.</p>')
    if n["id"] == "device":
        extra = ('<p class="q-note">' + INF + ' Interpretation by AI: a device rule sees only calls that leave the device. '
                 'Microsoft 365 Copilot, Copilot Studio and Foundry calls leave from Microsoft cloud services, so these controls do not cover them. Not tested.</p>')
    # The layer gaps the first page states in its controls table. Without this the reader sees them
    # only when a layer filter is on.
    if n["id"] == "fy":
        extra = ('<p class="q-note">For Foundry agents, no released guardrail was established by this review for call content (layer 3) or tool responses (layer 6). '
                 'The pages read on 2026-11-11 describe only preview controls at both layers.</p>')
    if n["id"] == "cs":
        extra = ('<p class="q-note">No released guardrail checks call content (layer 3). '
                 'The pages read on 2026-11-11 describe only a preview control there.</p>')
    note = ""
    if not n["ctl"] and not n["parts"]:
        note = "<p>No control is set here.</p>"
    return (f'<article class="{cls}" id="n-{n["id"]}" data-node="{n["id"]}" data-role="{n['role']}">'
            f'<header><span class="kind">{n["kind"]}</span><h3>{" ".join(n["title"])}</h3></header>'
            f'{"".join(parts)}{ctls}{extra}{note}</article>')


# ---- chips ---------------------------------------------------------------
CHIPS = ([("obj", "A", "A: company server only through the gateway"), ("obj", "B", "B: managed clients limited to approved servers")]
         + [("layer", "0", "Whole path")]
         + [("layer", str(i), f"{i} {LAYER_NAMES[i]}") for i in range(1, 7)])


def chips_html():
    def grp(name, label, items):
        b = "".join(f'<button type="button" class="chip" data-grp="{g}" data-val="{v}" aria-pressed="false">{t}</button>' for g, v, t in items)
        return f'<div class="chipset" role="group" aria-label="{label}"><span class="cl">{label}</span>{b}</div>'
    return ('<details class="flt" open><summary>Filter by objective or call layer<span class="flt-n" id="fltN"></span></summary>'
            + grp("obj", "Objective", [c for c in CHIPS if c[0] == "obj"])
            + grp("layer", "Call layer", [c for c in CHIPS if c[0] == "layer"])
            + '<p class="cl-note">Content filters on the user input and the final answer are left out: they are not MCP controls.</p></details>')


# ---- page parts ----------------------------------------------------------
# ---- page parts ----------------------------------------------------------
# Color has meaning on this page. Amber is the approved list on its way to the policy targets,
# blue is a live call on its way to the company server, red is blocked, preview or not verified,
# and grey is monitoring. The shared paper palette is replaced with a cooler one so the three read apart.
EXTRA_CSS = EXTRA_CSS_OLD.replace("</style>", """
:root{
  --bg:#EEF2F3; --surface:#FFFFFF; --ink:#13212A; --muted:#506069; --line:#C9D3D8; --rule:#13212A;
  --hover:rgba(19,33,42,.05);
  --red:#B42D1A; --red-soft:#F7E1DC; --hatch:rgba(180,45,26,.10);
  --pol:#8A5300; --pol-line:#C7861C; --pol-bg:#FBF0DC;
  --call:#1B5B85; --call-line:#2D6E9C; --call-bg:#E1ECF4;
  --gw-bg:#1B5B85; --gw-ink:#FFFFFF; --gw-muted:rgba(255,255,255,.78);
  --log:#6A7880;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0E161B; --surface:#15212A; --ink:#E2EAEE; --muted:#97A8B2; --line:#2A3B46; --rule:#E2EAEE;
    --hover:rgba(226,234,238,.06);
    --red:#F07A60; --red-soft:#3A1F19; --hatch:rgba(240,122,96,.13);
    --pol:#EBB45C; --pol-line:#C9902F; --pol-bg:#2E2414;
    --call:#7DB8E3; --call-line:#4F93C4; --call-bg:#142C3C;
    --gw-bg:#2A6E9E; --gw-ink:#FFFFFF; --gw-muted:rgba(255,255,255,.8);
    --log:#8395A0;
  }
}
a{text-decoration-color:var(--call-line)}
a:hover{color:var(--call)}
a:focus-visible,button:focus-visible{outline:2px solid var(--call);outline-offset:3px}
.mast{border-top-color:var(--call)}
.toc{background:var(--bg)}
/* compact header so the paths and the map show on the first screen */
h1{font-size:clamp(2.2rem,4.6vw,3.4rem);margin-top:18px}
.toc{margin-top:22px}
@media (max-width:640px){.toc ul{margin-top:22px}}
.toc + .sec,.toc + main > .sec:first-child{margin-top:28px}
.seg button[aria-pressed="true"]{background:var(--call);border-color:var(--call);color:#fff}
.seg button[data-view-btn="preview"][aria-pressed="true"]{background:var(--red);border-color:var(--red)}

/* controls above the map */
.dg-tools{display:grid;gap:10px;margin:6px 0 0}
.chipset{display:flex;flex-wrap:wrap;align-items:center;gap:6px}
.cl{flex:0 0 100%;font:600 0.7rem/1 var(--body);letter-spacing:0.08em;text-transform:uppercase;color:var(--muted);margin:2px 0 0}
.chip{--c:var(--ink);display:inline-flex;align-items:center;gap:7px;font:500 0.82rem/1.2 var(--body);padding:6px 10px;border:1px solid var(--line);border-radius:3px;background:var(--surface);color:var(--ink);cursor:pointer}
.chip:hover{border-color:var(--c)}
.chip[aria-pressed="true"]{background:var(--c);border-color:var(--c);color:var(--surface)}
.chip[data-val="A"]{--c:var(--call)}
.chip[data-val="B"]{--c:var(--pol-line)}
.chip.pk[data-k="pol"]{--c:var(--pol-line)}
.chip.pk[data-k="call"]{--c:var(--call)}
.chip.pk[data-k="red"]{--c:var(--red)}
.sw{display:inline-block;width:18px;height:0;border-top:2.5px solid var(--c)}
.chip[data-k="red"] .sw{border-top-style:dashed}
.chip[aria-pressed="true"] .sw{border-color:var(--surface)}
.dg-sum{font:500 0.85rem/1.4 var(--body);color:var(--muted);margin:0}
.path-note{font-size:0.9rem;margin:0;padding:8px 0 0;border-top:1px solid var(--line);min-height:1.5em}
.path-note:empty{display:none}

/* map and detail panel side by side on a wide screen, stacked on a narrow one */
.dg-layout{display:grid;grid-template-columns:minmax(0,1fr);gap:22px;margin-top:14px;align-items:start}
@media (min-width:1000px){
  .dg-layout{grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:30px}
  .panels{position:sticky;top:58px;max-height:calc(100vh - 72px);overflow:auto;overscroll-behavior:contain}
}
figure.mapfig{margin:0;gap:12px}
.map{position:relative;display:grid;grid-template-columns:16px minmax(0,1fr) 30px minmax(0,1fr) 30px minmax(0,1fr) 36px;row-gap:14px;align-items:stretch}
.map > p{margin:0}
.wires{position:absolute;inset:0;width:100%;height:100%;overflow:visible;pointer-events:none;z-index:0}
.zl{font:600 0.7rem/1.2 var(--body);letter-spacing:0.09em;text-transform:uppercase;align-self:end}
.zl.z-pol,.ch.z-pol{color:var(--pol)}
.zl.z-gw,.ch.z-call{color:var(--call)}
.ch{font:600 0.66rem/1.2 var(--body);letter-spacing:0.07em;text-transform:uppercase;align-self:end;padding-top:12px}
.wl{position:relative;z-index:1;align-self:start;justify-self:center;text-align:center;font:italic 500 0.72rem/1.25 var(--body);color:var(--call);background:var(--bg);padding:2px 4px;margin-top:2px}
.xl{position:relative;z-index:1;align-self:end;text-align:right;font:600 0.72rem/1.25 var(--body);color:var(--red);padding-right:6px}
.bx{--c:var(--call-line);position:relative;z-index:1;display:flex;flex-direction:column;gap:2px;min-height:68px;padding:8px 10px 9px;
  border:1.5px solid var(--c);border-radius:3px;background:var(--surface);color:var(--ink);text-decoration:none;
  transition:opacity .15s,box-shadow .15s}
.bx:hover{color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--c)}
.bx:focus-visible{outline:2px solid var(--c);outline-offset:3px}
.bx[aria-current="true"]{box-shadow:0 0 0 3px var(--bg),0 0 0 5px var(--c)}
.bx.pol{--c:var(--pol-line);background:var(--pol-bg)}
.bx.gw{--c:var(--gw-bg);background:var(--gw-bg);color:var(--gw-ink);justify-content:center;padding:14px 16px}
.bx.gw:hover{color:var(--gw-ink);box-shadow:inset 0 0 0 2px rgba(255,255,255,.35)}
.bx.be{--c:var(--call-line);background:var(--call-bg);border-width:2px;align-items:center;text-align:center;justify-content:center;min-height:62px;margin-top:16px}
.bx.log{--c:var(--log);border-style:dashed}
.bx.pv{--c:var(--red);border-style:dashed;background:repeating-linear-gradient(135deg,var(--hatch) 0 6px,transparent 6px 12px),var(--surface)}
.bt{font:700 0.92rem/1.18 var(--display);overflow-wrap:anywhere}
.bx.gw .bt{font-size:1.3rem}
.bx.be .bt{font-size:1.05rem}
.bs{font:500 0.74rem/1.25 var(--body);color:var(--muted)}
.bc,.bf{font:600 0.68rem/1.2 var(--mono);color:var(--muted);margin-top:auto;padding-top:4px}
.bx.gw .bs,.bx.gw .bc,.bx.gw .bf{color:var(--gw-muted)}
.bx.gw .bc,.bx.gw .bf{margin-top:6px}
.bp{align-self:flex-start;font:600 0.6rem/1.3 var(--mono);text-transform:uppercase;letter-spacing:0.06em;color:var(--red);border:1px solid var(--red);padding:0 4px;margin-bottom:2px;background:var(--surface)}
.bf{display:none;color:var(--ink)}
.filtering .bx .bc{display:none}
.filtering .bx .bf{display:block}
.bx.gw .bf{color:var(--gw-ink)}
.bx.dim,.bx.fade{opacity:.28}
.bx.on{box-shadow:0 0 0 2px var(--bg),0 0 0 4px var(--c)}
/* lines */
.w{fill:none;stroke-width:1.6;stroke-linejoin:round;transition:opacity .15s,stroke-width .15s}
.w.pol{stroke:var(--pol-line)}
.w.call{stroke:var(--call-line);stroke-width:2}
.w.red{stroke:var(--red);stroke-dasharray:6 4}
.w.log{stroke:var(--log);stroke-dasharray:2 4}
.w.dash{stroke-dasharray:6 4}
.w.pv{stroke-dasharray:3 3}
.w.hot{stroke-width:3}
.w.lit{stroke-width:3.2}
.w.fade{opacity:.15}
@media (prefers-reduced-motion:no-preference){
  .w.lit.red,.w.lit.dash,.w.lit.pv{animation:flow 1.8s linear infinite}
}
@keyframes flow{to{stroke-dashoffset:-30}}
.key{display:flex;flex-wrap:wrap;gap:4px 18px;font-size:0.8rem;color:var(--muted);margin:0;padding:0;list-style:none}
.key li{display:flex;align-items:center;gap:7px}
.key i{display:inline-block;width:22px;border-top:2.5px solid}
.key .k-pol{border-color:var(--pol-line)}
.key .k-hand{border-color:var(--pol-line);border-top-style:dashed}
.key .k-call{border-color:var(--call-line)}
.key .k-red{border-color:var(--red);border-top-style:dashed}
.key .k-log{border-color:var(--log);border-top-style:dotted}
@media (max-width:640px){
  .map{grid-template-columns:12px minmax(0,1fr) 18px minmax(0,1fr) 18px minmax(0,1fr) 30px;row-gap:12px}
  .bx{padding:6px 7px 7px;min-height:62px}
  .bt{font-size:0.8rem}
  .bs{font-size:0.68rem}
  .bc,.bf{font-size:0.62rem}
  .bx.gw{padding:10px 12px}
  .bx.gw .bt{font-size:1.1rem}
  .bx.be .bt{font-size:0.95rem}
  .ch{font-size:0.6rem;letter-spacing:0.04em}
  .wl{font-size:0.64rem;padding:1px 2px}
  .xl{font-size:0.66rem}
}

/* detail panel */
.panels{border-top:2px solid var(--rule);background:var(--surface);padding:0 16px 14px}
.pnav{display:none;align-items:center;gap:8px;flex-wrap:wrap;position:sticky;top:0;z-index:2;background:var(--surface);padding:10px 0;border-bottom:1px solid var(--line)}
.js .pnav{display:flex}
.cl-note{margin:6px 0 0;font-size:.86rem;color:var(--muted)}
.flt{display:block}
.flt > summary{cursor:pointer;width:max-content;max-width:100%;font:600 0.7rem/1.2 var(--body);letter-spacing:0.08em;text-transform:uppercase;color:var(--muted);padding:6px 0}
.flt > summary:hover{color:var(--ink)}
.flt-n{margin-left:8px;color:var(--call);letter-spacing:0}
.flt .chipset + .chipset{margin-top:10px}
#map,#details{scroll-margin-top:52px}
@media (max-width:999px){.pnav{top:var(--segh,46px)}}
.np [id]:not(.np){scroll-margin-top:140px}
@media (min-width:1000px){.np [id]:not(.np){scroll-margin-top:68px}}
.pnav button{font:600 0.74rem/1 var(--body);letter-spacing:0.04em;text-transform:uppercase;padding:7px 10px;border:1px solid var(--line);border-radius:3px;background:var(--surface);color:var(--ink);cursor:pointer}
.pnav button:hover{border-color:var(--ink)}
.pnav .pos{font:600 0.72rem/1 var(--mono);color:var(--muted)}
.pnav .back{margin-left:auto;font-size:0.8rem}
@media (min-width:1000px){.pnav .back{display:none}}
.np{--c:var(--call);padding:14px 0 4px}
.np + .np{border-top:1px solid var(--line)}
.js .np + .np{border-top:0}
.np[data-role="pol"]{--c:var(--pol)}
.np[data-role="pv"]{--c:var(--red)}
.np[data-role="log"]{--c:var(--log)}
.np header{display:grid;gap:4px;margin:0 0 4px}
.np header h3{margin:0;font-size:1.45rem;font-weight:750;letter-spacing:-0.012em;line-height:1.1}
.kind{font:600 0.7rem/1 var(--body);letter-spacing:0.08em;text-transform:uppercase;color:var(--c)}
.np h4{font:700 0.98rem/1.35 var(--display);margin:0 0 4px}
.np h4 .tg{margin-left:6px}
.np .rt{font:500 0.76rem/1.3 var(--body);color:var(--muted);margin-top:3px}
.np dl{display:grid;gap:2px;margin:6px 0 0}
.np dt{font:600 0.68rem/1.4 var(--body);letter-spacing:0.07em;text-transform:uppercase;color:var(--muted);margin-top:6px}
.np dd{margin:0;font-size:0.93rem}
.ctl,.part{padding:14px 0 12px;border-top:1px solid var(--line)}
.np header + .ctl,.np header + .part{border-top:2px solid var(--rule)}
.np .part{margin-top:28px}
.np header + .part{margin-top:14px}
.ctl.off{opacity:.3}
.ctl::before{content:"Control";display:block;font:600 0.66rem/1 var(--mono);letter-spacing:0.09em;text-transform:uppercase;color:var(--muted);margin-bottom:6px}
.js .np{display:none}
.js .np.sel{display:block}
.np .q-note{margin-top:12px}

/* approval workflow */
.wf-lane{--c:var(--pol-line);margin:16px 0 0}
.wf-lane[data-wf="a365"]{--c:var(--red)}
.wf-lane h4{margin:0 0 6px;font:700 0.95rem/1.35 var(--display)}
.wf-steps{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 8px}
.wf-steps button{font:500 0.82rem/1.25 var(--body);text-align:left;padding:7px 10px;border:1px solid var(--c);border-radius:3px;background:var(--surface);color:var(--ink);cursor:pointer}
.wf-steps button:hover{box-shadow:inset 0 0 0 1px var(--c)}
.wf-steps button[aria-pressed="true"]{background:var(--c);color:var(--surface)}
.wf-detail{padding:10px 12px;border:1px solid var(--c);border-radius:3px;background:var(--surface)}
.wf-detail p{margin:0}
.js .wf-detail{display:none}
.js .wf-detail.sel{display:block}

/* tables stack into label and value pairs on a phone */
.tbl{background:var(--surface)}
.tbl td[data-label="Expected result"]{color:var(--ink)}
@media (max-width:640px){
  .tbl-wrap{overflow:visible}
  .tbl{min-width:0;background:none}
  .tbl thead{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
  .tbl tr{display:block;padding:10px 0;border-top:1px solid var(--line)}
  .tbl tbody tr:first-child{border-top:0}
  .tbl td{display:grid;grid-template-columns:7.2rem minmax(0,1fr);gap:10px;border:0;padding:2px 0!important}
  .tbl td::before{content:attr(data-label);font:600 0.66rem/1.6 var(--body);letter-spacing:0.07em;text-transform:uppercase;color:var(--muted)}
  .tbl td:first-child{display:block;padding-bottom:4px!important}
  .tbl td:first-child::before{content:none}
}
.steps li::marker{color:var(--call);font-weight:700}
.sh h2 + .goal{margin-top:14px}
.sh .goal{position:relative;padding-left:7rem;margin:0 0 10px;line-height:1.65;font-size:0.97rem}
.sh .goal b{position:absolute;left:0;top:0.32em;margin:0;font:600 0.68rem/1.6 var(--body);letter-spacing:0.08em;text-transform:uppercase;color:var(--ink)}
@media (max-width:560px){
  .sh .goal{padding-left:0;margin-bottom:14px}
  .sh .goal b{position:static;display:block;margin-bottom:2px}
}
@media print{.dg-tools,.pnav,.wires{display:none}.np{display:block!important}.panels{position:static;max-height:none}}
</style>""")

def js_data(obj):
    return json.dumps(obj, ensure_ascii=False).replace("</", "<\\/")


MAP_DATA = js_data(dict(
    order=[n["id"] for n in NODES],
    preview=[n["id"] for n in NODES if n["preview"]],
    edges=[{k: e[k] for k in ("id", "a", "b", "k", "r", "paths")} | {"view": e.get("view", "")} for e in EDGES],
    paths={p["id"]: dict(nodes=p["nodes"], nodes_pv=p.get("nodes_pv", []), note=p["note"],
                         note_pv=p.get("note_pv", p["note"]), preview=p.get("preview", False)) for p in PATHS},
))

SCRIPT = """<script>
(function(){
  var body = document.body;
  body.classList.add('js');
  var h0 = location.hash;
  if(/^#ev-V\\d+$/.test(h0)){ location.replace('@@FACT@@' + h0); return; }
  var D = @@DATA@@;
  var btns = document.querySelectorAll('[data-view-btn]');
  var grid = document.getElementById('mapGrid');
  var wide = window.matchMedia('(min-width:1000px)');
  var seg = document.querySelector('.seg-wrap');
  function segH(){ if(seg){ document.documentElement.style.setProperty('--segh', seg.offsetHeight + 'px'); } }
  segH();
  window.addEventListener('resize', segH);
  var still = window.matchMedia('(prefers-reduced-motion: reduce)');
  var cur = null, hover = null, path = null;
  var objSel = {}, laySel = {};
  function view(){ return body.getAttribute('data-view'); }
  function urlFor(o, hash){
    var u = new URL(location.href);
    if(o === 'safe'){ u.searchParams.delete('path'); } else { u.searchParams.set('path', o); }
    return u.pathname + u.search + (hash === undefined ? u.hash : hash);
  }
  function visibleOrder(){
    return D.order.filter(function(id){ return view() === 'preview' || D.preview.indexOf(id) < 0; });
  }

  /* lines between boxes, drawn from where the boxes are */
  var NS = 'http://www.w3.org/2000/svg';
  var svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('class', 'wires');
  svg.setAttribute('aria-hidden', 'true');
  var marks = {pol:'var(--pol-line)', call:'var(--call-line)', red:'var(--red)'};
  var defs = '<defs>';
  Object.keys(marks).forEach(function(k){
    defs += '<marker id="mk-' + k + '" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto-start-reverse">'
         + '<path d="M0 0 L10 5 L0 10 z" style="fill:' + marks[k] + '"/></marker>';
  });
  defs += '<marker id="mk-x" viewBox="0 0 12 12" refX="6" refY="6" markerWidth="11" markerHeight="11" orient="0" markerUnits="userSpaceOnUse">'
       + '<path d="M1 1 L11 11 M11 1 L1 11" style="stroke:var(--red);stroke-width:2.4;fill:none"/></marker></defs>';
  svg.innerHTML = defs + '<g></g>';
  var layer = svg.lastChild;
  grid.insertBefore(svg, grid.firstChild);
  var lines = [];
  function R(el){
    if(!el || !el.offsetParent) return null;
    var r = el.getBoundingClientRect(), g = grid.getBoundingClientRect();
    var o = {l:r.left - g.left, r:r.right - g.left, t:r.top - g.top, b:r.bottom - g.top};
    o.cx = (o.l + o.r) / 2; o.cy = (o.t + o.b) / 2;
    return o;
  }
  function box(id){ return R(document.getElementById('b-' + id)); }
  function f(n){ return Math.round(n * 10) / 10; }
  function route(e){
    var a = box(e.a), b = box(e.b);
    if(!a || !b) return null;
    var tr = R(grid.querySelector('.g-trunk')), rl = R(grid.querySelector('.g-rail'));
    var tx = tr ? tr.cx : a.l - 8, rx = rl ? rl.l + 12 : a.r + 12, zx = rl ? rl.r - 8 : a.r + 24;
    switch(e.r){
      case 'h': return 'M' + f(a.r) + ' ' + f(a.cy) + ' H' + f(b.l - 1);
      case 'v':
        var x = (Math.max(a.l, b.l) + Math.min(a.r, b.r)) / 2;
        return 'M' + f(x) + ' ' + f(a.b) + ' V' + f(b.t - 1);
      case 'trunk':
        var yb = a.b + 10;
        return 'M' + f(a.l + 18) + ' ' + f(a.b) + ' V' + f(yb) + ' H' + f(tx) + ' V' + f(b.cy);
      case 'branch': return 'M' + f(tx) + ' ' + f(b.cy) + ' H' + f(b.l - 1);
      case 'rail': return 'M' + f(a.r) + ' ' + f(a.cy) + ' H' + f(rx) + ' V' + f(b.cy) + ' H' + f(b.r + 1);
      case 'blocked': return 'M' + f(rx) + ' ' + f(a.cy) + ' H' + f(zx) + ' V' + f(b.t - 7);
    }
    return null;
  }
  function draw(){
    layer.textContent = '';
    lines = [];
    D.edges.forEach(function(e){
      if(e.view && e.view !== view()) return;
      var d = route(e);
      if(!d) return;
      var p = document.createElementNS(NS, 'path');
      p.setAttribute('d', d);
      p.setAttribute('class', 'w ' + e.k + (e.view === 'preview' ? ' pv' : ''));
      var k = e.k.split(' ')[0];
      if(e.r === 'blocked'){ p.setAttribute('marker-end', 'url(#mk-x)'); }
      else if(k !== 'log' && e.r !== 'trunk'){ p.setAttribute('marker-end', 'url(#mk-' + k + ')'); }
      p.__e = e;
      layer.appendChild(p);
      lines.push(p);
    });
    paint();
  }
  function pathNodes(){
    if(!path) return null;
    var p = D.paths[path];
    return p.nodes.concat(view() === 'preview' ? p.nodes_pv : []);
  }
  function paint(){
    var hot = hover || cur, pn = pathNodes();
    var top = [];
    lines.forEach(function(p){
      var e = p.__e;
      var lit = !!path && e.paths.indexOf(path) >= 0;
      var h = !path && !!hot && (e.a === hot || e.b === hot);
      p.classList.toggle('lit', lit);
      p.classList.toggle('hot', h);
      p.classList.toggle('fade', !!path && !lit);
      if(lit || h) top.push(p);
    });
    top.forEach(function(p){ layer.appendChild(p); });
    grid.querySelectorAll('.bx').forEach(function(b){
      var id = b.getAttribute('data-node');
      b.classList.toggle('on', !!pn && pn.indexOf(id) >= 0);
      b.classList.toggle('fade', !!pn && pn.indexOf(id) < 0);
    });
  }
  var queued = false;
  function redraw(){ if(queued) return; queued = true; requestAnimationFrame(function(){ queued = false; draw(); }); }
  if('ResizeObserver' in window){ new ResizeObserver(redraw).observe(grid); } else { window.addEventListener('resize', redraw); }
  if(document.fonts && document.fonts.ready){ document.fonts.ready.then(redraw); }

  /* selecting a box shows its panel */
  var pos = document.getElementById('pPos');
  function select(id, how){
    var p = document.getElementById('n-' + id);
    if(!p) return;
    cur = id;
    document.querySelectorAll('.np').forEach(function(x){ x.classList.toggle('sel', x === p); });
    grid.querySelectorAll('.bx').forEach(function(x){
      if(x.getAttribute('data-node') === id){ x.setAttribute('aria-current', 'true'); } else { x.removeAttribute('aria-current'); }
    });
    var ord = visibleOrder();
    if(pos){ pos.textContent = (ord.indexOf(id) + 1) + ' of ' + ord.length; }
    var panels = document.getElementById('details');
    if(panels && wide.matches){ panels.scrollTop = 0; }
    if(how === 'tap' && !wide.matches){
      document.getElementById('details').scrollIntoView({behavior: still.matches ? 'auto' : 'smooth', block:'start'});
    }
    if(how === 'tap' || how === 'step'){ try{ history.replaceState(null, '', urlFor(view(), '#n-' + id)); }catch(e){} }
    paint();
  }
  function step(d){
    var ord = visibleOrder(), i = ord.indexOf(cur);
    var id = ord[(i + d + ord.length) % ord.length];
    select(id, 'step');
    if(!wide.matches){
      var nav = document.getElementById('details');
      if(nav.getBoundingClientRect().top < 0){ nav.scrollIntoView({block:'start'}); }
    }
  }
  document.querySelectorAll('[data-step-by]').forEach(function(b){
    b.addEventListener('click', function(){ step(+b.getAttribute('data-step-by')); });
  });
  grid.querySelectorAll('.bx').forEach(function(b){
    var id = b.getAttribute('data-node');
    b.addEventListener('click', function(e){ e.preventDefault(); select(id, 'tap'); });
    b.addEventListener('mouseenter', function(){ hover = id; paint(); });
    b.addEventListener('mouseleave', function(){ hover = null; paint(); });
    b.addEventListener('focus', function(){ hover = id; paint(); });
    b.addEventListener('blur', function(){ hover = null; paint(); });
  });

  /* follow a path */
  var note = document.getElementById('pathNote');
  function setPath(id){
    path = id;
    document.querySelectorAll('.chip.pk').forEach(function(c){ c.setAttribute('aria-pressed', c.getAttribute('data-path') === id ? 'true' : 'false'); });
    if(note){ note.innerHTML = id ? (view() === 'preview' ? D.paths[id].note_pv : D.paths[id].note) : ''; }
    paint();
  }
  document.querySelectorAll('.chip.pk').forEach(function(c){
    c.addEventListener('click', function(){ var id = c.getAttribute('data-path'); setPath(path === id ? null : id); });
  });

  /* filters */
  function anySel(s){ return Object.keys(s).some(function(k){ return s[k]; }); }
  function hit(el){
    var ok = true;
    if(anySel(objSel)){ ok = ok && (el.getAttribute('data-obj') || '').split(' ').some(function(v){ return objSel[v]; }); }
    if(anySel(laySel)){ ok = ok && (el.getAttribute('data-layer') || '').split(' ').some(function(v){ return laySel[v]; }); }
    return ok;
  }
  function filter(){
    var active = anySel(objSel) || anySel(laySel);
    var safe = view() === 'safe';
    var shown = 0, total = 0, nb = 0;
    grid.classList.toggle('filtering', active);
    document.querySelectorAll('.np').forEach(function(p){
      if(safe && p.classList.contains('view-preview')) return;
      nb++;
      var k = 0, n = 0;
      p.querySelectorAll('.ctl').forEach(function(c){
        var vis = !(safe && c.classList.contains('view-preview'));
        var m = !active || hit(c);
        c.classList.toggle('off', active && !m);
        if(vis){ n++; total++; if(m){ k++; shown++; } }
      });
      var b = document.getElementById('b-' + p.getAttribute('data-node'));
      if(b){
        b.classList.toggle('dim', active && k === 0);
        b.querySelector('.bf').textContent = n ? (k + ' of ' + n + ' match') : 'No controls';
      }
    });
    var fn = document.getElementById('fltN');
    if(fn){
      var on = document.querySelectorAll('.chip[data-grp][aria-pressed="true"]').length;
      fn.textContent = on ? ('(' + on + ' on)') : '';
    }
    var s = document.getElementById('dgSum');
    var gaps = {'3': 'Layer 3: this review established no released content guardrail for Foundry or Copilot Studio agents.',
                '6': 'Layer 6: the reviewed Foundry content guardrails are preview; MCP coverage is not established.'};
    var gapTxt = Object.keys(gaps).filter(function(k){ return laySel[k]; }).map(function(k){ return ' ' + gaps[k]; }).join('');
    if(s){ s.textContent = active ? (shown + ' of ' + total + ' controls match. Boxes without a match are dimmed.' + gapTxt) : (total + ' controls in ' + nb + ' boxes.'); }
  }
  /* on phones the filters start folded so the map follows the path chips */
  var flt = document.querySelector('.flt');
  if(flt && window.matchMedia('(max-width:640px)').matches){ flt.open = false; }
  document.querySelectorAll('.chip[data-grp]').forEach(function(ch){
    ch.addEventListener('click', function(){
      var g = ch.getAttribute('data-grp'), v = ch.getAttribute('data-val');
      var s = g === 'obj' ? objSel : laySel;
      s[v] = !s[v];
      ch.setAttribute('aria-pressed', s[v] ? 'true' : 'false');
      filter();
    });
  });

  /* design switch */
  function setView(o, keepUrl){
    body.setAttribute('data-view', o);
    btns.forEach(function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-view-btn') === o ? 'true' : 'false'); });
    if(!keepUrl){ try{ history.replaceState(null, '', urlFor(o)); }catch(e){} }
    if(o === 'safe' && cur && D.preview.indexOf(cur) >= 0){ select('gw'); }
    if(path && D.paths[path].preview && o === 'safe'){ setPath(null); } else if(path){ setPath(path); }
    if(cur){ select(cur); }
    filter();
    draw();
  }

  /* workflow steps */
  document.querySelectorAll('[data-wf]').forEach(function(wrap){
    var bs = wrap.querySelectorAll('.wf-steps button');
    var ds = wrap.querySelectorAll('.wf-detail');
    function pick(id){
      bs.forEach(function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-step') === id ? 'true' : 'false'); });
      ds.forEach(function(d){ d.classList.toggle('sel', d.getAttribute('data-step') === id); });
    }
    bs.forEach(function(b){ b.addEventListener('click', function(){ pick(b.getAttribute('data-step')); }); });
    pick(bs[0].getAttribute('data-step'));
  });
  function followHash(){
    var id = location.hash.slice(1);
    if(!id) return;
    try{ id = decodeURIComponent(id); }catch(e){}
    var el = document.getElementById(id);
    if(!el) return;
    var other = view() === 'safe' ? 'preview' : 'safe';
    if(el.closest('.view-' + other)){ setView(other); }
    var np = el.closest('.np');
    if(np){ select(np.getAttribute('data-node')); }
    if(np && el === np){
      document.getElementById(wide.matches ? 'map' : 'details').scrollIntoView({behavior:'instant'});
      return;
    }
    el.scrollIntoView({behavior:'instant'});
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){ setView(b.getAttribute('data-view-btn')); }); });
  document.querySelectorAll('[data-view-go]').forEach(function(a){ a.addEventListener('click', function(){ setView(a.getAttribute('data-view-go')); }); });
  var m = /[?&]path=(safe|preview)(?:&|$)/.exec(location.search);
  select('gw');
  setView(m ? m[1] : 'safe', true);
  followHash();
  window.addEventListener('hashchange', followHash);
  window.addEventListener('load', function(){ draw(); if(location.hash) followHash(); });
  if('IntersectionObserver' in window){
    var links = {};
    document.querySelectorAll('.toc a').forEach(function(a){ links[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        Object.keys(links).forEach(function(k){ links[k].classList.remove('on'); links[k].removeAttribute('aria-current'); });
        var a = links[e.target.id];
        if(a){ a.classList.add('on'); a.setAttribute('aria-current','location'); }
      });
    }, {rootMargin:'-20% 0px -70% 0px'});
    Object.keys(links).forEach(function(k){ var t = document.getElementById(k); if(t) io.observe(t); });
  }
})();
</script>""".replace("@@FACT@@", FACTCHECK_URL).replace("@@DATA@@", MAP_DATA)

MAST = f"""
  <a class="skip" href="#main-content">Skip to content</a>
  <header class="mast">
    <div class="meta"><span>Design · Microsoft stack · MCP</span><span>Documentation checked {CHECKED}</span></div>
    <h1>A proposed design for MCP Governance in a Microsoft ecosystem</h1>
    <p class="lead"><a href="mcp-governance-stride.html">Read the threat model for this design</a></p>
  </header>

  <nav class="toc" aria-label="Contents">
    <ul>
      <li><a href="#design">Design</a></li>
      <li><a href="#rollout">Rollout</a></li>
      <li><a href="#gaps">Gaps</a></li>
      <li class="view-preview"><a href="#preview">With preview</a></li>
      <li><a href="mcp-governance-stride.html">Threat model</a></li>
    </ul>
    <div class="seg-wrap"><span class="seg-lbl" id="seg-lbl">Select design</span>
    <div class="seg" role="group" aria-labelledby="seg-lbl">
      <button type="button" data-view-btn="safe" aria-pressed="true">Released only</button>
      <button type="button" data-view-btn="preview" aria-pressed="false">With preview</button>
    </div></div>
  </nav>
"""

KEY = ('<ul class="key" aria-label="Line key">'
       '<li><i class="k-pol"></i>Approved list</li>'
       '<li><i class="k-hand"></i>Set by hand</li>'
       '<li><i class="k-call"></i>Call to the company server</li>'
       '<li><i class="k-red"></i>Blocked or preview route</li>'
       '<li><i class="k-log"></i>Logging</li></ul>')

DESIGN = f"""
  <section class="sec" id="design" aria-labelledby="h-design">
    <header class="sh"><h2 id="h-design">The design</h2>
    <p class="goal"><b>In short</b>Keep the company MCP server behind the gateway and limit managed clients to approved servers. Map the approved inventory into each policy target, because visibility alone does not enforce access.&nbsp;{REC}</p><p class="goal"><b>Coverage</b><a href="#gaps">Gaps</a> limit Objective B; a gateway does not govern every client or external MCP server by itself.</p>
    <p class="goal view-safe"><b>Scope</b>This is the released-only design. It uses supported MCP capabilities in the API Management service, subject to tier availability. Preview features are in the other design: select With preview above, or read <a href="#preview">With preview</a>.</p>
    <p class="goal view-preview"><b>Scope</b>This design replaces the API Management service gateway with the separate AI Gateway product, which is in public preview, and adds the Agent 365 integration. Use it only in a sandbox. The released-only design stays underneath. Details and limits are in <a href="#preview">With preview</a>.</p>
    <p class="goal"><b>Objectives</b>A means company backend access through the gateway only. B means restricting managed clients to approved MCP servers.</p></header>
    <div class="dg-tools">
      <div class="chipset" role="group" aria-label="Follow a path"><span class="cl">Follow a path</span>{path_buttons()}</div>
      <p class="path-note" id="pathNote" aria-live="polite"></p>
      {chips_html()}
      <p class="dg-sum" id="dgSum" aria-live="polite"></p>
    </div>
    <div class="dg-layout">
      <figure class="mapfig" id="map" aria-describedby="figDesc">
{map_html()}
        {KEY}
        <figcaption class="view-preview">Hatched boxes and the lines that touch them are what preview adds. Everything else is the released design.</figcaption>
        <div class="vh" id="figDesc">{"".join(f"<p>{esc(s)}</p>" for s in re.split(r"(?<=[.]) (?=Every client|A direct call|In the preview)", DESC_FIG))}</div>
      </figure>
      <div class="panels" id="details">
        <div class="pnav"><button type="button" data-step-by="-1">Previous</button><span class="pos" id="pPos"></span><button type="button" data-step-by="1">Next</button><a class="back" href="#map">Back to diagram</a></div>
{"".join(panel(n) for n in NODES)}
      </div>
    </div>
  </section>
"""

# ---- preview section -----------------------------------------------------
def cut_block(start, end):
    i = PREVIEW_HTML.index(start)
    j = PREVIEW_HTML.index(end, i)
    return strip_anchors(PREVIEW_HTML[i:j])


pv_header = PREVIEW_HTML[PREVIEW_HTML.index('<header class="sh">'):PREVIEW_HTML.index("</header>") + 9]
pv_notes = re.findall(r'<p class="q-note">(Dedicated AI Gateway.*?)</p>|<p class="q-note">(Microsoft says preview features.*?)</p>', pv_block, re.S)
pv_notes = "".join(f'<p class="q-note">{a or b}</p>' for a, b in pv_notes)
pv_notes = pv_notes.replace(" Every row below is a preview feature and its requirement is a recommendation.", " Every preview control in the diagram is a preview feature and its requirement is a recommendation.")
if "Every preview control in the diagram" not in pv_notes:
    sys.exit("preview note wording changed in the shared builder")

WF_STEPS = [
    ("gov", "Company governance", [
        ("g1", "1 Requester adds the server to Git", "A requester adds the server, owner, sign-in, tools and risk class to the reviewed inventory in Git."),
        ("g2", "2 Security review", "Security reviews the server and each of its tools."),
        ("g3", "3a Approve and merge", "Approval merges the change into the inventory. The pipeline then applies it to the policy targets."),
        ("g4", "3b Deny and stop", "Denial records the reason in Git and stops the request."),
    ]),
    ("a365", "Agent 365 route, preview", [
        ("a1", "4 Developer registers the server", "For the separate BYO pilot, register the test endpoint after internal approval. Do not register direct access to the private company backend."),
        ("a2", "5 Admin reviews the request", "An AI Administrator or Global Administrator reviews the server name, publisher, requester, request date, server information and declared tools under Agents &gt; Tools &gt; Requests (preview). "
               f"{ev('a365-tools-role-ai', 'a365-tools-role-global', 'review-req-fields', 'review-req-info')} {evp('pv-byo-approval')} Individual tool controls are rolling out for supported Agent 365 servers. BYO server tool-level blocking is planned. Until then, block at server level and authorize at the gateway and backend. {ev('a365-tools-granular')} {evp('pv-byo-roll', 'pv-a365-ctrl')}"),
        ("a3", "6a Approve, consent, available", f"Approval makes the server available in the organizational registry. It becomes available to agent-building surfaces only after Microsoft Entra tenant consent. {ev('a365-tools-approve', 'a365-tools-consent')} {evp('pv-byo-approval')} Then apply target policies and backend authorization."),
        ("a4", "6b Reject", "Rejection leaves the server unavailable. Record the reason in Git."),
        ("a5", "7 Later deny", f"Mark the server denied in Git; the pipeline removes it from its targets. In the Microsoft 365 admin center, block it in the registry and remove its connector by hand. Verify that calls are denied. {REC}"),
    ]),
]


def workflow_html():
    out = []
    for key, title, steps in WF_STEPS:
        btns = "".join(f'<button type="button" data-step="{sid}" aria-pressed="false">{label}</button>' for sid, label, _ in steps)
        det = "".join(f'<div class="wf-detail" data-step="{sid}"><p>{text}</p></div>' for sid, _, text in steps)
        out.append(f'<div class="wf-lane" data-wf="{key}"><h4>{title}</h4><div class="wf-steps">{btns}</div>{det}</div>')
    return "".join(out)


PREVIEW = f"""
  <section class="sec view-preview" id="preview" aria-labelledby="h-preview">
    {pv_header}
    {pv_notes}
    <div class="sub3" id="approval-workflow">
      <h3>Approval and denial workflow</h3>
      <p>Use two gates: the company's reviewed inventory change, then Microsoft's tenant approval for the preview Agent 365 server route. An approval in one gate does not replace the other. {REC}</p>
      {workflow_html()}
      <p class="q-note">The Git pull request is the internal source-of-truth decision. The Microsoft 365 admin-center request is a separate product approval for the preview BYO route. Rejecting either stops rollout. This is the MCP server request queue {ev('a365-tools-tabs', 'review-req-queue')}. </p><p class="q-note">Approval of an agent publication is a separate workflow. The All agents registry is an inventory view; its Data &amp; tools details are read-only and may be missing for some agents. {ev('a365-agent-approve', 'a365-agent-request-review', 'a365-agent-readonly', 'a365-agent-incomplete')} These are distinct admin pages: Agents &gt; All agents &gt; Registry, and Agents &gt; Tools &gt; Registry or Requests (preview). {ev('a365-agent-all', 'a365-tools-tabs', 'a365-tools-status')}</p>
    </div>
    {cut_block('<div class="sub3" id="preview-tests">', '<div class="sub3" id="pilot">')}
    {cut_block('<div class="sub3" id="pilot">', '<span id="fallback">')}
  </section>
"""

FOOTER = f"""
  <footer>
    <p class="ai-note"><b>Made with AI</b><span>This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human. <span id="evidence">Sources and review notes: <a href="{FACTCHECK_URL}">fact check</a>.</span></span></p>
    <section class="tag-key" id="tag-key"><h2 id="h-tag-key"><a class="sec-link" href="#tag-key">Tags on this page</a></h2>
      <dl>
        <dt><span class="tg i">inference</span></dt><dd>Interpretation by AI. It is not stated in a source.</dd>
        <dt><span class="tg u">unverified</span></dt><dd>Not confirmed in a quoted source.</dd>
        <dt><span class="tg r">recommendation</span></dt><dd>A design choice proposed on this page, not documented Microsoft or GitHub behavior.</dd>
        <dt><span class="tg pv">preview</span></dt><dd>The feature is in preview. Use it for a sandbox pilot only.</dd>
      </dl>
    </section>
  </footer>
"""

ROLLOUT_HTML = strip_anchors(ROLLOUT)
GAPS_HTML = strip_anchors(GAPS)
_gap_split = ". Two switches are untested:"
assert GAPS_HTML.count(_gap_split) == 1
_a = GAPS_HTML.index('<li><strong id="gap-github-builtin">')
_b = GAPS_HTML.index("</li>", _a)
_li = GAPS_HTML[_a:_b].replace(_gap_split, ".</p><p>Two switches are untested:", 1)
GAPS_HTML = GAPS_HTML[:_a] + _li.replace('<li><strong id="gap-github-builtin">', '<li><p><strong id="gap-github-builtin">', 1) + "</p>" + GAPS_HTML[_b:]

def stack_tables(src):
    """Label each table cell with its column head, so narrow screens can stack rows."""
    def one(m):
        t = m.group(0)
        heads = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<th\b[^>]*>(.*?)</th>", t, re.S)]
        if not heads:
            return t
        def row(r):
            i = iter(range(10 ** 6))
            return re.sub(r"<td\b", lambda _m: f'<td data-label="{html.escape(heads[min(next(i), len(heads) - 1)])}"', r.group(0))
        return re.sub(r"<tr\b.*?</tr>", row, t, flags=re.S)
    return re.sub(r"<table\b.*?</table>", one, src, flags=re.S)


_extra_tests = [
    ("Clear publisher defaults, enable one approved Microsoft 365 connector and check an unapproved connector", "Only the individually approved connector is available within User access; review existing overrides", "B"),
    ("Repeat a Microsoft 365 write tool after one-time, conversation and saved approval", "Confirmation follows the selected approval scope; backend authorization still applies to every action", "A and B"),
    ("Use a valid token with the wrong audience, tenant or caller permission", "Rejected before backend execution", "A"),
    ("A read-only caller requests a write tool through the shared gateway identity", "Denied by caller-specific authorization", "A"),
    ("Switch accounts or start a client without cached server policy", "Required device policy remains enforced; verify each supported client", "B"),
    ("Change custom agent profiles, use a cloud session or call through a shell tool", "Document exclusions; prove separate client and egress controls before claiming coverage", "B"),
    ("Try an unapproved MCP destination from each Foundry and Copilot Studio path", "Blocked by the configured network or connector policy, or recorded as an unresolved gap", "B"),
    ("Deny a company MCP server while a client has stale policy or an active session", "Company gateway and backend reject new calls; automated targets update after refresh, and manual targets need recorded administrator changes", "A and B"),
    ("Check custom and HTTP connector restrictions while ACP is enabled", "Mixed mode retains the required classic policy blocks", "B"),
    ("Send one tool call and inspect gateway, backend and Purview records", "Caller and request correlate where supported; secrets are redacted and access is restricted", "A and B"),
]
_test_rows = "".join("<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>" for row in _extra_tests)
assert ROLLOUT_HTML.count("</tbody>") == 1
ROLLOUT_HTML = ROLLOUT_HTML.replace("</tbody>", _test_rows + "</tbody>")
ROLLOUT_HTML = stack_tables(ROLLOUT_HTML)
_preview_extra_tests = [
    ("Initialize a session and list tools with tool threat protection enabled", "These operations are not evaluated by this policy", "Separate authentication and server/metadata review"),
    ("Withhold the result of a completed controlled write", "No automatic retry; verify whether the action completed", "Post-invocation denial cannot reverse side effects"),
]
_preview_rows = "".join("<tr>" + "".join(f"<td>{v}</td>" for v in row) + "</tr>" for row in _preview_extra_tests)
assert PREVIEW.count("</tbody>") == 1
PREVIEW = PREVIEW.replace("</tbody>", _preview_rows + "</tbody>")
PREVIEW = stack_tables(PREVIEW)

BODY = f"""{HEAD}{STYLE}
{EXTRA_CSS}
</head>
<body data-view="safe">{MARKERS}<div class="page" id="top">
{MAST}
  <main id="main-content" tabindex="-1">
{DESIGN}{ROLLOUT_HTML}{GAPS_HTML}{PREVIEW}
  </main>
{FOOTER}
</div>

{SCRIPT}
</body>
</html>
"""

for ch in (chr(0x2014), chr(0x2013)):
    if ch in BODY:
        i = BODY.index(ch)
        sys.exit(f"em or en dash in output near {BODY[max(0, i - 60):i + 20]!r}")

from mcp_governance_interactive_edits import EDITS  # noqa: E402

FINAL = add_anchors(BODY)
for _old, _new in EDITS:
    if FINAL.count(_old) != 1:
        sys.exit(f"page edit does not apply exactly once: {_old[:80]!r}")
    FINAL = FINAL.replace(_old, _new)
from mcp_governance_interactive_review import apply_review
FINAL = apply_review(FINAL, ev, REC, INF, UNV, evp)

for ch in (chr(0x2014), chr(0x2013)):
    if ch in FINAL:
        i = FINAL.index(ch)
        sys.exit(f"em or en dash in final page near {FINAL[max(0, i - 60):i + 20]!r}")
OUT.write_text(FINAL, encoding="utf-8")
print(f"wrote {OUT.name}, {len(FINAL.splitlines())} lines, {len(CONTROLS)} controls on {len(NODES)} boxes")

# ---- quote table in the fact check file ----------------------------------
QUOTES_BEGIN, QUOTES_END = "<!-- Begin source quotes -->", "<!-- End source quotes -->"
_unavailable = set(interactive_evidence.UNAVAILABLE)
PREVIEW_COUNT = len(PREVIEW_ONLY - _unavailable)
SAFE_COUNT = len(QUOTES) - PREVIEW_COUNT - len(_unavailable)


def md_cell(text):
    text = html.escape(text, quote=False)
    for a, b in (("|", "&#124;"), ("*", "&#42;"), ("_", "&#95;"), ("`", "&#96;"), ("[", "&#91;"), ("]", "&#93;")):
        text = text.replace(a, b)
    return text


def md_url(url):
    return url.replace("(", "%28").replace(")", "%29").replace("|", "%7C").replace(" ", "%20")


rows = []
for key, skey, q in QUOTES:
    title, url, date = SOURCES[skey]
    where = "unverified: source unavailable" if key in _unavailable else "preview" if key in PREVIEW_ONLY else "released"
    rows.append(f'| <a id="ev-{IDS[key]}"></a>{IDS[key]} | {md_cell(q)} | [{md_cell(title)}]({md_url(url + frag(q))}) | {date or "not captured in review"} | {where} |')
table = (f"{QUOTES_BEGIN}\nGenerated by `scripts/build-mcp-governance-interactive.py` from the shared quote list. Do not edit by hand. "
         f"{len(QUOTES)} quotes, checked {CHECKED}: {SAFE_COUNT} back the released-only design and {PREVIEW_COUNT} back the preview additions" + (f"; {len(_unavailable)} unverified because the source was unavailable" if _unavailable else "") + ". "
         "Links request the quoted passage with browser text fragments. Page date is the date the source page shows.\n\n"
         "| Id | Quote | Source | Page date | Design |\n|---|---|---|---|---|\n" + "\n".join(rows) + f"\n{QUOTES_END}")
notes = NOTES.read_text(encoding="utf-8")
if QUOTES_BEGIN not in notes or QUOTES_END not in notes:
    sys.exit(f"{NOTES.name} has no quote markers")
head, rest = notes.split(QUOTES_BEGIN, 1)
tail = rest.split(QUOTES_END, 1)[1]
if head + table + tail != notes:
    NOTES.write_text(head + table + tail, encoding="utf-8")
    print(f"updated the quote table in {NOTES.name}")

for m in re.finditer(r"<(p|dd|td|li)\b[^>]*>(.*?)</\1>", FINAL, re.S):
    if m.group(1) == "li" and "<p" in m.group(2):
        continue
    words = len(re.sub(r"<[^>]+>", " ", m.group(2)).split())
    if words > 60:
        print(f"WARN {words} words: {re.sub(r'<[^>]+>', ' ', m.group(2))[:70]!r}")
defined = set(re.findall(r'\bid="([^"]+)"', FINAL))
for t in sorted(set(re.findall(r'href="#([^"]+)"', FINAL)) - defined):
    print(f"WARN dead anchor #{t}")
