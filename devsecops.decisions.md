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
