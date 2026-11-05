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
7. Sources table (78 rows).

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
