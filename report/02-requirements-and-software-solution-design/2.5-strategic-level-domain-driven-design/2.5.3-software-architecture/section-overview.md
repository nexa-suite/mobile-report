# 2.5.3 Software Architecture

La arquitectura estratégica se expresa con C4 y Structurizr. Nexa es un único
sistema B2B SaaS multi-tenant implementado como modular monolith; los Bounded
Contexts no se convierten automáticamente en containers, procesos o
deployments.

## Organización de la vista C4

| Vista | Propósito | Estado documentado |
| :--- | :--- | :--- |
| [2.5.3.1 Context](./2.5.3.1-context-level-diagrams.md) | Nexa, actores y sistemas externos abstractos | TARGET V1 y lectura AS-IS; no prueba runtime |
| [2.5.3.2 Container](./2.5.3.2-container-level-diagrams.md) | Superficies, API y stores que componen el sistema | AS-IS observado y V1 TARGET para clientes móviles |
| [Software Architecture Components Overview](./2.5.3.3-component-level-diagrams.md) | Componentes selectivos dentro de containers | Diseño objetivo; no inventario de clases |
| [2.5.3.3 Deployment](./2.5.3.4-deployment-diagrams.md) | Nodos, límites y relaciones de runtime | Topología TARGET; runtime debe probarse aparte |

El orden visible sigue el rubric oficial: Context, Container y Deployment. La
vista de componentes se conserva como un encabezado descriptivo sin numeración
artificial; el trabajo táctico detallado pertenece a la sección posterior
correspondiente.

## Decisiones de arquitectura

- El backend mantiene Java 25, Spring Boot 4.1.x y Spring Modulith dentro de un
  único modular monolith.
- PostgreSQL es físicamente compartido y tiene ownership lógico por contexto,
  con alcance explícito de Tenant/Workspace.
- Object Storage se accede detrás de ports/adapters; sus bytes no se mezclan
  con la autoridad transaccional de PostgreSQL.
- Website, Platform, Buyer Portal, Operations Mobile y Buyer Mobile son
  superficies/containers; no son Bounded Contexts.
- No se agrega Kafka, otro broker, una segunda base de datos, Kubernetes,
  microservicios ni transacciones distribuidas.

## AS-IS, TARGET y evidencia

Las vistas distinguen implementación observada, diseño V1 aceptado y runway.
Operations Mobile y Buyer Mobile son proyecciones V1 `TARGET / PLANNED /
PROPOSED`; su presencia en C4 no prueba framework, build, runtime, aceptación
de producto ni production readiness. Fuente semántica, hashes y exports están
en el [Chapter 2 provenance register](../../../assets/chapter-2/provenance.md).
