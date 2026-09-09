#!/usr/bin/env bash
set -euo pipefail

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

python3 - "$repo_root" <<'PY'
import pathlib
import re
import sys

root = pathlib.Path(sys.argv[1]).resolve()
files = [root / "README.md", root / "report", root / "delivery-checklists"]
link_pattern = re.compile(r"\]\(([^)]+)\)")
errors = []

navigation_files = (
    root / "report/00-front-matter/03-contents.md",
    root / "delivery-checklists/rubric-gap-matrix.md",
    root / "delivery-checklists/architecture-render-evidence-register.md",
    root / "delivery-checklists/current-diff-ownership-matrix.md",
    root / "delivery-checklists/conflict-reconciliation-ledger.md",
)
forbidden_navigation_references = (
    "2.2-interviews/2.2.4-physical-operations-and-delivery-research-plan.md",
    "2.2-interviews/2.2.5-secondary-research-physical-operations-and-delivery.md",
    "2.4-requirements-specification/2.4.0-to-be-scenario-mapping.md",
    "2.4-requirements-specification/section-overview.md",
    "2.4-requirements-specification/to-be-scenario-mapping.md",
    "2.5-strategic-level-domain-driven-design/section-overview.md",
    "2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/section-overview.md",
    "2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/section-overview.md",
    "2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/component-level-diagrams.md",
    "2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/2.5.3.3-component-level-diagrams.md",
    "2.5-strategic-level-domain-driven-design/2.5.4-strategic-ddd-traceability.md",
)
required_navigation_references = (
    "chapter-overview.md",
    "2.4-requirements-specification/2.4.1-user-stories.md",
    "2.4-requirements-specification/2.4.2-impact-mapping.md",
    "2.4-requirements-specification/2.4.3-product-backlog.md",
    "2.5.1-eventstorming/2.5.1.0-ddd-process-evidence.md",
    "2.5.1-eventstorming/2.5.1.1-candidate-context-discovery.md",
    "2.5.1-eventstorming/2.5.1.2-domain-message-flows-modeling.md",
    "2.5.1-eventstorming/2.5.1.3-bounded-context-canvases.md",
    "2.5.2-context-mapping.md",
    "2.5.3-software-architecture/2.5.3.1-context-level-diagrams.md",
    "2.5.3-software-architecture/2.5.3.2-container-level-diagrams.md",
    "2.5.3-software-architecture/2.5.3.4-deployment-diagrams.md",
)

for source in navigation_files:
    text = source.read_text(encoding="utf-8")
    for target in forbidden_navigation_references:
        if target in text:
            errors.append(f"obsolete Chapter II navigation reference: {source.relative_to(root)} -> {target}")

contents_text = navigation_files[0].read_text(encoding="utf-8")
for target in required_navigation_references:
    if target not in contents_text:
        errors.append(f"missing canonical Chapter II navigation reference: {target}")

for base in files:
    paths = [base] if base.is_file() else base.rglob("*.md")
    for source in paths:
        text = source.read_text(encoding="utf-8")
        for match in link_pattern.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target.endswith(".md") and not target.endswith("/"):
                continue
            resolved = (source.parent / target).resolve()
            if target.endswith("/"):
                directory_indexes = (
                    "README.md",
                    "chapter-overview.md",
                    "section-overview.md",
                )
                resolved = next(
                    (resolved / name for name in directory_indexes if (resolved / name).exists()),
                    resolved / "README.md",
                )
            if not resolved.exists():
                errors.append(f"{source.relative_to(root)} -> {target}")

if errors:
    print("broken local Markdown links:", file=sys.stderr)
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)

print("local Markdown links OK")
PY
