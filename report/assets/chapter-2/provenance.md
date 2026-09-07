# Chapter 2 DDD and architecture evidence provenance

## Scope and reading rule

This register covers the strategic DDD, C4 and tactical DDD material included
in Chapter 2. `TARGET` describes the accepted construction model; `AS-IS`
describes implementation evidence; `FUTURE` and `OPEN` remain outside the
implemented baseline. A copied or rendered diagram is not evidence that a
workshop, runtime, Product Acceptance or implementation review occurred.

Canonical authority is the Nexa Blueprint. Current implementation repositories
are used only for an AS-IS crosswalk. Operations Mobile and Buyer Mobile are
TARGET product projections/containers; neither is a Bounded Context.

## Authority manifest

| Evidence | Scope | Provenance and integrity | Classification |
| :--- | :--- | :--- | :--- |
| Final Project Statement V4.0 | Academic structure and rubric | Owner-provided attachment; SHA-256 `38be0c1baa77d0601c9605ef9ea72ad2fb510222a17a65944a06690621169f37`; attachment is not committed here | Normative input |
| Nexa Blueprint | Product, strategic DDD, architecture and data decisions | Git `origin/main` at `fce3ba6f8ca1622084a2114424086364e1f7d93f`; local canonical checkout also contains an unrelated untracked logo, excluded from this evidence set | Canonical authority |
| API repository | Existing Java/Spring implementation crosswalk | Git `origin/main` at `380e2427bc3883f23fbd7e9a82d452888f2074a8`; no target parity inferred from package names | AS-IS only |
| `nexa-ddd` visual set | External DDD process material | Local directory has no Git metadata and no embedded date/author provenance; nine SVGs observed 2026-09-06 and hashed below | External evidence, review pending |

## C4 Structurizr source and export

| Artifact | Source path | SHA-256 | State |
| :--- | :--- | :--- | :--- |
| Semantic source | `blueprint/01-shared/architecture/c4/structurizr/workspace.dsl` | `663a28e13d31b127a0a601c7f3bc9799e56634fb9edb0eded778bb0fd7fff3b5` | TARGET source |
| Generated JSON | `blueprint/01-shared/architecture/c4/structurizr/generated/workspace.json` | `a7a51c5367494747135632d1b60254e7c2c375ab8a5b535d813f88bafb849041` | Generated source |
| Manual JSON mirror | `blueprint/01-shared/architecture/c4/structurizr/workspace.json` | `a7a51c5367494747135632d1b60254e7c2c375ab8a5b535d813f88bafb849041` | Byte-identical mirror |

Selected exports were copied byte-for-byte from
`blueprint/01-shared/architecture/c4/exports/`; export timestamp observed in
the canonical checkout is `2026-08-30T18:28:57-0500`. The report retains both
SVG and PNG. PNG is used by the PDF path; SVG is retained for inspection.

| Report asset | Canonical export family | SVG SHA-256 |
| :--- | :--- | :--- |
| `c4/Nexa-SystemContext-V1-TARGET.svg` | L1 V1 TARGET | `6c23996f761e88f697135801ff0fd3a0617db406f6283dd3beb90cbafd416d64` |
| `c4/Nexa-Containers-V1-TARGET.svg` | L2 V1 TARGET | `f0d0e6352dc6fd340836a55c0aca9f036ea43118309d5ec9b55b58bf0ef0425b` |
| `c4/Nexa-Operations-Mobile-TARGET.svg` | L3 Operations Mobile V1 TARGET | `f0720ee3dee4da03e05aeeffcf01950f95af83f6d98583c14663ea906e6799dc` |
| `c4/Nexa-Buyer-Mobile-TARGET.svg` | L3 Buyer Mobile V1 TARGET | `65dc8df9f50eeac24e1b8e452144ee6fbc6a9e52c3f886b14e68475d7dcb007f` |
| `c4/Nexa-Deployment-V1-TARGET.svg` | V1 TARGET deployment | `594a26041b38446b9e91a8e73e3e45c879131ce7cd1d47022541fc83a824e585` |
| `c4/Nexa-API-IdentityTenantCustomer-TARGET.svg` | L3 API identity/tenant/customer component family | `3d4700e3b969ee266cbe5df2fdd8558be05ada4691dc6e545a7dd818023477e0` |
| `c4/Nexa-API-CommercialInventory-TARGET.svg` | L3 API commercial/inventory component family | `7c8429ef2a0a3d64d987232fc0ade451c45e0ee87e5ae83de2240f654df2ea45` |
| `c4/Nexa-API-FulfillmentDelivery-TARGET.svg` | L3 API fulfillment/delivery component family | `4713d941c5160e346e7aece5d56add67e076f314584ce3f05e721119c411e693` |
| `c4/Nexa-API-CreditPaymentDocuments-TARGET.svg` | L3 API credit/payment/documents component family | `f90c9ccf26726cf07bf5b2a31ce1ec48762bfb55fe83fd0f7d94eb24b933f038` |

The selected views are semantic exports from the Structurizr source. Cached
`.structurizr` thumbnails are intentionally not used because their labels and
timestamps do not form the current export set. The C4 model contains one Nexa
system. A C4 container is not a Bounded Context; PostgreSQL is physically
shared with logical ownership by context.

## Tactical DDD source set

For each exact BC-01..BC-11, the report includes a copied PlantUML domain
source and database-diagram source under `tactical/BC-XX/`. Sources were copied
from the matching Blueprint bounded-context directory at Blueprint
`origin/main` `fce3ba6f8ca1622084a2114424086364e1f7d93f`. Rendered SVG and PNG
were regenerated locally with PlantUML after copying. The database diagrams
are projections of the shared PostgreSQL target; they do not imply one physical
database or schema per BC. The canonical SQL files remain the database source
authority in Blueprint.

| Report source family | Count | Canonical source |
| :--- | ---: | :--- |
| Tactical domain PlantUML | 11 | `01-shared/domain/bounded-contexts/BC-XX-*/diagrams/domain-model.puml` |
| Tactical database PlantUML | 11 | `01-shared/domain/bounded-contexts/BC-XX-*/data/database-diagram.puml` |
| Local regenerated renders | 22 SVG + 22 PNG | PlantUML 1.2026.5, Java 26.0.1 observed 2026-09-06 |

## External `nexa-ddd` visual set

The visual mapping and inspection notes are in
[DDD process evidence](../../02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.0-ddd-process-evidence.md).
Original SVG hashes:

| Original image | Observed SHA-256 | Provenance |
| :--- | :--- | :--- |
| `step1-ddd.svg` | `0cf1aa86d22f479e06b48edfd025448fa2db70ef6cf83142455717d852078ff6` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step2-ddd.svg` | `b21560183ba3f4ecd6a5868e5fdd8a9a6e2ba58b2dbe92b0be7d6ad980fab058` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step3-ddd.svg` | `a1bd86f5b9f1cf73ff43c7a7316912c3f4774e3cf57a7ea243235911d3e2d3e5` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step4-ddd.svg` | `8f1c302ec234c88b9cc9b750caff88eee5c9b98a9e454ed1d730ac0963aaa782` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step5-ddd.svg` | `a9536b18acf3a208b7e934c0fbedcf0aac97d5fb407fdb3b21dca7131b2d6a90` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step6-ddd.svg` | `3abfe44f687050d840dc64ab92f5e1ee3ab64cde1a18cd0de40420605b502e59` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step7-ddd.svg` | `b03bccf0e9fcc7130b7d7f6668ad4fac848a7c6f036eca9c3bd8801e44b1babe` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step8-ddd.svg` | — | Not present in source directory; no substitute invented |
| `step9-ddd.svg` | `116631ba32f55e78a9af3b9dc2345e35b35dd4512c6b6db501a404437aae9d4a` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step10-ddd.svg` | `17230d2e03be50a05d7edd103477d4802032d85197eb3b107c0b447a267e5072` | `nexa-ddd`; no Git SHA/date/author embedded |

The `step6` artwork visibly contains a truncated personal name. It is not used
as authorship or participant evidence. The images support visual discussion of
the target model; they do not close the missing workshop, participant, date,
tool, acceptance or implementation gates.

## Reproduction commands

Run from the report worktree:

```sh
git status --short
shasum -a 256 report/assets/chapter-2/ddd-process/*.svg
shasum -a 256 report/assets/chapter-2/c4/*.svg
plantuml --check-syntax report/assets/chapter-2/tactical/BC-*/domain-model.puml report/assets/chapter-2/tactical/BC-*/database-diagram.puml
```

The canonical semantic source, generated JSON, SQL and tactical models remain
outside this derivative report. Any later source change requires a new hash and
fresh exports.
