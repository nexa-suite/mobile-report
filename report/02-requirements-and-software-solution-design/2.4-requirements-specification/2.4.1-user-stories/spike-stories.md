#### Spike Stories

Un Spike reduce una incertidumbre antes de una decisión. No es una Functional
User Story ni prueba arquitectura, investigación, integración, implementación o
validación de producto. Cada Spike deja fuente, experimento mínimo, límites y
una salida explícita: adoptar, diferir, rechazar o continuar con evidencia
adicional.

##### SPIKE-001 — Evaluar oportunidad de aprendizaje autónomo

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-001</td><td>Developer</td><td>Medium</td><td>SPIKE-EPIC-01 — Product uncertainty</td></tr>
<tr><th>Title</th><td colspan="3">Evaluar oportunidad de aprendizaje autónomo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo evaluar si existe una fuente canónica y una necesidad observable que justifique aprendizaje autónomo, para decidir adoptar, diferir o rechazar la exploración sin convertir una capacidad propuesta en funcionalidad de Nexa. La secuencia planificada es investigación en Sprint 2, PoC y selección condicionada en Sprint 3, y evidencia de integración sólo si existe decisión autorizada en Sprint 4.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Sprint 2 — investigación</strong></p><p><strong>Given</strong> no existe una decisión de producto aceptada</p><p><strong>When</strong> se revisan fuentes, necesidad y riesgos</p><p><strong>Then</strong> se registra una recomendación de adoptar, diferir o rechazar sin ejecutar PoC sobre datos de negocio.</p><p><strong>Scenario: Sprint 3 — PoC y selección condicionada</strong></p><p><strong>Given</strong> aparece una necesidad respaldada y límites de datos explícitos</p><p><strong>When</strong> la autoridad correspondiente permite definir el experimento mínimo</p><p><strong>Then</strong> usa datos no sensibles y deja la selección como decisión explícita, no como funcionalidad declarada.</p><p><strong>Scenario: Sprint 4 — evidencia de integración condicionada</strong></p><p><strong>Given</strong> existe selección autorizada y un resultado del PoC que justifica continuidad</p><p><strong>When</strong> se integra evidencia técnica acotada</p><p><strong>Then</strong> se clasifica como evidencia de integración, no como validación de producto o despliegue.</p></td></tr>
</tbody>
</table>

##### SPIKE-002 — Establecer tracks Mobile y límites de contratos

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-002</td><td>Developer</td><td>High</td><td>SPIKE-EPIC-02 — Mobile implementation tracks</td></tr>
<tr><th>Title</th><td colspan="3">Establecer tracks Mobile y límites de contratos</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo establecer el setup y los límites de contrato compatibles con la restricción académica Kotlin nativo + Flutter/Dart, o Kotlin Multiplatform (KMP), para evaluar opciones sin duplicar reglas de negocio ni seleccionar un framework para Operations Mobile o Buyer Mobile. Blueprint mantiene la decisión de framework OPEN / NOT STARTED.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Setup de experimento</strong></p><p><strong>Given</strong> existe la restricción académica Kotlin nativo + Flutter/Dart, o KMP</p><p><strong>When</strong> se prepara un baseline mínimo</p><p><strong>Then</strong> se documentan opciones, build, entorno, límites y responsable técnico sin convertirlas en una selección de producto.</p><p><strong>Scenario: Límite de contrato</strong></p><p><strong>Given</strong> dos opciones evaluadas consumen un flujo no autoritativo permitido</p><p><strong>When</strong> se comparan sus resultados</p><p><strong>Then</strong> se registran paridad, adaptación permitida y cualquier cambio requerido como contrato explícito.</p><p><strong>Scenario: Salida de decisión</strong></p><p><strong>Given</strong> termina la evaluación</p><p><strong>When</strong> se revisa la evidencia</p><p><strong>Then</strong> se propone adoptar, diferir o ajustar cada límite sin declarar implementación ni validación de producto.</p></td></tr>
</tbody>
</table>

##### SPIKE-003 — Delimitar identificadores de producto

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-003</td><td>Developer</td><td>Medium</td><td>SPIKE-EPIC-03 — Device capabilities</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar identificadores de producto</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar formatos Barcode, QR y GS1, ambigüedades y alternativa manual, para decidir qué identificación puede apoyar un flujo sin crear una decisión de inventario desde el dispositivo.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Formato evaluado</strong></p><p><strong>Given</strong> existe un identificador de prueba no sensible</p><p><strong>When</strong> se evalúa su lectura y consulta</p><p><strong>Then</strong> se registra formato, ambigüedad, permiso y contrato requerido.</p><p><strong>Scenario: Salida de decisión</strong></p><p><strong>Given</strong> la lectura no es única o la cámara no está disponible</p><p><strong>When</strong> se analiza la alternativa manual</p><p><strong>Then</strong> se adopta, difiere o rechaza el formato sin registrar recepción o picking por sí solo.</p></td></tr>
</tbody>
</table>

##### SPIKE-004 — Delimitar persistencia y recuperación local

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-004</td><td>Developer</td><td>High</td><td>SPIKE-EPIC-04 — Controlled continuity</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar persistencia y recuperación local</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar caché segura, borrador, evidencia temporal y metadatos de reintento, para decidir qué puede persistir, expirar y recuperarse sin declarar éxito de negocio ante una red interrumpida.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Dato clasificado</strong></p><p><strong>Given</strong> un dato candidato a persistencia local</p><p><strong>When</strong> se clasifica</p><p><strong>Then</strong> se identifica protección, expiración, limpieza por contexto y límite de autoridad.</p><p><strong>Scenario: Recuperación incierta</strong></p><p><strong>Given</strong> se interrumpe la red durante un envío</p><p><strong>When</strong> la aplicación se recupera</p><p><strong>Then</strong> muestra resultado no confirmado y usa idempotencia o conflicto del servidor antes de adoptar una decisión.</p></td></tr>
</tbody>
</table>

##### SPIKE-005 — Delimitar notificaciones y deep links

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-005</td><td>Developer</td><td>Medium</td><td>SPIKE-EPIC-05 — Contextual communication</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar notificaciones y deep links</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar eventos, permisos, expiración y revalidación de deep links, para decidir qué comunicación contextual puede abrir trabajo protegido sin exponer datos ni mutar hechos de negocio.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Enlace permitido</strong></p><p><strong>Given</strong> un evento candidato refiere a trabajo protegido</p><p><strong>When</strong> se prueba un deep link</p><p><strong>Then</strong> vuelve a validar Tenant, relación y permiso antes de mostrar el destino.</p><p><strong>Scenario: Enlace inválido</strong></p><p><strong>Given</strong> el enlace venció, es alterado o carece de permiso</p><p><strong>When</strong> se intenta abrir</p><p><strong>Then</strong> no expone datos y la salida adopta, difiere o rechaza el caso evaluado.</p></td></tr>
</tbody>
</table>

##### SPIKE-006 — Delimitar mapas y ubicación

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-006</td><td>Developer</td><td>Medium</td><td>SPIKE-EPIC-06 — Responsible navigation</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar mapas y ubicación</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar destino autorizado, permiso, retención y alternativa ante falla para navegación externa, para decidir si aporta valor sin introducir tracking continuo, ETA ni autoridad de ubicación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Navegación controlada</strong></p><p><strong>Given</strong> existe un destino autorizado de prueba</p><p><strong>When</strong> se abre en una aplicación externa</p><p><strong>Then</strong> se registra qué dato se comparte, qué permiso aplica y qué alternativa existe.</p><p><strong>Scenario: Falla o exceso de alcance</strong></p><p><strong>Given</strong> la navegación falla o se propone seguimiento adicional</p><p><strong>When</strong> se revisan límites y privacidad</p><p><strong>Then</strong> no cambia Delivery, no inventa llegada y la decisión adopta, difiere o rechaza la extensión.</p></td></tr>
</tbody>
</table>
