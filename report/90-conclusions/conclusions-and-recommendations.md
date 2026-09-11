# Conclusiones

Este cierre conecta el problema, los supuestos y las hipótesis con la
evidencia disponible. La conclusión es deliberadamente provisional: distingue
lo que la investigación ya permite sostener de lo que todavía requiere casos
directos, y no presenta el diseño ni la planificación como aceptación de
producto.

## Cierre del ciclo Lean UX hasta la evidencia disponible

| Elemento | Evidencia disponible | Conclusión actual | Estado |
| --- | --- | --- | --- |
| **Problem Statement** | Estadísticas de INEI, análisis competitivo y lenguaje de dominio describen una oportunidad de continuidad entre compromiso, preparación, despacho, entrega y recepción. | El problema es legítimo como objeto de investigación. Su magnitud en usuarios específicos de Nexa, su frecuencia y su impacto económico todavía no están cuantificados con investigación primaria. | **PARTIAL** |
| **Supuestos de negocio** | El contexto sectorial y la propuesta de valor tienen respaldo secundario; los artefactos Lean UX hacen explícitas las decisiones que deben contrastarse. | Existe una base razonable para investigar, pero monetización, adopción, disposición a cambiar y tamaño de la oportunidad no están validados. | **PARTIAL / OPEN** |
| **H1 — Warehouse & Dispatch Operations** | El diseño de entrevistas define casos de preparación, readiness y handoff, pero no hay entrevistas directas registradas para `Warehouse Operator` o `Dispatch Coordinator`. | No es posible confirmar ni rechazar que la pérdida de continuidad sea material ni que FA1 sea la respuesta adecuada. | **OPEN** |
| **H2 — Driver Delivery Execution** | El diseño de entrevistas define el `Delivery Attempt`, sus incidencias y su evidencia, pero no hay entrevistas directas registradas de `Driver` o `Delivery Operator`. | No es posible confirmar ni rechazar la hipótesis sobre atribución, recuperación y utilidad del recorrido Mobile. | **OPEN** |
| **H3 — B2B Buyers** | El registro del capítulo II conserva dos entrevistas Buyer (`INT-S3-01` e `INT-S3-02`) sobre visibilidad de llegada, continuidad del abastecimiento, confianza y soporte humano. Ninguna describe de principio a fin la recepción y verificación de cantidades. | La muestra aporta una señal exploratoria para investigar llegada, continuidad y soporte, pero no valida la recepción ni las discrepancias. Permanece por debajo de la cobertura requerida de 3–5 casos. | **PARTIAL / OPEN FOR VALIDATION** |

## Conclusiones generales

1. La evidencia secundaria y de dominio permite sostener el Problem Statement
   como una pregunta de ingeniería de software pertinente: la continuidad de
   información puede perderse cuando cambian la responsabilidad, el estado o
   la evidencia del pedido. Aún no permite atribuir una magnitud concreta a
   usuarios de Nexa.
2. La evidencia primaria no tiene la misma cobertura por segmento. Las dos
   entrevistas Buyer sugieren que la visibilidad de llegada, la continuidad del
   abastecimiento y el soporte humano merecen investigación adicional; H1 y H2
   siguen sin una base directa para decidir mantener, ajustar o descartar sus
   supuestos.
3. El resultado declarado por un Driver y la recepción declarada por un Buyer
   son hechos distintos. Mantener esa separación evita que una entrega marcada
   como realizada se convierta automáticamente en aceptación, y conserva la
   responsabilidad y la evidencia de cada actor.
4. DDD estratégico, C4 y los modelos tácticos aportan una forma coherente de
   asignar responsabilidades y diseñar contratos. Son evidencia de diseño
   TARGET; no prueban una aplicación implementada, un flujo ejecutado, una
   prueba en dispositivo ni aceptación de producto.
5. Los cuatro Sprint Planning traducen el alcance académico a una secuencia de
   trabajo trazable. Constituyen planificación y aprendizaje pendiente, no
   evidencia de que un Sprint, un build, una integración o un despliegue hayan
   concluido.
6. La siguiente evidencia debe actualizar los supuestos sin reescribir la
   historia: una contradicción puede ajustar o descartar una hipótesis, y una
   señal consistente puede justificar el experimento mínimo siguiente. La
   trazabilidad exige conservar el caso, el denominador, la fuente y la
   decisión tomada.

## Recomendaciones

- Completar entrevistas consentidas de Warehouse & Dispatch y Driver antes de
  caracterizar H1 o H2, y ampliar Buyer con casos de recepción, verificación y
  discrepancia.
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
