# AKS-sikkerhetsvurdering: decisions

- Translated the whole page to English (head, CSS comments, body, script strings). Structure is unchanged: tag, class and href counts match the original.
- Tab ids and filter keys renamed to English (grunnlag to basics, metode to method, arkitektur to architecture, relevans to relevance, kilder to sources, alle/tilgang/app/leveranse to all/credentials/workload/supply). Old `#hash` links to tabs now fall back to the first tab. Saved checklist and status in localStorage keep working because their keys and risk ids did not change.
- `lang="en-GB"` and `toLocaleDateString('en-GB')`, to match the other pages.
- File name kept (changing it would break existing links to the page).
- Dropped the Norwegian wording "Ikke vurdert" for "Not assessed", "Delvis" for "Partial", "Mangler" for "Missing", "Ukjent" for "Unknown".
