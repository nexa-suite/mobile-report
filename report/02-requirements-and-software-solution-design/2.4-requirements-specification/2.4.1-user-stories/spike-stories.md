#### Spike Stories

Un Spike reduce una incertidumbre antes de una decisión. No es una Functional
User Story ni convierte por sí solo una investigación, PoC o integración en
validación de producto. Cada Spike deja fuente, experimento mínimo, límites y
una salida explícita: adoptar, diferir, rechazar o continuar con evidencia
adicional. Cuando el alcance del Spike lo exige, la integración queda
documentada como evidencia técnica acotada y no como runtime aceptado.

**Tabla**<br>
*SPIKE-001 — Investigar, seleccionar e integrar una feature de aprendizaje autónomo*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-001</td><td>Developer</td><td>High</td><td>SPIKE-EPIC-01 — Autonomous learning feature</td></tr>
<tr><th>Title</th><td colspan="3">Investigar, seleccionar e integrar una feature de aprendizaje autónomo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo investigar, seleccionar e integrar una feature de aprendizaje autónomo que aporte un resultado Mobile real de Nexa, para cumplir el requisito académico con una decisión técnica reproducible sin crear una autoridad de negocio local. La feature debe usar una tecnología, librería o servicio no trabajado previamente en clase y debe evaluarse con datos no sensibles, contratos explícitos y límites de seguridad.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Necesidad y pregunta de investigación</strong></p><p><strong>Given</strong> un resultado Mobile comprometido y una feature de aprendizaje autónomo obligatoria</p><p><strong>When</strong> el Developer formula la necesidad, la pregunta y los límites de datos</p><p><strong>Then</strong> documenta el resultado esperado sin delegar reglas de negocio ni autorización al componente explorado.</p><p><strong>Scenario: Alternativas evaluadas</strong></p><p><strong>Given</strong> existe una pregunta de investigación delimitada</p><p><strong>When</strong> se comparan al menos dos tecnologías, librerías o servicios no trabajados previamente en clase</p><p><strong>Then</strong> se registran criterios de aprendizaje, exactitud o utilidad, privacidad, coste, operabilidad, accesibilidad, compatibilidad con Android nativo y la alternativa multiplataforma permitida, junto con riesgos y debilidades.</p><p><strong>Scenario: PoC reproducible</strong></p><p><strong>Given</strong> están definidos los criterios y datos sintéticos o no sensibles</p><p><strong>When</strong> se ejecuta el experimento mínimo</p><p><strong>Then</strong> se conserva la fuente, pasos, entorno, resultado observado y límites; no se presenta el PoC como build, runtime o aceptación de producto.</p><p><strong>Scenario: Selección e integración acotada</strong></p><p><strong>Given</strong> la comparación y el PoC muestran una alternativa viable</p><p><strong>When</strong> se selecciona una opción y se define su integración en el flujo Mobile</p><p><strong>Then</strong> quedan explícitos la decisión, el punto de integración, el contrato, el manejo de fallos, la observabilidad y la forma de revertir o aislar la feature.</p><p><strong>Scenario: Evidencia y reflexión</strong></p><p><strong>Given</strong> termina la investigación y la integración planificada o ejecutada</p><p><strong>When</strong> el equipo revisa el resultado</p><p><strong>Then</strong> documenta evidencia disponible, aprendizaje, limitaciones y una reflexión vinculada al Student Outcome 7 sin reclamar pruebas inexistentes.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*SPIKE-002 — Establecer tracks Mobile y límites de contratos*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-002</td><td>Developer</td><td>High</td><td>SPIKE-EPIC-02 — Mobile implementation tracks</td></tr>
<tr><th>Title</th><td colspan="3">Establecer tracks Mobile y límites de contratos</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo establecer el setup y los límites de contrato compatibles con la obligación académica <strong>Kotlin Android AND (Flutter/Dart OR KMP/Kotlin)</strong>: un Track A obligatorio de Android nativo con Kotlin y un Track B obligatorio de Flutter con Dart o Kotlin Multiplatform (KMP) con Kotlin, para evaluar opciones sin duplicar reglas de negocio ni seleccionar un framework para Operations Mobile o Buyer Mobile. La decisión de framework permanece OPEN / NOT STARTED.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Setup de experimento</strong></p><p><strong>Given</strong> existe la obligación académica <strong>Kotlin Android AND (Flutter/Dart OR KMP/Kotlin)</strong></p><p><strong>When</strong> se prepara un baseline mínimo</p><p><strong>Then</strong> se documentan opciones, build, entorno, límites y responsable técnico sin convertirlas en una selección de producto.</p><p><strong>Scenario: Límite de contrato</strong></p><p><strong>Given</strong> dos opciones evaluadas consumen un flujo no autoritativo permitido</p><p><strong>When</strong> se comparan sus resultados</p><p><strong>Then</strong> se registran paridad, adaptación permitida y cualquier cambio requerido como contrato explícito.</p><p><strong>Scenario: Salida de decisión</strong></p><p><strong>Given</strong> termina la evaluación</p><p><strong>When</strong> se revisa la evidencia</p><p><strong>Then</strong> se propone adoptar, diferir o ajustar cada límite sin declarar implementación ni validación de producto.</p></td></tr>
</tbody>
</table>

**Tabla**<br>

*SPIKE-003 — Delimitar identificadores de producto*

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

**Tabla**<br>
*SPIKE-004 — Delimitar persistencia y recuperación local*

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

**Tabla**<br>
*SPIKE-005 — Delimitar notificaciones y deep links*

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

**Tabla**<br>
*SPIKE-006 — Delimitar mapas y ubicación*

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
