#!/usr/bin/env bash
set -euo pipefail

report_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
statement_file=${NEXA_MOBILE_STATEMENT_PDF:-}
blueprint_root=${NEXA_BLUEPRINT_ROOT:-$report_root/../blueprint}
rubric_file=${NEXA_MOBILE_RUBRIC:-$blueprint_root/90-academic/mobile/enunciado-trabajo-final.md}
expected_statement_sha='38be0c1baa77d0601c9605ef9ea72ad2fb510222a17a65944a06690621169f37'
expected_rubric_sha='ac734ff3fe33f38185cd57b05d2ed48cd42a46239c87a78ff98418a4bb5b8e6f'

[[ -n "$statement_file" ]] || {
  echo 'BLOCKED BY MISSING LOCAL EXTERNAL SOURCE: set NEXA_MOBILE_STATEMENT_PDF to Final Project Statement V4.0' >&2
  exit 2
}
[[ -f "$statement_file" ]] || {
  echo "BLOCKED BY MISSING LOCAL EXTERNAL SOURCE: NEXA_MOBILE_STATEMENT_PDF=$statement_file" >&2
  exit 2
}
[[ -f "$rubric_file" ]] || {
  echo "BLOCKED BY MISSING LOCAL EXTERNAL SOURCE: Mobile rubric not found at $rubric_file" >&2
  exit 2
}

actual_statement_sha=$(shasum -a 256 "$statement_file" | awk '{print $1}')
actual_rubric_sha=$(shasum -a 256 "$rubric_file" | awk '{print $1}')

[[ "$actual_statement_sha" == "$expected_statement_sha" ]] || {
  echo "Final Project Statement V4.0 fingerprint mismatch: expected $expected_statement_sha, got $actual_statement_sha" >&2
  exit 1
}
[[ "$actual_rubric_sha" == "$expected_rubric_sha" ]] || {
  echo "Mobile rubric fingerprint mismatch: expected $expected_rubric_sha, got $actual_rubric_sha" >&2
  exit 1
}

printf 'canonical sources OK: statement=%s rubric=%s\n' "$actual_statement_sha" "$actual_rubric_sha"
