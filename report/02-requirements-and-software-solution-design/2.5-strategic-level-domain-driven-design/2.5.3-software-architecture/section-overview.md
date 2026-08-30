# 2.5.3 Software Architecture

La arquitectura se documentará con C4 y se basará en las vistas canónicas de `blueprint`. Nexa es el sistema principal; Website, Platform, Buyer Portal, API, PostgreSQL y Object Storage son los containers V1 aceptados. Operations Mobile y Buyer Mobile permanecen como containers planificados y propuestos.

Los diagramas deben distinguir el modelo lógico del dominio, los containers ejecutables y el runtime local. Los módulos de código no se convertirán automáticamente en Bounded Contexts o containers C4.
