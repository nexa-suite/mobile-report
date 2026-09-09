# Mobile Functional Stories V2

Estas capacidades permanecen en roadmap diferido. Su presencia conserva el inventario de producto, pero no amplía el compromiso de implementación del curso.

#### MOB-US-050 — Gestionar una discrepancia de recepción con evidencia

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-050` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Gestionar una discrepancia de recepción con evidencia |  |  |
| **Description** | Como **Warehouse Operator**, deseo registrar una discrepancia de recepción de entrada con evidencia, para que la decisión de recepción refleje lo encontrado físicamente. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Diferencia capturada**<br>**Given** se inspecciona una entrega de entrada<br>**When** el operador registra daño, fuga, producto incorrecto o cantidad incorrecta<br>**Then** Nexa conserva motivo, artículos afectados y evidencia para revisión.<br><br>**Scenario 2 — recepción controlado**<br>**Given** se registra una discrepancia<br>**When** el operador envía el resultado de recepción<br>**Then** Nexa no incrementa el stock vendible más allá de los hechos confirmados.<br><br>**Scenario 3 — Evidencia faltante**<br>**Given** falta un hecho o evidencia requerida<br>**When** el operador intenta enviar la discrepancia<br>**Then** Nexa explica qué falta y no registra una decisión incompleta. |  |  |

#### MOB-US-051 — Retener o poner en cuarentena stock y resolverlo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-051` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Retener o poner en cuarentena stock y resolverlo |  |  |
| **Description** | Como **Warehouse Operator**, deseo colocar stock cuestionable en retención o cuarentena y registrar su resolución, para impedir su uso antes de una decisión autorizada. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Proteger stock**<br>**Given** un lote tiene una condición que impide su uso normal<br>**When** el operador registra el motivo de retención o cuarentena<br>**Then** Nexa retira la cantidad afectada del trabajo disponible aplicable.<br><br>**Scenario 2 — Resolución autorizada**<br>**Given** un lote retenido fue revisado<br>**When** una persona autorizada lo libera o dispone de él<br>**Then** Nexa registra decisión, motivo y cantidad afectada sin borrar el historial de retención.<br><br>**Scenario 3 — Decisión desactualizada**<br>**Given** el lote cambió después de ser visualizado<br>**When** el operador intenta resolverlo<br>**Then** Nexa rechaza la decisión desactualizada y muestra el estado actual. |  |  |

#### MOB-US-018 — Mover stock entre ubicaciones del almacén

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-018` | Warehouse Operator | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |
| **Title** | Mover stock entre ubicaciones del almacén |  |  |
| **Description** | Como **Warehouse Operator**, deseo mover stock entre ubicaciones del almacén, para que el movimiento físico sea atribuible desde el origen hasta el destino. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Movimiento autorizado**<br>**Given** existen origen, destino, lote y cantidad autorizados<br>**When** el operador inicia una transferencia<br>**Then** Nexa conserva esos datos para revisión.<br><br>**Scenario 2 — Dato de transferencia faltante**<br>**Given** falta origen, destino, lote o motivo requerido<br>**When** el operador inicia la transferencia<br>**Then** Nexa deja el stock sin cambios.<br><br>**Scenario 3 — Destino incompatible**<br>**Given** el destino no puede aceptar la transferencia<br>**When** el operador la registra<br>**Then** Nexa mantiene la transferencia sin resolver y no afirma recepción.<br><br>**Scenario 4 — Reintento**<br>**Given** el resultado de la transferencia es desconocido<br>**When** el operador repite el movimiento<br>**Then** permanece una única transferencia trazable. |  |  |

#### MOB-US-052 — Confirmar la recepción en el destino de una transferencia interna

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-052` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Confirmar la recepción en el destino de una transferencia interna |  |  |
| **Description** | Como **Warehouse Operator**, deseo confirmar lo que llegó al destino de una transferencia interna, para que el registro de stock refleje el movimiento físico y cualquier diferencia. |  |  |
| **Acceptance Criteria** | **Scenario 1 — recepción completo**<br>**Given** una transferencia autorizada está en tránsito<br>**When** el operador destino confirma lote y cantidad esperados<br>**Then** Nexa registra destination recepción y cierra el movimiento de transferencia.<br><br>**Scenario 2 — recepción parcial o diferente**<br>**Given** el destino recibe otro lote o cantidad<br>**When** el operador lo registra<br>**Then** Nexa mantiene separados los hechos de origen y destino y expone la diferencia para resolución.<br><br>**Scenario 3 — recepción repetido**<br>**Given** destination recepción ya tiene un resultado aceptado<br>**When** el operador reintenta<br>**Then** Nexa devuelve el resultado original sin un segundo recepción. |  |  |

#### MOB-US-053 — Realizar un conteo cíclico y solicitar corrección de stock

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-053` | Warehouse Operator | High | `MOBILE-EPIC-08` — Transferencias y exactitud de inventario |
| **Title** | Realizar un conteo cíclico y solicitar corrección de stock |  |  |
| **Description** | Como **Warehouse Operator**, deseo contar una ubicación de almacenamiento y solicitar una corrección de stock, para resolver una diferencia física sin reescribir el historial. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Conteo registrado**<br>**Given** existe una ubicación permitida y una vista actual del stock<br>**When** el operador registra lote y cantidad observados<br>**Then** Nexa conserva el conteo con persona, momento y ubicación.<br><br>**Scenario 2 — Corrección revisada**<br>**Given** el conteo difiere del stock registrado<br>**When** se aprueba una corrección autorizada<br>**Then** Nexa registra evidencia correctiva y la cantidad resultante sin borrar movimientos anteriores.<br><br>**Scenario 3 — Cambio concurrente**<br>**Given** el stock cambió después de iniciar el conteo<br>**When** el operador envía la corrección<br>**Then** Nexa rechaza o reabre el conteo desactualizado en lugar de aplicar una corrección última escritura gana. |  |  |

#### MOB-US-057 — Resolver una discrepancia de despacho antes del handoff

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-057` | Dispatch Coordinator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Resolver una discrepancia de despacho antes del handoff |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo resolver una discrepancia de despacho antes del handoff, para que solo una entrega revisada abandone el control del almacén. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Diferencia identificada**<br>**Given** los bienes salientes no coinciden con la entrega preparada<br>**When** el coordinador registra la diferencia<br>**Then** Nexa identifica la entrega, lote o cantidad afectados y bloquea el handoff inseguro.<br><br>**Scenario 2 — Resolución autorizada**<br>**Given** la diferencia tiene una resolución aceptada<br>**When** el coordinador confirma la siguiente acción<br>**Then** Nexa actualiza la disponibilidad de despacho con evidencia trazable.<br><br>**Scenario 3 — Preparación desactualizada**<br>**Given** la entrega cambió después de la preparación<br>**When** el coordinador resuelve la discrepancia<br>**Then** Nexa solicita una decisión nueva en lugar de sobrescribir los hechos actuales. |  |  |

#### MOB-US-058 — Reasignar un conductor o reprogramar el despacho de forma segura

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-058` | Dispatch Coordinator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Reasignar un conductor o reprogramar el despacho de forma segura |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo reasignar un conductor o reprogramar un despacho de forma segura, para que la entrega siga siendo responsabilidad de una persona elegible en un momento acordado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Reasignación elegible**<br>**Given** una entrega preparada necesita otro conductor<br>**When** el coordinador selecciona una persona elegible<br>**Then** Nexa registra la nueva responsabilidad y conserva el historial de asignación anterior.<br><br>**Scenario 2 — Cambio de horario**<br>**Given** el despacho no puede continuar en el horario previsto<br>**When** el coordinador propone un nuevo horario<br>**Then** Nexa muestra el impacto y confirma el cambio una sola vez.<br><br>**Scenario 3 — Cambio concurrente**<br>**Given** otra persona cambió primero la entrega<br>**When** el coordinador envía el plan antiguo<br>**Then** Nexa lo rechaza y muestra la responsabilidad y horario actuales. |  |  |

#### MOB-US-061 — Registrar evidencia de temperatura en el despacho

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-061` | Dispatch Coordinator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Registrar evidencia de temperatura en el despacho |  |  |
| **Description** | Como **Dispatch Coordinator**, deseo registrar evidencia de temperatura en el despacho, para que la decisión de entrega refleje la condición observada antes del handoff. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Evidencia registrada**<br>**Given** una entrega requiere una comprobación de temperatura<br>**When** el coordinador registra la observación<br>**Then** Nexa conserva valor, unidad, persona, momento y contexto de entrega.<br><br>**Scenario 2 — Fuera de política**<br>**Given** la observación está fuera del rango aceptado<br>**When** el coordinador la envía<br>**Then** Nexa impide un despacho no revisado y muestra la decisión requerida.<br><br>**Scenario 3 — Confirmación faltante**<br>**Given** no se puede confirmar la observación<br>**When** el coordinador reintenta<br>**Then** Nexa no implica aprobación de cadena de frío. |  |  |

#### MOB-US-062 — Señalar la llegada de una entrega activa

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-062` | Driver or Delivery Operator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Señalar la llegada de una entrega activa |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo señalar la llegada de una entrega activa, para que el comprador y el equipo de entrega sepan que puede comenzar el handoff. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Llegada registrada**<br>**Given** el conductor tiene una entrega activo y autorizado<br>**When** señala su llegada<br>**Then** Nexa registra el evento y lo hace visible a destinatarios permitidos.<br><br>**Scenario 2 — Sin entrega activo**<br>**Given** el conductor no está asignado a una entrega activo<br>**When** señala llegada<br>**Then** Nexa rechaza la señal sin revelar otra entrega.<br><br>**Scenario 3 — entrega permanece abierto**<br>**Given** se registró la llegada<br>**When** el comprador o conductor consulta la entrega<br>**Then** permanece abierto hasta registrar por separado handoff y recepción. |  |  |

#### MOB-US-063 — Seguir instrucciones de entrega y datos de contacto autorizados

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-063` | Driver or Delivery Operator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Seguir instrucciones de entrega y datos de contacto autorizados |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo seguir las instrucciones y datos de contacto permitidos de la entrega, para coordinar el handoff con la persona prevista. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Contexto autorizado**<br>**Given** una entrega activa incluye instrucciones permitidas<br>**When** el conductor las abre<br>**Then** Nexa muestra solo la información necesaria para esa entrega.<br><br>**Scenario 2 — Instrucciones modificadas**<br>**Given** las instrucciones ya no son actuales<br>**When** el conductor las consulta<br>**Then** Nexa las marca como desactualizadas y exige confirmación nueva antes de usarlas.<br><br>**Scenario 3 — Información restringida**<br>**Given** un contacto o instrucción no está permitido para el conductor<br>**When** solicita acceso<br>**Then** Nexa lo oculta y explica la ruta permitida. |  |  |

#### MOB-US-065 — Registrar un incidente de entrega con mayor detalle

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-065` | Driver or Delivery Operator | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Registrar un incidente de entrega con mayor detalle |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo registrar un incidente de entrega con sus detalles relevantes, para que el equipo tome una decisión de seguimiento informada. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Incidente descrito**<br>**Given** una entrega activa encuentra un incidente permitido<br>**When** el conductor registra motivo, lugar dentro de la entrega y evidencia<br>**Then** Nexa conserva el incidente para revisión autorizada.<br><br>**Scenario 2 — El incidente no reescribe el resultado**<br>**Given** ya existe un resultado de entrega<br>**When** se añade un incidente<br>**Then** Nexa conserva el resultado original y vincula la evidencia nueva.<br><br>**Scenario 3 — Incidente incompleto**<br>**Given** faltan detalles requeridos<br>**When** el conductor intenta enviarlo<br>**Then** Nexa identifica la información faltante y no afirma un seguimiento completado. |  |  |

#### MOB-US-030 — Contactar al comprador durante la entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-030` | Driver or Delivery Operator | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |
| **Title** | Contactar al comprador durante la entrega |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo contactar al comprador durante la entrega, para resolver una duda de llegada mediante un canal autorizado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Canal futuro**<br>**Given** existe una política de contacto aceptada<br>**When** el conductor contacta al comprador<br>**Then** solo se usa el canal autorizado y su uso queda registrado.<br><br>**Scenario 2 — Consentimiento faltante**<br>**Given** falta consentimiento o asignación<br>**When** se solicita el contacto<br>**Then** no se inicia contacto personal.<br><br>**Scenario 3 — Resultado separado**<br>**Given** ocurre el contacto<br>**When** termina<br>**Then** por sí mismo no cambia el resultado de entrega ni el Buyer Receipt. |  |  |

#### MOB-US-035 — Continuar la evidencia de entrega después de perder conexión

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-035` | Driver or Delivery Operator | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |
| **Title** | Continuar la evidencia de entrega después de perder conexión |  |  |
| **Description** | Como **Driver / Delivery Operator**, deseo continuar la evidencia de entrega después de perder conexión, para que un flujo futuro de recuperación proteja la evidencia sin afirmar éxito falso. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Recuperación futura de evidencia**<br>**Given** se acepta una política futura de recuperación<br>**When** se captura evidencia sin conexión<br>**Then** su estado pendiente y contenido protegido mínimo quedan claros.<br><br>**Scenario 2 — Confirmación posterior**<br>**Given** la evidencia preparada se revisa posteriormente<br>**When** Nexa la acepta<br>**Then** solo el hecho exacto aceptado se vuelve autoritativo.<br><br>**Scenario 3 — Rechazo**<br>**Given** se rechaza la evidencia preparada<br>**When** se revisa<br>**Then** el motivo permanece claro y no se implica éxito de entrega. |  |  |

#### MOB-US-064 — Solicitar reprogramación de una entrega desde el campo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-064` | Customer Buyer | High | `MOBILE-EPIC-09` — Excepciones de despacho y coordinación de Delivery |
| **Title** | Solicitar reprogramación de una entrega desde el campo |  |  |
| **Description** | Como **Customer Buyer**, deseo solicitar un horario de entrega diferente, para que el equipo de entrega decida cómo gestionar mi disponibilidad. |  |  |
| **Acceptance Criteria** | **Scenario 1 — solicitud enviada**<br>**Given** el comprador está autorizado para una entrega activa<br>**When** propone un horario alternativo<br>**Then** Nexa registra una solicitud y muestra que espera una decisión de entrega.<br><br>**Scenario 2 — Decisión devuelta**<br>**Given** el equipo de entrega acepta o rechaza la solicitud<br>**When** el comprador consulta la entrega<br>**Then** Nexa muestra la decisión y el horario efectivo sin reescribir hechos anteriores.<br><br>**Scenario 3 — solicitud desactualizada**<br>**Given** la entrega ya es terminal o cambió<br>**When** el comprador envía la solicitud antigua<br>**Then** Nexa la rechaza con el estado actual de la entrega. |  |  |

#### MOB-US-067 — Proporcionar instrucciones de entrega y contacto alternativo para la recepción

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-067` | Customer Buyer | High | `MOBILE-EPIC-10` — Continuidad de Delivery para Customer Buyer |
| **Title** | Proporcionar instrucciones de entrega y contacto alternativo para la recepción |  |  |
| **Description** | Como **Customer Buyer**, deseo proporcionar instrucciones de entrega y un contacto alternativo para la recepción, para que la entrega llegue a la persona correcta bajo las condiciones acordadas. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Instrucciones proporcionadas**<br>**Given** el comprador está autorizado para la entrega<br>**When** guarda instrucciones<br>**Then** Nexa las asocia con esa entrega y muestra su periodo efectivo.<br><br>**Scenario 2 — Consentimiento del contacto alternativo**<br>**Given** una persona alternativa debe recibir la entrega<br>**When** el comprador proporciona contacto permitido y consentimiento<br>**Then** Nexa lo registra únicamente para el propósito de entrega definido.<br><br>**Scenario 3 — Cambio después del despacho**<br>**Given** la entrega está en un estado que no permite cambios<br>**When** el comprador edita instrucciones<br>**Then** Nexa rechaza el cambio o lo dirige a una decisión explícita. |  |  |

#### MOB-US-068 — Revisar la línea de tiempo de la entrega y reconocer su finalización

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-068` | Customer Buyer | High | `MOBILE-EPIC-10` — Continuidad de Delivery para Customer Buyer |
| **Title** | Revisar la línea de tiempo de la entrega y reconocer su finalización |  |  |
| **Description** | Como **Customer Buyer**, deseo revisar la línea de tiempo de la entrega y reconocer su finalización, para comprender el resultado registrado sin cambiar el historial. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Timeline visible**<br>**Given** el comprador puede acceder a una entrega<br>**When** abre su línea de tiempo<br>**Then** Nexa muestra los hechos autorizados ordenados y su estado actual.<br><br>**Scenario 2 — Acknowledgement separado**<br>**Given** la entrega tiene un resultado registrado<br>**When** el comprador lo reconoce<br>**Then** Nexa registra el acknowledgement separado de recepción, proof o finalización.<br><br>**Scenario 3 — Historial sin cambios**<br>**Given** el comprador reconoce una entrega<br>**When** otra persona permitida la consulta<br>**Then** los hechos subyacentes permanecen sin cambios. |  |  |

#### MOB-US-069 — Adjuntar evidencia a una discrepancia de entrega

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-069` | Customer Buyer | High | `MOBILE-EPIC-10` — Continuidad de Delivery para Customer Buyer |
| **Title** | Adjuntar evidencia a una discrepancia de entrega |  |  |
| **Description** | Como **Customer Buyer**, deseo adjuntar evidencia a una discrepancia de entrega, para que el proveedor revise la diferencia reportada con su contexto. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Evidencia adjunta**<br>**Given** el comprador tiene una discrepancia permitida<br>**When** añade evidencia<br>**Then** Nexa la vincula con esa discrepancia junto con persona y momento.<br><br>**Scenario 2 — Evidencia no soportada o insegura**<br>**Given** la evidencia no está disponible, es demasiado grande o no está permitida<br>**When** el comprador intenta añadirla<br>**Then** Nexa explica el problema y mantiene la discrepancia sin cambios.<br><br>**Scenario 3 — Hechos originales preservados**<br>**Given** la evidencia es aceptada<br>**When** se revisa la entrega<br>**Then** recepción, Driver outcome y discrepancia permanecen separados. |  |  |

#### MOB-US-046 — Contactar al conductor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-046` | Customer Buyer | High | `MOBILE-EPIC-07` — Operación de campo avanzada y continuidad selectiva |
| **Title** | Contactar al conductor |  |  |
| **Description** | Como **Customer Buyer**, deseo contactar al conductor, para resolver una duda de llegada mediante un canal autorizado de entrega. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Canal futuro**<br>**Given** existe una política de canal aceptada y una entrega activo<br>**When** el comprador contacta al conductor<br>**Then** solo se usa el canal autorizado.<br><br>**Scenario 2 — Sin permiso**<br>**Given** falta consentimiento o entrega activo<br>**When** se solicita el contacto<br>**Then** no se inicia contacto personal.<br><br>**Scenario 3 — Hechos separados**<br>**Given** ocurre el contacto<br>**When** termina<br>**Then** no cambia Driver outcome, Buyer Receipt ni el estado de entrega. |  |  |

#### MOB-US-004 — Revisar el trabajo operativo de un vistazo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-004` | Business Operations Manager | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Revisar el trabajo operativo de un vistazo |  |  |
| **Description** | Como **Business Operations Manager**, deseo revisar el trabajo operativo de un vistazo, para priorizarlo usando hechos actuales y confiables. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Vista futura**<br>**Given** existe una vista operativa futura aceptada<br>**When** el responsable la revisa<br>**Then** cada elemento indica su contexto y frescura.<br><br>**Scenario 2 — Hechos incompletos**<br>**Given** faltan hechos fuente o están desactualizados<br>**When** el responsable revisa la vista<br>**Then** la limitación es explícita y no se inventa ningún total.<br><br>**Scenario 3 — Alcance no autorizado**<br>**Given** el responsable carece de permiso de alcance<br>**When** solicita la vista<br>**Then** no se expone información operativa privada. |  |  |

#### MOB-US-005 — Identificar excepciones operativas críticas

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-005` | Business Operations Manager | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Identificar excepciones operativas críticas |  |  |
| **Description** | Como **Business Operations Manager**, deseo identificar excepciones operativas críticas, para atender trabajo bloqueado antes de que retrase a un cliente o una entrega. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Excepción aceptada**<br>**Given** existe una futura vista de excepciones aceptada<br>**When** el responsable revisa un elemento<br>**Then** quedan claros su alcance, severidad y trabajo responsable.<br><br>**Scenario 2 — Excepción incompleta**<br>**Given** los hechos de la excepción están incompletos<br>**When** se revisa el elemento<br>**Then** se marca como incompleto y no se trata como un nuevo estado de negocio.<br><br>**Scenario 3 — Respuesta autorizada**<br>**Given** una excepción requiere corrección<br>**When** el responsable la sigue<br>**Then** Nexa dirige a la persona al trabajo responsable autorizado. |  |  |

#### MOB-US-006 — Encontrar un cliente y su relación con el comprador

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-006` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Encontrar un cliente y su relación con el comprador |  |  |
| **Description** | Como **Sales Representative**, deseo encontrar una relación entre cliente y comprador, para trabajar con el cliente correcto en un flujo móvil futuro. |  |  |
| **Acceptance Criteria** | **Scenario 1 — cliente autorizado**<br>**Given** existe una relación autorizada<br>**When** el representante busca<br>**Then** solo se devuelven clientes permitidos.<br><br>**Scenario 2 — cliente no relacionado**<br>**Given** el cliente no está relacionado o está suspendido<br>**When** el representante lo abre<br>**Then** el trabajo protegido no está disponible.<br><br>**Scenario 3 — Resultado no confiable**<br>**Given** la búsqueda está vacía o no disponible<br>**When** termina<br>**Then** no se adivina ni expone ningún cliente. |  |  |

#### MOB-US-007 — Revisar productos, precios y disponibilidad

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-007` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Revisar productos, precios y disponibilidad |  |  |
| **Description** | Como **Sales Representative**, deseo revisar productos, precios y disponibilidad, para preparar demanda futura de un cliente con información confiable. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Producto autorizado**<br>**Given** existe una relación autorizada con el cliente<br>**When** se revisa un producto<br>**Then** se muestran precio y disponibilidad permitidos con su frescura.<br><br>**Scenario 2 — Producto no disponible**<br>**Given** un producto está oculto o no disponible<br>**When** se solicita<br>**Then** no puede tratarse como un compromiso.<br><br>**Scenario 3 — Información modificada**<br>**Given** cambia el precio o disponibilidad<br>**When** el representante continúa<br>**Then** Nexa exige confirmación actual. |  |  |

#### MOB-US-008 — Preparar una solicitud de cliente

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-008` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Preparar una solicitud de cliente |  |  |
| **Description** | Como **Sales Representative**, deseo preparar una solicitud de cliente, para organizar una intención antes de un envío autorizado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Preparación de borrador**<br>**Given** se conocen productos permitidos<br>**When** el representante prepara una solicitud<br>**Then** las cantidades permanecen como intención y no crean compromiso.<br><br>**Scenario 2 — Información modificada**<br>**Given** cambia información del producto o cliente<br>**When** se revisa la solicitud<br>**Then** el cambio es visible antes de la envío.<br><br>**Scenario 3 — borrador local**<br>**Given** la persona pierde conexión<br>**When** edita la solicitud<br>**Then** permanece como borrador no confirmado. |  |  |

#### MOB-US-009 — Enviar una solicitud o Direct Order asistido desde el trabajo de campo

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-009` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Enviar una solicitud o Direct Order asistido desde el trabajo de campo |  |  |
| **Description** | Como Representante de Ventas autorizado, deseo enviar la intención comercial del cliente conforme a la política del Tenant, para convertir el trabajo de campo en una solicitud o compromiso válido sin suplantar al comprador. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Política APPROVAL_REQUIRED**<br>**Given** el actor es un Representante de Ventas autorizado, existe Customer Account y Buyer Relationship con elegibilidad válida, la política comercial es APPROVAL_REQUIRED y existe un Sales Draft válido<br>**When** envía la intención comercial<br>**Then** Nexa crea y envía una Purchase Request, no confirma un Direct Order y mantiene al actor como Representante de Ventas sin suplantar al Comprador.<br><br>**Scenario 2 — Direct Order asistido**<br>**Given** el actor es un Representante de Ventas autorizado, existe Customer Account y Buyer Relationship con elegibilidad válida, la política comercial es DIRECT_ORDER y existe un Sales Draft válido<br>**When** confirma el Direct Order asistido<br>**Then** el servidor revalida autorización, relación, offer, price, terms, inventory protection y applicable credit y sólo confirma el compromiso si todas las decisiones tienen éxito, sin crear una Purchase Request artificial.<br><br>**Scenario 3 — Actor y borrador separados**<br>**Given** el Representante de Ventas trabaja dentro de su propia relación y existe un Sales Draft<br>**When** envía la intención comercial<br>**Then** el actor continúa siendo Representante de Ventas, Sales Draft != Buyer Draft y Nexa no suplanta al Comprador.<br><br>**Scenario 4 — Validación rechazada**<br>**Given** falla Customer Account, Buyer Relationship, offer, price, terms, inventory protection, applicable credit o autorización<br>**When** el representante intenta confirmar la intención<br>**Then** no se confirma un Direct Order válido ni se registra un compromiso parcial.<br><br>**Scenario 5 — Reintento idempotente**<br>**Given** el representante reenvía la misma intención comercial<br>**When** Nexa procesa el reintento<br>**Then** conserva un único resultado comercial y no duplica Purchase Request ni compromiso.<br><br>**Scenario 6 — Política vigente**<br>**Given** la política comercial cambia entre la preparación y el envío<br>**When** el representante envía su Sales Draft<br>**Then** Nexa usa la política vigente y no confirma una ruta que ya no está autorizada. |  |  |

#### MOB-US-010 — Seguir compromisos del cliente y crédito

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-010` | Sales Representative | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Seguir compromisos del cliente y crédito |  |  |
| **Description** | Como **Sales Representative**, deseo seguir los compromisos y el crédito del cliente, para comprender el progreso autorizado sin tomar localmente una decisión de crédito. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Progreso autorizado**<br>**Given** existe una relación autorizada<br>**When** se revisa el progreso<br>**Then** los hechos de compromiso y crédito relevante muestran su frescura.<br><br>**Scenario 2 — Hechos financieros incompletos**<br>**Given** los hechos financieros están desactualizados o incompletos<br>**When** se revisan<br>**Then** la limitación es explícita y no se inventa ninguna decisión.<br><br>**Scenario 3 — Pérdida de relación**<br>**Given** la relación ya no está autorizada<br>**When** se solicita el progreso<br>**Then** no se exponen hechos protegidos. |  |  |

#### MOB-US-036 — Explorar productos del proveedor

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-036` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Explorar productos del proveedor |  |  |
| **Description** | Como **Customer Buyer**, deseo explorar productos del proveedor, para revisar productos ofrecidos mediante mi relación con el proveedor. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Catálogo autorizado**<br>**Given** existe una relación activa de comprador<br>**When** se exploran productos<br>**Then** solo se muestran productos permitidos.<br><br>**Scenario 2 — Relación suspendida**<br>**Given** la relación del comprador está suspendida<br>**When** se exploran productos<br>**Then** no se expone información privada del producto.<br><br>**Scenario 3 — Información desactualizada**<br>**Given** la información del producto está desactualizada<br>**When** se explora<br>**Then** queda marcada como advisory y no crea autoridad para ordenar. |  |  |

#### MOB-US-037 — Revisar precio y disponibilidad del producto

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-037` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Revisar precio y disponibilidad del producto |  |  |
| **Description** | Como **Customer Buyer**, deseo revisar el precio y disponibilidad del producto, para preparar una solicitud futura con información actual del proveedor. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Producto actual**<br>**Given** existe una relación autorizada<br>**When** se revisa un producto<br>**Then** se muestran precio, términos y disponibilidad vendible con frescura.<br><br>**Scenario 2 — Producto desactualizado**<br>**Given** los hechos del producto están desactualizados<br>**When** el comprador continúa<br>**Then** se requiere confirmación actual.<br><br>**Scenario 3 — Producto no disponible**<br>**Given** el producto está oculto o no disponible<br>**When** se solicita<br>**Then** no puede tratarse como compromiso. |  |  |

#### MOB-US-038 — Preparar una Purchase Request

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-038` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Preparar una Purchase Request |  |  |
| **Description** | Como **Customer Buyer**, deseo preparar una Purchase Request, para organizar una compra futura sin confirmarla falsamente. |  |  |
| **Acceptance Criteria** | **Scenario 1 — borrador**<br>**Given** hay productos permitidos disponibles<br>**When** el comprador prepara una solicitud<br>**Then** permanece como borrador y no crea reserva.<br><br>**Scenario 2 — Producto modificado**<br>**Given** cambia el precio o disponibilidad<br>**When** el comprador revisa el borrador<br>**Then** el cambio es claro antes de la envío.<br><br>**Scenario 3 — Preparación local**<br>**Given** el comprador pierde conexión<br>**When** edita el borrador<br>**Then** permanece no confirmado. |  |  |

#### MOB-US-039 — Repetir una compra anterior

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-039` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Repetir una compra anterior |  |  |
| **Description** | Como **Customer Buyer**, deseo repetir una compra anterior, para preparar una nueva solicitud más rápidamente en un flujo futuro. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Historial reutilizado**<br>**Given** el comprador puede acceder al historial anterior<br>**When** lo reutiliza<br>**Then** Nexa crea un nuevo borrador y vuelve a comprobar los datos actuales del producto.<br><br>**Scenario 2 — Producto modificado**<br>**Given** un producto anterior ya no está disponible<br>**When** se reutiliza el historial<br>**Then** Nexa lo marca y no crea un pedido silencioso.<br><br>**Scenario 3 — Acción repetida**<br>**Given** el comprador repite la acción<br>**When** Nexa la procesa<br>**Then** no crea un segundo compromiso. |  |  |

#### MOB-US-040 — Enviar una solicitud o realizar un Direct Order

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-040` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Enviar una solicitud o realizar un Direct Order |  |  |
| **Description** | Como **Customer Buyer**, deseo enviar una solicitud o realizar un Direct Order, para que mi vía de compromiso elegida sea explícita y autorizada. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Purchase Request**<br>**Given** existe un borrador válido y una política válida<br>**When** el comprador envía una solicitud<br>**Then** se registra una única Purchase Request.<br><br>**Scenario 2 — Direct Order**<br>**Given** está permitido ordenar directamente<br>**When** el comprador elige esa vía<br>**Then** se registra una única ruta de Sales Order sin inventar una Purchase Request.<br><br>**Scenario 3 — Hechos modificados**<br>**Given** cambiaron precio, disponibilidad, crédito o permiso<br>**When** el comprador envía<br>**Then** no se registra ningún compromiso parcial. |  |  |

#### MOB-US-041 — Responder a un cambio material

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-041` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Responder a un cambio material |  |  |
| **Description** | Como **Customer Buyer**, deseo responder a un cambio material, para que mi compromiso futuro refleje una decisión explícita. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Aceptar cambio**<br>**Given** existe un cambio actual y autorizado<br>**When** el comprador lo acepta<br>**Then** Nexa registra el cambio versionado.<br><br>**Scenario 2 — Rechazar cambio**<br>**Given** el comprador lo rechaza<br>**When** Nexa registra la decisión<br>**Then** el compromiso original permanece intacto.<br><br>**Scenario 3 — Cambio desactualizado**<br>**Given** el cambio ya no es actual<br>**When** el comprador responde<br>**Then** Nexa solicita la decisión actual y no cambia nada silenciosamente. |  |  |

#### MOB-US-042 — Seguir solicitudes y pedidos

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-042` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Seguir solicitudes y pedidos |  |  |
| **Description** | Como **Customer Buyer**, deseo seguir solicitudes y pedidos, para comprender el progreso comercial autorizado. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Historial autorizado**<br>**Given** existe una relación autorizada<br>**When** se revisa el progreso<br>**Then** el estado e historial de solicitud y pedido permanecen diferenciados.<br><br>**Scenario 2 — Progreso actual**<br>**Given** existe una relación autorizada<br>**When** el comprador revisa el progreso<br>**Then** el estado de Purchase Request y Sales Order permanece diferenciado.<br><br>**Scenario 3 — Acceso revocado**<br>**Given** se revoca el acceso<br>**When** se solicita el progreso<br>**Then** no se expone información privada.<br><br>**Scenario 4 — Progreso desactualizado**<br>**Given** el progreso mostrado está desactualizado<br>**When** el comprador hace actualización<br>**Then** Nexa expone el resultado actual o un estado no disponible veraz. |  |  |

#### MOB-US-043 — Revisar estado de crédito y pago

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-043` | Customer Buyer | Medium | `MOBILE-EPIC-06` — Conveniencia comercial y operativa futura |
| **Title** | Revisar estado de crédito y pago |  |  |
| **Description** | Como **Customer Buyer**, deseo revisar el estado del crédito y del pago, para comprender lo adeudado sin tratar la evidencia reportada como confirmación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Crédito actual**<br>**Given** existe una relación autorizada<br>**When** se revisa el crédito<br>**Then** importe, moneda, frescura y fuente quedan claros.<br><br>**Scenario 2 — Estado de pago**<br>**Given** existe evidencia de pago<br>**When** el comprador la revisa<br>**Then** los estados reported, confirmed y rejected permanecen diferenciados.<br><br>**Scenario 3 — Estado desactualizado**<br>**Given** el estado de pago está desactualizado<br>**When** el comprador hace actualización<br>**Then** Nexa expone el estado actual o un estado no disponible veraz. |  |  |

#### MOB-US-070 — Ver documentos de negocio vinculados a solicitud o pedido

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-070` | Customer Buyer or Sales Representative | Medium | `MOBILE-EPIC-11` — Seguimiento comercial y financiero |
| **Title** | Ver documentos de negocio vinculados a solicitud o pedido |  |  |
| **Description** | Como **Customer Buyer or Sales Representative**, deseo ver un documento de negocio vinculado a una solicitud o un pedido, para usar la evidencia autorizada del trabajo comercial. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Documento autorizado**<br>**Given** un documento emitido pertenece a la relación permitida<br>**When** la persona lo solicita<br>**Then** Nexa proporciona su identidad y contenido autorizado.<br><br>**Scenario 2 — Documento faltante**<br>**Given** no existe un documento emitido<br>**When** la persona lo solicita<br>**Then** Nexa indica que no está disponible y no cambia ningún compromiso.<br><br>**Scenario 3 — Acceso revocado**<br>**Given** se revoca el permiso<br>**When** la persona solicita el documento<br>**Then** Nexa no expone contenido privado. |  |  |

#### MOB-US-071 — Reportar evidencia de pago y ver el resultado de revisión

| Story ID | User | Priority | Epic |
| --- | --- | --- | --- |
| `MOB-US-071` | Customer Buyer | Medium | `MOBILE-EPIC-11` — Seguimiento comercial y financiero |
| **Title** | Reportar evidencia de pago y ver el resultado de revisión |  |  |
| **Description** | Como **Customer Buyer**, deseo reportar evidencia de pago y ver su resultado de revisión, para seguir un pago sin afirmar yo mismo su confirmación. |  |  |
| **Acceptance Criteria** | **Scenario 1 — Evidencia reportada**<br>**Given** están disponibles una referencia, importe y evidencia permitidos<br>**When** el comprador los reporta<br>**Then** Nexa registra el reporte como no confirmado.<br><br>**Scenario 2 — Evidencia revisada**<br>**Given** el proceso responsable revisa el reporte<br>**When** el comprador consulta el estado<br>**Then** Nexa muestra el resultado de revisión sin reescribir el reporte.<br><br>**Scenario 3 — Reporte duplicado**<br>**Given** se vuelve a enviar el mismo reporte<br>**When** Nexa lo recibe<br>**Then** no aplica la evidencia dos veces. |  |  |
