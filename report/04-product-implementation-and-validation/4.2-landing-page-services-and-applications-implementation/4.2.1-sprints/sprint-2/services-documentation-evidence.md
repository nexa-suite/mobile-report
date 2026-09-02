# Services Documentation Evidence for Sprint Review

Documentar endpoints OpenAPI/Swagger, acciones, parámetros, ejemplos y commits.

## Current contract cross-reference

The complete operation-to-story mapping is in the
[Mobile V1 API contract register](../../../../../delivery-checklists/mobile-v1-api-contract-register.md).
These are candidate Sprint 2 operations only; no execution or Mobile client
completion is asserted.

| Candidate stories | Contract operations | Current state |
| :--- | :--- | :--- |
| MOB-US-020 | `GET /api/v1/dispatch-readiness-candidates` | API contract observed; readiness review pending |
| MOB-US-021 | `GET /api/v1/dispatch-assignees`; `POST /api/v1/dispatch-orders/{id}/assignments` | API contract observed; role/client evidence pending |
| MOB-US-022..025 | fulfillment/dispatch reads, handoff notes, fulfillment dispatch and route readiness | Related API operations observed; one-to-one business mapping and handoff evidence pending |
| MOB-US-026..028 | `GET /api/v1/my-deliveries`; `GET /api/v1/my-deliveries/{id}`; delivery transit start | API contract observed; driver/device/navigation evidence pending |
| MOB-US-031..034 | delivery attempts/outcomes, POD, temperature evidence and handoff tokens | API contract observed; physical proof and acceptance pending |

Sprint dates, owners, board URL, task mapping, screenshots, video and commit
IDs remain pending human evidence.
