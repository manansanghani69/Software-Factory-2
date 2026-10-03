# Documentation handbook

First design draft · 2026-10-01. This is the proposed document architecture for projects using the workflow; the current research packet is a design artifact rather than a populated project instance.

## Structure

Use repository Markdown for durable definitions. Create folders/files when content earns them. The illustrative layout below is a routing convention, not an instruction to create empty files.

```text
docs/definition/
├── README.md                  # index, manifest links, current slice, next session
├── HANDBOOK.md                # project-specific authoring rules and authority
├── PROJECT.md                 # intake + brief + Intent decision
├── CONTEXT.md                 # glossary only
├── DOMAIN.md                  # relationships, states, invariants, journey links
├── DELIVERY-MAP.md            # scope baseline, IDs, issue URLs, continuations
├── DECISIONS.md               # linked index: Wayfinder issues and ADRs
├── journeys/                  # flows/maps where a separate file is warranted
├── research/                  # findings and evidence for real questions
├── adr/                       # significant accepted decisions
├── contracts/                 # genuinely shared API/event/data contracts
├── features/<feature-id>/
│   ├── SPEC.md                # authoritative feature behavior
│   ├── ACCEPTANCE.md          # examples if too large for SPEC.md
│   ├── DESIGN.md              # conditional interaction/design definition
│   └── API.md                 # conditional feature-owned contract
└── slices/<slice-id>/
    ├── SLICE.md               # outcome, scope, baseline references
    ├── MANIFEST.md            # required + skipped artifacts
    ├── READINESS.md           # four gate records / links, approved packet
    └── TICKETS.md             # candidate packet; URL bindings after publish
```

Feature definitions may span slices. Each slice pins the approved revision of the feature rules it consumes. Add rules for the next slice as clearly unapproved proposals or in a separate draft; an approved feature file must distinguish current truth from future ideas. A shared contract has one authoritative file under `contracts/`; feature API docs reference it rather than creating a second definition.

The active slice index identifies current baselines, manifest status, open questions, GitHub map URLs, and the next valid skill. Every artifact is reachable from it. The handbook identifies where to write each kind of information and how to handle supersession.

## Mandatory information

| Artifact | Information required | May be combined? |
| --- | --- | --- |
| Project brief | Actors, present problem/baseline, evidence, desired outcomes/success signals, appetite, constraints, assumptions, non-goals | Intake can be a section |
| Glossary | Canonical project-specific terms and precise definitions | Keep glossary focused; domain mechanics live elsewhere |
| Delivery Map | Stable scope IDs, decomposition, slices, definitions, issue links, continuation edges | Journey map can be linked from it |
| Handbook/index | Authoring/authority rules, navigation, current slice, manifests, statuses | Small project may use one file |
| Decision index/map | Questions, evidence links, resolved pointers, fog, exclusions, affected slice/doc/gate | Use GitHub Wayfinder map as authoritative question index |
| Slice definition | Outcome, boundary, non-goals, approved feature/rule references, residual uncertainty/discretion | Feature details can be sections or linked files |
| Acceptance information | Observable rules and normal/failure/boundary examples with stable IDs | Keep inside SPEC.md until separation improves navigation |
| Readiness record | Gate approvals, exact revisions, residual risk, packet identity, published issue links | One record can contain all four gate entries |

Require the information, not a universal file count. Separate files when ownership, size, independent consumers, or reuse justify them. A one-screen feature may have behavior and examples in one SPEC.md. A multi-consumer API usually needs a separately reviewable contract.

## Document-selection stage

For each selected slice inspect every row. Record `required`, `covered by existing artifact`, or `skipped` with a reason, applicable scope, owner, prerequisites, and review evidence. Reassess when scope or risk changes. A skip is a judgment about applicability; it does not excuse omission of acceptance or relevant behavior.

| Dimension / trigger | Artifact or section | Questions it must settle |
| --- | --- | --- |
| Nontrivial behavior or state | Feature SPEC + acceptance examples | Actors, rules, state transitions, invariants, normal/failure/boundary behavior, side effects, exclusions |
| New interaction/navigation/content | UX/DESIGN | Journey, screen states, input/feedback, empty/loading/error states, accessibility, responsive behavior, copy where consequential |
| API/event/integration boundary changes | API/event contract | Consumers, auth, schemas, examples, validation/errors, versioning, compatibility, idempotency/order/retries where applicable |
| Persistent data/ownership/invariant changes | Data model; migration plan when needed | Ownership, lifecycle, invariants, retention/deletion, concurrency, migration sequencing, recovery |
| Consequential architecture/infrastructure choice | Design proposal/RFC; accepted ADR if warranted | Constraints, alternatives, feasibility evidence, boundaries, trade-offs, consequences |
| Permissions/sensitive data/trust/abuse change | Security/privacy assessment | Roles, allowed/denied actions, data exposure, trust assumptions, relevant abuse/privacy obligations |
| Performance/reliability/accessibility need | Quality section or quality plan | Measurable target, conditions, measurement/proof, failure tolerance, degraded behavior |
| Production operation/deployment change | Rollout/operations/rollback plan | Flag/ramp, support, observability, alerts where needed, compatibility, rollback/roll-forward conditions |
| Value/usability uncertainty | Research/experiment plan and findings | Hypothesis, evidence needed, participant/source relevance, decision threshold, learning limit |
| User-facing operation or support change | User-doc/support plan | Instructions, affected users, content owner, readiness/release need |
| Measurement required for selected outcome | Measurement section/analytics contract | Baseline, success signal, event meaning, data owner, collection conditions |

Security/compliance and quality depth follows the project context and actual affected boundaries. A routine document edit may legitimately skip most rows. A payments/identity change cannot skip consequential behavior merely to make the manifest look small.

## Metadata

Project artifacts use the following stable metadata, with `null` or `[]` for genuinely inapplicable fields:

```yaml
id: FEAT-INVITE-SPEC
type: feature-spec
status: draft
owner: human-name-or-role
scope_node: FEAT-INVITE
delivery_slice: [S01]
depends_on: [CONTRACT-INVITES, DEC-EXPIRY]
supersedes: null
last_updated: YYYY-MM-DD
decisions: []
issues: []
```

Use `revision` in approval records to identify a commit, tagged version, or immutable review snapshot. Date alone does not pin approved content. Maintain reciprocal links where needed to compute impact: a dependent names its prerequisites; the index can enumerate dependents. Manual review must follow those links, not imply an automated graph is running.

## Writing rules

1. Identify the authoritative subject and scope. Define one home for each rule/contract; cross-link other consumers.
2. Separate observed evidence, assumptions, proposals, approved truth, and implementation discretion. Give claims their sources and the limits of the evidence.
3. Make behavior observable. Prefer “An expired invitation is rejected with the defined error” over “Invitations are robust.” Relevant nonfunctional claims need a target and proof method.
4. Write normal, denied/failed, and boundary examples. Include state/time/order interactions when those affect behavior. Mark unanswered cases with Decision Ticket links.
5. Keep glossary terms in CONTEXT.md. Relationships, transitions, and rules belong in domain/feature definitions. Capture only significant irreversible trade-offs in ADRs.
6. Keep current approved truth coherent. Drafts for later slices must not silently redefine the current baseline.
7. Record exclusions and accepted discretion explicitly. A missing detail is not automatically implementer discretion.
8. Match depth to consequences. Expand a contract when independent consumers need precision; combine sections when separate files would only duplicate navigation.
9. Review from a fresh implementer's perspective: can they find the outcome, rules/examples, constraints, relevant source revisions, verification, and unresolved questions?
10. On change, record affected dependencies and approvals, retain superseded history, update the index, and rerun the responsible gate.

## Minimum content by artifact

**Feature specification:** purpose/outcome, actors and permissions, scope/non-goals, referenced domain language, rules/states, observable side effects, failure/boundary behavior, constraints, rule/example IDs, decision links, allowed discretion, applicable conditional docs.

**API/event contract:** operation/event purpose, consumers, authentication/authorization, schema and field semantics, example request/response or payload, validation/error behavior, compatibility/versioning. Add idempotency, ordering, retry/timeout, pagination, rate limits, and delivery guarantees only where applicable. Examples must agree with the schema.

**UX/design:** journey and interaction rules, critical screens/states, validation/feedback, accessibility, mobile/responsive expectations, and approved assets/prototypes. State which presentation details may be decided later.

**Data/migration:** ownership/invariants, lifecycle, conceptual schema, compatibility, backfill/migration order, irreversible steps, and applicable recovery/verification.

**Proposal/RFC:** problem, constraints, options, evidence, proposed choice, open questions, and reviewers. Acceptance is a decision; it does not schedule implementation.

**ADR:** one significant accepted decision, why alternatives lost, and meaningful consequences. Retain accepted/superseded status and successor links. Use the concise domain-modeling format where sufficient.

**Readiness:** gate judgments, named revisions, manifest completion, acceptance-to-work coverage, actual dependency order, residual risk/discretion, human/date, exact candidate packet, publication bindings.
