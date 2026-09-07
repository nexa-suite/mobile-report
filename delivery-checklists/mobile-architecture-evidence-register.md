# Registro de evidencia de arquitectura Mobile

## Límite de la proyección

Operations Mobile y Buyer Mobile son superficies cliente de `V1 TARGET /
PLANNED / PROPOSED`. Nexa continúa siendo un sistema; ninguna superficie móvil
se presenta como Bounded Context, backend independiente o autoridad de negocio.
El framework, el build y el dispositivo final permanecen abiertos hasta que el
SPIKE correspondiente y una prueba reproducible los establezcan.

## Crosswalk de vistas y prueba disponible

| Superficie o vista | Fuente del diseño | Historias V1 relacionadas | Evidencia disponible en este corte | Estado |
| :--- | :--- | :--- | :--- | :--- |
| Operations Mobile — context | C4 System Context V1 TARGET | MOB-US-001..003, 011..034 | Export trazado a Structurizr; sin runtime Mobile | `TARGET / OPEN` |
| Operations Mobile — container | C4 Containers V1 TARGET | MOB-US-011..034 | Cliente planificado que consume Nexa API | `TARGET / OPEN` |
| Buyer Mobile — context | C4 System Context V1 TARGET | MOB-US-001..003, 044, 047..049 | Export trazado a Structurizr; sin runtime Mobile | `TARGET / OPEN` |
| Buyer Mobile — container | C4 Containers V1 TARGET | MOB-US-044, 047..049 | Cliente planificado que consume Nexa API | `TARGET / OPEN` |
| Mobile delivery topology | C4 Deployment V1 TARGET | S1–S3 projection | Topología dibujada; no deployment ejecutado acreditado | `TARGET / OPEN` |

El [registro de contrato API Mobile V1](./mobile-v1-api-contract-register.md)
relaciona historias con operaciones documentadas. La existencia de una ruta o
un diagrama no demuestra que exista una aplicación Mobile instalable ni que el
contrato haya sido aceptado por Product o System Acceptance.

## Pruebas necesarias para cerrar runtime

| Gate | Prueba mínima | Estado del corte |
| :--- | :--- | :--- |
| Identidad de implementación | Framework, versión, módulo y commit del cliente | `OPEN` |
| Build | Comando reproducible y artefacto identificable | `NOT EVIDENCED` |
| Ejecución | Emulador o dispositivo, API base, sesión autorizada y fecha | `NOT EVIDENCED` |
| Flujo V1 | Capturas o video de estados loading, empty, error, stale/conflict y success | `NOT EVIDENCED` |
| Seguridad | Tenant/workspace context, autorización de objeto y rechazo de alcance | `NOT EVIDENCED` |
| Entrega | URL o distribución controlada, versión, rollback y soporte | `OPEN` |

Para la revisión, trate cada celda `OPEN` o `NOT EVIDENCED` como una condición
pendiente; no la convierta en una afirmación de implementación por la presencia
de una imagen C4, una especificación o un mockup.
