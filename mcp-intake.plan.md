# MCP server intake: plan

Page: `mcp-intake.html`. Started 2026-11-26.

## Goal

An intake process for MCP servers covering publisher checks, traditional and MCP-specific scans, onboarding, and reassessment. The guide opens with a four-stage interactive diagram. Each action expands in place and links to its detailed reference. The full evidence review is complete when two consecutive passes find no incorrect or incomplete statement.

## Scope

In: any MCP server (local package, local container, remote) from first request to retirement.

Out, and said on the page: vetting the MCP client or host, model-level prompt injection defences at run time, agent design.

## Sections and their jobs

| Section | Job |
|---|---|
| Start here | Four actions for reviewing, approving and monitoring a server |
| Process | The detailed procedure in nine stages |
| When something changes | Triggers, how each is detected, what runs again, what stays in use meanwhile |
| Walk through a case | Worked scenarios through the stages |
| Checks | Minimum checklist, full check requirements, pass conditions, fail actions, scope, and basis |
| Coverage | Vulnerability classes, checks that address them, what can still get through |
| Risk tiers and decisions | Tier rules, who decides, exceptions |
| Approval record | What is pinned and compared later |
| What the platform enforces | Enforcement points and what each does not check |
| Not covered | Exclusions and unknowns |

## Build

1. `scripts/mcp_intake_data.py`: sources, quotes, stages, checks, triggers, scenarios, coverage.
2. `scripts/build-mcp-intake.py`: writes the page and the ledger of statements.
3. `scripts/check-mcp-intake.py`: quotes exist in the sources, links and anchors resolve, ids resolve, every MCP01 to MCP10 is mapped, no dashes.
4. Browser test on desktop and narrow.
5. Persona review passes until two in a row are clean, recorded in `mcp-intake.factcheck.md`.
6. Add to `index.html`, commit on `dev`. No push.
