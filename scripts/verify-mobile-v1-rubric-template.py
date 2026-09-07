#!/usr/bin/env python3
"""Verify that each detailed Mobile V1 story follows the supplied rubric table."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
STORIES = (
    REPORT_ROOT
    / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
)

EXPECTED_STORY_IDS = (
    "MOB-US-001",
    "MOB-US-002",
    "MOB-US-003",
    "MOB-US-011",
    "MOB-US-012",
    "MOB-US-013",
    "MOB-US-014",
    "MOB-US-015",
    "MOB-US-016",
    "MOB-US-017",
    "MOB-US-019",
    "MOB-US-020",
    "MOB-US-021",
    "MOB-US-022",
    "MOB-US-023",
    "MOB-US-024",
    "MOB-US-025",
    "MOB-US-026",
    "MOB-US-027",
    "MOB-US-028",
    "MOB-US-031",
    "MOB-US-032",
    "MOB-US-033",
    "MOB-US-034",
    "MOB-US-044",
    "MOB-US-047",
    "MOB-US-048",
    "MOB-US-049",
)

REQUIRED_MARKERS = (
    "<th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th>",
    "<th>Title</th><td colspan=\"3\">",
    "<th colspan=\"4\">Description</th>",
    "<th colspan=\"4\">Acceptance Criteria</th>",
)


def story_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    blocks: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks.append((match.group(1), text[match.start() : end]))
    return blocks


def main() -> int:
    text = STORIES.read_text(encoding="utf-8")
    blocks = story_blocks(text)
    failures: list[str] = []
    actual_ids = [story_id for story_id, _ in blocks]

    if actual_ids != list(EXPECTED_STORY_IDS):
        failures.append("detailed V1 story IDs/order do not match the canonical lifecycle index")

    for story_id, block in blocks:
        for marker in REQUIRED_MARKERS:
            if marker not in block:
                failures.append(f"{story_id}: missing rubric marker {marker}")
        scenario_count = len(re.findall(r"<strong>Scenario:", block))
        if scenario_count != 4:
            failures.append(f"{story_id}: expected 4 Gherkin scenarios, got {scenario_count}")

    if len(blocks) != len(EXPECTED_STORY_IDS):
        failures.append(f"expected {len(EXPECTED_STORY_IDS)} detailed V1 records, got {len(blocks)}")

    if failures:
        print("mobile V1 rubric template validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("mobile V1 rubric template OK: records=28; fields=7; scenarios=112")
    return 0


if __name__ == "__main__":
    sys.exit(main())
