### 2.6.8. Bounded Context: Payments

This context owns provider-neutral Payment facts, attempts, callbacks, refunds,
corrections and reconciliation. Payment Reported is not Payment Confirmed.

#### 2.6.8.1. Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `Payment` | Intent/report/confirmation lifecycle and immutable monetary facts |
| `PaymentProviderEvent` | Verified callback identity and preserved payload metadata |
| `PaymentReconciliationCase` | Provider success/local failure or uncertain outcome |

`PaymentAttempt`, `PaymentRefund` and `PaymentCorrection` are Payment-owned
facts. Value objects include `PaymentId`, `ProviderReference`, `Money` and
`PaymentStatus`; policies include provider callback verification and payment
reconciliation. Payment application to Receivable is an explicit BC-07 port.

Invariantes de diseño: PREPAID needs Payment Confirmed before SO confirmation and
physical fulfillment; IMMEDIATE may confirm SO first and becomes due. Webhooks
are at-least-once and dedupe `(provider, eventId)`; provider success/local SO
failure becomes `UNALLOCATED / RECONCILIATION_REQUIRED`; payment history is
immutable and refund/correction is explicit. PAN, CVV and secrets are never
stored.

#### 2.6.8.2. Interface Layer

La Interface Layer cubre payment intent/report/status, provider callback,
refund/correction and reconciliation. Exact routes not verified in API are not
invented. The webhook edge verifies provider signatures and deduplication;
clients consume server status and cannot declare confirmation.

#### 2.6.8.3. Application Layer

La Application Layer inicia trabajo con proveedor, acepta callbacks, confirma o
reconcilia, solicita reembolsos y expone estado seguro. External I/O occurs outside long DB
transactions; local intent/attempt state is fenced and idempotent. BC-07
application coordination references Receivable by ID.

#### 2.6.8.4. Infrastructure Layer

La Infrastructure Layer organiza la propiedad lógica en PostgreSQL compartido sobre `payment`, `payment_attempt`,
`payment_provider_event`, `payment_refund`, `payment_correction` and
`payment_reconciliation_case`. Provider payload metadata is immutable and
secret-free. Stripe/provider adapters are ACLs; physical PostgreSQL remains
shared and no payment microservice is inferred.

#### 2.6.8.5. Bounded Context Software Architecture Component Level Diagrams

La vista C4 L3 **TARGET** muestra componentes conceptuales de este contexto dentro de Nexa API. No equivale a un Bounded Context adicional, una base de datos independiente ni una unidad de despliegue.

![BC-08 Payments — C4 L3 TARGET](../../../assets/chapter-2/c4/bc-08-payments-component.png)

#### 2.6.8.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.8.6.1. Bounded Context Domain Layer Class Diagrams

![BC-08 tactical domain model](../../../assets/chapter-2/tactical/BC-08/BC08_Payments.png)


##### 2.6.8.6.2. Bounded Context Database Design Diagram

![BC-08 database design projection](../../../assets/chapter-2/tactical/BC-08/database-diagram.png)

The drawing is a logical shared-PostgreSQL projection; keys and
provider-event dedupe remain defined by canonical SQL.
