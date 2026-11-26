"""Build mcp-intake.html from scripts/mcp_intake_data.py.

Usage:
  python3 -I scripts/build-mcp-intake.py            write the page
  python3 -I scripts/build-mcp-intake.py --ledger   also rewrite the statement table in
                                                    mcp-intake.factcheck.md, keeping verdicts
                                                    of unchanged wording
"""

import html
import re
import sys
from pathlib import Path
from urllib.parse import quote as urlquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import mcp_intake_data as D  # noqa: E402
from section_anchors import add_anchors  # noqa: E402

PAGE = ROOT / "mcp-intake.html"
LEDGER = ROOT / "mcp-intake.factcheck.md"
BEGIN = "<!-- ledger -->"
END = "<!-- /ledger -->"

APPLIES = {"P": "Package", "C": "Container", "R": "Remote"}
FAIL_TEXT = {
    "Block": "The server or version being assessed cannot move on until this is fixed. If the failing one is already in use, it is suspended, unless a change trigger says what to do instead.",
    "Review": "The approver decides and records why.",
}
STAGE = {s["key"]: s for s in D.STAGES}
CHECK = {c["id"]: c for c in D.CHECKS}

_statements = []


def esc(text):
    return html.escape(text, quote=True)


def say(text, basis="requirement"):
    """Escape a statement and record it for the fact check."""
    if (basis, text) not in _statements:
        _statements.append((basis, text))
    return esc(text)


def passage(qid):
    entry = D.Q[qid]
    key, words = entry[0], entry[1]
    title, url, _ = D.SOURCES[key]
    if len(entry) > 2:
        return f"{url}#page={entry[2]}", f"{title}, page {entry[2]}"
    parts = words.split()
    enc = lambda t: urlquote(t, safe="").replace("-", "%2D")
    if len(parts) > 8:
        fragment = f"{enc(' '.join(parts[:4]))},{enc(' '.join(parts[-4:]))}"
    else:
        fragment = enc(words)
    return f"{url}#:~:text={fragment}", title


def sources(quote_ids):
    if not quote_ids:
        return ""
    items = []
    for qid in quote_ids:
        url, title = passage(qid)
        items.append(f'<li><q>{esc(D.Q[qid][1])}</q> <a href="{esc(url)}">{esc(title)}</a></li>')
    label = "Quote" if len(items) == 1 else f"{len(items)} quotes"
    return f'<details class="src"><summary>{label}</summary><ul>{"".join(items)}</ul></details>'


def tag(name):
    return f' <span class="tag {name}">{name}</span>' if name else ""


def fact(f):
    basis = " ".join(x for x in (f["tag"], "quote:" + ",".join(f["q"]) if f["q"] else "") if x) or "requirement"
    return f'<span>{say(f["text"], basis)}</span>{tag(f["tag"])}{sources(f["q"])}'


def facts(items, cls="facts"):
    if not items:
        return ""
    return f'<ul class="{cls}">' + "".join(f"<li>{fact(f)}</li>" for f in items) + "</ul>"


def plain_list(items, tagname="ul", cls="", basis="requirement"):
    attr = f' class="{cls}"' if cls else ""
    return f"<{tagname}{attr}>" + "".join(f"<li>{say(i, basis)}</li>" for i in items) + f"</{tagname}>"


def chip(cid):
    return f'<a class="chip" href="#check-{cid}"><b>{cid}</b> {esc(CHECK[cid]["name"])}</a>'


def chips(ids):
    return '<ul class="chips">' + "".join(f"<li>{chip(i)}</li>" for i in ids) + "</ul>" if ids else ""


def intro():
    phases = (
        ("Screen the request",
         "Record the owner, purpose, data and access needed. Check the approved catalog and verify the publisher before downloading or connecting."),
        ("Assess the server",
         "Pin the local artifact and dependencies, or record the remote URL and get vendor evidence. Scan for vulnerabilities and malware, review tools and permissions, then test in isolation with test data."),
        ("Approve and release",
         "Have an independent approver review the findings. Record the approved configuration, limits and expiry. Roll it out to a small group first."),
        ("Watch for changes",
         "Compare live tool definitions with the approval record and track vulnerability alerts. Reassess changes before allowing them. Suspend access if you suspect compromise."),
    )
    rows = "\n".join(
        f'      <li><h3>{esc(title)}</h3><p>{say(action)}</p></li>'
        for title, action in phases
    )
    return f"""
  <header class="hero">
    <h1>MCP server intake</h1>
    <p class="lede">{say("Review new servers before use and reassess them when they change.")}</p>
  </header>

  <main>
  <section id="start-here">
    <h2 id="h-start-here">Start here</h2>
    <ol class="intake-steps">
{rows}
    </ol>
  </section>
"""


def process():
    panels = []
    for n, s in enumerate(D.STAGES, 1):
        ids = [c["id"] for c in D.CHECKS if c["stage"] == s["key"]]
        panels.append(f"""
    <article id="stage-{s['key']}">
      <h3 id="h-stage-{s['key']}">{n}. {esc(s['title'])}</h3>
      <dl class="pairs">
        <dt>Inputs</dt><dd>{plain_list(s['inputs'])}</dd>
        <dt>Actions</dt><dd>{plain_list(s['steps'], 'ol')}</dd>
        <dt>What runs</dt><dd>{say(s['runs'])}</dd>
        <dt>Output</dt><dd>{say(s['output'])}</dd>
        <dt>Gate</dt><dd>{say(s['gate'])}</dd>
      </dl>
      {facts(s['facts'])}
      {chips(ids)}
    </article>""")
    return f"""
  <section id="process">
    <h2 id="h-process">Process</h2>
    <p>{say("Nine stages run in order. A failed gate stops the server there. Nothing from the server runs before Sandbox.")}</p>
    {''.join(panels)}
  </section>
"""


def stage_links(active):
    return ", ".join(
        f'<a href="#stage-{s["key"]}">{esc(s["title"])}</a>'
        for s in D.STAGES if s["key"] in active
    )


def change():
    panels = "".join(f"""
    <details class="item" id="trigger-{t['id']}">
      <summary id="h-trigger-{t['id']}">{esc(t['title'])}</summary>
      <dl class="pairs">
        <dt>How it is noticed</dt><dd>{say(t['detect'])}</dd>
        <dt>Stages that run again</dt><dd>{stage_links(t['rerun'])}</dd>
        <dt>Meanwhile</dt><dd>{say(t['meanwhile'])}</dd>
        <dt>Checks to look at first</dt><dd>{chips(t['checks'])}</dd>
      </dl>
      {facts(t['facts'])}
    </details>""" for t in D.TRIGGERS)
    force = "".join(
        f'<tr><th scope="row">{say(name)}</th><td>{chips(ids)}</td></tr>' for name, ids in D.FORCE_REVIEW)
    return f"""
  <section id="changes">
    <h2 id="h-changes">When something changes</h2>
    <p>{say("A change is any difference from the approval record. Never update a server automatically unless it meets every condition for automatic approval.")}</p>
    {panels}
    <h3 id="h-auto-approval">Automatic approval of a new version</h3>
    <p>{say("Allow it only when all of these are true. It skips the Review stage, so nobody reads the code difference. The approver for the server's tier approves the rule in advance and is the approver of record. Otherwise a person decides.")}</p>
    {plain_list(D.AUTO)}
    <h3 id="h-force-review">Differences that need a person</h3>
    <div class="tbl"><table><thead><tr><th scope="col">Difference</th><th scope="col">Checks</th></tr></thead><tbody>{force}</tbody></table></div>
  </section>
"""


def cases():
    panels = []
    for s in D.SCENARIOS:
        steps = "".join(
            f'<li class="r-{p["result"]}"><p class="at"><a href="#stage-{p["stage"]}">{esc(STAGE[p["stage"]]["title"])}</a>'
            f' <span class="result">{D.RESULTS[p["result"]]}</span></p>'
            f'<p>{say(p["text"], "example")}</p>{chips(p["checks"])}</li>' for p in s["steps"])
        panels.append(f"""
    <details class="item" id="case-{s['id']}">
      <summary id="h-case-{s['id']}">{esc(s['title'])}</summary>
      <p>{say(s['intro'], 'example')}</p>
      {facts(s['facts'])}
      <ol class="steps">{steps}</ol>
    </details>""")
    return f"""
  <section id="cases">
    <h2 id="h-cases">Walk through a case</h2>
    {''.join(panels)}
  </section>
"""


def check_row(c):
    applies = " ".join(f'<span class="ap">{APPLIES[a]}</span>' for a in c["applies"])
    basis = sources(c["why"]) if c["why"] else ""
    note = f'<dt>Note</dt><dd>{fact(c["note"])}</dd>' if c["note"] else ""
    own = "" if c["why"] else f'<dt>Basis</dt><dd>{say("Requirement of this process. No source is quoted.", "label")}</dd>'
    if basis:
        own = f"<dt>Basis</dt><dd>{basis}</dd>"
    return f"""
      <details class="chk" id="check-{c['id']}">
        <summary><b>{c['id']}</b><span class="name">{say(c['name'])}</span><span class="fail {c['fail']}">{c['fail']}</span><span class="aps">{applies}</span></summary>
        <dl class="pairs">
          <dt>Do</dt><dd>{say(c['do'])}</dd>
          <dt>Passes when</dt><dd>{say(c['passes'])}</dd>
          {note}{own}
        </dl>
      </details>"""


def checks():
    groups = []
    for s in D.STAGES:
        rows = [c for c in D.CHECKS if c["stage"] == s["key"]]
        if rows:
            groups.append(f'<div class="group"><h3 id="h-checks-{s["key"]}">{esc(s["title"])} checks</h3>'
                          + "".join(check_row(c) for c in rows) + "</div>")
    tools = "".join(
        f'<tr><th scope="row">{esc(job)}</th><td>{say(names, "quote:" + ",".join(q))}{sources(q)}</td></tr>'
        for job, names, q in D.SCANNERS)
    return f"""
  <section id="checks">
    <h2 id="h-checks">Checks</h2>
    <h3 id="minimum-checklist">Minimum checklist</h3>
    {chips(D.MINIMUM)}
    <dl class="pairs">
      <dt><span class="fail Block">Block</span></dt><dd>{say(FAIL_TEXT['Block'])}</dd>
      <dt><span class="fail Review">Review</span></dt><dd>{say(FAIL_TEXT['Review'])}</dd>
    </dl>
    {''.join(groups)}
    <h3 id="h-scanner-tools">Example scanning tools</h3>
    <p>{say("Pick at least one tool for each job. Other tools can do the same jobs.")}</p>
    <div class="tbl"><table><thead><tr><th scope="col">Job</th><th scope="col">Tools</th></tr></thead><tbody>{tools}</tbody></table></div>
  </section>
"""


def coverage():
    groups = []
    for group, classes in D.COVERAGE:
        rows = []
        for v in classes:
            owasp = " ".join(f'<a class="code" href="#owasp-{c}">{c}</a>' for c in v["owasp"]) or '<span class="code">none</span>'
            basis = " ".join(x for x in (v["tag"], "quote:" + ",".join(v["q"]) if v["q"] else "") if x)
            rows.append(
                f'<tr><th scope="row">{say(v["name"], "label")}<span class="codes">{owasp}</span></th>'
                f'<td>{chips(v["checks"])}</td><td>{say(v["gap"], basis)}{tag(v["tag"])}{sources(v["q"])}</td></tr>')
        slug = re.sub(r"[^a-z]+", "-", group.lower()).strip("-")
        groups.append(f"""
    <h3 id="h-coverage-{slug}">{esc(group)}</h3>
    <div class="tbl"><table class="cov"><thead><tr><th scope="col">Weakness or attack</th><th scope="col">Checks against it</th><th scope="col">What can still get through</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>""")
    owasp = "".join(
        f'<li id="owasp-{code}"><a href="{esc(D.SOURCES[key][1])}">{code} {esc(name)}</a></li>'
        for code, (name, key) in D.OWASP.items())
    return f"""
  <section id="coverage">
    <h2 id="h-coverage">Coverage</h2>
    <p>{say("Matching a check to an attack is a design choice. It is not a measured detection rate, and the list of attacks is not complete.", "inference")}{tag("inference")}</p>
    {''.join(groups)}
    <h3 id="h-owasp-codes">OWASP MCP Top 10 codes</h3>
    <ul class="owasp">{owasp}</ul>
  </section>
"""


def decide():
    tiers = "".join(
        f'<tr><th scope="row">{n} {esc(name)}</th><td>{say(what)}</td><td>{say(who)}</td><td>{say(every)}</td></tr>'
        for n, name, what, who, every in D.TIERS)
    decisions = "".join(f"<dt>{esc(a)}</dt><dd>{say(b)}</dd>" for a, b in D.DECISIONS)
    return f"""
  <section id="tiers">
    <h2 id="h-tiers">Risk tiers and decisions</h2>
    <p>{say("Use the highest tier that fits. Adjust the names and intervals to your organisation.")}</p>
    <div class="tbl"><table><thead><tr><th scope="col">Tier</th><th scope="col">The server</th><th scope="col">Who approves</th><th scope="col">Recertify at least every</th></tr></thead><tbody>{tiers}</tbody></table></div>
    <h3 id="h-decisions">Decisions</h3>
    <dl class="pairs">{decisions}</dl>
  </section>

  <section id="record">
    <h2 id="h-record">Approval record</h2>
    <p>{say("Keep one record for each approved server. Later changes are compared with it. For a remote server, origin holds the URL and the authorization server details instead. The example is fictional.", "example")}</p>
    <pre tabindex="0"><code>{say(D.RECORD, "example")}</code></pre>
  </section>
"""


def platform():
    rows = "".join(
        f'<tr><th scope="row">{esc(e["name"])}</th><td>{say(e["matches"], "label")}</td><td>{facts(e["facts"])}</td></tr>'
        for e in D.ENFORCE)
    missing = "".join(f"<dt>{esc(a)}</dt><dd>{say(b)}</dd>" for a, b in D.NOT_COVERED)
    return f"""
  <section id="platform">
    <h2 id="h-platform">What the platform enforces</h2>
    <p>{fact(D.ENFORCE_GAP).replace("<span>", "", 1).replace("</span>", "", 1)}</p>
    <div class="tbl"><table class="plat"><thead><tr><th scope="col">Control</th><th scope="col">Works on</th><th scope="col">Limits</th></tr></thead><tbody>{rows}</tbody></table></div>
  </section>

  <section id="not-covered">
    <h2 id="h-not-covered">Not covered</h2>
    <dl class="pairs">{missing}</dl>
  </section>
"""


def footer(body):
    keys = {
        "inference": "Interpretation by AI that is not stated in a source.",
        "unverified": "Not confirmed in a quoted source.",
        "preview": "A feature in preview.",
    }
    rows = "".join(
        f'<dt><span class="tag {k}">{k}</span></dt><dd>{v}</dd>'
        for k, v in keys.items() if f'class="tag {k}"' in body)
    return f"""
  <footer>
    <p class="ai-note"><b>Made with AI</b><span>This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human.</span></p>
    <h2 id="h-tag-key">Tags on this page</h2>
    <dl class="pairs" id="tag-key">{rows}</dl>
  </footer>
"""


STYLE = """
:root{color-scheme:light;--bg:#F3F0E8;--ink:#17150F;--muted:#5F5A4F;--line:#D2CCBE;--rule:#17150F;--red:#B5321C;--green:#2E6B3A;--wash:#E9E5DA;
--display:"Archivo","Arial Narrow",Arial,sans-serif;--body:"Public Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;--mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){color-scheme:dark;--bg:#15140F;--ink:#ECE7DB;--muted:#A49E90;--line:#37342C;--rule:#ECE7DB;--red:#F07A60;--green:#8CCB93;--wash:#1F1D17}}
*{box-sizing:border-box}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--bg);color:var(--ink);font:1rem/1.55 var(--body);-webkit-font-smoothing:antialiased}
.page{max-width:960px;margin:0 auto;padding:0 max(20px,env(safe-area-inset-right,0px)) 48px max(20px,env(safe-area-inset-left,0px))}
a{color:inherit;text-decoration-color:var(--red);text-decoration-thickness:1.5px;text-underline-offset:3px}
a:hover{color:var(--red)}
a:focus-visible,summary:focus-visible,pre:focus-visible{outline:2px solid var(--red);outline-offset:3px}
h1,h2,h3{font-family:var(--display);text-wrap:balance;margin:0}
h1{font-size:clamp(2.2rem,6.4vw,4.4rem);font-weight:800;font-stretch:88%;line-height:.98;letter-spacing:-.02em}
h2{font-size:clamp(1.35rem,2.4vw,1.7rem);font-weight:750;line-height:1.1;letter-spacing:-.012em;margin-bottom:22px}
h3{font-size:1.2rem;font-weight:700;line-height:1.25;margin:32px 0 14px}
dt,thead th{font:600 .72rem/1.5 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
p{margin:0}
p + p{margin-top:12px}
ul,ol{margin:0;padding-left:1.2em}
dd{margin:0}
code,pre{font-family:var(--mono);font-size:.85rem}
pre{overflow-x:auto;background:var(--wash);padding:16px;margin:16px 0 0}
.top{display:flex;justify-content:space-between;gap:16px;padding:18px 0;border-bottom:1px solid var(--line);font-size:.85rem;color:var(--muted)}
.hero{padding:clamp(32px,6vw,64px) 0 24px;border-bottom:2px solid var(--rule)}
.hero .lede{margin-top:12px;font-size:clamp(1.05rem,1.7vw,1.2rem)}
#start-here{padding:24px 0}
.intake-steps{padding-left:1.75rem}
.intake-steps li{padding-left:.35rem}
.intake-steps li + li{margin-top:14px}
.intake-steps li::marker{color:var(--red);font:600 .9rem var(--mono)}
.intake-steps h3{margin:0 0 3px}
.related{display:flex;flex-wrap:wrap;gap:8px 24px;margin-top:20px;font-size:.92rem}

.reference,.item{border-top:1px solid var(--line)}
.reference + .related{border-top:1px solid var(--line);padding-top:20px;margin-top:0}
.reference > summary,.item > summary{cursor:pointer;padding:12px 0;font-weight:600}
.reference > summary{font-size:1.08rem}
.reference > section{padding:20px 0 28px}
.reference > section + section{border-top:1px solid var(--line)}
.item:first-of-type{margin-top:16px}
.item[open]{padding-bottom:16px}
.item > .pairs{margin-top:0}

.tag{display:inline-block;font:500 .68rem/1.5 var(--mono);letter-spacing:.04em;border:1px solid var(--red);color:var(--red);padding:0 5px;border-radius:2px;vertical-align:1px;white-space:nowrap;text-transform:none}
details.src{font-size:.85rem;color:var(--muted);margin-top:4px}
details.src summary{cursor:pointer;font:500 .72rem/1.6 var(--mono);width:fit-content}
details.src ul{margin-top:4px}
details.src li + li{margin-top:6px}
details.src q{color:var(--ink);overflow-wrap:anywhere}

.chip b{font-family:var(--mono);font-weight:600}
article{margin-top:28px;border-top:1px solid var(--rule);padding-top:4px}
article h3{margin-top:16px}
.facts{list-style:none;padding:0;margin-top:18px}
.facts li{padding:10px 0;border-top:1px solid var(--line)}
td .facts{margin:0}
td .facts li:first-child{border-top:0;padding-top:0}
.chips{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.chip{display:inline-block;border:1px solid var(--line);padding:4px 8px;font-size:.82rem;line-height:1.4;text-decoration:none}
.chip:hover{border-color:var(--red)}

.pairs{display:grid;grid-template-columns:minmax(0,180px) minmax(0,1fr);gap:0 20px;margin:12px 0 0}
.pairs dt,.pairs dd{padding:10px 0;border-top:1px solid var(--line)}
@media (max-width:640px){.pairs{grid-template-columns:minmax(0,1fr)}.pairs dt{padding-bottom:0}.pairs dd{border-top:0;padding-top:4px}}

.steps{list-style:none;padding:0;margin-top:18px}
.steps > li{padding:14px 0;border-top:1px solid var(--line)}
.steps .at{font-weight:600}
.result{font:600 .72rem/1.5 var(--mono);text-transform:uppercase;letter-spacing:.06em;border:1px solid currentColor;padding:1px 6px;margin-left:8px;white-space:nowrap}
.r-pass .result{color:var(--green)}
.r-stop .result{color:var(--bg);background:var(--red);border-color:var(--red)}
.steps .chips{margin-top:10px}
.chk{border-top:1px solid var(--line)}
.chk[open]{background:var(--wash)}
.chk > summary{display:grid;grid-template-columns:56px minmax(0,1fr) 72px 220px;gap:4px 12px;align-items:baseline;padding:10px 8px;cursor:pointer}
.chk > summary b{font-family:var(--mono);font-weight:600}
.chk > summary b::after{content:" +";color:var(--muted)}
.chk[open] summary b::after{content:" \\2212"}
.chk .pairs{margin:0;padding:0 8px 8px 76px}
.fail{font:600 .72rem/1.5 var(--mono);text-transform:uppercase;letter-spacing:.06em}
.fail.Block{color:var(--red)}
.aps{font:500 .72rem/1.5 var(--mono);color:var(--muted)}
.ap + .ap::before{content:"\\00b7  "}
@media (max-width:700px){.chk > summary{grid-template-columns:56px minmax(0,1fr)}.chk > summary .fail,.chk > summary .aps{grid-column:2}.chk .pairs{padding-left:8px}}

.tbl{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:.95rem}
th,td{text-align:left;vertical-align:top;padding:10px 16px 10px 0;border-bottom:1px solid var(--line)}
thead th{border-bottom-color:var(--rule)}
tbody th{font-weight:600}
.cov th,.cov td:nth-child(2){width:30%}
.plat th{width:22%}
.plat td:nth-child(2){width:20%}
.codes{display:block;margin-top:4px}
.code{font:500 .72rem/1.5 var(--mono);color:var(--muted);margin-right:8px}
.owasp{columns:2;column-gap:40px}
@media (max-width:720px){.cov thead,.plat thead{display:none}.cov tr,.cov th,.cov td,.plat tr,.plat th,.plat td{display:block;width:auto!important}.cov tr,.plat tr{border-bottom:1px solid var(--rule);padding:10px 0}.cov th,.cov td,.plat th,.plat td{border:0;padding:4px 0}.cov td:nth-child(3)::before{content:"Can still get through: ";font-weight:600}.plat td:nth-child(2)::before{content:"Works on: ";font-weight:600}.owasp{columns:1}}

footer{padding-top:28px;font-size:.88rem;color:var(--muted)}
footer h2{font-size:1rem;margin:0}
.ai-note{display:grid;grid-template-columns:auto minmax(0,1fr);gap:4px 14px;margin-bottom:22px}
.ai-note b{color:var(--ink)}
[id]{scroll-margin-top:16px}
"""

SCRIPT = """
function reveal(target) {
  for (let detail = target?.closest('details'); detail; detail = detail.parentElement.closest('details')) {
    detail.open = true;
  }
}

function followHash() {
  const target = document.getElementById(location.hash.slice(1));
  reveal(target);
  target?.scrollIntoView({behavior: 'instant'});
}

document.addEventListener('click', (event) => {
  if (event.defaultPrevented || event.button || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
  const link = event.target.closest('a[href^="#"]');
  if (link) reveal(document.getElementById(link.hash.slice(1)));
});

window.addEventListener('hashchange', followHash);
if (location.hash) requestAnimationFrame(followHash);
"""


def build():
    """Return (page text before section links are added, list of (basis, statement))."""
    _statements.clear()
    body = intro()
    references = (
        ("Stage-by-stage instructions", process()),
        ("Reassessment triggers", change()),
        ("Risk tiers and approval record", decide()),
        ("Checklist and scanning tools", checks()),
        ("Worked examples", cases()),
        ("Coverage and platform limits", coverage() + platform()),
    )
    body += "\n".join(
        f'  <details class="reference"><summary>{esc(title)}</summary>{content}  </details>'
        for title, content in references
    )
    body += """
    <p class="related">
      <a href="mcp-security.html#h-enterprise-controls">MCP Security: enterprise controls</a>
      <a href="mcp-governance-microsoft.html#h-controls">MCP governance on Microsoft: controls</a>
    </p>
  </main>
"""
    body += footer(body)
    page = f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>MCP server intake</title>
<meta name="description" content="Four steps to screen, assess, approve and monitor an MCP server, with detailed checks and reassessment triggers.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,600..800&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;family=Public+Sans:ital,wght@0,400;0,600;1,400&amp;display=swap">
<style>{STYLE}</style>
</head>
<body>

<div class="page">
  <div class="top"><a href="index.html">Kim Syversen</a><span>Current as of <time datetime="{D.CURRENT_AS_OF}">{D.CURRENT_AS_OF_TEXT}</time></span></div>
{body}</div>
<script>{SCRIPT}</script>
</body>
</html>
"""
    return "\n".join(line.rstrip() for line in page.split("\n")), list(_statements)


def cell(text):
    return text.replace("|", "\\|").replace("\n", "<br>")


def uncell(text):
    return text.replace("<br>", "\n").replace("\\|", "|")


def read_ledger():
    """Return {(basis, statement): verdict} from the fact check."""
    if not LEDGER.exists():
        return {}
    text = LEDGER.read_text(encoding="utf-8")
    if BEGIN not in text:
        return {}
    rows = {}
    for line in text.split(BEGIN)[1].split(END)[0].splitlines():
        parts = [p.strip() for p in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(parts) == 4 and parts[0].isdigit():
            rows[(uncell(parts[1]), uncell(parts[2]))] = parts[3]
    return rows


def write_ledger(statements):
    old = read_ledger()
    table = ["| # | Basis | Statement | Verdict |", "|---|---|---|---|"]
    table += [f"| {n} | {cell(b)} | {cell(t)} | {old.get((b, t), '')} |"
              for n, (b, t) in enumerate(statements, 1)]
    block = BEGIN + "\n" + "\n".join(table) + "\n" + END
    text = LEDGER.read_text(encoding="utf-8") if LEDGER.exists() else "# MCP server intake: fact check\n\n" + BEGIN + END + "\n"
    text = text.split(BEGIN)[0] + block + text.split(END)[1]
    LEDGER.write_text(text, encoding="utf-8")


def main(argv):
    page, statements = build()
    PAGE.write_text(add_anchors(page), encoding="utf-8")
    if "--ledger" in argv:
        write_ledger(statements)
    print(f"{PAGE.name} written, {len(statements)} statements")


if __name__ == "__main__":
    main(sys.argv[1:])
