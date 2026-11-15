# Agentic DevSecOps: fact check

Checked: 15 November 2026

## Scope and verdict

All 13 quotes on `agentic-devsecops.html` were found word for word in the source pages fetched on 15 November 2026. Straight quotes in the sources are shown as typographic quotes on the page.

## Interpretation by AI

- The eight phases, the agent task in each phase, and every input and output are interpretation by AI. No source prescribes this flow.
- The three human gates are a recommendation. The sources support human approval of high-impact actions in general.
- Grouping the sources into four changes, and the wording of each risk and control summary, is interpretation by AI.
- The sources describe LLM applications, one vendor's coding agent, and build provenance. None of them describes this eight-phase flow.

## Links

The 12 text links were opened in a browser on 15 November 2026 and land on the quoted passage. The heading link's anchor id was confirmed in the page source, not opened. The GitHub page was fetched at `/copilot/concepts/agents/cloud-agent/risks-and-mitigations`, which redirects to the address below. The heading quote links to the heading's own anchor, because a text link matched the page's side menu first.

## Sources

| Source | URL | Version status |
|---|---|---|
| OWASP Top 10 for LLM Applications 2025, LLM01 Prompt Injection | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 2025 list, current on the site |
| OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency | https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ | 2025 list, current on the site |
| GitHub Docs, Risks and mitigations for Copilot cloud agent | https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations | Living page, no version number |
| SLSA 1.2, Provenance | https://slsa.dev/spec/v1.2/provenance | Status: Approved |

## Quote review

| Row | Quote starts | Source | Verdict |
|---|---|---|---|
| Untrusted input, risk | "Indirect prompt injections occur when" | LLM01 | Confirmed |
| Untrusted input, risk | "Users can include hidden messages in issues" | GitHub | Confirmed |
| Untrusted input, control | "Separate and clearly denote untrusted content" | LLM01, mitigation 6 | Confirmed |
| Untrusted input, control | "Comments from users without write access" | GitHub | Confirmed |
| Agent access, risk | "Excessive Agency is the vulnerability that" | LLM06 | Confirmed |
| Agent access, control | "Limit the permissions that LLM extensions" | LLM06, mitigation 4 | Confirmed |
| Agent access, control | "Copilot cloud agent only has the ability to push" | GitHub | Confirmed |
| Human approval, risk | "The root cause of Excessive Agency is typically" | LLM06 | Confirmed |
| Human approval, control | "Utilise human-in-the-loop control" | LLM06, mitigation 6 | Confirmed |
| Human approval, control | "Draft pull requests created by Copilot cloud agent" | GitHub | Confirmed |
| Traceable handoffs, risk | "Administrators can lose sight of agents' work" | GitHub, heading text | Confirmed |
| Traceable handoffs, control | "It's the verifiable information about software artifacts" | SLSA | Confirmed |
| Traceable handoffs, control | "Copilot cloud agent's commits are authored by Copilot" | GitHub | Confirmed |

## Gaps

- The quote check was a one-off script run during drafting. No reusable check for this page is in `scripts/`.
- NIST SP 800-218A and the OWASP Top 10 for Agentic Applications 2026 were not read in full and are not cited.
- The risk summaries for "Human approval" and "Traceable handoffs" rest on one passage each.
