#### Spike Stories

Un Spike reduce una incertidumbre delimitada. No es una Functional User Story
ni convierte por sí solo una investigación, PoC o integración en validación de
producto. Cada Spike deja fuente, experimento mínimo, límites, criterios de
selección y el trabajo de integración que corresponda. Cuando el alcance del
Spike exige integración, ésta se documenta como evidencia técnica acotada y no
como runtime aceptado.

### Shared Spike Definition of Done

Un Spike se considera cerrado sólo cuando el equipo:

- responde la pregunta planteada y conserva las fuentes y hallazgos;
- registra el experimento mínimo o explica por qué no era necesario;
- documenta límites, riesgos y datos no sensibles utilizados;
- concluye si la opción se adopta, se difiere o se rechaza;
- refina el backlog o deja explícito el trabajo diferido; y
- cuando el alcance del Spike exige integración, registra la integración técnica
  acotada, sus fallos, reversión o aislamiento y su evidencia, sin presentarla
  como implementación productiva o aceptación de producto.

Estos criterios definen el cierre esperado; no prueban que un PoC o una
integración ya exista.

**Tabla**<br>
*SPIKE-001 — Investigar, evaluar e integrar una feature de aprendizaje autónomo*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-001</td><td>Developer</td><td>High</td><td>SPIKE-EPIC-01 — Autonomous learning feature</td></tr>
<tr><th>Title</th><td colspan="3">Investigar, evaluar e integrar una feature de aprendizaje autónomo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo investigar, evaluar e integrar técnicamente una feature de aprendizaje autónomo para un flujo Mobile representativo de Nexa, para tomar una decisión reproducible sin crear una autoridad de negocio local. La evaluación usa datos no sensibles, contratos explícitos y límites de seguridad; no declara una decisión de Producto aceptada ni preparación productiva.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Necesidad y pregunta de investigación</strong></p><p><strong>Given</strong> un flujo Mobile representativo y una incertidumbre de aprendizaje autónomo</p><p><strong>When</strong> el Developer formula la necesidad, la pregunta y los límites de datos</p><p><strong>Then</strong> documenta el resultado esperado sin delegar reglas de negocio ni autorización al componente explorado.</p><p><strong>Scenario: Alternativas y criterios</strong></p><p><strong>Given</strong> existe una pregunta de investigación delimitada</p><p><strong>When</strong> se comparan al menos dos alternativas</p><p><strong>Then</strong> se registran criterios de utilidad, exactitud, privacidad, coste, operabilidad, accesibilidad, compatibilidad, riesgos y debilidades.</p><p><strong>Scenario: Selección justificada y PoC reproducible</strong></p><p><strong>Given</strong> están definidos los criterios y datos sintéticos o no sensibles</p><p><strong>When</strong> se selecciona una alternativa y se ejecuta el experimento mínimo</p><p><strong>Then</strong> se conserva la justificación, fuente, pasos, entorno, resultado observado y límites, sin presentar el PoC como aceptación de producto.</p><p><strong>Scenario: Integración técnica acotada</strong></p><p><strong>Given</strong> la alternativa seleccionada puede probarse en un flujo representativo</p><p><strong>When</strong> se integra técnicamente de forma acotada</p><p><strong>Then</strong> conserva el contrato, maneja fallos y registra reversión o aislamiento sin reclamar preparación productiva.</p><p><strong>Scenario: Evidencia y reflexión</strong></p><p><strong>Given</strong> termina la investigación, evaluación e integración acotada</p><p><strong>When</strong> el equipo revisa el resultado</p><p><strong>Then</strong> documenta evidencia disponible, aprendizaje, limitaciones, una conclusión de adoptar, diferir o rechazar y una reflexión vinculada al Student Outcome 7 sin reclamar pruebas inexistentes.</p></td></tr>
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
<tr><td colspan="4">Como <strong>Developer</strong>, deseo establecer el baseline y los límites de contrato para Android nativo con Kotlin y cross-platform con Flutter/Dart, para documentar paridad, adaptaciones, restricciones e interoperabilidad entre Operations Mobile y Buyer Mobile sin duplicar reglas de negocio. La dirección Flutter/Dart ya está definida para el track cross-platform; este Spike no vuelve a seleccionar framework.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Baselines de los dos tracks</strong></p><p><strong>Given</strong> el plan contempla Android nativo con Kotlin y cross-platform con Flutter/Dart</p><p><strong>When</strong> se prepara el experimento mínimo</p><p><strong>Then</strong> se documentan versiones, SDK, build, entorno y restricciones de cada track sin presentar el resultado como implementación aceptada.</p><p><strong>Scenario: Paridad de contratos</strong></p><p><strong>Given</strong> ambos tracks consumen un flujo permitido</p><p><strong>When</strong> se comparan sus resultados</p><p><strong>Then</strong> se registran paridad, adaptación de plataforma, interoperabilidad y cualquier diferencia que no pueda modificar reglas, autorización ni autoridad del servidor.</p><p><strong>Scenario: Salida de investigación</strong></p><p><strong>Given</strong> termina el experimento</p><p><strong>When</strong> se revisa la evidencia</p><p><strong>Then</strong> se documentan baseline, contratos, restricciones, riesgos, límites y trabajo de integración propuesto, sin volver a abrir la decisión de framework ni declarar implementación o validación de producto.</p></td></tr>
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
<tr><td colspan="4"><p><strong>Scenario: Dato clasificado</strong></p><p><strong>Given</strong> un dato candidato a persistencia local</p><p><strong>When</strong> se clasifica</p><p><strong>Then</strong> se identifica protección, expiración, limpieza por contexto y límite de autoridad.</p><p><strong>Scenario: Recuperación incierta</strong></p><p><strong>Given</strong> se interrumpe la red durante un envío</p><p><strong>When</strong> la aplicación se recupera</p><p><strong>Then</strong> muestra resultado no confirmado y usa idempotencia o conflicto del servidor antes de adoptar una decisión.</p><p><strong>Scenario: Cierre y conclusión</strong></p><p><strong>Given</strong> se evaluaron los candidatos de persistencia y recuperación</p><p><strong>When</strong> el equipo revisa los resultados</p><p><strong>Then</strong> documenta qué puede persistir, su expiración y protección, cómo se recupera, qué casos se difieren y si la alternativa se adopta, se difiere o se rechaza.</p></td></tr>
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
<tr><td colspan="4"><p><strong>Scenario: Enlace permitido</strong></p><p><strong>Given</strong> un evento candidato refiere a trabajo protegido</p><p><strong>When</strong> se prueba un deep link</p><p><strong>Then</strong> vuelve a validar Tenant, relación y permiso antes de mostrar el destino.</p><p><strong>Scenario: Enlace inválido</strong></p><p><strong>Given</strong> el enlace está vencido, es alterado o carece de permiso</p><p><strong>When</strong> se intenta abrir</p><p><strong>Then</strong> no expone datos y el equipo documenta si el caso se adopta, se difiere o se rechaza.</p></td></tr>
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
<tr><td colspan="4"><p><strong>Scenario: Navegación controlada</strong></p><p><strong>Given</strong> existe un destino autorizado de prueba</p><p><strong>When</strong> se abre en una aplicación externa</p><p><strong>Then</strong> se registra qué dato se comparte, qué permiso aplica y qué alternativa existe.</p><p><strong>Scenario: Falla o exceso de alcance</strong></p><p><strong>Given</strong> la navegación falla o se propone seguimiento adicional</p><p><strong>When</strong> se revisan límites y privacidad</p><p><strong>Then</strong> no cambia Delivery, no inventa llegada y el equipo documenta si la extensión se adopta, se difiere o se rechaza.</p></td></tr>
</tbody>
</table>
