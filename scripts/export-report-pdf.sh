#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEFAULT_OUTPUT="$REPO_ROOT/output/upc-pre-202620-1acc0238-4949-nexa-team-report-av1.pdf"
OUTPUT_PATH="${1:-${NEXA_REPORT_PDF_OUTPUT:-$DEFAULT_OUTPUT}}"
REQUESTED_MODE="${NEXA_REPORT_EXPORT_MODE:-auto}"
PANDOC_IMAGE="${NEXA_PANDOC_IMAGE:-pandoc/latex@sha256:6e71008186280e8908e3816481165c0103d04c64162bc9c3f3fe7bc27c681fc5}"
PANDOC_PLATFORM="${NEXA_PANDOC_PLATFORM:-linux/amd64}"

if [[ "$OUTPUT_PATH" != /* ]]; then
  OUTPUT_PATH="$REPO_ROOT/$OUTPUT_PATH"
fi

if [[ "$REQUESTED_MODE" == "auto" ]]; then
  if command -v pandoc >/dev/null && command -v xelatex >/dev/null; then
    EXPORT_MODE="native"
  elif command -v docker >/dev/null; then
    EXPORT_MODE="docker"
  else
    printf 'PDF export requires pandoc plus xelatex, or Docker.\n' >&2
    exit 2
  fi
else
  EXPORT_MODE="$REQUESTED_MODE"
fi

mkdir -p "$(dirname "$OUTPUT_PATH")"
OUTPUT_DIR="$(cd "$(dirname "$OUTPUT_PATH")" && pwd)"
OUTPUT_NAME="$(basename "$OUTPUT_PATH")"
BUILD_DIR="$(mktemp -d "${TMPDIR:-/tmp}/nexa-mobile-report-build.XXXXXX")"
COMBINED_SOURCE="$BUILD_DIR/report.md"
HEADER_FILE="$BUILD_DIR/pdf-header.tex"
CANONICAL_SOURCES="$BUILD_DIR/canonical-sources.txt"
trap 'rm -rf "$BUILD_DIR"' EXIT

FRONT_MATTER=(
  report/00-front-matter/00-cover.md
  report/00-front-matter/01-version-history.md
  report/00-front-matter/02-project-report-collaboration-insights.md
  report/00-front-matter/03-contents.md
  report/00-front-matter/04-student-outcome.md
  report/00-front-matter/05-smart-objectives.md
)

REPORT_ROOTS=(
  report/01-presentation
  report/02-requirements-and-software-solution-design
  report/03-solution-ui-ux-design
  report/04-product-implementation-and-validation
  report/90-conclusions
  report/91-glossary
  report/92-bibliography
  report/93-annexes
)

for source in "${FRONT_MATTER[@]}"; do
  [[ -f "$REPO_ROOT/$source" ]] || {
    printf 'Missing required report source: %s\n' "$source" >&2
    exit 1
  }
done

for root in "${REPORT_ROOTS[@]}"; do
  [[ -d "$REPO_ROOT/$root" ]] || {
    printf 'Missing required report directory: %s\n' "$root" >&2
    exit 1
  }
done

find "${REPORT_ROOTS[@]/#/$REPO_ROOT/}" -type f -name '*.md' -print \
  | LC_ALL=C sort > "$CANONICAL_SOURCES"

if grep -Eq '/(chapter-overview|section-overview|sprint-overview)\.md$' \
  "$CANONICAL_SOURCES"; then
  printf 'Temporary overview source remains in the report tree.\n' >&2
  exit 1
fi

append_source() {
  local source="$1"
  sed -E 's|(\.\./)+assets/|report/assets/|g' "$REPO_ROOT/$source"
  printf '\n\n'
}

{
  append_source "${FRONT_MATTER[0]}"
  printf '\\clearpage\n\\tableofcontents\n\\clearpage\n\n'
  for source in "${FRONT_MATTER[@]:1}"; do
    append_source "$source"
  done
  while IFS= read -r absolute_source; do
    source="${absolute_source#"$REPO_ROOT/"}"
    append_source "$source"
  done < "$CANONICAL_SOURCES"
} > "$COMBINED_SOURCE"

printf '%s\n' '\usepackage{pdflscape}' > "$HEADER_FILE"

PANDOC_ARGUMENTS=(
  --from=markdown+raw_tex+task_lists+strikeout+autolink_bare_uris+emoji
  --standalone
  --top-level-division=section
  --pdf-engine=xelatex
  --include-in-header="$HEADER_FILE"
  --lua-filter="$REPO_ROOT/scripts/lib/report-pdf-filter.lua"
  --resource-path="$REPO_ROOT:$REPO_ROOT/report:$REPO_ROOT/report/assets:$BUILD_DIR"
  --metadata=lang:es
  --variable=papersize:a4
  --variable=geometry:margin=1in
  --variable=fontsize:11pt
)

case "$EXPORT_MODE" in
  native)
    command -v pandoc >/dev/null
    command -v xelatex >/dev/null
    pandoc "${PANDOC_ARGUMENTS[@]}" "$COMBINED_SOURCE" -o "$OUTPUT_PATH"
    ;;
  docker)
    command -v docker >/dev/null
    if ! docker image inspect "$PANDOC_IMAGE" >/dev/null 2>&1; then
      docker pull --platform "$PANDOC_PLATFORM" "$PANDOC_IMAGE"
    fi
    docker run --rm \
      --platform "$PANDOC_PLATFORM" \
      -v "$REPO_ROOT:/workspace:ro" \
      -v "$BUILD_DIR:/build:ro" \
      -v "$OUTPUT_DIR:/out" \
      -w /workspace \
      "$PANDOC_IMAGE" \
      --from=markdown+raw_tex+task_lists+strikeout+autolink_bare_uris+emoji \
      --standalone \
      --top-level-division=section \
      --pdf-engine=xelatex \
      --include-in-header=/build/pdf-header.tex \
      --lua-filter=/workspace/scripts/lib/report-pdf-filter.lua \
      --resource-path=/workspace:/workspace/report:/workspace/report/assets:/build \
      --metadata=lang:es \
      --variable=papersize:a4 \
      --variable=geometry:margin=1in \
      --variable=fontsize:11pt \
      /build/report.md \
      -o "/out/$OUTPUT_NAME"
    ;;
  *)
    printf 'Unsupported NEXA_REPORT_EXPORT_MODE: %s (use auto, native, or docker)\n' "$EXPORT_MODE" >&2
    exit 2
    ;;
esac

if [[ ! -s "$OUTPUT_PATH" ]]; then
  printf 'PDF export did not produce a non-empty file: %s\n' "$OUTPUT_PATH" >&2
  exit 1
fi

printf 'report PDF export OK: sources=%s output=%s mode=%s\n' \
  "$(wc -l < "$CANONICAL_SOURCES" | tr -d ' ')" "$OUTPUT_PATH" "$EXPORT_MODE"
