#!/usr/bin/env python3
"""Verify the academic story format for all 73 Mobile functional stories."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
STORIES = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
MASTER = REPO_ROOT.parent / "blueprint/03-mobile/requirements/master-mobile-backlog.md"


def master_ids() -> list[str]:
    return re.findall(r"^\| (MOB-US-\d{3}) \|", MASTER.read_text(encoding="utf-8"), re.MULTILINE)


def story_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^##### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    return [
        (match.group(1), text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)])
        for index, match in enumerate(matches)
    ]


def main() -> int:
    text = STORIES.read_text(encoding="utf-8")
    blocks = story_blocks(text)
    failures: list[str] = []
    expected_ids = master_ids()
    actual_ids = [story_id for story_id, _ in blocks]

    if len(expected_ids) != 73:
        failures.append(f"canonical functional story count: expected 73, got {len(expected_ids)}")
    if actual_ids != expected_ids:
        failures.append("functional story IDs/order do not match the canonical catalog")

    for story_id, block in blocks:
        required = (
            "| Story ID | Persona | Producto | Priority | Epic |",
            f"| {story_id} |",
            "**Title:**",
            "**Description:** Como ",
            "**Acceptance Criteria**",
        )
        for marker in required:
            if marker not in block:
                failures.append(f"{story_id}: missing {marker}")
        description_match = re.search(r"^\*\*Description:\*\* (.+)$", block, re.MULTILINE)
        if not description_match or not re.fullmatch(r"Como .+, deseo .+, para .+\.", description_match.group(1).strip()):
            failures.append(f"{story_id}: description must use 'Como ..., deseo ..., para ... .'")
        if not re.search(r"\| (Alta|Media|Baja) \|", block):
            failures.append(f"{story_id}: priority must be Alta, Media or Baja")
        scenarios = re.findall(r"\*\*Scenario: .+?\*\*", block)
        if len(scenarios) < 2:
            failures.append(f"{story_id}: expected at least two meaningful scenarios, got {len(scenarios)}")
        for keyword in ("**Given**", "**When**", "**Then**"):
            if block.count(keyword) < len(scenarios):
                failures.append(f"{story_id}: missing Gherkin {keyword}")
        if "<table>" in block or "Status" in block or re.search(r"\bP[0-9]\b", block):
            failures.append(f"{story_id}: legacy internal table or numeric priority remains")

    if len(blocks) != 73:
        failures.append(f"expected 73 detailed functional records, got {len(blocks)}")

    if failures:
        print("mobile story rubric validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    scenarios = len(re.findall(r"\*\*Scenario: .+?\*\*", text))
    print(f"mobile story rubric validation OK: records=73; required_fields=7; scenarios={scenarios}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
