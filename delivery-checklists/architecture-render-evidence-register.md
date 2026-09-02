# Architecture and diagram evidence register

## Evidence boundary

This register records versioned architecture and data-diagram sources observed
in the local Blueprint repository at the current report cut. A source file or
export proves provenance and availability; it does not prove that the report
team selected it, that a reviewer inspected its readability, that the Mobile
client is implemented, or that the product was accepted.

| Field | Observed value |
| :--- | :--- |
| Blueprint repository | `/Users/joaquinfranciscoverdebueno/Developer/nexa-suite/blueprint` |
| Branch / commit | `main` / `fce3ba6f8ca1622084a2114424086364e1f7d93f` |
| Working tree | Clean at inspection |
| Structurizr image | `structurizr/structurizr:2026.06.28` |
| Structurizr source review | `docker run ... validate ... workspace.dsl` — exit code `0` on 2026-09-01 |
| Academic state | `SOURCE/EXPORT OBSERVED; HUMAN VISUAL REVIEW AND REPORT SELECTION PENDING` |

## C4 source and export inventory

The semantic source is the Structurizr DSL. SVG/PNG files are versioned visual
exports and are not an alternative semantic source.

| View | Versioned source | Observed exports | Interpretation |
| :--- | :--- | :--- | :--- |
| System context | `01-shared/architecture/c4/structurizr/l1/l1.dsl` plus included `model/*.dsl` | `exports/l1/Nexa-SystemContext-ASIS.*`, `Nexa-SystemContext-V1-TARGET.*`, `Nexa-SystemContext-Future-Runway.*` | AS-IS, V1 TARGET and future runway are distinct; Mobile remains target/runway evidence |
| Containers | `01-shared/architecture/c4/structurizr/l2/l2.dsl` plus included `model/*.dsl` | `exports/l2/Nexa-Containers-ASIS.*`, `Nexa-Containers-V1-TARGET.*` | AS-IS and V1 TARGET are distinct; TARGET does not prove deployment |
| Mobile/API/Frontend components | `01-shared/architecture/c4/structurizr/l3/operations-mobile.dsl`, `buyer-mobile.dsl`, `api.dsl`, `platform.dsl`, `portal.dsl`, `website.dsl` | Corresponding `exports/l3/*.svg` and `*.png`, including `Nexa-Operations-Mobile-TARGET.*` and `Nexa-Buyer-Mobile-TARGET.*` | Mobile views are target projections; implementation and runtime remain open |
| Deployment | `01-shared/architecture/c4/structurizr/deployment/deployment.dsl` plus included deployment model | `exports/deployment/Nexa-Deployment-Local-ASIS.*`, `Nexa-Deployment-V1-TARGET.*` | Topology source/export observed; executed runtime and cloud operation need separate evidence |

The workspace entry point is
`01-shared/architecture/c4/structurizr/workspace.dsl`; generated JSON is
derived output and must not be edited by hand. Blueprint documents the pinned
renderer and the expected view names in its Structurizr README.

## Tactical and database diagram inventory

The following versioned files were observed for each of `BC-01` through
`BC-11`:

| Artifact family | Source pattern | Export pattern | Academic interpretation |
| :--- | :--- | :--- | :--- |
| Tactical domain model | `01-shared/domain/bounded-contexts/BC-*/diagrams/domain-model.puml` | `BC##_*.svg` and `BC##_*.png` in the same `diagrams/` directory | Target design source/export; selected context and reviewer still pending |
| Context database diagram | `01-shared/domain/bounded-contexts/BC-*/data/database-diagram.puml` | `database-diagram.svg` and `database-diagram.png` | Target data design source/export; ownership and readability review still pending |
| Master database diagram | `01-shared/data/master-target-relational-model.sql` | `master-database-diagram.puml`, `.svg`, `.png` | SQL is the stated source; PlantUML is a review projection, not a second schema definition |

The Blueprint master-data handoff explicitly requires grouping by the eleven
logical owners, marking scope/constraints and reviewing cross-context links.
That handoff is not replaced by the existence of generated files.

## Reproducible source fingerprints

These hashes identify representative source artifacts at the Blueprint commit
above. They are included to make later report copies and renders auditable.

| Source artifact | SHA-256 |
| :--- | :--- |
| `01-shared/architecture/c4/structurizr/workspace.dsl` | `663a28e13d31b127a0a601c7f3bc9799e56634fb9edb0eded778bb0fd7fff3b5` |
| `01-shared/architecture/c4/structurizr/l1/l1.dsl` | `3848f85afd2450bc3c5e870a9e1c8681d8bec2ffe0816f1f3091a496e2fcf36e` |
| `01-shared/architecture/c4/structurizr/l2/l2.dsl` | `d027071e57c99097d07573a01ae0ceb588d4f61a9dbf647e682ce6a89e156466` |
| `01-shared/architecture/c4/structurizr/l3/operations-mobile.dsl` | `ee979a6bab24c0d01783c58f408230e60bf660036381aa721ec0de130cf1ca13` |
| `01-shared/architecture/c4/structurizr/l3/buyer-mobile.dsl` | `9a3398f6baa03cb209988633117a7637af56575ab966540c5dbba91612fbc870` |
| `01-shared/architecture/c4/structurizr/deployment/deployment.dsl` | `8502d924c90cc013449cd6255d2060587e083062c9c25ee504ccd2d2787308c2` |
| `01-shared/data/master-target-relational-model.sql` | `32624afa2ce073fb4a613994a0bd6e2dd97a1d6e95a47a9781725638f7982d94` |
| `01-shared/domain/bounded-contexts/BC-06-fulfillment-delivery/diagrams/domain-model.puml` | `be21412d51d1ab0776122ccbb00adf768a13cd12004376f248eaac308ceba7cf` |
| `01-shared/domain/bounded-contexts/BC-06-fulfillment-delivery/data/database-diagram.puml` | `ffd5067f91fec3ebe5d491d56755eefd9fe0e5e57fa5ebdc8acde885c0e560ff` |

## Human closure checklist

- [ ] Architecture lead confirms the selected C4 views and explains AS-IS vs TARGET.
- [ ] Data/architecture owner confirms logical ownership for the eleven BCs and cross-context references.
- [ ] Report owner decides which source files/exports are copied or linked into the final academic repository.
- [ ] Human reviewer inspects legibility, labels, legend, source revision and export date.
- [ ] Any Mobile target diagram is presented as a design projection until client, device and acceptance evidence exist.
- [ ] Database source/import, master render and per-context renders are reviewed in the instructor-approved tool.

See [software architecture](../report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/section-overview.md), [tactical DDD coverage](../report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/2.6.1-bounded-context-coverage.md), [persistence evidence](./api-persistence-evidence-register.md) and the [rubric gap matrix](./rubric-gap-matrix.md).
