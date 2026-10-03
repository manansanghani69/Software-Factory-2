---
name: define-domain-model
description: Sharpen Project Definition System terminology, actors, relationships, states, invariants, and edge scenarios for one bounded scope.
---

# Define domain model

Use for one bounded domain-modeling session. Read [the operating contract](../project-definition-system/references/operating-contract.md), [the artifact handbook](../project-definition-system/references/artifact-handbook.md), [the glossary](../project-definition-system/references/terminology.md), and [the integration adapters](../project-definition-system/references/integration-adapters.md). Read existing project terminology, decisions, evidence, and relevant code for a feature change using the repository's discovery instructions.

## Work

1. Use the installed domain-modeling skill when available. Challenge overloaded or conflicting terms, choose canonical vocabulary, and keep the glossary free of implementation details.
2. Describe the in-scope actors, relationships, states, transitions, invariants, permissions, and edge scenarios in `DOMAIN.md` or the feature/slice definition. Compare claims with existing behavior where applicable.
3. Separate observed behavior, accepted rules, proposals, and uncertainty. Route each consequential unresolved rule to the relevant Wayfinder question or fog; do not declare it settled by drafting detail.
4. Offer an ADR only for a hard-to-reverse, surprising trade-off with real alternatives. Preserve stable IDs and links.

## Output and completion

Persist glossary changes, domain relationships/state rules, contradictions, edge scenarios, and affected definitions. Complete when terms in the current scope are consistent and relevant actors, states, and relationships are either described or linked to visible uncertainty.

End with the handoff template and a prepared manual continuation, such as `$define-journey-and-slice` when the broad journey is now ready, or `$define-wayfinder-chart` for a blocking question.
