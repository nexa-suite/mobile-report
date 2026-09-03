# Baseline vivo del informe móvil

## Propósito

Este documento registra el estado observable al iniciar la sincronización del
informe académico. Es un corte AS-IS: no representa una certificación de
implementación, aceptación del producto ni preparación para producción.

## Corte registrado

| Campo | Valor |
| :--- | :--- |
| Fecha del corte | 2026-09-01 |
| Repositorio del informe | `git@github.com:nexa-suite/mobile-report.git` |
| Rama de trabajo inicial | `chapter-02` |
| Rama por defecto del remoto | `main` |
| Estado inicial | Limpio, sin cambios locales |
| Base del avance | `3edeb196800a72a30299987a661e791c8f8fb50d` |
| Commit base | `docs(ch2): Correct gramatic errors` |

## Repositorios de evidencia consultados

Los SHA identifican el corte leído. El informe puede describir estos
repositorios como fuentes; no puede convertir un estado de otro repositorio en
evidencia de una funcionalidad móvil sin una verificación específica.

| Fuente | Rama/corte | SHA | Uso en el informe |
| :--- | :--- | :--- | :--- |
| `mobile-report` | `chapter-02` | `3edeb196800a72a30299987a661e791c8f8fb50d` | Informe actual y contenido de Capítulos I-II |
| `blueprint` | `main` | `fce3ba6f8ca1622084a2114424086364e1f7d93f` | Decisiones aceptadas, catálogo móvil y proyección académica |
| `nexa-ecosystem-report` | `main` | `e161fe522023bfe5929e76c4d7c66af211884b7e` | Evidencia histórica para clasificación, no autoridad actual |
| `mobile` | `main` | `88c99a1079d17ce4514791087451452bdbf17c51` | Implementación móvil observable, si la evidencia aplica |
| `api` | `main` | `380e2427bc3883f23fbd7e9a82d452888f2074a8` | API candidata y contratos verificables |
| `design-lab` | `main` | `c16c1f4b64af688754a7c3bc989db9308f825c66` | Fuente de decisiones y artefactos de diseño |
| `website` | `main` | `96ab63a95f923114627048283c323a501238ff53` | Landing Page y evidencia web |
| `platform` | `main` | `f8285f1bf0de83ed6fa95aa86d1dcc6efd4897f7` | Aplicación web de operaciones |
| `portal` | `main` | `672836b8369ea16cb1374d348d73ccacbebbc954` | Portal del comprador |

## Inventario local y tooling

| Comprobación | Resultado | Implicación |
| :--- | :--- | :--- |
| Archivos rastreados en el corte del informe | 59 | El branch inicial contenía sólo la base de Capítulos I-II y assets existentes |
| Markdown rastreado en el corte | 54 | No había pipeline documental local declarado |
| `package.json`, `Makefile`, `Taskfile`, Dockerfile, Compose, scripts o workflows en el corte | No encontrados | La generación PDF, lint y diagramas requiere configurar o documentar tooling antes de declarar un gate automatizado |
| Compose en `/Users/joaquinfranciscoverdebueno/Developer/nexa-suite` | No encontrado | No se declara un stack local levantado desde la raíz |
| Host | Apple M5, 10 cores, 16 GB RAM, macOS 26.6.2 | Capacidad disponible para validaciones locales |
| Docker Desktop | Server 29.7.2, ARM64/aarch64, 10 CPUs, aproximadamente 8.3 GB asignados | Runtime disponible; el compose del producto aún debe localizarse y verificarse |

## Gaps que bloquean una entrega final

- Identidad académica completa, códigos, fotos, docente y autoría por commit:
  requiere confirmación humana.
- Entrevistas S1, S2 y S3, participantes, grabaciones, capturas y análisis:
  requieren evidencia primaria real.
- Investigación secundaria de operaciones físicas y bibliografía Q1/Q2:
  requiere fuentes verificadas y registro de consulta.
- Runtime móvil, almacenamiento local, recurso del dispositivo, servicio REST,
  servicio externo, distribución y demostración en dispositivo físico:
  requieren validación técnica y evidencia reproducible.
- Datos de sprints, tablero, velocidad, tareas, revisiones, videos y
  despliegues: no se infieren desde la estructura del informe.

## Regla de actualización

Cada nuevo corte debe conservar fecha, rama, SHA y alcance de la comprobación.
Una fila sólo cambia a `VERIFIED` cuando existe una fuente concreta y una
verificación reproducible; la existencia de una plantilla no cambia el estado
de evidencia.

## Estado del worktree después del primer avance

| Campo | Valor |
| :--- | :--- |
| Rama actual | `feature/report-front-matter-and-governance` |
| Upstream | Sin configurar; no se ha publicado la rama |
| Estado | Cambios locales sin commit |
| Naturaleza de los cambios | Estructura, reconciliación documental, plan de investigación y backlog V1 |
| Gate | Revisión humana de ownership y diff pendiente; no crear commit automáticamente |

## Checkpoint seguro — 2026-09-01

El avance queda pausado para revisión humana. No hay archivos staged, commits
nuevos, upstream publicado, merge ni cambio persistente de identidad Git.

Comprobaciones ejecutadas antes de pausar:

- `git diff --check`: sin errores.
- User Stories: 28 encabezados detallados, 28 filas de resumen y 112 escenarios
  Gherkin.
- Registro manual: `0/28` historias aprobadas.
- Entrevistas actuales: `0` verificadas en S1, S2 y S3.

La siguiente reanudación debe comenzar revisando el diff y asignando el owner
humano de cada cambio. El primer gate no autoriza todavía `git add` ni `git
commit`; requiere confirmación explícita del owner, username, email, rama,
archivos y mensaje Conventional Commit.

El detalle operativo está en [human-commit-gate.md](./human-commit-gate.md).

## Verificación reproducible posterior — 2026-09-01

Tras reanudar el trabajo se ejecutaron dos gates locales adicionales, sin
staging ni commit:

- `bash scripts/verify-report-structure.sh` → `stories=28`,
  `summary_rows=28`, `scenarios=112`; además pasó el escaneo de términos
  internos prohibidos y whitespace final.
- `python3 scripts/verify-mobile-v1-transcription.py` → coincidencia con la
  proyección actual del Blueprint en actores, épicas, BC, puntos, Sprint y
  títulos; `28` filas, `28` títulos y `112` escenarios.
- `python3 scripts/verify-mobile-v1-api-register.py` → `28` historias y `60`
  mappings explícitos coinciden con `api/docs/openapi/openapi.json` (`268`
  paths); las `60` operaciones tienen respuestas y parámetros de ruta completos,
  pero el snapshot conserva `0` ejemplos request y `0` response; sigue siendo
  evidencia de contrato, no de cliente Mobile.
- `python3 scripts/verify-mobile-v1-review-register.py` → `28` filas del
  registro manual alineadas por actor/segmento/BC; las decisiones continúan en
  `PENDING HUMAN REVIEW`.
- `bash scripts/check-report-links.sh` → `local Markdown links OK`.
- `git diff --check` → sin errores.
- `bash scripts/inspect-api-persistence.sh` → PostgreSQL 18.4; tablas Mobile
  relevantes, conteos de constraints, `FORCE_RLS` y triggers/policies
  observados en modo sólo lectura.
- `mobile/node scripts/validate-repository.mjs` → repositorio documental, sin
  cliente nativo, build ni runtime.
- `api/./mvnw test` Docker-backed → `BUILD SUCCESS`; 482 pruebas, 0 fallos y
  148 omitidas; Testcontainers utilizó Docker 29.7.2 y PostgreSQL 18.4.
  El rerun del 2026-09-02 sin Docker disponible también terminó en
  `BUILD SUCCESS`, con 482 pruebas, 0 fallos y 152 omitidas; se conserva como
  baseline no-integrado y no sustituye la observación Docker-backed.

Estos resultados validan estructura y referencias locales del corte, pero no
validan entrevistas, aceptación de producto, runtime Mobile, dispositivo,
identidad de autores ni preparación para producción.

## Verificación de stack local e integración ampliada — 2026-09-01

Se levantó el compose moderno del API y se observaron saludables los servicios
API, PostgreSQL, MinIO, ClamAV, WireMock Stripe, Platform y Portal. El API
respondió `status=UP` en `/actuator/health`; Platform y Portal respondieron
HTTP `200`. MinIO se expuso en `127.0.0.1:19000` sólo porque el puerto local
9000 estaba ocupado por un kernel de Jupyter; la comunicación interna conservó
`modern-minio:9000`.

El comando ampliado `api/./mvnw clean verify -Dnexa.integration.enabled=true`
con endpoints locales produjo `BUILD FAILURE`: 482 pruebas, 3 fallas, 0
errores y 0 omitidas. Los adaptadores ClamAV, S3-compatible y Stripe WireMock
pasaron sus pruebas focalizadas; `MobileV1CoreContractsIT` pasó 6/6. Las tres
fallas observadas pertenecen a `TenantAdministrationIT` y quedan registradas
en [implementation-evidence-register.md](./implementation-evidence-register.md):
no se convierten en aceptación ni se corrigen dentro del alcance documental.

Este resultado es evidencia parcial de backend/integración. No demuestra
cliente Mobile nativo, aceptación de usuario, dispositivo físico, autoría de
commits, distribución ni preparación para producción.

## Reconciliación canónica de Sprints — 2026-09-01

La fuente académica y el Blueprint consultados definen tres Sprints, no cuatro:

| Sprint | Hito académico | Historias V1 proyectadas |
| :--- | :--- | :--- |
| S1 | TB1 | `MOB-US-001..017`, `MOB-US-019` |
| S2 | AV2 | `MOB-US-020..034` |
| S3 | TB2 | `MOB-US-044`, `MOB-US-047..049` |

Se actualizó el índice del capítulo IV para reflejar esta asignación. El
scaffold local no canónico de `sprint-4` quedó retirado del corte documental;
no se eliminó evidencia de producto ni se alteró ningún repositorio de código.
La asignación de historias sigue siendo candidata hasta la aceptación humana
del backlog y la existencia de evidencia real de cada Sprint.

La matriz completa por obligación, estado y responsable está en
[rubric-gap-matrix.md](./rubric-gap-matrix.md).

## Validaciones oficiales del Blueprint — 2026-09-01

Se ejecutaron los tres validadores locales del Blueprint:

```text
bash tooling/scripts/validate-academic-mobile.sh
bash tooling/scripts/validate-mobile-master-backlog.sh
bash tooling/scripts/validate-blueprint.sh
```

Los tres terminaron en `FAIL` por la misma condición: detectan
`90-academic/mobile/enunciado-trabajo-final.md` como artefacto source-like que
debería permanecer local-only/ausente del árbol publicable. Esa ruta es la
rúbrica canónica indicada para este trabajo y fue conservada; no se reescribió
ni se eliminó para maquillar el gate. No se observaron otros fallos en la salida
de estos tres comandos. El resultado queda como `BLOCKED BY TOOLING RULE`, no
como validación aprobada.

La inspección de persistencia local está registrada en
[api-persistence-evidence-register.md](./api-persistence-evidence-register.md).

## Verificación de fuentes de diagramas — 2026-09-01

Se inspeccionó el repositorio Blueprint en `main` en el commit
`fce3ba6f8ca1622084a2114424086364e1f7d93f`. Se observaron fuentes Structurizr
DSL, exports C4 AS-IS/TARGET, modelos PlantUML y fuentes/exports de datos para
los once Bounded Contexts. La validación documentada con
`structurizr/structurizr:2026.06.28` terminó con exit code `0` sobre
`workspace.dsl`.

La procedencia y hashes representativos están en
[architecture-render-evidence-register.md](./architecture-render-evidence-register.md).
El resultado no cierra la revisión visual humana, la selección de artefactos
para el informe, el ownership lógico ni ninguna afirmación de implementación o
aceptación Mobile.

## Checkpoint seguro actualizado — 2026-09-01

El estado queda en mini-freeze para revisión humana. La rama sigue siendo
`feature/report-front-matter-and-governance`, basada en
`3edeb196800a72a30299987a661e791c8f8fb50d`; no hay staging, commits nuevos,
upstream publicado, merge ni push.

Gates del checkpoint: huellas SHA-256 del prompt y rúbrica canónicos OK;
estructura `28/28/112`, transcripción canónica `28/28`
con `112` escenarios, registro API `60` operaciones explícitas, `60/60`
response blocks, `24` request bodies, `60/60` path parameters y alineación de
Sprint `28/28`; enlaces Markdown locales OK, `git diff --check` OK, API baseline
OK, matriz de rúbrica actualizada y gate de integración ampliado PARTIAL por las
tres fallas explícitas de `TenantAdministrationIT`. La revisión manual de
historias continúa en `0/28` y las entrevistas verificadas en `0` para S1, S2 y
S3.

No se autoriza `git add` ni `git commit` hasta que cada lead revise su historia
y el owner confirme identidad GitHub, email asociado, archivos, alcance,
validación y mensaje Conventional Commit en el [Human Commit
Gate](./human-commit-gate.md).

## Checkpoint seguro — inventario de arquitectura — 2026-09-01

Se añadió el [architecture and diagram evidence register](./architecture-render-evidence-register.md)
con la procedencia versionada de C4/Structurizr, PlantUML y diagramas de datos
observados en Blueprint. El DSL Structurizr fijado en
`structurizr/structurizr:2026.06.28` validó con exit code `0`; los exports y
fingerprints quedaron registrados como `SOURCE/EXPORT OBSERVED`.

El informe permanece en mini-freeze: la revisión visual, selección de artefactos,
ownership lógico, aprobación de las 28 historias, identidades de owners y
autorización de commit siguen pendientes. El cierre de este checkpoint no
declara implementación Mobile, aceptación de producto, runtime en dispositivo
ni preparación para producción.

## Cross-check bibliográfico — 2026-09-01

Se consultaron páginas públicas de métricas para las cuatro revistas candidatas
y se enlazaron en la [bibliografía](../report/92-bibliography/bibliography.md).
El resultado es sólo un cross-check preliminar; no sustituye la captura oficial
Scopus/Web of Science exigida por la rúbrica, por lo que el estado permanece
`PRELIMINARY / PENDING TEAM CAPTURE`.

## Precheck público de usernames — 2026-09-01

Las cinco URLs de GitHub proporcionadas por el prompt resolvieron a perfiles
públicos y quedaron registradas en [team-identity-register.md](./team-identity-register.md).
Esto sólo confirma disponibilidad pública del username y, cuando existe, el
display name; no confirma identidad legal, email asociado, ownership de cuenta,
lead de historia ni autoría de commit. El gate humano permanece abierto.

## Precheck de autores históricos — 2026-09-01

La revisión de `git log --all` encontró autores observables en `report`, `api`,
`mobile` y `blueprint`. El registro conserva sus hashes y correos exactos. Se
detectó que un commit histórico del informe usa el alias `ManoJVB10` para un
display name de Joaquín, mientras el prompt suministra `JoaquinBV511`; la
discrepancia queda expresamente pendiente de reconciliación humana. No se
atribuye ownership ni autoría nueva por estos datos.

## Reanudación desde handoff verificado — 2026-09-02

El handoff coincide con el estado técnico esperado: rama
`feature/report-front-matter-and-governance`, `HEAD`
`3edeb196800a72a30299987a661e791c8f8fb50d`, base igual, upstream inexistente,
staging vacío y ningún commit nuevo. El diff conserva `27` archivos rastreados
modificados y `119` archivos no rastreados (`146` paths en total); el `git diff --stat` del contenido
rastreado reporta `1680` inserciones y `1692` eliminaciones.

Antes de actualizar registros se creó una copia de recuperación fuera del
contenido académico:
`/tmp/nexa-mobile-report-handoff.pUPzYu/`. Contiene `tracked.diff`, estado,
`HEAD` y copia de `116` archivos no rastreados. No forma parte del informe ni
se debe committear.

Tras incorporar las asignaciones de leads, la matriz de ownership y la síntesis
secundaria S2 se generó una copia vigente en
`/tmp/nexa-mobile-report-resume.PJofE0/`, con el diff rastreado y los `119`
archivos no rastreados del corte actual. Ambas copias
están fuera del contenido académico y no se deben committear.

El handoff resolvió las cinco identidades actuales y el alias histórico de
Joaquín. Se actualizó el registro con estado
`OWNER CONFIRMED BY HANDOFF` y correo
`OWNER-CONFIRMED PROJECT COMMIT EMAIL`; no se convirtió esa resolución en
ownership automático de cada diff.

Se asignó la primera revisión semántica a Gino / `R0obxdnt` para
`MOB-US-011..017` y `MOB-US-019`; Diego, Gerard y Sebastián recibieron sus
respectivos lotes por el reparto del handoff; Joaquín conserva revisión
académica secundaria de las `28` historias. Las decisiones siguen en
`PENDING HUMAN REVIEW`, no se autoaprobaron.

La matriz [current-diff-ownership-matrix.md](./current-diff-ownership-matrix.md)
clasifica los `146` paths actuales en `9` unidades naturales. Su validador
reproducible pasó sin paths huérfanos ni duplicados; staging sigue vacío. El
siguiente checkpoint exige que Sebastián revise semánticamente la Unidad B
actualizada y que Gino continúe la primera revisión manual de historias; sólo
después se puede mostrar un diff staged exacto y solicitar autorización
explícita.

## P11 — reconciliación Chapter III con Design Lab — 2026-09-02

Se avanzó Chapter III con evidencia actual del Design Lab `v1.0.2`, commit
`c16c1f4b64af688754a7c3bc989db9308f825c66`. El informe ahora registra un ledger
de fingerprints de tokens, autenticación, entrega/POD y responsive, además de
un crosswalk explícito hacia los cinco user goals Mobile V1. La adopción queda
como `SOURCE OBSERVED / TARGET RECONCILED`; no se presenta como cliente Mobile,
pantalla renderizada, API consumida, autorización, dispositivo ni Product
Acceptance.

La evidencia fuente observada conserva las fronteras del propio Design Lab:
sus patrones son especímenes visuales y de interacción, las transiciones de
dominio no se ejecutan y la revisión visual humana, assistive technology,
catálogos `en_US`/`es_419`, Figma/LucidChart/Overflow, prototipo, captura y
dispositivo siguen pendientes. La matriz de rúbrica fue actualizada con ese
estado parcial.

Los gates documentales posteriores pasaron: fuentes canónicas, ownership
`146` paths/`9` units, transcripción `28/28/112`, revisión-register alineado,
API register `60` operaciones/`60` response blocks/`24` request bodies/`60/60`
path params/Sprint `28/28`, estructura del informe, enlaces Markdown,
`git diff --check`, sintaxis shell, compilación Python y staging vacío.

Una primera ejecución read-only de `bash scripts/inspect-api-persistence.sh` no
pudo conectarse al socket Docker porque el daemon aún no estaba disponible.
Después se inició Docker Desktop y únicamente `nexa-modern-postgres`; la
segunda ejecución terminó con exit `0` y observó PostgreSQL `18.4`, tablas,
columnas, constraints, FORCE_RLS, triggers y policies sin modificar datos. El
resultado se incorporó al registro de persistencia y sigue siendo evidencia de
backend, no de Mobile, dispositivo ni Product Acceptance.

Este checkpoint mantiene el mini-freeze: no hay `git add`, commit, merge, push
ni publicación. La revisión manual de historias permanece `0/28`; el siguiente
gate humano debe revisar la Unidad G/Chapter III y luego continuar con la
revisión individual de stories y artefactos antes de autorizar cualquier unidad
de commit.

## Gate bibliográfico y snapshot actual — 2026-09-02

Se añadió `scripts/verify-bibliography-citations.py` y se integró en el gate de
estructura. Comprueba los cuatro papers obligatorios fuera de la bibliografía,
sus DOI y el estado explícito `PRELIMINARY/PENDING`, además de detectar el uso
de las seis referencias técnicas registradas. Resultado: mandatory `4/4`, DOI
`4/4`, technical refs `6/6`.

El snapshot actual conserva `27` archivos rastreados modificados y `120`
archivos no rastreados (`147` paths); el diff rastreado permanece en `1680`
inserciones y `1692` eliminaciones. El validador de ownership pasó con
`147` paths y `9` unidades; el script nuevo pertenece a la Unidad I.

La copia de recuperación externa debe reflejar este snapshot antes de cualquier
otra edición: `/tmp/nexa-mobile-report-resume.PJofE0/`. El mini-freeze sigue
activo: el script mejora la verificación, pero no autoriza staging, commit,
merge, push ni publicación.

## P14/P15 — gates de entregables académicos — 2026-09-02

Los checklists `av1.md`, `tb1.md`, `av2.md` y `tb2.md` dejaron de ser sólo
recordatorios y ahora contienen gates verificables por hito: artefacto exigido,
estado observado y prueba de cierre. AV2 y TB2 separan explícitamente backend
público, consumo Mobile, videos, distribución, dispositivo, aceptación y
entrega final. Ningún hito fue marcado como completado.

El snapshot sigue en `147` paths (`27` rastreados modificados y `120` no
rastreados), con staging vacío. La siguiente acción condicionada es la revisión
humana de las unidades y de las `28` historias; mientras tanto, los estados
`OPEN`, `PARTIAL` y `PENDING HUMAN` permanecen intactos.

## Handoff aprobado e integración autorizada — 2026-09-02

DiegoS284 y JoaquinBV511 revisaron conjuntamente el handoff actual. La
integración del reporte V1 queda aprobada para `28/28` historias. Esta decisión
no inventa revisiones individuales de Gino, Gerard o Sebastián: su defensa
individual queda como follow-up y no bloquea la integración actual.

La autorización cubre staging, commits, push de la rama
`feature/report-front-matter-and-governance`, PR hacia `develop` y merge normal
si la validación queda verde salvo los gaps `PARTIAL` ya documentados. El
trabajo actual se atribuye sólo por unidad a Joaquín o Diego según
[current-diff-ownership-matrix.md](./current-diff-ownership-matrix.md); no se
reescribe historia ni se usa `main` como destino.

Estado técnico adicional: `OpenApiContractIT` y `MobileV1CoreContractsIT`
rerun focalizado pasó `7` tests, `0` failures, `0` errors y `0` skipped con
PostgreSQL efímero `18.4-alpine` administrado por Testcontainers. Esto respalda
contratos backend; no cierra Mobile client, dispositivo, aceptación ni
producción. La baseline general conserva `482/0/148` histórica Docker-backed y
`482/0/152` en el rerun sin Docker; la integración ampliada conserva sus `3`
fallas conocidas de `TenantAdministrationIT`.

El siguiente paso operativo es inspeccionar y commitear unidades lógicas con
identidad one-shot de Joaquín o Diego, verificar cada commit, publicar rama,
abrir PR y evaluar merge a `develop`. AV1, TB1, AV2 y TB2 permanecen abiertos;
el Goal activo continúa hacia TB2.

## Secuencia local integrada — 2026-09-02

La integración revisada quedó en `13` commits locales desde la base
`3edeb196800a72a30299987a661e791c8f8fb50d`, todos bajo la atribución autorizada
de Joaquín o Diego y con staging vacío. Los mensajes, autores, correos de
proyecto y hashes completos están en [human-commit-gate.md](./human-commit-gate.md).

El `HEAD` de la secuencia integrada es
`8fdf42018e9c3b3bfd343a1f319ae5ca831df5e6`. La rama
`feature/report-front-matter-and-governance` fue publicada correctamente y su
upstream quedó configurado en
`origin/feature/report-front-matter-and-governance`. No se ha hecho force-push,
merge a `main` ni release; el PR hacia `develop` sigue pendiente.

Validación documental posterior a la secuencia: fuentes canónicas OK,
estructura `28/28/112`, revisión-register alineado, API register
`60/60/24/60/28`, bibliografía `4/4` DOI y `6/6` referencias técnicas,
ownership `147` paths/`9` units, enlaces Markdown OK, `git diff --check` OK,
Structurizr exit `0`, persistencia read-only exit `0` y contrato focalizado
`7/0/0/0`. Las gates de runtime Mobile, dispositivo, distribución, aceptación,
videos, entrevistas actuales y Q1/Q2 oficial siguen abiertas según las
matrices AV1/TB1/AV2/TB2.

## Reconciliación aprobada publicada — 2026-09-02

El owner humano Joaquín Francisco Verde Bueno ejecutó la reconciliación
autorizada sobre `reconcile/report-integration-20260902`. El baseline de
`develop` fue `928cb1c4ca0a0848c4b0c0de32108c87ee97dada`; la rama de feature
`feature/report-front-matter-and-governance` quedó preservada en
`a19642c38ecf21905874fc5fbabceff0410320b6`; y el merge no squash es
`86351b3c75f471cb79c3d677718cf07dd035ae55`. Se resolvieron `76/76` conflictos
por path y semántica, con la autoridad Blueprint y la baseline de feature
aplicadas según el handoff humano.

La rama fue publicada en
`origin/reconcile/report-integration-20260902`. `origin/develop` y
`origin/main` permanecen en `928cb1c4ca0a0848c4b0c0de32108c87ee97dada`; no se
hizo force-push, release ni cambio en `main`. La PR hacia `develop` sigue
pendiente de apertura.

Los gates documentales y de arquitectura pasan: estructura, semantic scan
(`28` historias, `112` escenarios, `11` contextos), API register,
bibliografía, links, Structurizr, PlantUML, modelo de datos y persistencia
observada. La gate ampliada de API fue repetida con ClamAV, MinIO y Stripe
mock disponibles y conserva su estado `PARTIAL`: `482` tests, `3` fallas
conocidas de `TenantAdministrationIT`, `0` errores y `0` skipped. Las gates
de runtime Mobile, dispositivo, distribución, aceptación, videos,
entrevistas actuales y Q1/Q2 oficial permanecen abiertas.

## Checkpoint vigente post-reconciliación — 2026-09-02

Este corte supersede únicamente el estado operativo de los checkpoints
anteriores; conserva sus registros históricos y no convierte sus observaciones
en evidencia de implementación o aceptación.

| Campo | Valor |
| :--- | :--- |
| Rama | `reconcile/report-integration-20260902` |
| Último source checkpoint validado | `afe62423d5759a76b3126d86dd614edcc833a478` |
| Base `origin/develop` / `origin/main` | `928cb1c4ca0a0848c4b0c0de32108c87ee97dada` |
| Relación en el source checkpoint | `0` behind / `32` ahead |
| Worktree y staging | Limpio; staging vacío |
| Conflictos reconciliados | `76/76` por path y semántica, según ledger aprobado |
| Integración de historias | `28/28` aprobada por DiegoS284 y JoaquinBV511; defensa individual sigue follow-up humano |

La secuencia posterior a la auditoría contiene nueve commits nuevos hasta el
source checkpoint, todos con
la identidad confirmada de Joaquín y mensajes Conventional Commit. El commit
`a4300002c165cc250493258aa748989976a26799` registra la baseline Docker-backed
del API: `./mvnw test` terminó `BUILD SUCCESS`, `482` pruebas, `0` fallos y
`148` omitidas, con Java 25.0.4.1, Docker 29.7.2 y PostgreSQL 18.4-alpine.
El HEAD `afe62423d5759a76b3126d86dd614edcc833a478` sincroniza el conteo
semántico con el escaneo reproducible.
Los commits posteriores de este registro son sincronizaciones documentales;
el HEAD vivo y su relación con `develop` deben resolverse con `git` en cada
checkpoint, sin autorreferencia embebida.

Los gates actuales del informe permanecen reproducibles: estructura `28/28/112`,
transcripción `28/28/112`, registro API `60` operaciones y `60` bloques de
respuesta, revisión-register alineado, citas obligatorias `4/4`, DOI `4/4`,
referencias técnicas `6/6`, ownership `158` paths/`9` unidades, enlaces y
syntax checks OK, y semantic scan `233/81/106/28` sin claims actuales de
Mobile V1 pendientes. El gate de integración ampliada del API sigue
`PARTIAL` por las tres fallas de `TenantAdministrationIT` ya documentadas.

No existe PR abierto detectado para esta rama contra `develop`; la creación
requiere autenticación GitHub manual. No se ha hecho merge, release ni cambio
en `main`. Permanecen abiertos los gates de defensa individual, revisión
visual humana, runtime/dispositivo Mobile, distribución, videos, entrevistas
actuales, Product Acceptance, Q1/Q2 oficial y entregables finales.

## Checkpoint vigente después de Markdown lint — 2026-09-02

Este corte supersede el estado operativo anterior y conserva sus datos como
provenance. La tabla fija el source checkpoint inmediatamente anterior al
registro; el HEAD vivo y su relación se resuelven desde Git para evitar una
autorreferencia dentro del propio documento.

| Campo | Valor |
| :--- | :--- |
| Rama / source checkpoint | `reconcile/report-integration-20260902` / `2fb7092e6e45cbd02fff6ec3cdea86551c4956f0` |
| Upstream en el source checkpoint | `origin/reconcile/report-integration-20260902` en `2fb7092e6e45cbd02fff6ec3cdea86551c4956f0` |
| Base `origin/develop` / `origin/main` | `928cb1c4ca0a0848c4b0c0de32108c87ee97dada` |
| Relación viva | `0` behind / `42` ahead |
| Worktree / staging | Limpio / vacío |
| Ownership actual contra base histórica | `162` paths / `9` units |
| Markdown lint | `162` archivos, `0` issues |
| Integración Mobile V1 | `28/28` aprobada; defensa individual follow-up humano |
| Conflictos | `76/76` resueltos por path y semántica |

Los commits `82cd2b4b9e1b50f9718b10733b91e3e8d1510c9d`,
`0db654027248a4789e877dc26aedcf9146f2f45c` y
`2fb7092e6e45cbd02fff6ec3cdea86551c4956f0` registran, respectivamente, la
normalización de Markdown, su checkpoint de lint y la separación de provenance
semántica/estilo. El PR contra `develop` no está creado: requiere autenticación
GitHub manual. No se hizo merge, release ni cambio en `develop` o `main`.
