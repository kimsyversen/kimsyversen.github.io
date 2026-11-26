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


PHASES = (
    ("Screen the request", (
        ("Log the request", "Owner, purpose, data and access", "Name the person responsible. List the task, the data it needs and any changes the server should be allowed to make.", (("Request details", "stage-request"),)),
        ("Check the approved catalog", "Reuse a server if it meets the need.", "Compare the request with the existing approval. If the task needs broader access, send that change for review before granting it.", (("Approval record", "record"), ("Permission changes", "trigger-permissions"))),
        ("Verify the publisher", "Match the package or URL to vendor documentation.", "Start at the publisher's own site. Follow its link to the package, image or endpoint and check the exact name and owner.", (("Publisher checks", "h-checks-screen"),)),
    ), ("Before downloading or connecting", "Complete the desk checks before fetching a new artifact or contacting a candidate endpoint.", "stage-screen")),
    ("Assess the server", (
        ("Pin or record the server", "Pin local artifacts. Record the remote URL.", "For a package or image, record the version, digest and locked dependencies. For a hosted service, verify the endpoint and obtain evidence from its operator.", (("Artifact checks", "stage-pin"), ("Remote operator evidence", "check-H9"))),
        ("Scan and review", "Check for malware, vulnerabilities and excessive access.", "Scan local files without installing or starting the server. For a remote service, review the operator's scan evidence. Compare tool descriptions, instructions and requested permissions with the stated task.", (("Scan checks", "stage-scan"), ("Tool and permission review", "stage-review"))),
        ("Test in a sandbox", "Use test data and disposable credentials.", "Make the first connection or launch in isolation. Capture the tools and other metadata the client sees. Check observed file and network access against the request.", (("Sandbox procedure", "stage-sandbox"),)),
    ), ("Clear all blocking findings", "Keep the candidate out of production until every blocking check passes. Record how each finding was resolved.", "checks")),
    ("Approve and release", (
        ("Get an independent decision", "Use the approver for the risk tier.", "Assign the tier from the server's highest-risk capability. Give the designated approver the findings and proposed limits before rollout.", (("Risk tiers and approvers", "tiers"),)),
        ("Record what was approved", "Save the configuration, access limits and expiry.", "Record the reviewed artifact or endpoint, tool definitions, permissions, owner, approver and review date. Keep this baseline for later comparisons.", (("Example approval record", "record"),)),
        ("Release to a small group", "Enforce the approved configuration.", "Start with a limited pilot. Confirm the client applies the approved access limits and that the team can disable or roll back the server before widening access.", (("Release checks", "stage-release"), ("Platform controls", "platform"))),
    ), ("Release only with approval", "Release only the configuration covered by the decision. Keep a held or rejected candidate out of use.", "stage-decide")),
    ("Watch for changes", (
        ("Compare with the approval record", "Check tool definitions and permissions.", "Compare the live tool list, descriptions and access with the saved baseline. Hold newly exposed capabilities until the affected checks pass.", (("Tool changes", "trigger-surface"), ("Permission changes", "trigger-permissions"))),
        ("Track vulnerability advisories", "Check dependencies and vendor notices.", "Match alerts to the deployed version and its dependencies. For a hosted service, ask the operator whether the deployed service is affected.", (("Advisory response", "trigger-advisory"),)),
        ("Respond to suspected compromise", "Suspend access and investigate.", "Disable access, preserve relevant logs and identify affected installations. Revoke exposed credentials and investigate before restoring service.", (("Incident response", "trigger-incident"), ("Malicious package or publisher takeover", "trigger-malicious"))),
    ), ("Renew or retire before approval expires", "Have the owner confirm the need and the approver renew the record. Remove access when approval ends.", "trigger-expiry")),
)


def disclosure(title, hint, guidance, links, cls):
    refs = " ".join(f'<a href="#{target}">{esc(label)}</a>' for label, target in links)
    subtitle = f'<small>{say(hint)}</small>' if hint else ""
    return (f'<details class="{cls}"><summary><strong>{esc(title)}</strong>{subtitle}</summary>'
            f'<div class="guidance"><p>{say(guidance)}</p><div class="refs">{refs}</div></div></details>')


def intro():
    cards = []
    for n, (title, actions, gate) in enumerate(PHASES, 1):
        rows = "".join(disclosure(*action, "action") for action in actions)
        label, guidance, target = gate
        gate_html = disclosure(label, "", guidance, (("Decision criteria", target),), "gate")
        cards.append(f'<li class="phase p{n}"><span class="number">0{n}</span><h3>{esc(title)}</h3>{rows}{gate_html}</li>')
    hold = disclosure("Hold or reject", "Resolve blockers or record why you declined.", "For a hold, assign each blocker to an owner and repeat the failed checks. For a rejection, record the decision and stop the rollout.", (("Decision outcomes", "h-decisions"),), "hold")
    loop = disclosure("When something changes, rerun the affected checks", "", "Use the change type to decide which checks to repeat and whether the current deployment can stay in use during review.", (("Reassessment triggers", "changes"),), "loop")
    return f"""
  <header class="hero">
    <h1>MCP server intake</h1>
    <p class="lede">Local packages, containers and remote endpoints</p>
  </header>
  <main>
  <section id="start-here">
    <h2 class="sr-only" id="h-start-here">Start here</h2>
    <ol class="flow">{''.join(cards)}</ol>
    <div class="branches"><div class="withheld"><span>Approval withheld</span>{hold}</div>{loop}</div>
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
.page{max-width:1720px}
.hero{padding:22px 0 14px;border-bottom:1px solid var(--line)}
.hero h1{font-family:Georgia,serif}
:root{--bg:#f7f5ef;--ink:#162533;--line:#d5dbd7;--muted:#485967;--panel:#fff;--arrow:#63747c}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
.flow,.branches{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));column-gap:clamp(18px,2.6vw,46px)}
.flow{list-style:none;padding:0}
.phase,.hold{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:clamp(14px,1.45vw,26px)}
.phase{position:relative;display:flex;flex-direction:column;min-width:0}
.p1{--accent:#994323;--tint:#f7ebe1}
.p2{--accent:#294c9c;--tint:#ebeffb}
.p3{--accent:#11664a;--tint:#e3f1e9}
.p4,.branches{--accent:#783c78;--tint:#f3eaf3}
.number,.gate,.loop{background:var(--tint);color:var(--accent);border-radius:6px}
.number{align-self:flex-start;padding:3px 10px;font-weight:700;font-size:.85rem}
.phase h3{font-size:clamp(1.25rem,1.65vw,1.85rem);margin:12px 0 4px;padding-bottom:14px;border-bottom:1px solid var(--line)}
.phase h3 a.sec-link::after{display:none}
.phase:not(:last-child)::after{content:"";position:absolute;left:100%;top:64px;width:clamp(18px,2.6vw,46px);height:12px;background:var(--arrow);clip-path:polygon(0 42%,74% 42%,74% 0,100% 50%,74% 100%,74% 58%,0 58%)}
.flow summary,.branches summary,.library>summary{cursor:pointer}
.action{flex:1;padding:4px 0}
.action summary,.gate summary,.branches summary{position:relative;list-style:none;padding:8px 22px 8px 0;line-height:1.35}
.flow summary::-webkit-details-marker,.branches summary::-webkit-details-marker{display:none}
.flow summary::after,.branches summary::after{content:"+";position:absolute;right:4px;top:9px;color:var(--accent);font-weight:700}
.flow details[open]>summary::after,.branches details[open]>summary::after{content:"−"}
summary:hover strong{text-decoration:underline;text-underline-offset:3px}
summary small{display:block;color:var(--muted);font-size:.88rem;margin-top:4px}
.gate,.loop{font-size:.87rem}
.gate{margin-top:12px}
.gate summary,.loop summary{text-align:center;padding-left:18px}
.guidance{padding:6px 0 12px;font-size:.94rem;color:var(--ink)}
.refs{display:flex;flex-wrap:wrap;gap:4px 16px;margin-top:10px}
.gate .guidance,.loop .guidance{padding:4px 12px 12px}
.branches{position:relative;padding-bottom:4px}
.withheld{grid-column:3;position:relative;padding-top:16px;color:#9b3229}
.withheld>span{display:block;margin:0 0 12px 16%;font-weight:600;font-size:.86rem}
.withheld::before{content:"↓";position:absolute;left:9%;top:0;height:47px;display:flex;align-items:flex-end;border-left:2px solid currentColor;text-indent:-.52em;line-height:.8}
.hold{background:#faebe7;border-color:#e6c2b9;padding:5px 14px;--accent:#9b3229}
.loop{grid-column:2/5;justify-self:center;margin-top:22px;z-index:1;max-width:76%}
.loop summary{padding-right:26px}
.branches::before{content:"";position:absolute;inset:0 calc((100% - 3 * clamp(18px,2.6vw,46px)) / 8) 20px calc(37.5% - clamp(18px,2.6vw,46px) / 8);border:2px dashed var(--accent);border-top:0;pointer-events:none}
.branches::after{content:"▲";position:absolute;left:calc(37.5% - clamp(18px,2.6vw,46px) / 8);transform:translateX(-42%);top:-5px;color:var(--accent)}
.library{border-block:1px solid var(--line);padding:12px 0}
.library>summary{font-weight:700}
.library,.related,footer{max-width:1000px;margin-inline:auto}
@media(max-width:950px){
.flow,.branches{display:block}
.phase+.phase{margin-top:26px}
.phase:not(:last-child)::after{top:100%;left:50%;width:26px;transform-origin:left center;transform:translateY(-50%) rotate(90deg)}
.branches::before,.branches::after,.withheld::before{display:none}
.withheld>span{margin-left:0}
.loop{max-width:none;margin-top:12px}
}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--panel:#202526;--bg:#151a1d;--ink:#eef1f2;--muted:#c1cbcf}
.p1{--accent:#ffbd99;--tint:#452f23}.p2{--accent:#b5caff;--tint:#293650}.p3{--accent:#a5e4c6;--tint:#203e34}.p4,.branches{--accent:#e4bae6;--tint:#3c2c41}
.hold{background:#432e2b;--accent:#ffb4a7}.withheld{color:#ffb4a7}}
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
    body += '<details class="library"><summary>Full reference guide</summary>'
    body += "\n".join(
        f'  <details class="reference"><summary>{esc(title)}</summary>{content}  </details>'
        for title, content in references
    )
    body += """
    </details>
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
