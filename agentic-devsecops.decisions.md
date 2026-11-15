# Agentic DevSecOps: decisions

## 15 November 2026: first draft

- Eight phases: Plan, Code, Review, Build, Test, Release, Deploy, Operate. `devsecops.html` has ten (it adds Design, Monitor and Retire and has no Review). Reason: the owner approved the eight-phase flow. Review is its own phase because an agent checking another agent's change is a separate handoff with its own gate.
- Superseded on 15 November 2026 by the phase diagram, see below. Lanes are Input, Phase and agent task, Output. Reason: the page's job is to show what moves between phases. Governance and secure development activities stay on `devsecops.html`, which this page links to instead of repeating.
- The phase split and every input and output are tagged `inference`. Reason: no source prescribes this flow.
- Three human gates (spec, merge, production) are tagged `recommendation`. Reason: the placement is a design choice. The sources support human approval of high-impact actions in general, not these three points.
- The second section has four rows: untrusted input, agent access, human approval, traceable handoffs. Each row has one risk and one control. Reason: one home per fact. Vendor passages are labelled "One vendor's implementation" so they do not read as a standard.
- The AWS bulletin AWS-2025-015 (Amazon Q Developer for VS Code) is not used. Reason: the bulletin describes an over-scoped token in a build configuration and does not mention prompt injection or agents, so it does not support an agent claim.
- NIST SP 800-218A and the OWASP Top 10 for Agentic Applications 2026 are not quoted. Reason: only their landing pages were read, not the documents. Superseded for the OWASP document on 15 November 2026, see below. Still holds for NIST SP 800-218A.
- The page reuses the CSS of `devsecops.html` by copy. Reason: pages on this site are single files. A shared stylesheet would be one more file to keep in step for two pages.

## 15 November 2026: OWASP Top 10 for Agentic Applications 2026 cited

- Eight quotes from the document are added, one in each risk and control cell of the four rows. Reason: the owner asked for it to be read and cited, and it is the one source here written for agents and not for LLM applications in general.
- The four rows stay. No row per ASI entry. Reason: the page's job is the changes that agents bring to delivery, and the ten entries overlap those four changes. A second table would give the same fact two homes.
- Quotes link to the landing page with the printed page number in the label. Reason: the PDF is served as a download, so a `#page=` link cannot open it at the passage.
- ASI04 to ASI07, ASI09 and ASI10 are not quoted. Reason: supply chain, code execution, memory, agent-to-agent messages, human trust and rogue agents either belong on `devsecops.html` or do not map to one of the four rows without a new claim.

## 15 November 2026: phase diagram replaces the three lanes

- The three-lane table is replaced by a row of eight phase boxes. Each box shows the phase and the output it hands on. Selecting a box shows that phase's task, input, output, human gate and risks. Reason: the owner asked for the diagram with clickable phases. A handoff is now stated once, as the output of a box, and no longer also as the input of the next row.
- The diagram is HTML boxes, not an SVG drawing. Reason: eight boxes wrap to four columns and then to one column on narrow screens without a second drawing to keep in step.
- Phase ids (`#plan`, `#phase-plan` and so on) are kept. A link to a phase selects it first. Without scripts all eight phases are shown.
- Each phase lists two of the four changes with one sentence on how it shows up there, tagged `inference`, and links to the row in the table. Reason: the owner asked for risks per phase. The table stays the one home for risks, controls and source quotes. The phase lines only point to it.
- The four table rows have new ids (`risk-untrusted-input`, `risk-agent-access`, `risk-human-approval`, `risk-traceable-handoffs`) so the phases can link to them.
