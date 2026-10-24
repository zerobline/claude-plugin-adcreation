#!/usr/bin/env python3
"""Deterministic QA for OpenAI-only Mastermind fixtures and package structure.
Does not execute ChatGPT skills, measure audiences, or independently assess creative quality.
"""
import json
import pathlib
import re
import unittest
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIX = ROOT / "tests" / "fixtures"

def load_svg(name):
    src = (FIX / name).read_text(encoding="utf-8")
    root = ET.fromstring(src)
    return src, root

class OpenAIPluginFixtureTests(unittest.TestCase):
    def test_manifest_and_openai_only(self):
        m = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(m["version"], "0.3.2")
        self.assertEqual(m["name"], "mastermind-ad-engine")
        self.assertIn("com.openai", m["extensions"])
        self.assertNotIn("screenshots", m["extensions"]["com.openai"]["interface"])
        self.assertLessEqual(len(m["extensions"]["com.openai"]["interface"]["defaultPrompt"]), 3)
        ui = m["extensions"]["com.openai"]["interface"]
        self.assertEqual(ui["category"], "Creativity")
        for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
            self.assertTrue(ui[field].startswith("https://"), field)
            self.assertLessEqual(len(ui[field]), 1024)
        for path in ("PRIVACY.md", "SUPPORT.md", "TERMS.md"):
            self.assertTrue((ROOT / path).exists(), path)
        self.assertFalse((ROOT / ".claude-plugin").exists())
        self.assertFalse((ROOT / "mcp.json").exists())

    def test_skill_entrypoints(self):
        for name in ["ad-blueprint", "quick-ad", "ad-critique", "ad-remix"]:
            with self.subTest(name=name):
                text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertTrue(text.startswith("---\n"), "Missing YAML frontmatter")
                self.assertIn("name: " + name, text.split("---", 2)[1])
                self.assertIn("description:", text.split("---", 2)[1])
        bp = (ROOT / "skills/ad-blueprint/SKILL.md").read_text(encoding="utf-8")
        for v in ["product-truth-and-symbol.md", "Final-render here", "Symbol Lock", "not independent", "not rendered"]:
            self.assertIn(v, bp)

    def test_case1_billboard(self):
        svg, root = load_svg("case1-billboard.svg")
        self.assertEqual(root.attrib["viewBox"], "0 0 2400 1200")
        self.assertEqual(root.attrib["data-visual"], "mirror-split")
        self.assertLessEqual(len(re.findall(r"[A-Za-z]+", root.attrib["data-copy"])), 7)
        self.assertNotIn("qr", svg.lower())
        sheet = (FIX / "case1-build-sheet.md").read_text(encoding="utf-8")
        for stage in ["Clarify", "Flip", "Write", "Design", "Tribe", "Platform", "Taste Test"]:
            self.assertIn(stage, sheet)
        self.assertIn("Product truth", sheet)

    def test_case2_human_poster(self):
        svg, root = load_svg("case2-human-poster.svg")
        self.assertEqual(root.attrib["viewBox"], "0 0 1200 1800")
        self.assertEqual(root.attrib["data-visual"], "human-moment")
        tags = [el.tag.rsplit("}", 1)[-1] for el in root.iter()]
        self.assertIn("ellipse", tags, "Missing person head")
        self.assertIn("path", tags, "Missing person silhouette")
        self.assertIn('fill="#ffb700"', svg, "Missing cup accent")
        self.assertNotIn("05:30", svg, "Inferred opening time")

    def test_case3_critique(self):
        c = (FIX / "case3-critique.md").read_text(encoding="utf-8")
        for v in ["not a supplied image", "subjective", "97%", "not blind", "no real campaign"]:
            self.assertIn(v.lower(), c.lower())

    def test_case4_true_two_by_two(self):
        records = {}
        for key in ["AA", "AB", "BA", "BB"]:
            _, root = load_svg("case4-" + key + ".svg")
            self.assertEqual(root.attrib["viewBox"], "0 0 1080 1350")
            records[key] = (root.attrib["data-copy"], root.attrib["data-visual"])
        self.assertEqual(records["AA"][0], records["AB"][0])
        self.assertEqual(records["BA"][0], records["BB"][0])
        self.assertNotEqual(records["AA"][0], records["BA"][0])
        self.assertEqual(records["AA"][1], records["BA"][1])
        self.assertEqual(records["AB"][1], records["BB"][1])
        self.assertNotEqual(records["AA"][1], records["AB"][1])

    def test_case5_platform_rebuild(self):
        svg, root = load_svg("case5-motorway.svg")
        self.assertEqual(root.attrib["viewBox"], "0 0 2400 1200")
        self.assertNotIn("qr", svg.lower())
        self.assertLessEqual(len(re.findall(r"[A-Za-z]+", root.attrib["data-copy"])), 7)
        self.assertNotIn("explanatory paragraph", svg.lower())

    def test_all_svg_no_external_code(self):
        for p in FIX.glob("*.svg"):
            with self.subTest(svg=p.name):
                src, _ = load_svg(p.name)
                self.assertNotIn("<script", src.lower())
                self.assertNotIn("<foreignObject", src)
                self.assertNotIn("href=", src)

if __name__ == "__main__":
    unittest.main(verbosity=2)
