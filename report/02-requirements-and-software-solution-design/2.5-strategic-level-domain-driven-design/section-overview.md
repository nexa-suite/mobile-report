# 2.5 Strategic-Level Domain-Driven Design

Esta sección adapta las decisiones estratégicas de dominio y arquitectura de Nexa para el alcance del curso de Aplicaciones Móviles. La referencia principal es el dominio compartido definido en `blueprint`; las aplicaciones móviles son superficies que proyectan ese dominio y no crean Bounded Contexts nuevos.

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
