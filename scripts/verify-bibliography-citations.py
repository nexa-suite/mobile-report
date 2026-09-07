#!/usr/bin/env python3
"""Verify the report's mandatory bibliography references and evidence boundary."""

from __future__ import annotations

import re
import sys
from pathlib import Path


MANDATORY_IDS = ("D1", "D2", "M1", "M2")
TECHNICAL_IDS = ("T1", "T2", "T3", "T4", "T5", "T6")
ENTRY_PATTERN = re.compile(r"\*\*\[(?P<id>D[12]|M[12])\]\*\*.*?(?=\n\n\*\*\[|\Z)", re.DOTALL)


def fail(message: str) -> None:
    print(f"bibliography citations ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    report_root = repo_root / "report"
    bibliography_path = report_root / "92-bibliography" / "bibliography.md"

    if not bibliography_path.is_file():
        fail(f"missing bibliography: {bibliography_path}")

    bibliography = bibliography_path.read_text(encoding="utf-8")
    entries = {match.group("id"): match.group(0) for match in ENTRY_PATTERN.finditer(bibliography)}

    missing_entries = [reference_id for reference_id in MANDATORY_IDS if reference_id not in entries]
    if missing_entries:
        fail(f"missing mandatory entries: {', '.join(missing_entries)}")

    missing_dois = [
        reference_id
        for reference_id, entry in entries.items()
        if reference_id in MANDATORY_IDS and not re.search(r"https://doi\.org/10\.", entry)
    ]
    if missing_dois:
        fail(f"mandatory entries without DOI: {', '.join(missing_dois)}")

    body_references: dict[str, list[Path]] = {reference_id: [] for reference_id in MANDATORY_IDS}
    for markdown_path in report_root.rglob("*.md"):
        if markdown_path == bibliography_path:
            continue
        body = markdown_path.read_text(encoding="utf-8")
        for reference_id in MANDATORY_IDS:
            if re.search(rf"(?<![A-Za-z0-9])\[{reference_id}\](?![A-Za-z0-9])", body):
                body_references[reference_id].append(markdown_path.relative_to(repo_root))

    missing_body_references = [reference_id for reference_id, paths in body_references.items() if not paths]
    if missing_body_references:
        fail(f"mandatory entries not cited outside bibliography: {', '.join(missing_body_references)}")

    if "PRELIMINARY" not in bibliography or "Pending team capture" not in bibliography:
        fail("quartile status must remain explicitly preliminary and pending official capture")

    technical_usage = sum(
        1
        for reference_id in TECHNICAL_IDS
        if any(
            re.search(rf"(?<![A-Za-z0-9])\[{reference_id}\](?![A-Za-z0-9])", markdown_path.read_text(encoding="utf-8"))
            for markdown_path in report_root.rglob("*.md")
            if markdown_path != bibliography_path
        )
    )
    cited_ids = sum(bool(paths) for paths in body_references.values())
    print(
        "bibliography citations OK: "
        f"mandatory={cited_ids}/{len(MANDATORY_IDS)}; "
        f"doi={len(MANDATORY_IDS) - len(missing_dois)}/{len(MANDATORY_IDS)}; "
        f"technical_refs_used={technical_usage}/{len(TECHNICAL_IDS)}; "
        "quartile=PRELIMINARY/PENDING"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
