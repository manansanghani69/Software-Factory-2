#!/usr/bin/env python3
"""Regression checks for validation in a relocated skills bundle."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


SKILLS_ROOT = Path(__file__).resolve().parents[2]


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.skills = Path(self.temporary.name) / "skills"
        package = SKILLS_ROOT / "project-definition-system"
        manifest = yaml.safe_load((package / "manifest.yaml").read_text())
        for name in [package.name, *manifest["skills"]]:
            shutil.copytree(SKILLS_ROOT / name, self.skills / name, ignore=shutil.ignore_patterns("__pycache__"))
        self.validator = self.skills / "project-definition-system/scripts/validate_package.py"
        self.metadata = self.skills / "define-next/agents/openai.yaml"

    def validate(self):
        return subprocess.run(
            [sys.executable, str(self.validator)],
            cwd=self.temporary.name,
            capture_output=True,
            text=True,
        )

    def test_relocated_bundle_passes(self):
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_unrelated_skill_does_not_affect_validation(self):
        unrelated = self.skills / "unrelated-skill"
        unrelated.mkdir()
        # An unrelated skill's local references are outside this package's scope.
        (unrelated / "NOTES.md").write_text("/" + "Users/example/local-resource\n")
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_policy_must_be_a_yaml_boolean_false(self):
        cases = {
            "true with misleading comment": "policy:\n  allow_implicit_invocation: true # allow_implicit_invocation: false\n",
            "quoted false": 'policy:\n  allow_implicit_invocation: "false"\n',
            "misplaced policy": "interface:\n  policy:\n    allow_implicit_invocation: false\n",
            "missing policy": "interface: {}\n",
            "nonmapping policy": "policy: []\n",
            "nonmapping metadata": "[]\n",
            "invalid YAML": "policy: [\n",
        }
        for label, content in cases.items():
            with self.subTest(label=label):
                self.metadata.write_text(content)
                result = self.validate()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("define-next:", result.stdout)
                self.assertNotIn("Traceback", result.stderr)

    def test_owned_nonportable_reference_is_still_rejected(self):
        (self.skills / "define-next/NOTES.md").write_text("/" + "Users/example/local-resource\n")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("define-next/NOTES.md", result.stdout)

    def test_shared_markdown_missing_file_is_rejected(self):
        reference = self.skills / "project-definition-system/references/integration-adapters.md"
        with reference.open("a") as stream:
            stream.write("\n[Missing source](missing-source.md)\n")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("integration-adapters.md", result.stdout)
        self.assertIn("missing-source.md", result.stdout)

    def test_missing_anchors_are_rejected_in_shared_and_skill_files(self):
        cases = {
            "project-definition-system/templates/session-handoff.md": "#missing-heading",
            "define-next/SKILL.md": "../project-definition-system/references/operating-contract.md#missing-heading",
        }
        for relative, target in cases.items():
            with self.subTest(relative=relative):
                path = self.skills / relative
                original = path.read_text()
                path.write_text(original + f"\n[Missing section]({target})\n")
                result = self.validate()
                path.write_text(original)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("missing-heading", result.stdout)

    def test_duplicate_heading_anchor_passes_and_fenced_heading_is_not_a_target(self):
        template = self.skills / "project-definition-system/templates/session-handoff.md"
        with template.open("a") as stream:
            stream.write("\n## Resume\n\n## Resume\n\n[Second heading](#resume-1)\n")
            stream.write("\n```markdown\n## Example only\n```\n")
        result = self.validate()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        with template.open("a") as stream:
            stream.write("\n[Fenced heading](#example-only)\n")
        result = self.validate()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("example-only", result.stdout)

    def test_manifest_requires_parsed_resource_membership(self):
        path = self.skills / "project-definition-system/manifest.yaml"
        original = yaml.safe_load(path.read_text())
        cases = {
            "commented skill": yaml.safe_dump({**original, "skills": original["skills"][1:]}) + "#  - define-next\n",
            "duplicate skill": yaml.safe_dump({**original, "skills": original["skills"] + ["define-next"]}),
            "unexpected skill": yaml.safe_dump({**original, "skills": original["skills"] + ["unknown-skill"]}),
            "missing reference": yaml.safe_dump({**original, "shared_references": original["shared_references"][1:]}),
            "missing template": yaml.safe_dump({**original, "templates": original["templates"][1:]}),
            "wrong list type": yaml.safe_dump({**original, "templates": "not-a-list"}),
            "nonstring member": yaml.safe_dump({**original, "skills": [None]}),
            "nonmapping manifest": "[]\n",
            "invalid YAML": "skills: [\n",
        }
        for label, content in cases.items():
            with self.subTest(label=label):
                path.write_text(content.replace("\n- ", "\n  - "))
                result = self.validate()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("manifest", result.stdout)
                self.assertNotIn("Traceback", result.stderr)

    def test_session_handoff_requires_restart_navigation_fields(self):
        template = self.skills / "project-definition-system/templates/session-handoff.md"
        original = template.read_text()
        required = (
            "Definition index:",
            "Active slice record:",
            "Current brief:",
            "Latest gate record:",
            "Active map/frontier index:",
            "Current document manifest:",
            "Existing source documents consulted:",
            "Required inputs for that invocation:",
        )
        for label in required:
            with self.subTest(label=label):
                template.write_text(original.replace(label, ""))
                result = self.validate()
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                self.assertIn("session-handoff.md", result.stdout)
        template.write_text(original)


if __name__ == "__main__":
    unittest.main()
