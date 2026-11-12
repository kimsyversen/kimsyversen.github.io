# MCP governance STRIDE and DREAD model: decisions

1. Scope: the architecture on mcp-governance-microsoft-interactive.html only. Reason: the user asked for that page plus SC-500.
2. Method: STRIDE per element. External entities get S and R. Processes get all six. Data stores get T, R, I, D. Data flows get T, I, D. Reason: standard rule, and it makes coverage checkable (the builder fails if a cell has no threat).
3. Elements: EE1 Developer, EE2 M365 Copilot user, EE3 Requester and approver, EE4 Unapproved or malicious server (named E1 to E4 until 2026-11-12), P1 to P6, DS1 to DS3 (named D1 to D3 until 2026-11-12), F1 to F5. Reason: each maps to a box or arrow on the page.
4. Trust boundaries TB0 to TB7 follow the page's zones. F5 (bypass) is drawn as a red dashed edge because blocking it is the page's central control.
5. DREAD: 1 to 10 per factor, mean of five, one decimal. Bands: High 6 or above, Medium 4 or above, Low below 4. Reason: the first bands (7 and 4) gave 1 High, which hid differences. Bands changed once, before reading results by hand.
6. Scores are AI estimates, not observed. Every threat is `[inference]`. Reason: AGENTS.md evidence rules.
7. SC-500: mapped to skill names in the official study guide (page last updated 2026-05-13, read 2026-11-12; an earlier note said 2026-07-31, which the live page does not show), mostly skill 3.1 (AI security). Threats whose fix is a GitHub, VS Code, Intune or Power Platform setting are flagged `outside SC-500` (7 threats).
8. Output format: .drawio for the diagram, .tsv for the register, .dfd.xml for a single-page import. Reason: tsv opens in a spreadsheet; drawio is what the user asked for.
9. Not published or indexed. Reason: no request to publish.

## Evidence levels (2026-11-12)
- Decision: each threat is `exploited`, `disclosed` or `theoretical`. Reason: the goal asked for threats that are not theoretical only, so the page must show which ones have a public record and not hide the rest.
- Decision: only two records count as exploited (CISA KEV entry, vendor-confirmed backdoor). CVEs and researcher demos stay `disclosed`. Reason: a fixed vulnerability is not proof of attacks.
- Decision: records from other products (LiteLLM, Cursor, mcp-remote) are mapped by failure type and say so in the fact check. Reason: they show the failure class is real, not that this architecture is hit.
- Decision: two threats added (T3 package backdoor, E3 local tool runs untrusted input). Reason: real incidents had no matching row. At the time the ids were P2-T and P2-E, split into P2-Ta/P2-Tb and P2-Ea/P2-Eb; since the renumbering they are T2/T3 and E2/E3.
- Decision: DREAD rises only by a fixed rule where a record exists. Reason: keeps the lift visible and not hand-picked.


## Register box height (2026-11-12)
Chose a height computed from the text in each row over a fixed 30 px per row, because draw.io clips a table in a fixed-height box and hid rows 41 to 73. Flow labels get a white background so lines do not run through them.

## Threat ids by STRIDE letter (2026-11-12)

- Decision: threat ids are the STRIDE letter plus a number, counted in element order (E1 to F5): S1 to S10, T1 to T15, R1 to R13, I1 to I15, D1 to D14, E1 to E7. Reason: the owner asked for it. The old ids (element plus letter, such as P4-S) are gone from the data and notes.
- Superseded 2026-11-12: threat ids D1 to D14 clashed with data stores D1 to D3. The owner had the stores renamed DS1 to DS3.
- Superseded 2026-11-12: threat ids E1 to E7 used the same letters as external entities E1 to E4. The owner had the entities renamed EE1 to EE4, so the clash is gone. Old note: On the diagram, threat ids are only shown as coloured chips and element ids only as bold box titles, and the register puts the element id with its name, so the two do not share a spot.
- Decision: the DREAD register no longer shows SC-500 skills. Reason: owner request. The SC-500 map stays on page 3 and in the tsv.

## Web page (2026-11-12)

- Decision: `mcp-governance-stride.html` is built by `scripts/build-mcp-stride-page.py` from the same data module as the drawio, and the diagram is drawn from the drawio's own page 1 geometry. Reason: one source of truth; the page cannot drift from the attached file.
- Decision: one detail panel on the right, shared by diagram chips, register rows and score dots, and not modal. Reason: the reader can keep the diagram in view and step through threats with the arrow buttons.
- Decision: filters (STRIDE letter, rating, public record, element) apply to the diagram, the score dots and the register at once. Reason: one question, one answer in every view.
- Decision: raised DREAD scores show as hatched cells in the detail panel. Reason: makes the evidence rule visible per threat instead of only in the method text.
- Decision: the diagram scrolls sideways below 1080 px and the register stacks into cards below 760 px, hiding the five factor columns there. Reason: the diagram is unreadable when shrunk; the factors stay in the detail panel.
- Decision: V numbers in a threat's basis link to the design page's fact check, and gap or ctrl ids link to the design page. Reason: each claim reaches its quote in one click.
