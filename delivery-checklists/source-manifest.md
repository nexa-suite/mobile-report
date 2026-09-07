# Manifiesto reproducible de fuentes

## Corte observado

Fecha de observación: 2026-09-06.

Este manifiesto registra fuentes usadas para reconciliar el informe. Una fuente de
implementación demuestra solamente estado AS-IS; Blueprint conserva autoridad
canónica de Product, Domain y Architecture.

| Fuente | Tipo | Ubicación reproducible | Identificador observado | Autoridad | Uso |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Final Project Statement V4.0 | PDF externo local | `NEXA_MOBILE_STATEMENT_PDF` | SHA-256 `38be0c1baa77d0601c9605ef9ea72ad2fb510222a17a65944a06690621169f37` | Enunciado oficial | Estructura, hitos y rúbrica académica |
| Plantilla de portada | DOCX externo local | `NEXA_MOBILE_COVER_TEMPLATE` | SHA-256 `cc4226b18ac3dcd5935198ca9593de2c3b0b6706f36e1516269d3fab8235dbb1` | Referencia visual oficial | Composición de portada; no reutiliza datos de otro equipo |
| Mobile Report | repositorio Git | `https://github.com/nexa-suite/mobile-report` | `reconcile/report-integration-20260902` @ `fbc096423a52312d1afa8099a2646b99e0c0b8fe` (Wave 3 closure baseline) | Informe en integración | Contenido, colaboración y exportación; Wave 4 corrections are recorded in the audit register |
| Blueprint | repositorio Git | `NEXA_BLUEPRINT_ROOT` | `origin/main` @ `fce3ba6f8ca1622084a2114424086364e1f7d93f` | Canónica | Product, Domain, Architecture y backlog Mobile |
| API | repositorio Git | `NEXA_API_ROOT` | `origin/main` @ `380e2427bc3883f23fbd7e9a82d452888f2074a8` | AS-IS | Contratos y persistencia verificables |
| Platform | repositorio Git | `../platform` | `origin/main` @ `f8285f1bf0de83ed6fa95aa86d1dcc6efd4897f7` | AS-IS | Evidencia de superficie web de operaciones |
| Portal | repositorio Git | `../portal` | `origin/main` @ `672836b8369ea16cb1374d348d73ccacbebbc954` | AS-IS | Evidencia de superficie Buyer |
| Website | repositorio Git | `../website` | `origin/main` @ `96ab63a95f923114627048283c323a501238ff53` | AS-IS | Evidencia Landing Page |
| Mobile | repositorio Git | `../mobile` | `origin/main` @ `88c99a1079d17ce4514791087451452bdbf17c51` | AS-IS | Evidencia de cliente Mobile |
| Design Lab | repositorio Git | `../design-lab` | `origin/main` @ `c16c1f4b64af688754a7c3bc989db9308f825c66` | Diseño ejecutable | UX/UI y Design System; no implementación Mobile final |
| Nexa DDD | directorio local | `NEXA_DDD_SOURCE_DIR` | Directorio sin Git al corte | Evidencia a clasificar | Imágenes de proceso; cada uso requiere hash y registro visual |
| Nexa Ecosystem Report | fuente histórica | Referencia Git registrada en el ledger de procedencia | SHA histórico esperado `e161fe522023bfe5929e76c4d7c66af211884b7e` | Histórica | Needfinding y antecedentes; nunca redefine canon actual |
| Nexa historical local snapshot | fuente histórica local | `NEXA_HISTORICAL_ROOT` | Curated snapshot; revision and file hashes in [historical provenance](../report/93-annexes/annex-f-translation-and-terms/historical-evidence-provenance.md) | Histórica | Sólo clasificación/revisión de material histórico; no autoridad actual |

## Estados de worktrees al corte

| Repositorio | Rama local | HEAD local | Estado local |
| :--- | :--- | :--- | :--- |
| Blueprint | `docs/blueprint-canonical-memory-reconciliation` | `217d2bf2429d602d5d08771ed88fa0d1de12ba36` | `01-shared/nexa-official-logo/` no rastreado |
| API | `develop` | `72493f8669962a31743aa9daf06426f1af29e2d2` | Limpio |
| Platform | `develop` | `2a1f2f0db95561920f23eab6158903458c01d215` | Cambios locales ajenos presentes |
| Portal | `develop` | `ab60951cc0c755aee1926f3ed8807438d010aa6c` | Cambios locales ajenos presentes |
| Website | `develop` | `13e3a4c3114931e635adf15fd2c8f3740397b29b` | Limpio |
| Mobile | `develop` | `730b23143b2e100cd1e8c290313aa83d42b4b5a0` | `.DS_Store` y `.idea/` no rastreados |
| Design Lab | `feature/mobile-guidelines-foundation` | `04e2e4ea83b88792b4dc462d7edb700eb8d3faca` | Cambios locales ajenos presentes |

## Regla de resolución local

Las rutas externas se declaran mediante variables de entorno. Un checkout limpio
debe proporcionar las mismas fuentes y hashes. La ausencia de una fuente externa
se informa como `BLOCKED BY MISSING LOCAL EXTERNAL SOURCE`; nunca se sustituye con
una ruta privada de otro integrante.
