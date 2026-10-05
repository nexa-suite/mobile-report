# Conclusiones

El informe reúne la investigación del problema y los avances de implementación
de Nexa Mobile. AV1 permitió delimitar usuarios, tareas, supuestos e hipótesis;
TB1 aporta componentes publicados y comprobaciones técnicas. El efecto de la
solución sobre el trabajo de los usuarios requiere una evaluación propia.

## Problem Statement

El Problem Statement se sostiene como una pregunta de ingeniería pertinente:
cuando un pedido cambia de responsabilidad, la continuidad de información puede
debilitarse entre Warehouse & Dispatch, Driver y Buyer. Las entrevistas aportan
evidencia concreta de fricciones de coordinación y continuidad en esos tres
segmentos. Esta evidencia no permite estimar incidencia de mercado ni magnitud
económica para todas las empresas compatibles con Nexa.

La investigación también confirma la necesidad de conservar perspectivas
diferentes durante la entrega. El resultado registrado por Driver, el Buyer
Receipt, el Proof of Delivery y una Discrepancy no son intercambiables; cada uno
requiere contexto y responsabilidad propios.

## Contraste de las Lean UX Assumptions

*Contraste por familia de assumptions y evidencia disponible en AV1*

| Familia de assumptions | Evidencia de AV1 | Conclusión |
| --- | --- | --- |
| **Business Assumptions BA1–BA6** | El contexto sectorial y las entrevistas respaldan la relevancia del problema de coordinación y continuidad. | La relevancia del problema recibe sustento; monetización, adopción, sustitución de herramientas y disposición de pago no se establecen mediante Needfinding. |
| **Business Outcome Assumptions BOA1–BOA4** | AV1 define resultados de negocio observables y su relación con el problema. | Permanecen como proposiciones medibles; AV1 no midió el efecto de una feature sobre esos resultados. |
| **User Assumptions UA1–UA6** | La comprensión de Warehouse y Driver recibe soporte de investigación; Buyer se amplía desde una mirada centrada en recepción hacia reabastecimiento, puntualidad y continuidad comercial. | Los segmentos y responsabilidades se refinan sin convertir una muestra en representación universal. |
| **User Outcome & Benefit Assumptions UOBA1–UOBA6** | La investigación evidencia la importancia de claridad, continuidad, manejo de excepciones y coordinación. | El valor de una solución sobre esos outcomes requiere observación comparativa con una línea base. |
| **Feature Assumptions FA1–FA3** | Las features se mantienen vinculadas a problemas, actores y resultados esperados. | FA1, FA2 y FA3 continúan siendo hipótesis de valor de solución, no efectos demostrados. |

## Contraste de H1, H2 y H3

*Contraste acumulativo de las hypotheses en AV1 y TB1*

| Hypothesis | Qué aportó AV1 | Evidencia de TB1 | Alcance de la conclusión |
| --- | --- | --- | --- |
| **H1 — Warehouse & Dispatch Operations** | Aportó comprensión de verificación, continuidad entre preparación, alistamiento y transferencia operativa, y de las responsabilidades distintas de Warehouse y Dispatch. | Los recorridos de Warehouse documentan acceso, consulta e identificación y sus alternativas; la secuencia HP-03 muestra permiso de cámara, cámara abierta e identificación confirmada de producto. | El problema que da origen a FA1 recibe soporte y refinamiento; el efecto de FA1 sigue sin medición comparativa. |
| **H2 — Driver Delivery Execution** | Aportó evidencia sobre incidencias, comunicación, evidencia de entrega y restricciones móviles durante Delivery Attempts. | El diseño conserva rutas normales y excepciones de entrega. Este corte no aporta mediciones comparativas del desempeño de Driver. | El problema de continuidad y atribución durante la entrega recibe soporte; el efecto de FA2 sigue sin medición comparativa. |
| **H3 — B2B Buyers** | Amplió la comprensión de Buyer hacia reabastecimiento, continuidad comercial, puntualidad y coordinación con proveedores. Receipt y Discrepancy conservan relevancia, pero representan un subescenario más acotado. | Los recorridos de Buyer describen recepción y discrepancias como diseño; Buyer Mobile no se presenta como una aplicación publicada. | El problema que orienta FA3 se vuelve más preciso; el efecto de FA3 sigue sin medición comparativa. |

## Criterios de éxito definidos

Impact Mapping establece criterios de éxito para contrastar la solución con una
línea base comparable. AV1 estableció comprensión de problema y usuarios, pero
no ejecutó las mediciones controladas necesarias para comparar esos criterios.

*Criterios definidos para la evaluación de solución*

| Business Goal | Criterios definidos | Interpretación en AV1 |
| --- | --- | --- |
| **Goal 1 — Warehouse & Dispatch** | Reducir al menos **30 %** el esfuerzo de reconstrucción de contexto y lograr al menos **80 %** de escenarios correctos de identificación de producto, lote, cantidad y condición. | Son criterios para el experimento de solución correspondiente; AV1 no los mide como resultados alcanzados. |
| **Goal 2 — Driver** | Lograr al menos **85 %** de Delivery Attempts con asociación correcta entre Delivery, Attempt, resultado y evidencia, y reducir al menos **30 %** la reconstrucción o aclaración posterior. | Son criterios para contrastar la solución con una línea base; AV1 no los mide como resultados alcanzados. |
| **Goal 3 — Buyer** | Lograr al menos **80 %** de escenarios Buyer con contexto suficiente y reducir al menos **30 %** las aclaraciones manuales ante demora, excepción o diferencia. | Son criterios para el experimento de solución correspondiente; AV1 no los mide como resultados alcanzados. |

## Implicancias de ingeniería y producto

DDD estratégico, C4 y los modelos tácticos son artefactos de diseño y
arquitectura que organizan responsabilidades, contratos y límites de la
solución. El Product Backlog conserva trazabilidad de requisitos y planificación;
Jira conserva trazabilidad de backlog y Sprint; Needfinding conserva evidencia
de investigación sobre usuarios, problemas y tareas. Cada tipo de artefacto
aporta una clase de evidencia distinta.

La existencia o el estado de un Product Backlog o Sprint Backlog no constituye,
por sí solo, evidencia de implementación. Los incrementos técnicos se sustentan
independientemente mediante su evidencia de implementación y verificación
correspondiente. Esta separación evita atribuir ejecución, calidad o aceptación
de producto a la sola planificación.

La evidencia también recomienda conservar explícitamente los límites entre
Driver Outcome, Buyer Receipt, Proof of Delivery y Discrepancy. Las decisiones
de diseño, contratos y futuras pruebas deben preservar esa separación para no
convertir un hecho operativo en una aceptación comercial o de recepción.

## Implementación y validación de TB1

TB1 corresponde a la segunda entrega académica; los registros de Sprint conservan sus propios periodos de ejecución. Este corte aporta una aplicación Android publicada, servicios desplegados en
Render, una base de datos administrada en Neon y la configuración SMTP de Brevo. La aplicación Operations
Mobile puede instalarse desde su publicación y consultar el servicio mediante
HTTPS. La comprobación en Samsung S22 cubrió instalación e inicio de sesión;
las pruebas automatizadas complementan esa evidencia sin sustituir la
observación de los recorridos completos por cada perfil.

El catálogo de ICISA contiene 102 productos con imágenes y precios. Las
consultas autorizadas distinguen el catálogo interno de la selección comercial
visible para compradores. Esa diferencia conserva los permisos y evita
exponer información por el solo hecho de disponer de una cuenta.

El Website está publicado en GitHub Pages. Su diseño comunica el ámbito de
Nexa y organiza la información del producto. La disponibilidad de la página
permite revisar el contenido publicado. Las capturas del 5 de octubre muestran adaptación en escritorio y móvil, sin desbordamiento horizontal en la vista de 390 píxeles. Los resultados con usuarios requieren una evaluación propia.

El Sprint Backlog presenta 71 elementos y 317 puntos registrados en Jira,
separados de los 36 elementos y 144 puntos de la planificación inicial. El
estado de las incidencias documenta seguimiento del trabajo; los resultados
funcionales se sustentan con las comprobaciones de implementación y las
validaciones correspondientes.

La evidencia reunida acredita publicación y comprobación técnica de los
componentes disponibles. Las secuencias HP-01, HP-02 y HP-03 complementan esta evidencia con sesión, búsqueda manual y permiso/cámara/identificación de producto. La evaluación comparativa de los flujos por perfil y las sesiones con usuarios se conserva como una etapa distinta. Buyer Mobile mantiene su alcance de
diseño y no se presenta como una aplicación publicada.

**Mejora continua de AV1 a TB1**

La comparación con el checkpoint AV1 v1.0.1 permite identificar tres mejoras documentadas. Las observaciones corresponden a la revisión de los artefactos, sin atribuir retroalimentación a participantes o al docente.

| Mejora | Situación anterior y observación | Cambio aplicado | Resultado y evidencia |
| --- | --- | --- | --- |
| Trazabilidad de Sprint 2 | AV1 presentaba 36 elementos y 144 puntos planificados sin tablero o tickets evidenciados. Jira mostró posteriormente 71 elementos y 317 puntos. | Se incorporaron claves NX, responsables, estados, jerarquía y comparación con la planificación. | La variación de +35 elementos y +173 puntos se conserva en 4.2.2.3 y en NX-296, registrada el 5 de octubre, sin alterar la planificación histórica. |
| Claridad visual del diseño | AV1 no incluía las imágenes actuales del capítulo III; las descripciones no permitían inspeccionar las composiciones y recorridos. | Se incorporaron wireframes y mock-ups de Landing, referencias de estilo y recorridos móviles. | Los apartados 3.1.3 y 3.1.4 permiten examinar los artefactos visuales, distinguiendo diseño de validación con usuarios. |
| Evidencia de ejecución | AV1 no contenía las capturas actuales del capítulo IV; las descripciones de configuración no mostraban por sí solas los estados ejecutados. | Se añadieron evidencias de publicación, documentación de servicios, instalación y recorridos Android con leyendas sobre lo observado. | Las secciones 4.2.2.6–4.2.2.8 relacionan las afirmaciones con capturas y resultados concretos, conservando las fechas y límites de cada comprobación. |

## Recomendaciones

- Usar el As-Is documentado como línea base de comparación para experimentos de
  solución de bajo costo.
- Evaluar FA1, FA2 y FA3 frente a sus outcomes observables y a los criterios
  definidos en Impact Mapping.
- Mantener separados Driver Outcome, Buyer Receipt, Proof of Delivery y
  Discrepancy en requisitos, diseño, evidencia y cualquier incremento técnico.
- Refinar el Product Backlog cuando nueva evidencia cambie una prioridad, sin
  reescribir retrospectivamente los registros históricos de cada Sprint.
- Recopilar evidencia de implementación y usabilidad de forma independiente de
  la planificación, los modelos y el reporte.
- Contrastar las assumptions de adopción y monetización con evidencia adecuada
  antes de convertirlas en decisiones de producto o alcance.
- Mantener el registro de variaciones de alcance con su fecha, impacto y relación con la planificación original.
- Comprobar la disponibilidad del servicio antes de cada sesión y registrar
  los resultados de conexión y recuperación ante interrupciones.
- Ejecutar recorridos autenticados por rol en Android y registrar la evaluación
  de producto por separado de las pruebas automatizadas.
- Completar en el Website los destinos de contacto y redes sociales.
