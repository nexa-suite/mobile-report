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
