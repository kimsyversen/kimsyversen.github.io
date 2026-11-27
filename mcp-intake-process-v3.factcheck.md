# Fact check: MCP Server Intake Process

Checked 27 November 2026.

| Claim | Source | Verdict |
|---|---|---|
| About 70% of exposed MCP servers Wiz tested returned their full tool catalog to anonymous callers. | [Wiz Research, “The risk hiding behind exposed MCP servers”](https://www.wiz.io/blog/the-risk-hiding-behind-exposed-mcp-servers), “By the numbers” | Verified. The source describes exposed servers, not all MCP servers, and specifically says they returned the full tool catalog to anonymous callers. |
| The assessment uses four domains from the NHI guide. | [NHI MCP Server Trust Assessment Guide](https://nhimg.org/mcp-server-trust-assessment-guide), domains 1 to 4 | Verified. The guide names identity and authentication, permissions and tool surface, provenance, and change control. The intake's risk tiers, approval authorities and scanning matrix are organizational proposals. |
| Backslash Security provides guidance on endpoint and agent-context risks. | [How to Evaluate an MCP Server's Risk Before Employees Install It](https://www.backslash.security/learning/how-to-evaluate-an-mcp-server-s-risk-before-employees-install-it), “What makes an MCP server risky before anyone installs it?” | Verified as vendor guidance on execution location, inherited credentials, tool permissions and untrusted content. |

HTML checked in Chrome at 320, 390, 640, 850 and 1440 CSS pixels. All five steps, shared links, browser history, keyboard activation and reference disclosures worked without page overflow or console errors. Static checks covered local links, unique IDs and section anchors. The page retained all five steps with JavaScript disabled. Browser testing covered Chrome.

The workflow map was checked against steps 1 to 5 in the Markdown. Its branches show a rejected decision and reassessment after material change. Chrome checks at eight widths from 320 to 1600 CSS pixels covered both view links, the index link, expandable actions and branches, keyboard activation, history, direct links and page overflow. The print view includes all five steps and the assessment reference.

The canonical URL now opens the workflow map. Chrome checks at 320 to 1600 CSS pixels confirmed that opening and closing each of the 15 action dialogs preserves every card's dimensions and position. Keyboard dismissal, focus return, the detail-view link and the existing map URL also passed. With JavaScript disabled, action text remains available through inline disclosures.

The action dialogs were replaced on 27 November 2026 by a popover beside the clicked action. It copies that action's rows or paragraphs from the detail view at load time, so the text has one source. "Check effective access" and "Record evidence and safeguards" have no matching part in the detail view and show their map note instead. Chrome checks at 320, 390 and 1440 CSS pixels confirmed for all 15 actions that the popover opens inside the viewport, cards keep their size and position, page IDs stay unique and the page does not scroll sideways. Clicking the same action again, Escape and the close button each close it, and Escape returns focus to the action. The detail-view link opened the matching step. No console errors. Other browsers were not tested.
