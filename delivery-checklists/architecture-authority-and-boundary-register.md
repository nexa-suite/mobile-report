# Registro de autoridad y límites de arquitectura

## Propósito

Este registro permite revisar si una afirmación arquitectónica conserva la
autoridad de Blueprint y distingue diseño objetivo, implementación observada y
evidencia pendiente. No crea nuevos contextos, containers, endpoints ni
dependencias.

## Fuentes y alcance

| Elemento | Fuente fijada | Uso en el informe | Estado |
| :--- | :--- | :--- | :--- |
| Context Map y 11 Bounded Contexts | Blueprint Mobile V1 y modelo estratégico aceptado | Autoridad de Product y Domain | `SOURCE-BACKED / TARGET` |
| Sistema y containers C4 | `01-shared/architecture/c4/structurizr/workspace.dsl` y exports trazados | Separar Nexa, API, superficies, bases y almacenamiento | `SOURCE/EXPORT OBSERVED` |
| Paquetes tácticos | `2.6.1-bounded-context-coverage.md` y los once archivos BC | Describir capas y ownership lógico | `TARGET / PARTIAL AS-IS CROSSWALK` |
| Persistencia ejecutable | Registro API/persistence y repositorios inspeccionados | Informar sólo lo comprobado en código o configuración | `AS-IS PARTIAL` |
| Deployment | Export V1 y configuración que pueda reproducirse | No convertir topología dibujada en runtime probado | `TARGET / OPEN` |

Las rutas, hashes y fechas de exportación se encuentran en el [registro de
evidencia de diagramas](./architecture-render-evidence-register.md). Para una
revisión de origen, compare el corte Blueprint registrado allí con la fuente
actual; una imagen por sí sola no es autoridad semántica.

## Reglas de separación verificadas

| Relación que debe permanecer separada | Evidencia de control |
| :--- | :--- |
| Bounded Context ≠ Spring Modulith module | Los once contextos aparecen en Strategic/Tactical DDD; los módulos de código sólo se citan como implementación observada. |
| Bounded Context ≠ C4 Container | Las vistas C4 describen sistema, containers y componentes; el ownership de dominio se mantiene en el crosswalk táctico. |
| PostgreSQL compartido ≠ once bases físicas | Los diagramas de datos declaran ownership lógico y límites de acceso, sin inventar despliegues separados. |
| Mobile client ≠ autoridad de negocio | Las vistas de container y deployment mantienen API, autorización, idempotencia y transacciones en el servidor. |
| Diseño TARGET ≠ runtime AS-IS | Cada sección conserva las etiquetas `TARGET / PLANNED / PROPOSED`, `AS-IS VERIFIED` u `OPEN`. |

## Gate de revisión para el lector

Antes de considerar cerrada una afirmación, compruebe la fuente, el estado y el
límite de evidencia de la fila correspondiente. El corte actual deja abiertos
los siguientes puntos:

- revisión humana formal de la selección C4;
- ejecución reproducible de las superficies Mobile;
- contrato API aceptado con evidencia de request/response por Sprint;
- deployment local o cloud con versión, configuración y operación identificables;
- Product Acceptance, System Acceptance y Production Readiness.

La validación semántica reproducible es
[`verify-mobile-v1-semantics.py`](../scripts/verify-mobile-v1-semantics.py);
su resultado no sustituye esos gates humanos o de runtime.
