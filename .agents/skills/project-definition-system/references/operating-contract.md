# Project Definition System operating contract

## Purpose and authority

Define enough of the selected Delivery Slice that implementation requires no invention of material product behavior, boundaries, contracts, acceptance conditions, significant quality constraints, or prerequisite order. List implementation discretion explicitly. Classify every other unknown as a learning spike, deferred work, or out of scope.

The human owns outcome selection, appetite, evidence acceptance, business/legal judgment, risk acceptance, and gate approvals. The agent retrieves evidence, identifies contradictions, proposes alternatives, drafts artifacts, and assembles evidence. Detail is not authority. The coordinator recommends; it never crosses a gate, schedules work, launches a pipeline, or publishes issues merely because an artifact proposes it.

## Fresh bounded sessions

Resumable means saved artifacts can continue in a fresh chat. It never means running the whole workflow in one conversation. At startup, read the low-resolution current index/slice, latest gate, and frontier; then load only the relevant authoritative sources and templates. Verify important claims against those sources rather than treating a prior conversation or compressed handoff as authority.

One session has one bounded purpose:

- a decision session resolves one Wayfinder question;
- a definition session handles one coherent feature, contract, or behavioral branch;
- a review session handles the evidence for a named gate; Definition and Readiness may share a compact review while retaining separate judgments.

A large stage may span several sessions. Repeating a skill in the same chat is not a context reset. Every session writes actual artifacts and a short handoff naming changed files, settled decisions and source links, open questions or blockers, valid approvals with revisions, and the next valid manual invocation with required inputs. The handoff must give exact repository-relative paths or stable URLs and revisions for the definition index, active slice, current brief, latest gate, active map/frontier, manifest when relevant, and every source required by the next invocation. An unpinned label such as “current brief” is incomplete; a fresh session must be able to retrieve the authoritative input without relying on prior chat context.

## Stage and gate route

| Skill | Stage output | Gate or next boundary |
| --- | --- | --- |
| `define-capture` | Intake, provenance, classification, source index | `define-frame` |
| `define-frame` | Brief and Intent record | Intent Gate |
| `define-wayfinder-chart` | Decision Map, tickets, scoped fog | Next manual decision/work session |
| `define-domain-model` | Glossary, domain model, contradictions | Journey or blocking decision |
| `define-journey-and-slice` | Journey, candidate slices, selection evidence | Slice Gate |
| `define-document-manifest` | Complete manifest and drafting order | Definition frontier |
| `define-slice-definition` | Definitions, rules, examples, conditional docs | Definition Gate |
| `define-delivery-map` | Candidate packet, coverage, dependency order | Readiness review |
| `define-readiness-review` | Exact readiness record and packet authorization | Readiness Gate |
| `define-github-publish` | Verified issue bindings and handoff | Implementation consumer after Readiness, or the current definition frontier for planning-only publication |
| `define-change-recovery` | Impact record and reauthorized successor baseline | Responsible stage/gate |

`define-next` chooses among these based on current records. The four gates are Intent, Slice, Definition, and Readiness. Preserve unchanged approvals; do not ask the human to reconfirm them.

## Gate evidence and outcomes

For the gate under review, assess every evidence item below and retain the checklist with source revisions. Every result records human/date, outcome, reasons, conditions or return path, and authorized work. A pass requires an explicit human result and immutable artifact revisions; an unchecked item or unresolved material question prevents `pass`.

| Gate | Evidence checklist | Passing authorizes |
| --- | --- | --- |
| Intent | Target actors; present baseline; outcome/success signals; evidence vs assumptions; constraints; non-goals; appetite | Discovery and shaping within the intent |
| Slice | Outcome; vertical journey; included/excluded behavior; macro solution; dependencies; risk; opportunity cost; appetite | Detailed definition of the selected boundary |
| Definition | Complete manifest; rules/examples; applicable contracts/design/data; quality constraints; significant decisions; classified residual uncertainty; explicit discretion | Candidate implementation decomposition |
| Readiness | Current Definition approval; acceptance-to-work coverage; bounded execution units; dependencies/cycles/coordination; verification; document access; risk acceptance; exact candidate packet ID/revision | Publication and implementation handoff of that execution set |

`revise`, `spike`, `defer`, and `stop` identify a bounded return path or stopped scope. A `spike` result must name the exact learning question, limit, expected evidence, responsible person, and return gate in the gate record. It authorizes bounded research or a disposable prototype only; results do not authorize production code. A failed gate stops downstream commitment for the affected slice while unrelated approved work may continue.

If mapping exposes a material choice, update the responsible definition and repeat impacted approvals before Readiness passes. Separate Definition and Readiness judgments even when reviewed together.

## Maps and publication

The Wayfinder Decision Map indexes questions and decisions. The Delivery Map decomposes intended and approved work. A scope node has one structural parent; dependencies are separate edges. Precise questions become Decision Tickets, vague in-scope uncertainty stays fog, and excluded work is recorded out of scope. Use the installed Wayfinder behavior when available; the adapter reference defines the fallback.

Repository documents own durable intent, scope, behavior, contracts, acceptance, and accepted decisions. GitHub Issues own live hierarchy, assignment, blockers, and work state after publication. Before publication, the repository candidate packet owns proposed parentage. Never invent a repository URL or issue relationship.

Executable publication requires an explicit `define-github-publish` invocation for a named repository and exact passing Readiness packet. Explicitly scoped `define-wayfinder-chart` sessions may publish Decision Maps and decision tickets earlier. An explicit `define-github-publish` invocation may also publish a named planning-only packet of containers before Readiness; mark them as containers in definition with no execution authorization. Use the integration adapter's publication boundaries for each case.

Reconcile stable IDs before creation, create authorized issues once, store URLs immediately, wire parentage and blockers in a second pass, read back every relationship, and retain a partial ledger if interrupted. Keep approval readiness separate from lifecycle and blocker state. New behavior, contract, outcome, acceptance, consequential dependency, or appetite changes trigger recovery rather than silent edits.

Containers aggregate child completion and explicit integration acceptance. Closing all children is insufficient until the container's outcome is proved. Give each container an outcome, scope, child links, definition/gate links, and integration acceptance; avoid duplicate execution authorization between a container and its children.

Before conceptual overflow publication, check current tracker depth/width capabilities and whether added grouping has useful meaning. A continuation root records `logical_parent` and the complete stable-ID path in its body and repository map; links connect the logical parent and root in both directions. Mark the edge as logical rather than native, keep native relationships within supported limits, and read back both links. Width overflow uses meaningful groups or explicit continuations preserving logical parent/child IDs. Include every overflow exception in the handoff.

## Bounded-change route

A bounded change may reuse the accepted outcome, brief, glossary, and designs after checking currency and applicability. Confirm that it introduces no new material decision, contract, trust boundary, migration, or substantial scope expansion. Assess documents, define focused rules/examples, map the bounded issue, and record separate Definition/Readiness results in a compact review. Broader uncertainty returns to discovery/slicing; existing documents do not bypass a required gate.

## Rolling slices and shared contracts

Later definition may consume an approved current contract or propose a successor. Keep the baseline used by running issues intact and mark the successor as a proposal until approved. Every successor proposal identifies compatibility, migration order, affected running issues, and the point at which the successor becomes effective. Pin each consumer to its applicable revision; route material impacts on running work through recovery and the affected gates before switching its baseline.

## Recovery and state

On material change: record the trigger and old baseline; trace reverse links through dependencies, examples, contracts, and scope; mark affected artifacts/issues stale and control affected execution through its consumer; resolve the question; update definitions and decision history; recompute coverage/dependencies/appetite; repeat impacted gates; and update or supersede issue bindings. Preserve unrelated approvals.

Documents move `draft → review → approved → stale → superseded/retired`. Slices move `discovery → shaping → selected → defining → ready → implementing → complete`, with explicit defer/stop outcomes. Issues have lifecycle `open → in progress → review → done`, side outcomes `deferred`, `out of scope`, and `superseded`, plus independent claimed/unclaimed, blocked/unblocked, and readiness attributes.
