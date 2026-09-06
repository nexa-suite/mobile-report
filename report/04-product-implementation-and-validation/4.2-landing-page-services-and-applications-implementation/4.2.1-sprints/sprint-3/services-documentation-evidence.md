# Services Documentation Evidence for Sprint Review

Documentar endpoints OpenAPI/Swagger, acciones, parámetros, ejemplos y commits.

## Referencia cruzada de contratos actuales

Consulta el [registro de contratos API Mobile V1](../../../../../delivery-checklists/mobile-v1-api-contract-register.md)
para la revisión de origen, headers, contrato de respuesta y evidencia
restante. Estas filas son referencias cruzadas candidatas, no prueba de
ejecución de Sprint 3.

| Candidate stories | Contract operations | Current state |
| :--- | :--- | :--- |
| MOB-US-044 | `GET /api/v1/notifications/unread`; `GET /api/v1/notifications/unread-count`; `GET /api/v1/notifications` | API contract observed; notification provider and client delivery pending |
| MOB-US-047 | `POST /api/v1/delivery-handoff/validations` | API contract observed; buyer relationship and device acceptance pending |
| MOB-US-048 | `POST /api/v1/deliveries/{deliveryId}/buyer-receipts` | API contract observed; receipt workflow and client evidence pending |
| MOB-US-049 | Incident and Business Document Evidence operations; no dedicated buyer discrepancy path identified | Contract mapping requires human/product confirmation |

Sprint dates, owners, board URL, task mapping, screenshots, video and commit
IDs remain pending human evidence.
