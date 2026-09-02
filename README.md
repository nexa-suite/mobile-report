# Final Project Report

Repositorio Docs-as-Code del trabajo final del curso **1ACC0238 Aplicaciones para Dispositivos Móviles**.

| Campo | Valor |
|---|---|
| Periodo | 202620 |
| NRC | 4949 |
| Startup | nexa-team |
| Documento | Final Project Report |
| Formato fuente | Markdown modular |
| Flujo | GitFlow |
| Commits | Conventional Commits |

## Navegación del informe

El contenido principal se encuentra en [Contents](./report/00-front-matter/03-contents.md), organizado según la estructura oficial del enunciado:

1. [Front matter](./report/00-front-matter/03-contents.md)
2. [Capítulo I: Presentación](./report/01-presentation/chapter-overview.md)
3. [Capítulo II: Requirements Development and Software Solution Design](./report/02-requirements-and-software-solution-design/chapter-overview.md)
4. [Capítulo III: Solution UI/UX Design](./report/03-solution-ui-ux-design/chapter-overview.md)
5. [Capítulo IV: Product Implementation and Validation](./report/04-product-implementation-and-validation/chapter-overview.md)
6. [Conclusiones](./report/90-conclusions/conclusions-and-recommendations.md)
7. [Glosario](./report/91-glossary/glossary.md)
8. [Bibliografía](./report/92-bibliography/bibliography.md)
9. [Anexos](./report/93-annexes/annexes-overview.md)

## Control de avance

Los controles de entrega, el baseline de repositorios y la reconciliación con
las fuentes de autoridad se mantienen en [live-baseline.md](./delivery-checklists/live-baseline.md).
La procedencia de C4, Structurizr, PlantUML y los diagramas de datos se resume
en el [architecture and diagram evidence register](./delivery-checklists/architecture-render-evidence-register.md).
Esos documentos distinguen evidencia comprobada, estructura preparada y datos
que todavía requieren revisión o entrega humana.

## Convención de organización

Cada subpunto numerado de nivel 2 es una carpeta. Sus subpuntos de nivel 3 se encuentran directamente dentro de ella como archivos o carpetas anidadas. Las carpetas sin subpuntos utilizan un documento de contenido con nombre semántico, no un `README.md`.

## Flujo de ramas

```text
main
└── develop
    ├── chapter-01
    ├── chapter-02
    ├── chapter-03
    └── chapter-04
```

Las ramas `chapter-0X` contienen un commit documental por capítulo y se integran progresivamente en `develop`. La rama `main` representa el informe integrado y publicable.

## Estado documental

Los documentos inicialmente creados como estructura son plantillas de trabajo. Cada marcador debe ser reemplazado con evidencia contextualizada del proyecto antes de una entrega académica.
