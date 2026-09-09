#!/usr/bin/env python3
"""Check that the manual V1 review register matches the current Chapter 2.4 cards."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
STORIES = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories/user-stories.md"
REGISTER = REPO_ROOT / "delivery-checklists/mobile-v1-story-verification-register.md"
V1_IDS = (
    "MOB-US-001", "MOB-US-002", "MOB-US-003", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017",
    "MOB-US-019", "MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023",
    "MOB-US-024", "MOB-US-025", "MOB-US-026", "MOB-US-027", "MOB-US-028",
    "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034", "MOB-US-044",
    "MOB-US-047", "MOB-US-048", "MOB-US-049",
)
EXPECTED_ACTORS = {
    **{story_id: "Mobile User" for story_id in V1_IDS[:3]},
    **{story_id: "Warehouse Operator" for story_id in V1_IDS[3:11]},
    **{story_id: "Dispatch Coordinator" for story_id in V1_IDS[11:17]},
    **{story_id: "Driver or Delivery Operator" for story_id in V1_IDS[17:24]},
    **{story_id: "Customer Buyer" for story_id in V1_IDS[24:]},
}
EXPECTED_SEGMENTS = {
    **{story_id: "S1-S3" for story_id in V1_IDS[:3]},
    **{story_id: "S1" for story_id in V1_IDS[3:17]},
    **{story_id: "S2" for story_id in V1_IDS[17:24]},
    **{story_id: "S3" for story_id in V1_IDS[24:]},
}
EXPECTED_LEADS = {
    **{story_id: "Diego / DiegoS284" for story_id in V1_IDS[:3]},
    **{story_id: "Gino / R0obxdnt" for story_id in V1_IDS[3:11]},
    **{story_id: "Diego / DiegoS284" for story_id in V1_IDS[11:17]},
    **{story_id: "Gerard / GerardRojasMancilla" for story_id in V1_IDS[17:24]},
    **{story_id: "Sebastián / spinedo214" for story_id in V1_IDS[24:]},
}


def register_rows(text: str) -> list[list[str]]:
    start = text.index("## Register")
    end = text.index("## Current result", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        values = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if values and re.fullmatch(r"MOB-US-\d{3}", values[0]):
            rows.append(values)
    return rows


def story_actors(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^#### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    records: dict[str, str] = {}
    for index, match in enumerate(matches):
        block = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        row = re.search(
            r"<tr><td>(MOB-US-\d{3})</td><td>(.+?)</td><td>(?:Critical|High|Medium|Low|Future)</td><td>",
            block,
            re.DOTALL,
        )
        if row:
            records[row.group(1)] = row.group(2)
    return records


def main() -> int:
    failures: list[str] = []
    if not STORIES.is_file() or not REGISTER.is_file():
        print("mobile V1 review register validation: BLOCKED; missing report or register")
        return 2

    actors = story_actors(STORIES.read_text(encoding="utf-8"))
    reviews = register_rows(REGISTER.read_text(encoding="utf-8"))
    if [row[0] for row in reviews] != list(V1_IDS):
        failures.append("manual review register IDs/order differ from the canonical 28 V1 stories")
    if len(reviews) != 28:
        failures.append(f"review register rows: expected 28, got {len(reviews)}")

    for row in reviews:
        if len(row) != 8:
            failures.append(f"{row[0]}: expected eight review columns")
            continue
        story_id, actor_segment, bounded_context, lead, source, acceptance, evidence, decision = row
        expected_actor = EXPECTED_ACTORS.get(story_id)
        if actors.get(story_id) != expected_actor:
            failures.append(f"{story_id}: card actor={actors.get(story_id)!r}, expected={expected_actor!r}")
        if actor_segment != f"{expected_actor} / {EXPECTED_SEGMENTS[story_id]}":
            failures.append(f"{story_id}: register actor/segment is not current")
        if not re.fullmatch(r"BC-\d{2} — .+", bounded_context):
            failures.append(f"{story_id}: missing explicit owning Bounded Context")
        if lead != EXPECTED_LEADS[story_id]:
            failures.append(f"{story_id}: manual review lead differs from the approved allocation")
        if not all((source, acceptance, evidence, decision)):
            failures.append(f"{story_id}: manual review fields must remain present")

    if failures:
        print("mobile V1 review register validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("mobile V1 review register OK: rows=28; roles and manual review boundary retained")
    return 0


if __name__ == "__main__":
    sys.exit(main())
