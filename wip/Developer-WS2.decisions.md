# Decisions: Developer-WS2

Belongs to: [Developer-WS2.html](Developer-WS2.html)

## D1. Intune delivers, the client enforces

Chosen: say plainly that Intune has no MCP policy and use it as the delivery and drift channel for each client's own policy. Why: no Intune page checked on 2026-11-06 names an MCP setting, while Anthropic, VS Code, Cursor and the Claude Desktop help page each name Intune as a delivery route. The absence is an `[inference]`, not a quote.

## D2. One table per client, not one generic recipe

Chosen: a row per client (Claude Code, VS Code, GitHub Copilot, Codex, Claude Desktop, Cursor). Why: the keys, paths and strength of control differ a lot. A generic "deploy a file" answer would be wrong for VS Code (ADMX) and Cursor (dashboard allowlist).

## D3. Cursor is a split control

Chosen: MDM enforces the allowed team ID. The MCP allowlist is set in the team dashboard (Enterprise only). The MDM file `~/.cursor/permissions.json` sets what runs without approval, which is not a block. Why: that is what the Cursor pages say. Claiming an MDM MCP block would have no source.

## D4. Claims carry evidence chips, everything else is a requirement or label

Chosen: follow rule 3 of AGENTS.md. Claim text ends in chips (V1, V2) that link to the evidence table. All other text is listed in the ledger with a verdict. Why: the script can then fail on fact-style wording in unreviewed text.

## D5. Quotes with dashes are not used

Chosen: skip any quote with an en or em dash. Why: the page may not contain those characters and quotes must appear word for word.

## D6. Reuse of wip and governance work

Chosen: reuse the verified Defender, Global Secure Access, Intune firewall and dynamic keyword quotes from `scripts/governance_evidence.py` instead of fetching new ones. Why: same day check, same wording, less to go wrong. The pages in wip are not linked, since they are not published as pages on master.

## D7. Scope

Chosen: Windows and macOS. Linux is out because Intune Linux has no checked MCP path. Why: nothing to cite.

## D8. Gaps stay on the page

Chosen: name the gaps (local stdio servers in clients without managed policy, the Git to Intune pipeline, nothing tested in a tenant) as labelled items. Why: AGENTS.md says an untested system is a finding, not a weakness.

## D9. GitHub "about an hour" is not an MDM refresh time

Chosen: the page says the one hour figure applies to server-managed settings, and that no refresh time was found for MDM-managed settings (`[unverified]`). Why: the first draft put the figure on the MDM row, which the GitHub page does not say.

## D10. Long strings wrap on phones

Chosen: `overflow-wrap:anywhere` on text blocks. Why: on 2026-11-06 a 375px test showed 10px of sideways scroll from paths such as `%ProgramData%\OpenAI\Codex\requirements.toml`.

## D11. Wording follows the quote, not the other way round

Chosen: after reading each claim beside its quotes on 2026-11-06, four claims were cut back to what the quote says (Claude Code "fleet deployment", "turns MCP off", and the script type for the PowerShell and macOS rows). Why: the checker proves a quote exists, not that the claim reads it correctly.

## D12. Local servers in unmanaged clients get a detection requirement

Chosen: keep the gap on the page and add a requirement that a script reads such a client's MCP file and flags unapproved servers. Why: nothing sourced can block them, but the sourced delivery paths (custom compliance, remediations) can run a check. It is a design requirement, and it detects only.

## D13. Block-spanning quotes link to the longest single-block piece

Chosen: 15 of the 70 quotes cross table cells or code lines on their source page. For those, the link's text fragment points at the longest piece that sits inside one block (`BLOCK_FRAGS` in `scripts/developer_ws2_evidence.py`). The evidence table still shows the full quote. Why: a browser cannot highlight a text fragment that crosses a block boundary, so the first build's links for those quotes opened the page without a highlight. The checker now fails when a link target is not inside one block of its source.

## D14. App Control for Business is the sixth layer

Chosen: add a Windows layer using Intune App Control for Business (Microsoft Learn, read 2026-11-06). It can allow only approved clients to run, so a client with no managed MCP policy can be kept off Windows devices. It can also stop a local server that is its own program file. Why: the first build had no layer for local servers, and this is the one sourced Intune control that restricts what runs. Its use for MCP is `[inference]`, because the pages do not mention MCP. Limits kept on the page: a script run by an allowed node or python is not stopped, and no macOS equivalent was found. The new quotes are added after the old ones so earlier V numbers keep their numbers (V71 to V73).

## D15. (Superseded by D16.) Three fragments were shortened

Chosen at the time: shorten the fragments of V28, V33 and V35. This was reported as fixed, but the V33 and V35 re-check was not done by looking at the final screenshots. See D16.

## D16. Link test redone one by one, Cursor links get a search label

Chosen: on 2026-11-06 open all 76 source links one at a time, each in a fresh foreground tab, and view a screenshot of every link that did not scroll. Result: V13, V22 to V25, V39 and V57 show the highlight. The five Cursor links (V33 to V37) show no highlight and no scroll, because cursor.com ignores text fragments on a fresh load. The Cursor evidence rows now carry the label "Open the page, then search for the quote." Why: the claim must be checkable in a few clicks, and a link that cannot highlight needs to say so. A window scroll is only a proxy, since some sites scroll an inner pane. The fragments for V28, V33 and V35 stay shortened (D13).

## D17. macOS gets a file hash list layer, the gap stays on the page

Chosen: add a seventh layer, Defender file indicators on macOS (V74 to V76: macOS support, block stops read, write and execute, three file types). Why: App Control covers only Windows, and a hash list is the one sourced macOS control that stops a file running. It is a deny list and its use for MCP is `[inference]`. Not solved, and said so on the page: a local server that an allowed interpreter runs from a script file, and a macOS local server not on the list, are stopped by no layer here. Only the detection script covers them. An argument (`[inference]`) narrows the gap to clients the page does not manage, because a managed client refuses servers not on its allowlist. Nothing was tested in a tenant.

## D18. Script hosts, the one Windows lever, and no macOS allowlist

Chosen: add the Microsoft Learn script enforcement page as a source (V77, V78, read 2026-11-02). It says App Control does not control scripts run through an unenlightened script host, and that allowing such a host allows all its scripts. The page now says the one lever is to leave node and python out of the Windows App Control policy, at the price of stopping approved servers that need them, and the rollout steps ask for a per group choice. Whether node or python is unenlightened is not on a Microsoft page, so it is `[inference]`. A search on 2026-11-06 found no Microsoft macOS control that allows only approved executables, so the macOS gap stays. Why: the earlier page described the gap without the sourced reason for it. Still not solved, and the page says so.

## D19. Link test method, results, labels

Chosen: all 78 links were opened one at a time and a screenshot of each was viewed. Method notes: the capture clip must start at the visual viewport page offset, or scrolled pages come out black (the first set, now discarded). Parallel background tabs do not scroll. Result: 66 show the highlight, 12 do not (V28 to V32, V33 to V37, V40, V41). Those 12 carry the label "The highlight may not show on this site. Search the page for the quote." V77 used a range fragment that started at "App Control" and lit the page title, so its fragment is now the single block piece starting at "scripts run through" (BLOCK_FRAGS). Why: a link that does not do what a reader expects must say so. Cause found afterwards: with page scripts off all 12 links scroll and highlight, so the fragments are right and the sites' own scripts remove the highlight (Cursor also the scroll). Nothing in our link can prevent that, so the label stays.

## D20. The design is stated up front as a requirement

Chosen: the answer section opens with one requirement: only approved clients run, each approved client has a managed server list, and Intune delivers both and puts them back. Why: this is the closed-client design that the rest of the page supports with quotes. It is a design requirement, not a tested result. The hook asked for a fully solved case twice. What is blocked is a test in a real tenant (no tenant access here) and a Microsoft control that allows only approved executables on macOS or stops scripts under an allowed interpreter on Windows (none found, searched 2026-11-06). Neither was invented.

## D21. The page is cut to GitHub Copilot in VS Code

Chosen: on 2026-11-06 the owner said the only MCP client in use is GitHub Copilot in VS Code, and agreed to cut the page to that case. The page now has one client section (VS Code on Windows, VS Code on macOS, GitHub Copilot's own policy). Claude Code, Codex, Claude Desktop and Cursor were removed with their quotes. The PowerShell, macOS shell script and Win32 rows were removed, because they were carriers for managed files that VS Code does not need (VS Code uses ADMX on Windows and a profile on macOS). The seven layers stay. App Control and the macOS hash list now serve one purpose: keep any other MCP client off the laptop. Why: a shorter page has fewer claims to keep true, and the old gaps only matter if a second client is present. Quote numbers were reassigned in the cut (the page is not published, so no link depends on them).

The macOS route was checked: the official VS Code policy page says each release from 1.99 ships a sample `.mobileconfig`, and lists Intune for deploying profiles at scale. The page quotes both. Still `[unverified]`: that the macOS profile holds the three MCP policies, and its key names (the sample file was not opened). A vendor guide (JFrog) claims the allowlist can be sent as a macOS profile, but it is a vendor source and is not used.

The minimum VS Code versions (1.130 allow and deny, 1.132 managed-only) appear only in the page source, not in the rendered text the checker reads. The page does not state them. It has a requirement to check the version on the policy reference page.

Still true: nothing tested in a real tenant, and the two local-server gaps (allowed interpreter on Windows, macOS not on the deny list) are not solved.
