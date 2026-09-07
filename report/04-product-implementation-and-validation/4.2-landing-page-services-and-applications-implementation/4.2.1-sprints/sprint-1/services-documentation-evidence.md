# Services Documentation Evidence for Sprint Review

Documentar endpoints OpenAPI/Swagger, acciones, parámetros, ejemplos y commits.

## Referencia cruzada de contratos actuales

La instantánea actual del API se describe en el
[Mobile V1 API contract register](../../../../../delivery-checklists/mobile-v1-api-contract-register.md).
Las filas siguientes son candidatos de contrato para Sprint 1; no son evidencia
de ejecución del Sprint ni prueban consumo desde Mobile.

| Candidate stories | Contract operations | Current state |
| :--- | :--- | :--- |
| MOB-US-001..003 | `GET /api/v1/session`; `GET /api/v1/access-matrix`; authentication sign-in/refresh/sign-out | API contract observed; client and acceptance pending |
| MOB-US-011..012 | `GET /api/v1/skus/resolve`; `GET /api/v1/skus` | API contract observed; camera/manual-search evidence pending |
| MOB-US-013..014 | `POST /api/v1/inventory/inbound-receipts`; `GET /api/v1/inventory/lots/{lotId}` | API contract observed; request examples and receiving evidence pending |
| MOB-US-015..017 | inventory and lot reads; physical scan validation; adjustments/dispositions | API contract observed; role, device and immutable-history evidence pending |
| MOB-US-019 | temperature reading/evidence operations | Related API operations observed; applicability and physical evidence pending |

Sprint dates, owners, board URL, task mapping, screenshots, video and commit
IDs remain pending human evidence.
