"""Build the STRIDE and DREAD model files for the interactive MCP governance page.

  python3 -I scripts/build-mcp-stride.py

Writes mcp-governance-stride.drawio (3 pages), mcp-governance-stride.threats.tsv and
mcp-governance-stride.dfd.xml (page 1 alone, for a quick draw.io paste).
Fails if a STRIDE-per-element cell has no threat, a page id does not exist, or a dash slipped in.
"""

import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mcp_stride_data import (APPLIES, ELEMENTS, NOT_APPLICABLE, OUTSIDE, SC500, STRIDE,
                             THREATS, OBSERVED, adjust, dread_score, level_of, rating)

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "mcp-governance-microsoft-interactive.html"
BASE = "mcp-governance-stride"


def check():
    errs = []
    ids = set(re.findall(r'id="((?:ctrl|gap|n)-[a-z0-9-]+)"', PAGE.read_text()))
    seen = {}
    for i, t in enumerate(THREATS):
        el, cat, text, ctrls, sc, dr, basis = t
        if el not in ELEMENTS:
            errs.append(f"unknown element {el}")
            continue
        if cat not in APPLIES[ELEMENTS[el][0]]:
            errs.append(f"{el} {cat}: category does not apply to {ELEMENTS[el][0]}")
        for c in ctrls:
            if c not in ids:
                errs.append(f"{el} {cat}: page id missing: {c}")
        for s in sc:
            if s != OUTSIDE and s not in SC500:
                errs.append(f"{el} {cat}: unknown SC-500 code {s}")
        if len(dr) != 5 or not all(1 <= x <= 10 for x in dr):
            errs.append(f"{el} {cat}: bad DREAD {dr}")
        seen.setdefault((el, cat), []).append(i)
    for el, (kind, _) in ELEMENTS.items():
        for cat in APPLIES[kind]:
            if (el, cat) not in seen and (el, cat) not in NOT_APPLICABLE:
                errs.append(f"gap: {el} {cat} has no threat")
    blob = repr((THREATS, ELEMENTS, SC500))
    if "—" in blob or "–" in blob:
        errs.append("em or en dash in data")
    if errs:
        print("\n".join(errs))
        sys.exit(1)


def numbered():
    """Threat id = STRIDE letter plus a count in element order: S1, S2, T1 and so on."""
    per_cat, out = {}, []
    for t in THREATS:
        per_cat[t[1]] = per_cat.get(t[1], 0) + 1
        tid = f"{t[1]}{per_cat[t[1]]}"
        out.append((tid,) + t[:5] + (adjust(tid, t[5]), t[6]))
    unknown = set(OBSERVED) - {o[0] for o in out}
    if unknown:
        sys.exit(f"OBSERVED ids with no threat: {sorted(unknown)}")
    return out


def sc_names(codes):
    names = [SC500[c] for c in codes if c != OUTSIDE]
    return names, (OUTSIDE in codes)


def write_tsv(rows):
    head = ["id", "element", "element_name", "stride", "threat", "page_controls", "sc500_skills",
            "outside_sc500", "D", "R", "E", "A", "Di", "dread", "rating", "evidence", "evidence_refs", "basis"]
    lines = ["\t".join(head)]
    for tid, el, cat, text, ctrls, sc, dr, basis in rows:
        names, outside = sc_names(sc)
        lines.append("\t".join([
            tid, el, ELEMENTS[el][1], STRIDE[cat], text, " ".join(ctrls), "; ".join(names),
            "yes" if outside else "no", *map(str, dr), str(dread_score(dr)),
            rating(dread_score(dr)), level_of(tid),
            " | ".join(f"{t} <{u}>" for _, t, u in OBSERVED.get(tid, [])), basis]))
    (ROOT / f"{BASE}.threats.tsv").write_text("\n".join(lines) + "\n")


# ---------- draw.io ----------
FILL = {"ext": ("#F2F4F7", "#B8C0CC"), "proc": ("#EEF4FF", "#9DB8F2"), "store": ("#F3EEFF", "#B9A6F0")}
RCOL = {"High": ("#FDECEC", "#C9302C"), "Medium": ("#FFF6E0", "#B7791F"), "Low": ("#E7F6EC", "#1E7F3E")}


def esc(s):
    return html.escape(s, quote=True)


class Page:
    def __init__(self, name):
        self.name, self.cells, self.n = name, [], 1

    def nid(self):
        self.n += 1
        return f"c{self.n}"

    def box(self, x, y, w, h, value, style, cid=None):
        cid = cid or self.nid()
        self.cells.append(f'<mxCell id="{cid}" value="{esc(value)}" style="{style}html=1;" vertex="1" parent="1">'
                          f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')
        return cid

    def edge(self, a, b, value, style="", cid=None, pts=None, off=None):
        cid = cid or self.nid()
        geo = '<mxGeometry relative="1" as="geometry"/>'
        if off:
            geo = f'<mxGeometry relative="1" as="geometry"><mxPoint x="0" y="{off}" as="offset"/></mxGeometry>'
        if pts:
            geo = ('<mxGeometry relative="1" as="geometry"><Array as="points">'
                   + "".join(f'<mxPoint x="{x}" y="{y}"/>' for x, y in pts) + '</Array></mxGeometry>')
        value = f'<div style="background-color:#ffffff;padding:1px 4px;">{value}</div>' if value else value
        self.cells.append(f'<mxCell id="{cid}" value="{esc(value)}" style="edgeStyle=orthogonalEdgeStyle;rounded=1;html=1;'
                          f'labelBackgroundColor=default;defaultLabelBackgroundColor=page;fontSize=11;{style}" '
                          f'edge="1" source="{a}" target="{b}" parent="1">{geo}</mxCell>')

    def xml(self, w=1500, h=900):
        body = '<mxCell id="0"/><mxCell id="1" parent="0"/>' + "".join(self.cells)
        return f'<mxGraphModel adaptiveColors="auto" dx="0" dy="0" grid="1" gridSize="10" page="1" pageWidth="{w}" pageHeight="{h}"><root>{body}</root></mxGraphModel>'


CHIP = "display:inline-block;margin:1px;padding:0 4px;border-radius:3px;font-size:10px;font-weight:bold;line-height:15px;"


def chip(tid, rt, public):
    fg = RCOL[rt][1]
    if public:
        return f"<span style='{CHIP}background:{fg};color:#ffffff;border:1px solid {fg};'>{tid}</span>"
    return f"<span style='{CHIP}background:{RCOL[rt][0]};color:{fg};border:1px solid {fg};'>{tid}</span>"


def chips_by_element(rows):
    out = {}
    for r in rows:
        out.setdefault(r[1], []).append(chip(r[0], rating(dread_score(r[6])), level_of(r[0]) != "theoretical"))
    return {k: "".join(v) for k, v in out.items()}


def dfd_page(rows):
    p = Page("1 DFD and trust boundaries")
    chips = chips_by_element(rows)
    scores = [dread_score(r[6]) for r in rows]
    counts = {k: sum(1 for x in scores if rating(x) == k) for k in ("High", "Medium", "Low")}
    public = sum(1 for r in rows if level_of(r[0]) != "theoretical")
    p.box(20, 10, 1100, 30, "STRIDE threat model: MCP governance in a Microsoft ecosystem",
          "text;fontSize=22;fontStyle=1;align=left;fontColor=#1F2937;")
    p.box(20, 40, 1300, 22,
          f"{len(rows)} threats: {counts['High']} High, {counts['Medium']} Medium, {counts['Low']} Low by DREAD (AI estimates). "
          f"{public} match a public record. Each chip is one threat id; the register on page 2 has the detail.",
          "text;fontSize=12;align=left;fontColor=#5A626E;")

    bnd = ("rounded=1;arcSize=2;dashed=1;dashPattern=6 4;fillColor=#FBFBFC;strokeColor=#D9534F;strokeWidth=1.5;"
           "verticalAlign=top;align=left;spacingLeft=10;spacingTop=4;fontSize=11;fontColor=#B03A36;fontStyle=1;")
    for x, y, w, h, t in [
        (20, 80, 860, 220, "TB1  Company governance"),
        (920, 80, 620, 220, "TB2  Policy targets (Microsoft and GitHub clouds)"),
        (20, 350, 400, 290, "TB3  Managed Windows device"),
        (450, 350, 380, 290, "TB4  Microsoft cloud agents"),
        (860, 350, 300, 290, "TB5  Company Azure: gateway"),
        (1190, 350, 350, 290, "TB6  Private backend network"),
        (20, 730, 400, 150, "TB0  Internet: not company controlled"),
        (860, 730, 300, 150, "TB7  Monitoring"),
    ]:
        p.box(x, y, w, h, t, bnd)

    shape = {
        "ext": "rounded=0;fillColor=#FFFFFF;strokeColor=#475467;strokeWidth=1.5;",
        "proc": "rounded=1;arcSize=40;fillColor=#EEF4FF;strokeColor=#3E6FD8;strokeWidth=1.5;",
        "store": "shape=partialRectangle;left=0;right=0;fillColor=#F6F2FF;strokeColor=#7A5AF8;strokeWidth=2;",
    }

    def node(cid, x, y, w, h, name, kind):
        label = (f"<div style='font-size:12px;color:#1F2937;'><b>{cid}</b>  {name}</div>"
                 f"<div style='margin-top:6px;line-height:17px;'>{chips.get(cid, '')}</div>")
        p.box(x, y, w, h, label, f"{shape[kind]}whiteSpace=wrap;shadow=0;spacing=6;fontSize=12;", cid=cid)

    node("EE3", 50, 140, 160, 120, "Requester and approver", "ext")
    node("DS1", 280, 140, 200, 120, "Approved list in Git", "store")
    node("P1", 560, 140, 220, 120, "Sync pipeline", "proc")
    node("DS2", 1000, 140, 420, 120, "Policy targets (GitHub, Foundry, Power Platform, M365 admin center)", "store")
    node("EE1", 40, 420, 150, 110, "Developer", "ext")
    node("P2", 220, 400, 180, 150, "Managed client (VS Code, Windows device)", "proc")
    node("EE2", 465, 420, 115, 110, "M365 Copilot user", "ext")
    node("P3", 620, 395, 190, 120, "Cloud agents", "proc")
    node("P6", 620, 530, 190, 100, "Runtime detection", "proc")
    node("P4", 880, 410, 215, 130, "Gateway (API Management or AI Gateway)", "proc")
    node("P5", 1275, 410, 245, 130, "Company MCP server", "proc")
    node("EE4", 60, 790, 320, 70, "Unapproved or malicious MCP server", "ext")
    node("DS3", 885, 790, 230, 75, "Logs and Purview audit", "store")

    flow = "strokeColor=#667085;fontColor=#344054;strokeWidth=1.5;endArrow=block;endFill=1;"
    bad = "strokeColor=#D9534F;fontColor=#B03A36;dashed=1;strokeWidth=1.5;endArrow=block;endFill=1;jumpStyle=arc;jumpSize=10;"
    thin = "strokeColor=#98A2B3;fontColor=#5A626E;strokeWidth=1;endArrow=open;dashed=1;"

    def fl(a, b, fid, label, st, pts=None, show=True):
        text = f"<b>{fid}</b> {label}"
        if show:
            text += f"<br>{chips[fid]}"
        p.edge(a, b, text, st, pts=pts)

    def anc(ex=None, ey=None, nx=None, ny=None):
        out = ""
        for k, v in (("exitX", ex), ("exitY", ey), ("entryX", nx), ("entryY", ny)):
            if v is not None:
                out += f"{k}={v};"
        return out + "exitDx=0;exitDy=0;entryDx=0;entryDy=0;" if out else ""

    p.edge("EE3", "DS1", "pull request", flow)
    p.edge("DS1", "P1", "on merge", flow)
    fl("P1", "DS2", "F1", "policy update", flow)
    p.edge("DS2", "P2", "applied", thin + anc(0.05, 1, 0.5, 0), pts=[(1021, 322), (310, 322)])
    p.edge("DS2", "P3", "applied", thin + anc(0.15, 1, 0.5, 0), pts=[(1063, 338), (715, 338)])
    p.edge("EE1", "P2", "uses", flow + anc(1, 0.5, 0, 0.5))
    p.edge("EE2", "P3", "", flow + anc(1, 0.5, 0, 0.5))
    p.edge("P3", "P6", "checked", thin)
    fl("P2", "P4", "F2", "tool call", flow + anc(0.8, 1, 0.25, 1), pts=[(364, 672), (934, 672)])
    fl("P3", "P4", "F2", "", flow + anc(1, 0.4, 0, 0.3), show=False)
    fl("P4", "P5", "F3", "calls", flow + anc(1, 0.3, 0, 0.3))
    fl("P5", "P4", "F4", "response", flow + anc(0, 0.75, 1, 0.75))
    p.edge("P4", "DS3", "log", thin + anc(0.6, 1, 0.5, 0))
    fl("P2", "P5", "F5", "direct bypass attempt", bad + anc(0.4, 1, 0.5, 1), pts=[(292, 700), (1397, 700)])
    fl("P2", "EE4", "F5", "unapproved server", bad + anc(0.1, 1, 0.5, 0), show=False)

    legend = ("<div style='font-size:12px;font-weight:bold;color:#1F2937;margin-bottom:4px;'>How to read it</div>"
              f"<div style='line-height:19px;'>{chip('E4', 'High', False)} High {chip('S1', 'Medium', False)} Medium {chip('R2', 'Low', False)} Low: DREAD rating<br>"
              f"{chip('S8', 'Medium', True)} solid chip: matches a public record<br>"
              "Ids: S spoofing, T tampering, R repudiation, I information disclosure, D denial of service, E elevation of privilege<br>"
              "<span style='color:#B03A36;'>Red dashed box</span>: trust boundary. "
              "<span style='color:#B03A36;'>Red dashed line</span>: bypass flow</div>")
    p.box(1190, 730, 350, 150, legend,
          "rounded=1;arcSize=4;whiteSpace=wrap;align=left;verticalAlign=top;spacing=10;fillColor=#FFFFFF;strokeColor=#D0D5DD;fontSize=11;")
    return p


def table_page(name, header, rows, widths, title, w=1500):
    p = Page(name)
    p.box(20, 8, 1200, 30, title, "text;fontSize=20;fontStyle=1;align=left;fontColor=#1F2937;")
    th = "".join(f"<th align='left' style='padding:6px;background:#1F2937;color:#ffffff;'>{esc(h)}</th>" for h in header)
    body = ""
    for n, r in enumerate(rows):
        tds = ""
        zebra = "#FFFFFF" if n % 2 == 0 else "#F9FAFB"
        for i, c in enumerate(r["cells"]):
            bg = f" background:{r['bg'][i] if r.get('bg', {}).get(i) else zebra};"
            tds += f"<td valign='top' style='padding:4px 6px;border-bottom:1px solid #E4E7EC;{bg}'>{c}</td>"
        body += f"<tr>{tds}</tr>"
    cols = "".join(f"<col width='{x}'/>" for x in widths)
    tbl = f"<table style='border-collapse:collapse;font-size:11px;width:{sum(widths)}px' cellpadding='0'>{cols}<tr>{th}</tr>{body}</table>"
    import math, re as _re
    def row_h(r):
        mx = 1
        for i, c in enumerate(r["cells"]):
            parts = c.split("<br>")
            n = 0
            for part in parts:
                txt = _re.sub(r"<[^>]+>", "", part)
                n += max(1, math.ceil(len(txt) / max(4, (widths[i] - 12) / 5.4)))
            mx = max(mx, n)
        return 13 * mx + 10
    height = int((40 + 26 + sum(row_h(r) for r in rows)) * 1.12)
    p.box(20, 50, sum(widths) + 10, height, tbl, "text;whiteSpace=wrap;overflow=fill;align=left;verticalAlign=top;")
    return p, sum(widths) + 60, height + 100


EVCOL = {"exploited": "#FDECEC", "disclosed": "#FFF6E0", "theoretical": "#F2F4F7"}


def evidence_cell(tid):
    lv = level_of(tid)
    refs = OBSERVED.get(tid, [])
    if not refs:
        return "theoretical (interpretation by AI)"
    return f"<b>{lv}</b><br>" + "<br>".join(f"{esc(t)}<br><font style='font-size:9px'>{esc(u)}</font>" for _, t, u in refs)


def register_page(rows):
    ordered = sorted(rows, key=lambda r: (-dread_score(r[6]), r[0]))
    out = []
    for r in ordered:
        tid, el, cat, text, ctrls, sc, dr, basis = r
        s = dread_score(dr)
        rt = rating(s)
        out.append({"cells": [chip(tid, rt, level_of(tid) != "theoretical"), f"<b>{el}</b> {esc(ELEMENTS[el][1])}", esc(STRIDE[cat]), esc(text),
                              esc(" ".join(c for c in ctrls)), *map(str, dr), f"<b>{s}</b>", rt, evidence_cell(tid)],
                    "bg": {11: RCOL[rt][0], 12: EVCOL[level_of(tid)]}})
    hdr = ["ID", "Element", "STRIDE", "Threat (interpretation by AI)", "Page control ids", "D", "R", "E", "A", "Di", "Score", "Rating", "Evidence"]
    return table_page("2 DREAD register", hdr, out, [48, 170, 90, 400, 150, 22, 22, 22, 22, 24, 40, 58, 360],
                      "DREAD register, highest first (scores are AI estimates)")


def sc500_page(rows):
    by = {}
    for r in rows:
        for c in r[5]:
            by.setdefault(c, []).append(r[0])
    out = []
    for code, text in SC500.items():
        ids = sorted(by.get(code, []), key=lambda t: ("STRIDE".index(t[0]), int(t[1:])))
        out.append({"cells": [esc(text), esc(", ".join(ids)) if ids else "<i>not used by an MCP threat</i>", str(len(ids))]})
    out.append({"cells": ["<b>Related controls outside the SC-500 outline (GitHub, VS Code, Intune, Power Platform)</b>",
                          esc(", ".join(r[0] for r in rows if OUTSIDE in r[5])), str(sum(1 for r in rows if OUTSIDE in r[5]))],
                "bg": {0: "#FFF9DB"}})
    return table_page("3 SC-500 map", ["SC-500 skill measured (Microsoft Learn study guide, page last updated 2026-05-13)", "Related threat ids", "Count"],
                      out, [640, 560, 50], "Related SC-500 study topics (not verified mitigations; skill names as published)")


def dfd_text():
    """ASCII companion: logical flows and design requirements, not deployment evidence."""
    return """MCP governance: logical DFD

Governance:
  EE3 Requester/approver -> DS1 Approved list in Git -> P1 Sync pipeline
  P1 -> [F1 Policy update] -> DS2 Policy targets -> P2 Managed client
                                             -> P3 Cloud agents
  Microsoft 365 access is manual; Power Platform MCP policy stays manual until API validation.
  F1 aggregates validated automation and manual changes; it does not establish API support.

Tool execution:
  EE1 Developer -> P2 --[F2 Tool call]--> P4 Gateway --[F3]--> P5 MCP server
  EE2 User      -> P3 --[F2 Tool call]--> P4
                  P3 -> P6 Runtime detection
                  P4 <--[F4 Response]--- P5
                  P4 -> DS3 Logs and audit

Attempted bypasses (requirements to prevent, not verified blocks):
  P2 --[F5]--> P5
  P2 --[F5]--> EE4 Unapproved server

Flow description: a reviewed list supplies policy targets through a pipeline where
automation is supported. Clients and cloud agents request tools through a gateway;
the gateway calls the backend and exports audit data. F5 covers direct backend
access and unapproved external servers. F4 draws the backend response leg only;
gateway-to-client response legs and cloud-agent bypass legs are not drawn.

Logical zones (not proof of effective security boundaries):
  TB0 Internet: EE4
  TB1 Company governance: EE3, DS1, P1
  TB2 Policy targets: DS2
  TB3 Managed Windows device: EE1, P2
  TB4 Microsoft cloud agents: EE2, P3, P6
  TB5 Company Azure gateway: P4
  TB6 Private backend network (design requirement): P5
  TB7 Monitoring: DS3

The figure aggregates product variants. OAuth exchanges, downstream APIs and
stores, package distribution, external detector boundaries and non-gateway audit
feeds need more detailed models. A gateway does not inspect local stdio traffic. The direct Agent 365 BYO route is
excluded from this private backend; a gateway-fronted BYO composition is untested.
Foundry Network guardrails are preview; toolbox networking is a separate control.
ACP must retain mixed mode where classic policies protect custom/HTTP connectors.
Preview tool threat protection excludes discovery and session-management operations.
"""


def main():
    check()
    rows = numbered()
    write_tsv(rows)
    pages = [dfd_page(rows)]
    specs = [(1560, 900)]
    for fn in (register_page, sc500_page):
        pg, w, h = fn(rows)
        pages.append(pg)
        specs.append((w, h))
    diagrams = ""
    for i, (pg, (w, h)) in enumerate(zip(pages, specs)):
        diagrams += f'<diagram id="p{i+1}" name="{esc(pg.name)}">{pg.xml(w, h)}</diagram>'
    (ROOT / f"{BASE}.drawio").write_text(f'<mxfile host="app.diagrams.net" version="26.0.0">{diagrams}</mxfile>\n')
    (ROOT / f"{BASE}.dfd.xml").write_text(pages[0].xml(1560, 900) + "\n")
    (ROOT / f"{BASE}.dfd.txt").write_text(dfd_text())
    scores = [dread_score(r[6]) for r in rows]
    print(len(rows), "threats;", {k: sum(1 for s in scores if rating(s) == k) for k in ("High", "Medium", "Low")})


if __name__ == "__main__":
    main()
