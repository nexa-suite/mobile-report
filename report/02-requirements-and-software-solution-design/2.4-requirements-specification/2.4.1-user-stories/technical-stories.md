#### Technical Stories

Las Technical Stories habilitan resultados de las Functional User Stories; no
crean reglas de negocio ni prueban una implementación. El plan académico usa
dos tracks definidos: Android nativo con Kotlin y cross-platform con
Flutter/Dart. Sprint 1 y Sprint 2 concentran el baseline Android y el núcleo
operativo; Sprint 3 desarrolla el track Flutter/Dart y la paridad de contratos;
Sprint 4 consolida Flutter/Dart en target iOS. Esta asignación no declara
runtime, proveedor, distribución, implementación ni validación de producto.

**Tabla**<br>
*TS-MOB-001 — Integrar contratos REST con autoridad del servidor*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-001</td><td>Developer</td><td>High</td><td>TECH-EPIC-01 — Contract and security foundations</td></tr>
<tr><th>Title</th><td colspan="3">Integrar contratos REST con autoridad del servidor</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo integrar el base URL y entorno de API con clientes nativos tipados, manejo de bearer/sesión, Tenant y Workspace confirmados por servidor y Problem Details básicos, para que Mobile consuma contratos REST sin crear una autoridad paralela.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Cliente y entorno configurados</strong></p><p><strong>Given</strong> existe un entorno de API autorizado</p><p><strong>When</strong> Mobile inicia un flujo protegido</p><p><strong>Then</strong> usa su base URL configurada y clientes nativos tipados para el contrato correspondiente.</p><p><strong>Scenario: Sesión y contexto autorizados</strong></p><p><strong>Given</strong> el servidor devuelve una sesión válida</p><p><strong>When</strong> el cliente consume trabajo protegido</p><p><strong>Then</strong> envía el bearer o sesión requerido y conserva Tenant, Workspace y autorización con el significado confirmado por el servidor.</p><p><strong>Scenario: Problem Details y fallos básicos</strong></p><p><strong>Given</strong> el servidor responde 401, 403 o Problem Details, o la red no está disponible</p><p><strong>When</strong> el cliente procesa la respuesta</p><p><strong>Then</strong> la mapea de forma segura, comunica el estado y no inventa una confirmación local.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-002 — Implementar baseline técnico de compatibilidad de plataforma*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-002</td><td>Developer</td><td>High</td><td>TECH-EPIC-02 — Platform baselines</td></tr>
<tr><th>Title</th><td colspan="3">Implementar baseline técnico de compatibilidad de plataforma</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo implementar el baseline técnico de compatibilidad de Android nativo con Kotlin, para reproducir su build y validación técnica sin convertir la tarea en una selección de producto o framework.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Baseline Android autorizado</strong></p><p><strong>Given</strong> el Sprint asigna el baseline Android nativo con Kotlin</p><p><strong>When</strong> el Developer aplica las versiones, SDK, dispositivo y restricciones de build autorizadas</p><p><strong>Then</strong> el baseline es reproducible y registra su configuración sin abrir una nueva selección de producto o framework.</p><p><strong>Scenario: Validación identificable</strong></p><p><strong>Given</strong> el baseline Android nativo con Kotlin está configurado</p><p><strong>When</strong> se ejecutan build y pruebas</p><p><strong>Then</strong> el resultado identifica versión, commit y entorno, y no altera contratos ni autoridad compartidos.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-003 — Preservar paridad de contratos entre proyecciones Mobile*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-003</td><td>Developer</td><td>High</td><td>TECH-EPIC-01 — Contract and security foundations</td></tr>
<tr><th>Title</th><td colspan="3">Preservar paridad de contratos entre proyecciones Mobile</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo preservar el significado de contratos, errores, autorización e idempotencia entre las dos proyecciones, para que una diferencia de plataforma no cambie reglas compartidas.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Flujo comparable</strong></p><p><strong>Given</strong> dos opciones evaluadas implementan un flujo permitido</p><p><strong>When</strong> consumen el mismo contrato</p><p><strong>Then</strong> interpretan los mismos estados de éxito, error, conflicto e idempotencia.</p><p><strong>Scenario: Adaptación de interfaz</strong></p><p><strong>Given</strong> una opción exige una adaptación de presentación o dispositivo</p><p><strong>When</strong> se documenta la adaptación</p><p><strong>Then</strong> no altera autorización, Tenant/Workspace ni resultado de negocio.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-004 — Aislar capacidades de dispositivo de las reglas de negocio*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-004</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-03 — Device boundaries</td></tr>
<tr><th>Title</th><td colspan="3">Aislar capacidades de dispositivo de las reglas de negocio</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo encapsular cámara, navegación, almacenamiento y notificaciones detrás de límites técnicos, para que su disponibilidad no redefina autoridad, estado ni reglas del dominio.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Capacidad disponible</strong></p><p><strong>Given</strong> una capacidad está permitida para un flujo</p><p><strong>When</strong> el cliente la invoca</p><p><strong>Then</strong> entrega solo información autorizada y espera confirmación del servidor para un hecho de negocio.</p><p><strong>Scenario: Capacidad no disponible</strong></p><p><strong>Given</strong> falta permiso o la capacidad falla</p><p><strong>When</strong> el flujo continúa</p><p><strong>Then</strong> ofrece alternativa segura o comunica el límite sin inventar un resultado.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-005 — Proteger el estado local selectivo y no autoritativo*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-005</td><td>Developer</td><td>High</td><td>TECH-EPIC-04 — Controlled continuity</td></tr>
<tr><th>Title</th><td colspan="3">Proteger el estado local selectivo y no autoritativo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo proteger caché segura, borradores, evidencia temporal y metadatos de reintento, para conservar continuidad sin presentar el estado local como verdad de negocio.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Dato permitido</strong></p><p><strong>Given</strong> el dato está clasificado como caché, borrador, evidencia temporal o metadato de reintento</p><p><strong>When</strong> se persiste localmente</p><p><strong>Then</strong> queda protegido y vinculado al contexto autorizado.</p><p><strong>Scenario: Cambio de contexto</strong></p><p><strong>Given</strong> la persona cierra sesión o cambia de Tenant</p><p><strong>When</strong> se limpia el contexto local</p><p><strong>Then</strong> el siguiente contexto no puede leer datos protegidos del anterior.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-006 — Resolver reintentos, resultados inciertos e idempotencia*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-006</td><td>Developer</td><td>High</td><td>TECH-EPIC-04 — Controlled continuity</td></tr>
<tr><th>Title</th><td colspan="3">Resolver reintentos, resultados inciertos e idempotencia</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo gestionar reintentos, conflictos y resultados inciertos con identificadores durables, para que una interrupción no duplique ni sobrescriba un hecho de negocio.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Reintento de comando</strong></p><p><strong>Given</strong> el servidor procesa un comando pero el cliente no recibe la respuesta</p><p><strong>When</strong> el cliente reenvía el comando con el mismo identificador de idempotencia</p><p><strong>Then</strong> el servidor devuelve un único resultado sin duplicar el hecho.</p><p><strong>Scenario: Conflicto de versión</strong></p><p><strong>Given</strong> el recurso tiene una versión más nueva</p><p><strong>When</strong> el cliente envía una mutación basada en una versión anterior</p><p><strong>Then</strong> Nexa identifica el conflicto y no aplica last-write-wins silencioso.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-007 — Integrar cámara e identificadores para escaneo directo*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-007</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-03 — Device boundaries</td></tr>
<tr><th>Title</th><td colspan="3">Integrar cámara e identificadores para escaneo directo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo integrar cámara y decodificación de identificadores para escaneo directo, para enviar el código capturado a la resolución autoritativa del servidor sin convertir el dispositivo en autoridad de inventario.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Captura y decodificación directa</strong></p><p><strong>Given</strong> la cámara tiene permiso y obtiene un identificador Barcode, QR o GS1 permitido</p><p><strong>When</strong> el cliente lo decodifica</p><p><strong>Then</strong> envía el valor capturado al contrato de resolución autorizado.</p><p><strong>Scenario: Resolución autoritativa</strong></p><p><strong>Given</strong> el servidor procesa el identificador capturado</p><p><strong>When</strong> responde <code>RESOLVED</code>, <code>NOT_FOUND</code> o <code>AMBIGUOUS</code></p><p><strong>Then</strong> Mobile muestra ese resultado y no selecciona un SKU localmente.</p><p><strong>Scenario: Permiso o cámara no disponibles</strong></p><p><strong>Given</strong> falta permiso de cámara, la cámara no está disponible o la decodificación falla</p><p><strong>When</strong> la persona intenta escanear</p><p><strong>Then</strong> Mobile comunica el límite de forma segura y no inventa una identificación.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-008 — Abrir navegación externa con un límite de ubicación*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-008</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-03 — Device boundaries</td></tr>
<tr><th>Title</th><td colspan="3">Abrir navegación externa con un límite de ubicación</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo entregar un destino autorizado a navegación externa, para apoyar una entrega sin crear seguimiento continuo ni autoridad de ubicación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Destino autorizado</strong></p><p><strong>Given</strong> existe una entrega activa y un destino autorizado</p><p><strong>When</strong> se solicita navegación externa</p><p><strong>Then</strong> se entrega solo el destino permitido al proveedor elegido.</p><p><strong>Scenario: Navegación fallida</strong></p><p><strong>Given</strong> el proveedor externo no está disponible o el destino no es válido</p><p><strong>When</strong> se intenta abrir indicaciones</p><p><strong>Then</strong> la entrega conserva su estado y el fallo no inventa una llegada.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-009 — Preparar el manejo autorizado de notificaciones y deep links*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-009</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-05 — Quality and communication</td></tr>
<tr><th>Title</th><td colspan="3">Preparar el manejo autorizado de notificaciones y deep links</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo preparar el manejo técnico autorizado de notificaciones y deep links conforme a los límites aceptados, para revalidar el contexto antes de mostrar trabajo protegido sin asumir proveedor o integración productiva.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Contexto autorizado</strong></p><p><strong>Given</strong> SPIKE-005 tiene un límite registrado como adoptado, diferido o rechazado</p><p><strong>When</strong> el Developer prepara el caso autorizado</p><p><strong>Then</strong> la implementación consume sólo el contrato permitido y revalida Tenant, relación y permiso antes de mostrar información.</p><p><strong>Scenario: Enlace vencido</strong></p><p><strong>Given</strong> el enlace está vencido o el contexto ya no es válido</p><p><strong>When</strong> se intenta abrir</p><p><strong>Then</strong> comunica el estado, no expone datos protegidos y ofrece un estado recuperable cuando corresponda.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-010 — Aplicar i18n y accesibilidad en las aplicaciones móviles*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-010</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-05 — Quality and communication</td></tr>
<tr><th>Title</th><td colspan="3">Aplicar i18n y accesibilidad en las aplicaciones móviles</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo incorporar internacionalización y accesibilidad en ambas aplicaciones, para que contenido, estados y acciones puedan comprenderse y operarse con configuraciones y necesidades diferentes.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Cambio de idioma</strong></p><p><strong>Given</strong> la aplicación dispone de un idioma soportado</p><p><strong>When</strong> cambia la configuración</p><p><strong>Then</strong> títulos, errores y estados se presentan traducidos sin alterar los datos de negocio.</p><p><strong>Scenario: Lectura asistida</strong></p><p><strong>Given</strong> una persona utiliza una tecnología de asistencia</p><p><strong>When</strong> recorre un flujo Mobile</p><p><strong>Then</strong> controles, estados, errores y orden de lectura tienen nombres y relaciones comprensibles.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-011 — Preparar validación técnica y observabilidad mínima*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-011</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-05 — Quality and communication</td></tr>
<tr><th>Title</th><td colspan="3">Preparar validación técnica y observabilidad mínima</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo validar contratos, autorización, reintentos, estado local y errores con observabilidad mínima, para diagnosticar fallos sin registrar secretos, Tenant IDs innecesarios ni PII.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Validación de contrato</strong></p><p><strong>Given</strong> existe una operación Mobile representativa</p><p><strong>When</strong> se prueba éxito y error</p><p><strong>Then</strong> se verifica autorización, estructura, conflicto e idempotencia.</p><p><strong>Scenario: Señal segura</strong></p><p><strong>Given</strong> una solicitud Mobile falla</p><p><strong>When</strong> se registra una señal diagnóstica</p><p><strong>Then</strong> conserva correlación y causa útil sin incluir tokens, secretos o datos sensibles innecesarios.</p></td></tr>
</tbody>
</table>

**Tabla**<br>
*TS-MOB-012 — Preparar evidencia técnica de build, instalación y dispositivos*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-012</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-05 — Quality and communication</td></tr>
<tr><th>Title</th><td colspan="3">Preparar evidencia técnica de build, instalación y dispositivos</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo preparar evidencia repetible de build, instalación y prueba en dispositivos para los tracks definidos, para distinguir factibilidad técnica de validación de producto.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Build identificable</strong></p><p><strong>Given</strong> un track tiene configuración documentada</p><p><strong>When</strong> se genera un build de prueba</p><p><strong>Then</strong> el artefacto identifica track, versión, commit y entorno utilizados.</p><p><strong>Scenario: Evidencia separada</strong></p><p><strong>Given</strong> el build se instala en un dispositivo o emulador compatible</p><p><strong>When</strong> se registra el resultado</p><p><strong>Then</strong> se clasifica como evidencia técnica y no como investigación validada, aceptación funcional o preparación de producción.</p></td></tr>
</tbody>
</table>
