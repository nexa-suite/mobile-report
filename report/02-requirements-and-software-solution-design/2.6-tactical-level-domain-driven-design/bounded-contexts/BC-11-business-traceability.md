### 2.6.11. Bounded Context: Business Traceability

BC-11 conserva una línea append-only de hechos de negocio y referencias de
evidencia. Contextos emisores conservan autoridad de sus propios aggregates;
BC-11 no reconstituye ni muta modelos fuente.

#### 2.6.11.1. Domain Layer

El dominio modela sólo facts ya traducidos a valores semánticos. Inbox, outbox,
envelope de transporte y deduplicación técnica quedan fuera de Domain.

| Clase | Categoría | Propósito | Atributos / inputs clave | Operaciones principales | Relaciones / ownership |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `BusinessTraceabilityRecord` | Aggregate Root | Conservar fact consultable append-only. | `TraceabilityId`, `TenantId`, `BusinessObjectReference`, `ActorReference`, `CorrelationId`, time, metadata segura. | `append`. | Compone evidence references. |
| `TraceabilityEvidenceReference` | Entity | Conservar referencia de evidencia. | kind, external reference, content hash. | `attach`. | Propiedad de record; no posee bytes. |
| `BusinessObjectReference` | Value Object | Identificar sujeto entre contexts. | source context, object type, object ID. | inmutable. | Nunca carga objeto fuente. |
| `ActorReference`, `EvidenceReference` | Value Objects | Identificar actor/evidencia sin ownership. | type, ID, metadata segura. | inmutables. | Referencias tipadas externas. |
| `TraceabilityAppendPolicy`, `SensitivePayloadPolicy` | Domain Policies | Validar append y minimizar metadata. | fact traducido, Tenant, safe metadata. | `canAppend`, `sanitize`. | Puras; sin inbox/storage. |
| `BusinessTraceabilityRecordRepository` | Repository interface | Cargar y guardar root append-only. | `TraceabilityId`, root. | `byId`, `append`. | Implementación PostgreSQL. |

#### 2.6.11.2. Interface Layer

La interfaz separa query de timeline y consumo de facts. Los consumidores no
aceptan un scope ausente ni permiten mutar contexto fuente.

| Clase | Categoría | Propósito | Inputs clave | Operaciones principales | Colaboradores |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `TraceabilityQueryController` | REST Controller | Exponer timeline autorizado. | actor, Tenant/Workspace, subject/filter. | `getTimeline`, `getRecord`. | Query handler. |
| `BusinessFactConsumer` | Message Consumer | Recibir fact publicado duradero. | integration contract, event ID. | `consume`. | Inbox y append handler. |

#### 2.6.11.3. Application Layer

Application traduce contrato publicado, coordina deduplicación y append, y
construye proyección de consulta sin importar agregados fuente.

| Clase | Categoría | Propósito | Inputs clave | Operaciones principales | Colaboradores |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `AppendBusinessTraceabilityFactCommandHandler` | Command Handler | Agregar fact seguro y append-only. | `PublishedBusinessFact`, actor, evidence references. | `handle`. | Record repository y policies. |
| `TraceabilityTimelineQueryHandler` | Query Handler | Devolver timeline autorizada. | subject, filter, access scope. | `handle`. | Repository/projection. |
| `PublishedBusinessFactEventHandler` | Event Handler | Consumir fact deduplicado. | event ID, published fact. | `handle`. | Inbox y append handler. |
| `TraceabilityDeduplicationCoordinator` | Application Service | Coordinar claim/complete sin contaminar Domain. | event ID, consumer state. | `claim`, `complete`. | Inbox adapter. |

#### 2.6.11.4. Infrastructure Layer

Infrastructure implementa append repository, inbox y transporte posterior. Los
datos guardados excluyen secretos y credenciales de pago.

| Clase | Categoría | Propósito | Inputs / datos | Operaciones principales | Colaboradores |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `PostgresBusinessTraceabilityRecordRepository` | Repository implementation | Mapear record append-only y evidence references. | traceability records. | `byId`, `append`. | `BusinessTraceabilityRecordRepository`, PostgreSQL. |
| `TraceabilityFactInbox` | Inbox adapter | Deduplicar facts entregados al menos una vez. | event ID, status. | `claim`, `complete`. | Event handler/coordinator. |
| `TraceabilityTransportOutbox` | Transport support | Persistir publication posterior cuando corresponde. | outcome fact, correlación. | `enqueue`. | Transport adapter. |

#### 2.6.11.5. Bounded Context Software Architecture Component Level Diagrams

La vista C4 L3 separa query/fact consumer, intake, append application, dominio
y persistencia append-only. No convierte C4 Components en clases Java.

![Vista C4 L3 de BC-11 Business Traceability](../../../assets/chapter-2/c4/Nexa-API-BC-11-BusinessTraceability.svg)

*Nota. Elaboración propia.*

#### 2.6.11.6. Bounded Context Software Architecture Code Level Diagrams

Los diagramas concentran Domain en records, values y policies. El contrato
publicado es input de Application, no tipo táctico del Domain.

##### 2.6.11.6.1. Bounded Context Domain Layer Class Diagrams

El UML evita `IntegrationEventEnvelope`, inbox y outbox; presenta repository
append-only y referencias externas por identidad.

![Modelo de dominio táctico de BC-11 Business Traceability](../../../assets/chapter-2/tactical/BC-11/BC11_BusinessTraceability.svg)

*Nota. Elaboración propia.*

##### 2.6.11.6.2. Bounded Context Database Design Diagram

El modelo relacional usa uniqueness tenant-scoped de deduplicación y evidencia
FK local sólo hacia el record append-only.

![Diseño lógico de base de datos de BC-11 Business Traceability](../../../assets/chapter-2/tactical/BC-11/database-diagram.svg)

*Nota. Elaboración propia.*
