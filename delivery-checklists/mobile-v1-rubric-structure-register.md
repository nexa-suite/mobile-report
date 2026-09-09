# Mobile V1: registro de estructura de User Stories

## Contrato de la plantilla

El cuadro de la rúbrica se aplica sin cambiar el contenido del backlog. Cada
historia detallada V1 debe presentar, en este orden, los siete campos:

`Story ID` → `User` → `Priority` → `Epic ID` → `Title` → `Description` →
`Acceptance Criteria`.

La descripción y los criterios permanecen en la historia fuente
[2.4.1 User Stories](../report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories/2.4.1-user-stories.md).
Cada criterio contiene exactamente cuatro bloques `Scenario / Given / When /
Then`. Este registro demuestra estructura y no sustituye la revisión del
contenido, la decisión de Product Acceptance ni la defensa individual.

## Verificación reproducible

El validador ejecutable es
[`verify-mobile-v1-rubric-template.py`](../scripts/verify-mobile-v1-rubric-template.py).
El gate general lo ejecuta desde
[`verify-report-structure.sh`](../scripts/verify-report-structure.sh). La
salida esperada es `records=28; fields=7; scenarios=112`.

## Registro de historias detalladas

| Story ID | Campos en orden | Escenarios | Estado estructural |
| :--- | :--- | ---: | :--- |
| MOB-US-001 | 7 | 4 | PASS |
| MOB-US-002 | 7 | 4 | PASS |
| MOB-US-003 | 7 | 4 | PASS |
| MOB-US-011 | 7 | 4 | PASS |
| MOB-US-012 | 7 | 4 | PASS |
| MOB-US-013 | 7 | 4 | PASS |
| MOB-US-014 | 7 | 4 | PASS |
| MOB-US-015 | 7 | 4 | PASS |
| MOB-US-016 | 7 | 4 | PASS |
| MOB-US-017 | 7 | 4 | PASS |
| MOB-US-019 | 7 | 4 | PASS |
| MOB-US-020 | 7 | 4 | PASS |
| MOB-US-021 | 7 | 4 | PASS |
| MOB-US-022 | 7 | 4 | PASS |
| MOB-US-023 | 7 | 4 | PASS |
| MOB-US-024 | 7 | 4 | PASS |
| MOB-US-025 | 7 | 4 | PASS |
| MOB-US-026 | 7 | 4 | PASS |
| MOB-US-027 | 7 | 4 | PASS |
| MOB-US-028 | 7 | 4 | PASS |
| MOB-US-031 | 7 | 4 | PASS |
| MOB-US-032 | 7 | 4 | PASS |
| MOB-US-033 | 7 | 4 | PASS |
| MOB-US-034 | 7 | 4 | PASS |
| MOB-US-044 | 7 | 4 | PASS |
| MOB-US-047 | 7 | 4 | PASS |
| MOB-US-048 | 7 | 4 | PASS |
| MOB-US-049 | 7 | 4 | PASS |

`PASS` significa que la forma se encuentra en la fuente y que el validador
reproducible la volvió a contar en este corte. No significa que la historia
esté implementada, aceptada por Product o validada en runtime.
