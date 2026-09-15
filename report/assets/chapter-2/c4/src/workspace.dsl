workspace "Nexa Chapter 02" "C4 views for the Chapter 02 domain design" {
    !identifiers hierarchical

    model {
        interestedCompany = person "Interested Company Representative" "Requests an organizational relationship with Nexa."
        onboardingStaff = person "Nexa Onboarding Staff" "Approves company onboarding."
        tenantWorkforce = person "Tenant Workforce" "Company Owner, Tenant Administrator, sales, warehouse, dispatch and delivery roles."
        customerBuyer = person "Customer Buyer" "Requests, receives and reviews B2B commitments."

        paymentProvider = softwareSystem "Payment Provider" "External payment processing service."
        emailDeliveryService = softwareSystem "Email Delivery Service" "External email delivery service."
        pushDeliveryService = softwareSystem "Push Delivery Service" "Provider-neutral external push delivery service."
        mapsProvider = softwareSystem "Maps & Geolocation Provider" "External navigation and geolocation service."

        nexa = softwareSystem "Nexa" "Multi-tenant B2B SaaS for commercial commitments, inventory availability, fulfillment and delivery." {
            website = container "Nexa Website" "Public product discovery and relationship intake." "Static web application"
            platform = container "Nexa Platform" "Authenticated workforce experience." "Angular 22 SPA"
            buyerPortal = container "Nexa Buyer Portal" "Authenticated B2B Buyer experience." "Angular 22 SPA"
            operationsMobile = container "Operations Mobile" "Field workforce surface for warehouse, dispatch and delivery. It consumes authorized API contracts and retains only permitted non-authoritative local state." "Mobile client; Android/Kotlin and Flutter/Dart are evaluated tracks"
            buyerMobile = container "Buyer Mobile" "Buyer mobile surface for purchase, tracking, receipt, discrepancy and authorized tasks. It consumes authorized API contracts and has no business authority." "Mobile client; Android/Kotlin and Flutter/Dart are evaluated tracks"
            api = container "Nexa API" "Authoritative application and domain behavior, tenant enforcement and persistence orchestration." "Java 25 / Spring Boot 4.1 / Spring Modulith" {
                bc01Interface = component "Tenant Access API" "Receives onboarding, tenant, membership and role commands with server-side scope checks." "Spring MVC / REST"
                bc01Application = component "Tenant Onboarding and Access Application" "Runs provisioning, activation, membership assignment and access-evaluation use cases." "Java 25 / Spring Modulith application services"
                bc01Domain = component "Tenant Access Domain" "Enforces Tenant, Workspace, HumanIdentity, WorkforceMembership and RoleDefinition invariants." "Java 25 domain model"
                bc01Persistence = component "Tenant Access Persistence" "Maps governance roots and enforces scoped PostgreSQL access." "Spring Data JPA / PostgreSQL"

                bc02Interface = component "Customer Relationship API" "Receives customer-account and Buyer Relationship commands and queries." "Spring MVC / REST"
                bc02Application = component "Customer Relationship Application" "Runs account lifecycle, relationship approval and eligibility use cases." "Java 25 / Spring Modulith application services"
                bc02Domain = component "Customer Relationship Domain" "Enforces CustomerAccount and BuyerRelationship lifecycle rules." "Java 25 domain model"
                bc02Persistence = component "Customer Relationship Persistence" "Maps account, relationship and immutable history records." "Spring Data JPA / PostgreSQL"

                bc03Interface = component "Catalog and Offer API" "Receives catalog administration commands and authorized offer queries." "Spring MVC / REST"
                bc03Application = component "Catalog and Offer Application" "Runs product, SKU, policy lifecycle and offer-resolution use cases." "Java 25 / Spring Modulith application services"
                bc03Domain = component "Catalog Commercial Policy Domain" "Enforces Product, SKU, price, terms, promotion and snapshot rules." "Java 25 domain model"
                bc03Persistence = component "Catalog Commercial Policy Persistence" "Maps catalog and policy roots plus authorized media references." "Spring Data JPA / PostgreSQL"

                bc04Interface = component "Commercial Request and Order API" "Receives request submission, direct-order and SalesOrder commands." "Spring MVC / REST"
                bc04Application = component "Sales Commitment Application" "Coordinates commercial intent, commitment establishment and synchronous decisions." "Java 25 / Spring Modulith application services"
                bc04Domain = component "Sales Commitment Domain" "Enforces RequestDraft, PurchaseRequest, CommercialCommitment and SalesOrder rules." "Java 25 domain model"
                bc04Persistence = component "Sales Commitment Persistence" "Maps commercial roots, snapshots and durable publication state." "Spring Data JPA / PostgreSQL"

                bc05Interface = component "Inventory Availability API" "Receives availability, reservation, allocation, movement and transfer commands." "Spring MVC / REST"
                bc05Application = component "Inventory Protection Application" "Runs authoritative reservation, backing, allocation, movement and transfer use cases." "Java 25 / Spring Modulith application services"
                bc05Domain = component "Inventory Availability Domain" "Enforces inventory position, lot, reservation, backing, allocation and FEFO rules." "Java 25 domain model"
                bc05Persistence = component "Inventory Availability Persistence" "Maps inventory roots with locking and conditional-write support." "Spring Data JPA / PostgreSQL"

                bc06Interface = component "Fulfillment and Delivery API" "Receives fulfillment, delivery, POD and evidence commands." "Spring MVC / REST"
                bc06Application = component "Fulfillment Delivery Application" "Runs picking, delivery lifecycle, receipt, discrepancy and evidence use cases." "Java 25 / Spring Modulith application services"
                bc06Domain = component "Fulfillment Delivery Domain" "Enforces Fulfillment, Delivery, ProofOfDelivery and TemperatureEvidence rules." "Java 25 domain model"
                bc06Persistence = component "Fulfillment Delivery Persistence" "Maps execution roots and evidence metadata." "Spring Data JPA / PostgreSQL"

                bc07Interface = component "Credit and Receivable API" "Receives credit, receivable and financial-adjustment commands." "Spring MVC / REST"
                bc07Application = component "Credit Exposure Application" "Runs credit reservation, receivable issuance and payment-application use cases." "Java 25 / Spring Modulith application services"
                bc07Domain = component "Credit Receivables Domain" "Enforces CreditAccount, CreditReservation, Receivable and FinancialAdjustment rules." "Java 25 domain model"
                bc07Persistence = component "Credit Receivables Persistence" "Maps financial roots and durable payment-fact intake state." "Spring Data JPA / PostgreSQL"

                bc08Interface = component "Payment and Provider Webhook API" "Receives payment commands and authenticated provider callbacks." "Spring MVC / REST / webhook"
                bc08Application = component "Payment Reconciliation Application" "Runs reported-payment, translated-result, reconciliation and fact-publication use cases." "Java 25 / Spring Modulith application services"
                bc08Domain = component "Payments Domain" "Enforces Payment and PaymentReconciliationCase lifecycle rules." "Java 25 domain model"
                bc08Persistence = component "Payments Persistence and Inbox" "Maps payment roots and provider-event deduplication state." "Spring Data JPA / PostgreSQL"
                bc08ProviderAcl = component "Payment Provider Anti-Corruption Adapter" "Verifies provider signatures, translates payloads and performs provider I/O." "Java 25 / Spring integration adapter"

                bc09Interface = component "Business Document API" "Receives authorized document query, issue and replacement commands." "Spring MVC / REST"
                bc09Application = component "Document Issuance Application" "Runs issuance, durable generation and revision use cases." "Java 25 / Spring Modulith application services"
                bc09Domain = component "Business Documents Domain" "Enforces immutable document and number-series rules." "Java 25 domain model"
                bc09Persistence = component "Business Documents Persistence" "Maps document roots, number series and generation work state." "Spring Data JPA / PostgreSQL"
                bc09StorageAdapter = component "Document Rendering and Storage Adapter" "Renders documents and stores authorized bytes through application ports." "Java 25 / Spring integration adapter"

                bc10Interface = component "Notification Preference and Fact API" "Receives preference, subscription and published-fact intake requests." "Spring MVC / REST / message consumer"
                bc10Application = component "Notification Dispatch Application" "Runs notification creation, dispatch, retry and delivery-result use cases." "Java 25 / Spring Modulith application services"
                bc10Domain = component "Notifications Domain" "Enforces notification, template, preference and secure subscription rules." "Java 25 domain model"
                bc10Persistence = component "Notifications Persistence and Inbox" "Maps notification roots, protected endpoint references and fact deduplication state." "Spring Data JPA / PostgreSQL"
                bc10DeliveryAdapter = component "Email and Push Delivery Adapter" "Performs email and provider-neutral push I/O outside the domain model." "Java 25 / Spring integration adapter"

                bc11Interface = component "Traceability Query and Fact Consumer" "Receives authorized timeline queries and durable business facts." "Spring MVC / REST / message consumer"
                bc11Application = component "Traceability Append Application" "Deduplicates facts, appends records and serves authorized timeline projections." "Java 25 / Spring Modulith application services"
                bc11Domain = component "Business Traceability Domain" "Enforces append-only business-fact and evidence-reference rules." "Java 25 domain model"
                bc11Persistence = component "Traceability Append Persistence" "Maps append-only records and local deduplication state." "Spring Data JPA / PostgreSQL"
                bc11ProjectionAdapter = component "Traceability Fact Intake Adapter" "Consumes durable integration facts before application deduplication." "Java 25 / Spring integration adapter"
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
        nexa -> pushDeliveryService "Uses provider-neutral push delivery"
        nexa -> mapsProvider "Uses navigation services"

        nexa.website -> nexa.api "Submits public intake"
        nexa.platform -> nexa.api "Uses authorized workforce contracts"
        nexa.buyerPortal -> nexa.api "Uses authorized Buyer contracts"
        tenantWorkforce -> nexa.operationsMobile "Uses field-work capabilities"
        customerBuyer -> nexa.buyerMobile "Uses Buyer mobile capabilities"
        nexa.operationsMobile -> nexa.api "Uses authorized API contracts over HTTPS"
        nexa.buyerMobile -> nexa.api "Uses authorized API contracts over HTTPS"
        nexa.api -> nexa.postgresql "Reads and writes owned records"
        nexa.api -> nexa.objectStorage "Stores authorized bytes through ports"
        nexa.api -> paymentProvider "Uses translated payment contracts"
        nexa.api -> emailDeliveryService "Uses notification delivery contracts"
        nexa.api -> pushDeliveryService "Uses provider-neutral push contracts"
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
        nexa.api.bc04Application -> nexa.api.bc06Application "Publishes confirmed SalesOrder facts"

        nexa.api.bc05Interface -> nexa.api.bc05Application "Invokes"
        nexa.api.bc05Application -> nexa.api.bc05Domain "Coordinates"
        nexa.api.bc05Application -> nexa.api.bc05Persistence "Reads and writes"
        nexa.api.bc05Persistence -> nexa.postgresql "Uses owned records"
        nexa.api.bc05Application -> nexa.api.bc06Application "Publishes PhysicalAllocation facts"

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
        nexa.api.bc08Application -> nexa.api.bc09Application "Publishes payment facts"
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
        nexa.api.bc10DeliveryAdapter -> pushDeliveryService "Delivers push notifications"
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
            operationsMobileDevice = deploymentNode "Operations Mobile Device" "Runs the installed Operations Mobile application for field work." "Mobile device" {
                operationsMobileInstance = containerInstance nexa.operationsMobile
            }
            buyerMobileDevice = deploymentNode "Buyer Mobile Device" "Runs the installed Buyer Mobile application for authorized Buyer work." "Mobile device" {
                buyerMobileInstance = containerInstance nexa.buyerMobile
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
            include pushDeliveryService
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
            include nexa.operationsMobile
            include nexa.buyerMobile
            include nexa.api
            include nexa.postgresql
            include nexa.objectStorage
            include paymentProvider
            include emailDeliveryService
            include pushDeliveryService
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
            include pushDeliveryService
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
