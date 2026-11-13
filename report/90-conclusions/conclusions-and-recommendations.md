# Conclusiones

El desarrollo de Nexa Mobile ha evolucionado desde la investigación de necesidades y la definición de requisitos hasta la implementación progresiva de sus aplicaciones y la recopilación de evidencias técnicas y de validación. Durante AV1 se establecieron las bases del problema, los segmentos objetivo y las hipótesis de solución. En TB1 se documentaron los avances de Sprint 2, las interfaces y los primeros recorridos de ejecución. Finalmente, AV2 amplió la documentación de diseño, incorporó las evidencias de Sprint 3 y registró una primera entrevista de validación.

Los resultados muestran avances en la construcción de Nexa Operations Mobile y Nexa Buyer Mobile, así como en la integración de componentes y la documentación de servicios. Sin embargo, la implementación y las comprobaciones técnicas deben distinguirse de la aceptación funcional y de los resultados obtenidos con usuarios. El proyecto mantiene pendientes las verificaciones necesarias para demostrar el cumplimiento integral de los recorridos y de los objetivos definidos en Lean UX.

## Problem Statement

El Problem Statement de Nexa conserva su relevancia a partir de las necesidades identificadas durante Needfinding. Las entrevistas de AV1 permitieron reconocer dificultades relacionadas con la continuidad de información, la coordinación de responsabilidades y el tratamiento de situaciones excepcionales durante las operaciones de almacén, distribución y recepción de mercadería.

La investigación también permitió identificar necesidades particulares de los tres segmentos objetivo: Warehouse & Dispatch Operations, Driver Delivery Execution y B2B Buyers. Aunque sus actividades forman parte de un mismo proceso comercial y logístico, cada segmento requiere información y acciones diferentes.

Los avances posteriores refuerzan la importancia de conservar estos límites. El resultado de un intento de entrega, la evidencia de entrega, la recepción del comprador y el registro de una discrepancia representan hechos diferentes que no deben interpretarse como equivalentes.

La evidencia recopilada respalda la pertinencia del problema abordado, pero todavía no permite cuantificar su incidencia general en el mercado ni demostrar que Nexa haya reducido los tiempos, errores o dificultades identificados inicialmente.

## Contraste de las Lean UX Assumptions

Las assumptions formuladas durante AV1 orientaron la definición de funcionalidades y la planificación del producto. Los avances de TB1 y AV2 aportaron evidencias de diseño, implementación y ejecución que permiten analizar la evolución de estas propuestas.

*Contraste acumulativo de las familias de assumptions.*

| Familia de assumptions | Evidencia disponible | Conclusión |
| --- | --- | --- |
| **Business Assumptions BA1–BA6** | Needfinding permitió comprender dificultades de coordinación e información en los procesos comerciales y operativos. | La relevancia del problema cuenta con sustento cualitativo. La adopción, monetización y disposición de pago requieren investigación adicional. |
| **Business Outcome Assumptions BOA1–BOA4** | Se definieron resultados de negocio y criterios para evaluar las mejoras esperadas. | No se dispone todavía de mediciones comparativas que demuestren el impacto de las funcionalidades sobre estos resultados. |
| **User Assumptions UA1–UA6** | Se documentaron necesidades de Warehouse, Driver y Buyer; posteriormente se ampliaron los recorridos de diseño e implementación. | La comprensión de los segmentos evolucionó, pero las interfaces desarrolladas todavía requieren validación representativa con sus usuarios objetivo. |
| **User Outcome & Benefit Assumptions UOBA1–UOBA6** | Los diseños y las evidencias de ejecución abordan claridad, continuidad, recuperación y consulta de información. | La disponibilidad de componentes no demuestra por sí sola que los beneficios esperados hayan sido alcanzados. |
| **Feature Assumptions FA1–FA3** | Sprint 2 y Sprint 3 incorporaron avances de implementación y verificaciones relacionadas con las funcionalidades previstas. | Las hipótesis de valor continúan pendientes de una evaluación funcional y comparativa suficiente. |

La evolución del producto permite contrastar las assumptions con artefactos más concretos, pero no reemplaza la necesidad de comprobar sus efectos sobre el trabajo real de los usuarios.

## Contraste de H1, H2 y H3

Las tres hipótesis principales se mantienen vinculadas a los segmentos objetivo y a los resultados esperados de la solución. Durante AV2 se amplió la evidencia disponible sobre las aplicaciones móviles, sin alcanzar todavía una validación integral de las hipótesis.

*Contraste de las hipótesis con los avances documentados.*

| Hipótesis | Evidencia de AV1 y TB1 | Avances de AV2 | Conclusión |
| --- | --- | --- | --- |
| **H1 — Warehouse & Dispatch Operations** | Needfinding identificó necesidades de verificación y continuidad operativa. Sprint 2 documentó acceso, consulta e identificación de productos mediante Operations Mobile. | Se ampliaron las evidencias de ejecución de Operations Android, incluyendo navegación autorizada y recuperación de acceso. | Existe evidencia de implementación y ejecución de recorridos específicos, pero no una medición del efecto de FA1 sobre las actividades completas de almacén y despacho. |
| **H2 — Driver Delivery Execution** | La investigación identificó necesidades relacionadas con incidencias, resultados de entrega y conservación de evidencias. | Sprint 3 incorporó componentes relacionados con entregas asignadas, transferencia, ubicación y tratamiento de resultados de entrega. | El código integrado aporta evidencia de avance técnico, pero no demuestra todavía la ejecución y aceptación de un proceso completo de entrega. |
| **H3 — B2B Buyers** | Needfinding amplió la comprensión de las necesidades comerciales del comprador. Durante TB1, Buyer Mobile se documentó principalmente desde el diseño. | Se incorporó evidencia de implementación de Buyer Mobile con Flutter, incluyendo navegación, catálogo, consulta de productos y componentes relacionados con seguimiento y recepción. | Buyer Mobile cuenta con implementación y artefactos académicos, pero la confirmación de operaciones comerciales, entregas y recepción todavía requiere comprobaciones integradas. |

En consecuencia, H1, H2 y H3 continúan siendo hipótesis de solución pendientes de evaluación frente a los resultados definidos. Los avances permiten identificar qué componentes existen y qué aspectos requieren comprobación, sin atribuir beneficios que todavía no han sido medidos.

## Criterios de éxito definidos

Los objetivos establecidos mediante Impact Mapping proporcionan una referencia para evaluar posteriormente los beneficios de Nexa. Estos valores corresponden a criterios de éxito y no a resultados obtenidos durante las entregas académicas.

*Criterios previstos para la evaluación de la solución.*

| Business Goal | Criterios definidos | Estado de medición |
| --- | --- | --- |
| **Goal 1 — Warehouse & Dispatch** | Reducir al menos **30 %** el esfuerzo de reconstrucción de contexto y lograr al menos **80 %** de escenarios correctos de identificación de producto, lote, cantidad y condición. | No se dispone de una evaluación comparativa que permita confirmar estos resultados. |
| **Goal 2 — Driver** | Lograr al menos **85 %** de Delivery Attempts con asociación correcta entre Delivery, Attempt, resultado y evidencia, y reducir al menos **30 %** la reconstrucción o aclaración posterior. | Los recorridos completos de entrega todavía requieren comprobación funcional y medición. |
| **Goal 3 — Buyer** | Lograr al menos **80 %** de escenarios Buyer con contexto suficiente y reducir al menos **30 %** las aclaraciones manuales ante demora, excepción o diferencia. | Las evidencias de implementación y navegación no permiten demostrar todavía el cumplimiento de estos criterios. |

La medición futura deberá utilizar tareas representativas, una línea base comparable y resultados observables, diferenciando las respuestas de las aplicaciones de las confirmaciones proporcionadas por el servidor.

## Implicancias de ingeniería y producto

La documentación de Nexa relaciona las necesidades identificadas durante la investigación con las decisiones de diseño, los requisitos funcionales y la construcción del software. Los modelos DDD y C4 permiten representar responsabilidades y límites arquitectónicos, mientras que el Product Backlog y los registros de Sprint organizan la planificación y el seguimiento de las actividades.

Estas fuentes aportan evidencias diferentes. La existencia de una historia de usuario o de una pantalla diseñada no demuestra implementación; de la misma manera, la integración del código y los resultados satisfactorios de pruebas automatizadas no acreditan por sí solos la aceptación funcional de un proceso completo.

Durante Sprint 3 adquirió especial importancia la relación entre Operations Mobile, Buyer Mobile y Nexa API. Las aplicaciones presentan información y permiten solicitar acciones, mientras que las decisiones de negocio, las autorizaciones y la confirmación de resultados corresponden al servidor.

La arquitectura también debe conservar las diferencias entre el resultado de un intento de entrega, el Proof of Delivery, la recepción del comprador y una discrepancia. Esta separación evita interpretar como completada una operación que solamente ha sido iniciada o representada visualmente.

Mantener la trazabilidad entre diseño, código, servicios y resultados observados constituye una condición necesaria para continuar desarrollando las funcionalidades sin perder consistencia entre las distintas experiencias de Nexa.

## Implementación y evidencias de TB1

Durante TB1 se documentaron avances de Sprint 2 relacionados con Operations Mobile, Nexa API y el Website. Las evidencias incluyeron publicaciones de software, configuración de servicios, instalación de la aplicación Android y recorridos de consulta e identificación de productos.

El Website se presentó como una superficie pública de información sobre Nexa, con capturas de navegación en escritorio y dispositivos móviles. Asimismo, se documentó el uso de Render para el alojamiento del API, Neon para PostgreSQL y Brevo para el servicio de correo transaccional.

En el seguimiento de Sprint 2 se conservaron diferencias entre la planificación inicial de 36 elementos del Product Backlog y 144 Story Points, y el corte histórico de Jira que registró 71 elementos y 317 Story Points. Esta variación permitió mejorar la trazabilidad del trabajo sin modificar retrospectivamente la planificación original.

Las evidencias de ejecución de Operations Mobile permitieron observar estados de acceso, búsqueda manual e identificación de productos. No obstante, dichas comprobaciones correspondieron a recorridos específicos y no constituyeron una evaluación completa de las operaciones previstas.

En el corte de TB1, Buyer Mobile se encontraba documentado principalmente como propuesta de diseño. Esta situación evolucionó durante AV2 con la incorporación de su implementación Flutter y de nuevas evidencias de ejecución.

## Avances de implementación y verificación de AV2

### Actualización del diseño UI/UX

Durante AV2 se amplió la documentación del Capítulo III, incorporando y revisando recursos de Style Guidelines, arquitectura de información, wireframes, mockups, wireflows, User Flows y prototipado.

Estos artefactos permitieron explicar con mayor precisión la organización visual de Nexa, los recorridos previstos y las alternativas consideradas para situaciones como errores, indisponibilidad de servicios y cambios de estado.

La revisión también reforzó la relación entre las historias de usuario y las pantallas de Operations Mobile y Buyer Mobile. Esta correspondencia resulta importante para comprender qué acciones debe presentar cada aplicación y qué resultados necesitan confirmación mediante Nexa API.

Los diseños representan decisiones y comportamientos previstos; su documentación no sustituye la ejecución ni la validación con usuarios.

### Implementación documentada de Sprint 3

Sprint 3 se orientó a ampliar los recorridos de distribución, entrega y recepción de mercadería. Su planificación comprende **29 elementos del Product Backlog y 129 Story Points**, relacionados con funcionalidades móviles, tareas técnicas e investigación.

Durante esta etapa se documentaron modificaciones de Operations Android y Buyer Flutter, incluyendo componentes relacionados con entregas asignadas, seguimiento, transferencia, ubicación y recepción de productos.

Los Pull Requests #72, #73 y #74 de Nexa Mobile aportaron registros de integración y revisión técnica. También se documentaron correcciones relacionadas con los mensajes de autenticación de Buyer Mobile y la recuperación de acceso mediante reingreso biométrico en Operations Android.

La publicación Nexa Mobile v2.0.1 reúne Operations Android 1.3.1 y Buyer Flutter 1.2.1+4. Los artefactos disponibles permitieron realizar comprobaciones de instalación, acceso, navegación y presentación de estados en dispositivos Android.

Las verificaciones automatizadas de Nexa Mobile y Nexa API cuentan con ejecuciones satisfactorias documentadas para revisiones específicas. Adicionalmente, se incorporaron evidencias de contratos mediante Swagger UI y registros de infraestructura en Render y Neon.

Estas evidencias permiten reconocer avances de implementación, integración y verificación técnica. Sin embargo, las comprobaciones disponibles todavía no acreditan que todos los procesos de compra, entrega, transferencia y recepción puedan completarse satisfactoriamente contra los servicios desplegados.

### Primera entrevista de validación

Durante AV2 se realizó una primera entrevista de validación con Nicolás Castro-Solorza, de 23 años, quien cuenta con experiencia laboral como cajero y recepcionista en Tottus.

La sesión, realizada el 12 de noviembre de 2026, consistió en una demostración guiada de Nexa Operations Mobile utilizando una cuenta Sales. El entrevistador mostró la consulta de un cliente comercial, la revisión de su relación activa y la búsqueda de productos mediante el catálogo.

El participante valoró positivamente la facilidad para localizar productos y diferenciar alternativas mediante sus nombres y características. También destacó la utilidad de mostrar información como la marca y el gramaje.

Entre las oportunidades de mejora identificadas se encuentran una mayor diferenciación visual de secciones y controles, la necesidad de confirmar la disponibilidad de stock antes de una venta y el acceso a información complementaria de los productos.

Estas apreciaciones permiten orientar revisiones posteriores de la experiencia comercial. Sin embargo, la sesión fue guiada por el entrevistador y no incluyó la ejecución autónoma de tareas por parte del participante.

Por tanto, los resultados corresponden a una evaluación cualitativa preliminar. No permiten medir tiempos de ejecución, tasas de éxito ni la aceptación funcional de los recorridos completos. Las observaciones se desarrollan en las secciones 4.3.2 y 4.3.3 del Capítulo IV.

### Evidencia audiovisual de AV2

Durante AV2 se incorporaron tres primeras versiones audiovisuales relacionadas con la presentación del producto, la validación y la participación del equipo.

*Registro de los videos documentados para AV2.*

| Video | Evidencia presentada |
| --- | --- |
| **About the Product** | Demostración de las interfaces y recorridos representativos de Operations Mobile y Buyer Mobile. |
| **App Validation** | Registro de la primera entrevista de validación mediante una demostración guiada de Operations Mobile. |
| **About the Team** | Grabación grupal con participación de los cinco integrantes de nexa-team. |

Los enlaces, duraciones y referencias visuales se encuentran documentados en los apartados audiovisuales de Conclusiones y en el Anexo A.

Estas evidencias permiten comunicar el estado del proyecto durante AV2, pero no sustituyen las verificaciones técnicas ni la aceptación funcional del producto.

## Mejora continua entre AV1, TB1 y AV2

La evolución del informe y del producto permite identificar mejoras documentadas en planificación, diseño, implementación y organización de evidencias.

*Principales mejoras registradas durante las entregas.*

| Etapa | Mejora aplicada | Resultado documentado |
| --- | --- | --- |
| **AV1 a TB1** | Ampliación de la trazabilidad de Sprint 2 entre planificación, Jira y evidencias de implementación. | Se conservaron las diferencias entre el backlog planificado y los registros históricos, evitando confundir seguimiento con ejecución. |
| **AV1 a TB1** | Incorporación de recursos visuales de diseño y evidencias de ejecución Android. | Se facilitó la revisión de interfaces, recorridos y resultados observados. |
| **TB1 a AV2** | Ampliación de Style Guidelines, arquitectura de información y artefactos de diseño móvil. | El Capítulo III presenta una relación más completa entre requisitos, pantallas y recorridos previstos. |
| **TB1 a AV2** | Incorporación documental de Sprint 3 y evidencias de ambas aplicaciones móviles. | El informe registra avances de desarrollo, integración, verificaciones técnicas y ejecución de Operations Mobile y Buyer Mobile. |
| **TB1 a AV2** | Inicio de la validación de solución mediante una entrevista guiada. | Se recopilaron apreciaciones reales sobre búsqueda de productos, presentación visual e información comercial. |
| **TB1 a AV2** | Actualización de la documentación audiovisual y de colaboración. | Se incorporaron las primeras versiones de About the Product, App Validation y About the Team, vinculadas con sus registros correspondientes. |

Estas mejoras muestran una evolución desde la planificación y el diseño hacia la construcción y revisión del software. También permiten identificar con mayor claridad las actividades que todavía requieren comprobación.

## Limitaciones identificadas

A pesar de los avances alcanzados, la evidencia de AV2 presenta limitaciones relevantes.

La implementación de componentes y su integración en los repositorios no demuestra que todos los recorridos comerciales y operativos puedan completarse en un entorno conectado. Las respuestas del servidor y los cambios de estado de negocio deben comprobarse mediante pruebas funcionales específicas.

Asimismo, las pruebas automatizadas y las capturas de ejecución documentan resultados acotados a determinadas versiones y condiciones. No representan una garantía general sobre la calidad, compatibilidad o funcionamiento de todas las funcionalidades del producto.

En cuanto a la validación con usuarios, durante AV2 se realizó una entrevista guiada. Aunque permitió identificar apreciaciones útiles, la cobertura todavía no incluye una evaluación suficiente de los tres segmentos objetivo ni permite establecer resultados comparativos de usabilidad.

Finalmente, los criterios de éxito establecidos durante Lean UX permanecen pendientes de medición. Las mejoras esperadas en esfuerzo, precisión y continuidad operativa no pueden presentarse todavía como beneficios demostrados.

## Recomendaciones

- Ampliar las sesiones de validación con participantes representativos de Warehouse & Dispatch Operations, Driver Delivery Execution y B2B Buyers, incluyendo tareas ejecutadas directamente por los usuarios y recorridos pertinentes de la Landing Page.
- Comprobar los procesos completos de entrega y recepción mediante respuestas y estados confirmados por Nexa API, conservando evidencias de solicitudes, errores y resultados.
- Revisar la diferenciación visual de los controles y la presentación de información comercial, considerando las recomendaciones obtenidas durante la primera entrevista de validación.
- Verificar que la consulta de disponibilidad y los datos complementarios de los productos se presenten de forma comprensible, sin sustituir la autoridad del servidor sobre inventario y decisiones comerciales.
- Evaluar H1, H2 y H3 mediante tareas comparables y mediciones relacionadas con los criterios de éxito establecidos en Impact Mapping.
- Mantener la trazabilidad entre historias de usuario, diseños, cambios de código, pruebas y resultados observados, diferenciando planificación, implementación, verificación y aceptación funcional.
- Continuar revisando el tratamiento de errores, interrupciones y escenarios excepcionales, especialmente en procesos de entrega, transferencia y recepción.
- Conservar las evidencias históricas de cada entrega y actualizar los resultados del informe únicamente cuando existan nuevas comprobaciones que los sustenten.
