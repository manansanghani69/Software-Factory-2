#!/usr/bin/env python3
"""Validate the checked-in Project Definition System skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    print("Package validation requires Python 3 with PyYAML.", file=sys.stderr)
    raise SystemExit(1)


PACKAGE = Path(__file__).resolve().parents[1]
SKILLS_ROOT = PACKAGE.parent

EXPECTED = {
    "define-next": ("manual invocation", "define-"),
    "define-capture": ("intake", "define-frame"),
    "define-frame": ("Intent Gate", "define-wayfinder-chart"),
    "define-wayfinder-chart": ("Decision Map", "wayfinder"),
    "define-domain-model": ("glossary", "define-journey-and-slice"),
    "define-journey-and-slice": ("Slice Gate", "define-document-manifest"),
    "define-document-manifest": ("required", "define-slice-definition"),
    "define-slice-definition": ("Definition Gate", "define-delivery-map"),
    "define-delivery-map": ("candidate packet", "define-readiness-review"),
    "define-readiness-review": ("Readiness", "define-github-publish"),
    "define-github-publish": ("Readiness record", "define-next"),
    "define-change-recovery": ("stale", "define-"),
}

TEMPLATES = {
    "project-brief.md",
    "slice-definition.md",
    "feature-definition.md",
    "document-manifest.md",
    "gate-record.yaml",
    "delivery-map-record.yaml",
    "execution-issue.md",
    "decision-ticket.md",
    "publication-ledger.md",
    "session-handoff.md",
    "change-impact.md",
}

HANDOFF_FIELDS = {
    "Definition index:",
    "Active slice record:",
    "Current brief:",
    "Latest gate record:",
    "Active map/frontier index:",
    "Current document manifest:",
    "Existing source documents consulted:",
    "Required inputs for that invocation:",
}

SHARED_REFERENCES = {
    "references/operating-contract.md",
    "references/artifact-handbook.md",
    "references/terminology.md",
    "references/integration-adapters.md",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def frontmatter(text: str) -> str | None:
    match = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    return match.group(1) if match else None


def validate_manifest(errors: list[str]) -> None:
    path = PACKAGE / "manifest.yaml"
    if not path.is_file():
        return  # Missing resources are reported by main.
    try:
        manifest = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as error:
        fail(errors, f"invalid manifest YAML: {error}")
        return
    if not isinstance(manifest, dict):
        fail(errors, "manifest must be a YAML mapping")
        return
    expected_members = {
        "skills": set(EXPECTED),
        "shared_references": SHARED_REFERENCES,
        "templates": {f"templates/{name}" for name in TEMPLATES},
    }
    for field, expected in expected_members.items():
        members = manifest.get(field)
        if not isinstance(members, list) or any(not isinstance(item, str) for item in members):
            fail(errors, f"manifest {field} must be a list of strings")
            continue
        if len(members) != len(set(members)):
            fail(errors, f"manifest {field} contains duplicate entries")
        for missing in sorted(expected - set(members)):
            fail(errors, f"manifest {field} missing: {missing}")
        for unexpected in sorted(set(members) - expected):
            fail(errors, f"manifest {field} unexpected: {unexpected}")


def markdown_prose(text: str) -> str:
    """Exclude fenced examples from link and heading checks."""
    lines = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= fence[1] and not match.group(2).strip():
                fence = None
        elif match:
            fence = (match.group(1)[0], len(match.group(1)))
        else:
            lines.append(line)
    return "\n".join(lines)


def heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    for heading in re.findall(r"^ {0,3}#{1,6}\s+(.+)$", markdown_prose(text), flags=re.MULTILINE):
        heading = re.sub(r"\s+#+\s*$", "", heading)
        slug = re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")
        anchor = slug
        suffix = 0
        while anchor in anchors:
            suffix += 1
            anchor = f"{slug}-{suffix}"
        anchors.add(anchor)
    return anchors


def validate_markdown_links(path: Path, text: str, errors: list[str]) -> None:
    """Check local inline Markdown links and heading fragments used by this bundle."""
    for target in re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", markdown_prose(text)):
        target = target.strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        target_path = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        label = path.relative_to(SKILLS_ROOT)
        if not target_path.is_file():
            fail(errors, f"{label}: unresolved reference {target}")
        elif parsed.fragment:
            if unquote(parsed.fragment) not in heading_anchors(target_path.read_text(encoding="utf-8")):
                fail(errors, f"{label}: unresolved anchor {target}")


def main() -> int:
    errors: list[str] = []

    for required in (
        PACKAGE / "PACKAGE.md",
        PACKAGE / "manifest.yaml",
        *(PACKAGE / name for name in sorted(SHARED_REFERENCES)),
    ):
        if not required.is_file():
            fail(errors, f"missing package resource: {required.relative_to(SKILLS_ROOT)}")

    actual_templates = {path.name for path in (PACKAGE / "templates").glob("*") if path.is_file()}
    for template in sorted(TEMPLATES - actual_templates):
        fail(errors, f"missing template: {template}")

    handoff = PACKAGE / "templates/session-handoff.md"
    if handoff.is_file():
        handoff_text = handoff.read_text(encoding="utf-8")
        for field in sorted(HANDOFF_FIELDS):
            if field not in handoff_text:
                fail(errors, f"session-handoff.md: missing restart navigation field {field!r}")

    validate_manifest(errors)

    for skill_name, (marker, next_marker) in EXPECTED.items():
        skill_dir = SKILLS_ROOT / skill_name
        skill_file = skill_dir / "SKILL.md"
        metadata_file = skill_dir / "agents/openai.yaml"
        if not skill_file.is_file():
            fail(errors, f"missing skill: {skill_name}/SKILL.md")
            continue
        if not metadata_file.is_file():
            fail(errors, f"missing metadata: {skill_name}/agents/openai.yaml")

        text = skill_file.read_text(encoding="utf-8")
        fm = frontmatter(text)
        if fm is None:
            fail(errors, f"{skill_name}: missing YAML frontmatter")
        else:
            name_match = re.search(r"^name:\s*(\S+)\s*$", fm, flags=re.MULTILINE)
            description_match = re.search(r"^description:\s*.+$", fm, flags=re.MULTILINE)
            if not name_match or name_match.group(1) != skill_name:
                fail(errors, f"{skill_name}: frontmatter name mismatch")
            if not description_match:
                fail(errors, f"{skill_name}: missing frontmatter description")
            if "disable-model-invocation" in fm:
                fail(errors, f"{skill_name}: uses deprecated disable-model-invocation metadata")

        if marker.lower() not in text.lower():
            fail(errors, f"{skill_name}: missing stage marker {marker!r}")
        if next_marker.lower() not in text.lower():
            fail(errors, f"{skill_name}: missing next-action marker {next_marker!r}")
        for required_phrase in ("handoff", "operating contract", "manual"):
            if required_phrase.lower() not in text.lower():
                fail(errors, f"{skill_name}: missing bounded-session phrase {required_phrase!r}")

        if metadata_file.is_file():
            metadata = metadata_file.read_text(encoding="utf-8")
            try:
                parsed = yaml.safe_load(metadata)
            except yaml.YAMLError as error:
                fail(errors, f"{skill_name}: invalid openai.yaml: {error}")
            else:
                policy = parsed.get("policy") if isinstance(parsed, dict) else None
                if not isinstance(policy, dict) or policy.get("allow_implicit_invocation") is not False:
                    fail(errors, f"{skill_name}: policy.allow_implicit_invocation must be YAML boolean false")
            if "disable-model-invocation" in metadata:
                fail(errors, f"{skill_name}: deprecated invocation key in openai.yaml")

    owned_roots = [PACKAGE, *(SKILLS_ROOT / skill_name for skill_name in EXPECTED)]
    for owned_root in owned_roots:
        for path in owned_root.rglob("*"):
            if not path.is_file() or path.name == "validate_package.py" or "__pycache__" in path.parts:
                continue
            content = path.read_text(encoding="utf-8", errors="replace")
            if path.suffix == ".md":
                validate_markdown_links(path, content, errors)
            if "/Users/" in content or "Research/project-definition-system" in content:
                fail(errors, f"non-portable or unpublished research path in {path.relative_to(SKILLS_ROOT)}")

    if errors:
        print("Project Definition System package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Project Definition System package valid: {len(EXPECTED)} skills, {len(TEMPLATES)} templates")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
