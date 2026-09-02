#!/usr/bin/env python3
"""Verify every explicit Mobile V1 API mapping against the OpenAPI snapshot."""

from __future__ import annotations

import os
import json
import re
import sys
from pathlib import Path


REPORT_ROOT = Path(__file__).resolve().parents[1]
API_ROOT = Path(os.environ.get("NEXA_API_ROOT", REPORT_ROOT.parent / "api"))
REGISTER = REPORT_ROOT / "delivery-checklists/mobile-v1-api-contract-register.md"
STORIES = (
    REPORT_ROOT
    / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
)
OPENAPI = API_ROOT / "docs/openapi/openapi.json"
EXPECTED_IDS = [
    "MOB-US-001", "MOB-US-002", "MOB-US-003", "MOB-US-011", "MOB-US-012",
    "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017",
    "MOB-US-019", "MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023",
    "MOB-US-024", "MOB-US-025", "MOB-US-026", "MOB-US-027", "MOB-US-028",
    "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034", "MOB-US-044",
    "MOB-US-047", "MOB-US-048", "MOB-US-049",
]


def backlog_rows(text: str) -> list[list[str]]:
    start = text.index("## Backlog summary")
    end = text.index("## Detailed story records", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if not line.startswith("| ") or "MOB-US-" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and re.fullmatch(r"\d+", cells[0]) and re.fullmatch(r"MOB-US-\d{3}", cells[1]):
            rows.append(cells)
    return rows


def api_projection_rows(text: str) -> list[list[str]]:
    start = text.index("## Story-to-contract projection")
    end = text.index("## Reproducible checks", start)
    rows: list[list[str]] = []
    for line in text[start:end].splitlines():
        if not line.startswith("| ") or "MOB-US-" not in line:
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and re.fullmatch(r"S[123]", cells[0]) and re.fullmatch(r"MOB-US-\d{3}", cells[1]):
            rows.append(cells)
    return rows


def main() -> int:
    register_text = REGISTER.read_text(encoding="utf-8")
    document = json.loads(OPENAPI.read_text(encoding="utf-8"))
    backlog = backlog_rows(STORIES.read_text(encoding="utf-8"))
    api_rows = api_projection_rows(register_text)
    story_ids = re.findall(r"^\| S[123] \| (MOB-US-\d{3}) \|", register_text, re.MULTILINE)
    failures: list[str] = []

    if story_ids != EXPECTED_IDS:
        failures.append("API register story IDs/order do not match the canonical 28-row projection")
    if len(set(story_ids)) != len(story_ids):
        failures.append("API register contains duplicate story rows")

    backlog_by_id = {row[1]: row for row in backlog}
    sprint_alignment = 0
    for api_row in api_rows:
        report_row = backlog_by_id.get(api_row[1])
        if report_row is None:
            failures.append(f"API register story is absent from report backlog: {api_row[1]}")
            continue
        if api_row[0] != report_row[6]:
            failures.append(
                f"{api_row[1]} Sprint: API register={api_row[0]!r}, report={report_row[6]!r}"
            )
        else:
            sprint_alignment += 1

    operation_pattern = re.compile(
        r"`(GET|POST|PUT|PATCH|DELETE)\s+([^`]+)`\s+\(`([^`]+)`\)"
    )
    checked = 0
    response_blocks = 0
    request_bodies = 0
    request_examples = 0
    response_examples = 0
    complete_path_params = 0
    for method, path, operation_id in operation_pattern.findall(register_text):
        checked += 1
        normalized_path = path.strip()
        path_item = document.get("paths", {}).get(normalized_path, {})
        operation = path_item.get(method.lower())
        if operation is None:
            failures.append(f"missing OpenAPI operation: {method} {normalized_path} ({operation_id})")
            continue
        actual_operation_id = operation.get("operationId")
        if actual_operation_id != operation_id:
            failures.append(
                f"operationId mismatch for {method} {normalized_path}: "
                f"register={operation_id!r}, openapi={actual_operation_id!r}"
            )
        responses = operation.get("responses", {})
        if not responses:
            failures.append(f"operation has no response block: {method} {normalized_path} ({operation_id})")
        else:
            response_blocks += 1
        content = operation.get("requestBody", {}).get("content", {})
        if content:
            request_bodies += 1
            request_examples += sum(
                len(media.get("examples", {})) + int("example" in media)
                for media in content.values()
            )
        response_examples += sum(
            sum(
                len(media.get("examples", {})) + int("example" in media)
                for media in response.get("content", {}).values()
            )
            for response in responses.values()
        )
        path_variables = set(re.findall(r"{([^}]+)}", normalized_path))
        declared_path_params = {
            parameter.get("name")
            for parameter in [
                *path_item.get("parameters", []),
                *operation.get("parameters", []),
            ]
            if parameter.get("in") == "path"
        }
        if path_variables.issubset(declared_path_params):
            complete_path_params += 1
        else:
            missing = sorted(path_variables - declared_path_params)
            failures.append(
                f"path parameters missing for {method} {normalized_path}: {missing}"
            )

    if failures:
        print("mobile V1 API register validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(
        f"mobile V1 API register OK: stories={len(story_ids)} "
        f"explicit_operations={checked} response_blocks={response_blocks} "
        f"request_bodies={request_bodies} request_examples={request_examples} "
        f"response_examples={response_examples} path_params={complete_path_params}/{checked} "
        f"sprint_alignment={sprint_alignment}/{len(api_rows)} "
        f"openapi_paths={len(document.get('paths', {}))}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
