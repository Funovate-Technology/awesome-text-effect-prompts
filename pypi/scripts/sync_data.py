#!/usr/bin/env python3
"""Copy the repo-level index.json and licence files into the package before building.

index.json at the repo root is the single source of truth for the npm and the PyPI
package; the copy inside src/ is generated and never committed.
"""
import json
import pathlib
import shutil
import sys

PKG = pathlib.Path(__file__).resolve().parent.parent
REPO = PKG.parent
SRC = REPO / "index.json"
if not SRC.exists():
    sys.exit(f"[sync_data] missing {SRC} — run this from inside the repo")
data = json.loads(SRC.read_text(encoding="utf-8"))  # fail loudly on a broken index
if not data.get("styles"):
    sys.exit("[sync_data] index.json has no styles — refusing")
shutil.copyfile(SRC, PKG / "src" / "text_effect_prompts" / "index.json")
for f in ("LICENSE", "LICENSE-CODE", "NOTICE"):
    shutil.copyfile(REPO / f, PKG / f)
print(f"[sync_data] ok — {len(data['styles'])} styles")
