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
      <p class="lead">The repository list is the design's source of truth. The pipeline is our work, and none of it is built or tested. Control requirements and evidence follow below.</p>
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


PARTS_ROWS = [
    part("Approved list in Git", "Source of truth",
         "One repository holds the approved and denied MCP servers. A reviewed pull request changes it.",
         "Yes", "Yes"),
    part("Sync pipeline", "Source of truth",
         "Applies the list to each target after a merge. We build it. Nothing is built yet.",
         "Yes", "Yes"),
    part("Copilot Studio policy", "Target",
         f"Power Platform advanced connector policies support MCP server-level blocking, not individual MCP tools. Custom and HTTP connector types aren't supported {ev('pp-block', 'pp-custom')}. Check that the company server is covered. {REC}",
         "Yes", "Yes"),
    part("GitHub managed settings", "Target",
         f"An allow and deny list by server URL for GitHub Copilot clients, hosted on GitHub. {ev('gh-url', 'gh-block', 'gh-deploy')}",
         "Yes", "Yes"),
    part("Foundry tool list", "Target",
         f"A nonempty allowed tool list on each MCP tool. An empty list allows all. {ev('fy-allowed')}",
         "Yes", "Yes"),
    part("Agent 365 inventory", "Target",
         "Admin inventory view",
         "No", pv("Yes. New: discovers servers registered with the connected gateway.", "pv-disc")),
    part("Agent 365 block", "Target",
         "Admin access controls",
         "No", pv("Yes. New: blocks a server and controls individual tools on supported tiers. Tool control needs a static allowed-tools list per server.", "pv-a365-ctrl", "pv-a365-static")),
    part("URL allowlist", "Client controls",
         f"Managed clients may use only the approved MCP addresses. {ev('vs-allow', 'gh-url')}",
         "Yes", "Yes"),
    part("Windows outbound limits", "Client controls",
         f"Windows Firewall can block outbound connections that match no outbound rule. {ev('ifw-block')}",
         "Yes", pv("Yes. Optional extra: the Global Secure Access MCP firewall, which is preview and sees remote servers only.", "fw-preview", "fw-remote")),
    part("Sign-in required", "Client controls",
         "Clients must sign in before the gateway takes a call. Design requirement.",
         "Yes", "Yes"),
    part("Gateway product", "Gateway",
         "The service that every approved call passes through.",
         "API Management", pv("Azure AI Gateway is a separate preview resource type, with the limits listed under the preview controls.", "pv-notprod", "pv-res-change")),
    part("Publish MCP endpoints", "Gateway",
         "Offers approved servers to clients as MCP endpoints.",
         f"Yes. It can expose REST APIs as MCP servers or pass MCP servers through {ev('pv-apim-mcp')}. The source lists tiers and shows no preview label {ev('mcp-tiers')}. Microsoft announced general availability in Nov 2025 {ev('apim-ga')}.",
         pv("Yes. New: it can also combine tools from several servers, APIs and connectors behind one endpoint.", "pv-aig-comb")),
    part("Check identity", "Gateway",
         "The gateway checks who is calling.",
         f"Yes. It checks an Entra ID token or a subscription key. {ev('in-entra', 'in-key')}",
         pv("Yes. Entra access or a gateway API key.", "pv-aig-caller")),
    part("Authorize requests", "Gateway",
         "The gateway decides what the caller may do.",
         f"Yes. Policies can require and validate JWTs. {ev('mcp-authn')}",
         pv("Yes for callers.", "pv-aig-caller")),
    part("Log every call", "Gateway",
         "Every call through the gateway is recorded.",
         f"Yes. Policies can log every request. {ev('gw-policy')}",
         pv("Partly. The source names telemetry for tool usage.", "pv-aig-tel")),
    part("Limit request rate", "Gateway",
         "Caps how fast a caller can send requests.",
         f"Yes. Policies can limit requests per time period. {ev('mcp-rate')}",
         pv("Partly. The source names consumption limits.", "pv-aig-limits")),
    part("Tool threat protection", "Gateway",
         "Checks tool calls inside the gateway, in Audit or Block mode.",
         "No",
         pv("Yes. New: needs a delegated user token and a Defender or Purview license. One policy covers every tool of a server.", "pv-ttp-token", "pv-ttp-lic", "pv-ttp-scope")),
    part("Gateway routing for Foundry tools", "Gateway",
         "Sends Foundry MCP tools through an AI gateway.",
         "No",
         pv("Yes. New, and preview: only new tools made in the Foundry portal without managed OAuth, set at creation only.", "pv-fy-prev", "pv-fy-new")),
    part("Company MCP server, gateway only", "Backend",
         f"Our own server, which only the gateway can reach. {ev('iso-restrict')}",
         "Yes", "Yes"),
    part("Direct call blocked", "Backend",
         "A client that calls the server directly is refused.",
         "Yes", "Yes"),
]

PARTS = f"""
    <div class="sub3" id="parts">
      <h3>Parts of the design</h3>
      <p class="q-note">Each row is a box or measure in the figure. Yes means it is in that design, not that it is built. New marks what only the preview design adds.</p>
      {table(["Part", "What it does", "Released", "With preview"], PARTS_ROWS)}
      {prev(f'<p class="q-note">The preview gateway has no private endpoints, its virtual network and subnet cannot change after creation, and it has no content safety policy. {evp("pv-pe", "pv-vnet", "pv-regions", "pv-cs")} The controls table lists the preview limits relevant to this design.</p>')}
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
             "After merge, a pipeline we build applies the list to three targets: Power Platform policy for Copilot Studio, "
             "GitHub managed settings, and Foundry. Each target points to the clients it governs. The clients then pass through "
             "client controls, Windows outbound firewall rules where applicable, API Management and the company MCP server, which only the gateway can reach. A direct call from a client to the server is blocked.")
DESC_PREVIEW = ("Design target: the released-only design with preview additions. A Git repository holds the approved and denied MCP servers. "
                "After a reviewed merge, a pipeline we build applies the list to Power Platform policy for Copilot Studio, "
                "GitHub managed settings and Foundry. Each target points to the clients it governs. "
                "The clients then pass through client controls, Windows outbound firewall rules where applicable, Azure AI Gateway with tool threat protection, and a company MCP server that only the gateway can reach. "
                "A direct call from a client to the server is blocked. The design connects the Agent 365 admin view below the gateway.")

FIGURE = f"""
  <section class="sec" id="design" aria-labelledby="h-design">
    <header class="sh"><h2 id="h-design">The design</h2>
    <p class="goal"><b>In short</b>Keep the company MCP server behind the gateway and limit managed clients to approved servers.{prev(" With preview, add an Agent 365 admin view and optional blocking. Test preview features only in a sandbox.")}&nbsp;{REC}</p>
    <p class="goal"><b>Designs</b>Released only is the baseline and uses no feature labelled preview. With preview adds Agent 365 and tool threat protection, for a sandbox only.</p></header>
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
    <p class="goal"><b>How to read</b>Rows marked A deliver objective A. Rows marked B deliver objective B. Each documented fact cites a quote below.</p></header>
    {table(["Control", "Design requirement", "What Microsoft and GitHub document", "Label"], [
        ["Approved inventory<span class=\"rt\">Objectives A and B</span>",
         "Keep one list of approved MCP servers in a repository, with address, owner, permitted tools and risk class. Change it only by reviewed pull request. Set client policy from managed settings, not user-editable files. Use device management for device policies where supported.",
         f"GitHub managed settings apply the allow and deny lists to servers in user and repository settings {ev('gh-profiles')}. Foundry and Copilot Studio get the list from our pipeline. {REC}",
         REC],
        ["Policy sync, pipeline<span class=\"rt\">Objective B</span>",
         "On merge, a pipeline we build applies the list to each target. It reports any target it could not update. Manual edits in a target are overwritten or flagged on the next run. Nothing is built yet.",
         f"GitHub managed settings can be hosted on GitHub as a server-managed deployment {ev('gh-deploy')}. They are a file in the .github-private repository, changed by commit and push {ev('gh-file', 'gh-commit')}. The pipeline must make that commit. {REC}",
         f"{REC}"],
        ["Policy sync, Power Platform<span class=\"rt\">Objective B</span>",
         "Use an advanced connector policy through the Power Platform API only after confirming the company server is exposed as an MCP connector in the target environment. Expect whole-server blocking, not per-tool control.",
         f"Microsoft documents ACP API automation for deployment pipelines {ev('pp-pipe')}. ACP supports MCP connectors for server-level blocking, but not individual MCP tools {ev('pp-block')}. Custom and HTTP connector types aren't supported {ev('pp-custom')}. The API tutorial has no MCP-specific example; verify this path in the tenant before relying on it. {REC}",
         f"{REC}"],
        ["Policy sync, Foundry<span class=\"rt\">Objective B</span>",
         "Write an allowed tool list on every MCP tool, never an empty list. Use project network isolation for the rest. Treat a block by server URL as not available until a source or test shows it.",
         f"An MCP tool restricts access with a nonempty allowed tool list. An empty list allows every tool {ev('fy-allowed')}. Project networking governs network access {ev('fy-gov')}. ",
         f"{REC}"],
        ["Gateway<span class=\"rt\">Objective A</span>",
         "Publish each approved remote MCP endpoint through API Management. Check identity, authorize, rate-limit and log. Scope access by app or workload identity. Confirm the release status of each feature before relying on it.",
         f"For a remote Azure MCP Server, Microsoft suggests API Management as a gateway {ev('gw-consider')}: a single choke point {ev('gw-choke')}. Policies limit rates, restrict tool paths and log requests {ev('gw-policy')}. Clients go through it so the backend is not silently redirected {ev('gw-redirect')}. It can expose REST APIs as MCP servers or pass MCP servers through {ev('pv-apim-mcp')}.",
         REC],
        ["Backend isolation<span class=\"rt\">Objective A</span>",
         "Switch off public access to the backend. Accept inbound calls from the gateway only, over a private path.",
         f"Restrict MCP server connectivity so the gateway is the only permitted caller, or use private networking where supported {ev('iso-restrict')}. Azure Functions offers inbound access restrictions and private endpoints {ev('fn-ar', 'fn-pe')}. The Consumption plan has no private endpoints {ev('fn-cons')}. The API Management integration does not automatically route agents through a customer-hosted gateway {ev('iso-nogw')}.",
         REC],
        ["Identity<span class=\"rt\">Objective A</span>",
         "Only the gateway holds a credential or workload identity the backend accepts. The backend still checks the token, so a bypass fails.",
         f"The gateway can check an Entra ID token {ev('in-entra')} or a subscription key {ev('in-key')} before the request goes on {ev('gw-token')}. It can sign in to the backend with its managed identity {ev('out-mi')}. Checking the token again at the backend is our choice. {REC}",
         f"{REC}"],
        ["Client allowlist<span class=\"rt\">Objective B</span>",
         "Managed clients may use only the MCP addresses on the approved list, which the pipeline writes to GitHub managed settings. Users cannot add their own.",
         f"VS Code policies set an allowlist, a denylist and a managed-only mode {ev('vs-allow', 'vs-deny', 'vs-managed')}. GitHub managed settings match a remote server by URL with wildcards {ev('gh-url')} and block any server that matches no entry {ev('gh-block')}. Not covered: servers in custom agent profiles and the built-in GitHub server {ev('gh-profiles', 'gh-builtin')}. Coverage varies by environment {ev('gh-vary')}.",
         REC],
        ["Windows outbound limits<span class=\"rt\">Objective B</span>",
         "Block direct outbound calls from managed Windows devices to MCP servers we have not approved.",
         f"Intune can set Windows Firewall to block all outbound traffic that matches no rule {ev('ifw-block')}, a setting Microsoft says can be considered for certain highly secure environments {ev('dk-secure')}. Name-based rules have limits with proxies and some VPN tunnels {ev('dk-limits')}.",
         f"{REC}"],
        ["Local stdio servers<span class=\"rt\">Objective B</span>",
         "Limit which local server commands can start, through managed client policy. Add application control, least-privilege accounts and limits on sensitive files and credentials. Treat local administrators, other MCP clients and unmanaged devices as separate bypass risks.",
         f"The client launches a local server as a subprocess {ev('stdio')}. The stdio transport communicates over standard input and standard output {ev('stdio-io')}. GitHub managed settings match the exact command and each argument {ev('gh-cmd')}.",
         REC],
        ["Logging and checks<span class=\"rt\">Objectives A and B</span>",
         "Collect gateway logs and endpoint or client telemetry. Look for unapproved server connections, unexpected MCP processes, failed sign-ins and unusual tool use. Review the approved list on a schedule. Run the acceptance tests.",
         f"Gateway policies can log every request {ev('gw-policy')}.",
         REC],
    ])}
    <div class="sub3 opt-preview">
      <h3>Added with preview&nbsp;{PRE}</h3>
      <p class="q-note">Every row sits on top of the released controls above. None replaces one.</p>
      {table(["Control", "Design requirement", "What Microsoft documents", "Label"], [
        ["Agent 365 gateway integration<span class=\"rt\">Visibility, not the boundary</span>",
         "Connect the API Management gateway so admins can see registered servers and block one. Treat the block as extra visibility. It does not replace backend isolation. This is separate from the Agent 365 BYO server route below.",
         f"Agent 365 can discover and govern servers registered with a connected gateway {evp('pv-disc')}. It can block servers and control single tools on supported tiers {evp('pv-a365-ctrl')}. Tool control needs a static list of allowed tools {evp('pv-a365-static')}. API Management v1 tiers are not supported {evp('pv-a365-v1')}, and v2 tiers lack tool-level control {evp('pv-a365-v2')}.",
         f"{PRE} {REC}"],
        ["Agent 365 consent<span class=\"rt\">Tenant level</span>",
         "Before anyone grants it, name who approves the consent, who reviews the policy changes it allows, and how it is withdrawn.",
         f"An administrator grants the A365 MCP Gateway Policy Operator role at tenant level with a one-time consent {evp('pv-a365-role')}. It lets the service read and write API-scoped policies {evp('pv-a365-rw')}.",
         f"{PRE} {REC}"],
        ["AI Gateway resource type<span class=\"rt\">Objective A</span>",
         "Start any evaluation on the new resource type, not the older AI Gateway tier. Check each example and article against the new type before use.",
         f"From 14 Oct 2026 Microsoft is changing the AI Gateway resource type to Microsoft.ApiManagement/aigateways {evp('pv-res-change')}. Complete the migration before 15 Jan 2027 {evp('pv-res-date')}. The new runtime URL uses the domain ai.gateway.azure.com {evp('pv-domain')}, and keys go in the Authorization header with a Bearer scheme {evp('pv-bearer')}.",
         f"{PRE} {REC}"],
        ["AI Gateway limits<span class=\"rt\">Objective A</span>",
         "Check the network design first. Accept no private endpoint support, a virtual network and subnet that cannot change after creation, two regions and a different safety control, or choose another option.",
         f"Private endpoints are not supported {evp('pv-pe')}. The virtual network and subnet cannot be changed after creation {evp('pv-vnet')}. The content safety policy is not supported {evp('pv-cs')}. During public preview the regions are East US 2 and Sweden Central {evp('pv-regions')}.",
         f"{PRE} {REC}"],
        ["Gateway publishing<span class=\"rt\">Objective A</span>",
         "Publish approved tools through the gateway. Give the gateway its own backend credential, scoped to what the tools need.",
         f"The gateway can combine tools from remote MCP servers, OpenAPI APIs and connectors behind gateway MCP endpoints {evp('pv-aig-comb')}. With a shared backend connection, callers use that connection's permissions {evp('pv-shared-cred')}.",
         f"{PRE} {REC}"],
        ["Tool threat protection: who can use it<span class=\"rt\">Extra defence</span>",
         "Use it only in flows that carry a user token. Keep least privilege and human approval for destructive tools. Do not rely on it alone.",
         f"It requires a delegated Entra user token {evp('pv-ttp-token')}. App-only service-to-service calls are not supported {evp('pv-ttp-app')}. A Defender or Purview license is required {evp('pv-ttp-lic')}.",
         f"{PRE} {REC}"],
        ["Tool threat protection: modes and scope<span class=\"rt\">Extra defence</span>",
         "Test Audit mode, Block mode and the failure handling before trusting either. Plan for tools that already ran.",
         f"Audit mode fails open {evp('pv-ttp-audit')}. Block mode fails closed {evp('pv-ttp-block')}. One policy applies to every tool and caller of a server, not to one tool {evp('pv-ttp-scope')}. A denial after the call cannot undo it {evp('pv-ttp-post')}.",
         f"{PRE} {REC}"],
        ["Agent 365 BYO server route<span class=\"rt\">Separate route</span>",
         "Treat this as a separate registration route, not as the API Management gateway integration. Require developer registration and admin approval. Confirm its public endpoint fits the backend isolation target. Test each listed client surface before relying on it.",
         f"BYO servers route through the Agent 365 Tooling Gateway {evp('pv-byo-route')}. Preview clients: Copilot Studio, VS Code, Claude Code and GitHub Copilot CLI; not Foundry or declarative agents {evp('pv-byo-surf')}. An IT admin approves or rejects requests in the Microsoft 365 admin center {evp('pv-byo-approval')}. Servers need a publicly accessible endpoint {evp('pv-byo-endpoint')}. BYO tool-level blocking is planned {evp('pv-byo-tool-plan')}.",
         f"{PRE} {REC}"],
        ["Foundry gateway routing<span class=\"rt\">Separate route</span>",
         "Create new tools in the Foundry portal without managed OAuth. Check the endpoint, sign-in and logs. Do not assume old tools are covered.",
         f"Only new MCP tools created in the Foundry portal without managed OAuth are routed through an AI gateway {evp('pv-fy-prev')}. Routing is applied only at tool creation, and existing tools are not mediated automatically {evp('pv-fy-new')}.",
         f"{PRE} {REC}"],
        ["Outbound filter, optional<span class=\"rt\">Objective B</span>",
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
    <p class="goal"><b>Goal</b>Show where each control reaches and where it stops.&nbsp;{REC}</p></header>
    {table(["Environment", "Use", "Cannot", "Sources"], [
        ["Managed VS Code",
         "VS Code policy: allowlist, denylist and managed-only mode. Add Windows outbound limits where applicable.",
         "Apply to other MCP clients. These are VS Code policies.",
         ev('vs-allow', 'vs-deny', 'vs-managed')],
        ["GitHub Copilot, managed settings",
         "An allowlist by server URL in managed settings.",
         "Cover servers in custom agent profiles or the built-in GitHub server. Coverage varies by environment.",
         ev('gh-url', 'gh-block', 'gh-profiles', 'gh-builtin', 'gh-vary')],
        ["GitHub Copilot cloud agent",
         "Managed settings where the environment is covered.",
         "Use the agent firewall as the MCP control. It does not apply directly to MCP server processes.",
         ev('gh-fw', 'gh-vary')],
        ["Foundry agents",
         "Network isolation of the project with private endpoints, and an allowed tool list on each MCP tool, written by the pipeline.",
         f"Tool connectivity depends on where the downstream service is hosted.",
         ev('fy-gov', 'fy-pe', 'fy-tool', 'fy-allowed')],
        ["Copilot Studio",
         "A Power Platform advanced connector policy (ACP) that blocks a whole MCP server, set by the pipeline.",
         f"Block individual MCP tools through ACP. Custom and HTTP connector types aren't yet supported by ACP. Blocking a connector also blocks the MCP tools that rely on it.",
         ev('studio', 'pp-block', 'pp-api', 'pp-certified', 'pp-custom')],
        ["Unmanaged workstation",
         "Protect the backend on its own with the isolation and identity controls.",
         f"Rely on client rules. We assume none apply. {REC}",
         "Design requirement"],
        ["Local stdio server",
         "An exact-command list in GitHub managed settings, plus client and endpoint policy.",
         "The stdio transport uses standard input and output. Apply client and endpoint controls.",
         ev('stdio', 'stdio-io', 'gh-cmd')],
        ("opt-preview",
         ["Foundry, new tools with gateway routing",
          "Create the tool in the Foundry portal without managed OAuth, so it routes through an AI gateway. Check the endpoint and the logs.",
          "Cover tools made before routing, or tools that use managed OAuth.",
          evp('pv-fy-prev', 'pv-fy-new')]),
        ("opt-preview",
        ["Agent 365 BYO server route",
         "Require developer registration and admin approval before use. Test the listed client surfaces one by one.",
         "An IT admin approves each request. Use a publicly accessible endpoint. Foundry and Microsoft 365 declarative agents are unsupported clients. BYO tool-level blocking is planned. Version 2 has no tool-level control in the separate API Management integration.",
         evp('pv-byo-surf', 'pv-byo-tool-plan', 'pv-a365-v2', 'pv-byo-route', 'pv-byo-approval', 'pv-byo-endpoint')]),
        ("opt-preview",
         ["Local stdio server, with preview",
          "Keep the released client and endpoint controls. Consider the preview firewall only for remote MCP traffic.",
          "The Global Secure Access MCP firewall sees remote servers only. Local servers on a device aren't visible, and JSON-RPC batches aren't inspected.",
          evp('fw-remote')]),
    ])}
  </section>
"""

# ---- tests ---------------------------------------------------------------
TESTS = f"""
  <section class="sec" id="tests" aria-labelledby="h-tests">
    <header class="sh"><h2 id="h-tests">Acceptance tests</h2>
    <p class="goal"><b>Goal</b>Each row is a target outcome. API Management alone does not guarantee them. None has been run.&nbsp;{REC}</p></header>
    {table(["Test", "Expected result", "Objective", "Result"], [
        ["Call an approved MCP server through API Management", "Allowed", "A", "Not run"],
        ["Call the protected backend directly", "Blocked", "A", "Not run"],
        ["Call API Management without valid authorization", "Rejected", "A", "Not run"],
        ["Add an unapproved remote MCP server in a managed client", "Blocked", "B", "Not run"],
        ["Change the MCP URL in VS Code to a different server", "Blocked", "B", "Not run"],
        ["Start an unauthorized local MCP server", "Blocked or contained by endpoint controls", "B", "Not run"],
        ["Merge a pull request that denies a server", "Blocked in every target the pipeline reaches", "B", "Not run"],
        ["Edit a target by hand, then run the pipeline", "The edit is overwritten or flagged", "B", "Not run"],
        ["Repeat the direct call by IP address, from an unmanaged client, by another network path and from a cloud-hosted agent", "Blocked", "A", "Not run"],
    ])}
    <div class="sub3 opt-preview">
      <h3>Added with preview&nbsp;{PRE}</h3>
      {table(["Test", "Expected result", "What establishes the guarantee", "Result"], [
        ["Approved client calls the approved gateway MCP endpoint", "Allowed", "Gateway sign-in and the published tool policy", "Not run"],
        ["Admin blocks a whole MCP server in the API Management integration", "Denied at the gateway", "A verified integration and a runtime block", "Not run"],
        ["Admin blocks a single tool in the API Management integration", "Denied, only on a supported gateway with a static tool list", "An explicit tool-level policy test", "Not run"],
        ["Threat protection sees a risky tool argument", "Tool not run", "Block mode before the call", "Not run"],
        ["Threat protection sees a risky tool result", "Result withheld; the tool may already have run", "Block mode after the call", "Not run"],
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
        <li><strong>Publish.</strong> Publish the server through the gateway. Set the backend credential or managed identity, authorization, policies and logging. Use the gateway URL it gives you.</li>
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
    f"<strong>Nothing is tested in our tenant.</strong> Every expected result above is a target, not a result.",
    f"<strong>GitHub exemptions.</strong> Custom agent profiles and the built-in GitHub server are outside the allowlist, and coverage varies by environment. {ev('gh-profiles', 'gh-builtin', 'gh-vary')}",
    f"<strong>GitHub cloud agent firewall.</strong> It does not directly control MCP server processes. Do not treat it as control of the MCP server itself. {ev('gh-fw')}",
    f"<strong>Foundry and Copilot Studio.</strong> The sources show network isolation, a tool list per agent and blocking a whole MCP server. {ev('fy-gov', 'fy-allowed', 'pp-block')} Blocking one chosen external MCP URL in either was not found in the sources checked on {CHECKED}, so the design does not rely on it.",
    f"<strong>Power Platform API gap.</strong> ACP supports MCP connectors for server-level blocks {ev('pp-block')}, but the programmatic tutorial has no MCP-specific example {ev('pp-api')}. Confirm that the target environment and API expose the server before automating this policy. Custom and HTTP connector types aren't supported {ev('pp-custom')}. Build and test one target at a time.",
    f"<strong>Drift.</strong> A change made by hand in a target is not in the repository. The pipeline must overwrite it or raise an alert. {REC}",
    f"<strong>Local stdio servers.</strong> The client starts a local server as a subprocess {ev('stdio')}. The stdio transport uses standard input and standard output {ev('stdio-io')}. Apply client and endpoint controls.",
    f"<strong>Unmanaged workstations.</strong> Client rules are not assumed to apply there. Objective A relies on the backend refusing everyone but the gateway. {REC}",
    f"<strong>Windows endpoint outbound block.</strong> It stops all traffic that matches no rule, not only MCP, and rules by name have limits with proxies and some VPN tunnels. {ev('ifw-block', 'dk-limits')}",
    f"<strong>Feature release status.</strong> Microsoft announced general availability of API Management MCP governance in Nov 2025 {ev('apim-ga', 'apim-ga-tiers')}. Management features vary by tier {ev('pv-apim-tier')}. Confirm the tier you use.",
]
PV_GAPS_LIST = [
    f"<strong>Preview terms.</strong> Microsoft states preview features are not meant for production use and may have restricted functionality. Use a sandbox. {evp('pv-notprod')}",
    f"<strong>Resource migration.</strong> The AI Gateway resource type is changing and the older tier is permanently removed after the 15 Jan 2027 retirement date. {evp('pv-res-change', 'pv-res-date', 'pv-res-removed')}",
    f"<strong>Network limits.</strong> No private endpoints; the virtual network and subnet cannot change after creation. Check network and data-location rules first. {evp('pv-pe', 'pv-vnet', 'pv-regions')}",
    f"<strong>Agent 365 BYO coverage.</strong> The route requires a publicly accessible server endpoint {evp('pv-byo-endpoint')}. It supports four client surfaces; Foundry and Microsoft 365 declarative agents aren't supported {evp('pv-byo-surf')}. Individual-tool blocking for BYO servers is planned, not available yet {evp('pv-byo-tool-plan')}.",
    f"<strong>Other preview routes.</strong> In the separate API Management integration, v2 tiers lack tool-level access control {evp('pv-a365-v2')}. Foundry gateway routing covers only new MCP tools created in the portal without managed OAuth {evp('pv-fy-prev')}.",
    f"<strong>API Management integration does not force use.</strong> Agent 365 does not automatically route agents through a customer-hosted gateway. Configure agents to use the gateway endpoint, and make the backend refuse direct calls. {ev('iso-nogw')}",
    f"<strong>Threat protection needs a user token.</strong> App-only calls are not supported, a license is needed, and a denial after the call cannot undo it. {evp('pv-ttp-token', 'pv-ttp-app', 'pv-ttp-lic', 'pv-ttp-post')}",
    f"<strong>Keep the Agent 365 routes separate.</strong> The API Management integration discovers servers registered with the connected gateway {evp('pv-disc')}. BYO servers use a separate developer registration and admin approval flow {evp('pv-byo-route', 'pv-byo-approval')}. Do not treat either route as a pipeline sync.",
    f"<strong>Consent scope.</strong> The Agent 365 consent lets the service write API-scoped policies. Review it before granting. {evp('pv-a365-rw')}",
    f"<strong>Shared backend credential.</strong> With a shared backend connection, authorized callers use that connection's permissions. Scope upstream credentials narrowly. {evp('pv-shared-cred')}",
    f"<strong>Optional outbound filter.</strong> The Global Secure Access MCP firewall carries the preview label and sees remote servers only. {evp('fw-preview', 'fw-remote')}",
    f"<strong>New resource type untested.</strong> We have not tested Agent 365 or Foundry against the new resource type. Test it in your tenant.",
]
GAPS_OL = "\n".join(f"<li>{x}</li>" for x in GAPS_LIST)
PV_GAPS_OL = "\n".join(f"<li>{x}</li>" for x in PV_GAPS_LIST)
GAPS = f"""
  <section class="sec" id="gaps" aria-labelledby="h-gaps">
    <header class="sh"><h2 id="h-gaps">Known gaps and what has not been tested</h2>
    <p class="goal">{tg("u", "Bad&nbsp;news&nbsp;first")} Read these limits before you rely on the design.</p></header>
    <ol>
{GAPS_OL}
    </ol>
    <div class="sub3 opt-preview">
      <h3>Added with preview&nbsp;{PRE}</h3>
      <ol>
{PV_GAPS_OL}
      </ol>
    </div>
  </section>
"""

# ---- fallback ------------------------------------------------------------
FALLBACK = f"""
  <section class="sec opt-preview" id="fallback" aria-labelledby="h-fallback">
    <header class="sh"><h2 id="h-fallback">Fallback</h2>
    <p class="goal"><b>Goal</b>If a preview feature changes, keep the released-only design running underneath. Use the preview controls in a sandbox only.&nbsp;{REC}</p></header>
    <ol class="steps">
      <li>Keep production MCP servers behind the released-only design, using only API Management features whose release status we have confirmed.</li>
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
      <li><span class="n">1</span><h3>Do we allow preview features at all?</h3><p>Choices: never, in a sandbox only, or later. The released-only design works without preview.</p></li>
      <li><span class="n">2</span><h3>Which comes first: developer workstations or hosted agents?</h3><p>Workstations call for client rules and, on Windows, outbound limits. Hosted agents call for network isolation and data policies. Start where the more sensitive backends are. See the <a href="#env">environment table</a>.</p></li>
      <li><span class="n">3</span><h3>Do we accept a default outbound block on managed Windows laptops?</h3><p>Decide before rollout. The effect on other traffic is in the <a href="#gaps">gaps</a>.</p></li>
      <li><span class="n">4</span><h3>Who reviews list changes and owns the pipeline?</h3><p>Name the reviewers of the repository, the pipeline owner and the person called when a target fails to update.</p></li>
      <li class="opt-preview"><span class="n">5</span><h3>Who approves and reviews the Agent 365 consent?</h3><p>The consent lets the service write API policies. Name an approver and a reviewer. See the <a href="#controls">controls</a>.</p></li>
      <li class="opt-preview"><span class="n">6</span><h3>What ends the pilot?</h3><p>Set the exit evidence now: terms accepted, features released, clients covered. Without it the pilot has no end. See the <a href="#fallback">fallback</a>.</p></li>
      <li class="opt-preview"><span class="n">7</span><h3>Does a gateway with no private endpoints fit our network rules?</h3><p>The new resource has no private endpoints. Check the rules before building. See the <a href="#gaps">gaps</a>.</p></li>
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
      <p class="sub">Each product fact has a quote, found word for word on its source page on {CHECKED}. The link opens the page at the quote. Page date is the date the page shows. {safe(f"{SAFE_COUNT} quotes back the released-only design.")}{prev(f"{len(QUOTES)} quotes in all: {SAFE_COUNT} back the released-only design and {PV_COUNT} back the preview additions.")}</p>
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
