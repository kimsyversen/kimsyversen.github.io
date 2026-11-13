"""Build mcp-governance-microsoft.html.

Usage: python3 -I scripts/build-mcp-governance.py

Head, style, marker defs and the Made with AI note are cut from the finished
governance summary page so both pages look alike. The build stops if a marker is
missing. Quotes live in mcp_governance_evidence.py.

The page has one design for released features and one section, With preview, for
everything that needs a preview feature. Released sections may cite released-only
quotes through ev(); the preview section may cite any quote through evp(). The
quote table is written into the fact check file, mcp-governance-microsoft.factcheck.md,
between the Source quotes markers. Every V-number on the page links to its row there.
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
NOTES = ROOT / "mcp-governance-microsoft.factcheck.md"
FACTCHECK_URL = "https://github.com/kimsyversen/kimsyversen.github.io/blob/master/mcp-governance-microsoft.factcheck.md"
QUOTES_BEGIN = "<!-- Begin source quotes -->"
QUOTES_END = "<!-- End source quotes -->"
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
DESC = "A short design to make a gateway the only way to reach a company MCP server, comparing API Management's supported MCP capabilities with the separate AI Gateway public preview product and its preview integrations."
HEAD = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", HEAD, flags=re.S)
HEAD = re.sub(r'(<meta name="description" content=")[^"]*(")', rf"\g<1>{DESC}\2", HEAD)

SAFE_COUNT = len(QUOTES) - len(PREVIEW_ONLY)
PV_COUNT = len(PREVIEW_ONLY)

# Own rules, appended after the shared style so the look stays the same.
EXTRA_CSS = """<style>
.intro{grid-template-columns:1fr}
.fig-scroll pre.ascii{margin:0;font:0.8rem/1.3 var(--mono);white-space:pre;min-width:max-content;padding:2px 0}
pre.ascii .stop{color:var(--red)}
pre.ascii .ttl{font-weight:700}
pre.ascii .new{background:var(--red-soft);text-decoration:underline;text-underline-offset:2px}
.sub3{margin-top:6px}
.sub3 h3{font:700 1.02rem/1.35 var(--display);font-stretch:105%;margin:0 0 4px}
.sub3 h4{font:700 0.95rem/1.35 var(--display);margin:14px 0 4px}
.sec > .sub3{margin-top:26px}
tr.grp th{text-align:left;background:var(--bg2,rgba(127,127,127,.12));font-weight:700;padding:8px 10px}
.steps{margin:0;padding-left:1.4rem;display:grid;gap:8px}
/* Text uses the full page width. The shared style caps these at 36 to 56rem and sets text-wrap:balance, which shortens every line to about half of the 1200px page. */
.lead,.decision p,.blk > .sub,.goal,.body > p,figcaption,.ans p,.q-note{max-width:none}
p,li,td,th,dd,summary,figcaption,h4{text-wrap:wrap}
/* Design switch. Blocks tagged view-safe or view-preview show for one choice only. */
body[data-view="safe"] .view-preview{display:none!important}
body[data-view="preview"] .view-safe{display:none!important}
.toc{display:flex;align-items:center;gap:12px}
.toc ul{flex:1;min-width:0}
.seg-wrap{display:flex;flex:none;align-items:center;gap:10px;margin:5px 0}
.seg-lbl{font:600 0.72rem/1 var(--body);letter-spacing:0.05em;text-transform:uppercase;color:var(--muted);white-space:nowrap}
.seg{display:flex;flex:none}
.seg button{font:600 0.72rem/1 var(--body);letter-spacing:0.05em;text-transform:uppercase;padding:7px 9px;border:1px solid var(--ink);background:none;color:var(--ink);cursor:pointer;white-space:nowrap}
.seg button + button{border-left:0}
.seg button:hover{background:var(--hover)}
.seg button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
/* On a phone only the switch stays pinned. The contents links scroll away with the page. */
@media (max-width:640px){.toc{display:contents}.toc ul{margin-top:34px;border-top:1px solid var(--rule)}.seg-wrap{position:sticky;top:0;z-index:5;background:var(--bg);margin:0;padding:8px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}}
@media print{.seg-wrap{display:none}.view-safe,.view-preview{display:revert!important}}
</style>
<noscript><style>body[data-view] .view-preview,body[data-view] .view-safe{display:revert!important}.seg-wrap{display:none!important}</style></noscript>"""

SCRIPT = """<script>
(function(){
  // old links to a source quote (#ev-V12) now open the fact check file
  var h = location.hash;
  if(/^#ev-V\\d+$/.test(h)){ location.replace('@@FACT@@' + h); return; }
  // choose the design shown at the top; the choice lives in ?path=
  var body = document.body;
  var btns = document.querySelectorAll('[data-view-btn]');
  function urlFor(o){
    var u = new URL(location.href);
    if(o === 'safe'){ u.searchParams.delete('path'); } else { u.searchParams.set('path', o); }
    return u.pathname + u.search + u.hash;
  }
  function setView(o, keepUrl){
    body.setAttribute('data-view', o);
    btns.forEach(function(b){ b.setAttribute('aria-pressed', b.getAttribute('data-view-btn') === o ? 'true' : 'false'); });
    if(!keepUrl){ try{ history.replaceState(null, '', urlFor(o)); }catch(e){} }
  }
  function followHash(){
    var id = location.hash.slice(1);
    if(!id) return;
    try{ id = decodeURIComponent(id); }catch(e){}
    var el = document.getElementById(id);
    if(!el) return;
    var other = body.getAttribute('data-view') === 'safe' ? 'preview' : 'safe';
    if(el.closest('.view-' + other)){ setView(other); el.scrollIntoView(); }
  }
  btns.forEach(function(b){ b.addEventListener('click', function(){ setView(b.getAttribute('data-view-btn')); }); });
  document.querySelectorAll('[data-view-go]').forEach(function(a){ a.addEventListener('click', function(){ setView(a.getAttribute('data-view-go')); }); });
  var m = /[?&]path=(safe|preview)(?:&|$)/.exec(location.search);
  setView(m ? m[1] : 'safe', true);
  followHash();
  window.addEventListener('hashchange', followHash);
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
})();
</script>""".replace("@@FACT@@", FACTCHECK_URL)


# ---- helpers -------------------------------------------------------------
def _links(keys):
    ids = sorted((IDS[k] for k in keys), key=lambda v: int(v[1:]))
    return " ".join(f'<a class="ev" href="{FACTCHECK_URL}#ev-{v}">{v}</a>' for v in ids)


def ev(*keys):
    """Evidence links for the released design. Stops on a quote that only the preview design uses."""
    hidden = [k for k in keys if k in PREVIEW_ONLY]
    if hidden:
        sys.exit(f"released content links preview-only quotes: {hidden}")
    return _links(keys)


def evp(*keys):
    """Evidence links for the preview section. Any quote may be cited there."""
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
        if rc == "grp":
            trs.append(f'<tr class="grp"><th colspan="{len(head)}" scope="colgroup">{r[0]}</th></tr>')
            continue
        attr = f' class="{rc}"' if rc else ""
        trs.append(f"<tr{attr}>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    body = "\n".join(trs)
    return f'<div class="tbl-wrap"><table class="{cls}">\n<thead><tr>{th}</tr></thead>\n<tbody>\n{body}\n</tbody>\n</table></div>'



def pname(name, group):
    return f'{name}<span class="rt">{group}</span>'


def control_label(anchor, title, objective):
    return f'<span id="ctrl-{anchor}">{title}</span><span class="rt">{objective}</span>'


def control_link(anchor, title):
    return f'<a href="#ctrl-{anchor}">{title}</a>'


def ascii_fig(name):
    raw = (ROOT / f"mcp-governance-microsoft.figure-{name}.txt").read_text(encoding="utf-8")
    for tag in ("red", "b", "new"):
        if raw.count(f"[{tag}]") != raw.count(f"[/{tag}]"):
            sys.exit(f"unbalanced [{tag}] markers in figure {name}")
    out = html.escape(raw.rstrip("\n"), quote=False)
    out = out.replace("[red]", '<span class="stop">').replace("[b]", '<span class="ttl">').replace("[new]", '<span class="new">')
    return out.replace("[/red]", "</span>").replace("[/b]", "</span>").replace("[/new]", "</span>")



def anchors(*ids):
    """Empty anchors that keep the ids of removed headings working."""
    return "".join(f'<span id="{i}"></span>' for i in ids)


# ---- masthead ------------------------------------------------------------
MAST = f"""
  <a class="skip" href="#main-content">Skip to content</a>
  <header class="mast">
    <div class="meta"><span>Design · Microsoft stack · MCP</span><span>Documentation checked 11 Nov 2026</span></div>
    <h1>MCP Governance in a Microsoft ecosystem</h1>
    <div class="intro">
      <p class="lead">A proposed design to make a gateway the only way to reach a company MCP server and to limit managed clients to approved servers, across GitHub Copilot, VS Code, Foundry, Copilot Studio and Microsoft 365 Copilot.</p>
    </div>
  </header>

  <nav class="toc" aria-label="Contents">
    <ul>
      <li><a href="#design">Design</a></li>
      <li><a href="#controls">Controls</a></li>
      <li><a href="#rollout">Rollout</a></li>
      <li><a href="#gaps">Gaps</a></li>
      <li class="view-preview"><a href="#preview">With preview</a></li>
    </ul>
    <div class="seg-wrap"><span class="seg-lbl" id="seg-lbl">Select design</span>
    <div class="seg" role="group" aria-labelledby="seg-lbl">
      <button type="button" data-view-btn="safe" aria-pressed="true">Released only</button>
      <button type="button" data-view-btn="preview" aria-pressed="false">With preview</button>
    </div></div>
  </nav>
"""

# ---- design: one table for parts, control planes and gateways ------------
DESIGN_ROWS = [
    [pname("Approved list in Git", "Source of truth"),
     "Reviewed record of approved and denied MCP servers.",
     "A Git repository, changed by reviewed pull request.",
     control_link("inventory", "Approved inventory")],
    [pname("Sync pipeline", "Source of truth"),
     "On merge, writes the list to each policy target.",
     "A pipeline the company builds. Proposed work; not built yet.",
     control_link("pipeline", "Policy sync, pipeline")],
    [pname("GitHub Enterprise", "Policy target"),
     "Allows or blocks the MCP servers that VS Code and GitHub Copilot may use.",
     f"Managed settings file in the .github-private repository {ev('gh-file')}.",
     f"{control_link('client', 'Client allowlist')}; {control_link('pipeline', 'Policy sync, pipeline')}"],
    [pname("Power Platform", "Policy target"),
     "Controls which MCP connectors Copilot Studio agents may use.",
     f"Power Platform admin center {UNV}. The pipeline would use the Power Platform API, not verified for MCP.",
     control_link("power-platform", "Policy sync, Power Platform")],
    [pname("Microsoft Foundry", "Policy target"),
     "Limits the tools each Foundry agent may call on an MCP server.",
     f"Foundry portal {UNV}. An allowed tool list on each MCP tool; the pipeline for it is not tested.",
     control_link("foundry", "Policy sync, Foundry")],
    [pname("Microsoft 365 admin center", "Policy target"),
     "Offers MCP servers to Microsoft 365 Copilot as federated connectors.",
     f"Microsoft 365 admin center {ev('m365-admin')}. Set by hand; there is no pipeline.",
     f"{control_link('m365', 'Policy sync, Microsoft 365 Copilot')}; {control_link('m365-network', 'Microsoft 365 Copilot network path')}"],
    [pname("Client and device controls", "Enforcement"),
     "Managed URL policies and, on Windows, outbound firewall rules where applicable.",
     f"Intune and VS Code policy {INF}. They sit on the device, so they do not cover Microsoft 365 Copilot.",
     f"{control_link('client', 'Client allowlist')}; {control_link('windows', 'Windows outbound limits')}; {control_link('stdio', 'Local stdio servers')}"],
    [pname("Azure API Management", "Gateway"),
     f"The one door to the company MCP server, for every client. Its AI gateway capabilities extend the service and are not a separate offering {ev('apim-ai-not-separate')}.",
     f"Azure {INF}. MCP server management is listed for classic and v2 tiers {ev('mcp-tiers')}.",
     f"{control_link('gateway', 'Gateway')}; {control_link('backend', 'Backend isolation')}; {control_link('identity', 'Identity')}. Choose a v2 tier {REC}: the Foundry integration lists only v2 instances {ev('fy-aig-v2')}. A classic tier works for MCP but rules that integration out."],
    [pname("AI Gateway integrated with Foundry", "Gateway option"),
     f"The AI Gateway option in the Foundry portal. It is also an API Management service {ev('fy-aig-apim')}.",
     f"Create new makes a Basic v2 instance {ev('fy-aig-new')}. Use existing lists only v2 instances in the same tenant and subscription as the Foundry resource {ev('fy-aig-v2', 'fy-aig-same')}.",
     f"Not used for MCP tools: routing them through it is a preview feature. If Foundry is connected, use the company's existing v2 instance, so there is one gateway and one set of policies {REC}. Microsoft suggests Standard v2 or Premium v2 for production {ev('fy-aig-prod')}. {INF} Interpretation by AI: one instance can serve both roles. Not tested."],
    [pname("Company MCP server", "Backend"),
     "Only the gateway may reach it.",
     "The server's own network and identity settings.",
     f"{control_link('backend', 'Backend isolation')}; {control_link('identity', 'Identity')}"],
]

DESIGN = f"""
    <div class="sub3" id="parts">
      {anchors("parts-of-the-design", "planes", "control-planes", "which-gateway", "which-gateway-2")}
      <h3>Parts and control planes</h3>
      <p class="q-note">Map the approved inventory into each policy target. Visibility alone does not enforce access. {REC}</p>
      {table(["Part", "What it does", "Where it is set or run", "Use in this design"], DESIGN_ROWS)}
      <p class="q-note">{UNV} marks an admin surface name taken from the control plane list this page was checked against, not from a quoted source. {INF} marks interpretation by AI. Agent approval and lifecycle are separate from this page's MCP server workflow.</p>
    </div>
"""

# ---- design figure -------------------------------------------------------
# The figures are plain text files beside the page. Edit them, then rebuild.
# [red]...[/red] marks text that means caution, unverified or denied. [b]...[/b] marks a box title.

DESC_SAFE = ("Design target: a Git repository holds the approved and denied MCP servers. A reviewed pull request changes it. "
             "After merge, a pipeline applies the list to three targets: Power Platform policy for Copilot Studio, "
             "GitHub Enterprise managed settings, and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: "
             "Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. The released-only design uses the Azure API Management service and its existing AI gateway capabilities; MCP server management is listed for supported classic and v2 tiers, with capability availability varying by tier. "
             "The separate AI Gateway product is not used in this design. The first three clients pass through client sign-in, Windows outbound firewall rules administered by Intune on managed Windows devices where applicable, API Management identity checks and authorization, and the company MCP server, which accepts calls only from the gateway. "
             "The remote MCP URL allowlist applies to managed VS Code and GitHub Copilot clients; it is separate from device egress rules. "
             "Microsoft 365 Copilot calls API Management from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. A direct call from a client to the server is blocked. "
             "Agent 365 is not drawn: company servers join it through preview features.")
DESC_PREVIEW = ("Design target: the figure shows the released-only design with the preview additions shaded. The preview design uses the separate AI Gateway product, which is in public preview, in place of the Azure API Management service gateway in the released-only design. A Git repository holds the approved and denied MCP servers. "
                "After a reviewed merge, a pipeline applies the list to Power Platform policy for Copilot Studio, "
                "GitHub Enterprise managed settings and Foundry. A fourth target, the Microsoft 365 admin center, is set by hand. Each target names where it is administered and points to the clients it governs: "
                "Copilot Studio, VS Code with GitHub Copilot, Foundry agents and Microsoft 365 Copilot. "
                "The first three pass through client sign-in, Windows outbound firewall rules administered by Intune on managed Windows devices where applicable, AI Gateway identity checks and authorization with tool threat protection. With the Agent 365 integration, server inventory and blocking are listed for API Management v2 and AI Gateway; tool blocking, activity observability and threat protection are listed only for AI Gateway. "
                "The remote MCP URL allowlist applies to managed VS Code and GitHub Copilot clients; it is separate from device egress rules. "
                "Microsoft 365 Copilot calls the gateway from the Microsoft cloud, from fixed outbound addresses, and skips the client controls. "
                "A direct call from a client to the server is blocked. Below the gateway, the Microsoft 365 admin view shows the all-agents registry, MCP server status, and the preview requests queue. Shaded in the client controls box: the Global Secure Access MCP firewall. Shaded in the gateway box: the separate product, its public preview status, the Agent 365 tool block and tool threat protection. A separate shaded BYO server route box shows the Agent 365 Tooling Gateway, which is not for Foundry agents. Foundry gateway routing and the Defender checks are in the tables below.")

FIGURE = f"""
  <section class="sec" id="design" aria-labelledby="h-design">
    <header class="sh"><h2 id="h-design">The design</h2>
    <p class="goal"><b>In short</b>Keep the company MCP server behind the gateway and limit managed clients to approved servers.&nbsp;{REC}</p>
    <p class="goal view-safe"><b>Scope</b>This is the released-only design. It uses supported MCP capabilities in the API Management service, subject to tier availability. Preview features are in the other design: select With preview above, or read <a href="#preview">With preview</a>.</p>
    <p class="goal view-preview"><b>Scope</b>This design replaces the API Management service gateway with the separate AI Gateway product, which is in public preview, and adds the Agent 365 integration. Use it only in a sandbox. The released-only design stays underneath. Details and limits are in <a href="#preview">With preview</a>.</p></header>
    <figure class="view-safe">
      <div class="fig-scroll" tabindex="0" role="region" aria-label="MCP gateway design diagram, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_SAFE}">{ascii_fig("safe")}</pre>
      </div>
    </figure>
    <figure class="view-preview">
      <div class="fig-scroll" tabindex="0" role="region" aria-label="With-preview MCP gateway design diagram, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_PREVIEW}">{ascii_fig("preview")}</pre>
      </div>
      <figcaption class="q-note">Shaded boxes and lines are what preview adds. Everything else is the released design. With preview, connect the gateway to Agent 365 and test tool threat protection in a sandbox. The view combines distinct admin pages: Agents &gt; All agents &gt; Registry, and Agents &gt; Tools &gt; Registry or Requests (preview). {ev('a365-agent-all', 'a365-tools-tabs', 'a365-tools-status')} The BYO server route is separate; its limits are in the controls below.</figcaption>
    </figure>
{DESIGN}  </section>
"""

# ---- controls ------------------------------------------------------------
GR_PREV = [
    ["Tool call and tool response guardrails", "Foundry", "3 and 6",
     f"Both are in preview {evp('gr-fy-call', 'gr-fy-resp')}. The response control scans for indirect prompt injection {evp('pv-gr-fy-indirect')}. Controls take no effect for tools outside the supported list {evp('pv-gr-fy-support', 'pv-gr-fy-list', 'pv-gr-fy-noeffect')}. {INF} Interpretation by AI: the list does not name MCP, so do not rely on them for MCP."],
]
GR_PREV_RAW = [
    ("opt-preview", ["Threat detection", "Copilot Studio", "3", f"An external service allows or blocks a tool call. The page is prerelease {evp('pv-gr-cs-pre', 'pv-gr-cs-det')}. By default the call goes ahead if the service is silent for one second. This can be changed to block {evp('pv-gr-cs-1s', 'pv-gr-cs-errblock')}. It runs only with generative orchestration {evp('pv-gr-cs-gen')}. The agent shares data with the provider {evp('pv-gr-cs-share')}."]),
    ("opt-preview", ["Defender real-time protection", "Foundry, Copilot Studio", "Foundry 3 and 6, plus user input and final answer. Copilot Studio 3",
     f"Checks agent activity and can block a risky action before it runs {evp('pv-gr-def-how')}. Foundry (Preview): user requests, agent responses, tool calls and tool responses {evp('pv-gr-def-fy', 'pv-gr-def-fy2')}. Copilot Studio (Preview): tool calls {evp('pv-gr-def-cs', 'pv-gr-def-cs2')}."]),
    ("opt-preview", ["Defender on the Agent 365 path", "Agent 365", "3",
     f"Covers tool calls to customer MCP tools onboarded to Agent 365, but not agents that use unsupported tools or skip Work IQ MCP {evp('pv-gr-def-a365', 'pv-gr-def-unsup')}. {INF} Interpretation by AI: the line is not labelled preview on the page, but it needs a customer MCP server onboarded to Agent 365, and the sources call that path preview {evp('pv-byo-surf')}."]),
    ("opt-preview", ["Defender rules and scope", "Foundry, Copilot Studio, Agent 365", "Same as the two rows above",
     f"The default rule only audits {evp('pv-gr-def-audit')}. A custom rule blocks {evp('pv-gr-def-block')}. Blocking covers malicious content, secret exfiltration, evasion techniques and email to an unsafe domain {evp('pv-gr-def-mal', 'pv-gr-def-secret', 'pv-gr-def-evasion', 'pv-gr-def-mail')}. The email scenario is checked only at the tool request {evp('pv-gr-def-mailonly')}. A rule can be scoped only to agents with a Microsoft Entra agent ID {evp('pv-gr-def-entra')}."]),
    ("opt-preview", ["Defender for Endpoint runtime protection", "VS Code, GitHub Copilot", "Not stated",
     f"Local agents are covered by Defender for Endpoint, not by the rules above {evp('pv-gr-def-local')}. The article is prerelease {evp('pv-gr-mde-pre')}. It can block an action before it runs when the inspection method allows it {evp('pv-gr-mde-how')}. The Windows (preview) support table lists the VS Code GitHub Copilot extension {evp('pv-gr-mde-win', 'pv-gr-mde-vs')}. The layer for this client is not stated."]),
]
GR_PREV += [r[1] for r in GR_PREV_RAW]

DESC_GR_SAFE = ("Guardrails by layer for one MCP tool call, in three columns: Foundry agent, Copilot Studio, and VS Code with GitHub Copilot. "
                "Layer 1 which server: Foundry allowed_tools, Copilot Studio data policy, VS Code and GitHub allow and deny lists plus a server trust prompt in VS Code. "
                "Layer 2 person approves: Foundry require_approval, default always, which can be set to never. Copilot Studio can ask the user before running a tool, off by default and unverified for MCP tools. "
                "VS Code shows a confirmation dialog by default, the Allow all level skips it, and a company policy can lock it. "
                "Layer 3 call content: preview only for Foundry and Copilot Studio. In VS Code a preToolUse hook can deny a call, unverified for MCP tools. "
                "Layer 4 network and gateway: the table lists what applies to every client, plus two lines that apply to Foundry only. Layer 5 company MCP server: the design target is that only the gateway can call it. "
                "Layer 6 tool response: preview only for Foundry. Copilot Studio has a built-in prompt attack block, whose layer is an AI estimate. VS Code can ask for a review of the result before it enters the chat context, and this can be switched off.")

def gname(name):
    return pname(name, "Guardrail")


NONE_ADDED = "None added."

LAYER_ROWS = [
    ("grp", ["Whole path, not tied to one layer"]),
    [control_label("inventory", "Approved inventory", "Objectives A and B"),
     "All clients",
     f"Keep one list of approved MCP servers in a repository, with address, owner, permitted tools and risk class. Change it only by reviewed pull request. Review a server again when its address, sign-in, permissions or tools change. Set client policy from managed settings, not user-editable files. {REC}",
     f"GitHub managed settings apply the allow and deny lists to servers in user and repository settings {ev('gh-profiles')}. The proposed pipeline must configure Foundry and Copilot Studio separately. {REC}"],
    [control_label("pipeline", "Policy sync, pipeline", "Objective B"),
     "GitHub, Power Platform, Foundry",
     f"On merge of a reviewed change, a pipeline applies the list to each target. Each target gets its own credential, limited to writing that target. The pipeline reports any target it could not update. Manual edits in a target are overwritten or flagged on the next run. Nothing is built yet. {REC}",
     f"GitHub managed settings can be hosted on GitHub as a server-managed deployment {ev('gh-deploy')}. They are a file in the .github-private repository, changed by commit and push {ev('gh-file', 'gh-commit')}. Settings refresh within about an hour {ev('gh-refresh')}. Verify propagation. {REC}"],
    [control_label("logging", "Logging and checks", "Objectives A and B"),
     "All clients",
     f"Collect gateway logs and endpoint or client telemetry. Look for unapproved server connections, unexpected MCP processes, failed sign-ins and unusual tool use. Review the approved list on a schedule. Run the acceptance tests. {REC}",
     f"Gateway policies can log every request {ev('gw-policy')}. Microsoft 365 Copilot connector activity can be audited in Purview {ev('m365-audit')}."],

    ("grp", ["Layer 1, which server"]),
    [control_label("power-platform", "Policy sync, Power Platform", "Objective B"),
     "Copilot Studio",
     f"<span id=\"gap-unverified-url-block\"></span>Configure an advanced connector policy for MCP connectors listed in the target environment. Keep classic data policies for custom and HTTP connectors. Use manual configuration until API automation for the actual MCP entry is verified. Do not assume an arbitrary MCP URL is a supported policy entry. {REC}",
     f"ACP supports deployment-pipeline automation {ev('pp-pipe')}, MCP server-level blocking but not per-tool blocks {ev('pp-block')}, and connector blocking also blocks dependent MCP tools {ev('studio')}. Custom and HTTP connectors aren't supported {ev('pp-custom')}. The API tutorial lacks an MCP-specific example; verify this path in the target tenant {ev('pp-api')}. {REC}"],
    [control_label("foundry", "Policy sync, Foundry", "Objective B"),
     "Foundry",
     f"Configure each approved MCP connection with a nonempty allowed tool list. Remove or disable the connection when no tools should be allowed. Validate the pipeline separately. {REC}",
     f"An MCP tool restricts access with a nonempty allowed tool list. An empty list allows every tool {ev('fy-allowed')}."],
    [control_label("m365", "Policy sync, Microsoft 365 Copilot", "Objective B"),
     "Microsoft 365 Copilot",
     f"<span id=\"gap-m365-by-hand\"></span>Add each approved company MCP server by hand as a custom federated connector that points at the gateway address. Clear the external publisher type unless a server is on the list. Stage each connector to named groups. Record every manual change in the repository. {REC}",
     f"Federated connectors use MCP {ev('m365-mcp')}. A custom one starts with an MCP server {ev('m365-server')} and needs an admin role {ev('m365-roles')}. Admins control availability {ev('m365-admin', 'm365-org')}; every setting must allow the user {ev('m365-all')}. Tools can be blocked {ev('m365-toolblock')}. Agent and plugin access has no PowerShell or API option {ev('m365-noapi')}."],
    [control_label("client", "Client allowlist", "Objective B"),
     "VS Code, GitHub Copilot",
     f"Managed clients may use only the MCP addresses on the approved list, which the pipeline writes to GitHub managed settings. Users cannot add their own. {REC}",
     f"VS Code policies set an allowlist, a denylist and a managed-only mode {ev('vs-allow', 'vs-deny', 'vs-managed')}. GitHub settings match a remote server by URL wildcards {ev('gh-url')}, block unmatched servers {ev('gh-block')}, and a deny entry wins {ev('gh-deny')}. Not covered: servers in custom agent profiles and the built-in GitHub server {ev('gh-profiles', 'gh-builtin')}. Coverage varies by environment {ev('gh-vary')}."],
    [gname("Server trust prompt"), "VS Code", NONE_ADDED,
     f"Servers that do not come from the workspace MCP files can need a separate trust decision by the person. VS Code asks again after a configuration change. {ev('gr-vs-trust')}"],
    [control_label("stdio", "Local stdio servers", "Objective B"),
     "VS Code, GitHub Copilot",
     f"Limit which local server commands can start, through managed client policy. Add application control, least-privilege accounts and limits on sensitive files and credentials. Treat local administrators, other MCP clients and unmanaged devices as separate bypass risks. {REC}",
     f"The client launches a local server as a subprocess {ev('stdio')}. The stdio transport communicates over standard input and standard output {ev('stdio-io')}. GitHub managed settings match the exact command and each argument {ev('gh-cmd')}."],

    ("grp", ["Layer 2, person approves"]),
    [gname("Approval"), "Foundry", NONE_ADDED,
     f"require_approval defaults to always, which means a developer approves every call {ev('gr-fy-appr', 'gr-fy-always')}. It can be set to never, or to a list of tools that skip approval {ev('gr-fy-never')}. Microsoft advises approval for high-risk tools that write data {ev('gr-fy-high')}."],
    [gname("Ask before running"), "Copilot Studio", NONE_ADDED,
     f"A maker can set a tool to ask the end user for confirmation in the chat before it runs. The option is off by default. {ev('gr-cs-ask')} {UNV} The page describes tools in general. Not checked whether the option is offered for MCP tools."],
    [gname("Confirmation dialog"), "VS Code", NONE_ADDED,
     f"By default, actions that are not auto-approved need the person's confirmation, and the dialog shows the input parameters {ev('gr-vs-appr', 'gr-vs-manual')}. The Allow all level runs all tool calls without confirmation {ev('gr-vs-allowall')}. Assisted permissions lets an LLM judge assess each call {ev('gr-vs-assist')}. Documented for VS Code only."],
    [gname("Approval lock"), "VS Code", NONE_ADDED,
     f"A company can limit the levels above. A policy that turns off global auto-approval leaves only one-time approval and ignores saved approvals {ev('gr-vs-pol-auto')}. A managed setting can disable Allow all {ev('gr-vs-pol-bypass')}."],
    [gname("Write approval"), "Microsoft 365 Copilot", NONE_ADDED,
     f"For federated connectors, tools that write need user approval {ev('m365-write')}."],

    ("grp", [f"Layer 3, call content. Foundry and Copilot Studio have no released control here. Theirs are in <a href=\"#guardrails-preview\">With preview</a>."]),
    [gname("Tool call hook"), "VS Code, GitHub Copilot", NONE_ADDED,
     f"A preToolUse hook can inspect a supported tool's arguments and deny the call. A filter that misses a tool does not check that call {ev('gr-vs-hook')}. VS Code says hooks are not a substitute for enforced permissions or enterprise controls {ev('gr-vs-hook-not')}. {UNV} Not checked whether a hook sees MCP tool calls."],

    ("grp", ["Layer 4, network and gateway"]),
    [control_label("gateway", "Gateway", "Objective A"),
     "All clients",
     f"Publish each approved remote MCP endpoint through API Management. Check identity, authorize, rate-limit and log. Scope access by app or workload identity. Confirm the release status of each feature before relying on it. {REC}",
     f"For a remote Azure MCP Server, Microsoft suggests API Management as a gateway {ev('gw-consider')}: a single choke point {ev('gw-choke')}. Policies limit rates, restrict tool paths and log requests {ev('gw-policy')}. Clients go through it so the backend is not silently redirected {ev('gw-redirect')}. It can expose REST APIs as MCP servers or pass MCP servers through {ev('pv-apim-mcp')}."],
    [control_label("identity", "Identity", "Objective A"),
     "All clients, gateway and backend",
     f"Only the gateway holds a credential or workload identity the backend accepts. Require the backend to validate token audience and the authorized gateway identity; verify that other identities are rejected. {REC}",
     f"The gateway can check an Entra ID token {ev('in-entra')} or a subscription key {ev('in-key')} before the request goes on {ev('gw-token')}. It can sign in to the backend with its managed identity {ev('out-mi')}. Checking the token again at the backend is a design choice. {REC}"],
    [control_label("m365-network", "Microsoft 365 Copilot network path", "Objective A"),
     "Microsoft 365 Copilot",
     f"Let the gateway accept the Microsoft 365 Copilot outbound addresses, and still require sign-in. Review the address list on a schedule. Do not count on device controls for this client. {INF} Interpretation by AI: calls leave from the Microsoft cloud, so device URL policy and Windows firewall rules do not see them. {REC}",
     f"MCP calls from declarative agents and federated connectors use a fixed set of outbound addresses {ev('m365-ip')}. A server that filters by source address must allow them {ev('m365-ip-allow')}. Allow listing does not replace sign-in or authorization {ev('m365-ip-auth')}. The list can change with seven days' notice {ev('m365-ip-change')}."],
    [control_label("windows", "Windows outbound limits", "Objective B"),
     "Managed Windows devices",
     f"Block direct outbound calls from managed Windows devices to MCP servers that are not approved. {REC}",
     f"Intune can set Windows Firewall to block all outbound traffic that matches no rule {ev('ifw-block')}, a setting Microsoft says can be considered for certain highly secure environments {ev('dk-secure')}."],
    [control_label("foundry-network", "Foundry network and sandbox", "Objective B"),
     "Foundry",
     f"For toolboxes, configure project networking and downstream egress rules. A tool allowlist alone does not restrict which server URLs an agent can use. {REC}",
     f"For a Foundry toolbox, its hosting project governs network access {ev('fy-gov')}. Tool connectivity depends on where the downstream service is hosted {ev('fy-tool')}. The Network control limits outbound traffic for hosted agents and prompt agents on the Copilot harness only. Hosted agents also run in per-session VM sandboxes. {ev('gr-fy-net', 'gr-fy-sandbox')}"],

    ("grp", ["Layer 5, company MCP server"]),
    [control_label("backend", "Backend isolation", "Objective A"),
     "Company MCP server",
     f"Switch off public access to the backend. Accept inbound calls from the gateway only, over a private path. {REC}",
     f"Restrict MCP server connectivity so the gateway is the only permitted caller, or use private networking where supported {ev('iso-restrict')}. Azure Functions offers inbound access restrictions and private endpoints {ev('fn-ar', 'fn-pe')}. The classic Consumption plan has no private endpoints {ev('fn-cons')}. The API Management integration does not automatically route agents through a customer-hosted gateway {ev('iso-nogw')}."],

    ("grp", ["Layer 6, tool response. Foundry has a preview control only, in <a href=\"#guardrails-preview\">With preview</a>."]),
    [gname("Untrusted results"), "Foundry", NONE_ADDED,
     f"Microsoft says to treat tool descriptions, annotations and results from remote MCP servers as untrusted input. This is advice, not a control. {ev('gr-fy-untrust')}"],
    [gname("Prompt attack block"), "Copilot Studio", NONE_ADDED,
     f"Built-in protection against user prompt injection (UPIA) and cross-domain prompt injection (XPIA). At runtime the agent blocks attacks of these types. {ev('gr-cs-upia', 'gr-cs-block')} {INF} Interpretation by AI: the source does not say at which layer. It is listed here because cross-domain attacks can arrive in tool results."],
    [gname("Result review"), "VS Code", NONE_ADDED,
     f"Tool approval covers confirmation before or after a tool runs {ev('gr-vs-after')}. Post-approval adds a tool result to the chat context without review, and VS Code warns about prompt injection in external data {ev('gr-vs-post')}. {UNV} Not checked which tools ask for a result review by default."],
]

GUARDRAILS = f"""
    <div class="sub3" id="controls-by-layer">
      {anchors("guardrails", "h-guardrails", "what-each-guardrail-does")}
      <h3 id="h-controls-by-layer">Controls by call layer</h3>
      <p class="q-note">One table, in the order of one MCP tool call. A design control has a requirement. A product guardrail is listed for what it does, so its requirement says none added. Content filters on the user input and the final answer are left out: they are not MCP controls.</p>
      <figure>
        <div class="fig-scroll" tabindex="0" role="region" aria-label="Guardrails by layer, horizontally scrollable">
<pre class="ascii" role="img" aria-label="{DESC_GR_SAFE}">{ascii_fig("guardrails-safe")}</pre>
        </div>
      </figure>
      {table(["Control", "Applies to", "Design requirement", "What Microsoft and GitHub document"], LAYER_ROWS)}
      <p class="q-note">None found means the pages read on 2026-11-11 do not describe a guardrail at that layer. {UNV} Microsoft 365 Copilot is not a column in the figure; its rows are in layers 1, 2 and 4. Microsoft Defender real-time protection and Defender for Endpoint runtime protection are in <a href="#guardrails-preview">With preview</a>.</p>
    </div>
"""

CONTROLS = f"""
  <section class="sec" id="controls" aria-labelledby="h-controls">
    <header class="sh"><h2 id="h-controls">Controls</h2>
    <p class="goal"><b>How to read</b>A means company backend access through the gateway only. B means restricting managed clients to approved MCP servers.</p></header>
{GUARDRAILS}    {anchors("approval-boundaries", "approval-boundaries-and-cross-cutting-guardrails", "env", "h-env")}
  </section>
"""


# ---- rollout: order of work and acceptance tests -------------------------
ROLLOUT = f"""
  <section class="sec" id="rollout" aria-labelledby="h-rollout">
    <header class="sh"><h2 id="h-rollout">Rollout and tests</h2>
    <p class="goal"><b>Goal</b>API Management alone does not guarantee objectives A and B.&nbsp;{REC}</p></header>
    <div class="sub3" id="order">
      <h3 id="h-order">Order of work</h3>
    <ol class="steps">
      <li><strong>First.</strong> Inventory MCP use, put the approved list in a repository and build the pipeline that applies it.</li>
      <li><strong>Next.</strong> Isolate the company MCP backends and require access through API Management.</li>
      <li><strong>Then.</strong> Add endpoint application control, local server limits and outbound policy.</li>
      <li><strong>Finally.</strong> Add monitoring, review exceptions and run the bypass tests on a schedule.</li>
    </ol>
    </div>
    <div class="sub3" id="tests">
      <h3 id="h-tests">Acceptance tests</h3>
    <p class="q-note">No test has been run.</p>
    {table(["Test", "Expected result", "Objective"], [
        ["Call an approved MCP server through API Management", "Allowed", "A"],
        ["Call the protected backend directly", "Blocked", "A"],
        ["Call API Management without valid authorization", "Rejected", "A"],
        ["Add an unapproved remote MCP server in a managed client", "Blocked", "B"],
        ["Change the MCP URL in VS Code to a different server", "Blocked", "B"],
        ["Start an unauthorized local MCP server", "Blocked or contained by endpoint controls", "B"],
        ["Merge a pull request that denies a server", "Blocked in each supported target after policy propagation and client refresh", "B"],
        ["Edit a target by hand, then run the pipeline", "The edit is overwritten or flagged", "B"],
        ["Call an approved connector from Microsoft 365 Copilot", "Allowed, through API Management", "A"],
        ["Add a custom connector for an unapproved server without an admin role", "Blocked", "B"],
        ["Block a connector in the Microsoft 365 admin center", "Unavailable to users after the change takes effect", "B"],
        ["Repeat the direct call by IP address, from an unmanaged client, by another network path and from a cloud-hosted agent", "Blocked", "A"],
    ])}
    </div>
  </section>
"""

# ---- gaps ---------------------------------------------
GAPS_LIST = [
    f"<strong id=\"gap-github-builtin\">Built-in GitHub MCP server.</strong> Allow and deny lists cannot block it {ev('gh-builtin-order', 'gh-builtin')}. Two switches are untested: the MCP servers in Copilot policy, which turns off every MCP server {ev('gh-policy-off')}, and Registry only {ev('gh-reg-only')}, a public preview with weaker enforcement {ev('gh-reg-preview', 'gh-reg-bypass')}. No design control covers it. Pilot both, or limit it through GitHub account permissions.",
    f"<strong id=\"gap-m365-manual\">Microsoft 365 Copilot is set by hand.</strong> Agent and plugin access has no PowerShell or API option {ev('m365-noapi')}, so the pipeline cannot keep this target in step. {UNV} No page read says whether a custom connector can be created by API. Declarative agents that carry their own MCP server were not checked.",
    f"<strong id=\"gap-one-gateway\">One gateway for Foundry and the other clients.</strong> {INF} Interpretation by AI: the same v2 API Management instance can be the Foundry AI Gateway and the gateway for the company MCP server. The source lists the requirements for an existing instance but not this combined use. Not tested.",
    f"<strong id=\"gap-m365-status\">Microsoft 365 Copilot connector status.</strong> {INF} Interpretation by AI: the federated connector pages read on 2026-11-11 carry no preview label for the connectors, so the page treats them as released. Confirm in the target tenant.",
    f"<strong id=\"gap-github-cloud-agent\">GitHub Copilot cloud agent.</strong> Its firewall does not directly filter MCP server processes, so it is not their egress boundary. Only the client allowlist applies. {ev('gh-fw')}",
    f"<strong id=\"gap-windows-outbound\">Windows outbound block.</strong> It can block non-MCP traffic too, and name-based rules have limits with proxies and some VPN tunnels. {ev('ifw-block', 'dk-limits')}",
    f"<strong id=\"gap-tier-availability\">API Management tier availability.</strong> MCP features vary by tier. Confirm the target tier and release status before relying on a feature. {ev('apim-ga', 'apim-ga-tiers', 'pv-apim-tier')}",
]
GAPS_OL = "\n".join(f"<li>{x}</li>" for x in GAPS_LIST)
GAPS = f"""
  <section class="sec" id="gaps" aria-labelledby="h-gaps">
    <header class="sh"><h2 id="h-gaps">Gaps</h2>
    </header>
    <ol>
{GAPS_OL}
    </ol>
    {anchors("open", "h-open", "open-questions")}
  </section>
"""

# ---- with preview --------------------------------------------------------
PREVIEW = f"""
  <section class="sec view-preview" id="preview" aria-labelledby="h-preview">
    <header class="sh"><h2 id="h-preview">With preview&nbsp;{PRE}</h2>
    <p class="goal"><b>In short</b>Use the separate AI Gateway product and the Agent 365 integration in place of the API Management service gateway. AI Gateway is in public preview. Use this design only in a sandbox. If a preview feature changes, switch it off and fall back to the released-only design. {REC}</p>
    <p class="goal"><b>Baseline</b>The released-only design stays underneath. Build it first.</p></header>
    <div class="sub3" id="preview-controls">
      {anchors("added-with-preview-preview")}
      <h3>Added controls</h3>
      <p class="q-note">Dedicated AI Gateway is a separate product that replaces the API Management service gateway. It is the only gateway listed with tool blocking, tool activity and tool threat protection {evp('pv-a365-matrix', 'pv-a365-v2')}. Moving to it is a migration: a new resource and a new runtime address {evp('pv-res-change', 'pv-domain')}. See <a href="#ctrl-ai-resource">AI Gateway product and resource</a>.</p>
      <p class="q-note">Microsoft says preview features are not meant for production use and may have restricted functionality. {evp('pv-notprod')} Every row below is a preview feature and its requirement is a recommendation. {PRE} {REC}</p>
      {table(["Control", "Design requirement", "What Microsoft documents"], [
        [control_label("a365", "Agent 365 gateway integration", "Visibility, not the boundary"),
         "Connect the API Management gateway so admins can see registered servers and block one. Treat blocking as additional gateway enforcement. It does not replace backend isolation. This is separate from the Agent 365 BYO server route below.",
         f"Agent 365 discovers servers in connected gateways {evp('pv-disc')}. The preview integration lists inventory and server block/unblock for API Management v2 and AI Gateway; tool blocking, activity observability and threat protection only for AI Gateway {evp('pv-a365-matrix', 'pv-a365-v2')}. Tool blocking needs a static allowed-tools list {evp('pv-a365-static')}. v1 tiers are not supported {evp('pv-a365-v1')}."],
        [control_label("a365-consent", "Agent 365 consent", "Tenant level"),
         "Before anyone grants it, name who approves the consent, who reviews the policy changes it allows, and how it is withdrawn.",
         f"An administrator grants the A365 MCP Gateway Policy Operator role at tenant level with a one-time consent {evp('pv-a365-role')}. It lets the service read and write API-scoped policies {evp('pv-a365-rw')}."],
        [control_label("ai-resource", "AI Gateway product and resource", "Objective A"),
         f"Do not confuse AI gateway capabilities in the API Management service with the separate AI Gateway product and resource type {ev('apim-ai-not-separate')} {evp('pv-aig-separate')}. Evaluate the current AI Gateway resource rather than following examples written for the earlier resource type.",
         f"The separate AI Gateway product uses resource type Microsoft.ApiManagement/aigateways {evp('pv-res-change')}. Migrate the earlier Microsoft.ApiManagement/service AIGateway SKU before 15 Jan 2027 {evp('pv-res-date')}. The new runtime URL uses ai.gateway.azure.com {evp('pv-domain')}; keys go in an Authorization header with a Bearer scheme {evp('pv-bearer')}."],
        [control_label("ai-limits", "AI Gateway limits", "Objective A"),
         "Check the network design first. Confirm that a public gateway frontend, fixed virtual network and subnet, supported region and alternative content safety control meet the pilot requirements.",
         f"Gateway frontend private endpoints are not supported {evp('pv-pe')}. The virtual network and subnet cannot be changed after creation {evp('pv-vnet')}. The content safety policy is not supported {evp('pv-cs')}. During public preview the regions are East US 2 and Sweden Central {evp('pv-regions')}."],
        [control_label("ai-publish", "Gateway publishing", "Objective A"),
         "Publish approved tools through the gateway. Give the gateway its own backend credential, scoped to what the tools need.",
         f"The gateway can combine tools from remote MCP servers, OpenAPI APIs and connectors behind gateway MCP endpoints {evp('pv-aig-comb')}. With a shared backend connection, callers use that connection's permissions {evp('pv-shared-cred')}."],
        [control_label("ttp-users", "Tool threat protection: who can use it", "Extra defence"),
         "Use it only in flows that carry a user token. Keep least privilege and human approval for destructive tools. Do not rely on it alone.",
         f"It requires a delegated Entra user token {evp('pv-ttp-token')}. App-only service-to-service calls are not supported {evp('pv-ttp-app')}. A Defender or Purview license is required {evp('pv-ttp-lic')}."],
        [control_label("ttp-modes", "Tool threat protection: modes and scope", "Extra defence"),
         "Configure the evaluation mode in Microsoft Defender. Test Audit, Block and failure handling. Enable pre-invocation checks to stop calls and post-invocation checks to withhold results. Plan for tools that already ran.",
         f"Audit mode fails open {evp('pv-ttp-audit')}. Block mode fails closed {evp('pv-ttp-block')}. One policy applies to every tool and caller of a server, not to one tool {evp('pv-ttp-scope')}. A denial after the call cannot undo it {evp('pv-ttp-post')}."],
        [control_label("byo", "Agent 365 BYO server route", "Separate route"),
         "Treat this as a separate registration route, not as the API Management gateway integration. Require developer registration and admin approval. Confirm its public endpoint fits the backend isolation target. Test each listed client surface before relying on it.",
         f"BYO servers route through the Agent 365 Tooling Gateway {evp('pv-byo-route')}. Preview clients: Copilot Studio, VS Code, Claude Code and GitHub Copilot CLI; not Foundry or declarative agents {evp('pv-byo-surf')}. An IT admin approves or rejects requests in the Microsoft 365 admin center {evp('pv-byo-approval')}. Servers need a publicly accessible endpoint {evp('pv-byo-endpoint')}. BYO tool-level blocking is planned {evp('pv-byo-tool-plan', 'pv-byo-roll')}."],
        [control_label("foundry-routing", "Foundry gateway routing", "Separate route"),
         "Create new tools in the Foundry portal without managed OAuth. Check the endpoint, sign-in and logs. Do not assume old tools are covered.",
         f"Only new MCP tools created in the Foundry portal without managed OAuth are routed through an AI gateway {evp('pv-fy-prev')}. Routing is applied only at tool creation, and existing tools are not mediated automatically {evp('pv-fy-new')}."],
        [control_label("outbound-filter", "Outbound filter, optional", "Objective B"),
         "Add it only if the preview label is acceptable. Do not rely on it for local servers.",
         f"The Global Secure Access MCP firewall filters by URL pattern {evp('fw-urls')}. It carries the preview label {evp('fw-preview')} and inspects remote servers only {evp('fw-remote')}."],
      ])}
    </div>
    {anchors("preview-env", "where-the-preview-controls-apply")}
    <div class="sub3" id="approval-workflow">
      <h3>Approval and denial workflow</h3>
      <p>Use two gates: the company's reviewed inventory change, then Microsoft's tenant approval for the preview Agent 365 server route. An approval in one gate does not replace the other. {REC}</p>
      <figure>
        <p class="fig-hint">Approval and denial path for a company MCP server.</p>
        <div class="fig-scroll" tabindex="0" role="region" aria-label="MCP server approval workflow, horizontally scrollable">
<pre class="ascii" role="img" aria-label="A developer proposes a server in the reviewed Git inventory. A security reviewer approves or rejects the pull request. Rejection stops the request and is recorded as denied. After approval and merge, the developer registers the server through the Agent 365 preview flow. An administrator reviews the request in Microsoft 365 admin center Requests preview and approves or rejects it. Rejection leaves the server unavailable and the reason is recorded. Approval makes the server Available in the tools registry. Agent-building surfaces can use it only after Microsoft Entra tenant consent. The admin records the approved server and consent in the inventory, applies target-specific access controls, and monitors calls. A later deny blocks the server in the tools registry and updates the inventory and other policy targets.">{ascii_fig("approval")}</pre>
        </div>
        <figcaption class="q-note">The Git pull request is the internal source-of-truth decision. The Microsoft 365 admin-center request is a separate product approval for the preview BYO route. Rejecting either stops rollout. Admin approval makes the registry status Available; agent-building surfaces can use the server only after Microsoft Entra consent. {ev('a365-tools-approve', 'a365-tools-consent')} {evp('pv-byo-approval')}</figcaption>
      </figure>
      <ul>
        <li><strong>Who approves.</strong> An AI Administrator or Global Administrator, under Agents &gt; Tools &gt; Requests (preview). {ev('a365-tools-role-ai', 'a365-tools-role-global')} {evp('pv-byo-approval')}</li>
        <li><strong>Tool level.</strong> Individual tool controls are rolling out for supported Agent 365 servers. BYO server tool-level blocking is planned. Until then, block at server level and authorize at the gateway and backend. {ev('a365-tools-granular')} {evp('pv-byo-roll', 'pv-a365-ctrl')}</li>
        <li><strong>Revoke.</strong> Block the server in the registry, mark it denied in Git, remove it from the target allowlists and verify that calls are denied. Microsoft 365 admin actions do not update the other policy targets. {REC}</li>
      </ul>
      <p class="q-note">This is the MCP server request queue {ev('a365-tools-overview')}. Approval of an agent publication is a separate workflow. The All agents registry is an inventory view; its Data &amp; tools details are read-only and may be missing for some agents. {ev('a365-agent-approve', 'a365-agent-request-review', 'a365-agent-readonly', 'a365-agent-incomplete')}</p>
    </div>
    <div class="sub3" id="guardrails-preview">
      <h3>Guardrails added with preview</h3>
      <p class="q-note">These add to the controls by call layer above. Layer 4 also gains tool threat protection, in the added controls.</p>
      {table(["Guardrail", "Product", "Layer", "What it does and its limit"], GR_PREV)}
    </div>
    <div class="sub3" id="preview-tests">
      {anchors("added-with-preview-preview-2")}
      <h3>Tests added with preview</h3>
      <p class="q-note">No test has been run.</p>
      {table(["Test", "Expected result", "What establishes the guarantee"], [
        ["Approved client calls the approved gateway MCP endpoint", "Allowed", "Gateway sign-in and the published tool policy"],
        ["Admin blocks a whole MCP server in the API Management integration", "Denied at the gateway", "A verified integration and a runtime block"],
        ["Admin blocks a single tool in the API Management integration", "Denied, only on a supported gateway with a static tool list", "An explicit tool-level policy test"],
        ["Pre-invocation evaluation denies a tool argument", "Tool not run", "Block mode before the call"],
        ["Post-invocation evaluation denies a tool result", "Result withheld; the tool may already have run", "Block mode after the call"],
        ["Microsoft admin rejects a registered MCP server request", "Server remains unavailable", "Requests preview decision"],
        ["Microsoft admin approves without granting Entra consent", "Server remains unavailable to agent-building surfaces", "Approval plus required tenant consent"],
        ["Admin blocks an Available MCP server", "Tool calls are denied at runtime", "Registry block and the connected Agent 365 enforcement path"],
        ["Review the Agent registry, Tools registry and Requests queue", "Agent inventory, Available or Blocked server states, and pending preview requests are visible in their respective views", "Microsoft 365 admin center"],
        ["An app-only caller reaches a tool with the delegated-token protection", "Unsupported, or the protected call fails", "An explicit sign-in compatibility test"],
        ["The gateway is down, or a preview feature is withdrawn", "Safe stop, or a rollback to the released-only design", "Backend and client controls of the released-only design"],
      ])}
    </div>
    <div class="sub3" id="pilot">
      {anchors("preview-pilot-after-the-baseline-preview")}
      <h3>Preview pilot, after the baseline</h3>
      <ol class="steps">
        <li><strong>Scope.</strong> Pick a low-risk server with two read-only tools and one controlled write tool. Record owner, data class, sign-in and expected clients.</li>
        <li><strong>Resource type.</strong> Create the separate AI Gateway product on the current resource type in a supported public preview region {evp('pv-aig-separate', 'pv-res-change', 'pv-regions')}. Confirm eligibility, the public front door, networking, policy features and licensing.</li>
        <li><strong>Lock the backend.</strong> Make direct calls fail. Check the supported backend network design, because the new gateway has no private endpoints {evp('pv-pe')}.</li>
        <li><strong>Connect Agent 365.</strong> For the API Management integration, after named tenant-admin consent, connect the gateway and check that the server shows up. Review the permissions granted {evp('pv-a365-rw')}.</li>
        <li><strong>Test blocking.</strong> For the preview Agent 365 integration, test server block/unblock on a supported API Management v2 tier. Test tool blocking and threat protection only on the separate AI Gateway product, with a static tool list and a delegated user-token flow {evp('pv-a365-matrix', 'pv-a365-static', 'pv-ttp-token')}. Test Audit, Block and failure handling. App-only workloads are not supported {evp('pv-ttp-app')}.</li>
        <li><strong>Gate promotion.</strong> Require accepted support terms, released features, incident playbooks and a rollback plan before leaving the sandbox {evp('pv-notprod')}.</li>
      </ol>
    </div>
    {anchors("fallback", "h-fallback", "preview-open", "open-questions-for-the-preview", "who-approves-and-reviews-the-agent-365-consent", "what-ends-the-pilot", "does-a-gateway-with-no-private-endpoints-fit", "which-agent-365-route-will-the-pilot-use")}
  </section>
"""

FOOTER = f"""
  <footer>
    <p>The design is proposed. The preview additions are for a sandbox pilot.</p>
    {AI_NOTE}
    <p id="evidence">{anchors("evidence-details", "h-e")}Sources and review notes: <a href="{FACTCHECK_URL}">fact check</a>.</p>
  </footer>
"""

BODY = f"""{HEAD}{STYLE}
{EXTRA_CSS}
</head>
<body data-view="safe">{MARKERS}<div class="page" id="top">
{MAST}
  <main id="main-content" tabindex="-1">
{FIGURE}{CONTROLS}{ROLLOUT}{GAPS}{PREVIEW}
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
print(f"wrote {OUT.name}, {len(BODY.splitlines())} lines; {len(QUOTES)} quotes, {SAFE_COUNT} on the released-only design")


# ---- quote table in the fact check file ----------------------------------
def md_cell(text):
    text = html.escape(text, quote=False)
    for a, b in (("|", "&#124;"), ("*", "&#42;"), ("_", "&#95;"), ("`", "&#96;"), ("[", "&#91;"), ("]", "&#93;")):
        text = text.replace(a, b)
    return text


def md_url(url):
    return url.replace("(", "%28").replace(")", "%29").replace("|", "%7C").replace(" ", "%20")


QUOTE_ROWS = []
for key, skey, q in QUOTES:
    title, url, date = SOURCES[skey]
    where = "preview" if key in PREVIEW_ONLY else "released"
    QUOTE_ROWS.append(
        f'| <a id="ev-{IDS[key]}"></a>{IDS[key]} | {md_cell(q)} | [{md_cell(title)}]({md_url(url + frag(q))}) | {date or "none shown"} | {where} |')
QUOTE_TABLE = (
    f"{QUOTES_BEGIN}\n"
    f"Generated by `scripts/build-mcp-governance.py`. Do not edit by hand. {len(QUOTES)} quotes, checked {CHECKED}: "
    f"{SAFE_COUNT} back the released-only design and {PV_COUNT} back the preview additions. "
    "Links request the quoted passage with browser text fragments. Page date is the date the source page shows.\n\n"
    "| Id | Quote | Source | Page date | Design |\n|---|---|---|---|---|\n"
    + "\n".join(QUOTE_ROWS) + f"\n{QUOTES_END}")
notes = NOTES.read_text(encoding="utf-8")
if QUOTES_BEGIN not in notes or QUOTES_END not in notes:
    sys.exit(f"{NOTES.name} has no {QUOTES_BEGIN} and {QUOTES_END} markers")
head, rest = notes.split(QUOTES_BEGIN, 1)
tail = rest.split(QUOTES_END, 1)[1]
if head + QUOTE_TABLE + tail != notes:
    NOTES.write_text(head + QUOTE_TABLE + tail, encoding="utf-8")
    print(f"updated the quote table in {NOTES.name}")

for m in re.finditer(r"<(p|dd|td|li)\b[^>]*>(.*?)</\1>", BODY, re.S):
    words = len(re.sub(r"<[^>]+>", " ", m.group(2)).split())
    if words > 60:
        print(f"WARN {words} words: {re.sub(r'<[^>]+>', ' ', m.group(2))[:70]!r}")
defined = set(re.findall(r'\bid="([^"]+)"', BODY))
for t in sorted(set(re.findall(r'href="#([^"]+)"', BODY)) - defined):
    print(f"WARN dead anchor #{t}")
