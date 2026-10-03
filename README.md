# Nexa Mobile Report

Informe académico del curso Aplicaciones para Dispositivos Móviles. Presenta el problema, los requisitos, el diseño, la implementación y la validación de Nexa.

## Contenido

- [Presentación](report/01-presentation)
- [Requisitos y diseño de software](report/02-requirements-and-software-solution-design)
- [Diseño de experiencia e interfaces](report/03-solution-ui-ux-design)
- [Implementación y validación](report/04-product-implementation-and-validation)
- [Índice del informe](report/00-front-matter/03-contents.md)

## Productos

- [Aplicación móvil](https://github.com/nexa-suite/mobile)
- [Servicios de negocio](https://github.com/nexa-suite/api)
- [Website](https://github.com/nexa-suite/website)

El informe distingue planificación, diseño, implementación, comprobación técnica y validación con usuarios. El estado de cada apartado depende de la evidencia disponible; esta publicación no acredita una entrega final aceptada.

## Edición y comprobación

La fuente utiliza Markdown e imágenes relativas. Antes de publicar cambios:

```sh
git diff --check
bash -n scripts/export-report-pdf.sh
```

El script de exportación conserva la selección de apartados por entrega académica. Los documentos PDF generados necesitan revisión visual antes de utilizarse como entrega.

## Publicación actual

[Checkpoint v0.7.0](docs/releases/v0.7.0.md). El historial de publicaciones anteriores se conserva.
