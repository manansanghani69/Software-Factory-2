---
schema_version: 1
id: ADR-0001
title: Separate decision history from current contracts
type: adr
status: accepted
authority: informative
owner: project-owner
reviewers: []
last_reviewed: null
implementation_alignment:
  state: not-applicable
  checked_at: null
  checked_ref: null
implementation_refs: []
evidence_refs:
  - ../specifications/decision-workflow/decision-record.md
related_docs:
  - ../architecture/documentation-contract.md
  - ../capabilities/specification-discovery.md
related_decisions: []
supersedes: []
---

# Separate decision history from current contracts

GitHub holds the Wayfinder map and historical decision resolutions; versioned repository documents hold the current product contracts, with a small manifest linking each initiative's package. The user selected GitHub in Q13 and accepted the package/write-through/ownership rules in Q12 and Q21–Q25.

The alternatives were a local canonical tracker, one large specification issue, or a map that also stored all current requirements. GitHub keeps the collaborative decision journey visible, while canonical documents give each assertion a stable home. This costs explicit links and reconciliation between two systems; the [change protocol](../operations/specification-change-control.md) specifies that work.

Accepted records preserve the reasoning for a historical choice. Changing current intent updates canonical documents and preserves successor links, so an old issue answer does not silently outrank a newer approved contract. The accepted status records this particular choice; it does not activate the whole workflow specification.
