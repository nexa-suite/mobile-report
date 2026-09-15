# Conclusiones

Este cierre conecta el problema, los supuestos y las hipótesis con la
evidencia disponible. La conclusión es deliberadamente provisional: distingue
lo que la investigación ya permite sostener de lo que todavía requiere casos
directos, y no presenta el diseño ni la planificación como aceptación de
producto.

## Cierre del ciclo Lean UX hasta la evidencia disponible

| Elemento | Evidencia disponible | Conclusión actual | Estado |
| --- | --- | --- | --- |
| **Problem Statement** | Estadísticas de INEI, análisis competitivo y lenguaje de dominio describen una oportunidad de continuidad entre compromiso, preparación, despacho, entrega y recepción. | El problema es legítimo como objeto de investigación. Su magnitud en usuarios específicos de Nexa, su frecuencia y su impacto económico todavía no están cuantificados con investigación primaria. | **PARCIAL** |
| **Supuestos de negocio** | El contexto sectorial y la propuesta de valor tienen respaldo secundario; los artefactos Lean UX hacen explícitas las decisiones que deben contrastarse. | Existe una base razonable para investigar, pero monetización, adopción, disposición a cambiar y tamaño de la oportunidad no están validados. | **PARCIAL / PENDIENTE** |
| **H1 — Warehouse & Dispatch Operations** | Las entrevistas `INT-S1-01`, `INT-S1-02` e `INT-S1-03` cubren preparación, verificación, readiness y handoff en una muestra 3/3 del segmento. | La evidencia de investigación respalda y refina el problema de continuidad y la necesidad de FA1; no valida la solución y queda abierta a Solution Validation. | **EVIDENCE INFORMED / OPEN FOR SOLUTION VALIDATION** |
| **H2 — Driver Delivery Execution** | Las entrevistas `INT-S2-01`, `INT-S2-02` e `INT-S2-03` cubren entrega, incidencias, comunicación y evidencia en una muestra 3/3 del segmento. | La evidencia de investigación respalda y refina la necesidad de continuidad y atribución durante la entrega; no valida la solución y queda abierta a Solution Validation. | **EVIDENCE INFORMED / OPEN FOR SOLUTION VALIDATION** |
| **H3 — B2B Buyers** | Las entrevistas `INT-S3-01`, `INT-S3-02` e `INT-S3-03` cubren reabastecimiento, continuidad, puntualidad, coordinación con proveedores y disponibilidad para clientes propios; la recepción y discrepancia se describen con mayor detalle en `INT-S3-03`. | La evidencia de investigación amplía Buyer más allá del recibo y respalda continuidad comercial; receipt/discrepancy sigue siendo válido, pero la solución no está validada y queda abierta a Solution Validation. | **EVIDENCE INFORMED / OPEN FOR SOLUTION VALIDATION** |

## Conclusiones generales

1. La evidencia secundaria y de dominio permite sostener el Problem Statement
   como una pregunta de ingeniería de software pertinente: la continuidad de
   información puede perderse cuando cambian la responsabilidad, el estado o
   la evidencia del pedido. Aún no permite atribuir una magnitud concreta a
   usuarios de Nexa.
2. La evidencia primaria cubre los tres segmentos con una muestra 3/3/3. H1 y
   H2 quedan informadas por preparación, continuidad, entrega e incidencias;
   Buyer incluye reabastecimiento, coordinación, puntualidad, disponibilidad
   para clientes propios y, con mayor detalle en un caso, recepción y
   discrepancia. Esta evidencia orienta la Solution Validation, no la sustituye.
3. El resultado declarado por un Driver y la recepción declarada por un Buyer
   son hechos distintos. Mantener esa separación evita que una entrega marcada
   como realizada se convierta automáticamente en aceptación, y conserva la
   responsabilidad y la evidencia de cada actor.
4. DDD estratégico, C4 y los modelos tácticos aportan una forma coherente de
   asignar responsabilidades y diseñar contratos. Son evidencia de diseño
   propuesto; no prueban una aplicación implementada, un flujo ejecutado, una
   prueba en dispositivo ni aceptación de producto.
5. El Product Backlog y los cuatro Sprint Backlogs traducen el alcance
   académico a una secuencia de trabajo trazable, con estimaciones, tareas y
   subtareas. Constituyen planificación y aprendizaje pendiente, no evidencia
   de que un Sprint, un build, una integración o un despliegue hayan concluido.
6. La siguiente evidencia debe actualizar los supuestos sin reescribir la
   historia: una contradicción puede ajustar o descartar una hipótesis, y una
   señal consistente puede justificar el experimento mínimo siguiente. La
   trazabilidad exige conservar el caso, el denominador, la fuente y la
   decisión tomada.
7. Los Personas, Journey Maps y Empathy Maps del informe fueron elaborados en
   UXPressia y exportados para su incorporación; esa procedencia no acredita
   resultados de validación. El Product Backlog y la trazabilidad de Sprint se
   referencian mediante Jira; los videos de exposición no están disponibles y
   no se atribuyen resultados de esos medios.

## Recomendaciones

- Diseñar y ejecutar una ronda de Solution Validation para H1, H2 y H3, usando
  la evidencia 3/3/3 como base y manteniendo separados Needfinding y aceptación
  de solución.
- Ejecutar primero el descubrimiento mínimo de Lean UX: reconstruir un caso
  As-Is reciente, registrar fuentes, aclaraciones, tiempo, omisiones,
  asistencia y ambigüedad del handoff; sólo si el problema es material pasar a
  una representación de bajo costo y comparar contra la línea base.
- Mantener separados `Driver Outcome`, `Buyer Receipt`, `Proof of Delivery` y
  `Discrepancy` en requisitos, diseño, evidencia y futuras implementaciones.
- Registrar por separado cualquier prototipo, build, prueba de dispositivo,
  despliegue o resultado de usabilidad cuando exista su fuente verificable; no
  inferirlo desde el backlog, C4 o el PDF.
- Revisar supuestos de adopción y monetización con evidencia directa antes de
  convertirlos en decisiones de producto o de alcance.
