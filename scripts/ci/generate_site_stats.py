#!/usr/bin/env python3
"""Write docs/_data/stats.json from data/summaries or docs/_posts.

Kept as a normal script file (not YAML-embedded) so:
- python -m compileall catches syntax errors before deploy
- logic can be reviewed and tested locally
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="ignore")


# Header lines from src/ai/summarizer.py (English for both langs)
_RE_HEADER = re.compile(
    r"^(?:From\s+(\d+)\s+items,\s+(\d+)\s+important|Analyzed\s+(\d+)\s+items)",
    re.I | re.M,
)
_RE_ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def count_digest_items(text: str) -> int:
    """Count markdown H2 item headings (no regex brackets)."""
    n = 0
    for line in text.splitlines():
        if line.lstrip().startswith("## ["):
            n += 1
    return n


def parse_header_fetched(text: str) -> int | None:
    for line in text.splitlines():
        t = line.strip()
        if not t.startswith(">"):
            continue
        inner = t.lstrip(">").strip()
        m = _RE_HEADER.match(inner)
        if not m:
            continue
        if m.group(1):
            return int(m.group(1))
        if m.group(3):
            return int(m.group(3))
    return None


def count_posts_by_lang(docs_posts: Path, lang: str) -> int:
    if not docs_posts.exists():
        return 0
    c = 0
    for p in docs_posts.glob("*.md"):
        t = read_text(p)
        for line in t.splitlines():
            s = line.strip()
            if s.startswith("lang:"):
                val = s.split(":", 1)[1].strip()
                if val == lang:
                    c += 1
                break
    return c


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate docs/_data/stats.json")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Repository root (default: current directory)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    data_summaries = root / "data" / "summaries"
    docs_posts = root / "docs" / "_posts"
    out = root / "docs" / "_data" / "stats.json"
    out.parent.mkdir(parents=True, exist_ok=True)

    files: list[Path] = []
    if data_summaries.exists():
        files = sorted(data_summaries.glob("*.md"))
    if not files and docs_posts.exists():
        files = sorted(docs_posts.glob("*.md"))

    total_articles = 0
    total_fetched = 0
    last_digest_date: str | None = None

    for f in files:
        txt = read_text(f)
        total_articles += count_digest_items(txt)
        fetched = parse_header_fetched(txt)
        if fetched is not None:
            total_fetched += fetched

        dm = _RE_ISO_DATE.search(f.name) or (
            _RE_ISO_DATE.search(txt.splitlines()[0]) if txt else None
        )
        if dm:
            d = dm.group(0)
            if last_digest_date is None or d > last_digest_date:
                last_digest_date = d

    total_digests_zh = count_posts_by_lang(docs_posts, "zh")
    total_digests_en = count_posts_by_lang(docs_posts, "en")
    total_digests = total_digests_zh + total_digests_en

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_articles": int(total_articles),
        "total_fetched": int(total_fetched),
        "total_digests": int(total_digests),
        "total_digests_zh": int(total_digests_zh),
        "total_digests_en": int(total_digests_en),
        "last_digest_date": last_digest_date,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote", out, "->", payload)


if __name__ == "__main__":
    main()
