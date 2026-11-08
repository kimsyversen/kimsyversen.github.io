# Plan: Developer-WS2, Intune and MCP servers

Belongs to: [Developer-WS2.html](Developer-WS2.html)

Started 2026-11-06. Follows [Developer-WS.html](../Developer-WS.html) (card D06, MCP checks) and reuses the route matrix, Defender, Global Secure Access and firewall evidence from the enterprise agent governance pages.

## Goal

Find a working way to use Intune to govern MCP servers on managed developer workstations. Scope since 2026-11-06: GitHub Copilot in VS Code is the only MCP client (D21). Every statement must be correct, so every claim has a quote, a link and a date, or is labelled `[inference]` or `[unverified]`.

## Finding that shapes the page

Intune has no MCP setting of its own. It delivers each client's own managed policy (registry key, macOS profile, file) and can check that the policy is still there. The client does the blocking. A network layer and Defender discovery cover what the clients cannot.

## Page order

1. Masthead: goal, scope, status (nothing tested in a real tenant).
2. Answer and the seven layers (the last two are App Control and the macOS file hash list, added later).
3. Copilot in VS Code table: VS Code on Windows (ADMX), VS Code on macOS (profile), GitHub Copilot's own policy.
4. Delivery methods in Intune (ADMX import, macOS custom profile).
5. Drift and tampering.
6. Network and detection.
7. Open gaps.
8. Rollout steps.
9. Evidence table (exact quotes, links that open at the quote), how it was checked, footer with the Made with AI note.

## Rules

- Claim text carries evidence chips. All other text is a requirement or a label and sits in the reviewed-text ledger in `Developer-WS2.factcheck.md`.
- No quote may contain an em or en dash.
- Paragraphs 60 words or fewer. No em or en dashes on the page.
- localStorage: none used. If one is added, prefix `ws2-`.
- No colored bars on cards, no rounded shadow cards, no gradient banners. Look follows `threatmodelling.html`.

## Build

- `scripts/developer_ws2_evidence.py` holds sources and quotes. It reuses the Microsoft sources already checked for the governance summary.
- `scripts/build-developer-ws2.py` writes the page and the ledger block.
- `scripts/check-developer-ws2.py <cache-dir>` fetches each source, finds each quote word for word, checks the page lists it, checks the ledger matches the page, checks the fact-style wording rule and the 60 word rule.

## Steps

1. Notes (this file, decisions).
2. Evidence module and quote check.
3. Build page.
4. Fact check file with verdicts and ledger.
5. Index entry, footnote, dates.
6. Check light, dark, 375px, real clicks on evidence links, console.
