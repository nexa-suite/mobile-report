#!/usr/bin/env python3
"""Check that the manual Mobile V1 review register matches the report backlog."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
STORIES = (
    REPORT_ROOT
    / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
)
REGISTER = REPORT_ROOT / "delivery-checklists/mobile-v1-story-verification-register.md"


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


def parse_review_rows(text: str) -> list[list[str]]:
    start = text.index("## Register")
    end = text.index("## Current result", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if not line.startswith("| ") or "MOB-US-" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and re.fullmatch(r"MOB-US-\d{3}", cells[0]):
            rows.append(cells)
    return rows


def main() -> int:
    story_rows = table_rows(STORIES.read_text(encoding="utf-8"), "## Backlog summary", "## Detailed story records")
    review_rows = parse_review_rows(REGISTER.read_text(encoding="utf-8"))
    failures: list[str] = []

    if len(story_rows) != 28:
        failures.append(f"report summary rows: expected 28, got {len(story_rows)}")
    if len(review_rows) != 28:
        failures.append(f"review register rows: expected 28, got {len(review_rows)}")

    expected_ids = [row[1] for row in story_rows]
    actual_ids = [row[0] for row in review_rows]
    if actual_ids != expected_ids:
        failures.append("manual review register IDs/order differ from the report backlog")

    report_by_id = {row[1]: row for row in story_rows}
    expected_segments = {
        "Mobile User": {"S1-S3"},
        "Warehouse Operator": {"S1"},
        "Dispatch Coordinator": {"S1"},
        "Driver or Delivery Operator": {"S2"},
        "Customer Buyer": {"S3"},
    }
    expected_review_leads = {
        **{story_id: "Diego / DiegoS284" for story_id in ("MOB-US-001", "MOB-US-002", "MOB-US-003")},
        **{
            story_id: "Gino / R0obxdnt"
            for story_id in (
                "MOB-US-011",
                "MOB-US-012",
                "MOB-US-013",
                "MOB-US-014",
                "MOB-US-015",
                "MOB-US-016",
                "MOB-US-017",
                "MOB-US-019",
            )
        },
        **{
            story_id: "Diego / DiegoS284"
            for story_id in (
                "MOB-US-020",
                "MOB-US-021",
                "MOB-US-022",
                "MOB-US-023",
                "MOB-US-024",
                "MOB-US-025",
            )
        },
        **{
            story_id: "Gerard / GerardRojasMancilla"
            for story_id in (
                "MOB-US-026",
                "MOB-US-027",
                "MOB-US-028",
                "MOB-US-031",
                "MOB-US-032",
                "MOB-US-033",
                "MOB-US-034",
            )
        },
        **{
            story_id: "Sebastián / spinedo214"
            for story_id in ("MOB-US-044", "MOB-US-047", "MOB-US-048", "MOB-US-049")
        },
    }
    for review in review_rows:
        story_id = review[0]
        report = report_by_id.get(story_id)
        if report is None:
            continue
        if review[3] != expected_review_leads.get(story_id):
            failures.append(
                f"{story_id} review lead: register={review[3]!r}, expected={expected_review_leads.get(story_id)!r}"
            )
        actual_actor, separator, actual_segment = review[1].partition(" / ")
        if not separator or actual_actor != report[2]:
            failures.append(
                f"{story_id} actor: register={actual_actor!r}, report={report[2]!r}"
            )
        allowed_segments = expected_segments.get(report[2], set())
        if not allowed_segments:
            failures.append(f"{story_id}: no canonical segment mapping for actor {report[2]!r}")
        if actual_segment not in allowed_segments:
            failures.append(
                f"{story_id} segment: register={actual_segment!r}, allowed={sorted(allowed_segments)!r}"
            )
        if review[2] != report[7]:
            failures.append(f"{story_id} bounded context: register={review[2]!r}, report={report[7]!r}")
        if len(review) != 8 or any(not cell for cell in review[3:]):
            failures.append(f"{story_id}: review fields must remain present for manual completion")

    if failures:
        print("mobile V1 review register validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("mobile V1 review register OK: rows=28; actor/segment/BC aligned; manual decisions preserved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
