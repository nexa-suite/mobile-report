#!/usr/bin/env python3
"""Check that the manual V1 review register still matches Chapter 2.4."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
STORIES = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
REGISTER = REPO_ROOT / "delivery-checklists/mobile-v1-story-verification-register.md"
V1_IDS = (
    "MOB-US-001", "MOB-US-002", "MOB-US-003", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017",
    "MOB-US-019", "MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023",
    "MOB-US-024", "MOB-US-025", "MOB-US-026", "MOB-US-027", "MOB-US-028",
    "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034", "MOB-US-044",
    "MOB-US-047", "MOB-US-048", "MOB-US-049",
)

ACTOR_ES = {
    "Mobile User": "Usuario móvil",
    "Warehouse Operator": "Operador de Almacén",
    "Dispatch Coordinator": "Coordinador de Despacho",
    "Driver or Delivery Operator": "Conductor u Operador de Entrega",
    "Customer Buyer": "Comprador",
}


def register_rows(text: str) -> list[list[str]]:
    start = text.index("## Register")
    end = text.index("## Current result", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if not line.startswith("| "):
            continue
        values = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if values and re.fullmatch(r"MOB-US-\d{3}", values[0]):
            rows.append(values)
    return rows


def report_records(text: str) -> dict[str, tuple[str, str]]:
    matches = list(re.finditer(r"^### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    records: dict[str, tuple[str, str]] = {}
    for index, match in enumerate(matches):
        block = text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)]
        first = re.search(r"^\| (MOB-US-\d{3}) \| (.+?) \| (Alta|Media|Baja) \| .+ \|$", block, re.MULTILINE)
        bc = re.search(r"^\| (BC-\d{2} — .+?) \|", block, re.MULTILINE)
        if first and bc:
            records[first.group(1)] = (first.group(2), bc.group(1))
    return records


def main() -> int:
    failures: list[str] = []
    report = report_records(STORIES.read_text(encoding="utf-8"))
    reviews = register_rows(REGISTER.read_text(encoding="utf-8"))
    if [row[0] for row in reviews] != list(V1_IDS):
        failures.append("manual review register IDs/order differ from the 28 V1 stories")
    if len(reviews) != 28:
        failures.append(f"review register rows: expected 28, got {len(reviews)}")

    expected_leads = {
        **{story_id: "Diego / DiegoS284" for story_id in V1_IDS[:3]},
        **{story_id: "Gino / R0obxdnt" for story_id in V1_IDS[3:11]},
        **{story_id: "Diego / DiegoS284" for story_id in V1_IDS[11:17]},
        **{story_id: "Gerard / GerardRojasMancilla" for story_id in V1_IDS[17:24]},
        **{story_id: "Sebastián / spinedo214" for story_id in V1_IDS[24:]},
    }
    segments = {
        **{story_id: "S1-S3" for story_id in V1_IDS[:3]},
        **{story_id: "S1" for story_id in V1_IDS[3:11]},
        **{story_id: "S1" for story_id in V1_IDS[11:17]},
        **{story_id: "S2" for story_id in V1_IDS[17:24]},
        **{story_id: "S3" for story_id in V1_IDS[24:]},
    }
    for review in reviews:
        story_id = review[0]
        actor, bc = report.get(story_id, ("", ""))
        if not actor:
            failures.append(f"{story_id}: report record missing")
            continue
        expected_actor = ACTOR_ES[review[1].split(" / ", 1)[0]]
        if actor != expected_actor:
            failures.append(f"{story_id} actor: report={actor!r}, expected={expected_actor!r}")
        if review[1] != f"{review[1].split(' / ', 1)[0]} / {segments[story_id]}":
            failures.append(f"{story_id}: malformed actor/segment field")
        if review[2] != bc:
            failures.append(f"{story_id} Bounded Context: report={bc!r}, register={review[2]!r}")
        if review[3] != expected_leads[story_id]:
            failures.append(f"{story_id} review lead differs from the manual allocation")
        if len(review) != 8 or any(not cell for cell in review[3:]):
            failures.append(f"{story_id}: manual review fields must remain present")

    if failures:
        print("mobile V1 review register validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("mobile V1 review register OK: rows=28; actor/segment/BC aligned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
