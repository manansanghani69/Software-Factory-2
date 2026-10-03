---
name: define-readiness-review
description: Review an approved definition and exact candidate packet from a fresh implementer's perspective, then record the human Readiness Gate result.
---

# Define readiness review

Use for one gate review session after the Definition Gate and candidate packet. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), the manifest, exact definition revisions, and the [gate record template](../project-definition-system/templates/gate-record.yaml). Treat the packet identity and revision as part of the evidence.

This is a manual review invocation. It reviews one exact packet and records one human Readiness result.

## Work

1. Review from a fresh implementer's perspective: can the implementer find outcome, scope/non-goals, rules/examples, exclusions, discretion, applicable contracts/design/data/quality/operations, source revisions, and proof methods?
2. Check definition currency, manifest completion, acceptance-to-work coverage, material questions, dependency order/cycles, shared-resource coordination, document access, residual risks, and appetite.
3. Report each defect at its responsible layer. A missing material rule returns to definition; a missing question returns to Wayfinder; a decomposition or dependency problem returns to mapping. Do not turn a gap into implementer discretion.
4. Have the human choose `pass`, `revise`, `spike`, `defer`, or `stop` against the exact packet. Record human/date, reasons, conditions, accepted risks, authorized next work, approved revisions, and packet identity. Readiness is separate from live issue state.

## Output and completion

Persist the readiness checklist and gate record. Complete when every criterion is assessed and the human result is recorded. A pass requires no unresolved material invention and authorizes only publication of the exact packet.

End with a handoff and, only after a pass, this prepared continuation:

```text
Run $define-github-publish for repository <owner/repo> and approved packet <ID/revision>. Read the Readiness record, source revisions, and existing planning ledger. Reconcile stable IDs, publish only the approved set, verify every relationship, and report the handoff.
```
