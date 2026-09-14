### 2.6.2. Bounded Context: Customer & Buyer Relationships

BC-02 conserva Customer Account y Buyer Relationship. Una relación comercial
puede existir sin identidad Portal; BuyerRelationship no es HumanIdentity ni
WorkforceMembership.

#### 2.6.2.1. Canonical class dictionary

*Clases y responsabilidades de BC-02 por capa.*

| Layer | Class | Category | Purpose | Key Attributes / Inputs | Main Methods / Business Behavior | Relationships / Collaborators | Aggregate Owner / External References |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Domain | `CustomerAccount` | Aggregate Root | Cuenta comercial del cliente. | `CustomerAccountId`, `TenantId`, legal name, status. | Open, suspend and maintain contact data. | Owns contacts and addresses. | Owns `CustomerContact` and `CustomerAddress`. |
| Domain | `BuyerRelationship` | Aggregate Root | Elegibilidad entre supplier Tenant y Buyer. | `BuyerRelationshipId`, `CustomerAccountId`, `HumanIdentityId`, status. | Request, approve, suspend and revoke. | References account and identity by ID. | Owns immutable history records. |
| Domain | `BuyerRelationshipHistory` | Entity | Hecho inmutable de transición de relación. | From/to status, actor ID, occurred at. | Record transition once. | Belongs to BuyerRelationship. | `BuyerRelationship`. |
| Domain | `BuyerEligibilityPolicy` | Domain Policy | Evalúa elegibilidad con datos de relación y alcance. | Relationship status, AccessContext. | Allow or reject a purchase actor. | Pure policy; no repository or provider I/O. | Uses value objects only. |
| Domain | `AddressSnapshot` | Value Object | Dirección congelada para un uso autorizado. | Address fields and instructions. | Validate complete address. | Used by CustomerAddress. | `CustomerAccount`. |
| Interface | `BC-02 Interface Boundary` | Interface component | Traduce comandos y consultas de cuenta y relación. | Actor, tenant scope, version, payload. | Rejects unauthorized or stale requests. | Calls application orchestration. | Does not administer BC-01 identities. |
| Application | `BC-02 Application Orchestration` | Application component | Coordina cuentas, relaciones y su historial. | Commands, typed identity references. | Maintains independent account and relationship lifecycles. | Uses BC-01 scoped access contract. | References HumanIdentity by ID. |
| Infrastructure | `BC-02 Persistence Adapter` | Infrastructure component | Persiste cuentas y relaciones. | Tenant-scoped account records. | Maps roots and immutable history. | PostgreSQL shared physically. | No direct write to BC-01 records. |

Sales Commitment revalida Buyer Relationship mediante contrato antes de aceptar
un comando comercial. Una proyección de cliente no concede elegibilidad.

#### 2.6.2.2. Component and code-level diagrams

*Vista C4 L3 de BC-02 Customer & Buyer Relationships.*

![Vista C4 L3 de BC-02 Customer & Buyer Relationships](../../../assets/chapter-2/c4/Nexa-API-BC-02-CustomerBuyerRelationships.svg)

*Nota. Elaboración propia.*

*Modelo de dominio táctico de BC-02 Customer & Buyer Relationships.*

![Modelo de dominio táctico de BC-02 Customer & Buyer Relationships](../../../assets/chapter-2/tactical/BC-02/BC02_CustomerBuyerRelationships.svg)

*Nota. Elaboración propia.*

*Diseño lógico de base de datos de BC-02 Customer & Buyer Relationships.*

![Diseño lógico de base de datos de BC-02 Customer & Buyer Relationships](../../../assets/chapter-2/tactical/BC-02/database-diagram.svg)

*Nota. Elaboración propia.*
