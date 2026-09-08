#!/usr/bin/env python3
"""Validate Chapter II strategic DDD semantics and visual/rubric evidence."""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
BIG_PICTURE = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.5-big-picture-eventstorming.md"
CHAPTER = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design"
EVENTSTORMING = CHAPTER / "2.5.1-eventstorming"
ARCHITECTURE = CHAPTER / "2.5.3-software-architecture"
DDD_ASSETS = REPO_ROOT / "report/assets/chapter-2/ddd-process"
CANVAS_ASSETS = REPO_ROOT / "report/assets/chapter-2/bounded-context-canvases"

EXPECTED_CONTEXTS = {
    "BC-01": ("Tenant & Access Governance", "Supporting"),
    "BC-02": ("Customer & Buyer Relationships", "Supporting"),
    "BC-03": ("Catalog & Commercial Policy", "Supporting"),
    "BC-04": ("Sales Commitment", "Core"),
    "BC-05": ("Inventory Availability", "Core"),
    "BC-06": ("Fulfillment & Delivery", "Core"),
    "BC-07": ("Credit & Receivables", "Supporting"),
    "BC-08": ("Payments", "Generic"),
    "BC-09": ("Business Documents", "Generic"),
    "BC-10": ("Notifications", "Generic"),
    "BC-11": ("Business Traceability", "Supporting"),
}
CANVAS_ORDER = ["BC-04", "BC-05", "BC-06", "BC-03", "BC-02", "BC-07", "BC-01", "BC-11", "BC-08", "BC-09", "BC-10"]
MIRO_STEPS = (1, 2, 3, 4, 5, 6, 7, 9, 10)
STORY_NAMES = (
    "Company Onboarding",
    "Commercial Request",
    "Inventory Backing",
    "Delivery to POD",
    "Payment, Receivable",
)

REQUIRED_FILES = (
    BIG_PICTURE,
    CHAPTER / "section-overview.md",
    EVENTSTORMING / "section-overview.md",
    EVENTSTORMING / "2.5.1.1-candidate-context-discovery.md",
    EVENTSTORMING / "2.5.1.2-domain-message-flows-modeling.md",
    EVENTSTORMING / "2.5.1.3-bounded-context-canvases.md",
    CHAPTER / "2.5.2-context-mapping.md",
    ARCHITECTURE / "section-overview.md",
    ARCHITECTURE / "2.5.3.1-context-level-diagrams.md",
    ARCHITECTURE / "2.5.3.2-container-level-diagrams.md",
    ARCHITECTURE / "2.5.3.3-component-level-diagrams.md",
    ARCHITECTURE / "2.5.3.4-deployment-diagrams.md",
)


def visible(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def read(path: Path) -> str:
    return visible(path.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []
    blockers: list[str] = []
    for path in REQUIRED_FILES:
        if not path.is_file():
            failures.append(f"missing required file: {path}")
    if failures:
        print("Chapter II strategic DDD validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    big_picture = read(BIG_PICTURE)
    event_overview = read(EVENTSTORMING / "section-overview.md")
    candidate = read(EVENTSTORMING / "2.5.1.1-candidate-context-discovery.md")
    stories = read(EVENTSTORMING / "2.5.1.2-domain-message-flows-modeling.md")
    canvases = read(EVENTSTORMING / "2.5.1.3-bounded-context-canvases.md")
    context_map = read(CHAPTER / "2.5.2-context-mapping.md")
    architecture_overview = read(ARCHITECTURE / "section-overview.md")
    architecture_files = [read(path) for path in ARCHITECTURE.glob("*.md")]
    architecture = "\n".join(architecture_files)
    all_visible = "\n".join(read(path) for path in CHAPTER.rglob("*.md"))

    rows = re.findall(r"^\| (BC-\d{2}) \| ([^|]+) \| (Core|Supporting|Generic) \|", candidate, re.MULTILINE)
    found_contexts = {code: (name.strip(), classification) for code, name, classification in rows}
    if found_contexts != EXPECTED_CONTEXTS:
        failures.append(f"strategic context inventory mismatch: {found_contexts}")
    if len(rows) != 11:
        failures.append(f"strategic context row count: expected 11, got {len(rows)}")

    if not all(term in read(CHAPTER / "section-overview.md") for term in ("Core", "Supporting", "Generic", "exactamente 11")):
        failures.append("Chapter 2.5 overview missing classification or 11-context boundary")
    for step in (1, 2, 3):
        if f"Step {step}" not in big_picture or f"step{step}-ddd" not in big_picture:
            failures.append(f"2.3.5 missing visible Step {step} Miro evidence")
    for stale in ("TARGET / NOT YET VALIDATED", "antes de realizar la sesión", "faltan la sesión", "faltan las capturas", "session still pending", "before performing the session", "captures still missing"):
        if stale.lower() in big_picture.lower():
            failures.append(f"stale Big Picture wording remains: {stale}")
    for step in (4, 5, 6, 7, 9, 10):
        if f"Step {step}" not in event_overview or f"step{step}-ddd" not in event_overview:
            failures.append(f"2.5.1 missing visible Step {step} Miro evidence")
    if re.search(r"^#+ .*Step 8", big_picture + "\n" + event_overview, re.MULTILINE | re.IGNORECASE):
        failures.append("visible Step 8 heading introduced")
    for step in MIRO_STEPS:
        if not (DDD_ASSETS / f"step{step}-ddd.png").is_file():
            failures.append(f"missing Miro PNG asset: step{step}-ddd.png")
    if list(DDD_ASSETS.glob("step8-ddd.*")):
        failures.append("invented Step 8 Miro asset found")

    if not all(term in candidate for term in ("look-for-pivotal-events", "start-with-value", "DIRECT_ORDER", "Commercial Commitment != Inventory Backing", "Payment Reported != Payment Confirmed")):
        failures.append("candidate-context analysis missing required technique or boundary distinctions")
    if not all(term in candidate for term in ("Step 4", "Steps 5 y 6", "Step 7", "Step 9", "Step 10")):
        failures.append("candidate-context analysis missing explicit EventStorming progression linkage")

    story_headings = re.findall(r"^## Domain Story — (.+)$", stories, re.MULTILINE)
    if len(story_headings) != 5:
        failures.append(f"domain stories: expected 5, got {len(story_headings)}")
    for required in STORY_NAMES:
        if not any(required in heading for heading in story_headings):
            failures.append(f"missing domain story: {required}")
    if len(re.findall(r"^~~~mermaid$", stories, re.MULTILINE)) != 5:
        failures.append("domain stories must retain exactly five Mermaid sources")
    stories_compact = re.sub(r"\s+", " ", stories)
    if not all(term in stories_compact for term in ("Lane A", "Lane B", "Customer Account no es Tenant", "Buyer Relationship no es Workforce Membership", "Human Identity no se fabrica")):
        failures.append("Domain Story 1 supplier/tenant and customer relationship lanes not explicit")

    canvas_codes = re.findall(r"^## (BC-\d{2}) .+$", canvases, re.MULTILINE)
    if canvas_codes != CANVAS_ORDER:
        failures.append(f"canvas order mismatch: {canvas_codes}")
    for stage in (
        "Context Overview Definition",
        "Business Rules Distillation & Ubiquitous Language Capture",
        "Capability Analysis",
        "Capability Layering",
        "Dependencies Capture",
        "Design Critique",
    ):
        if canvases.count(f"**{stage}.**") != 11:
            failures.append(f"canvas stage {stage!r} is not present exactly 11 times")
    visual_canvas_count = 0
    for code in EXPECTED_CONTEXTS:
        matches = list(CANVAS_ASSETS.glob(f"{code.lower()}-*.svg"))
        png_matches = list(CANVAS_ASSETS.glob(f"{code.lower()}-*.png"))
        if len(matches) != 1 or len(png_matches) != 1:
            failures.append(f"visual canvas assets incomplete for {code}: svg={len(matches)} png={len(png_matches)}")
        if len(re.findall(rf"bounded-context-canvases/{re.escape(code.lower())}-[^)]+\.png", canvases)) != 1:
            failures.append(f"2.5.1.3 missing professor-facing canvas image for {code}")
        if len(matches) == 1 and len(png_matches) == 1:
            visual_canvas_count += 1

    for term in (
        "BC-04 Sales Commitment",
        "BC-05 Inventory Availability",
        "BC-06 Fulfillment & Delivery",
        "BC-07 Credit & Receivables",
        "BC-08 Payments",
        "BC-10 Notifications",
        "BC-11 Business Traceability",
        "Anti-Corruption Layer",
        "outbox durable",
        "No se adopta Shared Kernel",
    ):
        if term not in context_map:
            failures.append(f"context map missing: {term}")
    if len(re.findall(r"^\| Fusionar |^\| Colocar ", context_map, re.MULTILINE)) < 7:
        failures.append("context map alternatives incomplete")

    if not architecture_overview.startswith("# 2.5.3 Software Architecture"):
        failures.append("architecture overview heading missing")
    context_doc = read(ARCHITECTURE / "2.5.3.1-context-level-diagrams.md")
    container_doc = read(ARCHITECTURE / "2.5.3.2-container-level-diagrams.md")
    components_doc = read(ARCHITECTURE / "2.5.3.3-component-level-diagrams.md")
    deployment_doc = read(ARCHITECTURE / "2.5.3.4-deployment-diagrams.md")
    for actor in ("Interested Company / Prospect", "Company Owner", "Tenant Administrator", "Sales Representative", "Warehouse Operator", "Dispatch Coordinator", "Driver / Delivery Operator", "Customer Buyer"):
        if actor not in context_doc:
            failures.append(f"L1 actor missing: {actor}")
    for external in ("Payment Provider", "Email Delivery Service", "Maps & Geolocation Provider"):
        if external not in context_doc:
            failures.append(f"L1 external system missing: {external}")
    for container in ("Nexa Website", "Nexa Platform", "Nexa Buyer Portal", "Nexa API", "PostgreSQL", "Object Storage", "Operations Mobile", "Buyer Mobile"):
        if container not in container_doc:
            failures.append(f"C4 container missing: {container}")
    if not components_doc.startswith("# Software Architecture Components Overview"):
        failures.append("component view has artificial numbered heading")
    if not deployment_doc.startswith("# 2.5.3.3 Software Architecture Deployment Diagrams"):
        failures.append("deployment view does not use official 2.5.3.3 heading")
    if not re.search(r"Nexa es un único\s+sistema", architecture_overview) and "un solo Nexa" not in architecture:
        failures.append("architecture does not preserve one-system boundary")

    forbidden_numbering = re.compile(r"\b(?:Figure|Figura|Table|Tabla|Illustration|Ilustración|Diagram|Canvas)\s+\d+\b", re.IGNORECASE)
    professor_files = [BIG_PICTURE, *CHAPTER.rglob("*.md")]
    for path in professor_files:
        match = forbidden_numbering.search(read(path))
        if match:
            failures.append(f"forbidden numbered visual caption in {path.relative_to(REPO_ROOT)}: {match.group(0)}")
    if re.search(r"^#+ .*2\.5\.1\.0|^#+ .*2\.5\.4", all_visible, re.MULTILINE):
        failures.append("obsolete professor-facing 2.5.1.0/2.5.4 heading remains visible")
    for token in ("WORKSHOP_PENDING", "CANVAS_PENDING", "NOT EVIDENCED"):
        if token in all_visible:
            failures.append(f"audit-style token remains visible in Chapter 2.5: {token}")

    mermaid_renderer = shutil.which("mmdc")
    if mermaid_renderer:
        story_assets = REPO_ROOT / "report/assets/chapter-2/domain-stories"
        expected_story_assets = (
            "company-onboarding-authorized-relationship.svg",
            "commercial-request-direct-order-commitment.svg",
            "inventory-backing-fulfillment-dispatch.svg",
            "delivery-pod-buyer-receipt.svg",
            "payment-receivable-document-traceability.svg",
        )
        missing = [name for name in expected_story_assets if not (story_assets / name).is_file()]
        if missing:
            failures.append(f"mmdc available but Domain Story artifacts missing: {missing}")
        story_render_status = "RENDERED"
    else:
        blockers.append("BLOCKED — RENDER TOOLING: mmdc unavailable; Mermaid sources retained, no Domain Story images fabricated")
        story_render_status = "BLOCKED"

    if failures:
        print("Chapter II strategic DDD validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        for blocker in blockers:
            print(f"- {blocker}")
        return 1

    status = "OK" if not blockers else "OK WITH BLOCKED RENDER TOOLING"
    print(f"Chapter II strategic DDD validation {status}: miro=9/9; stories=5/5 Mermaid; story_images={story_render_status}; canvases=11/11 semantic; canvas_images={visual_canvas_count}/11; c4=1-system; forbidden_visual_numbering=0")
    for blocker in blockers:
        print(blocker)
    return 0


if __name__ == "__main__":
    sys.exit(main())
