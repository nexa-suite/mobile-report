# Tactical bounded-context packages

Each package follows the Statement V4.0 order: Domain Layer, Interface Layer,
Application Layer, Infrastructure Layer, Component Level Diagrams, Code Level
Diagrams, Domain Layer Class Diagram and Database Design Diagram.

| Code | Package |
| :--- | :--- |
| BC-01 | [Tenant & Access Governance](./BC-01-tenant-access-governance.md) |
| BC-02 | [Customer & Buyer Relationships](./BC-02-customer-buyer-relationships.md) |
| BC-03 | [Catalog & Commercial Policy](./BC-03-catalog-commercial-policy.md) |
| BC-04 | [Sales Commitment](./BC-04-sales-commitment.md) |
| BC-05 | [Inventory Availability](./BC-05-inventory-availability.md) |
| BC-06 | [Fulfillment & Delivery](./BC-06-fulfillment-delivery.md) |
| BC-07 | [Credit & Receivables](./BC-07-credit-receivables.md) |
| BC-08 | [Payments](./BC-08-payments.md) |
| BC-09 | [Business Documents](./BC-09-business-documents.md) |
| BC-10 | [Notifications](./BC-10-notifications.md) |
| BC-11 | [Business Traceability](./BC-11-business-traceability.md) |

Every package declares `DOMAIN MODEL: TARGET / ACCEPTED` and
`IMPLEMENTATION CROSSWALK: AS-IS VERIFIED / PARTIAL`. Target diagrams and
source hashes are in [Chapter 2 provenance](../../../../delivery-checklists/chapter-02-evidence-provenance.md).
