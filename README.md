<div align="center">

<img src="https://raw.githubusercontent.com/nexa-suite/.github/develop/profile/assets/nexa-logo.svg" alt="Nexa logo" width="220" />

# Nexa Mobile Report

**Academic report and delivery evidence for Nexa Mobile.**

![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white) ![Git](https://img.shields.io/badge/Git-Academic%20history-F05032?style=flat-square&logo=git&logoColor=white) ![Pandoc](https://img.shields.io/badge/Pandoc-PDF%20export-1A1A1A?style=flat-square) ![Latest Git tag](https://img.shields.io/github/v/tag/nexa-suite/mobile-report?sort=semver&style=flat-square&label=latest%20Git%20tag)

[Report chapters](./report) · [Release evidence](./docs/releases/v1.0.0.md) · [PDF export](./scripts/export-report-pdf.sh) · [Report assets](./report/assets)

</div>

---

## Project Entry Flow

The report connects academic evidence to the current Nexa delivery boundary:

1. Accepted Product, Domain, Architecture and Design decisions define the
   semantics used by the report.
2. Mobile currently integrates partial Operations Android/Kotlin/Jetpack Compose
   implementation evidence; this report does not claim Mobile V1 is complete.
3. Mobile Report organizes chapters, source material, evidence boundaries and
   reproducible export assets.
4. API, Platform, Buyer Portal and Website provide implementation or product
   context only when a source is verifiable.

## Overview

This repository contains the academic report for course `1ACC0238 Aplicaciones
para Dispositivos Móviles`. It documents product scope, research framing,
requirements, software solution design, UI/UX design, configuration
management, and four-Sprint academic Mobile planning.

It is documentation and academic evidence, not a Mobile runtime. A report
section describing a planned workflow or design artifact is not implementation,
deployment or production-readiness evidence.

## Nexa Product Ecosystem

<table>
<tr>
<td width="50%" valign="top">

### [Nexa Mobile Report](https://github.com/nexa-suite/mobile-report)

This repository: academic report, source material and delivery evidence.

![Markdown](https://img.shields.io/badge/Markdown-Documentation-000000?style=flat-square&logo=markdown&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Mobile](https://github.com/nexa-suite/mobile)

Operations Android/Kotlin/Jetpack Compose is partial implementation evidence
integrated in the current Mobile baseline, not a completed Mobile V1. Buyer
Mobile is an accepted Flutter/Dart target, not an implementation claim.

![Operations Android](https://img.shields.io/badge/Operations%20Mobile-partial%20evidence-3DDC84?style=flat-square&logo=android&logoColor=white) ![Buyer target](https://img.shields.io/badge/Buyer%20Mobile-TARGET%20Flutter%2FDart-64748B?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa API](https://github.com/nexa-suite/api)

Authoritative business and integration backbone for Nexa Suite.

![Java](https://img.shields.io/badge/Java-25-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring%20Boot-4.1-6DB33F?style=flat-square&logo=springboot&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Website](https://github.com/nexa-suite/website)

Public product experience and acquisition entry point.

![HTML5](https://img.shields.io/badge/HTML5-static-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-responsive-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-vanilla-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa Buyer Portal](https://github.com/nexa-suite/portal)

Buyer-facing Web experience for B2B purchasing and delivery visibility.

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Platform](https://github.com/nexa-suite/platform)

Internal operational Web workspace for tenant teams.

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-strict-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
</tr>
</table>

## Report Baseline

The `v1.0.0` release notes record the AV1 academic baseline: 97 Product
Backlog items, 426 story points, 9/9 formative Needfinding interviews, eleven
accepted Bounded Contexts and four academic Sprints. These are report and
research baseline facts, not claims that all backlog items or the Mobile
Product are implemented, accepted or production-ready.

## Tools Stack

| Concern | Current repository use |
| --- | --- |
| Source format | GitHub-Flavored Markdown |
| Academic traceability | Versioned chapters, release notes and report sources |
| Export | Pandoc and XeLaTeX through `scripts/export-report-pdf.sh` |
| Evidence | Relative report assets, diagrams and linked source material |
| Source control | Git, GitHub, Conventional Commits and signed history |

## Getting Started

```bash
git clone https://github.com/nexa-suite/mobile-report.git
cd mobile-report
git diff --check
NEXA_REPORT_EXPORT_MODE=native bash scripts/export-report-pdf.sh
```

Native export requires Pandoc and XeLaTeX. The script can use its documented
Docker mode when the native toolchain is unavailable. A generated PDF requires
visual review before it is used as a submission artifact.

## Validation

```bash
git diff --check
bash -n scripts/export-report-pdf.sh
```

The release evidence documents additional report, link, asset and export
checks. This README does not claim that a documentation-only change reruns the
full academic export or Product Acceptance gates.

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

- Mobile Report owns academic narrative, report structure, export and delivery
  evidence.
- Accepted Product, Domain, Architecture and Design decisions own Nexa
  semantics; the report does not redefine them.
- Mobile maintains client planning and implementation context.
- API owns business and integration contracts referenced by the report.
- Report evidence is distinct from implementation, deployment, Product
  Acceptance and production authorization.

## Documentation

- [Report chapters](./report)
- [v1.0.0 release notes](./docs/releases/v1.0.0.md)
- [v1.0.1 version history](./report/00-front-matter/01-version-history.md)
- [Changelog](./CHANGELOG.md)
- [Mobile repository](https://github.com/nexa-suite/mobile)
- [API contracts](https://github.com/nexa-suite/api/tree/main/docs/openapi)

## Nexa Engineering & Documentation

<table>
<tr>
<td width="50%" valign="top">

### [Nexa Blueprint](https://github.com/nexa-suite/blueprint)

Canonical Product, Domain, Architecture, data, security and accepted
engineering decision source.

![C4](https://img.shields.io/badge/C4-canonical%20model-64748B?style=flat-square) ![Markdown](https://img.shields.io/badge/Markdown-documentation-000000?style=flat-square&logo=markdown&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Web Report](https://github.com/nexa-suite/web-report)

Academic report and evidence repository for the Nexa Web course.

![Docs as Code](https://img.shields.io/badge/Docs%20as%20Code-academic%20evidence-64748B?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa Complementary](https://github.com/nexa-suite/complementary)

Supporting references, reproducible engineering resources and shared tooling.

![Support tooling](https://img.shields.io/badge/Support%20tooling-reference-64748B?style=flat-square)

</td>
<td width="50%" valign="top">

### [Nexa Design Lab](https://github.com/nexa-suite/design-lab)

UX/UI, interaction, design-system, prototype and current design-evidence
workspace.

![Angular](https://img.shields.io/badge/Angular-22-DD0031?style=flat-square&logo=angular&logoColor=white)

</td>
</tr>
</table>

## Security

Follow the repository [Security Policy](./.github/SECURITY.md) for reporting
vulnerabilities. Private interview data, credentials and local evidence remain
outside the public report.

## Legal

Copyright © 2026 Nexa. All rights reserved. No open-source license is claimed
by this README.

<div align="center"><br />Nexa · Academic evidence, explicit boundaries</div>
