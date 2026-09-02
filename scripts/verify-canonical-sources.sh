#!/usr/bin/env bash
set -euo pipefail

report_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
prompt_file=${NEXA_CANONICAL_PROMPT:-/Users/joaquinfranciscoverdebueno/Downloads/NEXA MOBILE ACADEMIC REPORT .md}
rubric_file=${NEXA_MOBILE_RUBRIC:-$report_root/../blueprint/90-academic/mobile/enunciado-trabajo-final.md}
expected_prompt_sha='af86ca49fb0e7b2add5313116bc7fd4651add5e8562bf215a8f9a78296a20370'
expected_rubric_sha='ac734ff3fe33f38185cd57b05d2ed48cd42a46239c87a78ff98418a4bb5b8e6f'

[[ -f "$prompt_file" ]] || { echo "missing canonical prompt: $prompt_file" >&2; exit 1; }
[[ -f "$rubric_file" ]] || { echo "missing Mobile rubric: $rubric_file" >&2; exit 1; }

actual_prompt_sha=$(shasum -a 256 "$prompt_file" | awk '{print $1}')
actual_rubric_sha=$(shasum -a 256 "$rubric_file" | awk '{print $1}')

[[ "$actual_prompt_sha" == "$expected_prompt_sha" ]] || {
  echo "canonical prompt fingerprint mismatch: expected $expected_prompt_sha, got $actual_prompt_sha" >&2
  exit 1
}
[[ "$actual_rubric_sha" == "$expected_rubric_sha" ]] || {
  echo "Mobile rubric fingerprint mismatch: expected $expected_rubric_sha, got $actual_rubric_sha" >&2
  exit 1
}

printf 'canonical sources OK: prompt=%s rubric=%s\n' "$actual_prompt_sha" "$actual_rubric_sha"
