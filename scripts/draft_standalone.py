#!/usr/bin/env python3
"""Draft a standalone prompt for every candidate style in data/source.json.

FontVibe's style layer is not a complete prompt: on the site it is combined
with a font description and a font reference image, so it contains
instructions such as "when the chosen font carries its own treatment ...".
This script asks an LLM to turn each layer into a self-contained prompt with
a {{TEXT}} placeholder. Every draft is then checked mechanically here, and
only enters the published set after a generic-model test (scripts/test_prompts.py)
and a human review of the test image.

    GEMINI_API_KEY=... python scripts/draft_standalone.py [--only id,id] [--force]

Writes data/standalone.json. Existing entries whose source hash still matches
are kept unless --force.
"""
import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = "gemini-3.8-flash"
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent" % MODEL

# Short sample words for styles whose FontVibe preview text is empty or not plain text.
TEST_TEXT_OVERRIDES = {
    "gothic_font": "Gothic", "cyberpunk": "CYBER", "anime_character": "HELLO", "bw_aesthetic": "MOOD",
    "chibi": "HELLO", "coquette_christmas": "NOEL", "cute_halloween": "BOO", "esports": "VICTORY",
    "flat_cartoon": "YAY", "kawaii": "CUTE", "nutcracker": "MERRY", "pink_christmas": "MERRY",
    "pink_halloween": "BOO", "preppy_christmas": "MERRY", "spooky_halloween": "SPOOKY",
    "vintage_christmas": "NOEL", "vintage_halloween": "BOO", "watercolor_christmas": "JOY",
}

INSTRUCTION = """You turn a "style layer" from a text-effect generator into a self-contained prompt for a general-purpose image model.

Background: on the source site the style layer is only one part of the final prompt. It is combined with a separate font description and a font reference image, so it contains instructions that only make sense inside that pipeline: who wins when "the chosen font" defines its own material or colour, fallback rules, priority rules, menus of tiers or deliverables. A general image model will receive only your prompt and no font.

What matters, in priority order:
1. The words render exactly. Begin with: Render the text "{{TEXT}}" exactly as written, character by character. Refer to the words as {{TEXT}} (literally, with the double braces) and make {{TEXT}} the only legible text in the image: leave out any other words, taglines, slogans, numbers or small secondary lines the layer mentions.
2. The image is recognisably this style. Keep the style's own vocabulary for letter treatment, material, colour, lighting, texture, composition and scene. Where the layer states a default or fallback ("otherwise ...", "if the font carries no material ..."), describe that default directly as how the letters look. Where it offers several variants, describe the single most representative one.
3. Nothing depends on the pipeline. Drop every reference to fonts, font priority, fallbacks, the selected font, tiers, deliverables or the generator itself.
4. Nothing is added. Do not introduce ideas that are not in the layer, and never name brands, products, platforms, franchises, studios, artists or other real people.

Write plain descriptive English prose in 90-200 words, no headings, no capitalised labels, no lists, no quality boilerplate such as "8k" or "masterpiece".

Also give one or two short, practical tips for someone using this prompt (for example what kind of words suit the style, or which detail to change to vary it). Tips must follow the same rules: no brands, no real people, no mention of fonts.
"""

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "prompt": {"type": "STRING"},
        "tips": {"type": "ARRAY", "items": {"type": "STRING"}},
    },
    "required": ["prompt", "tips"],
    "propertyOrdering": ["prompt", "tips"],
}

FORBIDDEN = re.compile(r"\bfonts?\b|typeface|FontVibe|PRIORITY|FALLBACK|\bselected\b|\bchosen\b|\btiers?\b", re.I)


def call(key, style):
    body = {
        "systemInstruction": {"parts": [{"text": INSTRUCTION}]},
        "contents": [{"role": "user", "parts": [{"text": "Style name: %s\n\nStyle layer (surface, colour & lighting):\n%s\n\nScene:\n%s" % (
            style["names"]["en"], style["style_layer"]["core"], style["style_layer"]["scene"] or "(none)")}]}],
        "generationConfig": {"responseMimeType": "application/json", "responseSchema": SCHEMA, "temperature": 0.4},
    }
    req = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    return json.loads(d["candidates"][0]["content"]["parts"][0]["text"])


def problems(p, deny):
    out = []
    if not p["prompt"].startswith('Render the text "{{TEXT}}" exactly as written'):
        out.append("bad opening")
    if FORBIDDEN.search(p["prompt"] + " " + " ".join(p["tips"])):
        out.append("pipeline word: %s" % FORBIDDEN.search(p["prompt"] + " " + " ".join(p["tips"])).group(0))
    for rx in deny:
        if rx.search(p["prompt"] + " " + " ".join(p["tips"])):
            out.append("denylisted: %s" % rx.pattern)
    n = len(p["prompt"].split())
    if n < 60 or n > 260:
        out.append("length %d words" % n)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("set GEMINI_API_KEY")
    src = json.load(open(os.path.join(ROOT, "data/source.json"), encoding="utf-8"))
    cur = json.load(open(os.path.join(ROOT, "data/curation.json"), encoding="utf-8"))
    deny = [re.compile(p) for p in cur["denylist"]]
    out_p = os.path.join(ROOT, "data/standalone.json")
    std = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {}
    only = set(filter(None, a.only.split(",")))
    todo = [(sid, st) for sid, st in sorted(src.items())
            if (not only or sid in only)
            and (a.force or sid not in std or std[sid].get("source_hash") != st["style_layer_hash"] or std[sid].get("problems"))]

    def draft(job):
        sid, st = job
        p, probs, calls = None, ["not run"], 0
        for attempt in range(3):
            try:
                p = call(key, st)
                calls += 1
            except Exception as e:  # network / quota: retry, never print the key
                print("  %s: request failed (%s %s)" % (sid, type(e).__name__, getattr(e, "code", "")), flush=True)
                time.sleep(5)
                continue
            p["tips"] = [t.strip() for t in p["tips"] if t.strip()][:2]
            probs = problems(p, deny)
            if not probs:
                break
        return sid, st, p, probs, calls

    total = 0
    with concurrent.futures.ThreadPoolExecutor(max(1, a.workers)) as ex:
        for sid, st, p, probs, calls in ex.map(draft, todo):
            total += calls
            text = TEST_TEXT_OVERRIDES.get(sid) or st["preview_text"] or "FONTVIBE"
            std[sid] = {"prompt": p["prompt"] if p else "", "tips": p["tips"] if p else [],
                        "test_text": text, "source_hash": st["style_layer_hash"],
                        "drafted_with": MODEL, "problems": probs}
            print("  %-28s %s" % (sid, "ok" if not probs else "PROBLEMS: " + "; ".join(probs)), flush=True)
            with open(out_p, "w", encoding="utf-8") as f:
                json.dump(dict(sorted(std.items())), f, ensure_ascii=False, indent=2)
                f.write("\n")
    print("LLM calls: %d" % total)


if __name__ == "__main__":
    main()
