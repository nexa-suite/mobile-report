# 2.5.1 EventStorming

El equipo utilizó EventStorming colaborativo en Miro para pasar de hechos
observables del dominio a una lectura estratégica de responsabilidades. La
secuencia conserva la división académica:

- 2.3.5 presenta Big Picture EventStorming con Step 1 — Unstructured
  Exploration, Step 2 — Timelines y Step 3 — Pain Points.
- Esta sección continúa con Step 4 — Pivotal Points, Step 5 — Commands, Step 6
  — Policies, Step 7 — Read Models, Step 9 — Aggregates y Step 10 — Bounded
  Contexts.

La secuencia colaborativa salta directamente de Step 7 a Step 9. Se conserva la
numeración real del tablero, sin reconstruir una etapa adicional.

## Lectura estratégica del modelado

Las capturas muestran cómo cada capa agrega una pregunta distinta:

| Etapa | Pregunta que responde | Resultado estratégico |
| :--- | :--- | :--- |
| Step 4 — Pivotal Points | ¿Dónde cambia autoridad, responsabilidad o consistencia? | Se aíslan decisiones comerciales, protección física, entrega, pago y corrección. |
| Step 5 — Commands | ¿Qué intención de un actor solicita una decisión? | Se separan actor, intención, comando, decisión autoritativa y hecho resultante. |
| Step 6 — Policies | ¿Qué reacción de negocio sigue a un hecho? | Se distinguen invariantes síncronas de propagación posterior a hechos confirmados. |
| Step 7 — Read Models | ¿Qué información necesita cada actor para decidir? | Se separan proyecciones de lectura de la autoridad de los contextos fuente. |
| Step 9 — Aggregates | ¿Qué debe ser consistente dentro de un modelo? | Se ubican límites de consistencia internos sin confundirlos con Bounded Contexts. |
| Step 10 — Bounded Contexts | ¿Qué lenguaje, reglas y autoridad deben permanecer juntos? | Se consolidan los once límites estratégicos aceptados por Nexa. |

## EventStorming — Step 4: Pivotal Points

![EventStorming — Step 4: Pivotal Points](../../../assets/chapter-2/ddd-process/step4-ddd.png)

El equipo proyectó sobre las timelines los puntos donde cambia autoridad,
responsabilidad, consistencia o lifecycle. El tablero destaca decisiones de
compromiso y aceptación de cambios materiales, protección de inventario,
continuidad de obligaciones, reconciliación de pagos y evidencia de entrega.

**Cambio respecto al Step 3.** Los pain points se transformaron en puntos
observables de decisión. Sirven para buscar límites de modelo y no para
nombrar contextos por conveniencia técnica.

## EventStorming — Step 5: Commands

![EventStorming — Step 5: Commands](../../../assets/chapter-2/ddd-process/step5-ddd.png)

El tablero relaciona actor, intención, command, decisión y Domain Event:
Customer Buyer y Sales Representative expresan intención comercial; Warehouse
Operator prepara trabajo físico; Dispatch Coordinator y Driver ejecutan
handoff y delivery; Payment Provider informa resultados externos. Command no es
endpoint y Command no es Domain Event. El command solicita una decisión; el
evento registra un hecho confirmado.

**Cambio respecto al Step 4.** Los puntos pivote se hicieron operables al
identificar quién solicita la decisión y qué autoridad confirma el resultado.

## EventStorming — Step 6: Policies

![EventStorming — Step 6: Policies](../../../assets/chapter-2/ddd-process/step6-ddd.png)

Las policies visibles conectan hechos con reacciones: submit de PR protege
compromiso, inventario y crédito aplicable; una entrega parcial conserva el
restante y crea continuidad; SalesOrderConfirmed planifica fulfillment;
DeliveryCompleted solicita documento; PaymentConfirmed aplica pago de forma
idempotente; NotificationDeliveryFailed permite retry sin mutar la fuente.

**Cambio respecto al Step 5.** El board hace explícita la regla posterior a
cada hecho. Los invariantes fuertes pueden ser síncronos y atómicos; la
propagación durable de hechos confirmados puede ser asíncrona mediante
outbox/inbox y entrega at-least-once. Esto no convierte Nexa en una arquitectura
de microservicios ni hace asíncrona una consistencia que debe ser atómica.

## EventStorming — Step 7: Read Models

![EventStorming — Step 7: Read Models](../../../assets/chapter-2/ddd-process/step7-ddd.png)

El tablero identifica información que actores necesitan para decidir: Purchase
Request, Resolved Offer Snapshot, Warehouse Stock/Batch Availability,
Fulfillment Queue, Delivery Timeline, Delivery Manifest, Payments, Ledger
Balances, Documents Registry y Authorized Timeline.

**Cambio respecto al Step 6.** Las policies se complementan con vistas de
lectura para compradores, ventas, warehouse, dispatch y operaciones. Read Model
no es autoridad de negocio, no es Bounded Context y no es una tabla.

## EventStorming — Step 9: Aggregates

![EventStorming — Step 9: Aggregates](../../../assets/chapter-2/ddd-process/step9-ddd.png)

El tablero propone etiquetas de consistencia como Tenant Governance Policy,
Buyer Account, Commercial Catalog, SalesOrder, Inventory Allocation,
Fulfillment Execution, Receivable Account, Payment Transaction, Document
Registry, Notification Dispatch y Audit Log.

**Cambio respecto al Step 7.** Las read models se relacionan con límites de
consistencia internos. Aggregate no es Bounded Context, tabla, Spring module ni
C4 Container. `Audit Log` se interpreta como terminología técnica distinta de
BC-11 Business Traceability; la nomenclatura canónica se conserva en el texto,
sin editar el asset histórico.

## EventStorming — Step 10: Bounded Contexts

![EventStorming — Step 10: Bounded Contexts](../../../assets/chapter-2/ddd-process/step10-ddd.png)

El agrupamiento final del tablero converge en los once Bounded Contexts
aceptados: Tenant & Access Governance, Customer & Buyer Relationships, Catalog
& Commercial Policy, Sales Commitment, Inventory Availability, Fulfillment &
Delivery, Credit & Receivables, Payments, Business Documents, Notifications y
Business Traceability.

**Cambio respecto al Step 9.** Las etiquetas de aggregate y sus límites de
consistencia se consolidan en modelos estratégicos con lenguaje y autoridad
propios. Mobile, Driver, Scanner, QR, Maps, Tracking y Push siguen siendo
superficies, capacidades o integraciones; no son Bounded Contexts.

Los nombres de eventos y commands mantienen lenguaje de dominio. No representan
automáticamente endpoints, clases Java, tablas ni eventos publicados. Las
relaciones, contratos y consistencia se desarrollan en las secciones siguientes.
