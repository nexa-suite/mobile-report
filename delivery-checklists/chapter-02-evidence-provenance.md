# Chapter 2 DDD and architecture evidence provenance

> Internal evidence register. This file is not part of the professor-facing report and must not be exported to the PDF.

## Scope and reading rule

This register covers the strategic DDD, C4 and tactical DDD material included
in Chapter 2. `TARGET` describes the accepted construction model; `AS-IS`
describes implementation evidence; `FUTURE` and `OPEN` remain outside the
implemented baseline. A copied or rendered diagram is not, by itself, evidence
of runtime, Product Acceptance or implementation review. The owner-provided
report input records that the nine-stage Miro EventStorming sequence was
performed collaboratively; the asset directory itself does not embed
participant, date or author metadata.

Canonical authority is the Nexa Blueprint. Current implementation repositories
are used only for an AS-IS crosswalk. Operations Mobile and Buyer Mobile are
TARGET product projections/containers; neither is a Bounded Context.

## Authority manifest

| Evidence | Scope | Provenance and integrity | Classification |
| :--- | :--- | :--- | :--- |
| Final Project Statement V4.0 | Academic structure and rubric | Owner-provided attachment; SHA-256 `38be0c1baa77d0601c9605ef9ea72ad2fb510222a17a65944a06690621169f37`; attachment is not committed here | Normative input |
| Nexa Blueprint | Product, strategic DDD, architecture and data decisions | Git `origin/main` at `fce3ba6f8ca1622084a2114424086364e1f7d93f`; local canonical checkout also contains an unrelated untracked logo, excluded from this evidence set | Canonical authority |
| API repository | Existing Java/Spring implementation crosswalk | Git `origin/main` at `380e2427bc3883f23fbd7e9a82d452888f2074a8`; no target parity inferred from package names | AS-IS only |
| `nexa-ddd` visual set | External DDD process material | Local directory has no Git metadata and no embedded date/author provenance; nine SVGs observed 2026-09-06 and hashed below | Workshop visual evidence; source metadata limited |

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

The visual mapping and inspection notes are integrated into the
[EventStorming section](../report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1-eventstorming.md),
[candidate-context analysis](../report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.1-candidate-context-discovery.md)
and [domain stories](../report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.2-domain-message-flows-modeling.md).
Original SVG hashes:

| Original image | Observed SHA-256 | Provenance |
| :--- | :--- | :--- |
| `step1-ddd.svg` | `452754afdb025fd31b81856fd164436a46e4d20d7f2b7463ed2d1b004145dcbc` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step2-ddd.svg` | `a297a385ae23f274f5836cb9685cb30d238cd6b8fb6aca1edc0ea76783130c1f` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step3-ddd.svg` | `e80e44bdded997dbc38f91622779aa24f49b9a4bcd49aa953fe3c489d78d6c10` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step4-ddd.svg` | `c6620d4b414142d4c4c09d628ffa828b17bd7c6ea7e39c340f260abc09ffbd` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step5-ddd.svg` | `06ceae65cfe103f168fc1731269bd6336913d537f6348378741190f6e3e9f4f4` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step6-ddd.svg` | `b64c9ce7f68d74ee25f07a5c3e91937a5f099dcb64b573d28b8900c2cb05ec94` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step7-ddd.svg` | `fcd1429ecedc48ce78878ee9e18610e42534e2f224ee015c4e0e39aa917fd695` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step9-ddd.svg` | `5b11da26d69497008cf06f2538149a3e2c8ff5773cc2c12cd3361bb6f6699720` | `nexa-ddd`; no Git SHA/date/author embedded |
| `step10-ddd.svg` | `0a67e056ece90cf77a293aa7d351d657b628f89ece45e1607d08823b8add373e` | `nexa-ddd`; no Git SHA/date/author embedded |

The `step6` artwork visibly contains a truncated personal name. It is not used
as authorship or participant evidence. The images support visual discussion of
the target model; they do not by themselves prove participant identity, formal
acceptance, implementation, runtime or production readiness.

## Chapter II visual closure artifacts

The nine real Miro assets are embedded in their professor-facing sections:
Steps 1–3 in 2.3.5 and Steps 4–7, 9 and 10 in 2.5.1. The report does not
reconstruct an additional board step.

Eleven existing Bounded Context Canvas artifacts are retained alongside the
accepted semantic source `2.5.1.3-bounded-context-canvases.md`. The source was
reworked into six-cell Markdown canvases; `scripts/render-chapter-2.5-canvases.py`
parses that structure and remains the deterministic refresh path. The generator
uses only Python standard-library SVG output. `rsvg-convert` 2.62.3 produced
deterministic PNG fallbacks for the PDF path. The SVG and PNG pairs are stored
under `report/assets/chapter-2/bounded-context-canvases/`.

The five Domain Story Mermaid blocks remain the editable source in
`2.5.1.2-domain-message-flows-modeling.md`. `mmdc` was unavailable in the
working environment and no Domain Story image was fabricated; this is recorded
as `BLOCKED — RENDER TOOLING` in the validator and final checkpoint.

## Reproduction commands

Run from the report worktree:

```sh
git status --short
shasum -a 256 report/assets/chapter-2/ddd-process/*.svg
shasum -a 256 report/assets/chapter-2/c4/*.svg
plantuml --check-syntax \
  report/assets/chapter-2/tactical/BC-*/domain-model.puml \
  report/assets/chapter-2/tactical/BC-*/database-diagram.puml
```

The canonical semantic source, generated JSON, SQL and tactical models remain
outside this derivative report. Any later source change requires a new hash and
fresh exports.
