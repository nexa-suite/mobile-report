# 2.6.x.2 Interface Layer

En esta capa se documentarán los Controllers, Consumers y demás puntos de entrada que expongan las capacidades del Bounded Context seleccionado. Las interfaces se describirán desde el contrato y la responsabilidad, no desde una lista inventada de endpoints.

La superficie móvil podrá consumir estas capacidades, pero no será presentada como propietaria del dominio.

## Uso de la plantilla

Los contratos y su crosswalk `AS-IS/TARGET` están separados por contexto en
[bounded-contexts](../bounded-contexts/). URI y DTO no evidenciados no deben
inventarse a partir de este placeholder.
