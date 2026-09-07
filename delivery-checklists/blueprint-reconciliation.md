# Reconciliación con Blueprint

## Fuentes de autoridad

La reconciliación usa el corte `blueprint/main`
(`fce3ba6f8ca1622084a2114424086364e1f7d93f`) y mantiene separadas las
decisiones de producto, la implementación observada y la evidencia académica.

| Fuente | Función |
| :--- | :--- |
| `01-shared/engineering/governance/source-of-truth.md` | Precedencia y separación AS-IS/TARGET |
| `01-shared/product/current-decisions.md` | Decisiones de producto aceptadas |
| `03-mobile/requirements/mobile-v1-catalog.md` | Catálogo maestro de 73 historias móviles |
| `90-academic/mobile/course-1acc0238/requirements-projection.md` | Proyección de las 28 historias V1 para el curso |
| `90-academic/mobile/course-1acc0238/rubric-compliance.md` | Registro de cobertura de la rúbrica |
| `90-academic/mobile/course-1acc0238/validation-evidence-plan.md` | Contrato de validación y gates pendientes |

## Decisiones incorporadas

- El curso trabaja con una proyección académica de **28 historias V1**. El
  catálogo de producto conserva **73 historias** distribuidas entre V1, V2,
  V3 y V4/Future; el informe no debe presentar el roadmap completo como V1.
- La solución móvil se documenta como dos superficies proyectadas: una para
  operaciones y otra para compradores. Mobile no se trata como un Bounded
  Contexto adicional.
- La operación móvil es online-first. El almacenamiento local se limita a
  lecturas seguras, borradores, evidencias y reintentos controlados; no se
  atribuye autoridad de negocio al dispositivo.
- Android nativo con Kotlin es la restricción vigente. La decisión
  cross-platform permanece abierta y debe sustentarse mediante el spike
  correspondiente.
- La API `v0.17.0` se considera evidencia candidata del backend; no prueba por
  sí misma el runtime móvil ni el cumplimiento completo de la rúbrica.
- El modelo estratégico conserva exactamente once Bounded Contexts; no se
  deducen desde pantallas, repositorios, paquetes, tablas o dispositivos.

## Bounded Contexts aceptados

| Código | Bounded Context |
| :--- | :--- |
| BC-01 | Tenant & Access Governance |
| BC-02 | Customer & Buyer Relationships |
| BC-03 | Catalog & Commercial Policy |
| BC-04 | Sales Commitment |
| BC-05 | Inventory Availability |
| BC-06 | Fulfillment & Delivery |
| BC-07 | Credit & Receivables |
| BC-08 | Payments |
| BC-09 | Business Documents |
| BC-10 | Notifications |
| BC-11 | Business Traceability |

## Historias V1 proyectadas

| Segmento | Sprint proyectado | IDs |
| :--- | :--- | :--- |
| S1 — Field & Warehouse Operations | S1 | `MOB-US-001`, `002`, `003`, `011`, `012`, `013`, `014`, `015`, `016`, `017`, `019` |
| S2 — Delivery Workforce | S2 | `MOB-US-020`, `021`, `022`, `023`, `024`, `025`, `026`, `027`, `028`, `031`, `032`, `033`, `034` |
| S3 — B2B Buyers | S3 | `MOB-US-044`, `047`, `048`, `049` |

La numeración completa y los criterios Gherkin se mantienen en la fuente de
proyección y se integran al documento de requisitos sin renombrar las historias
históricas. Cada historia necesita además una verificación de alcance,
ownership y fuente antes del cierre académico.

## Diferencias abiertas

| Tema | Estado | Tratamiento |
| :--- | :--- | :--- |
| Entrevistas S1/S3 históricas | Reutilización condicionada | Conservar etiquetas originales y verificar compatibilidad, fecha, segmento y evidencia individual |
| Entrevistas S2 de operaciones físicas | No cubiertas por defecto | Preparar campaña nueva para recepción, lotes, FEFO, picking, despacho, entrega y prueba de recepción |
| User stories del branch histórico | Superseded for V1 | Sustituir el baseline anterior de 49 historias por la proyección vigente de 28 |
| C4 y DDD táctico | Fuentes y exports versionados observados en Blueprint | Registrar selección, legibilidad, ownership y revisión humana; no confundir TARGET con implementación |
| Bibliografía reciente Q1/Q2 | Pendiente | Verificar cuatro fuentes, dos de dominio y dos de tecnología móvil, con cuartil y antigüedad |
| Validación en dispositivo físico | Pendiente | Requiere instalación, ejecución, captura y defensa por el equipo |

## Regla de publicación

El reporte puede explicar una decisión aceptada y enlazar su fuente, pero debe
rotular como `TARGET`, `RUNWAY`, `OPEN` o `PENDING HUMAN EVIDENCE` todo lo que no
esté comprobado en el corte de la implementación correspondiente.
