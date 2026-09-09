#!/usr/bin/env python3
"""Check the source-backed Chapter 2.4 projection without rewriting prose.

The former renderer owned an obsolete flat 2.4 layout, historic sprint
assignments and generated narrative. Chapter 2.4 now contains reviewed,
owner-authored research states and business-value ordering, so replacing those
files from a template would be unsafe. This compatibility entry point validates
the canonical inventory and never writes report artifacts.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
CHAPTER = REPORT_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification"
FUNCTIONAL = CHAPTER / "2.4.1-user-stories/user-stories.md"
TECHNICAL = CHAPTER / "2.4.1-user-stories/technical-stories.md"
SPIKES = CHAPTER / "2.4.1-user-stories/spike-stories.md"
BACKLOG = CHAPTER / "2.4.3-product-backlog.md"

EXPECTED_LANDING = {f"LAND-US-{number:03d}" for number in range(1, 7)}
EXPECTED_TECHNICAL = {f"TS-MOB-{number:03d}" for number in range(1, 13)}
EXPECTED_SPIKES = {f"SPIKE-{number:03d}" for number in range(1, 7)}
STORY_HEADING = re.compile(r"^#### ((?:LAND-US|MOB-US|TS-MOB|SPIKE)-\d{3}) — .+$", re.MULTILINE)


def resolve_blueprint_root() -> Path:
    explicit = os.environ.get("NEXA_BLUEPRINT_ROOT")
    if explicit:
        return Path(explicit)
    for ancestor in (REPORT_ROOT, *REPORT_ROOT.parents):
        candidate = ancestor / "blueprint"
        if candidate.is_dir():
            return candidate
    result = subprocess.run(
        ["git", "-C", str(REPORT_ROOT), "rev-parse", "--git-common-dir"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        common_dir = Path(result.stdout.strip())
        if not common_dir.is_absolute():
            common_dir = REPORT_ROOT / common_dir
        for ancestor in common_dir.resolve().parents:
            candidate = ancestor / "blueprint"
            if candidate.is_dir():
                return candidate
    return REPORT_ROOT.parent / "blueprint"


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def master_rows(path: Path) -> dict[str, dict[str, str]]:
    headers: list[str] | None = None
    rows: dict[str, dict[str, str]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ID | Title |"):
            headers = cells(line)
        elif headers and line.startswith("| MOB-US-"):
            values = cells(line)
            if len(values) == len(headers):
                row = dict(zip(headers, values))
                rows[row["ID"]] = row
    return rows


def headings(path: Path) -> list[str]:
    return STORY_HEADING.findall(path.read_text(encoding="utf-8"))


def backlog_rows(path: Path) -> list[list[str]]:
    text = path.read_text(encoding="utf-8")
    start = text.index("## Índice completo")
    end = text.index("## Sprints planificados", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        values = cells(line)
        if len(values) == 5 and values[0].isdigit() and re.fullmatch(
            r"(?:MOB-US|LAND-US|TS-MOB|SPIKE)-\d{3}", values[1]
        ):
            rows.append(values)
    return rows


def main() -> int:
    blueprint = resolve_blueprint_root()
    master = blueprint / "03-mobile/requirements/master-mobile-backlog.md"
    required = (master, FUNCTIONAL, TECHNICAL, SPIKES, BACKLOG)
    failures = [f"missing required artifact: {path}" for path in required if not path.is_file()]
    if failures:
        print("mobile report projection check: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    source = master_rows(master)
    functional_headings = headings(FUNCTIONAL)
    technical_headings = headings(TECHNICAL)
    spike_headings = headings(SPIKES)
    rows = backlog_rows(BACKLOG)
    canonical_ids = set(source)
    expected_ids = canonical_ids | EXPECTED_LANDING | EXPECTED_TECHNICAL | EXPECTED_SPIKES

    if len(source) != 73:
        failures.append(f"canonical functional inventory: expected 73, got {len(source)}")
    functional_ids = {story_id for story_id in functional_headings if story_id.startswith("MOB-US-")}
    landing_ids = {story_id for story_id in functional_headings if story_id.startswith("LAND-US-")}
    if functional_ids != canonical_ids:
        failures.append("functional story headings differ from the canonical inventory")
    if landing_ids != EXPECTED_LANDING:
        failures.append("landing story headings differ from LAND-US-001..006")
    if set(technical_headings) != EXPECTED_TECHNICAL:
        failures.append("technical story headings differ from TS-MOB-001..012")
    if set(spike_headings) != EXPECTED_SPIKES:
        failures.append("spike story headings differ from SPIKE-001..006")

    row_ids = [row[1] for row in rows]
    if len(rows) != 97:
        failures.append(f"academic backlog rows: expected 97, got {len(rows)}")
    if len(set(row_ids)) != len(row_ids):
        failures.append("academic backlog contains duplicate IDs")
    if set(row_ids) != expected_ids:
        failures.append("academic backlog IDs differ from the canonical plus support inventory")
    for expected_order, row in enumerate(rows, start=1):
        if row[0] != str(expected_order):
            failures.append(f"backlog order mismatch at row {expected_order}: {row[0]!r}")

    release_counts = Counter(
        "V4/Future" if row["Target Release"] == "V4_FUTURE" else row["Target Release"]
        for row in source.values()
    )
    if release_counts != Counter({"V1": 28, "V2": 35, "V3": 9, "V4/Future": 1}):
        failures.append(f"canonical release counts differ: {dict(release_counts)}")

    if failures:
        print("mobile report projection check: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        "mobile report projection check OK: no files written; "
        "functional=73; releases=28/35/9/1; landing=6; technical=12; spikes=6; backlog_rows=97"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
