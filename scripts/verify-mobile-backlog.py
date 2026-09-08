#!/usr/bin/env python3
"""Validate the complete Chapter 2.4 Mobile backlog projection."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT_ROOT = Path(os.environ.get("NEXA_BLUEPRINT_ROOT", REPO_ROOT.parent / "blueprint"))
MASTER = BLUEPRINT_ROOT / "03-mobile/requirements/master-mobile-backlog.md"
STORY_DIR = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification"
STORIES = STORY_DIR / "2.4.1-user-stories.md"
IMPACT = STORY_DIR / "2.4.2-impact-mapping.md"
BACKLOG = STORY_DIR / "2.4.3-product-backlog.md"

EXPECTED_PRIORITY = {"Alta", "Media", "Baja"}
EXPECTED_SPRINTS = {"S1", "S2", "S3", "S4", "Future"}
EXPECTED_TECHNICAL = {f"TS-MOB-{number:03d}" for number in range(1, 13)}
EXPECTED_SPIKES = {f"SPIKE-{number:03d}" for number in range(1, 7)}
EXPECTED_LANDING = {f"LAND-US-{number:03d}" for number in range(1, 7)}
EXPECTED_V1 = {
    "MOB-US-001", "MOB-US-002", "MOB-US-003", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017",
    "MOB-US-019", "MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023",
    "MOB-US-024", "MOB-US-025", "MOB-US-026", "MOB-US-027", "MOB-US-028",
    "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034", "MOB-US-044",
    "MOB-US-047", "MOB-US-048", "MOB-US-049",
}
EXPECTED_BACKLOG_ORDER = [
    "LAND-US-001", "LAND-US-002", "LAND-US-003", "LAND-US-004",
    "LAND-US-005", "LAND-US-006", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014",
    "MOB-US-015", "MOB-US-016", "MOB-US-017", "MOB-US-019",
    "MOB-US-022", "MOB-US-023", "MOB-US-024", "MOB-US-020",
    "MOB-US-021", "MOB-US-025", "MOB-US-026", "MOB-US-027",
    "MOB-US-028", "MOB-US-031", "MOB-US-032", "MOB-US-033",
    "MOB-US-034", "MOB-US-044", "MOB-US-047", "MOB-US-048",
    "MOB-US-049", "MOB-US-001", "MOB-US-002", "MOB-US-003",
    "TS-MOB-001", "TS-MOB-010", "SPIKE-002", "TS-MOB-005",
    "TS-MOB-006", "TS-MOB-007", "TS-MOB-008", "MOB-US-004",
    "MOB-US-005", "MOB-US-006",
    "MOB-US-007", "MOB-US-008", "MOB-US-009", "MOB-US-010",
    "MOB-US-018", "MOB-US-030", "MOB-US-035", "MOB-US-050",
    "MOB-US-051", "MOB-US-052", "MOB-US-053", "MOB-US-057",
    "MOB-US-058", "MOB-US-061", "MOB-US-062", "MOB-US-063",
    "MOB-US-064", "MOB-US-065", "MOB-US-036", "MOB-US-037",
    "MOB-US-038", "MOB-US-040", "MOB-US-042", "MOB-US-043",
    "MOB-US-046", "MOB-US-039", "MOB-US-041", "TS-MOB-002",
    "TS-MOB-003", "TS-MOB-004", "TS-MOB-009", "TS-MOB-011",
    "TS-MOB-012", "SPIKE-001", "SPIKE-003", "SPIKE-004",
    "SPIKE-005", "SPIKE-006", "MOB-US-045", "MOB-US-067",
    "MOB-US-068", "MOB-US-069", "MOB-US-070", "MOB-US-071",
    "MOB-US-072", "MOB-US-054", "MOB-US-055", "MOB-US-056",
    "MOB-US-059", "MOB-US-060", "MOB-US-066", "MOB-US-029",
    "MOB-US-073",
]
RESTRICTED_ACADEMIC_TOKENS = (
    "PROPOSED",
    "PARTIAL",
    "COVERED",
    "PARTIALLY COVERED",
    "NEEDS OWNER FOLLOW-UP",
    "RESEARCH VALIDATION PENDING",
    "NOT PRODUCT SCOPE",
    "TARGET /",
    "PLANNED;",
    "OPEN /",
    "FUTURE / UNASSIGNED",
    "owner follow-up",
    "acceptance pending",
    "evidence boundary",
    "AS-IS evidence register",
    "route inventory",
    "baseline hash",
    "dirty checkout",
    "no acceptance claimed",
    "no implementation claim",
    "Product Acceptance pending",
    "System Acceptance",
    "Production Readiness",
    "source-backed",
    "reconciliation gate",
)


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


def story_blocks(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^##### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    return {
        match.group(1): text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        for index, match in enumerate(matches)
    }


def backlog_rows(text: str) -> list[list[str]]:
    start = text.index("## Índice completo")
    end = text.index("## Sprints planificados", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if not re.match(r"^\| \d+ \|", line):
            continue
        values = cells(line)
        if len(values) == 5:
            rows.append(values)
    return rows


def validate() -> list[str]:
    failures: list[str] = []
    master = read_master()
    story_text = STORIES.read_text(encoding="utf-8")
    backlog_text = BACKLOG.read_text(encoding="utf-8")
    blocks = story_blocks(story_text)
    source_ids = [row["ID"] for row in master]
    expected_ids = set(source_ids)

    if len(master) != 73:
        failures.append(f"master rows: expected 73, got {len(master)}")
    if len(set(source_ids)) != 73:
        failures.append("master contains duplicate or missing story IDs")
    if list(blocks) != source_ids:
        failures.append("2.4.1 story IDs/order differ from the canonical catalog order")
    if set(blocks) != expected_ids:
        failures.append(f"2.4.1 story set: expected 73, got {len(blocks)}")

    for story_id, block in blocks.items():
        for marker in (
            "| Story ID | User | Priority | Epic |",
            "**Title:**",
            "**Description:** Como ",
            "**Acceptance Criteria**",
        ):
            if marker not in block:
                failures.append(f"{story_id}: missing {marker}")
        description_match = re.search(r"^\*\*Description:\*\* (.+)$", block, re.MULTILINE)
        if not description_match or not re.fullmatch(r"Como .+, deseo .+, para .+\.", description_match.group(1).strip()):
            failures.append(f"{story_id}: description must use 'Como ..., deseo ..., para ... .'")
        if not re.search(r"^\| MOB-US-\d{3} \| .+ \| (Alta|Media|Baja) \| .+ \|$", block, re.MULTILINE):
            failures.append(f"{story_id}: required fields or Spanish priority missing")
        scenarios = re.findall(r"\*\*Scenario: .+?\*\*", block)
        if len(scenarios) < 2:
            failures.append(f"{story_id}: fewer than two meaningful Gherkin scenarios")
        for keyword in ("**Given**", "**When**", "**Then**"):
            if block.count(keyword) < len(scenarios):
                failures.append(f"{story_id}: Gherkin keyword count missing {keyword}")

    app_mentions = set(re.findall(r"Nexa (?:Operations|Buyer) Mobile", story_text))
    if app_mentions != {"Nexa Operations Mobile", "Nexa Buyer Mobile"}:
        failures.append(f"product apps differ from the two-app model: {sorted(app_mentions)}")
    if re.search(r"\bP[0-9]\b", story_text):
        failures.append("numeric priority labels remain in 2.4.1")
    if "DIRECT_ORDER" not in story_text or "borrador de Ventas" not in story_text:
        failures.append("Direct Order reconciliation is missing from 2.4.1")

    rows = backlog_rows(backlog_text)
    if len(rows) != 97:
        failures.append(f"Product Backlog rows: expected 97, got {len(rows)}")
    if len({row[1] for row in rows}) != len(rows):
        failures.append("Product Backlog contains duplicate IDs")
    expected_backlog_ids = expected_ids | EXPECTED_LANDING | EXPECTED_TECHNICAL | EXPECTED_SPIKES
    actual_backlog_ids = {row[1] for row in rows}
    if actual_backlog_ids != expected_backlog_ids:
        failures.append("Product Backlog ID union differs from 73 Mobile + 6 Landing + 12 Technical + 6 Spike")
    actual_backlog_order = [row[1] for row in rows]
    if actual_backlog_order != EXPECTED_BACKLOG_ORDER:
        failures.append("Product Backlog order is not the approved global business-value sequence")
    for row in rows:
        if row[3] not in {"1", "2", "3", "5", "8"}:
            failures.append(f"{row[1]} has invalid story points: {row[3]}")
        if row[4] not in EXPECTED_SPRINTS:
            failures.append(f"{row[1]} has invalid Sprint: {row[4]}")
    if "| # Orden | User Story Id | Título | Story Points (1 / 2 / 3 / 5 / 8) | Sprint |" not in backlog_text:
        failures.append("Product Backlog main table does not use the required five columns")
    for sprint in ("S1", "S2", "S3", "S4", "Future"):
        if not re.search(rf"^\| {sprint} \|", backlog_text, re.MULTILINE):
            failures.append(f"Product Backlog missing Sprint row {sprint}")

    landing_ids = set(re.findall(r"^##### (LAND-US-\d{3}) —", story_text, re.MULTILINE))
    if landing_ids != EXPECTED_LANDING:
        failures.append("Landing story set differs from LAND-US-001..006")

    technical_ids = set(re.findall(r"^#### (TS-MOB-\d{3}) —", story_text, re.MULTILINE))
    if technical_ids != EXPECTED_TECHNICAL:
        failures.append("Technical Story set differs from TS-MOB-001..012")
    for marker in ("Developer", "Story points", "Planned Sprint", "Acceptance Criteria"):
        if marker not in story_text:
            failures.append(f"Technical Stories missing {marker}")
    for technology in ("Android Native/Kotlin", "Flutter/Dart", "iOS Native/SwiftUI"):
        if technology not in story_text:
            failures.append(f"Technical Stories missing accepted technology {technology}")
    if "Liquid Glass" not in story_text:
        failures.append("Technical Stories do not limit Liquid Glass to presentation")

    spike_ids = set(re.findall(r"^#### (SPIKE-\d{3}) —", story_text, re.MULTILINE))
    if spike_ids != EXPECTED_SPIKES:
        failures.append("Spike Story set differs from SPIKE-001..006")
    for marker in ("Objective", "Question", "Expected artifact", "Completion criteria"):
        if marker not in story_text:
            failures.append(f"Spike Stories missing {marker}")
    spike_002 = story_text[story_text.index("#### SPIKE-002") : story_text.index("#### SPIKE-003")]
    if not all(term in spike_002 for term in ("Android Native/Kotlin", "Flutter/Dart", "iOS Native/SwiftUI")):
        failures.append("SPIKE-002 does not compare all three accepted technologies")
    if re.search(r"Question.*(elegir|seleccionar una única|qué tecnología escoger)", spike_002, re.IGNORECASE):
        failures.append("SPIKE-002 is framed as a single-framework selection question")

    impact_text = IMPACT.read_text(encoding="utf-8")
    impact_story_ids = set(re.findall(r"\bMOB-US-\d{3}\b", impact_text))
    if impact_story_ids != EXPECTED_V1:
        failures.append("Impact Mapping must retain exactly the 28 Mobile V1 story references")
    story_descriptions = {
        story_id: match.group(1).strip()
        for story_id, block in blocks.items()
        if (match := re.search(r"^\*\*Description:\*\* (.+)$", block, re.MULTILINE))
    }
    for story_id in EXPECTED_V1:
        if story_descriptions.get(story_id) not in impact_text:
            failures.append(f"Impact Mapping must retain the full description for {story_id}")
    if any(token.lower() in impact_text.lower() for token in ("[baseline]", "[target]", "[metric]", "[time window]", "[ ]", "SMART completion template", "Tool capture")):
        failures.append("Impact Mapping contains placeholders or checklist content")

    academic_files = (STORIES, IMPACT, BACKLOG)
    for path in academic_files:
        text = path.read_text(encoding="utf-8")
        for token in RESTRICTED_ACADEMIC_TOKENS:
            if token.lower() in text.lower():
                failures.append(f"restricted professor-facing token in {path.name}: {token}")
        if re.search(r"\bP[0-9]\b", text):
            failures.append(f"numeric priority label in {path.name}")
        if "2.4.4-technical-stories" in text or "2.4.0-to-be-scenario-mapping" in text:
            failures.append(f"obsolete Chapter 2.4 filename in {path.name}")

    return failures


def main() -> int:
    required = (MASTER, STORIES, IMPACT, BACKLOG)
    if not all(path.is_file() for path in required):
        missing = [str(path) for path in required if not path.is_file()]
        print("mobile backlog validation: BLOCKED; missing files")
        for path in missing:
            print(f"- {path}")
        return 2
    failures = validate()
    if failures:
        print("mobile backlog validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    story_text = STORIES.read_text(encoding="utf-8")
    scenario_count = len(re.findall(r"\*\*Scenario: .+?\*\*", story_text))
    print(f"mobile backlog validation OK: functional_stories=73; backlog_rows=97; rendered_scenarios={scenario_count}; sprints=S1/S2/S3/S4/Future")
    return 0


if __name__ == "__main__":
    sys.exit(main())
