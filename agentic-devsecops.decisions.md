# Agentic DevSecOps: decisions

## 15 November 2026: first draft

- Eight phases: Plan, Code, Review, Build, Test, Release, Deploy, Operate. `devsecops.html` has ten (it adds Design, Monitor and Retire and has no Review). Reason: the owner approved the eight-phase flow. Review is its own phase because an agent checking another agent's change is a separate handoff with its own gate.
- Lanes are Input, Phase and agent task, Output. Reason: the page's job is to show what moves between phases. Governance and secure development activities stay on `devsecops.html`, which this page links to instead of repeating.
- The phase split and every input and output are tagged `inference`. Reason: no source prescribes this flow.
- Three human gates (spec, merge, production) are tagged `recommendation`. Reason: the placement is a design choice. The sources support human approval of high-impact actions in general, not these three points.
- The second section has four rows: untrusted input, agent access, human approval, traceable handoffs. Each row has one risk and one control. Reason: one home per fact. Vendor passages are labelled "One vendor's implementation" so they do not read as a standard.
- The AWS bulletin AWS-2025-015 (Amazon Q Developer for VS Code) is not used. Reason: the bulletin describes an over-scoped token in a build configuration and does not mention prompt injection or agents, so it does not support an agent claim.
- NIST SP 800-218A and the OWASP Top 10 for Agentic Applications 2026 are not quoted. Reason: only their landing pages were read, not the documents.
- The page reuses the CSS of `devsecops.html` by copy. Reason: pages on this site are single files. A shared stylesheet would be one more file to keep in step for two pages.
