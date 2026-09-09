# User Stories

## Requirements Specification and To-Be Scenario Mapping


Esta sección proyecta requisitos de negocio para Nexa Operations Mobile, Nexa
Buyer Mobile y la Landing pública. Las Functional User Stories describen
outcomes para actores; las Technical Stories y los Spikes delimitan habilitación
e incertidumbre sin trasladar la autoridad de negocio al cliente.

V1 es el alcance actual de producto y del curso: trabajo autorizado, recepción
y preparación de almacén, Dispatch Handoff, ejecución de Delivery, Buyer
Receipt, discrepancias y actualizaciones críticas. V2, V3 y V4/Future siguen
visibles como roadmap canónico, pero no son compromisos de implementación del
curso.

## To-Be Scenario Mapping

El To-Be describe comportamiento objetivo, no el As-Is Journey ni un cliente
implementado. Las decisiones protegidas continúan bajo autoridad del servidor y
del Bounded Context responsable.

| Escenario objetivo | Actor y producto | Comportamiento objetivo | Historias relacionadas |
| --- | --- | --- | --- |
| Authorized Mobile Work Context | Mobile User; Nexa Operations Mobile y Nexa Buyer Mobile | Nexa confirma Tenant, Workspace y permisos antes de exponer trabajo protegido. | MOB-US-001..003 |
| Warehouse Receiving, Identification and Preparation | Warehouse Operator; Nexa Operations Mobile | La persona identifica Product/SKU, registra hechos físicos y prepara trabajo con lotes, condición y evidencia. | MOB-US-011..017, MOB-US-019 |
| Dispatch Readiness and Handoff | Dispatch Coordinator; Nexa Operations Mobile | La persona verifica bienes, asigna responsabilidad y registra un Dispatch Handoff revisable. | MOB-US-020..025 |
| Driver Delivery Execution | Driver / Delivery Operator; Nexa Operations Mobile | La persona trabaja sobre una Delivery asignada, abre navegación externa cuando corresponde y registra Delivery Attempt, Driver Outcome y Proof of Delivery. | MOB-US-026..034 |
| Buyer Handoff, Receipt and Discrepancy | Customer Buyer; Nexa Buyer Mobile | La persona verifica el handoff, declara el Buyer Receipt y comunica discrepancias sin borrar hechos previos. | MOB-US-044, MOB-US-047..049 |
| Acquisition, Contact and Onboarding Initiation | Prospective Company Representative; Landing pública | La Landing comunica la propuesta, habilita contacto y recibe una solicitud de onboarding sin crear un Tenant o Workspace como hecho autoritativo. | LAND-US-001..006 |

### Reglas transversales

| Regla | Aplicación en el To-Be |
| --- | --- |
| Autoridad | El servidor confirma y persiste los hechos de negocio; el cliente no sustituye esa confirmación. |
| Conectividad | V1 es online-first. La caché segura, los borradores y la evidencia temporal apoyan continuidad, pero no confirman inventario, crédito, pagos, Sales Orders ni finalización de Delivery. |
| Integridad histórica | Una corrección conserva evidencia correctiva o de reversión; no reemplaza silenciosamente un hecho existente. |
| Ubicación | El alcance V1 entrega un destino autorizado a navegación externa; no introduce seguimiento continuo, ETA ni optimización de rutas. |
| Distinciones | Tenant, Workspace, Human Identity, Workforce Membership, Customer Account y Buyer Relationship conservan significados distintos. Dispatch Handoff, Driver Outcome y Buyer Receipt también son hechos separados. |

## Story Catalog and Traceability



Nexa Operations Mobile y Nexa Buyer Mobile son las dos proyecciones Mobile.
V1 es el alcance actual del curso; V2, V3 y V4/Future siguen visibles para
completitud de roadmap y se mantienen diferidos.

| Release | Functional Stories | Significado en este informe |
| --- | ---: | --- |
| V1 | 28 | Alcance actual de producto y curso. |
| V2 | 35 | Roadmap diferido; requiere refinamiento y evidencia antes de entrega. |
| V3 | 9 | Roadmap posterior de mayor costo o incertidumbre. |
| V4/Future | 1 | Hipótesis futura; no es compromiso de entrega. |
| **Total** | **73** | Inventario funcional canónico completo. |

## Epic registry

Un Epic agrupa requisitos de producto. No representa un Bounded Context, una
pantalla, una aplicación ni una unidad de despliegue.

| Epic | Resultado agrupado | Release(s) | Stories |
| --- | --- | --- | --- |
| MOBILE-EPIC-01 | Acceso seguro y contexto de trabajo | V1 | MOB-US-001..003 |
| MOBILE-EPIC-02 | Recepción, identificación y preparación de almacén | V1 | MOB-US-011..017, MOB-US-019 |
| MOBILE-EPIC-03 | Preparación de despacho y Dispatch Handoff | V1 | MOB-US-020..025 |
| MOBILE-EPIC-04 | Ejecución de Delivery y Proof of Delivery | V1 | MOB-US-026..028, MOB-US-031..034 |
| MOBILE-EPIC-05 | Handoff, Buyer Receipt y actualizaciones críticas | V1 | MOB-US-044, MOB-US-047..049 |
| MOBILE-EPIC-06 | Conveniencia comercial y operativa futura | V2 | MOB-US-004..010, MOB-US-036..043 |
| MOBILE-EPIC-07 | Operación de campo avanzada y continuidad selectiva | V2, V3 | MOB-US-018, MOB-US-029, MOB-US-030, MOB-US-035, MOB-US-045, MOB-US-046 |
| MOBILE-EPIC-08 | Transferencias y exactitud de inventario | V2, V3 | MOB-US-050..056 |
| MOBILE-EPIC-09 | Excepciones de despacho y coordinación de Delivery | V2, V3 | MOB-US-057..066 |
| MOBILE-EPIC-10 | Continuidad de Delivery para Customer Buyer | V2 | MOB-US-067..069 |
| MOBILE-EPIC-11 | Seguimiento comercial y financiero | V2, V3 | MOB-US-070..072 |
| MOBILE-EPIC-12 | Automatización de almacén futura | V4/Future | MOB-US-073 |

## Segmentos y actores actuales

| Segmento de investigación y producto | Actores V1 | Proyección | Estado de evidencia |
| --- | --- | --- | --- |
| Warehouse & Dispatch Operations | Warehouse Operator; Dispatch Coordinator | Nexa Operations Mobile | RESEARCH PENDING |
| Driver Delivery Execution | Driver / Delivery Operator | Nexa Operations Mobile | RESEARCH PENDING |
| B2B Buyers | Customer Buyer | Nexa Buyer Mobile | RESEARCH PENDING |

Mobile User es una abstracción transversal de MOB-US-001..003. Sirve a
Warehouse Operator, Dispatch Coordinator, Driver / Delivery Operator y
Customer Buyer cuando retoman trabajo autorizado; no es una User Persona ni un
segmento de investigación.

## Trazabilidad a nivel de Epic y cluster

| Epic / cluster | Current actor/segment | Lean UX relationship | Needfinding evidence | To-Be scenario | Stories |
| --- | --- | --- | --- | --- | --- |
| MOBILE-EPIC-01 — contexto de trabajo | Mobile User para los cuatro actores V1 | La continuidad de contexto y la exposición de trabajo autorizado son hipótesis de valor. | RESEARCH PENDING; no se reclasifica evidencia histórica. | Authorized Mobile Work Context | MOB-US-001..003 |
| MOBILE-EPIC-02/03 — almacén a despacho | Warehouse & Dispatch Operations; Warehouse Operator y Dispatch Coordinator | La continuidad entre hechos físicos, preparación y responsabilidad orienta el aprendizaje. | RESEARCH PENDING; se requiere investigación específica del segmento actual. | Warehouse Receiving, Identification and Preparation; Dispatch Readiness and Handoff | MOB-US-011..017, MOB-US-019..025 |
| MOBILE-EPIC-04 — ejecución de Delivery | Driver Delivery Execution; Driver / Delivery Operator | El intento atribuible y la evidencia revisable son hipótesis de continuidad operativa. | RESEARCH PENDING; no se renombra evidencia operativa previa como investigación de Driver. | Driver Delivery Execution | MOB-US-026..028, MOB-US-031..034 |
| MOBILE-EPIC-05 — recepción de Buyer | B2B Buyers; Customer Buyer | La claridad de handoff, receipt y discrepancia orienta el beneficio esperado. | RESEARCH PENDING; no se fabrican entrevistas de Buyer. | Buyer Handoff, Receipt and Discrepancy | MOB-US-044, MOB-US-047..049 |
| LAND-EPIC-01 — adquisición pública | Prospective Company Representative | La comprensión de la propuesta y el siguiente paso comercial son hipótesis de adquisición. | RESEARCH PENDING | Acquisition, Contact and Onboarding Initiation | LAND-US-001..006 |

## Landing Page User Stories

#### LAND-US-001 — Comprender la propuesta B2B de Nexa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-001` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |

| Field | Content |
| --- | --- |
| **Title** | Comprender la propuesta B2B de Nexa |
| **Description** | Como **Prospective Company Representative**, deseo comprender la propuesta B2B de Nexa para importadores y distribuidores, incluida la especialización de cadena de frío cuando aplique, para decidir si corresponde continuar la evaluación. |
| **Acceptance Criteria** | **Scenario 1 — Propuesta disponible**<br>**Given** una persona abre la Landing pública<br>**When** revisa la introducción del producto<br>**Then** identifica el contexto B2B de Nexa sin confundirlo con un ecommerce genérico ni con un producto exclusivo de cadena de frío.<br><br>**Scenario 2 — Especialización contextual**<br>**Given** la persona opera con productos que requieren cadena de frío<br>**When** revisa las capacidades públicas<br>**Then** encuentra esa especialización explicada como una capacidad aplicable y no como la única finalidad de Nexa. |

#### LAND-US-002 — Evaluar el ajuste con el perfil operativo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-002` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |

| Field | Content |
| --- | --- |
| **Title** | Evaluar el ajuste con el perfil operativo |
| **Description** | Como prospecto empresarial, deseo contrastar mi perfil operativo con las soluciones de Nexa, para decidir si debo iniciar una conversación o evaluación. |
| **Acceptance Criteria** | **Scenario 1 — Perfil presentado**<br>**Given** el prospecto opera como importador, distribuidor o empresa de almacenamiento en frío,<br>**When** revisa la solución correspondiente,<br>**Then** encuentra el contexto operativo descrito por Nexa.<br><br>**Scenario 2 — Siguiente paso común**<br>**Given** el prospecto combina más de un perfil,<br>**When** compara las soluciones,<br>**Then** puede continuar hacia un producto, contacto o demostración sin perder el contexto consultado. |

#### LAND-US-003 — Revisar capacidades y límites del producto

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-003` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |

| Field | Content |
| --- | --- |
| **Title** | Revisar capacidades y límites del producto |
| **Description** | Como prospecto empresarial, deseo revisar las capacidades y límites públicos del producto, para entender qué problema operativo aborda Nexa antes de continuar. |
| **Acceptance Criteria** | **Scenario 1 — Alcance público**<br>**Given** el prospecto abre el contenido del producto,<br>**When** revisa las capacidades descritas,<br>**Then** relaciona Nexa con resultados operativos de inventario, coordinación de pedidos, cadena de frío o entrega que el sitio comunique.<br><br>**Scenario 2 — Límite explícito**<br>**Given** una capacidad no está descrita en la fuente pública,<br>**When** el prospecto evalúa Nexa,<br>**Then** el contenido no promete una integración o resultado no establecido. |

#### LAND-US-004 — Revisar precios, preguntas frecuentes e información legal

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-004` | Prospective Company Representative | Medium | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |

| Field | Content |
| --- | --- |
| **Title** | Revisar precios, preguntas frecuentes e información legal |
| **Description** | Como prospecto empresarial, deseo consultar precios, preguntas frecuentes y condiciones legales, para evaluar el siguiente paso con información pública suficiente. |
| **Acceptance Criteria** | **Scenario 1 — Información pública disponible**<br>**Given** el prospecto necesita contexto comercial o legal,<br>**When** abre la sección correspondiente,<br>**Then** encuentra la información que la Landing publica.<br><br>**Scenario 2 — Pregunta sin respuesta**<br>**Given** el contenido público no responde una pregunta,<br>**When** el prospecto busca continuar,<br>**Then** obtiene una ruta de contacto o demostración en lugar de una respuesta inventada. |

#### LAND-US-005 — Iniciar el onboarding de una empresa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-005` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |

| Field | Content |
| --- | --- |
| **Title** | Iniciar el onboarding de una empresa |
| **Description** | Como **Prospective Company Representative**, deseo iniciar el onboarding de mi empresa desde la Landing, para solicitar un siguiente paso comercial sin que se cree ni active automáticamente un Tenant o Workspace. |
| **Acceptance Criteria** | **Scenario 1 — Solicitud válida**<br>**Given** el prospecto proporciona la información de empresa y contacto requerida<br>**When** envía la solicitud de onboarding<br>**Then** Nexa confirma únicamente la recepción de la solicitud y el siguiente paso disponible.<br><br>**Scenario 2 — Datos insuficientes**<br>**Given** faltan datos requeridos o no cumplen el formato<br>**When** el prospecto intenta enviar la solicitud<br>**Then** la Landing identifica la información pendiente sin afirmar que existe un Tenant o Workspace.<br><br>**Scenario 3 — Servicio no disponible**<br>**Given** el servicio de onboarding no responde<br>**When** el prospecto envía la solicitud<br>**Then** la Landing muestra un resultado no confirmado u ofrece contacto alternativo sin declarar un onboarding exitoso. |

#### LAND-US-006 — Contactar a Nexa o solicitar una demostración

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-006` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |

| Field | Content |
| --- | --- |
| **Title** | Contactar a Nexa o solicitar una demostración |
| **Description** | Como prospecto empresarial, deseo contactar a Nexa o solicitar una demostración, para obtener un siguiente paso comercial explícito cuando la información pública no sea suficiente. |
| **Acceptance Criteria** | **Scenario 1 — Solicitud válida**<br>**Given** el prospecto proporciona el contexto requerido,<br>**When** envía la solicitud de contacto o demostración,<br>**Then** la Landing comunica sólo el resultado real del envío.<br><br>**Scenario 2 — Datos inválidos**<br>**Given** falta un dato obligatorio o no cumple el formato,<br>**When** el prospecto envía la solicitud,<br>**Then** la Landing identifica la validación pendiente y no afirma que la solicitud fue recibida.<br><br>**Scenario 3 — Servicio no disponible**<br>**Given** el servicio de contacto no responde,<br>**When** el prospecto envía la solicitud,<br>**Then** la Landing muestra un fallo explícito y no confirma un contacto inexistente. |

## Mobile Functional User Stories

#### MOB-US-001 — Continuar el trabajo autorizado después de volver a Nexa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-001` | Mobile User | High | `MOBILE-EPIC-01` — Acceso seguro y contexto de trabajo |

| Field | Content |
| --- | --- |
| **Title** | Continuar el trabajo autorizado después de volver a Nexa |
| **Description** | Como **Mobile User**, deseo continuar de forma segura el trabajo autorizado al volver a Nexa, para reanudarlo sin exponer información protegida. |
| **Acceptance Criteria** | **Scenario 1 — Retorno válido**<br>**Given** una sesión válida y no revocada<br>**When** la persona vuelve a Nexa<br>**Then** Nexa confirma su identidad y expone solo el trabajo permitido.<br><br>**Scenario 2 — Retorno expirado**<br>**Given** una sesión expirada, revocada o malformada<br>**When** la persona vuelve<br>**Then** Nexa solicita nuevamente su identidad y no expone información protegida.<br><br>**Scenario 3 — Confirmación no disponible**<br>**Given** no se puede confirmar la identidad<br>**When** la persona vuelve sin conexión<br>**Then** Nexa indica que el trabajo no está disponible y no expone información protegida.<br><br>**Scenario 4 — Reintento seguro**<br>**Given** la persona repite el mismo retorno<br>**When** Nexa lo procesa<br>**Then** no duplica ninguna acción de negocio ni revela secretos. |

#### MOB-US-002 — Trabajar en la empresa y contexto de negocio previstos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-002` | Mobile User | High | `MOBILE-EPIC-01` — Acceso seguro y contexto de trabajo |

| Field | Content |
| --- | --- |
| **Title** | Trabajar en la empresa y contexto de negocio previstos |
| **Description** | Como **Mobile User**, deseo trabajar en la empresa y contexto de negocio previstos, para que cada tarea corresponda a la empresa y relación que pretendo atender. |
| **Acceptance Criteria** | **Scenario 1 — Un contexto autorizado**<br>**Given** existe un contexto autorizado<br>**When** la persona inicia el trabajo<br>**Then** Nexa usa ese contexto para cada lectura y acción permitida.<br><br>**Scenario 2 — Varios contextos autorizados**<br>**Given** existen varios contextos<br>**When** la persona elige uno<br>**Then** Nexa confirma la elección antes de mostrar trabajo protegido.<br><br>**Scenario 3 — Contexto ya no válido**<br>**Given** un contexto está suspendido o no autorizado<br>**When** la persona lo elige<br>**Then** Nexa lo rechaza y no expone información empresarial de ese alcance.<br><br>**Scenario 4 — Cambio de contexto**<br>**Given** la persona cambia de contexto<br>**When** el cambio tiene éxito<br>**Then** la información del contexto anterior no puede utilizarse en el nuevo. |

#### MOB-US-003 — Ver sólo el trabajo permitido para el rol

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-003` | Mobile User | High | `MOBILE-EPIC-01` — Acceso seguro y contexto de trabajo |

| Field | Content |
| --- | --- |
| **Title** | Ver sólo el trabajo permitido para el rol |
| **Description** | Como **Mobile User**, deseo ver solo el trabajo permitido para mi rol, para no intentar tareas que mi rol o relación no autorizan. |
| **Acceptance Criteria** | **Scenario 1 — Trabajo permitido**<br>**Given** el rol de la persona permite una tarea<br>**When** Nexa confirma el rol<br>**Then** la persona puede realizarla en el contexto activo.<br><br>**Scenario 2 — Permiso faltante**<br>**Given** el rol no permite una tarea<br>**When** la persona intenta realizarla<br>**Then** Nexa la rechaza aunque información antigua sugiera lo contrario.<br><br>**Scenario 3 — Cambio de permisos**<br>**Given** cambian los permisos<br>**When** Nexa vuelve a comprobar el rol<br>**Then** el trabajo no disponible deja de aceptarse.<br><br>**Scenario 4 — Permiso no confirmado**<br>**Given** no se puede comprobar el permiso<br>**When** la persona intenta una tarea<br>**Then** Nexa la bloquea e indica que se requiere confirmación. |

#### MOB-US-004 — Revisar el trabajo operativo de un vistazo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-004` | Business Operations Manager | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Revisar el trabajo operativo de un vistazo |
| **Description** | Como **Business Operations Manager**, deseo revisar el trabajo operativo de un vistazo, para priorizarlo usando hechos actuales y confiables. |
| **Acceptance Criteria** | **Scenario 1 — Vista futura**<br>**Given** existe una vista operativa futura aceptada<br>**When** el responsable la revisa<br>**Then** cada elemento indica su contexto y frescura.<br><br>**Scenario 2 — Hechos incompletos**<br>**Given** faltan hechos fuente o están desactualizados<br>**When** el responsable revisa la vista<br>**Then** la limitación es explícita y no se inventa ningún total.<br><br>**Scenario 3 — Alcance no autorizado**<br>**Given** el responsable carece de permiso de alcance<br>**When** solicita la vista<br>**Then** no se expone información operativa privada. |

#### MOB-US-005 — Identificar excepciones operativas críticas

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-005` | Business Operations Manager | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Identificar excepciones operativas críticas |
| **Description** | Como **Business Operations Manager**, deseo identificar excepciones operativas críticas, para atender trabajo bloqueado antes de que retrase a un cliente o una entrega. |
| **Acceptance Criteria** | **Scenario 1 — Excepción aceptada**<br>**Given** existe una futura vista de excepciones aceptada<br>**When** el responsable revisa un elemento<br>**Then** quedan claros su alcance, severidad y trabajo responsable.<br><br>**Scenario 2 — Excepción incompleta**<br>**Given** los hechos de la excepción están incompletos<br>**When** se revisa el elemento<br>**Then** se marca como incompleto y no se trata como un nuevo estado de negocio.<br><br>**Scenario 3 — Respuesta autorizada**<br>**Given** una excepción requiere corrección<br>**When** el responsable la sigue<br>**Then** Nexa dirige a la persona al trabajo responsable autorizado. |

#### MOB-US-006 — Encontrar un cliente y su relación con el comprador

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-006` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Encontrar un cliente y su relación con el comprador |
| **Description** | Como **Sales Representative**, deseo encontrar una relación entre cliente y comprador, para trabajar con el cliente correcto en un flujo móvil futuro. |
| **Acceptance Criteria** | **Scenario 1 — cliente autorizado**<br>**Given** existe una relación autorizada<br>**When** el representante busca<br>**Then** solo se devuelven clientes permitidos.<br><br>**Scenario 2 — cliente no relacionado**<br>**Given** el cliente no está relacionado o está suspendido<br>**When** el representante lo abre<br>**Then** el trabajo protegido no está disponible.<br><br>**Scenario 3 — Resultado no confiable**<br>**Given** la búsqueda está vacía o no disponible<br>**When** termina<br>**Then** no se adivina ni expone ningún cliente. |

#### MOB-US-007 — Revisar productos, precios y disponibilidad

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-007` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Revisar productos, precios y disponibilidad |
| **Description** | Como **Sales Representative**, deseo revisar productos, precios y disponibilidad, para preparar demanda futura de un cliente con información confiable. |
| **Acceptance Criteria** | **Scenario 1 — Producto autorizado**<br>**Given** existe una relación autorizada con el cliente<br>**When** se revisa un producto<br>**Then** se muestran precio y disponibilidad permitidos con su frescura.<br><br>**Scenario 2 — Producto no disponible**<br>**Given** un producto está oculto o no disponible<br>**When** se solicita<br>**Then** no puede tratarse como un compromiso.<br><br>**Scenario 3 — Información modificada**<br>**Given** cambia el precio o disponibilidad<br>**When** el representante continúa<br>**Then** Nexa exige confirmación actual. |

#### MOB-US-008 — Preparar una solicitud de cliente

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-008` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Preparar una solicitud de cliente |
| **Description** | Como **Sales Representative**, deseo preparar una solicitud de cliente, para organizar una intención antes de un envío autorizado. |
| **Acceptance Criteria** | **Scenario 1 — Preparación de borrador**<br>**Given** se conocen productos permitidos<br>**When** el representante prepara una solicitud<br>**Then** las cantidades permanecen como intención y no crean compromiso.<br><br>**Scenario 2 — Información modificada**<br>**Given** cambia información del producto o cliente<br>**When** se revisa la solicitud<br>**Then** el cambio es visible antes de la envío.<br><br>**Scenario 3 — borrador local**<br>**Given** la persona pierde conexión<br>**When** edita la solicitud<br>**Then** permanece como borrador no confirmado. |

#### MOB-US-009 — Enviar una solicitud o Direct Order asistido desde el trabajo de campo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-009` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Enviar una solicitud o Direct Order asistido desde el trabajo de campo |
| **Description** | Como Representante de Ventas autorizado, deseo enviar la intención comercial del cliente conforme a la política del Tenant, para convertir el trabajo de campo en una solicitud o compromiso válido sin suplantar al comprador. |
| **Acceptance Criteria** | **Scenario 1 — Política APPROVAL_REQUIRED**<br>**Given** el actor es un Representante de Ventas autorizado, existe Customer Account y Buyer Relationship con elegibilidad válida, la política comercial es APPROVAL_REQUIRED y existe un Sales Draft válido<br>**When** envía la intención comercial<br>**Then** Nexa crea y envía una Purchase Request, no confirma un Direct Order y mantiene al actor como Representante de Ventas sin suplantar al Comprador.<br><br>**Scenario 2 — Direct Order asistido**<br>**Given** el actor es un Representante de Ventas autorizado, existe Customer Account y Buyer Relationship con elegibilidad válida, la política comercial es DIRECT_ORDER y existe un Sales Draft válido<br>**When** confirma el Direct Order asistido<br>**Then** el servidor revalida autorización, relación, offer, price, terms, inventory protection y applicable credit y sólo confirma el compromiso si todas las decisiones tienen éxito, sin crear una Purchase Request artificial.<br><br>**Scenario 3 — Actor y borrador separados**<br>**Given** el Representante de Ventas trabaja dentro de su propia relación y existe un Sales Draft<br>**When** envía la intención comercial<br>**Then** el actor continúa siendo Representante de Ventas, Sales Draft != Buyer Draft y Nexa no suplanta al Comprador.<br><br>**Scenario 4 — Validación rechazada**<br>**Given** falla Customer Account, Buyer Relationship, offer, price, terms, inventory protection, applicable credit o autorización<br>**When** el representante intenta confirmar la intención<br>**Then** no se confirma un Direct Order válido ni se registra un compromiso parcial.<br><br>**Scenario 5 — Reintento idempotente**<br>**Given** el representante reenvía la misma intención comercial<br>**When** Nexa procesa el reintento<br>**Then** conserva un único resultado comercial y no duplica Purchase Request ni compromiso.<br><br>**Scenario 6 — Política vigente**<br>**Given** la política comercial cambia entre la preparación y el envío<br>**When** el representante envía su Sales Draft<br>**Then** Nexa usa la política vigente y no confirma una ruta que ya no está autorizada. |

#### MOB-US-010 — Seguir compromisos del cliente y crédito

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-010` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Seguir compromisos del cliente y crédito |
| **Description** | Como **Sales Representative**, deseo seguir los compromisos y el crédito del cliente, para comprender el progreso autorizado sin tomar localmente una decisión de crédito. |
| **Acceptance Criteria** | **Scenario 1 — Progreso autorizado**<br>**Given** existe una relación autorizada<br>**When** se revisa el progreso<br>**Then** los hechos de compromiso y crédito relevante muestran su frescura.<br><br>**Scenario 2 — Hechos financieros incompletos**<br>**Given** los hechos financieros están desactualizados o incompletos<br>**When** se revisan<br>**Then** la limitación es explícita y no se inventa ninguna decisión.<br><br>**Scenario 3 — Pérdida de relación**<br>**Given** la relación ya no está autorizada<br>**When** se solicita el progreso<br>**Then** no se exponen hechos protegidos. |

#### MOB-US-011 — Identificar un producto mediante el código del paquete o etiqueta

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-011` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Identificar un producto mediante el código del paquete o etiqueta |
| **Description** | Como **Warehouse Operator**, deseo identificar un producto desde el código del paquete o etiqueta, para manipular el producto correcto durante el trabajo de almacén. |
| **Acceptance Criteria** | **Scenario 1 — Una coincidencia**<br>**Given** un código permitido tiene una única coincidencia<br>**When** el operador lo proporciona<br>**Then** Nexa identifica el producto antes de cualquier acción de stock.<br><br>**Scenario 2 — Código desconocido**<br>**Given** el código es desconocido, ambiguo o está fuera del alcance de la persona<br>**When** el operador lo proporciona<br>**Then** Nexa lo rechaza y no adivina.<br><br>**Scenario 3 — Cámara no disponible**<br>**Given** la cámara o el scanner no está disponible<br>**When** el operador no puede proporcionar un código<br>**Then** puede usar la búsqueda manual de producto.<br><br>**Scenario 4 — Identificación repetida**<br>**Given** el operador proporciona nuevamente el mismo código<br>**When** Nexa lo resuelve<br>**Then** la identificación por sí sola no crea un hecho de recepción ni de picking. |

#### MOB-US-012 — Buscar manualmente un producto cuando no hay escaneo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-012` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Buscar manualmente un producto cuando no hay escaneo |
| **Description** | Como **Warehouse Operator**, deseo buscar manualmente un producto cuando el escaneo no está disponible, para continuar el trabajo seguro sin adivinar el producto. |
| **Acceptance Criteria** | **Scenario 1 — Coincidencia exacta**<br>**Given** se encuentra un producto permitido exacto<br>**When** el operador lo selecciona<br>**Then** Nexa identifica el producto para el siguiente paso.<br><br>**Scenario 2 — Coincidencia ambigua**<br>**Given** varios productos podrían coincidir<br>**When** el operador busca<br>**Then** Nexa exige una elección clara y no registra ningún hecho de stock.<br><br>**Scenario 3 — Sin conexión**<br>**Given** el operador no tiene conexión<br>**When** no se puede confirmar un producto<br>**Then** Nexa marca la elección como no verificada y bloquea el trabajo autoritativo de stock.<br><br>**Scenario 4 — Selección repetida**<br>**Given** el operador selecciona nuevamente el mismo producto<br>**When** repite la selección<br>**Then** no se duplica ningún hecho de recepción ni picking. |

#### MOB-US-013 — Registrar el stock recién recibido

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-013` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Registrar el stock recién recibido |
| **Description** | Como **Warehouse Operator**, deseo registrar el stock que acaba de llegar, para que el almacén tenga un registro confiable del stock recibido. |
| **Acceptance Criteria** | **Scenario 1 — Llegada válida**<br>**Given** el operador tiene permiso y proporciona producto, lote y cantidad positiva<br>**When** registra la llegada<br>**Then** Nexa registra un único hecho de stock recibido.<br><br>**Scenario 2 — Llegada inválida**<br>**Given** falta información requerida o es inválida<br>**When** el operador la registra<br>**Then** Nexa no realiza un cambio parcial de stock.<br><br>**Scenario 3 — Resultado incierto**<br>**Given** el resultado es desconocido<br>**When** el operador repite la misma llegada<br>**Then** Nexa devuelve el resultado original sin duplicar el stock.<br><br>**Scenario 4 — Sin conexión**<br>**Given** el operador no tiene conexión<br>**When** no se puede confirmar la llegada<br>**Then** Nexa muestra un estado no confirmado y no presenta el stock recibido como autoritativo. |

#### MOB-US-014 — Registrar lote, vencimiento y cantidad reales

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-014` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Registrar lote, vencimiento y cantidad reales |
| **Description** | Como **Warehouse Operator**, deseo registrar el lote, vencimiento y cantidad reales, para que el picking futuro use lo que llegó físicamente. |
| **Acceptance Criteria** | **Scenario 1 — Datos completos del lote**<br>**Given** el operador proporciona lote válido, vencimiento y cantidad positiva<br>**When** confirma la llegada<br>**Then** Nexa conserva esos datos para el stock recibido.<br><br>**Scenario 2 — Vencimiento inválido**<br>**Given** falta el vencimiento, está malformado o no es aceptable<br>**When** el operador lo registra<br>**Then** Nexa rechaza la llegada y no crea stock vendible.<br><br>**Scenario 3 — Llegada duplicada**<br>**Given** se vuelve a enviar la misma llegada<br>**When** Nexa la recibe<br>**Then** permanece una sola llegada y la cantidad no se duplica.<br><br>**Scenario 4 — Preparación local**<br>**Given** el operador pierde conexión<br>**When** prepara datos del lote<br>**Then** permanecen no confirmados y no pueden convertir el stock en vendible. |

#### MOB-US-015 — Comprobar lote y condición del stock antes del trabajo físico

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-015` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Comprobar lote y condición del stock antes del trabajo físico |
| **Description** | Como **Warehouse Operator**, deseo comprobar el lote actual y la condición del stock antes del trabajo físico, para elegir stock seguro y disponible para la tarea. |
| **Acceptance Criteria** | **Scenario 1 — Stock actual**<br>**Given** el operador tiene permiso<br>**When** comprueba el stock<br>**Then** la cantidad física, cantidad vendible, lote y condición aparecen diferenciados.<br><br>**Scenario 2 — Lote restringido**<br>**Given** el stock está vencido, retenido, en cuarentena o asignado<br>**When** se comprueba<br>**Then** no se trata como libremente vendible.<br><br>**Scenario 3 — Información desactualizada**<br>**Given** la información está desactualizada o no disponible<br>**When** el operador inicia el trabajo<br>**Then** Nexa exige confirmación actual.<br><br>**Scenario 4 — Otro alcance**<br>**Given** el lote pertenece a otra empresa o almacén<br>**When** se comprueba<br>**Then** no se expone ningún dato de cantidad ni lote. |

#### MOB-US-016 — Preparar el lote y cantidad correctos para el trabajo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-016` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Preparar el lote y cantidad correctos para el trabajo |
| **Description** | Como **Warehouse Operator**, deseo hacer picking del lote y cantidad correctos para el trabajo preparado, para que la entrega reciba el stock realmente preparado. |
| **Acceptance Criteria** | **Scenario 1 — Picking FEFO**<br>**Given** existe una asignación activa y lotes elegibles<br>**When** el operador selecciona el lote adecuado más antiguo<br>**Then** Nexa registra el picking contra ese lote y cantidad.<br><br>**Scenario 2 — Picking inseguro**<br>**Given** el lote es desconocido, vencido, está en cuarentena o no está asignado<br>**When** el operador intenta seleccionarlo<br>**Then** Nexa rechaza el picking sin consumir stock.<br><br>**Scenario 3 — Exceso de stock**<br>**Given** la cantidad solicitada excede la asignación restante<br>**When** el operador hace picking<br>**Then** Nexa rechaza el exceso y conserva la cantidad restante.<br><br>**Scenario 4 — Picking repetido**<br>**Given** el resultado es desconocido<br>**When** el operador repite el mismo picking<br>**Then** Nexa devuelve un único resultado y no consume stock dos veces. |

#### MOB-US-017 — Reportar una discrepancia física o disposición autorizada de stock

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-017` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Reportar una discrepancia física o disposición autorizada de stock |
| **Description** | Como **Warehouse Operator**, deseo reportar una discrepancia física o disposición autorizada del stock, para mantener visible la excepción sin borrar lo ocurrido. |
| **Acceptance Criteria** | **Scenario 1 — Diferencia observada**<br>**Given** el operador observa una diferencia<br>**When** se acepta el reporte autorizado<br>**Then** las cantidades ofrecidas, seleccionadas y restantes permanecen registradas por separado.<br><br>**Scenario 2 — Autoridad faltante**<br>**Given** falta permiso, motivo o evidencia requerida<br>**When** el operador reporta la diferencia<br>**Then** Nexa no registra ningún cambio de stock no autorizado.<br><br>**Scenario 3 — Reporte repetido**<br>**Given** el resultado es desconocido<br>**When** el operador repite el mismo reporte<br>**Then** Nexa conserva un único hecho de discrepancia.<br><br>**Scenario 4 — Nota sin conexión**<br>**Given** el operador no tiene conexión<br>**When** prepara un reporte<br>**Then** queda marcado como no confirmado y no puede cambiar el stock vendible. |

#### MOB-US-018 — Mover stock entre ubicaciones del almacén

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-018` | Warehouse Operator | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |

| Field | Content |
| --- | --- |
| **Title** | Mover stock entre ubicaciones del almacén |
| **Description** | Como **Warehouse Operator**, deseo mover stock entre ubicaciones del almacén, para que el movimiento físico sea atribuible desde el origen hasta el destino. |
| **Acceptance Criteria** | **Scenario 1 — Movimiento autorizado**<br>**Given** existen origen, destino, lote y cantidad autorizados<br>**When** el operador inicia una transferencia<br>**Then** Nexa conserva esos datos para revisión.<br><br>**Scenario 2 — Dato de transferencia faltante**<br>**Given** falta origen, destino, lote o motivo requerido<br>**When** el operador inicia la transferencia<br>**Then** Nexa deja el stock sin cambios.<br><br>**Scenario 3 — Destino incompatible**<br>**Given** el destino no puede aceptar la transferencia<br>**When** el operador la registra<br>**Then** Nexa mantiene la transferencia sin resolver y no afirma recepción.<br><br>**Scenario 4 — Reintento**<br>**Given** el resultado de la transferencia es desconocido<br>**When** el operador repite el movimiento<br>**Then** permanece una única transferencia trazable. |

#### MOB-US-019 — Registrar evidencia de temperatura para stock relevante

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-019` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |

| Field | Content |
| --- | --- |
| **Title** | Registrar evidencia de temperatura para stock relevante |
| **Description** | Como **Warehouse Operator**, deseo registrar evidencia de temperatura para el stock relevante, para que las decisiones de cadena de frío usen una lectura física atribuible. |
| **Acceptance Criteria** | **Scenario 1 — Lectura válida**<br>**Given** el operador tiene permiso y se conoce un lote o almacén<br>**When** registra una lectura válida<br>**Then** Nexa conserva valor, unidad, momento, persona y sujeto.<br><br>**Scenario 2 — Lectura preocupante**<br>**Given** una lectura está fuera del rango aceptado<br>**When** se registra<br>**Then** Nexa conserva la evidencia y no toma una decisión silenciosa de liberación.<br><br>**Scenario 3 — Lectura incompleta**<br>**Given** falta el sujeto o la unidad<br>**When** se registra la lectura<br>**Then** Nexa la rechaza sin crear evidencia incompleta.<br><br>**Scenario 4 — Fallo temporal**<br>**Given** no se puede confirmar la lectura<br>**When** el operador prepara la evidencia<br>**Then** permanece pendiente y no se afirma una disposición final del stock. |

#### MOB-US-020 — Ver entregas listas para preparar el despacho

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-020` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |

| Field | Content |
| --- | --- |
| **Title** | Ver entregas listas para preparar el despacho |
| **Description** | Como **Dispatch Coordinator**, deseo ver las entregas listas para preparación del despacho, para preparar únicamente entregas listas para salir del almacén. |
| **Acceptance Criteria** | **Scenario 1 — Entrega lista**<br>**Given** una entrega cumple sus condiciones de preparación<br>**When** el coordinador la comprueba<br>**Then** se identifica como lista para trabajo de despacho.<br><br>**Scenario 2 — No lista**<br>**Given** la asignación, picking o evidencia están incompletos<br>**When** el coordinador comprueba la entrega<br>**Then** no se presenta como lista.<br><br>**Scenario 3 — Preparación desactualizada**<br>**Given** la información de disponibilidad está desactualizada<br>**When** el coordinador inicia la preparación<br>**Then** Nexa exige una comprobación actual.<br><br>**Scenario 4 — Alcance incorrecto**<br>**Given** la entrega pertenece a otra empresa o almacén<br>**When** se comprueba<br>**Then** no se expone. |

#### MOB-US-021 — Asignar un conductor a una entrega lista

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-021` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |

| Field | Content |
| --- | --- |
| **Title** | Asignar un conductor a una entrega lista |
| **Description** | Como **Dispatch Coordinator**, deseo asignar un conductor a una entrega lista, para que la responsabilidad quede clara antes del handoff. |
| **Acceptance Criteria** | **Scenario 1 — conductor elegible**<br>**Given** una entrega está lista y un conductor es elegible<br>**When** el coordinador lo asigna<br>**Then** Nexa registra una única asignación.<br><br>**Scenario 2 — Asignación no elegible**<br>**Given** la entrega o el conductor no son elegibles<br>**When** el coordinador realiza la asignación<br>**Then** Nexa la rechaza y no cambia la responsabilidad de la entrega.<br><br>**Scenario 3 — Asignación desactualizada**<br>**Given** la entrega cambió después de ser leída<br>**When** el coordinador asigna el conductor<br>**Then** Nexa solicita información actual en lugar de sobrescribir el cambio.<br><br>**Scenario 4 — Asignación repetida**<br>**Given** el coordinador repite la misma asignación<br>**When** Nexa la recibe<br>**Then** la entrega conserva un único resultado de asignación. |

#### MOB-US-022 — Comprobar bienes salientes contra la entrega preparada

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-022` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |

| Field | Content |
| --- | --- |
| **Title** | Comprobar bienes salientes contra la entrega preparada |
| **Description** | Como **Dispatch Coordinator**, deseo comprobar los bienes salientes contra la entrega preparada, para que el conductor reciba lo que la entrega realmente requiere. |
| **Acceptance Criteria** | **Scenario 1 — Bienes coincidentes**<br>**Given** los bienes salientes coinciden con la asignación actual<br>**When** el coordinador los comprueba<br>**Then** Nexa registra que la preparación del handoff coincide.<br><br>**Scenario 2 — Diferencia**<br>**Given** el lote o cantidad difiere de la asignación<br>**When** el coordinador lo comprueba<br>**Then** Nexa detiene el handoff y conserva la discrepancia.<br><br>**Scenario 3 — Asignación modificada**<br>**Given** la asignación cambió después de la preparación<br>**When** el coordinador comprueba los bienes<br>**Then** Nexa exige una decisión de preparación nueva.<br><br>**Scenario 4 — Comprobación repetida**<br>**Given** se comprueban nuevamente los mismos bienes<br>**When** el coordinador repite la comprobación<br>**Then** la comprobación no crea un segundo movimiento de stock. |

#### MOB-US-023 — Conservar evidencia del handoff entre almacén y conductor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-023` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |

| Field | Content |
| --- | --- |
| **Title** | Conservar evidencia del handoff entre almacén y conductor |
| **Description** | Como **Dispatch Coordinator**, deseo conservar la evidencia del handoff entre almacén y conductor, para que el movimiento de bienes preparados pueda revisarse. |
| **Acceptance Criteria** | **Scenario 1 — Evidencia completa**<br>**Given** se conocen la entrega, los bienes y las personas responsables<br>**When** se registra el handoff<br>**Then** Nexa conserva la evidencia con momento e identidad de entrega.<br><br>**Scenario 2 — Evidencia faltante**<br>**Given** falta evidencia requerida<br>**When** el coordinador registra el handoff<br>**Then** Nexa lo deja no confirmado.<br><br>**Scenario 3 — Fallo de evidencia**<br>**Given** no se puede confirmar la evidencia<br>**When** el coordinador reintenta<br>**Then** Nexa muestra el estado no resuelto y no afirma un handoff completado.<br><br>**Scenario 4 — Handoff repetido**<br>**Given** se vuelve a enviar el mismo handoff<br>**When** Nexa lo recibe<br>**Then** permanece un único hecho de handoff y no se borra evidencia anterior. |

#### MOB-US-024 — Identificar de forma confiable un handoff de despacho

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-024` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |

| Field | Content |
| --- | --- |
| **Title** | Identificar de forma confiable un handoff de despacho |
| **Description** | Como **Dispatch Coordinator**, deseo identificar de forma confiable un handoff de despacho, para mantener vinculados la entrega correcta y el conductor durante todo el handoff. |
| **Acceptance Criteria** | **Scenario 1 — Handoff conocido**<br>**Given** existe una entrega preparada y un conductor asignado<br>**When** el coordinador identifica el handoff<br>**Then** Nexa lo vincula con esa entrega y asignación.<br><br>**Scenario 2 — Handoff incorrecto**<br>**Given** un identificador pertenece a otra entrega<br>**When** se utiliza<br>**Then** Nexa lo rechaza y no cambia ningún hecho de entrega.<br><br>**Scenario 3 — Identidad expirada**<br>**Given** la identidad del handoff ya no es válida<br>**When** se utiliza<br>**Then** Nexa exige un nuevo handoff autorizado.<br><br>**Scenario 4 — Significados separados**<br>**Given** el handoff está identificado<br>**When** se resuelve su identidad<br>**Then** Nexa no lo trata como Driver outcome ni como Buyer Receipt. |

#### MOB-US-025 — Confirmar que los bienes dejaron el control del almacén

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-025` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |

| Field | Content |
| --- | --- |
| **Title** | Confirmar que los bienes dejaron el control del almacén |
| **Description** | Como **Dispatch Coordinator**, deseo confirmar que los bienes dejaron el control del almacén, para que todos puedan confiar en el estado del despacho de la entrega. |
| **Acceptance Criteria** | **Scenario 1 — Handoff completo**<br>**Given** asignación, comprobaciones salientes, asignación del conductor y evidencia de handoff están completas<br>**When** el coordinador confirma el despacho<br>**Then** Nexa registra la entrega como dispatched.<br><br>**Scenario 2 — Handoff incompleto**<br>**Given** cualquier comprobación requerida está incompleta<br>**When** el coordinador confirma el despacho<br>**Then** Nexa deja la entrega como undispatched.<br><br>**Scenario 3 — Entrega modificada**<br>**Given** la entrega cambió después de la preparación<br>**When** el coordinador confirma el despacho<br>**Then** Nexa exige comprobaciones actuales en lugar de sobrescribir el cambio.<br><br>**Scenario 4 — Resultado incierto**<br>**Given** la confirmación pudo tener éxito<br>**When** el coordinador reintenta<br>**Then** Nexa resuelve un único resultado de despacho sin duplicar la transición. |

#### MOB-US-026 — Ver entregas asignadas al conductor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-026` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Ver entregas asignadas al conductor |
| **Description** | Como **Driver / Delivery Operator**, deseo ver las entregas asignadas a mí, para conocer las entregas de las que soy responsable hoy. |
| **Acceptance Criteria** | **Scenario 1 — Asignaciones actuales**<br>**Given** el conductor está autorizado<br>**When** se comprueban sus entregas asignadas<br>**Then** solo se muestran sus entregas actuales.<br><br>**Scenario 2 — Asignación retirada**<br>**Given** se retira una asignación<br>**When** el conductor vuelve a comprobar<br>**Then** la entrega deja de tratarse como asignada.<br><br>**Scenario 3 — Lista desactualizada**<br>**Given** la lista de asignaciones está desactualizada<br>**When** el conductor inicia el trabajo<br>**Then** Nexa exige confirmación actual.<br><br>**Scenario 4 — Entrega de otro conductor**<br>**Given** una entrega pertenece a otro conductor<br>**When** se solicita<br>**Then** no se expone información protegida de la entrega. |

#### MOB-US-027 — Iniciar una entrega asignada

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-027` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Iniciar una entrega asignada |
| **Description** | Como **Driver / Delivery Operator**, deseo iniciar una entrega asignada, para que el Delivery Attempt tenga un inicio claro y autorizado. |
| **Acceptance Criteria** | **Scenario 1 — Inicio asignado**<br>**Given** la entrega está asignada y lista<br>**When** el conductor la inicia<br>**Then** Nexa registra un único Delivery Attempt activo.<br><br>**Scenario 2 — Inicio no asignado**<br>**Given** la entrega no está asignada al conductor<br>**When** intenta iniciarla<br>**Then** Nexa la rechaza y no registra ningún Attempt.<br><br>**Scenario 3 — Ya iniciada**<br>**Given** ya existe un Attempt<br>**When** el conductor la inicia nuevamente<br>**Then** Nexa devuelve el Attempt actual sin crear otro.<br><br>**Scenario 4 — Sin conexión**<br>**Given** no se puede confirmar el inicio<br>**When** el conductor intenta comenzar<br>**Then** Nexa muestra un estado no confirmado y no afirma un Attempt activo. |

#### MOB-US-028 — Abrir indicaciones hacia el destino autorizado de la entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-028` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Abrir indicaciones hacia el destino autorizado de la entrega |
| **Description** | Como **Driver / Delivery Operator**, deseo abrir indicaciones hacia el destino autorizado de la entrega, para viajar al destino correcto sin cambiar el registro de entrega. |
| **Acceptance Criteria** | **Scenario 1 — Destino autorizado**<br>**Given** una entrega activa y autorizada tiene destino<br>**When** el conductor solicita indicaciones<br>**Then** Nexa entrega ese destino al servicio de navegación elegido.<br><br>**Scenario 2 — Destino faltante**<br>**Given** falta el destino o no está autorizado<br>**When** se solicitan indicaciones<br>**Then** Nexa no revela una ubicación no verificada.<br><br>**Scenario 3 — Navegación no disponible**<br>**Given** el servicio de navegación no está disponible<br>**When** se solicitan indicaciones<br>**Then** el Delivery Attempt no cambia y el fallo queda claro.<br><br>**Scenario 4 — Sin seguimiento almacenado**<br>**Given** se abren las indicaciones<br>**When** termina el handoff<br>**Then** Nexa no almacena ubicación continua ni background del conductor por esta acción. |

#### MOB-US-029 — Compartir la ubicación durante una entrega activa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-029` | Driver or Delivery Operator | Low | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |

| Field | Content |
| --- | --- |
| **Title** | Compartir la ubicación durante una entrega activa |
| **Description** | Como **Driver / Delivery Operator**, deseo compartir la ubicación de una entrega durante una entrega activa, para que un servicio de ubicación futuro y aceptado atienda una necesidad acotada de entrega. |
| **Acceptance Criteria** | **Scenario 1 — Consentimiento futuro**<br>**Given** se acepta una política futura de ubicación<br>**When** el conductor comparte una ubicación<br>**Then** consentimiento, alcance y retención quedan explícitos.<br><br>**Scenario 2 — Sin entrega activo**<br>**Given** no existe una entrega activa<br>**When** se solicita la ubicación<br>**Then** no se comparte ninguna ubicación.<br><br>**Scenario 3 — Límite de privacidad**<br>**Given** la persona retira el permiso<br>**When** se solicita compartir ubicación<br>**Then** no se divulga ninguna ubicación nueva. |

#### MOB-US-030 — Contactar al comprador durante la entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-030` | Driver or Delivery Operator | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |

| Field | Content |
| --- | --- |
| **Title** | Contactar al comprador durante la entrega |
| **Description** | Como **Driver / Delivery Operator**, deseo contactar al comprador durante la entrega, para resolver una duda de llegada mediante un canal autorizado. |
| **Acceptance Criteria** | **Scenario 1 — Canal futuro**<br>**Given** existe una política de contacto aceptada<br>**When** el conductor contacta al comprador<br>**Then** solo se usa el canal autorizado y su uso queda registrado.<br><br>**Scenario 2 — Consentimiento faltante**<br>**Given** falta consentimiento o asignación<br>**When** se solicita el contacto<br>**Then** no se inicia contacto personal.<br><br>**Scenario 3 — Resultado separado**<br>**Given** ocurre el contacto<br>**When** termina<br>**Then** por sí mismo no cambia el resultado de entrega ni el Buyer Receipt. |

#### MOB-US-031 — Registrar el resultado del intento de entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-031` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Registrar el resultado del intento de entrega |
| **Description** | Como **Driver / Delivery Operator**, deseo registrar el resultado del intento de entrega, para que el proveedor conozca lo ocurrido físicamente en el destino. |
| **Acceptance Criteria** | **Scenario 1 — Resultado permitido**<br>**Given** existe un Attempt activo y asignado<br>**When** el conductor registra un resultado permitido<br>**Then** Nexa conserva resultado, persona y momento.<br><br>**Scenario 2 — Resultado inválido**<br>**Given** el Attempt no está activo o el conductor no está autorizado<br>**When** se registra un resultado<br>**Then** Nexa no cambia el estado de entrega.<br><br>**Scenario 3 — Evidencia requerida**<br>**Given** el resultado necesita evidencia que falta<br>**When** el conductor lo registra<br>**Then** Nexa deja el resultado no confirmado.<br><br>**Scenario 4 — Resultado repetido**<br>**Given** el resultado es desconocido<br>**When** el conductor repite el mismo resultado<br>**Then** Nexa devuelve un único resultado y no sobrescribe el historial. |

#### MOB-US-032 — Registrar una entrega parcial o rechazada y lo que queda

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-032` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Registrar una entrega parcial o rechazada y lo que queda |
| **Description** | Como **Driver / Delivery Operator**, deseo registrar una entrega parcial o rechazada y lo que queda, para no perder ningún resultado físico ni obligación restante. |
| **Acceptance Criteria** | **Scenario 1 — Entrega parcial**<br>**Given** el conductor proporciona cantidades entregadas y restantes válidas<br>**When** registra el resultado parcial<br>**Then** Nexa conserva por separado las cantidades entregadas, rechazadas y restantes.<br><br>**Scenario 2 — Entrega rechazada**<br>**Given** los bienes son rechazados con un motivo<br>**When** se registra el rechazo<br>**Then** Nexa conserva el motivo y no declara completa la entrega.<br><br>**Scenario 3 — Continuación**<br>**Given** queda cantidad para una entrega futura<br>**When** se confirma el resultado<br>**Then** Nexa crea únicamente la continuación autorizada.<br><br>**Scenario 4 — Resultado incierto**<br>**Given** el resultado es desconocido<br>**When** el conductor reintenta<br>**Then** Nexa devuelve un único resultado y no sobrescribe hechos previos. |

#### MOB-US-033 — Conservar el Proof of Delivery

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-033` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Conservar el Proof of Delivery |
| **Description** | Como **Driver / Delivery Operator**, deseo conservar el Proof of Delivery, para que el resultado de entrega pueda revisarse sin perder su historial. |
| **Acceptance Criteria** | **Scenario 1 — Proof requerido**<br>**Given** el Attempt y los requisitos de evidencia son válidos<br>**When** el conductor proporciona el proof requerido<br>**Then** Nexa conserva su identidad, persona y momento.<br><br>**Scenario 2 — Proof faltante**<br>**Given** falta el proof requerido o es inválido<br>**When** el conductor finaliza el Attempt<br>**Then** Nexa no afirma un proof completado.<br><br>**Scenario 3 — Fallo temporal**<br>**Given** no se puede confirmar el proof<br>**When** el conductor reintenta<br>**Then** Nexa mantiene visible el estado no resuelto y no completa falsamente la entrega.<br><br>**Scenario 4 — Proof repetido**<br>**Given** se proporciona nuevamente el mismo proof<br>**When** Nexa lo recibe<br>**Then** permanece un único hecho de proof y no se borra evidencia anterior. |

#### MOB-US-034 — Presentar un código acotado de handoff de entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-034` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |

| Field | Content |
| --- | --- |
| **Title** | Presentar un código acotado de handoff de entrega |
| **Description** | Como **Driver / Delivery Operator**, deseo presentar un código acotado de handoff de entrega, para que el comprador identifique correctamente la entrega de forma segura. |
| **Acceptance Criteria** | **Scenario 1 — Código válido**<br>**Given** existe una entrega activo y autorizado<br>**When** el conductor presenta su código<br>**Then** Nexa vincula el código con esa entrega y Delivery Attempt.<br><br>**Scenario 2 — Código expirado o incorrecto**<br>**Given** el código está expirado, reutilizado o pertenece a otro entrega<br>**When** se comprueba<br>**Then** Nexa lo rechaza sin cambiar el estado de entrega.<br><br>**Scenario 3 — Código no disponible**<br>**Given** no se puede presentar el código<br>**When** el conductor usa el alternativa aprobado<br>**Then** el handoff permanece explícito y no se registra aceptación falsa.<br><br>**Scenario 4 — Hechos separados**<br>**Given** el comprador verifica el código<br>**When** la verificación tiene éxito<br>**Then** por sí sola no crea recepción, POD, pago ni finalización de entrega. |

#### MOB-US-035 — Continuar la evidencia de entrega después de perder conexión

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-035` | Driver or Delivery Operator | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |

| Field | Content |
| --- | --- |
| **Title** | Continuar la evidencia de entrega después de perder conexión |
| **Description** | Como **Driver / Delivery Operator**, deseo continuar la evidencia de entrega después de perder conexión, para que un flujo futuro de recuperación proteja la evidencia sin afirmar éxito falso. |
| **Acceptance Criteria** | **Scenario 1 — Recuperación futura de evidencia**<br>**Given** se acepta una política futura de recuperación<br>**When** se captura evidencia sin conexión<br>**Then** su estado pendiente y contenido protegido mínimo quedan claros.<br><br>**Scenario 2 — Confirmación posterior**<br>**Given** la evidencia preparada se revisa posteriormente<br>**When** Nexa la acepta<br>**Then** solo el hecho exacto aceptado se vuelve autoritativo.<br><br>**Scenario 3 — Rechazo**<br>**Given** se rechaza la evidencia preparada<br>**When** se revisa<br>**Then** el motivo permanece claro y no se implica éxito de entrega. |

#### MOB-US-036 — Explorar productos del proveedor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-036` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Explorar productos del proveedor |
| **Description** | Como **Customer Buyer**, deseo explorar productos del proveedor, para revisar productos ofrecidos mediante mi relación con el proveedor. |
| **Acceptance Criteria** | **Scenario 1 — Catálogo autorizado**<br>**Given** existe una relación activa de comprador<br>**When** se exploran productos<br>**Then** solo se muestran productos permitidos.<br><br>**Scenario 2 — Relación suspendida**<br>**Given** la relación del comprador está suspendida<br>**When** se exploran productos<br>**Then** no se expone información privada del producto.<br><br>**Scenario 3 — Información desactualizada**<br>**Given** la información del producto está desactualizada<br>**When** se explora<br>**Then** queda marcada como advisory y no crea autoridad para ordenar. |

#### MOB-US-037 — Revisar precio y disponibilidad del producto

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-037` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Revisar precio y disponibilidad del producto |
| **Description** | Como **Customer Buyer**, deseo revisar el precio y disponibilidad del producto, para preparar una solicitud futura con información actual del proveedor. |
| **Acceptance Criteria** | **Scenario 1 — Producto actual**<br>**Given** existe una relación autorizada<br>**When** se revisa un producto<br>**Then** se muestran precio, términos y disponibilidad vendible con frescura.<br><br>**Scenario 2 — Producto desactualizado**<br>**Given** los hechos del producto están desactualizados<br>**When** el comprador continúa<br>**Then** se requiere confirmación actual.<br><br>**Scenario 3 — Producto no disponible**<br>**Given** el producto está oculto o no disponible<br>**When** se solicita<br>**Then** no puede tratarse como compromiso. |

#### MOB-US-038 — Preparar una Purchase Request

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-038` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Preparar una Purchase Request |
| **Description** | Como **Customer Buyer**, deseo preparar una Purchase Request, para organizar una compra futura sin confirmarla falsamente. |
| **Acceptance Criteria** | **Scenario 1 — borrador**<br>**Given** hay productos permitidos disponibles<br>**When** el comprador prepara una solicitud<br>**Then** permanece como borrador y no crea reserva.<br><br>**Scenario 2 — Producto modificado**<br>**Given** cambia el precio o disponibilidad<br>**When** el comprador revisa el borrador<br>**Then** el cambio es claro antes de la envío.<br><br>**Scenario 3 — Preparación local**<br>**Given** el comprador pierde conexión<br>**When** edita el borrador<br>**Then** permanece no confirmado. |

#### MOB-US-039 — Repetir una compra anterior

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-039` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Repetir una compra anterior |
| **Description** | Como **Customer Buyer**, deseo repetir una compra anterior, para preparar una nueva solicitud más rápidamente en un flujo futuro. |
| **Acceptance Criteria** | **Scenario 1 — Historial reutilizado**<br>**Given** el comprador puede acceder al historial anterior<br>**When** lo reutiliza<br>**Then** Nexa crea un nuevo borrador y vuelve a comprobar los datos actuales del producto.<br><br>**Scenario 2 — Producto modificado**<br>**Given** un producto anterior ya no está disponible<br>**When** se reutiliza el historial<br>**Then** Nexa lo marca y no crea un pedido silencioso.<br><br>**Scenario 3 — Acción repetida**<br>**Given** el comprador repite la acción<br>**When** Nexa la procesa<br>**Then** no crea un segundo compromiso. |

#### MOB-US-040 — Enviar una solicitud o realizar un Direct Order

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-040` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Enviar una solicitud o realizar un Direct Order |
| **Description** | Como **Customer Buyer**, deseo enviar una solicitud o realizar un Direct Order, para que mi vía de compromiso elegida sea explícita y autorizada. |
| **Acceptance Criteria** | **Scenario 1 — Purchase Request**<br>**Given** existe un borrador válido y una política válida<br>**When** el comprador envía una solicitud<br>**Then** se registra una única Purchase Request.<br><br>**Scenario 2 — Direct Order**<br>**Given** está permitido ordenar directamente<br>**When** el comprador elige esa vía<br>**Then** se registra una única ruta de Sales Order sin inventar una Purchase Request.<br><br>**Scenario 3 — Hechos modificados**<br>**Given** cambiaron precio, disponibilidad, crédito o permiso<br>**When** el comprador envía<br>**Then** no se registra ningún compromiso parcial. |

#### MOB-US-041 — Responder a un cambio material

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-041` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Responder a un cambio material |
| **Description** | Como **Customer Buyer**, deseo responder a un cambio material, para que mi compromiso futuro refleje una decisión explícita. |
| **Acceptance Criteria** | **Scenario 1 — Aceptar cambio**<br>**Given** existe un cambio actual y autorizado<br>**When** el comprador lo acepta<br>**Then** Nexa registra el cambio versionado.<br><br>**Scenario 2 — Rechazar cambio**<br>**Given** el comprador lo rechaza<br>**When** Nexa registra la decisión<br>**Then** el compromiso original permanece intacto.<br><br>**Scenario 3 — Cambio desactualizado**<br>**Given** el cambio ya no es actual<br>**When** el comprador responde<br>**Then** Nexa solicita la decisión actual y no cambia nada silenciosamente. |

#### MOB-US-042 — Seguir solicitudes y pedidos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-042` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Seguir solicitudes y pedidos |
| **Description** | Como **Customer Buyer**, deseo seguir solicitudes y pedidos, para comprender el progreso comercial autorizado. |
| **Acceptance Criteria** | **Scenario 1 — Historial autorizado**<br>**Given** existe una relación autorizada<br>**When** se revisa el progreso<br>**Then** el estado e historial de solicitud y pedido permanecen diferenciados.<br><br>**Scenario 2 — Progreso actual**<br>**Given** existe una relación autorizada<br>**When** el comprador revisa el progreso<br>**Then** el estado de Purchase Request y Sales Order permanece diferenciado.<br><br>**Scenario 3 — Acceso revocado**<br>**Given** se revoca el acceso<br>**When** se solicita el progreso<br>**Then** no se expone información privada.<br><br>**Scenario 4 — Progreso desactualizado**<br>**Given** el progreso mostrado está desactualizado<br>**When** el comprador hace actualización<br>**Then** Nexa expone el resultado actual o un estado no disponible veraz. |

#### MOB-US-043 — Revisar estado de crédito y pago

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-043` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |

| Field | Content |
| --- | --- |
| **Title** | Revisar estado de crédito y pago |
| **Description** | Como **Customer Buyer**, deseo revisar el estado del crédito y del pago, para comprender lo adeudado sin tratar la evidencia reportada como confirmación. |
| **Acceptance Criteria** | **Scenario 1 — Crédito actual**<br>**Given** existe una relación autorizada<br>**When** se revisa el crédito<br>**Then** importe, moneda, frescura y fuente quedan claros.<br><br>**Scenario 2 — Estado de pago**<br>**Given** existe evidencia de pago<br>**When** el comprador la revisa<br>**Then** los estados reported, confirmed y rejected permanecen diferenciados.<br><br>**Scenario 3 — Estado desactualizado**<br>**Given** el estado de pago está desactualizado<br>**When** el comprador hace actualización<br>**Then** Nexa expone el estado actual o un estado no disponible veraz. |

#### MOB-US-044 — Saber cuándo una entrega requiere atención

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-044` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |

| Field | Content |
| --- | --- |
| **Title** | Saber cuándo una entrega requiere atención |
| **Description** | Como **Customer Buyer**, deseo saber cuándo una entrega requiere atención, para responder oportunamente a un cambio relevante. |
| **Acceptance Criteria** | **Scenario 1 — Actualización relevante**<br>**Given** un hecho permitido de entrega requiere atención del comprador<br>**When** Nexa envía una actualización<br>**Then** el comprador puede identificar la entrega relevante.<br><br>**Scenario 2 — Actualización no relacionada**<br>**Given** la entrega está fuera de la relación del comprador<br>**When** se prepara una actualización<br>**Then** no se revela información privada de la entrega.<br><br>**Scenario 3 — Fallo de entrega**<br>**Given** una actualización no puede entregarse<br>**When** el comprador abre Nexa<br>**Then** los hechos actuales de entrega siguen disponibles para actualización y ningún hecho cambia.<br><br>**Scenario 4 — Reintento de actualización**<br>**Given** una actualización se repite<br>**When** el comprador la recibe<br>**Then** no crea un segundo entrega, recepción ni hecho de discrepancia. |

#### MOB-US-045 — Ver un conductor activo en un mapa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-045` | Customer Buyer | Low | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |

| Field | Content |
| --- | --- |
| **Title** | Ver un conductor activo en un mapa |
| **Description** | Como **Customer Buyer**, deseo ver en un mapa un conductor activo, para que un servicio futuro y autorizado me ayude a comprender el horario de llegada. |
| **Acceptance Criteria** | **Scenario 1 — Ubicación futura**<br>**Given** se acepta una política futura de ubicación<br>**When** el comprador abre una entrega activo<br>**Then** solo se muestra ubicación acotada con consentimiento.<br><br>**Scenario 2 — Sin entrega activo**<br>**Given** no existe una entrega activo<br>**When** el comprador solicita un mapa<br>**Then** no se divulga la ubicación del conductor.<br><br>**Scenario 3 — Límite de privacidad**<br>**Given** falta permiso o relación<br>**When** el comprador solicita un mapa<br>**Then** no se divulga ninguna ubicación. |

#### MOB-US-046 — Contactar al conductor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-046` | Customer Buyer | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |

| Field | Content |
| --- | --- |
| **Title** | Contactar al conductor |
| **Description** | Como **Customer Buyer**, deseo contactar al conductor, para resolver una duda de llegada mediante un canal autorizado de entrega. |
| **Acceptance Criteria** | **Scenario 1 — Canal futuro**<br>**Given** existe una política de canal aceptada y una entrega activo<br>**When** el comprador contacta al conductor<br>**Then** solo se usa el canal autorizado.<br><br>**Scenario 2 — Sin permiso**<br>**Given** falta consentimiento o entrega activo<br>**When** se solicita el contacto<br>**Then** no se inicia contacto personal.<br><br>**Scenario 3 — Hechos separados**<br>**Given** ocurre el contacto<br>**When** termina<br>**Then** no cambia Driver outcome, Buyer Receipt ni el estado de entrega. |

#### MOB-US-047 — Verificar una entrega mediante el código de handoff

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-047` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |

| Field | Content |
| --- | --- |
| **Title** | Verificar una entrega mediante el código de handoff |
| **Description** | Como **Customer Buyer**, deseo verificar una entrega mediante el código de handoff, para confirmar que reviso la entrega correcta. |
| **Acceptance Criteria** | **Scenario 1 — Código coincidente**<br>**Given** existe un código válido, no expirado y una relación autorizada<br>**When** el comprador lo verifica<br>**Then** Nexa identifica la entrega y Delivery Attempt coincidentes.<br><br>**Scenario 2 — Código inválido**<br>**Given** el código está expirado, reutilizado, malformado o no relacionado<br>**When** el comprador lo verifica<br>**Then** Nexa lo rechaza y no cambia ningún hecho de recepción.<br><br>**Scenario 3 — Sin conexión**<br>**Given** no se puede confirmar el código<br>**When** el comprador lo verifica<br>**Then** Nexa muestra un estado no confirmado y ningún recepción tiene éxito.<br><br>**Scenario 4 — Límite de verificación**<br>**Given** el código está verificado<br>**When** el comprador continúa<br>**Then** la verificación por sí sola no confirma cantidades, POD, pago ni finalización de entrega. |

#### MOB-US-048 — Confirmar las cantidades realmente recibidas

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-048` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |

| Field | Content |
| --- | --- |
| **Title** | Confirmar las cantidades realmente recibidas |
| **Description** | Como **Customer Buyer**, deseo confirmar las cantidades realmente recibidas, para que el proveedor tenga un registro veraz de mi Buyer Receipt. |
| **Acceptance Criteria** | **Scenario 1 — recepción coincidente**<br>**Given** existe un handoff verificado y autorizado<br>**When** el comprador confirma las cantidades recibidas<br>**Then** Nexa registra un único hecho de Buyer Receipt con persona, momento y entrega.<br><br>**Scenario 2 — Cantidades diferentes**<br>**Given** las cantidades recibidas difieren del resultado del conductor<br>**When** el comprador las confirma<br>**Then** ambos hechos permanecen separados y la diferencia queda visible.<br><br>**Scenario 3 — Handoff desactualizado o reutilizado**<br>**Given** el handoff está desactualizado, expirado o ya utilizado<br>**When** el comprador confirma cantidades<br>**Then** Nexa rechaza la confirmación o devuelve el resultado original sin un segundo recepción.<br><br>**Scenario 4 — Sin conexión**<br>**Given** no se puede comprobar la confirmación del recepción<br>**When** el comprador lo intenta<br>**Then** Nexa no muestra éxito de recepción hasta recibir confirmación. |

#### MOB-US-049 — Reportar una discrepancia sin borrar los hechos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-049` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |

| Field | Content |
| --- | --- |
| **Title** | Reportar una discrepancia sin borrar los hechos |
| **Description** | Como **Customer Buyer**, deseo reportar una discrepancia sin borrar los hechos, para que el proveedor resuelva la diferencia manteniendo un historial confiable. |
| **Acceptance Criteria** | **Scenario 1 — Discrepancia registrada**<br>**Given** existe un contexto de handoff o recepción verificado<br>**When** el comprador reporta una discrepancia<br>**Then** Nexa conserva motivo, cantidad afectada, persona, momento y evidencia.<br><br>**Scenario 2 — Historiales separados**<br>**Given** el resultado del Driver outcome difiere del Buyer Receipt<br>**When** se registra la discrepancia<br>**Then** ambos hechos originales permanecen sin cambios y la diferencia queda visible.<br><br>**Scenario 3 — Reporte inválido**<br>**Given** falta motivo, permiso o evidencia requerida<br>**When** el comprador lo reporta<br>**Then** Nexa no registra una corrección no autorizada.<br><br>**Scenario 4 — Fallo temporal**<br>**Given** no se puede confirmar el reporte<br>**When** el comprador reintenta<br>**Then** Nexa conserva un único resultado pendiente o aceptado y no implica reembolso, cambio de pago ni finalización de entrega. |


#### MOB-US-050 — Gestionar una discrepancia de recepción con evidencia

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-050` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Gestionar una discrepancia de recepción con evidencia |
| **Description** | Como **Warehouse Operator**, deseo registrar una discrepancia de recepción de entrada con evidencia, para que la decisión de recepción refleje lo encontrado físicamente. |
| **Acceptance Criteria** | **Scenario 1 — Diferencia capturada**<br>**Given** se inspecciona una entrega de entrada<br>**When** el operador registra daño, fuga, producto incorrecto o cantidad incorrecta<br>**Then** Nexa conserva motivo, artículos afectados y evidencia para revisión.<br><br>**Scenario 2 — recepción controlado**<br>**Given** se registra una discrepancia<br>**When** el operador envía el resultado de recepción<br>**Then** Nexa no incrementa el stock vendible más allá de los hechos confirmados.<br><br>**Scenario 3 — Evidencia faltante**<br>**Given** falta un hecho o evidencia requerida<br>**When** el operador intenta enviar la discrepancia<br>**Then** Nexa explica qué falta y no registra una decisión incompleta. |

#### MOB-US-051 — Retener o poner en cuarentena stock y resolverlo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-051` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Retener o poner en cuarentena stock y resolverlo |
| **Description** | Como **Warehouse Operator**, deseo colocar stock cuestionable en retención o cuarentena y registrar su resolución, para impedir su uso antes de una decisión autorizada. |
| **Acceptance Criteria** | **Scenario 1 — Proteger stock**<br>**Given** un lote tiene una condición que impide su uso normal<br>**When** el operador registra el motivo de retención o cuarentena<br>**Then** Nexa retira la cantidad afectada del trabajo disponible aplicable.<br><br>**Scenario 2 — Resolución autorizada**<br>**Given** un lote retenido fue revisado<br>**When** una persona autorizada lo libera o dispone de él<br>**Then** Nexa registra decisión, motivo y cantidad afectada sin borrar el historial de retención.<br><br>**Scenario 3 — Decisión desactualizada**<br>**Given** el lote cambió después de ser visualizado<br>**When** el operador intenta resolverlo<br>**Then** Nexa rechaza la decisión desactualizada y muestra el estado actual. |

#### MOB-US-052 — Confirmar la recepción en el destino de una transferencia interna

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-052` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Confirmar la recepción en el destino de una transferencia interna |
| **Description** | Como **Warehouse Operator**, deseo confirmar lo que llegó al destino de una transferencia interna, para que el registro de stock refleje el movimiento físico y cualquier diferencia. |
| **Acceptance Criteria** | **Scenario 1 — recepción completo**<br>**Given** una transferencia autorizada está en tránsito<br>**When** el operador destino confirma lote y cantidad esperados<br>**Then** Nexa registra destination recepción y cierra el movimiento de transferencia.<br><br>**Scenario 2 — recepción parcial o diferente**<br>**Given** el destino recibe otro lote o cantidad<br>**When** el operador lo registra<br>**Then** Nexa mantiene separados los hechos de origen y destino y expone la diferencia para resolución.<br><br>**Scenario 3 — recepción repetido**<br>**Given** destination recepción ya tiene un resultado aceptado<br>**When** el operador reintenta<br>**Then** Nexa devuelve el resultado original sin un segundo recepción. |

#### MOB-US-053 — Realizar un conteo cíclico y solicitar corrección de stock

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-053` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Realizar un conteo cíclico y solicitar corrección de stock |
| **Description** | Como **Warehouse Operator**, deseo contar una ubicación de almacenamiento y solicitar una corrección de stock, para resolver una diferencia física sin reescribir el historial. |
| **Acceptance Criteria** | **Scenario 1 — Conteo registrado**<br>**Given** existe una ubicación permitida y una vista actual del stock<br>**When** el operador registra lote y cantidad observados<br>**Then** Nexa conserva el conteo con persona, momento y ubicación.<br><br>**Scenario 2 — Corrección revisada**<br>**Given** el conteo difiere del stock registrado<br>**When** se aprueba una corrección autorizada<br>**Then** Nexa registra evidencia correctiva y la cantidad resultante sin borrar movimientos anteriores.<br><br>**Scenario 3 — Cambio concurrente**<br>**Given** el stock cambió después de iniciar el conteo<br>**When** el operador envía la corrección<br>**Then** Nexa rechaza o reabre el conteo desactualizado en lugar de aplicar una corrección última escritura gana. |

#### MOB-US-054 — Solicitar sustitución de lote cuando FEFO no completa el trabajo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-054` | Warehouse Operator | Low | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Solicitar sustitución de lote cuando FEFO no completa el trabajo |
| **Description** | Como **Warehouse Operator**, deseo solicitar una sustitución permitida de lote cuando el lote esperado no puede completar el trabajo, para revisar el pedido sin omitir la política de disponibilidad. |
| **Acceptance Criteria** | **Scenario 1 — Sustitución solicitada**<br>**Given** el lote esperado no puede suministrar la cantidad preparada<br>**When** el operador propone una alternativa elegible<br>**Then** Nexa la envía a decisión autorizada con ambos lotes visibles.<br><br>**Scenario 2 — Decisión controlada**<br>**Given** una sustitución es rechazada o queda desactualizada<br>**When** el operador continúa<br>**Then** Nexa conserva la asignación original y explica la siguiente acción permitida. |

#### MOB-US-055 — Usar información ampliada de identidad de producto, paquete y almacenamiento

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-055` | Warehouse Operator | Low | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Usar información ampliada de identidad de producto, paquete y almacenamiento |
| **Description** | Como **Warehouse Operator**, deseo usar información más rica de identidad de producto, paquete y almacenamiento, para manipular el stock previsto con menos errores de identificación. |
| **Acceptance Criteria** | **Scenario 1 — Identidad resuelta**<br>**Given** existe un identificador permitido de paquete o almacenamiento<br>**When** el operador lo presenta<br>**Then** Nexa muestra el producto correspondiente y el contexto actual antes de iniciar el trabajo.<br><br>**Scenario 2 — Identidad no disponible**<br>**Given** el identificador es desconocido o ilegible<br>**When** el operador intenta continuar<br>**Then** Nexa ofrece un alternativa explícito o indica que se requiere confirmación. |

#### MOB-US-056 — Preparar un grupo de tareas de almacén

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-056` | Warehouse Operator | Low | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |

| Field | Content |
| --- | --- |
| **Title** | Preparar un grupo de tareas de almacén |
| **Description** | Como **Warehouse Operator**, deseo preparar un grupo de tareas de almacén, para trabajar eficientemente sin perder el resultado de cada elemento. |
| **Acceptance Criteria** | **Scenario 1 — Grupo preparado**<br>**Given** hay varias tareas permitidas disponibles<br>**When** el operador las agrupa<br>**Then** Nexa muestra claramente elementos, secuencia y comprobaciones requeridas.<br><br>**Scenario 2 — Un elemento difiere**<br>**Given** una tarea no puede completarse como fue preparada<br>**When** el operador registra la diferencia<br>**Then** Nexa mantiene separados los resultados de las otras tareas e identifica el elemento que requiere revisión. |

#### MOB-US-057 — Resolver una discrepancia de despacho antes del handoff

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-057` | Dispatch Coordinator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Resolver una discrepancia de despacho antes del handoff |
| **Description** | Como **Dispatch Coordinator**, deseo resolver una discrepancia de despacho antes del handoff, para que solo una entrega revisada abandone el control del almacén. |
| **Acceptance Criteria** | **Scenario 1 — Diferencia identificada**<br>**Given** los bienes salientes no coinciden con la entrega preparada<br>**When** el coordinador registra la diferencia<br>**Then** Nexa identifica la entrega, lote o cantidad afectados y bloquea el handoff inseguro.<br><br>**Scenario 2 — Resolución autorizada**<br>**Given** la diferencia tiene una resolución aceptada<br>**When** el coordinador confirma la siguiente acción<br>**Then** Nexa actualiza la disponibilidad de despacho con evidencia trazable.<br><br>**Scenario 3 — Preparación desactualizada**<br>**Given** la entrega cambió después de la preparación<br>**When** el coordinador resuelve la discrepancia<br>**Then** Nexa solicita una decisión nueva en lugar de sobrescribir los hechos actuales. |

#### MOB-US-058 — Reasignar un conductor o reprogramar el despacho de forma segura

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-058` | Dispatch Coordinator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Reasignar un conductor o reprogramar el despacho de forma segura |
| **Description** | Como **Dispatch Coordinator**, deseo reasignar un conductor o reprogramar un despacho de forma segura, para que la entrega siga siendo responsabilidad de una persona elegible en un momento acordado. |
| **Acceptance Criteria** | **Scenario 1 — Reasignación elegible**<br>**Given** una entrega preparada necesita otro conductor<br>**When** el coordinador selecciona una persona elegible<br>**Then** Nexa registra la nueva responsabilidad y conserva el historial de asignación anterior.<br><br>**Scenario 2 — Cambio de horario**<br>**Given** el despacho no puede continuar en el horario previsto<br>**When** el coordinador propone un nuevo horario<br>**Then** Nexa muestra el impacto y confirma el cambio una sola vez.<br><br>**Scenario 3 — Cambio concurrente**<br>**Given** otra persona cambió primero la entrega<br>**When** el coordinador envía el plan antiguo<br>**Then** Nexa lo rechaza y muestra la responsabilidad y horario actuales. |

#### MOB-US-059 — Preparar cargas agrupadas y múltiples paradas

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-059` | Dispatch Coordinator | Low | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Preparar cargas agrupadas y múltiples paradas |
| **Description** | Como **Dispatch Coordinator**, deseo preparar una carga de entrega agrupada con sus paradas, para despachar entregas compatibles manteniendo visibles sus restricciones. |
| **Acceptance Criteria** | **Scenario 1 — Carga compatible**<br>**Given** las entregas cumplen las reglas de agrupación aceptadas<br>**When** el coordinador prepara una carga<br>**Then** Nexa muestra cada entrega, parada y condición requerida.<br><br>**Scenario 2 — Entrega incompatible**<br>**Given** una entrega incumple una regla de cliente o cadena de frío<br>**When** el coordinador prepara la carga<br>**Then** Nexa la mantiene fuera de la carga y explica por qué. |

#### MOB-US-060 — Completar un handoff al transportista con responsabilidad trazable

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-060` | Dispatch Coordinator | Low | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Completar un handoff al transportista con responsabilidad trazable |
| **Description** | Como **Dispatch Coordinator**, deseo completar un handoff al transportista con responsabilidad clara, para que todos sepan quién controla la carga después de que abandona el almacén. |
| **Acceptance Criteria** | **Scenario 1 — Handoff aceptado**<br>**Given** existe una carga preparada y un carrier autorizado<br>**When** el coordinador registra el handoff<br>**Then** Nexa conserva carrier, persona, momento y responsabilidad de entrega.<br><br>**Scenario 2 — Evidencia incompleta**<br>**Given** falta evidencia requerida del handoff<br>**When** el coordinador intenta finalizarlo<br>**Then** Nexa deja la responsabilidad en el responsable actual e indica qué se requiere. |

#### MOB-US-061 — Registrar evidencia de temperatura en el despacho

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-061` | Dispatch Coordinator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Registrar evidencia de temperatura en el despacho |
| **Description** | Como **Dispatch Coordinator**, deseo registrar evidencia de temperatura en el despacho, para que la decisión de entrega refleje la condición observada antes del handoff. |
| **Acceptance Criteria** | **Scenario 1 — Evidencia registrada**<br>**Given** una entrega requiere una comprobación de temperatura<br>**When** el coordinador registra la observación<br>**Then** Nexa conserva valor, unidad, persona, momento y contexto de entrega.<br><br>**Scenario 2 — Fuera de política**<br>**Given** la observación está fuera del rango aceptado<br>**When** el coordinador la envía<br>**Then** Nexa impide un despacho no revisado y muestra la decisión requerida.<br><br>**Scenario 3 — Confirmación faltante**<br>**Given** no se puede confirmar la observación<br>**When** el coordinador reintenta<br>**Then** Nexa no implica aprobación de cadena de frío. |

#### MOB-US-062 — Señalar la llegada de una entrega activa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-062` | Driver or Delivery Operator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Señalar la llegada de una entrega activa |
| **Description** | Como **Driver / Delivery Operator**, deseo señalar la llegada de una entrega activa, para que el comprador y el equipo de entrega sepan que puede comenzar el handoff. |
| **Acceptance Criteria** | **Scenario 1 — Llegada registrada**<br>**Given** el conductor tiene una entrega activo y autorizado<br>**When** señala su llegada<br>**Then** Nexa registra el evento y lo hace visible a destinatarios permitidos.<br><br>**Scenario 2 — Sin entrega activo**<br>**Given** el conductor no está asignado a una entrega activo<br>**When** señala llegada<br>**Then** Nexa rechaza la señal sin revelar otra entrega.<br><br>**Scenario 3 — entrega permanece abierto**<br>**Given** se registró la llegada<br>**When** el comprador o conductor consulta la entrega<br>**Then** permanece abierto hasta registrar por separado handoff y recepción. |

#### MOB-US-063 — Seguir instrucciones de entrega y datos de contacto autorizados

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-063` | Driver or Delivery Operator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Seguir instrucciones de entrega y datos de contacto autorizados |
| **Description** | Como **Driver / Delivery Operator**, deseo seguir las instrucciones y datos de contacto permitidos de la entrega, para coordinar el handoff con la persona prevista. |
| **Acceptance Criteria** | **Scenario 1 — Contexto autorizado**<br>**Given** una entrega activa incluye instrucciones permitidas<br>**When** el conductor las abre<br>**Then** Nexa muestra solo la información necesaria para esa entrega.<br><br>**Scenario 2 — Instrucciones modificadas**<br>**Given** las instrucciones ya no son actuales<br>**When** el conductor las consulta<br>**Then** Nexa las marca como desactualizadas y exige confirmación nueva antes de usarlas.<br><br>**Scenario 3 — Información restringida**<br>**Given** un contacto o instrucción no está permitido para el conductor<br>**When** solicita acceso<br>**Then** Nexa lo oculta y explica la ruta permitida. |

#### MOB-US-064 — Solicitar reprogramación de una entrega desde el campo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-064` | Customer Buyer | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Solicitar reprogramación de una entrega desde el campo |
| **Description** | Como **Customer Buyer**, deseo solicitar un horario de entrega diferente, para que el equipo de entrega decida cómo gestionar mi disponibilidad. |
| **Acceptance Criteria** | **Scenario 1 — solicitud enviada**<br>**Given** el comprador está autorizado para una entrega activa<br>**When** propone un horario alternativo<br>**Then** Nexa registra una solicitud y muestra que espera una decisión de entrega.<br><br>**Scenario 2 — Decisión devuelta**<br>**Given** el equipo de entrega acepta o rechaza la solicitud<br>**When** el comprador consulta la entrega<br>**Then** Nexa muestra la decisión y el horario efectivo sin reescribir hechos anteriores.<br><br>**Scenario 3 — solicitud desactualizada**<br>**Given** la entrega ya es terminal o cambió<br>**When** el comprador envía la solicitud antigua<br>**Then** Nexa la rechaza con el estado actual de la entrega. |

#### MOB-US-065 — Registrar un incidente de entrega con mayor detalle

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-065` | Driver or Delivery Operator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Registrar un incidente de entrega con mayor detalle |
| **Description** | Como **Driver / Delivery Operator**, deseo registrar un incidente de entrega con sus detalles relevantes, para que el equipo tome una decisión de seguimiento informada. |
| **Acceptance Criteria** | **Scenario 1 — Incidente descrito**<br>**Given** una entrega activa encuentra un incidente permitido<br>**When** el conductor registra motivo, lugar dentro de la entrega y evidencia<br>**Then** Nexa conserva el incidente para revisión autorizada.<br><br>**Scenario 2 — El incidente no reescribe el resultado**<br>**Given** ya existe un resultado de entrega<br>**When** se añade un incidente<br>**Then** Nexa conserva el resultado original y vincula la evidencia nueva.<br><br>**Scenario 3 — Incidente incompleto**<br>**Given** faltan detalles requeridos<br>**When** el conductor intenta enviarlo<br>**Then** Nexa identifica la información faltante y no afirma un seguimiento completado. |

#### MOB-US-066 — Recuperar una entrega activa mediante operación offline selectiva

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-066` | Driver or Delivery Operator | Low | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |

| Field | Content |
| --- | --- |
| **Title** | Recuperar una entrega activa mediante operación offline selectiva |
| **Description** | Como **Driver / Delivery Operator**, deseo conservar evidencia seleccionada de entrega durante una pérdida de conexión, para recuperar el trabajo sin afirmar un resultado de entrega no confirmado. |
| **Acceptance Criteria** | **Scenario 1 — Evidencia retenida**<br>**Given** se captura un elemento de evidencia permitido sin conexión<br>**When** el conductor vuelve a tener cobertura<br>**Then** Nexa muestra su estado pendiente y permite revisarlo antes del envío.<br><br>**Scenario 2 — Recuperación autoritativa**<br>**Given** la entrega cambió mientras el dispositivo estaba offline<br>**When** se revisa la evidencia<br>**Then** Nexa resuelve explícitamente el conflicto y nunca aplica silenciosamente un resultado desactualizado. |

#### MOB-US-067 — Proporcionar instrucciones de entrega y contacto alternativo para la recepción

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-067` | Customer Buyer | High | `MOBILE-EPIC-10` — Continuidad de Delivery para Customer Buyer |

| Field | Content |
| --- | --- |
| **Title** | Proporcionar instrucciones de entrega y contacto alternativo para la recepción |
| **Description** | Como **Customer Buyer**, deseo proporcionar instrucciones de entrega y un contacto alternativo para la recepción, para que la entrega llegue a la persona correcta bajo las condiciones acordadas. |
| **Acceptance Criteria** | **Scenario 1 — Instrucciones proporcionadas**<br>**Given** el comprador está autorizado para la entrega<br>**When** guarda instrucciones<br>**Then** Nexa las asocia con esa entrega y muestra su periodo efectivo.<br><br>**Scenario 2 — Consentimiento del contacto alternativo**<br>**Given** una persona alternativa debe recibir la entrega<br>**When** el comprador proporciona contacto permitido y consentimiento<br>**Then** Nexa lo registra únicamente para el propósito de entrega definido.<br><br>**Scenario 3 — Cambio después del despacho**<br>**Given** la entrega está en un estado que no permite cambios<br>**When** el comprador edita instrucciones<br>**Then** Nexa rechaza el cambio o lo dirige a una decisión explícita. |

#### MOB-US-068 — Revisar la línea de tiempo de la entrega y reconocer su finalización

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-068` | Customer Buyer | High | `MOBILE-EPIC-10` — Continuidad de Delivery para Customer Buyer |

| Field | Content |
| --- | --- |
| **Title** | Revisar la línea de tiempo de la entrega y reconocer su finalización |
| **Description** | Como **Customer Buyer**, deseo revisar la línea de tiempo de la entrega y reconocer su finalización, para comprender el resultado registrado sin cambiar el historial. |
| **Acceptance Criteria** | **Scenario 1 — Timeline visible**<br>**Given** el comprador puede acceder a una entrega<br>**When** abre su línea de tiempo<br>**Then** Nexa muestra los hechos autorizados ordenados y su estado actual.<br><br>**Scenario 2 — Acknowledgement separado**<br>**Given** la entrega tiene un resultado registrado<br>**When** el comprador lo reconoce<br>**Then** Nexa registra el acknowledgement separado de recepción, proof o finalización.<br><br>**Scenario 3 — Historial sin cambios**<br>**Given** el comprador reconoce una entrega<br>**When** otra persona permitida la consulta<br>**Then** los hechos subyacentes permanecen sin cambios. |

#### MOB-US-069 — Adjuntar evidencia a una discrepancia de entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-069` | Customer Buyer | High | `MOBILE-EPIC-10` — Continuidad de Delivery para Customer Buyer |

| Field | Content |
| --- | --- |
| **Title** | Adjuntar evidencia a una discrepancia de entrega |
| **Description** | Como **Customer Buyer**, deseo adjuntar evidencia a una discrepancia de entrega, para que el proveedor revise la diferencia reportada con su contexto. |
| **Acceptance Criteria** | **Scenario 1 — Evidencia adjunta**<br>**Given** el comprador tiene una discrepancia permitida<br>**When** añade evidencia<br>**Then** Nexa la vincula con esa discrepancia junto con persona y momento.<br><br>**Scenario 2 — Evidencia no soportada o insegura**<br>**Given** la evidencia no está disponible, es demasiado grande o no está permitida<br>**When** el comprador intenta añadirla<br>**Then** Nexa explica el problema y mantiene la discrepancia sin cambios.<br><br>**Scenario 3 — Hechos originales preservados**<br>**Given** la evidencia es aceptada<br>**When** se revisa la entrega<br>**Then** recepción, Driver outcome y discrepancia permanecen separados. |

#### MOB-US-070 — Ver documentos de negocio vinculados a solicitud o pedido

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-070` | Customer Buyer or Sales Representative | Medium | `MOBILE-EPIC-11` — Seguimiento comercial y financiero |

| Field | Content |
| --- | --- |
| **Title** | Ver documentos de negocio vinculados a solicitud o pedido |
| **Description** | Como **Customer Buyer or Sales Representative**, deseo ver un documento de negocio vinculado a una solicitud o un pedido, para usar la evidencia autorizada del trabajo comercial. |
| **Acceptance Criteria** | **Scenario 1 — Documento autorizado**<br>**Given** un documento emitido pertenece a la relación permitida<br>**When** la persona lo solicita<br>**Then** Nexa proporciona su identidad y contenido autorizado.<br><br>**Scenario 2 — Documento faltante**<br>**Given** no existe un documento emitido<br>**When** la persona lo solicita<br>**Then** Nexa indica que no está disponible y no cambia ningún compromiso.<br><br>**Scenario 3 — Acceso revocado**<br>**Given** se revoca el permiso<br>**When** la persona solicita el documento<br>**Then** Nexa no expone contenido privado. |

#### MOB-US-071 — Reportar evidencia de pago y ver el resultado de revisión

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-071` | Customer Buyer | Medium | `MOBILE-EPIC-11` — Seguimiento comercial y financiero |

| Field | Content |
| --- | --- |
| **Title** | Reportar evidencia de pago y ver el resultado de revisión |
| **Description** | Como **Customer Buyer**, deseo reportar evidencia de pago y ver su resultado de revisión, para seguir un pago sin afirmar yo mismo su confirmación. |
| **Acceptance Criteria** | **Scenario 1 — Evidencia reportada**<br>**Given** están disponibles una referencia, importe y evidencia permitidos<br>**When** el comprador los reporta<br>**Then** Nexa registra el reporte como no confirmado.<br><br>**Scenario 2 — Evidencia revisada**<br>**Given** el proceso responsable revisa el reporte<br>**When** el comprador consulta el estado<br>**Then** Nexa muestra el resultado de revisión sin reescribir el reporte.<br><br>**Scenario 3 — Reporte duplicado**<br>**Given** se vuelve a enviar el mismo reporte<br>**When** Nexa lo recibe<br>**Then** no aplica la evidencia dos veces. |


#### MOB-US-072 — Trabajar con un cliente mediante una visita de campo autorizada

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-072` | Sales Representative | Low | `MOBILE-EPIC-11` — Seguimiento comercial y financiero |

| Field | Content |
| --- | --- |
| **Title** | Trabajar con un cliente mediante una visita de campo autorizada |
| **Description** | Como **Sales Representative**, deseo trabajar con un cliente mediante una visita de campo autorizada, para iniciar con el contexto correcto de relación y terminar con un seguimiento claro. |
| **Acceptance Criteria** | **Scenario 1 — Visita autorizada**<br>**Given** el representante tiene permiso para la relación del cliente<br>**When** inicia una visita<br>**Then** Nexa muestra el contexto permitido del cliente y su propósito.<br><br>**Scenario 2 — Seguimiento capturado**<br>**Given** la visita produce un seguimiento permitido<br>**When** el representante lo registra<br>**Then** Nexa vincula el resultado con la relación del cliente sin crear un compromiso no aprobado. |


#### MOB-US-073 — Usar evidencia de automatización de almacén en un trabajo controlado

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-073` | Warehouse Operator | Future | `MOBILE-EPIC-12` — Automatización de almacén futura |

| Field | Content |
| --- | --- |
| **Title** | Usar evidencia de automatización de almacén en un trabajo controlado |
| **Description** | Como **Warehouse Operator**, deseo revisar observaciones avanzadas de almacén mediante una decisión controlada, para que una automatización futura ayude al trabajo sin convertirse en verdad de stock no examinada. |
| **Acceptance Criteria** | **Scenario 1 — Resultado valioso antes de seleccionar tecnología**<br>**Given** Product explora observaciones avanzadas de almacén<br>**When** define el resultado de almacén antes de seleccionar un dispositivo o proveedor<br>**Then** identifica primero un resultado valioso de almacén.<br><br>**Scenario 2 — Observación automatizada subordinada**<br>**Given** existe una observación automatizada considerada para el trabajo<br>**When** se revisa para apoyar una decisión de almacén<br>**Then** permanece atribuible y revisable y está subordinada a la autorización del responsable del Bounded Context.<br><br>**Scenario 3 — Release sin implementación específica**<br>**Given** el release contempla esta hipótesis de automatización futura<br>**When** se describe su alcance<br>**Then** no promete una implementación específica de RFID, scanner, sensor, label ni telemetry. |
