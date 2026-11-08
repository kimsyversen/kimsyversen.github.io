"""Build Developer-WS2.html and refresh the reviewed-text ledger in Developer-WS2.factcheck.md.

Usage: python3 -I scripts/build-developer-ws2.py

Rules the build enforces (see AGENTS.md, rule 3):
- A claim is a <p class="claim"> that ends in evidence chips (V1, V2) or a tag
  ([inference], [unverified]). Every chip links to a quote listed on the page.
- All other text goes through T(verdict, text) and is recorded in the ledger
  block of the fact check file. Verdicts: label, requirement.
- Every quote in the evidence module must be cited at least once.
"""

import html
import sys
from pathlib import Path
from urllib.parse import quote as urlquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from developer_ws2_evidence import BLOCK_FRAGS, CHECKED, IDS, QUOTES, SOURCES  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "wip" / "Developer-WS2.html"
LEDGER = ROOT / "wip" / "Developer-WS2.factcheck.md"
BEGIN = "<!-- Begin reviewed presentation text -->"
END = "<!-- End reviewed presentation text -->"

TEXTS = {}  # text -> verdict
USED = set()


def esc(s):
    return html.escape(s, quote=False)


def T(verdict, text, tag="span", attrs=""):
    """A presentation text: a label or a requirement, never a claim about a product."""
    if TEXTS.setdefault(text, verdict) != verdict:
        sys.exit(f"text has two verdicts: {text!r}")
    a = f" {attrs}" if attrs else ""
    return f"<{tag}{a} data-rt>{esc(text)}</{tag}>"


def L(text, **kw):
    return T("label", text, **kw)


def R(text, **kw):
    return T("requirement", text, **kw)


def ev(*keys):
    for k in keys:
        if k not in IDS:
            sys.exit(f"unknown quote key {k}")
        USED.add(k)
    ids = sorted((IDS[k] for k in keys), key=lambda v: int(v[1:]))
    return " ".join(f'<a class="ev" href="#ev-{v}">{v}</a>' for v in ids)


def tg(cls, text):
    return f'<span class="tg {cls}">[{text}]</span>'


INF = tg("i", "inference")
UNV = tg("u", "unverified")


def C(text, keys=(), tags=()):
    """A claim paragraph. Needs at least one chip or tag."""
    if not keys and not tags:
        sys.exit(f"claim without evidence or tag: {text[:60]}")
    parts = [esc(text)] + list(tags) + ([ev(*keys)] if keys else [])
    return f'<p class="claim">{" ".join(parts)}</p>'


def frag(q):
    """Text fragment so the link opens the source at the quote."""
    words = q.split()
    enc = lambda s: urlquote(s, safe="").replace("-", "%2D")  # noqa: E731
    if len(q) <= 90 and "'" not in q:
        return f"#:~:text={enc(q)}"
    apos = [n for n, w in enumerate(words) if "'" in w]
    start, end = words[:6], words[-6:]
    if apos and apos[0] < 6:
        start = words[:apos[0]]
    if apos and apos[-1] >= len(words) - 6:
        end = words[apos[-1] + 1:]
    return f"#:~:text={enc(' '.join(start))},{enc(' '.join(end))}"


def table(headers, rows, cls="tbl"):
    th = "".join(f"<th>{L(h)}</th>" for h in headers)
    body = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            tag = "th" if i == 0 else "td"
            attr = f' scope="row" data-l="{html.escape(headers[i])}"' if i == 0 else f' data-l="{html.escape(headers[i])}"'
            cells.append(f"<{tag}{attr}>{c}</{tag}>")
        body.append("<tr>" + "".join(cells) + "</tr>")
    return (f'<div class="tbl-wrap"><table class="{cls}"><thead><tr>{th}</tr></thead>'
            f'<tbody>{"".join(body)}</tbody></table></div>')


def section(sid, title, *content):
    return (f'<section class="sec" id="{sid}">\n  {T("label", title, "h2")}\n  '
            + "\n  ".join(content) + "\n</section>")


# ---- content -------------------------------------------------------------
LAYERS = table(
    ["Layer", "What it must do", "Carried by"],
    [
        [L("Deliver"), R("The approved server list must be on every device."),
         L("Intune: ADMX policies, macOS profiles")],
        [L("Client policy"), R("VS Code with Copilot must refuse servers that are not approved."),
         L("VS Code enterprise policy, GitHub managed settings")],
        [L("Network policy"), R("Remote servers that are not approved must not be reachable."),
         L("Intune firewall policy, Global Secure Access MCP firewall")],
        [L("Detect"), R("Servers on devices must be found and compared with the approved list."),
         L("Defender local agent discovery")],
        [L("Re-apply"), R("A changed or missing policy must be put back."),
         L("Intune remediations, custom compliance")],
        [L("App control"), R("On Windows, only VS Code and approved local server programs must be allowed to run."),
         L("Intune App Control for Business policy")],
        [L("File hash list"), R("On macOS, known unapproved client programs and server scripts must be blocked by file hash."),
         L("Defender file indicators")],
    ],
)

CLIENTS = table(
    ["Part", "Intune route", "Blocking control", "Gap"],
    [
        [L("VS Code on Windows"),
         C("The docs name Microsoft Intune for the imported VS Code policy templates. Each release ships the ADMX files, from version 1.69. Intune's import of custom ADMX is a public preview.", ["vs-intune", "vs-admx", "in-admx-prev"]),
         C("ChatAllowedMcpServers lets only matching servers run. ChatDeniedMcpServers blocks matching servers, and deny wins. ChatAllowManagedMcpServersOnly uses only the managed allowlist.", ["vs-allow", "vs-deny", "vs-only"])
         + C("A policy value overrides the setting at every level. Computer-level policy beats user-level policy.", ["vs-over", "vs-pc"]),
         C("Only VS Code reads these policies. An MCP client other than VS Code is not covered by them.", ["vs-only"], [INF])],
        [L("VS Code on macOS"),
         C("Each release ships a sample .mobileconfig file. The docs list Microsoft Intune as a way to deploy profiles at scale.", ["vs-mac", "vs-mac-intune"]),
         C("Whether the macOS profile accepts the three MCP policies was not read in the sample file.", [], [UNV]),
         C("A syntax error in a policy value stops the setting from being applied.", ["vs-syntax"])],
        [L("GitHub Copilot"),
         C("Native MDM delivery is available on Windows and macOS. All native MDM values must be strings.", ["gh-mdm", "gh-str"])
         + C("The deploy and reference pages do not name Intune, so an Intune route is an inference.", [], [INF]),
         C("The effective allowlist is the intersection of all sources: a server must be permitted by every source.", ["gh-inter"]),
         C("First-party servers, such as the built-in GitHub MCP server, are exempt from deny rules and cannot be blocked.", ["gh-builtin"])],
    ],
)

DELIVERY = table(
    ["Method", "Our design", "Facts from Microsoft Learn"],
    [
        [L("Settings catalog with imported ADMX"),
         R("VS Code policy templates should be imported and assigned to the pilot group first."),
         C("Intune can import custom ADMX and ADML templates. The import is a public preview.", ["in-admx", "in-admx-prev"])],
        [L("macOS custom profile"),
         R("The sample profile from the VS Code app, edited to the approved list, should be uploaded as a .mobileconfig file."),
         C("macOS settings must be in an .xml or .mobileconfig file. The channel cannot be changed after the profile is saved.", ["in-mac", "in-chan"])],
    ],
)

# Links that, in the 2026-11-06 headless Chrome test, did not show a highlight (see the fact check).
NO_HIGHLIGHT = {IDS[k] for k in ("in-mac", "in-chan")}

EV_ROWS = "".join(
    f'<tr id="ev-{IDS[k]}"><td data-l="Id">{IDS[k]}</td><td data-l="Quote">{esc(q)}</td>'
    f'<td data-l="Source"><a href="{SOURCES[s][1]}{frag(BLOCK_FRAGS.get(k, q))}">{esc(SOURCES[s][0])}</a>'
    + (f'<br>{L("The highlight may not show on this site. Search the page for the quote.")}' if IDS[k] in NO_HIGHLIGHT else "")
    + '</td>'
    f'<td data-l="Page date">{esc(SOURCES[s][2])}</td></tr>'
    for k, s, q in QUOTES
)
EVIDENCE = (f'<div class="tbl-wrap"><table class="tbl ev-tbl"><thead><tr>'
            + "".join(f"<th>{L(h)}</th>" for h in ["Id", "Quote", "Source", "Page date"])
            + f"</tr></thead><tbody>{EV_ROWS}</tbody></table></div>")

ROLLOUT = ("<ol class=\"steps\">" + "".join(f"<li>{R(t, tag='span')}</li>" for t in [
    "VS Code and every other MCP-capable client on developer laptops must be listed first, from Defender discovery and from the software inventory.",
    "One approved server list must live in a repository, and the VS Code policy values must be written from it.",
    "A pilot group must get the Windows ADMX policy and the macOS profile first. VS Code must be tested with an approved and a blocked server.",
    "A client other than VS Code must be removed. On Windows an App Control policy must block it. On macOS a file indicator must block it by hash.",
    "Each laptop group must be assigned node and python as allowed or not allowed in its App Control policy, because allowing one allows every script it runs.",
    "Approved remote servers must be the only MCP destinations allowed through the firewall policy or Global Secure Access.",
    "Defender discovery must be compared with the approved list every week, and every difference must be explained or fixed.",
    "A laptop whose VS Code policy has changed must be found, and the approved policy must be put back.",
    "Nothing here must be called done until it has been tested in a real tenant.",
]) + "</ol>")

SECTIONS = [
    section("answer", "The answer",
            R("The design must be: GitHub Copilot in VS Code is the only MCP client that runs, VS Code must carry a managed MCP server list, and Intune must deliver it and put it back when it changes.", tag="p"),
            C("Intune has no MCP policy of its own. No Intune page read for this work names one.", [], [INF]),
            C("The VS Code docs name Intune for the imported policy templates on Windows and for macOS profiles.", ["vs-intune", "vs-mac-intune"]),
            C("VS Code has three MCP policies: an allowlist, a denylist and a managed-only switch. Deny wins. A policy value overrides the setting at every level.", ["vs-allow", "vs-deny", "vs-only", "vs-over"]),
            C("GitHub documents OS-level delivery for Copilot. The page does not name Intune, so the Intune route for that is an inference.", ["gh-mdm"], [INF]),
            C("Intune can deliver App Control for Business policies to Windows devices. They restrict which apps run, so code runs only if the policy says so.", ["ac-intune", "ac-apps", "ac-code"]),
            C("Windows only: an App Control policy that lists VS Code can keep another MCP client from running. It can also stop a local server that is its own program file. No source names MCP for this.", ["ac-apps"], [INF]),
            C("Defender file indicators can block a file on macOS. Blocking prevents the file from being read, written or executed. On macOS they cover Mach-O executables, POSIX shell scripts and AppleScript files.", ["ind-mac", "ind-block", "ind-types"]),
            C("On macOS, a file indicator can block a known unapproved client program or server script by its hash. That is a deny list, so a file not on the list is not stopped. No source names MCP for this.", ["ind-types"], [INF]),
            C("App Control does not control scripts run through an unenlightened script host, such as many third-party Java or Python engines. A policy that allows such a host implicitly allows all scripts run through it.", ["ac-unenl", "ac-implicit"]),
            C("If node or python is such a host, a local server that it runs from a script file is not stopped on Windows while the policy allows it. Leaving it out of the policy also stops every approved server that needs it. On macOS the script is stopped only if it is on the deny list.", [], [INF]),
            C("With VS Code as the only client, its managed list covers the local servers it starts. The open case is another client on the laptop, or another copy of VS Code that does not read the policy.", ["vs-only"], [INF])),
    section("layers", "Seven layers", LAYERS),
    section("clients", "Copilot in VS Code", CLIENTS),
    section("delivery", "How Intune delivers",
            DELIVERY),
    section("drift", "Drift and tampering",
            C("Remediations need devices that are Microsoft Entra joined or hybrid joined. One license listed is Windows Enterprise E3 or E5, included in Microsoft 365 F3, E3 or E5.", ["in-rem-join", "in-rem-lic"]),
            C("If a scheduled remediation run is missed, it runs when the device is online.", ["in-rem-miss"]),
            C("Custom compliance uses a PowerShell script on Windows and a POSIX shell script on Linux and macOS. The management extension checks for new or updated scripts and runs discovery scripts every eight hours.", ["in-comp-os", "in-comp-8h"]),
            C("GitHub says updated server-managed settings are applied within about an hour. No refresh time was found for MDM-managed settings.", ["gh-hour"], [UNV]),
            C("Whether Intune or a remediation puts back a changed VS Code policy value was not tested.", [], [UNV]),
            R("The approved list must be compared with device state at least weekly.", tag="p")),
    section("network", "Network and detection",
            C("An Intune firewall setting can block all outbound connections that do not match an outbound rule. It applies to Windows 1809 and later.", ["ifw-block", "ifw-ver"]),
            C("The Firewall CSP can be used with an MDM solution like Microsoft Intune. A rule for a domain name needs a DNS query to resolve it. Limits include proxy access, secure DNS services and some VPN tunnels.", ["dk-csp", "dk-dns", "dk-limits"]),
            C("The Global Secure Access MCP firewall is in preview. It needs a valid Microsoft Entra Internet Access license, the client on a joined device, and TLS inspection.", ["fw-preview", "fw-license", "fw-client", "fw-tls"]),
            C("Only remote MCP servers are inspected. Local MCP servers on a device are not visible to Global Secure Access.", ["fw-remote"]),
            C("Defender discovers supported AI agents and their MCP servers on onboarded devices. Details can include the server name, type, endpoint and the command that starts a local server.", ["def-disc", "def-cmd"]),
            C("Configuration discovery needs antivirus active mode and real-time protection. Plan 2 is the minimum license.", ["def-av", "def-lic"]),
            C("Discovery is not a complete inventory of installed software. It does not prove active use.", ["def-incomplete", "def-noproof"])),
    section("gaps", "Open gaps",
            C("Local servers that an allowed interpreter runs from a script file, and local servers on macOS that are not on a file deny list, are stopped by no layer here. The one lever is to leave the interpreter out of the Windows policy.", ["fw-remote", "def-incomplete", "ac-implicit"], [INF]),
            C("The Graph API can create a settings catalog policy. Whether every setting named on this page can be sent that way was not checked, so a pipeline from a repository to Intune is not shown.", ["graph-cp"], [UNV]),
            C("The Intune route for GitHub Copilot's own MDM values is not named by GitHub.", [], [INF]),
            C("Whether a second VS Code copy, such as Insiders or a portable install, reads the same policy was not checked.", [], [UNV]),
            R("VS Code on every laptop must be a version whose reference page lists the three MCP policies.", tag="p"),
            R("If another MCP client is found on a laptop, a script must read its MCP file and flag any server that is not approved. That detects a server. It does not stop one.", tag="p"),
            L("Nothing tested in a real tenant", tag="p")),
    section("rollout", "Rollout", ROLLOUT),
    section("evidence", "Evidence",
            L("Checked 2026-11-06: every quote below matched its source word for word, by script.", tag="p"),
            R("A match must be read as proof of the words only, not of the claim built on them.", tag="p"),
            L("Tags: inference means reasoned from the quotes with no source of its own. Unverified means not checked.", tag="p"),
            EVIDENCE),
]

CSS = """
:root{
  color-scheme:light;
  --bg:#F3F0E8; --ink:#17150F; --muted:#5F5A4F; --line:#D2CCBE; --rule:#17150F;
  --red:#B5321C; --red-soft:#F0DCD3; --hover:rgba(23,21,15,.035);
  --display:"Archivo","Arial Narrow",Arial,sans-serif;
  --body:"Public Sans",system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    color-scheme:dark;
    --bg:#15140F; --ink:#ECE7DB; --muted:#A49E90; --line:#37342C; --rule:#ECE7DB;
    --red:#F07A60; --red-soft:#3B211A; --hover:rgba(236,231,219,.04);
  }
}
*{box-sizing:border-box}
p,td,th,li,h2,dd,dt,.lead{overflow-wrap:anywhere}
@media (prefers-reduced-motion:no-preference){html{scroll-behavior:smooth}}
body{margin:0;background:var(--bg);color:var(--ink);font:1rem/1.55 var(--body);-webkit-font-smoothing:antialiased}
.page{max-width:1200px;margin:0 auto;padding:0 max(16px,env(safe-area-inset-right,0px)) 64px max(16px,env(safe-area-inset-left,0px))}
a{color:inherit;text-decoration-color:var(--red);text-decoration-thickness:1.5px;text-underline-offset:3px}
a:hover{color:var(--red)}
a:focus-visible,[tabindex]:focus-visible{outline:2px solid var(--red);outline-offset:3px}
h1,h2{font-family:var(--display);text-wrap:balance;margin:0}
h2{font-size:clamp(1.35rem,2.4vw,1.7rem);font-weight:750;line-height:1.1;letter-spacing:-0.012em}
p{margin:0}
.mast{border-top:6px solid var(--rule);padding-top:10px}
.meta{display:flex;justify-content:space-between;flex-wrap:wrap;gap:4px 16px;font-size:0.82rem;color:var(--muted);padding-bottom:10px;border-bottom:1px solid var(--rule)}
h1{font-size:clamp(2.6rem,9.5vw,7rem);font-weight:800;font-stretch:112%;line-height:0.9;letter-spacing:-0.035em;margin:30px 0 0;margin-left:-0.04em}
.intro{display:grid;grid-template-columns:minmax(0,7fr) minmax(0,5fr);gap:24px 56px;align-items:start;padding:26px 0 30px}
.lead{font-size:clamp(1.1rem,2vw,1.35rem);line-height:1.42;max-width:36rem;display:grid;gap:10px}
.spec{margin:0;display:grid;grid-template-columns:auto 1fr;font-size:0.9rem;border-top:1px solid var(--line)}
.spec dt,.spec dd{padding:7px 0;border-bottom:1px solid var(--line)}
.spec dt{padding-right:18px;color:var(--muted)}
.spec dd{margin:0}
@media (max-width:800px){.intro{grid-template-columns:1fr}}
.sec{border-top:1px solid var(--rule);padding:14px 0 40px;display:grid;gap:14px;align-content:start;scroll-margin-top:12px}
.claim{font-size:0.95rem}
.tbl-wrap{overflow-x:auto}
.tbl{border-collapse:collapse;width:100%;font-size:0.9rem;border-top:2px solid var(--rule);border-bottom:2px solid var(--rule)}
.tbl th,.tbl td{text-align:left;vertical-align:top;padding:12px 10px;border-top:1px solid var(--line)}
.tbl th:first-child,.tbl td:first-child{padding-left:4px}
.tbl thead th{font:600 0.68rem/1.4 var(--body);letter-spacing:0.09em;text-transform:uppercase;color:var(--muted);white-space:nowrap;padding-top:8px;padding-bottom:8px;border-top:0;border-bottom:1px solid var(--rule)}
.tbl tbody tr:first-child > *{border-top:0}
.tbl tbody th{font:700 1rem/1.2 var(--display)}
.tbl td .claim + .claim{margin-top:8px}
.tbl tr:target{background:var(--red-soft)}
.ev-tbl td:first-child{font:500 0.85rem var(--mono);white-space:nowrap}
.ev-tbl td:nth-child(2){max-width:34rem;overflow-wrap:anywhere}
.ev{font:500 0.72rem var(--mono);text-decoration:none;border-bottom:1.5px solid var(--red);padding:0 2px;margin-left:2px;white-space:nowrap}
.tg{font:600 0.62rem/1 var(--body);letter-spacing:0.06em;text-transform:uppercase;border:1px solid var(--muted);color:var(--muted);padding:2px 5px;white-space:nowrap}
.tg.u{border-color:var(--red);color:var(--red)}
.steps{margin:0;padding-left:1.4rem;display:grid;gap:8px}
@media (max-width:760px){
  .tbl-wrap{overflow:visible}
  .tbl thead{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
  .tbl,.tbl tbody,.tbl tr,.tbl th,.tbl td{display:block;width:100%}
  .tbl tbody tr{padding:12px 0;border-top:1px solid var(--line)}
  .tbl tbody tr:first-child{border-top:0}
  .tbl th,.tbl td,.tbl th:first-child,.tbl td:first-child{padding:4px 0;border:0}
  .tbl td::before{content:attr(data-l);display:block;font:600 0.64rem/1.4 var(--body);letter-spacing:0.09em;text-transform:uppercase;color:var(--muted)}
  .ev-tbl td:first-child{white-space:normal}
}
footer{border-top:2px solid var(--rule);padding-top:14px;display:grid;gap:10px;font-size:0.85rem;color:var(--muted)}
.ai-note{display:grid;grid-template-columns:9rem 1fr;gap:2px 16px;margin:6px 0 0;padding-top:12px;border-top:1px solid var(--line);font-size:0.78rem;line-height:1.5;color:var(--muted)}
.ai-note b{font-weight:600;font-size:0.68rem;letter-spacing:0.09em;text-transform:uppercase;color:var(--ink);padding-top:1px}
@media (max-width:560px){.ai-note{grid-template-columns:1fr}}
"""

HEAD = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Intune and MCP</title>
<meta name="description" content="How Intune can help govern MCP servers for GitHub Copilot in VS Code on managed laptops: it delivers the VS Code policy, and VS Code, the network and Defender do the rest.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,600..800&family=IBM+Plex+Mono:wght@400;500;600&family=Public+Sans:ital,wght@0,400;0,600;1,400&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="page">
<header class="mast">
  <div class="meta">{L("Current as of 2026-11-06")}<a href="../Developer-WS.html">{L("Developer workstation page")}</a></div>
  {L("Intune and MCP", tag="h1")}
  <div class="intro">
    <div class="lead">{R("Only approved MCP servers must run on a managed developer laptop.", tag="p")}{R("A change from the approved state must show up and be put back.", tag="p")}</div>
    <dl class="spec">
      <dt>{L("Scope")}</dt><dd>{L("Windows and macOS laptops managed by Intune, with GitHub Copilot in VS Code as the only MCP client")}</dd>
      <dt>{L("Status")}</dt><dd>{L("Nothing tested in a real tenant")}</dd>
      <dt>{L("Basis")}</dt><dd>{L("Vendor documentation, checked 2026-11-06")}</dd>
    </dl>
  </div>
</header>
"""

FOOT = """
<footer>
  <p class="ai-note"><b>Made with AI</b><span>This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human.</span></p>
</footer>
</div>
</body>
</html>
"""


def main():
    body = "\n".join(SECTIONS)
    unused = [k for k, _, _ in QUOTES if k not in USED]
    if unused:
        sys.exit(f"quotes never cited: {unused}")
    PAGE.write_text(HEAD + body + FOOT, encoding="utf-8")
    block = BEGIN + "\n| verdict | text |\n|---|---|\n" + "\n".join(
        f"| {v} | {t} |" for t, v in TEXTS.items()) + "\n" + END
    if LEDGER.exists() and BEGIN in LEDGER.read_text(encoding="utf-8"):
        md = LEDGER.read_text(encoding="utf-8")
        md = md.split(BEGIN, 1)[0] + block + md.split(END, 1)[1]
    else:
        md = ("# Fact check: Developer-WS2\n\nBelongs to: [Developer-WS2.html](Developer-WS2.html)\n\n"
              "## Reviewed presentation text\n\n" + block + "\n")
    LEDGER.write_text(md, encoding="utf-8")
    print(f"wrote {PAGE.name}: {len(QUOTES)} quotes, {len(TEXTS)} reviewed texts")


if __name__ == "__main__":
    main()
