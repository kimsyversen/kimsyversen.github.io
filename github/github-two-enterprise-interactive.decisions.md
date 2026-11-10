Belongs to: [GitHub two-enterprise reference](github-two-enterprise-interactive.html)

# Decisions

## Diagram checks

- After changes to diagram navigation, test each filter, open every highlighted box, and follow every source, Part of, and Related link. Confirm that sources load and that internal links leave the expected filter, popup, and URL hash. Use real clicks for a sample.
- Open shared `#f=` and `#n=` links directly to check that they restore the expected filter or box. Record the checks and any gaps here or in the fact check.

## 5 November 2026

- Keep the two-enterprise github.com baseline and clarify that the other hosting choices apply to A only. B uses personal accounts and public repositories, incompatible with GHE.com.
- Replace unsupported Well-Architected deviation attributions with design-choice explanations. Keep the existing node and filter IDs so saved links still work.
- Put primary-source links beside relevant popover text and record every box field and description sentence in a page-specific fact check. Leave the older drawings untouched and label their links as earlier versions.
- Distinguish proposed requirements, documented capabilities and explicit inferences. Acceptance checks are not tenant test results.
- Use plain borders and one accent according to the repository style rules. Split description paragraphs at sentence boundaries to keep them within 60 words.
- At phone widths, stack the existing controls vertically to make all labels readable without horizontal scrolling. Desktop structure, node IDs and filter IDs remain unchanged.
- Fix: Related links in a popup closed the popup instead of opening the related box. openPop() rebuilds the popup during the click, so the outside-click handler found the clicked button detached and treated it as an outside click. The handler now uses the event path captured at dispatch (5 Nov 2026). Tested: 15 filters, 288 filtered popups, 150 Part of links, 1035 Related links, 504 source links (49 unique URLs, all HTTP 200).

## 5 November 2026: every claim verifiable in the popup

- Each sentence in a popup description (and in the four design-choice notes) is one of three kinds. A design requirement or label needs no source and shows no number. A sourced fact (D) gets a number, and the Evidence list under the text holds the exact quote and a link that opens the source at that passage. An inference starts with "[inference]" and shows an Inference tag. Reason: AGENTS.md rule 3 says a box-level source list is not enough, so the reader must be able to check each claim in a few clicks.
- Evidence lives in `github-two-enterprise-interactive.evidence.tsv` (box, sentence start, kind, source, quote) and is copied into the page by `verify-evidence.mjs --write` as an inline block. Reason: no build step, one file for readers, one editable table for authors. The script fails if the inline block differs from the table.
- `verify-evidence.mjs` fetches every source and checks each quote word for word after normalising curly quotes, dashes, spaces and HTML entities. It also checks that each sentence start matches exactly one sentence, that every `[inference]` sentence has an I row, that each D source is on that box's source list, and that paragraphs stay at 60 words or fewer. Last run: 62 sourced, 12 inference, 256 design requirement or label sentences; 90 quotes checked against 33 pages; OK.
- The link uses a text fragment (`#:~:text=start,end`) built from the first and last words of the quote. Not every browser highlights it; Firefox and Safari support varies. The quote is on the page either way, so the claim stays checkable. Highlighting was confirmed once in Chrome (docs.github.com SAML page, 5 Nov 2026); Firefox and Safari were not tested.
- Sentences that overreached their source were reworded or split instead of sourced. Examples: "Multi-tenant SaaS" became "Standard GitHub Enterprise Cloud"; "Linux/Windows" became "Ubuntu/Windows"; SCIM deprovisioning now says "suspends the account; it does not delete it"; the PAT sentence no longer claims revocation of existing tokens.
- Summary lines, chips and "Proposed check" texts are design requirements or test steps (summary lines were finished later the same day, see "no facts outside the descriptions"). Four check texts carried facts without a source (IdP-only suspension, public organization metadata, token age criterion, hosted runner internet access) and one carried a push-protection limit. The first four were reworded to plain test steps. The push-protection limit moved into the description as a sourced sentence.
- The four design-choice notes are now rendered inside the description flow, with numbers and evidence, and are checked as pseudo boxes DEV.1 to DEV.4.

## 5 November 2026: test log for the evidence change

- Quote check: `node github/verify-evidence.mjs` passed (62 sourced, 12 inference, 256 design requirement or label; 90 quotes against 33 pages). Mutation check: changing one word in one quote made it fail ("QUOTE NOT FOUND"), and restoring the table made it pass again.
- Clicks, paced at about 110 ms: all 106 boxes opened with the right `#n=` hash, and all 414 Part of and Related links in those popups opened a box with the right title and hash. 0 failures.
- A first, faster run reported 99 failures. All of them were stale hashes: Chrome logged "Throttling navigation" and ignored the `replaceState` calls. No popup failed to open and no link went to the wrong box. Slower pacing removed every failure. A person clicking by hand cannot reach that rate.
- Real mouse clicks: opened box A.p3 under the build filter, then clicked its Related link "source (private)". It opened A.o1.src with hash `#n=A.o1.src`.
- Saved links: a fresh load of `#f=fl%3Abuild` restored the build filter (14 boxes on, one chip pressed, no popup). A fresh load of `#n=B.p15` opened the right popup with its evidence list and selected the right box.
- Source links: text-fragment link on the docs.github.com SAML page scrolled to and highlighted the quoted passage in Chrome.
- Dark and light mode, 332 px wide pane: popup text, evidence quote, links, number badge and Inference tag all had contrast 6.09 or higher (light) and 7.09 or higher (dark). Page width 317 px in a 332 px viewport, so no sideways scroll. No console errors. The screenshot tool could not paint (window minimized), so this was read from computed styles, not looked at.
- Not tested: Firefox and Safari; a real mouse click on every link (script clicks covered the rest); source pages changing after 5 Nov 2026 (re-run the verifier before moving "Current as of").

## 5 November 2026: no facts outside the descriptions

- The Stop-hook review found that card summaries still stated product facts with no number. The facts sat in the descriptions with evidence, but the card face repeated them without it.
- Decision: text outside a description (card summaries, titles, chips, flow steps, flow banners, page lead) holds design requirements and labels only. A product fact lives in a description, where it gets a number and a quote. Reason: those places have no evidence list, and AGENTS.md rule 3 wants every claim checkable from the diagram.
- Reworded: A.scim ("IdP groups drive enterprise teams. Keep managed users inside the enterprise."), B.scim ("Use per-org SAML, not enterprise SAML. Keep personal accounts."), B.idp ("The IdP owns provisioned membership"), B.v3 ("Do not claim full visibility of public activity.") and the page lead ("B stays on github.com for public work"; the fact that GHE.com has no public repositories is sourced in the g2 description).
- `verify-evidence.mjs` now scans 162 such texts for fact-style wording (cannot, does not, supports, syncs, never, always, by default, requires, available, automatic, enforces, prevents) and fails on a hit. Mutation check: putting "cannot contribute outside the enterprise" back into the A.scim summary made it fail. This is a wording guard, not a proof; a reviewer still decides what counts as a requirement.
- Not checked by the guard: the wording of proposed checks (`v`). They state expected test results ("Expected: it will not merge"), which are design requirements, and nine contain words like "cannot" for that reason.
- (Superseded.) The earlier line "Not done: summary lines still repeat some facts" is closed by this decision; it was removed from the section above when the gap was closed.

## 5 November 2026: every outside text has a recorded review

- Problem: the wording guard (a word list) is only a heuristic, and it did not look at proposed checks, source titles, filter labels, legend or page text. Nothing proved that each such text had been looked at.
- Decision: `github-two-enterprise-interactive.outside.tsv` lists every text outside the descriptions with a verdict. R is a design requirement or test step. L is a label, title or interface text. N is a code token that is never shown. `verify-evidence.mjs` finds the texts itself (string literals in the page script, plus the static page text and title attributes) and fails when a text is missing from the list or the list holds a text that is gone. A changed wording therefore fails until it is reviewed again.
- Scope today: 610 texts (R 123, L 274, N 213). Descriptions are not in this list; they have their own evidence rows.
- Limit: the check proves a verdict is recorded for the exact current wording. It does not prove the verdict is right. The verdicts were assigned by the AI that edited the page, and a person has not reviewed them. Mutation check: changing one summary, one proposed check and one static word each made the run fail ("NOT REVIEWED or changed since review"); restoring them made it pass.
- Source titles (the link text in "Primary sources") are labels for the cited topic. The claim is only what the quote beside the sentence says. One title that read as a claim was reworded: "Security manager includes source read" is now "Security manager role".
- Reworded because they read as product facts: B.p12 title "Per-org SAML keeps org SCIM" is now "Keep per-org SAML and org SCIM". The transfer note "not a native GitHub boundary" is now "outside GitHub". Three flow banners now use "must" or "may" (build, untrusted, respond).
- The G, X and G+X tags are design labels: where a control is planned (GitHub, outside GitHub, both). The lead and legend now say so ("planned in GitHub"). They are not claims about product behavior; those sit in the descriptions with evidence. 20 boxes tagged G or G+X have no sourced sentence of their own for that reason.
- Not checked: whether the verdicts are right; whether a text that is a requirement still reads as one to a reader (a person should read the list once); Firefox and Safari.

## 5 November 2026: boxes with no source say so, and the full click test was rerun

- Problem: a reader opening a box with no "Primary sources" list (32 of 106 boxes, for example "Private registry") could not tell whether a source was missing or not needed.
- Decision: such popups now show "Primary sources: None needed. These are design requirements, labels or marked as inference." This is shown only when the box has no sources; boxes with sources are unchanged. The outside-text list was refreshed for the new string (612 texts: R 123, L 276, N 213).
- Click test, rerun after all text changes, in headless Chrome against a copy of the page with the test script added (the visible pane throttled timers, so the same script ran too slowly there; virtual time was used instead, 130 ms between clicks): 106 boxes opened with no filter, then each of the 15 filters (288 highlighted boxes) opened. In total 394 popups, 1,599 Part of and Related links clicked, 1,070 source links checked for an https address, 15 filter chips and hashes checked. 0 failures.
- Each popup was checked for: popup open, `#n=` hash, either a source list or the "None needed" line (never both, never neither), and every link doing what its label says. Part of leaves one `fl:` filter pressed, `#f=fl%3A...` in the hash and the popup closed. Related opens the named box with its title and an `#n=` hash.
- Behavior, not a bug: opening a box clears the active filter (`filter = null` in the click handler), so "All" is pressed and the box's related set is highlighted. My first test run expected the filter to stay and reported 288 "failures" for that; the assertion was wrong and was corrected, not the page.
- Source link status, rechecked 5 November 2026 after the click test: every https address in the page (51 unique, one of them the font stylesheet) was fetched and returned HTTP 200. The verifier fetched and matched all 90 quotes on the same day. A 200 shows the page loads, not that the passage is still there; the quote match shows that.
- Light and dark at 375 px (live pane, A.e3): no sideways scroll (page width 375), popup inside the viewport, "None needed" line contrast 16.35 light and 14.17 dark, label 6.09 light and 7.09 dark. No console errors.
- Not tested: Firefox and Safari; real mouse clicks on this run (the earlier real-click sample was on the previous text).

## 5 November 2026: second review pass over every requirement sentence and outside text

- Why: the verdicts for the 256 requirement or label sentences and the 612 outside texts were assigned by one pass of the AI. A person has not reviewed them. To catch more mistakes before that, I read all 256 sentences and all 123 R outside texts again, looking only for product facts that were labelled as requirements. I also scanned the 276 label texts. This is a second read by the same AI, not a person's review.
- Found five sentences that stated or implied a product fact with no source, and one outside text. Each was reworded into a requirement or an aim, not sourced:
  - B.p2: "so a private repo cannot be made public by mistake" is now "so the aim is that no private repo is made public by mistake".
  - A.o1: "so people only see what they are granted" is now "so the aim is that private repositories are visible only to people who are granted access". Public organization metadata stays visible, so "only" overclaimed.
  - A.v2: "GitHub's short native Git-event retention" is now "GitHub's native retention for Git events". The old wording implied a retention period without a source.
  - DEV.3: "Private visibility supports explicit grants" is now "This design uses private visibility so that access is granted explicitly".
  - Outside text (B scope line): "Personal accounts linked by SAML and SCIM per org" is now "Personal accounts, with SAML and SCIM set up per org". The verifier failed on the old entry until the new wording was recorded, as designed.
- Read and left as requirements: sentences that say what this design does or requires ("Two-factor is required for every organization in the enterprise", "Lockfiles are mandatory"). They are choices, not claims about GitHub. One rationale sentence in c.soc ("repository names, paths and identities can reveal critical-system details") is general reasoning, not a product fact; a person may disagree.
- Rechecked after the rewording: verifier OK (612 outside texts reviewed, 0 stale; 90 quotes against 33 pages) and the full paced click test again, 394 popups, 1,599 links, 15 filters, 0 failures.
- Still open, and only a person can close it: reading `github-two-enterprise-interactive.outside.tsv` and the requirement sentences once and overruling any verdict.

## requirement sentences inside descriptions are now on the reviewed list too (2026-11-05)

- Before: only text outside descriptions had a recorded verdict. The 256 requirement or label sentences inside descriptions were classified only by the absence of an evidence row, so a reworded sentence could change silently.
- Now: each such sentence is in `github-two-enterprise-interactive.outside.tsv` with verdict R and the place `<box> description[<n>]`. The verifier fails if one is missing or reworded since review. 855 texts: R 366, L 276, N 213.
- Limit, unchanged: this proves a verdict is recorded for the exact wording, not that the verdict is right. The verdicts were assigned by the AI in two passes. A person has not reviewed them.

## sign-off by a person is tracked, and stays empty until one signs (2026-11-05)

- The verifier now prints whether a person has confirmed the reviewed list: none, current or stale. It never fails the run.
- `--sign "Name"` stores a hash of the list in `github-two-enterprise-interactive.signoff.txt`. A later change to any verdict or wording makes it stale.
- An agent must not run `--sign`. Status today: NONE. The AI cannot close this gap itself; the list needs a person to read it.

## independent AI review of the R and L verdicts (2026-11-05)

- On the user's choice, a separate subagent with no prior context re-judged all 642 R and L rows. It flagged 14 (two borderline); 628 were accepted.
- All 14 were reworded so they state a requirement and no product behavior: administrator exemptions became administrator accounts, "privileged" before pull_request_target was dropped, the AI manager role example was removed, "licensed" was removed, and the native-retention, built-in-bypass and provenance claims became plain requirements. Some followed sourced sentences in the same description, so the original was defensible, but the neutral wording is safer.
- A wording-guard hit on the B.v3 summary was fixed by rewording, not by loosening the guard.
- Limit: this second reviewer is also an AI. The sign-off by a person is still NONE.

### retest after the 14 rewordings (2026-11-05)

- Full click test rerun in headless Chrome (virtual time): 394 popups, 1,599 links, 1,070 source links, 91 boxes with the "None needed" line, 15 filters, 288 filtered boxes. 0 failures.
- Width check, light and dark, narrow window: no sideways scroll, 0 script errors. Only Chrome was tested.

## recheck of statements (2026-11-06)

- Reran the verifier against live sources: 90 of 90 quotes match. Read all 62 sourced sentences against their quotes for meaning.
- Reworded A.o1.src: CODEOWNERS review can be required by a ruleset or a branch protection rule, not only a ruleset. Reason: the CODEOWNERS page lists both. The evidence row prefix is unchanged, so the verifier needs no edit.
- Did not move any date: the page has no "current as of" line and the index lists no per-page date.
- Not rerun this time: the headless click test and the 375px check. This change is one sentence of text.
- Extended the recheck to the 12 inference sentences, 256 requirement sentences and all 855 other texts. No hidden product claims found. Moved "Facts checked" on the page to 6 Nov 2026. Person sign-off stays NONE by rule.

## fixes after the independent assessment (2026-11-10)

- Security manager (A.p14, B.p14, acc.2): name both roles and require recorded approval for the enterprise role. Chose this over forbidding the role outright, because the role is in public preview and the owner may have a reason to use it. The role is labelled public preview in the text.
- B.p2: state the limit for members and add a sourced sentence that organization owners can always create any type of repository. Chose a short owner list plus a scheduled review over the repository policy with a bypass list, because that policy is in public preview and recommendations must work without preview features.
- B.o1.tools and note 3: removed the guest collaborator exception instead of marking it "EMU only". It cannot apply in B, so it only added noise there.
- B.p7: say that the event itself can be missing, to match the source and B.v3.
- Reviewed list: the two section-link script fragments from 9 November got verdict N. Verdicts for the new sentences were set by the AI. Sign-off by a person stays NONE.
