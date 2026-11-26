# MCP server intake: decisions

2026-11-26. All are choices by AI, made while building to the requested goal.

1. **Nine stages in a fixed order.** Desk checks come before any download, file checks before any execution, and first execution happens only in an isolated sandbox. Reason: scanners that read tool lists can start the server.
2. **One approval record per server is the baseline.** A change is any difference from it. Reason: client allowlists match names, URLs or commands, so something else has to notice content changes.
3. **Checks have one home.** Stages, triggers, scenarios and coverage refer to checks by id.
4. **Basis shown per check.** A check either quotes a source or is a plain requirement. Statements that are AI interpretation carry the `inference` tag.
5. **No dependency on the preview MCP Registry or preview platform features.** They are mentioned with a `preview` tag only.
6. **Interactive HTML flow, no separate ASCII figure.** The flow is a set of buttons and panels in the page text, so it is its own text description. A second copy in ASCII would duplicate it.
7. **All text is in the static HTML.** Script only shows and hides. Without script, everything is visible.
8. **No browser storage.** State lives in the URL hash.
9. **Risk tiers are capability based.** The tier follows what the server can do, not who asks.
10. **Recommended cooling period for new versions: 7 days**, skipped for a fix to an exploited vulnerability. It is advice, not a sourced threshold.
