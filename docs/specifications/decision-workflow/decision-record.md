---
schema_version: 1
id: evidence.workflow-interview
title: Workflow design decision record
type: design-evidence
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
  - ../decision-workflow.md
related_decisions:
  - ../../decisions/ADR-0001-decision-history-and-current-contracts.md
  - ../../decisions/ADR-0002-intent-and-implementation.md
supersedes: []
---

# Workflow design decision record

This is a historical index of this conversation, not a second normative specification. The user accepted each round's recommendations except for the recorded Q13 and Q16 amendments. Source: the design conversation spanning September 28–29, 2026. Stable external comment URLs are not available for these approvals.

## Accepted decisions

| Question | Accepted direction |
| --- | --- |
| Q1 | A reusable guided workflow with templates and validation rules; no application or automation engine initially. |
| Q2 | Design for new and existing systems, with the first path limited to greenfield idea-to-specification work. |
| Q3 | One initiative model across project, phase, and feature hierarchy, with parent context and explicit scope. |
| Q4 | Completion requires human satisfaction, documented applicable design concerns, and explicit treatment of remaining questions. |
| Q5 | Adaptive rounds at the decision frontier, autonomous fact discovery, explicit decisions, and final human confirmation. |
| Q6 | Documents express intended behavior; code supplies observed behavior; divergence requires classification and resolution. |
| Q7 | Standard structure for authoritative documents; create applicable documents lazily. |
| Q8 | Record resolved terminology and decisions promptly; ADRs only for consequential, non-obvious trade-offs. |
| Q9 | Preserve the valued methods in an independent workflow without an external runtime repository dependency. |
| Q10 | End with a specification package and handoff; implementation, build tickets, CI enforcement, and reverse engineering are deferred. |
| Q11 | Stable top-level documentation taxonomy with domain-specific leaf documents and an added specifications category. |
| Q12 | A small specification manifest references the affected canonical documents rather than duplicating them. |
| Q13 | User amendment: GitHub holds maps and decision tickets, replacing the suggested local Markdown default. |
| Q14 | An adaptive decision graph operates within explicit coverage gates. |
| Q15 | Agents establish facts and recommendations; accountable humans settle consequential decisions and approve final intent. |
| Q16 | User amendment: maintain one glossary. CONTEXT.md was selected to match the installed domain-modeling convention; no docs/GLOSSARY.md copy. |
| Q17 | Explicit authority, implementation references, evidence, related documents, and related decisions replace ambiguous source_of_truth metadata. |
| Q18 | Compare materially different alternatives for consequential interface, seam, ownership, integration, and lock-in decisions. |
| Q19 | Behavior-changing implementation work includes its normative documentation update, with only explicit emergency deferrals. |
| Q20 | Semantic change history records behavior, contract, invariant, ownership, and scope changes; Git owns detailed edit history. |
| Q21 | One GitHub map, child decision issues, native dependencies, named links, assignment claims, and a final package link. |
| Q22 | One coherent, session-sized question per ticket; resolution records rationale, alternatives, consequences, evidence, and document impact. |
| Q23 | Research, prototype, grilling, and prerequisite task types preserve their human versus agent authority boundaries. |
| Q24 | Immediate write-through to draft canonical documents precedes decision resolution; finalization validates existing knowledge. |
| Q25 | Each assertion has one canonical home; other documents refer to it. |
| Q26 | Scenarios, outcomes, lifecycles, invariants, failures, and measurable acceptance drive specifications; user stories are optional. |
| Q27 | Stable identifiers cover normative obligations, not every paragraph. |
| Q28 | Only non-blocking questions can be deferred; ownership, risk, trigger, and expiry are explicit; core behavior cannot be deferred. |
| Q29 | Material contradictions create blocking decisions and are resolved across all affected sources. |
| Q30 | Coverage, scenario, consistency, and negative-space reviews; at least one review starts with documents alone. |
| Q31 | A fully specified approval gate and explicit owner approval precede activation and map closure. |
| Q32 | Type-specific lifecycles for specifications, canonical documents, ADRs, tickets, and maps. |
| Q33 | Active intent and implementation alignment are distinct; approved future behavior can remain unimplemented. |
| Q34 | Common machine-readable metadata, revision-scoped alignment, actual review dates, and durable ownership roles. |
| Q35 | Common metadata and type-specific bodies; required sections contain substantive answers or justified not-applicable results. |
| Q36 | Standard, elevated, and critical risk determine applicable evidence and review; lowering risk requires rationale. |
| Q37 | Future changes trace affected assertions and documents, classify behavior impact, update documentation, and review alignment. |
| Q38 | One orchestrating workflow draws on Wayfinder and specialist methods; skill dependency details still need reconciliation with Q9. |
| Q39 | A typed concern catalog generates applicable questions, prerequisites, evidence needs, risk escalation, and routing. |
| Q40 | Stakeholder knowledge gaps produce targeted questionnaires and blocked decisions; facts and decision authority remain distinct. |
| Q41 | Future reviews report Standards, Specification, and Documentation Alignment separately. |
| Q42 | Activation history identifies the approver, reviewed revision, package, map, reviewers, and supersession relationship. |
| Q43 | Explicit follow-up answer: standalone required process with optional compatible installed skill integrations. This reconciles Q9 and Q38. |
| Q44 | Explicit follow-up answer: settle behavior, contracts, ownership, consequential architecture, and test seams; leave implementation internals free unless an obligation depends on them. |

## Draft refinements for review

The following specify how to honor the accepted goals in difficult cases. They are visible refinements in the assembled draft, not claims that the user separately chose them during Q1–Q42.

- Git and GitHub changes use a recoverable sequence with reconciliation. They cannot be described as one atomic cross-system transaction.
- An approval record refers to an existing reviewed commit from a later record or external approval; a commit cannot contain its own eventual SHA.
- Assignment remains the visible claim, with an additional session pointer to distinguish simultaneous agents acting under the same human account.
- Closed GitHub status is insufficient to satisfy a prerequisite if the issue was abandoned, ruled out of scope, or superseded without a valid replacement.
- Proposed changes preserve the active baseline; assertions invalidated by a later decision reopen dependent review and cannot retain stale approvals.
- File-format-native contracts, such as OpenAPI and event schemas, carry compatible metadata or a sidecar instead of invalid Markdown YAML frontmatter.
- A stale date or the existence of a source path never establishes behavioral alignment.
- The original sequential stages act as coverage gates; known cross-cutting constraints may reopen earlier decisions.
- Explicit not-applicable or no-document-impact explanations keep the workflow usable for small initiatives without inventing documents.

## Remaining review

Q43 and Q44 are resolved. The [manifest](../decision-workflow.md) and its linked package await review of the assembled draft; no further material interview decision is currently identified.

## Source material consulted

The locally installed skills were read during the conversation: grill-with-docs, grilling, domain-modeling and its glossary/ADR formats, wayfinder and tracker guidance, codebase-design and its Design It Twice/deepening references, to-spec, to-questionnaire, implement, code-review, and writing-for-agents. These are local observations, not a claim to track the latest upstream release.

The draft intentionally adapts these differences: GitHub is required for map storage; ADRs use the user's docs/decisions location; the existing to-spec issue template becomes a package manifest; final synthesis cannot label a package ready before approval; documentation alignment is an additional future review axis. Existing installed skills have not been edited.
