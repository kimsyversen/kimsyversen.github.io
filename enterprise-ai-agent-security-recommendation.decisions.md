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
- (Superseded by the automatic publishing decision below.) Add "How the list reaches step 4" to section 2.4, in the page and the Markdown. A reader asked what makes the approved list reach each product by itself. The sources show an automatic path only for GitHub. For Agent 365, Foundry and API Center the table says so and marks the Git pipeline as our recommendation, not a product feature.
- Add a key under the 2.4 figure. Red dashed means a preview feature or the kill path, grey dotted means catalog only. The figure had no key before.
- Agent 365 registry boxes are now plain, not red dashed, in the target-state and 2.4 figures. Agent 365 is generally available. Only the bring-your-own MCP part is preview (Microsoft page checked 2026-11-05), so each box carries a small note saying that. Red dashed stays for whole preview features such as the Foundry tool policy and gateway.
- Step 1 of the 2.4 figure now says the request is made in GitHub (a pull request), in the page and the Markdown diagram. The pull request is where the checklist and review happen, and it needs to be clear it is not a ticket tool.
- Add "If VS Code is managed by Intune" under the 2.4 propagation table, in the page and the Markdown. A reader asked how Intune changes the setup. It is a short list, not a new figure, because it only affects the VS Code path. The main risk it names is two lists that differ, since MCP allowlists intersect across layers.
- Split the "one source of truth" Intune bullet in two after rechecking the vendor pages. The intersection rule applies to the GitHub MDM key `allowedMcpServers`. For a VS Code device policy, the Copilot setting wins and nothing is merged. The first wording blended them and would have misled an admin.
- Tag the 2.2 "Managed devices must be compliant" row as verified. It had no tag, and the Conditional Access grant controls page names the Intune compliance control.
- Make 2.4 say that publishing to step 4 is automatic, as a requirement. The owner ruled out copying the list by hand. The table now lists the automatic path per product instead of "by hand" or "your own build". Where the sources do not show an automatic step, the row says so and carries unverified. This replaces the earlier wording that only the GitHub path was automatic.
- The automatic route for Agent 365, API Center and Foundry runs through one pipeline job: register approved servers in Azure API Management, and write the Foundry Azure Policy assignment. API Management is the hub because its MCP servers can be created from REST API, ARM, Bicep, Azure CLI or Terraform, Agent 365 Tools Gateway discovers servers from it, and API Center syncs from it. The pipeline job itself is a recommendation and was not tested.
- Use the Agent 365 Tools Gateway (preview) route in the figure and table, not the bring-your-own request flow. The request flow needs a CLI step and an administrator approval, so it cannot be automatic. The Agent 365 box stays solid with a preview note, now "Tools Gateway is preview".
- Keep the Agent 365 allow or block step visible as a gap. The gateway page says an administrator applies it per server. No source shows it done by pipeline, and none says whether a newly found server starts allowed or blocked. Labelled unverified, with "Test that first".
- Step 4 label in the figure now reads "PUBLISHED AUTOMATICALLY". It is a design requirement, not a product claim. Box text in the figure was shortened to labels. The claims sit in the table, with tags and sources.
- Foundry box stays red dashed. Its tool policies are preview and the pipeline step is untested.
- Intune stays a gap: no source describes feeding Intune from Git, and it was not researched. It is labelled unverified in the note. The GitHub path already reaches VS Code automatically.
