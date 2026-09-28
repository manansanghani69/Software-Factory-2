# Sandcastle planning glossary

This glossary describes the planning domain. It intentionally avoids implementation details.

## Project

The complete effort being planned. A project may be greenfield or a bounded change to an existing product.

## Phase

A bounded delivery slice with an approved outcome, scope, documents, and implementation tickets. A phase should be a meaningful vertical slice rather than an arbitrary technical layer.

## Outcome

The measurable user or business result the work is intended to change. An outcome is the reason a phase exists.

## Capability

A durable ability the product or system must provide in order to achieve an outcome.

## Feature

A user-visible behavior or coherent slice of capability. A feature can contain stories and implementation tasks.

## Decision ticket

A ticket that resolves one question, investigation, or prerequisite. Research, prototype, grilling, and task tickets are decision-map work; they are not implementation work.

## Execution ticket

A ticket that describes approved implementation work. It is created only after the relevant phase passes the execution-readiness gate.

## Document

Durable evidence, behavior, design, contract, or decision record that explains what was agreed and why.

## Document manifest

The explicit list of documents required for a phase, including conditional documents that were considered and intentionally skipped.

## Scope map

The arbitrary-depth hierarchy that decomposes a project into phases, outcomes, capabilities, features, stories, and implementation tasks.

## Decision map

The Wayfinder index of unresolved questions and the decisions that make the route to the next phase clear.

## Fog of war

Known in-scope territory that cannot yet be phrased as a precise decision. Fog is recorded, not prematurely converted into tickets.

## Gate

An explicit approval boundary. This workflow has an outcome gate, a phase-scope gate, and an execution-readiness gate.

## Traceability

The ability to walk from an implementation ticket back through its acceptance criteria, documents, scope node, and outcome.

## Readiness

The state in which a phase has no hidden decisions required for implementation: its scope is approved, documents are present, behavior is testable, dependencies are ordered, and a human has approved the ticket set.

## Wayfinder

The decision-discovery layer. Wayfinder makes the route clear by resolving research, prototype, grilling, and prerequisite task tickets.

## Sandcastle

The implementation layer. Sandcastle executes approved implementation tickets and should not be responsible for inventing unresolved product behavior.
