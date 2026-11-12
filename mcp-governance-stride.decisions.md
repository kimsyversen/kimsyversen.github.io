# MCP governance STRIDE and DREAD model: decisions

1. Scope: the architecture on mcp-governance-microsoft-interactive.html only. Reason: the user asked for that page plus SC-500.
2. Method: STRIDE per element. External entities get S and R. Processes get all six. Data stores get T, R, I, D. Data flows get T, I, D. Clarified 2026-11-12: store R is selected for approval/change/audit history, not a universal store rule. Matrix checks establish enumeration only.
3. Elements: EE1 Developer, EE2 M365 Copilot user, EE3 Requester and approver, EE4 Unapproved or malicious server (named E1 to E4 until 2026-11-12), P1 to P6, DS1 to DS3 (named D1 to D3 until 2026-11-12), F1 to F5. Reason: each maps to a box or arrow on the page.
4. Trust boundaries TB0 to TB7 follow the page's zones. F5 (bypass) is drawn as a red dashed edge because blocking it is the page's central control.
5. DREAD: 1 to 10 per factor, mean of five, one decimal. Bands: High 6 or above, Medium 4 or above, Low below 4. Reason: the first bands (7 and 4) gave 1 High, which hid differences. Bands changed once, before reading results by hand.
6. Scores are AI estimates, not observed. Every threat is `[inference]`. Reason: AGENTS.md evidence rules.
7. SC-500: mapped to skill names in the official study guide (page last updated 2026-05-13, read 2026-11-12; an earlier note said 2026-07-31, which the live page does not show), mostly skill 3.1 (AI security). Threats whose fix is a GitHub, VS Code, Intune or Power Platform setting are flagged `outside SC-500` (7 threats).
8. Output format: .drawio for the diagram, .tsv for the register, .dfd.xml for a single-page import. Reason: tsv opens in a spreadsheet; drawio is what the user asked for.
9. Superseded by the web-page request below: originally not indexed. The page is now index entry 12. Publishing from `master` remains the owner's separate action.

## Evidence levels (2026-11-12)
- Decision: each threat is `exploited`, `disclosed` or `theoretical`. Reason: the goal asked for threats that are not theoretical only, so the page must show which ones have a public record and not hide the rest.
- Decision: only two records count as exploited (CISA KEV entry, vendor-confirmed backdoor). CVEs and researcher demos stay `disclosed`. Reason: a fixed vulnerability is not proof of attacks.
- Decision: records from other products (LiteLLM, Cursor, mcp-remote) are mapped by failure type and say so in the fact check. Reason: they show the failure class is real, not that this architecture is hit.
- Decision: two threats added (T3 package backdoor, E3 local tool runs untrusted input). Reason: real incidents had no matching row. At the time the ids were P2-T and P2-E, split into P2-Ta/P2-Tb and P2-Ea/P2-Eb; since the renumbering they are T2/T3 and E2/E3.
- Superseded by the verification review below: DREAD originally rose by a fixed rule where a record existed. Cross-product evidence does not establish those factors for this design.


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
- Superseded by the verification review below: raised DREAD scores originally showed as hatched cells. Automatic lifts and their UI were removed.
- Decision: the diagram scrolls sideways below 1080 px and the register stacks into cards below 760 px, hiding the five factor columns there. Reason: the diagram is unreadable when shrunk; the factors stay in the detail panel.
- Decision: V numbers in a threat's basis link to the design page's fact check, and gap or ctrl ids link to the design page. Reason: each claim reaches its quote in one click.
- Decision: selecting a box or flow name opens the detail panel on that element: its threats as cards sorted by score, a STRIDE count that marks letters not checked for its kind as n/a, and a link back from any threat opened there. It also filters the diagram and register to that element until the panel closes. Reason: owner request; the panel was the only place that showed a whole threat, and the old element click only filtered.
- Decision: in the element view the arrow buttons step through elements, and `#el-<id>` links open it. Reason: same controls and shareable links as the threat view.

## Verification review (2026-11-12)

- Preserve all 74 threat IDs, element IDs and public anchors; revise scenarios and preconditions in place. Each row now states a plausible STRIDE consequence rather than treating legitimate administration, a control gap or public reachability alone as an exploit.
- Keep DREAD values as uncalibrated scenario estimates and separate them from public-record evidence. The old automatic lifts and the original threshold-selection rationale do not establish risk calibration. Keep the existing 6/4 bands as explicitly local choices, with no claim of a standard or empirical threshold.
- Supersede the earlier public-record mapping where it conflicts with the fact check: 14 threat IDs retain evidence (2 exploited-class and 12 disclosed-class). Exclude mismatched or insufficient associations, move three read-exposure records to I5, and add separately labeled Asana news reporting, IONIX researcher evidence and Pillar Security campaign research. In particular the exploited LiteLLM command-execution flaw does not establish E5 shared-connection exploitation.
- Show related controls as design references, not proven mitigations. Preview detection remains optional; core authentication, authorization, transport integrity and network controls must work without preview functionality.
- Label the figure as a logical, aggregated model. Remove the untested `direct call: blocked` claim, identify omitted routes and boundaries, and keep an ASCII companion with the flow description. Expand the implementation model separately before claiming completeness.
- Keep exact scenario and diagram-label review ledgers in the fact check. `scripts/check-mcp-stride.py` checks them against the generated page/TSV and optionally verifies all 208 source-table quotes, including the six interactive-only Purview additions.
- Follow-up non-CVE search: add the WhatsApp experiment to I3, Supabase ticket experiment to T14 and active AntV malware advisory to T3. Preserve one authoritative scenario home per new record. Keep Smithery hosting compromise, GlassWorm lookalike installation and MCP reconnaissance as context because their mechanisms do not precisely match an existing row; exclude a withdrawn proxy-malware advisory. Do not convert published malware or researcher demonstrations into claims of victim compromise.
- Recheck 2026-11-12: T7 keeps its id, element, STRIDE letter, scores and basis but is reworded so the Tampering consequence is explicit (manipulated inspection input gives a wrong allow verdict). Reason: moving it to another letter would renumber public threat ids. The CVE-2026-33032 title was corrected to match the CVE record.

## Design page audit carried over (2026-11-12)

- I15 (F5, information disclosure) now covers cloud agents and unrestricted egress, and links Windows outbound limits, Foundry network and sandbox and the new design page gap `gap-foundry-prompt-agents` instead of backend isolation. Its basis cites V101. **Why:** the design page audit found that the Foundry Network control does not affect prompt agents outside the Copilot harness, and backend isolation does not stop traffic to another server. Id, element, letter and scores are unchanged, so public anchors and counts stay.
- No other row changed. The other design page fixes (gateway lead, Later deny step, pilot citation, device scope, rollout step) do not change a threat, a control link or a basis on this page.

## Governance alignment (2026-11-12)

Preserve all threat and element IDs, scenarios and scores. Correct related controls and bases for E5, I15 and T9 and the F1 scope instead of inventing new incidents or inferring lower residual risk from design edits. Explicitly exclude direct BYO access to the private backend; a gateway-fronted variant is untested.

- Completion pass: retain T9/T14 scenarios and scores while linking the actual Power Platform mixed-mode requirement and preview tool-evaluation scope. Discovery metadata is excluded from tool-invocation evaluation; no new attack coverage is claimed.
