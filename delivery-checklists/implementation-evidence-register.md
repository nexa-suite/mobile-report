# Implementation and validation evidence register

## Purpose

This register prevents a repository reference, a template or a target design
from being presented as a completed Mobile implementation. Each claim needs a
source revision, exact action, observed result and human reviewer.

## Cross-repository audit snapshot — 2026-09-02

The following refs were fetched and inspected locally on 2026-09-02. A ref
establishes provenance for the repository surface named in the row; it does not
transfer implementation, runtime, acceptance or production evidence to the
Mobile report.

| Repository / role | Ref / SHA / commit date | What the ref proves for this report | What it does not prove |
| :--- | :--- | :--- | :--- |
| `blueprint` — canonical decisions and target design | `main` / `fce3ba6f8ca1622084a2114424086364e1f7d93f` / 2026-08-30 | Current C4, strategic DDD, Mobile story projection, UML/data sources and published architecture decisions | Mobile client implementation, runtime, device distribution or Product Acceptance |
| `api` — backend and contract evidence | `main` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` / 2026-08-31 | API source, OpenAPI snapshot, persistence and executed backend tests at the recorded scope | Mobile consumption, complete integration gate, user acceptance or production readiness |
| `platform` — operations web surface | `main` / `f8285f1bf0de83ed6fa95aa86d1dcc6efd4897f7` / 2026-09-01 | Versioned operations surface and its observable web evidence | Operations Mobile client, physical-device behavior or Mobile acceptance |
| `portal` — buyer web surface | `main` / `672836b8369ea16cb1374d348d73ccacbebbc954` / 2026-09-01 | Versioned buyer portal surface and its observable web evidence | Buyer Mobile client, physical-device behavior or Mobile acceptance |
| `website` — public website surface | `main` / `96ab63a95f923114627048283c323a501238ff53` / 2026-08-31 | Versioned public discovery/contact surface | Mobile implementation, API authority or product acceptance |
| `mobile` — Mobile repository | `main` / `88c99a1079d17ce4514791087451452bdbf17c51` / 2026-08-31 | Current repository role; its validation identifies a documentation-only repository with no native build or runtime claim | Native/cross-platform client, device evidence, distribution, API consumption or acceptance |
| `design-lab` — design source | `main` / `c16c1f4b64af688754a7c3bc989db9308f825c66` / 2026-08-31 | Versioned design decisions and visual artifacts when individually cited | Mobile runtime, implementation, device behavior or Product Acceptance |
| `mobile-report` — last validated audit snapshot | `reconcile/report-integration-20260902` / `afe62423d5759a76b3126d86dd614edcc833a478` / 2026-09-02 | Reconciled report after nine post-audit commits; later register-only syncs are documented separately and the live ref is resolved from Git | A merged PR, human visual/story defense, Mobile runtime, user research closure or production readiness |

The implementation repositories were clean on inspection and remained on their
local `main` refs; the report remains on the published reconciliation branch.
Repository names and package boundaries are evidence coordinates only and do
not redefine the Blueprint Bounded Contexts or C4 containers.

## Current register

| Requirement | Expected evidence | Current state | Owner / reviewer |
| :--- | :--- | :--- | :--- |
| REST contract consumption | Contract/OpenAPI source, request/response, authorization and error evidence | API source and automated support tests observed; Mobile consumption not verified | Pending |
| Local storage | Client source, safe-cache/draft/retry design and failure tests | No Mobile client evidence | Pending |
| Device resource | Permission, denial, fallback and physical-device capture | Not produced | Pending |
| External service | Provider decision, boundary, failure behavior and test | Provider open | Pending |
| Native Android delivery | Build output, checksum, install and observed result | Not produced | Pending |
| Physical device | Device model/version, date and video/screenshots | Not produced | Pending |
| Sprint execution | Board export/capture, dates, owner, tasks, review and validation | Templates only | Pending |
| Automated tests | Exact command, exit status and relevant output | Latest Docker-backed baseline: `./mvnw test` → 482 run, 0 failures, 148 skipped; no-Docker rerun: 482 run, 0 failures, 152 skipped; expanded local integration gate remains partial; no report-local test suite | Pending |
| Canonical story transcription | Report summary and detailed records match current Blueprint projection | `python3 scripts/verify-mobile-v1-transcription.py` → 28 rows, 28 titles, 112 scenarios; report integration 28/28 approved, individual defense and Product Acceptance remain open | Partial |
| OpenAPI/Swagger | Versioned document and inspected endpoint evidence | [Mobile V1 API contract register](./mobile-v1-api-contract-register.md); explicit path/operationId checker matches the API snapshot; request/response examples and Mobile consumption remain pending | Partial |
| Database persistence | Source migrations, read-only PostgreSQL schema inspection and reviewed diagram source | [API persistence evidence register](./api-persistence-evidence-register.md) plus [architecture and diagram evidence register](./architecture-render-evidence-register.md); logical ownership and academic review remain open | Pending human |
| Deployment | Environment, configuration, migration, URL/distribution and rollback | No deployment evidence | Pending |
| User validation | 3–5 current sessions per segment with consent and analysis | 0 verified sessions | Pending |
| Heuristic evaluation | Annex E record per artifact and re-check | Not produced | Pending |

## Evidence captured in the current continuation

### Mobile repository — negative implementation evidence

| Field | Value |
| :--- | :--- |
| Repository / source SHA | `mobile` / `88c99a1079d17ce4514791087451452bdbf17c51` |
| Branch | `main` |
| Exact command | `node scripts/validate-repository.mjs` |
| Observed result | `Mobile repository validation passed: documentation-only, no native build or runtime claim.` |
| Interpretation | Confirms the current repository role and absence of a native Mobile artifact; it does not satisfy the Android, device, distribution or Product Acceptance gates. |

### API support evidence

| Field | Value |
| :--- | :--- |
| Repository / source SHA | `api` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` |
| Branch | `main` |
| Exact command | `./mvnw test` |
| Environment observed | Java `25.0.4.1`; Spring Boot `4.1.0`; Testcontainers `2.0.5`; Docker Server `29.7.2`; PostgreSQL `18.4-alpine` container during integration tests |
| Observed result | Docker-backed baseline: `BUILD SUCCESS`; 482 tests run, 0 failures, 148 skipped |
| Interpretation | Supports the API/backend source and test baseline only. It does not prove Mobile client consumption, user acceptance, physical-device behavior or production readiness. |

### Latest API baseline rerun — 2026-09-02

| Field | Value |
| :--- | :--- |
| Repository / source SHA | `api` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` |
| Branch | `main` |
| Exact command | `./mvnw test` |
| Environment observed | Java `25.0.4.1`; Docker/Testcontainers unavailable because `/var/run/docker.sock` was not present in the session |
| Observed result | `BUILD SUCCESS`; 482 tests run, 0 failures, 152 skipped |
| Interpretation | Refreshes the non-integration baseline only. The four additional skips are an environment difference, not evidence that integration behavior passed; Mobile consumption and acceptance remain open. |

### Latest Docker-backed API baseline rerun — 2026-09-02

| Field | Value |
| :--- | :--- |
| Repository / source SHA | `api` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` |
| Branch | `main` |
| Exact command | `./mvnw test` |
| Observed completion | `2026-09-02 18:31:56 -0500` |
| Environment observed | Java `25.0.4.1`; Spring Boot `4.1.0`; Testcontainers `2.0.5`; Docker Server `29.7.2`; Testcontainers-managed PostgreSQL `18.4-alpine` |
| Observed result | `BUILD SUCCESS`; 482 tests run, 0 failures, 148 skipped; Maven total time `24.199 s` |
| Interpretation | Strengthens the current backend baseline with Docker-backed integration infrastructure. It does not prove Sprint 3 execution, Mobile client consumption, physical-device behavior, Product Acceptance or production readiness. |

### Latest focused API contract rerun — 2026-09-02

| Field | Value |
| :--- | :--- |
| Repository / source SHA | `api` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` |
| Exact command | `./mvnw -Dtest=MobileV1CoreContractsIT,OpenApiContractIT -Dnexa.integration.enabled=true test` |
| Environment observed | Java `25.0.4.1`; Docker Server `29.7.2`; Testcontainers-managed PostgreSQL `18.4-alpine` |
| Observed result | `BUILD SUCCESS`; `7` tests run, `0` failures, `0` errors, `0` skipped; `OpenApiContractIT` `1/1`; `MobileV1CoreContractsIT` `6/6` |
| Interpretation | Focused backend contract evidence for the Mobile V1 projection only. It does not prove Mobile client consumption, device behavior, Product Acceptance or production readiness. |

### Local product stack and expanded integration evidence

| Field | Value |
| :--- | :--- |
| Source revision | `api` / `380e2427bc3883f23fbd7e9a82d452888f2074a8` / `main` |
| Local stack | Docker Compose services observed healthy: API, PostgreSQL, MinIO, ClamAV, WireMock Stripe, Platform and Portal |
| Host adjustment | MinIO was exposed on `127.0.0.1:19000` because `127.0.0.1:9000` was occupied by a local Jupyter kernel; the container-to-container endpoint remained `modern-minio:9000` |
| Runtime checks | API `/actuator/health` returned `{"groups":["liveness","readiness"],"status":"UP"}`; Platform and Portal returned HTTP `200` |
| Exact command | `set -a; . /Users/joaquinfranciscoverdebueno/Developer/nexa-suite/api/.env.local; set +a; ./mvnw clean verify -Dnexa.integration.enabled=true -Dnexa.clamav.host=127.0.0.1 -Dnexa.clamav.port=3310 -Dnexa.object-storage.endpoint=http://127.0.0.1:19000 -Dnexa.object-storage.bucket=nexa-private -Dnexa.object-storage.access-key="$NEXA_MINIO_ROOT_USER" -Dnexa.object-storage.secret-key="$NEXA_MINIO_ROOT_PASSWORD" -Dnexa.stripe.api-base-url=http://127.0.0.1:12111` (run from `api`) |
| Environment | Java `25.0.4.1`; Docker Server `29.7.2`; PostgreSQL `18.4-alpine`; Testcontainers `2.0.5` |
| Observed result | `BUILD FAILURE`; 482 tests run, 3 failures, 0 errors, 0 skipped |
| Focused adapter results | ClamAV, S3-compatible object storage and Stripe WireMock integration reports each recorded `1` test, `0` failures, `0` errors, `0` skipped; `MobileV1CoreContractsIT` recorded `6` tests, `0` failures, `0` errors, `0` skipped |
| Remaining failures | `TenantAdministrationIT`: `tenantAllowsOnlyItsExistingV1WorkspaceAndProtectsFinalOwnerAndAdministrator` expected HTTP `409`, observed `200`; `companyOwnerInvitationCannotCreateASecondActiveOwner` expected `409`, observed `403`; `workspaceSettingsHaveOneCanonicalWarehouseStrategyAndCustomFieldsHaveAFullLifecycle` expected `200`, observed `403` |
| Interpretation | Partial backend/integration evidence only. It verifies that the local external-adapter path was reachable and exercised, while the three tenant-administration assertions remain unresolved. It does not prove Mobile client consumption, Product Acceptance, physical-device behavior, authorship or production readiness. |

The previous baseline command and this expanded gate are retained as separate
observations. A failing or partial integration gate is not rewritten as a
passing result.

Both entries remain subject to a human reviewer and must be associated with a
story, contract or implementation claim before any report row changes to
`VERIFIED`.

### Persistence evidence captured in the current continuation

The local PostgreSQL schema was inspected read-only after the modern compose
stack became healthy, and the capture was repeated on 2026-09-02 after starting
only `nexa-modern-postgres`. The [API persistence evidence register](./api-persistence-evidence-register.md)
records the API SHA, migration revisions, relevant tables, constraint counts,
RLS state and append-only/lifecycle triggers observed. This is backend schema
evidence only; it does not close the Tactical DDD diagram, Mobile local-storage
behavior, Product Acceptance or production gates.

The pinned Blueprint Structurizr source was also validated with the documented
`structurizr/structurizr:2026.06.28` image (exit code `0`). Versioned C4,
PlantUML and SVG/PNG artifacts were observed and fingerprinted in the
[architecture and diagram evidence register](./architecture-render-evidence-register.md).
This validates source syntax/provenance only; it does not replace the human
visual review or the instructor-approved academic render.

## Verification format

Record each completed item as:

```text
Evidence ID:
Requirement/story:
Repository and source SHA:
Branch:
Exact command or interaction:
Date/time and environment:
Observed result:
Artifact link or checksum:
Human reviewer:
Decision: VERIFIED | PARTIAL | OPEN | REJECTED
```

`VERIFIED` means the evidence was actually inspected and supports the stated
scope. It does not automatically mean Product Acceptance or production
readiness.
