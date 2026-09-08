# Chapter II — C4 Manual Visual Review Guide

## Purpose

Use this guide for the Owner's manual visual review. Structurizr DSL remains the
semantic authority; this checklist evaluates presentation and evidence of the
existing report assets. Do not create a new C4 model from this checklist.

For every image, record one decision only after inspection:

- `KEEP`: current asset is readable and semantically aligned.
- `RE-EXPORT`: canonical view is correct but the asset needs a fresh export.
- `REDESIGN PRESENTATION`: readability or layout needs deliberate visual work.

## Context Level

### V1 TARGET system context

- Canonical view key: `Nexa-SystemContext-V1-TARGET`.
- Current report asset: `report/assets/chapter-2/c4/Nexa-SystemContext-V1-TARGET.png`.
- Source companion: `report/assets/chapter-2/c4/Nexa-SystemContext-V1-TARGET.svg`.

Checklist:

- [ ] Nexa is centered as one B2B SaaS system.
- [ ] Accepted actors are present and distinct.
- [ ] Only `Payment Provider`, `Email Delivery Service` and `Maps & Geolocation Provider` appear as external systems.
- [ ] PostgreSQL, API internals and Bounded Contexts do not appear in L1.
- [ ] Labels and relationship directions are readable.
- [ ] V1 TARGET is visible.
- [ ] Operations Mobile and Buyer Mobile are identified as planned/proposed projections.
- [ ] No FUTURE-only integration leaks into V1.

### AS-IS and Future semantic companions

- Canonical views: `Nexa-SystemContext-ASIS`, `Nexa-SystemContext-Future-Runway`.
- Current report asset policy: the report may keep the V1 TARGET export selected; do not imply that absent AS-IS/Future images are implementation evidence.
- [ ] If an additional image is inserted, record its exact canonical view key and state.

Manual decision: `KEEP / RE-EXPORT / REDESIGN PRESENTATION`: ______

## Container Level

- Canonical views: `Nexa-Containers-ASIS`, `Nexa-Containers-V1-TARGET`.
- Current report asset: `report/assets/chapter-2/c4/Nexa-Containers-V1-TARGET.png`.
- Source companion: `report/assets/chapter-2/c4/Nexa-Containers-V1-TARGET.svg`.

Checklist:

- [ ] Six AS-IS containers are visible: Nexa Website, Nexa Platform, Nexa Buyer Portal, Nexa API, PostgreSQL and Object Storage.
- [ ] Only two V1 TARGET Mobile additions are present where intended: Nexa Operations Mobile and Nexa Buyer Mobile.
- [ ] Technology labels match canonical Structurizr source.
- [ ] Responsibilities and communications are readable.
- [ ] Nexa API remains the authoritative application boundary.
- [ ] Mobile clients do not become authoritative backends.
- [ ] A Bounded Context is not presented as a C4 Container.
- [ ] PostgreSQL remains physically shared with logical ownership by context.

Manual decision: `KEEP / RE-EXPORT / REDESIGN PRESENTATION`: ______

## Components Overview

- Canonical selected views: `Nexa-API-IdentityTenantCustomer-TARGET`, `Nexa-API-CommercialInventory-TARGET`, `Nexa-API-FulfillmentDelivery-TARGET` and `Nexa-API-CreditPaymentDocuments-TARGET`.
- Current report assets: `report/assets/chapter-2/c4/Nexa-API-IdentityTenantCustomer-TARGET.png`, `Nexa-API-CommercialInventory-TARGET.png`, `Nexa-API-FulfillmentDelivery-TARGET.png` and `Nexa-API-CreditPaymentDocuments-TARGET.png`.

Checklist:

- [ ] Each selected view corresponds to a canonical L3 view.
- [ ] Components remain inside their parent container.
- [ ] Labels explain system-level responsibility rather than listing Java classes or packages.
- [ ] The selected views help explain the API's responsibility seams.
- [ ] No one-component-diagram-per-BC claim is introduced here; that belongs to 2.6.
- [ ] Component views do not redefine the strategic Context Map.

Manual decision: `KEEP / RE-EXPORT / REDESIGN PRESENTATION`: ______

## Deployment

- Canonical views: `Nexa-Deployment-Local-ASIS`, `Nexa-Deployment-V1-TARGET`.
- Current report asset: `report/assets/chapter-2/c4/Nexa-Deployment-V1-TARGET.png`.
- Source companion: `report/assets/chapter-2/c4/Nexa-Deployment-V1-TARGET.svg`.

Checklist:

- [ ] Local AS-IS and V1 TARGET are clearly distinguished.
- [ ] Nodes and runtime relationships match the canonical source.
- [ ] V1 TARGET Mobile devices are identified as planned projections.
- [ ] No cloud provider, network, secret, backup or availability claim is invented.
- [ ] No FUTURE deployment is described as current.
- [ ] PostgreSQL, Object Storage and Nexa API responsibilities are readable.
- [ ] Physical/runtime layout is legible at report scale.

Manual decision: `KEEP / RE-EXPORT / REDESIGN PRESENTATION`: ______

## Evidence handoff

- [ ] Record one decision for every current asset.
- [ ] If `RE-EXPORT`, use the canonical Structurizr DSL view key.
- [ ] If `REDESIGN PRESENTATION`, preserve semantic content and document the visual change.
- [ ] Do not claim visual acceptance until a human has inspected the final image in the report/PDF.
