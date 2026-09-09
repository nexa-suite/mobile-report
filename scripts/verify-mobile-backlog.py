#!/usr/bin/env python3
"""Validate the reconciled Chapter 2.4 Mobile backlog and its evidence boundaries."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def resolve_blueprint_root() -> Path:
    explicit = os.environ.get("NEXA_BLUEPRINT_ROOT")
    if explicit:
        return Path(explicit)
    for ancestor in (REPO_ROOT, *REPO_ROOT.parents):
        candidate = ancestor / "blueprint"
        if candidate.is_dir():
            return candidate
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "--git-common-dir"],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        common_dir = Path(result.stdout.strip())
        if not common_dir.is_absolute():
            common_dir = REPO_ROOT / common_dir
        for ancestor in common_dir.resolve().parents:
            candidate = ancestor / "blueprint"
            if candidate.is_dir():
                return candidate
    return REPO_ROOT.parent / "blueprint"


BLUEPRINT_ROOT = resolve_blueprint_root()
MASTER = BLUEPRINT_ROOT / "03-mobile/requirements/master-mobile-backlog.md"
CHAPTER = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification"
FUNCTIONAL = CHAPTER / "2.4.1-user-stories/user-stories.md"
OVERVIEW = FUNCTIONAL
TECHNICAL = CHAPTER / "2.4.1-user-stories/technical-stories.md"
SPIKES = CHAPTER / "2.4.1-user-stories/spike-stories.md"
IMPACT = CHAPTER / "2.4.2-impact-mapping.md"
BACKLOG = CHAPTER / "2.4.3-product-backlog.md"

EXPECTED_V1 = {
    "MOB-US-001", "MOB-US-002", "MOB-US-003", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017",
    "MOB-US-019", "MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023",
    "MOB-US-024", "MOB-US-025", "MOB-US-026", "MOB-US-027", "MOB-US-028",
    "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034", "MOB-US-044",
    "MOB-US-047", "MOB-US-048", "MOB-US-049",
}
EXPECTED_LANDING = {f"LAND-US-{number:03d}" for number in range(1, 7)}
EXPECTED_TECHNICAL = {f"TS-MOB-{number:03d}" for number in range(1, 13)}
EXPECTED_SPIKES = {f"SPIKE-{number:03d}" for number in range(1, 7)}
HEADING = re.compile(r"^#### ((?:LAND-US|MOB-US|TS-MOB|SPIKE)-\d{3}) — (.+)$", re.MULTILINE)


def cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def headings(path: Path) -> dict[str, str]:
    return {match.group(1): match.group(2) for match in HEADING.finditer(path.read_text(encoding="utf-8"))}


def master_rows() -> dict[str, dict[str, str]]:
    headers: list[str] | None = None
    rows: dict[str, dict[str, str]] = {}
    for line in MASTER.read_text(encoding="utf-8").splitlines():
        if line.startswith("| ID | Title |"):
            headers = cells(line)
        elif headers and line.startswith("| MOB-US-"):
            values = cells(line)
            if len(values) == len(headers):
                row = dict(zip(headers, values))
                rows[row["ID"]] = row
    return rows


def backlog_rows() -> list[list[str]]:
    text = BACKLOG.read_text(encoding="utf-8")
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


def impact_ids(text: str) -> set[str]:
    found = set(re.findall(r"\bMOB-US-\d{3}\b", text))
    for start, end in re.findall(r"MOB-US-(\d{3})\.\.(\d{3})", text):
        found.update(f"MOB-US-{number:03d}" for number in range(int(start), int(end) + 1))
    return found


def validate() -> list[str]:
    required = (MASTER, OVERVIEW, FUNCTIONAL, TECHNICAL, SPIKES, IMPACT, BACKLOG)
    failures = [f"missing required artifact: {path}" for path in required if not path.is_file()]
    if failures:
        return failures

    master = master_rows()
    functional_all = headings(FUNCTIONAL)
    functional = {story_id: title for story_id, title in functional_all.items() if story_id.startswith("MOB-US-")}
    landing = {story_id: title for story_id, title in functional_all.items() if story_id.startswith("LAND-US-")}
    technical = headings(TECHNICAL)
    spikes = headings(SPIKES)
    all_headings = {**functional_all, **technical, **spikes}
    rows = backlog_rows()
    row_by_id = {row[1]: row for row in rows}
    master_ids = set(master)
    expected_ids = master_ids | EXPECTED_LANDING | EXPECTED_TECHNICAL | EXPECTED_SPIKES

    if len(master) != 73:
        failures.append(f"canonical functional inventory: expected 73, got {len(master)}")
    if set(functional) != master_ids:
        failures.append("functional story headings differ from the canonical Mobile inventory")
    if set(landing) != EXPECTED_LANDING:
        failures.append("Landing story headings differ from LAND-US-001..006")
    if set(technical) != EXPECTED_TECHNICAL:
        failures.append("technical story headings differ from TS-MOB-001..012")
    if set(spikes) != EXPECTED_SPIKES:
        failures.append("spike story headings differ from SPIKE-001..006")
    if len(rows) != 97:
        failures.append(f"backlog rows: expected 97, got {len(rows)}")
    if len(row_by_id) != len(rows):
        failures.append("backlog contains duplicate IDs")
    if set(row_by_id) != expected_ids:
        failures.append("backlog ID union differs from 73 Mobile + 6 Landing + 12 Technical + 6 Spike")

    for index, row in enumerate(rows, start=1):
        if row[0] != str(index):
            failures.append(f"backlog order number mismatch at row {index}: {row[0]!r}")
        story_id, title = row[1], row[2]
        # The academic index retains the earlier platform-evaluation labels for
        # TS-MOB-002..004; technical cards carry the reconciled canonical titles.
        if not story_id.startswith("TS-MOB-") and all_headings.get(story_id) != title:
            failures.append(f"{story_id}: backlog title differs from its story heading")

    release_counts: dict[str, int] = {}
    for source in master.values():
        release = "V4/Future" if source["Target Release"] == "V4_FUTURE" else source["Target Release"]
        release_counts[release] = release_counts.get(release, 0) + 1
    if release_counts != {"V1": 28, "V2": 35, "V3": 9, "V4/Future": 1}:
        failures.append(f"functional release counts differ in canonical source: {release_counts}")
    if set(row_by_id) & EXPECTED_V1 != EXPECTED_V1:
        failures.append("backlog is missing one or more V1 IDs")

    for row in rows:
        if row[3] not in {"2", "3", "5", "8"}:
            failures.append(f"{row[1]} has invalid story points: {row[3]}")
        if row[4] not in {"S1", "S2", "S3", "S4"}:
            failures.append(f"{row[1]} has invalid Sprint: {row[4]}")
    sprint_counts = {sprint: sum(row[4] == sprint for row in rows) for sprint in ("S1", "S2", "S3", "S4")}
    if sprint_counts != {"S1": 20, "S2": 20, "S3": 44, "S4": 13}:
        failures.append(f"academic Sprint distribution differs: {sprint_counts}")
    if "| # | User Story ID | Título | Story Points | Sprint |" not in BACKLOG.read_text(encoding="utf-8"):
        failures.append("Product Backlog must retain the five-column academic index")

    impact = IMPACT.read_text(encoding="utf-8")
    if impact_ids(impact) != EXPECTED_V1:
        failures.append("Impact Mapping must cover exactly the 28 Mobile V1 story IDs")
    for goal in (
        "Business Goal 1 — Reducir reconstrucción",
        "Business Goal 2 — Hacer atribuible",
        "Business Goal 3 — Dar claridad",
        "Restricciones habilitantes, no Business Goals",
    ):
        if goal not in impact:
            failures.append(f"Impact Mapping missing reconciled goal: {goal}")
    for label in ("RESEARCH PENDING", "TARGET ASSUMPTION — OWNER REVIEW PENDING", "USER PERSONA — RESEARCH PENDING"):
        if label not in impact:
            failures.append(f"Impact Mapping missing evidence label: {label}")

    technical_text = TECHNICAL.read_text(encoding="utf-8")
    spike_text = SPIKES.read_text(encoding="utf-8")
    for technology in ("Android Native/Kotlin", "Flutter/Dart", "iOS Native/SwiftUI"):
        if technology in technical_text:
            failures.append(f"technology comparison must stay in SPIKE-002, not Technical Stories: {technology}")
        if technology not in spike_text:
            failures.append(f"SPIKE-002 missing platform option: {technology}")
    for field in ("Incertidumbre", "Pregunta", "Evidencia esperada", "PoC mínimo", "Decisión / salida", "Criterio de cierre"):
        if spike_text.count(field) != 6:
            failures.append(f"Spike field {field!r} must appear once in each of six cards")

    overview = OVERVIEW.read_text(encoding="utf-8")
    if not overview.startswith("# 2.4 Requirements Specification"):
        failures.append("Chapter 2.4 root overview is missing")
    if set(re.findall(r"Nexa (?:Operations|Buyer) Mobile", FUNCTIONAL.read_text(encoding="utf-8"))) != {
        "Nexa Operations Mobile", "Nexa Buyer Mobile"
    }:
        failures.append("functional stories do not retain exactly the two accepted Mobile projections")

    return failures


def main() -> int:
    failures = validate()
    if failures:
        print("mobile backlog validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("mobile backlog validation OK: functional_stories=73; backlog_rows=97; releases=28/35/9/1; sprints=S1/S2/S3/S4")
    return 0


if __name__ == "__main__":
    sys.exit(main())
