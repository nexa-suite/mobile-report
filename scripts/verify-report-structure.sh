#!/usr/bin/env bash
set -euo pipefail

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
stories="$repo_root/report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
strategic_traceability="$repo_root/report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.4-strategic-ddd-traceability.md"
sprint_index="$repo_root/report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/section-overview.md"
transcription_validator="$repo_root/scripts/verify-mobile-v1-transcription.py"
review_register_validator="$repo_root/scripts/verify-mobile-v1-review-register.py"
canonical_sources_validator="$repo_root/scripts/verify-canonical-sources.sh"
ownership_matrix_validator="$repo_root/scripts/verify-diff-ownership-matrix.py"
bibliography_citations_validator="$repo_root/scripts/verify-bibliography-citations.py"
semantic_validator="$repo_root/scripts/verify-mobile-v1-semantics.py"
mobile_backlog_validator="$repo_root/scripts/verify-mobile-backlog.py"

[[ -f "$stories" ]] || { echo "missing User Stories file: $stories" >&2; exit 1; }
[[ -f "$transcription_validator" ]] || { echo "missing Mobile V1 transcription validator: $transcription_validator" >&2; exit 1; }
[[ -f "$review_register_validator" ]] || { echo "missing Mobile V1 review-register validator: $review_register_validator" >&2; exit 1; }
[[ -f "$canonical_sources_validator" ]] || { echo "missing canonical-source validator: $canonical_sources_validator" >&2; exit 1; }
[[ -f "$ownership_matrix_validator" ]] || { echo "missing diff ownership-matrix validator: $ownership_matrix_validator" >&2; exit 1; }
[[ -f "$bibliography_citations_validator" ]] || { echo "missing bibliography-citations validator: $bibliography_citations_validator" >&2; exit 1; }
[[ -f "$semantic_validator" ]] || { echo "missing Mobile V1 semantic validator: $semantic_validator" >&2; exit 1; }
[[ -f "$mobile_backlog_validator" ]] || { echo "missing complete Mobile backlog validator: $mobile_backlog_validator" >&2; exit 1; }

bash "$canonical_sources_validator"
python3 "$ownership_matrix_validator"
python3 "$transcription_validator"
python3 "$review_register_validator"
python3 "$bibliography_citations_validator"
python3 "$semantic_validator"
python3 "$mobile_backlog_validator"

headings=$(rg -c '^### MOB-US-' "$stories")
summary_rows=$(awk -F'|' '/^\| [0-9]+ \| MOB-US-/{c++} END{print c+0}' "$stories")
scenarios=$(rg -o '<strong>Scenario:' "$stories" | wc -l | tr -d ' ')
expected_story_ids='MOB-US-001 MOB-US-002 MOB-US-003 MOB-US-004 MOB-US-005 MOB-US-006 MOB-US-007 MOB-US-008 MOB-US-009 MOB-US-010 MOB-US-011 MOB-US-012 MOB-US-013 MOB-US-014 MOB-US-015 MOB-US-016 MOB-US-017 MOB-US-018 MOB-US-019 MOB-US-020 MOB-US-021 MOB-US-022 MOB-US-023 MOB-US-024 MOB-US-025 MOB-US-026 MOB-US-027 MOB-US-028 MOB-US-029 MOB-US-030 MOB-US-031 MOB-US-032 MOB-US-033 MOB-US-034 MOB-US-035 MOB-US-036 MOB-US-037 MOB-US-038 MOB-US-039 MOB-US-040 MOB-US-041 MOB-US-042 MOB-US-043 MOB-US-044 MOB-US-045 MOB-US-046 MOB-US-047 MOB-US-048 MOB-US-049 MOB-US-050 MOB-US-051 MOB-US-052 MOB-US-053 MOB-US-054 MOB-US-055 MOB-US-056 MOB-US-057 MOB-US-058 MOB-US-059 MOB-US-060 MOB-US-061 MOB-US-062 MOB-US-063 MOB-US-064 MOB-US-065 MOB-US-066 MOB-US-067 MOB-US-068 MOB-US-069 MOB-US-070 MOB-US-071 MOB-US-072 MOB-US-073'
actual_story_ids=$(awk '/^### MOB-US-/{print $2}' "$stories" | paste -sd' ' -)
context_rows=$(awk -F'|' '/^\| BC-[0-9][0-9] —/{c++} END{print c+0}' "$strategic_traceability")
sprint_rows=$(awk -F'|' '/^\| Sprint [123] \|/{c++} END{print c+0}' "$sprint_index")

[[ "$headings" -eq 73 ]] || { echo "expected 73 detailed stories, got $headings" >&2; exit 1; }
[[ "$summary_rows" -eq 28 ]] || { echo "expected 28 summary rows, got $summary_rows" >&2; exit 1; }
[[ "$scenarios" -eq 259 ]] || { echo "expected 259 rendered Gherkin scenarios (256 source + 3 reconciled), got $scenarios" >&2; exit 1; }
[[ "$actual_story_ids" == "$expected_story_ids" ]] || { echo "Mobile story IDs/order do not match the live 73-row lifecycle index" >&2; exit 1; }
[[ "$context_rows" -eq 11 ]] || { echo "expected 11 strategic Bounded Context rows, got $context_rows" >&2; exit 1; }
[[ "$sprint_rows" -eq 3 ]] || { echo "expected exactly three canonical Sprint rows, got $sprint_rows" >&2; exit 1; }
! rg -q '^\| Sprint 4 \|' "$sprint_index" || { echo "non-canonical Sprint 4 row found" >&2; exit 1; }
rg -Fq 'MOB-US-001..017, MOB-US-019' "$sprint_index" || { echo "canonical Sprint 1 mapping missing" >&2; exit 1; }
rg -Fq 'MOB-US-020..034' "$sprint_index" || { echo "canonical Sprint 2 mapping missing" >&2; exit 1; }
rg -Fq 'MOB-US-044, MOB-US-047..049' "$sprint_index" || { echo "canonical Sprint 3 mapping missing" >&2; exit 1; }

required_files=(
  "$repo_root/report/00-front-matter/00-cover.md"
  "$repo_root/report/00-front-matter/03-contents.md"
  "$repo_root/report/00-front-matter/04-student-outcome.md"
  "$repo_root/report/01-presentation/1.3-target-segments/target-segments.md"
  "$repo_root/report/02-requirements-and-software-solution-design/2.2-interviews/2.2.4-physical-operations-and-delivery-research-plan.md"
  "$repo_root/report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.4-strategic-ddd-traceability.md"
  "$repo_root/report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/2.6.1-bounded-context-coverage.md"
  "$repo_root/report/03-solution-ui-ux-design/chapter-overview.md"
  "$repo_root/report/04-product-implementation-and-validation/chapter-overview.md"
  "$sprint_index"
  "$repo_root/delivery-checklists/mobile-v1-story-verification-register.md"
)

for file in "${required_files[@]}"; do
  [[ -f "$file" ]] || { echo "missing required report artifact: $file" >&2; exit 1; }
done

if rg -n -i '\b(AI-generated|generated by AI|Codex|LLM|subagent|agentic|prompt engineering)\b' \
  "$repo_root/README.md" "$repo_root/report" "$repo_root/delivery-checklists" --glob '*.md'; then
  echo "prohibited internal attribution found in report documentation" >&2
  exit 1
fi

if rg -n '[[:blank:]]+$' "$repo_root/README.md" "$repo_root/report" "$repo_root/delivery-checklists" --glob '*.md'; then
  echo "trailing whitespace found in report documentation" >&2
  exit 1
fi

printf 'report structure OK: stories=%s summary_rows=%s scenarios=%s\n' "$headings" "$summary_rows" "$scenarios"
