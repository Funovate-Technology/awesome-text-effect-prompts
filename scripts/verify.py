#!/usr/bin/env python3
"""Check that this repository says only true things about itself.

    python scripts/verify.py             # URL check on a random sample of 40
    python scripts/verify.py --urls all  # check every URL in index.json
    python scripts/verify.py --urls 0    # skip the network

Checks
  1. numbers   every number in the README's generated blocks matches index.json,
               and index.json matches the files under prompts/
  2. tests     every published style has a passed generic-model test on record
  3. denylist  no pattern from data/curation.json survives in any published file,
               and no excluded style id appears outside data/curation.json
  4. prompts   every standalone prompt contains {{TEXT}} and no pipeline wording
  5. urls      every (or a sample of) URL in index.json answers 200

Stdlib only. Exit code 0 = all checks passed.
"""
import argparse
import concurrent.futures
import json
import os
import random
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["en", "ja", "zh", "es", "pt", "de"]
SKIP_DIRS = {".git", "node_modules"}
# The denylist has to be written down somewhere; that file is the one exception.
DENYLIST_SOURCE = os.path.join("data", "curation.json")

fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond


def read(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return f.read()


def block(readme, marker):
    a, b = "<!-- %s:start -->" % marker, "<!-- %s:end -->" % marker
    return readme[readme.index(a) + len(a):readme.index(b)]


def check_numbers(idx, readme):
    st = idx["stats"]
    styles = idx["styles"]
    check(st["published"] == len(styles), "stats.published %d != %d styles" % (st["published"], len(styles)))
    md = []
    for root, dirs, files in os.walk(os.path.join(ROOT, "prompts")):
        md += [os.path.relpath(os.path.join(root, f), ROOT) for f in files if f.endswith(".md")]
    check(sorted(md) == sorted(s["file"] for s in styles), "prompts/*.md files do not match index.json")
    for cat, n in st["by_category"].items():
        check(n == sum(1 for s in styles if s["category"] == cat), "by_category[%s]" % cat)

    counts = block(readme, "counts")
    nums = [int(x) for x in re.findall(r"^\s*(\d+)\s", counts, re.M)]
    expect = [st["published"], sum(1 for v in st["by_category"].values() if v), len(st["languages"]),
              st["excluded_trademark"], st["failed_test"]]
    check(nums == expect, "README counts block %s != %s" % (nums, expect))

    tables = block(readme, "tables")
    for title, n in re.findall(r"^### (.+?) \((\d+)\)", tables, re.M):
        section = tables.split("### %s (%s)" % (title, n), 1)[1].split("###", 1)[0]
        rows = len(re.findall(r"^\| <img", section, re.M))
        check(int(n) == rows, "README table '%s' says %s, has %d rows" % (title, n, rows))
    total_rows = len(re.findall(r"^\| <img", tables, re.M))
    check(total_rows == st["published"], "README tables have %d rows, published %d" % (total_rows, st["published"]))

    langs = block(readme, "languages")
    for field, key in (("names", "names"), ("descriptions", "description")):
        m = re.search(r"^\| %s \|(.+)\|$" % field, langs, re.M)
        if check(m, "README languages row '%s' missing" % field):
            got = [int(x) for x in m.group(1).split("|")]
            want = [sum(1 for s in styles if s[key][l]) for l in LANGS]
            check(got == want, "README languages %s %s != %s" % (field, got, want))

    excl = block(readme, "excluded")
    m = re.search(r"(\d+) (?:style|styles) (?:are |is )?left out for trademark", readme)
    if m:
        check(int(m.group(1)) == st["excluded_trademark"], "README trademark count")
    failed_rows = len(re.findall(r"^\| `", excl, re.M))
    check(failed_rows == st["failed_test"], "README failure table has %d rows, stats say %d" % (failed_rows, st["failed_test"]))

    # Any "N styles" phrase anywhere in the README must be a number we can account for.
    allowed = {st["published"], st["styles_on_fontvibe"], st["excluded_trademark"], st["failed_test"], st["candidates"]}
    for n in re.findall(r"\*\*(\d+)\*\* (?:text-effect )?styles", readme):
        check(int(n) in allowed, "README mentions **%s** styles, which is none of %s" % (n, sorted(allowed)))


def check_tests(idx):
    tests = json.loads(read("data/tests.json"))
    for s in idx["styles"]:
        t = tests.get(s["id"])
        if not check(t is not None, "%s: no test on record" % s["id"]):
            continue
        check(t.get("passed") is True, "%s: test not passed" % s["id"])
        check(bool(t.get("attempts")), "%s: no attempts recorded" % s["id"])
        check(bool(t.get("image_file")) and any(a["file"] == t["image_file"] for a in t["attempts"]),
              "%s: test image not among attempts" % s["id"])
        check(s["test"]["passed"] is True and s["test"]["model"], "%s: index test block" % s["id"])
        check(len(t["attempts"]) <= 2, "%s: more than 2 generations" % s["id"])
    total = sum(len(t.get("attempts", [])) for t in tests.values())
    check(total <= 300, "total generations %d > 300" % total)
    return total


def published_files():
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            p = os.path.relpath(os.path.join(root, f), ROOT)
            if p == DENYLIST_SOURCE or not re.search(r"\.(md|json|cff|txt|js|mjs|ts|py|csv)$|^LICENSE|^NOTICE", f):
                continue
            yield p


def check_denylist():
    cur = json.loads(read(DENYLIST_SOURCE))
    deny = [re.compile(p) for p in cur["denylist"]]
    excluded = [e["id"] for e in cur["excluded"]]
    n = 0
    for p in published_files():
        text = read(p)
        n += 1
        for rx in deny:
            m = rx.search(text)
            check(not m, "%s: denylisted '%s' found (%r)" % (p, rx.pattern, m and text[max(0, m.start() - 40):m.end() + 20]))
        for sid in excluded:
            check(sid not in text, "%s: excluded style id '%s' appears" % (p, sid))
    return n


PIPELINE = re.compile(r"\bfonts?\b|typeface|PRIORITY|FALLBACK|\bselected\b|\bchosen\b", re.I)


def check_prompts(idx):
    for s in idx["styles"]:
        p = s["prompt"]
        check("{{TEXT}}" in p, "%s: prompt has no {{TEXT}}" % s["id"])
        m = PIPELINE.search(p)
        check(not m, "%s: pipeline wording in standalone prompt: %s" % (s["id"], m and m.group(0)))
        check(s["fontvibe_url"] == "https://fontvibe.ai/styles/" + s["id"].replace("_", "-"), "%s: fontvibe_url" % s["id"])


def status(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": "awesome-text-effect-prompts-verify/1.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.status
        except urllib.error.HTTPError as e:
            if method == "GET":
                return e.code
        except Exception as e:
            if method == "GET":
                return type(e).__name__
    return None


def check_urls(idx, how):
    urls = set()
    for s in idx["styles"]:
        urls.add(s["fontvibe_url"])
        urls.add(s["preview_image"])
        if s["test"].get("image"):
            urls.add(s["test"]["image"])
        for x in s["examples"]:
            urls.add(x["url"])
            urls.add(x["image"])
    urls = sorted(urls)
    if how == "0":
        return 0, 0
    if how != "all":
        random.seed()
        urls = random.sample(urls, min(int(how), len(urls)))
    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        res = list(ex.map(status, urls))
    bad = [(u, c) for u, c in zip(urls, res) if c != 200]
    for u, c in bad:
        check(False, "URL %s -> %s" % (u, c))
    return len(urls), len(bad)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls", default="40", help="'all', '0', or a sample size (default 40)")
    a = ap.parse_args()
    idx = json.loads(read("index.json"))
    readme = read("README.md")
    check_numbers(idx, readme)
    print("numbers   checked")
    total = check_tests(idx)
    print("tests     %d published styles, %d generations on record" % (len(idx["styles"]), total))
    n = check_denylist()
    print("denylist  %d files scanned" % n)
    check_prompts(idx)
    print("prompts   checked")
    checked, bad = check_urls(idx, a.urls)
    print("urls      %d checked, %d not 200" % (checked, bad))
    if fails:
        print("\nFAILED (%d):" % len(fails))
        for f in fails:
            print("  - " + f)
        sys.exit(1)
    print("\nall checks passed")


if __name__ == "__main__":
    main()
