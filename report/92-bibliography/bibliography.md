# Bibliography

## Research protocol and status

The bibliography is organized in APA 7 and separates domain research from
Mobile engineering/design research. The current date of the report cut is
2026-09-02; the candidate papers below fall within the two-year window.

They have verified title, authors, year, journal, volume/article number and DOI
from publisher or scholarly-record pages. The Q1/Q2 classification is
`PRELIMINARY` until the team attaches an official Scopus or Web of Science
quartile capture for the relevant year and category. Therefore this section is
not yet a closed rubric gate.

On 2026-09-01 a public metric cross-check was recorded for the four journals.
It is useful for provenance, but it is not the official Scopus/Web of Science
capture required by the rubric and does not change the state below.

## Domain candidates

**[D1]** Mustafa, M. F. M. S., Navaranjan, N., & Demirovic, A. (2024). Food
cold chain logistics and management: A review of current development and
emerging trends. *Journal of Agriculture and Food Research, 18*, 101343.
https://doi.org/10.1016/j.jafr.2024.101343

Use in the report: identifies current cold-chain research clusters and gaps in
practical application and human factors. It informs the S2 research plan; it
does not establish a Nexa requirement or acceptance result.

**[D2]** Zhou, X., Tang, J., Jacobs, T. L., & Saguy, I. S. (2025). Transforming
food supply chains through digital tracking and monitoring technologies.
*Trends in Food Science & Technology, 163*, 105142.
https://doi.org/10.1016/j.tifs.2025.105142

Use in the report: informs the distinction between product tracking,
time-temperature/freshness monitoring and operational traceability. It does
not authorize live tracking, IoT or a new Bounded Context in Mobile V1.

## Secondary research sources for Physical Operations and Delivery

These sources support the S2 research plan and the formulation of interview
questions. They are not substitutes for the four rubric candidates, do not
establish Nexa requirements and do not close the Q1/Q2 verification gate.

**[SR1]** GS1. (n.d.). *GS1 global traceability standard*. Retrieved September
2, 2026, from
https://www.gs1.org/standards/gs1-global-traceability-standard/current-standard

Use in the report: provides context for Critical Tracking Events, Key Data
Elements and the Who/What/Where/When/Why dimensions when asking about custody
and delivery handoffs. It does not define Nexa's Proof of Delivery contract.

**[SR2]** World Health Organization. (2022, April 11). *How to temperature map
cold chain equipment and storage areas (second edition)*.
https://www.who.int/publications/i/item/9789240042773

Use in the report: provides a documented temperature-mapping procedure as
methodological context. It does not transfer vaccine-specific thresholds,
tools or acceptance rules to Nexa products.

**[SR3]** De Lombaert, T., Braekers, K., De Koster, R., & Ramaekers, K. (2024).
What makes order picking so physically demanding? — Ergonomic evidence from a
large-scale lab experiment using subjective metrics. *IFAC-PapersOnLine, 58*(19),
181–186. https://doi.org/10.1016/j.ifacol.2024.09.139

Use in the report: informs questions about physical load, shelf height, product
weight, product quantity and device interaction in warehouse tasks. It is
contextual evidence, not evidence about Nexa users or product acceptance.

## Mobile engineering and UX candidates

**[M1]** Ilhan, A. E. (2025). Design approaches to improve user experience: An
example of a mobile app prototyping process. *International Journal of
Human-Computer Studies, 203*, 103569.
https://doi.org/10.1016/j.ijhcs.2025.103569

Use in the report: supports documenting design decisions, prototypes and
usability considerations as an explicit process rather than treating a static
screen as validation.

**[M2]** Maqbool, B., & Herold, S. (2024). Potential effectiveness and efficiency
issues in usability evaluation within digital health: A systematic literature
review. *Journal of Systems and Software, 208*, 111881.
https://doi.org/10.1016/j.jss.2023.111881

Use in the report: supports a mixed validation plan combining inquiry,
task/scenario testing and inspection, with accessibility and operability kept
visible. The review is methodological evidence, not evidence about Nexa users.

## Technical documentation

These references document technologies and diagram/contract tools actually
observed in the API, Blueprint or report evidence. They are not substitutes for
the four academic papers required by the rubric.

**[T1]** Oracle. (n.d.). *Java Platform, Standard Edition & JDK 25
documentation*. Retrieved September 2, 2026, from
https://docs.oracle.com/en/java/javase/25/docs/

**[T2]** Spring. (n.d.). *Spring Boot reference documentation*. Retrieved
September 2, 2026, from https://docs.spring.io/spring-boot/reference/

**[T3]** PostgreSQL Global Development Group. (n.d.). *PostgreSQL 18
documentation*. Retrieved September 2, 2026, from
https://www.postgresql.org/docs/18/

**[T4]** OpenAPI Initiative. (2021). *OpenAPI specification* (Version 3.1.0).
https://spec.openapis.org/oas/v3.1.0.html

**[T5]** PlantUML. (n.d.). *PlantUML language reference guide*. Retrieved
September 2, 2026, from https://plantuml.com/guide

**[T6]** Structurizr. (n.d.). *Structurizr documentation*. Retrieved September
2, 2026, from https://docs.structurizr.com/

## Quartile verification register

| ID | Journal | Year checked | Public metric cross-check | Official Scopus/WoS capture | State |
| :--- | :--- | ---: | :--- | :--- | :--- |
| D1 | Journal of Agriculture and Food Research | 2024 | [JRank metrics](https://jrank.net/journals/j-agr-food-res/metrics) reports Q1 in selected 2024 Scopus/WoS categories | Pending team capture | Preliminary |
| D2 | Trends in Food Science & Technology | 2025 | [JRank metrics](https://jrank.net/journals/trends-food-sci-tech/metrics) reports Q1 in selected 2024 Scopus/WoS categories | Pending team capture | Preliminary |
| M1 | International Journal of Human-Computer Studies | 2024/2025 | [JRank metrics](https://jrank.net/journals/int-j-hum_comput-st/metrics) reports Q1 in selected 2024 Scopus/WoS categories | Pending team capture | Preliminary |
| M2 | Journal of Systems and Software | 2024 | [JRank metrics](https://jrank.net/journals/j-syst-software/metrics) reports Q1 in selected 2024 Scopus/WoS categories | Pending team capture | Preliminary |

## Body citation plan

- Chapter II S2 research plan: `[D1]`, `[D2]`, `[SR1]`, `[SR2]`, `[SR3]`.
- Secondary research synthesis: `[SR1]`, `[SR2]`, `[SR3]`.
- Chapter III Mobile prototyping and interaction states: `[M1]`.
- Chapter IV validation design and heuristic/mixed-method rationale: `[M2]`.
- API baseline and Java/Spring/PostgreSQL environment: `[T1]`, `[T2]`, `[T3]`.
- OpenAPI contract register: `[T4]`.
- C4, UML and database diagram sources: `[T5]`, `[T6]`.

The four candidates must be cited in the corresponding body sections after the
team verifies their quartiles and approves the final APA formatting. The three
`SR` sources are contextual references only; they do not imply a new finding,
participant, percentage, Q1/Q2 candidate or product decision.
