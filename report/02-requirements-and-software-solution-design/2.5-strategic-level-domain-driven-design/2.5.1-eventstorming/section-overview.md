# 2.5.1 EventStorming

El equipo utilizó EventStorming colaborativo en Miro para pasar de hechos
observables del dominio a una lectura estratégica de responsabilidades. La
secuencia conserva la división académica:

- 2.3.5 presenta Big Picture EventStorming con Step 1 — Unstructured
  Exploration, Step 2 — Timelines y Step 3 — Pain Points.
- Esta sección continúa con Step 4 — Pivotal Points, Step 5 — Commands, Step 6
  — Policies, Step 7 — Read Models, Step 9 — Aggregates y Step 10 — Bounded
  Contexts.

La secuencia colaborativa continuó de Step 7 a Step 9; el taller de Miro no
definió una etapa Step 8. Se preserva la numeración real y no se reconstruye
una etapa inexistente.

## Lectura estratégica del modelado

Las capturas muestran cómo cada capa agrega una pregunta distinta:

| Etapa | Pregunta que responde | Resultado estratégico |
| :--- | :--- | :--- |
| Step 4 — Pivotal Points | ¿Dónde cambia autoridad, responsabilidad o consistencia? | Se aíslan decisiones comerciales, protección física, entrega, pago y corrección. |
| Step 5 — Commands | ¿Qué intención de un actor solicita una decisión? | Se separan actor, intención, comando, decisión autoritativa y hecho resultante. |
| Step 6 — Policies | ¿Qué reacción de negocio sigue a un hecho? | Se distinguen invariantes síncronas de propagación posterior a hechos confirmados. |
| Step 7 — Read Models | ¿Qué información necesita cada actor para decidir? | Se separan proyecciones de lectura de la autoridad de los contextos fuente. |
| Step 9 — Aggregates | ¿Qué debe ser consistente dentro de un modelo? | Se ubican límites de consistencia internos sin confundirlos con Bounded Contexts. |
| Step 10 — Bounded Contexts | ¿Qué lenguaje, reglas y autoridad deben permanecer juntos? | Se consolidan los once límites estratégicos aceptados por Nexa. |

Los nombres de los eventos y comandos se mantienen como lenguaje de dominio.
No representan automáticamente endpoints, clases Java, tablas ni eventos
publicados. Las relaciones, contratos y consistencia se desarrollan en las
secciones siguientes.
