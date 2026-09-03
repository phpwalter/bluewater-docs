#!/usr/bin/env python3
"""Validate Bluewater Markdown structure and repository-local links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED = (
    "<!-- locale-guard:language-bar:start -->",
    "<!-- locale-guard:language-bar:end -->",
    "📄 **File:**",
    "📅 **Status:**",
    "🏷️ **Tags:**",
    "🔖 **Version:**",
    "📅 **Date:**",
    "🌍 **Scope:**",
    "🤝 **Contributors:**",
    "👨‍💻 **Author:**",
    "Bluewater Principle",
    "## 📌 Purpose",
    "## 📚 Related Documents",
    "MIT License",
    "Last updated:",
)
PROHIBITED = ("{{DATE}}", "coming soon", "Content would be inserted", "CC BY 4.0")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    failures: list[str] = []
    canonical = sorted((repo / "docs/en").rglob("*.md"))

    for path in canonical:
        relative = path.relative_to(repo).as_posix()
        content = path.read_text(encoding="utf-8")
        if not content.strip():
            failures.append(f"{relative}: empty document")
            continue

        is_template = "_templates" in path.parts
        if not is_template:
            for marker in REQUIRED:
                if marker not in content:
                    failures.append(f"{relative}: missing {marker}")
            if f"📄 **File:** `{relative}`" not in content:
                failures.append(f"{relative}: metadata path does not match file")
            for phrase in PROHIBITED:
                if phrase.casefold() in content.casefold():
                    failures.append(f"{relative}: prohibited unresolved text {phrase!r}")

        for target in LINK.findall(content):
            target = target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            candidates = (resolved, Path(f"{resolved}.md"), resolved / "index.md", resolved / "README.md")
            if not any(candidate.exists() for candidate in candidates):
                failures.append(f"{relative}: unresolved link {target}")

    legacy = sorted((repo / "docs").rglob("*.md.txt"))
    failures.extend(f"{path.relative_to(repo)}: use .md instead of .md.txt" for path in legacy)

    if failures:
        print("Documentation validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Documentation validation passed for {len(canonical)} canonical Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
