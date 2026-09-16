#### Spike Stories

Un Spike reduce una incertidumbre delimitada mediante investigación, análisis o un
experimento mínimo. No es una Functional User Story y no convierte una PoC,
integración acotada o decisión técnica en validación de producto. Sus resultados
deben conservar fuentes, criterios, límites y la consecuencia que corresponda
para el Product Backlog.

### Shared Spike Definition of Done

Un Spike se considera cerrado sólo cuando el equipo:

- documenta la pregunta, las fuentes y los hallazgos relevantes;
- registra alternativas y criterios de evaluación proporcionales a la
  incertidumbre;
- documenta una PoC o experimento mínimo, o justifica de forma explícita por qué
  no es necesario;
- registra riesgos, limitaciones, privacidad y seguridad cuando aplican;
- conserva una conclusión técnica: adoptar, ajustar, diferir o rechazar;
- registra el refinamiento del backlog que resulte necesario;
- revisa los hallazgos con el equipo; y
- realiza el trabajo dentro de un **timebox de 8–16 horas en el Sprint**.

Los Story Points permanecen como estimación del Product Backlog; el timebox
describe el esfuerzo de investigación. Estos criterios definen cómo se cierra un
Spike, no afirman que la PoC, la integración o el producto ya existan.

*SPIKE-001 — Investigar, evaluar e integrar una feature de aprendizaje autónomo*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-001</td><td>Developer</td><td>High</td><td>SPIKE-EPIC-01 — Autonomous learning feature</td></tr>
<tr><th>Title</th><td colspan="3">Investigar, evaluar e integrar una feature de aprendizaje autónomo</td></tr>
<tr><th colspan="4">Context / uncertainty</th></tr>
<tr><td colspan="4">No está definido qué alternativa de aprendizaje autónomo puede aportar apoyo a un flujo Mobile representativo sin delegar reglas de negocio, autorización ni hechos del dominio a un componente local.</td></tr>
<tr><th colspan="4">Research objective</th></tr>
<tr><td colspan="4">Comparar alternativas documentadas y determinar, mediante un experimento reproducible con datos sintéticos o no sensibles, si alguna puede apoyar el aprendizaje del usuario dentro de límites de privacidad, operabilidad y coste.</td></tr>
<tr><th colspan="4">Spike Story</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo investigar, evaluar e integrar técnicamente una feature de aprendizaje autónomo para un flujo Mobile representativo de Nexa, para tomar una decisión reproducible sin crear una autoridad de negocio local.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Pregunta y límites documentados</strong></p><p><strong>Given</strong> un flujo Mobile representativo y una incertidumbre delimitada</p><p><strong>When</strong> el equipo formula la pregunta de investigación</p><p><strong>Then</strong> registra el resultado esperado, los datos permitidos y las reglas de negocio que el componente no puede decidir.</p><p><strong>Scenario: Fuentes y alternativas comparadas</strong></p><p><strong>Given</strong> existe una pregunta de investigación</p><p><strong>When</strong> el equipo revisa documentación y al menos dos alternativas</p><p><strong>Then</strong> compara utilidad, exactitud, privacidad, coste, compatibilidad, accesibilidad, operabilidad y dependencia.</p><p><strong>Scenario: Experimento mínimo reproducible</strong></p><p><strong>Given</strong> datos sintéticos o no sensibles y criterios definidos</p><p><strong>When</strong> se ejecuta una PoC acotada</p><p><strong>Then</strong> se registran entorno, entradas, pasos, resultado observado y límites sin presentarla como aceptación de producto.</p><p><strong>Scenario: Fallo y aislamiento</strong></p><p><strong>Given</strong> la alternativa entrega una respuesta incompleta, errónea o no disponible</p><p><strong>When</strong> se prueba el flujo representativo</p><p><strong>Then</strong> el flujo conserva autoridad del servidor y registra el aislamiento o reversión técnica requerido.</p><p><strong>Scenario: Conclusión y backlog</strong></p><p><strong>Given</strong> termina la comparación y la PoC</p><p><strong>When</strong> el equipo revisa hallazgos y riesgos</p><p><strong>Then</strong> documenta adoptar, ajustar, diferir o rechazar y el refinamiento de backlog resultante.</p></td></tr>
</tbody>
</table>
*SPIKE-002 — Establecer tracks Mobile y límites de contratos*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-002</td><td>Developer</td><td>High</td><td>TECH-EPIC-02 — Platform baselines</td></tr>
<tr><th>Title</th><td colspan="3">Establecer tracks Mobile y límites de contratos</td></tr>
<tr><th colspan="4">Context / uncertainty</th></tr>
<tr><td colspan="4">Android nativo con Kotlin y Flutter/Dart forman los tracks definidos para la planificación académica. La incertidumbre trata sus baselines, paridad y límites de contrato; Flutter/Dart no se vuelve a seleccionar en este Spike.</td></tr>
<tr><th colspan="4">Research objective</th></tr>
<tr><td colspan="4">Documentar una matriz de versión y entorno, y contrastar un contrato representativo para identificar diferencias de plataforma sin duplicar reglas de negocio ni cambiar la autoridad del servidor.</td></tr>
<tr><th colspan="4">Spike Story</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo establecer el baseline y los límites de contrato para los tracks Mobile definidos, para registrar paridad, adaptaciones, restricciones e interoperabilidad entre Operations Mobile y Buyer Mobile.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Matriz de baseline</strong></p><p><strong>Given</strong> los dos tracks definidos</p><p><strong>When</strong> se prepara el experimento</p><p><strong>Then</strong> se documentan versiones, SDK, herramientas de build, entorno y restricciones de cada track.</p><p><strong>Scenario: Contrato representativo</strong></p><p><strong>Given</strong> un contrato permitido y sin reglas locales de negocio</p><p><strong>When</strong> ambos tracks lo consumen en una prueba mínima</p><p><strong>Then</strong> se registra la entrada, la respuesta, el manejo de error y la autoridad que permanece en el servidor.</p><p><strong>Scenario: Diferencia de plataforma</strong></p><p><strong>Given</strong> una diferencia de compatibilidad, ciclo de vida o capacidad</p><p><strong>When</strong> se compara la paridad</p><p><strong>Then</strong> se documenta la adaptación necesaria sin cambiar autorización, contrato ni semántica de negocio.</p><p><strong>Scenario: Restricción y riesgo</strong></p><p><strong>Given</strong> una dependencia, versión o comportamiento no compatible</p><p><strong>When</strong> se evalúa su impacto</p><p><strong>Then</strong> se registra el límite, el riesgo y una alternativa proporcional.</p><p><strong>Scenario: Decisión de investigación</strong></p><p><strong>Given</strong> concluye la matriz y la prueba de contrato</p><p><strong>When</strong> el equipo revisa la evidencia</p><p><strong>Then</strong> documenta el baseline, las diferencias, la decisión técnica y el refinamiento de backlog sin reabrir la selección del framework.</p></td></tr>
</tbody>
</table>

*SPIKE-003 — Delimitar identificadores de producto*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-003</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-03 — Device boundaries</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar identificadores de producto</td></tr>
<tr><th colspan="4">Context / uncertainty</th></tr>
<tr><td colspan="4">Sprint 1 delimita un slice mínimo de escaneo directo. Este Spike investiga una estrategia más amplia de identificadores: Barcode, QR, GS1, ambigüedad y alternativa manual, sin otorgar al dispositivo autoridad sobre inventario.</td></tr>
<tr><th colspan="4">Research objective</th></tr>
<tr><td colspan="4">Definir qué formatos y casos de identificador pueden resolverse mediante un contrato autoritativo, qué ambigüedades requieren selección o entrada manual y cuáles deben diferirse.</td></tr>
<tr><th colspan="4">Spike Story</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar formatos Barcode, QR y GS1, sus ambigüedades y una alternativa manual, para decidir qué identificación puede apoyar un flujo sin crear una decisión de inventario desde el dispositivo.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Fuentes y formatos revisados</strong></p><p><strong>Given</strong> documentación de formatos y casos representativos no sensibles</p><p><strong>When</strong> el equipo compara Barcode, QR y GS1</p><p><strong>Then</strong> documenta estructura, compatibilidad, límites y fuente de cada formato evaluado.</p><p><strong>Scenario: Resolución autoritativa</strong></p><p><strong>Given</strong> un identificador leído o ingresado</p><p><strong>When</strong> se consulta un contrato representativo</p><p><strong>Then</strong> el servidor resuelve la identidad permitida y el cliente no confirma recepción, picking ni inventario por sí solo.</p><p><strong>Scenario: Identificador ambiguo</strong></p><p><strong>Given</strong> un valor que corresponde a más de una posibilidad o carece de contexto</p><p><strong>When</strong> se evalúa la resolución</p><p><strong>Then</strong> se registra el conflicto y la alternativa autorizada sin seleccionar una entidad de forma silenciosa.</p><p><strong>Scenario: Cámara no disponible</strong></p><p><strong>Given</strong> la cámara no está disponible, se deniega el permiso o la lectura falla</p><p><strong>When</strong> se prueba el caso</p><p><strong>Then</strong> se ofrece una alternativa manual definida y se conserva el límite de autoridad.</p><p><strong>Scenario: Conclusión y consecuencia</strong></p><p><strong>Given</strong> terminan los casos de formato y fallo</p><p><strong>When</strong> el equipo contrasta criterios de precisión, operabilidad y seguridad</p><p><strong>Then</strong> documenta el formato adoptado, ajustado, diferido o rechazado y el cambio de backlog necesario.</p></td></tr>
</tbody>
</table>

*SPIKE-004 — Delimitar persistencia y recuperación local*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-004</td><td>Developer</td><td>High</td><td>TECH-EPIC-04 — Controlled continuity</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar persistencia y recuperación local</td></tr>
<tr><th colspan="4">Context / uncertainty</th></tr>
<tr><td colspan="4">No está definido qué datos pueden permanecer localmente, cuándo expiran ni cómo se recupera una operación interrumpida sin afirmar éxito de negocio antes de una confirmación autoritativa.</td></tr>
<tr><th colspan="4">Research objective</th></tr>
<tr><td colspan="4">Clasificar datos candidatos, evaluar protección, expiración y limpieza por contexto, y comprobar la recuperación de un resultado incierto mediante idempotencia o conflicto del servidor.</td></tr>
<tr><th colspan="4">Spike Story</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar caché segura, borrador, evidencia temporal y metadatos de reintento, para decidir qué puede persistir, expirar y recuperarse sin declarar éxito de negocio ante una red interrumpida.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Clasificación de datos</strong></p><p><strong>Given</strong> un dato candidato a persistencia local</p><p><strong>When</strong> el equipo lo clasifica</p><p><strong>Then</strong> registra sensibilidad, propósito, protección, expiración y prohibición de persistencia cuando corresponda.</p><p><strong>Scenario: Limpieza de contexto</strong></p><p><strong>Given</strong> cambia, expira o se revoca el contexto autorizado</p><p><strong>When</strong> se ejecuta la limpieza</p><p><strong>Then</strong> los datos locales protegidos se eliminan o vuelven inaccesibles según la clasificación documentada.</p><p><strong>Scenario: Red interrumpida</strong></p><p><strong>Given</strong> se interrumpe la red durante un envío</p><p><strong>When</strong> la aplicación recupera conectividad</p><p><strong>Then</strong> conserva un resultado incierto y no declara éxito local.</p><p><strong>Scenario: Idempotencia o conflicto</strong></p><p><strong>Given</strong> existe un resultado incierto de una operación</p><p><strong>When</strong> se reintenta o consulta el estado</p><p><strong>Then</strong> usa una llave idempotente o una respuesta de conflicto del servidor antes de actualizar el estado visible.</p><p><strong>Scenario: Límite y decisión</strong></p><p><strong>Given</strong> terminan las pruebas de persistencia y recuperación</p><p><strong>When</strong> el equipo revisa seguridad, privacidad y operabilidad</p><p><strong>Then</strong> documenta qué persiste, qué expira, qué se difiere y la decisión técnica con su consecuencia de backlog.</p></td></tr>
</tbody>
</table>

*SPIKE-005 — Delimitar notificaciones y deep links*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-005</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-05 — Quality and communication</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar notificaciones y deep links</td></tr>
<tr><th colspan="4">Context / uncertainty</th></tr>
<tr><td colspan="4">No está definido qué eventos justifican una notificación, cómo se solicitan permisos ni cómo un deep link puede abrir trabajo protegido sin exponer información sensible.</td></tr>
<tr><th colspan="4">Research objective</th></tr>
<tr><td colspan="4">Contrastar documentación de plataforma y eventos candidatos para definir permisos, contenido mínimo, expiración, revalidación de autorización y criterios de accesibilidad y comunicación.</td></tr>
<tr><th colspan="4">Spike Story</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar eventos, permisos, expiración y revalidación de deep links, para decidir qué comunicación contextual puede abrir trabajo protegido sin exponer datos ni mutar hechos de negocio.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Eventos y fuentes revisados</strong></p><p><strong>Given</strong> documentación de plataforma y eventos candidatos</p><p><strong>When</strong> el equipo compara su pertinencia</p><p><strong>Then</strong> documenta evento, audiencia, propósito, contenido mínimo y alternativa de comunicación accesible.</p><p><strong>Scenario: Permiso informado</strong></p><p><strong>Given</strong> una notificación requiere permiso de plataforma</p><p><strong>When</strong> se prueba la solicitud</p><p><strong>Then</strong> se registra el momento, la explicación y el comportamiento ante denegación sin bloquear trabajo autorizado.</p><p><strong>Scenario: Deep link autorizado</strong></p><p><strong>Given</strong> un enlace refiere a trabajo protegido</p><p><strong>When</strong> se intenta abrir</p><p><strong>Then</strong> se revalida Tenant, relación, permiso y vigencia antes de mostrar el destino.</p><p><strong>Scenario: Enlace vencido o alterado</strong></p><p><strong>Given</strong> un enlace vencido, alterado o sin permiso</p><p><strong>When</strong> se intenta abrir</p><p><strong>Then</strong> no expone datos sensibles y registra un resultado seguro para el usuario.</p><p><strong>Scenario: Conclusión de comunicación</strong></p><p><strong>Given</strong> terminan las pruebas de permisos, enlace y contenido</p><p><strong>When</strong> el equipo revisa riesgos de privacidad, accesibilidad y dependencia</p><p><strong>Then</strong> documenta adoptar, ajustar, diferir o rechazar y el refinamiento de backlog correspondiente.</p></td></tr>
</tbody>
</table>

*SPIKE-006 — Delimitar mapas y ubicación*

<table>
<thead><tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr></thead>
<tbody>
<tr><td>SPIKE-006</td><td>Developer</td><td>Medium</td><td>TECH-EPIC-03 — Device boundaries</td></tr>
<tr><th>Title</th><td colspan="3">Delimitar mapas y ubicación</td></tr>
<tr><th colspan="4">Context / uncertainty</th></tr>
<tr><td colspan="4">No está definido si la navegación externa aporta valor suficiente para un destino autorizado, qué datos comparte el dispositivo ni cómo se maneja una denegación o falla sin introducir tracking continuo o ETA.</td></tr>
<tr><th colspan="4">Research objective</th></tr>
<tr><td colspan="4">Revisar documentación de proveedor y plataforma, y evaluar una navegación externa mínima para delimitar destino, permisos, privacidad, retención y comportamiento ante falla.</td></tr>
<tr><th colspan="4">Spike Story</th></tr>
<tr><td colspan="4">Como <strong>Developer</strong>, deseo delimitar destino autorizado, permiso, retención y alternativa ante falla para navegación externa, para decidir si aporta valor sin introducir tracking continuo, ETA ni autoridad de ubicación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Documentación y proveedor revisados</strong></p><p><strong>Given</strong> una alternativa de navegación externa</p><p><strong>When</strong> el equipo revisa su documentación de plataforma y proveedor</p><p><strong>Then</strong> registra compatibilidad, permisos, datos compartidos, retención y dependencias relevantes.</p><p><strong>Scenario: Destino autorizado</strong></p><p><strong>Given</strong> un destino permitido de prueba</p><p><strong>When</strong> se solicita navegación externa</p><p><strong>Then</strong> se comparte sólo el dato necesario y no se modifica Delivery ni se infiere una llegada.</p><p><strong>Scenario: Permiso denegado</strong></p><p><strong>Given</strong> el permiso de ubicación se deniega o no está disponible</p><p><strong>When</strong> se solicita navegación</p><p><strong>Then</strong> se presenta una alternativa definida sin recopilar ubicación adicional.</p><p><strong>Scenario: Falla de navegación</strong></p><p><strong>Given</strong> la aplicación externa falla, no está instalada o no acepta el destino</p><p><strong>When</strong> se intenta el handoff</p><p><strong>Then</strong> el usuario conserva el contexto autorizado y recibe un resultado que no afirma seguimiento ni ETA.</p><p><strong>Scenario: Privacidad y decisión</strong></p><p><strong>Given</strong> termina el experimento mínimo</p><p><strong>When</strong> el equipo contrasta valor, privacidad, accesibilidad y dependencia</p><p><strong>Then</strong> documenta la conclusión técnica, el límite explícito de no tracking continuo y la consecuencia de backlog.</p></td></tr>
</tbody>
</table>
