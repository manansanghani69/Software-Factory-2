# Notes

## Preferences (from intake, 2026-09-16)

- Strong prior: TypeScript, Claude Code-as-agent, Docker, git worktrees. DO NOT re-teach these.
- Mission emphasis: fully autonomous repo workflow (no human in the loop), + understanding Matt's orchestration patterns.
- Wants hands-on, short lessons with a single tangible win each.
- Environment: Windows/PowerShell, Docker Desktop installed, NO Claude Code token yet.
- Resolved 2026-09-16: use `opencode()` as the agent provider with an OpenCode Zen free-model key (`OPENCODE_API_KEY` in `.sandcastle/.env`). Model: `opencode/big-pickle`. See reference/free-tier-setup.html and RESOURCES.md. `maxRetries`/`fork()` remain unavailable on `opencode()`, so the retry path still needs `claudeCode`/`codex`/`pi` later.
- Lesson numbering: 0001, 0002, ... ; reference docs in ./reference/, components in ./assets/.

## Style

- No comments in code samples unless teaching.
- Tufte-ish: serif body, crisp code, margin notes where useful. Print-friendly.