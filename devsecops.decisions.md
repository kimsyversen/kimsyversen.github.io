# DevSecOps decisions

## 15 November 2026: risks must be documented, not theoretical

- Every risk in the table carries one documented case or one statistic beside its standard. Reason: the owner asked for real risks that apply to an enterprise. A standard shows that a control exists; a case shows that the consequence has happened.
- A risk without a documented case is removed, and the cell stays blank. Reason: a blank cell is more honest than a risk that only could happen. Removed for this reason: "Critical service goes unclassified" (Plan, governance) and "Security sign-off lacks test evidence" (Test, governance).
- One consequence has one home. "Security findings go untracked" (Build) and "Open actions lose ownership at handover" (Operate) were removed because the same consequence, a fix that is never made, already sits under Operate (the flaw is not patched) and Monitor (nobody checks that fixes were made).
- Consequences are written as events ("a regulator fines the company"), not as tendencies ("increasing the risk of"). The wording goes no further than the case source does.
- Preferred sources are regulators, courts, government auditors and the affected company's own incident report. Allegations are used only when labeled as allegations (FTC and Uber). A case against Optus was left out because it rested on allegations before a court.
- The US House Oversight Committee report on Equifax is used for four risks. Reason: it is one of few public reports that traces a breach through accountability, data scope, patching and monitoring, and each risk cites a different finding.
- The choice of case for each risk is interpretation by AI and is stated as such on the page.
- Each case link points to the quoted passage: a text fragment for web pages, a page number for PDFs.

## 15 November 2026: one page, two views

- `devsecops.html` holds both versions. A switch at the top selects DevSecOps or Agentic DevSecOps. Reason: the owner asked to see both on one page. The agentic page's design is the base, so the DevSecOps view now uses the same phase boxes and detail panel instead of the three lanes.
- Each view is a `data-view` block. Only one is visible. The address `#view-agentic` or `#view-devsecops` selects a view, and a link to a section in the other view switches to it first. Without scripts both views show.
- DevSecOps ids are unchanged. Agentic ids that collided (`lifecycle`, `map-heading`, the phase ids) got an `agentic-` prefix. The non-colliding ones (`risk-*`, `agent-risks`, `what-changes`) kept their names. Reason: public anchors must not change, and one page cannot have the same id twice.
- `agentic-devsecops.html` stays as a redirect to `devsecops.html#view-agentic`. It maps old anchors to the new ids. Reason: the old address is public. It has no notes of its own.
- The index lists one entry (10, DevSecOps). Entry 13 (Agentic DevSecOps) is retired and its number is not reused.
- The DevSecOps panel lists governance, secure development and a link to that phase's row in the risk table with the count of risks. Reason: the table stays the one home for risks and their evidence.
- Checkpoint phases (governance checkpoints, formerly diamonds) use the accent border and a "Checkpoint" label, as the agentic view does for human gates.
- Both flows have ten boxes in two rows of five. Reason: ten in one row is too narrow at the page width.
- The tag key appears only with the agentic view, the only view that uses tags.

---

# Agentic DevSecOps decisions (carried over from the former separate page)


### 15 November 2026: first draft

- Superseded on 15 November 2026 by the ten-phase flow, see below. Eight phases: Plan, Code, Review, Build, Test, Release, Deploy, Operate. `devsecops.html` has ten (it adds Design, Monitor and Retire and has no Review). Reason: the owner approved the eight-phase flow. Review is its own phase because an agent checking another agent's change is a separate handoff with its own gate.
- Superseded on 15 November 2026 by the phase diagram, see below. Lanes are Input, Phase and agent task, Output. Reason: the page's job is to show what moves between phases. Governance and secure development activities stay on `devsecops.html`, which this page links to instead of repeating.
- The phase split and every input and output are tagged `inference`. Reason: no source prescribes this flow.
- A fourth gate (retirement) was added on 15 November 2026, see below. Three human gates (spec, merge, production) are tagged `recommendation`. Reason: the placement is a design choice. The sources support human approval of high-impact actions in general, not these three points.
- The second section has four rows: untrusted input, agent access, human approval, traceable handoffs. Each row has one risk and one control. Reason: one home per fact. Vendor passages are labelled "One vendor's implementation" so they do not read as a standard.
- The AWS bulletin AWS-2025-015 (Amazon Q Developer for VS Code) is not used. Reason: the bulletin describes an over-scoped token in a build configuration and does not mention prompt injection or agents, so it does not support an agent claim.
- NIST SP 800-218A and the OWASP Top 10 for Agentic Applications 2026 are not quoted. Reason: only their landing pages were read, not the documents. Superseded for the OWASP document on 15 November 2026, see below. Still holds for NIST SP 800-218A.
- The page reuses the CSS of `devsecops.html` by copy. Reason: pages on this site are single files. A shared stylesheet would be one more file to keep in step for two pages.

### 15 November 2026: OWASP Top 10 for Agentic Applications 2026 cited

- Eight quotes from the document are added, one in each risk and control cell of the four rows. Reason: the owner asked for it to be read and cited, and it is the one source here written for agents and not for LLM applications in general.
- The four rows stay. No row per ASI entry. Reason: the page's job is the changes that agents bring to delivery, and the ten entries overlap those four changes. A second table would give the same fact two homes.
- Quotes link to the landing page with the printed page number in the label. Reason: the PDF is served as a download, so a `#page=` link cannot open it at the passage.
- ASI04 to ASI07, ASI09 and ASI10 are not quoted. Reason: supply chain, code execution, memory, agent-to-agent messages, human trust and rogue agents either belong on `devsecops.html` or do not map to one of the four rows without a new claim.

### 15 November 2026: phase diagram replaces the three lanes

- The three-lane table is replaced by a row of eight phase boxes. Each box shows the phase and the output it hands on. Selecting a box shows that phase's task, input, output, human gate and risks. Reason: the owner asked for the diagram with clickable phases. A handoff is now stated once, as the output of a box, and no longer also as the input of the next row.
- The diagram is HTML boxes, not an SVG drawing. Reason: eight boxes wrap to four columns and then to one column on narrow screens without a second drawing to keep in step.
- Phase ids (`#plan`, `#phase-plan` and so on) are kept. A link to a phase selects it first. Without scripts all eight phases are shown.
- Each phase lists two of the four changes with one sentence on how it shows up there, tagged `inference`, and links to the row in the table. Reason: the owner asked for risks per phase. The table stays the one home for risks, controls and source quotes. The phase lines only point to it.
- The four table rows have new ids (`risk-untrusted-input`, `risk-agent-access`, `risk-human-approval`, `risk-traceable-handoffs`) so the phases can link to them.

### 15 November 2026: Monitor and Retire added to the agentic view

- Ten phases: the eight above plus Monitor (09) and Retire (10). Reason: the owner asked for them. The eight-phase flow folded monitoring into Operate and had nothing on shutting a service down, and with both views on one page the same phase name meant two things.
- The two views still differ in one place each: the agentic view has Review and no Design, the DevSecOps view has Design and no Review. Not changed, because the owner asked only for Monitor and Retire.
- Operate is now "Run and respond" and no longer watches. Monitor takes the logs and the records of what the agents did, and hands on alerts, incident tickets and new issues. Alerts go to Operate. Tickets and issues go back to Plan.
- Retire has a human gate on the shutdown and the data deletion, tagged `recommendation`. Reason: deletion cannot be undone, and the ASI02 passage already quoted in the Human approval row names "delete" among the actions that need human confirmation.
- Retire's risk lines are Agent access (credentials held by the agents must be revoked too) and Human approval. Monitor's are Untrusted input and Traceable handoffs. No new table rows or quotes. Reason: the table's job is the four changes, and the phase lines only point to them.
- Operate's second risk line is now Traceable handoffs. The Untrusted input line about logs and vulnerability reports moved to Monitor, where those inputs now arrive.
- The agentic flow uses the `flow-10` layout. The `flow-8` styles are removed.
- New ids: `agentic-monitor`, `agentic-phase-monitor`, `agentic-retire`, `agentic-phase-retire`. No existing id changed.

### 15 November 2026: worked example in the agentic view

- A table "Example: fixing one bug with agents" (`#agentic-example`, heading `#example-fixing-one-bug-with-agents`) sits between the phases and the four changes. It follows one made-up fix through the ten phases: what the agent does, what it hands on, and the person at each gate. Reason: the owner asked for a simple, concrete example like the one on `threatmodelling.html`, because development with agents is new to most readers.
- The example is threat I from `threatmodelling.html` (a customer reads other customers' documents). Reason: the reader may already know the claims portal, and the tests and the 50-refusals alert match the controls listed there.
- It reuses the risk table styles. One new style, `.walk-gate`, marks the human gate lines.
- The whole example carries one `inference` tag. It adds no risk, control or quote. The four-changes table stays the one home for those.
- Retire is shown as "not part of this change", with what would happen when the portal is replaced. Reason: one fix does not retire a service, but leaving the row out would break the match with the ten phases.
