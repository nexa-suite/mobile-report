# Mobile Functional Stories V1

V1 concentra el alcance actual: trabajo autorizado, continuidad física de almacén, Dispatch Handoff, Delivery Attempt, Proof of Delivery, Buyer Receipt y discrepancias.

#### MOB-US-013 — Registrar el stock recién recibido

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-013` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Registrar el stock recién recibido |  |  |
| **Description** | Como **Warehouse Operator**, deseo registrar el stock que acaba de llegar, para que el almacén tenga un registro confiable del stock recibido. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Llegada válida**<br>**Given** el operador tiene permiso y proporciona producto, lote y cantidad positiva<br>**When** registra la llegada<br>**Then** Nexa registra un único hecho de stock recibido.<br><br>**Scenario 2 — Llegada inválida**<br>**Given** falta información requerida o es inválida<br>**When** el operador la registra<br>**Then** Nexa no realiza un cambio parcial de stock.<br><br>**Scenario 3 — Resultado incierto**<br>**Given** el resultado es desconocido<br>**When** el operador repite la misma llegada<br>**Then** Nexa devuelve el resultado original sin duplicar el stock.<br><br>**Scenario 4 — Sin conexión**<br>**Given** el operador no tiene conexión<br>**When** no se puede confirmar la llegada<br>**Then** Nexa muestra un estado no confirmado y no presenta el stock recibido como autoritativo. |  |  |

#### MOB-US-014 — Registrar lote, vencimiento y cantidad reales

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-014` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Registrar lote, vencimiento y cantidad reales |  |  |
| **Description** | Como **Warehouse Operator**, deseo registrar el lote, vencimiento y cantidad reales, para que el picking futuro use lo que llegó físicamente. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Datos completos del lote**<br>**Given** el operador proporciona lote válido, vencimiento y cantidad positiva<br>**When** confirma la llegada<br>**Then** Nexa conserva esos datos para el stock recibido.<br><br>**Scenario 2 — Vencimiento inválido**<br>**Given** falta el vencimiento, está malformado o no es aceptable<br>**When** el operador lo registra<br>**Then** Nexa rechaza la llegada y no crea stock vendible.<br><br>**Scenario 3 — Llegada duplicada**<br>**Given** se vuelve a enviar la misma llegada<br>**When** Nexa la recibe<br>**Then** permanece una sola llegada y la cantidad no se duplica.<br><br>**Scenario 4 — Preparación local**<br>**Given** el operador pierde conexión<br>**When** prepara datos del lote<br>**Then** permanecen no confirmados y no pueden convertir el stock en vendible. |  |  |

#### MOB-US-015 — Comprobar lote y condición del stock antes del trabajo físico

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-015` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Comprobar lote y condición del stock antes del trabajo físico |  |  |
| **Description** | Como **Warehouse Operator**, deseo comprobar el lote actual y la condición del stock antes del trabajo físico, para elegir stock seguro y disponible para la tarea. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Stock actual**<br>**Given** el operador tiene permiso<br>**When** comprueba el stock<br>**Then** la cantidad física, cantidad vendible, lote y condición aparecen diferenciados.<br><br>**Scenario 2 — Lote restringido**<br>**Given** el stock está vencido, retenido, en cuarentena o asignado<br>**When** se comprueba<br>**Then** no se trata como libremente vendible.<br><br>**Scenario 3 — Información desactualizada**<br>**Given** la información está desactualizada o no disponible<br>**When** el operador inicia el trabajo<br>**Then** Nexa exige confirmación actual.<br><br>**Scenario 4 — Otro alcance**<br>**Given** el lote pertenece a otra empresa o almacén<br>**When** se comprueba<br>**Then** no se expone ningún dato de cantidad ni lote. |  |  |

#### MOB-US-016 — Preparar el lote y cantidad correctos para el trabajo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-016` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Preparar el lote y cantidad correctos para el trabajo |  |  |
| **Description** | Como **Warehouse Operator**, deseo hacer picking del lote y cantidad correctos para el trabajo preparado, para que la entrega reciba el stock realmente preparado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Picking FEFO**<br>**Given** existe una asignación activa y lotes elegibles<br>**When** el operador selecciona el lote adecuado más antiguo<br>**Then** Nexa registra el picking contra ese lote y cantidad.<br><br>**Scenario 2 — Picking inseguro**<br>**Given** el lote es desconocido, vencido, está en cuarentena o no está asignado<br>**When** el operador intenta seleccionarlo<br>**Then** Nexa rechaza el picking sin consumir stock.<br><br>**Scenario 3 — Exceso de stock**<br>**Given** la cantidad solicitada excede la asignación restante<br>**When** el operador hace picking<br>**Then** Nexa rechaza el exceso y conserva la cantidad restante.<br><br>**Scenario 4 — Picking repetido**<br>**Given** el resultado es desconocido<br>**When** el operador repite el mismo picking<br>**Then** Nexa devuelve un único resultado y no consume stock dos veces. |  |  |

#### MOB-US-017 — Reportar una discrepancia física o disposición autorizada de stock

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-017` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Reportar una discrepancia física o disposición autorizada de stock |  |  |
| **Description** | Como **Warehouse Operator**, deseo reportar una discrepancia física o disposición autorizada del stock, para mantener visible la excepción sin borrar lo ocurrido. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Diferencia observada**<br>**Given** el operador observa una diferencia<br>**When** se acepta el reporte autorizado<br>**Then** las cantidades ofrecidas, seleccionadas y restantes permanecen registradas por separado.<br><br>**Scenario 2 — Autoridad faltante**<br>**Given** falta permiso, motivo o evidencia requerida<br>**When** el operador reporta la diferencia<br>**Then** Nexa no registra ningún cambio de stock no autorizado.<br><br>**Scenario 3 — Reporte repetido**<br>**Given** el resultado es desconocido<br>**When** el operador repite el mismo reporte<br>**Then** Nexa conserva un único hecho de discrepancia.<br><br>**Scenario 4 — Nota sin conexión**<br>**Given** el operador no tiene conexión<br>**When** prepara un reporte<br>**Then** queda marcado como no confirmado y no puede cambiar el stock vendible. |  |  |

#### MOB-US-019 — Registrar evidencia de temperatura para stock relevante

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-019` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Registrar evidencia de temperatura para stock relevante |  |  |
| **Description** | Como **Warehouse Operator**, deseo registrar evidencia de temperatura para el stock relevante, para que las decisiones de cadena de frío usen una lectura física atribuible. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Lectura válida**<br>**Given** el operador tiene permiso y se conoce un lote o almacén<br>**When** registra una lectura válida<br>**Then** Nexa conserva valor, unidad, momento, persona y sujeto.<br><br>**Scenario 2 — Lectura preocupante**<br>**Given** una lectura está fuera del rango aceptado<br>**When** se registra<br>**Then** Nexa conserva la evidencia y no toma una decisión silenciosa de liberación.<br><br>**Scenario 3 — Lectura incompleta**<br>**Given** falta el sujeto o la unidad<br>**When** se registra la lectura<br>**Then** Nexa la rechaza sin crear evidencia incompleta.<br><br>**Scenario 4 — Fallo temporal**<br>**Given** no se puede confirmar la lectura<br>**When** el operador prepara la evidencia<br>**Then** permanece pendiente y no se afirma una disposición final del stock. |  |  |

#### MOB-US-011 — Identificar un producto mediante el código del paquete o etiqueta

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-011` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Identificar un producto mediante el código del paquete o etiqueta |  |  |
| **Description** | Como **Warehouse Operator**, deseo identificar un producto desde el código del paquete o etiqueta, para manipular el producto correcto durante el trabajo de almacén. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Una coincidencia**<br>**Given** un código permitido tiene una única coincidencia<br>**When** el operador lo proporciona<br>**Then** Nexa identifica el producto antes de cualquier acción de stock.<br><br>**Scenario 2 — Código desconocido**<br>**Given** el código es desconocido, ambiguo o está fuera del alcance de la persona<br>**When** el operador lo proporciona<br>**Then** Nexa lo rechaza y no adivina.<br><br>**Scenario 3 — Cámara no disponible**<br>**Given** la cámara o el scanner no está disponible<br>**When** el operador no puede proporcionar un código<br>**Then** puede usar la búsqueda manual de producto.<br><br>**Scenario 4 — Identificación repetida**<br>**Given** el operador proporciona nuevamente el mismo código<br>**When** Nexa lo resuelve<br>**Then** la identificación por sí sola no crea un hecho de recepción ni de picking. |  |  |

#### MOB-US-012 — Buscar manualmente un producto cuando no hay escaneo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-012` | Warehouse Operator | Critical | `MOBILE-EPIC-02` — Recepción, identificación y preparación de almacén |
| **Title** | Buscar manualmente un producto cuando no hay escaneo |  |  |
| **Description** | Como **Warehouse Operator**, deseo buscar manualmente un producto cuando el escaneo no está disponible, para continuar el trabajo seguro sin adivinar el producto. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Coincidencia exacta**<br>**Given** se encuentra un producto permitido exacto<br>**When** el operador lo selecciona<br>**Then** Nexa identifica el producto para el siguiente paso.<br><br>**Scenario 2 — Coincidencia ambigua**<br>**Given** varios productos podrían coincidir<br>**When** el operador busca<br>**Then** Nexa exige una elección clara y no registra ningún hecho de stock.<br><br>**Scenario 3 — Sin conexión**<br>**Given** el operador no tiene conexión<br>**When** no se puede confirmar un producto<br>**Then** Nexa marca la elección como no verificada y bloquea el trabajo autoritativo de stock.<br><br>**Scenario 4 — Selección repetida**<br>**Given** el operador selecciona nuevamente el mismo producto<br>**When** repite la selección<br>**Then** no se duplica ningún hecho de recepción ni picking. |  |  |

#### MOB-US-020 — Ver entregas listas para preparar el despacho

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-020` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |
| **Title** | Ver entregas listas para preparar el despacho |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo ver las entregas listas para preparación del despacho, para preparar únicamente entregas listas para salir del almacén. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Entrega lista**<br>**Given** una entrega cumple sus condiciones de preparación<br>**When** el coordinador la comprueba<br>**Then** se identifica como lista para trabajo de despacho.<br><br>**Scenario 2 — No lista**<br>**Given** la asignación, picking o evidencia están incompletos<br>**When** el coordinador comprueba la entrega<br>**Then** no se presenta como lista.<br><br>**Scenario 3 — Preparación desactualizada**<br>**Given** la información de disponibilidad está desactualizada<br>**When** el coordinador inicia la preparación<br>**Then** Nexa exige una comprobación actual.<br><br>**Scenario 4 — Alcance incorrecto**<br>**Given** la entrega pertenece a otra empresa o almacén<br>**When** se comprueba<br>**Then** no se expone. |  |  |

#### MOB-US-022 — Comprobar bienes salientes contra la entrega preparada

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-022` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |
| **Title** | Comprobar bienes salientes contra la entrega preparada |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo comprobar los bienes salientes contra la entrega preparada, para que el conductor reciba lo que la entrega realmente requiere. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Bienes coincidentes**<br>**Given** los bienes salientes coinciden con la asignación actual<br>**When** el coordinador los comprueba<br>**Then** Nexa registra que la preparación del handoff coincide.<br><br>**Scenario 2 — Diferencia**<br>**Given** el lote o cantidad difiere de la asignación<br>**When** el coordinador lo comprueba<br>**Then** Nexa detiene el handoff y conserva la discrepancia.<br><br>**Scenario 3 — Asignación modificada**<br>**Given** la asignación cambió después de la preparación<br>**When** el coordinador comprueba los bienes<br>**Then** Nexa exige una decisión de preparación nueva.<br><br>**Scenario 4 — Comprobación repetida**<br>**Given** se comprueban nuevamente los mismos bienes<br>**When** el coordinador repite la comprobación<br>**Then** la comprobación no crea un segundo movimiento de stock. |  |  |

#### MOB-US-023 — Conservar evidencia del handoff entre almacén y conductor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-023` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |
| **Title** | Conservar evidencia del handoff entre almacén y conductor |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo conservar la evidencia del handoff entre almacén y conductor, para que el movimiento de bienes preparados pueda revisarse. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Evidencia completa**<br>**Given** se conocen la entrega, los bienes y las personas responsables<br>**When** se registra el handoff<br>**Then** Nexa conserva la evidencia con momento e identidad de entrega.<br><br>**Scenario 2 — Evidencia faltante**<br>**Given** falta evidencia requerida<br>**When** el coordinador registra el handoff<br>**Then** Nexa lo deja no confirmado.<br><br>**Scenario 3 — Fallo de evidencia**<br>**Given** no se puede confirmar la evidencia<br>**When** el coordinador reintenta<br>**Then** Nexa muestra el estado no resuelto y no afirma un handoff completado.<br><br>**Scenario 4 — Handoff repetido**<br>**Given** se vuelve a enviar el mismo handoff<br>**When** Nexa lo recibe<br>**Then** permanece un único hecho de handoff y no se borra evidencia anterior. |  |  |

#### MOB-US-024 — Identificar de forma confiable un handoff de despacho

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-024` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |
| **Title** | Identificar de forma confiable un handoff de despacho |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo identificar de forma confiable un handoff de despacho, para mantener vinculados la entrega correcta y el conductor durante todo el handoff. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Handoff conocido**<br>**Given** existe una entrega preparada y un conductor asignado<br>**When** el coordinador identifica el handoff<br>**Then** Nexa lo vincula con esa entrega y asignación.<br><br>**Scenario 2 — Handoff incorrecto**<br>**Given** un identificador pertenece a otra entrega<br>**When** se utiliza<br>**Then** Nexa lo rechaza y no cambia ningún hecho de entrega.<br><br>**Scenario 3 — Identidad expirada**<br>**Given** la identidad del handoff ya no es válida<br>**When** se utiliza<br>**Then** Nexa exige un nuevo handoff autorizado.<br><br>**Scenario 4 — Significados separados**<br>**Given** el handoff está identificado<br>**When** se resuelve su identidad<br>**Then** Nexa no lo trata como Driver outcome ni como Buyer Receipt. |  |  |

#### MOB-US-021 — Asignar un conductor a una entrega lista

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-021` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |
| **Title** | Asignar un conductor a una entrega lista |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo asignar un conductor a una entrega lista, para que la responsabilidad quede clara antes del handoff. |  |  |
| **Acceptance Criteria** | **Scenario 1 — conductor elegible**<br>**Given** una entrega está lista y un conductor es elegible<br>**When** el coordinador lo asigna<br>**Then** Nexa registra una única asignación.<br><br>**Scenario 2 — Asignación no elegible**<br>**Given** la entrega o el conductor no son elegibles<br>**When** el coordinador realiza la asignación<br>**Then** Nexa la rechaza y no cambia la responsabilidad de la entrega.<br><br>**Scenario 3 — Asignación desactualizada**<br>**Given** la entrega cambió después de ser leída<br>**When** el coordinador asigna el conductor<br>**Then** Nexa solicita información actual en lugar de sobrescribir el cambio.<br><br>**Scenario 4 — Asignación repetida**<br>**Given** el coordinador repite la misma asignación<br>**When** Nexa la recibe<br>**Then** la entrega conserva un único resultado de asignación. |  |  |

#### MOB-US-025 — Confirmar que los bienes dejaron el control del almacén

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-025` | Dispatch Coordinator | Critical | `MOBILE-EPIC-03` — Preparación de despacho y Dispatch Handoff |
| **Title** | Confirmar que los bienes dejaron el control del almacén |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo confirmar que los bienes dejaron el control del almacén, para que todos puedan confiar en el estado del despacho de la entrega. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Handoff completo**<br>**Given** asignación, comprobaciones salientes, asignación del conductor y evidencia de handoff están completas<br>**When** el coordinador confirma el despacho<br>**Then** Nexa registra la entrega como dispatched.<br><br>**Scenario 2 — Handoff incompleto**<br>**Given** cualquier comprobación requerida está incompleta<br>**When** el coordinador confirma el despacho<br>**Then** Nexa deja la entrega como undispatched.<br><br>**Scenario 3 — Entrega modificada**<br>**Given** la entrega cambió después de la preparación<br>**When** el coordinador confirma el despacho<br>**Then** Nexa exige comprobaciones actuales en lugar de sobrescribir el cambio.<br><br>**Scenario 4 — Resultado incierto**<br>**Given** la confirmación pudo tener éxito<br>**When** el coordinador reintenta<br>**Then** Nexa resuelve un único resultado de despacho sin duplicar la transición. |  |  |

#### MOB-US-026 — Ver entregas asignadas al conductor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-026` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Ver entregas asignadas al conductor |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo ver las entregas asignadas a mí, para conocer las entregas de las que soy responsable hoy. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Asignaciones actuales**<br>**Given** el conductor está autorizado<br>**When** se comprueban sus entregas asignadas<br>**Then** solo se muestran sus entregas actuales.<br><br>**Scenario 2 — Asignación retirada**<br>**Given** se retira una asignación<br>**When** el conductor vuelve a comprobar<br>**Then** la entrega deja de tratarse como asignada.<br><br>**Scenario 3 — Lista desactualizada**<br>**Given** la lista de asignaciones está desactualizada<br>**When** el conductor inicia el trabajo<br>**Then** Nexa exige confirmación actual.<br><br>**Scenario 4 — Entrega de otro conductor**<br>**Given** una entrega pertenece a otro conductor<br>**When** se solicita<br>**Then** no se expone información protegida de la entrega. |  |  |

#### MOB-US-027 — Iniciar una entrega asignada

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-027` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Iniciar una entrega asignada |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo iniciar una entrega asignada, para que el Delivery Attempt tenga un inicio claro y autorizado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Inicio asignado**<br>**Given** la entrega está asignada y lista<br>**When** el conductor la inicia<br>**Then** Nexa registra un único Delivery Attempt activo.<br><br>**Scenario 2 — Inicio no asignado**<br>**Given** la entrega no está asignada al conductor<br>**When** intenta iniciarla<br>**Then** Nexa la rechaza y no registra ningún Attempt.<br><br>**Scenario 3 — Ya iniciada**<br>**Given** ya existe un Attempt<br>**When** el conductor la inicia nuevamente<br>**Then** Nexa devuelve el Attempt actual sin crear otro.<br><br>**Scenario 4 — Sin conexión**<br>**Given** no se puede confirmar el inicio<br>**When** el conductor intenta comenzar<br>**Then** Nexa muestra un estado no confirmado y no afirma un Attempt activo. |  |  |

#### MOB-US-028 — Abrir indicaciones hacia el destino autorizado de la entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-028` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Abrir indicaciones hacia el destino autorizado de la entrega |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo abrir indicaciones hacia el destino autorizado de la entrega, para viajar al destino correcto sin cambiar el registro de entrega. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Destino autorizado**<br>**Given** una entrega activa y autorizada tiene destino<br>**When** el conductor solicita indicaciones<br>**Then** Nexa entrega ese destino al servicio de navegación elegido.<br><br>**Scenario 2 — Destino faltante**<br>**Given** falta el destino o no está autorizado<br>**When** se solicitan indicaciones<br>**Then** Nexa no revela una ubicación no verificada.<br><br>**Scenario 3 — Navegación no disponible**<br>**Given** el servicio de navegación no está disponible<br>**When** se solicitan indicaciones<br>**Then** el Delivery Attempt no cambia y el fallo queda claro.<br><br>**Scenario 4 — Sin seguimiento almacenado**<br>**Given** se abren las indicaciones<br>**When** termina el handoff<br>**Then** Nexa no almacena ubicación continua ni background del conductor por esta acción. |  |  |

#### MOB-US-031 — Registrar el resultado del intento de entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-031` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Registrar el resultado del intento de entrega |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo registrar el resultado del intento de entrega, para que el proveedor conozca lo ocurrido físicamente en el destino. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Resultado permitido**<br>**Given** existe un Attempt activo y asignado<br>**When** el conductor registra un resultado permitido<br>**Then** Nexa conserva resultado, persona y momento.<br><br>**Scenario 2 — Resultado inválido**<br>**Given** el Attempt no está activo o el conductor no está autorizado<br>**When** se registra un resultado<br>**Then** Nexa no cambia el estado de entrega.<br><br>**Scenario 3 — Evidencia requerida**<br>**Given** el resultado necesita evidencia que falta<br>**When** el conductor lo registra<br>**Then** Nexa deja el resultado no confirmado.<br><br>**Scenario 4 — Resultado repetido**<br>**Given** el resultado es desconocido<br>**When** el conductor repite el mismo resultado<br>**Then** Nexa devuelve un único resultado y no sobrescribe el historial. |  |  |

#### MOB-US-032 — Registrar una entrega parcial o rechazada y lo que queda

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-032` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Registrar una entrega parcial o rechazada y lo que queda |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo registrar una entrega parcial o rechazada y lo que queda, para no perder ningún resultado físico ni obligación restante. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Entrega parcial**<br>**Given** el conductor proporciona cantidades entregadas y restantes válidas<br>**When** registra el resultado parcial<br>**Then** Nexa conserva por separado las cantidades entregadas, rechazadas y restantes.<br><br>**Scenario 2 — Entrega rechazada**<br>**Given** los bienes son rechazados con un motivo<br>**When** se registra el rechazo<br>**Then** Nexa conserva el motivo y no declara completa la entrega.<br><br>**Scenario 3 — Continuación**<br>**Given** queda cantidad para una entrega futura<br>**When** se confirma el resultado<br>**Then** Nexa crea únicamente la continuación autorizada.<br><br>**Scenario 4 — Resultado incierto**<br>**Given** el resultado es desconocido<br>**When** el conductor reintenta<br>**Then** Nexa devuelve un único resultado y no sobrescribe hechos previos. |  |  |

#### MOB-US-033 — Conservar el Proof of Delivery

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-033` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Conservar el Proof of Delivery |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo conservar el Proof of Delivery, para que el resultado de entrega pueda revisarse sin perder su historial. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Proof requerido**<br>**Given** el Attempt y los requisitos de evidencia son válidos<br>**When** el conductor proporciona el proof requerido<br>**Then** Nexa conserva su identidad, persona y momento.<br><br>**Scenario 2 — Proof faltante**<br>**Given** falta el proof requerido o es inválido<br>**When** el conductor finaliza el Attempt<br>**Then** Nexa no afirma un proof completado.<br><br>**Scenario 3 — Fallo temporal**<br>**Given** no se puede confirmar el proof<br>**When** el conductor reintenta<br>**Then** Nexa mantiene visible el estado no resuelto y no completa falsamente la entrega.<br><br>**Scenario 4 — Proof repetido**<br>**Given** se proporciona nuevamente el mismo proof<br>**When** Nexa lo recibe<br>**Then** permanece un único hecho de proof y no se borra evidencia anterior. |  |  |

#### MOB-US-034 — Presentar un código acotado de handoff de entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-034` | Driver or Delivery Operator | Critical | `MOBILE-EPIC-04` — Ejecución de Delivery y Proof of Delivery |
| **Title** | Presentar un código acotado de handoff de entrega |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo presentar un código acotado de handoff de entrega, para que el comprador identifique correctamente la entrega de forma segura. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Código válido**<br>**Given** existe una entrega activo y autorizado<br>**When** el conductor presenta su código<br>**Then** Nexa vincula el código con esa entrega y Delivery Attempt.<br><br>**Scenario 2 — Código expirado o incorrecto**<br>**Given** el código está expirado, reutilizado o pertenece a otro entrega<br>**When** se comprueba<br>**Then** Nexa lo rechaza sin cambiar el estado de entrega.<br><br>**Scenario 3 — Código no disponible**<br>**Given** no se puede presentar el código<br>**When** el conductor usa el alternativa aprobado<br>**Then** el handoff permanece explícito y no se registra aceptación falsa.<br><br>**Scenario 4 — Hechos separados**<br>**Given** el comprador verifica el código<br>**When** la verificación tiene éxito<br>**Then** por sí sola no crea recepción, POD, pago ni finalización de entrega. |  |  |

#### MOB-US-044 — Saber cuándo una entrega requiere atención

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-044` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |
| **Title** | Saber cuándo una entrega requiere atención |  |  |
| **Description** | Como **Customer Buyer**, deseo saber cuándo una entrega requiere atención, para responder oportunamente a un cambio relevante. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Actualización relevante**<br>**Given** un hecho permitido de entrega requiere atención del comprador<br>**When** Nexa envía una actualización<br>**Then** el comprador puede identificar la entrega relevante.<br><br>**Scenario 2 — Actualización no relacionada**<br>**Given** la entrega está fuera de la relación del comprador<br>**When** se prepara una actualización<br>**Then** no se revela información privada de la entrega.<br><br>**Scenario 3 — Fallo de entrega**<br>**Given** una actualización no puede entregarse<br>**When** el comprador abre Nexa<br>**Then** los hechos actuales de entrega siguen disponibles para actualización y ningún hecho cambia.<br><br>**Scenario 4 — Reintento de actualización**<br>**Given** una actualización se repite<br>**When** el comprador la recibe<br>**Then** no crea un segundo entrega, recepción ni hecho de discrepancia. |  |  |

#### MOB-US-047 — Verificar una entrega mediante el código de handoff

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-047` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |
| **Title** | Verificar una entrega mediante el código de handoff |  |  |
| **Description** | Como **Customer Buyer**, deseo verificar una entrega mediante el código de handoff, para confirmar que reviso la entrega correcta. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Código coincidente**<br>**Given** existe un código válido, no expirado y una relación autorizada<br>**When** el comprador lo verifica<br>**Then** Nexa identifica la entrega y Delivery Attempt coincidentes.<br><br>**Scenario 2 — Código inválido**<br>**Given** el código está expirado, reutilizado, malformado o no relacionado<br>**When** el comprador lo verifica<br>**Then** Nexa lo rechaza y no cambia ningún hecho de recepción.<br><br>**Scenario 3 — Sin conexión**<br>**Given** no se puede confirmar el código<br>**When** el comprador lo verifica<br>**Then** Nexa muestra un estado no confirmado y ningún recepción tiene éxito.<br><br>**Scenario 4 — Límite de verificación**<br>**Given** el código está verificado<br>**When** el comprador continúa<br>**Then** la verificación por sí sola no confirma cantidades, POD, pago ni finalización de entrega. |  |  |

#### MOB-US-048 — Confirmar las cantidades realmente recibidas

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-048` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |
| **Title** | Confirmar las cantidades realmente recibidas |  |  |
| **Description** | Como **Customer Buyer**, deseo confirmar las cantidades realmente recibidas, para que el proveedor tenga un registro veraz de mi Buyer Receipt. |  |  |
| **Acceptance Criteria** | **Scenario 1 — recepción coincidente**<br>**Given** existe un handoff verificado y autorizado<br>**When** el comprador confirma las cantidades recibidas<br>**Then** Nexa registra un único hecho de Buyer Receipt con persona, momento y entrega.<br><br>**Scenario 2 — Cantidades diferentes**<br>**Given** las cantidades recibidas difieren del resultado del conductor<br>**When** el comprador las confirma<br>**Then** ambos hechos permanecen separados y la diferencia queda visible.<br><br>**Scenario 3 — Handoff desactualizado o reutilizado**<br>**Given** el handoff está desactualizado, expirado o ya utilizado<br>**When** el comprador confirma cantidades<br>**Then** Nexa rechaza la confirmación o devuelve el resultado original sin un segundo recepción.<br><br>**Scenario 4 — Sin conexión**<br>**Given** no se puede comprobar la confirmación del recepción<br>**When** el comprador lo intenta<br>**Then** Nexa no muestra éxito de recepción hasta recibir confirmación. |  |  |

#### MOB-US-049 — Reportar una discrepancia sin borrar los hechos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-049` | Customer Buyer | Critical | `MOBILE-EPIC-05` — Handoff de Delivery, Buyer Receipt y actualizaciones críticas |
| **Title** | Reportar una discrepancia sin borrar los hechos |  |  |
| **Description** | Como **Customer Buyer**, deseo reportar una discrepancia sin borrar los hechos, para que el proveedor resuelva la diferencia manteniendo un historial confiable. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Discrepancia registrada**<br>**Given** existe un contexto de handoff o recepción verificado<br>**When** el comprador reporta una discrepancia<br>**Then** Nexa conserva motivo, cantidad afectada, persona, momento y evidencia.<br><br>**Scenario 2 — Historiales separados**<br>**Given** el resultado del Driver outcome difiere del Buyer Receipt<br>**When** se registra la discrepancia<br>**Then** ambos hechos originales permanecen sin cambios y la diferencia queda visible.<br><br>**Scenario 3 — Reporte inválido**<br>**Given** falta motivo, permiso o evidencia requerida<br>**When** el comprador lo reporta<br>**Then** Nexa no registra una corrección no autorizada.<br><br>**Scenario 4 — Fallo temporal**<br>**Given** no se puede confirmar el reporte<br>**When** el comprador reintenta<br>**Then** Nexa conserva un único resultado pendiente o aceptado y no implica reembolso, cambio de pago ni finalización de entrega. |  |  |

#### MOB-US-001 — Continuar el trabajo autorizado después de volver a Nexa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-001` | Mobile User | High | `MOBILE-EPIC-01` — Acceso seguro y contexto de trabajo |
| **Title** | Continuar el trabajo autorizado después de volver a Nexa |  |  |
| **Description** | Como **Mobile User**, deseo continuar de forma segura el trabajo autorizado al volver a Nexa, para reanudarlo sin exponer información protegida. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Retorno válido**<br>**Given** una sesión válida y no revocada<br>**When** la persona vuelve a Nexa<br>**Then** Nexa confirma su identidad y expone solo el trabajo permitido.<br><br>**Scenario 2 — Retorno expirado**<br>**Given** una sesión expirada, revocada o malformada<br>**When** la persona vuelve<br>**Then** Nexa solicita nuevamente su identidad y no expone información protegida.<br><br>**Scenario 3 — Confirmación no disponible**<br>**Given** no se puede confirmar la identidad<br>**When** la persona vuelve sin conexión<br>**Then** Nexa indica que el trabajo no está disponible y no expone información protegida.<br><br>**Scenario 4 — Reintento seguro**<br>**Given** la persona repite el mismo retorno<br>**When** Nexa lo procesa<br>**Then** no duplica ninguna acción de negocio ni revela secretos. |  |  |

#### MOB-US-002 — Trabajar en la empresa y contexto de negocio previstos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-002` | Mobile User | High | `MOBILE-EPIC-01` — Acceso seguro y contexto de trabajo |
| **Title** | Trabajar en la empresa y contexto de negocio previstos |  |  |
| **Description** | Como **Mobile User**, deseo trabajar en la empresa y contexto de negocio previstos, para que cada tarea corresponda a la empresa y relación que pretendo atender. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Un contexto autorizado**<br>**Given** existe un contexto autorizado<br>**When** la persona inicia el trabajo<br>**Then** Nexa usa ese contexto para cada lectura y acción permitida.<br><br>**Scenario 2 — Varios contextos autorizados**<br>**Given** existen varios contextos<br>**When** la persona elige uno<br>**Then** Nexa confirma la elección antes de mostrar trabajo protegido.<br><br>**Scenario 3 — Contexto ya no válido**<br>**Given** un contexto está suspendido o no autorizado<br>**When** la persona lo elige<br>**Then** Nexa lo rechaza y no expone información empresarial de ese alcance.<br><br>**Scenario 4 — Cambio de contexto**<br>**Given** la persona cambia de contexto<br>**When** el cambio tiene éxito<br>**Then** la información del contexto anterior no puede utilizarse en el nuevo. |  |  |

#### MOB-US-003 — Ver sólo el trabajo permitido para el rol

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-003` | Mobile User | High | `MOBILE-EPIC-01` — Acceso seguro y contexto de trabajo |
| **Title** | Ver sólo el trabajo permitido para el rol |  |  |
| **Description** | Como **Mobile User**, deseo ver solo el trabajo permitido para mi rol, para no intentar tareas que mi rol o relación no autorizan. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Trabajo permitido**<br>**Given** el rol de la persona permite una tarea<br>**When** Nexa confirma el rol<br>**Then** la persona puede realizarla en el contexto activo.<br><br>**Scenario 2 — Permiso faltante**<br>**Given** el rol no permite una tarea<br>**When** la persona intenta realizarla<br>**Then** Nexa la rechaza aunque información antigua sugiera lo contrario.<br><br>**Scenario 3 — Cambio de permisos**<br>**Given** cambian los permisos<br>**When** Nexa vuelve a comprobar el rol<br>**Then** el trabajo no disponible deja de aceptarse.<br><br>**Scenario 4 — Permiso no confirmado**<br>**Given** no se puede comprobar el permiso<br>**When** la persona intenta una tarea<br>**Then** Nexa la bloquea e indica que se requiere confirmación. |  |  |
