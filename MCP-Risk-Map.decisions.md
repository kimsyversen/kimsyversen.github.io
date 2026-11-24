Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html). Other notes for the same page: [plan](MCP-Risk-Map.plan.md), [fact check](MCP-Risk-Map.factcheck.md).

# Decisions: MCP risk map (MCP-Risk-Map.html), 2 Nov 2026

Working notes.

- Eight risks, not ten plus seven. The user asked for low detail. Every risk maps to at least one OWASP MCP Top 10 entry or a section of the MCP specification.
- Dropped the "More risks" tables, the attack-path filter, the persona review tab and the incident-response section. They add detail and are not MCP-specific.
- Kept the diagram, popovers, status tracker, "Where to start" table, evidence and sources, so the page works like Developer-WS.html.
- Removed the "sandbox if enabled" box from the diagram. Claude Code runs local MCP servers outside its sandbox while VS Code can sandbox stdio servers, so one box would be wrong for one of them. The spec only says clients should sandbox servers; M03 says that.
- (Superseded by the 5 November review.) Only one MCP-specific attack is cited (Mitiga, May 2026). Anthropic called it out of scope and by design; Mitiga disagrees. Both positions are on the page. Other risks are described as OWASP categories or spec warnings with no incident cited.
- (Superseded by the 5 November review.) Did not state the values of the VS Code chat.mcp.access setting. Docs and source disagree (see Developer-WS.html). Only the policy names are used.
- Plugin4Shell excluded: Cloud Security Alliance does not name MCP as the affected component.
- Friction estimates and the risk order are interpretation by AI and are tagged [inference].
- Storage keys are mcp-tab and mcp-status. Both pages share one origin, so the old dev-* keys would mix state.
- Made the page easier for people new to MCP security: added a "How MCP works" box, a glossary, a plain-words line per risk, and moved vendor setting names into a collapsed "How to set it". Why: the user asked whether the page suits learners, and the original assumed prior knowledge.
- Added a separate "VS Code" tab and left the general risks as they were. Why: the user wanted VS Code as the base case, then chose to keep the general content and add a section. Each row names the risk it touches. The table stacks into cards under 680px so it does not scroll sideways.

## Diagram checks

- After changes to diagram navigation, test each filter, open every highlighted box or marker, and follow every popup link. Check that each control opens the expected popup or checklist and each source link loads. Use real clicks for a sample.
- Open shared links such as `#risks` directly and check that they restore the selected tab. Record the checks and any gaps here or in the fact check.

## 3 Nov 2026, "Made with AI" note

- **Plain label and one sentence at the end of the footer**, under a hairline rule, in the page's own muted and ink colours. Chose this over a pill or badge to keep it quiet and avoid the template look. Colours use the page tokens, so dark mode follows.
- **Wording:** "This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human." Same text on all five pages.
- **Layout:** label and text in two columns on desktop, stacked under 560 px.

## 5 November 2026, statement review

- Checked static prose, glossary, every VS Code row, and JavaScript-generated popovers, first controls, evidence and sources. Rechecked original claims rather than accepting the old ledger's OK verdicts.
- Qualified process privileges, host/client terminology, token semantics and data flows. MCP does not require every result to enter a model context or leave a laptop.
- Added Claude Code managed-file, allowlist and SDK exceptions. An empty managed server map does not disable all MCP surfaces. A URL-only allowlist blocks unmatched stdio servers within its scope, so it is not inherently an allowlist bypass.
- Retained Mitiga as attributed research. Removed the unsupported separate refresh-token capture claim. Kept its reported vendor response as a second-hand account. Added the persistence removal needed for remediation.
- Restricted OAuth HTTP exceptions to development loopback and SSRF advice to its documented discovery/deployment scope. Added redirect validation.
- Distinguished editor MCP sandboxing from the Copilot harness sandbox and included Windows support only for the latter. Retained the verified Claude/Codex harness restriction and added policy gaps for independently discovered Copilot servers.
- Exact command matching is configuration matching, not proof of safe executable or dependency contents. Structured Codex matching still excludes cwd and environment variables.
- Removed unused filter descriptions that referred to ten risks; the page has eight.
- Preserved public paths, tab and component ids, localStorage keys and the shared Made with AI note. Updated the index date in the same change.

## 8 Nov 2026, Microsoft ecosystem scope toggle

- **One page, one toggle.** The user wants one risk map with a General and a Microsoft ecosystem view, not two pages. A segmented control under the header sets `data-scope` on `html`. Reason: the tab ids, risk ids and shared layout stay the same, so existing links keep working.
- **Same eight risks, different content.** The Microsoft view keeps M01 to M08 so the OWASP mapping and the status tracker line up. What changes is the text, controls, diagram labels, start table, evidence and sources. Reason: a different risk list would break comparison between the two views.
- **Separate status per scope.** `mcp-status` stays General. `mcp-status-ms` holds the Microsoft view. Reason: a status such as "In place" for a Claude Code control says nothing about a Visual Studio control.
- **Hash.** `#risks&s=ms` or `#risks&s=g`. A hash value wins over the stored `mcp-scope`. Old `#risks` links still open and use the stored scope. Tab ids are unchanged.
- **The `vscode` tab id stays.** The label becomes "3 · VS Code and Microsoft" in the Microsoft view. The 13 VS Code rows remain. A new table "Other Microsoft surfaces" sits under them. Reason: renaming the id would break shared links.
- **Diagram.** Same component ids, new labels for the Microsoft view, plus one new box `gw` (MCP gateway or firewall) in the Outbound zone. Zones and arrows are shared. Reason: the data flow is the same, the products at each point differ.
- **Per-claim evidence for the Microsoft view.** Each Microsoft placement and each new table row carries the exact quote and a link that opens the page at that passage (text fragment). Reason: the repo rule says a diagram claim must be verifiable from the diagram itself. The check script fetches each source and confirms the quote word for word.
- **Known gap.** The General popups still list sources per box, not per claim. Not changed in this task. Logged here so it is not forgotten.
- **Mitiga in the Microsoft view.** The Mitiga research targets Claude Code, which is outside this scope. The Microsoft M05 text describes the same mechanism (a changed config redirecting a server) only where a Microsoft source supports it (Visual Studio re-trust on a changed URL or command, VS Code trusted-workspace behaviour). It says no demonstration against a Microsoft product was found. "Not observed."
- **CVEs.** CVE-2026-26118 and CVE-2026-32211 are shown as vendor advisories from the CVE record, not as observed incidents. CVE-2026-32211 lists "Azure Web Apps" as the affected product; the page says so. Invariant Labs is labelled third-party research.
- **Preview features are labelled preview** where the source says so (Windows ODR, Entra MCP firewall and logging, Agent 365 gateway and BYO, GitHub registry enforcement).
- **Not claimed:** a Copilot Studio per-tool approval flow. No such statement was found in the sources read.
- **Per-item evidence (mechanism).** Each Microsoft card item, table row, diagram placement and callout carries quote ids. `qBlock` renders them as a collapsed list with a text-fragment link. Reason: AGENTS.md rule 3, the reader checks each claim from the diagram itself.
- **`MSDATA` is the source of truth.** It is one JSON line in the page. The builder script that produced it is not shipped. Reason: the page is hand-written with no build step. Edit the line, then run the check script.
- **Whitespace fallback.** The check first matches a quote word for word. If that fails it matches with whitespace ignored and prints a note. Only `cs3` needs it, because the source page lists a bold label and its colon as separate elements. `sp5` was shortened to drop a trailing period for the same reason.
- **Start table (Microsoft view) holds recommendations.** They are design requirements, so they carry no quote. Friction labels stay interpretation by AI, tagged in the Sources tab.
- **One placement row per (risk, component) pair.** 33 rows. Reason: a popup lists each risk once per box, with its own quotes.
- **Callouts** pair a scope statement with its date and quote, so a preview or prerelease label is never separated from its source.
- **CVE sources have two URLs.** `u` is the human link, `f` is the CVE JSON used by the check. Reason: the MSRC page cannot be fetched. Text fragments are skipped for CVE links.
- **M01 check 3 is General only** (`sc-g`). It describes a Claude Code exception that has no Microsoft counterpart.
- **Mitiga quote `mi1` added** so the sentence about the research has a source in the Microsoft view too.
- **Fragment links avoid words with an apostrophe or quote mark.** A curly apostrophe in the source breaks a text fragment. Every fragment start and end string was checked against the fetched page text on 8 Nov 2026 (104 parts, all found after the `sp5` fix).
- **Fact-style check is narrow.** It flags product verbs (supports, blocks, enforces, requires, prevents, provides, inspects, discovers, always, never, automatically) and "is/are available, supported, enabled..." in text with no evidence list. The first version flagged any "is" or "are" and hit process statements, so it was narrowed. The 103 texts in the reviewed list each have a verdict (label, requirement or code token). A pass proves a verdict was recorded for the exact wording, not that the verdict is right.

### Test log, 8 Nov 2026
- `python3 -I scripts/check-mcp-risk-map.py <cache>`: 69 quotes found, 103 reviewed texts, 0 problems.
- Light, dark and 375 px, both scopes: no sideways scroll (`scrollWidth` 375 on all five tabs), no console errors.
- Real mouse clicks: a diagram marker, an "Also in" link, the scope toggle, and in dark mode the MCP gateway box (popup shows quotes and links). Scripted pass over every marker and box in both scopes: every popup link opened the right box and kept the right hash.
- Saved state: `#map&s=ms` and an old `#map` link both restore correctly. Status for the two scopes is stored separately.
- Not done: a real click on every box under every filter. The scripted pass covers them, real clicks cover a sample.
- Not tested: any setting or command on a managed machine.

## 8 Nov 2026, design principles applied to the Microsoft start table
- New rule 6 in AGENTS.md: least administration overhead, keep it simple, do not rely on preview features.
- **Start table changed (Microsoft view).** M06 now says prefer OAuth 2.0 over API keys and keep tokens out of mcp.json, and add API Management only for remote servers you host yourself. Reason: API Management is a whole service to run. M07 now says bind local HTTP servers to 127.0.0.1, check the Origin header, and allow remote servers only from the approved list in M01. Reason: the Entra MCP firewall is in preview. M08 dropped Defender advanced hunting for Agent 365 BYO servers (preview). It keeps OpenTelemetry export and the approved list.
- **Risk card checks changed.** M01 check 3 now says not to rely on the Agent 365 tools gateway, which is in preview. M07 check 1 asks about localhost binding and the Origin header instead of the Entra firewall. M06 check 1 applies only when servers sit behind API Management.
- **Preview features stay on the page, labelled.** Cards, popups, the Other Microsoft surfaces table and the Preview callout still describe them, because a reader may meet them. None is in the start table. The page says so.
- Not changed: M01 (the GitHub enterprise allowlist, not marked preview in the source page read), M02 to M05. Not checked: whether the GitHub allowlist moves to preview later. Recheck before moving "Current as of".
- Check script: 69 quotes found, 104 reviewed texts, 0 problems.


## 9 November 2026, complete source review

- General diagram markers now use the same quotation rendering as Microsoft markers. Both sets are included in the quotation checker. Detailed controls stay in the risk cards; marker prose is limited to the evidence attached to it.
- Trust and isolation claims name their product scope and bypass conditions. Source-matching quotations alone did not establish unconditional enforcement.
- Research demonstrations name the demonstrated client. A vendor CVE record is not treated as proof of a victim incident, and one article cannot establish that no other demonstration exists.
- The current fact-check inventory supersedes prior source mappings and wording. Historical reviews remain clearly labelled. Both cs3 and cxcmd need whitespace-insensitive quote matching; this supersedes the earlier claim that only cs3 needs it.

## 9 November 2026, framework selector and CoSAI

- **Three choices: All, OWASP MCP Top 10, CoSAI.** A risk shows when at least one entry of the chosen framework maps to it. Default is All, so existing links and saved state look the same as before except for the new risks.
- **Twelve risks, not eight.** CoSAI has threats that M01 to M08 did not hold: approval prompts and trust in the model (#7, #9, #13), shared tenants (#10), runaway cost and payload limits (#14, #33), and unprotected transport or message integrity (#12, #23, #27, #28). They became M09 to M12. Existing ids M01 to M08 are unchanged.
- **One home per framework entry.** Each of the 34 CoSAI threats and 10 OWASP entries has exactly one home risk, plus an optional "also" list. Reason: the page rule is mutually exclusive, collectively exhaustive, one authoritative home per fact.
- **M07 has no OWASP entry.** The OWASP list has no DNS rebinding, CSRF or SSRF item. M07 stays under CoSAI (#26, #29, #30) and the MCP specification. Under the OWASP view M07 is hidden and the mapping table says why.
- **M03 and OWASP MCP05 is a partial match.** MCP05 is about commands built from untrusted input. M03 is about a local server's start command. Both are arbitrary command execution. The mapping table says "partial" and tags it [inference].
- **Mapping is interpretation by AI.** Tagged [inference]. The framework titles and ids are quoted from the sources.
- **CoSAI paper quirks recorded.** Threat 4 cites "Prompt Injection (#12)" but the list numbers it #11. The page uses the list number. The paper is a draft.
- **Microsoft view and M09 to M12.** The cards and placements are product neutral (CoSAI and the MCP specification). Microsoft sources were not assessed against them (21 Nov 2026: the old wording "no Microsoft source was reviewed" was false, because the Azure MCP Server and Entra MCP firewall pages touch M10 to M12), so each card says "Not assessed in this view".
- **Placement fixes (general view).** M05 reuse of the stolen token moved from the local HTTP server to remote MCP servers, and a localhost-proxy row added at the local HTTP server. M06 confused-deputy row moved from "SaaS and cloud APIs" to "Remote MCP servers" and merged with the token row. M07 agent row no longer points to itself. M04 gets a row at the AI agent from the CoSAI definition. Reason: each row must sit where the quoted source says the control or the failure happens.
- **"top 10 risks" wording removed** from diagram box labels. The page now has twelve risks, not a top 10.
- **Counts are computed**, not typed, so the selector cannot leave a wrong number on the page.
- **CoSAI status wording.** The paper says "Draft" on pp. 2 and 5 and "Governing Board approval" on p. 4. The page calls it a draft and does not say the Governing Board approved it. Both quotes are in the ledger.
- **CoSAI category table quirk.** The category table labels #8 differently from the threat list. The page uses the threat list names and numbers (same rule as the #12 vs #11 quirk).
- **Saved choice order.** A `&f=` in the link wins. Without it the page uses `mcp-framework` from local storage, then All. A deep link to a card hidden by the current choice (for example `#risk-m09` under OWASP) switches the choice to All so the card opens.
- **Dead code left in.** Old helpers (`isX`, `MOREBY`, `openMoreRow`, `moreRows`) are unused and harmless. Not removed, to keep the change scoped.

## 9 November 2026, tab 1 order
- **Risk map first.** On the Risk map tab the order is now: Risk map of MCP, Risk by zone, Before you use the map, then How MCP works, In short and Words used on this page. Reason: the reader asked for the map at the top and the background at the bottom. Section ids and anchors are unchanged.
- **Map intro paragraph removed** (owner's request, 9 Nov 2026). The Risk map of MCP section now starts with the chips. The ledger rows are marked REMOVED.
- **How-to-use hints removed** (owner's request, 9 Nov 2026): "Pick a risk above, or select a marker or box in the diagram." (diagram summary line), "Select a marker or a box to see its risks." (caption), "Select a risk to show it in the diagram." (zone table intro) and the narrow-screen note "The diagram is wide. Drag sideways in it, or use the table below." The `.hint` CSS is left unused.
- **No "framework" on the page** (owner's note, 9 Nov 2026). OWASP MCP Top 10 is a beta list and the CoSAI paper is a draft, so neither is a framework. The page now says "Risk list" (selector, header line, mapping table column and heading text, copied status text). The ids `framework-mapping` and the `mcp-framework` storage key and `&f=` hash key are unchanged, because public links and saved settings must keep working. Older notes in this file and the ledger still say "framework" where they describe history.
- **Page column as wide as the diagram** (owner's request, 9 Nov 2026). `.wrap` max width went from 48rem to 1260px plus gutters, and the diagram figure no longer breaks out of the column. Every section, table and card now has the diagram's width (1260 px at a 1440 px window). Long paragraphs have longer lines on wide screens. Narrow screens are unchanged (no sideways scroll at 375 px on all five tabs).
- **Default diagram summary removed** (owner's request, 9 Nov 2026): the "Most risks meet in: ..." line. The line under the chips is now empty and hidden until a risk or a box is selected, then it shows that selection's summary. Side effect: selecting adds one line above the diagram.
- **"Before you use the map" section removed** (owner's request, 9 Nov 2026), both paragraphs and the heading. The anchor `#before-you-use-the-map` no longer exists on this page (AGENTS.md says never change an id; the owner asked for the text to go, and a heading with no text under it would be empty). The tab order in the entry above is now: Risk map of MCP, Risk by zone, How MCP works, In short, Words used. The statement that placement is interpretation by AI remains on the Risks tab (mapping table and grouping, tagged [inference]).
- **Diagram description caption removed** (owner's request, 9 Nov 2026): "Servers, packages, config and content (1) reach the workstation (2) ..." in both the General and the Microsoft version. The caption still holds "Arrows show selected paths, not every data flow." and the legend. The zone numbers 1 to 4 stay visible in the diagram and in the Risk by zone table headers.
- **Background sections removed** (owner's request, 9 Nov 2026): "How MCP works", "In short" (including the Microsoft item about two CVE records and Invariant Labs) and "Words used on this page". The anchors `#how-mcp-works`, `#in-short` and `#words-used-on-this-page` no longer exist on this page. The Risk map tab now holds only the risk map, the diagram and Risk by zone. The terms (DNS rebinding, confused deputy, token passthrough, SSRF and others) are no longer defined on the page. Most are still named in the risk cards, SSRF is not named in the Risks tab text.

## 9 Nov 2026: "my judgement" becomes "interpretation by AI" (owner's request)

- Owner's wording: "Marked [inference] is interpretation by AI, not stated in a source." Reason: the judgement is made by AI, not by the owner, so first person was wrong.
- Replaced on every page that said it: MCP-Risk-Map.html, Developer-WS.html, AKS-sikkerhetsvurdering.html, and the wip governance summary (page and build script). Includes "my estimate" (now "an AI estimate"), "my own assessment", "these definitions are mine", "our reading" and the "My judgement" evidence heading (now "Interpretation by AI").
- Added as a rule in AGENTS.md section 3 so new text follows it. Old diff lines in Developer-WS.factcheck.md keep the old wording as history.

## 9 Nov 2026: risks made MECE (owner's /goal)

- **Why.** The owner said two risks about the same thing means something is wrong, OWASP has 10 distinct risks and CoSAI might add some. A pair test found old overlaps: M02 held OWASP MCP03 (tool poisoning) and MCP04 (supply chain); M06 held MCP02 (scope creep) and MCP07 (authentication and authorization); M08 held MCP08 (audit) and MCP10 (over-sharing); M10 (CoSAI multitenancy) was the same subject as MCP10.
- **Result: 14 risks.** One home risk per OWASP entry, so OWASP view shows exactly 10. CoSAI adds M07 network reach, M09 approval and over-trust, M11 runaway cost, M12 weak protocol and transport.
- **Rules that keep them apart** (interpretation by AI): tool poisoning (M13) is the tool's own description or schema; prompt injection (M04) is content or output the model reads; supply chain (M02) is how code or a package arrived; command injection (M03) is the place where commands run; scope creep (M06) is how big permissions are; authentication and authorization (M14) is who may call and verify, including confused deputy and OAuth; token exposure (M05) is secret handling and reuse; transport (M12) is traffic unprotected in flight; network reach (M07) is binding, Origin, CORS, CSRF, SSRF; over-sharing (M10) is data or context reaching the wrong party, including other users of a shared server; audit (M08) is missing logs and inventory.
- **Notable moves.** M01 to M12 keep their ids and meaning where possible, so saved statuses stay valid. M02 lost tool poisoning (now M13). M06 lost authentication, confused deputy and OAuth (now M14). M08 lost over-sharing (now M10). M10 gained CoSAI #24. Typosquatting (#5) is homed in M02, with M01 as Also. CoSAI #1 and #18 are homed in M14.
- **OWASP's own MCP03 wording names the tools' outputs too.** The page keeps outputs under M04 and says so on the M13 card as interpretation by AI.
- **Saved statuses.** M02, M06, M08, M10 now cover narrower subjects than before. A status saved earlier for one of these may be broader than the new card. The page does not migrate saved values; the owner can reset.
- **Microsoft view.** M13 takes the tool-change reset (Visual Studio, Azure page). M14 takes API Management, CVE-2026-32211 and Copilot Studio authentication. M06 and M13 and M14 follow the same rule: no Microsoft source reviewed means "Not assessed" (M06). M10 takes only the OWASP listing placement.

## Final MECE and attribution pass, 9 November 2026

- Supersedes earlier claims that one home per framework entry alone proves MECE. Source categories overlap; classify individual failed controls with explicit exclusions and retain attack-chain cross-references.
- Preserve all public risk and section IDs and saved-setting keys. Add classification-boundaries without renaming the historical the-eight-risks anchor.
- Separate Copilot Studio evidence IDs (studio*) from CoSAI (cs*); add regression checks for source namespaces, entry coverage and static card labels.
- Move permission breadth to M06, approval to M09 and Windows isolation to M03. These are different failed controls, even when a single attack involves all three.
- Keep source claims distinct from interpretation by AI [inference]. No claim that a missing OWASP category name proves the topic absent from OWASP guidance.

## 10 November 2026: risk-by-zone table

- The zone table now shows every mapped component's finding, requirement, or control statement. Exact quotes and source links appear where the claim has a registered quote. Each risk row links to the detailed checks in its risk card. An unmapped cell is labeled as such and does not imply that no control exists.
- Added governance coverage for M03: the General view recommends sandboxing local servers with minimal default privileges and distinguishes that recommendation from the command allowlist, which only restricts which covered Copilot command can start. In the Microsoft view, the Windows on-device registry's per-agent access control is separately identified as prerelease and scoped to that registry.
- Added governance coverage for M09: the General view states a recommendation as interpretation by AI [inference]. The Microsoft view records the VS Code policy that makes selected tools require confirmation.
- The table is a summarized control and evidence index, not an exhaustive inventory of every control available in every client. The risk card remains the authoritative checklist.
- Rechecked the new Microsoft policy claims on 10 November 2026 and updated the index entry date. Kept the page-wide current-as-of date at 9 November because the older sources were not all rechecked.

## 14 November 2026: full recheck

- **Page-wide date moved to 14 November 2026** because every source was fetched and read again that day. The two "Current as of" heading ids keep "9-november-2026" (ids never change).
- **Mitiga line reports, not judges.** "Mitiga disagrees" overstated the article, which calls Anthropic's determination defensible. The page now gives Mitiga's own points.
- **M09 and M11 mapping sentence removed** instead of reworded: the card header already shows that the entries are CoSAI only.
- **Local harness deprecation goes in Limits**, not in each row, so each row keeps one job. Rows only name the harness where the docs scope a behaviour to it.
- **Tag key added to the footer** (AGENTS.md rule). The older footer sentence that defined `[inference]` was removed so the definition has one home.

## 21 November 2026

- **Only verified findings changed.** Each candidate from a reviewer was checked by a second reviewer with different competence before an edit. Four candidates were rejected and the page kept.
- **Prerelease qualifier kept in two places, not on every claim.** The source says only that "some information" on the Windows page relates to prereleased product, so the qualifier sits in the source label and the Preview callout, and the registry claims lose the label.
- **START rows follow the risk boundaries**: lifetime in M05, scope in M06, localhost binding in M07, transport integrity in M12.

- Iteration 3: config-file watch stays in M05 only, because M08 does not mention it and the control detects the Mitiga credential-theft chain.

- Iteration 4: Microsoft cards for M10 to M12 now say "Not assessed in this view" because the old "no source reviewed" text was false. General view now says it uses parts of the spec guidance.

- Iteration 6: Windows 11 Experimental sandbox claim removed instead of refetching, because it was the only claim on that source and cannot be quoted from cache. Gateway coverage now uses Microsoft's own caution (gw4) instead of our own "does not cover".

- Iteration 7: Invariant example kept out of the general M04 card to avoid a second home and a new vendor source. CoSAI #24 gets M13 only.

- Iteration 8: CVE tag exclusively-hosted-service dropped because no source explains it. Coverage-only suggestions (Azure monitoring, sandbox, GitHub connector blocking, OTel hashing) rejected to keep cards short.

- Iteration 9: sandbox platform claim restored because the agent-sandboxing page was refetched. CVE tag restored with a quote, since the cached record carries it.
- Iteration 10 (21 Nov 2026): accepted 6 of 7 findings (M05 Mitiga chain, M04 direct-injection scope note, M14 state-handle check, M14 legacy auth examples, VS Code registry fetch failure, VS Code sandbox scope). Rejected M07 CoSAI #26 widening. Left "session identifiers" as CoSAI wording. Clean-iteration count stays 0.
- Iteration 11 (21 Nov 2026): 0 findings in both views, no edits. Clean count 1.
- Iteration 12 (21 Nov 2026): 1 evidence-display finding (CVE-2026-26118 PR:L and ranges), fixed with quotes c1c to c1e. Clean count 0.
- Iteration 13 (21 Nov 2026): 5 of 8 findings accepted (Copilot Studio row mapping, vs13, GitHub row title, ccname quote, Mitiga prerequisite). Clean count 0.
- Iteration 14 (21 Nov 2026): 1 of 2 Microsoft findings accepted (1.145 rule attribution). General view clean. Clean count 0.
- Iteration 15 (21 Nov 2026): 0 findings in both views, no edits. Clean count 1.
- Iteration 16 (21 Nov 2026): 6 findings, 5 edited, 1 placement kept with new wording. Clean count 0.
- Iteration 17 (21 Nov 2026): 0 findings in both views, no edits. Clean count 1.
- Iteration 18 (21 Nov 2026): 3 findings, all edited (M08 identity capture and GSA TLS prerequisite, M05 lifetime check). Clean count 0.
- Iteration 19 (21 Nov 2026): 0 findings in both views, no edits. Clean count 1.
- Iteration 20 (22 Nov 2026): 4 findings, all edited (M01 gateway quote list, Copilot Studio GSA wording and quote, M03 agent-cell quote, M03 approval quote). Clean count 0.
- Iteration 21 (22 Nov 2026): 0 accepted findings (3 coverage suggestions rejected). Clean count 1.
- Iteration 22 (22 Nov 2026): 3 findings edited (Visual Studio 2026 scope of allow list, M02 env wording, M01 inference tag), 1 rejected. Clean count 0.
- Iteration 23 (22 Nov 2026): 0 findings in both views. Clean count 1.
- Iteration 24 (23 Nov 2026): 2 findings, 1 edited (Copilot Studio auth options scoped to the onboarding wizard), 1 rejected (Visual Studio 2026 scope stays). Clean count 0.
- Iteration 25 (23 Nov 2026): 3 findings, all edited (OpenTelemetry scoped to Copilot Chat in VS Code, autostart marked experimental, SSRF guidance scoped to OAuth metadata discovery). Clean count 0.
- Iteration 26 (23 Nov 2026): 2 findings, both edited (M03 sandbox SHOULD scoped to one-click local setup; Visual Studio tool-list reset separated from the 2026 18.7+ trust prompt). Clean count 0.
- Iteration 27 (23 Nov 2026): clean. Clean count 1.
- Iteration 28 General (23 Nov 2026): 3 findings, 1 rejected (token passthrough quote exists), 2 edited (CoSAI #26 outbound or inbound; OAuth discovery checks scoped to server-deployed clients). Clean count 0.
- Iteration 28 Microsoft (23 Nov 2026): 2 findings, 1 edited (Copilot Studio auth, query key and SSE scoped to the standard harness; DLP stays unscoped), 1 rejected again (GSA client prerequisite, no new evidence). Clean count 0.
- Iteration 29 (23 Nov 2026): General 2 findings edited (M01 serverName scope, M07 Origin scope), Microsoft none. Clean count 0.
- Iteration 30 (23 Nov 2026): General and Microsoft clean. Clean count 1.
- Iteration 31 (23 Nov 2026): General 2 findings, 1 edited (M05/cfgf entry point), 1 rejected (M02 local wording). Microsoft none. Clean count 0.
- Iteration 32 (23 Nov 2026): General none, Microsoft 2 findings edited (M08 coverage wording, Visual Studio 2026 name). Clean count 0.
- Iteration 33 (23 Nov 2026): General none, Microsoft 4 findings, 1 edited (APIM example wording), 3 rejected (CVE versions, GSA scope, Windows label). Clean count 0.
- Iteration 34: three findings accepted (M05 token lifetime now sourced to CoSAI via cs35 instead of [inference], M07 check 2 allows restricted IPC, SSE point scoped to the standard harness). Clean count 0.
- Iteration 35: nine findings, six accepted (gateway scope, autostart exclusions, Azure pinning scope, SSRF client scope, M14 plain words, CoSAI #1 wording), three rejected (BYO verb, workspace prompt, state handle MUST NOT). Clean count 0.
- Iteration 36: five findings accepted (APIM scope, identity capture default scope, DNS rebinding conditions, OWASP MCP05 validation qualifier, M13 plain words). Clean count 0.
- Iteration 37: one finding accepted (M05 remediation sentence narrowed to what Mitiga says about rotation). Microsoft view clean. Clean count 0.
- Iteration 38: four findings, all rejected (confused deputy MUST follows the spec sentence, Codex sentence already follows the identity setup, Invariant and GSA limits are coverage). Clean count 1.
- Iteration 39: one finding, rejected (autostart "starts" matches the documented default "Start servers that have never run or whose configuration has changed"). Clean count 2. Stop criterion met. "Current as of" and "checked on" stay at 14 November 2026 because the sources were not refetched in this run.
