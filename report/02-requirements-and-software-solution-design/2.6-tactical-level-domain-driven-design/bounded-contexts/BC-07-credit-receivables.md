# 2.6.8. BC-07 — Credit & Receivables

`DOMAIN MODEL: TARGET / ACCEPTED`
`IMPLEMENTATION CROSSWALK: AS-IS VERIFIED / PARTIAL`

Canonical target: Blueprint `01-shared/domain/bounded-contexts/BC-07-credit-receivables/`.
This context owns credit exposure, reservation and Receivable authority.
Payment is a separate context; Payment Confirmed is not a Receivable.

## 2.6.8.1 Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `CreditAccount` | Limit, exposure and reservation policy for one Customer Account |
| `CreditReservation` | Active protection for one commercial source; released/converted once |
| `Receivable` | Posted obligation, balance and due state |
| `FinancialAdjustment` | Explicit correction with reason and actor |

`ReceivableApplication` belongs to financial authority and references Payment
by ID. Value objects include `CreditAmount`, `AvailableCredit`, `Terms` and
`AdjustmentReason`; policies include `CreditDecisionPolicy` and
`DoubleCountPreventionPolicy`. Repositories own CreditAccount and Receivable
roots.

Target invariant: Available Credit = Credit Limit − Active Credit Reservations
− Outstanding Receivable Balances. Credit purchase reserves at PR submission;
direct order reserves in the same logical confirmation; credit/net Receivable
posts at SO confirmation. Applications cannot over-apply or double-apply;
corrections preserve original facts. Buyer sees safe projections, not internal
risk policy.

## 2.6.8.2 Interface Layer

Target contracts cover credit exposure, reservation, receivable posting,
payment application and explicit financial adjustment. Exact routes and DTOs
remain unclaimed where absent from API evidence. Capability authorization and
Tenant scope are server-side; external payment provider data enters through
BC-08 contracts.

## 2.6.8.3 Application Layer

Target handlers evaluate/reserve credit, post Receivable, apply/reverse Payment
references and record adjustments. Application boundaries coordinate BC-08
without a cross-context aggregate. Idempotency and concurrency protect last
credit; committed facts feed documents/notifications/traceability after commit.

## 2.6.8.4 Infrastructure Layer

Target shared PostgreSQL ownership covers `credit_account`,
`credit_reservation`, `receivable`, `receivable_application`,
`financial_adjustment` and `financial_ledger_entry`. Payment and Sales Order
identifiers are non-owning references. Tenant predicates, monetary checks and
history rules remain in canonical SQL; no physical BC database is asserted.

AS-IS anchor: API `creditreceivables` domain/application/public API,
persistence adapters, tests and migration V43/V76. Credit/reservation/
receivable code is `AS-IS VERIFIED`; complete target ledger/correction and
cross-context closure is `PARTIAL`; Mobile implementation and runtime are
`NOT EVIDENCED`.

## 2.6.8.5 Bounded Context Software Architecture Component Level Diagrams

`Nexa-API-CreditPaymentDocuments-TARGET` is the selected logical API family
for credit, payment and document collaboration. It is not three containers or
three physical databases.

![BC-07 component family — TARGET](../../../assets/chapter-2/c4/Nexa-API-CreditPaymentDocuments-TARGET.png)

Source/export provenance: [Chapter 2 register](../../../assets/chapter-2/provenance.md).

## 2.6.8.6 Bounded Context Software Architecture Code Level Diagrams

### 2.6.8.6.1 Bounded Context Domain Layer Class Diagrams

![BC-07 tactical domain model — TARGET](../../../assets/chapter-2/tactical/BC-07/BC07_CreditReceivables.png)

Source: [domain-model.puml](../../../assets/chapter-2/tactical/BC-07/domain-model.puml).

### 2.6.8.6.2 Bounded Context Database Design Diagram

![BC-07 target database projection](../../../assets/chapter-2/tactical/BC-07/database-diagram.png)

Source: [database-diagram.puml](../../../assets/chapter-2/tactical/BC-07/database-diagram.puml).
This is a logical projection of shared PostgreSQL with target constraints and
tenant scope; canonical SQL remains authority.

## Crosswalk and open evidence

| Concern | Classification | Evidence boundary |
| :--- | :--- | :--- |
| Credit/reservation/receivable code and tests | `AS-IS VERIFIED` | API `creditreceivables` at `origin/main` |
| Payment != Receivable and target authority | `TARGET / ACCEPTED` | Blueprint tactical model/data model |
| Complete application/correction parity | `PARTIAL` | Existing API does not prove all target invariants |
| Mobile financial workflow and Product Acceptance | `NOT EVIDENCED` | Mobile is indirect planned projection |
