### 2.6.3. Bounded Context: Catalog & Commercial Policy

Product, SKU, precio, términos y promociones permanecen diferenciados. Los
contextos posteriores referencian identidad o snapshots de SKU, no un grafo de
objetos Product.

#### 2.6.3.1. Domain Layer

*Agregados y límites invariantes de BC-03.*
| Aggregate/raíz | Límite e invariante |
| :--- | :--- |
| `Product` | Identidad y ciclo de vida comercial; las referencias a media y SKU permanecen acotadas |
| `SKU` | Identidad vendible direccionable de forma independiente, empaque y política de cadena de frío |
| `PriceList` | Ítems de precio efectivo e intervalos de vigencia |
| `CustomerTerms` | Elegibilidad de términos para un Customer Account referenciado |
| `Promotion` | Una transformación elegible; las promociones no se acumulan |

Los Value Objects de diseño incluyen `Money`, `Currency`, `SkuId`, `Visibility`,
`CommercialSnapshot` y `ColdChainRequirement`. `PriceResolver`,
`OfferResolutionPolicy` y `PromotionStackingPolicy` son límites de políticas de
dominio; `ProductRepository` y `SkuRepository` poseen sólo los roots de este
contexto. La resolución autoritativa de precio se revalida en la decisión PR/SO;
los previews no reservan inventario ni crédito. Product != SKU.

#### 2.6.3.2. Interface Layer

La Interface Layer cubre ciclo de vida de Product/SKU, consulta de catálogo y
resolución efectiva de precio/términos. Las respuestas API son contratos, no
entidades de persistencia; Mobile puede almacenar proyecciones seguras, pero no
establecer autoridad de precio ni requisitos de cold chain. Los nombres de URI y
DTO fuera de la evidencia API verificada permanecen abiertos.

#### 2.6.3.3. Application Layer

La Application Layer gestiona Product, SKU, listas de precios, promociones y la
resolución autoritativa de ofertas. Valida alcance Tenant, intervalos efectivos
y precedencia de políticas. La semántica de idempotency/version protege cambios
concurrentes de catálogo; los snapshots autoritativos pasan a Sales Commitment
como datos inmutables.

#### 2.6.3.4. Infrastructure Layer

La Infrastructure Layer organiza la propiedad lógica en PostgreSQL compartido sobre `product`, `sku`, `catalog_media`,
`price_list`, `price_list_item`, `base_price`, `customer_terms`, `promotion`
y `promotion_sku`. Los bytes de Object Storage permanecen detrás de un port de
aplicación. Ninguna tabla Product/SKU pertenece directamente a Sales o
Inventory; se usan IDs y snapshots inter-BC.

#### 2.6.3.5. Bounded Context Software Architecture Component Level Diagrams

Las siguientes clases son especificaciones **TARGET**. Conservan `Product` y
`SKU` como conceptos distintos, y separan una consulta de precio de la decisión
comercial autoritativa posterior.

*Clases TARGET por capa de BC-03*

| Capa | Clase | Tipo | Responsabilidad y límite de consistencia |
| --- | --- | --- | --- |
| Interface | `CatalogManagementController` | Controller | Traduce altas y cambios de Product, SKU y política comercial autorizados. |
| Interface | `CatalogPricingController` | Controller | Expone una consulta de precio/términos; una respuesta previa no crea compromiso. |
| Interface | `CatalogProjectionConsumer` | Consumer | Proyecta catálogo seguro para Platform, Portal o Mobile sin conceder visibilidad por sí mismo. |
| Application | `ManageProductHandler` | Command handler | Mantiene ciclo de vida de Product y metadatos de media dentro de su límite. |
| Application | `ManageSkuHandler` | Command handler | Conserva la identidad independiente de SKU y su requisito de cadena de frío cuando corresponda. |
| Application | `ResolveCatalogPriceHandler` | Query/application service | Aplica precedencia Base Price, Price List, Customer Terms y una Promotion; distingue preview de snapshot autoritativo. |
| Application | `ManagePriceListHandler` | Command handler | Protege intervalos efectivos versionados para evitar precios activos solapados. |
| Infrastructure | `CatalogProductRepositoryAdapter` | Repository implementation | Persiste Product y media referenciada en PostgreSQL compartido. |
| Infrastructure | `CatalogPricingAdapter` | Query adapter | Ejecuta la consulta efectiva de precio sin trasladar la política al cliente. |
| Infrastructure | `ObjectStorageMediaPort` | Storage adapter | Mantiene bytes de media fuera de PostgreSQL y bajo autorización de aplicación. |
| Infrastructure | `CatalogAuthorizationPort` | Contract adapter | Revalida Tenant y capacidad con BC-01 antes de mutar catálogo. |

La vista C4 L3 **TARGET** muestra componentes conceptuales de este contexto dentro de Nexa API. No equivale a un Bounded Context adicional, una base de datos independiente ni una unidad de despliegue.

*Vista C4 L3 TARGET de BC-03 Catalog & Commercial Policy.*

![BC-03 Catalog & Commercial Policy — C4 L3 TARGET](../../../assets/chapter-2/c4/Nexa-API-BC-03-CatalogCommercialPolicy-TARGET-dark.svg)

*Nota.* Exportación vectorial desde una vista Structurizr DSL enfocada en BC-03 Catalog & Commercial Policy, dentro del único contenedor Nexa API. Es evidencia de diseño TARGET; no acredita implementación, runtime ni una unidad de despliegue independiente. El diagrama se presenta como modelo de diseño y no como prueba de una implementación en ejecución.

#### 2.6.3.6. Bounded Context Software Architecture Code Level Diagrams

##### 2.6.3.6.1. Bounded Context Domain Layer Class Diagrams

*Modelo de dominio táctico de BC-03 Catalog & Commercial Policy.*
![BC-03 tactical domain model](../../../assets/chapter-2/tactical/BC-03/BC03_CatalogCommercialPolicy.png)
*Nota.* El diagrama se presenta como modelo de diseño y no como prueba de una implementación en ejecución.


##### 2.6.3.6.2. Bounded Context Database Design Diagram

*Proyección del diseño de base de datos de BC-03.*
![BC-03 database design projection](../../../assets/chapter-2/tactical/BC-03/database-diagram.png)

*Nota.* Es una proyección lógica de PostgreSQL compartido con restricciones; el SQL canónico mantiene la autoridad.
