# Plan: AKS-sikkerhetsvurdering.html

## 16 Nov 2026: plain language and request-flow figure

Goal: the page reads in plain words, and it shows how a request gets into AKS and where each check is applied.

1. Request-flow figure, first section of the Architecture tab.
   - Two lanes: a change to the cluster (Kubernetes API path) and a user's request to an app (network path).
   - Each step: component, owner, the check applied there, linked risks, exact source quote with link.
   - ASCII copy with a flow description in `AKS-sikkerhetsvurdering.flow.txt`.
2. Plain-language pass over page text and script-built strings. No change to facts, ids, storage keys or tags.
3. Notes: decisions, fact check (new quotes, dated 16 Nov 2026), Sources list, index entry date and footer date.
4. Checks: `scripts/section_anchors.py`, then `--check`. Browser check on desktop and narrow width: no sideways scroll, no console errors, tabs, filters, risk map, new figure links, link into a hidden tab.

Not in scope: rechecking the claims verified on 13 Nov 2026. The "Current as of" date stays unless those are rechecked.

## 26 Nov 2026, inference tags

Done. Open: the remaining tagged statements have no source that states them.
