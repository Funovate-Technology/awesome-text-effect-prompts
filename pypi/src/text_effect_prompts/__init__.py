"""text-effect-prompts — AI text-effect prompts from FontVibe.

Code: MIT. Prompts and data: CC BY 4.0 — please credit with a link to the style's
FontVibe page (see :func:`attribution`). https://fontvibe.ai/styles

Same API and data as the npm package of the same name.
"""
from __future__ import annotations

import json
from functools import lru_cache
from importlib import resources
from typing import Any, Dict, List, Optional

__all__ = [
    "LANGS", "PLACEHOLDER", "stats", "all_styles", "get", "list_styles", "search",
    "prompt", "name", "categories", "tags", "attribution",
]
__version__ = "1.0.0"

LANGS = ("en", "ja", "zh", "es", "pt", "de")
PLACEHOLDER = "{{TEXT}}"
_LICENSE_URL = "https://creativecommons.org/licenses/by/4.0/"

Style = Dict[str, Any]


@lru_cache(maxsize=1)
def _index() -> Dict[str, Any]:
    raw = resources.files(__package__).joinpath("index.json").read_text(encoding="utf-8")
    return json.loads(raw)


def _norm(s: Any) -> str:
    return ("" if s is None else str(s)).strip().lower()


def _take(items: List[Style], limit: Optional[int]) -> List[Style]:
    # None / negative mean "no limit"; never slice with a negative number.
    return items if limit is None or limit < 0 else items[:limit]


def stats() -> Dict[str, Any]:
    """Counts for the published collection (styles, categories, exclusions...)."""
    return _index()["stats"]


def all_styles() -> List[Style]:
    """Every published style."""
    return _index()["styles"]


def get(id_or_slug: str) -> Optional[Style]:
    """Look a style up by id ("neon_glow") or slug ("neon-glow")."""
    q = _norm(id_or_slug)
    return next((s for s in all_styles() if s["id"] == q or s["slug"] == q), None)


def categories() -> List[str]:
    """Category ids that have at least one style, in index order."""
    seen: List[str] = []
    for s in all_styles():
        if s["category"] not in seen:
            seen.append(s["category"])
    return seen


def tags() -> List[Dict[str, Any]]:
    """All tags with how many styles carry them, most common first."""
    counts: Dict[str, int] = {}
    for s in all_styles():
        for t in s["tags"]:
            counts[t] = counts.get(t, 0) + 1
    return [{"tag": t, "count": c} for t, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))]


def list_styles(category: Optional[str] = None, tag: Optional[str] = None, limit: Optional[int] = None) -> List[Style]:
    """Filter by category and/or tag."""
    cat, tg = _norm(category), _norm(tag)
    return _take([s for s in all_styles() if (not cat or s["category"] == cat) and (not tg or tg in s["tags"])], limit)


def search(query: str, lang: Optional[str] = None, category: Optional[str] = None, limit: Optional[int] = None) -> List[Style]:
    """Case-insensitive substring search over id, tags, and names and descriptions in
    all six languages (or only ``lang``). Name and id matches rank first."""
    q = _norm(query)
    if not q:
        return []
    if lang and lang not in LANGS:
        raise ValueError(f'text-effect-prompts: unknown lang "{lang}" (use one of {", ".join(LANGS)})')
    langs = (lang,) if lang else LANGS
    scored = []
    for s in list_styles(category=category):
        if q in s["id"] or q in s["slug"] or any(q in _norm(s["names"].get(l)) for l in langs):
            score = 3
        elif any(q in t for t in s["tags"]):
            score = 2
        elif any(q in _norm(s["description"].get(l)) for l in langs):
            score = 1
        else:
            continue
        scored.append((score, s))
    scored.sort(key=lambda x: -x[0])  # stable: keeps index order within a score
    return _take([s for _, s in scored], limit)


def prompt(id_or_slug: str, text: str) -> str:
    """The standalone prompt for a style with {{TEXT}} replaced by your words."""
    s = get(id_or_slug)
    if s is None:
        raise KeyError(f'text-effect-prompts: unknown style "{id_or_slug}"')
    t = "" if text is None else str(text)
    if not t.strip():
        raise ValueError("text-effect-prompts: text must not be empty")
    return s["prompt"].replace(PLACEHOLDER, t)


def name(id_or_slug: str, lang: Optional[str] = None) -> Optional[str]:
    """Localised name, falling back to English when a translation is missing."""
    s = get(id_or_slug)
    if s is None:
        return None
    return (lang and s["names"].get(lang)) or s["names"]["en"]


def attribution(id_or_slug: Optional[str] = None, fmt: str = "markdown") -> str:
    """A credit line for a style (or the whole collection when id is omitted).
    ``fmt`` is "markdown", "html" or "text"."""
    s = get(id_or_slug) if id_or_slug else None
    if id_or_slug and s is None:
        raise KeyError(f'text-effect-prompts: unknown style "{id_or_slug}"')
    url = s["fontvibe_url"] if s else "https://fontvibe.ai/styles"
    label = f'{s["names"]["en"]} prompt from FontVibe' if s else "Text-effect prompts from FontVibe"
    if fmt == "html":
        return label.replace("FontVibe", f'<a href="{url}">FontVibe</a>') + f' · <a href="{_LICENSE_URL}">CC BY 4.0</a>'
    if fmt == "text":
        return f"{label} — {url} — CC BY 4.0"
    if fmt == "markdown":
        return label.replace("FontVibe", f"[FontVibe]({url})") + f" · [CC BY 4.0]({_LICENSE_URL})"
    raise ValueError("text-effect-prompts: fmt must be markdown, html or text")
