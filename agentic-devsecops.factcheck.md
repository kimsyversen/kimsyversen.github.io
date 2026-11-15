# Agentic DevSecOps: fact check

Checked: 15 November 2026

## Scope and verdict

All 21 quotes on `agentic-devsecops.html` were found word for word in the sources fetched on 15 November 2026. Straight quotes in the sources are shown as typographic quotes on the page. The 8 quotes from the OWASP Top 10 for Agentic Applications 2026 were checked against text extracted from the PDF with `pdftotext -layout`, after joining lines and turning curly quotes into straight ones. The "without clear visibility" quote starts mid-sentence, and the "Issue short-lived" quote stops before the end of its sentence.

## Interpretation by AI

- The eight phases, the agent task in each phase, and every input and output are interpretation by AI. No source prescribes this flow.
- The risk lines under each phase (which of the four changes applies there, and how) are interpretation by AI. No source maps risks to these phases.
- The three human gates are a recommendation. The sources support human approval of high-impact actions in general.
- Grouping the sources into four changes, and the wording of each risk and control summary, is interpretation by AI.
- The sources describe LLM applications, one vendor's coding agent, and build provenance. None of them describes this eight-phase flow.

## Links

The 12 text links were opened in a browser on 15 November 2026 and land on the quoted passage. The heading link's anchor id was confirmed in the page source, not opened. The GitHub page was fetched at `/copilot/concepts/agents/cloud-agent/risks-and-mitigations`, which redirects to the address below. The heading quote links to the heading's own anchor, because a text link matched the page's side menu first.

The 8 agentic top 10 quotes link to the document's landing page and give the printed page number in the link label. Reason: the PDF is served as a download, so a link cannot open it at a page. The landing page was opened on 15 November 2026.

## Sources

| Source | URL | Version status |
|---|---|---|
| OWASP Top 10 for LLM Applications 2025, LLM01 Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 2025 list, current on the site |
| OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | 2025 list, current on the site |
| GitHub Docs, Risks and mitigations for Copilot cloud agent | https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations | Living page, no version number |
| SLSA 1.2, Provenance | https://slsa.dev/spec/v1.2/provenance | Status: Approved |
| OWASP Top 10 for Agentic Applications 2026 (PDF, 57 pages, file name `OWASP-Top-10-for-Agentic-Applications-2026-12.6-1.pdf`) | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | Landing page dated December 9, 2025 |

## Quote review

| Row | Quote starts | Source | Verdict |
|---|---|---|---|
| Untrusted input, risk | "Indirect prompt injections occur when" | LLM01 | Confirmed |
| Untrusted input, risk | "Due to inherent weaknesses in how natural-language instructions" | Agentic top 10, ASI01, page 9 | Confirmed |
| Untrusted input, risk | "Users can include hidden messages in issues" | GitHub | Confirmed |
| Untrusted input, control | "Separate and clearly denote untrusted content" | LLM01, mitigation 6 | Confirmed |
| Untrusted input, control | "Treat all natural-language inputs" | Agentic top 10, ASI01, mitigation 1, page 10 | Confirmed |
| Untrusted input, control | "Comments from users without write access" | GitHub | Confirmed |
| Agent access, risk | "Excessive Agency is the vulnerability that" | LLM06 | Confirmed |
| Agent access, risk | "Without a distinct, governed identity of its own" | Agentic top 10, ASI03, page 15 | Confirmed |
| Agent access, control | "Limit the permissions that LLM extensions" | LLM06, mitigation 4 | Confirmed |
| Agent access, control | "Issue short-lived, narrowly scoped tokens per task" | Agentic top 10, ASI03, mitigation 1, page 17 | Confirmed |
| Agent access, control | "Copilot cloud agent only has the ability to push" | GitHub | Confirmed |
| Human approval, risk | "The root cause of Excessive Agency is typically" | LLM06 | Confirmed |
| Human approval, risk | "Because agents plan, persist, and delegate autonomously" | Agentic top 10, ASI08, page 30 | Confirmed |
| Human approval, control | "Utilise human-in-the-loop control" | LLM06, mitigation 6 | Confirmed |
| Human approval, control | "Require explicit authentication for each tool invocation" | Agentic top 10, ASI02, mitigation 2, page 14 | Confirmed |
| Human approval, control | "Draft pull requests created by Copilot cloud agent" | GitHub | Confirmed |
| Traceable handoffs, risk | "without clear visibility into what agents are doing" | Agentic top 10, Letter from the Agentic Top 10 Leaders, page 7 | Confirmed |
| Traceable handoffs, risk | "Administrators can lose sight of agents' work" | GitHub, heading text | Confirmed |
| Traceable handoffs, control | "It's the verifiable information about software artifacts" | SLSA | Confirmed |
| Traceable handoffs, control | "Record all inter-agent messages" | Agentic top 10, ASI08, mitigation 10, page 32 | Confirmed |
| Traceable handoffs, control | "Copilot cloud agent's commits are authored by Copilot" | GitHub | Confirmed |

## Gaps

- The quote check was a one-off script run during drafting. No reusable check for this page is in `scripts/`.
- NIST SP 800-218A was not read in full and is not cited.
- From the OWASP Top 10 for Agentic Applications 2026, the pages read in full are the letter (7) and the quoted parts of ASI01, ASI02, ASI03, ASI04 and ASI08 (pages 9 to 17, 20, 30 and 32). The other entries and the appendices were only skimmed. ASI04 to ASI07, ASI09 and ASI10 are not quoted.
- Page numbers for the agentic top 10 are the numbers printed in the page footer. The PDF viewer's page count is one higher.
