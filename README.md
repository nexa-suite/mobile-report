<div align="center">

<img src="./report/assets/chapter-3/style-guidelines/brand/nexa-logo.svg" alt="Logotipo de Nexa" width="220" />

# nexa-mobile-report

**Informe académico y evidencia de entrega de Nexa Mobile**

[![Markdown](https://img.shields.io/badge/Markdown-Documentaci%C3%B3n-000000?style=for-the-badge&logo=markdown&logoColor=white)](./report)
[![Git](https://img.shields.io/badge/Git-Trazabilidad-F05032?style=for-the-badge&logo=git&logoColor=white)](./report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.2-source-code-management.md)
[![Jira Software](https://img.shields.io/badge/Jira_Software-Sprint_2-0052CC?style=for-the-badge&logo=jira&logoColor=white)](https://nexa-suite.atlassian.net/jira/software/projects/NX/boards/2/backlog)

[![Curso](https://img.shields.io/badge/Curso-1ACC0238%20Aplicaciones%20para%20Dispositivos%20M%C3%B3viles-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Período](https://img.shields.io/badge/Per%C3%ADodo-202620-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Universidad](https://img.shields.io/badge/Universidad-UPC-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Equipo](https://img.shields.io/badge/Equipo-nexa--team-0F172A?style=flat-square)](./report/00-front-matter/00-cover.md)
[![Entrega](https://img.shields.io/badge/Entrega-TB1%20%7C%20Sprint%202-0F766E?style=flat-square)](./report/04-product-implementation-and-validation/4.2-landing-page-and-mobile-application-implementation/4.2.2-sprint-2)
[![Release v2.0.1](https://img.shields.io/badge/Release-v2.0.1-0F766E?style=flat-square)](https://github.com/nexa-suite/mobile-report/releases/tag/v2.0.1)

[Informe](./report) · [Evidencia de Sprint 2](./report/04-product-implementation-and-validation/4.2-landing-page-and-mobile-application-implementation/4.2.2-sprint-2) · [Publicación v2.0.1](https://github.com/nexa-suite/mobile-report/releases/tag/v2.0.1) · [Exportar PDF](./scripts/export-report-pdf.sh) · [Recursos](./report/assets)

</div>

---

## Flujo del proyecto

El informe conecta las decisiones de producto y las superficies de Nexa con sus fuentes de trabajo y evidencia:

1. Las decisiones aceptadas de producto, dominio, arquitectura y diseño definen el alcance y sus conceptos.
2. El API aporta contratos de integración y decisiones de negocio para los flujos operativos.
3. Mobile, Web Clients y Website presentan superficies que consultan los servicios según su contexto.
4. Jira organiza el Product Backlog y el seguimiento de Sprint; GitHub conserva el historial de código, documentación y releases.
5. Mobile Report reúne la entrega académica TB1 y relaciona planificación, diseño, implementación, comprobación técnica y validación con su evidencia.

## Descripción

Este repositorio contiene el informe del curso **1ACC0238 Aplicaciones para Dispositivos Móviles**, período **202620**. La entrega TB1 documenta requisitos, diseño de experiencia e interfaces, y reúne evidencia sobre la implementación de Sprint 2. El informe distingue planificación, diseño, implementación, comprobación técnica y validación según las fuentes citadas.

## Ecosistema Nexa

<table>
<tr>
<td width="50%" valign="top">

### [Nexa Mobile](https://github.com/nexa-suite/mobile)

Operations Mobile es nativa Android/Kotlin. La publicación oficial es [v1.0.1](https://github.com/nexa-suite/mobile/releases/tag/v1.0.1), con [APK firmado](https://github.com/nexa-suite/mobile/releases/download/v1.0.1/nexa-operations-v1.0.1.apk), corrección de cámara, cierre de sesión y menú operativo en tarjetas. Buyer Mobile se documenta como objetivo de diseño `TARGET` en Flutter.

![Android](https://img.shields.io/badge/Android-Operations-3DDC84?style=flat-square&logo=android&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin-Mobile-7F52FF?style=flat-square&logo=kotlin&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-Buyer%20Mobile%20TARGET-02569B?style=flat-square&logo=flutter&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Mobile Report](https://github.com/nexa-suite/mobile-report)

Informe académico TB1, capítulos, fuentes de evidencia y exportación del documento.

![Markdown](https://img.shields.io/badge/Markdown-Informe-000000?style=flat-square&logo=markdown&logoColor=white) ![Pandoc](https://img.shields.io/badge/Pandoc-Exportaci%C3%B3n_PDF-1A1A1A?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa API](https://github.com/nexa-suite/api)

Servicios de negocio y contratos de integración para identidad, Tenant y flujos operativos. Publicación fuente [v1.0.0](https://github.com/nexa-suite/api/releases/tag/v1.0.0), desplegada mediante Docker en Render, con PostgreSQL en Neon y correo transaccional mediante Brevo. [Swagger UI](https://nexa-api-69bj.onrender.com/swagger-ui/index.html) presenta los contratos del servicio.

![Java](https://img.shields.io/badge/Java-Servicios-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-API-6DB33F?style=flat-square&logo=springboot&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Datos-4169E1?style=flat-square&logo=postgresql&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Website](https://github.com/nexa-suite/website)

Sitio público y punto de entrada para conocer Nexa. Publicación [v1.0.0](https://github.com/nexa-suite/website/releases/tag/v1.0.0), disponible en [GitHub Pages](https://nexa-suite.github.io/website/).

![HTML5](https://img.shields.io/badge/HTML5-Web-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-Responsive-1572B6?style=flat-square&logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-Web-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [Nexa Buyer Portal](https://github.com/nexa-suite/web-clients)

Experiencia web para catálogo, compras y seguimiento de entregas; forma parte del monorepo Web Clients.

![Angular](https://img.shields.io/badge/Angular-Web-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-Web-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
<td width="50%" valign="top">

### [Nexa Platform](https://github.com/nexa-suite/web-clients)

Espacio operativo para equipos de ventas, almacén y logística; forma parte del monorepo Web Clients.

![Angular](https://img.shields.io/badge/Angular-Web-DD0031?style=flat-square&logo=angular&logoColor=white) ![TypeScript](https://img.shields.io/badge/TypeScript-Web-3178C6?style=flat-square&logo=typescript&logoColor=white)

</td>
</tr>
</table>

## Herramientas del informe

| Uso | Herramientas |
| --- | --- |
| Fuente y documentación | GitHub Flavored Markdown, Git y GitHub |
| Seguimiento de trabajo | [Jira Software](https://nexa-suite.atlassian.net/jira/software/projects/NX/boards/2/backlog): Product Backlog y Sprint 2; requiere inicio de sesión y permisos del espacio |
| Diagramas y figuras | SVG e imágenes versionadas en `report/assets/` |
| Exportación | Pandoc y XeLaTeX mediante `scripts/export-report-pdf.sh` |

## Inicio rápido

```bash
git clone https://github.com/nexa-suite/mobile-report.git
cd mobile-report
git diff --check
```

Para exportar el informe en un entorno con los requisitos instalados:

```bash
NEXA_REPORT_EXPORT_MODE=native bash scripts/export-report-pdf.sh
```

Revisa visualmente el PDF exportado antes de usarlo como entrega.

## Estructura

```text
report/       Portada, capítulos, bibliografía y anexos
report/assets/ Figuras y recursos del informe
docs/releases/ Registro de publicaciones
scripts/      Exportación del PDF
README.md
```

## Documentación y publicación

- [Índice del informe](./report/00-front-matter/03-contents.md)
- [Implementación y evidencia de Sprint 2](./report/04-product-implementation-and-validation/4.2-landing-page-and-mobile-application-implementation/4.2.2-sprint-2)
- [Git, revisiones y releases](./report/04-product-implementation-and-validation/4.1-software-configuration-management/4.1.2-source-code-management.md)
- [Changelog](./CHANGELOG.md)
- [Release v2.0.1](https://github.com/nexa-suite/mobile-report/releases/tag/v2.0.1)

<div align="center">

Mantenido por el equipo Nexa · [github.com/nexa-suite/mobile-report](https://github.com/nexa-suite/mobile-report)

</div>
