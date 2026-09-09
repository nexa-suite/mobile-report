# Spike Stories

Los Spikes reducen incertidumbre antes de una decisión. No son Functional User Stories ni acreditan una arquitectura, integración, investigación o implementación como completada.

#### SPIKE-001 — Oportunidad de aprendizaje autónomo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `SPIKE-001` | Developer | Medium | `SPIKE-EPIC-01` — Investigación de producto móvil |
| **Title** | Oportunidad de aprendizaje autónomo |  |  |
| **Description** | Como **Developer**, deseo investigar oportunidad de aprendizaje autónomo, para reducir una incertidumbre antes de comprometer una decisión o una implementación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Objetivo de investigación**<br>**Given** Determinar qué oportunidad de aprendizaje autónomo aporta valor al trabajo móvil sin crear una autoridad paralela.<br>**When** Developer investiga la pregunta ¿Qué resultado observable, datos, límites de privacidad y mecanismo de revisión requiere la oportunidad seleccionada?<br>**Then** documenta la incertidumbre que debe reducirse sin promover una hipótesis como hecho de negocio.<br><br>**Scenario 2 — Evidencia esperada**<br>**Given** la investigación necesita evidencia verificable<br>**When** Developer compara alternativas o ejecuta una prueba acotada<br>**Then** Matriz de oportunidades, fuentes, datos, privacidad, factibilidad y prueba acotada.<br><br>**Scenario 3 — Cierre**<br>**Given** la evidencia fue revisada<br>**When** Developer cierra el Spike<br>**Then** Recomendación documentada, límites de uso definidos y ausencia explícita de afirmaciones de producción. |  |  |

#### SPIKE-002 — Bases compartidas y paridad funcional

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `SPIKE-002` | Developer | High | `SPIKE-EPIC-02` — Estrategia de implementación móvil |
| **Title** | Bases compartidas y paridad funcional |  |  |
| **Description** | Como **Developer**, deseo investigar bases compartidas y paridad funcional, para reducir una incertidumbre antes de comprometer una decisión o una implementación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Objetivo de investigación**<br>**Given** Determinar bases compartidas y estrategia de paridad funcional para Nexa Operations Mobile y Nexa Buyer Mobile.<br>**When** Developer investiga la pregunta ¿Cómo se comparan Android Native/Kotlin, Flutter/Dart e iOS Native/SwiftUI como opciones en evaluación para sostener contratos compartidos, estado local seguro, distribución y paridad funcional entre las dos aplicaciones?<br>**Then** documenta la incertidumbre que debe reducirse sin promover una hipótesis como hecho de negocio.<br><br>**Scenario 2 — Evidencia esperada**<br>**Given** la investigación necesita evidencia verificable<br>**When** Developer compara alternativas o ejecuta una prueba acotada<br>**Then** Matriz comparativa de flujos, seguridad, estado local, contratos, distribución, pruebas y mantenimiento para las opciones evaluadas; prueba acotada de un flujo común.<br><br>**Scenario 3 — Cierre**<br>**Given** la evidencia fue revisada<br>**When** Developer cierra el Spike<br>**Then** Trade-offs, límites, responsabilidades compartidas y diferencias permitidas de plataforma documentados. La evidencia no selecciona un framework ni duplica reglas de negocio. |  |  |

#### SPIKE-003 — Identificadores de producto

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `SPIKE-003` | Developer | Medium | `SPIKE-EPIC-03` — Capacidades del dispositivo |
| **Title** | Identificadores de producto |  |  |
| **Description** | Como **Developer**, deseo investigar identificadores de producto, para reducir una incertidumbre antes de comprometer una decisión o una implementación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Objetivo de investigación**<br>**Given** Determinar el alcance de Barcode, QR, GS1 y la alternativa manual para identificar productos, paquetes y ubicaciones.<br>**When** Developer investiga la pregunta ¿Qué formatos, permisos, ambigüedades, expiración, reutilización y validaciones del servidor son necesarios para una identificación confiable?<br>**Then** documenta la incertidumbre que debe reducirse sin promover una hipótesis como hecho de negocio.<br><br>**Scenario 2 — Evidencia esperada**<br>**Given** la investigación necesita evidencia verificable<br>**When** Developer compara alternativas o ejecuta una prueba acotada<br>**Then** Comparación de formatos, reglas de identificación, límites de seguridad y prueba controlada en dispositivo.<br><br>**Scenario 3 — Cierre**<br>**Given** la evidencia fue revisada<br>**When** Developer cierra el Spike<br>**Then** Alcance de identificadores, alternativa manual y preguntas de integración documentados sin crear un Bounded Context de dispositivo. |  |  |

#### SPIKE-004 — Persistencia y recuperación local

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `SPIKE-004` | Developer | High | `SPIKE-EPIC-04` — Continuidad controlada |
| **Title** | Persistencia y recuperación local |  |  |
| **Description** | Como **Developer**, deseo investigar persistencia y recuperación local, para reducir una incertidumbre antes de comprometer una decisión o una implementación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Objetivo de investigación**<br>**Given** Determinar qué información puede conservarse localmente y cómo recuperar cambios sin presentar éxito de negocio no confirmado.<br>**When** Developer investiga la pregunta ¿Cómo se clasifican, protegen, reintentan y reconcilian caché, borradores, evidencia temporal y metadatos de reintento?<br>**Then** documenta la incertidumbre que debe reducirse sin promover una hipótesis como hecho de negocio.<br><br>**Scenario 2 — Evidencia esperada**<br>**Given** la investigación necesita evidencia verificable<br>**When** Developer compara alternativas o ejecuta una prueba acotada<br>**Then** Clasificación de datos, modelo de protección, secuencia de sincronización, política de conflictos y prueba de recuperación.<br><br>**Scenario 3 — Cierre**<br>**Given** la evidencia fue revisada<br>**When** Developer cierra el Spike<br>**Then** Límite offline seguro documentado; inventario, compromiso, crédito, pago, entrega y recepción siguen dependiendo de confirmación autoritativa. |  |  |

#### SPIKE-005 — Notificaciones y deep links

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `SPIKE-005` | Developer | Medium | `SPIKE-EPIC-05` — Comunicación contextual |
| **Title** | Notificaciones y deep links |  |  |
| **Description** | Como **Developer**, deseo investigar notificaciones y deep links, para reducir una incertidumbre antes de comprometer una decisión o una implementación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Objetivo de investigación**<br>**Given** Determinar usos autorizados de notificaciones push y deep links para llevar a una persona a un contexto móvil válido.<br>**When** Developer investiga la pregunta ¿Qué eventos pueden iniciar una notificación, cómo se comprueban Tenant y permisos, y cómo expiran o se repiten los enlaces?<br>**Then** documenta la incertidumbre que debe reducirse sin promover una hipótesis como hecho de negocio.<br><br>**Scenario 2 — Evidencia esperada**<br>**Given** la investigación necesita evidencia verificable<br>**When** Developer compara alternativas o ejecuta una prueba acotada<br>**Then** Matriz de evento, canal, permiso, ámbito, expiración, reintento y destino permitido.<br><br>**Scenario 3 — Cierre**<br>**Given** la evidencia fue revisada<br>**When** Developer cierra el Spike<br>**Then** Reglas de navegación y seguridad documentadas; una notificación no cambia por sí sola el estado de negocio. |  |  |

#### SPIKE-006 — Mapas y ubicación

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `SPIKE-006` | Developer | Medium | `SPIKE-EPIC-06` — Navegación responsable |
| **Title** | Mapas y ubicación |  |  |
| **Description** | Como **Developer**, deseo investigar mapas y ubicación, para reducir una incertidumbre antes de comprometer una decisión o una implementación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Objetivo de investigación**<br>**Given** Determinar el uso móvil de mapas y ubicación respetando privacidad, batería y conectividad.<br>**When** Developer investiga la pregunta ¿Qué destino, permiso, observación del dispositivo, alternativa y límite de retención son necesarios para apoyar una entrega?<br>**Then** documenta la incertidumbre que debe reducirse sin promover una hipótesis como hecho de negocio.<br><br>**Scenario 2 — Evidencia esperada**<br>**Given** la investigación necesita evidencia verificable<br>**When** Developer compara alternativas o ejecuta una prueba acotada<br>**Then** Comparación de navegación externa, permisos, consumo, conectividad y alternativas de operación.<br><br>**Scenario 3 — Cierre**<br>**Given** la evidencia fue revisada<br>**When** Developer cierra el Spike<br>**Then** Límite mínimo documentado; el alcance inicial se mantiene en navegación externa autorizada y no en seguimiento continuo. |  |  |
