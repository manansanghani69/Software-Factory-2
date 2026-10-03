---
name: define-wayfinder-chart
description: Chart a bounded Wayfinder Decision Map for a project or slice, making precise questions, fog, blockers, and the available frontier visible.
---

# Define Wayfinder chart

Use for one bounded charting session, not for resolving a ticket. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), [the integration adapters](../project-definition-system/references/integration-adapters.md), and the [decision-ticket template](../project-definition-system/templates/decision-ticket.md). Read the installed Wayfinder skill and repository tracker instructions when available.

## Work

1. Load the accepted intent or slice, name the map destination, and read any existing map at low resolution. Keep the map small enough to orient a fresh session.
2. Breadth-first, identify currently precise questions, vague in-scope fog, exclusions, prerequisites, and the first available frontier. Do not pre-slice fog into invented tickets.
3. Create or update the Decision Map and direct child tickets within the explicitly authorized tracker scope. Each ticket has one precise question, impact links to scope/document/gate, evidence needed, type, and real blockers. Create tickets before wiring blockers.
4. Keep decomposition separate from decision questions. Link affected definitions and gates; do not treat a decision ticket as execution authorization.
5. Report the next frontier and a prepared manual invocation for one decision session. Apply the [Wayfinder adapter's manual research boundary](../project-definition-system/references/integration-adapters.md#wayfinder) to map Notes and continuations. A later session resolves at most one decision ticket; research exceptions require explicit human invocation.

## Output and completion

Persist the map, precise tickets, blocker edges, scoped fog, exclusions, and source links. Complete when every currently specifiable question has one home and accurate relationships, and the available frontier is visible. Charting hand-resolves no ticket and crosses no human gate.

End with a handoff naming the next valid manual invocation, for example:

```text
Run $wayfinder on <map URL or local map>. Resolve only <one ticket name>. Read its evidence links, record the human decision in the resolution, update the authoritative definition, and return with a session handoff.
```
