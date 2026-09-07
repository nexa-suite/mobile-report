# To-Be Scenario Mapping

Este mapa describe cómo las capacidades móviles proyectadas apoyan el trabajo
de Nexa. Las historias funcionales conservan la autoridad de negocio de los
Bounded Contexts responsables y no dependen de una plataforma concreta.

Nexa Operations Mobile reúne operaciones de negocio, ventas de campo, almacén,
despacho y entrega. Nexa Buyer Mobile atiende al Comprador con paridad de capacidad
de negocio respecto de las funciones aceptadas para la experiencia web, además
de capacidades móviles específicas. La paridad no implica copiar código,
interfaz ni defectos.

## Escenarios objetivo

| Escenario | Actores y producto | Contexto de trabajo | Comportamiento objetivo | Historias relacionadas |
| :--- | :--- | :--- | :--- | :--- |
| Acceso seguro y contexto de trabajo | Usuario móvil; Nexa Operations Mobile o Nexa Buyer Mobile | La persona necesita retomar una actividad dentro de la empresa y el ámbito autorizado. | Nexa confirma la sesión, resuelve Tenant/Workspace y muestra sólo capacidades permitidas. | MOB-US-001..003 |
| Recepción, identificación y preparación | Operador de Almacén; Nexa Operations Mobile | El trabajo físico requiere identificar producto, lote, cantidad y condición. | La persona consulta trabajo autorizado, registra hechos de recepción y preparación y conserva trazabilidad. | MOB-US-011..017, MOB-US-019 |
| Preparación de despacho y transferencia de responsabilidad | Coordinador de Despacho; Nexa Operations Mobile | Una entrega preparada debe salir del control del almacén con responsabilidad explícita. | El coordinador comprueba bienes, resuelve excepciones permitidas y registra la transferencia de responsabilidad hacia entrega. | MOB-US-020..025 |
| Ejecución de entrega y prueba | Conductor u Operador de Entrega; Nexa Operations Mobile | La entrega asignada requiere un intento, un resultado y evidencia revisable. | La persona consulta su trabajo, abre navegación externa autorizada y registra resultado, cantidades pendientes y Proof of Delivery. | MOB-US-026..034 |
| Recepción y discrepancia del comprador | Comprador; Nexa Buyer Mobile | El comprador necesita identificar la entrega correcta y registrar lo recibido. | Verifica el código de transferencia, confirma cantidades y reporta discrepancias sin borrar hechos previos. | MOB-US-044, MOB-US-047..049 |
| Adquisición pública y contacto | Visitante o representante de una empresa; Landing de Nexa | Una empresa necesita entender el valor B2B de cadena de frío y decidir si continúa. | La Landing explica capacidades, límites, precios e información legal y ofrece contacto o registro. | LAND-US-001..006 |

## Detalle de los recorridos

### Acceso y autorización

La persona vuelve a Nexa y solicita confirmar su identidad. El servidor resuelve
el contexto de Tenant/Workspace y las capacidades disponibles para la relación
de negocio. Si la sesión expiró, el contexto fue suspendido o la confirmación no
está disponible, Nexa informa que el trabajo no puede continuar y no expone
información protegida. El estado local no autoriza comandos.

### Operaciones físicas

El Operador de Almacén abre el trabajo permitido, identifica el Product/SKU y
consulta datos actuales de disponibilidad, lote y vencimiento. Registra recepción,
preparación, temperatura o discrepancia mediante las reglas del Bounded Context
responsable. FEFO, disponibilidad, condición y movimientos conservan sus hechos
separados; la identificación de un producto no crea por sí sola una recepción ni
un picking.

### Despacho y entrega

El Coordinador de Despacho revisa el trabajo preparado, comprueba los bienes y
registra la transferencia de responsabilidad con el Conductor u Operador de Entrega. La persona conductora
consulta la entrega asignada, abre indicaciones hacia el destino autorizado y
registra el intento, el resultado, las cantidades restantes y la prueba de entrega.
La navegación externa es una transferencia de destino; no representa seguimiento
continuo ni autoridad sobre el estado de la entrega.

### Recepción del comprador

El Comprador verifica la transferencia contra la entrega autorizada, confirma las
cantidades recibidas y registra la discrepancia cuando corresponde. La recepción
del comprador, el resultado del conductor, el Proof of Delivery, el pago y la
finalización de la entrega permanecen como hechos distintos.

### Trabajo comercial asistido

Un Representante de Ventas autorizado puede capturar un Direct Order asistido
cuando la política del Tenant es `DIRECT_ORDER`. El representante actúa dentro de
su propia relación y no suplanta al Comprador. Su borrador es distinto del borrador
del Comprador y el servidor revalida la autorización antes de confirmar cualquier
compromiso.

## Reglas transversales

| Regla | Aplicación en el escenario |
| :--- | :--- |
| Autoridad | El servidor y el Bounded Context responsable confirman y persisten los hechos de negocio. |
| Conectividad | El flujo es online-first. El almacenamiento local se limita a caché segura, borradores, evidencia temporal y metadatos de reintento. |
| Idempotencia | Un reintento con el mismo identificador devuelve un resultado único; no duplica recepción, picking, transferencia de responsabilidad, pago, entrega o recepción. |
| Integridad histórica | Las correcciones agregan evidencia correctiva o de reversión; no sustituyen silenciosamente un hecho anterior. |
| Ubicación | El alcance inicial abre navegación externa hacia un destino autorizado; no crea ubicación continua, ETA ni seguimiento en segundo plano. |
| Identidad | Tenant, Workspace, Human Identity, Workforce Membership, Customer Account y Buyer Relationship conservan significados distintos. |
