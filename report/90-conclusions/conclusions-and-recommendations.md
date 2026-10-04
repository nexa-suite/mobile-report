# Conclusiones

La evidencia reunida en AV1 permite sintetizar el problema, los supuestos y las
hipótesis de Nexa Mobile sin confundir investigación, planificación, diseño e
implementación. La investigación delimita problemas y contextos de trabajo; el
efecto de una solución requiere un experimento de solución independiente.

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

*Alcance de las hypotheses a partir de AV1*

| Hypothesis | Qué aportó AV1 | Alcance de la conclusión |
| --- | --- | --- |
| **H1 — Warehouse & Dispatch Operations** | Aportó comprensión de verificación, continuidad entre preparación, alistamiento y transferencia operativa, y de las responsabilidades distintas de Warehouse y Dispatch. | El problema que da origen a FA1 recibe soporte y refinamiento; el efecto de FA1 no fue medido. |
| **H2 — Driver Delivery Execution** | Aportó evidencia sobre incidencias, comunicación, evidencia de entrega y restricciones móviles durante Delivery Attempts. | El problema de continuidad y atribución durante la entrega recibe soporte; el efecto de FA2 no fue medido. |
| **H3 — B2B Buyers** | Amplió la comprensión de Buyer hacia reabastecimiento, continuidad comercial, puntualidad y coordinación con proveedores. Receipt y Discrepancy conservan relevancia, pero representan un subescenario más acotado. | El problema que orienta FA3 se vuelve más preciso; el efecto de FA3 no fue medido. |

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

## Implementación y validación de AV2

El Sprint 2 aporta una aplicación Android publicada, servicios disponibles en
Render y una base de datos administrada en Neon. La aplicación Operations
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
permite revisar el contenido publicado; su evaluación adaptable y los
resultados con usuarios requieren evidencia específica.

El Sprint Backlog presenta 71 elementos y 317 puntos registrados en Jira,
separados de los 36 elementos y 144 puntos de la planificación inicial. El
estado de las incidencias documenta seguimiento del trabajo; los resultados
funcionales se sustentan con las comprobaciones de implementación y las
validaciones correspondientes.

La evidencia reunida acredita publicación y comprobación técnica de los
componentes disponibles. Permanecen por completar la evaluación de cámara y
lectura de códigos en los recorridos de trabajo, la validación de los flujos
por perfil y las sesiones con usuarios. Buyer Mobile mantiene su alcance de
diseño y no se presenta como una aplicación publicada.

## Recomendaciones

- Usar el As-Is documentado como línea base de comparación para experimentos de
  solución de bajo costo.
- Evaluar FA1, FA2 y FA3 frente a sus outcomes observables y a los criterios
  definidos en Impact Mapping.
- Mantener separados Driver Outcome, Buyer Receipt, Proof of Delivery y
  Discrepancy en requisitos, diseño, evidencia y cualquier incremento técnico.
- Refinar el Product Backlog cuando nueva evidencia cambie una prioridad, sin
  reescribir retrospectivamente el historial de Sprint completado.
- Recopilar evidencia de implementación y usabilidad de forma independiente de
  la planificación, los modelos y el reporte.
- Contrastar las assumptions de adopción y monetización con evidencia adecuada
  antes de convertirlas en decisiones de producto o alcance.
- Resolver la diferencia entre la planificación de Sprint 2 y el tablero
  observado antes de presentar un compromiso actualizado.
- Comprobar la disponibilidad del servicio antes de cada sesión y registrar
  los resultados de conexión y recuperación ante interrupciones.
- Ejecutar recorridos autenticados por rol en Android y registrar la evaluación
  de producto por separado de las pruebas automatizadas.
- Completar en el Website los destinos de contacto y redes sociales, además de
  la evidencia audiovisual exigida por la rúbrica.
