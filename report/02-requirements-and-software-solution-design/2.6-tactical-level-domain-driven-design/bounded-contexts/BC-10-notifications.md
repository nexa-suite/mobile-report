### 2.6.10. Bounded Context: Notifications

BC-10 conserva intención, preferencias y estados de entrega. Un intento o fallo
de notificación no modifica el hecho de negocio que lo originó.

#### 2.6.10.1. Canonical class dictionary

*Clases y responsabilidades de BC-10 por capa.*

| Layer | Class | Category | Purpose | Key Attributes / Inputs | Main Methods / Business Behavior | Relationships / Collaborators | Aggregate Owner / External References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Domain | Notification | Aggregate Root | Conserva una intención de entrega y su estado. | Notification ID, template ID, source fact, status. | Schedule or cancel. | Reacts to PublishedBusinessFact. | Owns NotificationRecipient and NotificationAttempt. |
| Domain | NotificationTemplate | Aggregate Root | Conserva contenido versionado por canal. | Template ID, key, channel, version. | Publish and retire. | Referenced by Notification through ID. | Independent lifecycle. |
| Domain | NotificationPreference | Aggregate Root | Conserva una preferencia por destinatario y canal. | Preference ID, recipient reference, channel, enabled. | Enable and disable. | Uses a typed recipient reference. | Independent lifecycle. |
| Domain | PushSubscription | Aggregate Root | Conserva una suscripción técnica de entrega. | Subscription ID, recipient reference, token hash, status. | Rotate token and disable. | Uses recipient reference only. | Independent delivery root. |
| Domain | NotificationRecipient | Entity | Conserva un destinatario resuelto. | Recipient reference, channel and destination snapshot. | Suppress delivery. | Local to Notification. | Owned by Notification. |
| Domain | NotificationAttempt | Entity | Conserva cada intento de entrega. | Channel, status and attempted time. | Record result. | Local to Notification. | Owned by Notification. |
| Domain | PublishedBusinessFact | Published Language | Expresa un hecho consumible de otro contexto. | Event ID, type and source context. | Carries committed fact data. | Wrapped by IntegrationEventEnvelope. | Never imports source aggregate ownership. |
| Domain | ChannelSelectionPolicy | Domain Policy | Decide un canal permitido. | Preference and available channels. | Select channel. | Pure values supplied by application. | No email, push or provider dependency. |
| Domain | RetryPolicy | Domain Policy | Calcula el siguiente intento. | Previous attempt and retry rule. | Schedule retry. | Pure values supplied by application. | No transport dependency. |
| Interface | BC-10 Interface Boundary | Interface component | Traduce preferencias, lectura y hechos de entrega. | Actor, scope and published fact. | Rejects invalid or duplicate input. | Calls application orchestration. | Does not decide source business state. |
| Application | BC-10 Application Orchestration | Application component | Coordina creación, entrega y reintento. | Published fact, preference and work state. | Deduplicates, dispatches and projects after commit. | Uses envelopes and local IDs. | Provider I/O stays outside Domain. |
| Infrastructure | BC-10 Persistence and Delivery Adapters | Infrastructure component | Persiste hechos y entrega por canales. | Notification records, inbox and delivery messages. | Maps records and calls delivery adapters. | PostgreSQL, inbox, outbox, email and push adapters. | Does not own source context data. |

El estado del origen permanece autoritativo en su contexto. Las entregas se
procesan al menos una vez con idempotencia; payloads y referencias minimizan PII
y no incluyen secretos.

#### 2.6.10.2. Component and code-level diagrams

*Vista C4 L3 de BC-10 Notifications.*

![Vista C4 L3 de BC-10 Notifications](../../../assets/chapter-2/c4/Nexa-API-BC-10-Notifications.svg)

*Nota. Elaboración propia.*

*Modelo de dominio táctico de BC-10 Notifications.*

![Modelo de dominio táctico de BC-10 Notifications](../../../assets/chapter-2/tactical/BC-10/BC10_Notifications.svg)

*Nota. Elaboración propia.*

*Diseño lógico de base de datos de BC-10 Notifications.*

![Diseño lógico de base de datos de BC-10 Notifications](../../../assets/chapter-2/tactical/BC-10/database-diagram.svg)

*Nota. Elaboración propia.*
