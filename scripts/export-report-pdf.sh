#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUTPUT_PATH="${1:-${NEXA_REPORT_PDF_OUTPUT:-${TMPDIR:-/tmp}/nexa-mobile-report.pdf}}"
EXPORT_MODE="${NEXA_REPORT_EXPORT_MODE:-docker}"
PANDOC_IMAGE="${NEXA_PANDOC_IMAGE:-pandoc/latex@sha256:6e71008186280e8908e3816481165c0103d04c64162bc9c3f3fe7bc27c681fc5}"
PANDOC_PLATFORM="${NEXA_PANDOC_PLATFORM:-linux/amd64}"

if [[ "$OUTPUT_PATH" != /* ]]; then
  OUTPUT_PATH="$REPO_ROOT/$OUTPUT_PATH"
fi

mkdir -p "$(dirname "$OUTPUT_PATH")"
OUTPUT_DIR="$(cd "$(dirname "$OUTPUT_PATH")" && pwd)"
OUTPUT_NAME="$(basename "$OUTPUT_PATH")"
BUILD_DIR="$(mktemp -d "${TMPDIR:-/tmp}/nexa-mobile-report-build.XXXXXX")"
COMBINED_SOURCE="$BUILD_DIR/report.md"
trap 'rm -rf "$BUILD_DIR"' EXIT

SOURCES=(
  report/00-front-matter/00-cover.md
  report/00-front-matter/01-version-history.md
  report/00-front-matter/02-project-report-collaboration-insights.md
  report/00-front-matter/04-student-outcome.md
  report/00-front-matter/05-smart-objectives.md
)

while IFS= read -r source; do
  case "$source" in
    report/00-front-matter/03-contents.md)
      continue
      ;;
  esac
  SOURCES+=("$source")
done < <(
  find \
    report/01-presentation \
    report/02-requirements-and-software-solution-design \
    report/03-solution-ui-ux-design \
    report/04-product-implementation-and-validation \
    report/90-conclusions \
    report/91-glossary \
    report/92-bibliography \
    report/93-annexes \
    report/assets \
    -type f -name '*.md' -print | LC_ALL=C sort
)

append_source() {
  local source="$1"
  sed \
    -e 's|\.\./\.\./\.\./assets/|assets/|g' \
    -e 's|\.\./\.\./assets/|assets/|g' \
    -e 's|\.\./assets/|assets/|g' \
    "$REPO_ROOT/$source"
  printf '\n\n'
}

{
  append_source "${SOURCES[0]}"
  printf '\\clearpage\n\\tableofcontents\n\\clearpage\n\n'
  for source in "${SOURCES[@]:1}"; do
    append_source "$source"
  done
} > "$COMBINED_SOURCE"

PANDOC_ARGUMENTS=(
  --from=markdown+raw_tex+task_lists+strikeout+autolink_bare_uris+emoji
  --standalone
  --top-level-division=section
  --pdf-engine=xelatex
  --lua-filter="$REPO_ROOT/scripts/report-pdf-filter.lua"
  --resource-path="$REPO_ROOT:$REPO_ROOT/report:$REPO_ROOT/report/assets:$BUILD_DIR"
  --metadata=lang:es
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
      --lua-filter=/workspace/scripts/report-pdf-filter.lua \
      --resource-path=/workspace:/workspace/report:/workspace/report/assets:/build \
      --metadata=lang:es \
      --variable=geometry:margin=1in \
      --variable=fontsize:11pt \
      /build/report.md \
      -o "/out/$OUTPUT_NAME"
    ;;
  *)
    printf 'Unsupported NEXA_REPORT_EXPORT_MODE: %s (use native or docker)\n' "$EXPORT_MODE" >&2
    exit 2
    ;;
esac

if [[ ! -s "$OUTPUT_PATH" ]]; then
  printf 'PDF export did not produce a non-empty file: %s\n' "$OUTPUT_PATH" >&2
  exit 1
fi

printf 'report PDF export OK: sources=%s output=%s mode=%s\n' "${#SOURCES[@]}" "$OUTPUT_PATH" "$EXPORT_MODE"
