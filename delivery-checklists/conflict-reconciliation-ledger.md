# Conflict Reconciliation Ledger

**Status:** RESOLVED / VALIDATED

**Date:** 2026-09-02

**Human owner:** Joaquín Francisco Verde Bueno

**Purpose:** Non-academic delivery record for the approved report integration.

## Reconciliation inputs

| Ref | Meaning |
|---|---|
| `origin/develop` / ours | `928cb1c4ca0a0848c4b0c0de32108c87ee97dada` after the approved fast-forward of the main-only Chapter II commit |
| `feature/report-front-matter-and-governance` / theirs | `a19642c38ecf21905874fc5fbabceff0410320b6` |
| `origin/main` | `928cb1c4ca0a0848c4b0c0de32108c87ee97dada`; must remain unchanged |
| Initial report baseline | `3edeb196800a72a30299987a661e791c8f8fb50d` |

## Decision protocol

The current feature branch is the default semantic baseline. The Blueprint and
approved owner decision are authoritative for product meaning. Unique valid
content from develop and main must remain when it is not superseded. Each
conflict group is resolved by path and meaning; no global side selection is
used. Historical, future, pending and verified statements retain their
status rather than being converted into claims of completed evidence.

| Conflict path or group | Category | Feature meaning | Develop/main meaning | Canonical source | Decision | Result |
|---|---|---|---|---|---|---|
| `README.md` | A/C | Current report navigation, delivery references and control links | Basic report navigation and status template | Current report package and Blueprint | Keep current feature navigation; retain equivalent valid navigation | Resolved and included in `86351b3` |
| `delivery-checklists/av1.md`, `av2.md`, `tb1.md`, `tb2.md` | A | Reproducible gates with honest open/PARTIAL states | Short placeholders | Approved report gate model | Keep feature gates; placeholders are not evidence | Resolved and included in `86351b3` |
| `report/01-presentation/1.3-target-segments/target-segments.md` | A/D | V1 Operations/Buyer scope, deferred Sales scope, navigation handoff and no live tracking | Broad candidate scope including stale delivery and Sales wording | Blueprint V1 semantics | Keep feature mapping and explicit V1 boundaries | Resolved and included in `86351b3` |
| `report/02-requirements-and-software-solution-design/2.2-interviews/2.2.1-interview-design.md`, `2.2.2-interview-records.md`, `2.2.3-interview-analysis.md` | A/C | Three segments, recruitment protocol, provenance boundaries and no fabricated interviews | Generic future interview placeholders | Research authority and verified evidence | Keep feature research plan/status; preserve the absence of verified interviews | Resolved and included in `86351b3` |
| `report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.5-big-picture-eventstorming.md`, `2.3.6-ubiquitous-language.md` | A/C | Candidate domain events, exact context vocabulary, no Mobile/Scanner/QR/Device BC | Earlier generic event and terminology notes | Approved DDD model and Blueprint | Keep feature detail; retain valid 11-context and terminology boundaries | Resolved and included in `86351b3` |
| `report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.0-to-be-scenario-mapping.md`, `2.4.1-user-stories.md`, `2.4.2-impact-mapping.md`, `2.4.3-product-backlog.md` | A/D | Exact V1 target map and 28-story backlog with open impact metrics | Broad scenarios and stale 49-story/7-epic planning baseline | Approved V1 story register and Blueprint | Keep feature V1 requirements; do not carry stale totals as current scope | Resolved and included in `86351b3` |
| `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/**` conflicted files | A/C | Detailed target DDD, exact 11 strategic contexts and architecture boundaries | Shorter baseline diagrams and context list | Approved strategic DDD and C4 rules | Keep feature target model; preserve the valid 11-context boundary | Resolved and included in `86351b3` |
| `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/code-level-diagrams/**` and `section-overview.md` | A/C | Current tactical/API/persistence evidence, BC-06 model and honest status | Placeholder diagrams and generic 11-context references | Approved tactical model and evidence registers | Keep feature evidence; do not upgrade pending evidence | Resolved and included in `86351b3` |
| `report/03-solution-ui-ux-design/**` conflicted files | A | Current Design Lab-informed IA, mobile flows and evidence limits | Earlier scaffolding/placeholders | Released Design Lab and Blueprint scope | Keep feature UX package and its unverified-state wording | Resolved and included in `86351b3` |
| `report/04-product-implementation-and-validation/**` conflicted files | A/C | Three sprints, implementation evidence boundaries and pending validation records | Short placeholders | Approved sprint model and evidence status | Keep feature package; S1→TB1, S2→AV2, S3→TB2, no Sprint 4 | Resolved and included in `86351b3` |
| `report/90-conclusions/**`, `91-glossary/**`, `92-bibliography/**`, `93-annexes/**`, `report/assets/asset-index.md` | A/C | Current conclusion limits, vocabulary, source metadata and annex index | Older placeholders or narrower baseline text | Academic structure, source register and Blueprint | Keep feature package; retain only valid structure not contradicted by current meaning | Resolved and included in `86351b3` |
| Main-only commit `928cb1c` (`docs(mobile): adapt chapter 2 report`) | C/D | Current feature package supersedes stale portions while preserving valid structure | Chapter II baseline added directly to main | Owner decision and Blueprint | Audited; no valid unique content is intentionally dropped, and non-conflicted paths remain | Fast-forwarded into `develop`; reconciled in `86351b3` |

## Required semantic checks

- V1 is online-first. Local state is limited to safe drafts, temporary evidence
  and retry metadata; server state remains authoritative.
- V1 location is an external navigation handoff to an authorized destination.
  There is no continuous GPS, live tracking, ETA, geofence or route
  optimization commitment.
- Operations Mobile covers warehouse receiving/picking, dispatch handoff and
  driver delivery execution/proof. Buyer Mobile covers delivery updates,
  handoff verification, receipt and discrepancy. Sales is not a current
  Operations Mobile V1 role.
- Tenant and Workspace remain distinct; their V1 one-to-one projection is not
  a security or C4 identity rule.
- The report retains exactly 28 V1 stories and 112 Gherkin scenarios, while
  the 73-story Product Mobile roadmap remains V1 28, V2 35, V3 9 and V4/Future
  1 unless the Blueprint changes.
- The DDD model retains exactly 11 strategic Bounded Contexts and one Nexa C4
  Software System. Mobile is a container/surface, not a Bounded Context.

## Semantic scan classification

The approved scan was run across every Markdown file under `report/` after the
conflict paths were resolved. Terms were classified by their surrounding
meaning, not rejected globally.

| Category | Count | Interpretation |
|---|---:|---|
| Valid current | 233 | Current online-first, authority, surface and scope statements |
| Valid boundary | 81 | Explicit exclusions, negative rules and non-authoritative local states |
| Future/research | 105 | Spikes, hypotheses, open questions, deferred scope and research conditions |
| Historical/context | 28 | Historical baselines, secondary/competitor context and source discussion |
| Stale | 0 | No unresolved approved-conflict semantic claim |

The scan also confirmed `stories=28`, `scenarios=112`,
`strategic_contexts=11`, exactly three canonical Sprints, no Sprint 4 artifact,
and no technical surface presented as a Bounded Context.

## Reconciliation result

All `76/76` conflict paths were resolved by semantic path-level decisions and
committed by the human owner above in the non-squashed merge commit
`86351b3c75f471cb79c3d677718cf07dd035ae55`, with parents
`928cb1c4ca0a0848c4b0c0de32108c87ee97dada` and
`a19642c38ecf21905874fc5fbabceff0410320b6`.

The reconciliation branch was published at
`origin/reconcile/report-integration-20260902`. Report structure, semantic
inventory, transcription, review register, API register, bibliography,
links, Structurizr, PlantUML/data-model evidence and Markdown checks passed.
The expanded API integration gate was rerun with the external services
available and remains `PARTIAL`: `482` tests, `3` known
`TenantAdministrationIT` failures, `0` errors and `0` skipped. This ledger does
not change that status.
