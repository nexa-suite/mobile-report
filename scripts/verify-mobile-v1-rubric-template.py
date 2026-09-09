#!/usr/bin/env python3
"""Verify the academic format of the 73 Mobile functional story cards."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
STORIES = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories/user-stories.md"


def blueprint_root() -> Path:
    explicit = os.environ.get("NEXA_BLUEPRINT_ROOT")
    if explicit:
        return Path(explicit)
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "--git-common-dir"],
        check=False,
        capture_output=True,
        text=True,
    )
    candidates = [REPO_ROOT.parent / "blueprint"]
    if result.returncode == 0:
        common = Path(result.stdout.strip())
        if not common.is_absolute():
            common = REPO_ROOT / common
        candidates.extend(ancestor / "blueprint" for ancestor in common.resolve().parents)
    return next((candidate for candidate in candidates if candidate.is_dir()), candidates[0])


MASTER = blueprint_root() / "03-mobile/requirements/master-mobile-backlog.md"


def master_ids() -> list[str]:
    return re.findall(r"^\| (MOB-US-\d{3}) \|", MASTER.read_text(encoding="utf-8"), re.MULTILINE)


def story_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^#### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    return [
        (match.group(1), text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)])
        for index, match in enumerate(matches)
    ]


def main() -> int:
    if not STORIES.is_file() or not MASTER.is_file():
        print("mobile story rubric validation: BLOCKED; missing story catalog or Blueprint master")
        return 2

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
            "<table>",
            "<thead>",
            "<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>",
            f"<tr><td>{story_id}</td>",
            "<tr><th>Title</th><td colspan=\"3\">",
            "<tr><th colspan=\"4\">Description</th></tr>",
            "<tr><th colspan=\"4\">Acceptance Criteria</th></tr>",
            "<tr><td colspan=\"4\">",
            "</tbody>",
            "</table>",
        )
        for marker in required:
            if marker not in block:
                failures.append(f"{story_id}: missing {marker}")
        description = re.search(r"<tr><td colspan=\"4\">(Como .+?)</td></tr>", block, re.DOTALL)
        if not description:
            failures.append(f"{story_id}: description cell is missing")
        if not re.search(
            rf"<tr><td>{re.escape(story_id)}</td><td>.+?</td><td>(?:Critical|High|Medium|Low|Future)</td><td>.+?</td></tr>",
            block,
            re.DOTALL,
        ):
            failures.append(f"{story_id}: card priority or metadata row missing")
        scenarios = re.findall(r"<p><strong>Scenario: .+?</strong></p>", block)
        if len(scenarios) < 2:
            failures.append(f"{story_id}: expected at least two meaningful Gherkin scenarios, got {len(scenarios)}")
        for keyword in ("Given", "When", "Then"):
            marker = f"<p><strong>{keyword}</strong>"
            if block.count(marker) < len(scenarios):
                failures.append(f"{story_id}: missing Gherkin {keyword}")
        if "| Story ID | User | Priority | Epic |" in block or "| **Acceptance Criteria** |" in block:
            failures.append(f"{story_id}: legacy Markdown story table remains")

    if len(blocks) != 73:
        failures.append(f"expected 73 detailed functional records, got {len(blocks)}")

    if failures:
        print("mobile story rubric validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    scenarios = len(re.findall(r"<p><strong>Scenario: .+?</strong></p>", text))
    print(f"mobile story rubric validation OK: records=73; scenarios={scenarios}; source=Blueprint master")
    return 0


if __name__ == "__main__":
    sys.exit(main())
