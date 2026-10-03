# Project Definition System skill package

This package contains the manually invoked Project Definition System coordinator and stage skills.

The skills are the sibling `define-*` directories under `.agents/skills/`. The portable shared bundle in this directory is their single maintained runtime source for policy, terminology, integration adapters, and record templates.

## Package contents

- `references/operating-contract.md`: stages, gates, bounded-session rules, state model, recovery, and publication boundaries.
- `references/artifact-handbook.md`: artifact authority, metadata, mandatory information, writing rules, and session restart reads.
- `references/terminology.md`: the Project Definition System glossary.
- `references/integration-adapters.md`: adapters for Wayfinder, grilling, and domain-modeling, with safe fallbacks when a capability is unavailable.
- `templates/`: portable starter records for project artifacts and handoffs.
- `scripts/validate_package.py`: deterministic package validation.
- `scripts/test_validate_package.py`: relocated-bundle, invocation-policy, manifest, and reference regression checks.

Validation requires Python 3 with PyYAML, as does the official skill-creator quick validator. From the repository root, run `python3 .agents/skills/project-definition-system/scripts/validate_package.py` and `python3 .agents/skills/project-definition-system/scripts/test_validate_package.py`. The package validator checks only this bundle and its twelve owned skills, so unrelated skills in the destination root do not affect its result. It checks parsed manifest membership and local inline Markdown links/heading anchors across owned Markdown files, excluding fenced examples. These structural checks do not prove stage behavior; skill use remains manual.

Install later by copying the complete `.agents/skills/` package contents into the target repository or user skills root. Keep the `define-*` directories beside `project-definition-system/`; their relative reference links are intentionally resolved within that bundle. This step does not install the skills globally.
