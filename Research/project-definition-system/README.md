# Project Definition System

Approved design baseline: v1 · 2026-10-03

Workflow design approved. Skills are not yet implemented, and pilot validation is pending. The approved snapshot is identified by the Git tag `project-definition-v1`.

A manual workflow for turning an idea into approved definitions and implementation tickets. It serves one human decision-maker working with AI, and can accommodate a small team. It covers new projects and substantial changes to existing products.

The selected Delivery Slice becomes ready while the next slice is shaped in parallel. Completion means that implementation can proceed without inventing material product behavior, boundaries, contracts, acceptance conditions, or dependency order. Low-level implementation choices remain explicit discretion.

## Start here

1. Open [the visual walkthrough](./workflow.html). Choose a stage to see the human decisions, agent work, outputs, and exit condition.
2. Review [the operating workflow](./WORKFLOW.md) for gates, state, hierarchy, publication, and change recovery.
3. Review [the documentation handbook](./DOCUMENTATION.md) for structure, document selection, ownership, and writing rules.
4. Review [the manual skill specifications](./SKILL-SPECS.md) for how each session would run.
5. Use [the templates](./TEMPLATES.md) when applying the workflow later.

[CONTEXT.md](./CONTEXT.md) defines the language. [SOURCES.md](./SOURCES.md) records evidence and the synthesis. [ADR 0001](./docs/adr/0001-progressive-commitment.md) and [ADR 0002](./docs/adr/0002-artifact-authority-and-manual-control.md) preserve accepted structural choices.

## Current agreement

- GitHub Issues is the tracker. Repository documents carry durable definitions; GitHub carries live hierarchy, assignment, workflow state, and dependencies.
- Use two linked maps: a Wayfinder Decision Map and a Delivery Map. Decomposition and dependencies are separate relationships.
- Use four human gates: Intent, Slice, Definition, Readiness.
- Choose required documents through a change/risk assessment. Record deliberate skips.
- Use a manually invoked coordinator and stage skills. This packet specifies them; they are not installed skills.
- Review this system stage by stage. A small pilot project follows after the overall design looks good; no pilot was run for this draft.

## Boundary

This research lives independently of `Research/sandcastle/`. Its endpoint is an implementation handoff that any execution system can consume. Sandcastle is one possible consumer. This draft creates no GitHub Issues, installations, scheduled jobs, or production work.

## Review sequence

Start with Capture and Frame. Then review discovery/modeling, slicing, document selection, definition, mapping/readiness, and publication/recovery. Record adjustments in the applicable authoritative document. The walkthrough summarizes those documents; substantive changes should update both the source and its visible summary.

Before a later pilot, confirm the stage inputs/outputs, evidence thresholds, approval record, documentation structure, issue contract, and manual skill interfaces. Pilot feedback may change this draft.
