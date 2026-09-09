# 2.4 Requirements Specification

Esta sección especifica el escenario **To-Be** de Nexa sin presentarlo como
evidencia As-Is ni como una implementación aceptada. Las Functional User
Stories expresan resultados de negocio para actores; las Technical Stories
delimitan habilitación técnica; y los Spikes reducen incertidumbre antes de una
decisión. Ninguno crea una autoridad de negocio alternativa en Mobile.

## To-Be Scenario Mapping

| Escenario objetivo | Actor y proyección | Comportamiento objetivo | Historias relacionadas |
| --- | --- | --- | --- |
| Authorized Mobile Work Context | Mobile User; Operations Mobile y Buyer Mobile | Nexa confirma Tenant, Workspace y permisos antes de exponer trabajo protegido. | MOB-US-001..003 |
| Warehouse Receiving, Identification and Preparation | Warehouse Operator; Operations Mobile | La persona identifica Product/SKU, registra hechos físicos y prepara trabajo con lote, condición y evidencia. | MOB-US-011..017, MOB-US-019 |
| Dispatch Readiness and Handoff | Dispatch Coordinator; Operations Mobile | La persona verifica bienes, asigna responsabilidad y registra un Dispatch Handoff revisable. | MOB-US-020..025 |
| Driver Delivery Execution | Driver / Delivery Operator; Operations Mobile | La persona trabaja sobre una Delivery asignada, abre navegación externa cuando corresponde y registra Delivery Attempt, Driver Outcome y Proof of Delivery. | MOB-US-026..034 |
| Buyer Handoff, Receipt and Discrepancy | Customer Buyer; Buyer Mobile | La persona verifica el handoff, declara el Buyer Receipt y comunica discrepancias sin borrar hechos previos. | MOB-US-044, MOB-US-047..049 |
| Acquisition, Contact and Onboarding Initiation | Prospective Company Representative; Landing pública | La Landing explica Nexa, habilita contacto y recibe una solicitud sin crear un Tenant o Workspace como hecho autoritativo. | LAND-US-001..006 |

### Reglas transversales

| Regla | Aplicación en el To-Be |
| --- | --- |
| Autoridad | El servidor confirma y persiste hechos de negocio; el cliente no sustituye esa confirmación. |
| Conectividad | V1 es online-first. Caché segura, borradores y evidencia temporal apoyan continuidad, pero no confirman inventario, crédito, pagos, Sales Orders ni Delivery. |
| Integridad histórica | Una corrección conserva evidencia correctiva o de reversión; no reemplaza silenciosamente un hecho existente. |
| Ubicación | V1 entrega un destino autorizado a navegación externa; no introduce tracking continuo, ETA ni optimización de rutas. |
| Distinciones | Tenant, Workspace, Human Identity, Workforce Membership, Customer Account y Buyer Relationship son distintos. Dispatch Handoff, Driver Outcome y Buyer Receipt también son hechos separados. |

## Artefactos

- [2.4.1 User Stories](./user-stories.md)
- [Technical Stories](./technical-stories.md)
- [Spike Stories](./spike-stories.md)
- [2.4.2 Impact Mapping](../2.4.2-impact-mapping.md)
- [2.4.3 Product Backlog](../2.4.3-product-backlog.md)

V1 contiene 28 Functional User Stories. V2 (35), V3 (9) y V4/Future (1) se
mantienen como roadmap diferido; no se les asigna una aceptación ni una
implementación por aparecer en este informe.

---

# 2.4.1 User Stories

Este catálogo contiene Functional User Stories de la Landing pública y de las
dos proyecciones Mobile. El escenario To-Be, sus reglas transversales y los
límites de autoridad están definidos en
[2.4 Requirements Specification](../../chapter-overview.md). Las Technical Stories
y los Spikes se mantienen separados para no convertir habilitación o
incertidumbre en requisitos de negocio.

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

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>LAND-US-001</td><td>Prospective Company Representative</td><td>High</td><td>LAND-EPIC-01 — Adquisición pública e inicio de onboarding</td></tr>
<tr><th>Title</th><td colspan="3">Comprender la propuesta B2B de Nexa</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Prospective Company Representative</strong>, deseo comprender la propuesta B2B de Nexa para importadores, distribuidores y mayoristas, incluida la especialización de cadena de frío cuando aplique, para decidir si corresponde continuar la evaluación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Propuesta disponible</strong></p><p><strong>Given</strong> una persona abre la Landing pública</p><p><strong>When</strong> revisa la introducción del producto</p><p><strong>Then</strong> identifica el contexto B2B de Nexa sin confundirlo con un ecommerce genérico ni con un producto exclusivo de cadena de frío.</p><p><strong>Scenario: Especialización contextual</strong></p><p><strong>Given</strong> la persona opera con productos que requieren cadena de frío</p><p><strong>When</strong> revisa las capacidades públicas</p><p><strong>Then</strong> encuentra esa especialización explicada como una capacidad aplicable y no como la única finalidad de Nexa.</p></td></tr>
</tbody>
</table>

#### LAND-US-002 — Evaluar el ajuste con el perfil operativo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>LAND-US-002</td><td>Prospective Company Representative</td><td>High</td><td>LAND-EPIC-01 — Adquisición pública e inicio de onboarding</td></tr>
<tr><th>Title</th><td colspan="3">Evaluar el ajuste con el perfil operativo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como prospecto empresarial, deseo contrastar mi perfil operativo con las soluciones de Nexa, para decidir si debo iniciar una conversación o evaluación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Perfil presentado</strong></p><p><strong>Given</strong> el prospecto opera como importador, distribuidor o mayorista,</p><p><strong>When</strong> revisa la solución correspondiente,</p><p><strong>Then</strong> encuentra el contexto operativo descrito por Nexa y, cuando aplique, la especialización de cadena de frío.</p><p><strong>Scenario: Siguiente paso común</strong></p><p><strong>Given</strong> el prospecto combina más de un perfil,</p><p><strong>When</strong> compara las soluciones,</p><p><strong>Then</strong> puede continuar hacia un producto, contacto o demostración sin perder el contexto consultado.</p></td></tr>
</tbody>
</table>

#### LAND-US-003 — Revisar capacidades y límites del producto

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>LAND-US-003</td><td>Prospective Company Representative</td><td>High</td><td>LAND-EPIC-01 — Adquisición pública e inicio de onboarding</td></tr>
<tr><th>Title</th><td colspan="3">Revisar capacidades y límites del producto</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como prospecto empresarial, deseo revisar las capacidades y límites públicos del producto, para entender qué problema operativo aborda Nexa antes de continuar.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Alcance público</strong></p><p><strong>Given</strong> el prospecto abre el contenido del producto,</p><p><strong>When</strong> revisa las capacidades descritas,</p><p><strong>Then</strong> relaciona Nexa con resultados operativos de inventario, coordinación de pedidos, cadena de frío o entrega que el sitio comunique.</p><p><strong>Scenario: Límite explícito</strong></p><p><strong>Given</strong> una capacidad no está descrita en la fuente pública,</p><p><strong>When</strong> el prospecto evalúa Nexa,</p><p><strong>Then</strong> el contenido no promete una integración o resultado no establecido.</p></td></tr>
</tbody>
</table>

#### LAND-US-004 — Revisar precios, preguntas frecuentes e información legal

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>LAND-US-004</td><td>Prospective Company Representative</td><td>Medium</td><td>LAND-EPIC-01 — Adquisición pública e inicio de onboarding</td></tr>
<tr><th>Title</th><td colspan="3">Revisar precios, preguntas frecuentes e información legal</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como prospecto empresarial, deseo consultar precios, preguntas frecuentes y condiciones legales, para evaluar el siguiente paso con información pública suficiente.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Información pública disponible</strong></p><p><strong>Given</strong> el prospecto necesita contexto comercial o legal,</p><p><strong>When</strong> abre la sección correspondiente,</p><p><strong>Then</strong> encuentra la información que la Landing publica.</p><p><strong>Scenario: Pregunta sin respuesta</strong></p><p><strong>Given</strong> el contenido público no responde una pregunta,</p><p><strong>When</strong> el prospecto busca continuar,</p><p><strong>Then</strong> obtiene una ruta de contacto o demostración en lugar de una respuesta inventada.</p></td></tr>
</tbody>
</table>

#### LAND-US-005 — Iniciar el onboarding de una empresa

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>LAND-US-005</td><td>Prospective Company Representative</td><td>High</td><td>LAND-EPIC-01 — Adquisición pública e inicio de onboarding</td></tr>
<tr><th>Title</th><td colspan="3">Iniciar el onboarding de una empresa</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Prospective Company Representative</strong>, deseo iniciar el onboarding de mi empresa desde la Landing, para solicitar un siguiente paso comercial sin que se cree ni active automáticamente un Tenant o Workspace.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Solicitud válida</strong></p><p><strong>Given</strong> el prospecto proporciona la información de empresa y contacto requerida</p><p><strong>When</strong> envía la solicitud de onboarding</p><p><strong>Then</strong> Nexa confirma únicamente la recepción de la solicitud y el siguiente paso disponible.</p><p><strong>Scenario: Datos insuficientes</strong></p><p><strong>Given</strong> faltan datos requeridos o no cumplen el formato</p><p><strong>When</strong> el prospecto intenta enviar la solicitud</p><p><strong>Then</strong> la Landing identifica la información pendiente sin afirmar que existe un Tenant o Workspace.</p><p><strong>Scenario: Servicio no disponible</strong></p><p><strong>Given</strong> el servicio de onboarding no responde</p><p><strong>When</strong> el prospecto envía la solicitud</p><p><strong>Then</strong> la Landing muestra un resultado no confirmado u ofrece contacto alternativo sin declarar un onboarding exitoso.</p></td></tr>
</tbody>
</table>

#### LAND-US-006 — Contactar a Nexa o solicitar una demostración

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>LAND-US-006</td><td>Prospective Company Representative</td><td>High</td><td>LAND-EPIC-01 — Adquisición pública e inicio de onboarding</td></tr>
<tr><th>Title</th><td colspan="3">Contactar a Nexa o solicitar una demostración</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como prospecto empresarial, deseo contactar a Nexa o solicitar una demostración, para obtener un siguiente paso comercial explícito cuando la información pública no sea suficiente.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Solicitud válida</strong></p><p><strong>Given</strong> el prospecto proporciona el contexto requerido,</p><p><strong>When</strong> envía la solicitud de contacto o demostración,</p><p><strong>Then</strong> la Landing comunica sólo el resultado real del envío.</p><p><strong>Scenario: Datos inválidos</strong></p><p><strong>Given</strong> falta un dato obligatorio o no cumple el formato,</p><p><strong>When</strong> el prospecto envía la solicitud,</p><p><strong>Then</strong> la Landing identifica la validación pendiente y no afirma que la solicitud fue recibida.</p><p><strong>Scenario: Servicio no disponible</strong></p><p><strong>Given</strong> el servicio de contacto no responde,</p><p><strong>When</strong> el prospecto envía la solicitud,</p><p><strong>Then</strong> la Landing muestra un fallo explícito y no confirma un contacto inexistente.</p></td></tr>
</tbody>
</table>

#### MOB-US-001 — Continuar el trabajo autorizado después de volver a Nexa

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-001</td><td>Mobile User</td><td>High</td><td>MOBILE-EPIC-01 — Acceso seguro y contexto de trabajo</td></tr>
<tr><th>Title</th><td colspan="3">Continuar el trabajo autorizado después de volver a Nexa</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Mobile User</strong>, deseo continuar de forma segura el trabajo autorizado al volver a Nexa, para reanudarlo sin exponer información protegida.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Retorno válido</strong></p><p><strong>Given</strong> una sesión válida y no revocada</p><p><strong>When</strong> la persona vuelve a Nexa</p><p><strong>Then</strong> Nexa confirma su identidad y expone solo el trabajo permitido.</p><p><strong>Scenario: Retorno expirado</strong></p><p><strong>Given</strong> una sesión expirada, revocada o malformada</p><p><strong>When</strong> la persona vuelve</p><p><strong>Then</strong> Nexa solicita nuevamente su identidad y no expone información protegida.</p><p><strong>Scenario: Confirmación no disponible</strong></p><p><strong>Given</strong> no se puede confirmar la identidad</p><p><strong>When</strong> la persona vuelve sin conexión</p><p><strong>Then</strong> Nexa indica que el trabajo no está disponible y no expone información protegida.</p><p><strong>Scenario: Reintento seguro</strong></p><p><strong>Given</strong> la persona repite el mismo retorno</p><p><strong>When</strong> Nexa lo procesa</p><p><strong>Then</strong> no duplica ninguna acción de negocio ni revela secretos.</p></td></tr>
</tbody>
</table>

#### MOB-US-002 — Trabajar en la empresa y contexto de negocio previstos

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-002</td><td>Mobile User</td><td>High</td><td>MOBILE-EPIC-01 — Acceso seguro y contexto de trabajo</td></tr>
<tr><th>Title</th><td colspan="3">Trabajar en la empresa y contexto de negocio previstos</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Mobile User</strong>, deseo trabajar en la empresa y contexto de negocio previstos, para que cada tarea corresponda a la empresa y relación que pretendo atender.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Un contexto autorizado</strong></p><p><strong>Given</strong> existe un contexto autorizado</p><p><strong>When</strong> la persona inicia el trabajo</p><p><strong>Then</strong> Nexa usa ese contexto para cada lectura y acción permitida.</p><p><strong>Scenario: Varios contextos autorizados</strong></p><p><strong>Given</strong> existen varios contextos</p><p><strong>When</strong> la persona elige uno</p><p><strong>Then</strong> Nexa confirma la elección antes de mostrar trabajo protegido.</p><p><strong>Scenario: Contexto ya no válido</strong></p><p><strong>Given</strong> un contexto está suspendido o no autorizado</p><p><strong>When</strong> la persona lo elige</p><p><strong>Then</strong> Nexa lo rechaza y no expone información empresarial de ese alcance.</p><p><strong>Scenario: Cambio de contexto</strong></p><p><strong>Given</strong> la persona cambia de contexto</p><p><strong>When</strong> el cambio tiene éxito</p><p><strong>Then</strong> la información del contexto anterior no puede utilizarse en el nuevo.</p></td></tr>
</tbody>
</table>

#### MOB-US-003 — Ver sólo el trabajo permitido para el rol

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-003</td><td>Mobile User</td><td>High</td><td>MOBILE-EPIC-01 — Acceso seguro y contexto de trabajo</td></tr>
<tr><th>Title</th><td colspan="3">Ver sólo el trabajo permitido para el rol</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Mobile User</strong>, deseo ver solo el trabajo permitido para mi rol, para no intentar tareas que mi rol o relación no autorizan.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Trabajo permitido</strong></p><p><strong>Given</strong> el rol de la persona permite una tarea</p><p><strong>When</strong> Nexa confirma el rol</p><p><strong>Then</strong> la persona puede realizarla en el contexto activo.</p><p><strong>Scenario: Permiso faltante</strong></p><p><strong>Given</strong> el rol no permite una tarea</p><p><strong>When</strong> la persona intenta realizarla</p><p><strong>Then</strong> Nexa la rechaza aunque información antigua sugiera lo contrario.</p><p><strong>Scenario: Cambio de permisos</strong></p><p><strong>Given</strong> cambian los permisos</p><p><strong>When</strong> Nexa vuelve a comprobar el rol</p><p><strong>Then</strong> el trabajo no disponible deja de aceptarse.</p><p><strong>Scenario: Permiso no confirmado</strong></p><p><strong>Given</strong> no se puede comprobar el permiso</p><p><strong>When</strong> la persona intenta una tarea</p><p><strong>Then</strong> Nexa la bloquea e indica que se requiere confirmación.</p></td></tr>
</tbody>
</table>

#### MOB-US-004 — Revisar el trabajo operativo de un vistazo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-004</td><td>Business Operations Manager</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Revisar el trabajo operativo de un vistazo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Business Operations Manager</strong>, deseo revisar el trabajo operativo de un vistazo, para priorizarlo usando hechos actuales y confiables.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Vista futura</strong></p><p><strong>Given</strong> existe una vista operativa futura aceptada</p><p><strong>When</strong> el responsable la revisa</p><p><strong>Then</strong> cada elemento indica su contexto y frescura.</p><p><strong>Scenario: Hechos incompletos</strong></p><p><strong>Given</strong> faltan hechos fuente o están desactualizados</p><p><strong>When</strong> el responsable revisa la vista</p><p><strong>Then</strong> la limitación es explícita y no se inventa ningún total.</p><p><strong>Scenario: Alcance no autorizado</strong></p><p><strong>Given</strong> el responsable carece de permiso de alcance</p><p><strong>When</strong> solicita la vista</p><p><strong>Then</strong> no se expone información operativa privada.</p></td></tr>
</tbody>
</table>

#### MOB-US-005 — Identificar excepciones operativas críticas

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-005</td><td>Business Operations Manager</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Identificar excepciones operativas críticas</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Business Operations Manager</strong>, deseo identificar excepciones operativas críticas, para atender trabajo bloqueado antes de que retrase a un cliente o una entrega.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Excepción aceptada</strong></p><p><strong>Given</strong> existe una futura vista de excepciones aceptada</p><p><strong>When</strong> el responsable revisa un elemento</p><p><strong>Then</strong> quedan claros su alcance, severidad y trabajo responsable.</p><p><strong>Scenario: Excepción incompleta</strong></p><p><strong>Given</strong> los hechos de la excepción están incompletos</p><p><strong>When</strong> se revisa el elemento</p><p><strong>Then</strong> se marca como incompleto y no se trata como un nuevo estado de negocio.</p><p><strong>Scenario: Respuesta autorizada</strong></p><p><strong>Given</strong> una excepción requiere corrección</p><p><strong>When</strong> el responsable la sigue</p><p><strong>Then</strong> Nexa dirige a la persona al trabajo responsable autorizado.</p></td></tr>
</tbody>
</table>

#### MOB-US-006 — Encontrar un cliente y su relación con el comprador

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-006</td><td>Sales Representative</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Encontrar un cliente y su relación con el comprador</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Sales Representative</strong>, deseo encontrar una relación entre cliente y comprador, para trabajar con el cliente correcto en un flujo móvil futuro.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: cliente autorizado</strong></p><p><strong>Given</strong> existe una relación autorizada</p><p><strong>When</strong> el representante busca</p><p><strong>Then</strong> solo se devuelven clientes permitidos.</p><p><strong>Scenario: cliente no relacionado</strong></p><p><strong>Given</strong> el cliente no está relacionado o está suspendido</p><p><strong>When</strong> el representante lo abre</p><p><strong>Then</strong> el trabajo protegido no está disponible.</p><p><strong>Scenario: Resultado no confiable</strong></p><p><strong>Given</strong> la búsqueda está vacía o no disponible</p><p><strong>When</strong> termina</p><p><strong>Then</strong> no se adivina ni expone ningún cliente.</p></td></tr>
</tbody>
</table>

#### MOB-US-007 — Revisar productos, precios y disponibilidad

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-007</td><td>Sales Representative</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Revisar productos, precios y disponibilidad</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Sales Representative</strong>, deseo revisar productos, precios y disponibilidad, para preparar demanda futura de un cliente con información confiable.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Producto autorizado</strong></p><p><strong>Given</strong> existe una relación autorizada con el cliente</p><p><strong>When</strong> se revisa un producto</p><p><strong>Then</strong> se muestran precio y disponibilidad permitidos con su frescura.</p><p><strong>Scenario: Producto no disponible</strong></p><p><strong>Given</strong> un producto está oculto o no disponible</p><p><strong>When</strong> se solicita</p><p><strong>Then</strong> no puede tratarse como un compromiso.</p><p><strong>Scenario: Información modificada</strong></p><p><strong>Given</strong> cambia el precio o disponibilidad</p><p><strong>When</strong> el representante continúa</p><p><strong>Then</strong> Nexa exige confirmación actual.</p></td></tr>
</tbody>
</table>

#### MOB-US-008 — Preparar una solicitud de cliente

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-008</td><td>Sales Representative</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Preparar una solicitud de cliente</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Sales Representative</strong>, deseo preparar una solicitud de cliente, para organizar una intención antes de un envío autorizado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Preparación de borrador</strong></p><p><strong>Given</strong> se conocen productos permitidos</p><p><strong>When</strong> el representante prepara una solicitud</p><p><strong>Then</strong> las cantidades permanecen como intención y no crean compromiso.</p><p><strong>Scenario: Información modificada</strong></p><p><strong>Given</strong> cambia información del producto o cliente</p><p><strong>When</strong> se revisa la solicitud</p><p><strong>Then</strong> el cambio es visible antes de la envío.</p><p><strong>Scenario: borrador local</strong></p><p><strong>Given</strong> la persona pierde conexión</p><p><strong>When</strong> edita la solicitud</p><p><strong>Then</strong> permanece como borrador no confirmado.</p></td></tr>
</tbody>
</table>

#### MOB-US-009 — Enviar una solicitud o Direct Order asistido desde el trabajo de campo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-009</td><td>Sales Representative</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Enviar una solicitud o Direct Order asistido desde el trabajo de campo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como Representante de Ventas autorizado, deseo enviar la intención comercial del cliente conforme a la política del Tenant, para convertir el trabajo de campo en una solicitud o compromiso válido sin suplantar al comprador.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Política APPROVAL_REQUIRED</strong></p><p><strong>Given</strong> el actor es un Representante de Ventas autorizado, existe Customer Account y Buyer Relationship con elegibilidad válida, la política comercial es APPROVAL_REQUIRED y existe un Sales Draft válido</p><p><strong>When</strong> envía la intención comercial</p><p><strong>Then</strong> Nexa crea y envía una Purchase Request, no confirma un Direct Order y mantiene al actor como Representante de Ventas sin suplantar al Comprador.</p><p><strong>Scenario: Direct Order asistido</strong></p><p><strong>Given</strong> el actor es un Representante de Ventas autorizado, existe Customer Account y Buyer Relationship con elegibilidad válida, la política comercial es DIRECT_ORDER y existe un Sales Draft válido</p><p><strong>When</strong> confirma el Direct Order asistido</p><p><strong>Then</strong> el servidor revalida autorización, relación, offer, price, terms, inventory protection y applicable credit y sólo confirma el compromiso si todas las decisiones tienen éxito, sin crear una Purchase Request artificial.</p><p><strong>Scenario: Actor y borrador separados</strong></p><p><strong>Given</strong> el Representante de Ventas trabaja dentro de su propia relación y existe un Sales Draft</p><p><strong>When</strong> envía la intención comercial</p><p><strong>Then</strong> el actor continúa siendo Representante de Ventas, Sales Draft != Buyer Draft y Nexa no suplanta al Comprador.</p><p><strong>Scenario: Validación rechazada</strong></p><p><strong>Given</strong> falla Customer Account, Buyer Relationship, offer, price, terms, inventory protection, applicable credit o autorización</p><p><strong>When</strong> el representante intenta confirmar la intención</p><p><strong>Then</strong> no se confirma un Direct Order válido ni se registra un compromiso parcial.</p><p><strong>Scenario: Reintento idempotente</strong></p><p><strong>Given</strong> el representante reenvía la misma intención comercial</p><p><strong>When</strong> Nexa procesa el reintento</p><p><strong>Then</strong> conserva un único resultado comercial y no duplica Purchase Request ni compromiso.</p><p><strong>Scenario: Política vigente</strong></p><p><strong>Given</strong> la política comercial cambia entre la preparación y el envío</p><p><strong>When</strong> el representante envía su Sales Draft</p><p><strong>Then</strong> Nexa usa la política vigente y no confirma una ruta que ya no está autorizada.</p></td></tr>
</tbody>
</table>

#### MOB-US-010 — Seguir compromisos del cliente y crédito

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-010</td><td>Sales Representative</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Seguir compromisos del cliente y crédito</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Sales Representative</strong>, deseo seguir los compromisos y el crédito del cliente, para comprender el progreso autorizado sin tomar localmente una decisión de crédito.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Progreso autorizado</strong></p><p><strong>Given</strong> existe una relación autorizada</p><p><strong>When</strong> se revisa el progreso</p><p><strong>Then</strong> los hechos de compromiso y crédito relevante muestran su frescura.</p><p><strong>Scenario: Hechos financieros incompletos</strong></p><p><strong>Given</strong> los hechos financieros están desactualizados o incompletos</p><p><strong>When</strong> se revisan</p><p><strong>Then</strong> la limitación es explícita y no se inventa ninguna decisión.</p><p><strong>Scenario: Pérdida de relación</strong></p><p><strong>Given</strong> la relación ya no está autorizada</p><p><strong>When</strong> se solicita el progreso</p><p><strong>Then</strong> no se exponen hechos protegidos.</p></td></tr>
</tbody>
</table>

#### MOB-US-011 — Identificar un producto mediante el código del paquete o etiqueta

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-011</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Identificar un producto mediante el código del paquete o etiqueta</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo identificar un producto desde el código del paquete o etiqueta, para manipular el producto correcto durante el trabajo de almacén.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Una coincidencia</strong></p><p><strong>Given</strong> un código permitido tiene una única coincidencia</p><p><strong>When</strong> el operador lo proporciona</p><p><strong>Then</strong> Nexa identifica el producto antes de cualquier acción de stock.</p><p><strong>Scenario: Código desconocido</strong></p><p><strong>Given</strong> el código es desconocido, ambiguo o está fuera del alcance de la persona</p><p><strong>When</strong> el operador lo proporciona</p><p><strong>Then</strong> Nexa lo rechaza y no adivina.</p><p><strong>Scenario: Cámara no disponible</strong></p><p><strong>Given</strong> la cámara o el scanner no está disponible</p><p><strong>When</strong> el operador no puede proporcionar un código</p><p><strong>Then</strong> puede usar la búsqueda manual de producto.</p><p><strong>Scenario: Identificación repetida</strong></p><p><strong>Given</strong> el operador proporciona nuevamente el mismo código</p><p><strong>When</strong> Nexa lo resuelve</p><p><strong>Then</strong> la identificación por sí sola no crea un hecho de recepción ni de picking.</p></td></tr>
</tbody>
</table>

#### MOB-US-012 — Buscar manualmente un producto cuando no hay escaneo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-012</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Buscar manualmente un producto cuando no hay escaneo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo buscar manualmente un producto cuando el escaneo no está disponible, para continuar el trabajo seguro sin adivinar el producto.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Coincidencia exacta</strong></p><p><strong>Given</strong> se encuentra un producto permitido exacto</p><p><strong>When</strong> el operador lo selecciona</p><p><strong>Then</strong> Nexa identifica el producto para el siguiente paso.</p><p><strong>Scenario: Coincidencia ambigua</strong></p><p><strong>Given</strong> varios productos podrían coincidir</p><p><strong>When</strong> el operador busca</p><p><strong>Then</strong> Nexa exige una elección clara y no registra ningún hecho de stock.</p><p><strong>Scenario: Sin conexión</strong></p><p><strong>Given</strong> el operador no tiene conexión</p><p><strong>When</strong> no se puede confirmar un producto</p><p><strong>Then</strong> Nexa marca la elección como no verificada y bloquea el trabajo autoritativo de stock.</p><p><strong>Scenario: Selección repetida</strong></p><p><strong>Given</strong> el operador selecciona nuevamente el mismo producto</p><p><strong>When</strong> repite la selección</p><p><strong>Then</strong> no se duplica ningún hecho de recepción ni picking.</p></td></tr>
</tbody>
</table>

#### MOB-US-013 — Registrar el stock recién recibido

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-013</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Registrar el stock recién recibido</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo registrar el stock que acaba de llegar, para que el almacén tenga un registro confiable del stock recibido.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Llegada válida</strong></p><p><strong>Given</strong> el operador tiene permiso y proporciona producto, lote y cantidad positiva</p><p><strong>When</strong> registra la llegada</p><p><strong>Then</strong> Nexa registra un único hecho de stock recibido.</p><p><strong>Scenario: Llegada inválida</strong></p><p><strong>Given</strong> falta información requerida o es inválida</p><p><strong>When</strong> el operador la registra</p><p><strong>Then</strong> Nexa no realiza un cambio parcial de stock.</p><p><strong>Scenario: Resultado incierto</strong></p><p><strong>Given</strong> el resultado es desconocido</p><p><strong>When</strong> el operador repite la misma llegada</p><p><strong>Then</strong> Nexa devuelve el resultado original sin duplicar el stock.</p><p><strong>Scenario: Sin conexión</strong></p><p><strong>Given</strong> el operador no tiene conexión</p><p><strong>When</strong> no se puede confirmar la llegada</p><p><strong>Then</strong> Nexa muestra un estado no confirmado y no presenta el stock recibido como autoritativo.</p></td></tr>
</tbody>
</table>

#### MOB-US-014 — Registrar lote, vencimiento y cantidad reales

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-014</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Registrar lote, vencimiento y cantidad reales</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo registrar el lote, vencimiento y cantidad reales, para que el picking futuro use lo que llegó físicamente.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Datos completos del lote</strong></p><p><strong>Given</strong> el operador proporciona lote válido, vencimiento y cantidad positiva</p><p><strong>When</strong> confirma la llegada</p><p><strong>Then</strong> Nexa conserva esos datos para el stock recibido.</p><p><strong>Scenario: Vencimiento inválido</strong></p><p><strong>Given</strong> falta el vencimiento, está malformado o no es aceptable</p><p><strong>When</strong> el operador lo registra</p><p><strong>Then</strong> Nexa rechaza la llegada y no crea stock vendible.</p><p><strong>Scenario: Llegada duplicada</strong></p><p><strong>Given</strong> se vuelve a enviar la misma llegada</p><p><strong>When</strong> Nexa la recibe</p><p><strong>Then</strong> permanece una sola llegada y la cantidad no se duplica.</p><p><strong>Scenario: Preparación local</strong></p><p><strong>Given</strong> el operador pierde conexión</p><p><strong>When</strong> prepara datos del lote</p><p><strong>Then</strong> permanecen no confirmados y no pueden convertir el stock en vendible.</p></td></tr>
</tbody>
</table>

#### MOB-US-015 — Comprobar lote y condición del stock antes del trabajo físico

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-015</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Comprobar lote y condición del stock antes del trabajo físico</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo comprobar el lote actual y la condición del stock antes del trabajo físico, para elegir stock seguro y disponible para la tarea.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Stock actual</strong></p><p><strong>Given</strong> el operador tiene permiso</p><p><strong>When</strong> comprueba el stock</p><p><strong>Then</strong> la cantidad física, cantidad vendible, lote y condición aparecen diferenciados.</p><p><strong>Scenario: Lote restringido</strong></p><p><strong>Given</strong> el stock está vencido, retenido, en cuarentena o asignado</p><p><strong>When</strong> se comprueba</p><p><strong>Then</strong> no se trata como libremente vendible.</p><p><strong>Scenario: Información desactualizada</strong></p><p><strong>Given</strong> la información está desactualizada o no disponible</p><p><strong>When</strong> el operador inicia el trabajo</p><p><strong>Then</strong> Nexa exige confirmación actual.</p><p><strong>Scenario: Otro alcance</strong></p><p><strong>Given</strong> el lote pertenece a otra empresa o almacén</p><p><strong>When</strong> se comprueba</p><p><strong>Then</strong> no se expone ningún dato de cantidad ni lote.</p></td></tr>
</tbody>
</table>

#### MOB-US-016 — Preparar el lote y cantidad correctos para el trabajo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-016</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Preparar el lote y cantidad correctos para el trabajo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo hacer picking del lote y cantidad correctos para el trabajo preparado, para que la entrega reciba el stock realmente preparado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Picking FEFO</strong></p><p><strong>Given</strong> existe una asignación activa y lotes elegibles</p><p><strong>When</strong> el operador selecciona el lote adecuado más antiguo</p><p><strong>Then</strong> Nexa registra el picking contra ese lote y cantidad.</p><p><strong>Scenario: Picking inseguro</strong></p><p><strong>Given</strong> el lote es desconocido, vencido, está en cuarentena o no está asignado</p><p><strong>When</strong> el operador intenta seleccionarlo</p><p><strong>Then</strong> Nexa rechaza el picking sin consumir stock.</p><p><strong>Scenario: Exceso de stock</strong></p><p><strong>Given</strong> la cantidad solicitada excede la asignación restante</p><p><strong>When</strong> el operador hace picking</p><p><strong>Then</strong> Nexa rechaza el exceso y conserva la cantidad restante.</p><p><strong>Scenario: Picking repetido</strong></p><p><strong>Given</strong> el resultado es desconocido</p><p><strong>When</strong> el operador repite el mismo picking</p><p><strong>Then</strong> Nexa devuelve un único resultado y no consume stock dos veces.</p></td></tr>
</tbody>
</table>

#### MOB-US-017 — Reportar una discrepancia física o disposición autorizada de stock

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-017</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Reportar una discrepancia física o disposición autorizada de stock</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo reportar una discrepancia física o disposición autorizada del stock, para mantener visible la excepción sin borrar lo ocurrido.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Diferencia observada</strong></p><p><strong>Given</strong> el operador observa una diferencia</p><p><strong>When</strong> se acepta el reporte autorizado</p><p><strong>Then</strong> las cantidades ofrecidas, seleccionadas y restantes permanecen registradas por separado.</p><p><strong>Scenario: Autoridad faltante</strong></p><p><strong>Given</strong> falta permiso, motivo o evidencia requerida</p><p><strong>When</strong> el operador reporta la diferencia</p><p><strong>Then</strong> Nexa no registra ningún cambio de stock no autorizado.</p><p><strong>Scenario: Reporte repetido</strong></p><p><strong>Given</strong> el resultado es desconocido</p><p><strong>When</strong> el operador repite el mismo reporte</p><p><strong>Then</strong> Nexa conserva un único hecho de discrepancia.</p><p><strong>Scenario: Nota sin conexión</strong></p><p><strong>Given</strong> el operador no tiene conexión</p><p><strong>When</strong> prepara un reporte</p><p><strong>Then</strong> queda marcado como no confirmado y no puede cambiar el stock vendible.</p></td></tr>
</tbody>
</table>

#### MOB-US-018 — Mover stock entre ubicaciones del almacén

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-018</td><td>Warehouse Operator</td><td>High</td><td>MOBILE-EPIC-07 — Operación de campo avanzada y continuidad selectiva</td></tr>
<tr><th>Title</th><td colspan="3">Mover stock entre ubicaciones del almacén</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo mover stock entre ubicaciones del almacén, para que el movimiento físico sea atribuible desde el origen hasta el destino.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Movimiento autorizado</strong></p><p><strong>Given</strong> existen origen, destino, lote y cantidad autorizados</p><p><strong>When</strong> el operador inicia una transferencia</p><p><strong>Then</strong> Nexa conserva esos datos para revisión.</p><p><strong>Scenario: Dato de transferencia faltante</strong></p><p><strong>Given</strong> falta origen, destino, lote o motivo requerido</p><p><strong>When</strong> el operador inicia la transferencia</p><p><strong>Then</strong> Nexa deja el stock sin cambios.</p><p><strong>Scenario: Destino incompatible</strong></p><p><strong>Given</strong> el destino no puede aceptar la transferencia</p><p><strong>When</strong> el operador la registra</p><p><strong>Then</strong> Nexa mantiene la transferencia sin resolver y no afirma recepción.</p><p><strong>Scenario: Reintento</strong></p><p><strong>Given</strong> el resultado de la transferencia es desconocido</p><p><strong>When</strong> el operador repite el movimiento</p><p><strong>Then</strong> permanece una única transferencia trazable.</p></td></tr>
</tbody>
</table>

#### MOB-US-019 — Registrar evidencia de temperatura para stock relevante

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-019</td><td>Warehouse Operator</td><td>Critical</td><td>MOBILE-EPIC-02 — Recepción, identificación y preparación de almacén</td></tr>
<tr><th>Title</th><td colspan="3">Registrar evidencia de temperatura para stock relevante</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo registrar evidencia de temperatura para el stock relevante, para que las decisiones de cadena de frío usen una lectura física atribuible.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Lectura válida</strong></p><p><strong>Given</strong> el operador tiene permiso y se conoce un lote o almacén</p><p><strong>When</strong> registra una lectura válida</p><p><strong>Then</strong> Nexa conserva valor, unidad, momento, persona y sujeto.</p><p><strong>Scenario: Lectura preocupante</strong></p><p><strong>Given</strong> una lectura está fuera del rango aceptado</p><p><strong>When</strong> se registra</p><p><strong>Then</strong> Nexa conserva la evidencia y no toma una decisión silenciosa de liberación.</p><p><strong>Scenario: Lectura incompleta</strong></p><p><strong>Given</strong> falta el sujeto o la unidad</p><p><strong>When</strong> se registra la lectura</p><p><strong>Then</strong> Nexa la rechaza sin crear evidencia incompleta.</p><p><strong>Scenario: Fallo temporal</strong></p><p><strong>Given</strong> no se puede confirmar la lectura</p><p><strong>When</strong> el operador prepara la evidencia</p><p><strong>Then</strong> permanece pendiente y no se afirma una disposición final del stock.</p></td></tr>
</tbody>
</table>

#### MOB-US-020 — Ver entregas listas para preparar el despacho

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-020</td><td>Dispatch Coordinator</td><td>Critical</td><td>MOBILE-EPIC-03 — Preparación de despacho y Dispatch Handoff</td></tr>
<tr><th>Title</th><td colspan="3">Ver entregas listas para preparar el despacho</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo ver las entregas listas para preparación del despacho, para preparar únicamente entregas listas para salir del almacén.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Entrega lista</strong></p><p><strong>Given</strong> una entrega cumple sus condiciones de preparación</p><p><strong>When</strong> el coordinador la comprueba</p><p><strong>Then</strong> se identifica como lista para trabajo de despacho.</p><p><strong>Scenario: No lista</strong></p><p><strong>Given</strong> la asignación, picking o evidencia están incompletos</p><p><strong>When</strong> el coordinador comprueba la entrega</p><p><strong>Then</strong> no se presenta como lista.</p><p><strong>Scenario: Preparación desactualizada</strong></p><p><strong>Given</strong> la información de disponibilidad está desactualizada</p><p><strong>When</strong> el coordinador inicia la preparación</p><p><strong>Then</strong> Nexa exige una comprobación actual.</p><p><strong>Scenario: Alcance incorrecto</strong></p><p><strong>Given</strong> la entrega pertenece a otra empresa o almacén</p><p><strong>When</strong> se comprueba</p><p><strong>Then</strong> no se expone.</p></td></tr>
</tbody>
</table>

#### MOB-US-021 — Asignar un conductor a una entrega lista

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-021</td><td>Dispatch Coordinator</td><td>Critical</td><td>MOBILE-EPIC-03 — Preparación de despacho y Dispatch Handoff</td></tr>
<tr><th>Title</th><td colspan="3">Asignar un conductor a una entrega lista</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo asignar un conductor a una entrega lista, para que la responsabilidad quede clara antes del handoff.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: conductor elegible</strong></p><p><strong>Given</strong> una entrega está lista y un conductor es elegible</p><p><strong>When</strong> el coordinador lo asigna</p><p><strong>Then</strong> Nexa registra una única asignación.</p><p><strong>Scenario: Asignación no elegible</strong></p><p><strong>Given</strong> la entrega o el conductor no son elegibles</p><p><strong>When</strong> el coordinador realiza la asignación</p><p><strong>Then</strong> Nexa la rechaza y no cambia la responsabilidad de la entrega.</p><p><strong>Scenario: Asignación desactualizada</strong></p><p><strong>Given</strong> la entrega cambió después de ser leída</p><p><strong>When</strong> el coordinador asigna el conductor</p><p><strong>Then</strong> Nexa solicita información actual en lugar de sobrescribir el cambio.</p><p><strong>Scenario: Asignación repetida</strong></p><p><strong>Given</strong> el coordinador repite la misma asignación</p><p><strong>When</strong> Nexa la recibe</p><p><strong>Then</strong> la entrega conserva un único resultado de asignación.</p></td></tr>
</tbody>
</table>

#### MOB-US-022 — Comprobar bienes salientes contra la entrega preparada

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-022</td><td>Dispatch Coordinator</td><td>Critical</td><td>MOBILE-EPIC-03 — Preparación de despacho y Dispatch Handoff</td></tr>
<tr><th>Title</th><td colspan="3">Comprobar bienes salientes contra la entrega preparada</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo comprobar los bienes salientes contra la entrega preparada, para que el conductor reciba lo que la entrega realmente requiere.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Bienes coincidentes</strong></p><p><strong>Given</strong> los bienes salientes coinciden con la asignación actual</p><p><strong>When</strong> el coordinador los comprueba</p><p><strong>Then</strong> Nexa registra que la preparación del handoff coincide.</p><p><strong>Scenario: Diferencia</strong></p><p><strong>Given</strong> el lote o cantidad difiere de la asignación</p><p><strong>When</strong> el coordinador lo comprueba</p><p><strong>Then</strong> Nexa detiene el handoff y conserva la discrepancia.</p><p><strong>Scenario: Asignación modificada</strong></p><p><strong>Given</strong> la asignación cambió después de la preparación</p><p><strong>When</strong> el coordinador comprueba los bienes</p><p><strong>Then</strong> Nexa exige una decisión de preparación nueva.</p><p><strong>Scenario: Comprobación repetida</strong></p><p><strong>Given</strong> se comprueban nuevamente los mismos bienes</p><p><strong>When</strong> el coordinador repite la comprobación</p><p><strong>Then</strong> la comprobación no crea un segundo movimiento de stock.</p></td></tr>
</tbody>
</table>

#### MOB-US-023 — Conservar evidencia del handoff entre almacén y conductor

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-023</td><td>Dispatch Coordinator</td><td>Critical</td><td>MOBILE-EPIC-03 — Preparación de despacho y Dispatch Handoff</td></tr>
<tr><th>Title</th><td colspan="3">Conservar evidencia del handoff entre almacén y conductor</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo conservar la evidencia del handoff entre almacén y conductor, para que el movimiento de bienes preparados pueda revisarse.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Evidencia completa</strong></p><p><strong>Given</strong> se conocen la entrega, los bienes y las personas responsables</p><p><strong>When</strong> se registra el handoff</p><p><strong>Then</strong> Nexa conserva la evidencia con momento e identidad de entrega.</p><p><strong>Scenario: Evidencia faltante</strong></p><p><strong>Given</strong> falta evidencia requerida</p><p><strong>When</strong> el coordinador registra el handoff</p><p><strong>Then</strong> Nexa lo deja no confirmado.</p><p><strong>Scenario: Fallo de evidencia</strong></p><p><strong>Given</strong> no se puede confirmar la evidencia</p><p><strong>When</strong> el coordinador reintenta</p><p><strong>Then</strong> Nexa muestra el estado no resuelto y no afirma un handoff completado.</p><p><strong>Scenario: Handoff repetido</strong></p><p><strong>Given</strong> se vuelve a enviar el mismo handoff</p><p><strong>When</strong> Nexa lo recibe</p><p><strong>Then</strong> permanece un único hecho de handoff y no se borra evidencia anterior.</p></td></tr>
</tbody>
</table>

#### MOB-US-024 — Identificar de forma confiable un handoff de despacho

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-024</td><td>Dispatch Coordinator</td><td>Critical</td><td>MOBILE-EPIC-03 — Preparación de despacho y Dispatch Handoff</td></tr>
<tr><th>Title</th><td colspan="3">Identificar de forma confiable un handoff de despacho</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo identificar de forma confiable un handoff de despacho, para mantener vinculados la entrega correcta y el conductor durante todo el handoff.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Handoff conocido</strong></p><p><strong>Given</strong> existe una entrega preparada y un conductor asignado</p><p><strong>When</strong> el coordinador identifica el handoff</p><p><strong>Then</strong> Nexa lo vincula con esa entrega y asignación.</p><p><strong>Scenario: Handoff incorrecto</strong></p><p><strong>Given</strong> un identificador pertenece a otra entrega</p><p><strong>When</strong> se utiliza</p><p><strong>Then</strong> Nexa lo rechaza y no cambia ningún hecho de entrega.</p><p><strong>Scenario: Identidad expirada</strong></p><p><strong>Given</strong> la identidad del handoff ya no es válida</p><p><strong>When</strong> se utiliza</p><p><strong>Then</strong> Nexa exige un nuevo handoff autorizado.</p><p><strong>Scenario: Significados separados</strong></p><p><strong>Given</strong> el handoff está identificado</p><p><strong>When</strong> se resuelve su identidad</p><p><strong>Then</strong> Nexa no lo trata como Driver outcome ni como Buyer Receipt.</p></td></tr>
</tbody>
</table>

#### MOB-US-025 — Confirmar que los bienes dejaron el control del almacén

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-025</td><td>Dispatch Coordinator</td><td>Critical</td><td>MOBILE-EPIC-03 — Preparación de despacho y Dispatch Handoff</td></tr>
<tr><th>Title</th><td colspan="3">Confirmar que los bienes dejaron el control del almacén</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo confirmar que los bienes dejaron el control del almacén, para que todos puedan confiar en el estado del despacho de la entrega.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Handoff completo</strong></p><p><strong>Given</strong> asignación, comprobaciones salientes, asignación del conductor y evidencia de handoff están completas</p><p><strong>When</strong> el coordinador confirma el despacho</p><p><strong>Then</strong> Nexa registra la entrega como dispatched.</p><p><strong>Scenario: Handoff incompleto</strong></p><p><strong>Given</strong> cualquier comprobación requerida está incompleta</p><p><strong>When</strong> el coordinador confirma el despacho</p><p><strong>Then</strong> Nexa deja la entrega como undispatched.</p><p><strong>Scenario: Entrega modificada</strong></p><p><strong>Given</strong> la entrega cambió después de la preparación</p><p><strong>When</strong> el coordinador confirma el despacho</p><p><strong>Then</strong> Nexa exige comprobaciones actuales en lugar de sobrescribir el cambio.</p><p><strong>Scenario: Resultado incierto</strong></p><p><strong>Given</strong> la confirmación pudo tener éxito</p><p><strong>When</strong> el coordinador reintenta</p><p><strong>Then</strong> Nexa resuelve un único resultado de despacho sin duplicar la transición.</p></td></tr>
</tbody>
</table>

#### MOB-US-026 — Ver entregas asignadas al conductor

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-026</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Ver entregas asignadas al conductor</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo ver las entregas asignadas a mí, para conocer las entregas de las que soy responsable hoy.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Asignaciones actuales</strong></p><p><strong>Given</strong> el conductor está autorizado</p><p><strong>When</strong> se comprueban sus entregas asignadas</p><p><strong>Then</strong> solo se muestran sus entregas actuales.</p><p><strong>Scenario: Asignación retirada</strong></p><p><strong>Given</strong> se retira una asignación</p><p><strong>When</strong> el conductor vuelve a comprobar</p><p><strong>Then</strong> la entrega deja de tratarse como asignada.</p><p><strong>Scenario: Lista desactualizada</strong></p><p><strong>Given</strong> la lista de asignaciones está desactualizada</p><p><strong>When</strong> el conductor inicia el trabajo</p><p><strong>Then</strong> Nexa exige confirmación actual.</p><p><strong>Scenario: Entrega de otro conductor</strong></p><p><strong>Given</strong> una entrega pertenece a otro conductor</p><p><strong>When</strong> se solicita</p><p><strong>Then</strong> no se expone información protegida de la entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-027 — Iniciar una entrega asignada

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-027</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Iniciar una entrega asignada</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo iniciar una entrega asignada, para que el Delivery Attempt tenga un inicio claro y autorizado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Inicio asignado</strong></p><p><strong>Given</strong> la entrega está asignada y lista</p><p><strong>When</strong> el conductor la inicia</p><p><strong>Then</strong> Nexa registra un único Delivery Attempt activo.</p><p><strong>Scenario: Inicio no asignado</strong></p><p><strong>Given</strong> la entrega no está asignada al conductor</p><p><strong>When</strong> intenta iniciarla</p><p><strong>Then</strong> Nexa la rechaza y no registra ningún Attempt.</p><p><strong>Scenario: Ya iniciada</strong></p><p><strong>Given</strong> ya existe un Attempt</p><p><strong>When</strong> el conductor la inicia nuevamente</p><p><strong>Then</strong> Nexa devuelve el Attempt actual sin crear otro.</p><p><strong>Scenario: Sin conexión</strong></p><p><strong>Given</strong> no se puede confirmar el inicio</p><p><strong>When</strong> el conductor intenta comenzar</p><p><strong>Then</strong> Nexa muestra un estado no confirmado y no afirma un Attempt activo.</p></td></tr>
</tbody>
</table>

#### MOB-US-028 — Abrir indicaciones hacia el destino autorizado de la entrega

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-028</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Abrir indicaciones hacia el destino autorizado de la entrega</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo abrir indicaciones hacia el destino autorizado de la entrega, para viajar al destino correcto sin cambiar el registro de entrega.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Destino autorizado</strong></p><p><strong>Given</strong> una entrega activa y autorizada tiene destino</p><p><strong>When</strong> el conductor solicita indicaciones</p><p><strong>Then</strong> Nexa entrega ese destino al servicio de navegación elegido.</p><p><strong>Scenario: Destino faltante</strong></p><p><strong>Given</strong> falta el destino o no está autorizado</p><p><strong>When</strong> se solicitan indicaciones</p><p><strong>Then</strong> Nexa no revela una ubicación no verificada.</p><p><strong>Scenario: Navegación no disponible</strong></p><p><strong>Given</strong> el servicio de navegación no está disponible</p><p><strong>When</strong> se solicitan indicaciones</p><p><strong>Then</strong> el Delivery Attempt no cambia y el fallo queda claro.</p><p><strong>Scenario: Sin seguimiento almacenado</strong></p><p><strong>Given</strong> se abren las indicaciones</p><p><strong>When</strong> termina el handoff</p><p><strong>Then</strong> Nexa no almacena ubicación continua ni background del conductor por esta acción.</p></td></tr>
</tbody>
</table>

#### MOB-US-029 — Compartir la ubicación durante una entrega activa

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-029</td><td>Driver or Delivery Operator</td><td>Low</td><td>MOBILE-EPIC-07 — Operación de campo avanzada y continuidad selectiva</td></tr>
<tr><th>Title</th><td colspan="3">Compartir la ubicación durante una entrega activa</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo compartir la ubicación de una entrega durante una entrega activa, para que un servicio de ubicación futuro y aceptado atienda una necesidad acotada de entrega.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Consentimiento futuro</strong></p><p><strong>Given</strong> se acepta una política futura de ubicación</p><p><strong>When</strong> el conductor comparte una ubicación</p><p><strong>Then</strong> consentimiento, alcance y retención quedan explícitos.</p><p><strong>Scenario: Sin entrega activo</strong></p><p><strong>Given</strong> no existe una entrega activa</p><p><strong>When</strong> se solicita la ubicación</p><p><strong>Then</strong> no se comparte ninguna ubicación.</p><p><strong>Scenario: Límite de privacidad</strong></p><p><strong>Given</strong> la persona retira el permiso</p><p><strong>When</strong> se solicita compartir ubicación</p><p><strong>Then</strong> no se divulga ninguna ubicación nueva.</p></td></tr>
</tbody>
</table>

#### MOB-US-030 — Contactar al comprador durante la entrega

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-030</td><td>Driver or Delivery Operator</td><td>High</td><td>MOBILE-EPIC-07 — Operación de campo avanzada y continuidad selectiva</td></tr>
<tr><th>Title</th><td colspan="3">Contactar al comprador durante la entrega</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo contactar al comprador durante la entrega, para resolver una duda de llegada mediante un canal autorizado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Canal futuro</strong></p><p><strong>Given</strong> existe una política de contacto aceptada</p><p><strong>When</strong> el conductor contacta al comprador</p><p><strong>Then</strong> solo se usa el canal autorizado y su uso queda registrado.</p><p><strong>Scenario: Consentimiento faltante</strong></p><p><strong>Given</strong> falta consentimiento o asignación</p><p><strong>When</strong> se solicita el contacto</p><p><strong>Then</strong> no se inicia contacto personal.</p><p><strong>Scenario: Resultado separado</strong></p><p><strong>Given</strong> ocurre el contacto</p><p><strong>When</strong> termina</p><p><strong>Then</strong> por sí mismo no cambia el resultado de entrega ni el Buyer Receipt.</p></td></tr>
</tbody>
</table>

#### MOB-US-031 — Registrar el resultado del intento de entrega

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-031</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Registrar el resultado del intento de entrega</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo registrar el resultado del intento de entrega, para que el proveedor conozca lo ocurrido físicamente en el destino.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Resultado permitido</strong></p><p><strong>Given</strong> existe un Attempt activo y asignado</p><p><strong>When</strong> el conductor registra un resultado permitido</p><p><strong>Then</strong> Nexa conserva resultado, persona y momento.</p><p><strong>Scenario: Resultado inválido</strong></p><p><strong>Given</strong> el Attempt no está activo o el conductor no está autorizado</p><p><strong>When</strong> se registra un resultado</p><p><strong>Then</strong> Nexa no cambia el estado de entrega.</p><p><strong>Scenario: Evidencia requerida</strong></p><p><strong>Given</strong> el resultado necesita evidencia que falta</p><p><strong>When</strong> el conductor lo registra</p><p><strong>Then</strong> Nexa deja el resultado no confirmado.</p><p><strong>Scenario: Resultado repetido</strong></p><p><strong>Given</strong> el resultado es desconocido</p><p><strong>When</strong> el conductor repite el mismo resultado</p><p><strong>Then</strong> Nexa devuelve un único resultado y no sobrescribe el historial.</p></td></tr>
</tbody>
</table>

#### MOB-US-032 — Registrar una entrega parcial o rechazada y lo que queda

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-032</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Registrar una entrega parcial o rechazada y lo que queda</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo registrar una entrega parcial o rechazada y lo que queda, para no perder ningún resultado físico ni obligación restante.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Entrega parcial</strong></p><p><strong>Given</strong> el conductor proporciona cantidades entregadas y restantes válidas</p><p><strong>When</strong> registra el resultado parcial</p><p><strong>Then</strong> Nexa conserva por separado las cantidades entregadas, rechazadas y restantes.</p><p><strong>Scenario: Entrega rechazada</strong></p><p><strong>Given</strong> los bienes son rechazados con un motivo</p><p><strong>When</strong> se registra el rechazo</p><p><strong>Then</strong> Nexa conserva el motivo y no declara completa la entrega.</p><p><strong>Scenario: Continuación</strong></p><p><strong>Given</strong> queda cantidad para una entrega futura</p><p><strong>When</strong> se confirma el resultado</p><p><strong>Then</strong> Nexa crea únicamente la continuación autorizada.</p><p><strong>Scenario: Resultado incierto</strong></p><p><strong>Given</strong> el resultado es desconocido</p><p><strong>When</strong> el conductor reintenta</p><p><strong>Then</strong> Nexa devuelve un único resultado y no sobrescribe hechos previos.</p></td></tr>
</tbody>
</table>

#### MOB-US-033 — Conservar el Proof of Delivery

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-033</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Conservar el Proof of Delivery</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo conservar el Proof of Delivery, para que el resultado de entrega pueda revisarse sin perder su historial.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Proof requerido</strong></p><p><strong>Given</strong> el Attempt y los requisitos de evidencia son válidos</p><p><strong>When</strong> el conductor proporciona el proof requerido</p><p><strong>Then</strong> Nexa conserva su identidad, persona y momento.</p><p><strong>Scenario: Proof faltante</strong></p><p><strong>Given</strong> falta el proof requerido o es inválido</p><p><strong>When</strong> el conductor finaliza el Attempt</p><p><strong>Then</strong> Nexa no afirma un proof completado.</p><p><strong>Scenario: Fallo temporal</strong></p><p><strong>Given</strong> no se puede confirmar el proof</p><p><strong>When</strong> el conductor reintenta</p><p><strong>Then</strong> Nexa mantiene visible el estado no resuelto y no completa falsamente la entrega.</p><p><strong>Scenario: Proof repetido</strong></p><p><strong>Given</strong> se proporciona nuevamente el mismo proof</p><p><strong>When</strong> Nexa lo recibe</p><p><strong>Then</strong> permanece un único hecho de proof y no se borra evidencia anterior.</p></td></tr>
</tbody>
</table>

#### MOB-US-034 — Presentar un código acotado de handoff de entrega

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-034</td><td>Driver or Delivery Operator</td><td>Critical</td><td>MOBILE-EPIC-04 — Ejecución de Delivery y Proof of Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Presentar un código acotado de handoff de entrega</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo presentar un código acotado de handoff de entrega, para que el comprador identifique correctamente la entrega de forma segura.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Código válido</strong></p><p><strong>Given</strong> existe una entrega activo y autorizado</p><p><strong>When</strong> el conductor presenta su código</p><p><strong>Then</strong> Nexa vincula el código con esa entrega y Delivery Attempt.</p><p><strong>Scenario: Código expirado o incorrecto</strong></p><p><strong>Given</strong> el código está expirado, reutilizado o pertenece a otro entrega</p><p><strong>When</strong> se comprueba</p><p><strong>Then</strong> Nexa lo rechaza sin cambiar el estado de entrega.</p><p><strong>Scenario: Código no disponible</strong></p><p><strong>Given</strong> no se puede presentar el código</p><p><strong>When</strong> el conductor usa el alternativa aprobado</p><p><strong>Then</strong> el handoff permanece explícito y no se registra aceptación falsa.</p><p><strong>Scenario: Hechos separados</strong></p><p><strong>Given</strong> el comprador verifica el código</p><p><strong>When</strong> la verificación tiene éxito</p><p><strong>Then</strong> por sí sola no crea recepción, POD, pago ni finalización de entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-035 — Continuar la evidencia de entrega después de perder conexión

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-035</td><td>Driver or Delivery Operator</td><td>High</td><td>MOBILE-EPIC-07 — Operación de campo avanzada y continuidad selectiva</td></tr>
<tr><th>Title</th><td colspan="3">Continuar la evidencia de entrega después de perder conexión</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo continuar la evidencia de entrega después de perder conexión, para que un flujo futuro de recuperación proteja la evidencia sin afirmar éxito falso.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Recuperación futura de evidencia</strong></p><p><strong>Given</strong> se acepta una política futura de recuperación</p><p><strong>When</strong> se captura evidencia sin conexión</p><p><strong>Then</strong> su estado pendiente y contenido protegido mínimo quedan claros.</p><p><strong>Scenario: Confirmación posterior</strong></p><p><strong>Given</strong> la evidencia preparada se revisa posteriormente</p><p><strong>When</strong> Nexa la acepta</p><p><strong>Then</strong> solo el hecho exacto aceptado se vuelve autoritativo.</p><p><strong>Scenario: Rechazo</strong></p><p><strong>Given</strong> se rechaza la evidencia preparada</p><p><strong>When</strong> se revisa</p><p><strong>Then</strong> el motivo permanece claro y no se implica éxito de entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-036 — Explorar productos del proveedor

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-036</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Explorar productos del proveedor</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo explorar productos del proveedor, para revisar productos ofrecidos mediante mi relación con el proveedor.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Catálogo autorizado</strong></p><p><strong>Given</strong> existe una relación activa de comprador</p><p><strong>When</strong> se exploran productos</p><p><strong>Then</strong> solo se muestran productos permitidos.</p><p><strong>Scenario: Relación suspendida</strong></p><p><strong>Given</strong> la relación del comprador está suspendida</p><p><strong>When</strong> se exploran productos</p><p><strong>Then</strong> no se expone información privada del producto.</p><p><strong>Scenario: Información desactualizada</strong></p><p><strong>Given</strong> la información del producto está desactualizada</p><p><strong>When</strong> se explora</p><p><strong>Then</strong> queda marcada como advisory y no crea autoridad para ordenar.</p></td></tr>
</tbody>
</table>

#### MOB-US-037 — Revisar precio y disponibilidad del producto

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-037</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Revisar precio y disponibilidad del producto</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo revisar el precio y disponibilidad del producto, para preparar una solicitud futura con información actual del proveedor.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Producto actual</strong></p><p><strong>Given</strong> existe una relación autorizada</p><p><strong>When</strong> se revisa un producto</p><p><strong>Then</strong> se muestran precio, términos y disponibilidad vendible con frescura.</p><p><strong>Scenario: Producto desactualizado</strong></p><p><strong>Given</strong> los hechos del producto están desactualizados</p><p><strong>When</strong> el comprador continúa</p><p><strong>Then</strong> se requiere confirmación actual.</p><p><strong>Scenario: Producto no disponible</strong></p><p><strong>Given</strong> el producto está oculto o no disponible</p><p><strong>When</strong> se solicita</p><p><strong>Then</strong> no puede tratarse como compromiso.</p></td></tr>
</tbody>
</table>

#### MOB-US-038 — Preparar una Purchase Request

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-038</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Preparar una Purchase Request</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo preparar una Purchase Request, para organizar una compra futura sin confirmarla falsamente.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: borrador</strong></p><p><strong>Given</strong> hay productos permitidos disponibles</p><p><strong>When</strong> el comprador prepara una solicitud</p><p><strong>Then</strong> permanece como borrador y no crea reserva.</p><p><strong>Scenario: Producto modificado</strong></p><p><strong>Given</strong> cambia el precio o disponibilidad</p><p><strong>When</strong> el comprador revisa el borrador</p><p><strong>Then</strong> el cambio es claro antes de la envío.</p><p><strong>Scenario: Preparación local</strong></p><p><strong>Given</strong> el comprador pierde conexión</p><p><strong>When</strong> edita el borrador</p><p><strong>Then</strong> permanece no confirmado.</p></td></tr>
</tbody>
</table>

#### MOB-US-039 — Repetir una compra anterior

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-039</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Repetir una compra anterior</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo repetir una compra anterior, para preparar una nueva solicitud más rápidamente en un flujo futuro.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Historial reutilizado</strong></p><p><strong>Given</strong> el comprador puede acceder al historial anterior</p><p><strong>When</strong> lo reutiliza</p><p><strong>Then</strong> Nexa crea un nuevo borrador y vuelve a comprobar los datos actuales del producto.</p><p><strong>Scenario: Producto modificado</strong></p><p><strong>Given</strong> un producto anterior ya no está disponible</p><p><strong>When</strong> se reutiliza el historial</p><p><strong>Then</strong> Nexa lo marca y no crea un pedido silencioso.</p><p><strong>Scenario: Acción repetida</strong></p><p><strong>Given</strong> el comprador repite la acción</p><p><strong>When</strong> Nexa la procesa</p><p><strong>Then</strong> no crea un segundo compromiso.</p></td></tr>
</tbody>
</table>

#### MOB-US-040 — Enviar una solicitud o realizar un Direct Order

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-040</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Enviar una solicitud o realizar un Direct Order</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo enviar una solicitud o realizar un Direct Order, para que mi vía de compromiso elegida sea explícita y autorizada.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Purchase Request</strong></p><p><strong>Given</strong> existe un borrador válido y una política válida</p><p><strong>When</strong> el comprador envía una solicitud</p><p><strong>Then</strong> se registra una única Purchase Request.</p><p><strong>Scenario: Direct Order</strong></p><p><strong>Given</strong> está permitido ordenar directamente</p><p><strong>When</strong> el comprador elige esa vía</p><p><strong>Then</strong> se registra una única ruta de Sales Order sin inventar una Purchase Request.</p><p><strong>Scenario: Hechos modificados</strong></p><p><strong>Given</strong> cambiaron precio, disponibilidad, crédito o permiso</p><p><strong>When</strong> el comprador envía</p><p><strong>Then</strong> no se registra ningún compromiso parcial.</p></td></tr>
</tbody>
</table>

#### MOB-US-041 — Responder a un cambio material

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-041</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Responder a un cambio material</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo responder a un cambio material, para que mi compromiso futuro refleje una decisión explícita.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Aceptar cambio</strong></p><p><strong>Given</strong> existe un cambio actual y autorizado</p><p><strong>When</strong> el comprador lo acepta</p><p><strong>Then</strong> Nexa registra el cambio versionado.</p><p><strong>Scenario: Rechazar cambio</strong></p><p><strong>Given</strong> el comprador lo rechaza</p><p><strong>When</strong> Nexa registra la decisión</p><p><strong>Then</strong> el compromiso original permanece intacto.</p><p><strong>Scenario: Cambio desactualizado</strong></p><p><strong>Given</strong> el cambio ya no es actual</p><p><strong>When</strong> el comprador responde</p><p><strong>Then</strong> Nexa solicita la decisión actual y no cambia nada silenciosamente.</p></td></tr>
</tbody>
</table>

#### MOB-US-042 — Seguir solicitudes y pedidos

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-042</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Seguir solicitudes y pedidos</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo seguir solicitudes y pedidos, para comprender el progreso comercial autorizado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Historial autorizado</strong></p><p><strong>Given</strong> existe una relación autorizada</p><p><strong>When</strong> se revisa el progreso</p><p><strong>Then</strong> el estado e historial de solicitud y pedido permanecen diferenciados.</p><p><strong>Scenario: Progreso actual</strong></p><p><strong>Given</strong> existe una relación autorizada</p><p><strong>When</strong> el comprador revisa el progreso</p><p><strong>Then</strong> el estado de Purchase Request y Sales Order permanece diferenciado.</p><p><strong>Scenario: Acceso revocado</strong></p><p><strong>Given</strong> se revoca el acceso</p><p><strong>When</strong> se solicita el progreso</p><p><strong>Then</strong> no se expone información privada.</p><p><strong>Scenario: Progreso desactualizado</strong></p><p><strong>Given</strong> el progreso mostrado está desactualizado</p><p><strong>When</strong> el comprador hace actualización</p><p><strong>Then</strong> Nexa expone el resultado actual o un estado no disponible veraz.</p></td></tr>
</tbody>
</table>

#### MOB-US-043 — Revisar estado de crédito y pago

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-043</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-06 — Conveniencia comercial y operativa futura</td></tr>
<tr><th>Title</th><td colspan="3">Revisar estado de crédito y pago</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo revisar el estado del crédito y del pago, para comprender lo adeudado sin tratar la evidencia reportada como confirmación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Crédito actual</strong></p><p><strong>Given</strong> existe una relación autorizada</p><p><strong>When</strong> se revisa el crédito</p><p><strong>Then</strong> importe, moneda, frescura y fuente quedan claros.</p><p><strong>Scenario: Estado de pago</strong></p><p><strong>Given</strong> existe evidencia de pago</p><p><strong>When</strong> el comprador la revisa</p><p><strong>Then</strong> los estados reported, confirmed y rejected permanecen diferenciados.</p><p><strong>Scenario: Estado desactualizado</strong></p><p><strong>Given</strong> el estado de pago está desactualizado</p><p><strong>When</strong> el comprador hace actualización</p><p><strong>Then</strong> Nexa expone el estado actual o un estado no disponible veraz.</p></td></tr>
</tbody>
</table>

#### MOB-US-044 — Saber cuándo una entrega requiere atención

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-044</td><td>Customer Buyer</td><td>Critical</td><td>MOBILE-EPIC-05 — Handoff de Delivery, Buyer Receipt y actualizaciones críticas</td></tr>
<tr><th>Title</th><td colspan="3">Saber cuándo una entrega requiere atención</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo saber cuándo una entrega requiere atención, para responder oportunamente a un cambio relevante.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Actualización relevante</strong></p><p><strong>Given</strong> un hecho permitido de entrega requiere atención del comprador</p><p><strong>When</strong> Nexa envía una actualización</p><p><strong>Then</strong> el comprador puede identificar la entrega relevante.</p><p><strong>Scenario: Actualización no relacionada</strong></p><p><strong>Given</strong> la entrega está fuera de la relación del comprador</p><p><strong>When</strong> se prepara una actualización</p><p><strong>Then</strong> no se revela información privada de la entrega.</p><p><strong>Scenario: Fallo de entrega</strong></p><p><strong>Given</strong> una actualización no puede entregarse</p><p><strong>When</strong> el comprador abre Nexa</p><p><strong>Then</strong> los hechos actuales de entrega siguen disponibles para actualización y ningún hecho cambia.</p><p><strong>Scenario: Reintento de actualización</strong></p><p><strong>Given</strong> una actualización se repite</p><p><strong>When</strong> el comprador la recibe</p><p><strong>Then</strong> no crea un segundo entrega, recepción ni hecho de discrepancia.</p></td></tr>
</tbody>
</table>

#### MOB-US-045 — Ver un conductor activo en un mapa

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-045</td><td>Customer Buyer</td><td>Low</td><td>MOBILE-EPIC-07 — Operación de campo avanzada y continuidad selectiva</td></tr>
<tr><th>Title</th><td colspan="3">Ver un conductor activo en un mapa</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo ver en un mapa un conductor activo, para que un servicio futuro y autorizado me ayude a comprender el horario de llegada.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Ubicación futura</strong></p><p><strong>Given</strong> se acepta una política futura de ubicación</p><p><strong>When</strong> el comprador abre una entrega activo</p><p><strong>Then</strong> solo se muestra ubicación acotada con consentimiento.</p><p><strong>Scenario: Sin entrega activo</strong></p><p><strong>Given</strong> no existe una entrega activo</p><p><strong>When</strong> el comprador solicita un mapa</p><p><strong>Then</strong> no se divulga la ubicación del conductor.</p><p><strong>Scenario: Límite de privacidad</strong></p><p><strong>Given</strong> falta permiso o relación</p><p><strong>When</strong> el comprador solicita un mapa</p><p><strong>Then</strong> no se divulga ninguna ubicación.</p></td></tr>
</tbody>
</table>

#### MOB-US-046 — Contactar al conductor

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-046</td><td>Customer Buyer</td><td>High</td><td>MOBILE-EPIC-07 — Operación de campo avanzada y continuidad selectiva</td></tr>
<tr><th>Title</th><td colspan="3">Contactar al conductor</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo contactar al conductor, para resolver una duda de llegada mediante un canal autorizado de entrega.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Canal futuro</strong></p><p><strong>Given</strong> existe una política de canal aceptada y una entrega activo</p><p><strong>When</strong> el comprador contacta al conductor</p><p><strong>Then</strong> solo se usa el canal autorizado.</p><p><strong>Scenario: Sin permiso</strong></p><p><strong>Given</strong> falta consentimiento o entrega activo</p><p><strong>When</strong> se solicita el contacto</p><p><strong>Then</strong> no se inicia contacto personal.</p><p><strong>Scenario: Hechos separados</strong></p><p><strong>Given</strong> ocurre el contacto</p><p><strong>When</strong> termina</p><p><strong>Then</strong> no cambia Driver outcome, Buyer Receipt ni el estado de entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-047 — Verificar una entrega mediante el código de handoff

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-047</td><td>Customer Buyer</td><td>Critical</td><td>MOBILE-EPIC-05 — Handoff de Delivery, Buyer Receipt y actualizaciones críticas</td></tr>
<tr><th>Title</th><td colspan="3">Verificar una entrega mediante el código de handoff</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo verificar una entrega mediante el código de handoff, para confirmar que reviso la entrega correcta.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Código coincidente</strong></p><p><strong>Given</strong> existe un código válido, no expirado y una relación autorizada</p><p><strong>When</strong> el comprador lo verifica</p><p><strong>Then</strong> Nexa identifica la entrega y Delivery Attempt coincidentes.</p><p><strong>Scenario: Código inválido</strong></p><p><strong>Given</strong> el código está expirado, reutilizado, malformado o no relacionado</p><p><strong>When</strong> el comprador lo verifica</p><p><strong>Then</strong> Nexa lo rechaza y no cambia ningún hecho de recepción.</p><p><strong>Scenario: Sin conexión</strong></p><p><strong>Given</strong> no se puede confirmar el código</p><p><strong>When</strong> el comprador lo verifica</p><p><strong>Then</strong> Nexa muestra un estado no confirmado y ningún recepción tiene éxito.</p><p><strong>Scenario: Límite de verificación</strong></p><p><strong>Given</strong> el código está verificado</p><p><strong>When</strong> el comprador continúa</p><p><strong>Then</strong> la verificación por sí sola no confirma cantidades, POD, pago ni finalización de entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-048 — Confirmar las cantidades realmente recibidas

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-048</td><td>Customer Buyer</td><td>Critical</td><td>MOBILE-EPIC-05 — Handoff de Delivery, Buyer Receipt y actualizaciones críticas</td></tr>
<tr><th>Title</th><td colspan="3">Confirmar las cantidades realmente recibidas</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo confirmar las cantidades realmente recibidas, para que el proveedor tenga un registro veraz de mi Buyer Receipt.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: recepción coincidente</strong></p><p><strong>Given</strong> existe un handoff verificado y autorizado</p><p><strong>When</strong> el comprador confirma las cantidades recibidas</p><p><strong>Then</strong> Nexa registra un único hecho de Buyer Receipt con persona, momento y entrega.</p><p><strong>Scenario: Cantidades diferentes</strong></p><p><strong>Given</strong> las cantidades recibidas difieren del resultado del conductor</p><p><strong>When</strong> el comprador las confirma</p><p><strong>Then</strong> ambos hechos permanecen separados y la diferencia queda visible.</p><p><strong>Scenario: Handoff desactualizado o reutilizado</strong></p><p><strong>Given</strong> el handoff está desactualizado, expirado o ya utilizado</p><p><strong>When</strong> el comprador confirma cantidades</p><p><strong>Then</strong> Nexa rechaza la confirmación o devuelve el resultado original sin un segundo recepción.</p><p><strong>Scenario: Sin conexión</strong></p><p><strong>Given</strong> no se puede comprobar la confirmación del recepción</p><p><strong>When</strong> el comprador lo intenta</p><p><strong>Then</strong> Nexa no muestra éxito de recepción hasta recibir confirmación.</p></td></tr>
</tbody>
</table>

#### MOB-US-049 — Reportar una discrepancia sin borrar los hechos

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-049</td><td>Customer Buyer</td><td>Critical</td><td>MOBILE-EPIC-05 — Handoff de Delivery, Buyer Receipt y actualizaciones críticas</td></tr>
<tr><th>Title</th><td colspan="3">Reportar una discrepancia sin borrar los hechos</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo reportar una discrepancia sin borrar los hechos, para que el proveedor resuelva la diferencia manteniendo un historial confiable.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Discrepancia registrada</strong></p><p><strong>Given</strong> existe un contexto de handoff o recepción verificado</p><p><strong>When</strong> el comprador reporta una discrepancia</p><p><strong>Then</strong> Nexa conserva motivo, cantidad afectada, persona, momento y evidencia.</p><p><strong>Scenario: Historiales separados</strong></p><p><strong>Given</strong> el resultado del Driver outcome difiere del Buyer Receipt</p><p><strong>When</strong> se registra la discrepancia</p><p><strong>Then</strong> ambos hechos originales permanecen sin cambios y la diferencia queda visible.</p><p><strong>Scenario: Reporte inválido</strong></p><p><strong>Given</strong> falta motivo, permiso o evidencia requerida</p><p><strong>When</strong> el comprador lo reporta</p><p><strong>Then</strong> Nexa no registra una corrección no autorizada.</p><p><strong>Scenario: Fallo temporal</strong></p><p><strong>Given</strong> no se puede confirmar el reporte</p><p><strong>When</strong> el comprador reintenta</p><p><strong>Then</strong> Nexa conserva un único resultado pendiente o aceptado y no implica reembolso, cambio de pago ni finalización de entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-050 — Gestionar una discrepancia de recepción con evidencia

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-050</td><td>Warehouse Operator</td><td>High</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Gestionar una discrepancia de recepción con evidencia</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo registrar una discrepancia de recepción de entrada con evidencia, para que la decisión de recepción refleje lo encontrado físicamente.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Diferencia capturada</strong></p><p><strong>Given</strong> se inspecciona una entrega de entrada</p><p><strong>When</strong> el operador registra daño, fuga, producto incorrecto o cantidad incorrecta</p><p><strong>Then</strong> Nexa conserva motivo, artículos afectados y evidencia para revisión.</p><p><strong>Scenario: recepción controlado</strong></p><p><strong>Given</strong> se registra una discrepancia</p><p><strong>When</strong> el operador envía el resultado de recepción</p><p><strong>Then</strong> Nexa no incrementa el stock vendible más allá de los hechos confirmados.</p><p><strong>Scenario: Evidencia faltante</strong></p><p><strong>Given</strong> falta un hecho o evidencia requerida</p><p><strong>When</strong> el operador intenta enviar la discrepancia</p><p><strong>Then</strong> Nexa explica qué falta y no registra una decisión incompleta.</p></td></tr>
</tbody>
</table>

#### MOB-US-051 — Retener o poner en cuarentena stock y resolverlo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-051</td><td>Warehouse Operator</td><td>High</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Retener o poner en cuarentena stock y resolverlo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo colocar stock cuestionable en retención o cuarentena y registrar su resolución, para impedir su uso antes de una decisión autorizada.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Proteger stock</strong></p><p><strong>Given</strong> un lote tiene una condición que impide su uso normal</p><p><strong>When</strong> el operador registra el motivo de retención o cuarentena</p><p><strong>Then</strong> Nexa retira la cantidad afectada del trabajo disponible aplicable.</p><p><strong>Scenario: Resolución autorizada</strong></p><p><strong>Given</strong> un lote retenido fue revisado</p><p><strong>When</strong> una persona autorizada lo libera o dispone de él</p><p><strong>Then</strong> Nexa registra decisión, motivo y cantidad afectada sin borrar el historial de retención.</p><p><strong>Scenario: Decisión desactualizada</strong></p><p><strong>Given</strong> el lote cambió después de ser visualizado</p><p><strong>When</strong> el operador intenta resolverlo</p><p><strong>Then</strong> Nexa rechaza la decisión desactualizada y muestra el estado actual.</p></td></tr>
</tbody>
</table>

#### MOB-US-052 — Confirmar la recepción en el destino de una transferencia interna

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-052</td><td>Warehouse Operator</td><td>High</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Confirmar la recepción en el destino de una transferencia interna</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo confirmar lo que llegó al destino de una transferencia interna, para que el registro de stock refleje el movimiento físico y cualquier diferencia.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: recepción completo</strong></p><p><strong>Given</strong> una transferencia autorizada está en tránsito</p><p><strong>When</strong> el operador destino confirma lote y cantidad esperados</p><p><strong>Then</strong> Nexa registra destination recepción y cierra el movimiento de transferencia.</p><p><strong>Scenario: recepción parcial o diferente</strong></p><p><strong>Given</strong> el destino recibe otro lote o cantidad</p><p><strong>When</strong> el operador lo registra</p><p><strong>Then</strong> Nexa mantiene separados los hechos de origen y destino y expone la diferencia para resolución.</p><p><strong>Scenario: recepción repetido</strong></p><p><strong>Given</strong> destination recepción ya tiene un resultado aceptado</p><p><strong>When</strong> el operador reintenta</p><p><strong>Then</strong> Nexa devuelve el resultado original sin un segundo recepción.</p></td></tr>
</tbody>
</table>

#### MOB-US-053 — Realizar un conteo cíclico y solicitar corrección de stock

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-053</td><td>Warehouse Operator</td><td>High</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Realizar un conteo cíclico y solicitar corrección de stock</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo contar una ubicación de almacenamiento y solicitar una corrección de stock, para resolver una diferencia física sin reescribir el historial.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Conteo registrado</strong></p><p><strong>Given</strong> existe una ubicación permitida y una vista actual del stock</p><p><strong>When</strong> el operador registra lote y cantidad observados</p><p><strong>Then</strong> Nexa conserva el conteo con persona, momento y ubicación.</p><p><strong>Scenario: Corrección revisada</strong></p><p><strong>Given</strong> el conteo difiere del stock registrado</p><p><strong>When</strong> se aprueba una corrección autorizada</p><p><strong>Then</strong> Nexa registra evidencia correctiva y la cantidad resultante sin borrar movimientos anteriores.</p><p><strong>Scenario: Cambio concurrente</strong></p><p><strong>Given</strong> el stock cambió después de iniciar el conteo</p><p><strong>When</strong> el operador envía la corrección</p><p><strong>Then</strong> Nexa rechaza o reabre el conteo desactualizado en lugar de aplicar una corrección última escritura gana.</p></td></tr>
</tbody>
</table>

#### MOB-US-054 — Solicitar sustitución de lote cuando FEFO no completa el trabajo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-054</td><td>Warehouse Operator</td><td>Low</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Solicitar sustitución de lote cuando FEFO no completa el trabajo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo solicitar una sustitución permitida de lote cuando el lote esperado no puede completar el trabajo, para revisar el pedido sin omitir la política de disponibilidad.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Sustitución solicitada</strong></p><p><strong>Given</strong> el lote esperado no puede suministrar la cantidad preparada</p><p><strong>When</strong> el operador propone una alternativa elegible</p><p><strong>Then</strong> Nexa la envía a decisión autorizada con ambos lotes visibles.</p><p><strong>Scenario: Decisión controlada</strong></p><p><strong>Given</strong> una sustitución es rechazada o queda desactualizada</p><p><strong>When</strong> el operador continúa</p><p><strong>Then</strong> Nexa conserva la asignación original y explica la siguiente acción permitida.</p></td></tr>
</tbody>
</table>

#### MOB-US-055 — Usar información ampliada de identidad de producto, paquete y almacenamiento

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-055</td><td>Warehouse Operator</td><td>Low</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Usar información ampliada de identidad de producto, paquete y almacenamiento</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo usar información más rica de identidad de producto, paquete y almacenamiento, para manipular el stock previsto con menos errores de identificación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Identidad resuelta</strong></p><p><strong>Given</strong> existe un identificador permitido de paquete o almacenamiento</p><p><strong>When</strong> el operador lo presenta</p><p><strong>Then</strong> Nexa muestra el producto correspondiente y el contexto actual antes de iniciar el trabajo.</p><p><strong>Scenario: Identidad no disponible</strong></p><p><strong>Given</strong> el identificador es desconocido o ilegible</p><p><strong>When</strong> el operador intenta continuar</p><p><strong>Then</strong> Nexa ofrece un alternativa explícito o indica que se requiere confirmación.</p></td></tr>
</tbody>
</table>

#### MOB-US-056 — Preparar un grupo de tareas de almacén

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-056</td><td>Warehouse Operator</td><td>Low</td><td>MOBILE-EPIC-08 — Transferencias y exactitud de inventario</td></tr>
<tr><th>Title</th><td colspan="3">Preparar un grupo de tareas de almacén</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo preparar un grupo de tareas de almacén, para trabajar eficientemente sin perder el resultado de cada elemento.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Grupo preparado</strong></p><p><strong>Given</strong> hay varias tareas permitidas disponibles</p><p><strong>When</strong> el operador las agrupa</p><p><strong>Then</strong> Nexa muestra claramente elementos, secuencia y comprobaciones requeridas.</p><p><strong>Scenario: Un elemento difiere</strong></p><p><strong>Given</strong> una tarea no puede completarse como fue preparada</p><p><strong>When</strong> el operador registra la diferencia</p><p><strong>Then</strong> Nexa mantiene separados los resultados de las otras tareas e identifica el elemento que requiere revisión.</p></td></tr>
</tbody>
</table>

#### MOB-US-057 — Resolver una discrepancia de despacho antes del handoff

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-057</td><td>Dispatch Coordinator</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Resolver una discrepancia de despacho antes del handoff</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo resolver una discrepancia de despacho antes del handoff, para que solo una entrega revisada abandone el control del almacén.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Diferencia identificada</strong></p><p><strong>Given</strong> los bienes salientes no coinciden con la entrega preparada</p><p><strong>When</strong> el coordinador registra la diferencia</p><p><strong>Then</strong> Nexa identifica la entrega, lote o cantidad afectados y bloquea el handoff inseguro.</p><p><strong>Scenario: Resolución autorizada</strong></p><p><strong>Given</strong> la diferencia tiene una resolución aceptada</p><p><strong>When</strong> el coordinador confirma la siguiente acción</p><p><strong>Then</strong> Nexa actualiza la disponibilidad de despacho con evidencia trazable.</p><p><strong>Scenario: Preparación desactualizada</strong></p><p><strong>Given</strong> la entrega cambió después de la preparación</p><p><strong>When</strong> el coordinador resuelve la discrepancia</p><p><strong>Then</strong> Nexa solicita una decisión nueva en lugar de sobrescribir los hechos actuales.</p></td></tr>
</tbody>
</table>

#### MOB-US-058 — Reasignar un conductor o reprogramar el despacho de forma segura

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-058</td><td>Dispatch Coordinator</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Reasignar un conductor o reprogramar el despacho de forma segura</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo reasignar un conductor o reprogramar un despacho de forma segura, para que la entrega siga siendo responsabilidad de una persona elegible en un momento acordado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Reasignación elegible</strong></p><p><strong>Given</strong> una entrega preparada necesita otro conductor</p><p><strong>When</strong> el coordinador selecciona una persona elegible</p><p><strong>Then</strong> Nexa registra la nueva responsabilidad y conserva el historial de asignación anterior.</p><p><strong>Scenario: Cambio de horario</strong></p><p><strong>Given</strong> el despacho no puede continuar en el horario previsto</p><p><strong>When</strong> el coordinador propone un nuevo horario</p><p><strong>Then</strong> Nexa muestra el impacto y confirma el cambio una sola vez.</p><p><strong>Scenario: Cambio concurrente</strong></p><p><strong>Given</strong> otra persona cambió primero la entrega</p><p><strong>When</strong> el coordinador envía el plan antiguo</p><p><strong>Then</strong> Nexa lo rechaza y muestra la responsabilidad y horario actuales.</p></td></tr>
</tbody>
</table>

#### MOB-US-059 — Preparar cargas agrupadas y múltiples paradas

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-059</td><td>Dispatch Coordinator</td><td>Low</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Preparar cargas agrupadas y múltiples paradas</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo preparar una carga de entrega agrupada con sus paradas, para despachar entregas compatibles manteniendo visibles sus restricciones.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Carga compatible</strong></p><p><strong>Given</strong> las entregas cumplen las reglas de agrupación aceptadas</p><p><strong>When</strong> el coordinador prepara una carga</p><p><strong>Then</strong> Nexa muestra cada entrega, parada y condición requerida.</p><p><strong>Scenario: Entrega incompatible</strong></p><p><strong>Given</strong> una entrega incumple una regla de cliente o cadena de frío</p><p><strong>When</strong> el coordinador prepara la carga</p><p><strong>Then</strong> Nexa la mantiene fuera de la carga y explica por qué.</p></td></tr>
</tbody>
</table>

#### MOB-US-060 — Completar un handoff al transportista con responsabilidad trazable

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-060</td><td>Dispatch Coordinator</td><td>Low</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Completar un handoff al transportista con responsabilidad trazable</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo completar un handoff al transportista con responsabilidad clara, para que todos sepan quién controla la carga después de que abandona el almacén.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Handoff aceptado</strong></p><p><strong>Given</strong> existe una carga preparada y un carrier autorizado</p><p><strong>When</strong> el coordinador registra el handoff</p><p><strong>Then</strong> Nexa conserva carrier, persona, momento y responsabilidad de entrega.</p><p><strong>Scenario: Evidencia incompleta</strong></p><p><strong>Given</strong> falta evidencia requerida del handoff</p><p><strong>When</strong> el coordinador intenta finalizarlo</p><p><strong>Then</strong> Nexa deja la responsabilidad en el responsable actual e indica qué se requiere.</p></td></tr>
</tbody>
</table>

#### MOB-US-061 — Registrar evidencia de temperatura en el despacho

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-061</td><td>Dispatch Coordinator</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Registrar evidencia de temperatura en el despacho</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Dispatch Coordinator</strong>, deseo registrar evidencia de temperatura en el despacho, para que la decisión de entrega refleje la condición observada antes del handoff.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Evidencia registrada</strong></p><p><strong>Given</strong> una entrega requiere una comprobación de temperatura</p><p><strong>When</strong> el coordinador registra la observación</p><p><strong>Then</strong> Nexa conserva valor, unidad, persona, momento y contexto de entrega.</p><p><strong>Scenario: Fuera de política</strong></p><p><strong>Given</strong> la observación está fuera del rango aceptado</p><p><strong>When</strong> el coordinador la envía</p><p><strong>Then</strong> Nexa impide un despacho no revisado y muestra la decisión requerida.</p><p><strong>Scenario: Confirmación faltante</strong></p><p><strong>Given</strong> no se puede confirmar la observación</p><p><strong>When</strong> el coordinador reintenta</p><p><strong>Then</strong> Nexa no implica aprobación de cadena de frío.</p></td></tr>
</tbody>
</table>

#### MOB-US-062 — Señalar la llegada de una entrega activa

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-062</td><td>Driver or Delivery Operator</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Señalar la llegada de una entrega activa</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo señalar la llegada de una entrega activa, para que el comprador y el equipo de entrega sepan que puede comenzar el handoff.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Llegada registrada</strong></p><p><strong>Given</strong> el conductor tiene una entrega activo y autorizado</p><p><strong>When</strong> señala su llegada</p><p><strong>Then</strong> Nexa registra el evento y lo hace visible a destinatarios permitidos.</p><p><strong>Scenario: Sin entrega activo</strong></p><p><strong>Given</strong> el conductor no está asignado a una entrega activo</p><p><strong>When</strong> señala llegada</p><p><strong>Then</strong> Nexa rechaza la señal sin revelar otra entrega.</p><p><strong>Scenario: entrega permanece abierto</strong></p><p><strong>Given</strong> se registró la llegada</p><p><strong>When</strong> el comprador o conductor consulta la entrega</p><p><strong>Then</strong> permanece abierto hasta registrar por separado handoff y recepción.</p></td></tr>
</tbody>
</table>

#### MOB-US-063 — Seguir instrucciones de entrega y datos de contacto autorizados

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-063</td><td>Driver or Delivery Operator</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Seguir instrucciones de entrega y datos de contacto autorizados</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo seguir las instrucciones y datos de contacto permitidos de la entrega, para coordinar el handoff con la persona prevista.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Contexto autorizado</strong></p><p><strong>Given</strong> una entrega activa incluye instrucciones permitidas</p><p><strong>When</strong> el conductor las abre</p><p><strong>Then</strong> Nexa muestra solo la información necesaria para esa entrega.</p><p><strong>Scenario: Instrucciones modificadas</strong></p><p><strong>Given</strong> las instrucciones ya no son actuales</p><p><strong>When</strong> el conductor las consulta</p><p><strong>Then</strong> Nexa las marca como desactualizadas y exige confirmación nueva antes de usarlas.</p><p><strong>Scenario: Información restringida</strong></p><p><strong>Given</strong> un contacto o instrucción no está permitido para el conductor</p><p><strong>When</strong> solicita acceso</p><p><strong>Then</strong> Nexa lo oculta y explica la ruta permitida.</p></td></tr>
</tbody>
</table>

#### MOB-US-064 — Solicitar reprogramación de una entrega desde el campo

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-064</td><td>Customer Buyer</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Solicitar reprogramación de una entrega desde el campo</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo solicitar un horario de entrega diferente, para que el equipo de entrega decida cómo gestionar mi disponibilidad.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: solicitud enviada</strong></p><p><strong>Given</strong> el comprador está autorizado para una entrega activa</p><p><strong>When</strong> propone un horario alternativo</p><p><strong>Then</strong> Nexa registra una solicitud y muestra que espera una decisión de entrega.</p><p><strong>Scenario: Decisión devuelta</strong></p><p><strong>Given</strong> el equipo de entrega acepta o rechaza la solicitud</p><p><strong>When</strong> el comprador consulta la entrega</p><p><strong>Then</strong> Nexa muestra la decisión y el horario efectivo sin reescribir hechos anteriores.</p><p><strong>Scenario: solicitud desactualizada</strong></p><p><strong>Given</strong> la entrega ya es terminal o cambió</p><p><strong>When</strong> el comprador envía la solicitud antigua</p><p><strong>Then</strong> Nexa la rechaza con el estado actual de la entrega.</p></td></tr>
</tbody>
</table>

#### MOB-US-065 — Registrar un incidente de entrega con mayor detalle

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-065</td><td>Driver or Delivery Operator</td><td>High</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Registrar un incidente de entrega con mayor detalle</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo registrar un incidente de entrega con sus detalles relevantes, para que el equipo tome una decisión de seguimiento informada.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Incidente descrito</strong></p><p><strong>Given</strong> una entrega activa encuentra un incidente permitido</p><p><strong>When</strong> el conductor registra motivo, lugar dentro de la entrega y evidencia</p><p><strong>Then</strong> Nexa conserva el incidente para revisión autorizada.</p><p><strong>Scenario: El incidente no reescribe el resultado</strong></p><p><strong>Given</strong> ya existe un resultado de entrega</p><p><strong>When</strong> se añade un incidente</p><p><strong>Then</strong> Nexa conserva el resultado original y vincula la evidencia nueva.</p><p><strong>Scenario: Incidente incompleto</strong></p><p><strong>Given</strong> faltan detalles requeridos</p><p><strong>When</strong> el conductor intenta enviarlo</p><p><strong>Then</strong> Nexa identifica la información faltante y no afirma un seguimiento completado.</p></td></tr>
</tbody>
</table>

#### MOB-US-066 — Recuperar una entrega activa mediante operación offline selectiva

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-066</td><td>Driver or Delivery Operator</td><td>Low</td><td>MOBILE-EPIC-09 — Excepciones de despacho y coordinación de Delivery</td></tr>
<tr><th>Title</th><td colspan="3">Recuperar una entrega activa mediante operación offline selectiva</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Driver / Delivery Operator</strong>, deseo conservar evidencia seleccionada de entrega durante una pérdida de conexión, para recuperar el trabajo sin afirmar un resultado de entrega no confirmado.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Evidencia retenida</strong></p><p><strong>Given</strong> se captura un elemento de evidencia permitido sin conexión</p><p><strong>When</strong> el conductor vuelve a tener cobertura</p><p><strong>Then</strong> Nexa muestra su estado pendiente y permite revisarlo antes del envío.</p><p><strong>Scenario: Recuperación autoritativa</strong></p><p><strong>Given</strong> la entrega cambió mientras el dispositivo estaba offline</p><p><strong>When</strong> se revisa la evidencia</p><p><strong>Then</strong> Nexa resuelve explícitamente el conflicto y nunca aplica silenciosamente un resultado desactualizado.</p></td></tr>
</tbody>
</table>

#### MOB-US-067 — Proporcionar instrucciones de entrega y contacto alternativo para la recepción

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-067</td><td>Customer Buyer</td><td>High</td><td>MOBILE-EPIC-10 — Continuidad de Delivery para Customer Buyer</td></tr>
<tr><th>Title</th><td colspan="3">Proporcionar instrucciones de entrega y contacto alternativo para la recepción</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo proporcionar instrucciones de entrega y un contacto alternativo para la recepción, para que la entrega llegue a la persona correcta bajo las condiciones acordadas.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Instrucciones proporcionadas</strong></p><p><strong>Given</strong> el comprador está autorizado para la entrega</p><p><strong>When</strong> guarda instrucciones</p><p><strong>Then</strong> Nexa las asocia con esa entrega y muestra su periodo efectivo.</p><p><strong>Scenario: Consentimiento del contacto alternativo</strong></p><p><strong>Given</strong> una persona alternativa debe recibir la entrega</p><p><strong>When</strong> el comprador proporciona contacto permitido y consentimiento</p><p><strong>Then</strong> Nexa lo registra únicamente para el propósito de entrega definido.</p><p><strong>Scenario: Cambio después del despacho</strong></p><p><strong>Given</strong> la entrega está en un estado que no permite cambios</p><p><strong>When</strong> el comprador edita instrucciones</p><p><strong>Then</strong> Nexa rechaza el cambio o lo dirige a una decisión explícita.</p></td></tr>
</tbody>
</table>

#### MOB-US-068 — Revisar la línea de tiempo de la entrega y reconocer su finalización

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-068</td><td>Customer Buyer</td><td>High</td><td>MOBILE-EPIC-10 — Continuidad de Delivery para Customer Buyer</td></tr>
<tr><th>Title</th><td colspan="3">Revisar la línea de tiempo de la entrega y reconocer su finalización</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo revisar la línea de tiempo de la entrega y reconocer su finalización, para comprender el resultado registrado sin cambiar el historial.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Timeline visible</strong></p><p><strong>Given</strong> el comprador puede acceder a una entrega</p><p><strong>When</strong> abre su línea de tiempo</p><p><strong>Then</strong> Nexa muestra los hechos autorizados ordenados y su estado actual.</p><p><strong>Scenario: Acknowledgement separado</strong></p><p><strong>Given</strong> la entrega tiene un resultado registrado</p><p><strong>When</strong> el comprador lo reconoce</p><p><strong>Then</strong> Nexa registra el acknowledgement separado de recepción, proof o finalización.</p><p><strong>Scenario: Historial sin cambios</strong></p><p><strong>Given</strong> el comprador reconoce una entrega</p><p><strong>When</strong> otra persona permitida la consulta</p><p><strong>Then</strong> los hechos subyacentes permanecen sin cambios.</p></td></tr>
</tbody>
</table>

#### MOB-US-069 — Adjuntar evidencia a una discrepancia de entrega

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-069</td><td>Customer Buyer</td><td>High</td><td>MOBILE-EPIC-10 — Continuidad de Delivery para Customer Buyer</td></tr>
<tr><th>Title</th><td colspan="3">Adjuntar evidencia a una discrepancia de entrega</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo adjuntar evidencia a una discrepancia de entrega, para que el proveedor revise la diferencia reportada con su contexto.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Evidencia adjunta</strong></p><p><strong>Given</strong> el comprador tiene una discrepancia permitida</p><p><strong>When</strong> añade evidencia</p><p><strong>Then</strong> Nexa la vincula con esa discrepancia junto con persona y momento.</p><p><strong>Scenario: Evidencia no soportada o insegura</strong></p><p><strong>Given</strong> la evidencia no está disponible, es demasiado grande o no está permitida</p><p><strong>When</strong> el comprador intenta añadirla</p><p><strong>Then</strong> Nexa explica el problema y mantiene la discrepancia sin cambios.</p><p><strong>Scenario: Hechos originales preservados</strong></p><p><strong>Given</strong> la evidencia es aceptada</p><p><strong>When</strong> se revisa la entrega</p><p><strong>Then</strong> recepción, Driver outcome y discrepancia permanecen separados.</p></td></tr>
</tbody>
</table>

#### MOB-US-070 — Ver documentos de negocio vinculados a solicitud o pedido

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-070</td><td>Customer Buyer or Sales Representative</td><td>Medium</td><td>MOBILE-EPIC-11 — Seguimiento comercial y financiero</td></tr>
<tr><th>Title</th><td colspan="3">Ver documentos de negocio vinculados a solicitud o pedido</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer or Sales Representative</strong>, deseo ver un documento de negocio vinculado a una solicitud o un pedido, para usar la evidencia autorizada del trabajo comercial.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Documento autorizado</strong></p><p><strong>Given</strong> un documento emitido pertenece a la relación permitida</p><p><strong>When</strong> la persona lo solicita</p><p><strong>Then</strong> Nexa proporciona su identidad y contenido autorizado.</p><p><strong>Scenario: Documento faltante</strong></p><p><strong>Given</strong> no existe un documento emitido</p><p><strong>When</strong> la persona lo solicita</p><p><strong>Then</strong> Nexa indica que no está disponible y no cambia ningún compromiso.</p><p><strong>Scenario: Acceso revocado</strong></p><p><strong>Given</strong> se revoca el permiso</p><p><strong>When</strong> la persona solicita el documento</p><p><strong>Then</strong> Nexa no expone contenido privado.</p></td></tr>
</tbody>
</table>

#### MOB-US-071 — Reportar evidencia de pago y ver el resultado de revisión

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-071</td><td>Customer Buyer</td><td>Medium</td><td>MOBILE-EPIC-11 — Seguimiento comercial y financiero</td></tr>
<tr><th>Title</th><td colspan="3">Reportar evidencia de pago y ver el resultado de revisión</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Customer Buyer</strong>, deseo reportar evidencia de pago y ver su resultado de revisión, para seguir un pago sin afirmar yo mismo su confirmación.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Evidencia reportada</strong></p><p><strong>Given</strong> están disponibles una referencia, importe y evidencia permitidos</p><p><strong>When</strong> el comprador los reporta</p><p><strong>Then</strong> Nexa registra el reporte como no confirmado.</p><p><strong>Scenario: Evidencia revisada</strong></p><p><strong>Given</strong> el proceso responsable revisa el reporte</p><p><strong>When</strong> el comprador consulta el estado</p><p><strong>Then</strong> Nexa muestra el resultado de revisión sin reescribir el reporte.</p><p><strong>Scenario: Reporte duplicado</strong></p><p><strong>Given</strong> se vuelve a enviar el mismo reporte</p><p><strong>When</strong> Nexa lo recibe</p><p><strong>Then</strong> no aplica la evidencia dos veces.</p></td></tr>
</tbody>
</table>

#### MOB-US-072 — Trabajar con un cliente mediante una visita de campo autorizada

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-072</td><td>Sales Representative</td><td>Low</td><td>MOBILE-EPIC-11 — Seguimiento comercial y financiero</td></tr>
<tr><th>Title</th><td colspan="3">Trabajar con un cliente mediante una visita de campo autorizada</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Sales Representative</strong>, deseo trabajar con un cliente mediante una visita de campo autorizada, para iniciar con el contexto correcto de relación y terminar con un seguimiento claro.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Visita autorizada</strong></p><p><strong>Given</strong> el representante tiene permiso para la relación del cliente</p><p><strong>When</strong> inicia una visita</p><p><strong>Then</strong> Nexa muestra el contexto permitido del cliente y su propósito.</p><p><strong>Scenario: Seguimiento capturado</strong></p><p><strong>Given</strong> la visita produce un seguimiento permitido</p><p><strong>When</strong> el representante lo registra</p><p><strong>Then</strong> Nexa vincula el resultado con la relación del cliente sin crear un compromiso no aprobado.</p></td></tr>
</tbody>
</table>

#### MOB-US-073 — Usar evidencia de automatización de almacén en un trabajo controlado

<table>
<thead>
<tr><th>Story ID</th><th>User</th><th>Priority</th><th>Epic ID</th></tr>
</thead>
<tbody>
<tr><td>MOB-US-073</td><td>Warehouse Operator</td><td>Future</td><td>MOBILE-EPIC-12 — Automatización de almacén futura</td></tr>
<tr><th>Title</th><td colspan="3">Usar evidencia de automatización de almacén en un trabajo controlado</td></tr>
<tr><th colspan="4">Description</th></tr>
<tr><td colspan="4">Como <strong>Warehouse Operator</strong>, deseo revisar observaciones avanzadas de almacén mediante una decisión controlada, para que una automatización futura ayude al trabajo sin convertirse en verdad de stock no examinada.</td></tr>
<tr><th colspan="4">Acceptance Criteria</th></tr>
<tr><td colspan="4"><p><strong>Scenario: Resultado valioso antes de seleccionar tecnología</strong></p><p><strong>Given</strong> Product explora observaciones avanzadas de almacén</p><p><strong>When</strong> define el resultado de almacén antes de seleccionar un dispositivo o proveedor</p><p><strong>Then</strong> identifica primero un resultado valioso de almacén.</p><p><strong>Scenario: Observación automatizada subordinada</strong></p><p><strong>Given</strong> existe una observación automatizada considerada para el trabajo</p><p><strong>When</strong> se revisa para apoyar una decisión de almacén</p><p><strong>Then</strong> permanece atribuible y revisable y está subordinada a la autorización del responsable del Bounded Context.</p><p><strong>Scenario: Release sin implementación específica</strong></p><p><strong>Given</strong> el release contempla esta hipótesis de automatización futura</p><p><strong>When</strong> se describe su alcance</p><p><strong>Then</strong> no promete una implementación específica de RFID, scanner, sensor, label ni telemetry.</p></td></tr>
</tbody>
</table>

