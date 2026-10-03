# Operating workflow

First design draft · 2026-10-01. Accepted policy choices are recorded in the ADRs; this document makes them operational for review.

## 1. Operating rule

Define enough of the selected Delivery Slice that implementation requires no invention of material product behavior, boundaries, contracts, acceptance conditions, significant quality constraints, or prerequisite order. List the choices that remain at implementation discretion. Classify all other unknowns as a learning spike, deferred work, or out of scope.

The human owns outcome selection, appetite, evidence acceptance, business/legal judgments, risk acceptance, and gate approvals. AI interviews, retrieves facts, identifies contradictions, proposes alternatives, drafts artifacts, and assembles evidence. An AI-generated claim carries no evidential authority merely because it is detailed.

The workflow is manual: invoke one stage skill, review its output, record the result, and choose the next valid stage. The coordinator recommends that next stage. It does not schedule sessions or silently cross a human gate.

## 2. Stage route

| Stage | Starting material | Work and decision factors | Durable output | Completion / next step |
| --- | --- | --- | --- | --- |
| 01 Capture | Raw idea, notes, PRD, conversations, existing docs | Preserve the request, provenance, target situation, and contradictions. Identify greenfield, substantial feature, or small change. | Intake section/file; source links | Inputs are represented without invented certainty → Frame |
| 02 Frame | Intake and available evidence | Who has the problem? What is the current situation? Why now? Desired outcome, success signals, constraints, appetite, assumptions, exclusions. | Project brief | **Intent Gate** → discovery, revision, spike, defer, or stop |
| 03 Discover and model | Accepted intent | Chart Wayfinder; research facts; model vocabulary, actors, relationships, state, and the whole journey. Rank consequential uncertainty. | Decision Map, glossary, journey/domain model, research | Journey covered at broad resolution; questions/fog visible → shape slices |
| 04 Shape and slice | Journey, evidence, macro options | Connect the important solution elements. Propose coherent vertical slices and compare value, risk, dependencies, appetite, reversibility, and opportunity cost. | Broad Delivery Map; slice candidates | Each candidate has an outcome, boundary, exclusions, dependencies, and evidence → selection |
| 05 Select next slice | Candidate slices | Human chooses the next investment. A selected slice is a commitment to definition, not yet permission to implement. | Slice brief and scope baseline | **Slice Gate** → document selection |
| 06 Select documents | Selected scope and change/risk profile | Inspect every dimension in DOCUMENTATION.md. Choose artifacts and relevant depth, ownership, prerequisites, and skip reasons. | Document manifest | Every dimension assessed; required and skipped artifacts accounted for → definition |
| 07 Define slice | Manifest, scope, resolved decisions | Rules, examples, states, permissions, failures, UX, APIs/events, data, quality, and rollout as applicable. Resolve material questions through Wayfinder. | Approved feature/slice definitions and conditional docs | **Definition Gate** passes against named document revisions → mapping |
| 08 Map work | Approved definitions | Draft meaningful nodes and execution issues. Check coverage, dependencies, integration points, shared resources, and execution order. | Candidate ticket packet and Delivery Map links | Each acceptance example covered; no invented behavior → readiness |
| 09 Review readiness | Definition approval and candidate packet | Human checks traceability, testability, usable sequencing, residual risks, implementation discretion, and appetite. | Readiness record authorizing exact draft packet | **Readiness Gate** passes → publication |
| 10 Publish and hand off | Readiness approval, repo, candidate packet | Create/link issues, verify relationships, bind issue URLs to stable IDs, reconcile partial publication, assemble handoff. | GitHub issue hierarchy, dependencies, implementation packet | Published issues match approval and documents are accessible → implementation consumer |
| 11 Continue rolling definition | Slice N handoff and new evidence | Shape N+1; capture lessons, update later options, recover affected work when a material change appears. | Next slice frontier; change records | Repeat stages 03–10 for the next slice as needed |

Stages are an order of commitment, not a prohibition on iteration. New evidence returns to the responsible stage. Existing documents can satisfy inputs after applicability and currency are reviewed. No approved gate is bypassed by a pre-existing PRD.

## 3. Four gates

Every gate records a human, date, outcome, artifact references/revisions, reasons, open conditions, and the work it authorizes. Outcomes are `pass`, `revise`, `spike`, `defer`, and `stop`. An unchecked item or an unresolved material question prevents `pass`.

| Gate | Required decision | Evidence to inspect | What passing authorizes |
| --- | --- | --- | --- |
| Intent | Is this problem and intended outcome worth defining? | Target actors; baseline situation; outcome/success signals; evidence vs assumptions; constraints; non-goals; appetite | Discovery and shaping within that intent |
| Slice | Is this the next coherent portion to define? | Outcome; vertical user/system journey; included/excluded behavior; macro solution; dependencies; risk; opportunity cost; appetite | Detailed definition for that selected boundary |
| Definition | Is material behavior settled and approved? | Manifest; rules/examples; applicable contracts/design/data; quality constraints; significant decisions; classified residual uncertainty; explicit discretion | Candidate implementation decomposition |
| Readiness | Is this issue packet authorized for implementation? | Definition approval; coverage; execution units; dependencies; verification; doc accessibility; risk acceptance; candidate packet revision | Publication and handoff of the approved issue set |

Definition and Readiness can happen in one review session, but retain separate judgments. If mapping exposes a material choice, return to definition, update documents, and repeat the impacted approvals before readiness passes.

A spike result names the exact learning question, limit, evidence expected, responsible person, and return gate. Research or disposable prototypes are permitted learning work before production readiness. Their results do not automatically authorize production code. A failed gate stops downstream work for the affected slice; unrelated approved work may continue.

## 4. Decision Map and Delivery Map

Wayfinder's destination is scoped to the next commitment, such as “Definition Complete for Slice S01.” Project-wide foundational uncertainty can have its own map; a slice can have a separate map linked to the project. Keep each map small enough to orient a session.

Each Wayfinder map retains its direct child decision tickets and its existing chart/work conventions. This workflow adds links from each question to the affected scope node, document, and gate. It does not require rewriting the installed Wayfinder skill or turning execution tasks into Wayfinder decision work.

- Precise question: create a Decision Ticket even when it is blocked.
- Vague in-scope uncertainty: record fog with the scope/destination it affects.
- Excluded work: record out of scope. Reconsider it through a changed boundary or new effort.
- Available frontier: open, unblocked, unclaimed decision tickets; claim before work.
- Resolution: record evidence and the human decision where needed, close the question, update the map index, and write the resulting current rule into its authoritative definition.

The Delivery Map has a default decomposition:

```text
Project
└── Delivery Slice — outcome, baseline, appetite
    └── Capability
        └── Feature
            └── Story — rules and acceptance examples
                └── Task
                    └── Subtask
```

Skip levels without useful meaning. Add meaningful branches when the work requires them. Each node has one structural parent; dependencies are separate edges and can cross parents or slices. Outcomes attach to slices and scope nodes. Shared capabilities can be referenced from multiple slices; create a slice-specific work instance when needed rather than giving one issue multiple structural parents.

Readiness concerns the next execution units and their coverage, not whether every eventual subtask exists. A ready Story can be executable without child Tasks. A Story grouping ready Tasks is a container. Set `execution_role: container | executable` explicitly; node depth does not determine authorization.

## 5. Artifact authority and arbitrary depth

| Information | Authoritative home | Other representations |
| --- | --- | --- |
| Product intent, boundaries, behavior, contracts, acceptance | Approved repository documents | Issues link to exact rules/examples and baseline revisions |
| Investigation and decision conversation | Wayfinder decision issue | Decision index links with a one-line gist |
| Current accepted rule | Feature/slice/contract document | Resolution issue links to it |
| Significant trade-off and history | ADR | Definitions link to the ADR |
| Live assignment, native parentage, blockers, work state | GitHub Issues | Repository map links/snapshot; read GitHub for current work state |
| Proposed decomposition before publication | Repository Delivery Map / candidate packet | Reviewed and bound to GitHub URLs at publication |
| Conceptual overflow beyond native nesting | Explicit parent-ID edges in repository map | GitHub continuation roots link both ways |

The repository map explains scope and preserves a reviewable baseline. It does not pretend to be live issue status. After publication, synchronize deliberate hierarchy edits between GitHub and the scope record; do not make silent competing parent changes. Scope meaning remains defined by approved documents.

GitHub documents up to 100 children per parent and eight nested sub-issue levels. The default seven-node path fits. For larger conceptual maps:

1. First check whether the extra grouping serves a real decision or coordination need.
2. For a genuine depth limit, create a linked continuation root. Record `logical_parent` and the complete stable-ID path in its body and repository map. Native parentage must remain within the supported depth.
3. Link the continuation root from its logical parent and link back. Mark the relationship as a logical continuation rather than a native sub-issue.
4. For a width limit, split only into meaningful groupings or linked continuation groups, preserving logical parent/child IDs.

The conceptual map can have arbitrary depth; the native GitHub tree cannot. The publishing review must show where a conceptual edge uses a link instead of native nesting. This fallback incurs manual maintenance and is visible in the handoff.

## 6. Execution issue contract

Every executable issue carries a stable scope/work ID alongside its GitHub identity. Use a readable title; human references wrap the URL in that title rather than relying on bare numbers.

The body provides: objective/outcome; parent and slice; bounded scope and exclusions; links to relevant rules/examples and approved revisions; a short issue-specific behavior summary; acceptance checklist; validation method; quality/contract constraints; dependencies; allowed implementation discretion; and expected completion evidence. Link to enough context that a fresh session can understand the issue without reading this conversation.

Different levels can be executable. Avoid duplicate execution authorization for both a parent Story and all its Tasks. Container completion aggregates children and any explicit integration acceptance; merely closing child issues is insufficient if the slice outcome remains unproved.

Blockers describe genuine prerequisites. Shared files or resources may require coordination even where no product dependency exists; note the conflict and choose ownership or serialization. Check dependencies for cycles and unknown endpoints before readiness. Separate decision readiness from execution prerequisites: a ready approved issue can still be blocked by another implementation issue.

During delivery, adding or regrouping Tasks/Subtasks within approved behavior is allowed. Additions retain parent, source rules, and validation links. New behavior, contract changes, outcome changes, acceptance changes, consequential dependency changes, or expanded appetite trigger change recovery.

## 7. Manual publication protocol

Designing this workflow does not create project issues. On a future application, the human explicitly chooses the repository and invokes publishing for an approved packet.

1. Read the readiness record and confirm the packet revision and repository. Fetch existing matching IDs before creating issues.
2. Check tracker capabilities/access and document revision accessibility. If a required definition is only local, commit/share it through the authorized project workflow before handoff; never invent a repository URL.
3. Planning containers may be published earlier under the human's chosen planning scope. Mark them as containers in definition; they authorize no execution. Executable Stories/Tasks/Subtasks wait for readiness.
4. Create missing approved issues, parents before children where practical. Store the resulting URL against each stable ID immediately. Use a second pass for native parent edges and blockers after IDs exist.
5. If interrupted, retain the creation ledger, mark publication incomplete, and resume by ID lookup. Reuse matching issues; reconcile mismatches rather than creating duplicates or deleting history.
6. Read back titles, source links, roles, parents, blockers, and labels/fields. Verify the entire approved set, including any continuation links. Record URLs and publication completion in readiness/handoff evidence.
7. Hand off the outcome, baseline references, executable frontier, integration acceptance, residual risk, and allowed discretion to the implementation consumer.

The human manually invokes these steps through the publishing skill. Native issue relationships can be set through GitHub UI or supported APIs/CLI; a particular command is not part of the product contract.

## 8. Rolling lanes and shared contracts

Normally Slice N is implementing, N+1 is actively being defined, and later slices carry direction and fog. Several implementing slices are acceptable when their contracts, resources, and dependencies are independent or explicitly coordinated.

Later definition can consume approved current contracts. It can propose a successor contract, but it cannot silently mutate the baseline used by running issues. Such a proposal identifies compatibility, migration order, affected running issues, and the point at which the successor becomes effective.

Learning from delivery becomes evidence for N+1. When it reveals a material issue in N, recover that affected subtree. A single human's attention is the constraint: keep one main future slice in active definition unless there is a specific reason to increase it.

## 9. Change recovery

1. Record the trigger, affected rule/contract/outcome, and old baseline references.
2. Create a precise Wayfinder question, or record scoped fog until it becomes precise.
3. Follow reverse links through `depends_on`, acceptance references, contracts, and scope nodes. Mark the affected definitions and issues stale; explicitly block new execution or stop running affected work. Preserve unrelated approvals.
4. Resolve the question. Update current definitions, retain decision history, and write an ADR only for a significant costly-to-reverse trade-off.
5. Recompute acceptance coverage, dependencies, coordination, and appetite. Repeat the relevant gates through Readiness for impacted execution work.
6. Update/reissue affected issues with successor references and human approval. Preserve IDs where the same work remains; link replacements where scope fundamentally changes.

Stale records retain the reason and successor. Closing or relabeling an issue does not itself stop an external runner; the human must notify/control the actual implementation consumer through its normal mechanism.

## 10. State model

Documents: `draft → review → approved → stale → superseded/retired`. Revised stale content returns through draft/review; a new approval applies to its new revision. Approved history remains in version control.

Slices: `discovery → shaping → selected → defining → ready → implementing → complete`. Definition approval is recorded during `defining`; Readiness promotes to `ready`. Defer/stop are explicit side outcomes. Recovery returns affected work to the appropriate prior stage with a stale baseline marker.

Issues use lifecycle `open → in progress → review → done`, side outcomes `deferred`, `out of scope`, `superseded`, plus independent attributes `claimed/unclaimed` and `blocked/unblocked`. Approval readiness is a separate field. A claimed issue can also be blocked; labels must preserve that fact. Containers aggregate work rather than entering execution merely because they are open.

These distinctions refine the earlier shorthand state sequence: GitHub open/closed alone is insufficient to encode all concepts, and claim/block/readiness are not mutually exclusive lifecycle stages.

## 11. Small-change path and restart

A bounded change with an existing accepted outcome may reuse the brief, glossary, and established designs. Check that no new material decision, contract, trust boundary, migration, or substantial scope expansion appears. Assess documents, define focused behavior/examples, map the bounded issue, and record Definition/Readiness in one compact review. If any broader uncertainty appears, return to full discovery/slicing.

For a new session, read the brief, active slice, manifest, latest gate, and map index. Load detailed docs only for the next frontier item. End every session with changed artifacts, settled decisions, open blockers/fog, gate status, and the next valid manual invocation. This handoff supports continuity without reading an entire conversation.

## Completion standard

A slice is ready when its approved documents and candidate issue set account for outcome, scope/non-goals, behavior including relevant failures, applicable design/contracts/data/quality/operations, decisions and residual uncertainty, implementer discretion, verification, real dependencies, and the exact human-authorized execution set.

The handoff is complete when that set exists in GitHub with correct relationships and accessible baseline references. The overall workflow design remains a review draft until reviewed as a whole; a later small pilot supplies empirical validation.
