# 2.5 Strategic-Level Domain-Driven Design

Esta sección adapta las decisiones estratégicas de dominio y arquitectura de
Nexa para el alcance del curso de Aplicaciones Móviles. El dominio compartido
adoptado es la referencia de consistencia; las aplicaciones móviles son
superficies que proyectan ese dominio y no crean Bounded Contexts nuevos.

La propuesta mantiene separados el dominio aceptado, la evidencia de implementación existente y las decisiones futuras que todavía están en estado `PROPOSED`, `PLANNED` o `PENDING`.

## Reconciliación vigente

- El modelo aceptado contiene 11 Bounded Contexts. La propuesta anterior de 10
  contextos queda `SUPERSEDED`; Notifications y Business Traceability no se
  fusionan porque tienen autoridad y fallos distintos.
- Operations Mobile y Buyer Mobile son superficies/containers de una proyección
  de producto. No son Bounded Contexts, aunque tengan navegación, almacenamiento
  local o integraciones de dispositivo.
- Los hechos de Tenant, Workspace, identidad, compromiso, inventario,
  fulfillment, entrega, recepción, pago, documento, notificación y trazabilidad
  conservan su contexto propietario.

La procedencia, el impacto en el informe y las preguntas de revisión están en
[2.5.4 Strategic DDD Traceability](./2.5.4-strategic-ddd-traceability.md).

## Corte AV1 fuente-respaldado

El catálogo y sus límites se contrastaron con el Blueprint `origin/main`
`fce3ba6f8ca1622084a2114424086364e1f7d93f`. La evidencia visual externa de
DDD, su inspección, hashes y la ausencia explícita de `step8` están en
[2.5.1.0 DDD Process Evidence and Visual Mapping](./2.5.1-eventstorming/2.5.1.0-ddd-process-evidence.md).
Las fuentes C4 Structurizr, exports seleccionados y artefactos tácticos
copiados/renderizados tienen trazabilidad en el
[Chapter 2 provenance register](../../assets/chapter-2/provenance.md).

La evidencia de workshop, participantes, fecha/herramienta, aprobación humana,
runtime y Product Acceptance permanece `OPEN`; los artefactos no se presentan
como una sesión ejecutada ni como implementación terminada.
