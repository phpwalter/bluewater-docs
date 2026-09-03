#!/usr/bin/env python3
"""Synchronize framework-owned technical guides into the publication tree."""

from __future__ import annotations

import argparse
from pathlib import Path


MAPPINGS = {
    "docs/APP_DEVELOPERS.md": "docs/en/technical/application-developers.md",
    "docs/CORE_DEVELOPERS.md": "docs/en/technical/core-developers.md",
}


def publication_copy(content: str, destination: str) -> str:
    content = content.replace(
        "📄 **File:** `docs/APP_DEVELOPERS.md`",
        "📄 **File:** `docs/en/technical/application-developers.md`",
    ).replace(
        "📄 **File:** `docs/CORE_DEVELOPERS.md`",
        "📄 **File:** `docs/en/technical/core-developers.md`",
    )
    content = content.replace("[Framework overview](../README.md)", "[About Bluewater](../about-bluewater.md)")
    content = content.replace("[Core developer guide](CORE_DEVELOPERS.md)", "[Core developer guide](core-developers.md)")
    content = content.replace("[Application developer guide](APP_DEVELOPERS.md)", "[Application developer guide](application-developers.md)")
    content = content.replace("[License](../LICENSE)", "[Documentation license](../../../LICENSE)")
    content = content.replace(
        "This repository and its technical documentation are licensed under the [OSL-3.0 License](../LICENSE).",
        "This published documentation is licensed under the [MIT License](../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.",
    )
    if f"📄 **File:** `{destination}`" not in content:
        raise ValueError(f"Unable to establish destination metadata for {destination}")
    return content


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("framework", type=Path, help="Path to bluewater-framework checkout")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]

    for source_name, destination_name in MAPPINGS.items():
        source = args.framework.resolve() / source_name
        destination = repo / destination_name
        if not source.is_file():
            raise FileNotFoundError(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            publication_copy(source.read_text(encoding="utf-8"), destination_name),
            encoding="utf-8",
        )
        print(f"Synchronized {source_name} -> {destination_name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
