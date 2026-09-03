#!/usr/bin/env python3
"""Synchronize framework-owned technical guides into the publication tree."""

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path, PurePosixPath


LINK_RE = re.compile(r"(?P<prefix>!?\[[^\]]*\]\()(?P<target>[^)]+)(?P<suffix>\))")


def published_path(source: PurePosixPath) -> PurePosixPath:
    if source == PurePosixPath("README.md"):
        return PurePosixPath("docs/en/about-bluewater.md")
    if source == PurePosixPath("LICENSE"):
        return PurePosixPath("LICENSE")
    if source == PurePosixPath("docs/README.md"):
        return PurePosixPath("docs/en/technical/index.md")
    if source.parts[:1] == ("docs",) and source.suffix == ".md":
        return PurePosixPath("docs/en/technical", *source.parts[1:])
    return source


def resolve_link(source: PurePosixPath, target: str) -> PurePosixPath:
    normalized = os.path.normpath((source.parent / target).as_posix())
    return PurePosixPath(normalized)


def publication_copy(content: str, source: PurePosixPath, destination: PurePosixPath) -> str:
    content = re.sub(
        r"📄 \*\*File:\*\* `[^`]+`",
        f"📄 **File:** `{destination.as_posix()}`",
        content,
        count=1,
    )

    def rewrite(match: re.Match[str]) -> str:
        target = match.group("target")
        if target.startswith(("#", "http://", "https://", "mailto:")):
            return match.group(0)
        path_text, separator, fragment = target.partition("#")
        resolved = resolve_link(source, path_text)
        published = published_path(resolved)
        relative = os.path.relpath(published.as_posix(), destination.parent.as_posix())
        rewritten = relative + (separator + fragment if separator else "")
        return f'{match.group("prefix")}{rewritten}{match.group("suffix")}'

    content = LINK_RE.sub(rewrite, content)
    license_link = os.path.relpath("LICENSE", destination.parent.as_posix())
    content = re.sub(
        r"This repository and its technical documentation are licensed under the "
        r"\[OSL-3\.0 License\]\([^)]+\)\.",
        "This published documentation is licensed under the "
        f"[MIT License]({license_link}). Bluewater Framework source code is separately "
        "licensed under OSL-3.0.",
        content,
    )
    if f"📄 **File:** `{destination.as_posix()}`" not in content:
        raise ValueError(f"Unable to establish destination metadata for {destination}")
    return content


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("framework", type=Path, help="Path to bluewater-framework checkout")
    args = parser.parse_args()
    framework = args.framework.resolve()
    repo = Path(__file__).resolve().parents[1]
    destination_root = repo / "docs/en/technical"

    if destination_root.is_dir():
        shutil.rmtree(destination_root)
    destination_root.mkdir(parents=True)

    sources = sorted((framework / "docs").rglob("*.md"))
    if not sources:
        raise FileNotFoundError(framework / "docs")

    for source_file in sources:
        source = PurePosixPath(source_file.relative_to(framework).as_posix())
        destination = published_path(source)
        destination_file = repo / destination.as_posix()
        destination_file.parent.mkdir(parents=True, exist_ok=True)
        destination_file.write_text(
            publication_copy(source_file.read_text(encoding="utf-8"), source, destination),
            encoding="utf-8",
        )
        print(f"Synchronized {source} -> {destination}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
