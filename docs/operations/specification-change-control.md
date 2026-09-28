---
schema_version: 1
id: operations.specification-change-control
title: Specification approval and change protocol
type: operations-procedure
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
  - ../specifications/decision-workflow/validation.md
related_docs:
  - ../specifications/decision-workflow.md
  - ../capabilities/specification-discovery.md
  - ../architecture/documentation-contract.md
  - ../architecture/concern-catalog.md
related_decisions:
  - ../decisions/ADR-0002-intent-and-implementation.md
supersedes: []
---

# Specification approval and change protocol

## Purpose and trigger

Use this protocol when an initiative reaches specification review, a previously accepted decision changes, a session leaves partial writes, or future implementation differs from approved behavior. The first version specifies these rules; automation and product implementation remain outside the current destination.

## Owner, access, and preconditions

The initiative owner resolves approval and scope questions. Decision owners and reviewers are identified by the map and risk assessment. Before mutations, confirm the target repository, permitted GitHub operations, candidate branch, active baseline, and affected documents. A proposal author may prepare local drafts without claiming those drafts are current product truth.

## Approval gate

**GOV-APP-001**: A package may be offered for approval only when all of these conditions have evidence:

1. Destination, scope, actors, parent constraints, and non-goals are explicit.
2. Every required decision has a valid resolution, and no in-scope blocking fog or unresolved applicability remains.
3. Any retained deferral meets GOV-DEF-001 and does not prevent safe implementation of the declared destination.
4. All affected canonical documents, glossary terms, and qualifying ADRs are incorporated into the candidate revision.
5. Normative obligations needed by implementation and tests have stable identities.
6. Applicable interfaces, invariants, permissions, owned data, dependencies, failures, and recovery guarantees are settled.
7. Required alternatives have been compared and their consequences recorded.
8. No unresolved normative contradiction remains, including conflicts with active parent obligations.
9. The coverage, scenario, consistency, and negative-space review passes have no unresolved blocking findings.
10. A reviewer using the documents alone can determine intended behavior, limits, authoritative ownership, and remaining permitted choices.
11. Metadata, references, links, machine formats, and supersession relationships pass structural validation.
12. Required reviewers have recorded their outcome for the exact candidate revision.
13. The accountable owner has been given the complete reviewable package, findings, deferrals, and approval baseline to decide on.

**GOV-APP-002**: Activation requires an explicit owner approval of the candidate's substantive content. Prior acceptance of individual recommendations is not represented as a formal approval of an unseen assembled revision. A later semantic change invalidates affected review and approval; mechanical approval metadata can be recorded afterward without pretending it is a new product decision.

### Review passes

Coverage checks applicability and substantive document sections. Scenario review probes observable behavior, including denial, retries, duplicates, concurrency, partial failure, cancellation, limits, and recovery where relevant. Consistency checks definitions, ownership, dependencies, contracts, assertions, and rationale across sources. Negative-space review exposes implicit assumptions, unsupported cases, limits, deferrals, and exclusions.

Record each pass separately with reviewer identity, reviewed revision or explicit uncommitted snapshot limitation, input basis, document input set, findings, and outcome. Independence means one pass cannot hide another's failures. At least one pass must explicitly record a documents-only input basis and list its inspected package members; it must not rely on private conversational answers. This does not require inventing an additional human reviewer. Automated checks validate structure; they do not establish semantic completeness.

An uncommitted review is provisional. Before it can satisfy the approval gate, compare its recorded content snapshot with the actual candidate commit/tree and bind the outcome to identical reviewed content, or repeat the affected review. If no exact snapshot was preserved, the limitation statement cannot substitute for this comparison; repeat the review on the candidate revision.

## Deferral policy

**GOV-DEF-001**: A deferral records its exact question, why it is non-blocking, affected obligations/documents, risk, owner, revisit trigger, and expiry date. No core scope, actor permission, lifecycle, invariant, data owner, external contract, security obligation, critical failure behavior, or acceptance condition may be deferred within the current destination.

A detail legitimately left to implementation under WF-SCOPE-004 is a permitted choice, not an unanswered product decision requiring a deferral. For example, a private helper's filename can remain free; whether a cancelled payment grants access cannot. An irrelevant disaster-recovery concern can be not-applicable with a reason; an unknown required recovery objective cannot.

An expired deferral must be resolved or explicitly reassessed before the affected work continues or a new approval relies on it. The workflow specifies inspection at relevant sessions and reviews; continuous reminders or monitoring are separate features and must not be implied.

## Activation sequence and evidence

**GOV-ACT-001**: Git and GitHub do not share an atomic transaction. Activation uses a recoverable sequence whose individual results are verified and whose incomplete steps remain visible.

1. Assemble and validate a candidate documentation revision, with exact package member paths and their Git revision. Present it for owner approval and record the actual approver and required reviewer evidence. The approval identifies the reviewed commit or tree before any status-only finalization.
2. Incorporate the approved substantive content and the intended active/accepted statuses in the proposed documentation change. Merge through the repository's normal authorized review process. Verify that the effective content matches the approved content apart from permitted administrative metadata. A concurrent semantic change returns the affected package to review.
3. After the merge succeeds, obtain its exact effective commit. Write the activation record in a subsequent record or an external approval comment: package ID, approving owner, approval time, reviewed revision, effective commit, member paths, map link, reviewer outcomes, and any superseded scope.
4. Link the activation record from the manifest where a persistent pointer is needed, and from the GitHub map. Close the map only when the approval, merged package, and cross-system records are reconciled. Read back each remote result.

The commit named by a record already exists; a file does not attempt to contain its own eventual commit SHA. A candidate review SHA and an effective merge SHA can differ, for example after squash; the record preserves both and the content comparison.

The merged package is the effective documentation baseline once its approved content and statuses are verified. A later record-write failure leaves activation reconciliation pending, not an unapproved product decision and not a completed map. Resume fills only the missing records.

**GOV-HIST-001**: Historical review reads package members at the recorded effective commit. Current paths serve current navigation. An additive feature or phase package references parent constraints and changes its own scope; it does not supersede an entire project merely because one document changed.

## Revising decisions before approval

**GOV-CHANGE-001**: If an answer changes, identify every affected assertion, document, contract, dependent decision, and completed review. Record the replacement rationale, update the proposal, and return invalidated dependents to an unresolved state or connect a satisfying successor. Distinguish previous evidence from current evidence.

For example, changing a sign-up flow from payment-before-access to access-before-payment invalidates relevant lifecycle, permissions, failures, and contract assumptions even if the billing document is the only file named by the user. Review the related obligations before reporting the map complete.

## Changing an active specification

An active baseline remains available while a proposal evolves on a branch. A correction to explanatory wording may be reviewed locally; a change to normative behavior follows the affected discovery and approval gates. Parent requirements cannot be overridden solely by approval of a child feature: obtain the relevant parent's decision-owner resolution and update the affected canonical obligations in the new baseline.

Qualifying changed decisions create successor ADRs. Keep historical rationale and historical package membership retrievable. The new package states exactly what it supersedes; existing unrelated decisions retain their authority.

## Future implementation alignment

**GOV-ALIGN-001**: A future implementation change identifies its active package and affected assertion IDs, examines source references and related contracts, and classifies whether behavior changes. Impact analysis follows references and actual usage/evidence; a path list is a starting point and cannot prove completeness. If the repository provides a code knowledge graph, prefer it for symbol and call relationships, falling back when insufficient.

Every future logical change declares one of:

| documentation_impact | Required evidence |
| --- | --- |
| none | Reason why observable obligations remain unchanged and relevant verification evidence |
| updated | Links to the affected normative documents and approval of any changed intent |
| emergency-deferral | Owner, urgency and reason, affected assertions/documents, risk, expiry, and reconciliation work |

**GOV-ALIGN-002**: A behavior change is incomplete until the same change includes its normative documentation update or a valid explicit emergency deferral. Intent must be approved before code or documentation silently establishes a new obligation. An accidental bug is corrected against existing intent; its observed behavior is not automatically written into the contract.

Review Standards, Specification, and Documentation Alignment separately. Update alignment assessments only to the extent justified by the reviewed revision and evidence. An approved package may remain unimplemented or partial. Repository alignment says nothing about deployment unless a separately identified deployment record provides that evidence.

### Contradiction classification

**GOV-CONFLICT-001**: A material disagreement creates a blocking decision identifying conflicting claims, authority, dates/revisions, intent versus observation, and affected requirements. Resolution chooses the intended obligation, updates affected documents together, and records necessary migration or corrective work without implementing it under a discovery-only request.

| Observation | Response |
| --- | --- |
| Code differs because of an accidental defect | Preserve intended obligation; record correction need and drift |
| Documentation is stale relative to an already approved decision | Repair its canonical expression and affected references |
| New behavior is intentionally desired | Propose and approve changed intent; update documents with the eventual code change |
| Two normative documents disagree | Block activation, resolve ownership and intent, update both views or remove the duplicate assertion |
| Evidence cannot establish which applies | Record unknown alignment and seek the required decision/evidence |

Emergency deferral records drift rather than claiming alignment. Its expiry and owner are checked at the next affected session/review. Designing this policy does not create continuous enforcement or authorize emergency work by itself.

## Interruption and concurrency recovery

**GOV-CLAIM-001**: An active claim records ticket, responsible account, session identity, branch/checkpoint, and its most recent handoff. On a normal stop before resolution, save the checkpoint and release the claim; the session may be explicitly resumed and reclaimed later. A crash leaves an interrupted claim to reconcile before frontier selection.

Resume the same session if it is available. A replacement session can take over when the previous session is verifiably ended or the responsible owner explicitly transfers it; record that evidence, preserve the checkpoint, release the old claim, and establish the new one. Inactivity alone is not proof that another writer has stopped. If ownership or active-writer status cannot be established, identify that blocker and the responsible owner while working independent tickets. Assignment remains the visible claim and the session pointer distinguishes agents sharing an account.

**GOV-REC-001**: Before retrying, inspect GitHub and Git for writes that may already have succeeded. The checkpoint records map, ticket, session, branch, document revision, completed steps, pending steps, evidence links, and outstanding human input.

| Failure point | Recovery |
| --- | --- |
| Issue created, relationship write failed | Reuse the existing issue and repair relationships; do not create another issue by default |
| Document draft written, resolution comment failed | Preserve the draft revision; retry the missing comment and then verify semantic resolution |
| Ticket closed, map update failed | Restore the named map pointer from the existing resolution |
| Documentation merge succeeded, approval record or map close failed | Keep the effective approved baseline; reconcile the missing record and map status |
| Two sessions claim under one human account | Inspect session pointers; keep one active writer and assign independent work elsewhere |
| A session ended with an open claimed ticket | Apply GOV-CLAIM-001 to resume, release, or transfer it; an unverifiable writer remains an explicit blocker |
| Two branches alter one shared obligation | Compare meanings, resolve the conflict, and repeat affected review after rebase |
| A prerequisite closed as abandoned or superseded | Keep dependents blocked until a valid satisfying decision or successor exists |
| GitHub access is unavailable | Preserve local drafts and report unrecorded operations; do not claim a remote map update or substitute a new canonical tracker |

## Validation, rollback, and evidence retention

After each recovery, re-evaluate frontier eligibility, links, affected documents, and any approvals tied to changed content. Preserve user work when recovering branches. Reverting an unapproved local proposal differs from reversing an active decision; reversing active intent requires a visible decision and history.

Retain the original and replacement decision references, reviewed/effective revisions, reviewer findings, disposition, and map pointer. These are the minimum evidence needed to explain what was approved and to resume incomplete record updates.

## Change history

- 2026-09-29: Initial approval, deferral, change, and recovery protocol; refines Q31's atomicity goal into a recoverable cross-system sequence.
