<div align="center">

<img src="https://raw.githubusercontent.com/nexa-suite/.github/develop/profile/assets/nexa-logo.svg" alt="Nexa logo" width="220" />

# nexa-mobile-report

**Academic report and delivery evidence for the Nexa mobile planning runway.**

[![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=for-the-badge&logo=markdown&logoColor=white)](./report)
[![Jira](https://img.shields.io/badge/Jira-Sprints-0052CC?style=for-the-badge&logo=jira&logoColor=white)](./report/04-product-implementation-and-validation/4.2-landing-page-services-and-applications-implementation/4.2.1-sprints/section-overview.md)
[![GitFlow](https://img.shields.io/badge/GitFlow-Academic-F05032?style=for-the-badge&logo=git&logoColor=white)](./report/04-product-implementation-and-validation/4.1-software-configuration-management/section-overview.md)

[![Course](https://img.shields.io/badge/Course-1ACC0238%20Aplicaciones%20para%20Dispositivos%20M%C3%B3viles-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Cycle](https://img.shields.io/badge/Cycle-2026--02-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![University](https://img.shields.io/badge/University-UPC-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Team](https://img.shields.io/badge/Team-nexa--team-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Status](https://img.shields.io/badge/Status-AV1-F59E0B?style=flat-square)](./delivery-checklists/av1.md)

[Report chapters](./report) · [Delivery checklists](./delivery-checklists) · [Validation scripts](./scripts) · [Report assets](./report/assets)

</div>

<br>

---

## Project Entry Flow

The report repository connects evidence to the current Nexa delivery flow:

1. **Accepted product and architecture decisions** provide the scope, domain, architecture, and delivery baseline.
2. **Mobile** provides the current planning runway and repository baseline.
3. **Mobile Report** organizes academic chapters, evidence, validations, and export assets.
4. **API** provides the business and integration contract context.
5. **Platform**, **Buyer Portal**, and **Website** remain current implementation surfaces.
6. **Jira** and **GitFlow** organize sprint evidence, review points, and traceable changes.

## Overview

This repository contains the academic report for the mobile scope and the supporting delivery evidence used to reconcile that report with the current Nexa baseline.

It is documentation and validation infrastructure, not a mobile application. The report may describe target workflows or evaluated evidence, but it must not be read as proof that a native client, framework, build pipeline, or production deployment exists.

The report is organized for course 1ACC0238, Aplicaciones para Dispositivos Móviles, and the Nexa team delivery workflow.

## Nexa Product Ecosystem

<table>
<tr>
<td width="50%" valign="top">

### [Nexa Mobile](https://github.com/nexa-suite/mobile)

Documentation and native runway for future buyer and cold-chain field experiences. No application framework selected.

[Open Repository](https://github.com/nexa-suite/mobile)

![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white) ![Node.js](https://img.shields.io/badge/Node.js-validation-339933?style=flat-square&logo=nodedotjs&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-validation-2088FF?style=flat-square&logo=githubactions&logoColor=white) ![Status](https://img.shields.io/badge/status-planned-64748B?style=flat-square)

</td>
<td width="50%" valign="top">

### [Nexa Mobile Report](https://github.com/nexa-suite/mobile-report)

Academic report, delivery evidence, and validation for the mobile planning runway.

[Open Repository](https://github.com/nexa-suite/mobile-report)

![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white) ![Python](https://img.shields.io/badge/Python-validation-3776AB?style=flat-square&logo=python&logoColor=white) ![Jira](https://img.shields.io/badge/Jira-sprints-0052CC?style=flat-square&logo=jira&logoColor=white) ![GitFlow](https://img.shields.io/badge/GitFlow-academic-F05032?style=flat-square&logo=git&logoColor=white)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa API](https://github.com/nexa-suite/api)

Business and integration backbone for identity, tenant scope, and operational workflows.

[Open Repository](https://github.com/nexa-suite/api)

![Java](https://img.shields.io/badge/Java-25-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.1-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-4169E1?style=flat-square&logo=postgresql&logoColor=white) ![Flyway](https://img.shields.io/badge/Flyway-migrations-CC0200?style=flat-square&logo=flyway&logoColor=white) ![Release](https://img.shields.io/github/v/release/nexa-suite/api?display_name=tag&sort=semver&style=flat-square&label=release)

</td>
<td width="50%" valign="top">

### [Nexa Website](https://github.com/nexa-suite/website)

Public product experience and public product entry point.

[Open Repository](https://github.com/nexa-suite/website)

![HTML5](https://img.shields.io/badge/HTML5-static-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-responsive-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![Release](https://img.shields.io/github/v/release/nexa-suite/website?display_name=tag&sort=semver&style=flat-square&label=release)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa Buyer Portal](https://github.com/nexa-suite/portal)

Buyer-facing experience for catalog discovery, purchasing, and delivery visibility.

[Open Repository](https://github.com/nexa-suite/portal)

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Material](https://img.shields.io/badge/Angular%20Material-22-757575?style=flat-square&logo=materialdesign&logoColor=white) ![Release](https://img.shields.io/github/v/release/nexa-suite/portal?display_name=tag&sort=semver&style=flat-square&label=release)

</td>
<td width="50%" valign="top">

### [Nexa Platform](https://github.com/nexa-suite/platform)

Internal operational workspace for tenant teams, sales, warehouse, and logistics.

[Open Repository](https://github.com/nexa-suite/platform)

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Material](https://img.shields.io/badge/Angular%20Material-22-757575?style=flat-square&logo=materialdesign&logoColor=white) ![Release](https://img.shields.io/github/v/release/nexa-suite/platform?display_name=tag&sort=semver&style=flat-square&label=release)

</td>
</tr>
</table>
## Tools Stack

| Concern | Current tool |
|---|---|
| Source format | GitHub Flavored Markdown |
| Validation | Python and Bash repository validators |
| Diagram and visual evidence | SVG and image assets |
| PDF export | Pandoc and XeLaTeX when the export environment is available |
| Jira | Sprint tracking and review evidence |
| Source control | GitFlow, Conventional Commits, and branch traceability |
| Collaboration | Git and GitHub |

## Getting Started

~~~bash
git clone https://github.com/nexa-suite/mobile-report.git
cd mobile-report
bash scripts/verify-report-structure.sh
bash scripts/check-report-links.sh
~~~

Read the live-baseline and baseline-reconciliation checklists before adding evidence or changing the report narrative.

### Validation

~~~bash
bash scripts/verify-report-structure.sh
bash scripts/check-report-links.sh
git diff --check
~~~

For a PDF artifact, use [scripts/export-report-pdf.sh](./scripts/export-report-pdf.sh) and inspect the rendered result before treating the export as deliverable evidence.

## Project Structure

~~~text
report/
├── 00-front-matter/
├── 01-presentation/
├── 02-requirements-and-software-solution-design/
├── 03-solution-ui-ux-design/
├── 04-product-implementation-and-validation/
├── 90-conclusions/
├── 91-glossary/
├── 92-bibliography/
├── 93-annexes/
└── assets/
delivery-checklists/
scripts/
├── check-report-links.sh
├── export-report-pdf.sh
└── verify-report-structure.sh
README.md
~~~

## Ownership & Boundaries

- Mobile Report owns academic narrative, report structure, export, and delivery evidence.
- Accepted product and architecture decisions own the report's product and architecture semantics.
- Mobile owns the current client-planning runway.
- API owns business and integration contracts referenced by the report.
- Current product surfaces provide visual evidence for the report's intended client direction.
- Report content is evidence and evaluation material; it is not a substitute for implementation or production authorization.

## Documentation

- [Report chapters](./report)
- [Delivery checklists](./delivery-checklists)
- [Validation scripts](./scripts)
- [Mobile repository](https://github.com/nexa-suite/mobile)
- [API contracts](https://github.com/nexa-suite/api/tree/main/docs/openapi)

<div align="center">

<br>

Maintained by the Nexa team · [github.com/nexa-suite/mobile-report](https://github.com/nexa-suite/mobile-report)

</div>
