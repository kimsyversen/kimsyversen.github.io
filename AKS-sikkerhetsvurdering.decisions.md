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

## 16 Nov 2026, plain language and request-flow figure

Fact check: [AKS-sikkerhetsvurdering.factcheck.md](AKS-sikkerhetsvurdering.factcheck.md). Text copy of the figure: [AKS-sikkerhetsvurdering.flow.txt](AKS-sikkerhetsvurdering.flow.txt).

- **"How a request gets into AKS"** (id `how-a-request-gets-into-aks`) has its own tab, 5 Data flow (`dataflow`), after Architecture. It first sat in the Architecture tab (2026-11-16 moved). The Relevance tab (id `relevance`, so old links work) became 6 "Focus and skip", its section heading "Where to focus, and what to skip" (id unchanged). Runtime is now 7.
- **Two flows, not one.** A change to the cluster goes through the Kubernetes API (network path, authentication, authorization, admission, etcd, scheduler and kubelet). A user's request goes over the network (load balancer, ingress or Gateway, Service, NetworkPolicy, pod, outbound, Azure service). One combined flow would mix two different sets of checks. Lane ids: `a-change-to-the-cluster`, `a-users-request-to-an-app`.
- **Built in HTML, not SVG.** Numbered steps on a rail. Two columns on wide screens, one on narrow, so it never scrolls sideways. A filled number marks a step that can stop the request.
- **Each step with a source claim has the exact quote and a link to the passage** beside it. Steps without a quote are labels only (person or pipeline, user, pod).
- **Risk ids in the figure are buttons** that open the risk under Top 10. They take the status colour like the other risk tags.
- **Owner per step is tagged `[inference]`** once, in the section intro.
- **No TLS claim at the ingress step.** No clean source sentence was found.
- **Plain-language pass: wording only.** Ids, storage keys, risk titles, tags and facts are unchanged. Jargon was replaced or explained on first use (control plane, kubeconfig, default-deny, ingress and egress, IMDS, cluster-admin). "East-west" became "between namespaces". "Egress control" became "Outbound control".
- **Heading "Risk per part of the value chain" became "Risk per step, from code to monitoring"**, id kept as `risk-per-part-of-the-value-chain`.
- **Removed sentences that explain how a control works** ("Tap a layer", "Tap a marker or box", "Tap a risk", "Tick them off as you go").
- **"Current as of" and "Facts checked" stay at 13 Nov 2026.** Only the figure quotes were checked on 16 Nov. The Sources intro says so.
- **Seven sources added at the end of the list** so the existing numbers stay the same.
