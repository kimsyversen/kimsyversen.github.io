# VS Code agent guardrails: decisions

15 November 2026.

- Scope is the guardrails around AI agents in VS Code: Workspace Trust, permission levels, approvals, the sensitive-file rule, agent sandboxing and review. Reason: this is where VS Code uses the words guardrail and sandbox today. Extension and MCP trust appear only as short rows (superseded for MCP by the seventh action below).
- The page covers Copilot harness sessions with the default tools. Reason: the sandbox doc describes that setup, and the other harnesses behave differently. Mixing them would make each outcome a table of exceptions.
- The main figure is a course with four gates that one agent action runs through. The reader picks the action and the settings. Reason: the docs' key point is that approval and sandbox answer different questions, and that is easiest to see when one action meets both.
- Six actions (superseded by the seventh action below), picked so each shows a different rule: read-only command, `rm`, a read outside the project, a network send, an edit tool call, a fetch tool call.
- "When asked, you say Yes or No" (now labelled "Your answer when VS Code asks") is a setting, not a button in the flow. Reason: one model, no hidden state, and every result is reproducible from the settings.
- Outcomes that combine rules, and are not stated in one source sentence, carry `inference` or `unverified` at the gate.
- Each gate result shows the exact quote and a link with a text fragment that jumps to the passage.
- Same worksheet look as the threat modeling page: paper, ink, hairline rules, red only for "stopped". No cards, pills or gradients.
- The small ASCII face is the only decoration. It moves to the gate where the action ends.
- No ASCII figure file beside the page. Reason: the figure is interactive, not static, and each gate result is already plain text.
- No browser storage and no shared-state links. Reason: least upkeep.
- The docs' six-step baseline is quoted, not rewritten as recommendations. The sandbox step was tagged `preview`; superseded on 24 November 2026, when all preview tags were removed.
- Where the docs are silent, the VS Code source code is the source, quoted and linked by line at a pinned commit. Reason: it is the primary source for what the product does, and a pinned link keeps showing the quoted lines. Used for the built-in terminal rules (`cat`, `curl`) and for the "run outside the sandbox" prompt under Allow all.
- `cat ~/.ssh/id_ed25519` now runs without a question under Manual permissions. Supersedes the first version, which showed a prompt and marked it `unverified`.
- "The judging model says Yes or No" (now labelled "The AI reviewer's answer") is a setting, like "When asked, you say". Reason: no source says what the judge answers for a given call, so the page shows both outcomes. Supersedes the first version, where Assisted always passed.
- Under Assisted the judge is checked before the sandbox rule. Supersedes the first version, where a sandboxed command skipped the judge. Reason: the source code asks you when the judge says no, also for a sandboxed command.
- A control that cannot change the result is switched off, for example the `.env` rule under Allow all, the judge outside Assisted, and "Your answer when VS Code asks" when no check asks. Since 24 November 2026 `sync()` finds every such control by running `evaluate()` with each option and comparing the output. Reason: a live control that does nothing reads as a rule that works.
- Each control that maps to one VS Code setting shows the setting name, linked to the docs passage that names it. Reason: a reader can then change the same thing in VS Code. Controls without a setting show none.
- Seventh action: a tool call on a local MCP server. Supersedes "six actions" above. Reason: the docs baseline then had a step about MCP servers (the current baseline covers tool sources in step 5), and no action met the gates as one. It shows the approval question and whether the server runs inside the sandbox, nothing more, to keep the model small.
- Reader-facing text uses plain, literal words: "sandbox" instead of "fence", "checks" instead of "gates" or "course", headings that say what the section holds, step headings as questions, and results that start with "Result:" and say who approved. Supersedes the course and fence wording in the decisions above; the four-step figure itself stays. Reason: the owner found the metaphors and short verdicts ("Send the agent through", "It ran, because you said yes.") confusing. Ids, anchors and code names (`#course`, `#not-a-fence`, `fenced`) are unchanged so links keep working.
- 24 November 2026: the `.env` rule defaults to "Ask first" in the simulator. Reason: `chatSettings.ts` has a default rule for `.env` set to ask. Supersedes the earlier default of no rule.
- 24 November 2026: all `preview` tags and the Status column of the platform table are removed. Reason: the current docs no longer mark the sandbox as preview on macOS or Linux, and the Windows row says Experimental.
- 24 November 2026: per-server MCP sandboxing stays out of the model. The MCP example uses the default `chat.agent.sandbox.mcpServers`. Reason: keeps the simulator small, and the scope paragraph says it.
