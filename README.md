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

El contenido principal se encuentra en [`report/`](./report/), organizado según la estructura oficial del enunciado:

1. [Front matter](./report/00-front-matter/)
2. [Capítulo I: Presentación](./report/01-presentation/)
3. [Capítulo II: Requirements Development and Software Solution Design](./report/02-requirements-and-software-solution-design/)
4. [Capítulo III: Solution UI/UX Design](./report/03-chapter-iii-solution-ui-ux-design/)
5. [Capítulo IV: Product Implementation and Validation](./report/04-chapter-iv-product-implementation-and-validation/)
6. [Conclusiones](./report/90-conclusions/)
7. [Glosario](./report/91-glossary/)
8. [Bibliografía](./report/92-bibliography/)
9. [Anexos](./report/93-annexes/)

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
