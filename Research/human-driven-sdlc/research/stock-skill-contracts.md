# Stock skill contracts and local compatibility

Inspected: **2026-10-07**, Asia/Kolkata. Resolves the factual question in [Verify stock skill contracts and local compatibility](https://github.com/manansanghani69/Software-Factory-2/issues/2), within [Human-driven AI SDLC — decision map](https://github.com/manansanghani69/Software-Factory-2/issues/1).

The diagram is a proposal under review. This inventory records source contracts and candidate adaptation needs; it does not select a workflow, settle a human decision, or install changes. Earlier independent research efforts are not authority here.

## Evidence and revision

Upstream was inspected at commit [`6fd947921b935b7e1e69293a200400f0fdd5c15f`](https://github.com/mattpocock/skills/commit/6fd947921b935b7e1e69293a200400f0fdd5c15f). Every upstream link below is pinned to that revision. Full `SKILL.md` bytes were fetched from the official repository and compared with local files under `/Users/manansanghani/.agents/skills/`. Fingerprints identify inspected content, not a package release. Prompt instructions describe expected agent behavior; they are not deterministic guarantees that a run succeeds.

## Confirmed contracts

| Skill and source | Input and prerequisites | Output and mutations | Human interaction |
| --- | --- | --- | --- |
| [setup-matt-pocock-skills][setup] | Existing repository, agent instructions, remote, tracker/domain conventions. | Configures `docs/agents/issue-tracker.md`, domain rules, optional triage vocabulary, and the existing agent instruction file. Does not install skills or create empty glossary/ADR placeholders. | Presents findings and drafts before writing; confirms tracker and applicable choices. |
| [grill-me][grill-me] / [grilling][grilling] | A plan, idea, or decision. `grill-me` invokes `grilling`; both live under **productivity**, not engineering. | Shared understanding through a branching decision tree. No PRD template or publication step. Environment facts are delegated to subagents. | Asks the current unblocked questions with recommendations, waits for actual answers, and advances in rounds. Requires confirmation of shared understanding before acting. |
| [wayfinder][wayfinder] | A large uncertain effort with a named destination; configured tracker and its wayfinding operations. | Creates a map and child **decision questions**, claims tickets, records resolution comments, closes resolved tickets, updates the index/fog/dependencies. Default output is decisions, not build deliverables. | Destination and frontier are explored with the human. Grilling/prototype tickets require live human exchange. Charting resolves no human tickets; subsequent sessions resolve at most one, with research exceptions. |
| [to-spec][to-spec] | Current discussion and codebase understanding; tracker, triage vocabulary, glossary/ADRs where present. | Publishes a specification with problem, solution, user stories, implementation/testing decisions, scope, and notes; applies `ready-for-agent`. No general interview; synthesizes prior decisions. | Explicitly confirms proposed testing seams. The template asks for extensive user stories; it is not inherently lightweight. |
| [to-tickets][to-tickets] | Plan, specification, or conversation; fetches referenced issue body/comments; tracker and triage configuration. | Publishes build tickets with acceptance criteria and blockers, normally complete vertical slices sized to one context. Wide refactors have an expand–migrate–contract exception. Uses native dependencies and parents when supported; does not close/modify the parent. | Presents proposed deliverables/granularity/blockers and iterates until the human approves publication. |
| [implement][implement] | A spec or build tickets; agreed testing seams for TDD. | Changes code/tests, runs regular typechecks and focused tests plus a final full suite, invokes code review, then commits on the **current branch**. Does not specify branch creation, PR creation, or ticket closure. | Test seams are pre-agreed; the short skill does not define further stage checkpoints or authorize automatic progression to release. |
| [code-review][code-review] | Fixed comparison point, nonempty valid diff, spec source where available, standards sources and tracker configuration. | Parallel Standards and Spec reports, kept separate. Missing spec can be reported as unavailable. Reports findings; it does not itself promise fixes or standards changes. | Asks for an omitted fixed point and missing spec source. Source includes a defined standards-smell baseline overridden by documented repository standards. |
| [pr][pr] | Change summary and concrete before/after evidence. | Formats a PR **body** with visual summary, evidence, and merge-danger assessment. No push, PR creation, merge, or deployment operation. | No independent approval or execution protocol is defined in this formatting skill. |
| [codebase-design][codebase-design] | Module/interface/seam questions or another skill needing the vocabulary. | Shared architectural principles and terminology: depth, interface, seam, adapter, leverage, locality. A reference to consult, not a standalone design-review session or product UX method. | Does not prescribe a mandatory separate interview or decision artifact. |
| [tdd][tdd] | Behavior to implement and public seams confirmed with the human; glossary/ADRs where present. | Behavior tests through public interfaces and minimal implementation, one failing test then green per slice. Avoids implementation-coupled/tautological tests and bulk horizontal test writing. | No test at an unconfirmed seam. Current source places refactoring in review rather than the implementation loop. |

The [engineering catalog][catalog] distinguishes user-invoked skills from references reachable implicitly. The inspected local `agents/openai.yaml` files for wayfinder, to-spec, to-tickets, implement, and grill-me set `allow_implicit_invocation: false`; code-review, pr, and grilling lack that restriction. A manually driven playbook can invoke skills explicitly, but references being available does not itself define stage transitions.

### Existing candidates that may be reused

- **Specification and build planning:** `to-spec` and `to-tickets` already separate synthesis from executable work. Whether every entry path uses both remains a decision in [Choose entry paths and the minimum planning route](https://github.com/manansanghani69/Software-Factory-2/issues/4) and [Define the decision-to-spec handoff and readiness](https://github.com/manansanghani69/Software-Factory-2/issues/10).
- **Architecture vocabulary plus interviewing:** [grill-with-docs][grill-with-docs] invokes `grilling` and `domain-modeling`. `codebase-design` supplies module-design vocabulary; it does not replace UX planning or constitute a full architecture gate.
- **Whole-spec orchestration:** [implement-spec][implement-spec] drives parallel implementers in worktrees, an integration branch, merger subagents, final review/remediation, and tracker closeout. This is a distinct optional mode, not a requirement for the map's manually initiated stages.
- **Other specialized reuse:** the pinned catalog includes `prototype`, `diagnosing-bugs`, `research`, and `wizard`. Their presence is confirmed; this inventory has not audited their complete contracts or selected them for any entry path.

## Optional Impeccable capability

The installed [Impeccable skill](/Users/manansanghani/.agents/skills/impeccable/SKILL.md) declares **version 4.1.1**. It covers frontend UX/UI design, critique, accessibility/performance audit, design-system extraction, and related refinements. Its [shape playbook](/Users/manansanghani/.agents/skills/impeccable/reference/shape.md) discovers the audience/job, behavior, states, content ranges, direction, layout, and constraints; returns a design brief; obtains explicit confirmation or one correction round; and stops without writing implementation code or a direction contract.

This supports an optional planning route for missing UX design. It differs from `codebase-design`, which concerns code modules and interfaces. Availability is a fact; adoption, fidelity, treatment of existing designs, and design-readiness criteria remain with [Choose UX design routes and design readiness](https://github.com/manansanghani69/Software-Factory-2/issues/8). Only the main Impeccable instruction and shape reference were inspected here; its other commands and runtime scripts were not exercised.

## Local compatibility

All entries in the contract table and the additional `grill-with-docs`/`implement-spec` candidates exist locally. All compared main instruction files match the pinned upstream bytes **except**:

1. **implement:** local text says `Use /tdd` and `use /code-review`, where upstream says to call the Skill tool. The requested behaviors otherwise match. Invocation adaptation is relevant in environments without that tool.
2. **to-tickets:** local text uses “native blocking / sub-issue relationship” rather than separating the two, lacks the upstream explicit requirement to make build tickets children of an existing source issue, and always retains a body blocker section rather than omitting it when native edges are set. It still requires approval and does not modify the parent. This is instruction drift, not evidence that native hierarchy/dependencies are unavailable.

The observed [repository tracker configuration](../../../docs/agents/issue-tracker.md), at checkout base `69b9dab88c361fa557c62e6b7fe3d83a77e69f4b`, describes ordinary GitHub issue operations but lacks the Wayfinding operations section expected by stock `wayfinder`; this is a repository configuration adaptation need, separate from installed skill content. Creating/installing that adaptation is outside this research ticket.

SHA-256 fingerprints of locally inspected main instructions:

| Local skill | SHA-256 of `SKILL.md` | Compared upstream |
| --- | --- | --- |
| setup-matt-pocock-skills | `9a0c21694be19fa3eefc39343355d3af7414716ba364882c7432c2f821eac3e9` | Identical |
| grill-me | `caaf8b8de1684f96e26b28f3c29189db5c89cce4b73e1c93d86164f66ef88637` | Identical |
| grilling | `10ff989e7498b23b5acb49d5048f11dcd906757d2f79c5cdf8a00001381296f2` | Identical |
| grill-with-docs | `7de372c13488f1ee96cc11cd8907b56b6809cc93eef776eeddd37de6b6cbe3fe` | Identical |
| wayfinder | `fee6e1d0c50f0e736b4ef8a599060c959afae904c9a97d82c97f049fcc3aa0f1` | Identical |
| to-spec | `43ad9cf318e5e7d3d1fa360253a37021796dc87a0c2e595ad262661a10f85088` | Identical |
| to-tickets | `5c9fba69845c2519b9b35b9af42ae5142c21f8ca15ac2123dc2722002c8058ae` | Differences above |
| implement | `6d3fd9e83b8f36e5213854779db49b256a457a7ebb4a503e53fa7dcff696adc3` | Differences above |
| implement-spec | `7a22dd2e60b8fcece478ced9d2533582adf3520d695acd3ab715341535c9e56d` | Identical |
| code-review | `47f4e52c21694def9c7c11cbfbf891ca35eac7a93e395797515be3c8a409ae50` | Identical |
| pr | `ab63f1cf78647389edcd386c9427c5dfca27ed2836930c24773ffee834c19bcd` | Identical |
| codebase-design | `2c20617f87ec8af6a434859f381b2f061a69b530444e74eb39e78bb016a6d1e2` | Identical |
| tdd | `93ea419b76e9caaf26153b828e984f7c3fb136f4caa67b14af95f32ea965a1cc` | Identical |
| impeccable, version 4.1.1 | `9d124382509eb15da0862f145bca0e53be00aaddb05272e4efc9a0832de048a9` | No Matt Pocock counterpart |

Impeccable `reference/shape.md`: `a55f016c046cb6a27c55bd7f346375aeb506a755c4fbca19a5f92dbd42309c23`. Main-file identity does not prove every supporting reference/runtime file or host integration is identical.

## Unsupported promises in the original diagram

These are candidate requirements for the existing human decision tickets, not automatically approved changes:

- **Setup ensures all contradictory documents are updated:** stock setup provides consumer rules and configuration, not a universal consistency policy. Artifact authority and invalidation rules belong to [Choose artifact authority and change recovery](https://github.com/manansanghani69/Software-Factory-2/issues/6).
- **Lightweight grill-me outputs a structured PRD:** the interview has no fixed output artifact or lightweight budget. Define both in [Define lightweight framing and the PRD contract](https://github.com/manansanghani69/Software-Factory-2/issues/7).
- **Wayfinder children are ready to implement after interviewing:** decision questions and build tickets have different purposes. Their conversion/readiness belongs to the handoff and ticket-sizing decisions.
- **Codebase-design is a product-design or standalone architecture review step:** its documented role is an architectural reference. An explicit check can use it, but its trigger and output must be specified by the human.
- **Code review updates code to standards:** review reports findings. Remediation/acceptance and PR operation ownership belong to [Choose review coverage, remediation, and PR ownership](https://github.com/manansanghani69/Software-Factory-2/issues/14).
- **The final /pr stage delivers release:** that skill only shapes body text. Merge/release/rollback remain separate work and are already represented by [Define merge, release verification, and rollback handoffs](https://github.com/manansanghani69/Software-Factory-2/issues/15).

The implementation/review sequencing and change-visibility question is deliberately recorded only in [Verify which changes the stock implementation review actually sees](https://github.com/manansanghani69/Software-Factory-2/issues/3); consult that ticket's research asset/resolution for its evidence.

No newly sharp product/workflow question outside the current map was identified. Local version policy, instruction-host compatibility, and tracker configuration are concrete adaptation facts for the existing checkpoint/artifact/review decisions, rather than reasons to select tooling in this research ticket.

[catalog]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/README.md
[setup]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/setup-matt-pocock-skills/SKILL.md
[grill-me]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/productivity/grill-me/SKILL.md
[grilling]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/productivity/grilling/SKILL.md
[grill-with-docs]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/grill-with-docs/SKILL.md
[wayfinder]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/wayfinder/SKILL.md
[to-spec]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/to-spec/SKILL.md
[to-tickets]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/to-tickets/SKILL.md
[implement]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/implement/SKILL.md
[implement-spec]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/implement-spec/SKILL.md
[code-review]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/code-review/SKILL.md
[pr]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/pr/SKILL.md
[codebase-design]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/codebase-design/SKILL.md
[tdd]: https://github.com/mattpocock/skills/blob/6fd947921b935b7e1e69293a200400f0fdd5c15f/skills/engineering/tdd/SKILL.md
