---
schema_version: 1
id: ADR-0002
title: Separate approved intent from implementation evidence
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
  - ../operations/specification-change-control.md
related_decisions: []
supersedes: []
---

# Separate approved intent from implementation evidence

Normative documents describe intended behavior, while code and tests supply evidence of implemented behavior at a known revision. Approval status and implementation alignment remain separate. The user accepted this distinction in Q6, Q17, and Q33.

Treating code as the sole authority would turn defects into requirements; treating every active document as an implemented fact would misrepresent approved future work. The chosen model supports unimplemented, partial, aligned, drifted, unknown, and not-applicable assessments, at the cost of explicit evidence and divergence handling.

The [documentation contract](../architecture/documentation-contract.md) owns assessment semantics. The [change protocol](../operations/specification-change-control.md) owns how divergence is resolved. Neither a recent review date nor a test path alone proves alignment or deployment.
