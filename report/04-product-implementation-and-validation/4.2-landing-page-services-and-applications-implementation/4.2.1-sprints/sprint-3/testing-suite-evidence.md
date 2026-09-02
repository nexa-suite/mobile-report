# Testing Suite Evidence for Sprint Review

Documentar Unit Tests, Integration Tests, Acceptance Tests, Gherkin y commits de pruebas.

## Supporting backend baseline

The API `main` source at
`380e2427bc3883f23fbd7e9a82d452888f2074a8` was executed with Docker and
Testcontainers using `./mvnw test` on 2026-09-02. The observed result was
`BUILD SUCCESS`: 482 tests run, 0 failures and 148 skipped. The environment
used Java `25.0.4.1`, Spring Boot `4.1.0`, Testcontainers `2.0.5`, Docker
Server `29.7.2` and PostgreSQL `18.4-alpine`.

This is supporting backend evidence for the Sprint/TB2 record, not proof that
Sprint 3 Mobile execution is complete. It does not demonstrate a Mobile client,
physical-device behavior, distribution, Product Acceptance, final validation
video or production readiness. The expanded local integration gate remains
`PARTIAL` with the three documented `TenantAdministrationIT` failures; the
focused Mobile V1/API contract run remains recorded separately in the
[implementation evidence register](../../../../../delivery-checklists/implementation-evidence-register.md).

## Sprint 3 status

`OPEN — contextual Sprint 3 execution evidence, Mobile runtime evidence and
human review remain pending.`
