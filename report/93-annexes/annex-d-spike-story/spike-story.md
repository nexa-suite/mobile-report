## Annex D: Spike Stories

Este anexo amplía los seis Spike Stories de la sección 2.4.1. Cada Spike
investiga una incertidumbre concreta y define el material que permite cerrarla.
No representa una decisión o resultado que todavía no haya sido producido.

**Estado de evidencia:** los seis Spikes están planificados y sus resultados,
benchmarks, prototipos y decisiones de selección son **NOT YET DUE** hasta el
hito de Sprint que corresponda.

## SPIKE-001 — Oportunidad de aprendizaje autónomo

| Campo | Definición |
| :--- | :--- |
| Objective | Investigar, seleccionar e integrar de forma acotada una feature obligatoria de aprendizaje autónomo que aporte valor a una actividad móvil de Nexa. |
| Question | ¿Qué feature, resultado observable, datos, límites de privacidad y mecanismo de revisión requiere la oportunidad? |
| Expected artifact | Matriz de alternativas y fuentes, clasificación de datos, riesgos de privacidad, factibilidad, PoC reproducible y punto de integración documentado. |
| Completion criteria | Selección justificada, límite de integración, contrato, fallos, observabilidad y reversión documentados, con separación entre observación, sugerencia y decisión de negocio. |
| Scope | La oportunidad no puede confirmar inventario, crédito, pago, compromiso, entrega o recepción por sí sola. |

## SPIKE-002 — Bases compartidas y paridad funcional

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar bases compartidas para Nexa Operations Mobile y Nexa Buyer Mobile. |
| Question | ¿Cómo pueden Kotlin nativo junto con Flutter/Dart, o Kotlin Multiplatform (KMP), sostener contratos compartidos, estado local seguro, distribución y paridad funcional entre las dos aplicaciones sin presumir una selección? |
| Expected artifact | Matriz de flujos, seguridad, contrato, estado local, pruebas, distribución y mantenimiento, acompañada por una prueba acotada de un flujo común. |
| Completion criteria | Trade-offs, límites, responsabilidades compartidas y diferencias permitidas de plataforma documentados. Ninguna alternativa queda seleccionada o canónica sin evidencia y autoridad explícitas. |
| Scope | Las tecnologías se evalúan como alternativas de implementación; ninguna crea un Bounded Context ni sustituye la autoridad del servidor. |

## SPIKE-003 — Identificadores de producto

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar el alcance de Barcode, QR, GS1 y la alternativa manual para producto, paquete y ubicación. |
| Question | ¿Qué formatos, permisos, ambigüedades, expiración, reutilización y validaciones del servidor hacen confiable una identificación? |
| Expected artifact | Comparación de formatos, reglas de identificación, límites de seguridad y prueba controlada en dispositivo. |
| Completion criteria | Alcance, alternativa manual, errores esperados y preguntas de integración documentados sin atribuir autoridad al dispositivo. |
| Scope | Identificar no equivale a recibir, reservar, mover o consumir stock. |

## SPIKE-004 — Persistencia y recuperación local

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar qué información puede conservarse localmente y cómo recuperar cambios después de una interrupción. |
| Question | ¿Cómo se clasifican, protegen, reintentan y reconcilian caché, borradores, evidencia temporal y metadatos de reintento? |
| Expected artifact | Clasificación de datos, modelo de protección, secuencia de sincronización, política de conflictos y prueba de recuperación. |
| Completion criteria | Límite offline seguro documentado; los hechos de negocio dependen de confirmación autoritativa del servidor. |
| Scope | No se considera válida una confirmación local de inventario, compromiso, crédito, pago, entrega o recepción. |

## SPIKE-005 — Notificaciones y deep links

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar usos autorizados de notificaciones push y deep links para contextos móviles válidos. |
| Question | ¿Qué eventos pueden iniciar una notificación, cómo se comprueban Tenant y permisos, y cómo expiran o se repiten los enlaces? |
| Expected artifact | Matriz de evento, canal, permiso, ámbito, expiración, reintento y destino permitido. |
| Completion criteria | Reglas de navegación y seguridad documentadas; la notificación sólo orienta y no cambia por sí sola el estado de negocio. |
| Scope | La navegación iniciada por una notificación siempre vuelve a consultar información autorizada. |

## SPIKE-006 — Mapas y ubicación

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar el uso móvil de mapas y ubicación respetando privacidad, batería y conectividad. |
| Question | ¿Qué destino, permiso, observación del dispositivo, alternativa y límite de retención son necesarios para apoyar una entrega? |
| Expected artifact | Comparación de navegación externa, permisos, consumo, conectividad y alternativas de operación. |
| Completion criteria | Límite mínimo documentado; el alcance inicial permanece en navegación externa autorizada y no en seguimiento continuo. |
| Scope | No se deriva ETA, ubicación continua o autoridad de entrega a partir de una apertura de navegación. |

## Relación con la especificación

Los seis registros resumidos forman el catálogo de Spike Stories. Sus preguntas se relacionan con las historias `MOB-US` correspondientes, pero no agregan historias funcionales ni Bounded Contexts.

## Ruta de trazabilidad para requisitos posteriores del curso

La siguiente ruta prepara decisiones y evidencia futura sin presentar una
capacidad como completada. Cada requisito conserva la autoridad de los once
Bounded Contexts y requiere su propio artefacto verificable antes de declararse
implementado o validado.

| Requisito posterior | Punto de decisión y Product Backlog relacionado | Evidencia necesaria para comunicar avance |
| --- | --- | --- |
| Mobile nativo: Kotlin | `TS-MOB-002` define la restricción académica; los flujos operativos de Sprint 2 dan el siguiente corte funcional. No equivale a una selección de framework. | Build identificable, contrato consumido, prueba en emulador o dispositivo y resultados observados. |
| Multi-plataforma: Flutter/Dart o Kotlin Multiplatform (KMP) | `SPIKE-002` compara alternativas para paridad con el corte nativo. Ninguna se presupone aceptada. | Decisión documentada, proyecto reproducible, flujo equivalente y límites de paridad. |
| Local storage no autoritativo | `SPIKE-004` y `TS-MOB-005` delimitan caché, borradores, recuperación y protección. | Clasificación de datos, prueba de interrupción/recuperación y confirmación posterior del servidor. |
| Recurso de dispositivo | `SPIKE-003`, `TS-MOB-007` y `MOB-US-011..012` delimitan cámara, identificadores y entrada manual. | Permiso, alternativa manual, prueba controlada y contrato autorizado. |
| Servicio REST interno | `TS-MOB-001` conecta los clientes con Nexa API. | Contrato REST/OpenAPI, manejo de Problem Details, idempotencia y prueba de integración. |
| Servicio de terceros | `SPIKE-006` y `TS-MOB-008` evalúan navegación y geolocalización para entrega. | Comparación de proveedores, revisión de privacidad/costo, aceptación técnica y prueba reproducible. |
| Feature de aprendizaje autónomo | `SPIKE-001` se planifica en Sprint 2 e incluye investigación, selección e integración acotada de la feature obligatoria. | Alternativas, criterios, PoC reproducible, punto de integración, límites, reversión y evidencia disponible. |
| Dispositivo físico y distribución | `TS-MOB-012` prepara evidencia técnica de build, instalación y dispositivo. Firebase App Distribution sólo se evalúa como canal posible después de contar con cuenta, política y configuración aceptadas. | Build firmado o identificable, dispositivo físico, flujo observado, canal de distribución y resultado registrado. |
| Landing Page estática | `LAND-US-001..006` forman el corte de entrada pública de Sprint 2. | Artefacto HTML5/CSS3/JavaScript identificable, revisión de enlaces legales y comportamiento responsive observado. |
| Internacionalización y accesibilidad | `TS-MOB-010` cubre i18n y accesibilidad para clientes Mobile; la Landing aplica sus equivalentes web. | Recursos `en_US` y `es_419`, revisión de foco/contraste/tamaño táctil y, para web, semántica y ARIA. |
| Ética y comunicación legal | `LAND-US-004` organiza información comercial, preguntas frecuentes y enlaces legales. | Términos, condiciones y referencias éticas revisadas en el artefacto correspondiente. |
| Videos de exposición | [Anexo H: Videos de Exposiciones](../annex-h-videos-de-exposiciones.md) registra el estado de la evidencia audiovisual. | Archivo o enlace autorizado, descripción, fecha, duración y evidencia de la entrega correspondiente. |
