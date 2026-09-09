# Sprint 01 Planning Support Artifact

**Plan status:** To Do
**Evidence status:** PENDING TEAM CONFIRMATION
**Purpose:** Planning support derived from the current Product Backlog. This is
not Chapter IV evidence and does not report Sprint execution.

## Planning table

| Field | Value |
| --- | --- |
| Sprint # | Sprint 1 |
| Sprint Planning Background | PENDING TEAM CONFIRMATION — initial Sprint candidate derived from the ordered Product Backlog, Lean UX hypotheses and Needfinding gaps. |
| Start Date | PENDING TEAM CONFIRMATION |
| End Date | PENDING TEAM CONFIRMATION |
| Location / modality | PENDING TEAM CONFIRMATION |
| Prepared By | PENDING TEAM CONFIRMATION |
| Attendees | PENDING TEAM CONFIRMATION |
| Previous Sprint Review Summary | Not available — initial Sprint. |
| Previous Sprint Retrospective Summary | Not available — initial Sprint. |
| Sprint Goal | See dedicated Sprint Goal below. |
| Sprint Goal & selected Stories | Candidate scope below; requires team confirmation before commitment. |
| Historical Velocity | Not available — initial Sprint. |
| Planned Story Points | 44 candidate points; planned, not historical velocity. |

## Sprint Goal

> Our focus is on a public first step and protected first Mobile slices for
> Operations and Buyer.
>
> We believe it delivers a coherent way to start a company conversation,
> re-enter authorized work, identify warehouse context and recognize a Buyer
> delivery that needs attention.
>
> This will be confirmed when the selected stories meet the Sprint Definition of
> Done, their Android/Kotlin and Flutter/Dart tracks preserve the required
> contract boundaries, and the team reviews the evidence.

## Candidate selected stories

| User Story Id | User Story Title | Story Points | Reason for selection |
| --- | --- | ---: | --- |
| LAND-US-001 | Comprender la propuesta B2B de Nexa | 2 | Public acquisition entry point. |
| LAND-US-005 | Iniciar el onboarding de una empresa | 3 | Starts a non-authoritative company conversation. |
| MOB-US-001 | Continuar el trabajo autorizado después de volver a Nexa | 2 | First protected context slice. |
| MOB-US-002 | Trabajar en la empresa y contexto de negocio previstos | 3 | Makes Tenant/Workspace context explicit. |
| MOB-US-003 | Ver sólo el trabajo permitido para el rol | 3 | Protects role-scoped work. |
| MOB-US-011 | Identificar un producto mediante el código del paquete o etiqueta | 3 | First Operations warehouse identification slice. |
| MOB-US-012 | Buscar manualmente un producto cuando no hay escaneo | 2 | Safe fallback for the same warehouse slice. |
| MOB-US-044 | Saber cuándo una entrega requiere atención | 3 | First Buyer attention slice. |
| MOB-US-047 | Verificar una entrega mediante el código de handoff | 3 | Buyer handoff context without overwriting Driver facts. |
| TS-MOB-001 | Integrar contratos REST con autoridad del servidor | 5 | Required authority boundary for both tracks. |
| TS-MOB-002 | Definir criterios de compatibilidad de plataforma | 5 | Establishes the Android/Kotlin track. |
| TS-MOB-003 | Preservar paridad de contratos entre proyecciones Mobile | 5 | Establishes the Flutter/Dart track and shared contracts. |
| SPIKE-002 | Establecer tracks Mobile y límites de contratos | 5 | Records setup evidence and contract boundaries for both tracks. |
| **Total** |  | **44** | Candidate scope; no commitment before team confirmation. |

## Aspect leaders and collaborators

L = Leader; C = Collaborator. These are Sprint responsibilities, not permanent
specializations. They preserve collaboration across both Mobile tracks.

| Team member | Product & Scrum Coordination | Android/Kotlin Mobile Track | Flutter/Dart Mobile Track | API/Contract Integration | UX/Needfinding Translation | Quality & Acceptance | Landing / Public Acquisition |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Pinedo Sanchez, Sebastián Martín | C | L | C | C | C | C | C |
| Rojas Mancilla, Gerard Gianpier | C | C | C | L | C | C | L |
| Torrejón De Los Santos, Gino Rodrigo | C | C | L | C | C | C | C |
| Verde Bueno, Joaquín Francisco | C | C | C | C | L | L | C |
| Yucra Sandoval, Diego Sebastián | L | C | C | C | C | C | C |

## Sprint Backlog 1 — Engineering Tasks

| Sprint # | User Story Id | User Story Title | Work-Item / Task Id | Task Title | Description | Estimation (Hours) | Assigned To | Status |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- |
| Sprint 1 | LAND-US-001 | Comprender la propuesta B2B de Nexa | SB1-T01 | Public value narrative | Prepare the public narrative and acceptance checks that distinguish Nexa from generic ecommerce and preserve cold-chain specialization as contextual. | 4 | Rojas Mancilla, Gerard Gianpier (Lead); Yucra Sandoval, Diego Sebastián (Collaborator) | To Do |
| Sprint 1 | LAND-US-005 | Iniciar el onboarding de una empresa | SB1-T02 | Non-authoritative onboarding request | Define and build the candidate request flow so it never creates Tenant or Workspace as an authoritative fact. | 5 | Pinedo Sanchez, Sebastián Martín (Lead); Rojas Mancilla, Gerard Gianpier (Collaborator) | To Do |
| Sprint 1 | MOB-US-001 | Continuar el trabajo autorizado después de volver a Nexa | SB1-T03 | Authorized re-entry state | Implement the candidate re-entry state and explicit non-confirmed/error states for authorized Mobile work. | 5 | Torrejón De Los Santos, Gino Rodrigo (Lead); Pinedo Sanchez, Sebastián Martín (Collaborator) | To Do |
| Sprint 1 | MOB-US-002 | Trabajar en la empresa y contexto de negocio previstos | SB1-T04 | Tenant and Workspace revalidation | Add the Android/Kotlin context boundary that revalidates the intended Tenant and Workspace before protected work is shown. | 5 | Pinedo Sanchez, Sebastián Martín (Lead); Yucra Sandoval, Diego Sebastián (Collaborator) | To Do |
| Sprint 1 | MOB-US-003 | Ver sólo el trabajo permitido para el rol | SB1-T05 | Role-scoped work state | Implement candidate role-scoped loading, empty and denied states without trusting client authorization. | 5 | Torrejón De Los Santos, Gino Rodrigo (Lead); Verde Bueno, Joaquín Francisco (Collaborator) | To Do |
| Sprint 1 | MOB-US-011 | Identificar un producto mediante el código del paquete o etiqueta | SB1-T06 | Android identification adapter | Establish an Android/Kotlin code-input/capture boundary that sends only an identifier to an authorized contract. | 6 | Pinedo Sanchez, Sebastián Martín (Lead); Torrejón De Los Santos, Gino Rodrigo (Collaborator) | To Do |
| Sprint 1 | MOB-US-012 | Buscar manualmente un producto cuando no hay escaneo | SB1-T07 | Manual identification fallback | Implement the accessible manual lookup fallback and error state for unavailable or ambiguous capture. | 5 | Torrejón De Los Santos, Gino Rodrigo (Lead); Verde Bueno, Joaquín Francisco (Collaborator) | To Do |
| Sprint 1 | MOB-US-044 | Saber cuándo una entrega requiere atención | SB1-T08 | Buyer attention state | Build the Flutter/Dart candidate attention state for a Buyer without treating it as Delivery confirmation. | 5 | Torrejón De Los Santos, Gino Rodrigo (Lead); Pinedo Sanchez, Sebastián Martín (Collaborator) | To Do |
| Sprint 1 | MOB-US-047 | Verificar una entrega mediante el código de handoff | SB1-T09 | Buyer handoff-code state | Build the Flutter/Dart candidate handoff-code state with explicit authorization and uncertain-result feedback. | 5 | Torrejón De Los Santos, Gino Rodrigo (Lead); Rojas Mancilla, Gerard Gianpier (Collaborator) | To Do |
| Sprint 1 | TS-MOB-001 | Integrar contratos REST con autoridad del servidor | SB1-T10 | Contract fixture and Problem Details | Define contract fixtures for selected success, denied and conflict paths, including Problem Details interpretation. | 6 | Rojas Mancilla, Gerard Gianpier (Lead); Pinedo Sanchez, Sebastián Martín (Collaborator) | To Do |
| Sprint 1 | TS-MOB-002 | Definir criterios de compatibilidad de plataforma | SB1-T11 | Android/Kotlin baseline | Configure and document a repeatable Android/Kotlin baseline build and compatible emulator/device check. | 6 | Pinedo Sanchez, Sebastián Martín (Lead); Verde Bueno, Joaquín Francisco (Collaborator) | To Do |
| Sprint 1 | TS-MOB-003 | Preservar paridad de contratos entre proyecciones Mobile | SB1-T12 | Flutter/Dart baseline | Configure and document a repeatable Flutter/Dart baseline build and contract-parity check. | 6 | Torrejón De Los Santos, Gino Rodrigo (Lead); Pinedo Sanchez, Sebastián Martín (Collaborator) | To Do |
| Sprint 1 | SPIKE-002 | Establecer tracks Mobile y límites de contratos | SB1-T13 | Android track evidence | Record Android/Kotlin setup, build, device/emulator limit and one non-authoritative contract exercise. | 5 | Pinedo Sanchez, Sebastián Martín (Lead); Torrejón De Los Santos, Gino Rodrigo (Collaborator) | To Do |
| Sprint 1 | SPIKE-002 | Establecer tracks Mobile y límites de contratos | SB1-T14 | Flutter track evidence | Record Flutter/Dart setup, build, device/emulator limit and one non-authoritative contract exercise. | 5 | Torrejón De Los Santos, Gino Rodrigo (Lead); Pinedo Sanchez, Sebastián Martín (Collaborator) | To Do |
| Sprint 1 | SPIKE-002 | Establecer tracks Mobile y límites de contratos | SB1-T15 | Shared-boundary decision record | Compare the two track exercises and record contract parity, adaptation limits and unresolved decisions. | 4 | Rojas Mancilla, Gerard Gianpier (Lead); Yucra Sandoval, Diego Sebastián (Collaborator) | To Do |
| Sprint 1 | N/A | Cross-cutting research constraint | SB1-T16 | UXPressia evidence organization | Transcribe the three provisional personas and evidence labels into a reviewable UXPressia-ready structure without fabricating research. | 4 | Verde Bueno, Joaquín Francisco (Lead); Rojas Mancilla, Gerard Gianpier (Collaborator) | To Do |
| Sprint 1 | N/A | Cross-cutting quality constraint | SB1-T17 | Accessibility baseline | Define manual accessibility checks for labels, focus/order, dynamic text and manual input fallback in both tracks. | 5 | Verde Bueno, Joaquín Francisco (Lead); Pinedo Sanchez, Sebastián Martín (Collaborator) | To Do |
| Sprint 1 | N/A | Cross-cutting repository constraint | SB1-T18 | GitFlow and evidence baseline | Record branch, commit, review and reproducibility evidence needed for the candidate Sprint scope. | 4 | Yucra Sandoval, Diego Sebastián (Lead); Rojas Mancilla, Gerard Gianpier (Collaborator) | To Do |
| Sprint 1 | N/A | Cross-cutting contract constraint | SB1-T19 | Contract test harness | Prepare the narrow test harness for selected authorization, denial and uncertain-result contract fixtures. | 4 | Rojas Mancilla, Gerard Gianpier (Lead); Verde Bueno, Joaquín Francisco (Collaborator) | To Do |
| Sprint 1 | N/A | Cross-cutting review constraint | SB1-T20 | Review evidence package | Assemble the planned demonstration checklist, acceptance-criteria trace and review evidence locations; do not mark execution complete. | 4 | Yucra Sandoval, Diego Sebastián (Lead); Verde Bueno, Joaquín Francisco (Collaborator) | To Do |

**Planned task hours:** 98. This is a planning total, not recorded effort or
velocity. Every task is estimated from 4 to 8 hours and remains To Do.

## Sprint 1 Definition of Done

A selected story or required artifact is complete for this academic Sprint only
when all applicable conditions hold:

- required implementation or artifact exists and is traceable;
- its acceptance criteria are checked;
- relevant automated and/or manual tests pass;
- no known critical defect remains;
- code or artifact review is complete;
- contract and relevant integration behavior are verified;
- accessibility and security checks applicable to the work are recorded;
- documentation and evidence are updated; and
- the result is traceable to the repository and review record.

A build, a local screen or a task marked To Do is not evidence of validación de
investigación, preparación para producción o validación de producto.
