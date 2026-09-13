### 2.6.9. Bounded Context: Business Documents

Este contexto posee la identidad de documentos emitidos, la numeración,
snapshots inmutables, la intención de generación y las referencias privadas de
Object Storage. No posee la autoridad de Sales, Payment, Delivery ni fiscal.

#### 2.6.9.1. Domain Layer

*Agregados y límites invariantes de BC-09.*
| Aggregate/raíz | Límite e invariante |
| :--- | :--- |
| `BusinessDocument` | Snapshot solicitado, emitido o reemplazado y metadatos de disponibilidad |
| `DocumentNumberSeries` | Asignación de numeración con alcance definido |
| `DocumentGenerationRequest` | Intención de generación reintentable con idempotencia y lease |
| `ObjectStorageReference` | Metadatos para bytes privados fuera de PostgreSQL |

`DocumentSnapshotLine`, `DocumentRevision` y `EvidenceReference` preservan el
historial inmutable. Los Value Objects incluyen `DocumentId`, `DocumentNumber`,
`DocumentType`, `IssuedSnapshot`, `StorageReference` y `ContentHash`.
`DocumentNumberingPolicy` y `DocumentIssuePolicy` validan los snapshots de
origen; `BusinessDocumentRepository` posee el estado del documento.

Invariantes de diseño: los documentos emitidos nunca se mutan; las correcciones
vinculan una revisión o reemplazo nuevo; Commercial Invoice no es
automáticamente un documento fiscal SUNAT; PostgreSQL almacena metadatos y
snapshots mientras Object Storage contiene bytes privados; la numeración y la
generación son idempotentes y las brechas de secuencia son explícitas.

#### 2.6.9.2. Interface Layer

La Interface Layer cubre la solicitud de documento, disponibilidad, metadatos y
descarga autorizados, y la referencia de evidencia. No se inventan rutas
exactas. La autorización se resuelve en la API; las superficies Portal y Mobile
planificada reciben proyecciones seguras y nunca acceden a URL públicas de
objetos por inferencia.

#### 2.6.9.3. Application Layer

La Application Layer solicita y emite documentos, reemplaza o corrige mediante
revisiones vinculadas, registra metadatos de evidencia y reintenta la generación
con leases/fencing. Los snapshots de origen se leen mediante contratos
explícitos; la emisión confirma metadatos e intención durable antes del trabajo
externo de renderizado o almacenamiento.

#### 2.6.9.4. Infrastructure Layer

La Infrastructure Layer organiza la propiedad lógica en PostgreSQL compartido
sobre `document_number_series`, `business_document`, `document_snapshot_line`,
`document_revision`, `object_storage_reference` y
`document_generation_request`. Los bytes de Object Storage usan un puerto de
Application. Los adaptadores externos de renderizador o escáner de documentos
son ACL; no se infiere un blob de base de datos ni integración fiscal.

*Clases TARGET por capa de BC-09.*

Los nombres siguientes concretan responsabilidades previstas; no implican endpoints, proveedores ni implementación ya disponible.

| Capa | Clase / componente TARGET | Responsabilidad |
|---|---|---|
| Interface | `BusinessDocumentController` | Recibe comandos y consultas de documentos sin exponer entidades de persistencia. |
| Interface | `DocumentGenerationConsumer` | Consume hechos publicados que justifican solicitar una generación documental. |
| Interface | `DocumentAvailabilityConsumer` | Publica al borde de interfaz la disponibilidad de un artefacto ya emitido. |
| Application | `RequestBusinessDocumentHandler` | Valida la solicitud idempotente y fija el snapshot de origen que será trazable. |
| Application | `IssueBusinessDocumentHandler` | Coordina emisión, versionado y publicación del hecho de documento emitido. |
| Application | `ReplaceBusinessDocumentHandler` | Gestiona una sustitución explícita sin reescribir la evidencia histórica. |
| Application | `RegisterEvidenceReferenceHandler` | Registra referencias de evidencia bajo las reglas de retención del contexto. |
| Application | `RetryDocumentGenerationHandler` | Reintenta una generación fallida con una clave de deduplicación estable. |
| Infrastructure | `BusinessDocumentRepositoryAdapter` | Persiste metadatos, versiones y referencias del documento. |
| Infrastructure | `DocumentRendererAdapter` | Adapta el renderizado técnico a un contrato de aplicación. |
| Infrastructure | `ObjectStorageAdapter` | Guarda el binario fuera del agregado y devuelve una referencia controlada. |
| Infrastructure | `DocumentGenerationWorker` | Ejecuta trabajo diferido después del commit, sin I/O externo en la transacción de solicitud. |
| Infrastructure | `DocumentOutboxAdapter` | Publica hechos comprometidos mediante outbox durable. |

#### 2.6.9.5. Bounded Context Software Architecture Component Level Diagrams

La vista C4 L3 **TARGET** muestra componentes conceptuales de este contexto dentro de Nexa API. No equivale a un Bounded Context adicional, una base de datos independiente ni una unidad de despliegue.

*Vista C4 L3 TARGET de BC-09 Business Documents.*

![BC-09 Business Documents — C4 L3 TARGET](../../../assets/chapter-2/c4/Nexa-API-BC-09-BusinessDocuments-TARGET-dark.svg)

*Nota.* Exportación vectorial desde una vista Structurizr DSL enfocada en BC-09 Business Documents, dentro del único contenedor Nexa API. Es evidencia de diseño TARGET; no acredita implementación, runtime ni una unidad de despliegue independiente.

#### 2.6.9.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.9.6.1. Bounded Context Domain Layer Class Diagrams

*Modelo de dominio táctico de BC-09 Business Documents.*
![BC-09 tactical domain model](../../../assets/chapter-2/tactical/BC-09/BC09_BusinessDocuments.png)
*Nota.* El diagrama se presenta como modelo de diseño, no como inventario de código.


##### 2.6.9.6.2. Bounded Context Database Design Diagram

*Proyección del diseño de base de datos de BC-09.*
![BC-09 database design projection](../../../assets/chapter-2/tactical/BC-09/database-diagram.png)

*Nota.* Es una proyección lógica de PostgreSQL compartido; los bytes permanecen en Object Storage bajo autorización y el SQL canónico define las restricciones.
