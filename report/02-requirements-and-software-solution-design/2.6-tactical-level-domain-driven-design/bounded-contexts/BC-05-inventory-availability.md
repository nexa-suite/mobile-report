### 2.6.5. Bounded Context: Inventory Availability

BC-05 conserva stock físico, disponibilidad vendible y protección de demanda.
Reservation, Backing y Allocation son decisiones diferentes y no se sustituyen.

#### 2.6.5.1. Canonical class dictionary

*Clases y responsabilidades de BC-05 por capa.*

| Layer | Class | Category | Purpose | Key Attributes / Inputs | Main Methods / Business Behavior | Relationships / Collaborators | Aggregate Owner / External References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Domain | Warehouse | Aggregate Root | Define una ubicación operativa disponible. | Warehouse ID, tenant ID, code, status. | Open and close. | Is referenced by position, lot, backing and transfer IDs. | Owns SafetyStockPolicy. |
| Domain | InventoryPosition | Aggregate Root | Protege la disponibilidad por SKU y Warehouse. | Position ID, usable on-hand, active reservation quantity, version. | Apply movement, protect and release demand. | Uses Warehouse and SKU IDs. | Owns immutable InventoryMovement records. |
| Domain | InventoryLot | Aggregate Root | Conserva cantidad y estado físico de un lote. | Lot ID, warehouse ID, SKU ID, expiry, on-hand quantity. | Receive, hold and release hold. | Is selected later by allocation. | Owns LotDisposition. |
| Domain | InventoryReservation | Aggregate Root | Protege demanda de CommercialCommitment sin elegir lotes. | Reservation ID, commitment ID, status. | Protect and release. | References BC-04 commitment by ID. | Owns ReservationLine. |
| Domain | WarehouseBacking | Aggregate Root | Distribuye una reserva entre Warehouse elegibles. | Backing ID, reservation ID, status. | Distribute and release. | References InventoryReservation by ID. | Owns WarehouseBackingLine. |
| Domain | PhysicalAllocation | Aggregate Root | Selecciona lotes para un Fulfillment. | Allocation ID, backing ID, fulfillment ID, status. | Allocate FEFO and release. | References backing, lot and BC-06 fulfillment IDs. | Owns PhysicalAllocationLine. |
| Domain | WarehouseTransfer | Aggregate Root | Mantiene un traslado físico explícito. | Transfer ID, source and destination Warehouse IDs, status. | Request, dispatch and receive. | References Warehouse IDs. | Owns WarehouseTransferLine. |
| Domain | SellableAvailabilityPolicy | Domain Policy | Calcula disponibilidad vendible. | Usable on-hand, active reservations, safety stock. | Calculates usable on-hand minus reservations and safety stock. | Pure calculation over loaded values. | Backing does not produce a second subtraction. |
| Domain | FEFOAllocationPolicy | Domain Policy | Ordena lotes vendibles por vencimiento. | Eligible lots and required quantity. | Selects lots without crossing unavailable states. | Uses local lot data only. | No Fulfillment object ownership. |
| Interface | BC-05 Interface Boundary | Interface component | Traduce operaciones de stock y consulta autorizada. | Actor, tenant scope, version and command. | Rejects ambiguous scope or stale input. | Calls application orchestration. | Does not accept client scans as authoritative stock. |
| Application | BC-05 Application Orchestration | Application component | Coordina reserva, backing, allocation y transferencia. | Commercial or fulfillment contract, stock command. | Uses locks, conditional updates and idempotency. | Exchanges typed IDs with BC-04 and BC-06. | Does not mutate their tables. |
| Infrastructure | BC-05 Persistence Adapter | Infrastructure component | Persiste inventario y hechos inmutables. | Warehouse, position, lot and decision records. | Maps roots and local entities. | PostgreSQL, tenant-scoped transaction and local outbox. | No external domain ownership. |

Sellable Availability = usable on-hand − active Inventory Reservations − Safety
Stock. InventoryPosition mantiene el saldo de disponibilidad reconciliado desde
movimientos inmutables; InventoryLot conserva el hecho físico del lote. HOLD,
QUARANTINE, DAMAGED, WASTE, EXPIRED e IN_TRANSIT quedan fuera de la selección
vendible. WarehouseBacking sólo distribuye una Reservation y no vuelve a
descontarla.

#### 2.6.5.2. Component and code-level diagrams

*Vista C4 L3 de BC-05 Inventory Availability.*

![Vista C4 L3 de BC-05 Inventory Availability](../../../assets/chapter-2/c4/Nexa-API-BC-05-InventoryAvailability.svg)

*Nota. Elaboración propia.*

*Modelo de dominio táctico de BC-05 Inventory Availability.*

![Modelo de dominio táctico de BC-05 Inventory Availability](../../../assets/chapter-2/tactical/BC-05/BC05_InventoryAvailability.svg)

*Nota. Elaboración propia.*

*Diseño lógico de base de datos de BC-05 Inventory Availability.*

![Diseño lógico de base de datos de BC-05 Inventory Availability](../../../assets/chapter-2/tactical/BC-05/database-diagram.svg)

*Nota. Elaboración propia.*
