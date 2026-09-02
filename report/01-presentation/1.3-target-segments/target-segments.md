# 1.3 Target Segments

## Segmentación móvil propuesta

Luego de explorar el dominio, los actores y los flujos candidatos en la sección
1.2, Nexa organiza su alcance móvil en tres segmentos objetivo propuestos. Esta
clasificación sirve para orientar la investigación y el diseño; el
`blueprint` todavía marca la validación de investigación como pendiente.

| ID | Segmento | Actores principales | Aplicación | Necesidad móvil a explorar |
| --- | --- | --- | --- | --- |
| **MOB-SEG-01** | **Field & Warehouse Operations** | Warehouse Operator y Dispatch Coordinator para el alcance V1; Sales Representative es un actor diferido V2+. Business Operations Manager es un actor secundario transversal. | Nexa Operations Mobile | Investigar identificación, recepción, lotes, FEFO, picking, temperatura, preparación y despacho. Las tareas de ventas en campo se mantienen fuera del flujo V1 hasta nueva validación. |
| **MOB-SEG-02** | **Delivery Workforce** | Driver / Delivery Operator. | Nexa Operations Mobile | Ejecutar entregas asignadas, registrar intentos, incidencias, prueba de entrega y handoff con conectividad variable. La ubicación se limita a la acción autorizada de navegación; no se afirma seguimiento continuo. |
| **MOB-SEG-03** | **B2B Buyers** | Customer Buyer autorizado por la relación con el proveedor. | Nexa Buyer Mobile | En V1, atender notificaciones relevantes, verificar el handoff, confirmar cantidades recibidas y registrar discrepancias. Catálogo, solicitudes, pagos y otros flujos permanecen sujetos a V2+ y validación. |

Company Owner y Tenant Administrator continúan siendo actores principalmente
Web-first para las decisiones de gobierno de la empresa y de acceso técnico.
Mobile proyecta capacidades del dominio compartido y no crea un nuevo Bounded
Context.

## Relación entre los segmentos

Los segmentos representan partes diferentes del mismo ciclo comercial y
operativo:

```mermaid
flowchart LR
    BUYER["MOB-SEG-03 — B2B Buyers<br/>Catálogo, pedido y seguimiento"]
    FIELD["MOB-SEG-01 — Field & Warehouse Operations<br/>Ventas, almacén y despacho"]
    DRIVER["MOB-SEG-02 — Delivery Workforce<br/>Entrega y evidencia acotada"]
    API["Nexa API y dominio compartido<br/>Estado autorizado y trazabilidad"]

    BUYER -->|Solicitud, pedido y consulta| API
    FIELD -->|Captura, preparación y despacho| API
    DRIVER -->|Intento, POD e incidencias| API
    API -->|Estados, documentos y notificaciones| BUYER
    API -->|Disponibilidad y trabajo operativo| FIELD
    API -->|Entrega asignada y contexto activo| DRIVER
```

La separación evita tratar Mobile como una sola experiencia genérica. El
personal de almacén y despacho necesita rapidez y contexto; los conductores
necesitan continuidad y evidencia durante el ciclo activo de entrega; y los
compradores necesitan claridad para verificar la recepción. Las tres
experiencias deben conservar una fuente de autoridad común sin sobrescribir
hechos distintos, como el resultado del conductor y la cantidad aceptada o
disputada por el comprador.

## Características demográficas y ocupacionales

| Segmento | Características demográficas y ocupacionales | Entorno de trabajo |
| --- | --- | --- |
| MOB-SEG-01 | Warehouse Operators y Dispatch Coordinators para V1; Sales Representatives se investigan como alcance diferido. Su nivel de decisión varía entre tareas operativas, coordinación y excepciones autorizadas. | Almacén, cámara de frío, staging, punto de despacho y, sólo para el alcance diferido, campo comercial. |
| MOB-SEG-02 | Conductores y operadores de entrega responsables de trasladar pedidos, coordinar intentos, registrar incidencias y obtener evidencia de recepción. | Vehículos de reparto, rutas urbanas y establecimientos compradores; la conectividad y seguridad se deben observar en contexto. |
| MOB-SEG-03 | Dueños de negocio, encargados de compras, administradores de local, responsables de reposición y compradores B2B autorizados. | Local comercial, almacén del comprador, oficina o celular utilizado para recepción y coordinación. |

La edad, ubicación, frecuencia de uso, accesibilidad, conectividad y experiencia
digital de cada segmento deberán completarse con investigación primaria. No se
crearán personas validadas a partir de supuestos.

## Sustento histórico del dominio

| Fuente histórica | Dato relevante | Uso responsable en este informe |
| --- | --- | --- |
| Lucky-Xplora (2022) | Alrededor del 83% de las bodegas del canal tradicional se ubicaba en un nivel principiante de madurez digital y cerca del 28% utilizaba alguna aplicación para gestionar tareas del negocio. | Justifica investigar experiencias de bajo esfuerzo para compradores B2B; no representa una medición actual de adopción de Buyer Mobile. |
| Bravo De la Cruz et al. (2025) | El estudio citado reporta 64 rupturas de cadena de frío en el periodo analizado: 14 por congelación y 50 por sobrecalentamiento. | Justifica investigar registro, trazabilidad y disposición de evidencia térmica; no prueba que todos los tenants tengan el mismo riesgo. |

El informe Web anterior ofrece evidencia útil para justificar por qué estos
segmentos merecen investigación, pero no prueba por sí solo las necesidades
móviles. Lucky-Xplora (2022) reporta una madurez digital principalmente
incipiente en el canal tradicional y un uso limitado de aplicaciones para
gestionar tareas del negocio. Esta evidencia respalda explorar experiencias de
bajo esfuerzo para compradores B2B, sin afirmar una tasa universal de adopción.

La evidencia sobre cadena de frío también justifica investigar al personal de
almacén, despacho y entrega. Bravo De la Cruz et al. (2025) documentan
incidentes recurrentes de desviación térmica en el contexto estudiado. Para
Nexa, esto se traduce en una hipótesis sobre registro manual, trazabilidad y
disposición de productos; no autoriza a afirmar que todos los segmentos sufren
el mismo nivel de riesgo ni que exista telemetría IoT implementada.

## Necesidades y valor esperado por segmento

| Segmento | Dolor a investigar | Valor esperado de Nexa | Indicadores iniciales |
| --- | --- | --- | --- |
| MOB-SEG-01 | Información dispersa entre pedido, disponibilidad, inventario, preparación y despacho. | Continuidad de trabajo, siguiente acción clara y menor doble digitación. | Tiempo de completar una tarea, aclaraciones requeridas y datos reconstruidos manualmente. |
| MOB-SEG-02 | Dependencia de comunicación informal, conectividad variable y pérdida de evidencias de entrega. | Trabajo recuperable, estados explícitos y POD asociado a la entrega correcta. | Tareas recuperadas tras desconexión, evidencias asociadas y diferencias entre intentos. |
| MOB-SEG-03 | Incertidumbre sobre la entrega, recepción y discrepancias; catálogo, pedidos y pagos quedan sujetos al alcance aprobado. | Autonomía acotada para verificar la entrega y comunicar diferencias con respaldo del proveedor. | Tareas completadas sin asistencia, consultas repetitivas y tiempo para encontrar información. |

Estos indicadores son candidatos para entrevistas y experimentos. No son
métricas de éxito definitivas hasta contar con una línea base y evidencia de
validación.

## Límites de la proyección móvil

- El almacenamiento local puede conservar caché, borradores seguros,
  evidencias temporales y metadatos de reintento, pero la API mantiene la
  autoridad del negocio.
- El acceso a cámara, escaneo y ubicación se limita al contexto autorizado de
  la tarea; no se propone seguimiento permanente del personal ni ETA en vivo.
- El registro de temperatura es manual en la propuesta inicial. La medición
  automática mediante IoT queda fuera del alcance actual.
- Dispatch Handoff y POD son hechos diferentes. Las cantidades ofrecidas por
  el conductor y las aceptadas o disputadas por el comprador deben conservarse
  como historias separadas.
- Buyer Portal Web permanece como superficie independiente; Buyer Mobile es una
  proyección para los flujos V1 explícitos, no una sustitución total del portal.

## Mapeo del alcance V1

| Segmento | Historias V1 principales | Alcance no demostrado en este corte |
| :--- | :--- | :--- |
| MOB-SEG-01 | `MOB-US-001..003`, `MOB-US-011..017`, `MOB-US-019` | Venta en campo, inventario automático, IoT y cualquier flujo no incluido en la proyección |
| MOB-SEG-02 | `MOB-US-020..034` | Seguimiento permanente, GPS histórico, ETA en vivo y autoridad offline no forman parte de V1 |
| MOB-SEG-03 | `MOB-US-044`, `MOB-US-047..049` | Catálogo completo, solicitudes comerciales, pagos y documentos como paridad móvil |

La tabla organiza el backlog académico; no demuestra que las historias estén
implementadas o aceptadas.
