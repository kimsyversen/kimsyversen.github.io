Belongs to: [MCP Governance in a Microsoft ecosystem](mcp-governance-microsoft.html)

# Decisions: MCP Governance in a Microsoft ecosystem

## 2026-11-08

- **Page lives in `wip/`.** Same place as the governance summary. The index has no wip links, so the index is not edited.
- **Style copied from the governance summary.** The builder cuts head, style and the Made with AI note from that page, so both stay alike.
- **Two objectives, not one.** Objective A (backend) is enforceable. Objective B (clients) is not fully enforceable. Splitting them avoids promising B. Reason: the source request said B is much harder.
- **Backend is the hard boundary.** Client rules are a second layer. Reason: client rules have documented gaps (custom agent profiles, built-in GitHub server, varying coverage).
- **Preview feature kept optional.** (Superseded by the 2026-11-08 path decisions below for the preview path. Still true for the safe path.) The Global Secure Access MCP firewall is preview, so it is labelled preview and not needed for either objective. Reason: AGENTS.md design principle on preview features.
- **Endpoint outbound block shown as an open question.** It blocks all traffic without a rule and fails behind proxies and some VPNs. Reason: high admin cost, and AGENTS.md prefers least administration.
- **Foundry and Copilot Studio rows say "unverified".** No source found shows blocking one chosen external MCP URL. Reason: absence of a source is not proof.
- **"Consider placing it behind" kept as written.** The Azure MCP Server page says consider, not recommends. The page does not say Microsoft recommends it.
- **Acceptance tests listed as target outcomes, all "Not run".** Reason: nothing was tested in a tenant.
- **No expand button and a small own script.** The old script depends on a toggle this page does not have.
- **Table cells hold sourced prose.** The label checker does not capture table cells, so product claims sit there, each with a quote link. Text the checker does capture holds requirements and labels only.

## 2026-11-08, safe and preview-enabled paths

- **Two paths in one page, chosen by the reader.** The user asked to merge two markdown solutions (safe, preview-enabled) into this page with a selector. The page keeps its existing content and adds both documents.
- **User-requested exception to design principle 6.** AGENTS.md says not to rely on preview features and to label them. The preview path exists because the user asked for it. It is labelled preview everywhere, it is a sandbox pilot, and the safe path is the default. The page never says preview is needed.
- **The preview path is the safe path plus additions (superset).** Backend isolation, identity and client policy stay in both. Preview controls are extra visibility. Reason: if a preview feature is withdrawn, the safe design still holds. A Fallback section (preview only) says so.
- **One selector, no localStorage.** The choice is a `data-opt` attribute on body, set by the chooser buttons and by a Safe/Preview control in the sticky contents bar. It is kept in `?path=preview` (safe is the default and adds no parameter). Reason: AGENTS.md section 4 on saved state. A link opens the same path.
- **A hash into hidden content switches the path.** If a link such as `#fallback` points inside the hidden option, the page switches to that option and scrolls. Reason: shared links must not land on nothing.
- **No JavaScript shows both paths.** A noscript rule reveals both and hides the selector.
- **Preview-only evidence is hidden on the safe path.** 31 of 64 quotes belong to the preview path. The builder stops if shared content links one of them. The safe path shows 33. (Counts now 76 and 42 after the policy sync and parts table quotes.)
- **Global Secure Access.** The preview markdown excludes it on purpose. This page keeps it as an optional, preview-labelled outbound row on the preview path only. The safe outbound row no longer mentions it. Reason: the safe markdown relies on endpoint and network controls only.
- **Detail level held.** Each new control row is one row, cells at most 60 words. The preview markdown's long procedure is condensed to ten steps. Claims without a source (shared backend credential, uneven coverage, new resource type untested) are labelled inference or unverified.
- **Gateway row cites the API Management MCP quotes on both paths.** They are not preview-labelled on their page, but the page does not state their release status, so the safe gaps list says to confirm each feature before relying on it.

## 2026-11-08, GitHub as the policy source

- (Superseded by the next section.) **Both figures show GitHub managed settings above the client controls.** User request: allowed and denied MCP servers are governed through GitHub. Reason: the GitHub allow and deny list by URL is the documented client-side control. The diagram also says Foundry and Copilot Studio are not set by GitHub, because the sources say they need their own controls.
- (Superseded by the next section.) **Preview figure shows two lists.** GitHub (what clients may add) and Agent 365 (what the gateway serves) are separate. Added a gap and an open question about keeping them the same. Reason: drift would let a client add a server the gateway does not serve. Labelled inference.

## 2026-11-08, repository as the single source, pipeline to each product

- **The approved list lives in a Git repository. A reviewed pull request changes it. On merge a pipeline we build applies it to GitHub managed settings, Foundry and Power Platform (and Agent 365 on the preview path).** User request: accept a PR, add or deny a server, and have the change reach Foundry and Studio. Reason: one place to review and audit. Replaces the earlier note that Foundry and Copilot Studio are "not set by GitHub": the point holds only for GitHub's own settings, not for a pipeline.
- **The figure shows what each target can enforce.** Power Platform: whole MCP server only, not single tools (pp-block). GitHub: allow and deny list by URL, hosted on GitHub (gh-deploy). Foundry: a tool list per agent (fy-allowed), and no per-URL block found. Agent 365 (preview): Foundry is not a supported client surface (pv-byo-surf).
- **Pipeline arrows are design requirements, not product facts.** No source shows a pipeline writing to GitHub managed settings, or MCP servers in the Power Platform policy API. Labelled unverified and inference in the control table and gaps. Reason: the sources document the targets, not the sync.
- **Red in the figure stays for the denied direct path and for unverified status text.** Pipeline arrows are plain lines.
- **Added tests and gaps.** Merge a deny PR; edit a target by hand then run the pipeline; the pipeline does not exist; drift. The preview "two lists" gap became "a fourth copy of the list".

## 2026-11-08, ASCII figures instead of SVG

- **Both design figures are ASCII in text files** (`mcp-governance-microsoft.figure-safe.txt`, `.figure-preview.txt`), put in a `<pre class="ascii">` by the builder. User request: faster to update and work with. Reason: no coordinates to move, and a change shows up clearly in a diff. The old SVG drawing code is removed. Rule added to `AGENTS.md`.
- **Red is `[red]...[/red]` in the text file.** Same meaning as before: denied, unverified or not tested.
- **Each target now points to the clients it governs.** The old figure put targets above unrelated layers. Power Platform box is named Copilot Studio, with "Power Platform policy" beneath.
- **Agent 365 has a line from the pipeline but none to the clients.** The quote lists Copilot Studio, VS Code, Claude Code and GitHub Copilot CLI. That does not match our client boxes one to one, so no line is drawn. Unverified.
- **The label checker reads ASCII figures.** Each run of words in a `pre.ascii` is one text with a verdict. Box and arrow characters are skipped. The check proves a verdict was recorded for the exact wording, not that it is right.
- (Superseded by the next section.) **The red denied-path line is text** ("MCP clients - - - Direct access denied - - - X Private MCP backend"), since a line cannot cross the layers in ASCII.

## 2026-11-08, clearer figure language

- **Box titles are bold capitals.** `[b]...[/b]` in the text file becomes bold. User request: titles in the boxes should be easy to see. Rule added to `AGENTS.md`.
- **"Private MCP backend" is now "Company MCP server".** The user asked what it was and what technology it is. It is not a product. It is our own MCP server, which only the gateway can reach. The box says "Only the gateway can reach it". The page cites Azure Functions as the only host example, so the box names no technology.
- **The denied line says what it means.** "MCP clients --X--> Company MCP server" and "Blocked. Only the gateway may call the server." It replaces the dashed "Direct access denied" line. Still red, since red means denied.


## 2026-11-08, Agent 365 moved under the gateway

- **Agent 365 box now sits under the AI Gateway, with a line up to it labelled "Reads registered servers".** User question: where is the Agent 365 registry and how does it fit. Reason: the only documented link is that Agent 365 connects to the gateway and discovers the servers registered with it (pv-disc). It is a management view beside the traffic path, not a step in it.
- **The pipeline-to-Agent 365 arrow is removed from the figure.** (Supersedes "Agent 365 has a line from the pipeline" above.) No source shows how a pipeline would write to Agent 365. The caption keeps it as a design requirement. The "fourth copy of the list" gap stays.
- **Agent 365 still has no line to the clients.** The page does not verify which clients it covers.

## 2026-11-08, path names

- **The paths are now "Released only" and "With preview"** (buttons "Released" and "With preview"). They replace "Safe choice" and "Preview-enabled choice". User request, after asking for a better name. Reason: "safe" claims something nothing tested can back up, and the new names say what differs.
- **Internal names unchanged.** `data-opt="safe|preview"`, `opt-safe`, `?path=preview`, and the figure file names keep their old names so shared links and the build keep working. Only visible text changed. Older notes above still say "safe path" for the released-only path.

## 2026-11-08, "The answer" section removed

- **The section is gone. Its point is one sentence at the top of "The design", labelled "In short".** User request: merge the answer with the goal, and call it something other than "goal". The sentence holds Objective A (backend, built and tested) and Objective B (clients, a second layer, not promised) and the one repository list. The preview path adds one clause: preview controls only add visibility for gateway traffic.
- **Dropped with the section:** the long answer text for each path, the A/B/C list (C was "preview controls cover gateway traffic only", now the extra clause), the note that B depends on every client and network path, and the "neither objective needs a preview feature" line. The A/B definitions stay, because the figure and control tables use them. The "Answer" link is removed from the contents bar. The `#answer` anchor no longer exists.
- **"Red text marks what is denied or not verified" moved to the figure captions.**

## 2026-11-08, parts table

- **A table "Parts of the design" sits below the figures, inside The design.** User request: describe each box and measure briefly and show whether it is in released and with preview. 20 rows, four columns (part, what it does, released, with preview). The "extra with preview" column was merged into the With preview cell, as the user asked. New items say "New:". Reason: one table shows both the shared parts and what preview adds.
- **Preview cells carry quote links only on the preview path.** The released view shows the same text without links, because the preview quotes are hidden there and a link would lead nowhere.
- **Open items resolved from sources.** Publish MCP endpoints on released: the API Management MCP page lists tiers and shows no preview label (mcp-tiers), so "Yes". Authorize requests on released: JWT validation policy (mcp-authn). Limit request rate on released: rate limiting policy (mcp-rate). On the AI Gateway: callers are authorized by Entra access or an API key (pv-aig-caller), policies include consumption limits (pv-aig-limits), and telemetry covers tool usage (pv-aig-tel). So "Authorize requests" is "Yes for callers, per-tool rule not shown", "Limit request rate" and "Log every call" are "Partly", each labelled unverified.
- **The figures were not changed.** The preview gateway box still omits Authorize requests and Limit request rate. The table shows them. Foundry gateway routing stays out of the figure and in the table only, as agreed.


## 2026-11-08, preview figure aligned with the parts table

- **The AI Gateway box in the preview figure now lists Authorize requests and Limit request rate.** User request, after I pointed out the figure and the table disagreed. The box lists six items. Reason: the table already shows both, so the figure should too. The table keeps the detail: "Yes for callers, per-tool rule not shown" and "Partly", each unverified. The figure only names the measures, as design requirements. (Supersedes "The figures were not changed" above for the preview figure.)
- **Released figure unchanged.**

## 2026-11-08, full-width text and the fact check section

- **Text now uses the full width.** User report: many text blocks filled about half the page. Two causes in the shared style: `max-width` of 36 to 56rem on text blocks, and `text-wrap: balance` on paragraphs, list items, cells and captions. Both are overridden in the builder's own CSS (`OPT_CSS`). Headings still balance. The intro lead and the open question answers stay in their own grid columns. Rule added to `AGENTS.md`. The shared style on other pages is not changed.
- **"Evidence" section renamed "Fact check".** User request. Label: "Fact check, each product claim against its source". Heading: "Fact check". The intro says each product fact has a quote found word for word on its source page. The id `evidence` and the `#ev-V..` ids are kept so shared links still work. The contents link and the summary row say "Fact check". The Environment table column "Evidence" and the figure caption wording stay.
- **Open questions: the line "For the owners. The first question decides where to start." is removed.** User request.

## 2026-11-08, summary box and chooser removed, switch labelled

- **The summary box under the lead is removed** (Scope, Paths, Fact check, Kinds of claim, Tenant tests). User request. The lead now uses the full width. The links to the fact check section and to the governance summary that were in it are gone. The Fact check link stays in the contents bar. The labelling rule ("a product fact has a quote, our choices are labelled") is still shown by the labels on the page.
- **The "Choose a path" section is removed.** User request. The Released / With preview switch in the contents bar is the only control. It has the label "Select design" to its left. The default is Released. `?path=preview` still works. Its notes went with the section: the sentence that preview never replaces the released design (the Fallback section covers it on the preview path) and the note on the `?path=` address. The `#choose` anchor no longer exists. The "Path" link is gone from the contents bar.
- **"Decision makers" now links to Open questions** and says to compare the two designs with the switch. Reason: `#choose` is gone.
- **On narrow screens the contents bar wraps.** The switch sits on its own row below the links. Reason: with the label it was 305px wide and squeezed the links to a sliver at 375px.

## 2026-11-08, page title

- **Title and heading are now "MCP Governance in a Microsoft ecosystem".** User request. The old heading "Forcing MCP traffic through API Management" and the old title tag are replaced, so the heading and the browser tab match. The file name is unchanged. Reason: the page covers the whole design, not only the gateway.

## 2026-11-08, follow-up pass after the page review (12 items)

- **"Built and tested" removed from In short.** It said Objective A was "built and tested" while the gaps say nothing is tested. Now "a target not yet tested".
- **New lead.** It names the clients (GitHub Copilot, VS Code, Foundry, Copilot Studio), the repository, pipeline and gateway, and says nothing is built or tested. Reason: the old lead described an API Management page and the "nothing tested" statement left with the summary box.
- **Two lines under In short: Objectives and Designs.** Objectives define A and B in one place. Designs say Released only is the baseline and uses no feature labelled preview, and With preview adds Agent 365 and tool threat protection for a sandbox only. Reason: the chooser section that explained this was removed, and AGENTS.md rule 6 says the solution must work without preview. The "Decision makers" route says the same.
- **Button renamed "Released only"** to match the text ("released-only design"). `data-opt="safe"` and `?path=` are unchanged.
- **"Path" removed from visible text.** "Design" where it meant a design, "route" for the two Agent 365 and Foundry tags and the uneven coverage gap, "option" in the AI Gateway limits row. "Network path" and "private path" stay, they are about networks.
- **"Evidence" becomes "Sources"** in the Environment table header and in both figures' last line.
- **Fact check table columns:** Id 4.5rem, source 22%, date 7.5rem, the quote takes the rest (measured at 668px on a 1134px window).
- **Masthead meta line** is now "Design · Microsoft stack · MCP". The page does not link the governance summary any more, and it is not linked from the footer. Left for the owner.
- **Headings:** "Controls", "Environments", "Fallback" now match the contents bar. "Known gaps and what has not been tested" kept, because it says plainly what was not tested. The Gaps tag line reads "Bad news first. Read these limits before you rely on the design." The Controls goal tag is "How to read".
- **New first open question: "Do we allow preview features at all?"** (never, sandbox only, or later). The others are renumbered, 1 to 4 on Released only and 1 to 8 with preview.
- **Red text legend moved** from both figure captions to one line above each figure. The captions no longer repeat the Objective A and B sentences, the Objectives line covers them.
- **On a phone only the switch stays pinned** (46px). The contents links scroll away. Done with `display:contents` on the contents bar below 640px so the switch can stick to the page. Desktop is unchanged.
- **Not changed:** the 150 character line length on a wide screen. The user asked for full width. Options for later: larger body text or two columns for long notes.

## 2026-11-08, claim-by-claim check against source context

- **Goal: every statement on the page verified.** The word-for-word quote check passed from the start, but it only proves the words exist. I read each quote in its source context and compared it with the page wording.
- **Wording cut back where it went past the source.** Power Platform policy "blocks a whole server, not a single tool" now also says it covers certified connectors only (pp-certified, pp-custom), and the page says a company server may fall outside. Reason: the source says custom and HTTP connectors are not yet supported.
- **Seven quotes added** (83 in all, 47 released-only, 36 preview): pp-certified, pp-custom, pv-shared-cred, apim-ga, gh-file, gh-commit, pv-res-removed. Appended at the end so existing V ids keep their numbers.
- **Shared backend credential is sourced now** (pv-shared-cred) and no longer labelled inference. The old tier removal also has a source (pv-res-removed).
- **GitHub pipeline write is inference, not unverified.** The source shows managed settings are a file changed by commit and push. A pipeline making that commit follows from this, but nothing was tested. The label cell changed from unverified to inference.
- **API Management release status.** The Azure update page is script-rendered and could not be fetched. The quote comes from a third-party mirror (Microsoft 365 Message Center Archive). The page says so and says the source does not name each feature. Per-feature status stays unverified. Chosen over cutting the claim because it shows an announcement exists.
- **Left unverified, not cut:** per-URL block of one server in Foundry or Copilot Studio, MCP entries in the Power Platform policy API, sandboxing stdio servers, Foundry "cannot call arbitrary external MCP servers", AI Gateway per-tool rule and request rate limit. A web search found no official source. They stay labelled so the reader sees the gap.
- **Page date column:** compared with "Last updated on" on all 22 Learn pages. All match. No change.
- **Paragraph length.** Several lines went over 60 words after the additions and were trimmed. The gaps pipeline line now reads "Power Platform policies cover certified connectors only ... Build and test one target at a time."

## 2026-11-08, stop condition: no unverified statement left

- **Cut every claim without a source.** The stop condition asks that every statement be verified, and a label does not verify it. Removed from the tables and controls: per-URL block in Foundry or Copilot Studio, "an agent cannot call arbitrary external MCP servers", stdio sandboxing, the AI Gateway per-tool rule, request rate limit and log-every-call statements, the endpoint telemetry note and "older examples can be stale". The page has no "unverified" tag now. This supersedes the earlier choice to keep these as labelled gaps.
- **Absence statements stay only in Gaps** (Foundry and Copilot Studio per-URL block, MCP in the Power Platform policy tutorial). They say what the sources checked on 2026-11-08 do not show, and the design does not rely on them. The Power Platform tutorial text was searched and has no mention of MCP.
- **API Management release status now cites Microsoft's feed.** The release communications API (id 527626, status Launched) gives the GA text and "classic and v2 tiers, including the Developer tier and the Self-hosted Gateway". This supersedes the third-party mirror and its caveat. Reason: a first-party source names the tiers, so the "does not name each feature" gap is gone. The link in the quote table opens the raw feed without a text fragment.
- **Inference stays where it is a deduction** from sourced facts, and is labelled. Several were changed to recommendation where the text was our rule (the pipeline must make the commit; check that the company server is covered).

## 2026-11-08, no inference labels left

- **Every inference label removed.** The stop condition says every statement must be verified as correct, and a label does not verify. Each one was reworded to what a quote says, turned into a design requirement marked recommendation (our rule, not a product fact), or cut. This supersedes the earlier choice to keep inference as a label for deductions.
- **Cut:** "They reach GitHub clients only", "Tool blocking is not universal", "Tool-level blocking and threat protection may not remain". Reason: each was a deduction from the sources, not a quoted fact.
- **Page tags now:** recommendation and preview only. The ledger no longer has the "unverified" or "inference" label rows.

## 2026-11-08, final source-scope audit

- **Power Platform ACP wording now lists MCP connectors as a supported connector type for whole-server blocking.** Individual MCP tools remain unsupported; custom and HTTP connector types remain unsupported. Supersedes the older broad statement that ACP covers certified connectors only. Reason: the current ACP page lists MCP connectors separately from certified connectors.
- **Agent 365 routes stay separate.** The API Management integration's no-auto-routing limit is scoped to that integration. BYO server registration has its own admin approval flow, client list, public-endpoint requirement and future tool-level blocking status. The page does not describe either route as a pipeline write.
- **The preview pilot tests only the API Management integration where it says so.** BYO server route is identified separately in controls and open questions. Reason: route-specific blocking and routing limits differ.
- **Local stdio wording now follows the MCP transport spec.** It says the client starts a subprocess and that stdio communicates over standard input and standard output. Removed the unsupported claim that local stdio calls do not pass through a remote gateway.
- **Objective A is separate from the repository pipeline.** In short now says the list and pipeline apply Objective B; backend isolation is its own requirement. Reason: the pipeline targets client policy, while backend isolation controls the server path.
- **Azure AI Gateway is described as a separate preview resource type**, not a different product. The changed resource type is sourced in the table.
- **89 source quotes are listed** (49 on released-only, 40 on preview). V85-V88 were checked against live Microsoft Learn text, and V89 against the MCP transport specification. The latest shell quote fetch could not resolve external hosts. The prior 84-quote mechanical pass remains in the fact-check note.
- **V77 now quotes the certified-connector support row** instead of the page's broad certified-only limitation wording. The same source separately documents MCP server blocking, so the exact quote shown to readers no longer suggests ACP excludes MCP connectors.
- **The preview stdio row names only the documented filter scope.** The Global Secure Access MCP firewall sees remote MCP servers; local servers and JSON-RPC batches are outside its inspection, matching V31. Removed an unsupported statement about reaching local servers from Agent 365 or AI Gateway.
