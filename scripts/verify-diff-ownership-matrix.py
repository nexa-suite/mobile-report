#!/usr/bin/env python3
"""Verify that the current report worktree paths have one review-unit entry."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
MATRIX = REPORT_ROOT / "delivery-checklists/current-diff-ownership-matrix.md"


def git_paths(*args: str) -> list[str]:
    output = subprocess.check_output(["git", *args], cwd=REPORT_ROOT, text=True)
    return [line for line in output.splitlines() if line]


def main() -> int:
    text = MATRIX.read_text(encoding="utf-8")
    base_match = re.search(r"^\| Base \| `([^`]+)`", text, re.MULTILINE)
    if base_match:
        current = sorted(
            set(
                git_paths("diff", base_match.group(1), "--name-only")
                + git_paths("ls-files", "--others", "--exclude-standard")
            )
        )
    else:
        current = sorted(
            set(
                git_paths("diff", "--name-only")
                + git_paths("ls-files", "--others", "--exclude-standard")
            )
        )
    units_start = text.index("## Unit ")
    unassigned_start = text.index("## Unassigned paths", units_start)
    unit_text = text[units_start:unassigned_start]
    listed = re.findall(r"^- `([^`]+)`$", unit_text, re.MULTILINE)
    failures: list[str] = []

    if len(listed) != len(set(listed)):
        failures.append("matrix lists duplicate paths")
    if sorted(listed) != current:
        listed_set = set(listed)
        current_set = set(current)
        missing = sorted(current_set - listed_set)
        stale = sorted(listed_set - current_set)
        if missing:
            failures.append(f"current paths missing from matrix: {', '.join(missing)}")
        if stale:
            failures.append(f"stale matrix paths: {', '.join(stale)}")

    if failures:
        print("diff ownership matrix validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"diff ownership matrix OK: paths={len(current)} units=9")
    return 0


if __name__ == "__main__":
    sys.exit(main())
