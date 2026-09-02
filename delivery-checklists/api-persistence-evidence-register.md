# API persistence evidence register

## Scope and evidence boundary

This register records a source-backed and runtime-observed persistence slice for
the Mobile V1 projection. It is not a Database Design Diagram, it does not
assign ownership merely because tables share a PostgreSQL instance, and it does
not prove Mobile client consumption or Product Acceptance.

| Field | Observed value |
| :--- | :--- |
| API repository / source SHA | `/Users/joaquinfranciscoverdebueno/Developer/nexa-suite/api` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` on `main` |
| Compose container | `nexa-modern-postgres` |
| Database inspection | `PostgreSQL 18.4` on `aarch64-unknown-linux-musl`; database `nexa`; inspection role `nexa` |
| Source migrations inspected | `V77`, `V79`, `V91`, `V93`, `V94`, `V95`, `V96`, `V97`, `V98`, `V99` |
| Runtime status | `nexa-modern-postgres` healthy on the latest read-only capture; schema queried without changing data |
| Academic state | `PARTIAL — schema and constraints observed; diagram, source export and human review pending` |

The logical Bounded Context column below is a target classification from the
reconciled Blueprint/report model. It must be reviewed by the architecture/data
owner before it becomes an academic claim.

## Latest read-only runtime capture — 2026-09-02

| Field | Observed value |
| :--- | :--- |
| Preparation | Docker Desktop was available; only the stopped `nexa-modern-postgres` container was started for this query |
| Exact command | `bash scripts/inspect-api-persistence.sh` from the report repository |
| Result | Exit `0`; PostgreSQL `18.4` on `aarch64-unknown-linux-musl`; selected schema tables, columns, constraint counts, triggers and policies returned |
| Data safety | The script queries PostgreSQL system catalogs only; no insert, update, delete or migration was executed |
| Scope limit | This is backend persistence evidence, not Mobile client, device, Product Acceptance or final academic diagram evidence |

## Mobile-relevant tables observed

The columns listed are the relevant fields observed in the running schema, not
a replacement for the complete DDL.

| Target logical owner | Observed table | Relevant observed columns | Runtime isolation | Mobile V1 relation |
| :--- | :--- | :--- | :--- | :--- |
| BC-01 — Tenant & Access Governance | `tenant_management.workspace` | `id`, `tenant_id`, `name`, `slug`, `status`, `version` | No RLS flag observed on this table | MOB-US-002 context resolution; server authority remains required |
| BC-01 — Tenant & Access Governance | `tenant_management.workspace_membership` | `id`, `workspace_id`, `user_id`, `membership_type`, `status`, `version` | No RLS flag observed on this table | MOB-US-002/003 membership and role scope |
| BC-03 — Catalog & Commercial Policy | `catalog_management.sellable_sku` | `id`, `tenant_id`, `workspace_id`, `sku_code`, `gtin`, `status`, `visible`, `version`, `variant_id` | No RLS flag observed on this table | MOB-US-011/012 identifier resolution and manual search |
| BC-05 — Inventory Availability | `warehouse.inventory_lot` | `id`, `tenant_id`, `workspace_id`, `warehouse_id`, `zone_id`, `catalog_item_id`, `batch_number`, `expiration_date`, `stock_quantity`, `reserved_quantity`, `status`, `temperature_value`, `sku_id` | `FORCE_RLS` observed | MOB-US-013..017 and stock/lot safety boundary |
| BC-05 — Inventory Availability | `warehouse.physical_allocation` | `id`, `tenant_id`, `workspace_id`, `sales_order_id`, `inventory_backing_id`, `fulfillment_id`, `status`, `version`, `actor_membership_id`, `idempotency_key`, `request_hash` | `FORCE_RLS` observed | MOB-US-016 picking/allocation; command is server-authorized |
| BC-05 — Inventory Availability | `warehouse.inventory_temperature_evaluation` | `id`, `tenant_id`, `workspace_id`, `lot_id`, `received_value`, `expected_min`, `expected_max`, `status`, `disposition`, `created_at`, `resolved_at` | `FORCE_RLS` observed | MOB-US-019 temperature hold/disposition support; evidence is not automatic authority |
| BC-06 — Fulfillment & Delivery | `logistics.fulfillment` | `id`, `tenant_id`, `workspace_id`, `sales_order_id`, `physical_allocation_id`, `status`, lifecycle timestamps, `version`, `actor_membership_id` | `FORCE_RLS` observed | MOB-US-016 and dispatch preparation projection |
| BC-06 — Fulfillment & Delivery | `logistics.dispatch_order` | `id`, `tenant_id`, `workspace_id`, `dispatch_number`, `sales_order_id`, `client_account_id`, `status`, destination snapshot, delivery window, responsible membership, temperature fields, `version` | `FORCE_RLS` observed | MOB-US-020..025 dispatch readiness, assignment and warehouse control |
| BC-06 — Fulfillment & Delivery | `logistics.delivery` | `id`, `tenant_id`, `workspace_id`, `fulfillment_id`, `dispatch_order_id`, `status`, destination snapshot, scheduled/dispatched/delivered timestamps, `version` | `FORCE_RLS` observed | MOB-US-026..034 delivery lifecycle |
| BC-06 — Fulfillment & Delivery | `logistics.delivery_attempt` | `id`, `tenant_id`, `workspace_id`, `delivery_id`, `attempt_number`, `status`, `failure_reason`, `notes`, `occurred_at`, `outcome`, `attempted_at` | `FORCE_RLS` observed | MOB-US-027/031/032 attempt and outcome facts |
| BC-06 + BC-11 target evidence boundary | `logistics.proof_of_delivery` | `id`, `tenant_id`, `workspace_id`, `dispatch_order_id`, `delivery_id`, `attempt_id`, receiver/evidence declarations, evidence object IDs, `status`, `sealed_at` | `FORCE_RLS` observed | MOB-US-033 proof lifecycle; proof remains unresolved until confirmed |
| BC-06 + BC-11 target evidence boundary | `logistics.temperature_evidence` | `id`, `tenant_id`, `workspace_id`, `delivery_id`, `lot_id`, `value`, `temperature_celsius`, `unit`, `recorded_at`, `source`, `evidence_metadata`, `status`, `evidence_object_id`, `actor_membership_id` | `FORCE_RLS` observed | MOB-US-019 evidence projection and delivery evidence support |
| BC-06 + BC-11 target evidence boundary | `logistics.delivery_handoff_token` | `id`, `tenant_id`, `workspace_id`, `delivery_id`, `delivery_attempt_id`, `customer_account_id`, `token_hash`, issue/expiry, issuer, `idempotency_key`, `request_hash`, `status` | `FORCE_RLS` observed | MOB-US-034/047 bounded handoff; token is not receipt |
| BC-06 + BC-11 target evidence boundary | `logistics.buyer_receipt_fact` | `id`, `tenant_id`, `workspace_id`, `delivery_id`, `delivery_attempt_id`, `customer_account_id`, `buyer_membership_id`, `handoff_token_id`, `decision`, delivered/accepted quantities, `reason`, `idempotency_key`, `request_hash` | `FORCE_RLS` observed | MOB-US-048 receipt and disputed quantity fact |
| BC-10 — Notifications | `notifications.push_subscription` | `id`, `tenant_id`, `workspace_id`, recipient membership, `user_id`, `surface`, `installation_id`, `platform`, token hash, `status`, `version` | `FORCE_RLS` observed | Technical notification foundation; does not prove Mobile push delivery |

`BC-06 + BC-11 target evidence boundary` is intentionally unresolved as a
database ownership decision. The schema proves relationships and constraints;
it does not by itself establish the canonical ownership of every fact.

## Constraint and integrity observations

Counts below come from `pg_constraint` in the local database. Unique indexes
that are not represented as table constraints are not included in the counts.

| Table | PK | FK | UNIQUE | CHECK | Notes from source/runtime |
| :--- | ---: | ---: | ---: | ---: | :--- |
| `catalog_management.sellable_sku` | 1 | 4 | 3 | 9 | Identifier lookup index added by `V97`; no dedicated identifier table was inferred |
| `warehouse.inventory_lot` | 1 | 2 | 2 | 3 | Status/lot scope constraints; `V77` adds temperature/disposition support |
| `warehouse.inventory_temperature_evaluation` | 1 | 2 | 0 | 2 | Lot and workspace composite references; `V77` declares lifecycle values |
| `warehouse.physical_allocation` | 1 | 2 | 4 | 5 | Idempotency, backing/fulfillment uniqueness and terminal-state checks |
| `logistics.fulfillment` | 1 | 1 | 2 | 2 | Allocation and status/version constraints |
| `logistics.dispatch_order` | 1 | 4 | 3 | 5 | Dispatch status and scoped references |
| `logistics.delivery` | 1 | 3 | 2 | 3 | Delivery lifecycle and scoped references |
| `logistics.delivery_attempt` | 1 | 1 | 3 | 4 | Attempt number, outcome and failure-reason checks; `V79` |
| `logistics.proof_of_delivery` | 1 | 2 | 2 | 2 | `V79` source declares insertion only for final delivery |
| `logistics.temperature_evidence` | 1 | 2 | 1 | 2 | Append-only evidence trigger observed at runtime |
| `logistics.delivery_handoff_token` | 1 | 5 | 2 | 5 | Hash/window/status checks, active-token index and binding hardening in `V93`/`V95`/`V96` |
| `logistics.buyer_receipt_fact` | 1 | 7 | 3 | 5 | Quantity, decision, dispute-reason and handoff binding checks in `V93`/`V95` |
| `notifications.push_subscription` | 1 | 3 | 2 | 6 | `V94`/`V95`/`V99`; source currently constrains `surface` to `PLATFORM`/`PORTAL` |

## Runtime trigger and RLS observations

The local schema query observed `FORCE_RLS` on the selected logistics,
warehouse-evidence and notification tables. It also observed policies using
the current tenant/workspace settings on delivery, proof, temperature,
handoff, receipt, allocation and notification records.

Append-only or lifecycle triggers observed include:

- `logistics_buyer_receipt_fact_append_only`;
- `logistics_delivery_attempt_append_only` and its line trigger;
- `logistics_delivery_handoff_token_lifecycle_v17`;
- `logistics_pod_lifecycle_v15` and `logistics_pod_only_final_delivery`;
- `logistics_temperature_evidence_append_only`;
- `warehouse_lot_disposition_append_only`;
- notification delivery-attempt append-only protection.

These are persistence observations only. The API/application authorization,
transaction boundary, retry behavior and Mobile UX still require separate
evidence.

## Reproducible inspection command

The following read-only command was executed while the local compose stack was
healthy:

```text
bash scripts/inspect-api-persistence.sh
```

The script queries PostgreSQL system catalogs for the database version,
relevant tables, columns, constraint counts, triggers and policies. It performs
no insert, update, delete or migration operation. Its connection defaults are
local-only and can be overridden with the task-specific
`NEXA_PERSISTENCE_CONTAINER`, `NEXA_PERSISTENCE_DB_USER` and
`NEXA_PERSISTENCE_DB_NAME` variables; no password is printed or stored.

## Academic closure

| Gate | State | Required next evidence |
| :--- | :--- | :--- |
| Source-backed schema inventory | Observed | Keep API SHA and migration references attached |
| Logical ownership by Bounded Context | Target / human review pending | Architecture/data owner confirms each table and cross-context reference |
| Database Design Diagram | Blueprint source/export observed; academic review open | Confirm logical ownership, import/render in the instructor-approved tool and record reviewer |
| Mobile persistence behavior | Open | Mobile client source, harmless draft/cache/retry policy and failure tests |
| Product Acceptance | Open | Story-level manual verification and accepted device flow |

See [tactical DDD coverage](../report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/2.6.1-bounded-context-coverage.md),
[rubric gap matrix](./rubric-gap-matrix.md) and
[Mobile V1 API contract register](./mobile-v1-api-contract-register.md).
