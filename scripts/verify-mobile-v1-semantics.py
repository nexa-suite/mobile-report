#!/usr/bin/env python3
"""Audit Chapter 2.4 wording and cross-document Mobile boundaries."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CHAPTER = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.4-requirements-specification"
STORIES = CHAPTER / "2.4.1-user-stories.md"
BACKLOG = CHAPTER / "2.4.3-product-backlog.md"
IMPACT = CHAPTER / "2.4.2-impact-mapping.md"
DDD_CONTEXT_DISCOVERY = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.1-candidate-context-discovery.md"

ACADEMIC_TOKENS = (
    "P0", "P1", "P2", "P3", "PROPOSED", "PARTIAL", "COVERED",
    "PARTIALLY COVERED", "NEEDS OWNER FOLLOW-UP", "RESEARCH VALIDATION PENDING",
    "NOT PRODUCT SCOPE", "TARGET /", "PLANNED;", "OPEN /", "FUTURE / UNASSIGNED",
    "owner follow-up", "acceptance pending", "evidence boundary", "route inventory",
    "AS-IS evidence register", "baseline hash", "dirty checkout", "snapshot",
    "no acceptance claimed", "no implementation claim", "Product Acceptance pending",
    "System Acceptance", "Production Readiness", "source-backed", "reconciliation gate",
)
EXPECTED_V1 = {
    "MOB-US-001", "MOB-US-002", "MOB-US-003", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017",
    "MOB-US-019", "MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023",
    "MOB-US-024", "MOB-US-025", "MOB-US-026", "MOB-US-027", "MOB-US-028",
    "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034", "MOB-US-044",
    "MOB-US-047", "MOB-US-048", "MOB-US-049",
}


def story_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^##### (MOB-US-\d{3}) — .+$", text, re.MULTILINE))
    return [
        (match.group(1), text[match.start() : matches[index + 1].start() if index + 1 < len(matches) else len(text)])
        for index, match in enumerate(matches)
    ]


def backlog_ids(text: str) -> set[str]:
    start = text.index("## Índice completo")
    end = text.index("## Sprints planificados", start)
    return {
        values[1]
        for line in text[start:end].splitlines()
        if line.startswith("| ")
        for values in [[cell.strip() for cell in line.strip().strip("|").split("|")]]
        if len(values) == 5 and re.fullmatch(r"\d+", values[0])
    }


def main() -> int:
    failures: list[str] = []
    chapter_files = (STORIES, IMPACT, BACKLOG)
    for path in chapter_files:
        if not path.is_file():
            failures.append(f"missing Chapter 2.4 file: {path.name}")
            continue
        text = path.read_text(encoding="utf-8")
        for token in ACADEMIC_TOKENS:
            if token.lower() in text.lower():
                failures.append(f"internal token in {path.name}: {token}")
        if "2.4.0-to-be-scenario-mapping" in text or "2.4.4-technical-stories" in text:
            failures.append(f"obsolete Chapter 2.4 reference in {path.name}")

    story_text = STORIES.read_text(encoding="utf-8")
    blocks = story_blocks(story_text)
    story_ids = {story_id for story_id, _ in blocks}
    if story_ids != {f"MOB-US-{number:03d}" for number in range(1, 74)}:
        failures.append(f"functional story inventory is not exactly MOB-US-001..073: {len(story_ids)}")
    if len(blocks) != 73:
        failures.append(f"functional story headings: expected 73, got {len(blocks)}")
    if len(set(re.findall(r"\*\*Scenario: .+?\*\*", story_text))) == 0:
        failures.append("no Gherkin scenarios found in functional stories")
    if re.search(r"\bP[0-9]\b", story_text):
        failures.append("numeric priorities remain in functional stories")
    app_mentions = set(re.findall(r"Nexa (?:Operations|Buyer) Mobile", story_text))
    if app_mentions != {"Nexa Operations Mobile", "Nexa Buyer Mobile"}:
        failures.append(f"unexpected Mobile product apps: {sorted(app_mentions)}")
    for old_role in ("Mobile User", "Business Operations Manager", "Sales Representative", "Warehouse Operator", "Dispatch Coordinator", "Customer Buyer"):
        if re.search(rf"^\| MOB-US-\d{{3}} \| {re.escape(old_role)} \|", story_text, re.MULTILINE):
            failures.append(f"English actor remains in functional story table: {old_role}")
    if "DIRECT_ORDER" not in story_text or "servidor vuelve a validar" not in story_text:
        failures.append("Direct Order authorization/revalidation rule missing")
    functional_blocks = dict(blocks)
    sales_story = functional_blocks.get("MOB-US-009", "")
    buyer_story = functional_blocks.get("MOB-US-040", "")
    for term in (
        "APPROVAL_REQUIRED", "DIRECT_ORDER", "Customer Account", "Buyer Relationship",
        "Sales Draft", "Buyer Draft", "inventory protection", "applicable credit", "idempotente",
    ):
        if term.lower() not in sales_story.lower():
            failures.append(f"MOB-US-009 missing assisted-commercial term: {term}")
    for term in ("sin suplantar al Comprador", "no duplica", "Representante de Ventas"):
        if term.lower() not in sales_story.lower():
            failures.append(f"MOB-US-009 missing actor/idempotency rule: {term}")
    if "MOB-US-074" in story_text:
        failures.append("MOB-US-074 must not be introduced")
    if not re.search(r"\*\*Description:\*\* Como Comprador\b", buyer_story):
        failures.append("MOB-US-040 must retain Buyer ownership")
    for forbidden in ("Sales Representative", "Representante de Ventas", "Sales Draft", "Buyer Draft"):
        if forbidden.lower() in buyer_story.lower():
            failures.append(f"MOB-US-040 must remain Buyer-only: {forbidden}")
    if "### Cómo se relaciona el análisis con las historias" not in story_text:
        failures.append("research-to-story traceability section missing")
    for term in ("Needfinding", "Lean UX", "To-Be", "Epics", "User Stories"):
        if term not in story_text:
            failures.append(f"research-to-story traceability missing: {term}")

    backlog_text = BACKLOG.read_text(encoding="utf-8")
    if "MOB-US-074" in backlog_text:
        failures.append("MOB-US-074 must not be introduced in Product Backlog")
    ids = backlog_ids(backlog_text)
    expected_ids = {f"MOB-US-{number:03d}" for number in range(1, 74)} | {
        f"LAND-US-{number:03d}" for number in range(1, 7)
    } | {f"TS-MOB-{number:03d}" for number in range(1, 13)} | {f"SPIKE-{number:03d}" for number in range(1, 7)}
    if ids != expected_ids:
        failures.append("Product Backlog does not contain the complete functional/supporting inventory")
    for sprint in ("S1", "S2", "S3", "S4"):
        if not re.search(rf"^\| {sprint} \|", backlog_text, re.MULTILINE):
            failures.append(f"Product Backlog missing {sprint}")
    if "| # Orden | User Story Id | Título | Story Points (1 / 2 / 3 / 5 / 8) | Sprint |" not in backlog_text:
        failures.append("Product Backlog five-column table missing")

    impact_text = IMPACT.read_text(encoding="utf-8")
    impact_story_ids = set(re.findall(r"\bMOB-US-\d{3}\b", impact_text))
    if impact_story_ids != EXPECTED_V1:
        failures.append("Impact Mapping does not contain exactly the 28 Mobile V1 references")
    for heading in ("## Cadena de impacto", "Objetivo de negocio", "Impacto observable", "Resultado esperado", "Historias"):
        if heading not in impact_text:
            failures.append(f"Impact Mapping missing academic chain element: {heading}")
    story_descriptions = {
        story_id: match.group(1).strip()
        for story_id, block in blocks
        if (match := re.search(r"^\*\*Description:\*\* (.+)$", block, re.MULTILINE))
    }
    for story_id in EXPECTED_V1:
        description = story_descriptions.get(story_id, "")
        comparable = description.replace("Usuario móvil", "Mobile User")
        comparable = comparable.replace("Operador de Almacén", "Warehouse Operator")
        comparable = comparable.replace("Coordinador de Despacho", "Dispatch Coordinator")
        comparable = comparable.replace("Conductor u Operador de Entrega", "Driver / Delivery Operator")
        comparable = comparable.replace("Comprador", "Customer Buyer")
        impact_without_emphasis = impact_text.replace("**", "")
        if description not in impact_without_emphasis and comparable not in impact_without_emphasis:
            failures.append(f"Impact Mapping does not preserve full story wording for {story_id}")
    if re.search(r"\[(?:baseline|target|metric|time window|segment/actor)[^\]]*\]", impact_text, re.IGNORECASE):
        failures.append("Impact Mapping contains bracket placeholders")
    if "[ ]" in impact_text or "validated persona pending" in impact_text.lower():
        failures.append("Impact Mapping contains checklist or internal persona state")

    backlog_text = BACKLOG.read_text(encoding="utf-8")
    for term in ("## Criterio de priorización", "valor de negocio", "riesgo", "dependencias"):
        if term.lower() not in backlog_text.lower():
            failures.append(f"Product Backlog prioritization criterion missing: {term}")
    for path, text in ((STORIES, story_text), (BACKLOG, backlog_text)):
        if re.search(r"\b(?:V[1-4]|V4_FUTURE|Future|release|roadmap)\b", text, re.IGNORECASE):
            failures.append(f"release roadmap language remains in professor-facing {path.name}")

    if len(re.findall(r"^#### TS-MOB-\d{3} —", story_text, re.MULTILINE)) != 12:
        failures.append("Technical Stories must contain 12 outcomes")
    if not all(term in story_text for term in ("Android Native/Kotlin", "Flutter/Dart", "iOS Native/SwiftUI")):
        failures.append("Technical technology boundaries are incomplete")
    if len(re.findall(r"^#### SPIKE-\d{3} —", story_text, re.MULTILINE)) != 6:
        failures.append("Spike Stories must contain six research questions")
    spike_002 = story_text[story_text.index("#### SPIKE-002") : story_text.index("#### SPIKE-003")]
    if re.search(r"\| Question \|[^\n]*(?:elegir|seleccionar una única|qué tecnología escoger)", spike_002, re.IGNORECASE):
        failures.append("SPIKE-002 asks for single-framework selection")

    context_text = DDD_CONTEXT_DISCOVERY.read_text(encoding="utf-8")
    context_rows = re.findall(r"^\| (BC-\d{2}) \|", context_text, re.MULTILINE)
    if len(context_rows) != 11 or set(context_rows) != {f"BC-{number:02d}" for number in range(1, 12)}:
        failures.append(f"strategic Bounded Context inventory is not exactly 11: {context_rows}")
    if re.search(r"(?:Mobile|Scanner|QR|Device|Offline|Tracking|Push|Maps) (?:Bounded Context|BC)", "\n".join(path.read_text(encoding="utf-8") for path in chapter_files if path.is_file()), re.IGNORECASE):
        failures.append("technical surface presented as a Bounded Context")

    if failures:
        print("mobile Chapter 2.4 semantic validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    scenario_count = len(re.findall(r"\*\*Scenario: .+?\*\*", story_text))
    print(f"mobile Chapter 2.4 semantic validation OK: stories=73; v1={len(EXPECTED_V1)}; scenarios={scenario_count}; bounded_contexts=11; apps=2")
    return 0


if __name__ == "__main__":
    sys.exit(main())
