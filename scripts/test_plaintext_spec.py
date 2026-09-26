#!/usr/bin/env python3
"""Tests for deterministic GAAM plain-text publication."""
from pathlib import Path
import importlib.util
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("generate_plaintext_spec", ROOT / "scripts" / "generate_plaintext_spec.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(module)


class PlainTextPublicationTests(unittest.TestCase):
    def test_strips_presentation_metadata_and_preserves_semantics(self):
        source = """---
title: Example
---
# Heading

{% include gaam-meta.html %}

**MUST** preserve [authority](https://example.test/authority).

## Table

| Claim | State |
|---|---|
| Authority | active |

```json
{"state":"active"}
```
"""
        rendered = module.markdown_to_text(source)
        self.assertNotIn("title: Example", rendered)
        self.assertNotIn("{% include", rendered)
        self.assertIn("Heading\n=======", rendered)
        self.assertIn("MUST preserve authority <https://example.test/authority>.", rendered)
        self.assertIn("| Claim | State |", rendered)
        self.assertIn('{"state":"active"}', rendered)

    def test_output_is_deterministic(self):
        source = "# A\n\nText with `code` and *emphasis*.\n"
        self.assertEqual(module.markdown_to_text(source), module.markdown_to_text(source))

    def test_repository_spec_contains_normative_identity(self):
        rendered = module.render()
        self.assertIn("Governance, Authority and Assurance Metamodel Specification", rendered)
        self.assertIn("Version: 0.9.0", rendered)
        self.assertIn("GAAM-AUTH-001", rendered)
        self.assertIn("GAAM-RED-008", rendered)

    def test_output_path_uses_semantic_baseline(self):
        self.assertEqual(module.output_path().name, "gaam-specification-v0.9.0.txt")

    def test_generated_artifact_round_trip(self):
        rendered = module.render()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "gaam.txt"
            path.write_text(rendered, encoding="utf-8", newline="\n")
            self.assertEqual(path.read_text(encoding="utf-8"), rendered)


if __name__ == "__main__":
    unittest.main()
