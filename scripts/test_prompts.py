#!/usr/bin/env python3
"""Render each standalone prompt once on a general image model, for review.

    GEMINI_API_KEY=... python scripts/test_prompts.py --out DIR [--only id,id] [--retry id,id]

For every style in data/standalone.json that has no test yet, fill {{TEXT}}
with the style's `test_text`, generate one image and save it to DIR. The
attempt is recorded in data/tests.json with `passed: null`; a reviewer then
looks at every image and sets `passed` to true or false with a `note`.
Nothing is published until that review has happened (see scripts/export.py).

Budget guards: at most 2 attempts per style (--retry grants the second),
and a hard cap on the total number of generations recorded in tests.json.
"""
import argparse
import base64
import concurrent.futures
import datetime
import json
import os
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL = os.environ.get("TEST_MODEL", "gemini-2.5-flash-image")
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"
MAX_PER_STYLE = 2
HARD_CAP = 300


def generate(key, prompt, aspect):
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": aspect}},
    }
    req = urllib.request.Request(ENDPOINT % MODEL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json", "x-goog-api-key": key})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.load(r)
    for c in d.get("candidates") or []:
        for p in (c.get("content") or {}).get("parts") or []:
            inline = p.get("inlineData") or p.get("inline_data")
            if inline:
                return base64.b64decode(inline["data"]), inline.get("mimeType", "image/png")
    raise RuntimeError("no image in response (finishReason=%s)" % [c.get("finishReason") for c in d.get("candidates") or []])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", default="")
    ap.add_argument("--retry", default="", help="ids allowed a second attempt")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("set GEMINI_API_KEY")
    os.makedirs(a.out, exist_ok=True)
    std = json.load(open(os.path.join(ROOT, "data/standalone.json"), encoding="utf-8"))
    tp = os.path.join(ROOT, "data/tests.json")
    tests = json.load(open(tp, encoding="utf-8")) if os.path.exists(tp) else {}
    only = set(filter(None, a.only.split(",")))
    retry = set(filter(None, a.retry.split(",")))
    used = sum(len(t.get("attempts", [])) for t in tests.values())

    # Plan every job up front so the budget guards are applied before anything runs.
    jobs = []
    for sid, sp in sorted(std.items()):
        if only and sid not in only:
            continue
        if sp.get("problems") or not sp.get("prompt"):
            continue
        n = len((tests.get(sid) or {}).get("attempts", []))
        if n >= MAX_PER_STYLE or (n == 1 and sid not in retry):
            continue
        if used + len(jobs) >= HARD_CAP:
            print("HARD CAP of %d generations reached — not scheduling the rest." % HARD_CAP)
            break
        if a.limit and len(jobs) >= a.limit:
            break
        jobs.append((sid, sp, n))

    def run(job):
        sid, sp, n = job
        text = sp["test_text"]
        aspect = "16:9" if len(text) > 10 else "1:1"
        att = {"file": "", "error": ""}
        try:
            img, mime = generate(key, sp["prompt"].replace("{{TEXT}}", text), aspect)
            ext = {"image/png": "png", "image/jpeg": "jpg", "image/webp": "webp"}.get(mime, "png")
            fname = "%s-%d.%s" % (sid.replace("_", "-"), n + 1, ext)
            with open(os.path.join(a.out, fname), "wb") as f:
                f.write(img)
            att["file"] = fname
        except urllib.error.HTTPError as e:
            att["error"] = "HTTP %s %s" % (e.code, e.read()[:200].decode("utf-8", "replace"))
        except Exception as e:
            att["error"] = "%s: %s" % (type(e).__name__, str(e)[:200])
        att.update({"model": MODEL, "date": datetime.date.today().isoformat(), "text": text,
                    "aspect": aspect, "source_hash": sp["source_hash"]})
        return sid, att

    with concurrent.futures.ThreadPoolExecutor(max(1, a.workers)) as ex:
        for sid, att in ex.map(run, jobs):
            # Every attempt is recorded, failed or not: it may still have been billed.
            t = tests.get(sid) or {"attempts": []}
            t["attempts"].append(att)
            t.update({"model": MODEL, "date": att["date"], "text": att["text"], "image_file": att["file"],
                      "passed": None, "note": ""})
            tests[sid] = t
            used += 1
            print("  %-28s %s" % (sid, att["file"] or "ERROR " + att["error"][:120]), flush=True)
            with open(tp, "w", encoding="utf-8") as f:
                json.dump(tests, f, ensure_ascii=False, indent=2)
                f.write("\n")
    print("generations recorded in tests.json: %d (cap %d)" % (used, HARD_CAP))


if __name__ == "__main__":
    main()
