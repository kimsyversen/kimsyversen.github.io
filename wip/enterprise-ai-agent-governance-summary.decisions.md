# Decisions: Enterprise AI agent governance, summary

Belongs to: [enterprise-ai-agent-governance-summary.html](enterprise-ai-agent-governance-summary.html)

## 2026-11-06

**D1. One new page, the long page stays as it is.** Why: the user asked to copy the page and make a single short page. Readers who need detail follow links to the long page.

**D2. Reuse the 2.4 figure and the five-points figure unchanged.** Why: the user named these two figures as the picture of what they mean. Only link targets change. The figure text is already in the reviewed-text ledger.

**D3. "Can and cannot" is a route matrix with four content columns: We can, We cannot, Admin work, Evidence.** Why: it answers the user's three needs (what we can do, what we cannot do, what each tool does) in one place. It reuses the matrix layout, which stacks on a phone.

**D4. Each can/cannot cell gives an evidence id (V1, V2 and so on) that opens an exact quote and a source link on the same page.** Why: AGENTS.md rule 3. The reader can check a claim in two clicks. A script confirms each quote appears in the saved source text.

**D5. Claims without a quote are labelled.** `[unverified]` where no source shows it, `[inference]` where it follows from sources, `tenant test` where only a pilot can tell. Why: the user said all information must be correct.

**D6. Preview features are named as preview in the matrix.** Agent 365 Tools Gateway, Agent 365 BYO, Foundry approved-tools policy, Global Secure Access MCP firewall. Why: scope and behavior can change.

**D7. The page does not claim automation that no source documents.** The automation table separates "documented" from "our own pipeline (recommendation)". Why: pushing the approved list to Agent 365 allow or block by pipeline has no source.

**D8. (Superseded by D13.) Gaps section reuses the long page's ten gaps.** Why: they are already checked. A short page must not hide bad news.

**D9. Label checker takes a page path.** Why: the same rules apply to the new page, and one script is easier to keep correct than two.

**D10. No localStorage keys.** The page only needs the detail toggle, which does not save state. If saving is added later, use the prefix `ags-`.

**D11. Evidence ids are keyed, not typed by hand.** `scripts/governance_evidence.py` holds the quotes (46 after D18) and their sources. The build script and `scripts/check-evidence-quotes.py` both read it, so the page, the ids and the check cannot drift apart. Why: a typed id could point at the wrong quote.

**D12. The page has its own tools table, E7 note and watchlist.** It does not copy the long page's. Why: the long page's versions carry price and licence claims that this page cannot back with a quote (the Microsoft price page returned HTTP 403 to the checker). The E7 note keeps only what two quotes show and links to the long page for prices.

**D13. Gaps are rewritten, not copied.** Seven gaps that matter for MCP governance, each with evidence ids or a label, plus one line linking to the long page's other gaps. Supersedes D8. Why: the long page's gaps are written without evidence ids.

**D14. The sentence "Microsoft recommends this for agent policies." is dropped from the nine-rules table.** Why: no source was found for it. The long page is unchanged.

**D15. A network MCP firewall row is added to the route table.** It is not in the 2.4 figure. The page says so under the table. Why: the user asked what each tool does, and the firewall is part of the Microsoft stack. It is preview, remote servers only.

**D16. Gateway "We can" says "create MCP servers in API Management", not "register for Agent 365".** Why: V26 covers creating servers in API Management only. Found while reading the built page.

**D17. Allow or block by pipeline is labelled unverified for the gateway, BYO, Copilot Studio and the firewall.** Why: no source read shows an API or file that sets it. A person does it until a source says otherwise.

**D18. Verification pass on every unverified or inferred label (2026-11-06).** Added V37 to V46 at the end of the list so V1 to V36 keep their ids. Why: the user asked to attempt to verify what is unverified. E7 pricing was left out on purpose.

**D19. Resolved with a quote:** BYO registration by command line (V42), Copilot Studio data policy by PowerShell (V43), API Center to Foundry catalog (V44), Conditional Access in E7 (V45), Intune in bundles (V46), gateway block path and limits (V37 to V39). **Still labelled:** pipeline allow or block (gateway, BYO, firewall), new-server default, Foundry runtime blocking, API Center blocking, Foundry catalog as allowlist. Why: searched the pages, no source states them.

**D20. The Direct row claim was reworded, not verified.** "No tool blocks every path" cannot be shown. The page now says the gateway alone does not block direct access, which V40 and V41 state. Why: a negative claim needs a quote, and the narrower claim has one.

**D21. Intune is stated as "bundles such as E3, E5 and E7" (V46).** Why: the Intune price page returned HTTP 403, so a per-bundle line item cannot be quoted.

**D22. Agent Builder row added to the route table, the tools table and the gaps (V47 to V51).** Why: the user asked whether agents built in Agent Builder are covered. They are in the Agent 365 inventory, but the page had no row. The row says Agent Builder has no external-service actions of its own and that the Copilot Studio row applies after a copy. The diagram is unchanged, and the note under the table says the row is not in it.

**D23. "What we need to settle" moved from the top to after the gaps (id `#discuss` unchanged).** The lead, the role routes, the toc order and the part label ("Open decisions") changed to match. The page now opens with how we govern MCP servers. Why: the user said the main focus is governing MCP servers and what to do with them, and the decisions come after the reader has seen the options. The role route "Decision makers" now goes to the open questions at the end.

**D24. Agents Toolkit row added to the route table, the tools table and the gaps (V52 to V57).** Why: the user asked how Agents Toolkit is covered. It was only named inside the V47 quote. The Learn pages say a developer can attach any MCP server to a declarative agent, and an admin can block the plugin. No source says the Git list, the gateway or the firewall applies, so that is labelled unverified. The note under the table now lists the row as a proposed addition.

**D25. Meeting and discussion wording removed.** The "For the meeting" label, the "What we need to settle" heading, the "Discussion" toc item, the meta description and the index text no longer mention a meeting or discussion. The section is now "Open questions" (id `#discuss` unchanged). Why: the user asked to remove references to meetings. The content is unchanged.

**D26. Pilot content removed.** The pilot section (case-search example, six pass criteria), the pilot decision and the tenant-test question are gone. The stop runbook stays, as "Monitor and stop an agent", and the masthead still says no tenant test was run. Why: the user said the page does not need to talk about running a pilot.

**D27. "What E7 gives you" section removed.** The masthead scope no longer names E7. Why: the user said it is assumed E7 is present and price is irrelevant. The firewall and tools-table rows still say what E7 includes, because those facts decide whether a row works. V35 moved from the removed section to the tools-table row, so no quote is left uncited. Ids are unchanged.

**D28. Section headers no longer use Q1, Q2 or big word labels.** The big label beside each title (Q1, Can, Q2, Auto, Ops) is removed and the headers are single-column. Why: the user said not to frame content as questions, and "Can" and "Auto" overlapped their titles. Section ids (`#q1`, `#q2`) are unchanged so saved links keep working. Anchored sections also get a scroll margin so the sticky nav does not cover the title.

**D29. The five points on the target state and the open questions use a compact two-column list.** Number and point on the left, how and link on the right (stacked on a phone). Wording is unchanged, so the reviewed-text list is unchanged. Why: the user asked for the five points to take less space.

**D30. The Answer in "How we govern MCP servers" is now two sentences naming the control per technology.** It replaces the shorter general answer. Why: the user asked for the one-line answer to "how do we block MCP usage and allow only approved servers" to sit there. Each named control has its row and quotes in the route table. The preview and untested caveat is stated in the answer itself.

**D31. A second figure shows MCP traffic paths and splits the end user client from the rest.** It sits below the 2.4 figure, with a seven-row path table (number, path, where, what the sources say, evidence). Left zone is the device: VS Code and GitHub Copilot, the local MCP server, the Global Secure Access client. Right zone is not the client: GitHub settings file, MCP firewall, agents in the cloud, the Agent 365 gateway or registry, remote servers. Red dashed arrows mark gaps: the local server (path 4) and direct calls that skip the gateway (path 6). The figure holds labels only; every claim is in the table with a quote. Cloud placement of Copilot Studio, Foundry and the gateway is inference and says so. The 2.4 figure is unchanged. Why: the user asked to see network traffic limits, where traffic flows, and which parts are the client.

**D32. Local servers can be detected: Defender for Endpoint added (V58 to V65).** Path 4, the local stdio row, the firewall row and the local-servers gap said no tool sees local servers except the GitHub list. That was wrong: Defender discovers supported local agents and their MCP servers on onboarded devices (three Learn pages, updated 2026-11-03). The page now says detection and inventory only, that no source shows blocking (unverified), that Plan 2 is the minimum license and that discovery is not a complete inventory. The generally-available status is stated as generally available except preview scenarios, not as preview. Why: the user pointed out local servers can be detected, then asked that all statements be correct.

**D33. Full read of every claim against its quote (2026-11-06).** Two more wordings fixed. The Agents Toolkit gap said developers can point an agent at "any MCP server URL", which V52 does not say; it now says they can add an MCP server as a plugin. "Only the GitHub list restricts them" became "the one restriction with a source", because "only" cannot be proven. The other claims matched their quotes.

**D34. Cloud agent traffic can pass Global Secure Access (V66 to V69).** Path 6 said the client runs on the device so cloud agent traffic does not pass it. The MCP logging page lists a second configuration: the Copilot Studio integration routes agent traffic through Global Secure Access. Path 2 said the firewall sees traffic "only when" the client is on the device; the firewall page lists the client on a joined device and TLS inspection as prerequisites, so the text now says that. Whether firewall policy applies to Copilot Studio traffic is not shown and is labelled unverified. Defender discovery is stated as commercial cloud only (V69). GitHub "licensed users get it" was dropped (V1 does not say it), the merge and pull request steps are labelled as our process, the gateway row says servers registered with the gateway (V9), and the Agent Builder to Copilot Studio link is labelled inference. Why: the stop check found claims only partly backed by their quotes.

## Tests run 2026-11-06 (local server, in-app browser)

- `check-evidence-quotes.py`: 46 quotes found word for word in their live sources, and all 46 listed on the page. 0 problems (re-run after D18).
- `check-enterprise-agent-labels.py`: new page 252 texts, long page 391 texts, both pass.
- Index: no page missing, no broken link.
- Page: no console errors, no duplicate ids, no `#` link without a target, every long-page link target exists, no paragraph over 60 words, no em or en dash.
- 375px wide: no sideways scroll, matrix rows stack in one column.
- 1200px wide dark mode: dark background and light text, no sideways scroll.
- Real click on evidence link V12: URL hash became `#ev-V12`, row scrolled into view.
- Expand all detail button: opens the details block, label changes to "Collapse all detail".

Re-run after D18 (same day): 46 of 46 quotes found and listed, label checker passes on the new page (252 texts), index scripts clean, no console errors, no dashes, no duplicate ids, no broken `#` links. At 375px wide there is no sideways scroll. Dark mode at 1200px is correct. A real click on V44 set the hash `#ev-V44` and scrolled the row into view. The V44 source link carries a text fragment built from the quote.

Re-run after D22: 51 of 51 quotes found and listed, both label checks pass (253 and 391 texts), no console errors, no duplicate ids, no sideways scroll at 375px. A real click on V50 set the hash `#ev-V50`.

Not tested: text-fragment highlighting on the vendor pages (the links are built from the quote text; the pane could not show the highlight), light mode at 375px by eye, and every toc link by click. Link targets were checked by script.

Re-run after D23: 51 of 51 quotes found and listed, both label checks pass (253 and 391 texts), index scripts clean, no dashes.

Re-run after D24: 57 of 57 quotes found and listed, label checker passes (254 texts), no dashes.

Re-run after D26 and D27: 57 of 57 quotes found and listed, both label checks pass (232 and 391 texts), index scripts clean, no dashes. Browser check: no console errors, no duplicate ids, no broken # links, no sideways scroll at 375px, dark mode correct, real click on V35 set #ev-V35 and scrolled the row into view. Nothing tested in a real tenant.

Re-run after D28 and D29: 57 of 57 quotes, both label checks pass (232 and 391 texts), no dashes. Checked at 1000px wide and at 375px wide: no sideways scroll, no console errors, headers aligned, five points two-column on desktop and stacked on phone. Light mode at 375px not checked by eye.

Re-run after D31: 57 of 57 quotes, both label checks pass (258 and 391 texts), index scripts clean, no dashes, no duplicate ids (the new figure reuses the arrow markers of the 2.4 figure), no broken # links. Browser: figure and table correct in light and dark, no sideways page scroll at 375px (figure and table scroll inside their own box), no console errors, real click on V41 in path 6 set #ev-V41 and scrolled the row into view. Not tested: text-fragment highlight on vendor pages, anything in a real tenant.

Re-run after D32 and D33: 65 of 65 quotes found and listed, both label checks pass (258 and 391 texts), no dashes, no duplicate ids, no broken # links. Browser: no console errors, no sideways scroll at 375px, path 4 renders correctly, a real click on V58 set #ev-V58 and scrolled the row into view. Nothing tested in a real tenant or on a device.

Re-run after D34: 69 of 69 quotes found and listed, both label checks pass (258 and 391 texts).

## D35. Final statement pass (2026-11-06)

Read every statement in the built page text against its quote or label. Three wordings went beyond their quotes and were fixed: "connect the gateway once" (V12 does not say once), "none after linking" for API Center sync (V28 says sync is continuous, not that linking needs no work), and "automatic once API Management is linked". They now say a person links the two first, labelled inference, and sync is then continuous (V28).

Reused long-page blocks (risk tiers, action policy, checklist, nine rules, target-state figure, runbook) hold design choices, not product facts, and keep the recommendation label. The nine rules say "All are recommendations". The Conditional Access report-only and environment group rules were confirmed on the long page's fact check (rows 117 and 61).

Defender prerequisites on the page are only the ones quoted (V58 to V63, V69). Supported OS and minimum Defender versions are not stated on the page, so nothing there needs a quote.

Re-run: 69 of 69 quotes, both label checks pass (258 and 391 texts), no dashes.

## D36. Defender requirements quoted (2026-11-06)

The Defender prerequisites were re-read on the Learn page (last updated 2026-11-03). The page now states them with quotes V70 to V72: a supported Windows or macOS version, Defender Antivirus platform 4.18.26090.9 or later on Windows, Defender for Endpoint 101.26072.0017 or later on macOS. They sit in their own gap item, "Defender discovery needs", so the Local servers item stays under 60 words. The Plan 2, commercial cloud, active mode and incomplete inventory claims moved there too.

Question from the owner: can Intune block local MCP servers? Answer given in chat, page not changed. Found: no Intune setting for it. Defender AI agent runtime protection (public preview, page updated 2026-10-09) blocks agent actions on prompt injection, not unapproved MCP servers. Intune can deploy its settings. Our wording "no source shows it blocking a server" stays true.

Re-run: 72 of 72 quotes, label check 258 texts, no dashes, no duplicate ids, no broken # links.

## D37. Last pass on the reused blocks (2026-11-06)

Went through every sentence in the reused blocks and sorted each as a product fact or a design choice. Design choices (risk tiers, action policy, checklist, runbook, target-state figure, seven of the nine rules) are recommendations by nature, so no source can confirm them. The page labels them recommendation or "All are recommendations".

Two rules rest on a product fact and now have quotes: report-only mode (V73, Conditional Access report-only page, updated 2026-06-01) and environment group rules (V74, environment groups page, updated 2025-12-16). The long page's unsourced "Microsoft recommends this for agent policies" stays removed (see the RULES replace in the build script).

Copilot Studio traffic through Global Secure Access: still no source on whether firewall policy applies. The page says so (unverified). That is a finding, not a gap in the check.

Re-run: 74 of 74 quotes, label check 258 texts, no dashes.

## D38. Firewall per-server tool control, and the two open items (2026-11-06)

The firewall page also lists allow or block for Tools, Resources and Prompt templates per server (V75). The page only said URL patterns, which understated the control. Added to the firewall "We can" cell.

Searched the saved Defender pages and the Global Secure Access firewall and logging pages again for (a) Defender blocking a local MCP server and (b) firewall policy on Copilot Studio traffic. (a) No page says it blocks a server. (b) The firewall page never mentions Copilot Studio; the logging page says only that traffic routes through Global Secure Access. Both stay unverified. This is a finding: Microsoft's pages do not say.

Re-run: 75 of 75 quotes, label check 258 texts, no dashes.

## D39. Copilot Studio traffic and the MCP firewall (2026-11-06)

Read the Power Platform page on Global Secure Access for agents. It says forwarded traffic includes custom MCP servers and lists three filtering types (V76, V77). It does not mention the MCP firewall. Path 6 now says what the page states and keeps the firewall question unverified. Not tested in a tenant.

## D40. Copilot Studio and the MCP firewall: unverified to inference (2026-11-06)

(Supersedes the 'stays unverified' part of D39.) The firewall page enforces through a Conditional Access policy (V78). The Entra Copilot Studio page says profiles linked to Conditional Access are not supported for Copilot Studio agents (V79) and uses the baseline profile (V80). Path 6 now says no source shows the firewall applying and that it most likely does not. Labelled inference. Not tested in a tenant.

## D41. Defender local server blocking, searched again (2026-11-06)

Read the Defender what is new page. It lists local AI agent discovery (GA) and runtime protection (preview) that blocks risky activity such as prompt injection and unsafe agent actions. No wording says it blocks an unapproved MCP server. The page keeps "no source shows it blocking a server", labelled unverified. No page change.

## D42. Say what kind of claim each is (2026-11-06)

Added a "Kinds of claim" line to the masthead: product facts carry a quote, the reused blocks are our design choices that no source can confirm, gaps are labelled unverified. The goal "all statements correct" cannot be met for the two source-silent items, so the page now says so up front instead of leaving it to the labels.

## D43. Intune firewall allow list built from the approved Git list (2026-11-06)

Added a matrix row "Intune firewall allow list", an automation row and a gap item. The idea comes from the user: block unapproved remote MCP servers on managed devices with an allow list that a pipeline generates from the approved server list in GitHub.

What the sources show (V81 to V88): Intune firewall default blocks every outbound connection that matches no rule (Windows 1809 and later); Windows Firewall dynamic keywords can allow by domain name and are usable through the Firewall CSP with Intune; domain rules need a DNS lookup and fail behind a proxy, with secure DNS, some VPN tunnels and cached addresses; Microsoft calls the block-all default fit for certain highly secure environments; the Graph API creates configuration policies.

What no source shows: that Git feeds Intune, and that the Graph configuration policy API can write firewall dynamic keywords. Both are our design and labelled recommendation or unverified. Nothing was tested in a tenant.

Main limit stated on the page: the default blocks all outbound traffic that matches no rule, not only MCP. It is not MCP-aware, covers Windows only, and covers managed devices only. Defender custom indicators are a block list, not an allow list, so they were not used. No macOS source was read, so macOS is not claimed.

