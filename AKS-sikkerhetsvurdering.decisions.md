# AKS-sikkerhetsvurdering: decisions

Belongs to [AKS-sikkerhetsvurdering.html](AKS-sikkerhetsvurdering.html). Plan: [AKS-sikkerhetsvurdering.plan.md](AKS-sikkerhetsvurdering.plan.md).

- Translated the whole page to English (head, CSS comments, body, script strings). Structure is unchanged: tag, class and href counts match the original.
- Tab ids and filter keys renamed to English (grunnlag to basics, metode to method, arkitektur to architecture, relevans to relevance, kilder to sources, alle/tilgang/app/leveranse to all/credentials/workload/supply). Old `#hash` links to tabs now fall back to the first tab. Saved checklist and status in localStorage keep working because their keys and risk ids did not change.
- `lang="en-GB"` and `toLocaleDateString('en-GB')`, to match the other pages.
- File name kept (changing it would break existing links to the page).
- Dropped the Norwegian wording "Ikke vurdert" for "Not assessed", "Delvis" for "Partial", "Mangler" for "Missing", "Ukjent" for "Unknown".

## 3 Nov 2026, "Made with AI" note

- **Plain label and one sentence at the end of the footer**, under a hairline rule, in the page's own muted and ink colours. Chose this over a pill or badge to keep it quiet and avoid the template look. Colours use the page tokens, so dark mode follows.
- **Wording:** "This page was written with the help of AI. Its content has not necessarily been fully quality checked by a human." Same text on all five pages.
- **Layout:** label and text in two columns on desktop, stacked under 560 px.
