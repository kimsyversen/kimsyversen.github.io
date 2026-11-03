# Decisions: fact check of the Developer Workstation Risk Map (Developer-WS.html), 1 Nov 2026

Belongs to [Developer-WS.html](Developer-WS.html), named `Developer Workstation Risk Map.html` when this work was done. Other notes for the same page: [plan](Developer-WS.plan.md), [fact-check ledger](Developer-WS.factcheck.md).

Working notes.

- Git claims kept as written. Re-ran them on Git 2.54.0 (Apple Git-157); every result matched the 29 Oct run on 2.43.0. Added the re-run date instead of replacing the old one.
- GlassWorm (D03 and map note): "every editor" changed to "other editors, such as VS Code, Cursor and Windsurf". Socket names those three; no source says every editor.
- GhostApproval (D08): "several of the six" changed to the named agents. Wiz shows a misleading file name in Claude Code and Augment, and a write before the prompt in Windsurf and Amazon Q. Naming them is shorter to check later than a vague count.
- Repo upload (D10): named Grok Build and the July 2026 Hacker News report (researcher cereblab, CLI 0.2.93). Moved the source out of the GitSpawn note, which is about a different article, into its own entry at the end of SOURCES so no source numbers shift.
- Gen Digital (review note): the figures count protected users with detections, not confirmed infections. The old wording ("users, not detections") read as if detections played no part.
- Managed settings (D09): "a file-based policy" changed to "the managed policy itself". A local admin can also edit the plist and HKLM forms.
- Read(./.env) (D04 and map note): anchored to the folder Claude Code started in, per Anthropic's permissions page. "Project root" only holds when Claude starts there. Added that Read(.env) covers every level below.
- Codex reads (D07): added "by default". requirements.toml has deny_read, so "does not limit reads" was too absolute.
- (Superseded in the second pass.) Forever Security (response section): cut the claim that sessions "ran the attacker's command" and the debate about "every session". Kept only what sources say: the planted file targeted Codex's own config, and Forever advises checking ~/.codex/config.toml.
- Evidence: removed the "Still open" item about GitHub's sandbox.userPolicy keys, since the keys are now confirmed. Added a 1 Nov entry.
- (Superseded in the second pass.) Left as is: "A planted AGENTS.md in Downloads was found on a real machine in October 2026" (D05 map note). It is the author's own observation and cannot be checked from a source. Named in the review section.
- ClawHavoc "more than 1,000 skills on ClawHub in early 2026" kept. OWASP AST01 gives 1,184 in January 2026; see the second pass for the ClawHub source.

## Second pass, 1 Nov 2026 (after the first summary)

- ClawHavoc (D06): Snyk's ToxicSkills post (5 Feb 2026) reports 76 confirmed malicious skills and does not name ClawHavoc, so it does not back "more than 1,000". OWASP AST01 gives 1,184 in January 2026 but does not name ClawHub. Antiy CERT (6 Feb 2026) says "at least 1,184 malicious Skills have historically appeared on ClawHub". Kept the sentence and added Antiy as a source.
- Planted AGENTS.md (D05 body and map note): Help Net (26 Oct 2026) confirms a real find on a Forever customer's computer in ~/Downloads, but gives no find date. Changed "found ... in October 2026" to "reported ... in October 2026". This claim is now checked, not left open.
- Forever persistence (response section): Help Net says Codex "first changed its own settings" and that every later Codex session then runs the attacker's command in any project. My first rewrite dropped that point and kept a config.toml detail that Help Net does not name. Now: "Codex first changed its own settings, which then applied to every later Codex session in any project."
- Shortening pass. Word counts before and after:
  - D06 Plugin4Shell paragraph tail: 188 -> 83. Dropped the CSA aside about Bitbucket and self-hosted Git, the [contested] wording on Anthropic's marketplace list, and the [unverified] Codex sentence.
  - D06 Codex checklist item: 106 -> 53. The open question about plugin-bundled servers stays in Evidence, "Still open".
  - D06 map note: 27 -> 17. Dropped the [unverified] Codex clause.
  - D08 GhostApproval: names of single agents replaced by "in some, the prompt named a harmless file or came after the write". It is shorter and still true if more agents are found.
  - D04 Read(./.env), D10 Grok Build, D03 GlassWorm and the Evidence and Review entries: trimmed back to about their original length or shorter.

## Coverage: what was checked, part by part

All parts of the page were read. "Source" means the claim was compared with the page named in Sources (or the vendor page) on 30 Oct to 1 Nov 2026.

- Header, In short, Before you use the map, priority intro: dates and incident counts against the cited incidents. Fixed the date line.
- Current box (npm, GitSpawn, Plugin4Shell, package firewall, Windows sandboxes): source, plus `npm view npm version` (12.2.1). Date moved to 1 Nov.
- Where to start (START, 10 items): setting names against vendor docs. No change.
- What a status means: definitions only, nothing to check.
- D01 packages: npm 12 docs, npm config precedence, ChainDrop, GitHub package firewall. No change.
- D02 code on open: VS Code tasks and trust docs; Git claims re-run on Git 2.54.0. No change.
- D03 extensions: Amazon Q advisory, Socket on GlassWorm, Open VSX defaults. Fixed GlassWorm.
- D04 secrets: Claude Code permissions page, GitHub managed settings, ssh-add. Fixed Read(./.env).
- D05 prompt injection: Help Net / Forever Security, VS Code instructions docs. Fixed the find date.
- D06 MCP, plugins, skills: MCP spec and best practices, CSA and Plugin4Shell write-ups, Antiy, OWASP AST01, Codex managed config. Shortened; source added.
- D07 sandbox and network: Claude Code, Codex and VS Code sandbox docs. Added "by default" for Codex reads.
- D08 approval bypass: CVE-2025-53773, Wiz GhostApproval, Claude Code permission modes. Fixed the GhostApproval detail.
- D09 inventory and telemetry: Defender DeviceProcessEvents schema, Claude Code managed settings. Fixed "file-based policy".
- D10 data to AI services: VS Code own-key note, Hacker News on Grok Build, VS Code account policies. Named Grok Build.
- More risks D11 to D17 (MORE, SHORT): Dev Tunnels policies, Unit 42, SentinelLabs, Forever browser share (Help Net: "about a quarter"), Mitiga, s1ngularity. No change.
- Diagram labels (ZONES, COMP, ARROWS): product and file names only. No change.
- Map notes (PLACE, 77 notes): each against the card it summarises. Fixed D03, D04, D05 and D06 notes.
- If something got in: Microsoft IR guidance, Help Net on token advice and persistence. Fixed the Forever sentence.
- Review tab (merge, review, audit, verification rounds, 29 to 30 Oct): these record past review passes. Read for consistency with the cards; fixed the Gen Digital note. They are a record of past changes, so the old wording in them was not rewritten.
- Evidence status: removed the outdated sandbox.userPolicy item; added the 1 Nov entry.
- Sources: 62 entries. Fixed the GitSpawn note; added Grok Build and Antiy CERT.
- Footer: Git re-run date added.

Not checkable from a source: the priority order, owners per zone and friction estimates. The page already marks these as judgement.

## Pass 5, 1 Nov 2026: shortening and stale review notes

- Restore incident (earlier in this pass): a helper script was given the page path as its output file and overwrote the page. Restored from the backup, re-applied passes 4 and 4b and the D07 wording, and confirmed the lines and data matched. The helper now refuses an .html output path.
- Shortened 21 long paragraphs and checklist items by cutting, not rewording claims. Word count of those lines: 1,686 -> 1,423. D04 checklist: 298 -> 270. Biggest cuts: diagram caption 105 -> 75, D06 split into two paragraphs, D07 checks 65 -> 44 and 81 -> 57, D04 VS Code item 51 -> 30.
- Dropped, not changed: the caption sentence on Read/Edit and Docker (the diagram arrows still show it), "Score your own fleet", the Codex "trusts Downloads" clause, the GitHub token types in ChainDrop, the Gen Digital item list, the ssh "cooperating client" note, the chat.mcp.access value lists (still in Evidence, Still open).
- Review tab: three notes described text that later changed (Codex [unverified] tag, the caption's MCP authorisation sentence, Plugin4Shell "contested"). Put them in the past tense and said where the point lives now. Added one line to the 1 Nov list.
- (Superseded.) The items left open here were done in passes 6 to 8 and the ledger; see below.

## Pass names

The notes above use different names for the same passes. In Developer-WS.factcheck.md: pass 1 is the "first pass" (apply.py), pass 2 the "second pass" (apply2.py, apply3.py), pass 5 is "Pass 5" (pass5.py and the restore).

## Pass 3, 1 Nov 2026: shortening

- Shortened 33 long body paragraphs by cutting clauses, not rewording claims.

## Pass 4, 1 Nov 2026: map notes and data arrays

- Fixed four map notes against their sources:
  - D02 (PLACE[9]): split GitSpawn from Check Point's finding (CVE-2025-59536). They are different findings.
  - D06 (PLACE[27]): cut "must ... bind to localhost and authenticate". The MCP spec says must for Origin, should for localhost and auth.
  - D06 (PLACE[30]): "should accept only tokens issued for them" changed to must, plus must not pass tokens on (MCP authorization spec).
  - D06 (PLACE[31]): VS Code has no plugin marketplace lock (it has ChatEnabledPlugins); Codex added to the MCP allowlist list.
- Trimmed MORE, EVIDENCE and other PLACE notes.

## Pass 6, 1 Nov 2026: list splits and data trims

- Split long Review lists into one line per item. Trimmed MORE[0], MORE[2], EVIDENCE[0] and PLACE[30].

## Pass 7, 1 Nov 2026: Sources list

- SOURCES[6] OWASP MCP Top 10: ID range is MCP01 to MCP10, beta.
- SOURCES[21] The Register: research credited to Air Security, as the article says.
- SOURCES[24] Mitiga: date corrected to 5.5.2026.

## Pass 8 and the ledger, 1 Nov 2026

- Wrote Developer-WS.factcheck.md: one row per statement (968), with the source key, verdict, the pass that changed it, and a before and after log of every changed sentence. Chose a generated table over hand-written notes so every row is covered exactly once; the script fails if a row is missing or doubled.
- Checked the last NOT CHECKABLE row: code.claude.com/docs/en/settings-example exists and its managed example sets the keys the Sources note names. Now OK.
- Pass 8: split the one remaining 63-word Review sentence (Source corrections, 30 October) into an intro and six list items. Same words.
- Left alone: the `claude:viewport-fit-sides` meta tag that the watermark hook flags. It was there before this check and is outside its scope.
- Checks after pass 8: data arrays parse (only the three known ZONES, SHORT and DESC parse quirks of the dump helper), no em or en dashes in the page or notes, page renders with 4 tabs, 62 sources, a working map popover and no console errors.
- (Superseded by pass 9.) Statement length after pass 8: median 11 words; 10 statements over 35 words.

## Pass 9, 1 Nov 2026: paragraph length

- Why: sentences were short, but some paragraphs were not. Measured whole text blocks, not sentences: paragraphs, list items, table cells, caption rows and legend labels. Code samples are not counted.
- Rewrote the measuring script (paralen.py) with an HTML parser. The first version used a regex: it skipped the first item of each nested list and counted code samples and the whole diagram legend as prose. That is why it reported the diagram caption at 115 words; the caption text itself was 75.
- Target: no block over 60 words. Before: 230 blocks, longest 91, 19 over 60, median 24. After: 240 blocks, longest 60, none over 60, median 24. Total words 6,473 -> 6,387.
- Rendered check in the browser, including text built by the page script (map notes, More risks, Review lists): 468 blocks, longest 60, none over 60. The More risks control text (MORE[0].c) was 60 words in the data but 63 with its "Control in full:" label, so three words were cut ("protected", "that", "the").
- Longest data field (More risks, map notes, Evidence, Review, Sources): 58 words. ZONES, SHORT and DESC, which the dump helper cannot parse, top out at 23.
- Method: split ten long blocks at sentence breaks without changing words: the diagram caption and one paragraph in each of D01 to D09 (in D04 the infostealer sentence also moved up a paragraph). Cut words in ten blocks: Top 10 intro, status definitions, two D07 checks, D10, response step 2, Review intro, audit intro, Sources intro and More risks D11 (MORE[0]).
- Dropped, not changed: "Record who collected what, and when." (response step 2) and "Status is stored only in this browser" (Top 10 intro; the status definitions still say it). Re-checked the storage claim in the page code: status is read and written with localStorage, and the page makes no network calls.
- D04 card: 13 blocks, longest 52 words, 378 words in all. Its checklist is 9 items (6 top-level, 3 nested) of 10 to 52 words, 264 words in all. An earlier "about 365 words" figure came from a quick count that mis-nested the list; it was wrong.
- Ledger: 965 rows (was 968) because three pairs of sentences were joined. Each changed row has a "Pass 9:" note with the old wording. Verdicts: 403 OK, 35 FIXED, 18 CUT, 147 JUDGEMENT, 104 RECORD, 53 QUESTION, 205 UI.
- Statement length after pass 9: median 12 words, longest 56; 10 statements over 35, 3 over 45.

## Pass 9b, 1 Nov 2026: last unchecked sources

- Why: The Hacker News blocks scripted fetches (403), so three of its articles had been checked only through search results and mirrors. The GitSpawn day was marked NOT CHECKABLE.
- Read all three in the built-in browser on 1 Nov 2026.
- GitSpawn (Sources: "The Hacker News (2.9.2026)"): the article is dated Sep 02, 2026 and names Manifold Security. The date on the page was right. No change.
- Grok Build: dated 14 Jul 2026, researcher cereblab, version 0.2.93. Matches the page. No change.
- IDEsaster: the headline is "Researcher Uncovers 30+ Flaws in AI Coding Tools", one researcher (Ari Marzouk), dated 6 Dec 2025. The page said "Researchers uncover". Fixed to "Researcher uncovers". This is the 35th correction.
- No ledger row is NOT CHECKABLE now. Verdicts: 403 OK, 35 FIXED, 18 CUT, 147 JUDGEMENT, 104 RECORD, 53 QUESTION, 205 UI.
- Re-ran the checks after the fix: source 240 blocks, longest 60, none over 60. Rendered page, counting each block's own text without nested lists or code: 475 blocks, longest 60, none over 60, no console errors.

## File names, 2 Nov 2026

- Renamed the notes to `Developer-WS.plan.md`, `Developer-WS.decisions.md` and `Developer-WS.factcheck.md` so they match the page, now `Developer-WS.html`. Chose the page name as a prefix over a subfolder: the page keeps its URL, and the notes sort next to it.

## 3 Nov 2026, "Made with AI" note

- **Plain label and one sentence at the end of the footer**, under a hairline rule, in the page's own muted and ink colours. Chose this over a pill or badge to keep it quiet and avoid the template look. Colours use the page tokens, so dark mode follows.
- **Wording:** "This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human." Same text on all five pages.
- **Layout:** label and text in two columns on desktop, stacked under 560 px.
