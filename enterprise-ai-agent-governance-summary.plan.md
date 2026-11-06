# Plan: Enterprise AI agent governance, summary

Belongs to: [enterprise-ai-agent-governance-summary.html](enterprise-ai-agent-governance-summary.html)

Started 2026-11-06. Copy of the long page [enterprise-ai-agent-security-recommendation.html](enterprise-ai-agent-security-recommendation.html), cut down to one short page.

## Goal

The long page is too big to read. This page covers two things and nothing else:

1. How do we govern MCP servers in our enterprise? (figure from 2.4 of the long page)
2. What does the target state look like, as part of that governance? (figure "The five points on the target state")

Every answer says what we CAN do, what we CANNOT do and which tool does what. Automation and low admin work stay the main theme.

## Page order

1. Masthead: lead, scope, evidence, tenant tests.
2. How we govern MCP servers: the 2.4 figure, a traffic figure with path table (what is the end user client and what is not, D31), path 4 covers Defender local discovery (D32), four steps, risk tiers, action policy, server checklist. This is the main focus.
3. What we can and cannot do, route by route (matrix), with an evidence table of exact quotes.
4. Target state: the five-points figure, the five answers, which tool does which job.
5. Automation: what runs by itself, what a person still does, nine admin-saving rules.
6. Stop runbook: monitor and stop an agent.
7. Gaps: preview watchlist and the gaps.
8. Open questions: questions to settle (moved here from the top, see D23).
9. Sources, footer with the Made with AI note.

## Rules for this page

- Reuse figures, tiers, action policy, checklist, runbook and gap text from the long page without changing the claims. Only links are remapped.
- New prose (can/cannot matrix, automation table, open questions) uses wording that stays inside what the quotes say.
- No claim without a source link and a quote in the evidence table, or it is labelled `[unverified]` or `[inference]`.
- Paragraphs 60 words or fewer. No em or en dashes.
- localStorage: none used. If one is added, prefix `ags-`.
- Long page stays unchanged. This page links to it for the detail.

## Build

- `scripts/build-governance-summary.py` pulls the figures and blocks from the long page by marker and writes the new page. It fails if a marker is not found.
- `scripts/check-enterprise-agent-labels.py` takes the page path as an argument so it checks both pages.
- `scripts/check-evidence-quotes.py <cache-dir>` fetches each source and confirms each quote word for word. It also checks the page lists every quote.
- `scripts/governance_evidence.py` holds the quotes and sources.

## Steps

1. Notes (this file, decisions).
2. Build page.
3. Fact check file with verdicts, quote check and reviewed-text ledger.
4. Label checker passes on both pages.
5. Index entry n7, count 07, dates.
6. Check light, dark, 375px, links with real clicks, console.
