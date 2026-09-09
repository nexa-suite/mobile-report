# Technical Stories

Estas historias habilitan capacidades sin duplicar autoridad de negocio. Android Native/Kotlin, Flutter/Dart e iOS Native/SwiftUI permanecen como opciones de factibilidad donde la decisión de framework sigue abierta; las tarjetas de evaluación producen evidencia, no una selección implícita.

#### TS-MOB-001 — Integrar contratos REST con autoridad del servidor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-001` | Developer | High | `TECH-EPIC-01` — Contratos y autoridad |
| **Title** | Integrar contratos REST con autoridad del servidor |  |  |
| **Description** | Como Developer, deseo integrar contratos REST con contexto explícito de Tenant y autorización del servidor, para que ambas aplicaciones consulten y envíen hechos de negocio sin duplicar autoridad. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Solicitud con contexto**<br>**Given** una persona tiene una sesión y un contexto de Tenant autorizados,<br>**When** Developer envía una solicitud REST con el contexto requerido,<br>**Then** la respuesta contiene sólo datos y acciones permitidos para esa relación.<br><br>**Scenario 2 — Solicitud sin contexto**<br>**Given** una solicitud no contiene contexto válido o autorización suficiente,<br>**When** Developer la envía,<br>**Then** el contrato devuelve un error explícito y no expone datos de negocio.<br><br>**Scenario 3 — Resultado de negocio**<br>**Given** una operación modifica un hecho de negocio,<br>**When** Developer procesa la respuesta del servidor,<br>**Then** la aplicación conserva el resultado autoritativo y no lo sustituye con un valor local. |  |  |

#### TS-MOB-002 — Evaluar una base Android Native con Kotlin

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-002` | Developer | High | `TECH-EPIC-02` — Bases de plataforma |
| **Title** | Evaluar una base Android Native con Kotlin |  |  |
| **Description** | Como **Developer**, deseo evaluar una base Android Native con Kotlin como opción técnica, para obtener evidencia de factibilidad de un flujo representativo sin declarar una arquitectura móvil ya seleccionada. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Evaluación reproducible**<br>**Given** la opción Android Native con Kotlin tiene una configuración documentada<br>**When** Developer ejecuta una prueba acotada<br>**Then** obtiene evidencia de compilación y limitaciones reproducibles sin convertir la opción en una decisión aceptada.<br><br>**Scenario 2 — Contrato compartido**<br>**Given** existe un contrato REST autorizado para un flujo representativo<br>**When** Developer lo prueba desde la opción evaluada<br>**Then** la respuesta conserva la autoridad del servidor y la diferencia técnica queda documentada.<br><br>**Scenario 3 — Límite de la evaluación**<br>**Given** una regla pertenece al servidor o al dominio compartido<br>**When** Developer revisa la prueba<br>**Then** no introduce una segunda autoridad local para esa regla. |  |  |

#### TS-MOB-003 — Evaluar una base Flutter con Dart

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-003` | Developer | Medium | `TECH-EPIC-02` — Bases de plataforma |
| **Title** | Evaluar una base Flutter con Dart |  |  |
| **Description** | Como **Developer**, deseo evaluar una base Flutter con Dart como opción cross-platform, para comparar su factibilidad en Android e iOS sin afirmar que el framework haya sido seleccionado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Prueba cross-platform**<br>**Given** la opción Flutter con Dart está documentada para evaluación<br>**When** Developer ejecuta un flujo acotado en los destinos disponibles<br>**Then** registra la evidencia de factibilidad y sus límites sin declarar una selección de framework.<br><br>**Scenario 2 — Contrato compartido**<br>**Given** un flujo usa un contrato REST autorizado<br>**When** Developer lo prueba desde la opción evaluada<br>**Then** la respuesta del servidor conserva el mismo significado de negocio.<br><br>**Scenario 3 — Diferencia de plataforma**<br>**Given** Android e iOS requieren capacidades distintas del dispositivo<br>**When** Developer compara la opción<br>**Then** documenta la diferencia técnica sin alterar el resultado de negocio. |  |  |

#### TS-MOB-004 — Evaluar una base iOS Native con SwiftUI

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-004` | Developer | Medium | `TECH-EPIC-02` — Bases de plataforma |
| **Title** | Evaluar una base iOS Native con SwiftUI |  |  |
| **Description** | Como **Developer**, deseo evaluar una base iOS Native con SwiftUI como opción técnica, para obtener evidencia de factibilidad de los flujos que puedan proyectarse en iOS sin afirmar una decisión de arquitectura. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Prueba iOS**<br>**Given** la opción iOS Native con SwiftUI está documentada para evaluación<br>**When** Developer prueba un flujo autorizado<br>**Then** registra su resultado y limitaciones sin presentar la opción como seleccionada.<br><br>**Scenario 2 — Contrato autorizado**<br>**Given** un flujo iOS dispone de un contrato REST autorizado<br>**When** Developer lo prueba<br>**Then** la respuesta conserva el significado del contrato compartido.<br><br>**Scenario 3 — Responsabilidad separada**<br>**Given** una regla pertenece al servidor<br>**When** Developer revisa la prueba iOS<br>**Then** no encuentra una autoridad de negocio duplicada en el cliente. |  |  |

#### TS-MOB-005 — Proteger el estado local selectivo y no autoritativo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-005` | Developer | High | `TECH-EPIC-03` — Continuidad y capacidades del dispositivo |
| **Title** | Proteger el estado local selectivo y no autoritativo |  |  |
| **Description** | Como Developer, deseo proteger caché segura, borradores, evidencia temporal y metadatos de reintento, para conservar continuidad sin presentar el estado local como verdad de negocio. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Dato permitido**<br>**Given** el dato está clasificado como caché, borrador, evidencia temporal o metadato de reintento,<br>**When** Developer lo guarda localmente,<br>**Then** queda protegido y vinculado al contexto autorizado.<br><br>**Scenario 2 — Dato autoritativo**<br>**Given** el dato representa inventario, crédito, pago, compromiso, entrega o recepción,<br>**When** Developer intenta confirmarlo sólo con estado local,<br>**Then** la operación no se presenta como confirmada.<br><br>**Scenario 3 — Cierre de sesión**<br>**Given** la persona cierra sesión o cambia de Tenant,<br>**When** Developer limpia el contexto local,<br>**Then** el siguiente contexto no puede leer datos protegidos del anterior. |  |  |

#### TS-MOB-006 — Resolver reintentos, resultados inciertos e idempotencia

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-006` | Developer | High | `TECH-EPIC-03` — Continuidad y capacidades del dispositivo |
| **Title** | Resolver reintentos, resultados inciertos e idempotencia |  |  |
| **Description** | Como Developer, deseo gestionar reintentos, conflictos y resultados inciertos con identificadores durables, para que una interrupción no duplique ni sobrescriba un hecho de negocio. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Reintento de comando**<br>**Given** un comando pudo completarse pero la respuesta no llegó,<br>**When** Developer lo reenvía con el mismo identificador de idempotencia,<br>**Then** el servidor devuelve un único resultado sin duplicar el hecho.<br><br>**Scenario 2 — Conflicto de versión**<br>**Given** el recurso cambió después de la lectura del cliente,<br>**When** Developer envía una mutación con versión obsoleta,<br>**Then** la respuesta identifica el conflicto y no aplica última escritura gana.<br><br>**Scenario 3 — Resultado no confirmado**<br>**Given** la red interrumpe una operación,<br>**When** Developer actualiza el estado local,<br>**Then** lo presenta como no confirmado hasta recibir respuesta del servidor. |  |  |

#### TS-MOB-007 — Integrar cámara e identificadores con alternativa manual

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-007` | Developer | Medium | `TECH-EPIC-03` — Continuidad y capacidades del dispositivo |
| **Title** | Integrar cámara e identificadores con alternativa manual |  |  |
| **Description** | Como Developer, deseo integrar cámara, Barcode, QR y GS1 con una alternativa manual, para que la identificación del producto sea útil sin convertir el dispositivo en autoridad de inventario. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Identificador único**<br>**Given** la cámara obtiene un identificador permitido con una coincidencia única,<br>**When** Developer envía el valor al contrato de producto,<br>**Then** la respuesta identifica el producto sin registrar recepción o picking por sí sola.<br><br>**Scenario 2 — Identificador ambiguo**<br>**Given** el valor no existe, es ambiguo o no corresponde al Tenant,<br>**When** Developer lo envía,<br>**Then** el contrato devuelve una respuesta de rechazo explicable y no adivina el producto.<br><br>**Scenario 3 — Alternativa manual**<br>**Given** la cámara no está disponible,<br>**When** Developer envía una búsqueda manual,<br>**Then** el flujo permite continuar sólo después de una identificación autorizada. |  |  |

#### TS-MOB-008 — Abrir navegación externa con un límite de ubicación

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-008` | Developer | Medium | `TECH-EPIC-03` — Continuidad y capacidades del dispositivo |
| **Title** | Abrir navegación externa con un límite de ubicación |  |  |
| **Description** | Como Developer, deseo entregar un destino autorizado a una aplicación de navegación externa, para apoyar una entrega sin crear seguimiento continuo ni autoridad de ubicación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Destino autorizado**<br>**Given** existe una entrega activa y un destino autorizado,<br>**When** Developer solicita navegación externa,<br>**Then** entrega sólo el destino permitido al proveedor elegido.<br><br>**Scenario 2 — Destino no autorizado**<br>**Given** el destino falta, expiró o no corresponde a la relación,<br>**When** Developer solicita navegación,<br>**Then** no expone la ubicación ni cambia el estado de la entrega.<br><br>**Scenario 3 — Navegación fallida**<br>**Given** el proveedor externo no está disponible,<br>**When** Developer intenta abrir las indicaciones,<br>**Then** la entrega conserva su estado y el fallo se comunica sin inventar llegada. |  |  |

#### TS-MOB-009 — Evaluar notificaciones y deep links con autorización

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-009` | Developer | Medium | `TECH-EPIC-04` — Calidad y distribución |
| **Title** | Evaluar notificaciones y deep links con autorización |  |  |
| **Description** | Como **Developer**, deseo evaluar notificaciones y deep links con autorización, para definir sus límites de contexto y seguridad sin asumir un proveedor o una integración ya resueltos. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Contexto autorizado**<br>**Given** una notificación refiere a trabajo protegido<br>**When** Developer evalúa el deep link<br>**Then** el destino vuelve a comprobar Tenant, relación y permisos antes de mostrar información.<br><br>**Scenario 2 — Destino vencido**<br>**Given** el enlace venció o el contexto ya no es válido<br>**When** Developer lo prueba<br>**Then** la aplicación comunica el estado y no expone datos protegidos.<br><br>**Scenario 3 — Proveedor pendiente**<br>**Given** el canal de notificación todavía requiere decisión de proveedor<br>**When** Developer documenta la evaluación<br>**Then** se conserva la evidencia técnica sin declarar una integración aceptada. |  |  |

#### TS-MOB-010 — Aplicar i18n y accesibilidad en las aplicaciones móviles

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-010` | Developer | Medium | `TECH-EPIC-04` — Calidad y distribución |
| **Title** | Aplicar i18n y accesibilidad en las aplicaciones móviles |  |  |
| **Description** | Como Developer, deseo incorporar internacionalización y accesibilidad en ambas aplicaciones, para que el contenido, los estados y las acciones puedan comprenderse y operarse con diferentes configuraciones y necesidades. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Cambio de idioma**<br>**Given** la aplicación dispone de un idioma soportado,<br>**When** Developer cambia la configuración de idioma,<br>**Then** títulos, mensajes, errores y estados se presentan traducidos sin alterar los datos de negocio.<br><br>**Scenario 2 — Lectura asistida**<br>**Given** una persona utiliza una tecnología de asistencia,<br>**When** Developer recorre un flujo móvil,<br>**Then** controles, estados, errores y orden de lectura tienen nombres y relaciones comprensibles.<br><br>**Scenario 3 — Texto dinámico**<br>**Given** una respuesta contiene un nombre o mensaje variable,<br>**When** Developer lo presenta,<br>**Then** el contenido se adapta al idioma y tamaño de texto sin ocultar la acción o el resultado. |  |  |

#### TS-MOB-011 — Preparar validación técnica y observabilidad mínima

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-011` | Developer | Medium | `TECH-EPIC-04` — Calidad y distribución |
| **Title** | Preparar validación técnica y observabilidad mínima |  |  |
| **Description** | Como Developer, deseo validar contratos, autorización, reintentos, estado local y errores con observabilidad mínima, para diagnosticar fallos sin registrar secretos, Tenant IDs innecesarios o PII. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Validación de contrato**<br>**Given** existe una operación móvil representativa,<br>**When** Developer ejecuta la prueba de contrato con éxito y error,<br>**Then** verifica autorización, estructura de respuesta, conflicto e idempotencia.<br><br>**Scenario 2 — Señal diagnóstica segura**<br>**Given** una solicitud móvil falla,<br>**When** Developer registra la señal técnica,<br>**Then** conserva correlación y causa útil sin incluir tokens, secretos, Tenant IDs innecesarios o datos sensibles.<br><br>**Scenario 3 — Recuperación observable**<br>**Given** una operación se reintenta o entra en conflicto,<br>**When** Developer revisa la telemetría,<br>**Then** puede distinguir intento, resultado confirmado y resultado no confirmado sin alterar el hecho de negocio. |  |  |

#### TS-MOB-012 — Preparar evidencia técnica de build, instalación y dispositivos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `TS-MOB-012` | Developer | Medium | `TECH-EPIC-04` — Calidad y distribución |
| **Title** | Preparar evidencia técnica de build, instalación y dispositivos |  |  |
| **Description** | Como **Developer**, deseo definir evidencia repetible de build, instalación y prueba en dispositivos para las opciones técnicas en evaluación, para distinguir factibilidad técnica de aceptación de producto. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Build identificable**<br>**Given** una opción técnica tiene configuración documentada<br>**When** Developer genera un build de prueba<br>**Then** el artefacto identifica la opción, versión, commit y entorno utilizados.<br><br>**Scenario 2 — Instalación repetible**<br>**Given** existe un dispositivo o emulador compatible<br>**When** Developer instala el artefacto siguiendo la guía<br>**Then** puede ejecutar el flujo técnico previsto y registra el resultado.<br><br>**Scenario 3 — Evidencia separada**<br>**Given** el build y la instalación funcionan<br>**When** Developer documenta el resultado<br>**Then** lo clasifica como evidencia técnica y no como aceptación funcional, investigación validada o preparación de producción. |  |  |
