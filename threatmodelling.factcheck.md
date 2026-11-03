# Fact check: Threat modeling

Belongs to [threatmodelling.html](threatmodelling.html). Other notes for the same page: [plan](threatmodelling.plan.md), [decisions](threatmodelling.decisions.md).

Checked 3 November 2026. Sources were opened that day. Not run: nothing here was tested in a real system; the claims portal is fictional.

## Sources

- **ASVS** = OWASP ASVS v4.0.3, raw chapter files V3, V4, V7, V12 on GitHub (tag v4.0.3).
- **MS** = learn.microsoft.com, Threat Modeling Tool threats page (STRIDE categories).
- **TMM** = threatmodelingmanifesto.org.

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
| 8 | DREAD = damage, reproducibility, exploitability, affected users, discoverability | general knowledge | OK |
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
- **Move card** said "or insurance". NIST does not mention insurance, so it now says "a ready-made service and a written agreement".
- **Move example (Sign-in):** checked against the whole OpenID Connect Core 1.0 text (fetched and searched, 2 mentions of "password"). The spec has no sentence that says "the client never stores passwords". What it does say: the client verifies identity "based on the authentication performed by an Authorization Server"; the methods the server uses to authenticate (e.g. username and password) "are beyond the scope of this specification"; the client gets an ID token. So in the protocol the password goes to the provider, never to the client. The page therefore says "never receives them" (what the protocol shows), not "never stores them" (an inference). Holds for redirect-based federated sign-in, which is what the diagram shows.
- **"Numbers are made up":** a statement about our own choices, so the check is provenance, not a source. The plan, the decisions log ("Case and numbers are fictional") and git history (commit 227bd2c onward) show the likelihood, impact and scores were picked by the author to show the method. No data or source exists for them. The arithmetic of the numbers is verified separately (statement 9). The footer says so. No external source can confirm this, and none is claimed. Confirmed by the page owner (Kim Syversen) in chat on 3 Nov 2026: the portal and all likelihood and impact numbers are invented for illustration.
- **Browser check:** page opened in the built-in browser at 394 px and at an emulated 1280 px. No console errors, no horizontal overflow, no clipped cards or tables. At 1280 px the question row and the four-response row are four columns and the panels use the 7/5 and 8/4 splits. The pane is too small to show 1280 px readably, so I also rendered the page with headless Chrome at 1280 px and looked at the screenshot: four-column question row, 7/5 and 8/4 panels, matrix and register all render without overlap or clipping.

## Limits

- ASVS may change after 3 November 2026.
- Likelihood and impact numbers are made up to show the method.
