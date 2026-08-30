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
