### 2.6.8. Bounded Context: Payments

BC-08 conserva hechos de pago independientes del proveedor, sus intentos y la
conciliación. Payment Reported y Payment Confirmed son estados diferentes.

#### 2.6.8.1. Canonical class dictionary

*Clases y responsabilidades de BC-08 por capa.*

| Layer | Class | Category | Purpose | Key Attributes / Inputs | Main Methods / Business Behavior | Relationships / Collaborators | Aggregate Owner / External References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Domain | Payment | Aggregate Root | Mantiene el estado autoritativo de un pago. | Payment ID, customer account ID, optional commitment ID, money, status. | Report, confirm and fail. | References BC-02 account and optional BC-04 commitment IDs. | Owns attempt, provider event, refund and correction facts. |
| Domain | PaymentReconciliationCase | Aggregate Root | Conserva una discrepancia entre estado local y proveedor. | Case ID, payment ID, reason, status. | Open and resolve. | References Payment by ID. | Independent lifecycle. |
| Domain | PaymentAttempt | Entity | Conserva el resultado de un intento. | Provider reference, status and result. | Record result. | Local to Payment. | Owned by Payment. |
| Domain | PaymentProviderEvent | Entity | Conserva un callback proveedor-neutral. | Provider, event ID, payload digest, time. | Record immutable fact. | Receives a translated event. | Owned by Payment; unique provider/event pair is enforced by infrastructure. |
| Domain | PaymentRefund | Entity | Conserva una reversión explícita. | Refund ID, money, reason. | Record refund. | Local to Payment. | Owned by Payment. |
| Domain | PaymentCorrection | Entity | Conserva una corrección explícita. | Correction ID, amount delta, reason. | Record correction. | Local to Payment. | Owned by Payment. |
| Domain | PaymentStatePolicy | Domain Policy | Decide transiciones válidas de pago. | Payment and provider result values. | Evaluate confirmation and refund conditions. | Pure values supplied by application. | No provider port, HTTP or storage dependency. |
| Domain | PaymentReconciliationPolicy | Domain Policy | Decide cuándo abrir un caso de conciliación. | Local status and provider result values. | Evaluate mismatch. | Pure values supplied by application. | No external I/O. |
| Interface | BC-08 Interface Boundary | Interface component | Traduce comandos, consultas y callbacks verificados. | Actor, idempotency key or signed callback. | Rejects untrusted or duplicate input. | Calls application orchestration. | Client cannot declare confirmation. |
| Application | BC-08 Application Orchestration | Application component | Coordina intentos, callback, conciliación y publicación de hechos. | Payment command or translated provider event. | Performs provider I/O outside long database transactions; fences finalization. | Uses BC-07 only through Payment ID facts. | Signature verification, inbox and provider adapter stay outside Domain. |
| Infrastructure | BC-08 Persistence and Provider Adapters | Infrastructure component | Persiste hechos y traduce proveedor externo. | Payment records, inbox records and provider messages. | Deduplicates provider/event ID and maps provider contracts. | PostgreSQL, inbox, outbox and provider ACL. | Never stores PAN, CVV or secrets. |

PaymentReconciliationCase no es un hijo de Payment. El borde de interfaz y la
aplicación verifican y deduplican callbacks; Domain recibe sólo valores y hechos
ya traducidos. Un Payment Confirmed puede ser aplicado luego por BC-07, pero no
se convierte en un Receivable.

#### 2.6.8.2. Component and code-level diagrams

*Vista C4 L3 de BC-08 Payments.*

![Vista C4 L3 de BC-08 Payments](../../../assets/chapter-2/c4/Nexa-API-BC-08-Payments.svg)

*Nota. Elaboración propia.*

*Modelo de dominio táctico de BC-08 Payments.*

![Modelo de dominio táctico de BC-08 Payments](../../../assets/chapter-2/tactical/BC-08/BC08_Payments.svg)

*Nota. Elaboración propia.*

*Diseño lógico de base de datos de BC-08 Payments.*

![Diseño lógico de base de datos de BC-08 Payments](../../../assets/chapter-2/tactical/BC-08/database-diagram.svg)

*Nota. Elaboración propia.*
