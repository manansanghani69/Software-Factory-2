---
schema_version: 1
id: evidence.workflow-validation
title: Workflow design validation
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
  - ../../capabilities/specification-discovery.md
  - ../../architecture/documentation-contract.md
  - ../../architecture/concern-catalog.md
  - ../../operations/specification-change-control.md
related_decisions: []
supersedes: []
---

# Workflow design validation

This record evaluates the written design. No executable workflow, automated validator suite, target product, or live GitHub map has been created or tested. Results from a document review do not imply runtime conformance.

## Scenarios

| Scenario | Expected observable behavior | Owning rule |
| --- | --- | --- |
| Vague greenfield idea | Confirm destination, chart sharp questions, preserve fog, avoid premature build tickets | WF-ACC-001; DISC-INV-007 |
| Domain name has two meanings | Resolve the meaning with the human and update the sole glossary; examine dependent assertions | DOC-INV-002; DISC-INV-003 |
| Stakeholder alone knows a required fact | Block the affected decision, produce a targeted questionnaire, continue independent work | DISC-ERR-001 |
| Research finds a provider limitation | Record dated evidence; reopen affected choices instead of silently changing intent | GOV-CHANGE-001 |
| Actor permission is unanswered | Keep package unapproved; a core decision cannot become an ordinary deferral | GOV-DEF-001 |
| Private helper filename is unknown | Leave it as implementation freedom if it cannot affect an obligation | WF-SCOPE-004 |
| A concern cannot yet be classified | Preserve unresolved applicability; an empty ticket list is not sufficient | CONC-FLOW-001; GOV-APP-001 |
| Small reversible feature | Reuse relevant existing knowledge, justify non-applicable concerns, avoid empty document scaffolding | DOC-COVER-001 |
| No eligible ticket remains | Proceed to Review only if coverage is complete; otherwise report the exact prerequisite, claim, or fog blocker and next action | Discovery charting and Continue routing |
| Payment succeeds but provisioning fails | Decide partial-failure outcome, access, retry scope, repair, and observability before approval | Concern catalog: failure/recovery and ordering |
| A decision changes after related reviews pass | Find affected dependents, update draft documents, repeat invalidated reviews | GOV-CHANGE-001 |
| A child feature contradicts parent authorization | Obtain the parent decision owner's resolution and update affected obligations | GOV-CHANGE-001; approval gate |
| Ticket closes without a real answer | Closed status does not satisfy dependents; resolve missing semantics | DISC-INV-004 |
| Two sessions share the GitHub account | Inspect session-specific claim pointers and preserve one active writer per ticket | GOV-REC-001 |
| A session terminates while its ticket is claimed | Resume it or verify termination/owner transfer before releasing and reclaiming; ambiguous ownership stays visibly blocked | GOV-CLAIM-001 |
| Draft saved but comment write fails | Preserve the draft; retry only the missing operations after checking actual state | GOV-REC-001 |
| Merge succeeds but map close fails | Preserve approved effective baseline; record pending reconciliation and finish missing writes | GOV-ACT-001 |
| New evidence changes the candidate after approval | Invalidate affected approval; record a new reviewed revision | GOV-APP-002 |
| Uncommitted review is offered as approval evidence | Bind a preserved identical snapshot to the actual candidate, or repeat review if identity cannot be proved | Approval protocol: review passes |
| A reader opens a proposed edit to an active document | See draft status and baseline_ref pointing to the still-effective approved content | DOC-LIFE-001 |
| Alignment says aligned but only a file path exists | Reject insufficient assessment evidence; record unknown until adequately assessed | DOC-INV-003 |
| Code implements an accidental defect | Preserve intended contract and record drift/correction need | GOV-CONFLICT-001 |
| Emergency documentation update is deferred | Record visible drift with owner, scope, risk, and expiry; do not report alignment | GOV-ALIGN-002 |
| Read a year-old approval after files move | Read package members at the historical effective commit | GOV-HIST-001 |
| Write OpenAPI with standard doc metadata | Use schema-compatible metadata or a sidecar; contract remains format-valid | DOC-INT-001 |
| Specialist skills are absent or incompatible | Follow the local required method and disclose adaptations | WF-SCOPE-003 |

## Review status

The following results refer to the uncommitted local draft on 2026-09-29; they are not revision-pinned formal approval evidence.

| Pass | Result and evidence |
| --- | --- |
| Structural validation | Passed a one-off read-only check across 11 documents: required frontmatter fields and simple field shapes, allowed states, unique document IDs, 50 unique normative assertion definitions, 37 local Markdown links/anchors, 49 metadata references, Q1–Q44 coverage, and trailing whitespace. Repeated after the review corrections with no errors. This check is not a general YAML parser or the future validator implementation. |
| Coverage review | Author checked the accepted decisions against the manifest and member documents. Q43 resolves dependency portability; Q44 supplies the finite specification-depth boundary. No applicable concern can disappear without evidence or a recorded reason. |
| Scenario review | Author walked the cases above against the written rules. These establish a specified outcome, not runtime behavior; executable trials remain future work. |
| Consistency review | Separate reviewer Parfit, agent 01a0e95d-1b03-7980-a47b-072fab339493, reviewed from documents with no conversation history supplied. Five concrete gaps were reported. Targeted recheck confirmed four fully resolved and identified one remaining mismatch in the Continue interface summary; the author corrected that summary and checked it against the routing procedure. No other blocking inconsistency was reported within the targeted input set. |
| Negative-space review | Author checked omitted implementation tickets, absent runtime/integration, unpublished GitHub artifacts, uncommitted baseline, permitted implementation freedom, and remaining approval requirements. These limits are explicit. |

Formal owner approval and revision-pinned review remain pending until an actual candidate baseline exists.

## Fresh-reader findings and disposition

| Finding | Draft correction |
| --- | --- |
| Charting required a next ticket even when none existed | Added explicit routing to a ticket, a precise blocker/next action, or Review |
| Interrupted claims could strand work permanently | Added GOV-CLAIM-001 for checkpoint, release, verified resumption, and explicit transfer |
| Uncommitted review could be mistaken for revision-bound approval evidence | Made it provisional and required an identical preserved-snapshot comparison or repeated review |
| Documents-only review could not be identified from its evidence record | Required an input basis and inspected document set for at least one pass |
| A changed branch copy could still claim active status | Required draft status with baseline_ref to the still-effective approved content |

The initial reviewer could identify destination, canonical sources, exclusions, and this package's next review step. These findings improved resumability and approval evidence; they did not change the accepted destination.

For the targeted recheck, the reviewer directly inspected docs/capabilities/specification-discovery.md, docs/operations/specification-change-control.md, docs/architecture/documentation-contract.md, and this validation record. Matching excerpts were inspected from the manifest, CONTEXT.md, the concern catalog, and the decision record. The README produced no matching lines in that search, and the ADRs were not reread; the targeted recheck is not described as a fresh read of the entire package.

The final one-line correction makes the Continue interface explicitly allow transition to Review, matching its detailed procedure. This correction received author verification and structural revalidation, not a further independent review or owner approval.

## Coverage boundaries

This design covers discovery through an approval-ready package and specifies the later alignment policy. It does not demonstrate that skill instructions will be followed reliably in repeated runs, that tracker claims provide a hard lock, or that a test suite can detect all drift. A later workflow implementation needs representative end-to-end trials at Start, Continue, and Review, including the failure cases above.
