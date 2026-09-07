# 2.5.1 EventStorming

El EventStorming permite ordenar los eventos relevantes del dominio antes de
decidir sus límites. La sesión debe producir evidencia separable de las
hipótesis del equipo y alinearse con los 11 Bounded Contexts adoptados.

## Protocolo de sesión que debe evidenciarse

| Etapa | Resultado esperado | Evidencia requerida | Estado |
| :--- | :--- | :--- | :--- |
| Big Picture EventStorming | Timeline de eventos, comandos, actores, políticas y excepciones | Capturas progresivas, herramienta, fecha, duración y participantes | `WORKSHOP_PENDING` |
| Candidate Context Discovery | Agrupación y separación de candidatos mediante una técnica explícita | Capturas antes/después y explicación `start-with-value`, `start-with-simple` o `look-for-pivotal-events` | `WORKSHOP_PENDING` |
| Domain Storytelling | Flujos priorizados y mensajes entre autoridades | Diagramas por escenario, leyenda, fuente y revisión del equipo | `WORKSHOP_PENDING` |
| Bounded Context Canvases | Propósito, lenguaje, reglas, capacidades, dependencias y crítica | Canvas por contexto, versión, participantes y decisión | `WORKSHOP_PENDING` |

La rúbrica recomienda una sesión de EventStorming de 1–2 horas y una sesión de
Candidate Context Discovery de hasta 2 horas. Es una restricción de
organización del trabajo, no evidencia de que las sesiones ya ocurrieron.

## Límite de evidencia

El registro visual de `nexa-ddd` está disponible en
[2.5.1.0 DDD Process Evidence and Visual Mapping](./2.5.1.0-ddd-process-evidence.md).
Incluye nueve SVG inspeccionados, PNG de lectura en el informe y hashes de las
fuentes. El conjunto no contiene `step8`.

Estas imágenes son material externo de diseño; no documentan por sí solas
participantes, facilitador, fecha/herramienta, consenso o aceptación. La sesión
colaborativa, sus capturas fuente y la crítica formal permanecen
`WORKSHOP_PENDING`. La procedencia completa está en el
[registro de Chapter 2](../../../assets/chapter-2/provenance.md).
