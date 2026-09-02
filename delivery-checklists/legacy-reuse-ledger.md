# Legacy evidence reuse ledger

## Alcance

La fuente histórica es el repositorio `nexa-ecosystem-report`, rama `main`,
SHA `e161fe522023bfe5929e76c4d7c66af211884b7e`. Corresponde a otro curso,
periodo, equipo y alcance. Se usa sólo para localizar artefactos que podrían
ser reutilizados con adaptación y verificación manual.

### Clasificaciones

| Clasificación | Significado |
| :--- | :--- |
| REUSE | Compatible y verificable sin alterar significado; requiere aprobación |
| ADAPT | Puede aportar evidencia o formato, pero exige nueva relación con el alcance móvil |
| HISTORICAL CONTEXT ONLY | Sirve para entender el antecedente; no satisface el gate actual |
| SUPERSEDED | Reemplazado por decisiones o catálogo vigente |
| REJECT | No debe incorporarse por conflicto, ausencia de fuente o riesgo de confusión |

## Entrevistas históricas

| Registro histórico | Fuente | Segmento original | Posible uso actual | Clasificación | Verificación requerida |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Lorena Vanesa Silva Leca, 42, Chorrillos | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S1 — Commercial Coordination | Contexto de captura comercial y movilidad de campo diferida en S1; no prueba tareas de almacén | ADAPT | Revisar identidad, consentimiento, fecha, video, captura, preguntas, enlace y compatibilidad móvil |
| Cinthia Paola Levano Asca, 39, Lurín | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S1 — Commercial Coordination | Contexto histórico únicamente hasta resolver la identidad de la captura | HISTORICAL CONTEXT ONLY | La captura revisada muestra el nombre “César Marín”, no el nombre del registro; resolver con la fuente original y aprobación humana antes de cualquier uso |
| Celia Pérez Huaman, 51, San Miguel | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S1 — Commercial Coordination | Contexto de trabajo en campo, lentitud y necesidad de continuidad móvil | ADAPT | El registro histórico no contiene enlace individual; confirmar fuente antes de usarlo |
| Hilda Litano Ramos, 47, Villa El Salvador | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S2 — Operations / Account Owner | Vocabulario histórico de importación, documentación y cadena de frío | HISTORICAL CONTEXT ONLY | No contar para el nuevo S2 Delivery Workforce sin nueva autorización y campaña |
| Edith Taype Peñaloza, 49, Callao | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S2 — Operations / Account Owner | Contexto histórico de punto de venta, temperatura y acceso a inventario | HISTORICAL CONTEXT ONLY | No contar para el nuevo S2; verificar sólo si se necesita vocabulario |
| Jesica Maria Sandoval Romero, 48, Jesús María | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S2 — Operations / Account Owner | Contexto histórico de FEFO, transcripción y coordinación con almacén | HISTORICAL CONTEXT ONLY | No contar para el nuevo S2; revisar procedencia y alcance |
| Pedro Puente Arnao, 56, San Isidro | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S3 — B2B Buyer Portal | Necesidad de previsibilidad logística y visibilidad de entrega | ADAPT | Sólo 2 registros históricos S3: no cubren la muestra actual de 3–5 |
| Henrry García Robles, 49, San Borja | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | S3 — B2B Buyer Portal | Contexto histórico únicamente hasta resolver la identidad de la captura | HISTORICAL CONTEXT ONLY | La captura revisada muestra el nombre “Piero García Campos”, no el nombre del registro; resolver con la fuente original y aprobación humana antes de cualquier uso |

Los enlaces individuales y el consolidado registrados en la fuente histórica no
se declaran reproducibles hasta comprobarlos manualmente. La existencia de una
imagen en `report/assets/images/chapter-2/interviews/` tampoco prueba que la
captura corresponda al video o que exista consentimiento.

## Artefactos históricos

| Artefacto | Fuente | Clasificación | Acción en el informe móvil |
| :--- | :--- | :--- | :--- |
| Segmentos, personas, task matrix, journeys y empathy maps | `report/10-chapter-1-introduction/1-3-target-segments.md`; `report/20-chapter-2-requirements-elicitation/2-3-needfinding.md` | ADAPT | Conservar sólo como formato o antecedente; validar S1/S3 y no reutilizar S2 como campaña nueva |
| Big Picture EventStorming y Ubiquitous Language | `report/20-chapter-2-requirements-elicitation/2-4-big-picture-event-storming.md`; `2-5-ubiquitous-language.md` | HISTORICAL CONTEXT ONLY | Rehacer o reconciliar con los 11 contextos vigentes y evidencia de workshop actual |
| User stories, Impact Mapping y Product Backlog | `report/30-chapter-3-requirements-specification/` | SUPERSEDED | Sustituir por 28 `MOB-US` V1 y sus technical/spike stories |
| DDD estratégico, C4, UML y base de datos | `report/40-chapter-4-product-design/4-6*` a `4-8*` | SUPERSEDED | No copiar contextos, nombres, clases, tablas o relaciones sin reconciliación con Blueprint |
| Sprint, pruebas, API, despliegue y colaboración | `report/50-chapter-5-implementation-validation-deployment/` | HISTORICAL CONTEXT ONLY | No prueba Mobile, dispositivo físico, distribución ni estado actual de productos |
| Videos y anexos históricos | `report/annexes/` y enlaces documentados | HISTORICAL CONTEXT ONLY | Revisar cada enlace, archivo, fecha y alcance; no incorporar claims por referencia |
| Assets visuales históricos | `report/assets/images/` | ADAPT / HISTORICAL CONTEXT ONLY | Copiar sólo un asset identificado, compatible y revisado; mantener procedencia y etiqueta histórica |

## Architecture reconciliation audit — 2026-09-02

The local historical repository was inspected at `main` /
`e161fe522023bfe5929e76c4d7c66af211884b7e` after refreshing its available
refs. The public [nexa-ecosystem-report repository](https://github.com/upc-pre-202610-1asi0730-12242-king/nexa-ecosystem-report)
also resolved `refs/heads/main` to that SHA on 2026-09-02. Its architecture is
evidence of a previous report only. The current Blueprint remains the
authority for the Mobile report.

| Historical source observed | Evidence found | Current disposition |
| :--- | :--- | :--- |
| `report/40-chapter-4-product-design/4-6-domain-driven-software-architecture.md` | Explicit seven-context model: Identity and Access Management, Tenant Management, Catalog Management, Sales, Warehouse, Logistics and Invoicing | SUPERSEDED; do not copy as the current 11-context model |
| `report/40-chapter-4-product-design/4-6*` through `4-8*` | Historical C4, tactical UML and relational/database projections using the prior vocabulary | SUPERSEDED; retain only provenance or a format idea after mapping to live Blueprint sources |
| `report/30-chapter-3-requirements-specification/` | Prior user-story, impact-map and backlog corpus | SUPERSEDED for the current Mobile projection; current counts are 73 Product Mobile stories and 28 V1 stories |
| `report/50-chapter-5-implementation-validation-deployment/5-2-4-sprint-4.md` | Historical Sprint 4 implementation record | HISTORICAL CONTEXT ONLY; current academic sprint model is S1 → TB1, S2 → AV2, S3 → TB2 |
| `report/20-chapter-2-requirements-elicitation/` and `report/annexes/` | Interviews, secondary research, competitor context, links and validation artefacts | ADAPT or HISTORICAL CONTEXT ONLY per record; every item needs identity, provenance, scope and human verification |
| `report/assets/images/` and historical UX sections | Screenshots, mockups, journeys and presentation format | ADAPT only when an individual asset is compatible and reviewed; never treat it as current Mobile runtime evidence |

The audit found reusable research leads and presentation formats, but no
wholesale transfer is authorized. The old context names, old story totals,
Sprint 4 records and old architecture diagrams remain classified rather than
silently reintroduced into the report.

## Checklist de verificación por entrevista

Antes de usar una entrevista como evidencia, una persona responsable debe
marcar cada control:

- [ ] Nombre y apellido coinciden con el registro y la captura autorizada.
- [ ] Edad, distrito, rol, segmento y curso de origen están respaldados.
- [ ] Fecha, inicio, fin y duración se leen del video o fuente original.
- [ ] El enlace individual y el consolidado abren el registro correcto.
- [ ] La captura corresponde a la sesión y no es una imagen genérica.
- [ ] Las preguntas realmente aplicadas son recuperables.
- [ ] El resumen separa observación, cita e interpretación.
- [ ] El contenido es relevante para una historia o necesidad móvil concreta.
- [ ] No se reutiliza una entrevista S2 histórica para el nuevo S2 sin decisión explícita.
- [ ] La persona responsable y el equipo aceptan la adaptación antes de publicar.

## Decisión del corte

Por las discrepancias de identidad detectadas, no se reutiliza todavía ninguna entrevista como evidencia de needfinding móvil
cerrado. Se prepara la trazabilidad para que la revisión humana sea
registro-por-registro y no una aprobación masiva por similitud temática.
