---
name: define-change-recovery
description: Reconcile new evidence or a material change against approved definitions, stale work, dependencies, gates, and restart authorization.
---

# Define change recovery

Use when new evidence or a change request affects an accepted Project Definition baseline. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), [the integration adapters](../project-definition-system/references/integration-adapters.md), the affected definitions/issues, and the [change-impact template](../project-definition-system/templates/change-impact.md). Start from the current index, latest approvals, and exact old baseline.

This is a manual recovery invocation for one affected baseline. It does not silently reopen unrelated work.

## Work

1. Record the trigger, evidence, affected outcome/rule/contract, old baseline, and the scope of possible impact.
2. Trace reverse links through `depends_on`, acceptance references, contracts, scope nodes, gate records, and issue bindings. Mark affected definitions and issues stale; control affected implementation through its consumer. Preserve unrelated approvals.
3. Create a precise Wayfinder question or scoped fog entry. Resolve the new uncertainty with the human and update the authoritative definition and significant decision history. Create an ADR only for a costly-to-reverse, surprising trade-off with real alternatives.
4. Recompute scope, acceptance coverage, dependencies, coordination, risk, and appetite. For a successor shared contract, apply the [rolling-slice transition requirements](../project-definition-system/references/operating-contract.md#rolling-slices-and-shared-contracts). Classify affected work as revised, spiked, deferred, out of scope, or stopped.
5. Repeat the relevant gates through Readiness for affected execution work. Update or supersede issue bindings while preserving stable IDs where identity remains and linking successors where scope changes fundamentally.

## Output and completion

Persist the impact record, successor definitions/approval, stale/superseded links, reconciled issues, and restart guidance. Complete when every affected work item is reauthorized at a current baseline, deferred, or explicitly stopped, and unrelated approvals remain identifiable.

End with a handoff naming the responsible next stage and its exact inputs. Common continuations are `$define-slice-definition` for changed behavior, `$define-delivery-map` for changed decomposition, or `$define-readiness-review` after the affected packet is rebuilt.
