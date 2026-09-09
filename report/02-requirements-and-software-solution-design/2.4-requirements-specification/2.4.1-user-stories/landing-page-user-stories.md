# Landing Page User Stories

Estas historias describen la superficie pública de adquisición y contacto. La Landing inicia conversaciones y solicitudes de onboarding; no crea un Tenant ni activa un Workspace como hecho de negocio.

#### LAND-US-001 — Comprender la propuesta B2B de Nexa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-001` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |
| **Title** | Comprender la propuesta B2B de Nexa |  |  |
| **Description** | Como **Prospective Company Representative**, deseo comprender la propuesta B2B de Nexa para importadores y distribuidores, incluida la especialización de cadena de frío cuando aplique, para decidir si corresponde continuar la evaluación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Propuesta disponible**<br>**Given** una persona abre la Landing pública<br>**When** revisa la introducción del producto<br>**Then** identifica el contexto B2B de Nexa sin confundirlo con un ecommerce genérico ni con un producto exclusivo de cadena de frío.<br><br>**Scenario 2 — Especialización contextual**<br>**Given** la persona opera con productos que requieren cadena de frío<br>**When** revisa las capacidades públicas<br>**Then** encuentra esa especialización explicada como una capacidad aplicable y no como la única finalidad de Nexa. |  |  |

#### LAND-US-002 — Evaluar el ajuste con el perfil operativo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-002` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |
| **Title** | Evaluar el ajuste con el perfil operativo |  |  |
| **Description** | Como prospecto empresarial, deseo contrastar mi perfil operativo con las soluciones de Nexa, para decidir si debo iniciar una conversación o evaluación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Perfil presentado**<br>**Given** el prospecto opera como importador, distribuidor o empresa de almacenamiento en frío,<br>**When** revisa la solución correspondiente,<br>**Then** encuentra el contexto operativo descrito por Nexa.<br><br>**Scenario 2 — Siguiente paso común**<br>**Given** el prospecto combina más de un perfil,<br>**When** compara las soluciones,<br>**Then** puede continuar hacia un producto, contacto o demostración sin perder el contexto consultado. |  |  |

#### LAND-US-003 — Revisar capacidades y límites del producto

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-003` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |
| **Title** | Revisar capacidades y límites del producto |  |  |
| **Description** | Como prospecto empresarial, deseo revisar las capacidades y límites públicos del producto, para entender qué problema operativo aborda Nexa antes de continuar. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Alcance público**<br>**Given** el prospecto abre el contenido del producto,<br>**When** revisa las capacidades descritas,<br>**Then** relaciona Nexa con resultados operativos de inventario, coordinación de pedidos, cadena de frío o entrega que el sitio comunique.<br><br>**Scenario 2 — Límite explícito**<br>**Given** una capacidad no está descrita en la fuente pública,<br>**When** el prospecto evalúa Nexa,<br>**Then** el contenido no promete una integración o resultado no establecido. |  |  |

#### LAND-US-004 — Revisar precios, preguntas frecuentes e información legal

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-004` | Prospective Company Representative | Medium | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |
| **Title** | Revisar precios, preguntas frecuentes e información legal |  |  |
| **Description** | Como prospecto empresarial, deseo consultar precios, preguntas frecuentes y condiciones legales, para evaluar el siguiente paso con información pública suficiente. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Información pública disponible**<br>**Given** el prospecto necesita contexto comercial o legal,<br>**When** abre la sección correspondiente,<br>**Then** encuentra la información que la Landing publica.<br><br>**Scenario 2 — Pregunta sin respuesta**<br>**Given** el contenido público no responde una pregunta,<br>**When** el prospecto busca continuar,<br>**Then** obtiene una ruta de contacto o demostración en lugar de una respuesta inventada. |  |  |

#### LAND-US-005 — Iniciar el onboarding de una empresa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-005` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |
| **Title** | Iniciar el onboarding de una empresa |  |  |
| **Description** | Como **Prospective Company Representative**, deseo iniciar el onboarding de mi empresa desde la Landing, para solicitar un siguiente paso comercial sin que se cree ni active automáticamente un Tenant o Workspace. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Solicitud válida**<br>**Given** el prospecto proporciona la información de empresa y contacto requerida<br>**When** envía la solicitud de onboarding<br>**Then** Nexa confirma únicamente la recepción de la solicitud y el siguiente paso disponible.<br><br>**Scenario 2 — Datos insuficientes**<br>**Given** faltan datos requeridos o no cumplen el formato<br>**When** el prospecto intenta enviar la solicitud<br>**Then** la Landing identifica la información pendiente sin afirmar que existe un Tenant o Workspace.<br><br>**Scenario 3 — Servicio no disponible**<br>**Given** el servicio de onboarding no responde<br>**When** el prospecto envía la solicitud<br>**Then** la Landing muestra un resultado no confirmado u ofrece contacto alternativo sin declarar un onboarding exitoso. |  |  |

#### LAND-US-006 — Contactar a Nexa o solicitar una demostración

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `LAND-US-006` | Prospective Company Representative | High | `LAND-EPIC-01` — Adquisición pública e inicio de onboarding |
| **Title** | Contactar a Nexa o solicitar una demostración |  |  |
| **Description** | Como prospecto empresarial, deseo contactar a Nexa o solicitar una demostración, para obtener un siguiente paso comercial explícito cuando la información pública no sea suficiente. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Solicitud válida**<br>**Given** el prospecto proporciona el contexto requerido,<br>**When** envía la solicitud de contacto o demostración,<br>**Then** la Landing comunica sólo el resultado real del envío.<br><br>**Scenario 2 — Datos inválidos**<br>**Given** falta un dato obligatorio o no cumple el formato,<br>**When** el prospecto envía la solicitud,<br>**Then** la Landing identifica la validación pendiente y no afirma que la solicitud fue recibida.<br><br>**Scenario 3 — Servicio no disponible**<br>**Given** el servicio de contacto no responde,<br>**When** el prospecto envía la solicitud,<br>**Then** la Landing muestra un fallo explícito y no confirma un contacto inexistente. |  |  |
