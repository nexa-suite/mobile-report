### 2.6.6. Bounded Context: Fulfillment & Delivery

This Core Domain context owns execution plans, dispatch handoff, delivery
attempts, quantity outcomes, receipt and delivery evidence. Driver outcome,
Buyer receipt, Proof of Delivery and Business Traceability remain separate
facts.

#### 2.6.6.1. Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `Fulfillment` | Sales Order execution plan and picking/packing progression |
| `Delivery` | Delivery obligation, assignment, attempts and remaining quantity |
| `ProofOfDelivery` | Immutable delivery evidence; corrections are addenda |
| `TemperatureEvidence` | Manual reading/evidence and excursion decision input |

`FulfillmentLine`, `PickingResult`, `PickingDiscrepancy`, `DeliveryAssignment`,
`DeliveryAttempt`, `DeliveryQuantityOutcome`, `DeliveryHandoffToken`,
`BuyerReceiptFact`, `ProofOfDeliveryAddendum`, `TemperatureExcursion` and
`ContinuationDelivery` are entities/facts with bounded lifecycles. Value
objects include `DeliveryId`, `HandoffId`, `AttemptId`, `EvidenceRef`,
`GeoPoint` and `DeliveryQuantity`; policies include `PartialDeliveryPolicy`
and `DeliveryLocationPrivacyPolicy`.

Invariantes de diseño: allocation authority stays BC-05; failed attempts remain
under one Delivery; partial delivery records actual delivered/rejected truth
and creates one continuation for remaining obligation; POD is immutable and
corrected by addendum; temperature evidence is manual in the initial scope and excursion places
affected quantity on HOLD pending explicit disposition.

#### 2.6.6.2. Interface Layer

La Interface Layer cubre fulfillment planning, picking result, dispatch handoff,
assignment, delivery attempt, outcome, buyer receipt, POD and temperature
evidence. Exact URI/DTO names are not invented. The server authorizes every
critical transition; Operations Mobile and Buyer Mobile are planned projections.

#### 2.6.6.3. Application Layer

La Application Layer coordina inicio, finalización o cancelación del fulfillment,
emisión y resolución de handoff, asignación e intento de entrega, continuidad
parcial, recepción y registro de evidencia. Idempotency, tenant scope, immutable evidence metadata
and conflict outcomes are explicit. Durable outbox/inbox supports downstream
notifications and traceability after commit.

#### 2.6.6.4. Infrastructure Layer

La Infrastructure Layer organiza la propiedad lógica en PostgreSQL compartido sobre `fulfillment`, `fulfillment_line`,
`picking_result`, `picking_discrepancy`, `delivery`, `delivery_assignment`,
`delivery_attempt`, `delivery_attempt_line`, `delivery_quantity_outcome`,
`delivery_handoff_token`, `buyer_receipt_fact`, `proof_of_delivery`,
`proof_of_delivery_addendum`, `temperature_evidence`,
`temperature_excursion` and `continuation_delivery`. `sales_order_id`,
`physical_allocation_id` and SKU/operator IDs are non-owning cross-BC refs.
Object bytes use BC-09/Object Storage ports; no public URL is inferred.

#### 2.6.6.5. Bounded Context Software Architecture Component Level Diagrams

La familia de componentes de Nexa API representa la colaboración lógica
mostrada dentro de una API compartida. No equivale a un Bounded Context
adicional, una base de datos independiente ni una unidad de despliegue.

![BC-06 component family](../../../assets/chapter-2/c4/Nexa-API-FulfillmentDelivery-TARGET.png)

#### 2.6.6.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.6.6.1. Bounded Context Domain Layer Class Diagrams

![BC-06 tactical domain model](../../../assets/chapter-2/tactical/BC-06/BC06_FulfillmentDelivery.png)

Source: [domain-model.puml](../../../assets/chapter-2/tactical/BC-06/domain-model.puml).

##### 2.6.6.6.2. Bounded Context Database Design Diagram

![BC-06 database design projection](../../../assets/chapter-2/tactical/BC-06/database-diagram.png)

Source: [database-diagram.puml](../../../assets/chapter-2/tactical/BC-06/database-diagram.puml).
Logical ownership is in shared PostgreSQL; canonical SQL defines constraints,
tenant scope and evidence references.
