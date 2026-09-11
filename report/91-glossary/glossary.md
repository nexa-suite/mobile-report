# Glosario

Este glosario resume el lenguaje ubicuo de negocio usado en el informe. Conserva
los términos en inglés cuando evitan ambigüedad; no define paquetes,
tablas, endpoints ni decisiones de implementación.

*Vocabulario de negocio canónico utilizado por Nexa.*

| Término | Significado en Nexa | No debe confundirse con |
| --- | --- | --- |
| Tenant | Cliente Nexa y límite máximo de aislamiento de negocio y datos. | Workspace, Customer Account o despliegue. |
| Workspace | Entorno operativo actual asociado 1:1 con un Tenant. | Tenant, C4 Container o frontera de seguridad independiente. |
| Human Identity | Identidad global de una persona para autenticación. | Workforce Membership o Buyer Relationship. |
| Workforce Membership | Relación de trabajo, acceso y capacidades dentro de un Tenant. | Human Identity o Buyer Relationship. |
| Customer Account | Registro comercial de un cliente dentro de un Tenant. | Human Identity o Buyer Relationship. |
| Buyer Relationship | Relación comercial aprobada entre un Buyer y el Tenant proveedor. | Customer Account o acceso genérico al portal. |
| Product | Concepto de catálogo. | SKU o Inventory Lot. |
| SKU | Identidad comercial vendible concreta, incluida su unidad de medida. | Product o lote físico. |
| Base Price | Precio inicial autorizado del catálogo. | Precio final resuelto. |
| Price List | Configuración de precios aplicable a Tenant o cliente. | Identidad de SKU u override comercial arbitrario. |
| Customer Terms | Condiciones comerciales permitidas para un cliente. | Price List, Payment o Receivable. |
| Promotion | Única transformación permitida sobre el precio resuelto en el alcance actual. | Descuentos acumulados o autoridad de precio. |
| Draft (Cart / Request Draft) | Intención del Buyer antes de un envío autoritativo. | Purchase Request o compromiso de inventario. |
| Purchase Request | Solicitud comercial del Buyer sujeta a revisión. | Sales Order, orden de compra de proveedor o Draft SO. |
| Commercial Commitment | Demanda persistente de SKU y cantidad, propiedad de un PR/SO y neutral respecto de Warehouse. | Inventory Reservation, Warehouse Backing, Physical Allocation o Inventory Lot. |
| Sales Order | Obligación comercial confirmada e inmutable. | Purchase Request o liquidación financiera. |
| Physical Stock | Cantidad física en un Warehouse, incluso si no es vendible. | Sellable Availability. |
| Sellable Availability | Existencia utilizable menos compromisos activos y Safety Stock, autorizada por SKU y Warehouse. | Physical Stock o un total global sin calificar. |
| Inventory Reservation | Protección de demanda de Commercial Commitment propiedad de Inventory y distribuida sin seleccionar lote. | Commercial Commitment o Physical Allocation. |
| Warehouse Backing | Distribución determinista por SKU y Warehouse de la protección de Inventory Reservation. | Propiedad del Commercial Commitment o asignación de lote. |
| Safety Stock | Cantidad de política protegida en Warehouse. | Commitment, allocation o stock no utilizable. |
| Inventory Lot | Unidad de stock físico trazable en un Warehouse a la vez. | Manufacturer Batch o SKU. |
| Physical Allocation | Selección y autoridad de Inventory Lot(s) frente a un compromiso. | Commercial Commitment o escaneo de fulfillment. |
| Fulfillment | Trabajo operativo para preparar bienes comprometidos. | Delivery o Dispatch. |
| Dispatch | Coordinación y handoff de trabajo operativo. | Delivery o Route. |
| Delivery | Obligación programada o en intento de entregar bienes. | Delivery Attempt o Dispatch. |
| Delivery Attempt | Un intento dentro de la misma Delivery. | Nueva Delivery o finalización automática. |
| Continuation Delivery | Nueva Delivery para la cantidad restante después de una entrega parcial. | Reintento del intento original o backorder automático. |
| POD (Proof of Delivery) | Evidencia inmutable de entrega autorizada. | Estado mutable de Delivery. |
| Temperature Excursion | Observación fuera de rango que requiere evaluación. | Destrucción o cuarentena automáticas. |
| ColdChainDisposition | Resultado autorizado para cantidad afectada: `RELEASE`, `CONTINUE_HOLD`, `REJECT` o `WASTE`. | Destrucción automática o sinónimo de RETURN_TO_SUPPLIER. |
| HOLD | Cantidad no vendible pendiente de una disposición. | Quarantine, Waste o Release. |
| Credit Reservation | Crédito reservado para demanda comercial activa. | Outstanding Receivable. |
| Available Credit | Credit Limit menos Credit Reservations y Outstanding Receivables. | Saldo global del Buyer, `exposure` o `used`. |
| Receivable | Deuda o derecho de cobro comercial formal. | Payment o renderizado de documento. |
| Payment | Ciclo de movimiento, reporte y confirmación de dinero. | Proveedor de pagos o Receivable. |
| Payment Reported (Payment Report) | Afirmación manual o externa de pago que aún requiere manejo autorizado. | Payment Confirmed. |
| Payment Confirmed | Pago confirmado por el flujo autorizado. | Mero reporte de pago. |
| Financial Adjustment | Corrección explícita de una obligación financiera histórica; el documento emitido conserva su snapshot. | Reescritura silenciosa, mutación sólo documental o nota de crédito SUNAT automática. |
| Business Document | Artefacto comercial o de evidencia emitido con historial inmutable. | Security Audit o documento fiscal automático. |
| Notification | Intención de entrega y estado de canal. | Hecho fuente de negocio o Business Traceability. |
| Business Traceability | Representación durable de hechos significativos y su línea de tiempo. | Notification o Security Audit. |
| Security Audit | Evidencia de seguridad y autorización. | Línea de tiempo de negocio del Buyer. |

*Nota.* El vocabulario expresa el diseño de dominio propuesto para Nexa y no
acredita que una capacidad, estado o integración esté implementada en una
aplicación actual.
