# 2.6.6. BC-05 — Inventory Availability

`DOMAIN MODEL: TARGET / ACCEPTED`
`IMPLEMENTATION CROSSWALK: AS-IS VERIFIED / PARTIAL`

Canonical target: Blueprint `01-shared/domain/bounded-contexts/BC-05-inventory-availability/`.
This Core Domain context owns physical stock truth, sellable availability,
lot/expiry/disposition, inventory backing and Physical Allocation. Safety Stock
is a policy, not a reservation.

## 2.6.6.1 Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `InventoryPosition` | SKU + Warehouse quantity authority and sellable inputs |
| `InventoryLot` | Lot, expiry, disposition and physical quantity |
| `InventoryBacking` | Protects Commercial Commitment demand across eligible warehouses |
| `PhysicalAllocation` | Selects lot quantities for a Fulfillment contract |
| `WarehouseTransfer` | Explicit `REQUESTED -> IN_TRANSIT -> RECEIVED` movement |

`Warehouse`, `SafetyStockPolicy`, `InventoryMovement`, `LotDisposition`,
`PhysicalAllocationLine` and adjustment/count facts support the roots. Value
objects include `SkuId`, `WarehouseId`, `LotId`, `Quantity`, `ExpiryDate` and
`Disposition`; policies include `SellableAvailabilityPolicy` and
`FEFOAllocationPolicy`. Movement/adjustment facts are append-only.

Target invariant: Sellable Availability = usable on-hand − active Commercial
Commitments − Safety Stock, with backing counted once. HOLD, QUARANTINE,
DAMAGED/WASTE, EXPIRED and IN_TRANSIT are not sellable. Allocation cannot
exceed committed/backed or usable lot quantity. Scarce inventory uses
conditional updates, locks and version/CAS; no last-write-wins.

## 2.6.6.2 Interface Layer

Target contracts cover warehouse/lot receipt, availability, backing,
allocation, transfer, adjustment and picking inputs. URI/DTO names not present
in verified API evidence remain open. Any Mobile command is submitted to the
server; local scans/evidence cannot authorize allocation or mutate stock.

## 2.6.6.3 Application Layer

Target handlers coordinate availability decisions, commitment backing, FEFO
allocation and transfer transitions. They enforce Tenant scope, deterministic
warehouse selection and idempotent movement commands. Fulfillment receives
stable allocation IDs; it does not write inventory tables directly.

## 2.6.6.4 Infrastructure Layer

Target shared PostgreSQL ownership covers `warehouse`, `safety_stock_policy`,
`inventory_lot`, `inventory_position`, `inventory_movement`, `lot_disposition`,
`inventory_backing`, `inventory_backing_line`, `physical_allocation`,
`physical_allocation_line`, `warehouse_transfer`, `warehouse_transfer_line`
and `inventory_adjustment`. Tenant predicates and constraints stay in canonical
SQL. No physical database per BC is implied.

AS-IS anchor: API `inventoryavailability` domain/application/persistence and
warehouse/inventory migrations V15, V17, V38, V49 and V57. Warehouse,
reservation and availability code is `AS-IS VERIFIED`; full target backing,
allocation and no-double-count semantics are `PARTIAL`; Mobile runtime and
Product Acceptance are `NOT EVIDENCED`.

## 2.6.6.5 Bounded Context Software Architecture Component Level Diagrams

The API component family is `Nexa-API-CommercialInventory-TARGET`. It shows
logical commercial/inventory components inside the single Nexa API container;
it does not establish a separate Inventory container.

![BC-05 component family — TARGET](../../../assets/chapter-2/c4/Nexa-API-CommercialInventory-TARGET.png)

See [provenance](../../../assets/chapter-2/provenance.md) for Structurizr
source, export and hash.

## 2.6.6.6 Bounded Context Software Architecture Code Level Diagrams

### 2.6.6.6.1 Bounded Context Domain Layer Class Diagrams

![BC-05 tactical domain model — TARGET](../../../assets/chapter-2/tactical/BC-05/BC05_InventoryAvailability.png)

Source: [domain-model.puml](../../../assets/chapter-2/tactical/BC-05/domain-model.puml).

### 2.6.6.6.2 Bounded Context Database Design Diagram

![BC-05 target database projection](../../../assets/chapter-2/tactical/BC-05/database-diagram.png)

Source: [database-diagram.puml](../../../assets/chapter-2/tactical/BC-05/database-diagram.puml).
It is a logical shared-PostgreSQL projection; canonical SQL remains the
authority for PK/FK/unique/check and RLS/tenant-scope details.

## Crosswalk and open evidence

| Concern | Classification | Evidence boundary |
| :--- | :--- | :--- |
| Warehouse/inventory/reservation implementation | `AS-IS VERIFIED` | API `inventoryavailability` and migrations at `origin/main` |
| Availability, backing and Physical Allocation target | `TARGET / ACCEPTED` | Blueprint tactical model/data model |
| Complete concurrency and double-count closure | `PARTIAL` | Target rules not upgraded from diagram presence |
| Mobile capture, runtime and Product Acceptance | `NOT EVIDENCED` | Mobile is a planned projection |
