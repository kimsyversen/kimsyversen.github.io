"""Build mcp-governance-microsoft.html.

Usage: python3 -I scripts/build-mcp-governance.py

Head, style, marker defs and the Made with AI note are cut from the finished
governance summary page so both pages look alike. The build stops if a marker is
missing. Quotes live in mcp_governance_evidence.py.

The page has two paths. Blocks with class opt-safe show only on the safe path.
Blocks with class opt-preview show only on the preview-enabled path. Everything
else shows on both. The preview path is the safe path plus additions.
"""

import html
import re
import sys
from pathlib import Path
from urllib.parse import quote as urlquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from section_anchors import add_anchors  # noqa: E402
from mcp_governance_evidence import CHECKED, IDS, PREVIEW_ONLY, QUOTES, SOURCES  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BASE = "enterprise-ai-agent-governance-summary.html"
OUT = ROOT / "mcp-governance-microsoft.html"
SRC = (ROOT / "wip" / BASE).read_text(encoding="utf-8")


def cut(start, end):
    if SRC.count(start) != 1:
        sys.exit(f"marker not unique or missing ({SRC.count(start)}): {start[:60]!r}")
    i = SRC.index(start)
    j = SRC.find(end, i + len(start))
    if j < 0:
        sys.exit(f"end marker missing: {end[:60]!r}")
    return SRC[i:j + len(end)]


HEAD = SRC[:SRC.index("<style>")]
STYLE = cut("<style>", "</style>")
MARKERS = SRC[SRC.index("<body>") + 6:SRC.index('<div class="page" id="top">')]
AI_NOTE = cut('<p class="ai-note">', "</p>")

TITLE = "MCP Governance in a Microsoft ecosystem"
DESC = "A short design to make Azure API Management the only way to reach a company MCP server, as a released-only design and as a design with preview built on top of it."
HEAD = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", HEAD, flags=re.S)
HEAD = re.sub(r'(<meta name="description" content=")[^"]*(")', rf"\g<1>{DESC}\2", HEAD)

SAFE_COUNT = len(QUOTES) - len(PREVIEW_ONLY)
PV_COUNT = len(PREVIEW_ONLY)

# Own rules for the path switch. Appended after the shared style so the look stays the same.
OPT_CSS = """<style>
/* Path switch. Blocks tagged opt-safe or opt-preview show on one path only. */
body[data-opt="safe"] .opt-preview{display:none!important}
body[data-opt="preview"] .opt-safe{display:none!important}
.toc{display:flex;align-items:center;gap:12px}
.toc ul{flex:1;min-width:0}
.seg-wrap{display:flex;flex:none;align-items:center;gap:10px;margin:5px 0}
.seg-lbl{font:600 0.72rem/1 var(--body);letter-spacing:0.05em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.seg{display:flex;flex:none}
.intro{grid-template-columns:1fr}
.seg button{font:600 0.72rem/1 var(--body);letter-spacing:0.05em;text-transform:uppercase;padding:7px 9px;border:1px solid var(--ink);background:none;color:var(--ink);cursor:pointer;white-space:nowrap}
.seg button + button{border-left:0}
.seg button:hover{background:var(--hover)}
.seg button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
.fig-scroll pre.ascii{margin:0;font:0.8rem/1.3 var(--mono);white-space:pre;min-width:max-content;padding:2px 0}
pre.ascii .stop{color:var(--red)}
pre.ascii .ttl{font-weight:700}
.ev-fold > summary{cursor:pointer;font:600 0.95rem/1.4 var(--body);padding:8px 0;list-style-position:inside}
.ev-fold[open] > summary{margin-bottom:8px}
.sub3{margin-top:6px}
.sub3 h3{font:700 1.02rem/1.35 var(--display);font-stretch:105%;margin:0 0 4px}
.steps{margin:0;padding-left:1.4rem;display:grid;gap:8px}
/* Text uses the full page width. The shared style caps these at 36 to 56rem and sets text-wrap:balance, which shortens every line to about half of the 1200px page. */
.lead,.decision p,.blk > .sub,.goal,.body > p,figcaption,.ans p,.q-note{max-width:none}
p,li,td,th,dd,summary,figcaption,h4{text-wrap:wrap}
/* Fact check table: narrow Id and date columns so the quote gets the room. */
.src th:nth-child(1),.src td:nth-child(1){width:4.5rem}
.src th:nth-child(3),.src td:nth-child(3){width:22%}
.src th:nth-child(4),.src td:nth-child(4){width:7.5rem}
/* On a phone only the switch stays pinned. The contents links scroll away with the page. */
@media (max-width:640px){.toc{display:contents}.toc ul{margin-top:34px;border-top:1px solid var(--rule)}.seg-wrap{position:sticky;top:0;z-index:5;background:var(--bg);margin:0;padding:8px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}}
@media print{.seg-wrap{display:none}}
</style>
<noscript><style>body[data-opt] .opt-preview,body[data-opt] .opt-safe{display:revert!important}.seg-wrap{display:none!important}</style></noscript>"""

SCRIPT = """<script>
(function(){
  // mark the section in view in the contents bar
  if('IntersectionObserver' in window){
    var links = {};
    document.querySelectorAll('.toc a').forEach(function(a){ links[a.getAttribute('href').slice(1)] = a; });
    var io = new IntersectionObserver(function(es){
      es.forEach(function(e){
        if(!e.isIntersecting) return;
        Object.keys(links).forEach(function(k){
          links[k].classList.remove('on');
          links[k].removeAttribute('aria-current');
        });
        var a = links[e.target.id];
        if(a){ a.classList.add('on'); a.setAttribute('aria-current','location'); }
      });
    }, {rootMargin:'-20% 0px -70% 0px'});
    Object.keys(links).forEach(function(k){ var t = document.getElementById(k); if(t) io.observe(t); });
  }

  // choose between the released-only path and the with-preview path; the choice lives in ?path=
  var body = document.body;
  var btns = document.querySelectorAll('[data-opt-btn]');
  function urlFor(o){
    var u = new URL(location.href);
    if(o === 'safe'){ u.searchParams.delete('path'); } else { u.searchParams.set('path', o); }
    return u.pathname + u.search + u.hash;
  }
  function setOpt(o, keepUrl){
    body.setAttribute('data-opt', o);
    btns.forEach(function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-opt-btn') === o ? 'true' : 'false'); });
    if(!keepUrl){ try{ history.replaceState(null, '', urlFor(o)); }catch(e){} }
  }
  function jump(el){ try{ el.scrollIntoView({behavior:'instant', block:'start'}); }catch(e){ el.scrollIntoView(); } }
  function followHash(){
    var id = location.hash.slice(1);
    if(!id) return;
    try{ id = decodeURIComponent(id); }catch(e){}
    var el = document.getElementById(id);
    if(!el) return;
    var fold = el.closest('details');
    if(fold && !fold.open){ fold.open = true; jump(el); }
    var other = body.getAttribute('data-opt') === 'safe' ? 'preview' : 'safe';
    if(el.closest('.opt-' + other)){ setOpt(other); jump(el); }
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){ setOpt(b.getAttribute('data-opt-btn')); }); });
  var m = /[?&]path=(safe|preview)(?:&|$)/.exec(location.search);
  setOpt(m ? m[1] : 'safe', true);
  followHash();
  window.addEventListener('hashchange', followHash);
  // the browser can cancel the first jump while the page is still loading; repeat it once after load
  window.addEventListener('load', function(){
    var h = decodeURIComponent(location.hash.slice(1));
    var el = h && document.getElementById(h);
    if(el && el.closest('details.ev-fold')){ var f = el.closest('details'); f.open = true; jump(el); }
  });
  document.addEventListener('click', function(e){
    var a = e.target.closest && e.target.closest('a[href^="#ev-"]');
    var d = a && document.getElementById('evidence-details');
    if(d && !d.open) d.open = true;
  });
})();
</script>"""


# ---- helpers -------------------------------------------------------------
def _links(keys):
    ids = sorted((IDS[k] for k in keys), key=lambda v: int(v[1:]))
    return " ".join(f'<a class="ev" href="#ev-{v}">{v}</a>' for v in ids)


def ev(*keys):
    """Evidence links for content shown on both paths. Stops on a quote that only the preview path shows."""
    hidden = [k for k in keys if k in PREVIEW_ONLY]
    if hidden:
        sys.exit(f"shared content links preview-only quotes: {hidden}")
    return _links(keys)


def evp(*keys):
    """Evidence links for content inside an opt-preview block."""
    return _links(keys)


def tg(cls, text):
    return f'<span class="tg {cls}">{text}</span>'


UNV = tg("u", "unverified")
INF = tg("i", "inference")
REC = tg("r", "recommendation")
PRE = tg("pv", "preview")


def frag(q):
    """Text fragment for a link that opens the source at the quote."""
    words = q.split()
    if len(q) <= 90 and "'" not in q:
        text = urlquote(q, safe="").replace("-", "%2D")
        return f"#:~:text={text}"
    apos = [n for n, w in enumerate(words) if "'" in w]
    start = words[:6]
    if apos and apos[0] < 6:
        start = words[:apos[0]]
    end = words[-6:]
    if apos and apos[-1] >= len(words) - 6:
        end = words[apos[-1] + 1:]
    enc = lambda ws: urlquote(" ".join(ws), safe="").replace("-", "%2D")  # noqa: E731
    return f"#:~:text={enc(start)},{enc(end)}"


def table(head, rows, cls="tbl"):
    """A row is a list of cells, or (class, cells) to tag it for one path."""
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = []
    for r in rows:
        rc = ""
        if isinstance(r, tuple):
            rc, r = r
        attr = f' class="{rc}"' if rc else ""
        trs.append(f"<tr{attr}>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    body = "\n".join(trs)
    return f'<div class="tbl-wrap"><table class="{cls}">\n<thead><tr>{th}</tr></thead>\n<tbody>\n{body}\n</tbody>\n</table></div>'


def safe(x):
    return f'<span class="opt-safe">{x}</span>'


def prev(x):
    return f'<span class="opt-preview">{x}</span>'


# ---- masthead ------------------------------------------------------------
MAST = f"""
  <a class="skip" href="#main-content">Skip to content</a>
  <header class="mast">
    <div class="meta"><span>Design · Microsoft stack · MCP</span><span>Documentation checked 11 Nov 2026</span></div>
    <h1>MCP Governance in a Microsoft ecosystem</h1>
    <div class="intro">
      <p class="lead">A proposed design for governing MCP servers across GitHub Copilot, VS Code, Foundry, Copilot Studio and Microsoft 365 Copilot.</p>
    </div>
    <nav aria-label="Start by role">
      <ul class="routes">
        <li><a href="#design">Platform and security owners</a><p>See the design and its controls.</p></li>
        <li><a href="#env">Architects</a><p>See what works in each Microsoft environment.</p></li>
        <li><a href="#open">Decision makers</a><p>Released only is the baseline. Compare it with the preview design, then read the open questions.</p></li>
      </ul>
    </nav>
  </header>

  <nav class="toc" aria-label="Contents">
    <ul>
      <li><a href="#design">Design</a></li>
      <li><a href="#controls">Controls</a></li>
      <li><a href="#env">Environments</a></li>
      <li><a href="#tests">Tests</a></li>
      <li><a href="#order">Order</a></li>
      <li><a href="#gaps">Gaps</a></li>
      <li class="opt-preview"><a href="#fallback">Fallback</a></li>
      <li><a href="#open">Open questions</a></li>
      <li><a href="#guardrails">Guardrails</a></li>
      <li><a href="#evidence">Fact check</a></li>
    </ul>
    <div class="seg-wrap"><span class="seg-lbl" id="seg-lbl">Select design</span>
    <div class="seg" role="group" aria-labelledby="seg-lbl">
      <button type="button" data-opt-btn="safe" aria-pressed="true">Released only</button>
      <button type="button" data-opt-btn="preview" aria-pressed="false">With preview</button>
    </div></div>
  </nav>
"""

# ---- parts table ---------------------------------------------------------
def pv(text, *keys):
    """A With-preview cell. The released view shows the text; the preview view adds the quote links."""
    return safe(text) + prev(text + (" " + evp(*keys) if keys else ""))


def part(name, group, desc, rel, prv):
    return [f'{name}<span class="rt">{group}</span>', desc, rel, prv]


def control_label(anchor, title, objective):
    return f'<span id="ctrl-{anchor}">{title}</span><span class="rt">{objective}</span>'


def control_link(anchor, title):
    return f'<a href="#ctrl-{anchor}">{title}</a>'


def ascii_fig(name):
    raw = (ROOT / f"mcp-governance-microsoft.figure-{name}.txt").read_text(encoding="utf-8")
    for tag in ("red", "b"):
        if raw.count(f"[{tag}]") != raw.count(f"[/{tag}]"):
            sys.exit(f"unbalanced [{tag}] markers in figure {name}")
    out = html.escape(raw.rstrip("\n"), quote=False)
    out = out.replace("[red]", '<span class="stop">').replace("[b]", '<span class="ttl">')
    return out.replace("[/red]", "</span>").replace("[/b]", "</span>")


PARTS_ROWS = [
    part("Approved list in Git", "Source of truth",
         "Reviewed record of approved and denied MCP servers.",
         "Yes", "Yes"),
    part("Sync pipeline", "Source of truth",
         "On merge, writes the list to each policy target. Proposed work; not built yet. See <a href=\"#ctrl-pipeline\">Policy sync, pipeline</a>.",
         "Yes", "Yes"),
    part("Policy targets", "Targets",
         "GitHub managed settings: a commit to the .github-private repository (<a href=\"#ctrl-pipeline\">pipeline</a>). Copilot Studio: the Power Platform API (<a href=\"#ctrl-power-platform\">unverified for MCP</a>). Foundry: an allowed tool list on each MCP tool (<a href=\"#ctrl-foundry\">pipeline not tested</a>). Microsoft 365 Copilot: connectors set by hand (<a href=\"#ctrl-m365\">no pipeline</a>).",
         "Yes", "Yes"),
    part("MCP clients", "Callers",
         "Copilot Studio, VS Code, Foundry agents, GitHub Copilot and Microsoft 365 Copilot.",
         "Yes", "Yes"),
    part("Client controls", "Enforcement",
         "Managed URL policies and, on Windows, outbound firewall rules where applicable. They sit on the device, so they do not cover Microsoft 365 Copilot. See <a href=\"#ctrl-m365\">Policy sync, Microsoft 365 Copilot</a>.",
         "Yes", "Yes"),
    part("Gateway product", "Gateway",
         "API Management in the released-only path; the preview path adds Azure AI Gateway capabilities.",
         "API Management", "Azure AI Gateway added"),
    part("Company MCP server, gateway only", "Backend",
         "Company MCP server; only the gateway may reach it.",
         "Yes", "Yes"),
    part("Agent 365 gateway integration", "Preview admin view",
         "In the preview design, the Microsoft 365 admin center shows the organization agent registry, the tools registry with MCP server status, and MCP server registration requests. Connect the gateway to discover its servers.",
         "No", "New"),
    part("Other preview additions", "Optional controls",
         "Tool threat protection, Foundry gateway routing, and optional remote-server filtering. Details are in Controls.",
         "No", "New"),
]

PARTS = f"""
    <div class="sub3" id="parts">
      <h3>Parts of the design</h3>
      <p class="q-note">This is a component map. Controls below contain the implementation requirements, product limits and supporting evidence. New marks a preview addition.</p>
      {table(["Part", "Role in the flow", "Released only", "With preview"], PARTS_ROWS)}
    </div>
"""

PLANES = f"""
    <div class="sub3" id="planes">
      <h3>Control planes</h3>
      <p class="q-note">Each row is an admin surface for policy or visibility. Map the approved inventory into policy targets. Registry views help administrators inspect agents, servers and requests, but visibility alone does not enforce access. {REC}</p>
      {table(["Control plane", "Administered in", "What it governs for MCP in this design", "Control"], [
        ["Power Platform", f"Power Platform admin center {UNV}", "MCP connectors that Copilot Studio agents may use.", control_link('power-platform', 'Policy sync, Power Platform')],
        ["GitHub Enterprise", f"Managed settings file in the .github-private repository {ev('gh-file')}", "MCP servers that VS Code and GitHub Copilot may use.", f"{control_link('client', 'Client allowlist')}; {control_link('pipeline', 'Policy sync, pipeline')}"],
        ["Microsoft Foundry", f"Foundry portal {UNV}", "Tools each Foundry agent may call on an MCP server.", control_link('foundry', 'Policy sync, Foundry')],
        ["Microsoft 365 Copilot", f"Microsoft 365 admin center {ev('m365-admin')}", "MCP servers offered to Microsoft 365 Copilot as federated connectors.", control_link('m365', 'Policy sync, Microsoft 365 Copilot')],
        ["Microsoft 365 agent inventory", f"Agents > All agents > Registry {ev('a365-agent-all')}", f"Organization-wide agent inventory. Agent details include tools when the platform reports them, but the metadata is read-only and incomplete for some agents {ev('a365-agent-readonly', 'a365-agent-incomplete')}.", "Visibility only; agent approval and lifecycle are not this MCP server control."],
        ["Microsoft Agent 365 tools", f"Agents > Tools > Registry and Requests {ev('a365-tools-overview', 'a365-tools-tabs')}", f"Registry shows MCP server status as Available or Blocked {ev('a365-tools-status')}. Requests (preview) reviews server registrations. {safe('Not used in this design.')}{prev('Admin view and blocking.')}", safe("None") + prev(f"{control_link('a365', 'Agent 365 gateway integration')}; {control_link('byo', 'Agent 365 BYO server route')}; <a href=\"#approval-workflow\">Approval and denial workflow</a>")],
        ["Azure API Management", f"Azure {INF}", "The one door to the company MCP server, for every client.", f"{control_link('gateway', 'Gateway')}; {control_link('backend', 'Backend isolation')}; {control_link('identity', 'Identity')}"],
        ["Device management", f"Intune and VS Code policy {INF}", "URL allowlist and Windows outbound rules on managed devices.", f"{control_link('client', 'Client allowlist')}; {control_link('windows', 'Windows outbound limits')}; {control_link('stdio', 'Local stdio servers')}"],
      ])}
      <p class="q-note">{UNV} marks an admin surface name taken from the control plane list this page was checked against, not from a quoted source. {INF} marks interpretation by AI. The agent inventory provides visibility; approval and lifecycle for agents are separate from this page's MCP server workflow.</p>
    </div>
    <div class="sub3 opt-preview" id="approval-workflow">
      <h3>Approval and denial workflow</h3>
      <p>Use two gates: the company's reviewed inventory change, then Microsoft's tenant approval for the preview Agent 365 server route. An approval in one gate does not replace the other. {REC}</p>
      <figure>
        <p class="fig-hint">Approval and denial path for a company MCP server.</p>
        <div class="fig-scroll" tabindex="0" role="region" aria-label="MCP server approval workflow, horizontally scrollable">
<pre class="ascii" role="img" aria-label="A developer proposes a server in the reviewed Git inventory. A security reviewer approves or rejects the pull request. Rejection stops the request and is recorded as denied. After approval and merge, the developer registers the server through the Agent 365 preview flow. An administrator reviews the request in Microsoft 365 admin center Requests preview and approves or rejects it. Rejection leaves the server unavailable and the reason is recorded. Approval is followed by Microsoft Entra tenant consent; only then does the server become Available in the tools registry. The admin records the approved server and consent in the inventory, applies target-specific access controls, and monitors calls. A later deny blocks the server in the tools registry and updates the inventory and other policy targets.">{ascii_fig("approval")}</pre>
        </div>
        <figcaption class="q-note">The Git pull request is the internal source-of-truth decision. The Microsoft 365 admin-center request is a separate product approval for the preview BYO route. Rejecting either stops rollout. The registry status is Available only after admin approval and required Microsoft Entra consent. {ev('a365-tools-approve', 'a365-tools-consent')} {evp('pv-byo-approval')}</figcaption>
      </figure>
      <ol>
        <li><strong>Propose.</strong> The requester adds the MCP server URL, owner, authentication, declared tools, permissions and risk notes to the approved inventory. The developer registration must use the same server and gateway endpoint.</li>
        <li><strong>Review internally.</strong> Review the server and each tool, identity path, data access, owner and rollback plan. Merge the pull request only if approved. If denied, record the reason and keep the server out of every target.</li>
        <li><strong>Submit for Microsoft approval.</strong> For the Agent 365 BYO preview route, the developer registers the server. An AI Administrator or Global Administrator reviews its requester, publisher, server information and declared tools under Agents &gt; Tools &gt; Requests (preview), then approves or rejects it. {ev('a365-tools-role-ai', 'a365-tools-role-global')} {evp('pv-byo-approval')}</li>
        <li><strong>Consent and enable.</strong> After approval, grant the required Microsoft Entra tenant consent. The server becomes available only after consent. Record the consent and resulting Available state in the inventory. {ev('a365-tools-consent', 'a365-tools-status')}</li>
        <li><strong>Limit and monitor.</strong> Restrict access with target-specific policies and backend authorization. Individual tool controls are rolling out for supported Agent 365 servers; BYO server tool-level blocking is planned, so use server-level blocking and gateway/backend authorization for BYO until tool controls are supported. {ev('a365-tools-granular')} {evp('pv-byo-roll', 'pv-a365-ctrl')}</li>
        <li><strong>Reject or revoke.</strong> A rejected request stays unavailable. If an approved server later fails review, block it in the registry, mark it denied in Git, remove it from target allowlists, and verify calls are denied. Microsoft 365 admin actions do not automatically update the other target policies. {REC}</li>
      </ol>
      <p class="q-note">This is the MCP server request queue. Approval of an agent publication is a separate workflow. The All agents registry is an inventory view; its Data &amp; tools details are read-only and may be missing for some agents. {ev('a365-agent-approve', 'a365-agent-request-review', 'a365-agent-readonly', 'a365-agent-incomplete')}</p>
    </div>
"""

# ---- design figures ------------------------------------------------------
# The figures are plain text files beside the page. Edit them, then rebuild.
# [red]...[/red] marks text that means caution, unverified or denied. [b]...[/b] marks a box title.


DESC_SAFE = ("Design target: a Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. "
             "After merge, a pipeline applies the list to three targets: Power Platform policy for Copilot Studio, "
             "GitHub Enterprise managed settings, and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: "
             "Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. The first three pass through "
             "client controls, Windows outbound firewall rules where applicable, API Management and the company MCP server, which only the gateway can reach. "
             "Microsoft 365 Copilot calls API Management from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. A direct call from a client to the server is blocked. "
             "Agent 365 is not drawn: company servers join it through preview features.")
DESC_PREVIEW = ("Design target: the released-only design with preview additions. A Git repository holds the approved and denied MCP servers. "
                "After a reviewed merge, a pipeline applies the list to Power Platform policy for Copilot Studio, "
                "GitHub Enterprise managed settings and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: "
                "Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. "
                "The first three pass through client controls, Windows outbound firewall rules where applicable, Azure AI Gateway with tool threat protection, and a company MCP server that only the gateway can reach. "
                "Microsoft 365 Copilot calls the gateway from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. "
                "A direct call from a client to the server is blocked. Below the gateway, the Microsoft 365 admin view shows the all-agents registry, MCP server status, and the preview requests queue.")

FIGURE = f"""
  <section class="sec" id="design" aria-labelledby="h-design">
    <header class="sh"><h2 id="h-design">The design</h2>
    <p class="goal"><b>In short</b>Keep the company MCP server behind the gateway and limit managed clients to approved servers.{prev(" With preview, add an Agent 365 admin view and optional blocking. Test preview features only in a sandbox.")}&nbsp;{REC}</p>
    <p class="goal"><b>Designs</b>Released only is the target baseline. Use only confirmed released features; keep unverified automation out of production. With preview adds Agent 365 and tool threat protection, for a sandbox only.</p></header>
    <figure class="opt-safe">
      <p class="fig-hint">Scroll the diagram sideways to follow the flow.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="MCP gateway design diagram, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_SAFE}">{ascii_fig("safe")}</pre>
      </div>
    </figure>
    <figure class="opt-preview">
      <p class="fig-hint">Scroll the diagram sideways to follow the flow.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="With-preview MCP gateway design diagram, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_PREVIEW}">{ascii_fig("preview")}</pre>
      </div>
      <figcaption class="q-note">With preview, connect the API Management gateway to Agent 365 and test tool threat protection in a sandbox. The view combines distinct admin pages: Agents &gt; All agents &gt; Registry, and Agents &gt; Tools &gt; Registry or Requests (preview). {ev('a365-agent-all', 'a365-tools-tabs', 'a365-tools-status')} The BYO server route is separate; its limits are listed below.</figcaption>
    </figure>
{PARTS}{PLANES}  </section>
"""

# ---- controls ------------------------------------------------------------
CONTROLS = f"""
  <section class="sec" id="controls" aria-labelledby="h-controls">
    <header class="sh"><h2 id="h-controls">Controls</h2>
    <p class="goal"><b>How to read</b>A means company backend access through the gateway only. B means restricting managed clients to approved MCP servers. These are targets, with coverage limits below. Each documented fact cites a quote.</p></header>
    {table(["Control", "Design requirement", "What Microsoft and GitHub document", "Label"], [
        [control_label("inventory", "Approved inventory", "Objectives A and B"),
         "Keep one list of approved MCP servers in a repository, with address, owner, permitted tools and risk class. Change it only by reviewed pull request. Set client policy from managed settings, not user-editable files. Use device management for device policies where supported.",
         f"GitHub managed settings apply the allow and deny lists to servers in user and repository settings {ev('gh-profiles')}. The proposed pipeline must configure Foundry and Copilot Studio separately. {REC}",
         REC],
        [control_label("pipeline", "Policy sync, pipeline", "Objective B"),
         "On merge of a reviewed change, a pipeline applies the list to each target. Each target gets its own credential, limited to writing that target. The pipeline reports any target it could not update. Manual edits in a target are overwritten or flagged on the next run. Nothing is built yet.",
         f"GitHub managed settings can be hosted on GitHub as a server-managed deployment {ev('gh-deploy')}. They are a file in the .github-private repository, changed by commit and push {ev('gh-file', 'gh-commit')}. Settings refresh within about an hour {ev('gh-refresh')}. Verify propagation. {REC}",
         f"{REC}"],
        [control_label("power-platform", "Policy sync, Power Platform", "Objective B"),
         f"<span id=\"gap-unverified-url-block\"></span>Configure an advanced connector policy for MCP connectors listed in the target environment. Keep classic data policies for custom and HTTP connectors. Use manual configuration until API automation for the actual MCP entry is verified. Do not assume an arbitrary MCP URL is a supported policy entry.",
         f"ACP supports deployment-pipeline automation {ev('pp-pipe')}, MCP server-level blocking but not per-tool blocks {ev('pp-block')}, and connector blocking also blocks dependent MCP tools {ev('studio')}. Custom and HTTP connectors aren't supported {ev('pp-custom')}. The API tutorial lacks an MCP-specific example; verify this path in the target tenant {ev('pp-api')}. {REC}",
         f"{REC}"],
        [control_label("foundry", "Policy sync, Foundry", "Objective B"),
         f"Configure each approved MCP connection with a nonempty allowed tool list. Remove or disable the connection when no tools should be allowed. Validate the pipeline separately. For toolboxes, configure project networking and downstream egress rules; a tool allowlist alone does not restrict which server URLs an agent can use.",
         f"An MCP tool restricts access with a nonempty allowed tool list. An empty list allows every tool {ev('fy-allowed')}. For a Foundry toolbox, its hosting project governs network access {ev('fy-gov')}. Tool connectivity depends on where the downstream service is hosted {ev('fy-tool')}.",
         f"{REC}"],
        [control_label("m365", "Policy sync, Microsoft 365 Copilot", "Objective B"),
         f"<span id=\"gap-m365-by-hand\"></span>Add each approved company MCP server by hand as a custom federated connector that points at the gateway address. Clear the external publisher type unless a server is on the list. Stage each connector to named groups. Record every manual change in the repository.",
         f"Federated connectors use MCP {ev('m365-mcp')}. A custom one starts with an MCP server {ev('m365-server')} and needs an admin role {ev('m365-roles')}. Admins control availability {ev('m365-admin', 'm365-org')}; every setting must allow the user {ev('m365-all')}. Tools can be blocked {ev('m365-toolblock')}. Agent and plugin access has no PowerShell or API option {ev('m365-noapi')}.",
         f"{REC}"],
        [control_label("m365-network", "Microsoft 365 Copilot network path", "Objective A"),
         f"Let the gateway accept the Microsoft 365 Copilot outbound addresses, and still require sign-in. Review the address list on a schedule. Do not count on device controls for this client. {INF} Interpretation by AI: calls leave from the Microsoft cloud, so device URL policy and Windows firewall rules do not see them.",
         f"MCP calls from declarative agents and federated connectors use a fixed set of outbound addresses {ev('m365-ip')}. A server that filters by source address must allow them {ev('m365-ip-allow')}. Allow listing does not replace sign-in or authorization {ev('m365-ip-auth')}. The list can change with seven days' notice {ev('m365-ip-change')}.",
         f"{REC}"],
        [control_label("gateway", "Gateway", "Objective A"),
         "Publish each approved remote MCP endpoint through API Management. Check identity, authorize, rate-limit and log. Scope access by app or workload identity. Confirm the release status of each feature before relying on it.",
         f"For a remote Azure MCP Server, Microsoft suggests API Management as a gateway {ev('gw-consider')}: a single choke point {ev('gw-choke')}. Policies limit rates, restrict tool paths and log requests {ev('gw-policy')}. Clients go through it so the backend is not silently redirected {ev('gw-redirect')}. It can expose REST APIs as MCP servers or pass MCP servers through {ev('pv-apim-mcp')}.",
         REC],
        [control_label("backend", "Backend isolation", "Objective A"),
         "Switch off public access to the backend. Accept inbound calls from the gateway only, over a private path.",
         f"Restrict MCP server connectivity so the gateway is the only permitted caller, or use private networking where supported {ev('iso-restrict')}. Azure Functions offers inbound access restrictions and private endpoints {ev('fn-ar', 'fn-pe')}. The classic Consumption plan has no private endpoints {ev('fn-cons')}. The API Management integration does not automatically route agents through a customer-hosted gateway {ev('iso-nogw')}.",
         REC],
        [control_label("identity", "Identity", "Objective A"),
         "Only the gateway holds a credential or workload identity the backend accepts. Require the backend to validate token audience and the authorized gateway identity; verify that other identities are rejected.",
         f"The gateway can check an Entra ID token {ev('in-entra')} or a subscription key {ev('in-key')} before the request goes on {ev('gw-token')}. It can sign in to the backend with its managed identity {ev('out-mi')}. Checking the token again at the backend is a design choice. {REC}",
         f"{REC}"],
        [control_label("client", "Client allowlist", "Objective B"),
         "Managed clients may use only the MCP addresses on the approved list, which the pipeline writes to GitHub managed settings. Users cannot add their own.",
         f"VS Code policies set an allowlist, a denylist and a managed-only mode {ev('vs-allow', 'vs-deny', 'vs-managed')}. GitHub managed settings match a remote server by URL with wildcards {ev('gh-url')} and block any server that matches no entry {ev('gh-block')}. Not covered: servers in custom agent profiles and the built-in GitHub server {ev('gh-profiles', 'gh-builtin')}. Coverage varies by environment {ev('gh-vary')}.",
         REC],
        [control_label("windows", "Windows outbound limits", "Objective B"),
         "Block direct outbound calls from managed Windows devices to MCP servers that are not approved.",
         f"Intune can set Windows Firewall to block all outbound traffic that matches no rule {ev('ifw-block')}, a setting Microsoft says can be considered for certain highly secure environments {ev('dk-secure')}.",
         f"{REC}"],
        [control_label("stdio", "Local stdio servers", "Objective B"),
         "Limit which local server commands can start, through managed client policy. Add application control, least-privilege accounts and limits on sensitive files and credentials. Treat local administrators, other MCP clients and unmanaged devices as separate bypass risks.",
         f"The client launches a local server as a subprocess {ev('stdio')}. The stdio transport communicates over standard input and standard output {ev('stdio-io')}. GitHub managed settings match the exact command and each argument {ev('gh-cmd')}.",
         REC],
        [control_label("logging", "Logging and checks", "Objectives A and B"),
         "Collect gateway logs and endpoint or client telemetry. Look for unapproved server connections, unexpected MCP processes, failed sign-ins and unusual tool use. Review the approved list on a schedule. Run the acceptance tests.",
         f"Gateway policies can log every request {ev('gw-policy')}.",
         REC],
    ])}
    <div class="sub3" id="approval-boundaries">
      <h3>Approval boundaries and cross-cutting guardrails</h3>
      <p>Keep one reviewed inventory, but translate it into each target's control. A server allowlist, an agent's tool allowlist, and a federated connector audience are different settings. Treat the target's actual policy as the effective control, and record exceptions and sync status. {REC}</p>
      <ul>
        <li><strong>Review capability changes.</strong> Re-review a server when its URL, authentication, permissions, or exposed tools change. Remove tools an agent does not need, and keep Foundry's <code>allowed_tools</code> list nonempty. An empty list permits all tools. {ev('fy-allowed')} {REC}</li>
        <li><strong>Check coverage exceptions.</strong> GitHub's allow and deny lists do not block the built-in GitHub MCP server and do not apply to servers in custom agent profiles. Power Platform blocks MCP servers as a whole, not individual tools. Add separate controls for these gaps. {ev('gh-builtin', 'gh-profiles', 'pp-block')} {REC}</li>
        <li><strong>Enforce identity and authorization at the service.</strong> Require authentication and authorize each request at the gateway and backend. Network allowlisting and a client approval prompt do not grant permission to read or change data. Microsoft says IP allowlisting does not replace authentication or authorization. {ev('m365-ip-auth', 'in-entra', 'out-mi')} {REC}</li>
        <li><strong>Verify and audit the whole path.</strong> Test that an unapproved server, an unapproved tool, and an unauthorized identity are denied. Check that each policy target received the current inventory. Retain gateway logs and review connector activity in Purview where applicable. {ev('gw-policy', 'm365-audit')} {REC}</li>
      </ul>
    </div>
    <div class="sub3 opt-preview">
      <h3>Added with preview&nbsp;{PRE}</h3>
      <p class="q-note">These requirements and limits apply to preview additions. Microsoft says preview features are not meant for production use and may have restricted functionality. {evp('pv-notprod')}</p>
      {table(["Control", "Design requirement", "What Microsoft documents", "Label"], [
        [control_label("a365", "Agent 365 gateway integration", "Visibility, not the boundary"),
         "Connect the API Management gateway so admins can see registered servers and block one. Treat blocking as additional gateway enforcement. It does not replace backend isolation. This is separate from the Agent 365 BYO server route below.",
         f"Agent 365 can discover and govern servers registered with a connected gateway {evp('pv-disc')}. It can block servers {evp('pv-a365-ctrl')}. Tool-level control needs the AI Gateway tier {evp('pv-a365-tier')} and a static allowed-tools list {evp('pv-a365-static')}. v1 tiers are not supported {evp('pv-a365-v1')}; v2 tiers lack tool-level control and tool threat protection {evp('pv-a365-v2')}.",
         f"{PRE} {REC}"],
        [control_label("a365-consent", "Agent 365 consent", "Tenant level"),
         "Before anyone grants it, name who approves the consent, who reviews the policy changes it allows, and how it is withdrawn.",
         f"An administrator grants the A365 MCP Gateway Policy Operator role at tenant level with a one-time consent {evp('pv-a365-role')}. It lets the service read and write API-scoped policies {evp('pv-a365-rw')}.",
         f"{PRE} {REC}"],
        [control_label("ai-resource", "AI Gateway resource type", "Objective A"),
         "Start any evaluation on the new resource type, not the older AI Gateway tier. Check each example and article against the new type before use.",
         f"From 14 Oct 2026 Microsoft is changing the AI Gateway resource type to Microsoft.ApiManagement/aigateways {evp('pv-res-change')}. Complete the migration before 15 Jan 2027 {evp('pv-res-date')}. The new runtime URL uses the domain ai.gateway.azure.com {evp('pv-domain')}, and keys go in the Authorization header with a Bearer scheme {evp('pv-bearer')}.",
         f"{PRE} {REC}"],
        [control_label("ai-limits", "AI Gateway limits", "Objective A"),
         "Check the network design first. Confirm that a public gateway frontend, fixed virtual network and subnet, supported region and alternative content safety control meet the pilot requirements.",
         f"Gateway frontend private endpoints are not supported {evp('pv-pe')}. The virtual network and subnet cannot be changed after creation {evp('pv-vnet')}. The content safety policy is not supported {evp('pv-cs')}. During public preview the regions are East US 2 and Sweden Central {evp('pv-regions')}.",
         f"{PRE} {REC}"],
        [control_label("ai-publish", "Gateway publishing", "Objective A"),
         "Publish approved tools through the gateway. Give the gateway its own backend credential, scoped to what the tools need.",
         f"The gateway can combine tools from remote MCP servers, OpenAPI APIs and connectors behind gateway MCP endpoints {evp('pv-aig-comb')}. With a shared backend connection, callers use that connection's permissions {evp('pv-shared-cred')}.",
         f"{PRE} {REC}"],
        [control_label("ttp-users", "Tool threat protection: who can use it", "Extra defence"),
         "Use it only in flows that carry a user token. Keep least privilege and human approval for destructive tools. Do not rely on it alone.",
         f"It requires a delegated Entra user token {evp('pv-ttp-token')}. App-only service-to-service calls are not supported {evp('pv-ttp-app')}. A Defender or Purview license is required {evp('pv-ttp-lic')}.",
         f"{PRE} {REC}"],
        [control_label("ttp-modes", "Tool threat protection: modes and scope", "Extra defence"),
         "Configure the evaluation mode in Microsoft Defender. Test Audit, Block and failure handling. Enable pre-invocation checks to stop calls and post-invocation checks to withhold results. Plan for tools that already ran.",
         f"Audit mode fails open {evp('pv-ttp-audit')}. Block mode fails closed {evp('pv-ttp-block')}. One policy applies to every tool and caller of a server, not to one tool {evp('pv-ttp-scope')}. A denial after the call cannot undo it {evp('pv-ttp-post')}.",
         f"{PRE} {REC}"],
        [control_label("byo", "Agent 365 BYO server route", "Separate route"),
         "Treat this as a separate registration route, not as the API Management gateway integration. Require developer registration and admin approval. Confirm its public endpoint fits the backend isolation target. Test each listed client surface before relying on it.",
         f"BYO servers route through the Agent 365 Tooling Gateway {evp('pv-byo-route')}. Preview clients: Copilot Studio, VS Code, Claude Code and GitHub Copilot CLI; not Foundry or declarative agents {evp('pv-byo-surf')}. An IT admin approves or rejects requests in the Microsoft 365 admin center {evp('pv-byo-approval')}. Servers need a publicly accessible endpoint {evp('pv-byo-endpoint')}. BYO tool-level blocking is planned {evp('pv-byo-tool-plan')}.",
         f"{PRE} {REC}"],
        [control_label("foundry-routing", "Foundry gateway routing", "Separate route"),
         "Create new tools in the Foundry portal without managed OAuth. Check the endpoint, sign-in and logs. Do not assume old tools are covered.",
         f"Only new MCP tools created in the Foundry portal without managed OAuth are routed through an AI gateway {evp('pv-fy-prev')}. Routing is applied only at tool creation, and existing tools are not mediated automatically {evp('pv-fy-new')}.",
         f"{PRE} {REC}"],
        [control_label("outbound-filter", "Outbound filter, optional", "Objective B"),
         "Add it only if the preview label is acceptable. Do not rely on it for local servers.",
         f"The Global Secure Access MCP firewall filters by URL pattern {evp('fw-urls')}. It carries the preview label {evp('fw-preview')} and inspects remote servers only {evp('fw-remote')}.",
         f"{PRE} {REC}"],
      ])}
    </div>
  </section>
"""

# ---- environments --------------------------------------------------------
ENV = f"""
  <section class="sec" id="env" aria-labelledby="h-env">
    <header class="sh"><h2 id="h-env">Environments</h2>
    <p class="goal"><b>Goal</b>Map each environment to the controls that apply. Product details and limits live in Controls and Known gaps.&nbsp;{REC}</p></header>
    {table(["Environment", "Controls to apply"], [
        ["Managed VS Code",
         f"{control_link('client', 'Client allowlist')}; {control_link('stdio', 'Local stdio servers')}"] ,
        ["GitHub Copilot, managed settings",
         f"{control_link('client', 'Client allowlist')}; {control_link('stdio', 'Local stdio servers')}"] ,
        ["GitHub Copilot cloud agent",
         f"<span id=\"gap-github-cloud-agent\"></span>{control_link('client', 'Client allowlist')}. The cloud agent firewall does not directly filter MCP server processes; do not rely on it as their runtime egress boundary {ev('gh-fw')}"],
        ["Foundry agents",
         control_link('foundry', 'Policy sync, Foundry')],
        ["Copilot Studio",
         control_link('power-platform', 'Policy sync, Power Platform')],
        ["Microsoft 365 Copilot",
         f"{control_link('m365', 'Policy sync, Microsoft 365 Copilot')}; {control_link('m365-network', 'Microsoft 365 Copilot network path')}; {control_link('identity', 'Identity')}"],
        ["Unmanaged workstation",
         f"{control_link('backend', 'Backend isolation')}; {control_link('identity', 'Identity')}"] ,
        ["Local stdio server",
         control_link('stdio', 'Local stdio servers')],
        ("opt-preview",
         ["Agent 365 with API Management",
          f"{control_link('a365', 'Agent 365 gateway integration')}; {control_link('backend', 'Backend isolation')}"]),
        ("opt-preview",
         ["Foundry, new tools with gateway routing",
          control_link('foundry-routing', 'Foundry gateway routing')]),
        ("opt-preview",
        ["Agent 365 BYO server route",
         control_link('byo', 'Agent 365 BYO server route')]),
    ])}
  </section>
"""

# ---- tests ---------------------------------------------------------------
TESTS = f"""
  <section class="sec" id="tests" aria-labelledby="h-tests">
    <header class="sh"><h2 id="h-tests">Acceptance tests</h2>
    <p class="goal"><b>Goal</b>Each row is a target outcome. API Management alone does not guarantee them.&nbsp;{REC}</p></header>
    {table(["Test", "Expected result", "Objective", "Result"], [
        ["Call an approved MCP server through API Management", "Allowed", "A", "Not run"],
        ["Call the protected backend directly", "Blocked", "A", "Not run"],
        ["Call API Management without valid authorization", "Rejected", "A", "Not run"],
        ["Add an unapproved remote MCP server in a managed client", "Blocked", "B", "Not run"],
        ["Change the MCP URL in VS Code to a different server", "Blocked", "B", "Not run"],
        ["Start an unauthorized local MCP server", "Blocked or contained by endpoint controls", "B", "Not run"],
        ["Merge a pull request that denies a server", "Blocked in each supported target after policy propagation and client refresh", "B", "Not run"],
        ["Edit a target by hand, then run the pipeline", "The edit is overwritten or flagged", "B", "Not run"],
        ["Call an approved connector from Microsoft 365 Copilot", "Allowed, through API Management", "A", "Not run"],
        ["Add a custom connector for an unapproved server without an admin role", "Blocked", "B", "Not run"],
        ["Block a connector in the Microsoft 365 admin center", "Unavailable to users after the change takes effect", "B", "Not run"],
        ["Repeat the direct call by IP address, from an unmanaged client, by another network path and from a cloud-hosted agent", "Blocked", "A", "Not run"],
    ])}
    <div class="sub3 opt-preview">
      <h3>Added with preview&nbsp;{PRE}</h3>
      {table(["Test", "Expected result", "What establishes the guarantee", "Result"], [
        ["Approved client calls the approved gateway MCP endpoint", "Allowed", "Gateway sign-in and the published tool policy", "Not run"],
        ["Admin blocks a whole MCP server in the API Management integration", "Denied at the gateway", "A verified integration and a runtime block", "Not run"],
        ["Admin blocks a single tool in the API Management integration", "Denied, only on a supported gateway with a static tool list", "An explicit tool-level policy test", "Not run"],
        ["Pre-invocation evaluation denies a tool argument", "Tool not run", "Block mode before the call", "Not run"],
        ["Post-invocation evaluation denies a tool result", "Result withheld; the tool may already have run", "Block mode after the call", "Not run"],
        ["Microsoft admin rejects a registered MCP server request", "Server remains unavailable", "Requests preview decision", "Not run"],
        ["Microsoft admin approves without granting Entra consent", "Server remains unavailable to agent-building surfaces", "Approval plus required tenant consent", "Not run"],
        ["Admin blocks an Available MCP server", "Tool calls are denied at runtime", "Registry block and the connected Agent 365 enforcement path", "Not run"],
        ["Review the Agent registry, Tools registry and Requests queue", "Agent inventory, Available or Blocked server states, and pending preview requests are visible in their respective views", "Microsoft 365 admin center", "Not run"],
        ["An app-only caller reaches a tool with the delegated-token protection", "Unsupported, or the protected call fails", "An explicit sign-in compatibility test", "Not run"],
        ["The gateway is down, or a preview feature is withdrawn", "Safe stop, or a rollback to the released-only design", "Backend and client controls, and the fallback plan", "Not run"],
      ])}
    </div>
  </section>
"""

# ---- order of work -------------------------------------------------------
ORDER = f"""
  <section class="sec" id="order" aria-labelledby="h-order">
    <header class="sh"><h2 id="h-order">Order of work</h2>
    <p class="goal"><b>Goal</b>{safe("Four steps, in this order.")}{prev("Build the baseline first. The pilot starts only after it.")}&nbsp;{REC}</p></header>
    <ol class="steps">
      <li><strong>First.</strong> Inventory MCP use, put the approved list in a repository and build the pipeline that applies it.</li>
      <li><strong>Next.</strong> Isolate the company MCP backends and require access through API Management.</li>
      <li><strong>Then.</strong> Add endpoint application control, local server limits and outbound policy.</li>
      <li><strong>Finally.</strong> Add monitoring, review exceptions and run the bypass tests on a schedule.</li>
    </ol>
    <div class="sub3 opt-preview">
      <h3>Preview pilot, after the baseline&nbsp;{PRE}</h3>
      <ol class="steps">
        <li><strong>Scope.</strong> Pick a low-risk server with two read-only tools and one controlled write tool. Record owner, data class, sign-in and expected clients.</li>
        <li><strong>Resource type.</strong> Create the AI Gateway on the new resource type in a supported region {evp('pv-res-change', 'pv-regions')}. Confirm eligibility, the public front door, networking, policy features and licensing.</li>
        <li><strong>Publish.</strong> Publish the server through the gateway. Set the backend credential or managed identity, authorization, policies and logging. Use the gateway URL it issues.</li>
        <li><strong>Lock the backend.</strong> Make direct calls fail. Check the supported backend network design, because the new gateway has no private endpoints {evp('pv-pe')}.</li>
        <li><strong>Connect Agent 365.</strong> For the API Management integration, after named tenant-admin consent, connect the gateway and check that the server shows up. Review the permissions granted {evp('pv-a365-rw')}.</li>
        <li><strong>Test blocking.</strong> For the API Management integration, test a server block, then a named tool on a supported tier with a static tool list. If tool blocking fails on the new resource type, treat that combination as unsupported.</li>
        <li><strong>Threat protection.</strong> Turn it on in a user-token flow. Test Audit, Block and failure handling. Do not expect the same result for app-only workloads {evp('pv-ttp-app')}.</li>
        <li><strong>Client policy.</strong> Apply the repository list to the managed client allowlists, Foundry and Copilot Studio through the pipeline. Add endpoint and outbound controls.</li>
        <li><strong>Monitor.</strong> Watch gateway events, denied calls, admin changes and direct-connect attempts. Record blind spots and log retention.</li>
        <li><strong>Gate promotion.</strong> Require accepted support terms, released features, incident playbooks and a rollback plan before leaving the sandbox {evp('pv-notprod')}.</li>
      </ol>
    </div>
  </section>
"""

# ---- gaps ----------------------------------------------------------------
GAPS_LIST = [
    f"<strong>No part of the design is tested in a tenant.</strong> Every expected result above is a target, not a result.{prev(' This includes Agent 365 and Foundry against the new AI Gateway resource type.')}",
    f"<strong id=\"gap-github-builtin\">Built-in GitHub MCP server.</strong> Allow and deny lists cannot block it {ev('gh-builtin-order', 'gh-builtin')}. Two other switches are untested for it: the MCP servers in Copilot policy, which turns off all MCP {ev('gh-policy-off')}, and Registry only {ev('gh-reg-only')}, a public preview with weaker enforcement {ev('gh-reg-preview', 'gh-reg-bypass')}. The design has no control for it. See the <a href=\"#open\">open questions</a>.",
    f"<strong id=\"gap-m365-manual\">Microsoft 365 Copilot is set by hand.</strong> Agent and plugin access has no PowerShell or API option {ev('m365-noapi')}, so the pipeline cannot keep this target in step. {UNV} No page read says whether a custom connector can be created by API. Declarative agents that carry their own MCP server were not checked.",
    f"<strong id=\"gap-m365-status\">Microsoft 365 Copilot connector status.</strong> {INF} Interpretation by AI: the federated connector pages read on 2026-11-11 carry no preview label for the connectors, so the page treats them as released. Confirm in the target tenant.",
    f"<strong id=\"gap-windows-outbound\">Windows outbound block.</strong> It can block non-MCP traffic too, and name-based rules have limits with proxies and some VPN tunnels. {ev('ifw-block', 'dk-limits')}",
    f"<strong id=\"gap-tier-availability\">API Management tier availability.</strong> MCP features vary by tier. Confirm the target tier and release status before relying on a feature. {ev('apim-ga', 'apim-ga-tiers', 'pv-apim-tier')}",
]
GAPS_OL = "\n".join(f"<li>{x}</li>" for x in GAPS_LIST)
GAPS = f"""
  <section class="sec" id="gaps" aria-labelledby="h-gaps">
    <header class="sh"><h2 id="h-gaps">Known gaps and what has not been tested</h2>
    <p class="goal">{tg("u", "Bad&nbsp;news&nbsp;first")} Read these limits before relying on the design.</p></header>
    <ol>
{GAPS_OL}
    </ol>
  </section>
"""

# ---- fallback ------------------------------------------------------------
FALLBACK = f"""
  <section class="sec opt-preview" id="fallback" aria-labelledby="h-fallback">
    <header class="sh"><h2 id="h-fallback">Fallback</h2>
    <p class="goal"><b>Goal</b>If a preview feature changes, keep the released-only design running underneath. Use the preview controls in a sandbox only.&nbsp;{REC}</p></header>
    <ol class="steps">
      <li>Keep production MCP servers behind the released-only design, using only API Management features whose release status is confirmed.</li>
      <li>Switch off the preview integrations for the affected workloads.</li>
      <li>Keep client policy, backend isolation, least privilege and logging as they are.</li>
      <li>Check which capabilities remain before the switch. {REC}</li>
    </ol>
  </section>
"""

# ---- open questions ------------------------------------------------------
OPEN = """
  <section class="sec" id="open" aria-labelledby="h-open">
    <header class="sh"><h2 id="h-open">Open questions</h2></header>
    <ol class="ans tight">
      <li><span class="n">1</span><h3>Are preview features allowed at all?</h3><p>Choices: never, in a sandbox only, or later. Require released features for production. The proposed pipeline and cross-client enforcement still need validation.</p></li>
      <li><span class="n">2</span><h3>Which comes first: developer workstations or hosted agents?</h3><p>Workstations call for client rules and, on Windows, outbound limits. Hosted agents call for network isolation and data policies. Start where the more sensitive backends are. See the <a href="#env">environment table</a>.</p></li>
      <li><span class="n">3</span><h3>Is a default outbound block on managed Windows laptops acceptable?</h3><p>Decide before rollout. The effect on other traffic is in the <a href="#gaps">gaps</a>.</p></li>
      <li><span class="n">4</span><h3>Who reviews list changes and owns the pipeline?</h3><p>Name the reviewers of the repository, the pipeline owner and the person called when a target fails to update. Name who applies the list by hand in the Microsoft 365 admin center.</p></li>
      <li><span class="n">5</span><h3>Is the built-in GitHub MCP server acceptable on managed clients?</h3><p>The allow and deny lists cannot block it. Choices: accept it, turn off the MCP servers in Copilot policy (stops all servers), or limit it through GitHub account permissions. <span class="tg i">inference</span> No source checked says whether that policy or Registry only covers the built-in server. Test both in a pilot.</p></li>
      <li class="opt-preview"><span class="n">6</span><h3>Who approves and reviews the Agent 365 consent?</h3><p>The consent lets the service write API policies. Name an approver and a reviewer. See the <a href="#controls">controls</a>.</p></li>
      <li class="opt-preview"><span class="n">7</span><h3>What ends the pilot?</h3><p>Set the exit evidence now: terms accepted, features released, clients covered. Without it the pilot has no end. See the <a href="#fallback">fallback</a>.</p></li>
      <li class="opt-preview"><span class="n">8</span><h3>Does a gateway with no private endpoints fit the network rules?</h3><p>The new resource has no private endpoints. Check the rules before building. See the <a href="#gaps">gaps</a>.</p></li>
      <li class="opt-preview"><span class="n">9</span><h3>Which Agent 365 route will the pilot use?</h3><p>Choose the API Management gateway integration or the separate BYO server registration route. See the <a href="#controls">controls</a>.</p></li>
    </ol>
  </section>
"""

# ---- evidence ------------------------------------------------------------
EV_ROWS = []
for key, skey, q in QUOTES:
    title, url, date = SOURCES[skey]
    shown = date or "none shown"
    cls = ' class="opt-preview"' if key in PREVIEW_ONLY else ""
    EV_ROWS.append(
        f'<tr id="ev-{IDS[key]}"{cls}><td>{IDS[key]}</td><td>{html.escape(q, quote=False)}</td>'
        f'<td><a href="{url}{frag(q)}">{title}</a></td><td>{shown}</td></tr>')
EV_TABLE = "\n".join(EV_ROWS)

EVIDENCE = f"""
  <section id="evidence" aria-labelledby="h-e">
    <div class="part">
      <p class="lbl"><b>Fact check</b> · Each product claim against its source</p>
      <h2 id="h-e">Fact check</h2>
    </div>
    <details class="blk ev-fold" id="evidence-details" style="margin-top:20px">
      <summary>Show the source quotes</summary>
      <p class="sub">Product claims are supported by the source excerpts below, checked on {CHECKED}. Links request the quoted passage using browser text fragments. Page date is the date the page shows. {safe(f"{SAFE_COUNT} quotes back the released-only design.")}{prev(f"{len(QUOTES)} quotes in all: {SAFE_COUNT} back the released-only design and {PV_COUNT} back the preview additions.")}</p>
      <div class="tbl-wrap"><table class="tbl src">
        <thead><tr><th>Id</th><th>Quote</th><th>Source</th><th>Page date</th></tr></thead>
        <tbody>
{EV_TABLE}
        </tbody>
      </table></div>
    </details>
  </section>
"""


# ---- guardrails by layer -------------------------------------------------
DESC_GR_SAFE = ("Guardrails by layer for one MCP tool call, in three columns: Foundry agent, Copilot Studio, and VS Code with GitHub Copilot. "
                "Layer 1 user input: Foundry has harm levels and a prompt attack check, Copilot Studio has a built-in prompt attack block, whose layer is an AI estimate, and GitHub says its content filter may scan prompts. "
                "Layer 2 which server: Foundry allowed_tools, Copilot Studio data policy, VS Code and GitHub allow and deny lists plus a server trust prompt in VS Code. "
                "Layer 3 person approves: Foundry require_approval, default always, which can be set to never. Copilot Studio can ask the user before running a tool, off by default and unverified for MCP tools. "
                "VS Code shows a confirmation dialog by default, the Allow all level skips it, and a company policy can lock it. "
                "Layer 4 call content: preview only for Foundry and Copilot Studio. In VS Code a preToolUse hook can deny a call, unverified for MCP tools. "
                "Layer 5 network and gateway: the design above applies to every client, plus two lines that apply to Foundry only. Layer 6 company MCP server: the design target is that only the gateway can call it. "
                "Layer 7 tool response: preview only for Foundry, none found for Copilot Studio. VS Code can ask for a review of the result before it enters the chat context, and this can be switched off. "
                "Layer 8 final answer: Foundry has harm levels and a protected material flag, Copilot Studio is not stated, and GitHub says its content filter may scan answers. "
                "Below the figure: Copilot Studio content moderation has no stated layer. Foundry agent guardrails have preview status, and with none set the agent uses the guardrail of its model.")
DESC_GR_PREVIEW = DESC_GR_SAFE.replace("Layer 4 call content: preview only for Foundry and Copilot Studio. ",
                "Layer 4 call content: Foundry has a tool call guardrail in preview that does not list MCP, Copilot Studio has threat detection in preview that by default allows the call after one second without a reply. ").replace(
                "Layer 7 tool response: preview only for Foundry, none found for Copilot Studio. ",
                "Layer 7 tool response: Foundry has a tool response guardrail in preview that does not list MCP, none found for Copilot Studio. ").replace(
                "the design above applies to every client,", "the design above applies to every client, with tool threat protection in preview,").replace(
                "plus two lines that apply to Foundry only.", "plus a Defender rule for tool calls to MCP tools onboarded to Agent 365 and two lines that apply to Foundry only.") + (
                " In preview, a Microsoft Defender real-time protection rule also applies for Foundry at layers 1, 4, 7 and 8 and for Copilot Studio at layer 4."
                " Defender for Endpoint runtime protection, in preview on Windows, lists the VS Code GitHub Copilot extension, with no layer stated.")
for _old in ("Layer 4 call content: Foundry has a tool call guardrail", "Layer 7 tool response: Foundry has a tool response guardrail", "with tool threat protection in preview,", "onboarded to Agent 365 and two lines"):
    if _old not in DESC_GR_PREVIEW:
        sys.exit(f"guardrail preview description lost: {_old}")

GR_ROWS = [
    ["Harm levels", "Foundry", "1 and 8", f"Checks hate, violence, sexual and self-harm content in user input and in the answer. These controls cannot be deleted, only overridden. {ev('gr-fy-harm', 'gr-fy-del')}"],
    ["Prompt attack check", "Foundry", "1", f"Scans the user input for jailbreak attacks and blocks it if one is found. {ev('gr-fy-in', 'gr-fy-block')}"],
    ["Protected material", "Foundry", "8", f"Flags copyrighted text in the answer. The action is annotate only, so it does not block. {ev('gr-fy-out', 'gr-fy-flag')}"],
    ["Agent over model", "Foundry", "All", f"Agent guardrails are in preview {ev('gr-fy-agprev')}. An agent's guardrail overrides the guardrail on its model {ev('gr-fy-override')}. With no agent guardrail, the agent inherits the guardrail of its model deployment {ev('gr-fy-inherit')}. {INF} Interpretation by AI: on the released-only path, set the controls on the model deployment."],
    ["Tool list", "Foundry", "2", f"allowed_tools limits which tools the agent may use. An empty list allows all tools, not none. {ev('fy-allowed')}"],
    ["Approval", "Foundry", "3", f"require_approval defaults to always, which means a developer approves every call {ev('gr-fy-appr', 'gr-fy-always')}. It can be set to never, or to a list of tools that skip approval {ev('gr-fy-never')}. Microsoft advises approval for high-risk tools that write data {ev('gr-fy-high')}."],
    ["Tool call and tool response guardrails", "Foundry", "4 and 7",
     safe(f"Both are preview features, not in the released-only design. {ev('gr-fy-call', 'gr-fy-resp')}")
     + prev(f"Both are in preview {evp('gr-fy-call', 'gr-fy-resp')}. The response control scans for indirect prompt injection {evp('pv-gr-fy-indirect')}. Controls take no effect for tools outside the supported list {evp('pv-gr-fy-support', 'pv-gr-fy-list', 'pv-gr-fy-noeffect')}. {INF} Interpretation by AI: the list does not name MCP, so do not rely on them for MCP.")],
    ["Untrusted results", "Foundry", "7", f"Microsoft says to treat tool descriptions, annotations and results from remote MCP servers as untrusted input. This is advice, not a control. {ev('gr-fy-untrust')}"],
    ["Network control and sandbox", "Foundry", "5", f"The Network control limits outbound traffic for hosted agents and prompt agents on the Copilot harness only. Hosted agents also run in per-session VM sandboxes. {ev('gr-fy-net', 'gr-fy-sandbox')}"],
    ["Prompt attack block", "Copilot Studio", "1", f"Built-in protection against user prompt injection (UPIA) and cross-domain prompt injection (XPIA). At runtime the agent blocks attacks of these types. {ev('gr-cs-upia', 'gr-cs-block')} {INF} Interpretation by AI: the source does not say at which layer. Layer 1 is the fit for user prompt injection. Cross-domain attacks may also arrive in tool results."],
    ["Content moderation", "Copilot Studio", "Not stated", f"Covers predefined harmful-content categories. The sources checked do not say at which layer. {ev('gr-cs-mod')}"],
    ["Data policy", "Copilot Studio", "2", f"Blocking Power Platform connectors also blocks the tools of connected MCP servers. It works per server, not per tool. {ev('studio', 'pp-block')}"],
    ["Ask before running", "Copilot Studio", "3", f"A maker can set a tool to ask the end user for confirmation in the chat before it runs. The option is off by default. {ev('gr-cs-ask')} {UNV} The page describes tools in general. Not checked whether the option is offered for MCP tools."],
    ("opt-preview", ["Threat detection", "Copilot Studio", "4", f"An external service allows or blocks a tool call. The page is prerelease {evp('pv-gr-cs-pre', 'pv-gr-cs-det')}. By default the call goes ahead if the service is silent for one second. This can be changed to block {evp('pv-gr-cs-1s', 'pv-gr-cs-errblock')}. It runs only with generative orchestration {evp('pv-gr-cs-gen')}. The agent shares data with the provider {evp('pv-gr-cs-share')}."]),
    ("opt-preview", ["Defender real-time protection", "Foundry, Copilot Studio", "Foundry 1, 4, 7, 8. Copilot Studio 4",
     f"Checks agent activity and can block a risky action before it runs {evp('pv-gr-def-how')}. Foundry (Preview): user requests, agent responses, tool calls and tool responses {evp('pv-gr-def-fy', 'pv-gr-def-fy2')}. Copilot Studio (Preview): tool calls {evp('pv-gr-def-cs', 'pv-gr-def-cs2')}."]),
    ("opt-preview", ["Defender on the Agent 365 path", "Agent 365", "4",
     f"Covers tool calls to customer MCP tools onboarded to Agent 365, but not agents that use unsupported tools or skip Work IQ MCP {evp('pv-gr-def-a365', 'pv-gr-def-unsup')}. {INF} Interpretation by AI: the line is not labelled preview on the page, but it needs a customer MCP server onboarded to Agent 365, and the sources call that path preview {evp('pv-byo-surf')}."]),
    ("opt-preview", ["Defender rules and scope", "Foundry, Copilot Studio, Agent 365", "Same as the two rows above",
     f"The default rule only audits {evp('pv-gr-def-audit')}. A custom rule blocks {evp('pv-gr-def-block')}. Blocking covers malicious content, secret exfiltration, evasion techniques and email to an unsafe domain {evp('pv-gr-def-mal', 'pv-gr-def-secret', 'pv-gr-def-evasion', 'pv-gr-def-mail')}. The email scenario is checked only at the tool request {evp('pv-gr-def-mailonly')}. A rule can be scoped only to agents with a Microsoft Entra agent ID {evp('pv-gr-def-entra')}."]),
    ("opt-preview", ["Defender for Endpoint runtime protection", "VS Code, GitHub Copilot", "Not stated",
     f"Local agents are covered by Defender for Endpoint, not by the rules above {evp('pv-gr-def-local')}. The article is prerelease {evp('pv-gr-mde-pre')}. It can block an action before it runs when the inspection method allows it {evp('pv-gr-mde-how')}. The Windows (preview) support table lists the VS Code GitHub Copilot extension {evp('pv-gr-mde-win', 'pv-gr-mde-vs')}. The layer for this client is not stated."]),
    ["Allow and deny lists", "VS Code, GitHub Copilot", "2", f"VS Code policies and GitHub managed settings can set an allow list and a deny list. When an allow list is set, a server that matches no entry is blocked. A deny entry wins over an allow entry. {ev('vs-allow', 'vs-deny', 'gh-block', 'gh-deny')}"],
    ["Server trust prompt", "VS Code", "2", f"Servers that do not come from the workspace MCP files can need a separate trust decision by the person. VS Code asks again after a configuration change. {ev('gr-vs-trust')}"],
    ["Confirmation dialog", "VS Code", "3", f"By default, actions that are not auto-approved need the person's confirmation, and the dialog shows the input parameters {ev('gr-vs-appr', 'gr-vs-manual')}. The Allow all level runs all tool calls without confirmation {ev('gr-vs-allowall')}. Assisted permissions lets an LLM judge assess each call {ev('gr-vs-assist')}. Documented for VS Code only."],
    ["Approval lock", "VS Code", "3", f"A company can limit the levels above. A policy that turns off global auto-approval leaves only one-time approval and ignores saved approvals {ev('gr-vs-pol-auto')}. A managed setting can disable Allow all {ev('gr-vs-pol-bypass')}. {UNV} Not tested on a managed device."],
    ["Tool call hook", "VS Code, GitHub Copilot", "4", f"A preToolUse hook can inspect a supported tool's arguments and deny the call. A filter that misses a tool does not check that call {ev('gr-vs-hook')}. VS Code says hooks are not a substitute for enforced permissions or enterprise controls {ev('gr-vs-hook-not')}. {UNV} Not checked whether a hook sees MCP tool calls."],
    ["Result review", "VS Code", "7", f"Tool approval covers confirmation before or after a tool runs {ev('gr-vs-after')}. Post-approval adds a tool result to the chat context without review, and VS Code warns about prompt injection in external data {ev('gr-vs-post')}. {UNV} Not checked which tools ask for a result review by default."],
    ["Content filter", "GitHub Copilot", "1 and 8", f"GitHub says Copilot Chat may at times include a content filter that scans prompts and responses to detect and block harmful content. {ev('gr-gh-filter')} {INF} Interpretation by AI: the words at times and may mean this is not a control to count on."],
]

GUARDRAILS = f"""
  <section class="sec" id="guardrails" aria-labelledby="h-guardrails">
    <header class="sh"><h2 id="h-guardrails">Guardrails by layer</h2>
    <p class="goal"><b>Goal</b>Show where each client can stop a bad request or answer, along the path of one MCP tool call. This is a different view of the design above. Layer 6 and most of layer 5 repeat the design. Only the lines marked Foundry only or Agent 365 path only are new.</p></header>
    <figure class="opt-safe">
      <p class="fig-hint">Scroll the diagram sideways to follow the flow.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="Guardrails by layer, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_GR_SAFE}">{ascii_fig("guardrails-safe")}</pre>
      </div>
    </figure>
    <figure class="opt-preview">
      <p class="fig-hint">Scroll the diagram sideways to follow the flow.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="Guardrails by layer with preview features, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_GR_PREVIEW}">{ascii_fig("guardrails-preview")}</pre>
      </div>
    </figure>
    <p class="q-note">None found means the pages read on 2026-11-11 do not describe a guardrail at that layer. {UNV} It does not prove that none exists.</p>
    <p class="q-note">Quotes for layers 1 to 4, 7 and 8 and for the lines marked Foundry only or Agent 365 path only are in the table below. The rest of layers 5 and 6 is the design above.</p>
    <p class="q-note">Microsoft 365 Copilot is not a column in this view. Its documented guardrails for federated connectors: tools that write need user approval {ev('m365-write')}, admins can block a tool or a connector {ev('m365-toolblock')}, and activity can be audited in Purview {ev('m365-audit')}. See <a href="#ctrl-m365">Policy sync, Microsoft 365 Copilot</a>.</p>
    {safe('<p class="q-note">Microsoft Defender real-time protection and Defender for Endpoint runtime protection are left out of this released-only view. They are on the preview path.</p>')}
    <div class="sub3">
      <h3>What each guardrail does</h3>
      {table(["Guardrail", "Product", "Layer", "What it does and its limit"], GR_ROWS)}
    </div>
  </section>
"""

FOOTER = f"""
  <footer>
    <p>Documentation checked {CHECKED}. The design is proposed. No tests have run in a real tenant, on a managed laptop or on a hosted agent runtime. {prev("The preview additions are for a sandbox pilot.")}</p>
    {AI_NOTE}
  </footer>
"""

BODY = f"""{HEAD}{STYLE}
{OPT_CSS}
</head>
<body data-opt="safe">{MARKERS}<div class="page" id="top">
{MAST}
  <main id="main-content" tabindex="-1">
{FIGURE}{CONTROLS}{ENV}{TESTS}{ORDER}{GAPS}{FALLBACK}{OPEN}{GUARDRAILS}{EVIDENCE}
  </main>
{FOOTER}
</div>

{SCRIPT}
</body>
</html>
"""

for ch in (chr(0x2014), chr(0x2013)):
    if ch in BODY:
        sys.exit("em or en dash found in output")

OUT.write_text(add_anchors(BODY), encoding="utf-8")
print(f"wrote {OUT.name}, {len(BODY.splitlines())} lines; {len(QUOTES)} quotes, {SAFE_COUNT} on the released-only path")

for m in re.finditer(r"<(p|dd|td|li)\b[^>]*>(.*?)</\1>", BODY, re.S):
    words = len(re.sub(r"<[^>]+>", " ", m.group(2)).split())
    if words > 60:
        print(f"WARN {words} words: {re.sub(r'<[^>]+>', ' ', m.group(2))[:70]!r}")
defined = set(re.findall(r'\bid="([^"]+)"', BODY))
for t in sorted(set(re.findall(r'href="#([^"]+)"', BODY)) - defined):
    print(f"WARN dead anchor #{t}")
