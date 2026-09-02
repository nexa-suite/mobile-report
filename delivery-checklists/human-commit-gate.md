# Human Commit Gate

## Estado del corte

| Campo | Valor |
| :--- | :--- |
| Estado | `CURRENT REVIEWED INTEGRATION AUTHORIZED — COMMIT SEQUENCE OPEN` |
| Rama | `feature/report-front-matter-and-governance` |
| Base revisada | `3edeb196800a72a30299987a661e791c8f8fb50d` |
| Upstream | No configurado |
| Staging | Vacío antes del primer commit; staging controlado por unidad |
| Commits nuevos | Ninguno |
| Report integration review | `28/28` approved by `DiegoS284` + `JoaquinBV511` on `2026-09-02` |
| Individual defense review | Follow-up; not required to block current report integration |
| Identidad de owners | Owner-confirmed handoff `5/5`; current reviewed-unit attribution limited to Joaquín/Diego |

Este gate protege la trazabilidad del informe. La aprobación actual autoriza
integrar el diff revisado por Diego y Joaquín, sujeto a staging exacto,
validación y separación por unidad. No convierte una fuente, una proyección o
una prueba local en implementación, aceptación de producto o preparación para
producción.

## Condiciones obligatorias antes de cada commit

La persona responsable debe confirmar explícitamente, para ese commit:

1. Nombre legal y username actuales, tomados del registro owner-confirmed.
2. Email del proyecto tomado como `OWNER-CONFIRMED PROJECT COMMIT EMAIL`; no
   presentarlo como GitHub-verified sin evidencia separada.
3. Rama exacta, archivos incluidos y resumen de una sola unidad lógica.
4. Fuente o requisito que justifica el cambio.
5. Qué debe poder explicar el owner durante la revisión.
6. Validación ejecutada, con resultado real y reproducible.
7. Mensaje Conventional Commit en inglés, con scope canónico.

No se usan trailers de coautoría, identidades inferidas, fechas inventadas ni
commits artificiales. Un commit debe contener una unidad revisable y no se
crea sólo para aumentar el historial.

## Plantilla de autorización

| Campo | Confirmación humana |
| :--- | :--- |
| Owner legal | Joaquín / Diego, según unidad |
| GitHub username | `JoaquinBV511` / `DiegoS284`, según unidad |
| Email asociado confirmado por owner | `joaquinverdebueno@gmail.com` / `diego64g284@gmail.com` |
| Rama | `feature/report-front-matter-and-governance` |
| Archivos | Exactos por unidad, registrados en [current-diff-ownership-matrix.md](./current-diff-ownership-matrix.md) |
| Resumen | Revisado conjuntamente; separación natural por alcance |
| Fuente / requisito | Prompt canónico, rúbrica, Blueprint y repositorios de evidencia fijados |
| Explicación del owner | Requerida antes de cada commit; no se atribuye trabajo actual a Gino, Gerard o Sebastián |
| Validación ejecutada | `bash scripts/verify-report-structure.sh` (incluye huellas SHA-256 del prompt y rúbrica canónicos, ownership matrix y citas bibliográficas); `python3 scripts/verify-diff-ownership-matrix.py` → `147` paths, `9` units; `python3 scripts/verify-bibliography-citations.py` → mandatory `4/4`, DOI `4/4`, technical refs `6/6`, quartile `PRELIMINARY/PENDING`; `python3 scripts/verify-mobile-v1-transcription.py` → `28` rows, `28` titles, `112` scenarios; `python3 scripts/verify-mobile-v1-review-register.py` → `28` rows aligned; `python3 scripts/verify-mobile-v1-api-register.py` → `28` stories, `60` explicit operations, `60` response blocks, `24` request bodies, `60/60` path params, Sprint alignment `28/28`, `268` OpenAPI paths; `bash scripts/check-report-links.sh`; `bash scripts/inspect-api-persistence.sh`; `git diff --check`; Structurizr `2026.06.28 validate` exit `0`; API baseline Docker-backed `./mvnw test` 482/0/148 and latest no-Docker rerun 482/0/152; expanded local integration gate partial: 482 run, 3 failures, 0 errors, 0 skipped; canonical Sprint 1–3 and rubric-gap audit recorded |
| Mensaje Conventional Commit | Se define por unidad y se inspecciona en staging |
| Autorización explícita para `git add` y `git commit` | `YES — current reviewed Diego/Joaquín units` |

## Unidades de commit propuestas

Estas unidades son una propuesta para facilitar el diff review; no son
autorización ni deben ejecutarse sin owner, identidad y confirmación explícita.
La separación evita mezclar requisitos, arquitectura, UX y gates técnicos.

| Unidad | Alcance a revisar | Owner propuesto | Reviewers | Mensaje candidato |
| :--- | :--- | :--- | :--- | :--- |
| A | README, front matter, rúbrica, baseline, colaboración y milestones | Joaquín / `JoaquinBV511` | Team review | `docs(rubric): reconcile academic report baseline` |
| B | Entrevistas, Needfinding, provenance y research gates | Joaquín / `JoaquinBV511` | Diego; team review | `docs(research): reconcile mobile needfinding evidence` |
| C | 28 User Stories, AC, Impact Mapping, Product Backlog y requirements registers | Joaquín / `JoaquinBV511` | Diego; team review | `docs(requirements): align mobile v1 academic backlog` |
| D | Strategic DDD, 11 BCs, Context Map, UL y discovery provenance | Joaquín / `JoaquinBV511` | Sebastián; Diego | `docs(ddd): reconcile strategic domain model` |
| E | C4, Structurizr, system boundaries, AS-IS/TARGET y architecture evidence | Diego / `DiegoS284` | Gino | `docs(architecture): synchronize canonical c4 evidence` |
| F | Tactical DDD, UML, PlantUML, database models y persistence evidence | Joaquín / `JoaquinBV511` + Diego / `DiegoS284`, split by path | Team review | `docs(ddd): reconcile tactical domain and data models` / `docs(implementation): document verified persistence evidence` |
| G | Mobile UX, i18n, accessibility, interaction states y Design Lab mapping | Joaquín / `JoaquinBV511` | Diego; team review | `docs(ux): prepare mobile experience evidence` |
| H | SCM, sprints, API/implementation evidence y validation structure | Split by actual scope | Team review | `docs(sprint): add reproducible sprint evidence gates` / `docs(implementation): document verified mobile api evidence` |
| I | Reproducible report and technical validation scripts | Joaquín + Diego, split by script scope | Team review | `chore(report): add reproducible report validation gates` / `chore(architecture): add technical evidence validation gates` |

Cada fila requiere inspección de archivos exactos antes de staging. La
aprobación conjunta del 2026-09-02 cubre la integración actual; no crea
historial de revisión individual de historias ni atribuye el diff actual a
teammates ausentes. Si una unidad no es explicable por un solo owner, se divide
por path. No se agrega `Co-authored-by` ni atribución de herramientas internas.

## Estado del mini-freeze

El mini-freeze global fue levantado por Diego y Joaquín el 2026-09-02 para la
integración revisada. Se mantiene freeze por unidad durante staging e
inspección: cualquier path inesperado, validación fallida, conflicto semántico
o identidad ambigua detiene la secuencia. La revisión individual de defensa de
historias permanece separada y no bloquea estos commits.

## Alcance manual de las historias

La revisión persona por persona usa
[mobile-v1-story-verification-register.md](./mobile-v1-story-verification-register.md).
Cada lead debe leer la historia completa, sus cuatro escenarios, el Bounded
Context, las dependencias y el límite entre evidencia propuesta, implementada
y aceptada. El registro sólo puede pasar a `APPROVED` por decisión humana con
fecha, revisor y fuente.

La auditoría completa frente al enunciado está en
[rubric-gap-matrix.md](./rubric-gap-matrix.md); la matriz de contratos API está
en [mobile-v1-api-contract-register.md](./mobile-v1-api-contract-register.md).
La evidencia de persistencia observada está en
[api-persistence-evidence-register.md](./api-persistence-evidence-register.md).
La procedencia y validación de diagramas está en
[architecture-render-evidence-register.md](./architecture-render-evidence-register.md).
La matriz exacta de paths y unidades está en
[current-diff-ownership-matrix.md](./current-diff-ownership-matrix.md).
La identidad de los cinco owners está en
[team-identity-register.md](./team-identity-register.md); sus identidades,
correos de proyecto y autorización de integración actual están resueltos por
el handoff aprobado. Future workstreams de Gino, Gerard y Sebastián requieren
revisión propia antes de atribución.
