---
name: define-next
description: Recommend the next valid manual action in an existing Project Definition System workspace from its current index, slice, gates, and frontier.
---

# Define next

Use this as the coordinator after a project-definition handoff or when the next stage is unclear. It recommends one bounded manual invocation; the human chooses and starts it.

Read [the operating contract](../project-definition-system/references/operating-contract.md) and [the artifact handbook](../project-definition-system/references/artifact-handbook.md). In the project workspace, read only the low-resolution definition index, current brief, active slice, latest gate records, manifest status, map summaries, and latest session handoff. Load detailed artifacts only when they are needed to prove the next frontier.

## Work

1. Identify the project/slice baseline and the latest valid human approval. Preserve unchanged approvals by revision.
2. Check the prerequisites and completion criteria for the current stage. Flag stale, contradictory, missing, or inaccessible records; do not repair them silently. Treat a handoff as incomplete when it does not provide exact paths or stable URLs plus revisions for the records and source documents needed by the next action.
3. Find the next frontier: the earliest unblocked stage or decision whose inputs are current. If independent frontiers exist, list them and explain their dependency trade-off.
4. Recommend exactly one preferred next action, with its skill name, bounded purpose, required inputs, relevant sources, expected artifact changes, and applicable human decision.

## Output

Report:

- current position and baseline;
- stale records, blockers, or missing evidence;
- why the preferred action is valid now;
- a ready-to-paste manual invocation for the human;
- the gate result or human input that the action must produce.

For the ready-to-paste invocation, list every required input as an exact path or
stable URL with its revision. If the project index or handoff only says “current
brief”, “existing docs”, or another unpinned label, report the continuity failure
and do not claim the next action is ready.

Use the [session handoff template](../project-definition-system/templates/session-handoff.md) for the continuation details. Do not write an approval, invoke another skill, create issues, schedule work, or publish a packet.

## Completion

Complete only when the human has one valid, actionable next invocation and can see the evidence and dependencies that make it next.

Common continuation shape:

```text
Run $<skill-name> for <project/slice>. Read <specific inputs>. Work on <one bounded branch>. Persist <artifacts>, record <gate or open questions>, and end with a session handoff naming the next valid manual invocation.
```
