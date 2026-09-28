# ADR 0001: Decision-first inception before Sandcastle execution

- **Status:** Accepted
- **Date:** 2026-09-28
- **Scope:** Sandcastle project-planning workflow

## Context

Sandcastle is effective at implementing, reviewing, and sequencing work, but implementation machinery is not a substitute for product and system decisions. Starting from loosely described issues forces the implementation agent to discover scope, behavior, contracts, and dependencies while it is already changing the codebase.

The existing Wayfinder pattern is strong at making a route visible through decision tickets, but its map is not itself a complete project-inception model. A reliable workflow needs to support greenfield projects, arbitrary-depth scope maps, risk-based documentation, rolling phases, and a clean handoff into implementation.

## Decision

Use a decision-first workflow with two connected maps:

1. A **Wayfinder decision map** resolves research, prototype, grilling, and prerequisite task tickets. It records decisions and honest fog of war.
2. A **scope map** decomposes approved work to arbitrary depth: project, phase, outcome, capability, feature, story, and implementation task.

The workflow creates a mandatory core document set and selects conditional artifacts through a change-dimension checklist. Human approval is required at the outcome, phase-scope, and execution-readiness gates.

Implementation tickets are created only after the next phase is execution-ready. The repository scope map remains the canonical hierarchy; an issue tracker is a projection of that map and must not erase intermediate levels.

When an approved decision changes, affected documents and tickets become stale, the impacted subtree is stopped, and the decision map is reopened or extended. Unrelated work can continue.

## Consequences

### Positive

- Sandcastle receives implementation work with explicit scope, behavior, acceptance, and dependencies.
- Future phases can be shaped in parallel without pretending that unresolved decisions are settled.
- Arbitrary-depth planning does not depend on issue-tracker nesting capabilities.
- Document creation is proportional to risk instead of being a fixed ceremony.
- Changes can be traced and recovered without silently rewriting history.

### Costs

- Work begins with more deliberate discovery and review.
- The repository needs a canonical scope map and document index.
- Humans must explicitly approve the three gates.
- The workflow must maintain links between decisions, documents, scope nodes, and tickets.

## Alternatives considered

### Let Sandcastle discover requirements during implementation

Rejected. This mixes product decisions with code changes, makes acceptance ambiguous, and causes parallel tickets to encode conflicting assumptions.

### Create a fixed document set for every project

Rejected. Some projects need API, design, migration, security, or operations artifacts; others do not. A conditional manifest records both required and deliberately skipped documents.

### Use only the issue tracker as the hierarchy

Rejected. Tracker nesting is not guaranteed to support the required depth, and a tracker is a poor canonical store for durable planning context.

### Fully specify every future phase before implementation begins

Rejected. It creates stale plans and delays value. Rolling phases preserve direction while allowing later decisions to use what was learned earlier.
