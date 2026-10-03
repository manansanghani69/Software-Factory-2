---
name: define-slice-definition
description: Define one coherent feature, contract, or behavioral branch with observable rules, examples, uncertainty, and Definition Gate evidence.
---

# Define slice

Use for one bounded definition session after the manifest. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), [the integration adapters](../project-definition-system/references/integration-adapters.md), and the current slice/manifest. For a feature use the [feature template](../project-definition-system/templates/feature-definition.md); for a contract or other conditional artifact read the applicable [content criteria](../project-definition-system/references/artifact-handbook.md#minimum-content-by-artifact).

This is a manual invocation: one session handles one coherent feature, contract, or behavioral branch. A large slice spans sessions. A repeated invocation in the same chat is not a fresh context reset.


## Work

1. Load only the relevant authoritative drafts, accepted decisions, source evidence, glossary, and current branch. Verify important claims against them.
2. Establish observable rules and concrete normal, failure/denied, permission, state/time/order, and boundary examples as relevant. Keep rule/example IDs stable.
3. Draft applicable behavior, UX/design, API/event, data, quality, security, and operational content from the manifest. Link shared contracts instead of duplicating them.
4. Route material unknowns to Wayfinder; classify residual uncertainty as resolved, implementation discretion, spike, deferred, or out of scope. Missing detail is not automatically discretion.
5. Cross-check conflicting definitions and shared contracts. For a successor shared contract, apply the [rolling-slice transition requirements](../project-definition-system/references/operating-contract.md#rolling-slices-and-shared-contracts). When every required branch is current, assemble Definition Gate evidence naming exact revisions. Ask the human for the result; record no pass without approval.

## Output and completion

Persist the definition artifacts, decision links, examples, uncertainty classification, discretion, and gate evidence. The branch is complete when its manifest criterion is met. The Definition Gate passes only after all required definitions agree and the human approves their revisions.

End with a handoff and either another definition invocation or:

```text
Run $define-delivery-map for <slice>. Read the passed Definition Gate, approved document revisions, accepted examples, exclusions, discretion, and dependencies. Draft a bounded candidate packet without inventing behavior.
```
