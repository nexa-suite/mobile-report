workspace "Nexa Chapter 02" "C4 views for the Chapter 02 domain design" {
    !identifiers hierarchical

    model {
        interestedCompany = person "Interested Company Representative" "Requests an organizational relationship with Nexa."
        onboardingStaff = person "Nexa Onboarding Staff" "Approves company onboarding."
        tenantWorkforce = person "Tenant Workforce" "Company Owner, Tenant Administrator, sales, warehouse, dispatch and delivery roles."
        customerBuyer = person "Customer Buyer" "Requests, receives and reviews B2B commitments."

        paymentProvider = softwareSystem "Payment Provider" "External payment processing service."
        emailDeliveryService = softwareSystem "Email Delivery Service" "External email delivery service."
        mapsProvider = softwareSystem "Maps & Geolocation Provider" "External navigation and geolocation service."

        nexa = softwareSystem "Nexa" "Multi-tenant B2B SaaS for commercial commitments, inventory availability, fulfillment and delivery." {
            website = container "Nexa Website" "Public product discovery and relationship intake." "Static web application"
            platform = container "Nexa Platform" "Authenticated workforce experience." "Angular 22 SPA"
            buyerPortal = container "Nexa Buyer Portal" "Authenticated B2B Buyer experience." "Angular 22 SPA"
            api = container "Nexa API" "Authoritative application and domain behavior, tenant enforcement and persistence orchestration." "Java 25 / Spring Boot 4.1 / Spring Modulith" {
                bc01Interface = component "BC-01 Interface Boundary" "Accepts onboarding, identity and access requests." "REST boundary"
                bc01Application = component "BC-01 Application Orchestration" "Coordinates scoped tenant and access use cases." "Application layer"
                bc01Domain = component "BC-01 Domain Model and Policies" "Tenant, HumanIdentity, WorkforceMembership, RoleDefinition and onboarding invariants." "Domain layer"
                bc01Persistence = component "BC-01 Persistence Adapter" "Stores tenant-scoped governance records." "Infrastructure adapter"

                bc02Interface = component "BC-02 Interface Boundary" "Accepts customer and Buyer Relationship requests." "REST boundary"
                bc02Application = component "BC-02 Application Orchestration" "Coordinates customer and relationship use cases." "Application layer"
                bc02Domain = component "BC-02 Domain Model and Policies" "Customer Account and Buyer Relationship invariants." "Domain layer"
                bc02Persistence = component "BC-02 Persistence Adapter" "Stores customer and relationship records." "Infrastructure adapter"

                bc03Interface = component "BC-03 Interface Boundary" "Accepts catalog and commercial-policy requests." "REST boundary"
                bc03Application = component "BC-03 Application Orchestration" "Resolves authorized commercial offers." "Application layer"
                bc03Domain = component "BC-03 Domain Model and Policies" "Product, SKU, PriceList, CustomerTerms and Promotion invariants." "Domain layer"
                bc03Persistence = component "BC-03 Persistence Adapter" "Stores catalog and policy records." "Infrastructure adapter"

                bc04Interface = component "BC-04 Interface Boundary" "Accepts commercial intent and confirmation commands." "REST boundary"
                bc04Application = component "BC-04 Application Orchestration" "Coordinates Purchase Request, Direct Order and commitment decisions." "Application layer"
                bc04Domain = component "BC-04 Domain Model and Policies" "RequestDraft, PurchaseRequest, CommercialCommitment and SalesOrder invariants." "Domain layer"
                bc04Persistence = component "BC-04 Persistence Adapter" "Stores commercial lifecycle records." "Infrastructure adapter"

                bc05Interface = component "BC-05 Interface Boundary" "Accepts availability, reservation and allocation commands." "REST boundary"
                bc05Application = component "BC-05 Application Orchestration" "Coordinates inventory protection and physical allocation." "Application layer"
                bc05Domain = component "BC-05 Domain Model and Policies" "Warehouse, inventory, lot, reservation, backing and allocation invariants." "Domain layer"
                bc05Persistence = component "BC-05 Persistence Adapter" "Stores inventory facts and positions." "Infrastructure adapter"

                bc06Interface = component "BC-06 Interface Boundary" "Accepts fulfillment, delivery and evidence commands." "REST boundary"
                bc06Application = component "BC-06 Application Orchestration" "Coordinates fulfillment and delivery lifecycle work." "Application layer"
                bc06Domain = component "BC-06 Domain Model and Policies" "Fulfillment, Delivery, POD and TemperatureEvidence invariants." "Domain layer"
                bc06Persistence = component "BC-06 Persistence Adapter" "Stores fulfillment and delivery records." "Infrastructure adapter"

                bc07Interface = component "BC-07 Interface Boundary" "Accepts credit and receivable commands." "REST boundary"
                bc07Application = component "BC-07 Application Orchestration" "Coordinates credit, receivable and adjustment use cases." "Application layer"
                bc07Domain = component "BC-07 Domain Model and Policies" "CreditAccount, CreditReservation, Receivable and FinancialAdjustment invariants." "Domain layer"
                bc07Persistence = component "BC-07 Persistence Adapter" "Stores credit and receivable records." "Infrastructure adapter"

                bc08Interface = component "BC-08 Interface Boundary" "Accepts payment reports and provider callbacks." "REST and webhook boundary"
                bc08Application = component "BC-08 Application Orchestration" "Coordinates payment and reconciliation use cases." "Application layer"
                bc08Domain = component "BC-08 Domain Model and Policies" "Payment and PaymentReconciliationCase invariants." "Domain layer"
                bc08Persistence = component "BC-08 Persistence Adapter" "Stores payment and reconciliation facts." "Infrastructure adapter"
                bc08ProviderAcl = component "BC-08 Provider ACL" "Translates provider payloads and performs provider I/O." "Infrastructure adapter"

                bc09Interface = component "BC-09 Interface Boundary" "Accepts authorized document commands." "REST boundary"
                bc09Application = component "BC-09 Application Orchestration" "Coordinates document generation and revision work." "Application layer"
                bc09Domain = component "BC-09 Domain Model and Policies" "BusinessDocument and DocumentNumberSeries invariants." "Domain layer"
                bc09Persistence = component "BC-09 Persistence Adapter" "Stores document metadata and immutable history." "Infrastructure adapter"
                bc09StorageAdapter = component "BC-09 Object Storage Adapter" "Stores and retrieves authorized document bytes through a port." "Infrastructure adapter"

                bc10Interface = component "BC-10 Interface Boundary" "Accepts notification administration commands." "REST boundary"
                bc10Application = component "BC-10 Application Orchestration" "Consumes published facts and coordinates notification delivery." "Application layer"
                bc10Domain = component "BC-10 Domain Model and Policies" "Notification, templates, preferences and subscription invariants." "Domain layer"
                bc10Persistence = component "BC-10 Persistence Adapter" "Stores notification lifecycle records." "Infrastructure adapter"
                bc10DeliveryAdapter = component "BC-10 Delivery Adapter" "Performs channel I/O outside the domain model." "Infrastructure adapter"

                bc11Interface = component "BC-11 Interface Boundary" "Accepts authorized traceability queries." "REST boundary"
                bc11Application = component "BC-11 Application Orchestration" "Deduplicates and appends published business facts." "Application layer"
                bc11Domain = component "BC-11 Domain Model and Policies" "BusinessTraceabilityRecord and evidence-reference invariants." "Domain layer"
                bc11Persistence = component "BC-11 Persistence Adapter" "Stores append-only traceability records." "Infrastructure adapter"
                bc11ProjectionAdapter = component "BC-11 Fact Intake Adapter" "Receives durable integration facts and manages inbox state." "Infrastructure adapter"
            }
            postgresql = container "PostgreSQL" "Shared physical transactional persistence with logical ownership by context." "PostgreSQL" {
                tags "Database"
            }
            objectStorage = container "Object Storage" "Authorized document and evidence bytes." "S3-compatible object storage" {
                tags "Storage"
            }
        }

        interestedCompany -> nexa "Requests company onboarding"
        onboardingStaff -> nexa "Reviews onboarding"
        tenantWorkforce -> nexa "Administers and operates authorized work"
        customerBuyer -> nexa "Requests and receives commitments"
        nexa -> paymentProvider "Uses payment services"
        nexa -> emailDeliveryService "Uses delivery services"
        nexa -> mapsProvider "Uses navigation services"

        nexa.website -> nexa.api "Submits public intake"
        nexa.platform -> nexa.api "Uses authorized workforce contracts"
        nexa.buyerPortal -> nexa.api "Uses authorized Buyer contracts"
        nexa.api -> nexa.postgresql "Reads and writes owned records"
        nexa.api -> nexa.objectStorage "Stores authorized bytes through ports"
        nexa.api -> paymentProvider "Uses translated payment contracts"
        nexa.api -> emailDeliveryService "Uses notification delivery contracts"
        nexa.api -> mapsProvider "Uses authorized navigation contracts"

        nexa.api.bc01Interface -> nexa.api.bc01Application "Invokes"
        nexa.api.bc01Application -> nexa.api.bc01Domain "Coordinates"
        nexa.api.bc01Application -> nexa.api.bc01Persistence "Reads and writes"
        nexa.api.bc01Persistence -> nexa.postgresql "Uses owned records"

        nexa.api.bc02Interface -> nexa.api.bc02Application "Invokes"
        nexa.api.bc02Application -> nexa.api.bc02Domain "Coordinates"
        nexa.api.bc02Application -> nexa.api.bc02Persistence "Reads and writes"
        nexa.api.bc02Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc02Application -> nexa.api.bc01Application "Uses scoped access contract"

        nexa.api.bc03Interface -> nexa.api.bc03Application "Invokes"
        nexa.api.bc03Application -> nexa.api.bc03Domain "Coordinates"
        nexa.api.bc03Application -> nexa.api.bc03Persistence "Reads and writes"
        nexa.api.bc03Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc03Application -> nexa.api.bc02Application "Uses eligibility contract"

        nexa.api.bc04Interface -> nexa.api.bc04Application "Invokes"
        nexa.api.bc04Application -> nexa.api.bc04Domain "Coordinates"
        nexa.api.bc04Application -> nexa.api.bc04Persistence "Reads and writes"
        nexa.api.bc04Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc04Application -> nexa.api.bc02Application "Uses Buyer Relationship contract"
        nexa.api.bc04Application -> nexa.api.bc03Application "Uses ResolvedOfferSnapshot contract"
        nexa.api.bc04Application -> nexa.api.bc05Application "Requests inventory protection"
        nexa.api.bc04Application -> nexa.api.bc07Application "Requests credit decision"
        nexa.api.bc04Application -> nexa.api.bc06Application "Publishes confirmed Sales Order"

        nexa.api.bc05Interface -> nexa.api.bc05Application "Invokes"
        nexa.api.bc05Application -> nexa.api.bc05Domain "Coordinates"
        nexa.api.bc05Application -> nexa.api.bc05Persistence "Reads and writes"
        nexa.api.bc05Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc05Application -> nexa.api.bc06Application "Publishes PhysicalAllocation reference"

        nexa.api.bc06Interface -> nexa.api.bc06Application "Invokes"
        nexa.api.bc06Application -> nexa.api.bc06Domain "Coordinates"
        nexa.api.bc06Application -> nexa.api.bc06Persistence "Reads and writes"
        nexa.api.bc06Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc06Application -> nexa.api.bc05Application "Requests physical mutation"
        nexa.api.bc06Application -> nexa.api.bc09Application "Publishes delivery and POD facts"
        nexa.api.bc06Application -> nexa.api.bc10Application "Publishes notification facts"
        nexa.api.bc06Application -> nexa.api.bc11Application "Publishes traceability facts"

        nexa.api.bc07Interface -> nexa.api.bc07Application "Invokes"
        nexa.api.bc07Application -> nexa.api.bc07Domain "Coordinates"
        nexa.api.bc07Application -> nexa.api.bc07Persistence "Reads and writes"
        nexa.api.bc07Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc07Application -> nexa.api.bc09Application "Publishes receivable facts"
        nexa.api.bc07Application -> nexa.api.bc10Application "Publishes notification facts"
        nexa.api.bc07Application -> nexa.api.bc11Application "Publishes traceability facts"

        nexa.api.bc08Interface -> nexa.api.bc08Application "Invokes"
        nexa.api.bc08Application -> nexa.api.bc08Domain "Coordinates"
        nexa.api.bc08Application -> nexa.api.bc08Persistence "Reads and writes"
        nexa.api.bc08Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc08Application -> nexa.api.bc08ProviderAcl "Uses provider port"
        nexa.api.bc08ProviderAcl -> paymentProvider "Translates provider I/O"
        nexa.api.bc08Application -> nexa.api.bc07Application "Publishes payment facts"
        nexa.api.bc08Application -> nexa.api.bc09Application "Publishes document facts"
        nexa.api.bc08Application -> nexa.api.bc10Application "Publishes notification facts"
        nexa.api.bc08Application -> nexa.api.bc11Application "Publishes traceability facts"

        nexa.api.bc09Interface -> nexa.api.bc09Application "Invokes"
        nexa.api.bc09Application -> nexa.api.bc09Domain "Coordinates"
        nexa.api.bc09Application -> nexa.api.bc09Persistence "Reads and writes"
        nexa.api.bc09Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc09Application -> nexa.api.bc09StorageAdapter "Uses storage port"
        nexa.api.bc09StorageAdapter -> nexa.objectStorage "Stores authorized bytes"
        nexa.api.bc09Application -> nexa.api.bc10Application "Publishes document facts"
        nexa.api.bc09Application -> nexa.api.bc11Application "Publishes traceability facts"

        nexa.api.bc10Interface -> nexa.api.bc10Application "Invokes"
        nexa.api.bc10Application -> nexa.api.bc10Domain "Coordinates"
        nexa.api.bc10Application -> nexa.api.bc10Persistence "Reads and writes"
        nexa.api.bc10Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc10Application -> nexa.api.bc10DeliveryAdapter "Uses channel port"
        nexa.api.bc10DeliveryAdapter -> emailDeliveryService "Delivers email"
        nexa.api.bc10Application -> nexa.api.bc11Application "Publishes delivery outcomes"

        nexa.api.bc11Interface -> nexa.api.bc11Application "Invokes"
        nexa.api.bc11Application -> nexa.api.bc11Domain "Coordinates"
        nexa.api.bc11Application -> nexa.api.bc11Persistence "Appends records"
        nexa.api.bc11Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc11ProjectionAdapter -> nexa.api.bc11Application "Supplies deduplicated facts"

        deploymentEnvironment "Provider-neutral topology" {
            publicEdge = deploymentNode "Public Edge" "Serves public and authenticated web clients." "HTTPS" {
                websiteInstance = containerInstance nexa.website
                platformInstance = containerInstance nexa.platform
                buyerPortalInstance = containerInstance nexa.buyerPortal
            }
            applicationRuntime = deploymentNode "Application Runtime" "Runs the modular Nexa API." "Container runtime" {
                apiInstance = containerInstance nexa.api
            }
            dataServices = deploymentNode "Data Services" "Stores transactional and object data." "Managed data services" {
                postgresqlInstance = containerInstance nexa.postgresql
                objectStorageInstance = containerInstance nexa.objectStorage
            }
        }
    }

    views {
        systemContext nexa "system-context" {
            include interestedCompany
            include onboardingStaff
            include tenantWorkforce
            include customerBuyer
            include nexa
            include paymentProvider
            include emailDeliveryService
            include mapsProvider
            autolayout lr
        }

        container nexa "containers" {
            include interestedCompany
            include onboardingStaff
            include tenantWorkforce
            include customerBuyer
            include nexa.website
            include nexa.platform
            include nexa.buyerPortal
            include nexa.api
            include nexa.postgresql
            include nexa.objectStorage
            include paymentProvider
            include emailDeliveryService
            include mapsProvider
            autolayout lr
        }

        deployment nexa "Provider-neutral topology" "deployment" {
            include *
            autolayout lr
        }

        component nexa.api "identity-tenant-customer" {
            include nexa.api.bc01Interface
            include nexa.api.bc01Application
            include nexa.api.bc01Domain
            include nexa.api.bc01Persistence
            include nexa.api.bc02Interface
            include nexa.api.bc02Application
            include nexa.api.bc02Domain
            include nexa.api.bc02Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "commercial-inventory" {
            include nexa.api.bc03Application
            include nexa.api.bc03Domain
            include nexa.api.bc04Application
            include nexa.api.bc04Domain
            include nexa.api.bc05Application
            include nexa.api.bc05Domain
            include nexa.api.bc07Application
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "fulfillment-delivery" {
            include nexa.api.bc04Application
            include nexa.api.bc05Application
            include nexa.api.bc06Interface
            include nexa.api.bc06Application
            include nexa.api.bc06Domain
            include nexa.api.bc06Persistence
            include nexa.api.bc09Application
            include nexa.api.bc10Application
            include nexa.api.bc11Application
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "credit-payment-documents" {
            include nexa.api.bc07Application
            include nexa.api.bc07Domain
            include nexa.api.bc08Application
            include nexa.api.bc08Domain
            include nexa.api.bc08ProviderAcl
            include nexa.api.bc09Application
            include nexa.api.bc09Domain
            include nexa.api.bc09StorageAdapter
            include nexa.postgresql
            include nexa.objectStorage
            include paymentProvider
            autolayout lr
        }

        component nexa.api "bc-01-tenant-access-governance" {
            include nexa.api.bc01Interface
            include nexa.api.bc01Application
            include nexa.api.bc01Domain
            include nexa.api.bc01Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-02-customer-buyer-relationships" {
            include nexa.api.bc02Interface
            include nexa.api.bc02Application
            include nexa.api.bc02Domain
            include nexa.api.bc02Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-03-catalog-commercial-policy" {
            include nexa.api.bc03Interface
            include nexa.api.bc03Application
            include nexa.api.bc03Domain
            include nexa.api.bc03Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-04-sales-commitment" {
            include nexa.api.bc04Interface
            include nexa.api.bc04Application
            include nexa.api.bc04Domain
            include nexa.api.bc04Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-05-inventory-availability" {
            include nexa.api.bc05Interface
            include nexa.api.bc05Application
            include nexa.api.bc05Domain
            include nexa.api.bc05Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-06-fulfillment-delivery" {
            include nexa.api.bc06Interface
            include nexa.api.bc06Application
            include nexa.api.bc06Domain
            include nexa.api.bc06Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-07-credit-receivables" {
            include nexa.api.bc07Interface
            include nexa.api.bc07Application
            include nexa.api.bc07Domain
            include nexa.api.bc07Persistence
            include nexa.postgresql
            autolayout lr
        }

        component nexa.api "bc-08-payments" {
            include nexa.api.bc08Interface
            include nexa.api.bc08Application
            include nexa.api.bc08Domain
            include nexa.api.bc08Persistence
            include nexa.api.bc08ProviderAcl
            include nexa.postgresql
            include paymentProvider
            autolayout lr
        }

        component nexa.api "bc-09-business-documents" {
            include nexa.api.bc09Interface
            include nexa.api.bc09Application
            include nexa.api.bc09Domain
            include nexa.api.bc09Persistence
            include nexa.api.bc09StorageAdapter
            include nexa.postgresql
            include nexa.objectStorage
            autolayout lr
        }

        component nexa.api "bc-10-notifications" {
            include nexa.api.bc10Interface
            include nexa.api.bc10Application
            include nexa.api.bc10Domain
            include nexa.api.bc10Persistence
            include nexa.api.bc10DeliveryAdapter
            include nexa.postgresql
            include emailDeliveryService
            autolayout lr
        }

        component nexa.api "bc-11-business-traceability" {
            include nexa.api.bc11Interface
            include nexa.api.bc11ProjectionAdapter
            include nexa.api.bc11Application
            include nexa.api.bc11Domain
            include nexa.api.bc11Persistence
            include nexa.postgresql
            autolayout lr
        }

        styles {
            element "Person" {
                shape person
                background #084C61
                color #FFFFFF
            }
            element "Software System" {
                background #177E89
                color #FFFFFF
            }
            element "Container" {
                background #DB3A34
                color #FFFFFF
            }
            element "Component" {
                background #6D597A
                color #FFFFFF
            }
            element "Database" {
                shape cylinder
                background #5E548E
                color #FFFFFF
            }
            element "Storage" {
                shape cylinder
                background #5E548E
                color #FFFFFF
            }
        }
    }
}
