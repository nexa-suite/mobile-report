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
    text = module.STORIES.read_text(encoding="utf-8")
    scenarios = len(re.findall(r"<strong>Scenario:", text))
    print(
        "mobile V1 transcription OK: lifecycle_stories=73; detailed_v1=28; "
        f"source_scenarios=256; rendered_v1_gherkin_scenarios={scenarios}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
