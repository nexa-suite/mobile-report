# Mobile Functional Stories V3 and Future

V3 contiene outcomes posteriores que requieren mayor refinamiento. V4/Future conserva una hipótesis de automatización de almacén sin seleccionar mecanismo ni fecha de entrega.

#### MOB-US-054 — Solicitar sustitución de lote cuando FEFO no completa el trabajo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-054` | Warehouse Operator | Low | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Solicitar sustitución de lote cuando FEFO no completa el trabajo |  |  |
| **Description** | Como **Warehouse Operator**, deseo solicitar una sustitución permitida de lote cuando el lote esperado no puede completar el trabajo, para revisar el pedido sin omitir la política de disponibilidad. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Sustitución solicitada**<br>**Given** el lote esperado no puede suministrar la cantidad preparada<br>**When** el operador propone una alternativa elegible<br>**Then** Nexa la envía a decisión autorizada con ambos lotes visibles.<br><br>**Scenario 2 — Decisión controlada**<br>**Given** una sustitución es rechazada o queda desactualizada<br>**When** el operador continúa<br>**Then** Nexa conserva la asignación original y explica la siguiente acción permitida. |  |  |

#### MOB-US-055 — Usar información ampliada de identidad de producto, paquete y almacenamiento

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-055` | Warehouse Operator | Low | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Usar información ampliada de identidad de producto, paquete y almacenamiento |  |  |
| **Description** | Como **Warehouse Operator**, deseo usar información más rica de identidad de producto, paquete y almacenamiento, para manipular el stock previsto con menos errores de identificación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Identidad resuelta**<br>**Given** existe un identificador permitido de paquete o almacenamiento<br>**When** el operador lo presenta<br>**Then** Nexa muestra el producto correspondiente y el contexto actual antes de iniciar el trabajo.<br><br>**Scenario 2 — Identidad no disponible**<br>**Given** el identificador es desconocido o ilegible<br>**When** el operador intenta continuar<br>**Then** Nexa ofrece un alternativa explícito o indica que se requiere confirmación. |  |  |

#### MOB-US-056 — Preparar un grupo de tareas de almacén

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-056` | Warehouse Operator | Low | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Preparar un grupo de tareas de almacén |  |  |
| **Description** | Como **Warehouse Operator**, deseo preparar un grupo de tareas de almacén, para trabajar eficientemente sin perder el resultado de cada elemento. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Grupo preparado**<br>**Given** hay varias tareas permitidas disponibles<br>**When** el operador las agrupa<br>**Then** Nexa muestra claramente elementos, secuencia y comprobaciones requeridas.<br><br>**Scenario 2 — Un elemento difiere**<br>**Given** una tarea no puede completarse como fue preparada<br>**When** el operador registra la diferencia<br>**Then** Nexa mantiene separados los resultados de las otras tareas e identifica el elemento que requiere revisión. |  |  |

#### MOB-US-059 — Preparar cargas agrupadas y múltiples paradas

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-059` | Dispatch Coordinator | Low | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Preparar cargas agrupadas y múltiples paradas |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo preparar una carga de entrega agrupada con sus paradas, para despachar entregas compatibles manteniendo visibles sus restricciones. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Carga compatible**<br>**Given** las entregas cumplen las reglas de agrupación aceptadas<br>**When** el coordinador prepara una carga<br>**Then** Nexa muestra cada entrega, parada y condición requerida.<br><br>**Scenario 2 — Entrega incompatible**<br>**Given** una entrega incumple una regla de cliente o cadena de frío<br>**When** el coordinador prepara la carga<br>**Then** Nexa la mantiene fuera de la carga y explica por qué. |  |  |

#### MOB-US-060 — Completar un handoff al transportista con responsabilidad trazable

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-060` | Dispatch Coordinator | Low | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Completar un handoff al transportista con responsabilidad trazable |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo completar un handoff al transportista con responsabilidad clara, para que todos sepan quién controla la carga después de que abandona el almacén. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Handoff aceptado**<br>**Given** existe una carga preparada y un carrier autorizado<br>**When** el coordinador registra el handoff<br>**Then** Nexa conserva carrier, persona, momento y responsabilidad de entrega.<br><br>**Scenario 2 — Evidencia incompleta**<br>**Given** falta evidencia requerida del handoff<br>**When** el coordinador intenta finalizarlo<br>**Then** Nexa deja la responsabilidad en el responsable actual e indica qué se requiere. |  |  |

#### MOB-US-066 — Recuperar una entrega activa mediante operación offline selectiva

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-066` | Driver or Delivery Operator | Low | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Recuperar una entrega activa mediante operación offline selectiva |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo conservar evidencia seleccionada de entrega durante una pérdida de conexión, para recuperar el trabajo sin afirmar un resultado de entrega no confirmado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Evidencia retenida**<br>**Given** se captura un elemento de evidencia permitido sin conexión<br>**When** el conductor vuelve a tener cobertura<br>**Then** Nexa muestra su estado pendiente y permite revisarlo antes del envío.<br><br>**Scenario 2 — Recuperación autoritativa**<br>**Given** la entrega cambió mientras el dispositivo estaba offline<br>**When** se revisa la evidencia<br>**Then** Nexa resuelve explícitamente el conflicto y nunca aplica silenciosamente un resultado desactualizado. |  |  |

#### MOB-US-029 — Compartir la ubicación durante una entrega activa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-029` | Driver or Delivery Operator | Low | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |
| **Title** | Compartir la ubicación durante una entrega activa |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo compartir la ubicación de una entrega durante una entrega activa, para que un servicio de ubicación futuro y aceptado atienda una necesidad acotada de entrega. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Consentimiento futuro**<br>**Given** se acepta una política futura de ubicación<br>**When** el conductor comparte una ubicación<br>**Then** consentimiento, alcance y retención quedan explícitos.<br><br>**Scenario 2 — Sin entrega activo**<br>**Given** no existe una entrega activa<br>**When** se solicita la ubicación<br>**Then** no se comparte ninguna ubicación.<br><br>**Scenario 3 — Límite de privacidad**<br>**Given** la persona retira el permiso<br>**When** se solicita compartir ubicación<br>**Then** no se divulga ninguna ubicación nueva. |  |  |

#### MOB-US-045 — Ver un conductor activo en un mapa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-045` | Customer Buyer | Low | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |
| **Title** | Ver un conductor activo en un mapa |  |  |
| **Description** | Como **Customer Buyer**, deseo ver en un mapa un conductor activo, para que un servicio futuro y autorizado me ayude a comprender el horario de llegada. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Ubicación futura**<br>**Given** se acepta una política futura de ubicación<br>**When** el comprador abre una entrega activo<br>**Then** solo se muestra ubicación acotada con consentimiento.<br><br>**Scenario 2 — Sin entrega activo**<br>**Given** no existe una entrega activo<br>**When** el comprador solicita un mapa<br>**Then** no se divulga la ubicación del conductor.<br><br>**Scenario 3 — Límite de privacidad**<br>**Given** falta permiso o relación<br>**When** el comprador solicita un mapa<br>**Then** no se divulga ninguna ubicación. |  |  |

#### MOB-US-072 — Trabajar con un cliente mediante una visita de campo autorizada

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-072` | Sales Representative | Low | `MOBILE-EPIC-11` — Seguimiento comercial y financiero |
| **Title** | Trabajar con un cliente mediante una visita de campo autorizada |  |  |
| **Description** | Como **Sales Representative**, deseo trabajar con un cliente mediante una visita de campo autorizada, para iniciar con el contexto correcto de relación y terminar con un seguimiento claro. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Visita autorizada**<br>**Given** el representante tiene permiso para la relación del cliente<br>**When** inicia una visita<br>**Then** Nexa muestra el contexto permitido del cliente y su propósito.<br><br>**Scenario 2 — Seguimiento capturado**<br>**Given** la visita produce un seguimiento permitido<br>**When** el representante lo registra<br>**Then** Nexa vincula el resultado con la relación del cliente sin crear un compromiso no aprobado. |  |  |

#### MOB-US-073 — Usar evidencia de automatización de almacén en un trabajo controlado

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-073` | Warehouse Operator | Future | `MOBILE-EPIC-12` — Automatización de almacén futura |
| **Title** | Usar evidencia de automatización de almacén en un trabajo controlado |  |  |
| **Description** | Como **Warehouse Operator**, deseo revisar observaciones avanzadas de almacén mediante una decisión controlada, para que una automatización futura ayude al trabajo sin convertirse en verdad de stock no examinada. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Resultado valioso antes de seleccionar tecnología**<br>**Given** Product explora observaciones avanzadas de almacén<br>**When** define el resultado de almacén antes de seleccionar un dispositivo o proveedor<br>**Then** identifica primero un resultado valioso de almacén.<br><br>**Scenario 2 — Observación automatizada subordinada**<br>**Given** existe una observación automatizada considerada para el trabajo<br>**When** se revisa para apoyar una decisión de almacén<br>**Then** permanece atribuible y revisable y está subordinada a la autorización del responsable del Bounded Context.<br><br>**Scenario 3 — Release sin implementación específica**<br>**Given** el release contempla esta hipótesis de automatización futura<br>**When** se describe su alcance<br>**Then** no promete una implementación específica de RFID, scanner, sensor, label ni telemetry. |  |  |
