# 2.5.3 Software Architecture

La arquitectura se documentará con C4 y Structurizr para mantener una lectura
consistente del sistema, sus containers y sus nodos. Nexa es el sistema
principal; Website, Platform, Buyer Portal, API, PostgreSQL y Object Storage
son los containers AS-IS/V1 aceptados. Operations Mobile y Buyer Mobile se
incorporan sólo en la vista V1 TARGET como clientes planificados.

## Vistas y límite de evidencia

| Vista C4 | Contenido requerido | Estado en este informe |
| :--- | :--- | :--- |
| Context | Nexa, grupos de actores y sistemas externos abstractos | Diseño observado; taller y revisión del informe pendientes |
| Container AS-IS | Website, Platform, Buyer Portal, API, PostgreSQL y Object Storage | Diseño observado; prueba de runtime pendiente |
| Container V1 TARGET | Containers AS-IS más Operations Mobile y Buyer Mobile | Diseño objetivo; no se afirma runtime Mobile |
| Component | Componentes dentro de un container ejecutable seleccionado | Diseño observado; vista y revisión seleccionadas pendientes |
| Deployment local | Nodos, servicios, red y almacenamiento de un entorno ejecutado | Diseño observado; evidencia de ejecución pendiente |
| Deployment cloud | Proveedor, red, secretos, backup, rollback y observabilidad | Abierto; no se afirma producción |

La línea base del API es un modular monolith con Java 25, Spring Boot 4.1 y
evidencia de Spring Modulith en el código compartido. Esta afirmación describe
la base backend observada; no prueba un cliente Mobile ni un contrato API
aceptado. PostgreSQL permanece físicamente compartido con ownership lógico por
contexto.

Los diagramas deben distinguir el modelo lógico de dominio, los containers
ejecutables y los nodos de runtime. Los módulos de código no se convierten
automáticamente en Bounded Contexts ni en containers C4. Cada imagen incluida
requiere fuente, revisión, fecha de exportación y revisión visual humana. La
procedencia observada se conserva en el
[registro de evidencia de arquitectura y diagramas](../../../../delivery-checklists/architecture-render-evidence-register.md).
