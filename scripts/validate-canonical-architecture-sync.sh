#!/usr/bin/env bash
# Validates the Chapter 2 canonical-architecture projection against Blueprint.
set -euo pipefail

usage() {
  printf 'Usage: %s --blueprint-dir /absolute/path/to/nexa-suite/blueprint\n' "$0" >&2
  exit 64
}

blueprint_dir=''
while (($#)); do
  case "$1" in
    --blueprint-dir)
      (($# >= 2)) || usage
      blueprint_dir=$2
      shift 2
      ;;
    *)
      usage
      ;;
  esac
done

[[ -n "$blueprint_dir" ]] || usage
git -C "$blueprint_dir" rev-parse --is-inside-work-tree >/dev/null 2>&1 || usage

report_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)

python3 - "$report_root" "$blueprint_dir" <<'PY'
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

report_root = Path(sys.argv[1]).resolve()
blueprint_root = Path(sys.argv[2]).resolve()
report_dir = report_root / "report"
report_bc_dir = report_dir / "02-requirements-and-software-solution-design" / "2.6-tactical-level-domain-driven-design" / "bounded-contexts"
blueprint_bc_dir = blueprint_root / "01-shared" / "domain" / "bounded-contexts"
manifest = report_dir / "assets" / "chapter-2" / "provenance" / "wave3-construction-blueprint.md"
errors: list[str] = []


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def one(paths: list[Path], label: str) -> Path | None:
    if len(paths) != 1:
        errors.append(f"{label}: expected 1 path, found {len(paths)}")
        return None
    return paths[0]


def root_set(path: Path) -> set[str]:
    return {
        match.group(1).strip()
        for match in re.finditer(
            r"^\|\s*`([^`]+)`\s*\|\s*[^|]*\bAggregate Root\b[^|]*\|",
            read(path),
            re.MULTILINE,
        )
    }


def table_row(path: Path, name: str) -> str | None:
    for line in read(path).splitlines():
        if line.startswith("|") and f"`{name}`" in line:
            return line
    errors.append(f"{path.relative_to(report_root)}: missing table row for {name}")
    return None


report_pages: dict[str, Path] = {}
for bc_number in range(1, 12):
    bc = f"BC-{bc_number:02d}"
    page = one(sorted(report_bc_dir.glob(f"{bc}-*.md")), f"{bc} report page")
    blueprint_bc = one(sorted(blueprint_bc_dir.glob(f"{bc}-*")), f"{bc} Blueprint directory")
    if page is None or blueprint_bc is None:
        continue
    blueprint_model = blueprint_bc / "tactical-model.md"
    if not blueprint_model.is_file():
        errors.append(f"{blueprint_model}: missing tactical model")
        continue
    report_pages[bc] = page
    report_roots = root_set(page)
    blueprint_roots = root_set(blueprint_model)
    if report_roots != blueprint_roots:
        errors.append(
            f"{bc}: Aggregate Root mismatch; report={sorted(report_roots)}, Blueprint={sorted(blueprint_roots)}"
        )


bc01 = report_pages.get("BC-01")
if bc01:
    onboarding = table_row(bc01, "CompanyOnboardingRequest")
    if onboarding and "TenantId" not in onboarding:
        errors.append("BC-01: CompanyOnboardingRequest must carry TenantId at submission")
    if re.search(r"(?:No existe Tenant al enviar|sin Tenant ni Workspace)", read(bc01), re.IGNORECASE):
        errors.append("BC-01: onboarding must not claim submission without Tenant identity")

bc05 = report_pages.get("BC-05")
if bc05 and re.search(r"^\|\s*`WarehouseBacking`\s*\|\s*Aggregate Root\b", read(bc05), re.MULTILINE):
    errors.append("BC-05: WarehouseBacking must be InventoryReservation-owned Entity, not Aggregate Root")

bc06 = report_pages.get("BC-06")
if bc06:
    delivery = table_row(bc06, "Delivery")
    receipt = table_row(bc06, "BuyerReceiptFact")
    if delivery and "BuyerRelationshipId" in delivery:
        errors.append("BC-06: Delivery must not own BuyerRelationship")
    if delivery and "no posee BuyerRelationship" not in delivery:
        errors.append("BC-06: Delivery row must state non-ownership of BuyerRelationship")
    if receipt and "BuyerRelationshipId" not in receipt:
        errors.append("BC-06: BuyerReceiptFact must carry BuyerRelationship identity")

bc10 = report_pages.get("BC-10")
if bc10 and re.search(r"^\|\s*`PushSubscription`\s*\|\s*Aggregate Root\b", read(bc10), re.MULTILINE):
    errors.append("BC-10: PushSubscription must be a technical/application record, not Aggregate Root")


link_pattern = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+[^)]*)?\)")
checked_links = 0
for markdown in sorted(report_dir.rglob("*.md")):
    for match in link_pattern.finditer(read(markdown)):
        target = unquote(match.group(1).strip().strip("<>"))
        if not target or target.startswith("#") or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE) or target.startswith("//"):
            continue
        target = target.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        checked_links += 1
        resolved = (markdown.parent / target).resolve()
        if not resolved.exists():
            errors.append(f"broken local link: {markdown.relative_to(report_root)} -> {target}")


if not manifest.is_file():
    errors.append("missing Wave 3 architecture provenance manifest")
    source_commit = ""
else:
    source_match = re.search(r"^source-commit:\s*([0-9a-f]{40})\s*$", read(manifest), re.MULTILINE)
    if not source_match:
        errors.append("provenance manifest has no valid source-commit")
        source_commit = ""
    else:
        source_commit = source_match.group(1)
        blueprint_head = subprocess.check_output(
            ["git", "-C", str(blueprint_root), "rev-parse", "HEAD"], text=True
        ).strip()
        if source_commit != blueprint_head:
            errors.append(f"provenance source-commit {source_commit} != Blueprint HEAD {blueprint_head}")


artifact_pairs: list[tuple[Path, Path]] = []


def add_artifact_pair(artifact: Path, candidates: list[Path]) -> None:
    source = one(candidates, f"canonical source for {artifact.relative_to(report_root)}")
    if source is not None:
        artifact_pairs.append((artifact, source))


c4_exports = blueprint_root / "01-shared" / "architecture" / "c4" / "exports"
for artifact in sorted((report_dir / "assets" / "chapter-2" / "c4").glob("*")):
    if artifact.is_file() and artifact.suffix in {".svg", ".png"}:
        add_artifact_pair(artifact, sorted(c4_exports.rglob(artifact.name)))

for artifact in sorted((report_dir / "assets" / "chapter-2" / "tactical").rglob("*")):
    if artifact.is_file() and artifact.suffix in {".svg", ".png"}:
        bc_dirs = sorted(blueprint_bc_dir.glob(f"{artifact.parent.name}-*"))
        if len(bc_dirs) == 1:
            add_artifact_pair(artifact, sorted(bc_dirs[0].rglob(artifact.name)))
        else:
            errors.append(f"canonical source directory for {artifact.relative_to(report_root)}: expected 1, found {len(bc_dirs)}")

storytelling = blueprint_root / "01-shared" / "domain" / "processes" / "domain-storytelling"
for artifact in sorted((report_dir / "assets" / "chapter-2" / "domain-storytelling").glob("*")):
    if artifact.is_file() and artifact.suffix in {".svg", ".png"}:
        add_artifact_pair(artifact, sorted(storytelling.glob(artifact.name)))

for artifact, source in artifact_pairs:
    if artifact.read_bytes() != source.read_bytes():
        errors.append(f"asset provenance mismatch: {artifact.relative_to(report_root)} != {source.relative_to(blueprint_root)}")

if len(artifact_pairs) != 112:
    errors.append(f"canonical asset count changed: expected 112, found {len(artifact_pairs)}")

if errors:
    print("REPORT CANONICAL SYNC: FAIL", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print("REPORT CANONICAL SYNC: PASS")
print("- Blueprint Aggregate Root sets: 11 matched")
print("- Wave 3.1 semantic closure assertions: PASS")
print(f"- local Markdown links: {checked_links} resolved")
print(f"- provenance source commit: {source_commit}")
print(f"- canonical artifacts: {len(artifact_pairs)} byte-identical")
PY
