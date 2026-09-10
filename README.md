<div align="center">

<img src="https://raw.githubusercontent.com/nexa-suite/.github/develop/profile/assets/nexa-logo.svg" alt="Nexa logo" width="220" />

# nexa-mobile-report

**Academic report and delivery evidence for the Nexa mobile planning runway.**

[![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=for-the-badge&logo=markdown&logoColor=white)](./report)
[![Git](https://img.shields.io/badge/Git-Academic%20history-F05032?style=for-the-badge&logo=git&logoColor=white)](./report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.2-source-code-management.md)

[![Course](https://img.shields.io/badge/Course-1ACC0238%20Aplicaciones%20para%20Dispositivos%20M%C3%B3viles-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Period](https://img.shields.io/badge/Period-202620-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![University](https://img.shields.io/badge/University-UPC-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Team](https://img.shields.io/badge/Team-nexa--team-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Status](https://img.shields.io/badge/Status-v0.1.1%20hotfix-F59E0B?style=flat-square)](./docs/releases/v0.1.1.md)

[Report chapters](./report) · [Release evidence](./docs/releases/v0.1.1.md) · [PDF export](./scripts/export-report-pdf.sh) · [Report assets](./report/assets)

</div>

---

## Project Entry Flow

The report repository connects academic evidence to the current Nexa delivery
flow:

1. **Accepted product, domain, architecture, and design decisions** define
   scope and semantics.
2. **Mobile** provides the current mobile planning runway; it is not evidence
   of a completed native client.
3. **Mobile Report** organizes academic chapters, source materials, evidence
   boundaries, and export assets.
4. **API** provides business and integration-contract context.
5. **Platform**, **Buyer Portal**, and **Website** are current product
   surfaces referenced where their evidence is available.
6. **Git and GitHub** preserve traceable changes. A public Product Board is
   referenced only when the team provides the genuine source.

## Overview

This repository contains the academic report for Nexa in course 1ACC0238,
*Aplicaciones para Dispositivos Móviles*. It documents product scope, research
framing, software solution design, UI/UX design, configuration management, and
Sprint 1 planning.

It is documentation and academic evidence, not a mobile application. A report
section may describe a planned workflow or a design artifact, but it does not
prove that a native client, framework, build pipeline, deployment, or user
study exists.

## Nexa Product Ecosystem

<table>
<tr>
<td width="50%" valign="top">

### [Nexa Mobile](https://github.com/nexa-suite/mobile)

Documentation and planning runway for future buyer and cold-chain field
experiences. No mobile application framework is established by this report.

[Open Repository](https://github.com/nexa-suite/mobile)

![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white) ![Status](https://img.shields.io/badge/status-planned-64748B?style=flat-square)

</td>
<td width="50%" valign="top">

### [Nexa Mobile Report](https://github.com/nexa-suite/mobile-report)

Academic report, evidence boundaries, source materials, and reproducible PDF
export for the mobile planning runway.

[Open Repository](https://github.com/nexa-suite/mobile-report)

![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white) ![Pandoc](https://img.shields.io/badge/Pandoc-PDF%20export-1A1A1A?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa API](https://github.com/nexa-suite/api)

Business and integration backbone for identity, tenant scope, and operational
workflows.

[Open Repository](https://github.com/nexa-suite/api)

![Java](https://img.shields.io/badge/Java-25-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.1-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-4169E1?style=flat-square&logo=postgresql&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Website](https://github.com/nexa-suite/website)

Public product experience and entry point.

[Open Repository](https://github.com/nexa-suite/website)

![HTML5](https://img.shields.io/badge/HTML5-static-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-responsive-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa Buyer Portal](https://github.com/nexa-suite/portal)

Buyer-facing experience for catalog discovery, purchasing, and delivery
visibility.

[Open Repository](https://github.com/nexa-suite/portal)

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Platform](https://github.com/nexa-suite/platform)

Internal operational workspace for tenant teams, sales, warehouse, and
logistics.

[Open Repository](https://github.com/nexa-suite/platform)

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
</tr>
</table>

## Tools Stack

| Concern | Current repository use |
| --- | --- |
| Source format | GitHub Flavored Markdown |
| Report validation | Relative-link and asset checks, shell syntax checks, and `git diff --check` |
| Diagram and visual evidence | Versioned SVG and image assets |
| PDF export | Pandoc and XeLaTeX through the repository export script |
| Product Board | A genuine public Board is added only when the team makes its source available |
| Source control | Git, GitHub, Conventional Commits, and signed contributor history |
| Collaboration | Git history and GitHub public contribution evidence |

## Getting Started

```bash
git clone https://github.com/nexa-suite/mobile-report.git
cd mobile-report
git diff --check
NEXA_REPORT_EXPORT_MODE=native bash scripts/export-report-pdf.sh
```

Review the current report, release notes, and canonical Blueprint before
changing product, domain, or architecture wording. A generated PDF requires
visual review before it is used as a submission artifact.

## Project Structure

```text
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
docs/releases/
scripts/
├── export-report-pdf.sh
└── lib/report-pdf-filter.lua
README.md
```

## Ownership & Evidence Boundaries

- Mobile Report owns academic narrative, report structure, export, and delivery
  evidence.
- Accepted product, domain, architecture, and design decisions own Nexa
  semantics; the report does not redefine them.
- Mobile owns the client-planning runway.
- API owns business and integration contracts referenced by the report.
- Product surfaces provide visual or technical evidence only when the report
  cites a verifiable source.
- Report content is academic evidence; it is not implementation, deployment,
  or production authorization.

## Documentation

- [Report chapters](./report)
- [v0.1.1 release notes](./docs/releases/v0.1.1.md)
- [Changelog](./CHANGELOG.md)
- [Mobile repository](https://github.com/nexa-suite/mobile)
- [API contracts](https://github.com/nexa-suite/api/tree/main/docs/openapi)
- [Canonical Blueprint](https://github.com/nexa-suite/blueprint)

## v0.1.1 Hotfix

`v0.1.1` reconciles the report with the current 202620 statement and rubrics
while preserving `v0.1.0` as historical provenance. Its release notes retain
the genuine human and external evidence that remains open; the hotfix does not
represent those records as completed.

<div align="center">

Maintained by the Nexa team · [github.com/nexa-suite/mobile-report](https://github.com/nexa-suite/mobile-report)

</div>
