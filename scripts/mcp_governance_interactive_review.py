"""Interactive-only corrections from the holistic source review, 2026-11-12.

The legacy builder remains unchanged. Scoped replacements fail if shared wording drifts.
"""
import re


def apply_review(page, ev, rec, inf, unv, evp):
    def replace(old, new):
        nonlocal page
        assert page.count(old) == 1, (old[:100], page.count(old))
        page = page.replace(old, new)

    def control(cid, requirement=None, documented=None):
        nonlocal page
        pattern = rf'(<div class="ctl[^\"]*" id="ctrl-{re.escape(cid)}"[^>]*>)(.*?)(</div>)'
        def edit(m):
            body = m[2]
            for label, value in [('Design requirement', requirement), ('What Microsoft and GitHub document|What Microsoft documents', documented)]:
                if value is not None:
                    body, count = re.subn(rf'(<dt>(?:{label})</dt><dd>).*?</dd>', lambda n: n[1] + value + '</dd>', body, flags=re.S)
                    assert count == 1, (cid, label, count)
            return m[1] + body + m[3]
        page, count = re.subn(pattern, edit, page, flags=re.S)
        assert count == 1, (cid, count)

    control('inventory', requirement=(
        'Keep approved and denied servers in reviewed Git changes, with endpoint, owner, authentication, permitted tools and risk class. '
        'Use the company gateway URL for company backends. Review address, identity, permissions, tool and version changes. '
        f'Pin and verify local packages or container digests; a URL or command allowlist does not establish code integrity. {rec}'))
    control('pipeline', requirement=(
        'Build adapters for GitHub managed settings and Foundry connection tool lists; validate each before deployment. '
        'Keep Power Platform MCP policy manual until its API path is verified. Microsoft 365 connector access stays manual. '
        f'Use separate least-privilege credentials, record the reviewed commit and target result, and reconcile drift. {rec}'))
    replace('The proposed pipeline must configure Foundry and Copilot Studio separately.',
            'Configure Foundry connections separately; keep Copilot Studio policy manual until its MCP adapter is verified.')
    control('client', requirement=(
        'Set a managed allowlist of approved endpoints and reject unmatched servers on each supported client. '
        'For restrictions that must survive account switching or unavailable server policy, use protected device policy. '
        f'Test precedence and client versions. Built-in servers, custom profiles, cloud sessions and other clients need separate coverage. {rec}'),
        documented=(
        f'VS Code documents allow, deny and managed-only policies {ev("vs-allow", "vs-managed", "vs-deny")}. '
        f'GitHub matches URLs and blocks unmatched entries; deny wins {ev("gh-url", "gh-block", "gh-deny")}. '
        f'Custom agent profiles and first-party servers have exceptions; client coverage varies {ev("gh-profiles", "gh-builtin", "gh-vary")}. '
        f'Server policy follows the signed-in account {ev("review-account")}; local delivery can persist across account changes {ev("review-local-policy")}.'))
    control('stdio', requirement=(
        'Limit local launch commands through managed policy. Pin reviewed artifacts and verify their integrity before execution. '
        'Apply application control, process isolation, least privilege and file and credential restrictions. '
        f'Account for local administrators, shell tools, other MCP clients and unmanaged devices as bypass paths. {rec}'))
    control('windows', requirement=(
        'Restrict device egress to approved destinations where operationally feasible. Test DNS, proxies, VPNs and permitted general web traffic. '
        f'Windows Firewall is not an MCP URL or tool-content allowlist; a permitted HTTPS destination may carry other traffic. {inf} '
        f'Combine egress restrictions with client policy and application control. {rec}'))
    control('gateway', requirement=(
        'Publish company MCP endpoints through API Management. Explicitly configure every client connection to that gateway address. '
        'Authenticate, authorize each caller and tool, rate-limit and log. Enforce tool arguments and object permissions at the server. '
        f'Do not treat an HTTP path filter as an MCP tool-name policy without verifying JSON-RPC handling. {rec}'))
    control('identity', requirement=(
        'Choose inbound and backend authentication separately. Validate issuer, tenant, audience, expiry and caller permissions at the gateway. '
        'For the shared managed-identity baseline, only the gateway identity may authenticate to the private backend. '
        f'Authorize each upstream caller before using that shared identity; do not trust caller-supplied identity headers. {rec}'),
        documented=(
        f'API Management validates Entra tokens or subscription keys {ev("in-entra", "in-key")}; its managed identity can authenticate to a backend {ev("out-mi")}. '
        f'OBO preserves user delegation and requires a downstream token {ev("review-obo")}. '
        f'{rec} For a delegated variant, keep gateway-only networking, acquire the correct backend audience token and retain user authorization. '
        f'{unv} No OBO implementation or cross-client sign-in flow has been tested. A subscription key alone does not identify an individual user. {inf}'))
    control('backend', requirement=(
        'Disable public backend access and permit the company gateway over a private path. Require valid backend authentication and least-privilege tool authorization. '
        f'Select hosting and a gateway tier that support the required private connection; classic Functions Consumption cannot meet this private-endpoint baseline. {rec}'))
    control('logging', requirement=(
        'Collect gateway, backend and supported client telemetry. Correlate authenticated caller, tenant, tool, decision and request ID. '
        'Redact credentials and sensitive payloads; restrict log access and retention. Monitor unapproved connections, policy drift and unusual tool use. '
        f'Review the inventory and run bypass tests periodically. {rec}'))
    control('purview-audit', requirement=(
        f'Validate actual audit events and fields for each agent integration before relying on server or tool visibility. {rec} '
        f'{inf} MCP calls may fall within agent-to-tools interactions; the cited Purview pages do not explicitly establish MCP endpoint coverage.'),
        documented=(
        f'Agent 365 instances are audited from creation, including agent-to-tools interactions {ev("purview-audit-on", "purview-audit-tools", "purview-audit-search")}. '
        f'The listed Agent 365 DLP interactions exclude tool calls {ev("purview-dlp-scope")}; DSPM inventories recently active agents {ev("purview-dspm-inventory")}. '
        f'Foundry auditing covers prompts and responses after the required integration setup {ev("purview-foundry-audit", "review-purview-setup")}. '
        'This is audit coverage, not a demonstrated MCP DLP boundary.'))
    control('byo', requirement=(
        'Exclude direct BYO access to the private company backend: it contradicts gateway-only access. '
        'If piloting BYO, use a separate test endpoint, or test registration of the company gateway URL with compatible authentication. '
        f'Keep backend isolation and caller authorization intact; neither composition is validated here. {rec}'))
    control('ttp-users', requirement=(
        'Use a separate pilot endpoint for delegated user-token flows. Keep app-only workloads on an appropriately authenticated baseline endpoint. '
        f'One server policy covers every caller, so mixing incompatible callers can reject legitimate calls. {rec}'))
    control('power-platform', requirement=(
        '<span id="gap-unverified-url-block"></span>Configure ACP for listed MCP connectors; arbitrary URL entries are unverified. '
        'Retain mixed mode while classic data policies protect custom and HTTP connectors; ACP-only mode ignores those policies. '
        f'Keep configuration manual until the actual MCP API adapter is verified. {rec}'),
        documented=(
        f'ACP supports deployment-pipeline automation {ev("pp-pipe")}, MCP server-level blocking but not per-tool blocks {ev("pp-block")}, '
        f'and connector blocking also blocks dependent MCP tools {ev("studio")}. '
        f'Custom and HTTP connectors need classic policies {ev("pp-custom")}; mixed mode enforces both policy types {ev("review-acp-mixed")}. '
        f'ACP general availability depends on design-time enforcement reaching each workload {ev("review-acp-rollout")}. '
        f'{rec} Confirm Copilot Studio rollout before including ACP in a released-only deployment. Retain classic policies and record any remaining MCP coverage gap until then. '
        f'{unv} The API tutorial does not establish the actual MCP-specific policy payload.'))
    control('ttp-modes', requirement=(
        'Configure evaluation mode in Microsoft Defender. Test Audit, Block and evaluator failures. '
        'Use pre-invocation checks to stop calls and post-invocation checks to withhold results. '
        f'Do not automatically retry a write whose result was withheld: the action may already have completed. {rec}'),
        documented=(
        f'Audit mode fails open; Block mode fails closed {evp("pv-ttp-audit", "pv-ttp-block")}. '
        f'One policy covers every tool and caller of a server {evp("pv-ttp-scope")}. '
        f'Discovery and session management are not evaluated {evp("review-ttp-discovery")}; initialize, tools/list and notifications are excluded. '
        f'A post-call denial cannot undo execution {evp("pv-ttp-post")}; automatic retry is discouraged {evp("review-ttp-retry")}.'))
    control('foundry-routing', requirement=(
        'Pilot automatic routing only for newly created portal MCP tools without managed OAuth. '
        'The baseline instead configures the company gateway URL explicitly; it does not depend on automatic Foundry mediation. '
        f'Check the endpoint, authentication and request logs for each connection. {rec}'))

    replace('On merge, writes the list to each policy target.', 'Proposed adapters map reviewed Git decisions to the targets with validated automation.')
    replace('GitHub, Power Platform, Foundry</dd>', 'GitHub and Foundry; Power Platform pending API validation</dd>')
    replace('build the pipeline that applies it. Set the Microsoft 365 admin center by hand.', 'build and validate its target adapters. Configure Microsoft 365 access and Power Platform MCP policy manually until their respective automation is verified.')
    replace('Add an unapproved remote MCP server in a managed client</td><td data-label="Expected result">Blocked', 'Add an unapproved remote MCP server in a managed client</td><td data-label="Expected result">Blocked within verified policy scope; record documented exceptions')
    replace('Blocked in each target the pipeline writes to, after policy propagation and client refresh', 'Denied at automated targets after refresh; manual targets require recorded administrator changes')
    replace('Mark the server denied in Git; the pipeline removes it from its targets. In the Microsoft 365 admin center, block it in the registry and remove its connector by hand. Verify that calls are denied.',
            'Record the denial in Git and apply an urgent company-gateway block before waiting for client refresh. Reconcile automated targets, manually deny Power Platform and Microsoft 365 access, and block the separate BYO registration if used. Verify runtime denial and active-session behavior.')
    replace('Approval merges the change into the inventory. The pipeline then applies it to the policy targets.', 'Approval merges the inventory decision. Validated pipeline adapters update their targets; administrators apply and record the remaining manual policy changes.')
    replace('For Copilot Studio agents, no released guardrail checks call content (layer 3).', 'No released guardrail was established by this review for Copilot Studio call content (layer 3).')
    replace('The pages read on 2026-11-11 describe only preview controls at both layers.', 'The reviewed controls at both layers are preview; the supported-tool list does not establish MCP coverage.')
    replace('The pages read on 2026-11-11 describe only a preview control there.', 'The reviewed external detection control at that layer is preview.')
    replace('Not used for MCP tools: routing them through it is a preview feature', 'Automatic routing of newly added MCP tools through the Foundry integration is a preview feature')
    replace('Choose a v2 tier', 'Choose a suitable v2 tier if the Foundry integration is required')
    replace('The API Management integration does not automatically route agents through a customer-hosted gateway', 'Agent 365 does not automatically route agents through a customer-hosted gateway')
    replace('Confirm its public endpoint fits the backend isolation target.', 'Keep its public endpoint separate from the private backend.') if 'Confirm its public endpoint fits the backend isolation target.' in page else None
    replace('Dedicated AI Gateway is a separate product that can replace the API Management service gateway. It is the only gateway listed with tool blocking, tool activity and tool threat protection', 'Dedicated AI Gateway is a separate product that can replace the API Management service gateway. In the Agent 365 integration capability matrix, only AI Gateway lists tool blocking, tool activity and tool threat protection')
    replace('Blocked or preview route</li>', 'Rejected route or preview alternative</li>')
    # 2026-11-12 holistic review: cite the overview for the separate product, fix ownership and scope wording.
    replace('A separate AI Gateway product, not the API Management service ' + ev('apim-ai-not-separate'),
            'A separate AI Gateway product ' + evp('pv-aig-separate') + ', not the AI gateway capabilities built into the API Management service ' + ev('apim-ai-not-separate'))
    replace('Configure Microsoft 365 access and Power Platform MCP policy manually until their respective automation is verified.',
            'Configure Microsoft 365 agent access by hand; it has no API option. Configure Power Platform MCP policy by hand until its API path is verified.')
    replace('separate AI Gateway product and resource type ' + ev('apim-ai-not-separate') + ' ' + evp('pv-aig-separate'),
            'separate AI Gateway product and resource type ' + ev('apim-ai-not-separate') + ' ' + evp('pv-aig-separate', 'pv-res-change'))
    replace('<dt>Applies to</dt><dd>Agent 365 agent instances</dd>', '<dt>Applies to</dt><dd>Agent 365 agent instances and Foundry AI interactions</dd>')
    replace('No design control covers them. Pilot both, or limit it through GitHub account permissions.',
            f'No design control covers them. Pilot both switches, or limit the built-in server through GitHub account permissions. {rec}')
    replace('Hatched boxes and the lines that touch them are what preview adds. Everything else is the released design.', 'Hatching marks preview-only boxes; preview controls also live on shared boxes. The BYO line is a rejected alternative for this private backend.')
    assert page.count('What establishes the guarantee') == 14
    page = page.replace('What establishes the guarantee', 'Required control or validation')
    replace('The federated connector pages read on 2026-11-11', 'The federated connector pages reviewed on 2026-11-13')
    replace('The released-only design stays underneath. Details and limits',
            'Keep the baseline controls; replacing the gateway requires a tested migration and rollback. Details and limits')
    replace('If a preview feature changes, switch it off and fall back to the released-only design.',
            'Plan a safe stop and test migration back to the released gateway before replacing it.')
    replace('The released-only design stays underneath. Build it first.',
            'Build the released gateway first. Preserve its controls and test rollback before a preview gateway pilot.')
    replace('Safe stop, or a rollback to the released-only design</td>',
            'Safe stop or a tested migration back to the released gateway</td>')
    replace('Automatic routing of newly added MCP tools through the Foundry integration is a preview feature <span class="tg pv">preview</span>',
            'Automatic routing of newly added MCP tools through the Foundry integration <span class="tg pv">preview</span>')
    # 2026-11-12 second full read: the Option 2 use line was a fragment that lost "not used for MCP tools".
    replace('<dt>Use in this design</dt><dd>Automatic routing of newly added MCP tools through the Foundry integration <span class="tg pv">preview</span>',
            '<dt>Use in this design</dt><dd>Not used for MCP tools; the baseline sets the gateway URL itself. Automatic routing applies only to new portal MCP tools without managed OAuth <span class="tg pv">preview</span>')
    return page
