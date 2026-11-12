Belongs to: [MCP governance in a Microsoft ecosystem, interactive](mcp-governance-microsoft-interactive.html)

# Plan: MCP governance in a Microsoft ecosystem, interactive

## Goal

A new page from the content of `mcp-governance-microsoft.html`. Design and Controls become one interactive diagram of the MCP call path, modeled on the architecture diagram in `AKS-sikkerhetsvurdering.html`. The old page stays unchanged.

## Sections and their jobs (MECE)

| Section | Job | Holds | Does not hold |
|---|---|---|---|
| Design | Where each part sits and which control lives on it | The diagram, filters by layer and objective, one detail panel per box (what it is, where it is set, controls, product guardrails, preview additions) | Order of work, tests, gaps, approval steps |
| Rollout and tests | Order of work and acceptance tests for the released design | Steps, test table | Control wording (lives on the box) |
| Gaps | What the sources or the design leave open | One list | Controls, tests |
| With preview (preview view only) | Process and checks for the preview additions | Approval workflow (interactive), tests added, pilot | Preview controls (they live on their box, marked preview) |

Rule: a control has one home box. Cross references are links to the box (`#n-<id>`) or to the gap (`#gap-...`).

## Build

```bash
python3 -I scripts/build-mcp-governance-interactive.py
python3 -I scripts/check-enterprise-agent-labels.py mcp-governance-microsoft-interactive.html
python3 -I scripts/section_anchors.py --check
```

The builder writes the page and the quote table in the fact check. Quotes come from `scripts/mcp_governance_evidence.py`, shared with the old page.

## Steps

- [x] Study the AKS diagram and repo conventions
- [x] Define the structure
- [x] Build the page
- [x] Verify statements against quotes and record the result
- [x] Index entry, label ledger, browser checks

## 2026-11-12, redesign for portrait and color

Goal from the owner: make the page beautiful and interactive, with no sideways scrolling in portrait mode, and with color. Content must stay correct and nothing essential may be lost.

Approach:

- Replace the 1226 px wide SVG with an HTML diagram that reflows. Boxes are links in a CSS grid, top to bottom: 1 source of truth, 2 policy targets and clients (four lanes: target, client, what sits before the gateway), 3 gateway with logging and the preview route, 4 company server.
- Draw connectors in one SVG layer that the script computes from the box positions, so they follow the layout at every width. Without script the boxes still read in order.
- Color with meaning, not one color per step: amber for the policy plane (Git, pipeline, policy targets), blue for the call path (clients, device, gateway, server), red for blocked and preview, neutral for logging.
- Desktop: diagram on the left, sticky detail panel on the right. Phone: panel below the diagram, Previous and Next to step through boxes, and a link back to the diagram.
- New interaction: Follow a path (one per client, plus the preview route and the blocked direct call) lights the boxes and lines on that path. Filters keep working and show matching counts on each box.
- Keep every panel's text, ids and the shared builder content unchanged. Keep `#n-<id>` and `#ctrl-<id>` links working.

Steps:

- [x] Rewrite the diagram, styles and script in the builder
- [x] Restyle the rest of the page with the same palette, light and dark
- [x] Compare content with the old build: every control, part and note still present
- [x] Browser checks: 375 px, 768 px and desktop, both designs, filters, paths, shared links, console
- [x] Label check, anchor check, fact check log

## Holistic review completed (2026-11-12)

- [x] Review all control, part, gap, test and workflow wording against current primary-source passages.
- [x] Correct released/preview boundaries, manual target work, identity/authorization and BYO topology.
- [x] Align STRIDE bases and related controls; preserve public IDs and regenerate exports.
- [x] Run quote, label, anchor, local-link, JavaScript/JSON syntax and deterministic-build checks.
- [ ] Browser QA follow-up: desktop/narrow rendering, console, filters, paths and preview deep links. Blocked by locked native access and in-app browser local-file URL policy; see fact check. No tenant acceptance tests have been run.

Completion pass: added mixed-mode connector enforcement and preview discovery/retry limits, aligned STRIDE T9/T14, and reran all static/build/evidence checks successfully. Browser QA was attempted again; Chrome remained unavailable and the Mac was locked. The browser follow-up above remains blocked; design-stage content review is complete.

Final completion pass: source and logic review complete, including workload-specific ACP availability (V216) and remaining automation wording. Static, source-snapshot and reproducible-build checks pass. Browser QA was retried and remains environment-blocked; no tenant acceptance test is claimed.

Commit attempted on `dev`; the workspace denied creation of `.git/index.lock` because git metadata is read-only. Reviewed changes remain uncommitted. Nothing was published.
