# 2.6 Tactical-Level Domain-Driven Design

Esta sección se organizará por los Bounded Contexts aceptados en `blueprint`. La aplicación móvil no tendrá una carpeta propia de DDD táctico porque Operations Mobile y Buyer Mobile son proyecciones de los contextos compartidos.

| Código | Bounded Context |
|---|---|
| BC-01 | Tenant & Access Governance |
| BC-02 | Customer & Buyer Relationships |
| BC-03 | Catalog & Commercial Policy |
| BC-04 | Sales Commitment |
| BC-05 | Inventory Availability |
| BC-06 | Fulfillment & Delivery |
| BC-07 | Credit & Receivables |
| BC-08 | Payments |
| BC-09 | Business Documents |
| BC-10 | Notifications |
| BC-11 | Business Traceability |

La plantilla incluida sirve para documentar cada contexto cuando existan clases, componentes y persistencia respaldados por la implementación o por un diseño objetivo aprobado. No se trasladan automáticamente los siete contextos del proyecto Web.

## Paquete táctico requerido por cada BC

Cada contexto debe documentarse con el mismo contrato de lectura para que el
revisor pueda separar diseño objetivo, evidencia AS-IS y comportamiento Mobile:

| Subsección | Contenido mínimo | Estado del corte |
| :--- | :--- | :--- |
| Domain Layer | Entities, Value Objects, Aggregates, Factories/Domain Services y Repository interfaces; invariantes | `TARGET / REVIEW_PENDING` |
| Application Layer | Capabilities, Command Handlers, Event Handlers, transacciones e idempotencia | `TARGET / REVIEW_PENDING` |
| Interface Layer | Controllers, Consumers, DTO/contract boundary, autorización y errores | `TARGET / REVIEW_PENDING` |
| Infrastructure Layer | Repositories, persistencia, mensajería y adapters externos | `TARGET / REVIEW_PENDING` |
| Component Diagram | Componentes dentro de los containers participantes y sus interacciones | `TARGET / RENDER_REVIEW_PENDING` |
| Domain Class Diagram | Clases, interfaces, enums, atributos, métodos, visibilidad, relaciones y multiplicidad | `TARGET / RENDER_REVIEW_PENDING` |
| Database Diagram | Tablas, columnas, PK/FK/UNIQUE/CHECK, ownership lógico e inmutabilidad | `TARGET / RENDER_REVIEW_PENDING` |

La matriz de [cobertura táctica](./2.6.1-bounded-context-coverage.md) enlaza
cada BC con los artefactos canónicos observados en Blueprint. El paquete de
[diagramas de clases](./bounded-context-template/code-level-diagrams/2.6.x.6.1-domain-layer-class-diagrams.md)
y el paquete de [diagramas de base de datos](./bounded-context-template/code-level-diagrams/2.6.x.6.2-database-design-diagrams.md)
preparan una revisión detallada de BC-06 y un inventario de BC-01..BC-11.
La existencia de una fuente, export o plantilla no demuestra que el equipo
haya realizado la sesión, importado el diagrama en la herramienta académica o
implementado el modelo.
