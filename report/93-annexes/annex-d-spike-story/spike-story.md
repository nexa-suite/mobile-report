# Annex D — Spike Stories

Este anexo amplía los seis Spike Stories de la sección 2.4.1. Cada Spike
investiga una incertidumbre concreta y define el material que permite cerrarla.
No representa una decisión o resultado que todavía no haya sido producido.

## SPIKE-001 — Oportunidad de aprendizaje autónomo

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar qué oportunidad de aprendizaje autónomo aporta valor a una actividad móvil de Nexa. |
| Question | ¿Qué resultado observable, datos, límites de privacidad y mecanismo de revisión requiere la oportunidad? |
| Expected artifact | Matriz de oportunidades y fuentes, clasificación de datos, riesgos de privacidad, factibilidad y prueba acotada. |
| Completion criteria | Recomendación documentada, límites de uso definidos y separación entre observación, sugerencia y decisión de negocio. |
| Scope | La oportunidad no puede confirmar inventario, crédito, pago, compromiso, entrega o recepción por sí sola. |
| Planned Sprint | S3 |

## SPIKE-002 — Bases compartidas y paridad funcional

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar bases compartidas para Nexa Operations Mobile y Nexa Buyer Mobile. |
| Question | ¿Cómo pueden Android Native/Kotlin, Flutter/Dart e iOS Native/SwiftUI sostener contratos compartidos, estado local seguro, distribución y paridad funcional entre las dos aplicaciones? |
| Expected artifact | Matriz de flujos, seguridad, contrato, estado local, pruebas, distribución y mantenimiento, acompañada por una prueba acotada de un flujo común. |
| Completion criteria | Trade-offs, límites, responsabilidades compartidas y diferencias permitidas de plataforma documentados. No se reduce la investigación a elegir una única tecnología. |
| Scope | Las tecnologías son aceptadas como opciones de implementación de este capítulo; Liquid Glass sólo se considera en presentación. Ninguna crea un Bounded Context. |
| Planned Sprint | S1 |

## SPIKE-003 — Identificadores de producto

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar el alcance de Barcode, QR, GS1 y la alternativa manual para producto, paquete y ubicación. |
| Question | ¿Qué formatos, permisos, ambigüedades, expiración, reutilización y validaciones del servidor hacen confiable una identificación? |
| Expected artifact | Comparación de formatos, reglas de identificación, límites de seguridad y prueba controlada en dispositivo. |
| Completion criteria | Alcance, alternativa manual, errores esperados y preguntas de integración documentados sin atribuir autoridad al dispositivo. |
| Scope | Identificar no equivale a recibir, reservar, mover o consumir stock. |
| Planned Sprint | S2 |

## SPIKE-004 — Persistencia y recuperación local

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar qué información puede conservarse localmente y cómo recuperar cambios después de una interrupción. |
| Question | ¿Cómo se clasifican, protegen, reintentan y reconcilian caché, borradores, evidencia temporal y metadatos de reintento? |
| Expected artifact | Clasificación de datos, modelo de protección, secuencia de sincronización, política de conflictos y prueba de recuperación. |
| Completion criteria | Límite offline seguro documentado; los hechos de negocio dependen de confirmación autoritativa del servidor. |
| Scope | No se considera válida una confirmación local de inventario, compromiso, crédito, pago, entrega o recepción. |
| Planned Sprint | S2 |

## SPIKE-005 — Notificaciones y deep links

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar usos autorizados de notificaciones push y deep links para contextos móviles válidos. |
| Question | ¿Qué eventos pueden iniciar una notificación, cómo se comprueban Tenant y permisos, y cómo expiran o se repiten los enlaces? |
| Expected artifact | Matriz de evento, canal, permiso, ámbito, expiración, reintento y destino permitido. |
| Completion criteria | Reglas de navegación y seguridad documentadas; la notificación sólo orienta y no cambia por sí sola el estado de negocio. |
| Scope | La navegación iniciada por una notificación siempre vuelve a consultar información autorizada. |
| Planned Sprint | S3 |

## SPIKE-006 — Mapas y ubicación

| Campo | Definición |
| :--- | :--- |
| Objective | Determinar el uso móvil de mapas y ubicación respetando privacidad, batería y conectividad. |
| Question | ¿Qué destino, permiso, observación del dispositivo, alternativa y límite de retención son necesarios para apoyar una entrega? |
| Expected artifact | Comparación de navegación externa, permisos, consumo, conectividad y alternativas de operación. |
| Completion criteria | Límite mínimo documentado; el alcance inicial permanece en navegación externa autorizada y no en seguimiento continuo. |
| Scope | No se deriva ETA, ubicación continua o autoridad de entrega a partir de una apertura de navegación. |
| Planned Sprint | S4 |

## Relación con la especificación

Los seis registros resumidos están en [2.4.1 Spike Stories](../../02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-spike-stories.md). Sus preguntas se relacionan con las historias `MOB-US` correspondientes, pero no agregan historias funcionales ni Bounded Contexts.
