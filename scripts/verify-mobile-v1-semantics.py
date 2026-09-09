#!/usr/bin/env python3
"""Validate Mobile V1 semantic boundaries across the reconciled Chapter 2.4."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHAPTER = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification"
FUNCTIONAL = CHAPTER / "2.4.1-user-stories/user-stories.md"
TECHNICAL = CHAPTER / "2.4.1-user-stories/technical-stories.md"
SPIKES = CHAPTER / "2.4.1-user-stories/spike-stories.md"
IMPACT = CHAPTER / "2.4.2-impact-mapping.md"
BACKLOG = CHAPTER / "2.4.3-product-backlog.md"
NEEDFINDING = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.2-user-task-matrix.md"
CONTEXT_DISCOVERY = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.1-candidate-context-discovery.md"

MODULE_PATH = Path(__file__).with_name("verify-mobile-backlog.py")
spec = importlib.util.spec_from_file_location("verify_mobile_backlog", MODULE_PATH)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load validator: {MODULE_PATH}")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def backlog_row(text: str, story_id: str) -> list[str] | None:
    match = re.search(rf"^\| \d+ \| {re.escape(story_id)} \|(.+)$", text, re.MULTILINE)
    if not match:
        return None
    return [cell.strip() for cell in f"| {story_id} |{match.group(1)}".strip().strip("|").split("|")]


def main() -> int:
    failures = validator.validate()
    required = (FUNCTIONAL, TECHNICAL, SPIKES, IMPACT, BACKLOG, NEEDFINDING, CONTEXT_DISCOVERY)
    failures.extend(f"missing required semantic artifact: {path}" for path in required if not path.is_file())
    if failures:
        print("mobile Chapter 2.4 semantic validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    functional = FUNCTIONAL.read_text(encoding="utf-8")
    technical = TECHNICAL.read_text(encoding="utf-8")
    spikes = SPIKES.read_text(encoding="utf-8")
    impact = IMPACT.read_text(encoding="utf-8")
    backlog = BACKLOG.read_text(encoding="utf-8")
    needfinding = NEEDFINDING.read_text(encoding="utf-8")
    scoped_text = "\n".join((functional, technical, spikes, impact, backlog, needfinding))

    apps = set(re.findall(r"Nexa (?:Operations|Buyer) Mobile", functional))
    if apps != {"Nexa Operations Mobile", "Nexa Buyer Mobile"}:
        failures.append(f"accepted two-app model differs: {sorted(apps)}")
    for stale_term in ("Field & Warehouse Operations", "Delivery Workforce", "Sales Mobile"):
        if stale_term in scoped_text:
            failures.append(f"stale Mobile terminology remains: {stale_term}")
    if "Sales no es un segmento de investigación\nMobile V1" not in needfinding:
        failures.append("Needfinding must keep Sales outside Mobile V1 research")
    for story_id in ("MOB-US-006", "MOB-US-007", "MOB-US-008", "MOB-US-009", "MOB-US-010"):
        row = backlog_row(backlog, story_id)
        if row is None or row[2] not in {"2", "3", "5", "8"} or row[3] not in {"S1", "S2", "S3", "S4"}:
            failures.append(f"{story_id}: Sales convenience must retain a bounded academic plan")

    for technology in ("Android Native/Kotlin", "Flutter/Dart", "iOS Native/SwiftUI"):
        if technology in technical:
            failures.append(f"{technology}: framework comparison duplicated outside SPIKE-002")
        if technology not in spikes:
            failures.append(f"{technology}: missing from SPIKE-002")
    if "no constituye un motor genérico de sincronización" not in spikes:
        failures.append("SPIKE-004 must explicitly reject a generic synchronization engine")
    for spike_field in ("Incertidumbre", "Pregunta", "Evidencia esperada", "PoC mínimo", "Decisión / salida", "Criterio de cierre"):
        if spikes.count(spike_field) != 6:
            failures.append(f"each Spike must expose {spike_field}")

    first_goal = impact.find("Business Goal 1")
    enabling = impact.find("Restricciones habilitantes, no Business Goals")
    auth = impact.find("MOB-US-001")
    if first_goal < 0 or enabling < 0 or auth < enabling:
        failures.append("Impact Mapping must keep authorization as an enabling constraint, not the first Business Goal")
    for label in ("RESEARCH PENDING", "TARGET ASSUMPTION — OWNER REVIEW PENDING", "USER PERSONA — RESEARCH PENDING"):
        if label not in impact:
            failures.append(f"Impact Mapping evidence state missing: {label}")

    context_rows = re.findall(r"^\| (BC-\d{2}) \|", CONTEXT_DISCOVERY.read_text(encoding="utf-8"), re.MULTILINE)
    if set(context_rows) != {f"BC-{number:02d}" for number in range(1, 12)} or len(context_rows) != 11:
        failures.append("Strategic DDD must retain exactly 11 Bounded Contexts")
    if re.search(r"(?:Mobile|Scanner|QR|Device|Offline|Tracking|Push|Maps) (?:Bounded Context|BC)", scoped_text, re.IGNORECASE):
        failures.append("a technical surface is presented as a Bounded Context")

    if failures:
        print("mobile Chapter 2.4 semantic validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("mobile Chapter 2.4 semantic validation OK: apps=2; v1=28; contexts=11; future_sprints=none")
    return 0


if __name__ == "__main__":
    sys.exit(main())
