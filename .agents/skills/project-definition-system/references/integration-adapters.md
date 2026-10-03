# Integration adapters

These adapters preserve the approved workflow without making the package depend on an unpublished research path or on a previous chat.

## Wayfinder

When the installed `wayfinder` skill is available, read and use it for Decision Map/chart/work behavior and its repository tracker instructions. Keep one destination per map, direct child decision tickets, native blockers, claims, frontier, fog, and resolution comments. The Project Definition System adds links from each question to affected scope, document, and gate; it does not rewrite Wayfinder's tracker mechanics.

The Project Definition System's manual-control contract overrides Wayfinder's automatic research-dispatch step. Charting records research tickets and returns prepared manual invocations; it does not launch research subagents. Independent investigations, including parallel research, require the human to explicitly invoke them. Carry this boundary into the map's Notes and every prepared Wayfinder continuation so a fresh work session retains it.

If Wayfinder is unavailable, record the same map and ticket fields in the repository's approved local tracker or Markdown records, clearly mark the fallback, and leave a precise manual continuation. Do not invent tracker APIs, issue URLs, or automatic publication.

## Grilling

When the installed `grilling` skill is available, use it for human decisions: ask the whole current decision frontier, give a recommendation, wait for answers, and recompute the frontier. Retrieve environmental facts yourself. Never simulate the human's gate approval or resolution.

If it is unavailable, ask only the currently blocking decision questions in the same explicit format and stop for the human response. Preserve every answer in the authoritative artifact and gate record.

## Domain modeling

When the installed `domain-modeling` skill is available, use it for canonical terms, edge scenarios, glossary updates, and sparse ADRs. Keep the glossary free of implementation details. Cross-check existing behavior where a codebase exists, and route consequential unresolved rules to Wayfinder.

If it is unavailable, apply the same glossary/domain/ADR separation from `artifact-handbook.md`; do not invent a replacement skill or claim a term is settled without human evidence.

## GitHub and manual control

An explicit `define-wayfinder-chart` invocation may create/update a Decision Map, decision tickets, and their live relationships only within the human's named repository/tracker and planning scope. These issues authorize decision work, never implementation. Without that authority, retain local drafts and a manual continuation.

An explicit `define-github-publish` invocation may publish a named planning-only packet of containers before Readiness. Mark them as containers in definition with no execution authorization. A packet containing executable work requires a passing Readiness record for its exact revision before publication or promotion of any existing planning issue to executable work.

An explicit `define-change-recovery` invocation may mark affected live issues stale/blocked and reconcile or supersede them within its authorized tracker scope. Reauthorizing affected execution requires the relevant gates through Readiness. Other stage skills draft issues and relationships locally.

Repository sharing/pushing follows the separately authorized project workflow. No stage invocation schedules jobs, starts implementation, or launches automatic orchestration. A manual recommendation is not an invocation.
