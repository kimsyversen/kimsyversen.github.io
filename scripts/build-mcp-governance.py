"""Build wip/mcp-governance-microsoft.html.

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
from mcp_governance_evidence import CHECKED, IDS, PREVIEW_ONLY, QUOTES, SOURCES  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
BASE = "enterprise-ai-agent-governance-summary.html"
OUT = ROOT / "wip" / "mcp-governance-microsoft.html"
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
  function followHash(){
    var id = location.hash.slice(1);
    if(!id) return;
    try{ id = decodeURIComponent(id); }catch(e){}
    var el = document.getElementById(id);
    if(!el) return;
    var other = body.getAttribute('data-opt') === 'safe' ? 'preview' : 'safe';
    if(el.closest('.opt-' + other)){ setOpt(other); el.scrollIntoView(); }
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){ setOpt(b.getAttribute('data-opt-btn')); }); });
  var m = /[?&]path=(safe|preview)(?:&|$)/.exec(location.search);
  setOpt(m ? m[1] : 'safe', true);
  followHash();
  window.addEventListener('hashchange', followHash);
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
    <div class="meta"><span>Design · Microsoft stack · MCP</span><span>Documentation checked 8 Nov 2026</span></div>
    <h1>MCP Governance in a Microsoft ecosystem</h1>
    <div class="intro">
      <p class="lead">A proposed design for governing MCP servers across GitHub Copilot, VS Code, Foundry and Copilot Studio. Select Released only or With preview. Nothing is built or tested yet.</p>
      <p class="lead">The repository list is the design's source of truth. The pipeline is a design requirement, and none of it is built or tested. Control requirements and evidence follow below.</p>
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


PARTS_ROWS = [
    part("Approved list in Git", "Source of truth",
         "Reviewed record of approved and denied MCP servers.",
         "Yes", "Yes"),
    part("Sync pipeline", "Source of truth",
         "On merge, writes the list to each policy target. Proposed work; not built yet. See <a href=\"#ctrl-pipeline\">Policy sync, pipeline</a>.",
         "Yes", "Yes"),
    part("Policy targets", "Targets",
         "GitHub managed settings: a commit to the .github-private repository (<a href=\"#ctrl-pipeline\">pipeline</a>). Copilot Studio: the Power Platform API (<a href=\"#ctrl-power-platform\">unverified for MCP</a>). Foundry: an allowed tool list on each MCP tool (<a href=\"#ctrl-foundry\">pipeline not tested</a>).",
         "Yes", "Yes"),
    part("MCP clients", "Callers",
         "Copilot Studio, VS Code, Foundry agents, and GitHub Copilot.",
         "Yes", "Yes"),
    part("Client controls", "Enforcement",
         "Managed URL policies and, on Windows, outbound firewall rules where applicable.",
         "Yes", "Yes"),
    part("Gateway product", "Gateway",
         "API Management in the released-only path; the preview path adds Azure AI Gateway capabilities.",
         "API Management", "Azure AI Gateway added"),
    part("Company MCP server, gateway only", "Backend",
         "Company MCP server; only the gateway may reach it.",
         "Yes", "Yes"),
    part("Agent 365 gateway integration", "Preview admin view",
         "Admin view connected to the gateway. Product controls are detailed below.",
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

# ---- design figures ------------------------------------------------------
# The figures are plain text files beside the page. Edit them, then rebuild.
# [red]...[/red] marks text that means caution, unverified or denied. [b]...[/b] marks a box title.
def ascii_fig(name):
    raw = (ROOT / "wip" / f"mcp-governance-microsoft.figure-{name}.txt").read_text(encoding="utf-8")
    for tag in ("red", "b"):
        if raw.count(f"[{tag}]") != raw.count(f"[/{tag}]"):
            sys.exit(f"unbalanced [{tag}] markers in figure {name}")
    out = html.escape(raw.rstrip("\n"), quote=False)
    out = out.replace("[red]", '<span class="stop">').replace("[b]", '<span class="ttl">')
    return out.replace("[/red]", "</span>").replace("[/b]", "</span>")


DESC_SAFE = ("Design target: a Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. "
             "After merge, a pipeline applies the list to three targets: Power Platform policy for Copilot Studio, "
             "GitHub managed settings, and Foundry. Each target points to the clients it governs. The clients then pass through "
             "client controls, Windows outbound firewall rules where applicable, API Management and the company MCP server, which only the gateway can reach. A direct call from a client to the server is blocked.")
DESC_PREVIEW = ("Design target: the released-only design with preview additions. A Git repository holds the approved and denied MCP servers. "
                "After a reviewed merge, a pipeline applies the list to Power Platform policy for Copilot Studio, "
                "GitHub managed settings and Foundry. Each target points to the clients it governs. "
                "The clients then pass through client controls, Windows outbound firewall rules where applicable, Azure AI Gateway with tool threat protection, and a company MCP server that only the gateway can reach. "
                "A direct call from a client to the server is blocked. The design connects the Agent 365 admin view below the gateway.")

FIGURE = f"""
  <section class="sec" id="design" aria-labelledby="h-design">
    <header class="sh"><h2 id="h-design">The design</h2>
    <p class="goal"><b>In short</b>Keep the company MCP server behind the gateway and limit managed clients to approved servers.{prev(" With preview, add an Agent 365 admin view and optional blocking. Test preview features only in a sandbox.")}&nbsp;{REC}</p>
    <p class="goal"><b>Designs</b>Released only is the target baseline. Use only confirmed released features; keep unverified automation out of production. With preview adds Agent 365 and tool threat protection, for a sandbox only.</p></header>
    <figure class="opt-safe">
      <p class="fig-hint">Scroll the diagram sideways to follow the flow.</p>
      <p class="q-note">Red text marks denied traffic.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="MCP gateway design diagram, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_SAFE}">{ascii_fig("safe")}</pre>
      </div>
    </figure>
    <figure class="opt-preview">
      <p class="fig-hint">Scroll the diagram sideways to follow the flow.</p>
      <p class="q-note">Red text marks denied traffic.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="With-preview MCP gateway design diagram, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_PREVIEW}">{ascii_fig("preview")}</pre>
      </div>
      <figcaption class="q-note">With preview, connect the API Management gateway to Agent 365 and test tool threat protection in a sandbox. The BYO server route is separate; its limits are listed below.</figcaption>
    </figure>
{PARTS}  </section>
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
    <div class="sub3 opt-preview">
      <h3>Added with preview&nbsp;{PRE}</h3>
      <p class="q-note">These requirements and limits apply to preview additions. Microsoft says preview features are not meant for production use and may have restricted functionality. {evp('pv-notprod')}</p>
      {table(["Control", "Design requirement", "What Microsoft documents", "Label"], [
        [control_label("a365", "Agent 365 gateway integration", "Visibility, not the boundary"),
         "Connect the API Management gateway so admins can see registered servers and block one. Treat blocking as additional gateway enforcement. It does not replace backend isolation. This is separate from the Agent 365 BYO server route below.",
         f"Agent 365 can discover and govern servers registered with a connected gateway {evp('pv-disc')}. It can block servers; individual-tool control requires the AI Gateway tier {evp('pv-a365-ctrl')}. Tool control needs a static list of allowed tools {evp('pv-a365-static')}. API Management v1 tiers are not supported {evp('pv-a365-v1')}, and v2 tiers lack tool-level control and tool threat protection {evp('pv-a365-v2')}.",
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
      <li><span class="n">4</span><h3>Who reviews list changes and owns the pipeline?</h3><p>Name the reviewers of the repository, the pipeline owner and the person called when a target fails to update.</p></li>
      <li class="opt-preview"><span class="n">5</span><h3>Who approves and reviews the Agent 365 consent?</h3><p>The consent lets the service write API policies. Name an approver and a reviewer. See the <a href="#controls">controls</a>.</p></li>
      <li class="opt-preview"><span class="n">6</span><h3>What ends the pilot?</h3><p>Set the exit evidence now: terms accepted, features released, clients covered. Without it the pilot has no end. See the <a href="#fallback">fallback</a>.</p></li>
      <li class="opt-preview"><span class="n">7</span><h3>Does a gateway with no private endpoints fit the network rules?</h3><p>The new resource has no private endpoints. Check the rules before building. See the <a href="#gaps">gaps</a>.</p></li>
      <li class="opt-preview"><span class="n">8</span><h3>Which Agent 365 route will the pilot use?</h3><p>Choose the API Management gateway integration or the separate BYO server registration route. See the <a href="#controls">controls</a>.</p></li>
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
    <div class="blk" style="margin-top:20px">
      <p class="sub">Product claims are supported by the source excerpts below, checked on {CHECKED}. Links request the quoted passage using browser text fragments. Page date is the date the page shows. {safe(f"{SAFE_COUNT} quotes back the released-only design.")}{prev(f"{len(QUOTES)} quotes in all: {SAFE_COUNT} back the released-only design and {PV_COUNT} back the preview additions.")}</p>
      <div class="tbl-wrap"><table class="tbl src">
        <thead><tr><th>Id</th><th>Quote</th><th>Source</th><th>Page date</th></tr></thead>
        <tbody>
{EV_TABLE}
        </tbody>
      </table></div>
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
{FIGURE}{CONTROLS}{ENV}{TESTS}{ORDER}{GAPS}{FALLBACK}{OPEN}{EVIDENCE}
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

OUT.write_text(BODY, encoding="utf-8")
print(f"wrote {OUT.name}, {len(BODY.splitlines())} lines; {len(QUOTES)} quotes, {SAFE_COUNT} on the released-only path")

for m in re.finditer(r"<(p|dd|td|li)\b[^>]*>(.*?)</\1>", BODY, re.S):
    words = len(re.sub(r"<[^>]+>", " ", m.group(2)).split())
    if words > 60:
        print(f"WARN {words} words: {re.sub(r'<[^>]+>', ' ', m.group(2))[:70]!r}")
defined = set(re.findall(r'\bid="([^"]+)"', BODY))
for t in sorted(set(re.findall(r'href="#([^"]+)"', BODY)) - defined):
    print(f"WARN dead anchor #{t}")
