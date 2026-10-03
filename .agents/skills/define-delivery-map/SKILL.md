---
name: define-delivery-map
description: Decompose approved definitions into a traceable candidate delivery map and execution packet with coverage and real dependency order.
---

# Define delivery map

Use after a passing Definition Gate. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), the approved definitions and examples, and the [delivery-map](../project-definition-system/templates/delivery-map-record.yaml) and [execution issue](../project-definition-system/templates/execution-issue.md) templates.

This is a manual invocation. It drafts one bounded candidate packet and ends with a fresh-session handoff; it does not publish or start execution.

## Work

1. Decompose into meaningful scope nodes. Give each one stable ID, structural parent, slice/outcome, source documents, acceptance references, execution role (`container` or `executable`), and baseline revision.
2. Define bounded execution issues without inventing product behavior. Map every accepted rule/example to executable work and integration acceptance. Apply the operating contract's container completion criteria and avoid duplicate authorization between containers and children.
3. Add actual dependencies and shared-resource coordination. Check cycles, unknown endpoints, and current native nesting/width capabilities. For conceptual overflow apply the operating contract's continuation evidence requirements, including the complete stable-ID path and both link directions.
4. Preserve implementation discretion and link every candidate unit to authoritative documents. Record coverage, execution order, unresolved ambiguity, and overflow exceptions in the candidate packet.

## Output and completion

Persist the Delivery Map, candidate ticket packet, coverage matrix, dependency/coordination evidence, and source links. Complete when every accepted example is covered, every proposed execution unit is bounded and verifiable, and dependency/continuation relationships are inspectable. If mapping exposes material ambiguity, return to `$define-slice-definition` or the responsible Wayfinder question.

End with a handoff and a prepared review invocation:

```text
Run $define-readiness-review for <slice> and packet <ID/revision>. Read the exact Definition Gate revisions, manifest, candidate packet, coverage, and dependency evidence from a fresh implementer's perspective. Record the human Readiness result.
```
