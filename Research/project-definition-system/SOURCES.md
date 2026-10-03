# Research evidence

Reviewed 2026-10-01. Framework descriptions below are source facts; the four gates, artifact split, skill set, and exact stage order are our synthesis and the user's accepted choices. This is a workflow design, not a pilot result.

| Source | What it establishes | How this design uses it |
| --- | --- | --- |
| [Shape Up: Principles of Shaping](https://basecamp.com/shapeup/1.1-chapter-02) | A solution needs meaningful boundaries and enough macro detail, while leaving implementation room. Shaping and building can overlap. | Define material behavior for the selected slice and leave implementation discretion explicit. |
| [Shape Up: Hand Over Responsibility](https://basecamp.com/shapeup/3.1-chapter-10) | Up-front tasks differ from work discovered during implementation; the whole project context must remain accessible. | Use an initial ready issue set, revisable mechanics, and linked slice context on each issue. |
| [Shape Up: Place Your Bets](https://basecamp.com/shapeup/2.3-chapter-09) | New-product work can need bounded R&D before reliable shaping. | Permit learning spikes with questions and exit conditions before production commitment. |
| [Jeff Patton: Dual Track Development](https://jpattonassociates.com/dual-track-development/) | Discovery and delivery are concurrent learning/building activities requiring collaboration. | Shape the next slice while delivering the current slice; feed learning back into both. |
| [Jeff Patton: Story Mapping reference](https://www.jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) | Begin with the whole journey at low resolution, explore variants, and choose holistic release slices. | Build the journey before detailed task decomposition; attach an outcome to every slice. |
| [SVPG: Four Big Risks](https://www.svpg.com/four-big-risks/) | Discovery considers value, usability, feasibility, and viability. | Inspect the relevant risk profile when selecting and defining slices. |
| [Cucumber: Example Mapping](https://cucumber.io/docs/bdd/example-mapping/) | Stories can be clarified through rules, examples, questions, and newly identified stories. | Use concrete examples for normal, failure, and boundary behavior; keep unanswered questions visible. |
| [Michael Nygard: Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) | Significant decisions benefit from small records of context, decision, status, and consequences; history remains accessible. | Preserve consequential accepted decisions in ADRs and link superseded records. |
| [Rust RFC process](https://rust-lang.github.io/rfcs/) | Substantial changes get proposal/review/acceptance; accepted proposals do not guarantee scheduling or implementation. | Distinguish a proposed solution from a baseline and reserve proposal documents for decisions that need review. |
| [GitHub: Adding sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues) | Up to 100 sub-issues per parent and eight nested sub-issue levels; relationships can include other repositories. | Use native decomposition within limits, with explicit continuation links for deeper conceptual maps. |
| [GitHub: Issue dependencies](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-issue-dependencies) | Blocking relationships are distinct from parent/sub-issue decomposition. | Use blockers for real prerequisites and parents for grouping. |

## Local primary material

- Installed [Wayfinder skill](/Users/manansanghani/.agents/skills/wayfinder/SKILL.md): one destination/map, direct child decision tickets, progressive fog, blockers, claims, and separate chart/work modes. Its current map is two levels by convention, independent of GitHub's deeper native capability.
- [Grilling](/Users/manansanghani/.agents/skills/grilling/SKILL.md) and [Domain Modeling](/Users/manansanghani/.agents/skills/domain-modeling/SKILL.md): decision frontiers, human choices, canonical glossary, and sparing ADR capture.
- [Writing for Agents](/Users/manansanghani/.agents/skills/writing-for-agents/SKILL.md): clear completion criteria, shared references, and manually invoked router/stage skill boundaries.
- Existing [Sandcastle inception guide](../sandcastle/reference/project-inception-workflow.html) and [ADR](../sandcastle/docs/adr/0001-decision-first-inception-before-sandcastle.md): prior local synthesis. This new research develops its own authority and manual operation model without modifying those files.

## Deliberate adaptations

This system uses more explicit definition and issue readiness than Shape Up's usual project handoff because the desired consumer is a human-plus-AI implementation workflow. That is a trade-off: the initial decomposition aids execution, but the readiness gate must never imply that all future tasks are known. The approved behavioral baseline and permitted discretion determine which later changes are routine and which reopen definition.

Four gates are our operating design rather than a universal industry standard. Documentation effort follows actual change and risk. No framework proves these gates or skills work in this repository; a later pilot will supply that evidence.
