#!/usr/bin/env python3
"""Rebuild this repository from FontVibe's public API.

    python scripts/export.py            # fetch the API, then rebuild everything
    python scripts/export.py --offline  # rebuild from data/source.json without fetching

Steps
  1. fetch   POST /styles/v1/list in six locales (en ja zh es pt de) and
             POST /gallery/v1/list for official example works (author 17).
  2. scrub   apply data/curation.json: drop excluded styles, rewrite brand /
             franchise / real-person mentions, drop localized sentences that
             still contain a denylisted term. Result -> data/source.json.
  3. build   merge data/standalone.json (the hand-checked standalone prompts)
             and data/tests.json (generic-model test results) and write
             prompts/<category>/<slug>.md, index.json, the README tables and
             npm/data/index.json.

A style is published only if it has a standalone prompt AND a passed test.
The standalone prompt records a hash of the style layer it was written from;
if FontVibe later changes that style, the entry is flagged `stale` in
index.json so it can be rewritten and re-tested.

Stdlib only. No credentials are needed or read.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.fontvibe.ai/logicSrv/FontVibeAPI"
SITE = "https://fontvibe.ai"
REPO = "https://github.com/Funovate-Technology/awesome-text-effect-prompts"
LANGS = ["en", "ja", "zh", "es", "pt", "de"]
OFFICIAL_AUTHOR_ID = 17
WORKS_PER_STYLE = 3
CATEGORY_ORDER = ["effects", "aesthetics", "text_styles", "scenes", "occasions"]
CATEGORY_TITLES = {
    "effects": "Effects",
    "aesthetics": "Aesthetics",
    "text_styles": "Text styles",
    "scenes": "Scenes",
    "occasions": "Occasions",
}
# Where the generic-model test images are hosted. Empty = not hosted yet
# (the image is then referenced by file name only; see data/tests.json).
TEST_IMAGE_BASE = os.environ.get("TEST_IMAGE_BASE", "")

UA = "awesome-text-effect-prompts-export/1.0 (+%s)" % REPO


def path(*p):
    return os.path.join(ROOT, *p)


def load(p):
    with open(path(p), encoding="utf-8") as f:
        return json.load(f)


def dump(p, obj):
    with open(path(p), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def post(endpoint, body, locale=None, tries=3):
    headers = {"Content-Type": "application/json", "User-Agent": UA}
    if locale and locale != "en":
        headers["X-Locale"] = locale
    data = json.dumps(body).encode()
    for i in range(tries):
        try:
            req = urllib.request.Request(API + endpoint, data=data, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.load(r)
            if str(d.get("Code")) != "200":
                raise RuntimeError("%s -> %s %s" % (endpoint, d.get("Code"), d.get("Msg")))
            return d["Data"]
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def slug(style_id):
    return style_id.replace("_", "-")


def style_url(style_id):
    return "%s/styles/%s" % (SITE, slug(style_id))


def work_url(gen_id):
    return "%s/gallery/%s" % (SITE, gen_id)


# ───────────────────────────── fetch ─────────────────────────────

STYLE_FIELDS = ["StyleId", "Name", "Category", "Tags", "Description", "PromptCore",
                "PromptScene", "ParentStyleId", "PreviewImageUrl", "PreviewText"]


def fetch():
    by_lang = {}
    for lang in LANGS:
        fields = STYLE_FIELDS if lang == "en" else ["StyleId", "Name", "Description"]
        d = post("/styles/v1/list", {"Category": "", "Fields": fields, "PageSize": 500, "Offset": 0}, lang)
        by_lang[lang] = {s["StyleId"]: s for s in d["List"]}
        print("  styles[%s]: %d" % (lang, len(d["List"])))
    works = {}
    for sid in by_lang["en"]:
        d = post("/gallery/v1/list", {"Style": sid, "AuthorId": OFFICIAL_AUTHOR_ID, "PageSize": 40})
        works[sid] = [
            {"id": w["GenerationId"], "image": w["ImageUrl"], "text": w.get("TextContent", ""),
             "likes": w.get("LikeCount", 0), "boost": w.get("EditorialBoost", 0) or 0,
             "aspect": w.get("AspectRatio", "")}
            for w in d.get("List") or []
        ]
    print("  works fetched for %d styles" % len(works))
    return by_lang, works


# ───────────────────────────── scrub ─────────────────────────────

def compile_denylist(cur):
    return [re.compile(p) for p in cur["denylist"]]


def denied(text, deny):
    return [rx.pattern for rx in deny if text and rx.search(text)]


def apply_rules(text, sid, rules):
    for r in rules:
        if sid in r["styles"]:
            text = re.sub(r["pattern"], r["replace"], text)
    return text


SENT_SPLIT = re.compile(r"(?<=[.!?。！？])\s*")


def drop_denied_sentences(text, deny):
    if not denied(text, deny):
        return text
    parts = [p for p in SENT_SPLIT.split(text) if p.strip()]
    kept = [p for p in parts if not denied(p, deny)]
    joiner = "" if re.search(r"[\u3040-\u30ff\u4e00-\u9fff]", text) else " "
    return joiner.join(kept).strip()


def scrub(by_lang, works, cur):
    deny = compile_denylist(cur)
    rules = cur["scrub_rules"]
    excluded = {e["id"] for e in cur["excluded"]}
    renamed = {r["id"]: r for r in cur["renamed"]}
    out = {}
    for sid, en in sorted(by_lang["en"].items()):
        if sid in excluded:
            continue
        names, descs = {}, {}
        for lang in LANGS:
            s = by_lang[lang].get(sid, {})
            name, desc = s.get("Name", "") or "", s.get("Description", "") or ""
            if lang == "en":
                name = apply_rules(name, sid, rules)
                desc = apply_rules(desc, sid, rules)
                if sid in renamed:
                    name = renamed[sid]["to"]
            if denied(name, deny):
                name = ""
            desc = drop_denied_sentences(desc, deny)
            names[lang], descs[lang] = name, desc
        core = apply_rules(en.get("PromptCore", "") or "", sid, rules)
        scene = apply_rules(en.get("PromptScene", "") or "", sid, rules)
        bad = denied(core + " " + scene + " " + " ".join(en.get("Tags") or []), deny)
        if bad:
            raise SystemExit("unscrubbed term(s) %s in style %s — add a scrub rule to data/curation.json" % (bad, sid))
        ws = [w for w in works.get(sid, [])
              if not denied(w["text"], deny) and not denied(w["image"], deny)
              and w["image"] != en.get("PreviewImageUrl")]
        ws.sort(key=lambda w: (-w["boost"], -w["likes"], w["id"]))
        preview = en.get("PreviewImageUrl") or ""
        if denied(preview, deny) and ws:
            # The file name itself carries a denylisted term: use the top official work instead.
            preview = ws.pop(0)["image"]
        out[sid] = {
            "id": sid,
            "slug": slug(sid),
            "category": en["Category"],
            "parent": en.get("ParentStyleId") or "",
            "tags": [t.lower() for t in (en.get("Tags") or [])],
            "names": names,
            "description": descs,
            "preview_text": en.get("PreviewText") or "",
            "preview_image": preview,
            "style_layer": {"core": core, "scene": scene},
            "style_layer_hash": layer_hash(core, scene),
            "examples": [{"image": w["image"], "url": work_url(w["id"])} for w in ws[:WORKS_PER_STYLE]],
        }
    return out


def layer_hash(core, scene):
    return hashlib.sha256((core + "\n" + scene).encode()).hexdigest()[:16]


# ───────────────────────────── build ─────────────────────────────

def yaml_str(s):
    return json.dumps(s, ensure_ascii=False)


def fill(prompt, text):
    return prompt.replace("{{TEXT}}", text)


def test_image_url(t):
    if t.get("image_url"):
        return t["image_url"]
    if TEST_IMAGE_BASE and t.get("image_file"):
        return TEST_IMAGE_BASE.rstrip("/") + "/" + t["image_file"]
    return ""


def render_md(e):
    L = ["---"]
    L.append("id: %s" % e["id"])
    L.append("slug: %s" % e["slug"])
    L.append("category: %s" % e["category"])
    if e["parent"]:
        L.append("parent: %s" % e["parent"])
    L.append("tags: [%s]" % ", ".join(yaml_str(t) for t in e["tags"]))
    L.append("names:")
    for lang in LANGS:
        L.append("  %s: %s" % (lang, yaml_str(e["names"][lang])))
    L.append("description:")
    for lang in LANGS:
        L.append("  %s: %s" % (lang, yaml_str(e["description"][lang])))
    L.append("fontvibe_url: %s" % e["fontvibe_url"])
    L.append("preview_image: %s" % e["preview_image"])
    L.append("examples:")
    for x in e["examples"]:
        L.append("  - url: %s" % x["url"])
        L.append("    image: %s" % x["image"])
    t = e["test"]
    L.append("test:")
    L.append("  model: %s" % t["model"])
    L.append("  date: %s" % t["date"])
    L.append("  text: %s" % yaml_str(t["text"]))
    L.append("  image: %s" % yaml_str(t["image"]))
    L.append("  passed: %s" % ("true" if t["passed"] else "false"))
    L.append("  note: %s" % yaml_str(t.get("note", "")))
    L.append("license: CC-BY-4.0")
    L.append("---")
    L.append("")
    name = e["names"]["en"]
    L.append("# %s" % name)
    L.append("")
    if e["description"]["en"]:
        L.append("> %s" % e["description"]["en"])
        L.append("")
    L.append("[![%s on FontVibe](%s)](%s)" % (name, e["preview_image"], e["fontvibe_url"]))
    L.append("")
    L.append("**Try it with your own words on FontVibe → [%s](%s)**" % (e["fontvibe_url"].replace("https://", ""), e["fontvibe_url"]))
    L.append("")
    L.append("## Standalone prompt")
    L.append("")
    L.append("Replace `{{TEXT}}` with your words. Written for general image models; tested on `%s`." % t["model"])
    L.append("")
    L.append("```text")
    L.append(e["prompt"])
    L.append("```")
    L.append("")
    if t["image"]:
        L.append("Generic-model test (`%s`, text \"%s\", %s):" % (t["model"], t["text"], t["date"]))
        L.append("")
        L.append("![test render](%s)" % t["image"])
        L.append("")
    else:
        L.append("Tested on `%s` with the text \"%s\" on %s — passed (legible, correctly spelled, recognisably this style)." % (t["model"], t["text"], t["date"]))
        L.append("")
    if e["examples"]:
        L.append("## Examples made on FontVibe")
        L.append("")
        L.append(" ".join("[![example](%s)](%s)" % (x["image"], x["url"]) for x in e["examples"]))
        L.append("")
    L.append("## Original FontVibe style layer")
    L.append("")
    L.append("This is the style layer FontVibe itself uses. It is **not** a complete prompt: on FontVibe it is combined with a font description, a font reference image and the model routing for that style, so some sentences refer to \"the chosen font\". Use the standalone prompt above with other tools.")
    L.append("")
    L.append("**Surface, colour & lighting**")
    L.append("")
    L.append("```text")
    L.append(e["style_layer"]["core"])
    L.append("```")
    if e["style_layer"]["scene"]:
        L.append("")
        L.append("**Scene**")
        L.append("")
        L.append("```text")
        L.append(e["style_layer"]["scene"])
        L.append("```")
    L.append("")
    L.append("## Tips")
    L.append("")
    for tip in e["tips"]:
        L.append("- %s" % tip)
    L.append("")
    L.append("---")
    L.append("")
    L.append("Prompt and data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please credit with a link to [%s](%s) — see [Attribution](../../README.md#attribution)." % (e["fontvibe_url"].replace("https://", ""), e["fontvibe_url"]))
    L.append("")
    return "\n".join(L)


GENERIC_TIPS = [
    "Short words (1–3 words, under ~15 letters) come out most reliably on general models; long phrases are where spelling breaks first.",
    "Results are best on FontVibe, where this style is paired with a real font, a font reference image and the model it was tuned on. General models get the material, colour and mood but choose their own letter shapes.",
]


def build(src):
    cur = load("data/curation.json")
    std = load("data/standalone.json")
    tests = load("data/tests.json")
    entries, skipped = [], {"no_prompt": [], "failed": [], "untested": []}
    for sid, e in sorted(src.items()):
        sp = std.get(sid)
        t = tests.get(sid)
        if not sp:
            skipped["no_prompt"].append(sid)
            continue
        if not t:
            skipped["untested"].append(sid)
            continue
        if not t.get("passed"):
            skipped["failed"].append(sid)
            continue
        e = dict(e)
        e["fontvibe_url"] = style_url(sid)
        e["prompt"] = sp["prompt"]
        e["stale"] = sp.get("source_hash") != e["style_layer_hash"]
        e["tips"] = list(sp.get("tips") or []) + GENERIC_TIPS
        e["test"] = {"model": t["model"], "date": t["date"], "text": t["text"],
                     "image": test_image_url(t), "image_file": t.get("image_file", ""),
                     "passed": True, "note": t.get("note", "")}
        entries.append(e)

    # prompts/
    for root, dirs, files in os.walk(path("prompts")):
        for f in files:
            if f.endswith(".md"):
                os.remove(os.path.join(root, f))
    for e in entries:
        d = path("prompts", e["category"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, e["slug"] + ".md"), "w", encoding="utf-8") as f:
            f.write(render_md(e))

    missing = {lang: {"names": 0, "description": 0} for lang in LANGS}
    for e in entries:
        for lang in LANGS:
            missing[lang]["names"] += not e["names"][lang]
            missing[lang]["description"] += not e["description"][lang]

    cats = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
    stats = {
        "styles_on_fontvibe": len(src) + len(cur["excluded"]),
        "excluded_trademark": len(cur["excluded"]),
        "candidates": len(src),
        "published": len(entries),
        "failed_test": len(skipped["failed"]),
        "untested": len(skipped["untested"]),
        "no_prompt": len(skipped["no_prompt"]),
        "by_category": {c: cats.get(c, 0) for c in CATEGORY_ORDER},
        "languages": LANGS,
        "missing_translations": missing,
        "stale": sum(1 for e in entries if e["stale"]),
        "test_model": sorted({e["test"]["model"] for e in entries}),
    }
    index = {
        "name": "awesome-text-effect-prompts",
        "version": load("npm/package.json")["version"] if os.path.exists(path("npm/package.json")) else "0.0.0",
        "license": "CC-BY-4.0",
        "homepage": SITE + "/styles",
        "repository": REPO,
        "placeholder": "{{TEXT}}",
        "stats": stats,
        "styles": [
            {k: e[k] for k in ["id", "slug", "category", "parent", "tags", "names", "description",
                               "fontvibe_url", "preview_image", "examples", "prompt", "style_layer",
                               "test", "stale"]}
            | {"file": "prompts/%s/%s.md" % (e["category"], e["slug"])}
            for e in entries
        ],
        "failed": [{"id": sid, "reason": tests[sid].get("note", "")} for sid in skipped["failed"]],
    }
    dump("index.json", index)
    os.makedirs(path("npm", "data"), exist_ok=True)
    dump("npm/data/index.json", index)
    write_readme(entries, stats, skipped, tests, cur)
    print("  published %d, failed %d, untested %d, no prompt %d" % (
        len(entries), len(skipped["failed"]), len(skipped["untested"]), len(skipped["no_prompt"])))
    return index


def md_cell(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def write_readme(entries, stats, skipped, tests, cur):
    p = path("README.md")
    with open(p, encoding="utf-8") as f:
        readme = f.read()

    def put(marker, body):
        nonlocal readme
        a, b = "<!-- %s:start -->" % marker, "<!-- %s:end -->" % marker
        i, j = readme.index(a) + len(a), readme.index(b)
        readme = readme[:i] + "\n" + body.rstrip() + "\n" + readme[j:]

    # counts
    c = stats
    lines = [
        "```",
        "%5d   styles published, each with a standalone prompt tested on a general image model" % c["published"],
        "%5d   categories" % sum(1 for v in c["by_category"].values() if v),
        "%5d   languages for names and descriptions (en · ja · zh · es · pt · de)" % len(c["languages"]),
        "%5d   styles on FontVibe left out for trademark reasons" % c["excluded_trademark"],
        "%5d   styles left out because their standalone prompt failed the test" % c["failed_test"],
        "```",
    ]
    put("counts", "\n".join(lines))

    # category tables
    out = []
    for cat in CATEGORY_ORDER:
        es = [e for e in entries if e["category"] == cat]
        if not es:
            continue
        out.append("### %s (%d)" % (CATEGORY_TITLES[cat], len(es)))
        out.append("")
        out.append("| Preview | Style | Prompt | Try it |")
        out.append("|---|---|---|---|")
        for e in es:
            out.append("| <img src=\"%s\" width=\"120\" alt=\"%s\"> | **%s**<br>%s | [prompt](prompts/%s/%s.md) | [fontvibe.ai](%s) |" % (
                e["preview_image"], md_cell(e["names"]["en"]), md_cell(e["names"]["en"]),
                md_cell(e["description"]["en"]), cat, e["slug"], e["fontvibe_url"]))
        out.append("")
    put("tables", "\n".join(out))

    # failures + exclusions
    # Trademark exclusions are only counted here (their ids carry the marks);
    # the full list with reasons is data/curation.json.
    out = ["| Style | Try it on FontVibe | Why the standalone prompt was left out |", "|---|---|---|"]
    for sid in skipped["failed"]:
        out.append("| `%s` | [%s](%s) | %s |" % (sid, slug(sid), style_url(sid), md_cell(tests[sid].get("note", ""))))
    put("excluded", "\n".join(out))

    # translations
    m = stats["missing_translations"]
    out = ["| | " + " | ".join(LANGS) + " |", "|---|" + "---:|" * len(LANGS),
           "| names | " + " | ".join(str(stats["published"] - m[l]["names"]) for l in LANGS) + " |",
           "| descriptions | " + " | ".join(str(stats["published"] - m[l]["description"]) for l in LANGS) + " |"]
    put("languages", "\n".join(out))

    with open(p, "w", encoding="utf-8") as f:
        f.write(readme)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--offline", action="store_true", help="rebuild from data/source.json without fetching")
    ap.add_argument("--fetch-only", action="store_true", help="refresh data/source.json and stop")
    a = ap.parse_args()
    if a.offline:
        src = load("data/source.json")
    else:
        print("fetching %s ..." % API)
        by_lang, works = fetch()
        src = scrub(by_lang, works, load("data/curation.json"))
        dump("data/source.json", src)
        print("  data/source.json: %d candidate styles" % len(src))
        if a.fetch_only:
            return
    build(src)


if __name__ == "__main__":
    sys.exit(main())
