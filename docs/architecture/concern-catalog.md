---
schema_version: 1
id: architecture.discovery-concerns
title: Discovery concern catalog
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
  - ../capabilities/specification-discovery.md
  - documentation-contract.md
  - ../operations/specification-change-control.md
related_decisions: []
supersedes: []
---

# Discovery concern catalog

## Purpose and scope

This catalog turns an initiative's known facts into relevant questions and completion evidence. It is consulted by concern; it is not a questionnaire presented in full on every run.

## Evaluation procedure

**CONC-FLOW-001**: For every concern, inspect its applicability and available evidence. Record applicable, not-applicable with a reason, or unresolved applicability. For an applicable concern, record its prerequisite decisions, question, deciding owner, evidence gap, risk, target documents, and completion test. Already settled concerns link their current evidence instead of creating duplicate tickets.

A sharp question can become a blocked ticket before its prerequisites resolve. Fog contains only questions not yet sharp enough to ticket. A concern does not become not-applicable merely because answering it is difficult. Unknown applicability remains a visible gap. Keep each initiative's coverage record with its review evidence and link it from the map.

| Concern | When applicable and evidence to inspect | Prerequisites and questions exposed | Completion evidence and canonical destination |
| --- | --- | --- | --- |
| Destination and scope | Always; idea, stakeholder intent, parent package | Who benefits, what changes, what is excluded, what level is this initiative? | Owner-confirmed outcome and exclusions; specification manifest |
| Actors and authority | Always; stakeholder roles and existing policy | Scope; who can decide, use, administer, or support this capability? | Named decision roles and actor responsibilities; manifest/capability |
| Outcomes and acceptance | Always; actor needs and baseline pain | Scope and actors; what observable result means success? | Measurable outcomes, representative success/failure scenarios; manifest/capability |
| Domain language and relationships | Always; stakeholder examples, parent glossary | Scope; which concepts, identities, relationships, ambiguities, and lifetimes matter? | Canonical meanings and relationships; CONTEXT.md and domain map |
| Capabilities and product surfaces | Always assess; journeys and entry points | Actors, outcomes, language; where does each ability belong and how is it reached? | Coherent capability ownership and surface references; capabilities/product-surfaces |
| Permissions and tenancy | Actor actions, privileged work, shared data, or multiple tenants; policy evidence | Actors and owned data; who can do what to which resource and under what context? | Denial cases, privilege changes, tenancy isolation; capability rules and matrix references |
| Lifecycle and invariants | Stateful or rule-driven behavior; real examples and exceptions | Domain model and outcomes; which transitions are legal and which rules must always hold? | Allowed/disallowed transitions, terminal states, cancellation and reversal scenarios; capability |
| Data ownership and privacy | Persistent or exchanged data; classification and retention needs | Domain model and constraints; who owns mutations, identity, retention, deletion, and access? | One accountable owner per data concept and lifecycle obligations; capability plus systemic views |
| Module interfaces and seams | Technical collaboration or consequential decomposition; existing constraints | Behavior and ownership; what must callers know, what varies, where can behavior be tested? | Compared alternatives where consequential, narrow caller obligations, observable test seams; architecture |
| External contracts and integrations | Machine-facing exchange or third-party reliance; primary provider documentation | Behavior, data, provider constraints; payloads, limits, auth, compatibility, failure responsibility? | Supported wire contracts, versions, errors, ownership, and limits; interfaces/platform |
| Ordering, retries, and concurrency | Repeatable, concurrent, scheduled, or asynchronous actions; transport behavior | Lifecycle and interfaces; duplicates, out-of-order arrival, conflicts, idempotency scope? | Explicit scenario outcomes and caller guarantees; capabilities/interfaces |
| Failure and recovery | Every fallible workflow; dependency failure evidence | Behavior and dependencies; what can partially succeed, how is it observed and repaired? | Failure classification, user-visible results, compensation/recovery; capability/operations |
| Security and abuse | Always assess attack exposure; actual data and trust relationships | Actors, tenancy, contracts; abuse cases, secrets, access changes, trust assumptions? | Relevant protections and threat scenarios, owner and review evidence; capabilities/platform/architecture |
| Non-functional requirements | Always assess constraints; expected workloads, partner obligations | Outcomes and dependencies; latency, capacity, availability, cost ceilings, correctness tolerance? | Measurable limits with units, conditions, and evidence plan; capability/architecture |
| Surface interaction and accessibility | Human-facing surfaces; representative users and context | Actors and workflows; navigation, empty/loading/error states, keyboard access, locale needs? | Observable interaction and accessibility scenarios; product-surfaces |
| Observability and audit | Operational or accountable behavior; failure and support needs | Workflows and failure classes; what signals explain success, denial, loss, or delay? | Events/metrics/log obligations, privacy limits, ownership; capability/platform |
| Deployment and operations | Environment-dependent behavior; actual hosting constraints if known | Architecture and constraints; release, config, rollback, support responsibility? | Intended operating guarantees and procedures, explicit unavailable environment facts; operations |
| Migration and compatibility | Existing data, contract versions, imported data, or planned cutover | Ownership and lifecycle; old/new coexistence, reversal, validation, seeding? | Migration invariants and rollback/forward recovery decisions; operations/interfaces |
| Disaster recovery | Durable critical state or availability commitments; retention and dependency facts | Data criticality and availability; loss tolerance, restore objective, recovery verification? | RPO/RTO or justified alternatives, restore validation and responsibility; operations/architecture |
| Testing and evidence | Always; observable seams and acceptance outcomes | Invariants, contracts, failures; what demonstrates correctness without depending on internal layout? | Coverage of obligations and high-value scenarios at appropriate seams; capability/contracts |
| Unknowns and exclusions | Always; review findings and conflicting evidence | All current concerns; what is unsupported, assumed, deferred, or not yet understood? | Explicit non-goals, admissible deferrals, remaining blockers; manifest/review evidence |

Cross-cutting constraints may be discovered early and reshape preceding decisions. External provider or legal/contractual claims need dated primary evidence or an explicitly identified knowledge-holder answer. The workflow never fabricates load, retention, compliance, or availability requirements merely to populate a template.

## Risk rules

**CONC-RISK-001**: Assess risk from the actual initiative and record the rationale. Use the highest applicable level. Raising risk reopens the affected coverage and review obligations; lowering it requires an explicit reason and owner acceptance.

| Level | Typical trigger | Additional rigor |
| --- | --- | --- |
| Standard | Reversible internal behavior with low data and operational impact | Owner review and all applicable concern checks |
| Elevated | Shared contracts, personal data, money-related workflow, external integration, migration, meaningful operational impact | Review by the responsible domain owner and relevant failure/compatibility evidence |
| Critical | Authentication/authorization, financial correctness, regulated or safety-critical behavior, irreversible migration, contractual availability, disaster recovery | Explicit specialist reviewer responsibilities, adversarial scenarios, concrete evidence for the critical obligation |

Risk selects relevant work; it does not create fictitious teams or automatically demand unrelated compliance checklists. The same person may have multiple qualified responsibilities; record the actual review and limitations. Where expertise is missing, obtain it through the stakeholder-gap path.

**CONC-DESIGN-001**: Consequential module interfaces, seams, data ownership, capability placement, external contracts, and technology lock-in require materially different alternatives. Risk can increase the evidence and reviewers needed; it cannot waive a consequential trade-off by calling the initiative small. Reversible internal details allowed by WF-SCOPE-004 do not require speculative alternatives.

## Example of frontier progression

A vague request for billing first exposes who is charged, what they receive, and whether payment gates access. If payment gates access, lifecycle and failure questions become precise: what happens after payment succeeds but access provisioning fails? That answer then constrains data ownership, retry/idempotency obligations, recovery, and support visibility. The catalog supplies coverage while the actual answers determine the route. No billing policy is predetermined by this example.

## Verification criteria

Each applicable row has evidence or an explicit unresolved ticket; each not-applicable row has a reason. Review checks that important concerns cannot disappear merely because the frontier is empty. [Validation scenarios](../specifications/decision-workflow/validation.md) exercise this behavior.

## Change history

- 2026-09-29: Initial typed concern catalog and risk policy, implementing accepted Q36 and Q39 at specification level.
