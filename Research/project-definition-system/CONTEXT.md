# Project Definition System glossary

The language of the manual process that makes a project or substantial change ready for implementation.

## Intent and scope

**Project**: The complete effort under definition, including its intended outcomes and scope boundaries. It may be a new product or a substantial change to an existing product.

**Outcome**: A measurable change in a user's or business's situation that justifies the work. It belongs to a project or Delivery Slice rather than being a unit of implementation work.

**Planning Stage**: A bounded step in the definition process with inputs, outputs, and an exit condition.
_Avoid_: Phase when referring to a process step

**Delivery Slice**: A bounded vertical portion of a project with its own outcome, scope, definition, and acceptance conditions. It can become ready while later slices are still being shaped.
_Avoid_: Phase when referring to a delivery portion

**Capability**: A durable ability the product or system provides in support of an outcome.

**Feature**: A coherent part of a capability with identifiable user-visible or system-visible behavior.

**Story**: An independently understandable behavioral portion of a feature, with rules and concrete acceptance examples.

**Task**: A bounded piece of implementation work serving a Story or another approved scope node.

**Subtask**: A smaller piece of implementation work within a Task. Further decomposition may exist when it adds useful meaning.

**Appetite**: The amount of time, cost, or complexity the human is willing to invest in a selected slice. It is a constraint on selection rather than a prediction of effort.

## Maps and uncertainty

**Decision Map**: An index of questions and decisions that makes the route to a named destination visible.

**Delivery Map**: The decomposition of intended and approved work into meaningful scope nodes, with slice boundaries and links to definitions.

**Scope Node**: An identifiable element in the Delivery Map, with one decomposition parent and potentially several dependencies.

**Decision Ticket**: A precise question or investigation whose resolution advances the Decision Map. It may involve research, a prototype, conversation, or prerequisite work.

**Container Issue**: An issue representing a scope grouping and progress, rather than executable implementation work.

**Execution Issue**: An issue authorizing a defined unit of implementation work with acceptance conditions and verification guidance.

**Frontier**: The unresolved decisions whose prerequisites are settled and that are available to be worked on now.

**Fog**: Recognized in-scope uncertainty that cannot yet be stated as a precise decision question.

**Implementation Discretion**: An explicitly allowed choice that implementers can make without changing approved material behavior, scope, contracts, or acceptance conditions.

**Spike**: A bounded investigation or disposable experiment with a precise learning question and an exit condition.

## Definitions and approvals

**Document Manifest**: The assessment of required artifacts for a slice, including deliberately skipped artifacts and their reasons.

**Gate**: A human decision boundary authorizing the next commitment based on linked evidence.

**Baseline**: An approved version of the selected scope and its definitions. Material changes require an explicit review of their impact.

**Material Change**: A change to outcomes, boundaries, product behavior, contracts, acceptance, significant constraints, or consequential dependency order.

**Definition Complete**: The state in which a selected slice has approved material behavior and boundaries, with residual uncertainty classified explicitly.

**Readiness**: The state in which an approved definition has a coherent, traceable, verifiable implementation issue set and usable dependency order.

**Readiness Record**: The evidence, human approval, document revisions, and candidate issue set authorizing implementation for a slice.

**Stale**: Content or work whose former approval no longer applies because a prerequisite changed.

**Traceability**: The ability to follow an execution issue through its acceptance examples, authoritative definition, scope node, and intended outcome, and to find affected work in the reverse direction.
