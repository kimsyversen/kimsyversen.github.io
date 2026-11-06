Belongs to: [enterprise-ai-agent-security-recommendation.html](enterprise-ai-agent-security-recommendation.html)

# HTML presentation plan

Goal: show the content of [enterprise-ai-agent-security-recommendation.md](enterprise-ai-agent-security-recommendation.md) as a structured page that stakeholders can read quickly, with diagrams that carry the main ideas.

## Scope

- Content comes from the Markdown. No claim is added, removed or reworded on purpose, except splitting paragraphs to 60 words or fewer.
- Look follows `threatmodelling.html`. Red means caution only.
- Plain HTML, inline CSS and JS, no build step on the site.

## Page structure

1. Summary and the five layers, with the feedback loop.
2. Where the approved list is enforced and where it is not.
3. Four things that will surprise people.
4. Target-state diagram.
5. Part 2 sections 2.2 to 2.9, each with a short "at a glance" view and collapsible detail.
6. Part 3 admin effort, Part 4 rollout (gantt), Part 5 known gaps.
7. Sources table (82 rows).

## Diagrams

- Layered target state (SVG).
- MCP approval flow with kill path (SVG).
- Five-layer row with feedback loop.
- Risk-tier ladder, release stepper, rollout gantt, preview watchlist.

## Checks before done

- Light, dark and 375px. No sideways scroll, no console errors.
- No em or en dashes. Paragraphs of 60 words or fewer. Made with AI note present.
- Index entry added, index checks pass.

## How the HTML is made

A script in the session scratchpad turned the Markdown into the page body and filled a hand-built template. The output was committed as plain HTML. After that, edit the HTML by hand. The script is not kept in the repo.

## Part 6, technical guide (2026-11-06)

Request: split the document into an overview (what it says) and a technical part (what you actually do). Input: ten photos of a Copilot answer about MCP security, used as a topic list only.

- Parts 1 to 5 stay as the overview. Part numbers and ids do not change.
- New Part 6 "Technical guide: what you actually do" (`#part6`, nav "Technical guide"), placed after Part 5 and before Sources.
  - 6.1 Eight controls in order: Discover, Register, Authenticate, Authorize, Broker, Restrict, Approve, Monitor. One table, each row links to the Part 2 section that holds the product settings.
  - 6.2 Figure: the request path. Labels and requirements only. Boxes link to the control rows.
  - 6.3 Steps per control, each step tagged. Vendor facts point to numbered evidence.
  - 6.4 Registry record: 17 fields, marked recommendation, with who reads each field.
  - 6.5 Log record per tool call, with what the Global Secure Access MCP log gives today and what it does not.
  - 6.6 Limits: what the controls do not see, and what was not checked.
  - 6.7 Evidence: numbered claims, exact quotes, links. Quotes are checked word for word against fetched pages.
- Header: say which parts are overview and which is technical.
- Sources: add the new pages to the table, with the 6 Nov 2026 read date.
- Not on the page: anything from the "EY deck" the photos mention. It is not in our sources.
- Done when: quotes match mechanically, light, dark and 375px checked, every in-page link works, index entry updated.


## Reader paths and pilot (2026-11-06)

- Give decision makers the pilot decision, developers the remote MCP guide and operations the stop procedure.
- Use one case-search example from summary to pilot. Keep the three kinds of approval distinct and document the chosen low-risk rule exception.
- Keep the Git publication requirement. Report discovery, configuration and invocation enforcement as separate outcomes. Maintain one matrix per client route.
- Keep the site styling and shared IDs. Use stacked reading paths at 375 px and leave wide detail available as a reference.
- Verify anchors, disclosures, representative mouse clicks, light and dark layouts, and the wording ledger. A reader test with people in the three roles is a separate follow-up.


## Discussion diagrams (2026-11-06)

- Open the body with the full technical target-state diagram and keep the 2.1 anchor.
- Show the MCP approval and publication diagram in 2.4. Keep rejection, publication by destination, enforcement checks, monitoring and revocation visible.
- Keep the short text paths below both diagrams. At narrow widths scroll the diagram within its own region.


## Five points diagram (2026-11-06)

- Goal: one diagram in Part 1, built on the 2.1 target state, that lets a reader see all five points of "The answer in one minute" in about a minute.
- Layout: left column "Policy changes in Git" (repository, approved pull request, automatic publication, verify deployed policy). Right column keeps the target-state layers top to bottom: people and devices, Entra, agent platforms, agent actions, tool access, data, audit. A bus line carries the published policy from Git into each layer. Audit feeds a read-back arrow into the verify box.
- Numbers 1 to 5 sit on the matching layers: 1 agent platforms, 2 tool access, 3 managed cloud desktop, 4 Entra identity and agent actions, 5 Git column and verify.
- Text is labels and design requirements only. No product behaviour claims. Each text gets a verdict in the factcheck ledger and the script must pass.
- Place: inside the Part 1 block, after the numbered list. Ids: `five-points`, `t-five`, `d-five`.
- Done when: script passes, light, dark and 375px checked, no console errors, index dates updated.

## 2026-11-06, QA of the 2.1 diagram

Belongs to [the page](enterprise-ai-agent-security-recommendation.html). Compare 2.1 with the rest of the page, add what is missing at the same detail level, keep ids and links, update the ledger. Done: see decisions of the same date.
