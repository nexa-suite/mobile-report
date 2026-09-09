# Spike Stories

Un Spike reduce una incertidumbre antes de una decisión. No es una Functional
User Story ni prueba arquitectura, integración, investigación, implementación o
aceptación de producto. Cada Spike debe dejar evidencia revisable y una salida
explícita: decidir, diferir o descartar.

#### SPIKE-001 — Oportunidad de aprendizaje autónomo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| SPIKE-001 | Developer | Medium | SPIKE-EPIC-01 — Investigación de producto móvil |

| Campo | Contenido |
| --- | --- |
| Incertidumbre | No existe decisión aceptada que justifique una capacidad de aprendizaje autónomo para Mobile. |
| Pregunta | ¿Hay una necesidad de producto con fuente canónica, resultado observable y límites de datos que justifique explorarla? |
| Evidencia esperada | Referencias de producto, matriz de valor/riesgo, límites de privacidad y evidencia de necesidad; ausencia de fuente también es evidencia para diferir. |
| PoC mínimo | No se ejecuta PoC sin alcance aceptado. Si se autoriza, usa datos no sensibles y un artefacto aislado que no modifica hechos de negocio. |
| Decisión / salida | Recomendar explorar, diferir o descartar; documentar el alcance y las restricciones si procede. |
| Criterio de cierre | La incertidumbre, fuente, evidencia y decisión quedan registradas; no se presenta una capacidad propuesta como funcionalidad de Nexa. |

#### SPIKE-002 — Bases compartidas y paridad funcional

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| SPIKE-002 | Developer | High | SPIKE-EPIC-02 — Estrategia de implementación móvil |

| Campo | Contenido |
| --- | --- |
| Incertidumbre | Aún no se ha seleccionado framework o runtime para Operations Mobile y Buyer Mobile. |
| Pregunta | ¿Cómo comparan Android Native/Kotlin, Flutter/Dart e iOS Native/SwiftUI frente a contratos, seguridad, accesibilidad, distribución, pruebas y mantenimiento? |
| Evidencia esperada | Matriz con criterios de TS-MOB-002, build reproducible, límites de dispositivo y prueba acotada de un flujo representativo sin duplicar reglas de negocio. |
| PoC mínimo | Un flujo técnico no autoritativo que consume o valida un contrato permitido y registra versión, entorno, resultado y limitación. |
| Decisión / salida | ADR o registro de decisión que seleccione, difiera o descarte alternativas, con trade-offs y responsable de aprobación. |
| Criterio de cierre | La comparación es reproducible, no infiere Product Acceptance y no convierte una alternativa en selección antes de la decisión explícita. |

#### SPIKE-003 — Identificadores de producto

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| SPIKE-003 | Developer | Medium | SPIKE-EPIC-03 — Capacidades del dispositivo |

| Campo | Contenido |
| --- | --- |
| Incertidumbre | No está definido qué formatos de Barcode, QR o GS1 son necesarios ni cuándo una alternativa manual es suficiente. |
| Pregunta | ¿Qué formatos, permisos, ambigüedades, caducidad y validaciones del servidor se requieren para identificar un producto, paquete o ubicación de manera segura? |
| Evidencia esperada | Inventario de formatos encontrados, reglas de identificación, fallos/ambigüedades y límites de seguridad. |
| PoC mínimo | Lectura controlada de un identificador no sensible y búsqueda manual equivalente; ninguna prueba registra recepción o picking por sí sola. |
| Decisión / salida | Alcance de formatos soportados, alternativa manual y preguntas de contrato pendientes. |
| Criterio de cierre | La recomendación separa identificación de cualquier decisión de inventario y no crea un Bounded Context de dispositivo. |

#### SPIKE-004 — Persistencia y recuperación local

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| SPIKE-004 | Developer | High | SPIKE-EPIC-04 — Continuidad controlada |

| Campo | Contenido |
| --- | --- |
| Incertidumbre | Falta decidir qué caché segura, borrador, evidencia temporal y metadato de reintento puede persistir sin declarar éxito de negocio. |
| Pregunta | ¿Cómo se protegen, expiran, reintentan y recuperan esos datos cuando se pierde conectividad o cambia el contexto autorizado? |
| Evidencia esperada | Clasificación de datos, política de protección/limpieza, secuencia de reintento, comportamiento ante conflicto y resultado de recuperación. |
| PoC mínimo | Crear un borrador o evidencia temporal, interrumpir la red y comprobar que la aplicación lo muestra como no confirmado hasta la respuesta autoritativa. |
| Decisión / salida | Límite offline seguro y política de recuperación; no constituye un motor genérico de sincronización. |
| Criterio de cierre | Inventario, compromiso, crédito, pago, entrega y recepción conservan confirmación del servidor; no hay last-write-wins silencioso. |

#### SPIKE-005 — Notificaciones y deep links

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| SPIKE-005 | Developer | Medium | SPIKE-EPIC-05 — Comunicación contextual |

| Campo | Contenido |
| --- | --- |
| Incertidumbre | No se han seleccionado proveedor, eventos permitidos ni límites de navegación para notificaciones. |
| Pregunta | ¿Qué evento, permiso, ámbito, expiración y validación de Tenant/relación requiere cada deep link? |
| Evidencia esperada | Matriz evento-canal-destino, política de expiración/reintento, prueba de autorización y riesgos de información expuesta. |
| PoC mínimo | Abrir un deep link de prueba hacia un contexto autorizado y comprobar que un enlace inválido, expirado o sin permiso no expone datos. |
| Decisión / salida | Lista de casos permitidos, restricciones de proveedor y contrato de revalidación al abrir. |
| Criterio de cierre | La notificación no cambia por sí sola un hecho de negocio y la decisión de proveedor sigue explícita si aún no existe. |

#### SPIKE-006 — Mapas y ubicación

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| SPIKE-006 | Developer | Medium | SPIKE-EPIC-06 — Navegación responsable |

| Campo | Contenido |
| --- | --- |
| Incertidumbre | Falta confirmar qué uso de ubicación aporta valor sin introducir tracking continuo, retención excesiva o una autoridad de ubicación. |
| Pregunta | ¿Qué destino autorizado, permiso, alternativa, límite de retención y comportamiento ante falla necesita la navegación externa? |
| Evidencia esperada | Comparación de navegación externa, permisos, conectividad, batería, privacidad y alternativas manuales. |
| PoC mínimo | Abrir un destino autorizado en una aplicación externa y comprobar que la falla no modifica Delivery ni inventa llegada. |
| Decisión / salida | Límite de ubicación permitido, requisitos de privacidad y criterios para diferir cualquier tracking adicional. |
| Criterio de cierre | El alcance inicial queda limitado a navegación externa autorizada; no se declara ETA, optimización de rutas ni seguimiento continuo. |
