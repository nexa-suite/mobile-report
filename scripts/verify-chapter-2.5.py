#!/usr/bin/env python3
"""Validate the scoped Chapter 2.5 strategic DDD/report structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CHAPTER = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design"
EVENTSTORMING = CHAPTER / "2.5.1-eventstorming"
ARCHITECTURE = CHAPTER / "2.5.3-software-architecture"

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

REQUIRED_FILES = (
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


def main() -> int:
    failures: list[str] = []
    for path in REQUIRED_FILES:
        if not path.is_file():
            failures.append(f"missing Chapter 2.5 file: {path}")

    if failures:
        print("Chapter 2.5 validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    overview = visible((CHAPTER / "section-overview.md").read_text(encoding="utf-8"))
    event_overview = visible((EVENTSTORMING / "section-overview.md").read_text(encoding="utf-8"))
    candidate = visible((EVENTSTORMING / "2.5.1.1-candidate-context-discovery.md").read_text(encoding="utf-8"))
    stories = visible((EVENTSTORMING / "2.5.1.2-domain-message-flows-modeling.md").read_text(encoding="utf-8"))
    canvases = visible((EVENTSTORMING / "2.5.1.3-bounded-context-canvases.md").read_text(encoding="utf-8"))
    context_map = visible((CHAPTER / "2.5.2-context-mapping.md").read_text(encoding="utf-8"))
    architecture_overview = visible((ARCHITECTURE / "section-overview.md").read_text(encoding="utf-8"))
    architecture_files = [visible(path.read_text(encoding="utf-8")) for path in ARCHITECTURE.glob("*.md")]
    architecture = "\n".join(architecture_files)
    all_visible = "\n".join(f"{path.name}\n{visible(path.read_text(encoding='utf-8'))}" for path in CHAPTER.rglob("*.md"))

    rows = re.findall(r"^\| (BC-\d{2}) \| ([^|]+) \| (Core|Supporting|Generic) \|", candidate, re.MULTILINE)
    found_contexts = {code: (name.strip(), classification) for code, name, classification in rows}
    if found_contexts != EXPECTED_CONTEXTS:
        failures.append(f"strategic context inventory mismatch: {found_contexts}")
    if len(rows) != 11:
        failures.append(f"strategic context row count: expected 11, got {len(rows)}")

    if not all(term in overview for term in ("Core", "Supporting", "Generic", "exactamente 11")):
        failures.append("Chapter 2.5 overview is missing classification or 11-context boundary")
    if not all(f"Step {step}" in event_overview for step in ("4", "5", "6", "7", "9", "10")):
        failures.append("EventStorming continuation does not document steps 4,5,6,7,9,10")
    if re.search(r"^#+ .*Step 8", event_overview, re.MULTILINE | re.IGNORECASE):
        failures.append("a visible Step 8 heading was introduced")
    if not all(term in candidate for term in ("look-for-pivotal-events", "start-with-value", "DIRECT_ORDER", "Commercial Commitment != Inventory Backing", "Payment Reported != Payment Confirmed")):
        failures.append("candidate-context analysis is missing required technique or boundary distinctions")

    story_headings = re.findall(r"^## Domain Story — (.+)$", stories, re.MULTILINE)
    if len(story_headings) != 5:
        failures.append(f"domain stories: expected 5, got {len(story_headings)}")
    for required in ("Company Onboarding", "Commercial Request", "Inventory Backing", "Delivery to POD", "Payment, Receivable"):
        if not any(required in heading for heading in story_headings):
            failures.append(f"missing domain story: {required}")

    canvas_codes = re.findall(r"^## (BC-\d{2}) .+$", canvases, re.MULTILINE)
    expected_order = ["BC-04", "BC-05", "BC-06", "BC-03", "BC-02", "BC-07", "BC-01", "BC-11", "BC-08", "BC-09", "BC-10"]
    if canvas_codes != expected_order:
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
        failures.append("context map alternatives are incomplete")

    if not architecture_overview.startswith("# 2.5.3 Software Architecture"):
        failures.append("architecture overview heading is missing")
    context_doc = (ARCHITECTURE / "2.5.3.1-context-level-diagrams.md").read_text(encoding="utf-8")
    container_doc = (ARCHITECTURE / "2.5.3.2-container-level-diagrams.md").read_text(encoding="utf-8")
    components_doc = (ARCHITECTURE / "2.5.3.3-component-level-diagrams.md").read_text(encoding="utf-8")
    deployment_doc = (ARCHITECTURE / "2.5.3.4-deployment-diagrams.md").read_text(encoding="utf-8")
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
        failures.append("component view has an artificial numbered heading")
    if not deployment_doc.startswith("# 2.5.3.3 Software Architecture Deployment Diagrams"):
        failures.append("deployment view does not use official 2.5.3.3 heading")
    if not re.search(r"Nexa es un único\s+sistema", architecture_overview) and "un solo Nexa" not in architecture:
        failures.append("architecture does not preserve one-system boundary")

    if re.search(r"^#+ .*2\.5\.1\.0|^#+ .*2\.5\.4", all_visible, re.MULTILINE):
        failures.append("obsolete professor-facing 2.5.1.0/2.5.4 heading remains visible")
    for token in ("WORKSHOP_PENDING", "CANVAS_PENDING", "NOT EVIDENCED"):
        if token in all_visible:
            failures.append(f"audit-style token remains visible in Chapter 2.5: {token}")
    if re.search(r"^#+ .*Step 8", all_visible, re.MULTILINE | re.IGNORECASE):
        failures.append("Step 8 heading remains visible")

    if failures:
        print("Chapter 2.5 validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Chapter 2.5 validation OK: contexts=11; stories=5; canvases=11; steps=4,5,6,7,9,10; c4=1-system")
    return 0


if __name__ == "__main__":
    sys.exit(main())
