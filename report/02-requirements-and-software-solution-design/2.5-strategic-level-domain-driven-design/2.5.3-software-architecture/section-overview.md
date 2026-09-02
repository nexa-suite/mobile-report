# 2.5.3 Software Architecture

La arquitectura se documentará con C4 y se basará en las vistas canónicas de
`blueprint` y en la fuente semántica de Structurizr [T6]. Nexa es el sistema principal; Website, Platform, Buyer Portal,
API, PostgreSQL y Object Storage son los containers AS-IS/V1 aceptados.
Operations Mobile y Buyer Mobile se incorporan sólo en la vista V1 TARGET como
clientes planificados.

## Views and evidence boundary

| C4 view | Required content | State in this report |
| :--- | :--- | :--- |
| Context | Nexa, actor groups and abstract external systems | Blueprint source/export observed; workshop and report review pending |
| Container AS-IS | Website, Platform, Buyer Portal, API, PostgreSQL and Object Storage | Blueprint source/export observed; runtime proof pending |
| Container V1 TARGET | AS-IS containers plus Operations Mobile and Buyer Mobile | Blueprint target/export observed; no Mobile runtime claim |
| Component | Components inside a selected executable container | Blueprint source/export observed; selected report view and review pending |
| Deployment local | Nodes, services, network and storage for an executed local environment | Blueprint source/export observed; execution evidence pending |
| Deployment cloud | Provider, network, secrets, backup, rollback and observability | Open; no production claim |

The API baseline is a Java 25/Spring Boot 4.1 modular monolith with Spring
Modulith evidence in the shared source. This statement describes the candidate
backend source; it does not prove a Mobile client or an accepted API contract.
PostgreSQL remains physically shared with logical Bounded Context ownership.

The diagrams must distinguish the logical domain model, executable containers
and runtime nodes. Modules of code do not automatically become Bounded Contexts
or C4 containers. Every included image needs its source, revision, export date,
and human visual review. The observed provenance and fingerprints are recorded
in the [architecture and diagram evidence register](../../../../delivery-checklists/architecture-render-evidence-register.md).
