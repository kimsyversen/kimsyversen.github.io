# Keeping this site up to date

Work and commit on `dev`. The owner publishes from `master`, where everything is public, including working notes. Keep secrets and customer data out of the repo.

## 1. Index

Keep the published list in [index.html](index.html) in sync in the same commit. Add new entries first with the next number, remove retired entries, and preserve existing entry numbers. Update the entry date for content changes and the footer date whenever the index changes. Check affected links.

## 2. Drafts and notes

Check sources during drafting. When substantial page changes need content review, share a draft before polishing the layout.

Keep only the notes a page needs, named after the page and kept beside it. Use `.plan.md` for open work, `.decisions.md` for lasting choices and reasons, and `.factcheck.md` for verification. Keep superseded decisions marked for history and working notes off reader-facing pages.

For pages with multiple sections or tables, define each section's job and scope. Within that scope, make categories mutually exclusive and collectively exhaustive (MECE): give each fact one authoritative home, use cross-references for related views, and label exclusions or unknowns instead of duplicating facts or implying unsupported coverage.

## 3. Evidence

- Verify factual claims against primary sources and record the date and verdict in the fact check. Cut unsupported claims or label them `[unverified]` or `[inference]`. Record gaps in testing.
- Write `[inference]` as interpretation by AI, not stated in a source. Never write it as the owner's or a person's own view: no "my", "our" or "mine" (not "my judgement", "my estimate", "our reading", "these definitions are mine"). Use "interpretation by AI" or "AI estimate" in sentences, headings and generated text on every page, and in the fact check. A tag that already says it, such as the `inference` tag on a page, needs no such wording after it.
- Tags (`inference`, `unverified`, `recommendation`, `preview`) stand alone in the text: do not add "Interpretation by AI:" or any repeat of the tag's meaning after them. Each page that uses tags ends with a "Tags on this page" key under the Made with AI note. The key lists only the tags that page uses, with one sentence each: `inference` is interpretation by AI that is not stated in a source, `unverified` is not confirmed in a quoted source, `recommendation` is a design choice proposed on the page, and `preview` is a feature in preview. Add or remove a key row in the same edit that adds or removes the last use of a tag.
- Put the exact quote and a link to its passage beside each sourced diagram claim. Reserve diagram text without evidence for requirements and labels.
- Run the page's quote and label checks when evidence or wording changes. Recheck sources and update the fact check before moving the page's "Current as of" date.

## 4. Public links and saved settings

Preserve public URLs, link anchors, and saved settings. Use page-specific keys for new browser storage. If asked to rename a public file, check incoming links and move its notes with it.

Make every section linkable. Each `<section>` and each `<article>` that holds a heading has a stable `id` on it or on its heading, and every `<h2>` and `<h3>` has an `id` and is a link to it (`a.sec-link`), so a reader can copy the address of that part. This includes headings built by script. A heading that already links to another page is exempt. Never change an existing id. New ids come from the heading text. On tabbed pages a section id must not equal a tab id, and a link to a section in a hidden tab must open that tab first. Run `python3 -I scripts/section_anchors.py` after adding sections. Builders run it on their output.

## 5. Style and checks


- Keep static flow and architecture figures in plain text ASCII files beside the page. Give each figure a text description of the flow.
- Run `python3 -I scripts/section_anchors.py --check` before finishing. It fails if a section has no id or link.
- Write only sentences the reader would miss if you deleted them; never restate a heading or label, say where something is on the page, or state the obvious.
- Check layout changes on desktop and a narrow viewport for sideways page scroll and console errors. Test affected controls and shared links when behavior changes. Keep detailed diagram checks with the relevant page.

## 6. Recommendations

Prefer the simplest option with the least upkeep and explain any added complexity. Recommendations must work without preview features. Label preview features when mentioned.
