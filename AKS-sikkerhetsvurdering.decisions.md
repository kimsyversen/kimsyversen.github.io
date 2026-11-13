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

## 13 Nov 2026, content verification

Fact check: [AKS-sikkerhetsvurdering.factcheck.md](AKS-sikkerhetsvurdering.factcheck.md).

- **Heading text moved to "Current as of 13 November 2026", id kept** as `current-as-of-1-november-2026`. Existing links to that section keep working.
- **Platform support bullet now says 60 days and the forced upgrade from 1 June 2027.** Without it the bullet read as if a cluster could stay on an old version for as long as it liked.
- **Azure Linux 2.0 bullet reworded** because 31 October 2026 has passed. The source still says removal "begins" on that date, so the page says "was set to begin".
- **"Plan a migration" became "Migrate before then"** for Ingress NGINX. Support ends this month, so planning is too late.
- **FIPS line names FIPS 140-3**, which is what the Microsoft page says. "Validated modules" was looser than the source.
- **Tags stand alone.** Removed "is interpretation by AI" before `[inference]` in three places and added the "Tags on this page" key (inference, unverified) under the Made with AI note.
- **Layer headings built by script get an id and a link.** Ids come from the heading text. A link to a layer id selects that layer first.
- **Top 10 intro says there is one extra supply chain item**, so ten OWASP risks and eleven cards add up.
- **Control plane wording follows the source.** "Operates, hardens and patches" became "provides, manages and maintains", the words Microsoft uses. The "Less relevant for now" item no longer says Microsoft patches the control plane, because Kubernetes patches reach it through cluster upgrades, which the customer controls.
- **REST reference added to Sources** for the field names used with `az aks show`. The CLI page does not list them.
- **Pod Sandboxing left without a preview tag.** Its own Microsoft page has no preview label. The older concepts-security page still says "(preview)". Recorded as a source conflict in the fact check.
