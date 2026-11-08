# Fact check: Developer-WS2

Belongs to: [Developer-WS2.html](Developer-WS2.html)

## Reviewed presentation text

<!-- Begin reviewed presentation text -->
| verdict | text |
|---|---|
| label | Deliver |
| requirement | The approved server list must be on every device. |
| label | Intune: ADMX policies, macOS profiles |
| label | Client policy |
| requirement | VS Code with Copilot must refuse servers that are not approved. |
| label | VS Code enterprise policy, GitHub managed settings |
| label | Network policy |
| requirement | Remote servers that are not approved must not be reachable. |
| label | Intune firewall policy, Global Secure Access MCP firewall |
| label | Detect |
| requirement | Servers on devices must be found and compared with the approved list. |
| label | Defender local agent discovery |
| label | Re-apply |
| requirement | A changed or missing policy must be put back. |
| label | Intune remediations, custom compliance |
| label | App control |
| requirement | On Windows, only VS Code and approved local server programs must be allowed to run. |
| label | Intune App Control for Business policy |
| label | File hash list |
| requirement | On macOS, known unapproved client programs and server scripts must be blocked by file hash. |
| label | Defender file indicators |
| label | Layer |
| label | What it must do |
| label | Carried by |
| label | VS Code on Windows |
| label | VS Code on macOS |
| label | GitHub Copilot |
| label | Part |
| label | Intune route |
| label | Blocking control |
| label | Gap |
| label | Settings catalog with imported ADMX |
| requirement | VS Code policy templates should be imported and assigned to the pilot group first. |
| label | macOS custom profile |
| requirement | The sample profile from the VS Code app, edited to the approved list, should be uploaded as a .mobileconfig file. |
| label | Method |
| label | Our design |
| label | Facts from Microsoft Learn |
| label | The highlight may not show on this site. Search the page for the quote. |
| label | Id |
| label | Quote |
| label | Source |
| label | Page date |
| requirement | VS Code and every other MCP-capable client on developer laptops must be listed first, from Defender discovery and from the software inventory. |
| requirement | One approved server list must live in a repository, and the VS Code policy values must be written from it. |
| requirement | A pilot group must get the Windows ADMX policy and the macOS profile first. VS Code must be tested with an approved and a blocked server. |
| requirement | A client other than VS Code must be removed. On Windows an App Control policy must block it. On macOS a file indicator must block it by hash. |
| requirement | Each laptop group must be assigned node and python as allowed or not allowed in its App Control policy, because allowing one allows every script it runs. |
| requirement | Approved remote servers must be the only MCP destinations allowed through the firewall policy or Global Secure Access. |
| requirement | Defender discovery must be compared with the approved list every week, and every difference must be explained or fixed. |
| requirement | A laptop whose VS Code policy has changed must be found, and the approved policy must be put back. |
| requirement | Nothing here must be called done until it has been tested in a real tenant. |
| requirement | The design must be: GitHub Copilot in VS Code is the only MCP client that runs, VS Code must carry a managed MCP server list, and Intune must deliver it and put it back when it changes. |
| label | The answer |
| label | Seven layers |
| label | Copilot in VS Code |
| label | How Intune delivers |
| requirement | The approved list must be compared with device state at least weekly. |
| label | Drift and tampering |
| label | Network and detection |
| requirement | VS Code on every laptop must be a version whose reference page lists the three MCP policies. |
| requirement | If another MCP client is found on a laptop, a script must read its MCP file and flag any server that is not approved. That detects a server. It does not stop one. |
| label | Nothing tested in a real tenant |
| label | Open gaps |
| label | Rollout |
| label | Checked 2026-11-06: every quote below matched its source word for word, by script. |
| requirement | A match must be read as proof of the words only, not of the claim built on them. |
| label | Tags: inference means reasoned from the quotes with no source of its own. Unverified means not checked. |
| label | Evidence |
| label | Current as of 2026-11-06 |
| label | Developer workstation page |
| label | Intune and MCP |
| requirement | Only approved MCP servers must run on a managed developer laptop. |
| requirement | A change from the approved state must show up and be put back. |
| label | Scope |
| label | Windows and macOS laptops managed by Intune, with GitHub Copilot in VS Code as the only MCP client |
| label | Status |
| label | Basis |
| label | Vendor documentation, checked 2026-11-06 |
<!-- End reviewed presentation text -->


## Claims and verdicts (2026-11-06)

Each row is one claim paragraph on the page. Two steps were done. The script found each quote in its source word for word. Then each claim was read next to its quotes, and wording that went past a quote was changed earlier (marked in the verdict). Reading is a judgment, not a mechanical test. Rows for clients that left the page were removed on 2026-11-06 (see D21 in the decisions file).

| # | Claim | Evidence | Verdict |
|---|---|---|---|
| 1 | Intune has no MCP policy of its own. No Intune page read for this work names one. | none | Labelled inference. No quote. Drawn from pages read, not stated on them. |
| 2 | The VS Code docs name Intune for the imported policy templates on Windows and for macOS profiles. | V1 V48 | Read against the quotes 2026-11-06; matches. The Windows quote names Intune for the imported templates. The macOS quote lists Intune with Apple Business Manager under deploying profiles at scale. |
| 3 | VS Code has three MCP policies: an allowlist, a denylist and a managed-only switch. Deny wins. A policy value overrides the setting at every level. | V2 V3 V4 V5 | Read against the quotes 2026-11-06; matches. The reference page lists a minimum VS Code version per policy (1.130 for the allowlist and denylist, 1.132 for managed-only, read in the page source, not in the rendered text). That is not on the page as a claim, so the page asks for a version check instead. |
| 4 | GitHub documents OS-level delivery for Copilot. The page does not name Intune, so the Intune route for that is an inference. | V8 | Read against the quote 2026-11-06; the quoted part matches. The Intune route is an inference with no quote. |
| 5 | Intune can deliver App Control for Business policies to Windows devices. They restrict which apps run, so code runs only if the policy says so. | V39 V40 V41 | Read against the quotes 2026-11-06; matches. The Intune quote says "managed Windows devices". The Windows page quote is about code running only if policy says so. |
| 6 | Windows only: an App Control policy that lists VS Code can keep another MCP client from running. It can also stop a local server that is its own program file. No source names MCP for this. | V40 | Labelled inference. The quote says the policy restricts the apps users can run. Applying it to MCP clients and servers is reasoning, not a source statement. Not tested. |
| 7 | Defender file indicators can block a file on macOS. Blocking prevents the file from being read, written or executed. On macOS they cover Mach-O executables, POSIX shell scripts and AppleScript files. | V42 V43 V44 | Read against the quotes 2026-11-06; matches. The page's Windows note says PE files only. The macOS note names the three types. |
| 8 | On macOS, a file indicator can block a known unapproved client program or server script by its hash. That is a deny list, so a file not on the list is not stopped. No source names MCP for this. | V44 | Labelled inference. The quote lists the file types. Applying it to MCP clients has no quote. Not tested. Hash lists need the exact file, so a new build of a client is not covered until it is added. |
| 9 | App Control does not control scripts run through an unenlightened script host, such as many third-party Java or Python engines. A policy that allows such a host implicitly allows all scripts run through it. | V45 V46 | Read against the quotes 2026-11-06; matches. The page says "many 3rd-party Java or Python engines", so it does not say node or python specifically. The claim keeps "many" and "such as". |
| 10 | If node or python is such a host, a local server that it runs from a script file is not stopped on Windows while the policy allows it. Leaving it out of the policy also stops every approved server that needs it. On macOS the script is stopped only if it is on the deny list. | none | Labelled inference. Whether node or python is an unenlightened host was not found on a Microsoft page and was not tested. The cost of leaving them out is reasoning from how the approved servers start (for example npx). |
| 11 | With VS Code as the only client, its managed list covers the local servers it starts. The open case is another client on the laptop, or another copy of VS Code that does not read the policy. | V5 | Labelled inference. The quote shows the managed-only setting uses only the managed allowlist. That this covers every local server VS Code starts was not tested. A user-built client would not be covered. |
| 12 | The docs name Microsoft Intune for the imported VS Code policy templates. Each release ships the ADMX files, from version 1.69. Intune's import of custom ADMX is a public preview. | V1 V6 V12 | Read against the quotes 2026-11-06; matches. |
| 13 | ChatAllowedMcpServers lets only matching servers run. ChatDeniedMcpServers blocks matching servers, and deny wins. ChatAllowManagedMcpServersOnly uses only the managed allowlist. | V3 V4 V5 | Read against the quotes 2026-11-06; matches. |
| 14 | A policy value overrides the setting at every level. Computer-level policy beats user-level policy. | V2 V7 | Read against the quotes 2026-11-06; matches. |
| 15 | Only VS Code reads these policies. An MCP client other than VS Code is not covered by them. | V5 | Labelled inference. The policies are VS Code settings. No source says another client ignores them, and none says it reads them. |
| 16 | Each release ships a sample .mobileconfig file. The docs list Microsoft Intune as a way to deploy profiles at scale. | V47 V48 | Read against the quotes 2026-11-06; matches. The sample file is in the VS Code app bundle under Contents/Resources/app/policies (read on the page, not quoted). Version 1.99 is the first with a sample. |
| 17 | Whether the macOS profile accepts the three MCP policies was not read in the sample file. | none | Labelled unverified. No quote. The sample file was not opened. The docs say a profile holds key and value pairs for the available policies (read 2026-11-06, not quotable because of how the page renders code), which is a reason to expect it, not proof. |
| 18 | A syntax error in a policy value stops the setting from being applied. | V49 | Read against the quote 2026-11-06; matches. The note appears in the macOS steps. Whether it also holds on Windows was not checked. |
| 19 | Native MDM delivery is available on Windows and macOS. All native MDM values must be strings. | V8 V9 | Read against the quotes 2026-11-06; matches. |
| 20 | The deploy and reference pages do not name Intune, so an Intune route is an inference. | none | Labelled inference. No quote. Drawn from pages read, not stated on them. |
| 21 | The effective allowlist is the intersection of all sources: a server must be permitted by every source. | V10 | Read against the quotes 2026-11-06; matches. |
| 22 | First-party servers, such as the built-in GitHub MCP server, are exempt from deny rules and cannot be blocked. | V21 | Read against the quotes 2026-11-06; matches. |
| 23 | Intune can import custom ADMX and ADML templates. The import is a public preview. | V11 V12 | Read against the quotes 2026-11-06; matches. |
| 24 | macOS settings must be in an .xml or .mobileconfig file. The channel cannot be changed after the profile is saved. | V13 V14 | Read against the quotes 2026-11-06; matches. |
| 25 | Remediations need devices that are Microsoft Entra joined or hybrid joined. One license listed is Windows Enterprise E3 or E5, included in Microsoft 365 F3, E3 or E5. | V15 V16 | Read against the quotes 2026-11-06; matches. |
| 26 | If a scheduled remediation run is missed, it runs when the device is online. | V17 | Read against the quotes 2026-11-06; matches. |
| 27 | Custom compliance uses a PowerShell script on Windows and a POSIX shell script on Linux and macOS. The management extension checks for new or updated scripts and runs discovery scripts every eight hours. | V18 V19 | Read against the quotes 2026-11-06; matches. |
| 28 | GitHub says updated server-managed settings are applied within about an hour. No refresh time was found for MDM-managed settings. | V20 | Read against the quotes 2026-11-06; the quoted part matches. The unverified part has no quote. |
| 29 | Whether Intune or a remediation puts back a changed VS Code policy value was not tested. | none | Labelled unverified. No quote. Not tested. |
| 30 | An Intune firewall setting can block all outbound connections that do not match an outbound rule. It applies to Windows 1809 and later. | V33 V34 | Read against the quotes 2026-11-06; matches. |
| 31 | The Firewall CSP can be used with an MDM solution like Microsoft Intune. A rule for a domain name needs a DNS query to resolve it. Limits include proxy access, secure DNS services and some VPN tunnels. | V35 V36 V37 | Read against the quotes 2026-11-06; matches. |
| 32 | The Global Secure Access MCP firewall is in preview. It needs a valid Microsoft Entra Internet Access license, the client on a joined device, and TLS inspection. | V28 V30 V31 V32 | Read against the quotes 2026-11-06; matches. |
| 33 | Only remote MCP servers are inspected. Local MCP servers on a device are not visible to Global Secure Access. | V29 | Read against the quotes 2026-11-06; matches. |
| 34 | Defender discovers supported AI agents and their MCP servers on onboarded devices. Details can include the server name, type, endpoint and the command that starts a local server. | V22 V24 | Read against the quotes 2026-11-06; matches. |
| 35 | Configuration discovery needs antivirus active mode and real-time protection. Plan 2 is the minimum license. | V23 V26 | Read against the quotes 2026-11-06; matches. |
| 36 | Discovery is not a complete inventory of installed software. It does not prove active use. | V25 V27 | Read against the quotes 2026-11-06; matches. |
| 37 | Local servers that an allowed interpreter runs from a script file, and local servers on macOS that are not on a file deny list, are stopped by no layer here. The one lever is to leave the interpreter out of the Windows policy. | V25 V29 V46 | Read against the quotes 2026-11-06; the quoted part matches. The inference part has no quote. A web search on 2026-11-06 found no Microsoft control that allows only approved executables on macOS, and no Microsoft page that names node or python for App Control script enforcement. |
| 38 | The Graph API can create a settings catalog policy. Whether every setting named on this page can be sent that way was not checked, so a pipeline from a repository to Intune is not shown. | V38 | Read against the quotes 2026-11-06; the quoted part matches. The unverified part has no quote. |
| 39 | The Intune route for GitHub Copilot's own MDM values is not named by GitHub. | none | Labelled inference. No quote. Drawn from the pages read, not stated on them. |
| 40 | Whether a second VS Code copy, such as Insiders or a portable install, reads the same policy was not checked. | none | Labelled unverified. No quote. The reference page offers a link to open each policy in VS Code Insiders, which suggests Insiders reads policies, but that was not read as a statement. |

## How it was checked

- `python3 -I scripts/check-developer-ws2.py <cache-dir>` on 2026-11-06: 49 quotes from 17 source pages, each found word for word, 0 problems. The source pages were fetched on 2026-11-06 and the checker reads that copy. Every quote is listed on the page with a link that opens the source at that passage.
- The same script checks that every chip points at a listed quote, that no paragraph has more than 60 words, that no en or em dash is on the page, that the Made with AI note is word for word, that no note file is named on the page, and that the ledger above matches the page text exactly.
- The ledger script proves a verdict was recorded for the exact wording. It does not prove the verdict is right. Each label or requirement was judged by reading it.
- Scope cut on 2026-11-06: the page covers GitHub Copilot in VS Code only (D21). The quotes for Claude Code, Codex, Claude Desktop and Cursor, and for PowerShell scripts, macOS shell scripts and Win32 apps, were removed with their claims. Quote numbers were reassigned in that cut.

## Findings that rest on absence

- "No Intune page read names an MCP setting" is `[inference]`. Pages read: the ADMX import, macOS custom settings, remediations, custom compliance, firewall and dynamic keyword pages, and earlier the script and Win32 pages. Not a search of all Intune documentation.
- "GitHub pages do not name Intune" is `[inference]`. Pages read: GitHub Copilot managed settings deploy and reference pages.
- "App Control can keep another client or a local server program from running" is `[inference]`. The sources say the policy restricts which apps run on managed Windows devices. They do not mention MCP. Pages read: the Intune App Control for Business page and the Application Control for Windows overview.
- "No layer stops script-run local servers, or macOS local servers not on a deny list" is `[inference]` from the Global Secure Access and Defender quotes (remote only, discovery only), from App Control being about apps, and from file indicators being per file hash. On 2026-11-06 a web search for a Microsoft macOS allowlist (Intune or Defender) returned only third-party tools such as Santa, and Microsoft pages that do not cover it. The App Control script enforcement page says scripts run through an unenlightened host such as many 3rd-party Java or Python engines are not controlled.
- "Only VS Code reads these policies" is `[inference]`. The policies are VS Code settings.
- The VS Code macOS route was checked on 2026-11-06 on the official page (code.visualstudio.com/docs/enterprise/policies). It says each release from 1.99 ships a sample `.mobileconfig`, and lists Intune for deploying profiles at scale. A vendor guide (JFrog) says the allowlist is delivered as a macOS configuration profile and needs a recent VS Code. That vendor source is not used on the page.

## Not tested

- Nothing was tested on a real system or in a real Intune tenant. No policy was deployed, no remediation was run and no client was seen to honour a policy.
- Not opened: the sample `.mobileconfig` in the VS Code app. So it is `[unverified]` that the macOS profile holds the three MCP policies and which domain and key names it uses.
- Not checked: MDM refresh time for GitHub Copilot, sending every named setting through the Graph API, whether a second VS Code copy (Insiders, portable) reads the same policy. These are `[unverified]` on the page.
- Whether Intune or a remediation puts back a changed VS Code policy value was not tested.
- Minimum VS Code versions: in the page source of the policy reference (not in its rendered text), the allowlist and denylist carry 1.130 and the managed-only switch 1.132. Another source said a later version. The page does not state a number. It asks for a version check.
- Still open: a local server that an allowed interpreter (node, python) runs from a script file, and a macOS local server that is not on a file hash list, are stopped by no layer here. Sourced (Microsoft Learn, 2026-11-02): App Control does not control scripts run through an unenlightened script host, and allowing such a host allows all scripts run through it. The one lever on Windows is to leave node and python out of the policy, which also stops approved servers that need them. Whether node or python is unenlightened was not found on a Microsoft page (`[inference]`). No Microsoft macOS control that allows only approved executables was found on 2026-11-06. With Copilot in VS Code as the only client, these gaps matter only if another client or another VS Code copy is present (`[inference]`). This gap is stated on the page and is not solved by it.

## Browser test, 2026-11-06 (local server, built-in browser)

### Current page (cut to Copilot in VS Code), 2026-11-06

- Desktop 1280 wide, light: scroll width equals client width, no console errors.
- 375px wide, dark emulated: scroll width 375, no sideways scroll, no console errors.
- No `localStorage` is used.
- The three links added in the cut, viewed one at a time in the built-in browser with a screenshot of each: V47 (sample .mobileconfig sentence), V48 (range fragment, "For enterprise deployments ... such as:") and V49 (syntax error sentence, single-block fragment). All three show the highlighted text. The first V49 fragment started at a weak word ("If") and was replaced with a single-block piece.
- Checker: 49 quotes, 49 link targets, 81 page texts, 79 ledger rows, 0 problems.
- Not tested: a real mouse click on every source link, a one-by-one highlight re-run of the other 46 links after the renumbering (the 78-link run below was on the earlier six-client page), and anything in a real tenant. Of the 12 links that did not highlight in the earlier run, only the two Microsoft Learn custom settings for Apple links (now V13 and V14) are still on the page. They keep the label "The highlight may not show on this site. Search the page for the quote." and were not re-run.

### Earlier six-client page (superseded, kept as history)

- Desktop light: no sideways scroll (scroll width equals client width), no console errors.
- Dark mode emulated: background and text colours switch to the dark tokens.
- 375px wide: first run scrolled sideways by 10px because long paths and key names did not wrap. Fixed with `overflow-wrap:anywhere` on text blocks. After the fix scroll width is 375, nothing sticks out.
- Real mouse click on chip V3: the URL hash becomes `#ev-V3` and the page scrolls to that row. The row's source link carries a `#:~:text=` fragment.
- Source links, all 78 opened one at a time in a fresh foreground headless Chrome tab (DevTools protocol, no mouse), on 2026-11-06, and a screenshot of each viewed one by one. Parallel tabs were tried first and discarded, because background tabs do not scroll. A first screenshot set was all black for scrolled pages (the capture clip was document-relative) and was discarded. Result with scripts on: 66 show the highlighted quote (V1 to V27, V38, V39, V42 to V78). 12 do not: V28 to V32, V40 and V41 scroll to the passage but show no highlight even after 12 seconds, and V33 to V37 (cursor.com) neither scroll nor highlight. Cause found the same day: the same 12 links were opened again with page scripts switched off (CDP `Emulation.setScriptExecutionDisabled`), and all 12 scroll to the quote and highlight it (screenshots viewed for V28 to V37, V40 and V41). So the fragments are right and each site's own scripts clear the highlight or the scroll after load. That is the observed behaviour. The exact script was not identified. A site can change this at any time. V77 first lit the page title and top block, because a range fragment started at the words App Control. Its fragment now starts at the words scripts run through, and the screenshot shows the sentence lit. The 12 evidence rows carry the label "The highlight may not show on this site. Search the page for the quote." The quotes themselves match the pages (checker). Earlier notes that V28, V33 and V35 had been fixed were wrong: those highlights came from same-document navigation in a reused tab.
- Not tested: a real mouse click on a source link (it opens a new tab outside the test pane), and whether a source page changes after 2026-11-06. The checker re-fetches each quote and each link target and fails if either no longer matches.
- After the final rebuild: checker 78 quotes, 78 link targets, 88 ledger rows, 0 problems.
- Re-check after the seventh layer and the Cursor label, 2026-11-06, built-in browser: 375px wide, scroll width 375, no console errors. Dark emulated: background rgb(21, 20, 15), text rgb(236, 231, 219). The Cursor evidence rows show the search label. Not tested: a real mouse click on every source link, and any of the controls in a real tenant.
- No `localStorage` is used.
