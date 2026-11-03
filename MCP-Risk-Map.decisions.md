# Decisions: MCP risk map (MCP-Risk-Map.html), 2 Nov 2026

Belongs to [MCP-Risk-Map.html](MCP-Risk-Map.html). Other notes for the same page: [plan](MCP-Risk-Map.plan.md), [fact check](MCP-Risk-Map.factcheck.md).

Working notes.

- Eight risks, not ten plus seven. The user asked for low detail. Every risk maps to at least one OWASP MCP Top 10 entry or a section of the MCP specification.
- Dropped the "More risks" tables, the attack-path filter, the persona review tab and the incident-response section. They add detail and are not MCP-specific.
- Kept the diagram, popovers, status tracker, "Where to start" table, evidence and sources, so the page works like Developer-WS.html.
- Removed the "sandbox if enabled" box from the diagram. Claude Code runs local MCP servers outside its sandbox while VS Code can sandbox stdio servers, so one box would be wrong for one of them. The spec only says clients should sandbox servers; M03 says that.
- Only one MCP-specific attack is cited (Mitiga, May 2026). Anthropic called it out of scope and by design; Mitiga disagrees. Both positions are on the page. Other risks are described as OWASP categories or spec warnings with no incident cited.
- Did not state the values of the VS Code chat.mcp.access setting. Docs and source disagree (see Developer-WS.html). Only the policy names are used.
- Plugin4Shell excluded: Cloud Security Alliance does not name MCP as the affected component.
- Friction estimates and the risk order are my judgement and are tagged [inference].
- Storage keys are mcp-tab and mcp-status. Both pages share one origin, so the old dev-* keys would mix state.
- Made the page easier for people new to MCP security: added a "How MCP works" box, a glossary, a plain-words line per risk, and moved vendor setting names into a collapsed "How to set it". Why: the user asked whether the page suits learners, and the original assumed prior knowledge.
- Added a separate "VS Code" tab and left the general risks as they were. Why: the user wanted VS Code as the base case, then chose to keep the general content and add a section. Each row names the risk it touches. The table stacks into cards under 680px so it does not scroll sideways.

## 3 Nov 2026, "Made with AI" note

- **Plain label and one sentence at the end of the footer**, under a hairline rule, in the page's own muted and ink colours. Chose this over a pill or badge to keep it quiet and avoid the template look. Colours use the page tokens, so dark mode follows.
- **Wording:** "This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human." Same text on all five pages.
- **Layout:** label and text in two columns on desktop, stacked under 560 px.
