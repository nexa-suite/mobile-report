# Chapter II — Domain Story Rendering Guide

## Purpose

Use this guide to complete the five captured Domain Story diagrams requested by
the academic rubric. Mermaid source remains editable in the professor-facing
chapter. This file is internal and must not be exported to the PDF.

## Current source and tooling gate

- Source: `report/02-requirements-and-software-solution-design/2.5-strategic-level-domain-driven-design/2.5.1-eventstorming/2.5.1.2-domain-message-flows-modeling.md`.
- Required source blocks: exactly five `~~~mermaid` blocks.
- Preferred output: deterministic SVG, with PNG only when the PDF path requires it.
- Current gate: check whether a safe deterministic renderer is already available before rendering.
- Do not install arbitrary global tooling and do not fabricate screenshots.

## Five stories and desired assets

| Domain Story | Desired SVG filename | Final insertion location |
| :--- | :--- | :--- |
| Company Onboarding & Authorized Relationship | `company-onboarding-authorized-relationship.svg` | Adjacent to the story in `2.5.1.2-domain-message-flows-modeling.md` |
| Commercial Request / Direct Order to Commitment | `commercial-request-direct-order-commitment.svg` | Adjacent to the story in `2.5.1.2-domain-message-flows-modeling.md` |
| Inventory Backing to Fulfillment to Dispatch | `inventory-backing-fulfillment-dispatch.svg` | Adjacent to the story in `2.5.1.2-domain-message-flows-modeling.md` |
| Delivery to POD to Buyer Receipt | `delivery-pod-buyer-receipt.svg` | Adjacent to the story in `2.5.1.2-domain-message-flows-modeling.md` |
| Payment, Receivable, Document and Traceability | `payment-receivable-document-traceability.svg` | Adjacent to the story in `2.5.1.2-domain-message-flows-modeling.md` |

Approved asset directory: `report/assets/chapter-2/domain-stories/`.

## Render and capture checklist

- [ ] Verify the renderer version and record the exact command in the evidence register.
- [ ] Render each Mermaid block from the current Markdown source.
- [ ] Keep all actor, object, fact, authority and handoff labels intact.
- [ ] Confirm Story 1 keeps separate Supplier/Tenant onboarding and Supplier-Customer relationship lanes.
- [ ] Confirm `Customer Account != Tenant` and `Buyer Relationship != Workforce Membership` remain readable.
- [ ] Confirm no diagram claims Mobile as a Bounded Context.
- [ ] Confirm arrows do not overlap labels.
- [ ] Confirm text is legible at report/PDF scale.
- [ ] Confirm the image is not cropped.
- [ ] Confirm exported SVG does not contain private account data or fabricated workshop metadata.
- [ ] Preserve the Mermaid source even after inserting the image.

## Insert and validate

1. [ ] Add each real SVG reference next to the corresponding story.
2. [ ] Add PNG only if the PDF renderer cannot resolve SVG safely.
3. [ ] Validate every local link.
4. [ ] Review the rendered PDF page manually.
5. [ ] Update the rubric checkpoint with the five actual image paths.

## Completion gate

Domain Story image evidence is complete only when all five stories have a real,
readable capture or deterministic render, every local reference resolves, and a
human confirms visual clarity. Mermaid source alone does not close this gate.
