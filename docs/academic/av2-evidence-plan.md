# Plan de evidencia para AV2 — Sprint 2

Corte documental: 2 de octubre de 2026. Este plan organiza evidencia pendiente frente a la rúbrica V4.0 de AV2. Describe acciones para sustentar los criterios; no asigna una nota ni garantiza una calificación. La evaluación de producto y la evaluación ABET son matrices distintas, cada una sobre 20 puntos.

## Criterios de producto y entrega

| Criterio AV2 | Puntaje máximo | Evidencia disponible | Acción pendiente |
| --- | ---: | --- | --- |
| Sprint backlog | 2 | Plan de 36 elementos y 144 puntos; matriz de liderazgo y cambios atribuibles. | Vincular tareas con tickets y Board reales, estados observados, responsables y resultados; conservar evidencia de priorización y aceptación. |
| Landing Page pública y responsive | 1 | Website local y páginas de alcance. | Corregir destinos, traducción y contenido pendiente; demostrar URL pública, responsive, propósito, capturas/video de app, pitch, CTA, contacto y redes visibles, colaboración GitFlow y videos preliminares de producto/equipo. |
| REST API desplegada y documentada | 2 | Contratos, implementación y pruebas automatizadas; API local. | Demostrar despliegue público y 100 % de endpoints del alcance; seguridad por token, OpenAPI con descripciones y ejemplos completos, comportamiento y trazabilidad de código/GitFlow. |
| Aplicación móvil integrada en dispositivo físico | 4.5 | APK, integración local con API y pruebas en emuladores; capturas de recorridos observados. | Ejecutar tareas prioritarias completas en dispositivo físico; demostrar Material Design, conformidad con User Flows/backlog, convenciones y organización de código/recursos, colaboración GitFlow y aceptación de historias requeridas. |
| Proceso colaborativo | 2.5 | Liderazgo planificado y autoría verificable. | Incorporar registros reales de planning, review, retrospectiva, asistencia y decisiones; completar reportes individuales. |
| Entrevistas grabadas de validación de app y Landing Page | 1.5 | No hay evidencia de esta actividad en el corte. | Realizar sesiones grabadas con al menos tres usuarios por segmento, tareas de persona/user goal sin enseñar la interfaz; vincular hallazgos a sesión, descripción, heurística, severidad y propuesta de corrección. |
| About the Product | 1 | Página de producto pendiente de contenido aprobado. | Grabar propósito, beneficios, funciones y demostración; al menos un testimonio por persona, 50 % de contenido editado, escenas y participantes descritos, música/marca, captura, URL e incrustación. |
| About the Team | 1 | Perfiles del equipo; página pública pendiente. | Grabar trabajo real y narración, actividades y autoevaluación de cada integrante; al menos 50 % editado, escenas/participantes descritos, música/marca, captura, URL e incrustación. |
| Mejora continua | 2 | Correcciones técnicas y trazabilidad de versiones. | Vincular feedback real de TB1 y validaciones con cambios concretos y resultados; no sustituirlo por una lista de commits. |
| Comunicación | 2.5 | Informe estructurado con fuentes y límites de evidencia. | Revisar coherencia, lenguaje, APA 7 y exposición; entregar informe PDF, presentación PPTX/PDF, participación DOCX/PDF, artefactos ZIP y exposición MP4. |
| **Total** | **20** | | |

Las cinco primeras historias de la priorización registrada son `MOB-US-004`, `MOB-US-013`, `MOB-US-016`, `MOB-US-017` y `MOB-US-022`. Debe registrarse evidencia de sus criterios de aceptación y no deducir su aceptación de que exista una pantalla o una prueba técnica.

## Capítulo III: capturas, userflows y wireflows

No se han evidenciado wireframes, mockups o prototipos visuales con enlaces de revisión de Figma en este corte. Diagramas Mermaid y capturas de ejecución no acreditan por sí solos un prototipo diseñado ni su conformidad. Los diagramas deben distinguir la tarea diseñada del recorrido ejecutado. Cada captura debe identificar rol, pantalla, paso y resultado, con datos de demostración autorizados. Se debe proteger información personal y credenciales antes de publicar imágenes.

| Rol o superficie | Evidencia ya registrada | Recorrido y capturas que deben completarse |
| --- | --- | --- |
| Warehouse | Selección de SKU, recepción de 1.25 unidades y stock retornado. | Acceso y selección de contexto; lote/stock; recepción y resultado; preparación; excepción térmica, evidencia, HOLD y disposición autorizada cuando exista una carga adecuada. |
| Sales | Pantalla inicial y formulario vacío. | Producto seleccionado, solicitud comercial completa, envío y resultado autoritativo; relación con Buyer autorizado. |
| Logistics / Dispatch | Entrada y consulta sin carga operativa completa. | Preparación READY, planificación de ventana cuando falte, evaluación de agrupación, bloqueos conocidos, asignación y handoff; resultado visible de cada paso. |
| Driver | Sin cuenta y entrega asignada demostradas en el corte. | Sesión autorizada, inicio y cierre de jornada, captura de ubicación sólo durante jornada, entrega asignada, intento y resultado; incidencia/HOLD cuando corresponda y prohibición de disposición no autorizada. |
| BOM | Inicio y lista vacía de excepciones. | Excepción real de demostración, asignación, seguimiento y cierre tras resolución válida; rechazo de acciones fuera de sus capacidades. |
| Owner / administración | Cuenta local disponible. | Selección de contexto, gestión autorizada de equipo y permisos; confirmar que las capacidades otorgadas coinciden con el rol operativo previsto. |
| Buyer | Cuenta Portal disponible; no es un cliente de Operations Mobile. | Validar relación con proveedor y límites de lectura por API/Portal; no presentar un recorrido Buyer como pantalla de la aplicación Operations. |
| Website | Inicio, menú, cambio de idioma, página de producto pendiente, Platform y FAQ. | Inicio, solución, producto/equipo completos y FAQ tras corregir destinos; capturas responsive del sitio que realmente se publique. |

Los 12 archivos de captura registrados permiten ilustrar recorridos parciales de Warehouse, Sales, Logistics y BOM. No prueban una venta completa, una entrega terminada, coordinación de una excepción con datos ni aceptación de usuarios. Los wireflows deben incluir salidas de error, permisos insuficientes y recuperación cuando esos estados se hayan observado.

## Capítulo IV: evidencia del Sprint 2

1. Conectar Sprint backlog, Board y tickets reales con tareas y resultados. Mantener diferenciados lo planificado, implementado, verificado y aceptado.
2. Incorporar resultados técnicos con versión, comando, cantidades de pruebas, fallos y omisiones. Separar pruebas automáticas de recorridos con servicios reales y de aceptación de usuarios.
3. Registrar instalación y tareas completas en dispositivo físico. Una instalación desde Android Studio y una ejecución en emulador no satisfacen por sí solas ese requisito.
4. Completar evidencia de despliegue autorizado con URL, versión y comprobaciones del entorno publicado. Un servicio en localhost no prueba publicación.
5. Registrar entrevistas de validación, observaciones y recomendaciones; relacionar cada mejora con la evidencia que la originó.
6. Completar review y retrospectiva con participantes y decisiones reales. La firma de un commit no acredita una ceremonia ni aprendizaje individual.
7. Sustentar la Learning Feature con investigación y resultados observables: cuatro artículos Q1/Q2 de los últimos dos años (dos de dominio y dos de tecnologías/técnicas móviles), citados en APA 7, método, alternativa evaluada y aplicación al proyecto. No atribuir un Spike o benchmark sólo por existir pruebas.

## Student Outcome 7

| Criterio ABET | Puntaje máximo | Evidencia reunida | Sustentación pendiente |
| --- | ---: | --- | --- |
| 7.c1: adquirir y aplicar conocimientos | 10 | Aportes atribuibles, dos dominios de aplicación, fortalezas y limitaciones; método de comprobación reproducible. | Reflexión revisada por cada integrante: conocimiento nuevo, estrategia de aprendizaje, alternativa evaluada y resultado propio; Individual Member Performance Report y evidencia de investigación. |
| 7.c2: aprendizaje permanente | 10 | Intereses profesionales y objetivos SMART con horas, productos y plazos de 12, 18 o 24 meses. | Confirmación personal y seguimiento del plan. La guía propone objetivos trimestrales, certificación, bibliografía y comunidades como ampliación de evidencia; su exigibilidad debe distinguirse de la matriz oficial. |
| **Total** | **20** | | |

La actualización AV2 del Student Outcome se mantiene en `feature/front-matter`. Los intereses y metas previos se conservan; no se presentan certificaciones como obtenidas ni se infieren reflexiones personales a partir de autoría de código.

## Orden de cierre

Primero resolver cualquier defecto reproducible y conservar pruebas técnicas. Después completar recorridos con datos y dispositivo físico. A continuación registrar validación con usuarios, feedback y mejoras. Finalmente consolidar evidencia de despliegue, ceremonias, sustentación individual y presentación. Las actividades humanas y la publicación requieren su evidencia propia; no pueden completarse mediante reconstrucciones ficticias.
