# Sandcastle Resources

## Knowledge

- [README: github.com/mattpocock/sandcastle](https://github.com/mattpocock/sandcastle)
  Primary source. Covers the full API surface: `run()`, sandbox providers, branch strategies, prompt resolution, templates. Use for: anything about the current JS API.
- [Sandcastle docs directory: docs/](https://github.com/mattpocock/sandcastle/tree/main/docs)
  ADRs (architecture decision records), e.g. ADR 0003 worktree reuse, ADR 0010 structured output, ADR 0018 fork vs resume, ADR 0019 hanging-process timeouts. Use for: the design rationale behind the library's mechanics.
- [Matt Pocock's YouTube](https://www.youtube.com/@mattpocockuk)
  Screencasts of building/using agent tooling and the software-factory pattern. Use for: seeing the workflow in action and hearing design intent.
- [@ai-hero/sandcastle on npm](https://www.npmjs.com/package/@ai-hero/sandcastle)
  Package facts: version, exports, publish cadence. Use for: keeping this workspace pinned to a real version.
- [Standard Schema (standardschema.dev)](https://standardschema.dev)
  The schema-validation interface Sandcastle's `Output` uses. Use for: structured-output lessons (Zod/Valibot/ArkType).
- [OpenCode Zen (dev.opencode.ai/docs/zen)](https://dev.opencode.ai/docs/zen)
  Curated model gateway with free models (Big Pickle, Union Alpha Free, etc.). Use for: free-tier `opencode()` agent wiring. Live model list: `curl https://opencode.ai/zen/v1/models`.

## Wisdom (Communities)

- [Sandcastle GitHub Issues](https://github.com/mattpocock/sandcastle/issues)
  Real problems people hit with providers, Windows quirks, and agent config. Use for: troubleshooting real-world breakage.
- [Matt Pocock's Discord (#AI channel)](https://discord.gg/matt)

## Gaps

- No verified Windows-specific setup notes from a primary source yet — collect during the `<token>` setup and `init` lessons and record what actually works.