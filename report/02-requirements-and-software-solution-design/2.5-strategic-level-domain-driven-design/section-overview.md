# 2.5 Strategic-Level Domain-Driven Design

Strategic Domain-Driven Design convierte el conocimiento del dominio en
límites de modelo, responsabilidades y relaciones explícitas. En Nexa, el
análisis parte de una sola plataforma B2B SaaS multi-tenant: las superficies
Web y Mobile proyectan el dominio compartido, pero no crean Bounded Contexts
adicionales.

El Core Domain de Nexa es la coordinación confiable de compromisos comerciales
B2B contra disponibilidad de inventario real, seguida de fulfillment físico y
entrega trazables bajo lote, vencimiento y restricciones opcionales de cadena
de frío.

## Clasificación estratégica de los Bounded Contexts de Nexa

La clasificación expresa diferenciación, densidad de políticas y riesgo de
negocio. Generic no significa irrelevante: indica una capacidad más
reemplazable o común, mientras su corrección sigue siendo crítica.

| Clasificación | Bounded Contexts | Razón estratégica |
| :--- | :--- | :--- |
| Core | BC-04 Sales Commitment; BC-05 Inventory Availability; BC-06 Fulfillment & Delivery | Diferencian la coordinación entre obligación comercial, verdad física y resultado de entrega. |
| Supporting | BC-01 Tenant & Access Governance; BC-02 Customer & Buyer Relationships; BC-03 Catalog & Commercial Policy; BC-07 Credit & Receivables; BC-11 Business Traceability | Hacen posible operar de forma segura, elegible, configurable, financieramente consistente y explicable. |
| Generic | BC-08 Payments; BC-09 Business Documents; BC-10 Notifications | Aíslan capacidades comunes o sustituibles sin transferirles la autoridad de los hechos de negocio. |

El modelo final contiene exactamente 11 Bounded Contexts:

| Código | Bounded Context |
| :--- | :--- |
| BC-01 | Tenant & Access Governance |
| BC-02 | Customer & Buyer Relationships |
| BC-03 | Catalog & Commercial Policy |
| BC-04 | Sales Commitment |
| BC-05 | Inventory Availability |
| BC-06 | Fulfillment & Delivery |
| BC-07 | Credit & Receivables |
| BC-08 | Payments |
| BC-09 | Business Documents |
| BC-10 | Notifications |
| BC-11 | Business Traceability |

Mobile, Operations Mobile, Buyer Mobile, Android, Flutter, iOS, cámara,
scanner, QR, push, offline, ubicación, mapas, cold chain e IoT no son
Bounded Contexts. Son superficies, capacidades, integraciones o decisiones de
implementación que consumen contratos de los contextos propietarios.

## Organización de la sección

- 2.5.1 EventStorming continúa el Big Picture presentado en 2.3.5 y lleva el
  modelo hasta puntos pivote, comandos, políticas, read models, agregados y
  límites estratégicos.
- 2.5.1.1 explica el razonamiento para descubrir candidatos y conservar las
  once fronteras.
- 2.5.1.2 presenta cinco Domain Stories, con actores, actividades, objetos de
  trabajo, autoridad y colaboración entre contextos.
- 2.5.1.3 completa un Bounded Context Canvas para cada contexto, en orden de
  importancia estratégica.
- 2.5.2 representa el Context Map, sus contratos, patrones y alternativas.
- 2.5.3 presenta la arquitectura C4 del sistema Nexa en niveles de contexto,
  container, componentes y deployment.

El diseño estratégico permanece separado de la implementación observada.
Bounded Context, Spring Modulith ApplicationModule, paquete Java, esquema
PostgreSQL, C4 Container y deployment unit son conceptos distintos. La
arquitectura objetivo conserva un Spring Boot modular monolith, PostgreSQL
físicamente compartido con ownership lógico y Object Storage detrás de puertos
de aplicación.

Las decisiones de dominio se leen junto con el Ubiquitous Language de 2.3.6 y
el diseño táctico de 2.6; esta sección no duplica diccionarios completos,
clases, tablas ni detalles de UX.
