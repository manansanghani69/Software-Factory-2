# Project Definition System artifact handbook

## Restart and navigation

For a fresh session, locate the project's definition index (normally `docs/definition/README.md`) and read the brief, active slice, manifest, latest gate, and map index. Load detailed documents only for the next frontier item. Every artifact must be reachable from the index. If a project uses another established layout, preserve it and record the authority mapping in its handbook.

## Authority and layout

Use repository Markdown for durable definitions. A normal layout is:

```text
docs/definition/
├── README.md · HANDBOOK.md · PROJECT.md · CONTEXT.md · DOMAIN.md
├── DELIVERY-MAP.md · DECISIONS.md
├── journeys/ · research/ · adr/ · contracts/
├── features/<feature-id>/SPEC.md, ACCEPTANCE.md, DESIGN.md, API.md
└── slices/<slice-id>/SLICE.md, MANIFEST.md, READINESS.md, TICKETS.md
```

Create only artifacts that earn their own boundary. A feature may combine behavior and examples in one specification. A shared contract has one authoritative home under `contracts/`; consumers link to it. Existing current artifacts may satisfy a manifest row only after currency and applicability are checked.

| Information | Authoritative home |
| --- | --- |
| Intent, boundaries, behavior, contracts, acceptance | Approved repository documents |
| Investigation and decision conversation | Wayfinder Decision Ticket |
| Current accepted rule | Feature, slice, or contract document |
| Significant trade-off/history | ADR |
| Live assignment, parentage, blockers, work state | GitHub Issues after publication |
| Proposed decomposition before publication | Delivery Map/candidate packet |

## Required metadata

Every project artifact should carry stable metadata, using `null` or `[]` when genuinely inapplicable:

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

Approval records use an immutable commit, tag, or review snapshot as `revision`; a date alone does not pin approved content. Maintain reciprocal links where impact must be computed. Stable IDs survive ordinary revisions and are superseded only when the identity changes.

## Mandatory information

- Project brief: actors, present problem/baseline, evidence, outcomes/signals, appetite, constraints, assumptions, non-goals.
- Glossary: canonical project terms and precise definitions; keep mechanics elsewhere.
- Delivery Map: stable IDs, decomposition, slices, definitions, issue links, continuations.
- Handbook/index: authority rules, navigation, current slice, manifests, statuses.
- Decision Map: questions, evidence, resolutions, fog, exclusions, affected scope/document/gate.
- Slice definition: outcome, boundary, non-goals, approved references, uncertainty, discretion.
- Acceptance: observable normal, failure, and boundary examples with stable IDs.
- Readiness: gate approvals, exact revisions, manifest completion, coverage, dependency order, risk/discretion, human/date, exact candidate packet, publication bindings.

## Document selection and content criteria

At manifest selection, inspect every dimension below plus mandatory information. Record `required`, `covered by existing current artifact`, or `skipped` with reason, applicable scope, owner, approver, prerequisites, intended authority, content depth, and review evidence. Reassess on scope/risk change; a skip cannot omit relevant behavior or acceptance. During definition, load only the rows and artifact criteria applicable to the current branch.

| Dimension / trigger | Artifact or section | Questions it must settle |
| --- | --- | --- |
| Nontrivial behavior or state | Feature SPEC + acceptance examples | Actors, rules, transitions, invariants, normal/failure/boundary behavior, side effects, exclusions |
| New interaction/navigation/content | UX/DESIGN | Journey, screen states, input/feedback, empty/loading/error states, accessibility, responsive behavior, consequential copy |
| API/event/integration boundary change | API/event contract | Consumers, auth, schemas, examples, validation/errors, versioning, compatibility, applicable idempotency/order/retries |
| Persistent data/ownership/invariant change | Data model; migration plan when needed | Ownership, lifecycle, invariants, retention/deletion, concurrency, migration order, recovery |
| Consequential architecture/infrastructure choice | Proposal/RFC; accepted ADR when warranted | Constraints, alternatives, feasibility evidence, boundaries, trade-offs, consequences |
| Permissions/sensitive data/trust/abuse change | Security/privacy assessment | Roles, allowed/denied actions, exposure, trust assumptions, relevant abuse/privacy obligations |
| Performance/reliability/accessibility need | Quality section or plan | Measurable target, conditions, measurement/proof, failure tolerance, degraded behavior |
| Production operation/deployment change | Rollout/operations/rollback plan | Flag/ramp, support, observability, applicable alerts, compatibility, rollback/roll-forward conditions |
| Value/usability uncertainty | Research/experiment plan and findings | Hypothesis, needed evidence, participant/source relevance, decision threshold, learning limit |
| User-facing operation/support change | User-doc/support plan | Instructions, affected users, content owner, readiness/release need |
| Measurement required for outcome | Measurement/analytics contract | Baseline, success signal, event meaning, data owner, collection conditions |

Match depth to actual consequences and affected boundaries. A routine document edit may skip most dimensions; consequential payments or identity behavior remains required.

### Minimum content by artifact

**Feature specification:** purpose/outcome, actors and permissions, scope/non-goals, domain language, rules/states, observable side effects, failure/boundary behavior, constraints, rule/example IDs, decision links, discretion, applicable conditional documents.

**API/event contract:** operation/event purpose, consumers, authentication/authorization, schema and field semantics, request/response or payload examples, validation/errors, compatibility/versioning. Add idempotency, ordering, retry/timeout, pagination, rate limits, and delivery guarantees where applicable. Examples must agree with schemas.

**UX/design:** journey and interaction rules, critical screens/states, validation/feedback, accessibility, mobile/responsive expectations, approved assets/prototypes, and presentation details left to discretion.

**Data/migration:** ownership/invariants, lifecycle, conceptual schema, compatibility, backfill/migration order, irreversible steps, applicable recovery and verification.

**Proposal/RFC:** problem, constraints, options, evidence, proposed choice, open questions, reviewers. Acceptance does not schedule implementation.

**ADR:** one significant accepted decision, why alternatives lost, meaningful consequences, accepted/superseded status, successor links.

**Readiness:** gate judgments, named revisions, manifest completion, acceptance-to-work coverage, actual dependency order, residual risk/discretion, human/date, exact candidate packet, publication bindings.

## Writing and evidence

Identify one authoritative home for every rule or contract. Separate observed evidence, assumptions, proposals, approved truth, and implementation discretion. Give consequential claims sources and evidence limits. Make behavior observable and include relevant normal, denied/failed, boundary, state/time/order examples. An unanswered case stays visible with a Decision Ticket link.

Keep glossary terms in the glossary; put relationships, transitions, and rules in domain/feature definitions. Use ADRs only for significant, costly-to-reverse trade-offs. Mark later-slice drafts as proposals, never as current truth. Record exclusions and discretion explicitly: a missing detail is not automatically discretion. Match depth to risk and review from a fresh implementer's perspective.

## Fresh-session handoff

Use the session-handoff template at the end of every invocation. It is not a replacement for the artifacts: changed files and the current gate/frontier must be written into the project index or handoff record, and important claims must remain linked to authoritative source revisions. A usable handoff names exact repository-relative paths or stable URLs plus revisions for the definition index, active slice, current brief, latest gate, map/frontier, manifest when relevant, and every source document required by the next invocation. If any of those are unknown, record the handoff as incomplete and stop at that frontier rather than asking a fresh session to guess.
