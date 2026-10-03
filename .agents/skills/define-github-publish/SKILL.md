---
name: define-github-publish
description: Publish an explicitly approved Project Definition issue packet to GitHub, reconcile stable IDs, verify relationships, and assemble the implementation handoff.
---

# Define GitHub publish

Use only on an explicit invocation naming the target repository and exact publication scope. Executable work requires an already passing Readiness packet. A named planning-only packet may publish containers earlier; those issues remain containers in definition and authorize no execution. Decision Map/ticket publication belongs to explicitly scoped `$define-wayfinder-chart` sessions. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), [the integration adapters](../project-definition-system/references/integration-adapters.md), and the [publication ledger](../project-definition-system/templates/publication-ledger.md). Do not infer a target repository, approval, or publication authority from a draft.

This is a manual publication invocation. It never runs automatically and never broadens the approved packet.

## Work

1. Read the exact packet revision, repository target, existing ledger, document-access evidence, and explicit human publication authority. For execution, verify the current passing Readiness record matches the entire packet. For planning-only publication, verify every issue is a container and the named planning scope is authorized; stop if executable work is included without Readiness. Reuse planning bindings when later publishing the approved execution set.
2. Check tracker access/capabilities and fetch existing issues by stable ID before creating anything. If a source is only local, use the authorized project workflow to make it accessible; never invent a URL.
3. Create missing approved issues once, parents before children where practical, and store each URL against its stable ID immediately. Keep containers distinct from executable issues.
4. Wire native parentage and actual blockers in a second pass. For conceptual overflow, verify the complete stable-ID path, logical parent, and both continuation links as required by the operating contract. Keep readiness, lifecycle, claim, and blocked state separate.
5. Read back titles, roles, source links, parents, blockers, labels/fields, continuation links, and the complete approved set. Reconcile partial success by lookup and ledger, never by creating duplicates or deleting history.
6. Assemble the execution handoff with baseline references, executable frontier, container/integration acceptance, residual risk, discretion, issue URLs, and publication status. For planning-only publication, record bindings and the next definition frontier with no execution authorization.

## Output and completion

Persist the verified ledger, bindings, and handoff. Complete when every approved issue exists once with the correct role, source references, relationships, status evidence, and usable links. Newly surfaced definition changes return through recovery and gates; they are not silently inserted into approved issues.

End an execution publication with a handoff naming the implementation consumer and the next `$define-next` invocation for the following slice. End a planning-only publication with `$define-next` for the current definition frontier. This skill does not start implementation, schedule orchestration, or change approved semantics.
