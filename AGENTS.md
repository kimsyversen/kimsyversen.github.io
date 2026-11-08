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
- Put the exact quote and a link to its passage beside each sourced diagram claim. Reserve diagram text without evidence for requirements and labels.
- Run the page's quote and label checks when evidence or wording changes. Recheck sources and update the fact check before moving the page's "Current as of" date.

## 4. Public links and saved settings

Preserve public URLs, link anchors, and saved settings. Use page-specific keys for new browser storage. If asked to rename a public file, check incoming links and move its notes with it.

## 5. Style and checks

- Follow [threatmodelling.html](threatmodelling.html) for content page style and copy its Made with AI note word for word. Write in English, let body text fill its column, and avoid em and en dashes.
- Keep static flow and architecture figures in plain text ASCII files beside the page. Give each figure a text description of the flow.
- Check layout changes on desktop and a narrow viewport for sideways page scroll and console errors. Test affected controls and shared links when behavior changes. Keep detailed diagram checks with the relevant page.

## 6. Recommendations

Prefer the simplest option with the least upkeep and explain any added complexity. Recommendations must work without preview features. Label preview features when mentioned.
