#!/usr/bin/env python3
"""Validate the repo's doc-facing source of truth surfaces.

This keeps the human-facing README chapter counts, MkDocs navigation, and the
root complexity-table shim aligned with the actual docs tree.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
MKDOCS_PATH = ROOT / "mkdocs.yml"
DOCS_DIR = ROOT / "docs"
ROOT_COMPLEXITY_PATH = ROOT / "COMPLEXITY_MASTER_TABLE.md"
DOCS_COMPLEXITY_PATH = DOCS_DIR / "complexity_master_table.md"

README_ROW_RE = re.compile(
    r"^\|\s*(?P<left_label>[^|]+?)\s*\|\s*(?P<left_count>\d+)\s*\|\s*"
    r"(?P<right_label>[^|]+?)\s*\|\s*(?P<right_count>\d+)\s*\|$"
)
TOP_LEVEL_NAV_RE = re.compile(r"^  - (?P<label>[^:]+):(?:\s*(?P<path>.+))?$")
CHILD_NAV_RE = re.compile(r"^      - (?P<label>[^:]+):\s*(?P<path>.+)$")
CHAPTER_FOLDER_RE = re.compile(r"^\d{2}_.+")
PROBLEM_FILE_RE = re.compile(r"^\d{2}_.+\.md$")


def parse_readme_counts(text: str) -> dict[str, int]:
    """Extract the chapter-count table from README.md."""

    counts: dict[str, int] = {}
    in_section = False

    for line in text.splitlines():
        stripped = line.strip()
        if stripped == "## 📚 題目分類":
            in_section = True
            continue

        if not in_section:
            continue

        if stripped == "---":
            break

        match = README_ROW_RE.match(line)
        if not match:
            continue

        left_label = match.group("left_label").strip()
        right_label = match.group("right_label").strip()
        counts[left_label] = int(match.group("left_count"))
        counts[right_label] = int(match.group("right_count"))

    return counts


def parse_mkdocs_chapter_counts(text: str) -> dict[str, tuple[str, int]]:
    """Extract chapter navigation counts from mkdocs.yml.

    Returns a mapping of chapter label -> (chapter folder, number of child
    problem pages).
    """

    groups: dict[str, list[str]] = {}
    in_nav = False
    current_label: str | None = None
    current_children: list[str] = []

    for line in text.splitlines():
        if not in_nav:
            if line.strip() == "nav:":
                in_nav = True
            continue

        top_level = TOP_LEVEL_NAV_RE.match(line)
        if top_level:
            if current_label is not None:
                groups[current_label] = current_children

            label = top_level.group("label").strip()
            path = top_level.group("path")
            if path is None:
                current_label = label
                current_children = []
            else:
                current_label = None
                current_children = []
            continue

        if current_label is None:
            continue

        child = CHILD_NAV_RE.match(line)
        if child:
            current_children.append(child.group("path").strip())

    if current_label is not None:
        groups[current_label] = current_children

    chapter_counts: dict[str, tuple[str, int]] = {}
    for label, children in groups.items():
        prefixes = {path.split("/", 1)[0] for path in children if "/" in path}
        if len(prefixes) != 1:
            continue

        folder = next(iter(prefixes))
        if not CHAPTER_FOLDER_RE.match(folder):
            continue

        chapter_counts[label] = (folder, len(children))

    return chapter_counts


def count_problem_pages(folder: Path) -> int:
    """Count numbered problem markdown files inside a chapter folder."""

    return sum(
        1
        for path in folder.glob("*.md")
        if path.is_file() and PROBLEM_FILE_RE.match(path.name)
    )


def main() -> int:
    errors: list[str] = []

    readme_text = README_PATH.read_text(encoding="utf-8")
    mkdocs_text = MKDOCS_PATH.read_text(encoding="utf-8")
    readme_counts = parse_readme_counts(readme_text)
    mkdocs_counts = parse_mkdocs_chapter_counts(mkdocs_text)

    if not DOCS_COMPLEXITY_PATH.exists():
        errors.append("docs/complexity_master_table.md is missing.")

    if not ROOT_COMPLEXITY_PATH.exists():
        errors.append("COMPLEXITY_MASTER_TABLE.md is missing.")
    else:
        root_complexity_text = ROOT_COMPLEXITY_PATH.read_text(encoding="utf-8")
        if "docs/complexity_master_table.md" not in root_complexity_text:
            errors.append(
                "COMPLEXITY_MASTER_TABLE.md must point to docs/complexity_master_table.md."
            )
        if "## 0) 符號約定" in root_complexity_text or "## 1) 30 秒速背總表" in root_complexity_text:
            errors.append(
                "COMPLEXITY_MASTER_TABLE.md still contains the full duplicated table."
            )

    if "📚 複雜度總表（完整版）: complexity_master_table.md" not in mkdocs_text:
        errors.append(
            "mkdocs.yml must keep the canonical complexity table on docs/complexity_master_table.md."
        )

    for label, (folder_name, nav_count) in sorted(mkdocs_counts.items()):
        folder = DOCS_DIR / folder_name
        if not folder.exists():
            errors.append(f"docs chapter folder is missing for '{label}': {folder_name}.")
            continue

        actual_count = count_problem_pages(folder)

        readme_count = readme_counts.get(label)
        if readme_count is None:
            errors.append(f"README.md is missing the chapter count entry for '{label}'.")
        elif readme_count != actual_count:
            errors.append(
                f"README.md count mismatch for '{label}': expected {actual_count}, found {readme_count}."
            )

        if nav_count != actual_count:
            errors.append(
                f"mkdocs.yml count mismatch for '{label}': expected {actual_count}, found {nav_count}."
            )

    missing_in_nav = sorted(set(readme_counts) - set(mkdocs_counts))
    if missing_in_nav:
        errors.append(
            "mkdocs.yml is missing chapter labels from README.md: "
            + ", ".join(missing_in_nav)
        )

    extra_in_nav = sorted(set(mkdocs_counts) - set(readme_counts))
    if extra_in_nav:
        errors.append(
            "README.md is missing chapter labels from mkdocs.yml: "
            + ", ".join(extra_in_nav)
        )

    if errors:
        print("Repository consistency check failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository consistency check passed: README counts, MkDocs nav, and the "
        "complexity-table shim are aligned."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
