#!/usr/bin/env python3
"""Render deterministic SVG Bounded Context Canvases from 2.5.1.3 Markdown."""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.3-bounded-context-canvases.md"
DEFAULT_OUTPUT = REPO_ROOT / "report/assets/chapter-2/bounded-context-canvases"
EXPECTED_ORDER = ["BC-04", "BC-05", "BC-06", "BC-03", "BC-02", "BC-07", "BC-01", "BC-11", "BC-08", "BC-09", "BC-10"]
STAGE_LABELS = {
    "Context Overview": "Context / Purpose",
    "Business Rules & Ubiquitous Language": "Ubiquitous Language / Invariants",
    "Capability Analysis": "Capabilities",
    "Capability Layering": "Capability Layering",
    "Dependencies": "Inbound / Outbound Dependencies",
    "Design Critique": "Design Critique / Rejected Alternative",
}
COLORS = {"Core": "#0f4c5c", "Supporting": "#3d5a80", "Generic": "#495057"}


def normalize(value: str) -> str:
    value = re.sub(r"[`*_]", "", value)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def compact(value: str, limit: int = 330) -> str:
    value = normalize(value)
    sentences = re.split(r"(?<=[.!?])\s+", value)
    result = ""
    for sentence in sentences:
        candidate = f"{result} {sentence}".strip()
        if len(candidate) > limit:
            break
        result = candidate
        if len(result) >= limit * 0.72:
            break
    if not result:
        result = value[:limit].rstrip()
    if len(result) < len(value):
        result = result.rstrip(" .") + "…"
    return result


def wrap(value: str, width: int = 74) -> list[str]:
    words = value.split()
    lines: list[str] = []
    line = ""
    for word in words:
        if line and len(line) + len(word) + 1 > width:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        lines.append(line)
    return lines


def text_element(value: str, x: int, y: int, size: int, *, weight: str = "400", fill: str = "#18212b") -> str:
    return f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}px" font-weight="{weight}" fill="{fill}">{html.escape(value)}</text>'


def parse_canvases(text: str) -> list[dict[str, object]]:
    headings = list(re.finditer(r"^## (BC-\d{2}) (.+?) — (Core|Supporting|Generic)$", text, re.MULTILINE))
    canvases: list[dict[str, object]] = []
    table_cell_pattern = re.compile(r"^\| (.+?) \| (.+?) \|$", re.MULTILINE)
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.start() : end]
        stages: dict[str, str] = {}
        for row in table_cell_pattern.finditer(block):
            for cell in row.groups():
                match = re.match(r"\*\*(.+?)\*\*<br><br>(.+)$", cell.strip())
                if match and match.group(1).strip() in STAGE_LABELS:
                    stages[match.group(1).strip()] = compact(match.group(2))
        missing = [stage for stage in STAGE_LABELS if stage not in stages]
        if missing:
            raise SystemExit(f"{heading.group(1)} missing stages: {', '.join(missing)}")
        canvases.append({
            "code": heading.group(1),
            "name": heading.group(2).strip(),
            "classification": heading.group(3),
            "stages": stages,
        })
    if [canvas["code"] for canvas in canvases] != EXPECTED_ORDER:
        raise SystemExit("2.5.1.3 canvas order is not BC-01..BC-11")
    return canvases


def render(canvas: dict[str, object]) -> str:
    code = str(canvas["code"])
    name = str(canvas["name"])
    classification = str(canvas["classification"])
    stages = canvas["stages"]
    assert isinstance(stages, dict)
    width = 1600
    box_width = 750
    box_height = 300
    header_height = 120
    meta_height = 70
    gap = 28
    top = header_height + meta_height + 26
    height = top + 3 * box_height + 2 * gap + 72
    accent = COLORS[classification]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#f7f9fb"/>',
        f'<rect width="{width}" height="{header_height}" fill="{accent}"/>',
        text_element(f"{code} {name} — Bounded Context Canvas", 46, 62, 34, weight="700", fill="#ffffff"),
        text_element("Strategic DDD visual summary sourced from 2.5.1.3", 46, 98, 18, fill="#e7eef3"),
        f'<rect x="46" y="{header_height + 22}" width="300" height="38" rx="19" fill="{accent}"/>',
        text_element(f"Classification: {classification}", 68, header_height + 47, 18, weight="700", fill="#ffffff"),
    ]
    ordered_stages = list(STAGE_LABELS)
    for index, stage in enumerate(ordered_stages):
        row, col = divmod(index, 2)
        x = 46 + col * (box_width + gap)
        y = top + row * (box_height + gap)
        parts.append(f'<rect x="{x}" y="{y}" width="{box_width}" height="{box_height}" rx="14" fill="#ffffff" stroke="#c8d2dc" stroke-width="2"/>')
        parts.append(f'<rect x="{x}" y="{y}" width="{box_width}" height="54" rx="14" fill="#eaf0f5"/>')
        parts.append(f'<rect x="{x}" y="{y + 40}" width="{box_width}" height="14" fill="#eaf0f5"/>')
        parts.append(text_element(STAGE_LABELS[stage], x + 22, y + 35, 21, weight="700", fill=accent))
        lines = wrap(str(stages[stage]), width=66)
        for line_index, line in enumerate(lines[:8]):
            parts.append(text_element(line, x + 22, y + 88 + line_index * 26, 18))
    footer_y = height - 28
    parts.append(text_element("Source: accepted semantic canvas content in report/2.5.1.3", 46, footer_y, 16, fill="#5e6b78"))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    canvases = parse_canvases(SOURCE.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    for canvas in canvases:
        filename = f"{str(canvas['code']).lower()}-{re.sub(r'[^a-z0-9]+', '-', str(canvas['name']).lower()).strip('-')}.svg"
        (args.output / filename).write_text(render(canvas), encoding="utf-8")
    print(f"rendered {len(canvases)} deterministic SVG canvases to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
