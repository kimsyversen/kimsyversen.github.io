Belongs to: [enterprise-ai-agent-security-recommendation.md](enterprise-ai-agent-security-recommendation.md)

# Review decisions

## 2026-11-05

- Preserve the recommendation structure and existing URLs. Correct individual statements and contradictory summaries rather than replace the document.
- Treat vendor documentation as evidence of documented capabilities, not proof of tenant deployment or complete containment. Qualify diagrams, account scope, gateway paths, telemetry and preview features accordingly.
- Keep unknown first-start behavior explicit. A failed search does not justify calling undocumented behavior verified.
- Treat the Git-approved MCP list as the source of truth and publish it to each product's native policy. In Foundry, the preview Azure Policy can deny noncompliant tool configuration requests; do not describe that as runtime invocation control or removal of tools from existing agents. Use backend revocation or a supported gateway for runtime blocks, and validate tenant behavior.
- Retain the historical ledger and add a current section that supersedes conflicting findings. Source update dates are the dates displayed on the retrieved articles, not inferred publication dates.
- (Superseded.) Keep this as Markdown. No public HTML page, index entry or site styling changed.

## 2026-11-05, HTML page

- Publish an HTML page, [enterprise-ai-agent-security-recommendation.html](enterprise-ai-agent-security-recommendation.html), for stakeholders. This replaces the earlier "keep as Markdown" decision. The Markdown stays the source of record and keeps the full ledger.
- The page was generated from the Markdown once, then is maintained by hand as plain HTML. The site has no build step, and a generator would be one more thing to keep alive.
- Diagrams are hand-built inline SVG and HTML, not Mermaid. They follow the site look in light and dark and need no script or CDN. Mermaid in the Markdown is unchanged.
- Chosen pictures: the five layers with a feedback loop, a layered target state, the MCP approval flow with a kill path, a table of where the approved list is enforced, a risk-tier ladder, a release stepper, and a rollout gantt. Each one answers a question a stakeholder asks.
- Dense detail sits in collapsible blocks with an "Expand all detail" button. Everything is expanded when printed.
- Tags carry over: verified, recommendation, inference, unverified, preview. Red is used for caution only (preview, unverified, not tested).
- Paragraphs are split to 60 words or fewer. Words and facts were not changed to do this.
- The page is listed as entry 06 in the index. The index has no top sentence now, so only the list entry and the page count changed.
