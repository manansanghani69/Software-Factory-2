---
schema_version: 1
id: architecture.documentation-contract
title: Documentation contract
type: architecture-view
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
  - ../../CONTEXT.md
  - ../specifications/decision-workflow.md
  - ../operations/specification-change-control.md
related_decisions:
  - ../decisions/ADR-0001-decision-history-and-current-contracts.md
  - ../decisions/ADR-0002-intent-and-implementation.md
supersedes: []
---

# Documentation contract

## Ownership and routing

**DOC-INV-001**: Each current normative assertion has one canonical home. A summary identifies itself as a summary and links to that home. Historical resolutions and approval baselines preserve what was true of the decision at the time; they do not compete with the current contract.

| Home | Owns | Refers elsewhere for |
| --- | --- | --- |
| CONTEXT.md | Canonical domain meanings and rejected synonyms | Requirements, implementation, architectural rationale |
| docs/README.md | Entry points and conditional navigation | Detailed rules |
| docs/DOCUMENTATION_STRUCTURE.md | Target repository's document taxonomy and routing | Individual capability behavior |
| docs/AGENT_GUIDE.md | How an agent finds authority, reviews, and required workflow steps | Duplicated glossary or product rules |
| docs/CONTRIBUTING.md | Change, review, and contribution procedure | Capability-specific behavior |
| docs/capabilities/ | Outcomes, permission rules, invariants, behavior, lifecycle, data ownership | Shared contracts, systemic views, executable recovery procedures |
| docs/product-surfaces/ | Navigation, presentation, actor journeys, accessibility | Business rules owned by capabilities |
| docs/platform/ | Shared platform guarantees, callers' obligations, shared failures | Unrelated business policy |
| docs/architecture/ | System relationships, module interfaces and seams, structural constraints | Restated capability rules or copied interface schemas |
| docs/interfaces/ | Machine-facing contracts and versioned schemas | Business rationale and detailed runbooks |
| docs/operations/ | Operational procedures, recovery, migration, and incident actions | Invented measurements or unverified production state |
| docs/decisions/ | Rationale, alternatives, and consequences of qualifying decisions | Complete copies of current requirements |
| docs/specifications/ | Initiative scope, acceptance outcomes, package membership, approval pointers | Repeated bodies of member documents |

Create leaf documents when they contain relevant knowledge. The target taxonomy is a routing standard, not a request to create empty folders or pretend an irrelevant concern applies. This workflow-design repository currently contains only applicable members; the future target repository can add the remaining index and guide documents when useful.

Examples of resolving overlap: a capability owns its permission rule; a global role-permission matrix references its assertion ID. An interface schema owns field types and wire error shapes; the capability owns why that failure occurs. An operations document owns a restore procedure; the capability links the recovery guarantees. A database view owns storage structure while the capability owns business data ownership and invariants.

**DOC-INV-002**: CONTEXT.md is the single domain glossary. Use one for the initial workflow. If a later system demonstrably needs several bounded contexts, each term gets one context-qualified home and a context map; never maintain mirrored glossaries for the same context.

## Common metadata

**DOC-INT-001**: Every documentation artifact has machine-readable identity, purpose, authority, ownership, lifecycle, and relationships. Markdown uses YAML frontmatter. A source-code reference is evidence location, not a declaration that implementation overrides approved intent.

| Field | Shape and meaning |
| --- | --- |
| schema_version | Positive integer; version of the metadata contract |
| id | Stable globally unique document identifier, retained through rename |
| title | Human-readable name |
| type | Registered document type with an applicable body template and state model |
| status | Value allowed by that document type |
| authority | normative, informative, or generated |
| owner | Accountable human/team/role; role must resolve to an actual owner before approval |
| reviewers | Required reviewer roles or identities; empty where no additional reviewer is required |
| last_reviewed | ISO date of a real completed document review, or null before review |
| implementation_alignment | state, checked_at, checked_ref; see below |
| implementation_refs | Source locations relevant to the document; empty before implementation |
| evidence_refs | Locations supporting claims; existence alone does not establish correctness |
| related_docs | Relative paths or stable URLs to other documentation |
| related_decisions | References to relevant ADRs |
| supersedes | IDs of genuinely replaced artifacts; empty for a new or additive document |

Use empty arrays rather than fabricated paths or teams. Dates, statuses, and owners must express actual evidence. A narrative section can carry more specific links without putting every link into frontmatter.

For a machine contract, use valid format-native metadata where supported, or a neighbouring metadata sidecar identifying the contract and its digest/revision. Do not prepend Markdown frontmatter to JSON, OpenAPI, or event schemas that would no longer validate. Generated material identifies its generator and authoritative inputs; edits belong in those inputs.

### Implementation alignment

**DOC-INV-003**: Approval status describes intended behavior; alignment describes observed implementation at a specific revision. Neither proves deployment status or production verification.

| Alignment state | Meaning |
| --- | --- |
| unimplemented | The described behavior has no implementation yet |
| partial | Only an explicitly identified subset is implemented |
| aligned | Examined behavior matches the contract for the stated checked revision and coverage |
| drifted | A known difference remains between intent and observed implementation |
| unknown | No adequate current assessment is available |
| not-applicable | The artifact has no meaningful implementation comparison, for example a navigation index |

An aligned assessment requires a checked revision, assessment date, evidence, and explicit coverage. Partial or drifted assessments identify the subset or mismatch. Unknown, unimplemented, and not-applicable may have null check fields. A check is not refreshed by editing its date. When a semantic document change or relevant code change invalidates evidence, reassess or record unknown; preserve the old evidence in history.

A broad integration-test directory in evidence_refs only identifies where to investigate. A test report, reviewed diff, or inspected behavior at a named revision supports an actual assessment. The first workflow version defines this assessment protocol and does not automate it.

### Type-specific metadata

| Type | Additional fields |
| --- | --- |
| Specification manifest | initiative_type, parent_specification, risk, map_url, approval_record; member list in the body |
| ADR | decision_date, decision_owner where known; related assertion/document IDs |
| Generated document | generator and input references with revision or digest |
| Machine contract sidecar | described contract path, format, schema revision/digest |
| Proposed revision of an active document | baseline_ref identifying the still-effective approved commit and document path/ID |

Fields referring to external records remain null until those records exist. Every activation must bind actual approver identities to the accountable roles.

## Artifact states

**DOC-LIFE-001**: Lifecycle states use the following meanings and transitions. A draft may contain user-accepted decisions while its assembled revision remains unapproved.

| Artifact | States and transitions |
| --- | --- |
| Specification manifest | draft → in-review → active → superseded; draft or in-review → abandoned |
| Canonical document | draft → active → deprecated or superseded |
| ADR | proposed → accepted → deprecated or superseded |
| GitHub decision ticket | Native open/closed; assignment marks a claim; resolution records the semantic disposition |
| GitHub map | Open until its destination is reached or explicitly abandoned |

Review feedback returns an in-review manifest to draft. Existing active documents keep their effective baseline while proposed revisions are reviewed on a separate branch. In that branch, a semantically revised copy is marked draft and carries baseline_ref pointing to its still-effective approved revision; it must not retain active as a claim about unapproved changed content. The approved copy remains active at its effective revision. Read approval status together with branch/revision provenance.

The revised copy retains its stable document ID; this is a revision, not a second canonical home. Activation changes the approved candidate's status to active and records its new effective baseline. An additive initiative does not supersede its parent's entire package. A new baseline replaces only the scope it explicitly supersedes.

Accepted ADRs retain their historical choice and rationale. A changed choice creates a successor ADR and a supersession pointer, not a rewrite implying the old decision never occurred. Git history is sufficient for replaced file contents; move files into an archive directory only when that improves navigation and references remain valid.

## Assertion identity

**DOC-INT-002**: Give stable IDs to requirements that implementation, tests, or reviews must trace. Use a capability or concern prefix and a category, for example BILL-INV-001 or DISC-ERR-001. IDs are globally unique, are retained on rename, and are never recycled for a different obligation.

One ID may identify a coherent rule or procedure with several inseparable steps. Independent obligations with different owners or acceptance tests receive distinct IDs. Explanatory text, every user-story sentence, and headings do not each need an ID. References do not redefine the obligation.

When an obligation changes, retain its ID if it is the same conceptual obligation and its historical revisions remain identifiable. Splitting, merging, or replacing obligations records successor/predecessor relationships. Tests must not silently keep passing against an obsolete meaning.

## Body templates

**DOC-COVER-001**: The applicable template is a coverage contract. Required sections contain substantive content or an explicit not-applicable explanation. Relevant unresolved content is a draft question linked to a ticket, not filler prose. Owners can keep short documents concise by linking shared canonical material.

### Business capability

Use the user's original structure: Purpose; Scope; Non-goals; Domain terms; Actors and permissions; Invariants; Workflows and lifecycle; Interface; Data ownership; Dependencies; Error and failure behavior; Security considerations; Observability; Testing expectations; Operations and recovery; Related decisions; Change history.

The Interface section addresses commands, queries, HTTP endpoints, events, or exchange formats as applicable, and includes caller constraints and failure semantics. Domain terms links the glossary rather than creating local conflicting definitions. Dependencies name obligations and failure coupling, not just library names. Testing expectations identify observable seams and scenarios, not internal test-by-test implementation instructions.

### Product surface

Purpose and actors; Scope and exclusions; Entry points and navigation; Journeys and capability references; Presentation and interaction states; Accessibility and localization where applicable; Permissions references; Loading, empty, error, and recovery states; Acceptance scenarios; Related decisions; Change history.

### Platform concern

Purpose and scope; Consumers; Guarantees and invariants; Interface and configuration; Ownership and dependencies; Limits and failure behavior; Security; Observability; Testing and operational references; Related decisions; Change history.

### Architecture view

Question and scope of the view; Elements and responsibilities; Relationships and constraints; Ownership or seams; Dependencies; Trade-offs and ADR references; Consequences for other views; Verification criteria; Change history. Use a diagram only when it clarifies the relationships.

### Interface contract

Purpose, owner, and consumers; Canonical schema and version; Inputs and outputs; Authentication and authorization references; Preconditions and invariants; Failure semantics; Ordering, retries, idempotency, concurrency, and limits where applicable; Compatibility and evolution policy; Conformance examples and tests; Related decisions. Keep exact wire shapes in a validated machine format when useful.

### Operations procedure

Purpose and trigger; Owner and escalation; Preconditions and access; Safe sequence; Validation and stop conditions; Rollback or recovery; Evidence to retain; Related contracts and decisions; Change history. Before production exists, specify intended guarantees and unresolved environment facts rather than inventing executable credentials, endpoints, or recovery measurements.

### Specification manifest

Destination; Problem and actor outcomes; Scope and parent constraints; Non-goals; Package membership with ownership; Acceptance outcomes; Explicit deferrals or open decisions; Approval and historical baseline pointer; Handoff. Detailed requirements remain in package members.

### ADR

Title and a short statement of context, choice, and why. Add alternatives and consequences when they explain a real trade-off. Status and supersession metadata preserve evolution. Use an ADR only when reversal is costly, the reason is surprising without context, and a genuine alternative was considered. Routine requirements stay in their canonical document.

### Index, agent guide, and contribution guide

An index supplies entry points and links conditioned on what a reader is doing. The agent guide explains how to find authority, scope, and the next workflow action; it links the glossary and process instead of duplicating them. The contribution guide states the change/review procedure and ownership rules. A document-structure guide owns the repository-specific taxonomy and placement examples.

### Domain glossary

Context name and short scope description, followed by terms with tight definitions and rejected synonyms where useful. Only domain concepts belong here. Keep implementation details, product requirements, and decision scratch notes in their respective canonical homes.

## Semantic history

**DOC-HIST-001**: A semantic change history records changes to behavior, contracts, invariants, data ownership, or scope, with a link to the governing package, ticket, or ADR. Formatting, spelling, and ordinary link corrections remain in Git history. Recording approval elsewhere must not create a second manually maintained log of every edit.

## Verification criteria

The [approval protocol](../operations/specification-change-control.md) owns the gate. Structural validation checks allowed states and fields, document/assertion uniqueness, references, supersession coherence, machine formats, and missing required sections. Human review checks applicability, meaning, conflicts, and evidence quality. A schema-valid document can still be wrong.

## Related decisions

See [ADR-0001](../decisions/ADR-0001-decision-history-and-current-contracts.md) and [ADR-0002](../decisions/ADR-0002-intent-and-implementation.md).

## Change history

- 2026-09-29: Initial documentation contract from the accepted interview, including type-specific templates and evidence-scoped alignment.
