# Manual skill specifications

First design draft · 2026-10-01. These are reviewable skill contracts and invocation examples, not registered or installed skills. Names beginning `define-` are proposed. Ordinary prompts can run the same process before skills exist.

## Shared contract

Each proposed skill is manually invoked. The coordinator is a router: it recommends a skill and gives a prepared invocation; the human starts that session. It cannot autonomously invoke user-only skills. Shared policy is reached through [WORKFLOW.md](./WORKFLOW.md), artifact content through [DOCUMENTATION.md](./DOCUMENTATION.md), and record shapes through [TEMPLATES.md](./TEMPLATES.md). Load only the relevant stage/branch references plus the project brief, active slice, map index, and latest gate.

Every stage returns: artifacts changed; settled decisions and evidence; open questions/fog; blocked prerequisites; approval status; and next valid manual invocation. Carry existing approvals across sessions at their recorded revisions. Ask only for missing decisions or changed evidence, not routine reconfirmation. A human decision cannot be manufactured by an AI interviewing itself.

Every stage preserves stable IDs and existing user content. Evidence retrieval is the agent's job. New artifacts start as drafts; a gate approval is recorded only from the human. Success means the completion criterion is satisfied, including meaningful omissions detected by the relevant manifest, rather than a template simply existing.

## define-next — coordinator

**Input:** project directory or project/slice issue URL and desired progress.

**Steps:** Read the current index/brief, active slice, gate records, manifests, and map summaries. Determine the last valid commitment and whether its prerequisites are current. Identify the next frontier or stage; flag contradictory or stale records. Recommend one manual invocation with its necessary inputs. If several independent decisions are available, show them with the dependency reasoning.

**Output:** current position, blocker explanation if any, prepared next prompt, and approval needed at the applicable gate.

**Complete when:** the human has one valid, actionable next step and can see why it is next.

**Boundary:** recommends; it does not cross gates, launch a pipeline, or publish issues merely because they are proposed.

**Example prompt:** “Using define-next, read docs/definition and identify the next valid action for S01.”

## define-capture

**Input:** raw idea/material and existing project records, if any.

**Steps:** Preserve the source request and its provenance. Normalize actors/problem/current situation without turning a proposed solution into an established need. Separate evidence, assumptions, contradictions, and questions. Classify the work as greenfield, substantial feature, or bounded change; identify existing artifacts to reuse.

**Output:** intake in the project brief, source index, work classification, and missing decisions for Frame.

**Complete when:** every supplied material is represented or linked, contradictions are visible, and no invented certainty replaces the raw request.

**Next:** define-frame.

## define-frame

**Input:** intake and source evidence.

**Steps:** Interview using grilling/domain-modeling practices. Resolve target actors, current problem, desired outcome and success signal, constraints, appetite, assumptions, and explicit exclusions. Retrieve environmental facts rather than asking the human to discover them. Offer a brief for human review and record the Intent Gate result.

**Output:** project brief and Intent Gate record.

**Complete when:** the human chooses a gate result against a coherent brief. A pass requires the Intent evidence in WORKFLOW.md; another result identifies the responsible next action.

**Next:** Wayfinder chart/domain modeling after pass; otherwise revise/spike/defer/stop.

## define-wayfinder-chart

**Input:** accepted project intent or selected slice, named next destination, GitHub repository, relevant map if one exists.

**Steps:** Read the installed Wayfinder skill and repository tracker instructions. Breadth-first interview the decision space. Distinguish precise questions from fog and excluded work. Propose the map and child tickets; publish planning/decision issues only within the explicitly invoked tracker scope. Create issues before wiring blockers, and link each decision to its affected node/document/gate. Use current Wayfinder chart and work modes; charting hand-resolves no tickets.

**Output:** project or slice Decision Map, precise tickets, blockers, scoped fog, and map URL.

**Complete when:** currently specifiable questions have one home and accurate relationships; the available frontier is visible.

**Next:** manually run Wayfinder work mode on the next frontier decision; domain-model or journey-and-slice when their inputs are available.

**Research handling:** investigations may run independently if the human invokes them. Nothing in this specification requires scheduled or automatic execution.

## define-domain-model

**Input:** brief, existing terminology, evidence, decisions, relevant existing code for feature work.

**Steps:** Use domain-modeling for canonical terms; keep CONTEXT.md a glossary. Put actors, relationships, state transitions, invariants, and edge scenarios in DOMAIN.md or feature definitions. Compare claims with existing behavior where applicable. Route unresolved consequential rules to Wayfinder rather than declaring them settled.

**Output:** glossary, domain model, contradictions/questions and affected definitions.

**Complete when:** terms in the current scope have consistent meanings and relevant actors/states/relationships are either described or linked to visible uncertainty.

**Next:** journey-and-slice or the blocking decision.

## define-journey-and-slice

**Input:** intent, broad domain/journey information, evidence and macro solution options.

**Steps:** Map the whole journey at broad resolution. Explore alternative actors, exceptions, and important risks. Sketch the macro solution, then propose coherent vertical slices. Attach outcomes, boundaries, exclusions, dependencies, evidence and appetite to each candidate. Compare the next candidates using structured human judgment. Record the selected slice and Slice Gate.

**Output:** journey map, broad Delivery Map, slice brief and selection evidence.

**Complete when:** the selected slice is coherent and independently verifiable, alternatives are visible, later work/fog remains visible, and the human chooses a gate result.

**Next:** document-manifest after pass.

## define-document-manifest

**Input:** Slice Gate approval, scope, relevant existing docs, actual change/risk profile.

**Steps:** Assess every dimension in DOCUMENTATION.md. Mark required, covered by an existing current artifact, or skipped with reason. Choose content depth, canonical location, owner, dependencies and approver. Combine sections when that reduces duplication. Split genuine shared contracts into their authoritative home.

**Output:** manifest, documentation index/handbook updates, drafting order.

**Complete when:** every dimension and mandatory information item is accounted for, including deliberate skips and current-artifact verification.

**Next:** slice-definition on the next unblocked artifact/rule.

## define-slice-definition

**Input:** selected boundary, manifest, resolved decisions, relevant authoritative drafts.

**Steps:** Work one coherent artifact or behavioral branch per session. Establish rules and concrete examples; inspect normal, failure, permission, state/time/order, and boundary cases as relevant. Draft applicable design, API/event, data, quality, and operational content. Route material unknowns to Wayfinder. Classify residual uncertainty and permitted discretion. Cross-check conflicting definitions and shared contracts. When all required content is current, assemble the Definition Gate evidence and seek the human judgment.

**Output:** feature/slice definitions, conditional artifacts, decision links, uncertainty classification, Definition Gate.

**Complete when:** the current branch satisfies its manifest criterion; the whole stage passes only after all required definitions agree and the human approves their revisions.

**Next:** another definition branch or Decision Ticket; delivery-map after Definition pass.

## define-delivery-map

**Input:** Definition Gate approval and authoritative rules/examples.

**Steps:** Decompose into meaningful nodes. Specify container/executable roles. Draft issues without inventing additional product behavior. Map every accepted example to executable work and integration acceptance. Add actual dependencies, coordinate shared resources, check for cycles, and identify overflow beyond GitHub nesting/width limits. Preserve stable IDs and link candidate work to its sources.

**Output:** scope-map revision, candidate ticket packet, acceptance coverage and execution order.

**Complete when:** each accepted example is covered, every proposed execution unit is bounded and verifiable, and dependency/continuation relationships are inspectable.

**Next:** readiness-review. If mapping exposes material ambiguity, return to slice-definition/Wayfinder.

## define-readiness-review

**Input:** candidate packet, manifest, Definition Gate approval and exact source revisions.

**Steps:** Review from a fresh implementer's perspective. Check definition currency, rule/example coverage, exclusions, discretion, applicable quality/contracts, dependency order, coordination, document access and residual risks. Report defects at their responsible layer. Have the human choose Readiness outcome against the packet identity/revision.

**Output:** readiness record with human/date, evidence, approved issue set or a bounded return path.

**Complete when:** every criterion is assessed and the human result is recorded; passing requires no unresolved material invention and a usable execution packet.

**Next:** github-publish after pass, otherwise revise/spike/defer/stop.

## define-github-publish

**Input:** explicit target repository, Readiness approval, candidate packet revision, existing planning issue ledger.

**Steps:** Follow WORKFLOW.md's publication protocol: reconcile stable IDs; verify access and source links; create approved issues; store URLs immediately; wire parents/blockers; read back all relationships; reconcile partial success; update bindings and handoff. Apply readiness separately from dependency blocking. Use explicit continuation links when required.

**Output:** GitHub hierarchy, actual blocker graph, binding ledger, handoff packet.

**Complete when:** every approved issue exists once with its correct role, source references, relationships, and status, and the handoff links are usable.

**Next:** implementation consumer; define-next for the following slice.

**Recovery:** interrupted publication resumes from the ledger and tracker lookup. Newly surfaced definition changes return through relevant gates; they are not silently inserted into approved issues.

## define-change-recovery

**Input:** new evidence/change request, baseline, affected scope/docs/issues.

**Steps:** Record trigger and current baseline; follow reverse trace links; mark affected artifacts/issues stale and control the affected implementation through its consumer. Resolve new uncertainty via Wayfinder. Update definitions and significant decision history. Recompute coverage/dependencies/appetite, repeat relevant gates, and update or supersede impacted work.

**Output:** impact record, successor definitions/approval, reconciled issues and restart guidance.

**Complete when:** all affected work is accounted for and either reauthorized at a current baseline, deferred, or explicitly stopped; unrelated approvals remain identifiable.

**Next:** the responsible definition stage until recovery passes, then implementation/next-slice shaping.

## Packaging decision for later implementation

Proposed skills would use manual invocation (`disable-model-invocation: true`) and human-facing descriptions. Shared reference files hold policy so it has one maintained home. The router recommends skills, and the human invokes them. Skill implementation and installation follow review of this packet; the later pilot evaluates session continuity, definition omissions, rework, traceability, and usefulness of ticket depth.
