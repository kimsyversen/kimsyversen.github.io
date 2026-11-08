# Pilot test plan: Developer-WS2

Belongs to: [Developer-WS2.html](Developer-WS2.html)

Written 2026-11-06, cut to GitHub Copilot in VS Code the same day. Nothing here has been run. The page says "Nothing tested in a real tenant". This file is the test that would change that. Run it in a pilot group of one Windows laptop and one Mac, both enrolled in Intune, and fill in the Result column.

## How to run

1. Pick one harmless approved MCP server (call it A) and one unapproved one (call it B). Both must be easy to tell apart by name.
2. For each row: deliver the policy with Intune, wait for it to apply (or sync the device), restart VS Code, then try A and B in Copilot agent mode.
3. Pass means A runs and B does not. Write what you saw, not only pass or fail.
4. Then edit the delivered value by hand and see whether Intune puts it back (rows 7 and 8).
5. Before row 1: on the VS Code policy reference page, check the minimum version listed for the three MCP policies, and run Developer: Policy Diagnostics in VS Code to see which policies it reads.

## Tests

| # | Part | Platform | Deliver | Expected (from the page) | Result |
|---|---|---|---|---|---|
| 1 | VS Code allowlist | Win | ADMX import, ChatAllowedMcpServers with A only | A runs, B blocked | |
| 2 | VS Code denylist | Win | ChatDeniedMcpServers with B | B blocked even if also on the allowlist | |
| 3 | VS Code managed-only | Win | ChatAllowManagedMcpServersOnly | only the managed allowlist counts | |
| 4 | VS Code macOS profile | Mac | edit the sample .mobileconfig from the app, upload as an Intune custom profile | the sample holds the three MCP policies, A runs, B blocked | |
| 5 | Bad value | Mac | put a syntax error in a policy value | the setting is not applied, the Window log shows an error | |
| 6 | GitHub Copilot MDM | Win, Mac | native MDM values (strings) | A runs, B blocked, built-in GitHub server cannot be blocked | |
| 7 | Re-apply, Windows | Win | change a policy value by hand | Intune puts it back, or a remediation does | |
| 8 | Re-apply, macOS | Mac | remove the profile or edit a value | Intune puts it back | |
| 9 | Firewall | Win | Intune block-all-outbound with an allow rule for A's host | A's host reachable, B's host not | |
| 10 | Defender discovery | Win, Mac | none, read the portal | A and B both listed, with the start command for a local server | |
| 11 | Second copy | Win, Mac | install VS Code Insiders or a portable copy | record whether it reads the same policy | |

## Tests for the open cases

These are expected to show the gap. Record exactly what happens.

| # | Case | Steps | Expected | Result |
|---|---|---|---|---|
| 12 | Windows, interpreter allowed | App Control policy allows node.exe. Run a local MCP server B as `node server.js` from a client with no managed list | B runs (not blocked) | |
| 13 | Windows, interpreter left out | Remove node.exe from the policy. Repeat 12. Then try approved server A that needs node | B blocked, and A blocked too | |
| 14 | macOS, hash deny list | Add B's file hash as a Defender file indicator (block). Run B. Then change one byte of B and run again | first run blocked, changed file runs | |
| 15 | Other client, Windows | App Control allows only approved clients. Start an unapproved MCP client | client does not run | |
| 16 | Other client, macOS | Add an unapproved client's hash as a block indicator. Start it | blocked by hash only, a renamed or rebuilt client is not stopped | |

## What the results decide

- Rows 1 to 11 pass: the VS Code layer works as the page says.
- Row 4 settles the open macOS question (does the profile hold the MCP policies).
- Row 13 shows whether leaving the interpreter out is workable for developers.
- Rows 14 and 16 show how far a deny list gets on macOS.
- Row 15 decides whether the closed-client design holds on Windows. Without it, the design stays an inference.
- Move a statement from inference to tested only after its row has a result and the date it was run.
