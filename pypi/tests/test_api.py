import unittest

import text_effect_prompts as tep
from text_effect_prompts.__main__ import main


class ApiTest(unittest.TestCase):
    def test_counts_match_stats(self):
        self.assertEqual(len(tep.all_styles()), tep.stats()["published"])
        self.assertTrue(tep.categories())

    def test_get_by_id_and_slug(self):
        s = tep.all_styles()[0]
        self.assertIs(tep.get(s["id"]), s)
        self.assertIs(tep.get(s["slug"].upper()), s)
        self.assertIsNone(tep.get("no-such-style"))

    def test_prompt_fills_placeholder(self):
        s = tep.all_styles()[0]
        out = tep.prompt(s["slug"], "HELLO")
        self.assertIn("HELLO", out)
        self.assertNotIn(tep.PLACEHOLDER, out)
        with self.assertRaises(ValueError):
            tep.prompt(s["slug"], "  ")
        with self.assertRaises(KeyError):
            tep.prompt("no-such-style", "x")

    def test_every_style_has_placeholder_and_links(self):
        for s in tep.all_styles():
            self.assertIn(tep.PLACEHOLDER, s["prompt"], s["id"])
            self.assertTrue(s["fontvibe_url"].startswith("https://fontvibe.ai/styles/"), s["id"])

    def test_search_ranks_and_filters(self):
        hits = tep.search("neon")
        self.assertTrue(hits)
        self.assertEqual(tep.search(""), [])
        self.assertLessEqual(len(tep.search("a", limit=3)), 3)
        with self.assertRaises(ValueError):
            tep.search("neon", lang="xx")

    def test_list_filters(self):
        cat = tep.categories()[0]
        self.assertTrue(all(s["category"] == cat for s in tep.list_styles(category=cat)))
        top = tep.tags()[0]
        self.assertEqual(len(tep.list_styles(tag=top["tag"])), top["count"])

    def test_name_falls_back_to_english(self):
        s = tep.all_styles()[0]
        self.assertEqual(tep.name(s["id"]), s["names"]["en"])
        self.assertTrue(tep.name(s["id"], "ja"))

    def test_attribution_formats(self):
        s = tep.all_styles()[0]
        self.assertIn(s["fontvibe_url"], tep.attribution(s["id"]))
        self.assertIn("<a href=", tep.attribution(s["id"], "html"))
        self.assertIn("CC BY 4.0", tep.attribution(fmt="text"))
        with self.assertRaises(ValueError):
            tep.attribution(s["id"], "pdf")

    def test_cli(self):
        self.assertEqual(main([tep.all_styles()[0]["slug"], "HI"]), 0)
        self.assertEqual(main(["--search", "neon"]), 0)
        self.assertEqual(main(["--list"]), 0)
        self.assertEqual(main(["nope", "x"]), 1)


if __name__ == "__main__":
    unittest.main()
