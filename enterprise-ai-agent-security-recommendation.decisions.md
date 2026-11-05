Belongs to: [enterprise-ai-agent-security-recommendation.md](enterprise-ai-agent-security-recommendation.md)

# Review decisions

## 2026-11-05

- Preserve the recommendation structure and existing URLs. Correct individual statements and contradictory summaries rather than replace the document.
- Treat vendor documentation as evidence of documented capabilities, not proof of tenant deployment or complete containment. Qualify diagrams, account scope, gateway paths, telemetry and preview features accordingly.
- Keep unknown first-start behavior explicit. A failed search does not justify calling undocumented behavior verified.
- Treat the Git-approved MCP list as the source of truth and publish it to each product's native policy. In Foundry, the preview Azure Policy can deny noncompliant tool configuration requests; do not describe that as runtime invocation control or removal of tools from existing agents. Use backend revocation or a supported gateway for runtime blocks, and validate tenant behavior.
- Retain the historical ledger and add a current section that supersedes conflicting findings. Source update dates are the dates displayed on the retrieved articles, not inferred publication dates.
- Keep this as Markdown. No public HTML page, index entry or site styling changed.
