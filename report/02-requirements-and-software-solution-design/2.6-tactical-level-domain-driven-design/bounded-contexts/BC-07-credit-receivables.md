### 2.6.7. Bounded Context: Credit & Receivables

Este contexto posee la autoridad sobre la exposición crediticia, las reservas y
los Receivable. Payment es un contexto separado; Payment Confirmed no constituye
un Receivable.

#### 2.6.7.1. Domain Layer

*Agregados y límites invariantes de BC-07.*
| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `CreditAccount` | Limit, exposure and reservation policy for one Customer Account |
| `CreditReservation` | Active protection for one commercial source; released/converted once |
| `Receivable` | Posted obligation, balance and due state |
| `FinancialAdjustment` | Explicit correction with reason and actor |

`ReceivableApplication` pertenece a la autoridad financiera y referencia
Payment por ID. Los Value Objects incluyen `CreditAmount`, `AvailableCredit`,
`Terms` y `AdjustmentReason`; las políticas incluyen `CreditDecisionPolicy` y
`DoubleCountPreventionPolicy`. Los Repository poseen las raíces CreditAccount y
Receivable.

Invariante de diseño: Available Credit = Credit Limit − Active Credit Reservations
− Outstanding Receivable Balances. La compra a crédito reserva al enviar la PR;
el pedido directo reserva en la misma confirmación lógica; el Receivable de
crédito o neto se registra al confirmar la SO. Las aplicaciones no pueden
aplicar montos por encima del saldo ni duplicarlos; las correcciones preservan
los hechos originales. Buyer recibe proyecciones seguras, no la política interna
de riesgo.

#### 2.6.7.2. Interface Layer

La Interface Layer cubre la exposición crediticia, la reserva, el registro de
Receivable, la aplicación de Payment y el ajuste financiero explícito. No se
declaran rutas ni DTOs exactos cuando no existe evidencia de API. La autorización
por capacidad y el alcance Tenant se resuelven del lado del servidor; los datos
del proveedor externo de pagos ingresan mediante contratos de BC-08.

#### 2.6.7.3. Application Layer

La Application Layer evalúa y reserva crédito, registra Receivable, aplica o
revierte referencias de Payment y registra ajustes. Los límites de Application
coordinan BC-08 sin un Aggregate entre contextos. La idempotencia y la
concurrencia protegen el último crédito; los hechos confirmados alimentan
documentos, notificaciones y trazabilidad después del commit.

#### 2.6.7.4. Infrastructure Layer

La Infrastructure Layer organiza la propiedad lógica en PostgreSQL compartido
sobre `credit_account`, `credit_reservation`, `receivable`,
`receivable_application`, `financial_adjustment` y `financial_ledger_entry`.
Los identificadores de Payment y Sales Order son referencias sin propiedad. Los
predicados Tenant, las validaciones monetarias y las reglas de historial se
mantienen en SQL canónico; no se afirma una base de datos física por BC.

#### 2.6.7.5. Bounded Context Software Architecture Component Level Diagrams

Las siguientes clases son especificaciones **TARGET**. Preservan que Payment y
Receivable son autoridades distintas, y que la corrección financiera agrega un
hecho en vez de reescribir la obligación original.

*Clases TARGET por capa de BC-07*

| Capa | Clase | Tipo | Responsabilidad y límite de consistencia |
| --- | --- | --- | --- |
| Interface | `CreditExposureController` | Controller | Presenta exposición y decisiones permitidas sin revelar política interna a un Buyer. |
| Interface | `ReceivablesController` | Controller | Expone historial financiero autorizado, no la confirmación de un proveedor de pagos. |
| Interface | `CreditReservationPort` | Contract interface | Recibe la solicitud síncrona de BC-04; no es una ruta REST inventada. |
| Interface | `ReceivableProjectionConsumer` | Consumer | Proyecta información segura para Platform, Portal o Mobile. |
| Application | `EvaluateCreditHandler` | Application service | Calcula crédito disponible bajo bloqueo/CAS sobre cuenta y reservas activas. |
| Application | `EstablishCreditReservationHandler` | Command handler | Protege crédito en submit PR o confirmación Direct Order con idempotencia durable. |
| Application | `PostReceivableHandler` | Command handler | Publica obligación crédito/net en confirmación de Sales Order, no universalmente en entrega o factura. |
| Application | `ApplyPaymentToReceivableHandler` | Command handler | Consume un Payment confirmado por ID y evita sobreaplicar o duplicar la aplicación. |
| Application | `RecordFinancialAdjustmentHandler` | Command handler | Añade ajuste explícito, actor y razón conservando ledger e importe original. |
| Infrastructure | `CreditAccountRepositoryAdapter` | Repository implementation | Persiste cuenta y reserva con restricciones monetarias y alcance Tenant. |
| Infrastructure | `ReceivableRepositoryAdapter` | Repository implementation | Persiste obligación, aplicaciones y ledger sin poseer Payment. |
| Infrastructure | `PaymentFactPort` | Contract adapter | Consume el resultado proveedor-neutral de BC-08 por contrato explícito. |
| Infrastructure | `CreditOutboxAdapter` | Outbox adapter | Emite hechos de reserva y obligación sólo al finalizar la transacción. |

La vista C4 L3 **TARGET** muestra componentes conceptuales de este contexto dentro de Nexa API. No equivale a un Bounded Context adicional, una base de datos independiente ni una unidad de despliegue.

*Vista C4 L3 TARGET de BC-07 Credit & Receivables.*

![BC-07 Credit & Receivables — C4 L3 TARGET](../../../assets/chapter-2/c4/Nexa-API-BC-07-CreditReceivables-TARGET-dark.svg)

*Nota.* Exportación vectorial desde una vista Structurizr DSL enfocada en BC-07 Credit & Receivables, dentro del único contenedor Nexa API. Es evidencia de diseño TARGET; no acredita implementación, runtime ni una unidad de despliegue independiente.

#### 2.6.7.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.7.6.1. Bounded Context Domain Layer Class Diagrams

*Modelo de dominio táctico de BC-07 Credit & Receivables.*
![BC-07 tactical domain model](../../../assets/chapter-2/tactical/BC-07/BC07_CreditReceivables.png)
*Nota.* El diagrama se presenta como modelo de diseño, no como inventario de código.


##### 2.6.7.6.2. Bounded Context Database Design Diagram

*Proyección del diseño de base de datos de BC-07.*
![BC-07 database design projection](../../../assets/chapter-2/tactical/BC-07/database-diagram.png)

*Nota.* Es una proyección lógica de PostgreSQL compartido con restricciones y alcance Tenant; el SQL canónico mantiene la autoridad.
