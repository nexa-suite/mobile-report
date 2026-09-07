# Handoff diff ownership matrix

## Purpose

This matrix captures the 158-path diff observed during the verified handoff
before reconciliation. It is retained as path-level ownership provenance and
is not a list of current uncommitted paths, authorship approval or commit
authorization.

| Field | Value |
| :--- | :--- |
| Snapshot | Handoff snapshot 2026-09-02; branch `reconcile/report-integration-20260902` |
| Base | `3edeb196800a72a30299987a661e791c8f8fb50d` (historical handoff comparison base) |
| Recovery copy | `/tmp/nexa-mobile-report-resume.PJofE0/` |
| Staging | 94 exact paths prepared; branch published; commit and PR pending the Verified signature gate |
| Current worktree | Follow-up research, requirements and architecture evidence are listed under the owning units; every new unit requires its own signed Battle commit |
| Commit rule | One coherent unit; no `Co-authored-by`; published history remains immutable and new attribution follows the owner-confirmed identity register |

## Unit A — Report governance / front matter

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín / `JoaquinBV511` | Team review | `docs(rubric): reconcile academic report baseline` |

- Canonical / academic sources: Prompt canónico; Final Project Statement V4.0; rúbrica de front matter, entrega y control de participación.
- Rubric requirement: Front matter, README, versiones, colaboración, milestones, annexes y gates documentales.
- Story IDs affected: Cross-cutting; no story approval.
- Owner must explain: Qué cambió, por qué la estructura sigue V4.0, qué evidencia está comprobada y qué permanece pendiente.
- Status: `CURRENT INTEGRATION APPROVED — JOAQUÍN AUTHORIZED`.

Exact files:

- `README.md`
- `report/01-presentation/chapter-overview.md`
- `delivery-checklists/av1.md`
- `delivery-checklists/av2.md`
- `delivery-checklists/blueprint-reconciliation.md`
- `delivery-checklists/file-naming.md`
- `delivery-checklists/human-commit-gate.md`
- `delivery-checklists/current-diff-ownership-matrix.md`
- `delivery-checklists/live-baseline.md`
- `delivery-checklists/source-manifest.md`
- `delivery-checklists/rubric-gap-matrix.md`
- `delivery-checklists/rubric-status.md`
- `delivery-checklists/team-identity-register.md`
- `delivery-checklists/conflict-reconciliation-ledger.md`
- `delivery-checklists/professor-clarification-register.md`
- `delivery-checklists/wave-4-professor-grade-audit.md`
- `report/assets/chapter-1/.gitkeep`
- `report/01-presentation/1.1-startup-profile/1.1.1-startup-description.md`
- `report/01-presentation/1.2-solution-profile/1.2.1-background-and-problem.md`
- `report/01-presentation/1.2-solution-profile/1.2.2-lean-ux-process/1.2.2.1-problem-statements.md`
- `report/01-presentation/1.2-solution-profile/1.2.2-lean-ux-process/1.2.2.2-assumptions.md`
- `report/01-presentation/1.2-solution-profile/1.2.2-lean-ux-process/1.2.2.3-hypothesis-statements.md`
- `report/01-presentation/1.1-startup-profile/1.1.2-team-member-profiles.md`
- `report/assets/chapter-1/startup-profile/sebastian-pinedo-sanchez.png`
- `report/01-presentation/1.2-solution-profile/1.2.2-lean-ux-process/1.2.2.4-lean-ux-canvas.md`
- `report/00-front-matter/00-cover.md`
- `report/00-front-matter/01-version-history.md`
- `report/00-front-matter/02-project-report-collaboration-insights.md`
- `report/00-front-matter/03-contents.md`
- `report/00-front-matter/04-student-outcome.md`
- `report/00-front-matter/05-smart-objectives.md`
- `report/90-conclusions/conclusions-and-recommendations.md`
- `report/91-glossary/glossary.md`
- `report/93-annexes/annex-a-student-outcome/student-outcome-7.md`
- `report/93-annexes/annex-b-participant-performance-report/participant-performance-report.md`
- `report/93-annexes/annex-c-video-guidelines/video-guidelines.md`
- `report/93-annexes/annex-d-spike-story/spike-story.md`
- `report/93-annexes/annex-e-ux-heuristics-evaluation/ux-heuristics-evaluation.md`
- `report/93-annexes/annex-f-translation-and-terms/translation-and-terms.md`
- `report/93-annexes/annex-g-bibliographic-categories/business-domain.md`
- `report/93-annexes/annex-g-bibliographic-categories/general-considerations.md`
- `report/93-annexes/annex-g-bibliographic-categories/languages-frameworks-and-tools.md`
- `report/93-annexes/annex-g-bibliographic-categories/software-engineering-methods-and-techniques.md`
- `report/93-annexes/annexes-overview.md`
- `report/assets/annexes/.gitkeep`
- `report/assets/asset-index.md`
- `report/assets/front-matter/.gitkeep`
- `report/assets/front-matter/upc-logo.png`

## Unit B — Research / Needfinding

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín / `JoaquinBV511` | Diego; team review | `docs(research): reconcile mobile needfinding evidence` |

- Canonical / academic sources: Prompt canónico; historical reuse ledger; fuentes de investigación registradas.
- Rubric requirement: §2.1–§2.3, entrevistas, Needfinding, segmentación, bibliografía y Anexo A/B.
- Story IDs affected: Research support for all V1; no story approval.
- Owner must explain: Qué evidencia es histórica, reusable, adaptada o pendiente; por qué S2 requiere investigación nueva.
- Status: `CURRENT INTEGRATION APPROVED — JOAQUÍN AUTHORIZED`; the new Annex A
  register and terminology/provenance correction are owned by Sebastián's
  signed follow-up unit.

Exact files:

- `report/01-presentation/1.3-target-segments/target-segments.md`
- `report/assets/chapter-2/.gitkeep`
- `report/02-requirements-and-software-solution-design/2.2-interviews/2.2.1-interview-design.md`
- `report/02-requirements-and-software-solution-design/2.2-interviews/2.2.2-interview-records.md`
- `report/02-requirements-and-software-solution-design/2.2-interviews/2.2.3-interview-analysis.md`
- `report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.5-big-picture-eventstorming.md`
- `report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.1-user-personas.md`
- `report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.6-ubiquitous-language.md`
- `delivery-checklists/historical-interview-reuse-ledger.md`
- `report/93-annexes/annex-a-student-outcome/historical-interview-evidence-register.md`
- `report/02-requirements-and-software-solution-design/2.2-interviews/2.2.4-physical-operations-and-delivery-research-plan.md`
- `report/02-requirements-and-software-solution-design/2.2-interviews/2.2.5-secondary-research-physical-operations-and-delivery.md`
- `report/02-requirements-and-software-solution-design/2.1-competitors/2.1.1-competitive-analysis.md`
- `report/02-requirements-and-software-solution-design/2.3-needfinding/2.3.2-user-task-matrix.md`
- `report/02-requirements-and-software-solution-design/2.1-competitors/2.1.2-competitor-strategies-and-tactics.md`
- `report/92-bibliography/bibliography.md`
- `report/02-requirements-and-software-solution-design/2.2-interviews/section-overview.md`
- `report/93-annexes/annex-a-student-outcome/historical-interviews/celia-perez.jpeg`
- `report/93-annexes/annex-a-student-outcome/historical-interviews/lorena-silva.jpeg`
- `report/93-annexes/annex-a-student-outcome/historical-interviews/pedro-puente.jpeg`
- `report/93-annexes/annex-f-translation-and-terms/historical-evidence-provenance.md`

## Unit C — V1 requirements / backlog

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín / `JoaquinBV511` | Diego; team review | `docs(requirements): align mobile v1 academic backlog` |

- Canonical / academic sources: Blueprint Mobile V1 projection; prompt canónico; rúbrica §2.4.
- Rubric requirement: 73 User Stories, 256 source scenarios plus 3 faithfully reconciled Gherkin scenarios for MOB-US-073, Acceptance Criteria, Impact Mapping y Product Backlog; V1 remains 28 stories.
- Story IDs affected: MOB-US-001, 002, 003, 011–017, 019–034, 044, 047–049.
- Owner must explain: Cada historia completa, sus criterios Gherkin (cuatro escenarios en las historias fuente y tres escenarios reconciliados en MOB-US-073), prioridad, Epic, BC, Sprint, dependencias y límite de evidencia.
- Status: `CURRENT INTEGRATION APPROVED — JOAQUÍN AUTHORIZED`; the rubric
  structure validator and register are owned by Gino's signed follow-up unit.

Exact files:

- `report/02-requirements-and-software-solution-design/2.4-requirements-specification/section-overview.md`
- `report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.0-to-be-scenario-mapping.md`
- `report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md`
- `report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.2-impact-mapping.md`
- `report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.3-product-backlog.md`
- `delivery-checklists/mobile-v1-story-verification-register.md`
- `delivery-checklists/mobile-v1-rubric-structure-register.md`
- `report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.4-technical-stories.md`

## Unit D — Strategic DDD

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín / `JoaquinBV511` | Sebastián; Diego | `docs(ddd): reconcile strategic domain model` |

- Canonical / academic sources: Current Blueprint strategic model; prompt canónico; rúbrica §2.5.
- Rubric requirement: EventStorming, UL, candidate contexts, Context Map y Strategic DDD.
- Story IDs affected: All V1 through domain traceability; no implementation claim.
- Owner must explain: Por qué existen exactamente 11 BC, sus relaciones, autoridad de dominio y separación AS-IS/TARGET.
- Status: `CURRENT INTEGRATION APPROVED — JOAQUÍN AUTHORIZED`.

Exact files:

- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/section-overview.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.1-candidate-context-discovery.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.2-domain-message-flows-modeling.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.3-bounded-context-canvases.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.2-context-mapping.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/section-overview.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.4-strategic-ddd-traceability.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.0-ddd-process-evidence.md`
- `report/assets/chapter-2/ddd-process/step1-ddd.png`
- `report/assets/chapter-2/ddd-process/step1-ddd.svg`
- `report/assets/chapter-2/ddd-process/step10-ddd.png`
- `report/assets/chapter-2/ddd-process/step10-ddd.svg`
- `report/assets/chapter-2/ddd-process/step2-ddd.png`
- `report/assets/chapter-2/ddd-process/step2-ddd.svg`
- `report/assets/chapter-2/ddd-process/step3-ddd.png`
- `report/assets/chapter-2/ddd-process/step3-ddd.svg`
- `report/assets/chapter-2/ddd-process/step4-ddd.png`
- `report/assets/chapter-2/ddd-process/step4-ddd.svg`
- `report/assets/chapter-2/ddd-process/step5-ddd.png`
- `report/assets/chapter-2/ddd-process/step5-ddd.svg`
- `report/assets/chapter-2/ddd-process/step6-ddd.png`
- `report/assets/chapter-2/ddd-process/step6-ddd.svg`
- `report/assets/chapter-2/ddd-process/step7-ddd.png`
- `report/assets/chapter-2/ddd-process/step7-ddd.svg`
- `report/assets/chapter-2/ddd-process/step9-ddd.png`
- `report/assets/chapter-2/ddd-process/step9-ddd.svg`

## Unit E — C4 / Structurizr / system architecture

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Diego / `DiegoS284` | Gino; Gerard | `docs(architecture): synchronize canonical c4 evidence` |

- Canonical / academic sources: Blueprint C4/Structurizr source and observed exports; prompt canónico; rúbrica arquitectura.
- Rubric requirement: Context, container, component y deployment diagrams; system boundary; AS-IS/TARGET.
- Story IDs affected: All V1 where architecture evidence is cited.
- Owner must explain: Diferencia entre System, containers y BC; procedencia, versión, validación y límites de cada diagrama.
- Status: `CURRENT INTEGRATION APPROVED — DIEGO AUTHORIZED`; Gerard owns the
  Mobile runtime-boundary register as a separate signed architecture unit.

Exact files:

- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/2.5.3.1-context-level-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/2.5.3.2-container-level-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/2.5.3.3-component-level-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/2.5.3.4-deployment-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.3-software-architecture/section-overview.md`
- `delivery-checklists/architecture-render-evidence-register.md`
- `delivery-checklists/architecture-authority-and-boundary-register.md`
- `delivery-checklists/mobile-architecture-evidence-register.md`
- `report/assets/chapter-2/c4/Nexa-API-CommercialInventory-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-API-CommercialInventory-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-API-CreditPaymentDocuments-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-API-CreditPaymentDocuments-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-API-FulfillmentDelivery-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-API-FulfillmentDelivery-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-API-IdentityTenantCustomer-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-API-IdentityTenantCustomer-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-Buyer-Mobile-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-Buyer-Mobile-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-Containers-V1-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-Containers-V1-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-Deployment-V1-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-Deployment-V1-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-Operations-Mobile-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-Operations-Mobile-TARGET.svg`
- `report/assets/chapter-2/c4/Nexa-SystemContext-V1-TARGET.png`
- `report/assets/chapter-2/c4/Nexa-SystemContext-V1-TARGET.svg`

## Unit F — Tactical DDD / UML / database

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín / `JoaquinBV511` for target report artifacts; Diego / `DiegoS284` for observed persistence evidence | Team review | `docs(ddd): reconcile tactical domain and data models` / `docs(implementation): document verified persistence evidence` |

- Canonical / academic sources: Blueprint tactical/data sources; API source and read-only persistence inspection; prompt canónico; rúbrica §2.6.
- Rubric requirement: Domain/Application/Interface/Infrastructure layers, class diagrams, component diagrams y database design.
- Story IDs affected: All V1 where BC, data or persistence boundary is cited.
- Owner must explain: Qué es modelo TARGET, qué fue observado en API/PostgreSQL y qué no se debe presentar como implementación.
- Status: `CURRENT INTEGRATION APPROVED — SPLIT JOAQUÍN/DIEGO BY PATH`; Gino
  remains candidate for a future Tactical DDD/UML/DB review.

Exact files:

- `delivery-checklists/api-persistence-evidence-register.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/section-overview.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/2.6.1-bounded-context-coverage.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/code-level-diagrams/code-level-overview.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/code-level-diagrams/2.6.x.6.1-domain-layer-class-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/code-level-diagrams/2.6.x.6.2-database-design-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/context-overview.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/application-layer.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/component-level-diagrams.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/domain-layer.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/infrastructure-layer.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-context-template/interface-layer.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-01-tenant-access-governance.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-02-customer-buyer-relationships.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-03-catalog-commercial-policy.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-04-sales-commitment.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-05-inventory-availability.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-06-fulfillment-delivery.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-07-credit-receivables.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-08-payments.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-09-business-documents.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-10-notifications.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/BC-11-business-traceability.md`
- `report/02-requirements-and-software-solution-design/2.6-tactical-level-domain-driven-design/bounded-contexts/README.md`
- `report/assets/chapter-2/provenance.md`
- `report/assets/chapter-2/tactical/BC-01/BC01_TenantAccessGovernance.png`
- `report/assets/chapter-2/tactical/BC-01/BC01_TenantAccessGovernance.svg`
- `report/assets/chapter-2/tactical/BC-01/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-01/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-01/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-01/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-02/BC02_CustomerBuyerRelationships.png`
- `report/assets/chapter-2/tactical/BC-02/BC02_CustomerBuyerRelationships.svg`
- `report/assets/chapter-2/tactical/BC-02/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-02/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-02/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-02/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-03/BC03_CatalogCommercialPolicy.png`
- `report/assets/chapter-2/tactical/BC-03/BC03_CatalogCommercialPolicy.svg`
- `report/assets/chapter-2/tactical/BC-03/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-03/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-03/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-03/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-04/BC04_SalesCommitment.png`
- `report/assets/chapter-2/tactical/BC-04/BC04_SalesCommitment.svg`
- `report/assets/chapter-2/tactical/BC-04/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-04/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-04/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-04/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-05/BC05_InventoryAvailability.png`
- `report/assets/chapter-2/tactical/BC-05/BC05_InventoryAvailability.svg`
- `report/assets/chapter-2/tactical/BC-05/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-05/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-05/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-05/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-06/BC06_FulfillmentDelivery.png`
- `report/assets/chapter-2/tactical/BC-06/BC06_FulfillmentDelivery.svg`
- `report/assets/chapter-2/tactical/BC-06/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-06/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-06/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-06/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-07/BC07_CreditReceivables.png`
- `report/assets/chapter-2/tactical/BC-07/BC07_CreditReceivables.svg`
- `report/assets/chapter-2/tactical/BC-07/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-07/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-07/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-07/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-08/BC08_Payments.png`
- `report/assets/chapter-2/tactical/BC-08/BC08_Payments.svg`
- `report/assets/chapter-2/tactical/BC-08/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-08/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-08/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-08/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-09/BC09_BusinessDocuments.png`
- `report/assets/chapter-2/tactical/BC-09/BC09_BusinessDocuments.svg`
- `report/assets/chapter-2/tactical/BC-09/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-09/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-09/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-09/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-10/BC10_Notifications.png`
- `report/assets/chapter-2/tactical/BC-10/BC10_Notifications.svg`
- `report/assets/chapter-2/tactical/BC-10/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-10/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-10/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-10/domain-model.puml`
- `report/assets/chapter-2/tactical/BC-11/BC11_BusinessTraceability.png`
- `report/assets/chapter-2/tactical/BC-11/BC11_BusinessTraceability.svg`
- `report/assets/chapter-2/tactical/BC-11/database-diagram.png`
- `report/assets/chapter-2/tactical/BC-11/database-diagram.puml`
- `report/assets/chapter-2/tactical/BC-11/database-diagram.svg`
- `report/assets/chapter-2/tactical/BC-11/domain-model.puml`

## Unit G — Mobile UX / i18n / accessibility

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín / `JoaquinBV511` | Diego; team review | `docs(ux): prepare mobile experience evidence` |

- Canonical / academic sources: Current Design Lab evidence; Blueprint Mobile scope; prompt canónico; rúbrica Chapter III.
- Rubric requirement: Style Guidelines, IA, Mobile wireframes, wireflows, mock-ups, user flows, prototype, i18n y accessibility.
- Story IDs affected: All V1 target UX; no runtime or acceptance claim.
- Owner must explain: Estados felices/no felices, touch/accessibility, i18n, límites de Design Lab y evidencia aún no renderizada.
- Status: `CURRENT INTEGRATION APPROVED — JOAQUÍN AUTHORIZED`; Gerard remains
  candidate for a future Mobile UX evidence workstream after personal review.

Exact files:

- `report/03-solution-ui-ux-design/3.1-product-design/3.1.1-style-guidelines/3.1.1.1-general-style-guidelines.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.1-style-guidelines/section-overview.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/3.1.2.1-organization-systems.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/3.1.2.2-labeling-systems.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/3.1.2.3-seo-and-meta-tags.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/3.1.2.4-searching-systems.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/3.1.2.5-navigation-systems.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.2-information-architecture/section-overview.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.3-landing-page-ui-design/3.1.3.1-landing-page-wireframes.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.3-landing-page-ui-design/3.1.3.2-landing-page-mockups.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.3-landing-page-ui-design/section-overview.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/3.1.4.1-mobile-application-wireframes.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/3.1.4.2-mobile-application-wireflows.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/3.1.4.3-mobile-application-mockups.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/3.1.4.4-mobile-application-user-flows.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/3.1.4.5-mobile-application-prototyping.md`
- `report/03-solution-ui-ux-design/3.1-product-design/3.1.4-mobile-applications-ux-ui-design/section-overview.md`
- `report/03-solution-ui-ux-design/3.1-product-design/section-overview.md`
- `report/03-solution-ui-ux-design/chapter-overview.md`
- `report/assets/chapter-3/.gitkeep`

## Unit H — SCM / sprint / implementation evidence

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Split by actual path: Joaquín for academic/sprint report; Diego for API/implementation evidence | Team review | `docs(sprint): add reproducible sprint evidence gates` / `docs(implementation): document verified mobile api evidence` |

- Canonical / academic sources: Current API/Mobile repositories, prompt canónico, Final Project Statement V4.0, rúbrica Chapter IV.
- Rubric requirement: SCM, S1/S2/S3, services/OpenAPI, tests, deployment, runtime, validation y collaboration.
- Story IDs affected: Sprint mappings for all V1; no execution claim from templates.
- Owner must explain: Qué evidencia técnica existe, qué falta para Mobile/device/production y qué commits/URLs/captures son reales.
- Status: `CURRENT INTEGRATION APPROVED — SPLIT JOAQUÍN/DIEGO BY PATH`.

Exact files:

- `delivery-checklists/implementation-evidence-register.md`
- `delivery-checklists/mobile-v1-api-contract-register.md`
- `delivery-checklists/tb1.md`
- `delivery-checklists/tb2.md`
- `report/assets/chapter-4/.gitkeep`
- `report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.1-development-environment-configuration.md`
- `report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.2-source-code-management.md`
- `report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.3-style-guide-and-coding-conventions.md`
- `report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.4-software-deployment-configuration.md`
- `report/04-product-implementation-and-validation/4.1-software-configuration-management/section-overview.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/section-overview.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/aspect-leaders-and-collaborators.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/development-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/execution-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/services-documentation-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/software-deployment-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/sprint-backlog.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/sprint-overview.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/sprint-planning.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/team-collaboration-insights.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-1/testing-suite-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/aspect-leaders-and-collaborators.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/development-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/execution-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/services-documentation-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/software-deployment-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/sprint-backlog.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/sprint-overview.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/sprint-planning.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/team-collaboration-insights.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-2/testing-suite-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/aspect-leaders-and-collaborators.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/development-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/execution-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/services-documentation-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/software-deployment-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/sprint-backlog.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/sprint-overview.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/sprint-planning.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/team-collaboration-insights.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/sprint-3/testing-suite-evidence.md`
- `report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/section-overview.md`
- `report/04-product-implementation-and-validation/4.3-validation-interviews/4.3.1-interview-design.md`
- `report/04-product-implementation-and-validation/4.3-validation-interviews/4.3.2-interview-records.md`
- `report/04-product-implementation-and-validation/4.3-validation-interviews/4.3.3-heuristic-evaluations.md`
- `report/04-product-implementation-and-validation/4.3-validation-interviews/section-overview.md`
- `report/04-product-implementation-and-validation/chapter-overview.md`
- `report/04-product-implementation-and-validation/supplementary-sections/video-about-the-product.md`
- `report/04-product-implementation-and-validation/supplementary-sections/video-about-the-team.md`
- `report/04-product-implementation-and-validation/supplementary-sections/video-app-validation.md`

## Unit I — Report validation tooling

| Owner | Reviewers | Candidate |
| :--- | :--- | :--- |
| Joaquín for report validators and export pipeline; Diego for technical validators | Team review | `docs(report): complete academic reconciliation and rubric alignment` |

- Canonical / academic sources: Report structure and canonical source fingerprints; prompt canónico; rubric validation gates.
- Rubric requirement: Reproducible Markdown, link, structure, transcription and contract checks.
- Story IDs affected: No direct story ownership; validators cover V1 projection.
- Owner must explain: Cobertura, límites y resultados exactos de cada script; ausencia de atribución interna en contenido académico.
- Status: `TECHNICAL VALIDATION PASSED — VERIFIED COMMIT GATE PENDING`.

Exact files:

- `scripts/check-report-links.sh`
- `scripts/inspect-api-persistence.sh`
- `scripts/verify-canonical-sources.sh`
- `scripts/verify-mobile-v1-api-register.py`
- `scripts/verify-mobile-v1-review-register.py`
- `scripts/verify-mobile-v1-transcription.py`
- `scripts/generate-mobile-backlog-report.py`
- `scripts/verify-mobile-backlog.py`
- `scripts/verify-diff-ownership-matrix.py`
- `scripts/verify-bibliography-citations.py`
- `scripts/verify-report-structure.sh`
- `scripts/verify-mobile-v1-rubric-template.py`
- `scripts/verify-mobile-v1-semantics.py`
- `scripts/export-report-pdf.sh`
- `scripts/report-pdf-filter.lua`
- `delivery-checklists/report-export.md`
- `.markdownlint-cli2.jsonc`
- `.gitignore`

## Unassigned paths

None. Every path in the pre-reconciliation handoff inventory and each new
follow-up artifact is assigned to one review unit.

## Review rule

Review each unit's exact files and diff before staging. The joint 2026-09-02
review authorizes the original integration; the follow-up units are separately
signed and validated by their owner. Split mixed ownership by path or stop. No
historical commit is amended to make the new balance appear retroactive.
