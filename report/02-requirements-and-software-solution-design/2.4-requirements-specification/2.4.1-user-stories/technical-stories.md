#### Technical Stories

Las Technical Stories habilitan resultados de las Functional User Stories; no
crean reglas de negocio ni prueban una implementación. La obligación académica
se lee inequívocamente como **Kotlin Android AND (Flutter/Dart OR KMP/Kotlin)**:
Track A es obligatorio y exige Android nativo con Kotlin; Track B también es
obligatorio y permite una alternativa multiplataforma, Flutter con Dart o Kotlin
Multiplatform (KMP) con Kotlin. La selección de framework Mobile en Blueprint
continúa **OPEN / NOT STARTED**: este plan no asigna framework a Operations
Mobile o Buyer Mobile, ni declara runtime, proveedor, distribución o validación
de producto.

##### TS-MOB-001 — Integrar contratos REST con autoridad del servidor

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-001</td><td>Developer</td><td>High</td><td>TECH-EPIC-01 — Contract and security foundations</td></tr>
<tr><th>Title</th><td colspan="3">Integrar contratos REST con autoridad del servidor</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo integrar contratos REST explícitos con Nexa API, para que los tracks académicos que se evalúen consuman datos y comandos sin crear una autoridad paralela ni seleccionar un framework fuera del experimento.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Contrato autorizado</strong></p><p><strong>Given</strong> una proyección Mobile solicita trabajo protegido</p><p><strong>When</strong> consume un contrato REST aprobado</p><p><strong>Then</strong> conserva Tenant, Workspace, autorización y significado de respuesta definidos por el servidor.</p><p><strong>Scenario: Respuesta de error</strong></p><p><strong>Given</strong> el servidor rechaza, encuentra conflicto o no puede procesar una solicitud</p><p><strong>When</strong> el cliente recibe Problem Details</p><p><strong>Then</strong> comunica el estado sin inventar una confirmación local.</p></td></tr>
</tbody>
</table>

##### TS-MOB-002 — Definir criterios de compatibilidad de plataforma

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-002</td><td>Developer</td><td>High</td><td>TECH-EPIC-02 — Platform baselines</td></tr>
<tr><th>Title</th><td colspan="3">Definir criterios de compatibilidad de plataforma</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo documentar compatibilidad, seguridad, accesibilidad, build y prueba para el Track A obligatorio de Android nativo con Kotlin y el Track B obligatorio de una alternativa multiplataforma permitida (Flutter/Dart o KMP/Kotlin), para evaluar límites técnicos sin convertir el experimento en una selección canónica de Blueprint.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Baseline de experimento</strong></p><p><strong>Given</strong> existen el Track A obligatorio de Android nativo con Kotlin y el Track B obligatorio de Flutter/Dart o KMP/Kotlin</p><p><strong>When</strong> se define un baseline mínimo</p><p><strong>Then</strong> documenta versiones, dispositivo/emulador, límites y criterios de comparación sin asignar un framework a una proyección de producto.</p><p><strong>Scenario: Límite explícito</strong></p><p><strong>Given</strong> aparece una plataforma o proveedor no evaluado</p><p><strong>When</strong> se propone incorporarlo</p><p><strong>Then</strong> queda fuera del experimento hasta una decisión explícita y no se presenta como trabajo académico comprometido.</p></td></tr>
</tbody>
</table>

##### TS-MOB-003 — Preservar paridad de contratos entre proyecciones Mobile

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

##### TS-MOB-004 — Aislar capacidades de dispositivo de las reglas de negocio

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

##### TS-MOB-005 — Proteger el estado local selectivo y no autoritativo

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

##### TS-MOB-006 — Resolver reintentos, resultados inciertos e idempotencia

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-006</td><td>Developer</td><td>High</td><td>TECH-EPIC-04 — Controlled continuity</td></tr>
<tr><th>Title</th><td colspan="3">Resolver reintentos, resultados inciertos e idempotencia</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo gestionar reintentos, conflictos y resultados inciertos con identificadores durables, para que una interrupción no duplique ni sobrescriba un hecho de negocio.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Reintento de comando</strong></p><p><strong>Given</strong> un comando pudo completarse pero la respuesta no llegó</p><p><strong>When</strong> se reenvía con el mismo identificador de idempotencia</p><p><strong>Then</strong> el servidor devuelve un único resultado sin duplicar el hecho.</p><p><strong>Scenario: Conflicto de versión</strong></p><p><strong>Given</strong> el recurso cambió después de la lectura del cliente</p><p><strong>When</strong> se envía una mutación obsoleta</p><p><strong>Then</strong> se identifica el conflicto y no se aplica last-write-wins silencioso.</p></td></tr>
</tbody>
</table>

##### TS-MOB-007 — Integrar cámara e identificadores con alternativa manual

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-007</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-03 — Device boundaries</td></tr>
<tr><th>Title</th><td colspan="3">Integrar cámara e identificadores con alternativa manual</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo integrar cámara, Barcode, QR y GS1 con una alternativa manual, para que la identificación sea útil sin convertir el dispositivo en autoridad de inventario.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Identificador único</strong></p><p><strong>Given</strong> la cámara obtiene un identificador permitido con coincidencia única</p><p><strong>When</strong> se envía al contrato autorizado</p><p><strong>Then</strong> identifica el producto sin registrar recepción o picking por sí sola.</p><p><strong>Scenario: Cámara no disponible</strong></p><p><strong>Given</strong> la cámara no está disponible o el identificador es ambiguo</p><p><strong>When</strong> la persona usa la alternativa manual</p><p><strong>Then</strong> el flujo continúa solo después de una identificación autorizada.</p></td></tr>
</tbody>
</table>

##### TS-MOB-008 — Abrir navegación externa con un límite de ubicación

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

##### TS-MOB-009 — Evaluar notificaciones y deep links con autorización

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>TS-MOB-009</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-05 — Quality and communication</td></tr>
<tr><th>Title</th><td colspan="3">Evaluar notificaciones y deep links con autorización</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo evaluar notificaciones y deep links con autorización, para definir límites de contexto y seguridad sin asumir proveedor o integración resueltos.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Contexto autorizado</strong></p><p><strong>Given</strong> un deep link refiere a trabajo protegido</p><p><strong>When</strong> la aplicación lo abre</p><p><strong>Then</strong> vuelve a comprobar Tenant, relación y permisos antes de mostrar información.</p><p><strong>Scenario: Destino vencido</strong></p><p><strong>Given</strong> el enlace venció o el contexto ya no es válido</p><p><strong>When</strong> se intenta abrir</p><p><strong>Then</strong> comunica el estado y no expone datos protegidos.</p></td></tr>
</tbody>
</table>

##### TS-MOB-010 — Aplicar i18n y accesibilidad en las aplicaciones móviles

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

##### TS-MOB-011 — Preparar validación técnica y observabilidad mínima

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

##### TS-MOB-012 — Preparar evidencia técnica de build, instalación y dispositivos

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
