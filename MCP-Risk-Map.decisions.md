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
