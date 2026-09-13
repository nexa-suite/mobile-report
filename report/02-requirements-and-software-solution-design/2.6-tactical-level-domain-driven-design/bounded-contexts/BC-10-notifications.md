### 2.6.10. Bounded Context: Notifications

Este contexto posee la intención de notificación, la política de destinatario y
canal, la entrega in-app o por correo y los hechos de reintento. El fallo de una
notificación nunca cambia el estado de negocio de origen. La entrega Mobile es
una proyección, no un BC Mobile.

#### 2.6.10.1. Domain Layer

*Agregados y límites invariantes de BC-10.*
| Aggregate/raíz | Límite e invariante |
| :--- | :--- |
| `Notification` | Intent, selección de destinatario y canal, y ciclo de vida |
| `NotificationTemplate` | Política versionada de template y contenido por canal |
| `NotificationPreference` | Preferencia y supresión por destinatario y canal |
| `PushSubscription` | Registro de entrega por destinatario y dispositivo, no un Aggregate Mobile |

`NotificationRecipient` y `NotificationAttempt` son hechos propiedad de
Notifications. Los Value Objects incluyen `NotificationId`, `TemplateKey`,
`Channel`, `DeliveryStatus` y `RecipientReference`; `ChannelSelectionPolicy` y
`RetryPolicy` son servicios de dominio. Los canales del alcance inicial son
in-app y correo; WhatsApp es externo o manual.

Invariantes de diseño: la entrega es al menos una vez con intentos deduplicados
visibles; el reintento o fallo terminal nunca muta PR, SO, Payment ni Delivery;
los payloads excluyen secretos y PII innecesario; la rotación de suscripciones y
el manejo de tokens inválidos se mantienen como comportamiento técnico de
entrega.

#### 2.6.10.2. Interface Layer

La Interface Layer cubre la lectura y preferencias de Notifications, la intención
de notificación, el estado de canal, el ciclo de vida de suscripciones y los
callbacks de workers. No se inventan rutas exactas ni DTOs de proveedor ausentes
en la evidencia de API. Los hechos de origen ingresan por outbox/inbox durable;
la confirmación del cliente no es confirmación del hecho de origen.

#### 2.6.10.3. Application Layer

La Application Layer consume hechos de origen, persiste la intención de
notificación, elige destinatario y canal, despacha, reintenta y proyecta una
vista in-app. Lease/fencing, idempotencia y backoff acotado protegen contra la
entrega duplicada. El estado de negocio de origen permanece bajo propiedad de su
BC de origen.

#### 2.6.10.4. Infrastructure Layer

La Infrastructure Layer organiza la propiedad lógica en PostgreSQL compartido
sobre `notification_template`, `notification`, `notification_recipient`,
`notification_preference`, `notification_attempt` y `push_subscription`. Los
adaptadores de proveedor se mantienen como ACL; no se asume un proveedor ni un
tercer canal. La persistencia técnica de outbox/inbox es infraestructura
compartida, no un BC nuevo.

*Clases TARGET por capa de BC-10.*

Los nombres siguientes concretan responsabilidades previstas; no implican endpoints, canales ni proveedores ya implementados.

| Capa | Clase / componente TARGET | Responsabilidad |
|---|---|---|
| Interface | `NotificationController` | Expone operaciones de consulta y preferencia sin decidir reglas de negocio. |
| Interface | `NotificationDeliveryConsumer` | Recibe hechos comprometidos que habilitan una entrega al destinatario. |
| Interface | `NotificationProjectionConsumer` | Materializa vistas de notificación sin convertirse en autoridad sobre el hecho origen. |
| Application | `CreateNotificationCandidateHandler` | Convierte un hecho elegible en un candidato deduplicable y auditable. |
| Application | `DispatchNotificationHandler` | Orquesta la entrega por canal usando preferencias resueltas por contrato. |
| Application | `RetryNotificationDeliveryHandler` | Programa un reintento acotado sin duplicar una entrega aceptada. |
| Application | `ManageNotificationPreferenceHandler` | Cambia preferencias explícitas del destinatario bajo su alcance autorizado. |
| Application | `ProjectNotificationHandler` | Actualiza la proyección de lectura a partir de hechos ya comprometidos. |
| Infrastructure | `NotificationRepositoryAdapter` | Persiste candidatos, intentos, preferencias y estados de entrega. |
| Infrastructure | `EmailDeliveryAdapter` | Implementa el puerto de entrega por correo sin filtrar secretos o PII innecesaria. |
| Infrastructure | `InAppNotificationAdapter` | Implementa el canal interno de notificaciones de la plataforma. |
| Infrastructure | `NotificationOutboxWorker` | Publica y consume trabajo durable con semántica al-menos-una-vez. |

#### 2.6.10.5. Bounded Context Software Architecture Component Level Diagrams

La vista C4 L3 **TARGET** muestra componentes conceptuales de este contexto dentro de Nexa API. No equivale a un Bounded Context adicional, una base de datos independiente ni una unidad de despliegue.

*Vista C4 L3 TARGET de BC-10 Notifications.*

![BC-10 Notifications — C4 L3 TARGET](../../../assets/chapter-2/c4/Nexa-API-BC-10-Notifications-TARGET-dark.svg)

*Nota.* Exportación vectorial desde una vista Structurizr DSL enfocada en BC-10 Notifications, dentro del único contenedor Nexa API. Es evidencia de diseño TARGET; no acredita implementación, runtime ni una unidad de despliegue independiente.

#### 2.6.10.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.10.6.1. Bounded Context Domain Layer Class Diagrams

*Modelo de dominio táctico de BC-10 Notifications.*
![BC-10 tactical domain model](../../../assets/chapter-2/tactical/BC-10/BC10_Notifications.png)
*Nota.* El diagrama se presenta como modelo de diseño, no como inventario de código.


##### 2.6.10.6.2. Bounded Context Database Design Diagram

*Proyección del diseño de base de datos de BC-10.*
![BC-10 database design projection](../../../assets/chapter-2/tactical/BC-10/database-diagram.png)

*Nota.* Es propiedad lógica en PostgreSQL compartido con restricciones de entrega; no implica una base de datos Mobile ni el despliegue de un proveedor push.
