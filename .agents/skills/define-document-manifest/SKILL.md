---
name: define-document-manifest
description: Assess a selected slice's documentation and risk dimensions, record required or skipped artifacts, and expose the next definition frontier.
---

# Define document manifest

Use after a passing Slice Gate. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), the current slice and existing documents, and the [manifest template](../project-definition-system/templates/document-manifest.md). Load detailed references only for dimensions that apply.

## Work

1. Inspect every dimension in the artifact handbook: behavior/state; UX; API/event/integration; data/migration; architecture; security/privacy/trust; quality; operations/rollout; research/experiments; support/user docs; measurement; and mandatory content.
2. For each dimension mark `required`, `covered by existing current artifact`, or `skipped` with a concrete applicability reason. Use the handbook's content criteria to record scope, owner, approver, prerequisites, evidence, intended authority, and content depth.
3. Combine sections when that avoids duplication. Put genuinely shared contracts in one authoritative home. Verify current artifacts rather than accepting names or templates as coverage.
4. Record the drafting order and the first unblocked artifact or rule. A skip is a judgment, not an excuse to omit relevant behavior or acceptance.

## Output and completion

Persist the complete manifest and index/handbook updates. Complete only when every dimension and mandatory information item is accounted for, including deliberate skips and current-artifact verification.

End with a handoff and a prepared manual continuation:

```text
Run $define-slice-definition for <slice> on <next artifact or behavioral branch>. Read the manifest row, scope baseline, applicable decisions, and only the authoritative sources needed for that branch. Draft rules/examples, classify uncertainty, and stop at the Definition Gate when all branches are current.
```
