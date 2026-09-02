#!/usr/bin/env python3
"""Audit the report for the approved Mobile V1 semantic boundaries."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REPORT_ROOT = REPO_ROOT / "report"
STARTUP = REPORT_ROOT / "01-presentation/1.1-startup-profile/1.1.1-startup-description.md"
TARGET_SEGMENTS = REPORT_ROOT / "01-presentation/1.3-target-segments/target-segments.md"
SPRINT_INDEX = REPORT_ROOT / (
    "04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/"
    "4.2.1-sprints/section-overview.md"
)
STORY_FILE = REPORT_ROOT / (
    "02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
)
DDD_TRACEABILITY = REPORT_ROOT / (
    "02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/"
    "2.5.4-strategic-ddd-traceability.md"
)

INVENTORY_RULES = {
    "connectivity/local state": re.compile(
        r"offline|sincroniz|conectividad|caché|cache|reintento", re.IGNORECASE
    ),
    "location/navigation": re.compile(
        r"gps|tracking|seguimiento|ubicaci[oó]n|eta|geocerca|geofence|"
        r"route optimization|optimizaci[oó]n de rutas|mapas|navegaci[oó]n",
        re.IGNORECASE,
    ),
    "scope/counts": re.compile(
        r"49 historias|49 stories|7 Mobile Epics|7 epics|73 Mobile stories|"
        r"28 Mobile V1|28 historias",
        re.IGNORECASE,
    ),
    "context identity": re.compile(
        r"Mobile Bounded Context|Mobile BC|Scanner BC|QR BC|Device BC|"
        r"Bounded Contexts?|Tenant\s*=\s*Workspace|Tenant\s*≠\s*Workspace",
        re.IGNORECASE,
    ),
    "surface roles": re.compile(
        r"Operations Mobile|Sales Representative|Sales|Buyer Mobile",
        re.IGNORECASE,
    ),
}

STALE_PATTERNS = (
    re.compile(r"conectividad\s+intermitente\s*,\s*(?:con\s+)?sincronizaci[oó]n\s+expl[ií]cita", re.IGNORECASE),
    re.compile(r"ubicaci[oó]n\s+durante\s+una\s+entrega\s+activa", re.IGNORECASE),
    re.compile(r"Operations Mobile\s+(?:para|supports)\s+ventas", re.IGNORECASE),
    re.compile(r"Sales\s+(?:in|en)\s+Operations Mobile", re.IGNORECASE),
    re.compile(r"Tenant\s*=\s*Workspace", re.IGNORECASE),
)

ARCHITECTURE_REPORT_FILES = (
    REPORT_ROOT / (
        "02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/"
        "2.5.3-software-architecture/2.5.3.1-context-level-diagrams.md"
    ),
    REPORT_ROOT / (
        "02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/"
        "2.5.3-software-architecture/2.5.3.2-container-level-diagrams.md"
    ),
    REPORT_ROOT / (
        "02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/"
        "2.5.3-software-architecture/2.5.3.3-component-level-diagrams.md"
    ),
    REPORT_ROOT / (
        "02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/"
        "2.5.3-software-architecture/2.5.3.4-deployment-diagrams.md"
    ),
    REPO_ROOT / "delivery-checklists/architecture-render-evidence-register.md",
)

# These patterns identify claims that were explicitly rejected by the current
# Blueprint reconciliation. Historical decisions, future research and explicit
# boundaries are retained and classified instead of being deleted.
ARCHITECTURE_STALE_PATTERNS = (
    ("legacy-seven-context-model", re.compile(
        r"\b(?:7|seven)\s+(?:bounded\s+contexts?|contextos(?:\s+delimitados)?)\b|"
        r"\b(?:IAM|Tenant Management|Catalog Management|Sales|Warehouse|Logistics|Invoicing)\s+"
        r"(?:Bounded Context|context|BC)\b",
        re.IGNORECASE,
    )),
    ("legacy-mobile-count-or-epics", re.compile(
        r"\b(?:49\s+(?:mobile\s+)?(?:stories|historias)|7\s+Mobile\s+Epics|7\s+epics)\b",
        re.IGNORECASE,
    )),
    ("technical-mobile-bounded-context", re.compile(
        r"\b(?:Mobile|Scanner|QR|Device|Offline|Tracking|Push|Maps)\s+(?:Bounded Context|BC)\b",
        re.IGNORECASE,
    )),
    ("mobile-target-runway-conflation", re.compile(
        r"(?:planificad[oa]s?/propuest[oa]s?\s+para\s+el\s+runway|"
        r"RUNWAY/TARGET|Mobile\s+remains\s+target/runway\s+evidence)",
        re.IGNORECASE,
    )),
    ("offline-authority-claim", re.compile(
        r"\b(?:offline-first|autoridad\s+offline|offline\s+authority)\b",
        re.IGNORECASE,
    )),
    ("active-location-authority-claim", re.compile(
        r"\b(?:ubicaci[oó]n\s+durante\s+una\s+entrega\s+activa|"
        r"active\s+delivery\s+location|continuous\s+GPS|GPS\s+continuo|"
        r"seguimiento\s+en\s+vivo|live\s+tracking)\b",
        re.IGNORECASE,
    )),
)

NEGATION_MARKERS = re.compile(
    r"\b(?:no|not|sin|never|does not|cannot|fuera|excluye|excludes|"
    r"deferred|diferid[oa]|no se|not current)\b",
    re.IGNORECASE,
)
ARCHITECTURE_NEGATION_MARKERS = re.compile(
    r"\b(?:no|not|sin|ni|ningun[oa]|never|does not|cannot|fuera|excluye|"
    r"excludes|deferred|diferid[oa]|no se|not current)\b",
    re.IGNORECASE,
)
HISTORICAL_MARKERS = re.compile(
    r"histor(?:ical|ic|y)|hist[oó]ric|old|previous|antigu|baseline|competitor|"
    r"bibliograf|fuente secundaria|secondary source",
    re.IGNORECASE,
)
FUTURE_MARKERS = re.compile(
    r"future|futuro|pending|pendiente|proposed|propuesta|candidate|candidat[oa]|"
    r"research|investig|spike|open|runway|V2\+|deferred|diferid[oa]|hypothesis|"
    r"hip[oó]tesis|experiment",
    re.IGNORECASE,
)


def classify(line: str, path: Path) -> str:
    if HISTORICAL_MARKERS.search(line) or "competitor" in str(path).lower():
        return "historical/context"
    if FUTURE_MARKERS.search(line):
        return "future/research"
    if NEGATION_MARKERS.search(line):
        return "valid boundary"
    return "valid current"


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def classify_architecture(line: str, path: Path) -> str:
    if HISTORICAL_MARKERS.search(line) or "competitor" in str(path).lower():
        return "historical/context"
    if FUTURE_MARKERS.search(line):
        return "future/research"
    if ARCHITECTURE_NEGATION_MARKERS.search(line):
        return "valid boundary"
    return "valid current"


def audit_files() -> list[Path]:
    roots = (REPORT_ROOT, REPO_ROOT / "delivery-checklists", REPO_ROOT / "scripts")
    paths = {
        path
        for root in roots
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in {".md", ".py", ".sh"}
    }
    # The validator contains the rejected vocabulary as executable patterns;
    # excluding its own source avoids counting those literals as report claims.
    return sorted(path for path in paths if path.resolve() != Path(__file__).resolve())


def architecture_audit(files: list[Path], failures: list[str]) -> Counter[str]:
    classifications: Counter[str] = Counter()

    for path in files:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        for line_number, line in enumerate(lines, start=1):
            for label, pattern in ARCHITECTURE_STALE_PATTERNS:
                if not pattern.search(line):
                    continue
                # Semantic exclusions are often written on the adjacent line
                # of a wrapped Markdown paragraph. Inspect a small local
                # window so a negated boundary is not misread as a positive
                # product claim merely because the matched term wrapped.
                context = " ".join(lines[max(0, line_number - 3):line_number + 5])
                category = classify_architecture(context, path)
                classifications[f"{label}/{category}"] += 1
                if category == "valid current":
                    failures.append(
                        f"stale architecture claim in {path.relative_to(REPO_ROOT)}:{line_number}: {label}"
                    )

    required_anchors = {
        ARCHITECTURE_REPORT_FILES[0]: (
            "vista `V1 TARGET`", "TARGET V1 / PLANNED / PROPOSED", "no capacidades implementadas"
        ),
        ARCHITECTURE_REPORT_FILES[1]: (
            "containers `V1 TARGET / PLANNED / PROPOSED`", "clientes planificados para V1"
        ),
        ARCHITECTURE_REPORT_FILES[2]: ("proyecciones `V1 TARGET / PLANNED / PROPOSED`",),
        ARCHITECTURE_REPORT_FILES[3]: (
            "`TARGET V1 / PLANNED / PROPOSED`", "no se ha demostrado runtime desplegado"
        ),
        ARCHITECTURE_REPORT_FILES[4]: (
            "Mobile in V1 TARGET", "TARGET V1 / PLANNED / PROPOSED"
        ),
    }
    for path, anchors in required_anchors.items():
        text = normalized(path.read_text(encoding="utf-8"))
        for anchor in anchors:
            if anchor not in text:
                failures.append(f"canonical architecture anchor missing in {path.relative_to(REPO_ROOT)}: {anchor}")

    return classifications


def main() -> int:
    failures: list[str] = []
    markdown_files = sorted(REPORT_ROOT.rglob("*.md"))
    scanned_files = audit_files()
    inventory: Counter[str] = Counter()

    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for marker in ("<<<<<<<", "=======", ">>>>>>>"):
            if marker in text:
                failures.append(f"conflict marker {marker} in {path.relative_to(REPO_ROOT)}")
        compact = normalized(text)
        for pattern in STALE_PATTERNS:
            if pattern.search(compact):
                failures.append(f"stale semantic claim in {path.relative_to(REPO_ROOT)}: {pattern.pattern}")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in INVENTORY_RULES.items():
                if pattern.search(line):
                    inventory[classify(line, path)] += 1
                    if label == "context identity" and re.search(
                        r"(?:Mobile|Scanner|QR|Device)\s+Bounded Context", line, re.IGNORECASE
                    ) and not NEGATION_MARKERS.search(line):
                        failures.append(
                            f"technical surface presented as Bounded Context at "
                            f"{path.relative_to(REPO_ROOT)}:{line_number}"
                        )

    startup_text = STARTUP.read_text(encoding="utf-8")
    startup_compact = normalized(startup_text).lower()
    startup_requirements = (
        "online-first",
        "borradores seguros",
        "evidencias temporales",
        "metadatos de reintento",
        "el servidor mantiene la autoridad",
        "navegación",
        "GPS continuo",
        "seguimiento en vivo",
        "ETA",
        "geocerca",
        "optimización de rutas",
    )
    for requirement in startup_requirements:
        if requirement.lower() not in startup_compact:
            failures.append(f"startup semantic anchor missing: {requirement}")

    target_text = TARGET_SEGMENTS.read_text(encoding="utf-8")
    if "Sales Representative es un actor diferido V2+" not in target_text:
        failures.append("target segments do not defer Sales Representative from Operations Mobile V1")
    if not re.search(r"no forman parte de V1", target_text, re.IGNORECASE):
        failures.append("target segments do not exclude continuous tracking/location authority from V1")

    sprint_text = SPRINT_INDEX.read_text(encoding="utf-8")
    sprint_rows = re.findall(r"^\|\s*Sprint\s+([123])\s*\|", sprint_text, re.MULTILINE)
    if sprint_rows != ["1", "2", "3"]:
        failures.append(f"canonical sprint rows differ from S1/S2/S3: {sprint_rows}")
    if re.search(r"Sprint\s+4|sprint-4", "\n".join(path.as_posix() for path in markdown_files), re.IGNORECASE):
        failures.append("Sprint 4 artifact remains in the report")

    story_text = STORY_FILE.read_text(encoding="utf-8")
    story_count = len(re.findall(r"^### MOB-US-\d{3} ", story_text, re.MULTILINE))
    scenario_count = len(re.findall(r"^- \*\*Scenario:", story_text, re.MULTILINE))
    if story_count != 28:
        failures.append(f"V1 story headings: expected 28, got {story_count}")
    if scenario_count != 112:
        failures.append(f"V1 Gherkin scenarios: expected 112, got {scenario_count}")

    ddd_text = DDD_TRACEABILITY.read_text(encoding="utf-8")
    context_count = len(re.findall(r"^\| BC-\d{2} —", ddd_text, re.MULTILINE))
    if context_count != 11:
        failures.append(f"strategic context rows: expected 11, got {context_count}")

    architecture_classifications = architecture_audit(scanned_files, failures)

    print(
        "mobile V1 semantic inventory: "
        + ", ".join(f"{category}={inventory.get(category, 0)}" for category in (
            "valid current", "valid boundary", "future/research", "historical/context"
        ))
    )
    print(f"mobile V1 semantic counts: stories={story_count} scenarios={scenario_count} strategic_contexts={context_count}")
    print(
        "architecture stale scan: "
        f"files={len(scanned_files)} (Markdown + scripts; validator source excluded), "
        f"classified_hits={sum(architecture_classifications.values())}"
    )
    for classification, count in sorted(architecture_classifications.items()):
        print(f"- {classification}={count}")
    if failures:
        print("mobile V1 semantic validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("mobile V1 semantic validation OK: online-first boundaries and exclusions are explicit")
    return 0


if __name__ == "__main__":
    sys.exit(main())
