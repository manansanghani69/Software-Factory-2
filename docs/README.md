---
schema_version: 1
id: index.documentation
title: Documentation
type: documentation-index
status: draft
authority: informative
owner: project-owner
reviewers: []
last_reviewed: null
implementation_alignment:
  state: not-applicable
  checked_at: null
  checked_ref: null
implementation_refs: []
evidence_refs: []
related_docs:
  - specifications/decision-workflow.md
  - ../CONTEXT.md
related_decisions: []
supersedes: []
---

# Documentation

Start with the [workflow specification](specifications/decision-workflow.md). This repository currently holds the design of a reusable workflow from an idea to an approved Specification Package. The executable skill, GitHub integration, and automated validators have not been implemented.

The draft consolidates accepted interview decisions Q1–Q44. The [decision record](specifications/decision-workflow/decision-record.md) preserves their history and distinguishes subsequent proposals. Approval of those recommendations does not imply that an implementation exists or that this assembled revision has been approved.

| Read when | Document |
| --- | --- |
| Orienting to scope, deliverables, and acceptance | [Specification manifest](specifications/decision-workflow.md) |
| Resolving domain language | [Canonical glossary](../CONTEXT.md) |
| Charting, resolving a ticket, or resuming discovery | [Discovery lifecycle](capabilities/specification-discovery.md) |
| Deciding where knowledge belongs or how to structure a document | [Documentation contract](architecture/documentation-contract.md) |
| Choosing applicable questions and evidence | [Concern catalog](architecture/concern-catalog.md) |
| Approving, revising, or reconciling a specification | [Change and approval protocol](operations/specification-change-control.md) |
| Checking the rationale for durable choices | [Decision history versus current contracts](decisions/ADR-0001-decision-history-and-current-contracts.md), [Intent versus implementation](decisions/ADR-0002-intent-and-implementation.md) |
| Checking design evidence and remaining gaps | [Validation scenarios](specifications/decision-workflow/validation.md) |

All normative documents remain drafts unless their own status says otherwise. `project-owner` is an accountable role, presently represented by the requesting user; it is not an invented team or a recorded approval identity. `last_reviewed: null` means no formal document review has been recorded. Approval and implementation alignment are separate concepts.
