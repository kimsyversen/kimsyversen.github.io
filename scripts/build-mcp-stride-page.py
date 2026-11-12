"""Build mcp-governance-stride.html: the STRIDE diagram with clickable threats, and the DREAD register.

  python3 -I scripts/build-mcp-stride.py        (first, if the data changed)
  python3 -I scripts/build-mcp-stride-page.py

Boundary and element geometry and edge routes come from page 1 of mcp-governance-stride.drawio.
Threats, scores and evidence come from scripts/mcp_stride_data.py. Never hand edit the html.
"""

import html
import importlib.util
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from mcp_stride_data import (ELEMENTS, LEVELS, OBSERVED, STRIDE, dread_score, level_of, rating)  # noqa: E402
from section_anchors import add_anchors  # noqa: E402

_spec = importlib.util.spec_from_file_location("mcp_stride_build", HERE / "build-mcp-stride.py")
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)

ROOT = HERE.parent
BASE = "mcp-governance-stride"
DESIGN = "mcp-governance-microsoft-interactive.html"
REPO = "https://github.com/kimsyversen/kimsyversen.github.io/blob/master/"
AS_OF = ("2026-11-12", "12 Nov 2026")
KIND = {"ext": "External entity", "proc": "Process", "store": "Data store", "flow": "Data flow"}
FACTORS = ["Damage", "Reproducibility", "Exploitability", "Affected users", "Discoverability"]

esc = lambda s: html.escape(str(s), quote=True)  # noqa: E731


# ---------- read the drawio ----------
def read_drawio():
    root = ET.parse(ROOT / f"{BASE}.drawio").getroot()
    page = next(d for d in root.iter("diagram") if d.get("id") == "p1")
    cells = {}
    bounds, nodes, edges = [], {}, []
    for c in page.iter("mxCell"):
        cells[c.get("id")] = c
    for cid, c in cells.items():
        g = c.find("mxGeometry")
        val = c.get("value") or ""
        if c.get("vertex") == "1":
            x, y, w, h = (float(g.get(k, 0)) for k in ("x", "y", "width", "height"))
            if val.startswith("TB"):
                tb, _, name = val.partition("  ")
                bounds.append({"id": tb, "name": name.strip(), "x": x, "y": y, "w": w, "h": h})
            elif cid in ELEMENTS:
                nodes[cid] = {"x": x, "y": y, "w": w, "h": h}
        elif c.get("edge") == "1":
            st = dict(kv.split("=", 1) for kv in (c.get("style") or "").split(";") if "=" in kv)
            pts = [(float(p.get("x")), float(p.get("y"))) for p in g.iter("mxPoint") if p.get("as") is None]
            text = re.sub(r"<[^>]+>", " ", html.unescape(val))
            text = re.sub(r"\s+", " ", text).strip()
            fid = None
            m = re.match(r"(F\d)\b\s*(.*)", text)
            label = text
            if m:
                fid, label = m.group(1), m.group(2)
                label = re.sub(r"\b[STRIDE]\d+\b", "", label).strip()
            show_chips = bool(fid) and bool(re.search(r"<span", html.unescape(val)))
            kind = "bad" if st.get("strokeColor") == "#D9534F" else ("thin" if st.get("strokeColor") == "#98A2B3" else "flow")
            edges.append({"src": c.get("source"), "tgt": c.get("target"), "st": st, "pts": pts,
                          "fid": fid, "label": label, "chips": show_chips, "kind": kind})
    if len(nodes) != len(ELEMENTS) - 5:
        sys.exit(f"drawio nodes {sorted(nodes)} do not match the element list")
    return bounds, nodes, edges


def anchor(n, ax, ay):
    return (n["x"] + n["w"] * ax, n["y"] + n["h"] * ay)


def route(e, nodes):
    s, t, st = nodes[e["src"]], nodes[e["tgt"]], e["st"]
    start = anchor(s, float(st["exitX"]), float(st["exitY"])) if "exitX" in st else None
    end = anchor(t, float(st["entryX"]), float(st["entryY"])) if "entryX" in st else None
    if start is None and end is None:
        lo, hi = max(s["y"], t["y"]), min(s["y"] + s["h"], t["y"] + t["h"])
        if lo < hi:
            y = (lo + hi) / 2
            if s["x"] < t["x"]:
                return [(s["x"] + s["w"], y), (t["x"], y)]
            return [(s["x"], y), (t["x"] + t["w"], y)]
        x = (max(s["x"], t["x"]) + min(s["x"] + s["w"], t["x"] + t["w"])) / 2
        if s["y"] < t["y"]:
            return [(x, s["y"] + s["h"]), (x, t["y"])]
        return [(x, s["y"]), (x, t["y"] + t["h"])]
    if end is None:
        end = (start[0], t["y"]) if t["y"] > start[1] else (start[0], t["y"] + t["h"])
    pts = [start] + e["pts"] + [end]
    out = [pts[0]]
    vertical_first = "exitY" in st and float(st["exitY"]) in (0.0, 1.0)
    for i, (a, b) in enumerate(zip(pts, pts[1:])):
        if a[0] != b[0] and a[1] != b[1]:
            if i == 0 and vertical_first:
                my = (a[1] + b[1]) / 2
                out += [(a[0], my), (b[0], my)]
            else:
                mx = (a[0] + b[0]) / 2
                out += [(mx, a[1]), (mx, b[1])]
        out.append(b)
    return out


def point_at(path, frac):
    segs = list(zip(path, path[1:]))
    lens = [abs(b[0] - a[0]) + abs(b[1] - a[1]) for a, b in segs]
    goal = sum(lens) * frac
    for (a, b), ln in zip(segs, lens):
        if goal <= ln and ln:
            f = goal / ln
            return (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f), abs(b[0] - a[0]) >= abs(b[1] - a[1])
        goal -= ln
    return path[-1], True


# ---------- threats ----------
def threats():
    raw = {}
    per = {}
    for t in build.THREATS:
        per[t[1]] = per.get(t[1], 0) + 1
        raw[f"{t[1]}{per[t[1]]}"] = t[5]
    out = []
    for tid, el, cat, text, ctrls, _sc, dr, basis in build.numbered():
        s = dread_score(dr)
        out.append({"id": tid, "el": el, "cat": cat, "text": text, "ctrls": ctrls, "dr": list(dr),
                    "raw": list(raw[tid]), "score": s, "rating": rating(s), "level": level_of(tid),
                    "refs": [list(r) for r in OBSERVED.get(tid, [])],
                    "basis": basis.replace("AI inference", "interpretation by AI")})
    return out


def control_labels(ids):
    src = (ROOT / DESIGN).read_text()
    out = {}
    for cid in ids:
        m = re.search(rf'id="{re.escape(cid)}"[^>]*>\s*<h4>(.*?)<', src, re.S)
        if m:
            out[cid] = re.sub(r"\s+", " ", html.unescape(m.group(1))).strip()
            continue
        m = (re.search(rf'<span id="{re.escape(cid)}"></span>(.*?)<', src, re.S)
             or re.search(rf'<strong id="{re.escape(cid)}">(.*?)</strong>', src, re.S))
        if not m:
            sys.exit(f"control {cid} not found on {DESIGN}")
        words = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).split()
        out[cid] = "Gap: " + " ".join(words[:9]).rstrip(".,") + (" ..." if len(words) > 9 else "")
    return out


# ---------- svg ----------
CH = 7.9     # mono glyph width at 13px
CHIP_H = 21


def chip_w(tid):
    return round(len(tid) * CH + 14)


def chip_svg(t, x, y):
    pub = " pub" if t["level"] != "theoretical" else ""
    lab = f'{t["id"]}: {STRIDE[t["cat"]]}, {t["rating"]} {t["score"]}'
    if t["level"] != "theoretical":
        lab += f', {t["level"]}'
    w = chip_w(t["id"])
    return (f'<g class="chip r-{t["rating"].lower()}{pub}" data-t="{t["id"]}" data-cat="{t["cat"]}" role="button" tabindex="0" '
            f'aria-label="{esc(lab)}" transform="translate({x:.1f} {y:.1f})"><title>{esc(t["id"])}: {esc(t["text"])}</title>'
            f'<rect width="{w}" height="{CHIP_H}" rx="3"/><text x="{w / 2:.1f}" y="15">{esc(t["id"])}</text></g>')


def chips_flow(ts, x0, y0, maxw):
    """Lay chips out left to right, wrapping at maxw. Returns svg and the height used."""
    out, x, y = [], x0, y0
    for t in ts:
        w = chip_w(t["id"])
        if x + w > x0 + maxw and x > x0:
            x, y = x0, y + CHIP_H + 5
        out.append(chip_svg(t, x, y))
        x += w + 5
    return "".join(out), (y - y0 + CHIP_H) if ts else 0


def wrap(text, width, cw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        nxt = f"{cur} {w}".strip()
        if len(nxt) * cw > width and cur:
            lines.append(cur)
            cur = w
        else:
            cur = nxt
    return lines + [cur] if cur else lines


SHORT = {
    "EE3": "Requester and approver", "DS1": "Approved list in Git", "P1": "Sync pipeline",
    "DS2": "Policy targets (GitHub, Foundry, Power Platform, M365 admin center)", "EE1": "Developer",
    "P2": "Managed client (VS Code, Windows device)", "EE2": "M365 Copilot user", "P3": "Cloud agents",
    "P6": "Defender checks (preview)", "P4": "Gateway (API Management or AI Gateway)", "P5": "Company MCP server",
    "EE4": "Unapproved or malicious MCP server", "DS3": "Logs and Purview audit",
}


def node_svg(eid, n, ts):
    kind = ELEMENTS[eid][0]
    x, y, w, h = n["x"], n["y"], n["w"], n["h"]
    pad = 10
    if kind == "proc":
        shape = f'<rect class="shape" x="{x}" y="{y}" width="{w}" height="{h}" rx="20"/>'
    elif kind == "store":
        shape = (f'<rect class="shape" x="{x}" y="{y}" width="{w}" height="{h}"/>'
                 f'<path class="store-line" d="M{x} {y}h{w}M{x} {y + h}h{w}"/>')
    else:
        shape = f'<rect class="shape" x="{x}" y="{y}" width="{w}" height="{h}"/>'
    inner = w - 2 * pad - (8 if kind == "proc" else 0)
    lx = x + pad + (4 if kind == "proc" else 0)
    lines = wrap(f"{eid} {SHORT[eid]}", inner, 7.3)
    tspans = ""
    for i, ln in enumerate(lines):
        if i == 0 and ln.startswith(eid):
            ln_rest = ln[len(eid):]
            tspans += f'<tspan x="{lx}" dy="0"><tspan class="eid">{esc(eid)}</tspan>{esc(ln_rest)}</tspan>'
        else:
            tspans += f'<tspan x="{lx}" dy="17">{esc(ln)}</tspan>'
    ty = y + pad + 13
    chips, ch_h = chips_flow(ts, lx, ty + 17 * (len(lines) - 1) + 10, inner)
    need = (ty + 17 * (len(lines) - 1) + 10 + ch_h) - (y + h)
    if need > -4:
        print(f"warning: {eid} content overflows its box by {need + 4:.0f}px")
    label = f"{eid} {ELEMENTS[eid][1]}: {KIND[kind].lower()} with {len(ts)} threats. Show only these threats"
    return (f'<g class="node k-{kind}" data-el="{eid}">'
            f'<g class="el-hit" data-el="{eid}" role="button" tabindex="0" aria-pressed="false" aria-label="{esc(label)}">'
            f'{shape}<text class="nm" y="{ty}">{tspans}</text></g>{chips}</g>')


def flow_label_svg(e, path, ts_by_el, frac):
    (cx, cy), _ = point_at(path, frac)
    fid, label = e["fid"], e["label"]
    title = f"{fid} {label}".strip() if fid else label
    if not title:
        return ""
    tw = len(title) * 7.0 + 14
    if not fid:
        return (f'<g class="elabel"><rect x="{cx - tw / 2:.1f}" y="{cy - 10:.1f}" width="{tw:.1f}" height="20" rx="3"/>'
                f'<text x="{cx:.1f}" y="{cy + 4:.1f}">{esc(title)}</text></g>')
    ts = ts_by_el.get(fid, []) if e["chips"] else []
    cw = sum(chip_w(t["id"]) + 5 for t in ts) - 5 if ts else 0
    bw = max(tw, cw + 14)
    bh = 22 + (CHIP_H + 6 if ts else 0)
    top = cy - bh / 2
    chips, _ = chips_flow(ts, cx - cw / 2, top + 24, cw + 1)
    name = f"{fid} {ELEMENTS[fid][1]}: data flow with {len(ts_by_el.get(fid, []))} threats. Show only these threats"
    return (f'<g class="flab" data-el="{fid}"><rect class="flab-bg" x="{cx - bw / 2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="4"/>'
            f'<g class="el-hit" data-el="{fid}" role="button" tabindex="0" aria-pressed="false" aria-label="{esc(name)}">'
            f'<rect class="hit" x="{cx - tw / 2:.1f}" y="{top + 2:.1f}" width="{tw:.1f}" height="19"/>'
            f'<text x="{cx:.1f}" y="{top + 16:.1f}"><tspan class="eid">{esc(fid)}</tspan> {esc(label)}</text></g>{chips}</g>')


# label position along the edge, where the midpoint would sit on another line or box
LABEL_AT = {("P2", "EE4"): 0.5, ("P3", "P6"): None, ("EE2", "P3"): None}


def diagram(ts):
    bounds, nodes, edges = read_drawio()
    by_el = {}
    for t in ts:
        by_el.setdefault(t["el"], []).append(t)
    parts = []
    for b in sorted(bounds, key=lambda b: b["id"]):
        parts.append(f'<g class="tb"><rect x="{b["x"]}" y="{b["y"]}" width="{b["w"]}" height="{b["h"]}" rx="6"/>'
                     f'<text x="{b["x"] + 12}" y="{b["y"] + 19}"><tspan class="tbid">{esc(b["id"])}</tspan> {esc(b["name"])}</text></g>')
    lines, labels = [], []
    for e in edges:
        path = route(e, nodes)
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in path)
        el = f' data-el="{e["fid"]}"' if e["fid"] else ""
        lines.append(f'<path class="edge e-{e["kind"]}"{el} d="{d}" marker-end="url(#m-{e["kind"]})"/>')
        frac = LABEL_AT.get((e["src"], e["tgt"]), 0.5)
        if frac is None:
            continue
        labels.append(flow_label_svg(e, path, by_el, frac))
    node_svgs = [node_svg(eid, n, by_el.get(eid, [])) for eid, n in nodes.items()]
    xs = [b["x"] for b in bounds] + [b["x"] + b["w"] for b in bounds]
    ys = [b["y"] for b in bounds] + [b["y"] + b["h"] for b in bounds]
    vb = (min(xs) - 6, min(ys) - 6, max(xs) - min(xs) + 12, max(ys) - min(ys) + 12)
    defs = "".join(
        f'<marker id="m-{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path class="mk-{k}" d="{"M1 1L9 5L1 9" if k == "thin" else "M0 0L10 5L0 10z"}"/></marker>' for k in ("flow", "bad", "thin"))
    return (f'<svg class="dfd" viewBox="{" ".join(f"{v:g}" for v in vb)}" role="group" aria-label="Data flow diagram with trust boundaries. '
            f'Each threat id is a button." xmlns="http://www.w3.org/2000/svg"><defs>{defs}</defs>'
            + "".join(parts) + "".join(lines) + "".join(node_svgs) + "".join(labels) + "</svg>"), len(bounds), edges


# ---------- score spread ----------
def spread(ts):
    lo, hi = 3.0, 7.5
    W, X0, X1 = 900, 40, 880
    sx = lambda v: X0 + (v - lo) / (hi - lo) * (X1 - X0)  # noqa: E731
    stacks = {}
    dots = []
    for t in sorted(ts, key=lambda t: (t["score"], t["id"])):
        k = t["score"]
        n = stacks.get(k, 0)
        stacks[k] = n + 1
        dots.append((t, sx(k), n))
    top = max(stacks.values())
    R, GAP = 6.5, 15
    base = 24 + top * GAP
    H = base + 34
    out = [f'<svg class="spread" viewBox="0 0 {W} {H}" aria-hidden="true">',
           f'<rect class="band b-low" x="{sx(lo):.1f}" y="10" width="{sx(4) - sx(lo):.1f}" height="{base - 4:.1f}"/>',
           f'<rect class="band b-med" x="{sx(4):.1f}" y="10" width="{sx(6) - sx(4):.1f}" height="{base - 4:.1f}"/>',
           f'<rect class="band b-high" x="{sx(6):.1f}" y="10" width="{sx(hi) - sx(6):.1f}" height="{base - 4:.1f}"/>',
           f'<text class="bandl" x="{sx(lo) + 6:.1f}" y="24">Low</text>',
           f'<text class="bandl" x="{sx(4) + 6:.1f}" y="24">Medium</text>',
           f'<text class="bandl" x="{sx(6) + 6:.1f}" y="24">High</text>',
           f'<path class="axis" d="M{X0} {base + 6}H{X1}"/>']
    v = lo
    while v <= hi + 1e-9:
        out.append(f'<path class="axis" d="M{sx(v):.1f} {base + 6}v5"/><text class="tick" x="{sx(v):.1f}" y="{base + 25}">{v:g}</text>')
        v += 0.5
    for t, x, n in dots:
        pub = " pub" if t["level"] != "theoretical" else ""
        out.append(f'<circle class="dot r-{t["rating"].lower()}{pub}" data-t="{t["id"]}" cx="{x:.1f}" cy="{base - R - n * GAP:.1f}" r="{R}"><title>{t["id"]} {t["score"]}</title></circle>')
    out.append("</svg>")
    return "".join(out)


# ---------- register ----------
def register_rows(ts):
    rows = []
    for t in sorted(ts, key=lambda t: (-t["score"], t["id"])):
        pub = " pub" if t["level"] != "theoretical" else ""
        bars = "".join(f'<td class="f" data-v="{v}"><span>{v}</span><i style="--v:{v}"></i></td>' for v in t["dr"])
        nrefs = len(t["refs"])
        ev = f'<span class="lv lv-{t["level"]}">{t["level"]}</span>'
        if nrefs:
            ev += f'<span class="nref">{nrefs} record{"s" if nrefs > 1 else ""}</span>'
        rows.append(
            f'<tr id="t-{t["id"]}" data-t="{t["id"]}">'
            f'<td class="cid"><button type="button" class="chip-b r-{t["rating"].lower()}{pub}" data-t="{t["id"]}" '
            f'aria-label="Open {t["id"]}">{t["id"]}</button></td>'
            f'<td class="tx"><p>{esc(t["text"])}</p><p class="sub"><b>{t["el"]}</b> {esc(SHORT.get(t["el"], ELEMENTS[t["el"]][1]))}'
            f' <span aria-hidden="true">·</span> {STRIDE[t["cat"]]}</p></td>'
            f'{bars}<td class="sc"><b>{t["score"]:.1f}</b><span class="rt rt-{t["rating"].lower()}">{t["rating"]}</span></td>'
            f'<td class="ev">{ev}</td></tr>')
    return "".join(rows)


def strip_dashes(s):
    if "—" in s or "–" in s:
        sys.exit("em or en dash in page output")
    return s


def main():
    build.check()
    ts = threats()
    ctrl_ids = sorted({c for t in ts for c in t["ctrls"]})
    labels = control_labels(ctrl_ids)
    svg, n_bounds, _ = diagram(ts)
    n = len(ts)
    cnt = {k: sum(t["rating"] == k for t in ts) for k in ("High", "Medium", "Low")}
    lv = {k: sum(t["level"] == k for t in ts) for k in LEVELS}
    els = {k: [e for e, v in ELEMENTS.items() if v[0] == k] for k in KIND}
    data = {
        "threats": ts,
        "elements": {k: [v[0], v[1], SHORT.get(k, v[1])] for k, v in ELEMENTS.items()},
        "stride": STRIDE, "kind": KIND, "factors": FACTORS, "ctrl": labels, "design": DESIGN,
        "fc": REPO + "mcp-governance-microsoft-interactive.factcheck.md#ev-",
    }
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    tpl = (HERE / "mcp_stride_page_template.html").read_text()
    page = (tpl.replace("{{SVG}}", svg)
               .replace("{{SPREAD}}", spread(ts))
               .replace("{{ROWS}}", register_rows(ts))
               .replace("{{DATA}}", blob)
               .replace("{{N}}", str(n))
               .replace("{{HIGH}}", str(cnt["High"])).replace("{{MED}}", str(cnt["Medium"])).replace("{{LOW}}", str(cnt["Low"]))
               .replace("{{EXPL}}", str(lv["exploited"])).replace("{{DISC}}", str(lv["disclosed"])).replace("{{THEO}}", str(lv["theoretical"]))
               .replace("{{NEL}}", str(len(ELEMENTS))).replace("{{NEXT}}", str(len(els["ext"])))
               .replace("{{NPROC}}", str(len(els["proc"]))).replace("{{NSTORE}}", str(len(els["store"])))
               .replace("{{NFLOW}}", str(len(els["flow"]))).replace("{{NTB}}", str(n_bounds))
               .replace("{{ASOF}}", AS_OF[0]).replace("{{ASOFT}}", AS_OF[1]).replace("{{REPO}}", REPO)
               .replace("{{DESIGN}}", DESIGN))
    left = re.findall(r"\{\{[A-Z]+\}\}", page)
    if left:
        sys.exit(f"unfilled placeholders: {left}")
    page = strip_dashes(add_anchors(page))
    (ROOT / f"{BASE}.html").write_text(page)
    print(f"wrote {BASE}.html: {n} threats, {cnt}, {lv}")


if __name__ == "__main__":
    main()
