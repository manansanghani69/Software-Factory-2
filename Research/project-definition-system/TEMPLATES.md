# Record templates

These are unfilled shapes for future use. Examples are explanatory fragments, not a test project. Adapt file boundaries using DOCUMENTATION.md.

## Project brief

```markdown
# Project <ID>: <name>
## Intake and provenance
Raw request, source links, contradictions, work classification.
## Actors and present situation
Who experiences what problem? Current baseline and supporting evidence.
## Intended outcome
Outcome ID, success signal, baseline, measurement conditions.
## Appetite and constraints
Human's acceptable investment; dependencies and restrictions.
## Scope direction and explicit non-goals
## Evidence, assumptions, and open questions
Each consequential assumption has an owner, evidence need, or decision link.
## Intent Gate
Link to the judgment and approved revision.
```

## Slice definition

```markdown
# <S01>: <name>
## Outcome and why this slice now
Value, evidence, appetite, risk, opportunity cost, alternatives.
## Included journey and scope nodes
One coherent vertical user/system outcome.
## Explicit exclusions and later options
## Macro solution and prerequisite contracts
## Authoritative definitions
Feature/rule/example IDs and approved revision references.
## Residual uncertainty
Resolved | implementation discretion | spike | deferred | out of scope
Every entry includes a reason and affected scope.
## Allowed implementation discretion
Choices and constraints; material changes return to definition.
## Gate references
Slice, Definition, Readiness judgments.
```

## Feature definition and acceptance

```markdown
# <feature ID>: <name>
## Purpose, actors, and scope
## Permissions and states
## Rules
### RULE-01: <observable requirement>
Preconditions, observable behavior/side effects, exceptions.
## Examples
| ID | Rule | Starting state / input | Action | Expected observation |
| --- | --- | --- | --- | --- |
| EX-01 | RULE-01 | Normal case | ... | ... |
| EX-02 | RULE-01 | Failure/denied case | ... | ... |
| EX-03 | RULE-01 | Boundary case | ... | ... |
## Applicable contracts/design/data/quality
Authoritative links. Include constraints and proof methods.
## Questions and decisions
Wayfinder links; approved answers appear as current rules above.
## Implementation discretion
## Baseline / slice applicability
```

For example, an invitation feature might have a rule “An expired invitation cannot be accepted.” A boundary example must define what happens exactly at expiry. The workflow must ask/resolve that decision; it cannot infer it from the adjective “expired.”

## Manifest

```markdown
# Document manifest: <S01>
Scope revision: <commit/snapshot>
| Dimension | Artifact / section | Required / existing / skipped | Reason | Owner | Prerequisites | Evidence / status |
| --- | --- | --- | --- | --- | --- | --- |
One row per dimension from DOCUMENTATION.md, plus mandatory content.
```

## Gate / readiness record

```yaml
gate: intent | slice | definition | readiness
scope: S01
outcome: pass | revise | spike | defer | stop
human: <name>
date: <timestamp>
approved_artifacts:
  - id: FEAT-01-SPEC
    revision: <commit-or-immutable-snapshot>
packet: <candidate-packet-ID-and-revision-or-null>
reasons: []
residual_risks_accepted: []
conditions_or_return_path: []
authorized_next_work: <scope-of-authorization>
supersedes_approval: <prior-record-or-null>
published_issue_bindings: []
publication_status: not-started | partial | verified
```

Readiness adds an inspected checklist: document currency/manifest, coverage, material questions, discretion, dependencies/cycles/coordination, proof methods, document access, and exact candidate set. `pass` requires human approval; publishing URLs complete the binding without changing the authorized semantics.

## Delivery Map record

```yaml
id: STORY-01
name: <readable name>
kind: story
parent: FEAT-01
delivery_slice: S01
outcome: OUT-01
execution_role: executable
source_docs: [FEAT-01-SPEC]
acceptance_refs: [EX-01, EX-02]
depends_on: [TASK-PREREQUISITE]
github_issue: null
logical_parent: null
baseline_revision: <approved-revision>
```

Before publication the candidate map owns proposed parentage. After publication GitHub owns live native parentage; the repository preserves approved scope and URL bindings. `logical_parent` is populated only for an explicit continuation beyond native limits.

## Execution issue

```markdown
# [WORK-ID] <readable title>
Type: execution · Role: executable · Slice: S01 · Parent: <title/link>
Definition baseline: <approved revision links>
Readiness: <record/link> · Source rules/examples: <links>

## Objective
Outcome and the bounded behavior this unit contributes.
## Scope and exclusions
## Behavior and relevant constraints
Short issue-specific summary; link full authoritative definitions.
## Acceptance
- [ ] <observable condition referencing EX-01>
- [ ] <failure/boundary condition referencing EX-02>
- [ ] <integration/quality condition where relevant>
## Validation and completion evidence
Meaningful check(s), expected result, integration/release proof as applicable.
## Dependencies and coordination
Actual native blockers; shared resource coordination if relevant.
## Implementation discretion
Permitted choices and constraints.
```

A container issue lists outcome, scope, children, definition/gate links, and integration acceptance. It is explicitly marked `container` and is not assigned as a duplicate execution unit.

## Decision ticket extension

Keep the installed Wayfinder question shape; add links where necessary:

```markdown
## Question
<one precise question>
## Impact
Affected slice, scope node, document, and gate.
## Evidence needed
Source research, prototype, scenario, or human judgment.
```

Resolution stays in the Wayfinder resolution comment; the current behavior goes into its authoritative definition. The map holds a linked one-line gist rather than repeating the resolution.

## Publication ledger

```markdown
Approved packet: <ID/revision> · Repository: <owner/repo>
| Stable work ID | GitHub URL | Role | Native parent | Logical continuation | Blockers verified | Source links verified |
| --- | --- | --- | --- | --- | --- | --- |
```

## Session handoff

```markdown
Scope / slice:
Artifacts changed:
Settled decisions and evidence:
Open frontier / fog:
Stale records or blocking prerequisites:
Latest valid gate and approved revisions:
Next valid manual invocation and its inputs:
```

## Change impact record

```markdown
Trigger and evidence:
Old baseline:
Material rule/contract/outcome affected:
Impacted documents/issues via reverse links:
Affected execution stopped/blocked through consumer:
Wayfinder question or fog:
Successor definitions:
Gates to repeat and their results:
Updated/superseded issue bindings:
Restart authorization:
```
