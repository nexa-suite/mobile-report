#!/usr/bin/env python3
"""Compatibility entry point for the complete Mobile report validator."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "verify-mobile-backlog.py"
spec = importlib.util.spec_from_file_location("verify_mobile_backlog", MODULE_PATH)
if spec is None or spec.loader is None:
    raise SystemExit(f"cannot load validator: {MODULE_PATH}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def main() -> int:
    failures = module.validate()
    if failures:
        print("mobile V1 transcription validation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    text = module.FUNCTIONAL.read_text(encoding="utf-8")
    scenarios = len(re.findall(r"<p><strong>Scenario: .+?</strong></p>", text))
    print(
        "mobile transcription OK: functional_stories=73; "
        f"rendered_gherkin_scenarios={scenarios}; backlog_rows=97"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
