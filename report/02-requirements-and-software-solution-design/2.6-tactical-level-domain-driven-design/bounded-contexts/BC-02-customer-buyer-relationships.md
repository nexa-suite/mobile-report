# 2.6.2. BC-02 — Customer & Buyer Relationships

`DOMAIN MODEL: TARGET / ACCEPTED`
`IMPLEMENTATION CROSSWALK: AS-IS VERIFIED / PARTIAL`

Canonical target: Blueprint `01-shared/domain/bounded-contexts/BC-02-customer-buyer-relationships/`.
This context owns supplier-Tenant customer accounts, contacts, addresses and
Buyer Relationship lifecycle. Customer Account may exist without Portal
identity; Buyer Relationship is not Human Identity or Workforce Membership.

## 2.6.2.1 Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `CustomerAccount` | Account, contacts and addresses for a supplier Tenant |
| `BuyerRelationship` | Invitation, approval, suspension and revocation for one supplier Tenant |
| `BuyerRelationshipHistory` | Immutable lifecycle facts, not a mutable child graph |

`CustomerContact` and `CustomerAddress` compose into CustomerAccount.
`ContactInformation`, `Address`, `CustomerAccountId`, `RelationshipId`,
`SupplierTenantId` and `RelationshipStatus` are target value objects/types.
`BuyerEligibilityPolicy` evaluates status and Tenant scope. Repositories are
`CustomerAccountRepository` and `BuyerRelationshipRepository`. The accepted scope allows one
active principal Buyer Identity per Customer Account and preserves lifecycle
history.

## 2.6.2.2 Interface Layer

Target roles expose account, address and Buyer Relationship commands/queries
through versioned contracts. The exact URI is not invented. Authorization
comes from BC-01; Sales Commitment revalidates relationship eligibility when a
purchase is submitted. Portal/Mobile read projections cannot authorize by
themselves.

## 2.6.2.3 Application Layer

Target handlers create accounts, maintain contact/address data, approve or
suspend relationships and link a principal identity by reference. Account and
relationship transitions are separate local consistency boundaries. Commands
carry idempotency/version semantics where retries or stale relationship state
could duplicate approval; committed facts may reach BC-11 through outbox.

## 2.6.2.4 Infrastructure Layer

Target shared-PostgreSQL ownership covers `customer_account`,
`customer_contact`, `customer_address`, `buyer_relationship` and
`buyer_relationship_history`. Foreign keys to Tenant, Workspace and Human
Identity are stable references; no cross-BC aggregate graph or direct write to
BC-01 tables is implied. RLS/tenant predicates remain required where supported
by the canonical SQL.

AS-IS anchor: API `customerbuyerrelationships` account/address application,
domain and persistence paths, plus `sales.client_account` migrations and the
V71 single-buyer constraint. Account/address operations are `AS-IS VERIFIED`;
explicit target relationship approval/history is `PARTIAL`; Mobile runtime and
complete parity are `NOT EVIDENCED`.

## 2.6.2.5 Bounded Context Software Architecture Component Level Diagrams

`Nexa-API-IdentityTenantCustomer-TARGET` is the selected logical component
family. It groups identity, tenant and customer API concerns within Nexa API;
it is not a deployment unit or a fourth context.

![BC-02 component family — TARGET](../../../assets/chapter-2/c4/Nexa-API-IdentityTenantCustomer-TARGET.png)

Source/export hash and Structurizr provenance: [Chapter 2 register](../../../../delivery-checklists/chapter-02-evidence-provenance.md).

## 2.6.2.6 Bounded Context Software Architecture Code Level Diagrams

### 2.6.2.6.1 Bounded Context Domain Layer Class Diagrams

![BC-02 tactical domain model — TARGET](../../../assets/chapter-2/tactical/BC-02/BC02_CustomerBuyerRelationships.png)

Source: [domain-model.puml](../../../assets/chapter-2/tactical/BC-02/domain-model.puml).

### 2.6.2.6.2 Bounded Context Database Design Diagram

![BC-02 target database projection](../../../assets/chapter-2/tactical/BC-02/database-diagram.png)

Source: [database-diagram.puml](../../../assets/chapter-2/tactical/BC-02/database-diagram.puml).
Shared PostgreSQL and logical ownership remain the target; no physical
database per context is asserted.

## Crosswalk and open evidence

| Concern | Classification | Evidence boundary |
| :--- | :--- | :--- |
| Account/contact/address code | `AS-IS VERIFIED` | API `customerbuyerrelationships` paths at `origin/main` |
| Buyer Relationship target lifecycle | `TARGET / ACCEPTED` | Blueprint tactical model and target SQL |
| Approval/history parity | `PARTIAL` | Existing membership constraint is supporting evidence, not full target proof |
| Mobile implementation, runtime and validación de producto | `NOT EVIDENCED` | Client remains planned projection |
