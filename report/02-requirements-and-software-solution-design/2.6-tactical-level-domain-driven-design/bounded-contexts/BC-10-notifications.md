# 2.6.11. BC-10 — Notifications

`DOMAIN MODEL: TARGET / ACCEPTED`
`IMPLEMENTATION CROSSWALK: AS-IS VERIFIED / PARTIAL`

Canonical target: Blueprint `01-shared/domain/bounded-contexts/BC-10-notifications/`.
This context owns notification intent, recipient/channel policy, in-app/email
delivery and retry facts. Notification failure never changes source business
state. Mobile delivery is a projection, not a Mobile BC.

## 2.6.11.1 Domain Layer

| Aggregate/root | Boundary and invariant |
| :--- | :--- |
| `Notification` | Intent, recipient/channel selection and lifecycle |
| `NotificationTemplate` | Versioned channel template/content policy |
| `NotificationPreference` | Recipient/channel preference and suppression |
| `PushSubscription` | Target recipient/device delivery record, not a Mobile aggregate |

`NotificationRecipient` and `NotificationAttempt` are notification-owned
facts. Value objects include `NotificationId`, `TemplateKey`, `Channel`,
`DeliveryStatus` and `RecipientReference`; `ChannelSelectionPolicy` and
`RetryPolicy` are domain services. V1 channels are in-app and email; WhatsApp
is external/manual.

Target invariants: delivery is at-least-once with visible deduped attempts;
retry/terminal failure never mutates PR, SO, Payment or Delivery; payloads
exclude secrets/unnecessary PII; subscription rotation and invalid-token
handling remain technical delivery behavior.

## 2.6.11.2 Interface Layer

Target contracts cover notification read/preferences, notification intent,
channel status, subscription lifecycle and worker callbacks. Exact routes or
provider DTOs absent from API evidence are not invented. Source facts enter
through durable outbox/inbox; client acknowledgment is not source confirmation.

## 2.6.11.3 Application Layer

Target handlers consume source facts, persist notification intent, choose
recipient/channel, dispatch, retry and project an in-app view. Lease/fencing,
idempotency and bounded backoff protect duplicate delivery. Source business
state remains owned by its origin BC.

## 2.6.11.4 Infrastructure Layer

Target shared PostgreSQL ownership covers `notification_template`,
`notification`, `notification_recipient`, `notification_preference`,
`notification_attempt` and `push_subscription`. Provider adapters remain ACLs;
no provider or third channel is assumed. Technical outbox/inbox persistence is
shared infrastructure, not a new BC.

AS-IS anchor: API `notifications` application/service/controller paths,
in-app inbox/preferences, push subscription/outbox adapters and migrations
V36/V44/V59/V94–V100 where present at `origin/main`. In-app inbox/preferences
are `AS-IS VERIFIED`; durable intent/attempt and full email retry are `PARTIAL`;
Mobile provider configuration, runtime and Product Acceptance are `NOT EVIDENCED`.

## 2.6.11.5 Bounded Context Software Architecture Component Level Diagrams

The selected logical API family is `Nexa-API-FulfillmentDelivery-TARGET`,
which shows one possible source-event/notification collaboration inside the
single API container. It is not a notification deployment unit.

![BC-10 component family — TARGET](../../../assets/chapter-2/c4/Nexa-API-FulfillmentDelivery-TARGET.png)

The relationship is a target component view; source/export hashes are in the
[provenance register](../../../assets/chapter-2/provenance.md).

## 2.6.11.6 Bounded Context Software Architecture Code Level Diagrams

### 2.6.11.6.1 Bounded Context Domain Layer Class Diagrams

![BC-10 tactical domain model — TARGET](../../../assets/chapter-2/tactical/BC-10/BC10_Notifications.png)

Source: [domain-model.puml](../../../assets/chapter-2/tactical/BC-10/domain-model.puml).

### 2.6.11.6.2 Bounded Context Database Design Diagram

![BC-10 target database projection](../../../assets/chapter-2/tactical/BC-10/database-diagram.png)

Source: [database-diagram.puml](../../../assets/chapter-2/tactical/BC-10/database-diagram.puml).
This is shared-PostgreSQL logical ownership with target delivery constraints;
it does not imply a Mobile database or push provider deployment.

## Crosswalk and open evidence

| Concern | Classification | Evidence boundary |
| :--- | :--- | :--- |
| In-app notification/preference implementation | `AS-IS VERIFIED` | API `notifications` at `origin/main` |
| Intent/attempt/retry target separation | `TARGET / ACCEPTED` | Blueprint tactical model/data model |
| Complete email/push provider and recovery parity | `PARTIAL` | Existing adapters do not prove full target delivery |
| Mobile notification runtime and Product Acceptance | `NOT EVIDENCED` | Mobile remains planned projection |
