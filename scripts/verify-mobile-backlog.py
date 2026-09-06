#!/usr/bin/env python3
"""Validate the 12-Epic, 73-story Mobile report transcription."""

from __future__ import annotations

import html
import re
import sys
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_ROOT = REPORT_ROOT.parent / "blueprint"
MASTER = BLUEPRINT_ROOT / "03-mobile/requirements/master-mobile-backlog.md"
CATALOG = BLUEPRINT_ROOT / "03-mobile/requirements/mobile-v1-catalog.md"
STORIES = REPORT_ROOT / (
    "report/02-requirements-and-software-solution-design/"
    "2.4-requirements-specification/2.4.1-user-stories.md"
)
BACKLOG = REPORT_ROOT / (
    "report/02-requirements-and-software-solution-design/"
    "2.4-requirements-specification/2.4.3-product-backlog.md"
)

BC_NAMES = {
    "BC-01": "Tenant & Access Governance",
    "BC-02": "Customer & Buyer Relationships",
    "BC-03": "Catalog & Commercial Policy",
    "BC-04": "Sales Commitment",
    "BC-05": "Inventory Availability",
    "BC-06": "Fulfillment & Delivery",
    "BC-07": "Credit & Receivables",
    "BC-08": "Payments",
    "BC-09": "Business Documents",
    "BC-10": "Notifications",
    "BC-11": "Business Traceability",
}

EPIC_TITLES = {
    "MOBILE-EPIC-01": "Safe Access & Work Context",
    "MOBILE-EPIC-02": "Warehouse Receiving, Identification & Picking",
    "MOBILE-EPIC-03": "Dispatch Preparation & Handoff",
    "MOBILE-EPIC-04": "Driver Delivery Execution & Proof",
    "MOBILE-EPIC-05": "Delivery Handoff, Buyer Receipt & Critical Updates",
    "MOBILE-EPIC-06": "Commercial & Operational Mobile Convenience",
    "MOBILE-EPIC-07": "Advanced Field Mobility & Offline Operations",
    "MOBILE-EPIC-08": "Warehouse Transfer & Inventory Accuracy",
    "MOBILE-EPIC-09": "Dispatch Exception & Delivery Coordination",
    "MOBILE-EPIC-10": "Buyer Delivery Continuity",
    "MOBILE-EPIC-11": "Mobile Commercial & Financial Follow-through",
    "MOBILE-EPIC-12": "Future Intelligent Field Operations",
}

# MOB-US-073 is a canonical User Story whose three source Outcome Conditions
# are rendered as Gherkin scenarios without adding product behavior.
REPORT_SCENARIO_OVERRIDES = {"MOB-US-073": 3}


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def read_master() -> list[dict[str, str]]:
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in MASTER.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ID | Title | Actor |"):
            headers = cells(line)
        elif headers and line.startswith("| MOB-US-"):
            values = cells(line)
            if len(values) == len(headers):
                rows.append(dict(zip(headers, values)))
    return rows


def read_catalog() -> dict[str, dict[str, object]]:
    text = CATALOG.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## (MOB-US-\d{3}) — (.+)$", text, re.MULTILINE))
    result: dict[str, dict[str, object]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end]
        result[match.group(1)] = {
            "title": match.group(2).strip(),
            "scenarios": re.findall(r"^- (Scenario: .+)$", block, re.MULTILINE),
        }
    return result


def report_story_blocks(text: str) -> dict[str, tuple[str, str]]:
    matches = list(re.finditer(r"^### (MOB-US-\d{3}) — (.+)$", text, re.MULTILINE))
    return {
        match.group(1): (
            match.group(2).strip(),
            text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)],
        )
        for index, match in enumerate(matches)
    }


def report_table_rows(text: str, start_heading: str, end_heading: str) -> list[list[str]]:
    start = text.index(start_heading)
    end = text.index(end_heading, start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if line.startswith("| ") and "MOB-US-" in line:
            values = cells(line)
            if values and re.fullmatch(r"\d+", values[0]):
                rows.append(values)
    return rows


def validate() -> list[str]:
    failures: list[str] = []
    master = read_master()
    catalog = read_catalog()
    report_text = STORIES.read_text(encoding="utf-8")
    backlog_text = BACKLOG.read_text(encoding="utf-8")
    blocks = report_story_blocks(report_text)

    if len(master) != 73:
        failures.append(f"master rows: expected 73, got {len(master)}")
    if len(catalog) != 73:
        failures.append(f"catalog stories: expected 73, got {len(catalog)}")

    source_ids = [row["ID"] for row in master]
    if len(set(source_ids)) != 73:
        failures.append("master contains duplicate or missing story IDs")
    if set(source_ids) != set(catalog):
        failures.append("master and catalog story ID sets differ")

    epic_start = report_text.index("## Inventario de Epics")
    epic_end = report_text.index("## Backlog summary", epic_start)
    epic_lines = report_text[epic_start:epic_end].splitlines()
    epic_header = "| Epic ID | Title | Description | User Stories |"
    if epic_header not in epic_lines:
        failures.append("Epic table does not use the required four columns")
    epic_rows = [
        cells(line)
        for line in epic_lines
        if line.startswith("| MOBILE-EPIC-")
    ]
    if len(epic_rows) != 12:
        failures.append(f"Epic rows: expected 12, got {len(epic_rows)}")
    expected_epic_membership: dict[str, list[str]] = {epic_id: [] for epic_id in EPIC_TITLES}
    for row in master:
        expected_epic_membership[row["Epic"]].append(row["ID"])
    for row in epic_rows:
        if len(row) != 4:
            failures.append(f"Epic row has wrong column count: {row!r}")
            continue
        epic_id, title, description, story_text = row
        if epic_id not in EPIC_TITLES:
            failures.append(f"unknown Epic ID: {epic_id}")
            continue
        if title != EPIC_TITLES[epic_id]:
            failures.append(f"{epic_id} title differs from the live registry")
        actual_ids = [value.strip() for value in story_text.split(",")]
        if actual_ids != expected_epic_membership[epic_id]:
            failures.append(f"{epic_id} story membership differs from the live registry")
        if not description or not re.search(r"[áéíóúñ]", description, re.IGNORECASE):
            failures.append(f"{epic_id} description is not presented in Spanish")

    v1_rows = report_table_rows(report_text, "## Backlog summary", "## Story records")
    expected_v1 = [row for row in master if row["Target Release"] == "V1"]
    if len(v1_rows) != 28:
        failures.append(f"V1 summary rows: expected 28, got {len(v1_rows)}")
    if [row[1] for row in v1_rows] != [row["ID"] for row in expected_v1]:
        failures.append("V1 summary IDs/order differ from the live lifecycle index")
    for actual, expected in zip(v1_rows, expected_v1):
        if len(actual) != 8:
            failures.append(f"{expected['ID']} V1 summary has wrong column count")
            continue
        comparisons = {
            "actor": (actual[2], expected["Actor"]),
            "priority": (actual[3], expected["Priority"]),
            "epic": (actual[4], f"{expected['Epic']} — {EPIC_TITLES[expected['Epic']]}"),
            "points": (actual[5], expected["Story Points"]),
            "sprint": (actual[6], expected["Sprint Planned"]),
            "bounded context": (actual[7], f"{expected['Primary BC']} — {BC_NAMES[expected['Primary BC']]}"),
        }
        for field, (actual_value, expected_value) in comparisons.items():
            if actual_value != expected_value:
                failures.append(
                    f"{expected['ID']} {field}: report={actual_value!r}, expected={expected_value!r}"
                )

    if len(blocks) != 73:
        failures.append(f"story records: expected 73 headings, got {len(blocks)}")
    if list(blocks) != source_ids:
        failures.append("story heading IDs/order differ from the live lifecycle index")

    for row in master:
        story_id = row["ID"]
        title, block = blocks.get(story_id, ("", ""))
        if not block:
            continue
        if title != row["Title"]:
            failures.append(f"{story_id} title differs from the live lifecycle index")
        if block.count("<table>") != 1:
            failures.append(f"{story_id} must contain exactly one HTML table")
        required_header = "<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>"
        if required_header not in block:
            failures.append(f"{story_id} missing required four-column story header")
        for forbidden in (
            "Points",
            "Sprint",
            "Owning Bounded Context",
            "Canonical user story",
            "Source file",
            "Verification status",
        ):
            if f"<th>{forbidden}</th>" in block or f"<th colspan=\"4\">{forbidden}</th>" in block:
                failures.append(f"{story_id} contains forbidden academic-table field: {forbidden}")
        source_scenarios = len(catalog[story_id]["scenarios"])
        expected_scenarios = REPORT_SCENARIO_OVERRIDES.get(story_id, source_scenarios)
        actual_scenarios = len(re.findall(r"<strong>Scenario:", block))
        if actual_scenarios != expected_scenarios:
            failures.append(
                f"{story_id} scenarios: report={actual_scenarios}, expected={expected_scenarios}"
            )
        if expected_scenarios:
            scenario_segments = re.findall(
                r"<strong>Scenario:.*?(?=<strong>Scenario:|</td>)",
                block,
                re.DOTALL,
            )
            for segment in scenario_segments:
                for keyword in ("Given", "When", "Then"):
                    if f"<strong>{keyword}</strong>" not in segment:
                        failures.append(f"{story_id} scenario missing Gherkin keyword {keyword}")
            criteria_start = block.find("<tr><th colspan=\"4\">Acceptance Criteria</th></tr>")
            criteria = block[criteria_start:] if criteria_start >= 0 else ""
            if not re.search(r"[áéíóúñ]", criteria, re.IGNORECASE):
                failures.append(f"{story_id} acceptance criteria lack Spanish prose")
            if story_id == "MOB-US-073":
                criteria = block[block.find("<tr><th colspan=\"4\">Acceptance Criteria</th></tr>"):]
                for anchor in (
                    "resultado valioso de almacén",
                    "atribuible y revisable",
                    "RFID, scanner, sensor, label ni telemetry",
                ):
                    if anchor not in criteria:
                        failures.append(f"MOB-US-073 missing reconciled Outcome Condition: {anchor}")

    backlog_rows = report_table_rows(backlog_text, "## Índice completo del ciclo de vida", "## Estado de evidencia")
    if len(backlog_rows) != 73:
        failures.append(f"Product Backlog lifecycle rows: expected 73, got {len(backlog_rows)}")
    if [row[1] for row in backlog_rows] != source_ids:
        failures.append("Product Backlog IDs/order differ from the live lifecycle index")
    expected_releases = {"V1": 28, "V2": 35, "V3": 9, "V4_FUTURE": 1}
    release_counts = {release: 0 for release in expected_releases}
    for row in backlog_rows:
        if len(row) >= 6:
            release_counts[row[5]] = release_counts.get(row[5], 0) + 1
    if release_counts != expected_releases:
        failures.append(f"Product Backlog release counts: report={release_counts}, expected={expected_releases}")
    if "73 historias" not in backlog_text:
        failures.append("Product Backlog does not state the complete 73-story inventory")

    total_scenarios = len(re.findall(r"<strong>Scenario:", report_text))
    source_scenarios = sum(len(value["scenarios"]) for value in catalog.values())
    expected_total_scenarios = source_scenarios + sum(REPORT_SCENARIO_OVERRIDES.values())
    if source_scenarios != 256:
        failures.append(f"source catalog scenarios: expected 256, got {source_scenarios}")
    if total_scenarios != expected_total_scenarios:
        failures.append(
            f"report Gherkin scenarios: expected {expected_total_scenarios}, got {total_scenarios}"
        )

    return failures


def main() -> int:
    failures = validate()
    if failures:
        print("mobile backlog validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    report_text = STORIES.read_text(encoding="utf-8")
    total_scenarios = len(re.findall(r"<strong>Scenario:", report_text))
    print(
        "mobile backlog validation OK: epics=12 stories=73 V1=28 releases=28/35/9/1 "
        f"source_scenarios=256 rendered_gherkin_scenarios={total_scenarios}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
