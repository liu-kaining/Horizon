"""Smoke tests for GitHub Actions helper scripts under scripts/ci/."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_generate_site_stats_writes_json(tmp_path: Path) -> None:
    (tmp_path / "docs" / "_posts").mkdir(parents=True)
    sample = """---
lang: zh
---
# Horizon 每日速递 - 2026-05-07

> From 10 items, 3 important content pieces were selected

---

## [Example](https://example.com) ⭐️ 8.0/10

Summary line.

**标签**: `#rust`
"""
    (tmp_path / "docs" / "_posts" / "2026-05-07-summary-zh.md").write_text(sample, encoding="utf-8")

    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts/ci/generate_site_stats.py"), "--root", str(tmp_path)],
        check=True,
        cwd=tmp_path,
    )

    out = tmp_path / "docs" / "_data" / "stats.json"
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["total_articles"] == 1
    assert data["total_fetched"] == 10
    assert data["total_digests_zh"] == 1


def test_generate_search_index_entries(tmp_path: Path) -> None:
    (tmp_path / "docs" / "_posts").mkdir(parents=True)
    sample = """---
lang: zh
---
## [News](https://news.example) ⭐️ 7.5/10

**标签**: `#ai`, `#rust`
"""
    (tmp_path / "docs" / "_posts" / "2026-05-07-summary-zh.md").write_text(sample, encoding="utf-8")

    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts/ci/generate_search_index.py"), "--root", str(tmp_path)],
        check=True,
        cwd=tmp_path,
    )

    idx = json.loads((tmp_path / "docs" / "assets" / "search-index.json").read_text(encoding="utf-8"))
    assert len(idx) == 1
    assert idx[0]["title"] == "News"
    assert idx[0]["score"] == 7.5
    assert "ai" in idx[0]["tags"]
