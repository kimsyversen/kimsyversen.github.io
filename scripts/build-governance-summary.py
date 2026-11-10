"""Build enterprise-ai-agent-governance-summary.html from the long page plus new text.

Usage: python3 -I scripts/build-governance-summary.py

Reused blocks (style, both figures, tiers, action policy, checklist, runbook,
nine rules, script) are cut from the long page by marker. The build stops
if a marker is missing or not unique. Everything else is written here.
"""

import html
import re
import sys
from pathlib import Path
from urllib.parse import quote as urlquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from section_anchors import add_anchors  # noqa: E402
from governance_evidence import CHECKED, IDS, QUOTES, SOURCES  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
LONG = "enterprise-ai-agent-security-recommendation.html"
OUT = ROOT / "wip" / "enterprise-ai-agent-governance-summary.html"
SRC = (ROOT / "wip" / LONG).read_text(encoding="utf-8")


def cut(start, end, last=False):
    if not last and SRC.count(start) != 1:
        sys.exit(f"marker not unique or missing ({SRC.count(start)}): {start[:60]!r}")
    i = SRC.rindex(start) if last else SRC.index(start)
    j = SRC.find(end, i + len(start))
    if j < 0:
        sys.exit(f"end marker missing: {end[:60]!r}")
    return SRC[i:j + len(end)]


# ---- reused blocks -------------------------------------------------------
HEAD = SRC[:SRC.index("<style>")]
STYLE = cut("<style>", "</style>")
i = SRC.index('role="region" aria-label="MCP server approval diagram')
FIG24 = SRC[SRC.rindex("<figure>", 0, i):SRC.index("</figure>", i) + len("</figure>")]
PATH24 = cut('<ol class="path">\n      <li><h4>Request and review</h4>', "</ol>")
TIERS = cut('<h3 style="font-size:1.05rem;margin-top:8px" id="risk-tiers-recommendation">', "<li>Review date</li>\n    </ul>")
FIVE = cut('<figure id="five-points">', "</figure>")
ANS = cut('<ol class="ans">', "</ol>").replace('<ol class="ans">', '<ol class="ans tight">')
RUNBOOK = cut('<ol class="path">\n      <li><h4>Find the affected calls</h4>', "Test revocation in the pilot</a></p>")
RULES = cut('<table class="tbl">\n<thead>\n<tr>\n<th>Principle</th>', "</table>")
SCRIPT = cut("<script>", "</script>", last=True)
AI_NOTE = cut('<p class="ai-note">', "</p>")

# One unsourced sentence in the long page's table is not carried over.
RULES = RULES.replace(" Microsoft recommends this for agent policies.", "")

# Pilot wording is not carried over.
def drop(block, old, new):
    if old not in block:
        sys.exit(f"text missing: {old[:60]!r}")
    return block.replace(old, new)



FIG24 = drop(FIG24, '<a href="#pilot">Run the pilot checks</a>', "Run the checks")
FIG24 = drop(FIG24, 'Follow the <a href="#pilot">pilot checks</a> and <a href="#operate">revocation procedure</a>.', 'Follow the <a href="#operate">revocation procedure</a>.')
FIVE = drop(FIVE, "Check product scope and pilot coverage", "Check product scope and coverage")
RUNBOOK = drop(RUNBOOK, ' · <a href="#pilot-revoke">Test revocation in the pilot</a>', "")

EXTRA_CSS = """
.rt{display:block;font-weight:400;color:var(--muted);font-size:0.8rem;margin-top:2px}
.matrix-row .ev{margin-right:4px}
.q-note{font-size:0.9rem;color:var(--muted);max-width:46rem;margin-top:10px}
.sh{display:block}
section[id]{scroll-margin-top:52px}
.sh h2{grid-column:auto}
.ans.tight li{grid-template-columns:1.6rem minmax(0,5fr) minmax(0,6fr);gap:2px 16px;padding:10px 0}
.ans.tight .n{font-size:1.15rem;line-height:1.3}
.ans.tight h3{font-size:1rem;line-height:1.3}
.ans.tight p{grid-column:3;grid-row:1;font-size:0.9rem;margin-top:0}
@media (max-width:640px){.ans.tight li{grid-template-columns:1.6rem minmax(0,1fr);gap:2px 10px}.ans.tight p{grid-column:2;grid-row:auto}}
"""
STYLE = STYLE.replace("</style>", EXTRA_CSS + "</style>")


# ---- helpers -------------------------------------------------------------
def ev(*keys):
    ids = sorted((IDS[k] for k in keys), key=lambda v: int(v[1:]))
    return " ".join(f'<a class="ev" href="#ev-{v}">{v}</a>' for v in ids)


def tg(cls, text):
    return f'<span class="tg {cls}">{text}</span>'


# Link the two rules that rest on a product fact to their quotes.
RULES = drop(RULES, "<td>Run new Conditional Access rules in report-only mode, then enforce.</td>",
             f"<td>Run new Conditional Access rules in report-only mode, then enforce. {ev('ca-report')}</td>")
RULES = drop(RULES, "<td>One rule set for many Power Platform environments.</td>",
             f"<td>One rule set for many Power Platform environments. {ev('envgrp-rules')}</td>")


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


def route(rid, name, tool, can, cannot, admin, keys, preview=False):
    pv = " " + PRE if preview else ""
    idattr = f' id="{rid}"' if rid else ""
    return f"""
          <div class="matrix-row"{idattr} role="row">
            <h4 role="rowheader">{name}{pv} <span class="rt">{tool}</span></h4>
            <div role="cell"><b class="matrix-label" aria-hidden="true">We can</b><p>{can}</p></div>
            <div role="cell"><b class="matrix-label" aria-hidden="true">We cannot</b><p>{cannot}</p></div>
            <div role="cell"><b class="matrix-label" aria-hidden="true">Admin work</b><p>{admin}</p></div>
            <div role="cell"><b class="matrix-label" aria-hidden="true">Evidence</b><p>{ev(*keys) if keys else "Design requirement"}</p></div>
          </div>"""


# ---- new text ------------------------------------------------------------
MAST = f"""
  <a class="skip" href="#main-content">Skip to content</a>
  <header class="mast">
    <div class="meta"><span>Governance summary · Microsoft stack</span><span>Documentation checked 6 Nov 2026</span></div>
    <h1>Governing MCP servers and AI agents</h1>
    <div class="intro">
      <p class="lead">How we govern MCP servers and what to do with them. The page shows what we can do, what we cannot do and which tool does the job, then the target state. Open questions are at the end.</p>
      <dl class="spec">
        <dt class="lbl">Scope</dt><dd>MCP servers, agents and consultant access</dd>
        <dt class="lbl">Evidence</dt><dd><a href="#evidence">{len(QUOTES)} exact quotes</a> and the <a href="{LONG}">long page</a></dd>
        <dt class="lbl">Kinds of claim</dt><dd>A product fact has a quote. The risk tiers, action policy, checklist, runbook and target state are our design choices, labelled recommendation. No source can confirm them. A gap is labelled unverified.</dd>
        <dt class="lbl">Tenant tests</dt><dd class="w">None run.</dd>
      </dl>
    </div>
    <nav aria-label="Start by role">
      <ul class="routes">
        <li><a href="#q1">Platform and security owners</a><p>See how the approved list is governed and what each route can do.</p></li>
        <li><a href="#q2">Architects</a><p>See the target state and which tool does which job.</p></li>
        <li><a href="#discuss">Decision makers</a><p>Go to the open questions.</p></li>
      </ul>
    </nav>
  </header>

  <nav class="toc" aria-label="Contents">
    <ul>
      <li><a href="#q1">MCP governance</a></li>
      <li><a href="#can">Can and cannot</a></li>
      <li><a href="#q2">Target state</a></li>
      <li><a href="#auto">Automation</a></li>
      <li><a href="#gaps">Gaps</a></li>
      <li><a href="#discuss">Open questions</a></li>
      <li><a href="#evidence">Evidence</a></li>
      <li class="btn-li" style="margin-left:auto"><button class="btn" type="button" id="toggle" aria-pressed="false">Expand all detail</button></li>
    </ul>
  </nav>
"""

DISCUSS = f"""
  <section id="discuss" aria-labelledby="h-d">
    <div class="part">
      <p class="lbl"><b>Open questions</b> · For the owners</p>
      <h2 id="h-d">Open questions</h2>
    </div>
    <div class="blk" style="margin-top:20px">
      <ol class="ans tight">
        <li><span class="n">1</span><h3>Is Git the one source of the approved MCP list?</h3><p>Every route then takes its entries from one reviewed file. Without it, each platform keeps its own list and the lists drift. See <a href="#q1">how the list is governed</a>.</p></li>
        <li><span class="n">2</span><h3>Which routes do we enable?</h3><p>Enable only the routes that fit our needs. Keep the rest disabled. The <a href="#can">route table</a> shows what each route can and cannot do.</p></li>
        <li><span class="n">3</span><h3>Who owns the list, and who approves tiers 2 and 3?</h3><p>Name an owner for the list and for each server. Security and the data owner approve tiers 2 and 3. See the <a href="#tiers">risk tiers</a>.</p></li>
        <li><span class="n">4</span><h3>Do we accept preview controls?</h3><p>The watchlist names every control that its vendor labels preview. Decide whether we use them, and who re-checks them each month. See the <a href="#watchlist">preview watchlist</a>.</p></li>
      </ol>
    </div>
  </section>
"""

def _row(n, path, where, text, keys):
    return (f'<tr id="tp{n}"><td>{n}</td><td>{path}</td><td>{where}</td><td>{text}</td>'
            f'<td>{ev(*keys)}</td></tr>')


TRAFFIC_ROWS = "\n".join([
    _row(1, "GitHub settings file to VS Code", "Reaches the client",
         "Policy, not traffic. Create or update the file in the <code>.github-private</code> repository. Updated settings are applied within about an hour. Coverage varies between environments. The built-in GitHub MCP server cannot be blocked.",
         ["gh-file", "gh-server", "gh-hour", "gh-vary", "gh-builtin"]),
    _row(2, "VS Code to the Global Secure Access client", "End user client",
         f"The firewall prerequisites include the Global Secure Access client on a device that is Entra joined or hybrid joined, and TLS inspection, without which it cannot enforce MCP policy. It also needs an Entra Internet Access license, which E7 includes.",
         ["fw-client", "fw-tls", "fw-license", "e7-entra"]),
    _row(3, "Client to MCP firewall to remote server", "Not the client",
         f"Allow or deny remote servers by URL pattern. The firewall is in preview. JSON-RPC batches are not inspected. Logging covers remote servers only.",
         ["fw-urls", "fw-preview", "fw-remote", "log-remote"]),
    _row(4, "VS Code to a local MCP server", "End user client",
         f"Local servers that run on a device are not visible to Global Secure Access, so the firewall cannot stop them. Defender for Endpoint can discover supported agents and their configured MCP servers on onboarded devices, and its matrix lists the VS Code GitHub Copilot extension. It is generally available on supported Windows and macOS devices, except preview scenarios. That is detection and inventory, and no source shows it blocking a server. {UNV} The GitHub settings file from path 1 can limit them, where coverage varies.&nbsp;{REC}",
         ["fw-remote", "def-disc", "def-vscode", "def-ga", "def-cmd", "def-noproof", "gh-file", "gh-vary"]),
    _row(5, "Agents in the cloud to the gateway to a remote server", "Not the client",
         f"The gateway can block or allow a whole server. A server blocked in the Agent 365 bring-your-own registry cannot be called at runtime from any supported client surface. Foundry and Microsoft 365 declarative agents are not supported there. Both are preview.&nbsp;{PRE}",
         ["gw-block", "gw-preview", "byo-runtime", "byo-clients", "byo-preview"]),
    _row(6, "Agents in the cloud straight to a remote server", "Not the client",
         f"Agent 365 does not send agents through a customer-hosted gateway by itself. To prevent direct access, make the gateway the only permitted caller or use private networking. For Copilot Studio agents, the Global Secure Access integration forwards agent traffic, including custom MCP servers, and logs MCP traffic without TLS inspection. Web content filtering, threat intelligence filtering and network file filtering apply to it. No source shows the MCP firewall applying to this traffic. The firewall is enforced through a Conditional Access policy, and Copilot Studio agents are documented only with the baseline profile, not with profiles linked to Conditional Access. So the firewall most likely does not apply.&nbsp;{INF}",
         ["apim-route", "apim-restrict", "log-cs", "cs-fwd", "cs-ctl", "fw-ca", "cs-noca", "cs-base"]),
    _row(7, "Policy on agents in the cloud", "Not the client",
         "Policy, not traffic. In Copilot Studio, blocking Power Platform connectors also blocks the tools in connected MCP servers. In Foundry, an Azure Policy deny stops a non-matching request and marks existing resources non-compliant. The approved-tools policy is in preview.",
         ["studio", "deny-prevent", "deny-existing", "pol-approved"]),
])

TRAFFIC = f"""
    <h3 id="traffic" style="font-size:1.05rem;margin-top:28px">Where MCP traffic flows, and what is the end user's client&nbsp;{REC}</h3>
    <figure>
      <p class="fig-hint">Scroll the diagram sideways to follow all paths.</p>
      <div class="fig-scroll" tabindex="0" role="region" aria-label="MCP traffic diagram, horizontally scrollable">
<svg class="fg" viewBox="0 0 1000 400" role="group" aria-labelledby="ttr dtr">
<title id="ttr">MCP traffic paths and the end user client</title>
<desc id="dtr">Proposed view of where MCP traffic flows. The left zone is the end user's device and holds VS Code with GitHub Copilot, a local MCP server and the Global Secure Access client. The right zone is not the user's client and holds the GitHub settings file, the MCP firewall, agents in the cloud, the Agent 365 gateway and remote MCP servers. Seven numbered paths are explained in the table below.</desc>

<text class="zl" x="20" y="16">END USER DEVICE (THE CLIENT)</text>
<rect class="zone" x="10" y="26" width="390" height="330"/>
<text class="zl" x="430" y="16">NOT THE USER'S CLIENT: CLOUD AND NETWORK</text>
<rect class="zone" x="420" y="26" width="570" height="330"/>

<rect class="box" x="30" y="50" width="350" height="60"/>
<text class="t" x="205" y="76">VS Code and GitHub Copilot</text>
<text class="s" x="205" y="96">end user client</text>

<rect class="box" x="30" y="270" width="165" height="62"/>
<text class="t" x="112" y="296">Local MCP server</text>
<text class="s" x="112" y="314">stdio, on the device</text>

<rect class="box" x="215" y="270" width="165" height="62"/>
<text class="t" x="297" y="296">Global Secure Access</text>
<text class="s" x="297" y="314">client on the device</text>

<rect class="box" x="440" y="50" width="230" height="60"/>
<text class="t" x="555" y="76">GitHub settings file</text>
<text class="s" x="555" y="96">managed-settings.json</text>

<rect class="box pv" x="440" y="270" width="230" height="62"/>
<text class="t" x="555" y="296">MCP firewall</text>
<text class="s" x="555" y="314">Global Secure Access</text>

<rect class="box" x="730" y="50" width="200" height="72"/>
<text class="t" x="830" y="74">Agents in the cloud</text>
<text class="s" x="830" y="93">Copilot Studio, Foundry</text>
<text class="s" x="830" y="110">Data policy, Azure Policy</text>

<rect class="box pv" x="730" y="160" width="200" height="62"/>
<text class="t" x="830" y="186">Agent 365 gateway</text>
<text class="s" x="830" y="204">or registry</text>

<rect class="box" x="730" y="270" width="200" height="62"/>
<text class="t" x="830" y="296">Remote MCP servers</text>
<text class="s" x="830" y="314">approved or not</text>

<path class="ln" d="M440 80H382" marker-end="url(#arr)"/>
<path class="ln" d="M297 110V268" marker-end="url(#arr)"/>
<path class="ln stop" d="M112 110V268" marker-end="url(#arrr)"/>
<path class="ln" d="M380 301H438" marker-end="url(#arr)"/>
<path class="ln" d="M670 301H728" marker-end="url(#arr)"/>
<path class="ln" d="M830 122V158" marker-end="url(#arr)"/>
<path class="ln" d="M830 222V268" marker-end="url(#arr)"/>
<path class="ln stop" d="M930 86H960V301H932" marker-end="url(#arrr)"/>

<circle class="pt" cx="410" cy="64" r="9"/><text class="pn" x="410" y="68">1</text>
<circle class="pt" cx="297" cy="190" r="9"/><text class="pn" x="297" y="194">2</text>
<circle class="pt" cx="409" cy="285" r="9"/><text class="pn" x="409" y="289">3</text>
<circle class="pt" cx="699" cy="285" r="9"/><text class="pn" x="699" y="289">3</text>
<circle class="pt" cx="112" cy="190" r="9"/><text class="pn" x="112" y="194">4</text>
<circle class="pt" cx="850" cy="140" r="9"/><text class="pn" x="850" y="144">5</text>
<circle class="pt" cx="850" cy="245" r="9"/><text class="pn" x="850" y="249">5</text>
<circle class="pt" cx="960" cy="190" r="9"/><text class="pn" x="960" y="194">6</text>
<circle class="pt" cx="730" cy="50" r="9"/><text class="pn" x="730" y="54">7</text>

<path class="ln" d="M20 382H50" marker-end="url(#arr)"/>
<text class="al" x="58" y="386">Solid line: policy or traffic</text>
<path class="ln stop" d="M250 382H280" marker-end="url(#arrr)"/>
<text class="al stop" x="288" y="386">Red dashed line: path with a gap</text>
<rect class="box pv" x="520" y="372" width="26" height="16"/>
<text class="al" x="554" y="386">Red dashed box: preview</text>
</svg>
      </div>
      <figcaption>Proposed view. Numbers match the paths in the table below. The placement of the cloud services is interpretation by AI.</figcaption>
    </figure>
    <div class="tbl-wrap"><table class="tbl">
<thead><tr><th>No</th><th>Path</th><th>Where</th><th>What the sources say</th><th>Evidence</th></tr></thead>
<tbody>
{TRAFFIC_ROWS}
</tbody></table></div>
    <p class="q-note">VS Code, the local server and the Global Secure Access client are on the device. {ev("fw-remote", "log-client")} Placing the other boxes in the cloud is interpretation by AI, because no quote says where they run.&nbsp;{INF}</p>
"""

Q1 = f"""
  <section class="sec" id="q1" aria-labelledby="h-q1">
    <header class="sh"><h2 id="h-q1">How we govern MCP servers</h2>
    <p class="goal"><b>Goal</b>Keep one approved list in Git and distribute it automatically. Verify each route before allowing use.&nbsp;{REC}</p></header>
    <div class="decision">
      <h3>Answer&nbsp;{REC}</h3>
      <p>Keep one approved MCP list in Git, and publish it by pull request into each technology's own control: the GitHub settings file for VS Code and Copilot, the Agent 365 registry or gateway for agents, data policies for Copilot Studio, Azure Policy for Foundry, and the network firewall for remote servers.</p>
      <p>No single control covers every agent, so combine these, restrict direct API access with permissions at the source, and accept that most of these are previews that are untested in our tenant (see the <a href="#can">route table</a>).</p>
    </div>
    {FIG24}
    {TRAFFIC}
    {PATH24}
    <div id="tiers">
    {TIERS}
    </div>
  </section>
"""

ROWS = "".join([
    route("pub-vscode", "VS Code and GitHub Copilot", "GitHub <code>managed-settings.json</code>",
          "Allow or deny MCP servers set in user and repository settings. Create or update the file in the <code>.github-private</code> repository. Updated settings apply automatically within about an hour.",
          "Cover servers in repository custom agent profiles. Block the built-in GitHub server. Coverage varies by environment.",
          f"Settings apply automatically once the file is updated. Using a pull request to approve each change is our own process. {REC}",
          ["gh-file", "gh-server", "gh-hour", "gh-profiles", "gh-builtin", "gh-vary"]),
    route("pub-a365", "Agent 365 Tools Gateway", "Agent 365 with Azure API Management",
          "Find MCP servers registered with the gateway. Discovery might take a few minutes. Block or allow a whole server, and single tools on supported servers. Block a tool in the admin center when the server is on the AI Gateway tier. Create MCP servers in API Management with REST API, ARM, Bicep, CLI or Terraform.",
          f"Connect the gateway without the Global Administrator role. Block a tool on API Management v1 tiers. Set allow or block from a pipeline: the page documents the admin center only. {UNV} Know whether a new server starts allowed or blocked. {UNV}",
          f"Creating servers in API Management can be automatic from our pipeline. {REC} A person connects the gateway and sets allow or block in the admin center.",
          ["gw-preview", "gw-discover", "gw-block", "gw-tools", "apim-block", "apim-tier", "apim-v1", "gw-ga", "apim-rest"], preview=True),
    route("route-a365-byo", "Agent 365 bring-your-own registry", "Agent 365 BYO MCP",
          "Block a whole server. A blocked server cannot be called from any client surface. Supported surfaces: Copilot Studio, Visual Studio Code, Claude Code and GitHub Copilot CLI.",
          "Cover Foundry or Microsoft 365 declarative agents. Block single tools: planned for a future release. Republish a new version during preview. Register a server without a public endpoint.",
          f"A developer registers the server with the <code>a365</code> command line. A person reviews each request, approves it and grants Entra permissions. Approval from a pipeline: no source shows it. {UNV}",
          ["byo-preview", "byo-clients", "byo-runtime", "byo-tool", "byo-republish", "byo-public", "byo-cli", "byo-approve"], preview=True),
    route("route-studio", "Copilot Studio", "Power Platform data policies",
          "Block Power Platform connectors. That also blocks the tools in connected MCP servers. Create a data policy with the <code>New-DlpPolicy</code> PowerShell command.",
          f"Turn the Git list into connector entries without our own script. Mapping the list to connectors is our own build. {REC}",
          f"A person sets the data policy today. Our pipeline could call the command. Not tested. {REC}",
          ["studio", "dlp-cmd"]),
    route("route-builder", "Agent Builder", "Microsoft 365 Copilot, users build their own agents",
          "Show Agent Builder agents in the Agent 365 inventory. Switch Agent Builder on or off for the organization.",
          f"Add actions that integrate external services in Agent Builder: copy the agent to Copilot Studio for that. See draft Agent Builder agents in the inventory. Use MCP servers: the page does not mention them. {UNV}",
          f"A person switches Agent Builder on or off. After a copy to Copilot Studio, the Copilot Studio row applies, which is interpretation by AI of the quote. {INF}",
          ["ab-inv", "ab-draft", "ab-ext", "ab-copy", "ab-admin"]),
    route("route-toolkit", "Agents Toolkit", "Microsoft 365 Agents Toolkit, developers build declarative agents with MCP plugins",
          "Build a declarative agent that uses an MCP server as a plugin. Block the plugin package or manage who can use it in the Microsoft 365 admin center. Review plugin access requests and standalone MCP server registration requests there.",
          f"Count plugin availability as access control for the server: it grants no access to external services or data. Apply the Git list to these plugins: no source shows it. {UNV} Say whether the Agent 365 gateway or the network firewall sees this traffic: not shown. {UNV}",
          "A person approves or blocks each plugin and each registration request. A developer needs custom app upload enabled to test. The server's own hosting and runtime controls are separate.",
          ["tk-build", "tk-block", "tk-req", "tk-noaccess", "tk-sideload", "tk-sep"]),
    route("pub-foundry", "Foundry agent tools", "Azure Policy approved tools",
          "Limit agents to approved tool types, MCP endpoints and connectors. Deny rejects a request that breaks the rule. Create the policy with the Azure CLI.",
          f"Change existing resources: they are only marked non-compliant. Block calls at run time: not shown. {INF}",
          f"Our pipeline writes the Git list into the policy assignment. This is our own build and is not tested. {REC}",
          ["pol-approved", "deny-prevent", "deny-existing", "pol-cli"], preview=True),
    route("route-local", "Local MCP via stdio", "GitHub <code>serverCommand</code> list",
          "Allow a local server by its exact command and each argument, on clients that support the setting.",
          f"Use wildcards. Be seen or logged by Global Secure Access: it covers remote servers only. List the servers already on devices: Defender for Endpoint discovers supported ones, and no source shows it blocking them. {UNV}",
          "Automatic with the GitHub file. A person lists each exact command.",
          ["gh-exact", "gh-wild", "fw-remote", "log-remote", "def-disc", "def-incomplete"]),
    route("route-gsa", "Network MCP firewall", "Global Secure Access, Entra Internet Access",
          "Allow or deny remote MCP servers by URL pattern. Allow or block tools, resources or prompt templates per server. Log traffic to remote MCP servers.",
          "See local servers (Defender for Endpoint can detect some) or JSON-RPC batches. Work without the client on a joined device and without TLS inspection. Work without the Entra Internet Access license. E7 includes that license.",
          f"No source shows the Git list feeding the URL lists. {UNV} A person sets them.",
          ["fw-preview", "fw-urls", "fw-prim", "fw-remote", "def-disc", "fw-license", "fw-client", "fw-tls", "log-client", "e7-entra"], preview=True),
    route("route-intune", "Intune firewall allow list", "Intune, Windows Firewall",
          f"Block every outbound connection that matches no rule, then allow approved servers by domain name with dynamic keywords. Intune can deliver the dynamic keywords through the Firewall CSP. Applies to managed Windows devices. {REC}",
          f"Block only MCP traffic: the default blocks all outbound traffic that matches no rule. Microsoft calls that default fit for certain highly secure environments. Rely on domain rules behind a proxy, secure DNS, some VPN setups or cached addresses. Cover macOS or unmanaged devices: the setting names Windows 1809 and later. {INF}",
          f"Our pipeline would write the approved Git list into an Intune policy. The Graph API creates configuration policies. Whether it can write firewall dynamic keywords: not shown. Not tested. {REC} A person tests the block-all default on a pilot first.",
          ["ifw-block", "ifw-ver", "dk-csp", "dk-example", "dk-dns", "dk-limits", "dk-secure", "graph-cp"]),
    route("route-direct", "Direct API or data access", "Permissions at the API or data source",
          f"Enforce access at the API or data source. {REC}",
          "Rely on the gateway alone to block direct access. Agents are not routed through it automatically, and connectivity must be restricted so the gateway is the only permitted caller.",
          "The data owner sets permissions for each resource. A person restricts server connectivity.",
          ["apim-route", "apim-restrict"]),
    route("pub-apic", "Azure API Center catalog", "API Center",
          "Keep an inventory of remote and local MCP servers. Help people find them. Sync continuously from API Management. Integrate registered servers with the Foundry tool catalogs.",
          f"Block calls. The sources describe inventory and discovery only. {INF} Show that the Foundry catalog stops agents from using other tools: not shown. {UNV}",
          f"A person links API Center to API Management first. Synchronization is then continuous. {INF}",
          ["apic-inv", "apic-sync", "apic-foundry"]),
])

CAN = f"""
  <section class="sec" id="can" aria-labelledby="h-can">
    <header class="sh"><h2 id="h-can">What we can and cannot do, route by route</h2>
    <p class="goal"><b>Read this first</b>Each row cites exact quotes below. A label marks anything a quote does not show.</p></header>
    <div class="blk" style="margin-top:14px">
      <div class="matrix" role="table" aria-labelledby="h-can">
        <div class="matrix-row matrix-head" role="row">
          <span role="columnheader">Route and tool</span>
          <span role="columnheader">We can</span>
          <span role="columnheader">We cannot</span>
          <span role="columnheader">Admin work</span>
          <span role="columnheader">Evidence</span>
        </div>{ROWS}
      </div>
      <p class="q-note">The network firewall, Agent Builder and Agents Toolkit rows are proposed additions. The approval diagram above does not show them. The Admin work column describes our design unless it cites a quote.</p>
    </div>
  </section>
"""

Q2 = f"""
  <section class="sec" id="q2" aria-labelledby="h-q2">
    <header class="sh"><h2 id="h-q2">The target state, as part of the governance</h2>
    <p class="goal"><b>Goal</b>Show how the pieces fit. One policy in Git, enforced by each platform, with work access from a managed desktop.&nbsp;{REC}</p></header>
    <div class="decision">
      <h3>Answer&nbsp;{REC}</h3>
      <p>The target state is the same approved list, enforced in layers. Git holds the policy. Each platform enforces it with its own control. Consultants work from a managed desktop. Agents get their own identity, start read-only and need approval for high-impact actions. Logs and revocation close the loop.</p>
    </div>
    {ANS}
    {FIVE}
    <p class="muted">All five points describe the proposed design.</p>

    <div class="blk" id="tools">
      <h3>Which tool does which job</h3>
      <div class="body"><div class="tbl-wrap"><table class="tbl">
<thead><tr><th>Job</th><th>Main tool</th><th>Where to look</th></tr></thead>
<tbody>
<tr><td>Who can sign in, from what device</td><td>Entra Conditional Access, Intune</td><td>E7 includes the Entra Suite {ev("e7")} and Conditional Access through it. {ev("e7-ca")} Intune comes in bundles such as E3, E5 and E7. {ev("intune-bundle")}</td></tr>
<tr><td>Consultant access</td><td>Entra B2B guests, access packages with expiry and reviews</td><td>Evidence on the <a href="{LONG}#s22">long page, 2.2</a>.</td></tr>
<tr><td>Safe workplace for unmanaged consultants</td><td>Dev Box, Windows 365 or Azure Virtual Desktop</td><td>Design requirement. Not tested.&nbsp;{REC}</td></tr>
<tr><td>Allowed MCP servers in VS Code and GitHub Copilot</td><td>GitHub <code>managed-settings.json</code></td><td><a href="#pub-vscode">Route table</a>. {ev("gh-file", "gh-hour")}</td></tr>
<tr><td>Approve and block remote MCP servers</td><td>Agent 365 Tools Gateway and BYO registry</td><td><a href="#pub-a365">Gateway</a> and <a href="#route-a365-byo">BYO</a> rows. Both preview. {ev("gw-preview", "byo-preview")}</td></tr>
<tr><td>Block connectors in Copilot Studio</td><td>Power Platform data policies</td><td><a href="#route-studio">Studio row</a>. {ev("studio")}</td></tr>
<tr><td>Agents that developers build with MCP plugins</td><td>Agents Toolkit, then the admin center</td><td><a href="#route-toolkit">Agents Toolkit row</a>. {ev("tk-build", "tk-block", "tk-req", "tk-noaccess")}</td></tr>
<tr><td>Agents that users build themselves</td><td>Agent Builder, then Copilot Studio</td><td><a href="#route-builder">Agent Builder row</a>. {ev("ab-inv", "ab-ext", "ab-copy", "ab-admin")}</td></tr>
<tr><td>Restrict tools in Foundry</td><td>Azure Policy approved tools</td><td><a href="#pub-foundry">Foundry row</a>. Preview. {ev("pol-approved")}</td></tr>
<tr><td>Catalog of MCP servers</td><td>Azure API Center</td><td><a href="#pub-apic">API Center row</a>. {ev("apic-inv")}</td></tr>
<tr><td>Check remote MCP traffic on the network</td><td>Global Secure Access MCP firewall</td><td><a href="#route-gsa">Firewall row</a>. Preview. {ev("fw-preview")}</td></tr>
<tr><td>Data protection, monitoring and inventory</td><td>Purview, Agent 365, Defender, Sentinel</td><td>Evidence on the <a href="{LONG}#s27">long page, 2.7</a> and <a href="{LONG}#s29">2.9</a>.</td></tr>
</tbody>
</table></div></div>
    </div>
  </section>
"""

AUTO_ROWS = [
    ("Approve a server change", "Pull request with the checklist. Tier 1 can be approved by the checklist.", "Named approvers for tiers 2 to 4.", f"{REC}"),
    ("Publish to GitHub and VS Code", f"Updated settings apply automatically within about an hour. A merge as the trigger is our own process. {REC}", "Approve the pull request, which is our own process.", ev("gh-file", "gh-server", "gh-hour")),
    ("Create servers for the gateway", "Our pipeline can create MCP servers in API Management. The service documents REST API, ARM, Bicep, CLI and Terraform.", "Connect the gateway, as Global Administrator. Allow or block each server in the admin center. Allow or block from a pipeline is not shown.", f"{ev('apim-rest', 'gw-ga', 'apim-block')} {UNV}"),
    ("Agent 365 bring-your-own", "A developer registers the server with the <code>a365</code> command line, which can be scripted. Approval is not automatic in any source.", "Review the request, approve it, grant Entra permissions.", f"{ev('byo-cli', 'byo-approve')} {UNV}"),
    ("Foundry tool policy", "Our pipeline writes the Git list into the policy assignment. Not tested.", "Review results. Handle existing agents and runtime separately.", f"{REC} {ev('deny-existing')}"),
    ("Copilot Studio data policy", "The <code>New-DlpPolicy</code> command creates a data policy. Our pipeline would call it. Not tested.", "Set the data policy until the pipeline exists.", f"{ev('dlp-cmd')} {REC}"),
    ("API Center inventory", "Continuous sync from API Management.", f"A person links the two first. {INF}", ev("apic-sync")),
    ("Network firewall lists", "Nothing documented.", "Set the URL allow and deny lists.", UNV),
    ("Intune firewall allow list", "Our pipeline would turn the Git list into an Intune policy. The Graph API creates configuration policies. Not tested.", "Test the block-all default on a pilot. Approve each rollout.", f"{ev('graph-cp', 'dk-csp')} {REC}"),
    ("Logs", "The firewall logs remote MCP traffic.", "Review the monthly pack.", f"{ev('log-remote')} {REC}"),
]
AUTO_TABLE = "\n".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in AUTO_ROWS)

AUTO = f"""
  <section class="sec" id="auto" aria-labelledby="h-auto">
    <header class="sh"><h2 id="h-auto">Automation and admin work</h2>
    <p class="goal"><b>Goal</b>Automate every step a source shows can be automated. Name each step a person still does.&nbsp;{REC}</p></header>
    <div class="blk" style="margin-top:14px">
      <div class="body"><div class="tbl-wrap"><table class="tbl">
<thead><tr><th>Step</th><th>Automatic</th><th>A person</th><th>Evidence</th></tr></thead>
<tbody>
{AUTO_TABLE}
</tbody>
</table></div></div>
      <details class="deep" id="rules"><summary>Nine rules that keep admin work low<span>All are recommendations</span></summary><div class="body">
        <div class="tbl-wrap">{RULES}</div>
      </div></details>
    </div>
  </section>
"""

PILOT_SEC = f"""
  <section class="sec" id="operate" aria-labelledby="ops-title">
    <header class="sh"><h2 id="ops-title">Monitor and stop an agent</h2>
    <p class="goal"><b>Runbook</b>Use these steps for the affected route.&nbsp;{REC}</p></header>
    {RUNBOOK}
  </section>
"""

WATCH = [
    ("Agent 365 Tools Gateway", ["gw-preview"]),
    ("Agent 365 bring-your-own MCP registry", ["byo-preview"]),
    ("Azure Policy approved tools for Foundry", ["pol-approved"]),
    ("Global Secure Access MCP firewall", ["fw-preview"]),
]
WATCH_ROWS = "\n".join(f"<tr><td>{n}</td><td>{ev(*k)}</td></tr>" for n, k in WATCH)

GAPS_LIST = [
    f"<strong>Nothing is tested in our tenant.</strong> Each place that says test is a step still to do, not a result. {UNV}",
    f"<strong>Gateway and BYO carry the preview label.</strong> Scope and behavior can change. {ev('gw-preview', 'byo-preview')}",
    f"<strong>Allow or block by pipeline.</strong> The gateway documents blocking in the admin center. BYO documents a person approving. No source shows a pipeline for either. Plan for a person to do it. {ev('apim-block', 'byo-approve')} {UNV}",
    f"<strong>Foundry.</strong> Deny acts on create and update. Existing resources are only marked non-compliant. Runtime blocking is not shown. {ev('deny-prevent', 'deny-existing')} {INF}",
    f"<strong>Local servers.</strong> The network firewall and its logs do not see them. Defender for Endpoint discovers supported ones on onboarded devices. No source shows it blocking a server. {UNV} The GitHub exact-command list is the one restriction with a source, on supported clients. {ev('fw-remote', 'log-remote', 'def-disc', 'gh-exact')}",
    f"<strong>Intune allow list.</strong> The default outbound block stops all traffic that matches no rule, not only MCP, and Microsoft calls it fit for certain highly secure environments. Domain rules fail behind a proxy, secure DNS, some VPNs and cached addresses. Windows only. Whether the Intune firewall profile takes domain names directly: not shown. Not tested. {ev('ifw-block', 'ifw-ver', 'dk-secure', 'dk-limits')} {UNV}",
    f"<strong>Defender discovery needs.</strong> The commercial cloud, Defender for Endpoint Plan 2 at minimum, and antivirus in active mode. Windows needs antivirus platform 4.18.26090.9 or later. macOS needs Defender for Endpoint 101.26072.0017 or later. Microsoft says discovery is not a complete inventory of installed software. {ev('def-cloud', 'def-lic', 'def-av', 'def-os', 'def-win', 'def-mac', 'def-incomplete')}",
    f"<strong>GitHub exemptions.</strong> Custom agent profiles and the built-in server are exempt. Coverage varies by environment. {ev('gh-profiles', 'gh-builtin', 'gh-vary')}",
    f"<strong>Direct connections.</strong> The gateway does not route agents by itself. Restrict server connectivity so the gateway is the only caller. Permissions at the API or data source still apply. {ev('apim-route', 'apim-restrict')}",
    f"<strong>Agent Builder.</strong> It has no external actions of its own, and draft agents from it are not in the inventory. An on or off switch is the only control the page documents. {ev('ab-ext', 'ab-copy', 'ab-draft', 'ab-admin')}",
    f"<strong>Agents Toolkit.</strong> Developers can add an MCP server as a plugin to a declarative agent. The admin center can block the plugin, but no source shows the Git list, the gateway or the firewall applying to it. {ev('tk-build', 'tk-block', 'tk-noaccess')} {UNV}",
    f"<strong>More gaps are on the long page:</strong> unmanaged consultant laptops, personal Copilot access, guest licensing, Sentinel connectors and policy start-up behavior. See its <a href=\"{LONG}#part5\">known gaps</a>.",
]
GAPS_OL = "\n".join(f"<li>{x}</li>" for x in GAPS_LIST)

GAPS = f"""
  <section id="gaps" aria-labelledby="h-g">
    <div class="part">
      <p class="lbl"><b>Gaps</b> · Read before you rely on any of it</p>
      <h2 id="h-g">Known gaps and what has not been tested</h2>
    </div>
    <div class="blk" style="margin-top:20px" id="watchlist">
      <p class="sub">{tg("u", "Bad&nbsp;news&nbsp;first")} Nothing here has been run in our tenant. Every place that says test is a step still to do.</p>
      <h3 style="font-size:1.05rem">Preview watchlist</h3>
      <p class="muted" style="font-size:0.92rem;max-width:46rem">Controls its vendor labels preview. Re-check them monthly.</p>
      <div class="tbl-wrap"><table class="tbl">
        <thead><tr><th>Control</th><th>Evidence</th></tr></thead>
        <tbody>
{WATCH_ROWS}
        </tbody>
      </table></div>
      <h3 style="font-size:1.05rem;margin-top:10px">The gaps</h3>
      <div class="body"><ol>
{GAPS_OL}
</ol></div>
    </div>
  </section>
"""

EV_ROWS = []
for key, skey, q in QUOTES:
    title, url, date = SOURCES[skey]
    shown = date or "none shown"
    EV_ROWS.append(
        f'<tr id="ev-{IDS[key]}"><td>{IDS[key]}</td><td>{html.escape(q, quote=False)}</td>'
        f'<td><a href="{url}{frag(q)}">{title}</a></td><td>{shown}</td></tr>')
EV_TABLE = "\n".join(EV_ROWS)

EVIDENCE = f"""
  <section id="evidence" aria-labelledby="h-e">
    <div class="part">
      <p class="lbl"><b>Evidence</b> · Exact quotes and sources</p>
      <h2 id="h-e">Quotes behind the route table</h2>
    </div>
    <div class="blk" style="margin-top:20px">
      <p class="sub">Each quote was found word for word on its source page on {CHECKED}. The link opens the page at the quote. Page date is the date the page shows.</p>
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
    <p>Documentation checked {CHECKED}. The controls shown here are proposed. No tests have run in a real tenant, on a consultant device or on an agent runtime.</p>
    {AI_NOTE}
  </footer>
"""

# ---- assemble ------------------------------------------------------------
HEAD = re.sub(r"<title>.*?</title>", "<title>Governing MCP servers summary</title>", HEAD, flags=re.S)
HEAD = re.sub(r'(<meta name="description" content=")[^"]*(")',
              r"\1How to govern MCP servers and what the target state looks like, with what we can and cannot do.\2", HEAD)
MARKERS = SRC[SRC.index("<body>") + 6:SRC.index('<div class="page" id="top">')]

BODY = f"""{HEAD}{STYLE}
</head>
<body>{MARKERS}<div class="page" id="top">
{MAST}
  <main id="main-content" tabindex="-1">
{Q1}{CAN}{Q2}{AUTO}{PILOT_SEC}{GAPS}{DISCUSS}{EVIDENCE}
  </main>
{FOOTER}
</div>

{SCRIPT}
</body>
</html>
"""

REMAP = {"#map": "#can", "#s24": "#q1", "#part5": "#gaps"}
for a, b in REMAP.items():
    BODY = BODY.replace(f'href="{a}"', f'href="{b}"')
defined = set(re.findall(r'\bid="([^"]+)"', BODY))
moved = set()


def to_long(m):
    target = m.group(1)
    if target in defined:
        return m.group(0)
    moved.add(target)
    return f'href="{LONG}#{target}"'


BODY = re.sub(r'href="#([^"]+)"', to_long, BODY)

for ch in (chr(0x2014), chr(0x2013)):
    if ch in BODY:
        sys.exit("em or en dash found in output")

OUT.write_text(add_anchors(BODY), encoding="utf-8")
print(f"wrote {OUT.name}, {len(BODY.splitlines())} lines")
print("links sent to the long page:", ", ".join(sorted(moved)) or "none")

for m in re.finditer(r"<(p|dd)\b[^>]*>(.*?)</\1>", BODY, re.S):
    words = len(re.sub(r"<[^>]+>", " ", m.group(2)).split())
    if words > 60:
        print(f"WARN {words} words: {re.sub(r'<[^>]+>', ' ', m.group(2))[:70]!r}")
