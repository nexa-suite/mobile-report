# Legacy Evidence Provenance Ledger

> Internal reproducibility record for Chapter I and Chapter II. This ledger is
> an evidence-control aid, not a substitute for consent, source review or
> current user research.

## Authority and scope

The historical material below is retained as evidence about an earlier
research exercise. It does not override Statement V4.0, the canonical Nexa
model or the current report. In particular, the legacy seven-context DDD,
C4/UML/DB diagrams, old segment names and old product scope are not current
decisions.

Current authority remains the report's accepted product and domain material,
with exactly these eleven Bounded Contexts:

`BC-01 Tenant & Access Governance`, `BC-02 Customer & Buyer Relationships`,
`BC-03 Catalog & Commercial Policy`, `BC-04 Sales Commitment`,
`BC-05 Inventory Availability`, `BC-06 Fulfillment & Delivery`,
`BC-07 Credit & Receivables`, `BC-08 Payments`, `BC-09 Business Documents`,
`BC-10 Notifications`, and `BC-11 Business Traceability`.

Mobile remains a product projection and surface. It is not a Bounded Context.

## Reproducible source manifest

| Field | Value |
| :--- | :--- |
| Historical repository | [`upc-pre-202610-1asi0730-12242-king/nexa-ecosystem-report`](https://github.com/upc-pre-202610-1asi0730-12242-king/nexa-ecosystem-report) |
| Historical source revision | `e161fe522023bfe5929e76c4d7c66af211884b7e` |
| Local curated snapshot | `/Users/diegosandoval284/Developer/nexa-legacy` |
| Local report source | `/Users/diegosandoval284/Developer/nexa-legacy/01-product` |
| Inspection date | `2026-09-06` |
| Original report paths | `report/10-chapter-1-introduction/1-2-solution-profile.md`; `report/10-chapter-1-introduction/1-3-target-segments.md`; `report/20-chapter-2-requirements-elicitation/2-1-competitors.md`; `report/20-chapter-2-requirements-elicitation/2-2-interviews.md`; `report/20-chapter-2-requirements-elicitation/2-3-needfinding.md` |
| Curated local interview source | `01-product/requirements/elicitation/2-2-interviews.md` |
| Curated local visual source | `01-product/research/visuals/interviews/` |
| Publication status | `REVIEW_BEFORE_REPUBLICATION` |

Source-file checksums from the curated snapshot:

| Local file | SHA-256 |
| :--- | :--- |
| `01-product/strategy/report-introduction/1-2-solution-profile.md` | `9e54db37e4ef32fa6fa98879560ad4ff6213053d795c2eb48386900a92d6bc2b` |
| `01-product/strategy/report-introduction/1-3-target-segments.md` | `932d447c1716ab549f981bad9fcb378076b6ffc828538de3d0ebdfa92303dfd` |
| `01-product/requirements/elicitation/2-1-competitors.md` | `51706f80663b71ef7417f64a0d41117fed606baebb1f9307582e975e4aa1ee4d` |
| `01-product/requirements/elicitation/2-2-interviews.md` | `29eeb00180ba62e1b117b07eb2b6d7e5c9e1a0065d01395e1f0d00eb904a5e97` |
| `01-product/requirements/elicitation/2-3-needfinding.md` | `58456d578cd3900b3e78c88d3c943a45d3189d02fcfb829e1ccd290e79652b73` |

Commands and checks used:

```text
rg --files /Users/diegosandoval284/Developer/nexa-legacy
shasum -a 256 <source-file>
file <interview-image>
curl -L -s -o /dev/null -w '%{http_code} %{url_effective}\n' <source-link>
```

The five source GitHub Markdown blobs and the checked historical links
returned HTTP 200 during this inspection. HTTP availability does not prove
identity, consent, content or current validity.

## Verifiable counts and denominator

The historical interview file records **8 profiles**: **3 old S1 Commercial
Coordination**, **3 old S2 Operations / Account Owner**, and **2 old S3 B2B
Buyer Portal**. Therefore the candidate package for historical S1/S3 reuse is
**5 records** (S1: 3; S3: 2). The current mobile campaign has **0 verified
records** in every current segment.

| Set | S1 | S2 | S3 | Interpretation |
| :--- | ---: | ---: | ---: | :--- |
| Historical source records | 3 | 3 | 2 | Source-stated profiles; not a current campaign |
| Candidate historical S1/S3 package | 3 | — | 2 | Facts may inform current questions after review |
| Current course campaign verified | 0 | 0 | 0 | No current interview is claimed here |
| Required new campaign | 3–5 | 3–5 | 3–5 | S2 requires primary research; S3 needs at least one additional current participant if no sixth source record is recovered |

Old S2 records remain historical context only. They do not satisfy the
current `S2 — Physical Operations & Delivery` sample. No sixth S1/S3 record
was recovered in the inspected source package; no record is invented.

## Artifact translation register

Classification values are controlled: `REUSE EXACT FACT`, `ADAPT NARRATIVE`,
`HISTORICAL CONTEXT ONLY`, `SUPERSEDED`, and `REJECT`.

| Legacy artifact | Source path at pinned revision | Current destination | Classification | Reason and evidence status |
| :--- | :--- | :--- | :--- | :--- |
| Solution profile: research/problem framing | `report/10-chapter-1-introduction/1-2-solution-profile.md` | [1.2.1 Background and Problem](../../01-presentation/1.2-solution-profile/1.2.1-background-and-problem.md); Lean UX files | `ADAPT NARRATIVE` | Historical qualitative framing may inform wording. Current problem, hypotheses and scope remain report-owned; no historical claim is presented as current validation. |
| Target segments | `report/10-chapter-1-introduction/1-3-target-segments.md` | [1.3 Target Segments](../../01-presentation/1.3-target-segments/target-segments.md) | `ADAPT NARRATIVE` | Old S1 field dimension and old S3 trust/status observations can inform current research. Old S2 account-owner scope is not current S2. |
| Interview records | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | [2.2.2 Interview Records](../../02-requirements-and-software-solution-design/2.2-interviews/2.2.2-interview-records.md) | `ADAPT NARRATIVE` | Five S1/S3 source records are transcribed as historical candidates with identity, consent and link gates. They are not counted as current records. |
| Interview analysis | `report/20-chapter-2-requirements-elicitation/2-2-interviews.md` | [2.2.3 Interview Analysis](../../02-requirements-and-software-solution-design/2.2-interviews/2.2.3-interview-analysis.md) | `ADAPT NARRATIVE` | Source-stated observations are separated from current hypotheses and percentages are not reused as current validation. |
| Needfinding artifacts | `report/20-chapter-2-requirements-elicitation/2-3-needfinding.md` | Future Annex B / current owner-controlled needfinding area | `HISTORICAL CONTEXT ONLY` | Source may locate old personas, task matrices and journeys; current owner scope does not publish them here without source and identity review. |
| Competitor descriptions | `report/20-chapter-2-requirements-elicitation/2-1-competitors.md` | Current competitor work, if separately reverified | `HISTORICAL CONTEXT ONLY` | Riqra, Drivin, OnTracking/RedGPS and Defontana descriptions are dated; no current market claim is copied. |
| Legacy DDD, C4, UML and DB model | Legacy report architecture sections and binaries | None | `SUPERSEDED` | Conflicts with current canonical 11 BC and must not be migrated. |
| Historical video package | OneDrive/SharePoint links in source interview records | Individual links retained in [2.2.2](../../02-requirements-and-software-solution-design/2.2-interviews/2.2.2-interview-records.md) | `REUSE EXACT FACT` | URLs returned HTTP 200 on inspection; content, identity, permissions and consent remain human-review queue. |
| Historical interview captures | `01-product/research/visuals/interviews/*.jpeg` | [Annex A legacy capture](../annex-a-student-outcome/legacy-interviews/lorena-silva.jpeg) | `ADAPT NARRATIVE` | Three captures copied byte-for-byte and hashed below. Captures are not identity proof; publication permission remains open. |

## Participant-level ledger: candidate S1/S3 package

All summaries below preserve source wording as descriptive historical facts;
they are not current user quotes, validated needs or requirements.

| ID / source segment | Source participant and trace | Candidate use now | Evidence and unresolved gate |
| :--- | :--- | :--- | :--- |
| `LEGACY-S1-01` / Commercial Coordination | Lorena Vanesa Silva Leca; 42; Chorrillos; Android/Windows; Google Chrome; WhatsApp, Excel, ERP's; `0:00:05–0:26:05` (26:01). Individual: [`https://cutt.ly/3t7J9Nja`](https://cutt.ly/3t7J9Nja). Consolidated: [`https://cutt.ly/Ct7JM0DK`](https://cutt.ly/Ct7JM0DK). | `ADAPT NARRATIVE`: field coordination, messaging dependence, manual stock/credit checks, latency/availability questions. | Source capture copied to [lorena-silva.jpeg](../annex-a-student-outcome/legacy-interviews/lorena-silva.jpeg), SHA-256 `95286d096c49d35724d4fefe00c2ab099e50f9851254c22bf9012a8cb3bc94ad`. Link HTTP 200 observed; identity, date, consent and publication permission pending. |
| `LEGACY-S1-02` / Commercial Coordination | Cinthia Paola Levano Asca; 39; Lurín; Android/Windows; Chrome/Edge; WhatsApp, email, phone, Excel, ERP's; `0:26:06–0:47:05` (20:59). Individual: [`https://cutt.ly/9t7J37nn`](https://cutt.ly/9t7J37nn). Consolidated: [`https://cutt.ly/Ct7JM0DK`](https://cutt.ly/Ct7JM0DK). | `HISTORICAL CONTEXT ONLY` until identity is resolved; source reports fragmented Trello/WhatsApp/Excel, imprecise stock, manual supervisor check and desire for simpler order capture. | Source capture is not copied: visual label reads **“César Marín”**, not the source record name. Link HTTP 200 observed; identity, date, consent and permission pending. |
| `LEGACY-S1-03` / Commercial Coordination | Celia Pérez Huaman; 51; San Miguel; Android/Windows; Microsoft Edge; WhatsApp, phone, Excel; `0:47:06–1:04:01` (16:55). Individual link is blank in source. Consolidated: [`https://cutt.ly/Ct7JM0DK`](https://cutt.ly/Ct7JM0DK). | `ADAPT NARRATIVE` only for field usability, performance/connectivity and duplicate-data questions; not a current validation. | Source capture copied to [celia-perez.jpeg](../annex-a-student-outcome/legacy-interviews/celia-perez.jpeg), SHA-256 `2d338a7f86549ea5a4f81c9de0d8b26c47b32732fc15acb093f02a73740b049f`. Individual link missing; identity, date, consent and permission pending. |
| `LEGACY-S3-01` / B2B Buyer Portal | Pedro Puente Arnao; 56; San Isidro; iOS/MacOS; Safari/Chrome; WhatsApp, phone, Excel, Yape, TikTok; `2:12:08–2:24:34` (12:26). Individual: [`https://cutt.ly/Tt7J7pEx`](https://cutt.ly/Tt7J7pEx). Consolidated: [`https://cutt.ly/Ct7JM0DK`](https://cutt.ly/Ct7JM0DK). | `ADAPT NARRATIVE`: delivery-arrival uncertainty, handoff/receipt evidence, discrepancy and human-support questions. Old catalog/order/payment claims are not imported into Mobile V1. | Source capture copied to [pedro-puente.jpeg](../annex-a-student-outcome/legacy-interviews/pedro-puente.jpeg), SHA-256 `5a2bbe177688db079e6a02bfc9f7bda445109efe47afa8e258cfc0e73040768a`. Link HTTP 200 observed; identity, date, consent and permission pending. |
| `LEGACY-S3-02` / B2B Buyer Portal | Henrry García Robles; 49; San Borja; Android/Windows; Google Chrome; WhatsApp, phone, Excel, Yape; `2:24:35–2:40:00` (15:25). Individual: [`https://cutt.ly/yt7J7RTk`](https://cutt.ly/yt7J7RTk). Consolidated: [`https://cutt.ly/Ct7JM0DK`](https://cutt.ly/Ct7JM0DK). | `HISTORICAL CONTEXT ONLY` until identity is resolved; source reports trust, human support and bounded use of dispatch/GPS technology. | Source capture is not copied: visual label reads **“Piero García Campos”**, not the source record name. Link HTTP 200 observed; identity, date, consent and permission pending. |

## Old S2 records: context only

These records are retained to make the denominator auditable, not to fill the
current `S2 — Physical Operations & Delivery` sample.

| ID | Source record | Timing | Classification |
| :--- | :--- | :--- | :--- |
| `LEGACY-S2-01` | Hilda Litano Ramos; 47; Villa El Salvador; Android/Windows; Chrome; ERP, WhatsApp, phone, Excel. | `1:04:07–1:19:39` (15:32); [`https://cutt.ly/Dt7J4i85`](https://cutt.ly/Dt7J4i85) | `HISTORICAL CONTEXT ONLY` |
| `LEGACY-S2-02` | Edith Taype Peñaloza; 49; Callao; Android/Windows; Chrome; ERP, WhatsApp, phone, Excel. | `1:19:40–1:51:08` (31:28); [`https://cutt.ly/2t7J4Akh`](https://cutt.ly/2t7J4Akh) | `HISTORICAL CONTEXT ONLY` |
| `LEGACY-S2-03` | Jesica Maria Sandoval Romero; 48; Jesús María; iOS/MacOS; Safari/Chrome; ERP, phone, Excel. | `1:51:09–2:12:02` (20:54); [`https://cutt.ly/bt7J42QX`](https://cutt.ly/bt7J42QX) | `HISTORICAL CONTEXT ONLY` |

The old S2 material can suggest questions about documents, expiry, FEFO,
temperature and operational controls. It cannot prove current driver behavior,
delivery handoff, POD acceptance, connectivity or safety requirements.

## Copied and rejected visual assets

| Asset | Source path | SHA-256 | Destination / decision | Reason |
| :--- | :--- | :--- | :--- | :--- |
| `lorena-silva.jpeg` | `01-product/research/visuals/interviews/lorena-silva.jpeg` | `95286d096c49d35724d4fefe00c2ab099e50f9851254c22bf9012a8cb3bc94ad` | `../annex-a-student-outcome/legacy-interviews/lorena-silva.jpeg` | Copied byte-for-byte; historical capture only; permission review open. |
| `celia-perez.jpeg` | `01-product/research/visuals/interviews/celia-perez.jpeg` | `2d338a7f86549ea5a4f81c9de0d8b26c47b32732fc15acb093f02a73740b049f` | `../annex-a-student-outcome/legacy-interviews/celia-perez.jpeg` | Copied byte-for-byte; no individual link in source; identity and permission review open. |
| `pedro-puente.jpeg` | `01-product/research/visuals/interviews/pedro-puente.jpeg` | `5a2bbe177688db079e6a02bfc9f7bda445109efe47afa8e258cfc0e73040768a` | `../annex-a-student-outcome/legacy-interviews/pedro-puente.jpeg` | Copied byte-for-byte; historical capture only; permission review open. |
| `cinthia-levano.jpeg` | `01-product/research/visuals/interviews/cinthia-levano.jpeg` | `807b0b5308d87673b7e0827dfe3e45b941cf931874542cc2bbe4a0f7ed94f3da` | None | `REJECT` for republication in this cut: visible label “César Marín” conflicts with record name. |
| `henrry-garcia.jpeg` | `01-product/research/visuals/interviews/henrry-garcia.jpeg` | `62105691695e1b4cf45f166835e73ecbf40bfa8613f70f6e8dfdb17000bc1f8e` | None | `REJECT` for republication in this cut: visible label “Piero García Campos” conflicts with record name. |

The remaining three old S2 captures are not copied because those records are
outside the current reusable S1/S3 package. The source retains their paths and
links above for audit only.

## Evidence queue

`RESEARCH_PENDING` is an internal queue state. It must not be rendered as a
finding, quote, percentage or acceptance claim.

| Queue item | Required proof | Owner / destination |
| :--- | :--- | :--- |
| Identity and consent for `LEGACY-S1-01`, `LEGACY-S1-03`, `LEGACY-S3-01` | Human review of video, participant mapping, date, consent and publication permission | Research reviewer; update this ledger and Annex A |
| Identity mismatch `LEGACY-S1-02` | Resolve “César Marín” versus “Cinthia Paola Levano Asca” before any image or quote use | Research reviewer; keep record historical-only until resolved |
| Identity mismatch `LEGACY-S3-02` | Resolve “Piero García Campos” versus “Henrry García Robles” before any image or quote use | Research reviewer; keep record historical-only until resolved |
| Missing individual link `LEGACY-S1-03` | Recover source link or record why it cannot be recovered | Research reviewer; do not invent URL |
| Historical video contents | Human inspection of the HTTP-available OneDrive/SharePoint assets and timing | Research reviewer; preserve original Cutt.ly URLs |
| New S2 evidence | Recruit and review 3–5 current `S2 — Physical Operations & Delivery` participants | Current 2.2 campaign |
| Additional S3 evidence | Recruit and review at least one current S3 participant if no sixth source record is recovered | Current 2.2 campaign |
| Current competitor evidence | Reverify current claims with dated authoritative sources | Current competitor owner; not supplied by this ledger |

Until queue items close, historical material can orient questions and preserve
provenance, but cannot be described as current Mobile validation.
