# Mission and prior-knowledge intake for the Sandcastle course

Established at the first session (2026-09-16): the mission is a fully autonomous repo workflow — AFK agents that implement, review, and merge without human intervention — plus understanding Matt Pocock's orchestration patterns. Prior knowledge already strong (TypeScript, Claude Code-as-agent, Docker, git worktrees), so all foundational material is skipped. The critical environment fact is that the user has Docker Desktop but no Claude Code token yet.

## Implications for teaching

- `opencode()` is a validated built-in agent provider, so the first autonomous run can happen without a Claude Code token. Lesson 0001 is built around that unlock; the session-resume / structured-output-retry path (which needs `claudeCode`/`codex`/`pi`) is a later hurdle, not the first one.
- Primary source for all knowledge: the Sandcastle README, especially How-it-works, Prompts, and RunOptions.
- Workspace is Windows/PowerShell; steps must be PowerShell-safe.
- A glossary is deferred until the user demonstrates working understanding of Sandcastle terms (run, agent provider, sandbox provider, branch strategy) after completing Lesson 0001.