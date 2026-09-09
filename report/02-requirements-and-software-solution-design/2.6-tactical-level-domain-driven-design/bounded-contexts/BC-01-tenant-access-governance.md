## 2.6 Tactical-Level Domain-Driven Design

Esta sección describe los once Bounded Contexts aceptados para Nexa. Operations
Mobile y Buyer Mobile son proyecciones de estos contextos compartidos; no crean
un contexto táctico propio ni modifican la autoridad del dominio.

| Código | Bounded Context |
| --- | --- |
| BC-01 | Tenant & Access Governance |
| BC-02 | Customer & Buyer Relationships |
| BC-03 | Catalog & Commercial Policy |
| BC-04 | Sales Commitment |
| BC-05 | Inventory Availability |
| BC-06 | Fulfillment & Delivery |
| BC-07 | Credit & Receivables |
| BC-08 | Payments |
| BC-09 | Business Documents |
| BC-10 | Notifications |
| BC-11 | Business Traceability |

Cada contexto presenta sus responsabilidades de Domain, Interface, Application
e Infrastructure, junto con diagramas de componentes, clases de dominio y
persistencia. Los modelos describen el diseño objetivo definido en el Blueprint;
la lectura de la implementación existente se mantiene separada y no equivale a
una prueba de comportamiento en ejecución.

### 2.6.1 BC-01 — Tenant & Access Governance

El modelo de BC-01 protege el aislamiento de Tenant, la identidad de Workspace,
el vínculo con Human Identity, la membresía de fuerza laboral, los roles y las
capacidades. `Tenant` no es `Workspace`; `HumanIdentity` no es
`WorkforceMembership` ni `BuyerRelationship`.

#### 2.6.1.1 Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `Tenant` | Lifecycle and isolation policy; one active Workspace and one active Company Owner in initial scope |
| `HumanIdentity` | Global person identity; never duplicated per Tenant |
| `WorkforceMembership` | Tenant/workspace participation, status and capability context |
| `RoleDefinition` | Role lifecycle and capability assignment |
| `CompanyOnboardingRequest` | Intake and activation handoff; no access before Tenant lifecycle gate |

`Workspace` is a Tenant-owned entity with its own identity. Value objects are
`TenantId`, `WorkspaceId`, `MembershipId`, `CompanyInformation`, `AccessContext`
and `CapabilityCode`; `AccessEligibilityPolicy` is a domain service.
`TenantRepository` and `WorkforceMembershipRepository` persist roots. Target
invariants: missing scope fails closed, Tenant is the maximum isolation
boundary, the current scope has one Workspace/active owner, and client-supplied tenant IDs do
not establish authorization.

#### 2.6.1.2 Interface Layer

Target interface roles are onboarding, authentication/session, tenant access
and capability resolution. URI names are intentionally omitted until a
versioned contract is accepted. The API remains authoritative; Portal and
planned Mobile surfaces consume authorized projections. Security audit remains
distinct from BC-11 business traceability.

#### 2.6.1.3 Application Layer

Target handlers coordinate onboarding submission, Tenant activation, access
evaluation, membership capability changes and ownership transfer. Each command
reconstructs Tenant/Workspace context server-side, applies authorization and
uses version/CAS or deterministic locking where an owner or membership race
matters. Local commit may publish a durable outbox fact; no new published event
is inferred here.

#### 2.6.1.4 Infrastructure Layer

Target persistence is the shared PostgreSQL projection `tenant`, `workspace`,
`human_identity`, `company_onboarding_request`, `workforce_membership`,
`role_definition`, `capability_definition`, `membership_role` and
`membership_capability_override`, with tenant scope and constraints defined by
the canonical SQL. Repositories and authorization adapters are logical
ownership seams, not separate databases. Object Storage and Mobile are not
owned by this context.

AS-IS anchor: API `origin/main` contains `tenantaccessgovernance/iam` and
tenant-management documentation/classes. Classification: identity/session
and existing access paths `AS-IS VERIFIED`; full target onboarding,
single-owner orchestration and capability semantics `PARTIAL`; runtime parity
and complete target workflow `NOT EVIDENCED`.

#### 2.6.1.5 Bounded Context Software Architecture Component Level Diagrams

The logical component family is `Nexa-API-IdentityTenantCustomer-TARGET`.
It groups API components for identity, tenant and customer concerns inside one
API container; it does not create an Identity container or a new BC.

![BC-01 component family — TARGET](../../../assets/chapter-2/c4/Nexa-API-IdentityTenantCustomer-TARGET.png)

El diagrama representa un diseño objetivo. No demuestra por sí solo que exista
una clase Java equivalente ni una implementación en ejecución.

#### 2.6.1.6 Bounded Context Software Architecture Code Level Diagrams

The code-level drawings below are target construction models, regenerated from
copied PlantUML sources. They are not source-code inventory.

##### 2.6.1.6.1 Bounded Context Domain Layer Class Diagrams

![BC-01 tactical domain model — TARGET](../../../assets/chapter-2/tactical/BC-01/BC01_TenantAccessGovernance.png)

Source: [domain-model.puml](../../../assets/chapter-2/tactical/BC-01/domain-model.puml).
El diagrama se presenta como modelo de diseño, no como inventario de código.

##### 2.6.1.6.2 Bounded Context Database Design Diagram

![BC-01 target database projection](../../../assets/chapter-2/tactical/BC-01/database-diagram.png)

Source: [database-diagram.puml](../../../assets/chapter-2/tactical/BC-01/database-diagram.puml).
This is a logical ownership projection of shared PostgreSQL; it shows target
keys/constraints and tenant scope, not a physical BC database.

#### Lectura de implementación y límite de evidencia

| Concern | Classification | Evidence boundary |
| :--- | :--- | :--- |
| IAM/session and tenant access code | `AS-IS VERIFIED` | API `tenantaccessgovernance/iam` at `origin/main` |
| Target domain boundary and diagrams | `TARGET / ACCEPTED` | Blueprint tactical model, PlantUML and target SQL |
| Complete target onboarding/ownership implementation | `PARTIAL` | No claim beyond observed API classes |
| Mobile implementation, runtime and validación de producto | `NOT EVIDENCED` | Mobile remains a planned projection |
