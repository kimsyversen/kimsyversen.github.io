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
- Friction estimates and the risk order are my judgement and are tagged [inference].
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
- **CVEs.** CVE-2026-26118 and CVE-2026-32211 are shown as vendor advisories from the CVE record, not as observed incidents. CVE-2026-32211 lists "Azure Web Apps" as the affected product with the tag exclusively-hosted-service; the page says so. Invariant Labs is labelled third-party research.
- **Preview features are labelled preview** where the source says so (Windows ODR, Entra MCP firewall and logging, Agent 365 gateway and BYO, GitHub registry enforcement).
- **Not claimed:** a Copilot Studio per-tool approval flow. No such statement was found in the sources read.
- **Per-item evidence (mechanism).** Each Microsoft card item, table row, diagram placement and callout carries quote ids. `qBlock` renders them as a collapsed list with a text-fragment link. Reason: AGENTS.md rule 3, the reader checks each claim from the diagram itself.
- **`MSDATA` is the source of truth.** It is one JSON line in the page. The builder script that produced it is not shipped. Reason: the page is hand-written with no build step. Edit the line, then run the check script.
- **Whitespace fallback.** The check first matches a quote word for word. If that fails it matches with whitespace ignored and prints a note. Only `cs3` needs it, because the source page lists a bold label and its colon as separate elements. `sp5` was shortened to drop a trailing period for the same reason.
- **Start table (Microsoft view) holds recommendations.** They are design requirements, so they carry no quote. Friction labels stay my judgement, tagged in the Sources tab.
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
