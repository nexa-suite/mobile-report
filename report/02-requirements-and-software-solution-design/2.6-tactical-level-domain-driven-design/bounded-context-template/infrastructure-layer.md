# 2.6.x.4 Infrastructure Layer

En esta capa se documentarán las implementaciones de Repository, el acceso a PostgreSQL, la mensajería y los adaptadores de servicios externos que correspondan al Bounded Context. La persistencia compartida de V1 no significa que todos los contextos compartan ownership de las mismas tablas.

Las integraciones deberán conservar los límites de autorización, idempotencia y traducción definidos en el Context Map.

## Uso de la plantilla

Cada paquete de [bounded-contexts](../bounded-contexts/) identifica persistencia
objetivo, adapters y límites de evidencia. PostgreSQL es físicamente compartido
con ownership lógico; este placeholder no asigna tablas.
