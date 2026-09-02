# Mobile V1 story verification register

## Purpose

This register is the manual review gate for the 28 academic Mobile V1
stories. It is intentionally separate from the backlog: a row in the backlog
does not prove that an actor, lead, research source, acceptance criterion or
implementation has been verified.

The expected role and segment are taken from the canonical Mobile projection
and target-segment model. Sprint assignment is tracked separately in the
backlog; a story's delivery Sprint is not its research segment. The default
review allocation below comes from the verified handoff and is an assignment,
not an approval or a commit-ownership decision. Joaquín performs a secondary
academic/report-integration review across all 28 stories. Each assigned lead
must be able to explain the story, its four Gherkin scenarios, its Bounded
Context and its evidence boundary before the row is approved.

## Review protocol

For every row, the reviewer records:

1. `Owner / lead`: use the owner-confirmed identity registry and the default
   allocation in this handoff; per-unit ownership still needs explicit review.
2. `Source`: canonical story and any research record or accepted product
   decision used to support it.
3. `Acceptance`: all four scenarios read and checked for actor, permission,
   failure path, duplicate/unknown-result behavior and historical integrity.
4. `Scope`: Product, App, Surface, primary/secondary Bounded Contexts and
   Mobile justification are understood.
5. `Evidence`: research, API, client, device and Product Acceptance status are
   recorded separately; a proposed story is not labeled implemented.
6. `Decision`: `APPROVED`, `REFINE`, `REJECT` or `PENDING HUMAN REVIEW`, with
   reviewer, date and link to the evidence.

## Current report integration approval — 2026-09-02

`28/28 REPORT INTEGRATION APPROVED` by `DiegoS284` (Nexa Team Lead / Mobile
App Lead) and `JoaquinBV511` (Report Lead). The approval covers the current V1
projection, academic Story/AC transcription, Sprint mapping and report
reconciliation.

`INDIVIDUAL DEFENSE REVIEW: FOLLOW-UP / NOT REQUIRED TO BLOCK INTEGRATION`.
The row-level `Source checked`, `Four AC checked` and `Evidence checked`
columns remain `Pending` until each assigned lead performs the separate defense
review. No individual approval is inferred for Gino, Gerard or Sebastián.

## Register

| Story ID | Expected actor / segment | Owning Bounded Context | Owner / lead | Source checked | Four AC checked | Evidence checked | Decision / notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| MOB-US-001 | Mobile User / S1-S3 | BC-01 — Tenant & Access Governance | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-002 | Mobile User / S1-S3 | BC-01 — Tenant & Access Governance | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-003 | Mobile User / S1-S3 | BC-01 — Tenant & Access Governance | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-011 | Warehouse Operator / S1 | BC-03 — Catalog & Commercial Policy | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-012 | Warehouse Operator / S1 | BC-03 — Catalog & Commercial Policy | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-013 | Warehouse Operator / S1 | BC-05 — Inventory Availability | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-014 | Warehouse Operator / S1 | BC-05 — Inventory Availability | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-015 | Warehouse Operator / S1 | BC-05 — Inventory Availability | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-016 | Warehouse Operator / S1 | BC-05 — Inventory Availability | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-017 | Warehouse Operator / S1 | BC-05 — Inventory Availability | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-019 | Warehouse Operator / S1 | BC-06 — Fulfillment & Delivery | Gino / R0obxdnt | Pending | Pending | Pending | Pending human review |
| MOB-US-020 | Dispatch Coordinator / S1 | BC-06 — Fulfillment & Delivery | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-021 | Dispatch Coordinator / S1 | BC-06 — Fulfillment & Delivery | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-022 | Dispatch Coordinator / S1 | BC-06 — Fulfillment & Delivery | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-023 | Dispatch Coordinator / S1 | BC-06 — Fulfillment & Delivery | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-024 | Dispatch Coordinator / S1 | BC-06 — Fulfillment & Delivery | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-025 | Dispatch Coordinator / S1 | BC-06 — Fulfillment & Delivery | Diego / DiegoS284 | Pending | Pending | Pending | Pending human review |
| MOB-US-026 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-027 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-028 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-031 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-032 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-033 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-034 | Driver or Delivery Operator / S2 | BC-06 — Fulfillment & Delivery | Gerard / GerardRojasMancilla | Pending | Pending | Pending | Pending human review |
| MOB-US-044 | Customer Buyer / S3 | BC-10 — Notifications | Sebastián / spinedo214 | Pending | Pending | Pending | Pending human review |
| MOB-US-047 | Customer Buyer / S3 | BC-06 — Fulfillment & Delivery | Sebastián / spinedo214 | Pending | Pending | Pending | Pending human review |
| MOB-US-048 | Customer Buyer / S3 | BC-06 — Fulfillment & Delivery | Sebastián / spinedo214 | Pending | Pending | Pending | Pending human review |
| MOB-US-049 | Customer Buyer / S3 | BC-06 — Fulfillment & Delivery | Sebastián / spinedo214 | Pending | Pending | Pending | Pending human review |

## Current result

`28/28` stories are approved for report integration in this report cut by
`DiegoS284 + JoaquinBV511` on `2026-09-02`. Default leads remain assigned for
the separate individual defense review; that follow-up is not required to
block current report integration. The register must not convert row-level
source, AC or implementation evidence to `APPROVED` from a script, from the
existence of a canonical row or from a commit title.

## Commit relationship

Before a future commit that changes story-specific evidence, the assigned lead
must review the complete row. Current report-integration commits are authorized
by the joint 2026-09-02 gate and must follow the exact owner, username, project
email, branch, file, source, validation and Conventional Commit records in
[human-commit-gate.md](./human-commit-gate.md). No commit is created by this
register itself.
