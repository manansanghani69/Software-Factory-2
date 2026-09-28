---
schema_version: 1
id: domain.specification-workflow
title: Specification workflow language
type: domain-glossary
status: draft
authority: normative
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
  - docs/specifications/decision-workflow.md
related_decisions: []
supersedes: []
---

# Specification workflow language

The domain of discovering, approving, and maintaining the intended behavior of a software project. This is the sole glossary for this domain.

## Work and discovery

**Initiative**: A scoped undertaking at project, phase, or feature level, with a destination and any parent context.
_Avoid_: Using feature to mean every size of undertaking.

**Destination**: The explicit outcome that determines when an initiative's discovery is finished and which work belongs outside it.

**Wayfinder map**: The shared index of an initiative's destination, resolved decisions, remaining fog, and excluded work.
_Avoid_: Specification, backlog.

**Decision ticket**: A bounded question whose resolution supplies a decision or evidence needed to reach the destination.
_Avoid_: Implementation ticket, build task.

**Frontier**: The set of open, unclaimed decision tickets whose decision prerequisites have been satisfied.

**Fog**: In-scope uncertainty that cannot yet be phrased as a precise decision question.
_Avoid_: Backlog, out of scope.

**Concern**: A category of design questions with an applicability rule, prerequisites, evidence needs, and completion criteria.

**Capability**: A coherent business ability described through its outcomes, rules, workflows, and owned data.
_Avoid_: Module when referring to the business ability; one capability need not correspond to one code module.

**Product surface**: A user-facing place through which actors access capabilities.

## Knowledge and approval

**Canonical document**: The designated current home of a particular body of knowledge, with ownership and references to related knowledge.

**Normative assertion**: An approved or proposed obligation about intended behavior against which an implementation or test can be assessed.

**Specification Package**: An initiative's manifest and the exact revisions of the affected canonical documents that together define its intended outcome.
_Avoid_: One giant specification, implementation plan.

**Specification manifest**: The entry point that states an initiative's scope, acceptance outcomes, document membership, and approval status.

**Decision owner**: The human accountable for accepting a decision and its consequences.

**Approval baseline**: The identified documentation revision accepted by the accountable owner and required reviewers.

**Implementation alignment**: A revision-scoped assessment of how observed implementation behavior compares with approved intended behavior.
_Avoid_: Deployed status, approval status.

**Drift**: A difference between intended behavior and observed implementation behavior requiring classification and resolution.

**Deferral**: An explicitly owned unanswered question with a bounded risk, revisit trigger, and expiry.

**Emergency deferral**: A recorded, time-limited exception to completing documentation alignment in the same change as urgent implementation work.

**Reconciliation**: Completion of outstanding cross-system records after the underlying approved documentation change has succeeded.
