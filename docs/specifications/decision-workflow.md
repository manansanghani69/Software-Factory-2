---
schema_version: 1
id: spec.decision-workflow
title: Idea-to-specification workflow
type: specification-manifest
status: draft
authority: normative
owner: project-owner
reviewers: []
last_reviewed: null
implementation_alignment:
  state: unimplemented
  checked_at: null
  checked_ref: null
implementation_refs: []
evidence_refs:
  - decision-workflow/validation.md
related_docs:
  - ../../CONTEXT.md
  - ../capabilities/specification-discovery.md
  - ../architecture/documentation-contract.md
  - ../architecture/concern-catalog.md
  - ../operations/specification-change-control.md
  - decision-workflow/decision-record.md
related_decisions:
  - ../decisions/ADR-0001-decision-history-and-current-contracts.md
  - ../decisions/ADR-0002-intent-and-implementation.md
supersedes: []
initiative_type: project
parent_specification: null
risk: elevated
map_url: null
approval_record: null
---

# Idea-to-specification workflow

## Destination

Define a reusable, Wayfinder-style workflow that takes a loosely expressed software idea through evidence gathering and human decisions to an approved, internally consistent Specification Package. The package should be sufficient to derive implementation tickets in a later effort and should establish how subsequent behavior changes keep documentation accurate.

This initiative produces a workflow specification. Creating an executable skill, running this workflow on a real product, and implementing that product are separate undertakings.

## Problem and outcomes

The project owner wants to make consequential decisions explicit before implementation, avoid hidden assumptions and contradictory documents, and retain useful context across sessions. A folder of populated templates alone does not establish that these outcomes have been met.

- **WF-OUT-001**: A new session can recover the destination, settled decisions, frontier, and authoritative documents without the original conversation.
- **WF-OUT-002**: Each applicable concern ends in a supported decision, a justified not-applicable result, or an admissible non-blocking deferral.
- **WF-OUT-003**: An implementer can identify intended outcomes, invariants, permissions, contracts, failures, owned data, and acceptance conditions from the package.
- **WF-OUT-004**: Every accepted decision has a reasoning trail and an identifiable documentation effect or a justified no-effect result.
- **WF-OUT-005**: Future behavior changes have a specified process for updating intent and assessing alignment without silently legitimizing defects.

## Scope

The first supported discovery path is a greenfield project. The conceptual initiative model includes project, phase, and feature levels; later paths can reuse it for changes to existing systems. A parent context constrains a child initiative; a child cannot silently override the parent's active obligations.

The deliverable defines GitHub maps and decision tickets, staged discovery, the concern catalog, human authority, document ownership and templates, metadata, traceability, scenario reviews, approval, historical reproducibility, and the future alignment policy.

The design is classified elevated because it governs shared normative contracts and approval history across Git and GitHub. No critical product-domain obligation has been identified in this workflow-design scope; a future target initiative receives its own risk assessment.

**WF-SCOPE-001**: Decision tickets are in scope; implementation tickets are outside this destination. The two must remain distinguishable in naming, purpose, and handoff.

**WF-SCOPE-002**: Capability names from the initial example, including billing and teams/players, are illustrative. The workflow derives the capabilities and product surfaces appropriate to the actual project.

## Non-goals

- Product code generation, production operations, database migrations, or CI enforcement.
- Executable workflow tools, automatic drift detection, or claims that metadata proves correctness.
- Full existing-codebase reverse engineering in the first path.
- Implementing project-management synchronization beyond defining the GitHub protocol.
- Creating an application, a workflow engine, or a new global skill installation in this effort.
- Deriving implementation tickets; this belongs to a later research and design effort.

## Package membership

This manifest owns the initiative scope and outcome IDs. The following documents own the detailed obligations; other sections link to them instead of copying their rules.

| Document | Owns |
| --- | --- |
| [Canonical glossary](../../CONTEXT.md) | Domain meanings |
| [Specification discovery](../capabilities/specification-discovery.md) | Session behavior, maps, ticket lifecycle, authority, stage gates, resumption |
| [Documentation contract](../architecture/documentation-contract.md) | Document routing, metadata, templates, assertion identity, state meanings |
| [Concern catalog](../architecture/concern-catalog.md) | Applicability, evidence, prerequisites, risk, and completion criteria for discovery concerns |
| [Change and approval protocol](../operations/specification-change-control.md) | Review gate, activation, rework, future alignment, interruption recovery |
| [ADR-0001](../decisions/ADR-0001-decision-history-and-current-contracts.md) and [ADR-0002](../decisions/ADR-0002-intent-and-implementation.md) | Rationale for the two durable knowledge-model choices |

The [decision record](decision-workflow/decision-record.md) is historical evidence, and [validation scenarios](decision-workflow/validation.md) describe how to assess the design. Neither introduces a second source of product obligations.

## Acceptance outcomes

- **WF-ACC-001**: A vague greenfield idea produces an agreed destination, scoped initial tickets, visible dependencies, and explicitly recorded fog without creating speculative build tickets.
- **WF-ACC-002**: A ticket with unanswered prerequisites stays blocked; independent research can proceed; a human-owned decision cannot be closed solely by an agent's recommendation.
- **WF-ACC-003**: Resolving a material decision updates affected draft canonical documents and records the evidence before semantic resolution is considered complete.
- **WF-ACC-004**: Retrying a session after partial GitHub or Git operations reconciles existing records without duplicate decisions or falsely declaring completion.
- **WF-ACC-005**: A material contradiction, missing critical requirement, or stale approval prevents package activation.
- **WF-ACC-006**: A reviewer with only the package can distinguish approved intent from implemented and deployed behavior, locate each obligation's owner, and discover explicit non-goals and deferrals.
- **WF-ACC-007**: A future behavior change preserves historical approvals and superseded rationale while proposing a consistent new current contract.
- **WF-ACC-008**: A later workflow can derive build tickets from the manifest, stable assertions, scenarios, and test seams without repeating foundational discovery.

Validation is proportionate to this design-only effort. Passing a document walkthrough is evidence about the design, not proof that GitHub integration or an executable workflow works.

## Portability and specification depth

**WF-SCOPE-003**: The required process is standalone. Compatible installed specialist skills are optional integrations; their absence cannot remove a required reasoning step. This resolves Q43 and the earlier Q9/Q38 tension.

**WF-SCOPE-004**: The specification settles behavior, contracts, data ownership, consequential architecture, and test seams. Internal algorithms, file layout, and other reversible implementation choices remain open unless they affect a requirement. This is the accepted Q44 boundary.

The destination is complete when relevant obligations are determined and validated for the declared scope. It cannot guarantee that implementation will reveal no new facts; the change protocol governs those discoveries.

## Status and handoff

The interview decisions Q1–Q44 were accepted, including the GitHub-only map, single-glossary, portability, and specification-depth choices. This assembled specification is still a draft. No approved commit, formal reviewer outcome, or GitHub map has been fabricated; the metadata records those absences explicitly.

After review findings are settled, the next handoff is this package for final specification approval. Building the workflow and deriving implementation tickets remain outside this effort.
