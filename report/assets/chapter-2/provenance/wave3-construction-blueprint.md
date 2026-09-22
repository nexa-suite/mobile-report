---
status: accepted
scope: chapter-2
source-repository: nexa-suite/blueprint
source-commit: 01325138b5c6206d0ab3ab47b57b238fadf21dfb
last-reviewed: 2026-09-20
---

# Wave 3.2 canonical architecture asset provenance

This manifest records current Chapter 2 architecture assets copied from the
canonical Blueprint Wave 3.2 closure output. The source repository owns Product, Domain,
Architecture, DSL, PlantUML and SQL semantics. This report owns only the
academic narrative and copied generated artifacts.

| Report destination | Canonical Blueprint source path | Generated/copied artifact type |
| --- | --- | --- |
| `report/assets/chapter-2/c4/*.{svg,png}` | `01-shared/architecture/c4/structurizr/workspace.dsl` and includes; generated at `01-shared/architecture/c4/exports/{l1,l2,l3,dynamic,deployment}/` | Structurizr-generated C4 SVG/PNG, copied unchanged. |
| `report/assets/chapter-2/tactical/BC-XX/BCXX_*.{svg,png}` | `01-shared/domain/bounded-contexts/BC-XX/diagrams/domain-model.puml` | PlantUML-generated tactical Domain UML SVG/PNG, copied unchanged. |
| `report/assets/chapter-2/tactical/BC-XX/database-diagram.{svg,png}` | `01-shared/domain/bounded-contexts/BC-XX/data/target-relational-model.sql` via `tooling/scripts/generate-target-database-diagrams.py` and generated `database-diagram.puml` | PlantUML-generated per-BC ERD SVG/PNG, copied unchanged. |
| `report/assets/chapter-2/domain-storytelling/*.{svg,png}` | `01-shared/domain/processes/domain-storytelling/*.puml` | PlantUML-generated current Domain Story SVG/PNG, copied unchanged. |

No `.dsl`, `.puml` or SQL semantic source is retained as a current Chapter 2
architecture asset. Historical discovery evidence in `ddd-process/` remains
explicitly historical and does not override this current construction baseline.
