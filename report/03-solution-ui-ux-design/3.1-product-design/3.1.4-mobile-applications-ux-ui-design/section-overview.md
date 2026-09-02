# 3.1.4 Mobile Applications UX/UI Design

The Mobile target has two surfaces and one domain authority:

| Surface | Primary roles | V1 scope |
| :--- | :--- | :--- |
| Operations Mobile | Mobile User, Warehouse Operator, Dispatch Coordinator, Driver/Delivery Operator | MOB-US-001..003, 011..034 |
| Buyer Mobile | Mobile User, Customer Buyer | MOB-US-001..003, 044, 047..049 |

The following documents define the required states and traceability, but no
rendered Mobile screen, prototype URL, build or physical-device evidence is
claimed in this cut.

## Design Lab-to-Mobile crosswalk — TARGET

The Design Lab supplies reusable visual and interaction evidence. The
crosswalk below records how that evidence informs the Mobile target while
keeping business authority in the API and Blueprint. A source pattern is not a
Mobile implementation and does not close a user story.

| Mobile target concern | Design Lab evidence observed | Target carry-forward | Boundary that remains open |
| :--- | :--- | :--- | :--- |
| Session return and context selection — `MOB-US-001..003` | `src/app/documentation/patterns/authentication/authentication-page.ts`; locale, invalid, authenticating, workspace and success states | Show a safe access sequence, visible status and `en`/`es` copy variants before protected work | Real identity, session, Tenant/Workspace authorization and revocation remain API/runtime evidence |
| Warehouse work and Product/SKU identification — `MOB-US-011..019` | `src/app/documentation/patterns/data-dense-operations/data-dense-operations-page.ts`; search, local scope, rows, loading, error and empty states | Keep dense operational data scannable, scope-limited and recoverable | Inventory, lot/expiry, quantity and manual-fallback rules require Mobile/API evidence and product review |
| Dispatch readiness and handoff — `MOB-US-020..025` | `src/app/documentation/patterns/dispatch-board/dispatch-board-page.ts`; status columns, empty handoff column, action menu and keyboard-equivalent movement | Expose source, destination, current status and a non-drag command path | The specimen performs no persisted transition; handoff authorization, idempotency and history remain open |
| Delivery execution and proof — `MOB-US-026..034` | `src/app/documentation/patterns/delivery-pod/delivery-pod-page.ts`; pending/received proof and receiver/time/document detail | Separate attempt, outcome, proof pending and confirmed states | Driver outcome, POD, evidence upload, device permissions and server confirmation remain unverified |
| Buyer receipt and discrepancy — `MOB-US-044, 047..049` | `src/app/documentation/patterns/async-operations/async-operations-page.ts`; processing, error, retry, warning and cancellation sequence | Keep unknown results visible and make retry/cancel decisions explicit | Buyer relationship, handoff code, received quantities and immutable discrepancy facts require domain/API evidence |
| Responsive and inclusive behavior — all target flows | `src/app/documentation/patterns/responsive-composition/responsive-composition-page.ts` and Design Lab quality routes | Preserve hierarchy at 1440, 1024, 768, 390 and 320px; retain labels, focus equivalents and local data overflow | Design Lab browser evidence is not a physical Mobile device, assistive-technology or final UX review |

### Adoption decisions

1. Future Mobile screens use semantic and component aliases from the recorded
   token layers; raw values are not copied per screen.
2. State language keeps `Delivery outcome`, `Buyer Receipt`, `Proof of
   Delivery`, `Notification` and `Business Traceability` distinct.
3. Drag-and-drop is never the only path; commands need an accessible direct
   equivalent and a visible result.
4. English remains the default product language. The observed Design Lab
   `en`/`es` specimens guide copy review, but `en_US` and `es_419` catalogs,
   pluralization and Mobile runtime behavior remain to be produced.
5. The final wireframes, mock-ups, wireflows, user flows and prototype must
   record their own source file, revision, viewport, state and reviewer.

Current status: `SOURCE OBSERVED / TARGET RECONCILED / MOBILE RENDER AND
HUMAN REVIEW PENDING`.

- [Wireframes](./3.1.4.1-mobile-application-wireframes.md)
- [Wireflows](./3.1.4.2-mobile-application-wireflows.md)
- [Mock-ups](./3.1.4.3-mobile-application-mockups.md)
- [User flows](./3.1.4.4-mobile-application-user-flows.md)
- [Prototyping](./3.1.4.5-mobile-application-prototyping.md)
