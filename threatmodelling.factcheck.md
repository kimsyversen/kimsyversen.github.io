# Fact check: Threat modeling

Belongs to [threatmodelling.html](threatmodelling.html). Other notes for the same page: [decisions](threatmodelling.decisions.md).

Checked 3 November, 15 November and 28 November 2026. Sources were opened on those days. Not run: nothing here was tested in a real system; the claims portal is fictional.

## Sources

- **ASVS** = OWASP ASVS v4.0.3, raw chapter files V3, V4, V7, V12 on GitHub (tag v4.0.3).
- **MS** = learn.microsoft.com, Threat Modeling Tool threats page (STRIDE categories).
- **TMM** = threatmodelingmanifesto.org.
- **DREAD** = learn.microsoft.com, "Threat modeling for drivers" (section "The DREAD approach to threat assessment").

## Statements

| # | Statement | Source | Verdict |
| --- | --- | --- | --- |
| 1 | ASVS 3.3.1 logout and expiry invalidate the session token; 3.3.2 periodic re-authentication | ASVS | OK |
| 2 | ASVS 4.1.1 server-side access control; 4.1.3 least privilege; 4.1.5 fail securely; 4.2.1 IDOR | ASVS | OK |
| 3 | ASVS 7.2.2 failed access control decisions are logged | ASVS | OK. The alert on many denials is not in ASVS; the footer now says so |
| 4 | ASVS 12.1.1 large files; 12.1.3 quota per user; 12.2.1 type by content; 12.4.1 stored outside web root with limited permissions; 12.4.2 antivirus scan | ASVS | OK |
| 5 | The four questions are worded as on the manifesto page | TMM | Question 3 was "What do we do about it?"; the manifesto says "What are we going to do about it?". Fixed in a second pass on 3 Nov 2026 (curl of the page) |
| 6 | The six STRIDE names and meanings | MS | OK |
| 7 | STRIDE per element table (entity S R; process all; store T I D, R if log; flow T I D) | Larry Osterman, Microsoft blog archive (2007) | OK. The post "What does STRIDE have to do with threat modeling?" (7 Sep 2007) states all four rows: entity S R; process all six; store T I D plus R, because logs live in stores; flow T I D. It also says EoP does not apply to stores. The footer now cites it |
| 8 | DREAD = damage, reproducibility, exploitability, affected users, discoverability | Microsoft Learn, "Threat modeling for drivers" | OK since 15 Nov 2026: "DREAD stands for: Damage, Reproducibility, Exploitability, Affected users, Discoverability". Before that it rested on general knowledge only |
| 9 | Scores: 4x5=20, 3x4=12, 2x5=10, 3x3=9, 2x4=8, 2x3=6; matrix positions and band colors match; residual 1x5=5 is low | page arithmetic | OK |
| 10 | Footer links all return HTTP 200 | curl | OK |
| 11 | ASVS 5.0.0 is the current release and renumbers requirements | web search, one result set | OK. Footer now says the IDs match 4.0.3 only |

## Fixed on the page

- Move card used letter S as its example, but the register treats S as Reduce. Now labelled "Sign-in" with no letter.
- Threat R said the log from threat I "gives some trail". That log only records denied requests, so it does not cover uploads. Reworded, and a six-month review date added to match the Accept card.
- Threat T wording "more than the portal can write" fixed to "others besides the portal can write".

## Second pass, 3 Nov 2026

Re-checked from the sources, not from the first pass: raw ASVS 4.0.3 text for all 13 cited IDs (all match), the Osterman post (all four element rows match), the MS STRIDE page (definitions match), the manifesto page (wording), footer links (all 200). Matrix cell bands, dot positions and scores re-derived by hand: all correct.

- Question 3 heading now uses the manifesto wording.
- Fig. 1 caption said "across it, we cannot trust the other side". Reworded: the level of trust changes at the boundary, so data crossing it must be checked.
- DREAD note said "It works", which is an opinion. Replaced with a plain comparison of five numbers against two.
- Threat T control cited ASVS 12.4.1 for "only the portal can write". 12.4.1 says stored outside the web root with limited permissions. Control reworded to match.

## Third pass, 3 Nov 2026

- **Four responses (Remove, Reduce, Move, Accept):** NIST's page "Question 3: What are we going to do about it?" lists eliminate, disrupt, transfer responsibility, accept. It says transfers need documented agreements, and accepted threats need to be documented and periodically reviewed. Microsoft's SDL talks (Shostack 2008) have no "transfer", so the page cites NIST, not Microsoft, for this. Footer updated.
- **Move card** said "or insurance". NIST does not mention insurance, so it now says "a ready-made service and a written agreement". (Wording superseded 28 Nov 2026, finding 6.)
- **Move example (Sign-in):** checked against the whole OpenID Connect Core 1.0 text (fetched and searched, 2 mentions of "password"). The spec has no sentence that says "the client never stores passwords". What it does say: the client verifies identity "based on the authentication performed by an Authorization Server"; the methods the server uses to authenticate (e.g. username and password) "are beyond the scope of this specification"; the client gets an ID token. So in the protocol the password goes to the provider, never to the client. The page therefore says "never receives them" (what the protocol shows), not "never stores them" (an inference). Holds for redirect-based federated sign-in, which is what the diagram shows.
- **"Numbers are made up":** a statement about our own choices, so the check is provenance, not a source. The plan, the decisions log ("Case and numbers are fictional") and git history (commit 227bd2c onward) show the likelihood, impact and scores were picked by the author to show the method. No data or source exists for them. The arithmetic of the numbers is verified separately (statement 9). The footer says so. No external source can confirm this, and none is claimed. Confirmed by the page owner (Kim Syversen) in chat on 3 Nov 2026: the portal and all likelihood and impact numbers are invented for illustration.
- **Browser check:** page opened in the built-in browser at 394 px and at an emulated 1280 px. No console errors, no horizontal overflow, no clipped cards or tables. At 1280 px the question row and the four-response row are four columns and the panels use the 7/5 and 8/4 splits. The pane is too small to show 1280 px readably, so I also rendered the page with headless Chrome at 1280 px and looked at the screenshot: four-column question row, 7/5 and 8/4 panels, matrix and register all render without overlap or clipping.

## Fourth pass, 15 Nov 2026

Sources fetched again with curl before moving "Last updated" to 15 Nov 2026.

- **ASVS 4.0.3:** raw chapter files V3, V4, V7 and V12 at tag v4.0.3. All 12 cited IDs still read as in statements 1 to 4.
- **Manifesto:** all four questions appear on the page with the wording the page uses.
- **Osterman post:** all four element rows match statement 7.
- **NIST Question 3:** eliminate, disrupt, transfer responsibility, accept. Transfer needs documentation and agreements; accepted threats are documented and periodically reviewed.
- **MS STRIDE page:** the six category names are present. Definitions not re-read word for word this pass.
- **DREAD:** now has a primary source (statement 8). Linked in the footer.
- **Footer links:** all six external links return HTTP 200.
- **Fig. 1 and the Move card:** the drawing now has a customer-to-provider flow labelled "password" and a provider-to-portal flow labelled "identity". This matches the OpenID Connect reading in the third pass. The old drawing lacked the first flow, so the third-pass line "which is what the diagram shows" was wrong until today.
- **Not sourced, tagged `[recommendation]`:** the score levels (15, 8, 7), two numbers instead of DREAD, and the alert on many denials.
- **Cut as unsupported:** "Five numbers give more to argue about than two".
- **Threat S:** the weakness (no expiry, logout does not end the session) matches ASVS 3.3.1 and 3.3.2.
- **Arithmetic:** no score, matrix position or band changed.

## Presentation mode, 23 Nov 2026

- **Method and STRIDE.** The five slides follow the four questions in the [Threat Modeling Manifesto](https://www.threatmodelingmanifesto.org/). The six category names match [Microsoft's STRIDE table](https://learn.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-threats#stride-model). The slide reads threat examples from the worksheet register.
- **Scope and scoring.** Checked the fictional scope and cloud crossings against the worksheet and its [text diagram](threatmodelling.dfd.txt). Confirmed I at likelihood 4 and impact 5 (20, high) and R at likelihood 2 and impact 3 (6, low) against the worksheet's matrix and bands.
- **Treatment and review.** The four choices match the worksheet's names for the responses in [NIST Question 3](https://pages.nist.gov/nccoe-genomic-data-threat-modeling/Vol_C/PTM/Question3.html). The ownership example matches server-side enforcement and object-level access control in [OWASP ASVS 4.0.3, 4.1.1 and 4.2.1](https://github.com/OWASP/ASVS/blob/v4.0.3/4.0/en/0x12-V4-Access-Control.md). The two-customer test and the new handler role are fictional workshop exercises.
- **Browser checks.** Chromium at 1280 × 720, 1440 × 900, 375 × 667 and 320 × 568 with the light and dark palettes represented. Verified navigation, reveals, all six threat choices, keyboard marker activation, full screen on desktop, slide and worksheet links, selection and scroll restoration, and no horizontal page overflow or application console errors. The environment could not load the existing Google Fonts stylesheet or a favicon. Browser checks used fallback fonts. Other browsers and assistive technology were outside this pass.
- **Presentation UI follow-up.** The browser checks above predate the masthead presentation control, removal of facilitator labels and added matrix risk key. This follow-up could not be checked in a browser because the preview blocked local-file URLs and the workspace could not bind a local HTTP server. The section-anchor check and `git diff --check` passed.

## Persona review, 28 Nov 2026

Superseded by the [independent review](#independent-review-28-nov-2026). Kept for history.

Reviewer personas went through the page statement by statement until two rounds in a row found nothing. Each deviation needed three verdicts from different personas. All personas ran in one AI context, so they are different viewpoints and not independent reviewers. This table was written after the rounds from the evidence gathered in them.

Personas: P1 STRIDE practitioner, P2 ASVS auditor, P3 risk and logic analyst, P4 first-time reader, P5 accessibility and front-end tester, P6 repository rules editor, P7 source checker, P8 system and diagram architect.

### Sources opened again

- **ASVS 4.0.3:** raw V3, V4, V7 and V12 at tag v4.0.3. All 12 cited IDs match. The second pass says 13 cited IDs; the page cites 12.
- **ASVS 5.0:** the OWASP ASVS README names 5.0.0 as the latest stable release, with new numbering.
- **Manifesto:** the four questions match.
- **MS STRIDE page:** definitions read again. Tampering is the malicious modification of data. The other five match the page.
- **Osterman (2007):** the element rules match.
- **DREAD:** the five words match.
- **NIST Question 3:** eliminate (may mean giving up a feature), disrupt (identify, add or improve controls), transfer responsibility (documentation and agreements), accept (documented and periodically reviewed, may be paired with monitoring).
- **OpenID Connect Core 1.0:** the client verifies identity from the authentication done by the authorization server.
- **WAI-ARIA 1.2:** [roles which cannot be named](https://www.w3.org/TR/wai-aria-1.2/) include generic and paragraph.
- **Footer links:** all six external links return HTTP 200.

### Findings, all confirmed and fixed

| # | Round | Deviation | Verdict 1 | Verdict 2 | Verdict 3 |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Page date said 23 Nov after content changes | P7: git log has page commits on 24 and 26 Nov | P6: repository rules tie the entry date to content changes | P4: the index entry showed 26 Nov |
| 2 | 1 | Lead and captions had a width limit | P6: rules forbid `max-width` on paragraphs and captions | P5: lead measured 576 of 649 px | P3: the limit was in the CSS (`36rem`, `44rem`) |
| 3 | 1 | Tampering asked only about unseen changes | P7: MS defines it as malicious modification | P1: a change that is noticed is still tampering | P3: threat T is about who may write, not about being seen |
| 4 | 1 | Handlers read documents, but the drawing has no handler or flow, and scope did not say so | P8: no such flow in the drawing or the text figure | P4: the page says handlers read the documents | P1: slide 5 treats handler access as a change to the model |
| 5 | 1 | "Accept or watch" read as a fifth response | P7: NIST pairs monitoring with accept | P3: the page defines four responses | P4: "Done when" asks for one of the four |
| 6 | 1 | Move card required a ready-made service | P7: NIST asks for documentation and agreements | P4: slide 4 asks only for an agreement | P3: the footer says the responses follow NIST |
| 7 | 1 | The 4.1.3 row had a review, not a test | P2: least privilege can be tested by trying what is not allowed | P3: the old text had no pass or fail | P4: the section promises a test for every control |
| 8 | 1 | The 7.2.2 test checked only the alert | P2: 7.2.2 is about logging denied decisions | P3: an alert can fire while entries are missing | P4: the control names both logging and alert |
| 9 | 1 | Threat R called the upload trail thin, but there is none | P3: the same row says the portal does not log it | P4: the control table logs only denied attempts | P6: the first pass notes say the log does not cover uploads |
| 10 | 1 | Residual risk read as achieved | P3: slide 5 says to run tests before revising the score | P2: no test has been run on the fictional portal | P4: question 4 still asks whether the controls work |
| 11 | 1 | "Controls below" and "tests above" | P6: rules forbid saying where things are | P5: the two panels sit side by side on desktop, so "above" was wrong | P4: the words give no way to get to the controls |
| 12 | 1 | "Done when" allowed a failed test and left out the owner | P3: a run test can fail | P4: the control section requires owner and test | P1: question 4 asks whether controls work |
| 13 | 1 | Slide 5 left out lessons and the incident trigger | P4: the worksheet asks what was learned | P3: the worksheet reruns after an incident or a similar attack | P1: card 4 ends with writing down what was learned |
| 14 | 1 | Names set on elements whose role forbids names | P7: WAI-ARIA 1.2 prohibits it | P5: 15 `i` elements and one `p` had `aria-label` | P4: the labels are the only words for the dots, so they must be allowed |
| 15 | 1 | Focusable table wrappers had no role or name | P5: both could take focus unnamed | P7: a generic element cannot be named, so a role is needed | P4: the retested tree names both groups |
| 16 | 2 | Enter on the new controls link did nothing (caused by fix 11) | P5: reproduced in the browser, the row toggled and the address did not change | P3: the row key handler cancelled the key | P4: after the fix Enter and click both open the controls |
| 17 | 2 | Slide 1 scope did not get fix 4 | P4: slide and worksheet scope differed | P8: the slide drawing has no handler flow | P6: the diff showed only the worksheet changed |

The accessibility tree showed the names after fixes 14 and 15. Their screen reader effect was not observed.

### Rounds

- Round 1: 15 findings. Round 2: 2 findings. Round 3: none. Round 4: none.

### Raised and rejected

- Threats S, E, D and T have no owner, test or review date, and the register has no level column: the controls section is labelled as threat I only, and the level follows from the score.
- Click hint under Fig. 1, Fig. 2 caption, two-headed flows, no trust boundary in the legend, short Repudiation question: deliberate or explained next to them.
- "Draw the system as it is built", "named owner", "all numbers are made up": advice or accurate enough.
- Report damage and claims are not listed in scope or assets: upload and customer documents cover them.
- Remove for threat E while files are still served: it is called the first control, with the rest listed.
- Likelihood 1 and impact 5 rated low: a design choice of the bands.
- Slide 3 shows ratings before the reveal: the scores and ranking stay hidden.
- Register rows cannot take focus: the markers give the same action by keyboard.
- The scope drawing description and "Review in six months": accurate.
- Footer says the responses follow NIST "under other names" while Accept keeps its name: the NIST names are listed beside it.
- Moving between slides does not change the page address: each slide heading is a link to that slide.
- Smooth scrolling stalled in one test: the preview pane drew 2 frames in 2 seconds, and a later scroll reached its target.
- Low contrast flagged on drawing letters: the checker missed the filled shape behind them.

### Browser checks

Built-in Chromium at 1280 x 800, 640 x 800 (light and dark) and 375 x 812. No console messages and no sideways page scroll. All five slides and reveals, marker keys, slide links and the two table groups checked. An automated text contrast check at 640 px found no failure apart from the false positive above.

## Repeated verification, 28 Nov 2026

Superseded by the [independent review](#independent-review-28-nov-2026). Kept for history.

Done because the first table was not recorded while the findings were verified. Findings 1 to 15 were checked against the page in commit 2bfd519, 16 against a copy of the fixed page without its fix, and 17 by comparing the original slide with the fixed scope. Sources for ASVS, Microsoft, NIST, WAI-ARIA, HTML-AAM and axe were opened again before the verdicts. P9 is a front-end developer persona. All personas still ran in one AI context.

All 51 verdicts: deviation confirmed.

| # | Verdict 1 | Verdict 2 | Verdict 3 |
| --- | --- | --- | --- |
| 1 | P6: rules tie the date to content changes; the page said 23 Nov | P7: commit e908dd1 (26 Nov) changed visible text | P4: the page said 23 Nov, its index entry 26 Nov |
| 2 | P6: `.lead` 36rem and `figcaption` 44rem break the width rule | P5: lead 576 of 649 px at 1280, captions 704 of 753 px at 800 | P9: computed `max-width` was set before, `none` after |
| 3 | P7: Microsoft defines tampering as malicious modification of data | P1: Microsoft driver guidance says changing data; stealth is not needed | P3: threat T is about who may write |
| 4 | P8: the drawing has no handler or handler flow | P4: handlers read documents, scope excluded only their system | P1: slide 5 treats new handler access as a model change |
| 5 | P3: "or watch" sits beside four defined responses | P7: NIST puts monitoring under accept | P4: "Done when" asks for one of the four |
| 6 | P7: NIST asks for documentation and agreements, no service | P4: slide 4 asked only for an agreement | P3: the card made a ready-made service part of every Move |
| 7 | P2: least privilege (4.1.3) can be tested by a refused request | P3: "Review of roles and access rules" has no pass or fail | P4: the section promises a test per control |
| 8 | P2: 7.2.2 requires failed decisions to be logged | P3: the old test passed with log entries missing | P4: the control names logging, the test checked only the alert |
| 9 | P3: the row says no logging, then says the trail is thin | P4: the control table logs only denied attempts | P1: repudiation is the lack of a trace; "thin" implies one for uploads |
| 10 | P3: "goes from 4 to 1" stated before any test | P2: the section says an untested control is only a claim | P4: slide 5 says run tests before revising the score |
| 11 | P6: rules forbid saying where things are | P5: at 1280 "tests above" was to the left (same top edge) | P4: "below" gave no way to reach the controls |
| 12 | P3: a test that has run may have failed | P2: control owners are required but were not in the criteria | P4: question 4 asks whether controls work |
| 13 | P4: the worksheet asks what was learned, the slide did not | P3: the slide lacked the incident trigger | P1: card 4 ends with writing down what was learned |
| 14 | P7: WAI-ARIA 1.2 prohibits names on generic and paragraph | P9: HTML-AAM maps `i` to generic and `p` to paragraph | P5: 15 `i` and one `p` had `aria-label` and no role |
| 15 | P5: at 375 both wrappers scrolled and took focus without role or name | P7: axe `focus-order-semantics` asks for a role (best practice, minor) | P9: a plain `div` is generic and cannot be named |
| 16 | P5: copy without the fix: Enter left the address unchanged and marked the row | P9: the row key handler calls `preventDefault` on Enter | P4: a keyboard reader could not follow the link |
| 17 | P8: slide 1 omitted how handlers get documents | P4: worksheet and slide gave different scopes | P6: one fact must not differ between two places |

Findings 14 and 15: effect with a screen reader not observed. Finding 15 is a best-practice gap, rated low.

One new candidate, rejected: the 7.2.2 test does not check what each log entry contains. P2 raised it, since the requirement says logs should include relevant metadata. P3 and P4 rejected it: the control claims only that denied attempts are logged and alerted, not full coverage of the requirement.

## Independent review, 28 Nov 2026

Six separate AI agents, each with its own context and one role: STRIDE practitioner (S), ASVS auditor (A), technical editor (E), accessibility specialist (X), front-end developer (F) and release editor (R). They did not read this file or the decisions. A deviation counted when three of them confirmed it.

### The 17 earlier findings

All confirmed, each by three agents: 3 to 10, 12, 13 and 17 by S, A and E; 1, 2, 11 and 14 to 16 by X, F and R.

- 4 and 9: confirmed narrowly.
- 11: breaks the repository rule. A WCAG failure was not established.
- 14 and 15: effect with a screen reader not observed.
- 16: caused by fix 11, not present before it. Reproduced with the Return key.
- 17: caused by fix 4, not present before it.
- Fixes 6, 7 and 10 left gaps, handled as candidates below.

### New deviations, confirmed by three and fixed

| Deviation | Confirmed by | Fix |
| --- | --- | --- |
| The 4.1.3 test could pass with a list that allows too much | S, A, E | The list is checked against the customer's own claims |
| The example breaks the owner and test rule without saying so | S, A, E | The page says what the example leaves out |
| "Done when" left out gaps and lessons | S, A, E | New item |
| The system description left out viewing and did not scope damage reports | S, A, E | Sentence rewritten |
| The first control test tried only refusals | S, A, E | It also opens the customer's own document |
| "Or is missing" in the 4.1.5 control had no test | S, A, E | The test also removes the check |
| Slide 5 left out the "similar attack" trigger | S, A, E | Added |
| "Then remove it" in the new 4.1.5 test could mean the error | S, A, E | "Remove the check" |
| The slide 1 caption left out viewing | S, A, E | Added |
| The slide 5 answer never looked for new threats | S, A, E | New item |
| A selected marker looked the same with and without keyboard focus (WCAG 2.2, 2.4.7) | X, F, R | Red ring on focus |
| "Finish" kept a Right arrow shortcut that does nothing | X, F, R | Attribute removed on the last slide |

### Raised and not fixed

| Candidate | Confirmed by |
| --- | --- |
| The register has no level word | A, E (S rejected) |
| "Review in six months" for threat R has no date | S, E (A rejected) |
| Slide 5 "Run the tests before revising the score" | A, E (S rejected) |
| Fig. 1 `aria-label` leaves out two flows | X (F, R rejected) |
| Strike-through on the earlier score of 20 | A only |
| Move wording | E only |
| Missing dates | E only |
| "Opens or runs" | S only |
| ASVS 4.2.1 covered only in part | A only |
| Writers to the document store not in Fig. 1 | E only |
| ASVS 7.2.2 log metadata not tested | A only |
| Accepting a residual score of 5 | none |
| No alert threshold | none |
| Click hint under Fig. 1 | none |
| "See the register on the page" in the text figure | none |
| After opening a slide by its address and closing it, focus does not move to "Present" | none: F saw it and judged it too small, R rejected it |

### Rounds

- Round 1: five new deviations, all low and fixed.
- Round 2: no findings from all six.
- Round 3, on the same page as round 2: no findings from S, A, E and R. The owner cancelled the extra review before X and F reported, so round 3 is incomplete.

## Limits

- ASVS may change after 28 November 2026.
- Likelihood and impact numbers are made up to show the method.
- The page has not been tested with a screen reader, in browsers other than Chromium, or in forced colours mode.
- The red focus ring has 2.99:1 contrast against the dark marker fill in light mode and 2.22:1 in dark mode (calculated). It has 5.36:1 and 6.72:1 against the page.
