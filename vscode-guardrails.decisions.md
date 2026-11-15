# VS Code agent guardrails: decisions

15 November 2026.

- Scope is the guardrails around AI agents in VS Code: Workspace Trust, permission levels, approvals, the sensitive-file rule, agent sandboxing and review. Reason: this is where VS Code uses the words guardrail and sandbox today. Extension and MCP trust appear only as short rows.
- The page covers Copilot harness sessions with the default tools. Reason: the sandbox doc describes that setup, and the other harnesses behave differently. Mixing them would make each outcome a table of exceptions.
- The main figure is a course with four gates that one agent action runs through. The reader picks the action and the settings. Reason: the docs' key point is that approval and sandbox answer different questions, and that is easiest to see when one action meets both.
- Six actions, picked so each shows a different rule: read-only command, `rm`, a read outside the project, a network send, an edit tool call, a fetch tool call.
- "When asked, you say Yes or No" is a setting, not a button in the flow. Reason: one model, no hidden state, and every result is reproducible from the settings.
- Outcomes that combine rules, and are not stated in one source sentence, carry `inference` or `unverified` at the gate.
- Each gate result shows the exact quote and a link with a text fragment that jumps to the passage.
- Same worksheet look as the threat modeling page: paper, ink, hairline rules, red only for "stopped". No cards, pills or gradients.
- The small ASCII face is the only decoration. It moves to the gate where the action ends.
- No ASCII figure file beside the page. Reason: the figure is interactive, not static, and each gate result is already plain text.
- No browser storage and no shared-state links. Reason: least upkeep.
- The docs' six-step baseline is quoted, not rewritten as recommendations. The sandbox step is tagged `preview`.
