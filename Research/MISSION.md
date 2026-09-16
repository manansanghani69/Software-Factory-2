# Mission: Building an autonomous agent pipeline with Sandcastle

## Why

I want to build a project that runs without human intervention — AFK coding agents that pick up work on my GitHub repos, implement it, review it, and merge it. Sandcastle is the orchestration layer that makes that possible, and I want to understand Matt Pocock's agent-orchestration patterns deeply enough to build this myself.

## Success looks like

- `sandcastle init` + `run()` working on my own machine against a real repo, changes landing safely on a branch
- A **fully autonomous loop**: an agent picks up issues, implements them, a second agent reviews, and results merge back — no human touching it mid-flight
- I can explain and re-build Sandcastle's core mechanics (branch strategies, sandbox providers, sessions, lifecycles) from memory
- A review pipeline that runs `npm test` in the sandbox and gates the merge on green tests

## Constraints

- Machine: Windows (PowerShell), Docker Desktop installed
- No Claude Code token set up yet — need to assess fastest path to a working agent provider (Claude Code via `claude setup-token` vs opencode/codex)
- Prior knowledge already strong: TypeScript, Claude Code as an agent, Docker, git worktrees
- Speed matters — fluent in tooling already, so lessons should go straight to Sandcastle-specific mechanics

## Out of scope

- General TypeScript/Node fundamentals
- Docker fundamentals
- Claude Code feature tour (used only as the agent Sandcastle drives)
- Building a provider from scratch for its own sake — only if a real need appears