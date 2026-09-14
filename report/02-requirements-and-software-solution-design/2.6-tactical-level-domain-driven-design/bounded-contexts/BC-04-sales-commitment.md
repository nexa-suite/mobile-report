### 2.6.4. Bounded Context: Sales Commitment

BC-04 conserva la intención comercial, el compromiso y la orden. Sus raíces
tienen ciclos de vida separados; una referencia entre ellas usa identidad.

#### 2.6.4.1. Canonical class dictionary

*Clases y responsabilidades de BC-04 por capa.*

| Layer | Class | Category | Purpose | Key Attributes / Inputs | Main Methods / Business Behavior | Relationships / Collaborators | Aggregate Owner / External References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Domain | RequestDraft | Aggregate Root | Mantiene intención editable antes de una solicitud. | Draft ID, buyer relationship ID, status. | Add lines and submit. | Uses SKU IDs. | Owns RequestDraftLine; BuyerRelationship is a BC-02 ID. |
| Domain | PurchaseRequest | Aggregate Root | Mantiene una solicitud enviada y su vencimiento. | Request ID, buyer relationship ID, expiry, status. | Submit, accept a material change or reject. | Supplies the optional origin of a commitment. | Owns PurchaseRequestLine and MaterialChangeProposal. |
| Domain | CommercialCommitment | Aggregate Root | Registra demanda comercial confirmable. | Commitment ID, origin, optional request ID, status. | Establish from request or direct order; cancel. | Consumes typed reservation and credit decisions. | Owns CommercialCommitmentLine and CommitmentAdjustment. |
| Domain | SalesOrder | Aggregate Root | Consolida el ciclo de vida de la orden. | Sales order ID, commitment ID, status. | Confirm or cancel. | References CommercialCommitment by ID. | Owns SalesOrderLine; no root composition. |
| Domain | CommercialSnapshot | Value Object | Conserva precio y términos aceptados en una línea. | SKU ID, money, TermsSnapshot. | Preserves a decision input. | Passed through the commercial flow. | Local immutable value. |
| Domain | CommitmentAcceptancePolicy | Domain Policy | Evalúa reglas puras para aceptar un compromiso. | InventoryReservationDecision, CreditReservationDecision. | Decide whether commitment is admissible. | Receives published values already loaded by application. | No repository, provider or cross-context object ownership. |
| Interface | BC-04 Interface Boundary | Interface component | Traduce comandos y consultas comerciales autorizadas. | Actor, scope, version and idempotency key. | Rejects invalid or stale input. | Calls application orchestration. | Does not reserve stock directly. |
| Application | BC-04 Application Orchestration | Application component | Coordina la transición comercial y los contratos requeridos. | Request or direct-order command; typed decisions. | Preserves idempotency and origin semantics. | Uses BC-05 and BC-07 contracts by typed IDs. | Does not load their aggregates. |
| Infrastructure | BC-04 Persistence Adapter | Infrastructure component | Persiste raíces, líneas y snapshots propios. | Commercial records. | Maps local aggregates. | PostgreSQL and local outbox. | Does not own inventory or credit tables. |

El origen PURCHASE_REQUEST exige PurchaseRequestId. DIRECT_ORDER no contiene
Purchase Request. La aplicación coordina las decisiones de inventario y crédito
por contratos explícitos; la transición a SalesOrder mantiene referencias de
identidad y no libera ni crea una reserva duplicada.

#### 2.6.4.2. Component and code-level diagrams

*Vista C4 L3 de BC-04 Sales Commitment.*

![Vista C4 L3 de BC-04 Sales Commitment](../../../assets/chapter-2/c4/Nexa-API-BC-04-SalesCommitment.svg)

*Nota. Elaboración propia.*

*Modelo de dominio táctico de BC-04 Sales Commitment.*

![Modelo de dominio táctico de BC-04 Sales Commitment](../../../assets/chapter-2/tactical/BC-04/BC04_SalesCommitment.svg)

*Nota. Elaboración propia.*

*Diseño lógico de base de datos de BC-04 Sales Commitment.*

![Diseño lógico de base de datos de BC-04 Sales Commitment](../../../assets/chapter-2/tactical/BC-04/database-diagram.svg)

*Nota. Elaboración propia.*
