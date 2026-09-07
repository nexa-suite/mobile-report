# 2.4 Requirements Specification

Esta sección presenta la especificación académica de Nexa Mobile. Organiza los
escenarios objetivo, las historias de usuario, el mapeo de impactos y el Product
Backlog sin confundir requisitos con una implementación concreta.

El catálogo funcional conserva 73 historias `MOB-US-001` a `MOB-US-073`.
Nexa Operations Mobile reúne operaciones de negocio, ventas de campo, almacén,
despacho y entrega. Nexa Buyer Mobile busca paridad de capacidades de negocio
con las funciones aceptadas para compradores, además de capacidades móviles específicas.
La especificación permanece neutral respecto de Android Native/Kotlin,
Flutter/Dart e iOS Native/SwiftUI.

## Organización de 2.4

- [To-Be Scenario Mapping](./to-be-scenario-mapping.md)
- [2.4.1 User Stories](./2.4.1-user-stories.md)
- [Landing Functional Stories](./2.4.1-landing-stories.md)
- [Technical Stories](./2.4.1-technical-stories.md)
- [Spike Stories](./2.4.1-spike-stories.md)
- [2.4.2 Impact Mapping](./2.4.2-impact-mapping.md)
- [2.4.3 Product Backlog](./2.4.3-product-backlog.md)

La subsección 2.4.1 reúne historias funcionales, técnicas y de investigación
relacionadas con la especificación. Annex D conserva el detalle ampliado de los
seis Spike Stories. Los tres apartados oficiales mantienen su jerarquía:
2.4.1 User Stories, 2.4.2 Impact Mapping y 2.4.3 Product Backlog.

El Product Backlog ordena las historias por valor de negocio y distribuye el
trabajo académico en S1, S2, S3, S4 y Future. El orden de Sprint es planificado;
no representa un Sprint Backlog ni afirma ejecución.

La captura asistida de un Direct Order por un Representante de Ventas autorizado
se permite cuando la política del Tenant es `DIRECT_ORDER`. El flujo conserva la
separación entre Comprador y Ventas, distingue sus borradores y exige
revalidación del servidor.
