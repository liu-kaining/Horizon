#!/usr/bin/env python3
"""Build docs/assets/search-index.json from docs/_posts for client-side search.

Parses item headings without embedding '[' in regex character classes (YAML-safe).
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="ignore")


_RE_TAG_INLINE = re.compile(r"`#([^`]+)`")
_RE_LANG = re.compile(r"^lang:\s*(zh|en)\s*$", re.M)
_RE_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")
_RE_TAGS_LINE = re.compile(r"^\*\*(?:Tags|标签)\*\*:\s*(?P<body>.+?)\s*$", re.M)


def parse_item_header_line(line: str) -> dict[str, str | float] | None:
    """Parse `## [title](url) … N/10` without brittle emoji-specific regex."""
    s = line.strip()
    if not s.startswith("## ["):
        return None
    try:
        rest = s[3:].lstrip()  # after ##
        if not rest.startswith("["):
            return None
        close_title = rest.find("](")
        if close_title < 1:
            return None
        title = rest[1:close_title]
        tail = rest[close_title + 2 :]
        if ")" not in tail:
            return None
        url_end = tail.index(")")
        url = tail[:url_end]
        after = tail[url_end + 1 :].strip()
        m = re.search(r"(\d+(?:\.\d+)?)/10\s*$", after)
        if not m:
            return None
        score = float(m.group(1))
        return {"title": title.strip(), "url": url.strip(), "score": score}
    except (ValueError, IndexError):
        return None


def extract_tags_after_header(chunk: str) -> list[str]:
    m = _RE_TAGS_LINE.search(chunk)
    if not m:
        return []
    return [t.strip() for t in _RE_TAG_INLINE.findall(m.group("body")) if t.strip()]


def iter_item_regions(text: str) -> list[tuple[int, int]]:
    """Return (start_line_index, end_line_index_exclusive) for each ## [ item block."""
    lines = text.splitlines()
    starts: list[int] = []
    for i, line in enumerate(lines):
        if parse_item_header_line(line):
            starts.append(i)
    regions: list[tuple[int, int]] = []
    for j, start in enumerate(starts):
        end = starts[j + 1] if j + 1 < len(starts) else len(lines)
        regions.append((start, end))
    return regions


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate docs/assets/search-index.json")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("."),
        help="Repository root (default: current directory)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    posts_dir = root / "docs" / "_posts"
    out = root / "docs" / "assets" / "search-index.json"
    out.parent.mkdir(parents=True, exist_ok=True)

    if not posts_dir.exists():
        out.write_text("[]\n", encoding="utf-8")
        print("No posts found; wrote empty index:", out)
        return

    entries: list[dict] = []

    for md in sorted(posts_dir.glob("*.md")):
        txt = read_text(md)
        lang_m = _RE_LANG.search(txt)
        lang = lang_m.group(1) if lang_m else None

        date_m = _RE_DATE.search(md.name) or _RE_DATE.search(txt)
        digest_date = date_m.group(1) if date_m else None

        digest_url: str | None = None
        if digest_date:
            y, mo, d = digest_date.split("-")
            slug = md.stem
            digest_url = f"/{y}/{mo}/{d}/{slug}.html"

        lines = txt.splitlines()
        for start, end in iter_item_regions(txt):
            header_line = lines[start]
            parsed = parse_item_header_line(header_line)
            if not parsed:
                continue
            chunk = "\n".join(lines[start:end])
            tags = extract_tags_after_header(chunk)
            entries.append(
                {
                    "lang": lang,
                    "digest_date": digest_date,
                    "digest_url": digest_url or str(parsed["url"]),
                    "title": parsed["title"],
                    "score": parsed["score"],
                    "tags": tags,
                }
            )

    out.write_text(json.dumps(entries, ensure_ascii=False) + "\n", encoding="utf-8")
    print("Wrote", out, "entries:", len(entries))


if __name__ == "__main__":
    main()
