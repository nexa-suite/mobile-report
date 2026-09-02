#!/usr/bin/env python3
"""Compare the report's Mobile V1 table with the canonical Blueprint projection."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_ROOT = Path(
    os.environ.get("NEXA_BLUEPRINT_ROOT", REPORT_ROOT.parent / "blueprint")
)
REPORT_STORIES = (
    REPORT_ROOT
    / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
)
CANONICAL_PROJECTION = (
    BLUEPRINT_ROOT / "90-academic/mobile/course-1acc0238/requirements-projection.md"
)


def table_rows(text: str, start_heading: str, end_heading: str) -> list[list[str]]:
    start = text.index(start_heading)
    end = text.index(end_heading, start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if not line.startswith("| ") or "MOB-US-" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and re.fullmatch(r"MOB-US-\d{3}", cells[1]):
            rows.append(cells)
    return rows


def story_blocks(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### (MOB-US-\d{3}) (?:—|-)(.+)$", text, re.MULTILINE))
    blocks: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        blocks[match.group(1)] = text[match.start() : end]
    return blocks


def scenario_texts(block: str) -> list[str]:
    scenarios = re.findall(r"^\s*- (?:\*\*Scenario:|Scenario:)(.*)$", block, re.MULTILINE)
    return [re.sub(r"\*\*", "", scenario).strip() for scenario in scenarios]


def main() -> int:
    report_text = REPORT_STORIES.read_text(encoding="utf-8")
    canonical_text = CANONICAL_PROJECTION.read_text(encoding="utf-8")
    report_rows = table_rows(report_text, "## Backlog summary", "## Detailed story records")
    canonical_rows = table_rows(canonical_text, "## V1 backlog order", "## Visible V1 field registry")
    report_blocks = story_blocks(report_text)
    canonical_blocks = story_blocks(canonical_text)

    failures: list[str] = []
    if len(report_rows) != 28:
        failures.append(f"report summary rows: expected 28, got {len(report_rows)}")
    if len(canonical_rows) != 28:
        failures.append(f"canonical projection rows: expected 28, got {len(canonical_rows)}")

    expected_ids = [row[1] for row in canonical_rows]
    actual_ids = [row[1] for row in report_rows]
    if actual_ids != expected_ids:
        failures.append("report story IDs/order differ from canonical projection")

    canonical_by_id = {row[1]: row for row in canonical_rows}
    report_by_id = {row[1]: row for row in report_rows}
    for story_id in expected_ids:
        canonical = canonical_by_id[story_id]
        report = report_by_id.get(story_id)
        if report is None:
            continue
        comparisons = {
            "actor": (report[2], canonical[2]),
            "priority": (report[3], canonical[3]),
            "epic": (report[4], canonical[4]),
            "points": (report[5], canonical[7]),
            "sprint": (report[6], canonical[8]),
            "bounded context": (report[7], canonical[6]),
        }
        for field, (actual, expected) in comparisons.items():
            if actual != expected:
                failures.append(
                    f"{story_id} {field}: report={actual!r}, canonical={expected!r}"
                )

        canonical_title = canonical[5]
        block = report_blocks.get(story_id, "")
        heading = re.search(rf"^### {re.escape(story_id)} — (.+)$", block, re.MULTILINE)
        if not heading:
            failures.append(f"{story_id}: detailed record heading missing")
        elif heading.group(1).strip() != canonical_title:
            failures.append(
                f"{story_id} title: report={heading.group(1).strip()!r}, canonical={canonical_title!r}"
            )
        scenarios = re.findall(r"^- \*\*Scenario:", block, re.MULTILINE)
        if len(scenarios) != 4:
            failures.append(f"{story_id} scenarios: expected 4, got {len(scenarios)}")
        scenario_lines = re.findall(r"^- \*\*Scenario:.*$", block, re.MULTILINE)
        for scenario in scenario_lines:
            for keyword in ("Given", "when", "then"):
                if not re.search(rf"\b{keyword}\b", scenario, re.IGNORECASE):
                    failures.append(f"{story_id} scenario missing {keyword}: {scenario}")
        required_fields = (
            "| User / Actor |",
            "| Epic |",
            "| Priority / Points / Sprint |",
            "| Owning Bounded Context |",
            "| Description |",
            "| Canonical user story |",
        )
        for field in required_fields:
            if field not in block:
                failures.append(f"{story_id}: missing required field {field}")
        canonical_scenarios = scenario_texts(canonical_blocks.get(story_id, ""))
        report_scenarios = scenario_texts(block)
        if report_scenarios != canonical_scenarios:
            failures.append(
                f"{story_id} Gherkin scenarios differ from canonical projection"
            )

    if failures:
        print("mobile V1 transcription validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("mobile V1 transcription OK: rows=28 titles=28 scenarios=112")
    return 0


if __name__ == "__main__":
    sys.exit(main())
