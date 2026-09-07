# Annex D: Spike Stories

## Alcance y evidencia

Las siguientes Spike Stories registran incertidumbres de investigación o
decisión técnica que pueden afectar la proyección Mobile. No son User Stories,
no entregan funcionalidad de producción y no crean Bounded Contexts. Todos los
spikes permanecen OPEN hasta que se produzca la evidencia indicada y exista la
aceptación del responsable correspondiente.

Fuente compartida: blueprint/01-shared/product/requirements/spike-stories.md.
Reconciliación Mobile: blueprint/03-mobile/requirements/mobile-spike-reconciliation.md.
Los resultados aún no realizados no se redactan como decisiones cerradas.

## Spike Story index

| ID | Research question | Alternatives | Completion criteria | Expected artifact | Owner | Milestone | State |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| SPIKE-001 | ¿Qué feature de autonomous learning es pertinente y seguro para el curso? | Asistencia basada en reglas; modelo local/on-device; servicio externo; deferir si no hay ajuste seguro. | Comparar relevancia, privacidad, factibilidad y demostrabilidad; recomendar o documentar insuficiencia. | Matriz de candidatos, fuentes, límites de datos y recomendación. | Academic/Product owner | AV2 | OPEN |
| SPIKE-002 | ¿Cómo distribuir Native Android/Kotlin y una opción cross-platform entre Operations Mobile y Buyer Mobile? | Native Android/Kotlin; Flutter/Dart; Kotlin Multiplatform; asignación mixta. | Comparar workflow, seguridad, device, estado local, coste y restricción académica; mantener decisión explícita. | Matriz de decisión y PoC o insuficiencia documentada. | Technical/Product owner | TB1 | OPEN |
| SPIKE-003 | ¿Qué identificadores Barcode/QR/GS1 y fallback manual son seguros? | Cámara/scanner; librería externa; entrada manual; deferir formatos no soportados. | Definir alcance de identificadores, permisos, ambigüedad, TTL/replay y validación server-side. | Pack de evidencia de escaneo, comparación de formatos y recomendación. | Mobile technical owner | TB1 | OPEN / PARTIAL contract evidence |
| SPIKE-004 | ¿Qué datos pueden permanecer locales y cómo se recuperan fallos o conflictos? | Online-only; caché segura; borrador local; cola idempotente para evidencia seleccionada. | Clasificar datos, definir retry/conflict/encryption y excluir éxito autoritativo offline o sync genérico. | Matriz de datos, escenarios de recuperación y secuencia de sincronización. | Architecture/Mobile owner | TB1 | OPEN / target boundary defined |
| SPIKE-005 | ¿Qué eventos requieren push y cómo se protegen deep links expirados o stale? | Push provider-neutral; email fallback; in-app refresh; no push para baja criticidad. | Definir eventos, canales, permisos, tenant scope, expiración, retry y ownership de source state. | Matriz evento-canal, threat cases y recomendación de proveedor/configuración. | Notifications/Mobile owner | TB2 | OPEN / PARTIAL API foundation |
| SPIKE-006 | ¿Qué capacidad mínima de mapas/ubicación aporta valor sin tracking permanente? | Navegación externa; ubicación sólo en Delivery activo; ubicación manual; deferir live location. | Evaluar privacy, batería, conectividad, consentimiento y fallback; excluir tracking permanente. | Pack de ubicación, observaciones device/provider y recomendación. | Product/privacy/Architecture owner | TB2 | OPEN |

## Spike Story details

### SPIKE-001 — Select the autonomous-learning feature and external technology

- **Question:** Which learning feature and external technology satisfy the
  course while remaining useful to Nexa?
- **Objective:** Compare product relevance, data/privacy constraints, course
  outcome and feasibility.
- **Alternatives:** Rule-based assistance, local/on-device model, external
  service or defer if no safe fit.
- **Expected evidence:** Candidate matrix, sources, privacy/data boundary and a
  feasibility PoC or explicit insufficiency.
- **Completion criteria:** One recommendation or evidence-backed open decision;
  no production feature claim.
- **Expected artifact:** Evidence pack and recommendation.
- **Owner:** Academic/Product owner.
- **Milestone:** AV2.
- **State:** OPEN; no research result asserted.

### SPIKE-002 — Evaluate Native versus cross-platform distribution

- **Question:** How should Native Android/Kotlin, Flutter/Dart and/or Kotlin
  Multiplatform be distributed across Operations Mobile and Buyer Mobile?
- **Objective:** Evaluate workflow/device fit, security, selective local state,
  shared integration and delivery cost.
- **Alternatives:** Native Android/Kotlin, Flutter/Dart, Kotlin Multiplatform or
  mixed allocation.
- **Expected evidence:** Decision matrix, constrained build/PoC, app-to-framework
  mapping and course constraints.
- **Completion criteria:** Trade-offs and risks are recorded, and Owner/course
  acceptance exists before closing the decision.
- **Expected artifact:** Framework/app allocation recommendation.
- **Owner:** Technical/Product owner.
- **Milestone:** TB1.
- **State:** OPEN; no framework selected.

### SPIKE-003 — Evaluate Barcode, QR and GS1 scanning

- **Question:** Which physical identifiers should Mobile scan, under which
  permission, ambiguity, offline and server-validation constraints?
- **Objective:** Investigate camera capability, formats, reliability, manual
  fallback, QR TTL/replay and future GS1 boundary.
- **Alternatives:** Camera scanner, external scanning library, manual identifier
  entry or defer unsupported formats.
- **Expected evidence:** Standards/technology comparison, representative scan
  result, fallback and security notes.
- **Completion criteria:** Identifier scope, validation boundary and unresolved
  questions are explicit; no Scanner Bounded Context is created.
- **Expected artifact:** Scan evidence pack and recommendation.
- **Owner:** Mobile technical owner.
- **Milestone:** TB1.
- **State:** OPEN; API compatibility is partial evidence, device research pending.

### SPIKE-004 — Evaluate Mobile local storage and selective recovery

- **Question:** What Mobile data can be local and how should retry, conflict,
  encryption and stale state behave?
- **Objective:** Define safe cache/draft/evidence staging without fake
  authoritative success.
- **Alternatives:** Online-only, secure cache, local draft or idempotent queue for
  selected evidence.
- **Expected evidence:** Data classification, conflict/retry scenarios,
  synchronization sequence and feasibility evidence.
- **Completion criteria:** Safe offline boundary and connectivity-required
  workflows are explicit; no generic offline sync is claimed.
- **Expected artifact:** Storage/synchronization recommendation.
- **Owner:** Architecture/Mobile owner.
- **Milestone:** TB1.
- **State:** OPEN; target boundary defined, implementation absent.

### SPIKE-005 — Evaluate Push Notifications and deep links

- **Question:** Which business events merit Mobile push and how should
  authenticated, tenant-scoped deep links recover?
- **Objective:** Evaluate channel policy, permission lifecycle, retry, routing,
  privacy and source-state ownership.
- **Alternatives:** Provider-neutral push, email fallback, in-app refresh or no
  push for low-criticality facts.
- **Expected evidence:** Event-to-notification matrix, deep-link threat cases,
  provider options and delivery/recovery evidence.
- **Completion criteria:** Push classes, safety rules and provider decisions are
  documented; notifications never become source authority.
- **Expected artifact:** Notification/deep-link evidence pack.
- **Owner:** Notifications/Mobile owner.
- **Milestone:** TB2.
- **State:** OPEN; API subscription foundation is partial evidence.

### SPIKE-006 — Evaluate Maps, live location, privacy, battery and fallback

- **Question:** What map or active-Delivery location capability provides useful
  value with limited privacy, battery, connectivity and provider risk?
- **Objective:** Evaluate external navigation, active-only sharing, consent,
  retention, battery behavior and unavailable-map fallback.
- **Alternatives:** External navigation only, active-Delivery location, manual
  location or defer live location.
- **Expected evidence:** Privacy/threat notes, battery/connection observations,
  map options and fallback flow.
- **Completion criteria:** Minimum location boundary and exclusions are explicit;
  permanent tracking and live buyer maps remain excluded.
- **Expected artifact:** Location evidence pack and recommendation.
- **Owner:** Product/privacy/Architecture owner.
- **Milestone:** TB2.
- **State:** OPEN; V1 remains external navigation handoff only.

## Definition of Done for any Spike

A Spike closes only when its question, alternatives, evidence, completion
criteria, expected artifact, owner and milestone are recorded; the actual
artifact is linked; unresolved assumptions remain visible; and the responsible
Owner accepts the result. A source contract or planned story is not a Spike
result.
