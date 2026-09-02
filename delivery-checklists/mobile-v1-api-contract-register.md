# Mobile V1 API contract evidence

## Scope and status

This register projects the current API contract into the academic Mobile V1
backlog using the interface-description boundary defined by OpenAPI [T4]. It
does not claim that a Mobile client consumes the contract, that a screen
exists, or that a story has been accepted.

| Field | Observed value |
| :--- | :--- |
| Status | `PARTIAL — BACKEND CONTRACT ONLY` |
| API repository | `/Users/joaquinfranciscoverdebueno/Developer/nexa-suite/api` |
| API source SHA | `380e2427bc3883f23fbd7e9a82d452888f2074a8` on `main` |
| Runtime contract | `GET http://127.0.0.1:8080/v3/api-docs` |
| Snapshot | `api/docs/openapi/openapi.json` |
| OpenAPI document | `3.1.0`, title `Nexa API`, version `0.17.0` |
| Document size | 268 paths and 275 schemas |
| Contract test | `OpenApiContractIT`: 1 run, 0 failures, 0 errors, 0 skipped |
| Mobile contract test | `MobileV1CoreContractsIT`: 6 runs, 0 failures, 0 errors, 0 skipped |
| Latest focused rerun | `MobileV1CoreContractsIT,OpenApiContractIT`: 7 runs, 0 failures, 0 errors, 0 skipped on 2026-09-02 |
| Mobile repository state | `mobile` SHA `88c99a1079d17ce4514791087451452bdbf17c51`; validation reports documentation-only and no native build/runtime claim |

## Contract conventions observed

- Authentication is represented by the bearer scheme and explicit session and
  refresh operations. Native refresh uses `X-Nexa-Refresh-Token` and the
  contract distinguishes client/surface headers.
- Critical mutations expose `Idempotency-Key` and, where the operation is
  versioned, `If-Match`. The client must not treat a retry as proof that a
  business mutation was duplicated or confirmed.
- The shared `NexaProblemDetail` schema includes `code`, `correlationId`,
  `category` and `retryable` in addition to the HTTP problem fields.
- The contract preserves separate delivery, Driver outcome, Buyer receipt,
  proof-of-delivery and notification operations. No endpoint was inferred for
  a screen or device resource.

## Story-to-contract projection

`Observed` means the path and operation are present in the OpenAPI snapshot.
`Partial` means a related contract exists but the story still needs product,
device or client evidence. `No direct path` means the current snapshot does
not expose a dedicated operation for that business action; it must not be
filled by guessing another endpoint's meaning.

| Sprint | Story | Business action | Observed contract | Status | Remaining evidence |
| :--- | :--- | :--- | :--- | :--- | :--- |
| S1 | MOB-US-001 | Return to an authorized session | `POST /api/v1/authentication/sign-in` (`signIn`); `POST /api/v1/authentication/refresh` (`refresh`); `GET /api/v1/session` (`session`); `POST /api/v1/authentication/sign-out` (`signOut`) | Partial | Native client flow, denial states and device evidence |
| S1 | MOB-US-002 | Work in the intended company/context | `GET /api/v1/session` (`session`); `GET /api/v1/organization/current` (`getCurrentOrganization`); `GET /api/v1/workspaces` (`workspaces`); `GET /api/v1/access-matrix` (`accessMatrix`) | Partial | Context selection behavior and Mobile authorization evidence |
| S1 | MOB-US-003 | See work allowed by role | `GET /api/v1/access-matrix` (`accessMatrix`); `GET /api/v1/permissions/catalog` (`listPermissionCatalog`) | Partial | Permission-change interaction and client evidence |
| S1 | MOB-US-011 | Identify a product by package/label code | `GET /api/v1/skus/resolve` (`resolveSellableSkuIdentifier`) | Partial | Camera/scanner permission, fallback and physical-device evidence |
| S1 | MOB-US-012 | Search for a product manually | `GET /api/v1/skus` (`listSellableSkus`); `GET /api/v1/catalog-items` (`listCatalogItems`) | Partial | Mobile search behavior and evidence that selection creates no stock fact |
| S1 | MOB-US-013 | Record stock that arrived | `POST /api/v1/inventory/inbound-receipts` (`receive`) | Partial | Request example, role acceptance, client retry and real receiving evidence |
| S1 | MOB-US-014 | Record lot, expiry and quantity | `POST /api/v1/inventory/inbound-receipts` (`receive`); `GET /api/v1/inventory/lots/{lotId}` (`lot`) | Partial | Payload verification and client draft/unconfirmed state |
| S1 | MOB-US-015 | Check lot and stock condition | `GET /api/v1/inventory` (`listInventory`); `GET /api/v1/inventory/lots` (`listInventoryLots`); `GET /api/v1/inventory/lots/{lotId}` (`lot`); `GET /api/v1/inventory-availability` (`availability`) | Partial | Freshness, authorization and Mobile observation |
| S1 | MOB-US-016 | Pick an eligible lot and quantity | `POST /api/v1/inventory/physical-allocation-scan-validations` (`validatePhysicalAllocationPickingScan`); `POST /api/v1/fulfillments/{fulfillmentId}/picking-starts` (`startFulfillmentPicking`); `POST /api/v1/fulfillments/{fulfillmentId}/picking-confirmations` (`confirmFulfillmentPicking`) | Partial | Client scan flow and acceptance on device |
| S1 | MOB-US-017 | Report discrepancy or disposition | `POST /api/v1/inventory/adjustments` (`adjust`); `POST /api/v1/inventory/lots/{lotId}/dispositions` (`recordInventoryLotDisposition`); `POST /api/v1/inventory/lots/{lotId}/quarantines` (`quarantineLot`); `POST /api/v1/inventory/lots/{lotId}/blocks` (`blockLot`); `POST /api/v1/inventory/waste-movements` (`waste`) | Partial | Role/evidence matrix and immutable-history validation |
| S1 | MOB-US-019 | Record relevant temperature evidence | `POST /api/v1/dispatch-orders/{id}/temperature-readings` (`temperature`); `POST /api/v1/deliveries/{deliveryId}/temperature-evidence` (`recordDeliveryTemperatureEvidence`) | Partial | Applicable subject, device source and physical evidence |
| S2 | MOB-US-020 | See deliveries ready for dispatch | `GET /api/v1/dispatch-readiness-candidates` (`readiness`); `GET /api/v1/dispatch-readiness-candidates/{id}` (`readinessOne`) | Partial | Current readiness review and Mobile presentation |
| S2 | MOB-US-021 | Assign a driver | `GET /api/v1/dispatch-assignees` (`listDispatchAssignees`); `POST /api/v1/dispatch-orders/{id}/assignments` (`assign`) | Partial | Owner/role acceptance and client retry evidence |
| S2 | MOB-US-022 | Check outgoing goods | `GET /api/v1/dispatch-orders/{id}` (`dispatch`); `GET /api/v1/fulfillments/{fulfillmentId}` (`getFulfillment`) | Partial | No dedicated check operation identified; confirm business mapping |
| S2 | MOB-US-023 | Preserve warehouse-driver handoff evidence | `GET /api/v1/dispatch-orders/{id}/handoff-notes` (`handoffNotes`); `POST /api/v1/dispatch-orders/{id}/handoff-notes` (`appendHandoffNote`) | Partial | Evidence artifact, roles and human review |
| S2 | MOB-US-024 | Identify a dispatch handoff reliably | `GET /api/v1/dispatch-orders/{id}` (`dispatch`); `GET /api/v1/deliveries/{deliveryId}` (`getDelivery`) | No direct path | Confirm whether a dedicated identifier-resolution contract is required |
| S2 | MOB-US-025 | Confirm goods left warehouse control | `POST /api/v1/fulfillments/{fulfillmentId}/dispatches` (`dispatchFulfillment`); `POST /api/v1/dispatch-orders/{id}/route-readiness` (`ready`) | Partial | End-to-end handoff evidence and current business transition |
| S2 | MOB-US-026 | See deliveries assigned to the driver | `GET /api/v1/my-deliveries` (`myDeliveries`); `GET /api/v1/my-deliveries/{id}` (`myDelivery`) | Partial | Driver identity, scope and Mobile client evidence |
| S2 | MOB-US-027 | Begin an assigned delivery | `POST /api/v1/deliveries/{deliveryId}/transit-starts` (`startDeliveryTransit`); `GET /api/v1/my-deliveries/{id}` (`myDelivery`) | Partial | Assignment, retry and physical-device evidence |
| S2 | MOB-US-028 | Open directions to authorized destination | `GET /api/v1/my-deliveries/{id}` (`myDelivery`) supplies the delivery context | Partial | External navigation handoff, location privacy and device evidence; no tracking claim |
| S2 | MOB-US-031 | Record delivery-attempt outcome | `POST /api/v1/deliveries/{deliveryId}/attempts` (`recordDeliveryAttempt`); `POST /api/v1/dispatch-orders/{id}/delivery-completions` (`complete`) | Partial | Outcome matrix, client retry and acceptance evidence |
| S2 | MOB-US-032 | Record partial/rejected delivery and remainder | `POST /api/v1/dispatch-orders/{id}/partial-deliveries` (`completePartialDelivery`); `POST /api/v1/dispatch-orders/{id}/delivery-attempts` (`recordFailedDeliveryAttempt`) | Partial | Quantity/reason examples and user validation |
| S2 | MOB-US-033 | Preserve proof of delivery | `POST /api/v1/deliveries/{deliveryId}/pod` (`captureDeliveryProofOfDelivery`); `POST /api/v1/deliveries/{deliveryId}/pod/seals` (`sealDeliveryProofOfDelivery`); Business Document Evidence endpoints | Partial | Camera/storage/device proof and acceptance evidence |
| S2 | MOB-US-034 | Present a bounded handoff code | `POST /api/v1/deliveries/{deliveryId}/handoff-tokens` (`issueDeliveryBuyerHandoffToken`) | Partial | Code presentation, expiry/replay and human/device evidence |
| S3 | MOB-US-044 | Know when delivery needs attention | `GET /api/v1/notifications/unread` (`listUnreadNotifications`); `GET /api/v1/notifications/unread-count` (`unreadCount`); `GET /api/v1/notifications` (`listNotifications`) | Partial | Notification provider, consent and Mobile delivery evidence |
| S3 | MOB-US-047 | Verify delivery through handoff code | `POST /api/v1/delivery-handoff/validations` (`validateDeliveryBuyerHandoffToken`) | Partial | Buyer relationship, invalid/reused code and device evidence |
| S3 | MOB-US-048 | Confirm quantities received | `POST /api/v1/deliveries/{deliveryId}/buyer-receipts` (`recordBuyerDeliveryReceipt`) | Partial | Buyer acceptance, retry/idempotency and device evidence |
| S3 | MOB-US-049 | Report discrepancy without erasing facts | `POST /api/v1/dispatch-orders/{id}/incidents` (`incident`); Business Document Evidence endpoints | No direct path | Confirm buyer-facing discrepancy contract and evidence ownership |

## Reproducible checks

Executed against the API source revision above:

```text
GET http://127.0.0.1:8080/actuator/health
→ status=UP for liveness and readiness

./mvnw clean verify -Dnexa.integration.enabled=true [local ClamAV, MinIO and Stripe mock endpoints]
→ BUILD FAILURE: 482 tests, 3 failures, 0 errors, 0 skipped

OpenApiContractIT
→ 1 test, 0 failures, 0 errors, 0 skipped

MobileV1CoreContractsIT
→ 6 tests, 0 failures, 0 errors, 0 skipped

python3 scripts/verify-mobile-v1-api-register.py
→ `mobile V1 API register OK`: 28 stories and 60 explicit path/operationId
mappings match the `api/docs/openapi/openapi.json` snapshot; all 60 operations
have response blocks and complete path parameters. The snapshot exposes 24
request bodies among those mappings but currently contains 0 request examples
and 0 response examples, so the OpenAPI/Swagger academic gate remains
`PARTIAL` until examples, captures and human review are supplied. No
client-consumption claim is made.
```

The three failed assertions are recorded in the implementation evidence
register. They belong to `TenantAdministrationIT`; they do not invalidate the
specific OpenAPI and Mobile V1 contract test results, but they prevent a
green full integration claim.

## Human review fields

| Field | State |
| :--- | :--- |
| Mobile lead | Pending |
| API contract owner | Pending |
| Report integration review | `28/28` approved by `DiegoS284 + JoaquinBV511`; individual defense follow-up |
| Product Acceptance | Pending |
| Physical-device acceptance | Pending |
| Decision | `OPEN — DO NOT PROMOTE TO IMPLEMENTED OR ACCEPTED` |
