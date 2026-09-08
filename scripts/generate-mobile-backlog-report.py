#!/usr/bin/env python3
"""Generate the professor-facing Chapter 2.4 artifacts from live Mobile sources.

The lifecycle index is read from master-mobile-backlog.md and the story body
and acceptance criteria are read from mobile-v1-catalog.md. Canonical IDs and
Gherkin keywords remain stable while the report narrative is presented in
Spanish.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BLUEPRINT = ROOT.parent / "blueprint/03-mobile/requirements"
REPORT = ROOT
MASTER = BLUEPRINT / "master-mobile-backlog.md"
CATALOG = BLUEPRINT / "mobile-v1-catalog.md"
USER_STORIES = (
    REPORT
    / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.1-user-stories.md"
)
PRODUCT_BACKLOG = (
    REPORT
    / "report/02-requirements-and-software-solution-design/2.4-requirements-specification/2.4.3-product-backlog.md"
)


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_master() -> list[dict[str, str]]:
    lines = MASTER.read_text(encoding="utf-8").splitlines()
    headers: list[str] | None = None
    rows: list[dict[str, str]] = []
    for line in lines:
        if line.startswith("| ID | Title | Actor |"):
            headers = table_cells(line)
            continue
        if headers and line.startswith("| MOB-US-"):
            cells = table_cells(line)
            if len(cells) == len(headers):
                rows.append(dict(zip(headers, cells)))
    if len(rows) != 73:
        raise SystemExit(f"master backlog expected 73 rows, got {len(rows)}")
    return rows


def parse_catalog() -> dict[str, dict[str, object]]:
    text = CATALOG.read_text(encoding="utf-8")
    matches = list(re.finditer(r"^## (MOB-US-\d{3}) — (.+)$", text, re.MULTILINE))
    result: dict[str, dict[str, object]] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.start() : end]
        story_match = re.search(
            r"^### User Story\s*\n\n(.+?)\n\n### Acceptance Criteria",
            block,
            re.MULTILINE | re.DOTALL,
        )
        scenarios = re.findall(r"^- (Scenario: .+)$", block, re.MULTILINE)
        result[match.group(1)] = {
            "title": match.group(2).strip(),
            "story": story_match.group(1).strip() if story_match else "",
            "scenarios": scenarios,
        }
    if len(result) != 73:
        raise SystemExit(f"mobile catalog expected 73 stories, got {len(result)}")
    return result


EPICS: dict[str, tuple[str, str, list[str]]] = {
    "MOBILE-EPIC-01": ("Acceso seguro y contexto de trabajo", "Permitir que cada persona retome el trabajo autorizado dentro de la empresa y el ámbito correcto.", ["MOB-US-001", "MOB-US-002", "MOB-US-003"]),
    "MOBILE-EPIC-02": ("Recepción, identificación y preparación de almacén", "Recibir, identificar y preparar stock conservando datos seguros de lote y condición.", ["MOB-US-011", "MOB-US-012", "MOB-US-013", "MOB-US-014", "MOB-US-015", "MOB-US-016", "MOB-US-017", "MOB-US-019"]),
    "MOBILE-EPIC-03": ("Preparación de despacho y handoff", "Preparar y liberar una entrega con evidencia clara de bienes y responsabilidad explícita.", ["MOB-US-020", "MOB-US-021", "MOB-US-022", "MOB-US-023", "MOB-US-024", "MOB-US-025"]),
    "MOBILE-EPIC-04": ("Ejecución de entrega y prueba", "Ejecutar una entrega asignada y conservar su resultado y prueba con atribución.", ["MOB-US-026", "MOB-US-027", "MOB-US-028", "MOB-US-031", "MOB-US-032", "MOB-US-033", "MOB-US-034"]),
    "MOBILE-EPIC-05": ("Handoff de entrega, recepción del comprador y actualizaciones críticas", "Verificar el handoff previsto, registrar la recepción del comprador y comunicar cambios críticos.", ["MOB-US-044", "MOB-US-047", "MOB-US-048", "MOB-US-049"]),
    "MOBILE-EPIC-06": ("Conveniencia comercial y operativa móvil", "Preparar y seguir trabajo operativo, comercial y financiero con información autorizada.", ["MOB-US-004", "MOB-US-005", "MOB-US-006", "MOB-US-007", "MOB-US-008", "MOB-US-009", "MOB-US-010", "MOB-US-036", "MOB-US-037", "MOB-US-038", "MOB-US-039", "MOB-US-040", "MOB-US-041", "MOB-US-042", "MOB-US-043"]),
    "MOBILE-EPIC-07": ("Movilidad avanzada de campo y operación offline", "Extender el trabajo de campo sólo cuando se acepten reglas explícitas de ubicación, contacto y recuperación.", ["MOB-US-018", "MOB-US-029", "MOB-US-030", "MOB-US-035", "MOB-US-045", "MOB-US-046"]),
    "MOBILE-EPIC-08": ("Transferencia de almacén y exactitud de inventario", "Resolver transferencias, conteos, disposiciones y resultados de exactitud del almacén.", ["MOB-US-050", "MOB-US-051", "MOB-US-052", "MOB-US-053", "MOB-US-054", "MOB-US-055", "MOB-US-056"]),
    "MOBILE-EPIC-09": ("Excepciones de despacho y coordinación de entrega", "Resolver excepciones de despacho y entrega preservando responsabilidad y evidencia.", ["MOB-US-057", "MOB-US-058", "MOB-US-059", "MOB-US-060", "MOB-US-061", "MOB-US-062", "MOB-US-063", "MOB-US-064", "MOB-US-065", "MOB-US-066"]),
    "MOBILE-EPIC-10": ("Continuidad de entrega para el comprador", "Ayudar al comprador a preparar, comprender y evidenciar la continuidad de la entrega y su línea de tiempo.", ["MOB-US-067", "MOB-US-068", "MOB-US-069"]),
    "MOBILE-EPIC-11": ("Seguimiento comercial y financiero", "Llevar documentos, evidencia de pago y seguimiento de visitas de cliente con autorización verificable.", ["MOB-US-070", "MOB-US-071", "MOB-US-072"]),
    "MOBILE-EPIC-12": ("Operaciones de campo inteligentes futuras", "Explorar asistencia controlada a partir de observaciones más ricas del almacén.", ["MOB-US-073"]),
}


TITLE_ES = {
    "MOB-US-001": "Continuar el trabajo autorizado después de volver a Nexa",
    "MOB-US-002": "Trabajar en la empresa y contexto de negocio previstos",
    "MOB-US-003": "Ver sólo el trabajo permitido para el rol",
    "MOB-US-004": "Revisar el trabajo operativo de un vistazo",
    "MOB-US-005": "Identificar excepciones operativas críticas",
    "MOB-US-006": "Encontrar un cliente y su relación con el comprador",
    "MOB-US-007": "Revisar productos, precios y disponibilidad",
    "MOB-US-008": "Preparar una solicitud de cliente",
    "MOB-US-009": "Enviar una Purchase Request desde el trabajo de campo",
    "MOB-US-010": "Seguir compromisos del cliente y crédito",
    "MOB-US-011": "Identificar un producto mediante el código del paquete o etiqueta",
    "MOB-US-012": "Buscar manualmente un producto cuando no hay escaneo",
    "MOB-US-013": "Registrar el stock recién recibido",
    "MOB-US-014": "Registrar lote, vencimiento y cantidad reales",
    "MOB-US-015": "Comprobar lote y condición del stock antes del trabajo físico",
    "MOB-US-016": "Preparar el lote y cantidad correctos para el trabajo",
    "MOB-US-017": "Reportar una discrepancia física o disposición autorizada de stock",
    "MOB-US-018": "Mover stock entre ubicaciones del almacén",
    "MOB-US-019": "Registrar evidencia de temperatura para stock relevante",
    "MOB-US-020": "Ver entregas listas para preparar el despacho",
    "MOB-US-021": "Asignar un conductor a una entrega lista",
    "MOB-US-022": "Comprobar bienes salientes contra la entrega preparada",
    "MOB-US-023": "Conservar evidencia del handoff entre almacén y conductor",
    "MOB-US-024": "Identificar de forma confiable un handoff de despacho",
    "MOB-US-025": "Confirmar que los bienes dejaron el control del almacén",
    "MOB-US-026": "Ver entregas asignadas al conductor",
    "MOB-US-027": "Iniciar una entrega asignada",
    "MOB-US-028": "Abrir indicaciones hacia el destino autorizado de la entrega",
    "MOB-US-029": "Compartir la ubicación durante una entrega activa",
    "MOB-US-030": "Contactar al comprador durante la entrega",
    "MOB-US-031": "Registrar el resultado del intento de entrega",
    "MOB-US-032": "Registrar una entrega parcial o rechazada y lo que queda",
    "MOB-US-033": "Conservar el Proof of Delivery",
    "MOB-US-034": "Presentar un código acotado de handoff de entrega",
    "MOB-US-035": "Continuar la evidencia de entrega después de perder conexión",
    "MOB-US-036": "Explorar productos del proveedor",
    "MOB-US-037": "Revisar precio y disponibilidad del producto",
    "MOB-US-038": "Preparar una Purchase Request",
    "MOB-US-039": "Repetir una compra anterior",
    "MOB-US-040": "Enviar una solicitud o realizar un Direct Order",
    "MOB-US-041": "Responder a un cambio material",
    "MOB-US-042": "Seguir solicitudes y pedidos",
    "MOB-US-043": "Revisar estado de crédito y pago",
    "MOB-US-044": "Saber cuándo una entrega requiere atención",
    "MOB-US-045": "Ver un conductor activo en un mapa",
    "MOB-US-046": "Contactar al conductor",
    "MOB-US-047": "Verificar una entrega mediante el código de handoff",
    "MOB-US-048": "Confirmar las cantidades realmente recibidas",
    "MOB-US-049": "Reportar una discrepancia sin borrar los hechos",
    "MOB-US-050": "Gestionar una discrepancia de recepción con evidencia",
    "MOB-US-051": "Retener o poner en cuarentena stock y resolverlo",
    "MOB-US-052": "Confirmar la recepción en el destino de una transferencia interna",
    "MOB-US-053": "Realizar un conteo cíclico y solicitar corrección de stock",
    "MOB-US-054": "Solicitar sustitución de lote cuando FEFO no completa el trabajo",
    "MOB-US-055": "Usar información ampliada de identidad de producto, paquete y almacenamiento",
    "MOB-US-056": "Preparar un grupo de tareas de almacén",
    "MOB-US-057": "Resolver una discrepancia de despacho antes del handoff",
    "MOB-US-058": "Reasignar un conductor o reprogramar el despacho de forma segura",
    "MOB-US-059": "Preparar cargas agrupadas y múltiples paradas",
    "MOB-US-060": "Completar un handoff al transportista con responsabilidad trazable",
    "MOB-US-061": "Registrar evidencia de temperatura en el despacho",
    "MOB-US-062": "Señalar la llegada de una entrega activa",
    "MOB-US-063": "Seguir instrucciones de entrega y datos de contacto autorizados",
    "MOB-US-064": "Solicitar reprogramación de una entrega desde el campo",
    "MOB-US-065": "Registrar un incidente de entrega con mayor detalle",
    "MOB-US-066": "Recuperar una entrega activa mediante operación offline selectiva",
    "MOB-US-067": "Proporcionar instrucciones de entrega y contacto alternativo para la recepción",
    "MOB-US-068": "Revisar la línea de tiempo de la entrega y reconocer su finalización",
    "MOB-US-069": "Adjuntar evidencia a una discrepancia de entrega",
    "MOB-US-070": "Ver documentos de negocio vinculados a solicitud o pedido",
    "MOB-US-071": "Reportar evidencia de pago y ver el resultado de revisión",
    "MOB-US-072": "Trabajar con un cliente mediante una visita de campo autorizada",
    "MOB-US-073": "Usar evidencia de automatización de almacén en un trabajo controlado",
}


ACTOR_ES = {
    "Mobile User": "Usuario móvil",
    "Business Operations Manager": "Responsable de Operaciones",
    "Sales Representative": "Representante de Ventas",
    "Warehouse Operator": "Operador de Almacén",
    "Dispatch Coordinator": "Coordinador de Despacho",
    "Driver or Delivery Operator": "Conductor u Operador de Entrega",
    "Customer Buyer": "Comprador",
    "Customer Buyer or Sales Representative": "Comprador o Representante de Ventas",
}


TEXT_REPLACEMENTS = (
    ("Operations Mobile", "Nexa Operations Mobile"),
    ("Buyer Mobile", "Nexa Buyer Mobile"),
    ("Customer Buyer or Sales Representative", "Comprador o Representante de Ventas"),
    ("Driver or Delivery Operator", "Conductor u Operador de Entrega"),
    ("Business Operations Manager", "Responsable de Operaciones"),
    ("Sales Representative", "Representante de Ventas"),
    ("Warehouse Operator", "Operador de Almacén"),
    ("Dispatch Coordinator", "Coordinador de Despacho"),
    ("Customer Buyer", "Comprador"),
    ("Mobile User", "Usuario móvil"),
    ("no generic sync", "sin sincronización genérica"),
    ("provider-neutral", "independiente del proveedor"),
    ("server-side", "del servidor"),
    ("last-write-wins", "última escritura gana"),
    ("cold-chain", "cadena de frío"),
    ("customer", "cliente"),
    ("customers", "clientes"),
    ("buyer", "comprador"),
    ("buyers", "compradores"),
    ("supplier", "proveedor"),
    ("suppliers", "proveedores"),
    ("representative", "representante"),
    ("driver", "conductor"),
    ("manager", "responsable"),
    ("operator", "operador"),
    ("coordinator", "coordinador"),
    ("warehouse", "almacén"),
    ("dispatch", "despacho"),
    ("delivery", "entrega"),
    ("request", "solicitud"),
    ("requests", "solicitudes"),
    ("submission", "envío"),
    ("scanning", "escaneo"),
    ("payment", "pago"),
    ("policy", "política"),
    ("order", "pedido"),
    ("orders", "pedidos"),
    ("completion", "finalización"),
    ("status", "estado"),
    ("source", "fuente"),
    ("current", "actual"),
    ("future", "futuro"),
    ("feature", "capacidad"),
    ("device", "dispositivo"),
    ("provider", "proveedor"),
    ("automation", "automatización"),
    ("owner", "responsable"),
    ("mobile", "móvil"),
)


def translate_text(text: str) -> str:
    translated = text
    for source, target in TEXT_REPLACEMENTS:
        translated = re.sub(rf"\b{re.escape(source)}\b", target, translated, flags=re.IGNORECASE if source.islower() else 0)
    translated = translated.replace("quiero", "deseo")
    translated = translated.replace("el representative", "el representante")
    translated = translated.replace("el buyer", "el comprador")
    translated = translated.replace("el driver", "el conductor")
    translated = translated.replace("el customer", "el cliente")
    translated = translated.replace("la request", "la solicitud")
    translated = translated.replace("una request", "una solicitud")
    translated = translated.replace("un request", "una solicitud")
    translated = re.sub(r"\bPurchase solicituds?\b", "Purchase Request", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bDirect pedido\b", "Direct Order", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bSales pedido\b", "Sales Order", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bentrega Attempt\b", "Delivery Attempt", translated)
    translated = re.sub(r"\bProof of entrega\b", "Proof of Delivery", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bcomprador Receipt\b", "Buyer Receipt", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bconductor outcome\b", "Driver outcome", translated)
    translated = re.sub(r"\balmacén-to-conductor\b", "entre almacén y conductor", translated)
    translated = re.sub(r"\bdespacho handoff\b", "handoff de despacho", translated)
    translated = re.sub(r"\buna envío\b", "un envío", translated)
    translated = re.sub(r"\bel entrega\b", "la entrega", translated)
    translated = re.sub(r"\bdel entrega\b", "de la entrega", translated)
    translated = re.sub(r"\bal entrega\b", "a la entrega", translated)
    translated = re.sub(r"\bcomprador receipt\b", "Buyer Receipt", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bentrega handoff\b", "handoff de entrega", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bcarrier handoff\b", "handoff al transportista", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bbusiness document\b", "documento de negocio", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\breceiving\b", "recepción", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\binbound\b", "de entrada", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bavailability\b", "disponibilidad", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bhold\b", "retención", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bquarantine\b", "cuarentena", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bstops\b", "paradas", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bstop\b", "parada", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\blocation\b", "ubicación", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bfallback\b", "alternativa", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bdraft\b", "borrador", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\brecipients\b", "destinatarios", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\brecipient\b", "destinatario", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\brefresh\b", "actualización", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\brefund\b", "reembolso", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\breservation\b", "reserva", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\btracking\b", "seguimiento", translated, flags=re.IGNORECASE)
    translated = re.sub(r"(?<!Buyer )\breceipt\b", "recepción", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bun entrega\b", "una entrega", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bel entrega\b", "la entrega", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bese entrega\b", "esa entrega", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\beste entrega\b", "esta entrega", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\buna pedido silenciosa\b", "un pedido silencioso", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\buna pedido\b", "un pedido", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bentrega correcto\b", "entrega correcta", translated, flags=re.IGNORECASE)
    translated = re.sub(r"\bentrega y Attempt\b", "entrega y Delivery Attempt", translated)
    return translated


def actor_label(actor: str) -> str:
    return ACTOR_ES.get(actor, translate_text(actor))


def app_label(app: str) -> str:
    return "; ".join(
        "Nexa Operations Mobile" if value.strip() == "Operations Mobile" else
        "Nexa Buyer Mobile" if value.strip() == "Buyer Mobile" else value.strip()
        for value in app.split(";")
    )


def priority_label(priority: str) -> str:
    labels = {"1": "Alta", "2": "Media", "3": "Baja"}
    number = priority.strip()[-1:]
    if number not in labels:
        raise SystemExit(f"unsupported priority: {priority}")
    return labels[number]


def academic_scenarios(story_id: str) -> list[str]:
    return [
        translate_text(line)
        for line in AC[story_id]
        if not re.search(r"Postergación|deferred|fuera de V1", line, re.IGNORECASE)
    ]


BC_NAMES = {
    "BC-01": "Tenant & Access Governance",
    "BC-02": "Customer & Buyer Relationships",
    "BC-03": "Catalog & Commercial Policy",
    "BC-04": "Sales Commitment",
    "BC-05": "Inventory Availability",
    "BC-06": "Fulfillment & Delivery",
    "BC-07": "Credit & Receivables",
    "BC-08": "Payments",
    "BC-09": "Business Documents",
    "BC-10": "Notifications",
    "BC-11": "Business Traceability",
}


CAP_NAMES = {
    "CAP-02": "Acceso y gobernanza de la fuerza de trabajo",
    "CAP-03": "Cuentas de clientes y relaciones con compradores",
    "CAP-04": "Catálogo y política comercial",
    "CAP-05": "Compras y borradores del comprador",
    "CAP-06": "Purchase Requests y Sales Orders",
    "CAP-07": "Disponibilidad y reserva de inventario",
    "CAP-08": "Recepción y operaciones de almacén",
    "CAP-09": "Fulfillment, despacho y entrega",
    "CAP-10": "Evidencia de cadena de frío y disposición",
    "CAP-11": "Crédito y cuentas por cobrar",
    "CAP-12": "Pagos y correcciones",
    "CAP-13": "Documentos de negocio",
    "CAP-14": "Notificaciones",
    "CAP-15": "Trazabilidad de negocio",
    "CAP-16": "Visibilidad operativa",
}


UNESTIMATED_POINTS = {
    "MOB-US-029": "8",
    "MOB-US-045": "8",
    "MOB-US-054": "8",
    "MOB-US-055": "5",
    "MOB-US-056": "8",
    "MOB-US-059": "8",
    "MOB-US-060": "5",
    "MOB-US-066": "8",
    "MOB-US-072": "5",
    "MOB-US-073": "8",
}


GLOBAL_BACKLOG_ORDER = [
    "LAND-US-001", "LAND-US-002", "LAND-US-003", "LAND-US-004",
    "LAND-US-005", "LAND-US-006",
    "MOB-US-011", "MOB-US-012", "MOB-US-013", "MOB-US-014",
    "MOB-US-015", "MOB-US-016", "MOB-US-017", "MOB-US-019",
    "MOB-US-022", "MOB-US-023", "MOB-US-024", "MOB-US-020",
    "MOB-US-021", "MOB-US-025", "MOB-US-026", "MOB-US-027",
    "MOB-US-028", "MOB-US-031", "MOB-US-032", "MOB-US-033",
    "MOB-US-034", "MOB-US-044", "MOB-US-047", "MOB-US-048",
    "MOB-US-049", "MOB-US-001", "MOB-US-002", "MOB-US-003",
    "TS-MOB-001", "TS-MOB-010", "SPIKE-002", "TS-MOB-005",
    "TS-MOB-006", "TS-MOB-007", "TS-MOB-008", "MOB-US-004",
    "MOB-US-005", "MOB-US-006",
    "MOB-US-007", "MOB-US-008", "MOB-US-009", "MOB-US-010",
    "MOB-US-018", "MOB-US-030", "MOB-US-035", "MOB-US-050",
    "MOB-US-051", "MOB-US-052", "MOB-US-053", "MOB-US-057",
    "MOB-US-058", "MOB-US-061", "MOB-US-062", "MOB-US-063",
    "MOB-US-064", "MOB-US-065", "MOB-US-036", "MOB-US-037",
    "MOB-US-038", "MOB-US-040", "MOB-US-042", "MOB-US-043",
    "MOB-US-046", "MOB-US-039", "MOB-US-041", "TS-MOB-002",
    "TS-MOB-003", "TS-MOB-004", "TS-MOB-009", "TS-MOB-011",
    "TS-MOB-012", "SPIKE-001", "SPIKE-003", "SPIKE-004",
    "SPIKE-005", "SPIKE-006", "MOB-US-045", "MOB-US-067",
    "MOB-US-068", "MOB-US-069", "MOB-US-070", "MOB-US-071",
    "MOB-US-072", "MOB-US-054", "MOB-US-055", "MOB-US-056",
    "MOB-US-059", "MOB-US-060", "MOB-US-066", "MOB-US-029",
    "MOB-US-073",
]


S2_IDS = {
    "MOB-US-004", "MOB-US-005", "MOB-US-006", "MOB-US-007",
    "MOB-US-008", "MOB-US-009", "MOB-US-010", "MOB-US-018",
    "MOB-US-030", "MOB-US-035", "MOB-US-050", "MOB-US-051",
    "MOB-US-052", "MOB-US-053", "MOB-US-057", "MOB-US-058",
    "MOB-US-061", "MOB-US-062", "MOB-US-063", "MOB-US-064",
    "MOB-US-065",
}


S3_IDS = {
    "MOB-US-036", "MOB-US-037", "MOB-US-038", "MOB-US-040",
    "MOB-US-042", "MOB-US-043", "MOB-US-046",
}


S4_IDS = {
    "MOB-US-039", "MOB-US-041", "MOB-US-067", "MOB-US-068",
    "MOB-US-069", "MOB-US-070", "MOB-US-071",
}


LANDING_BACKLOG = [
    ("LAND-US-001", "Comprender la propuesta B2B de cadena de frío de Nexa", "2", "S1"),
    ("LAND-US-002", "Evaluar el ajuste con el perfil operativo", "3", "S1"),
    ("LAND-US-003", "Revisar capacidades y límites del producto", "2", "S1"),
    ("LAND-US-004", "Revisar precios, preguntas frecuentes e información legal", "2", "S1"),
    ("LAND-US-005", "Iniciar el registro de la empresa y su Workspace", "3", "S1"),
    ("LAND-US-006", "Contactar a Nexa o solicitar una demostración", "3", "S1"),
]


TECHNICAL_BACKLOG = [
    ("TS-MOB-001", "Integrar contratos REST con autoridad del servidor", "5", "S1"),
    ("TS-MOB-002", "Establecer una base Android Native con Kotlin", "5", "S2"),
    ("TS-MOB-003", "Establecer una base Flutter con Dart para Android e iOS", "5", "S3"),
    ("TS-MOB-004", "Establecer una base iOS Native con SwiftUI", "5", "S3"),
    ("TS-MOB-005", "Proteger el estado local selectivo y no autoritativo", "5", "S2"),
    ("TS-MOB-006", "Resolver reintentos, resultados inciertos e idempotencia", "5", "S2"),
    ("TS-MOB-007", "Integrar cámara e identificadores con alternativa manual", "3", "S2"),
    ("TS-MOB-008", "Abrir navegación externa con un límite de ubicación", "3", "S2"),
    ("TS-MOB-009", "Integrar notificaciones y deep links con autorización", "3", "S3"),
    ("TS-MOB-010", "Aplicar i18n y accesibilidad en las aplicaciones móviles", "3", "S1"),
    ("TS-MOB-011", "Preparar validación técnica y observabilidad mínima", "3", "S4"),
    ("TS-MOB-012", "Preparar evidencia de build, distribución y dispositivos", "3", "S4"),
]


SPIKE_BACKLOG = [
    ("SPIKE-001", "Investigar una oportunidad de aprendizaje autónomo", "3", "S3"),
    ("SPIKE-002", "Comparar bases compartidas y paridad funcional móvil", "5", "S1"),
    ("SPIKE-003", "Investigar identificadores Barcode, QR y GS1", "3", "S2"),
    ("SPIKE-004", "Investigar persistencia local y recuperación selectiva", "5", "S2"),
    ("SPIKE-005", "Investigar notificaciones push y deep links", "3", "S3"),
    ("SPIKE-006", "Investigar mapas, ubicación, privacidad, batería y alternativa", "3", "S4"),
]


SPIKE_SUMMARY = {
    "SPIKE-001": (
        "Determinar qué oportunidad de aprendizaje autónomo aporta valor al trabajo móvil",
        "Matriz de oportunidades, fuentes, datos, privacidad, factibilidad y prueba acotada",
        "Recomendación documentada y límites de uso definidos, sin afirmar resultados de producción",
    ),
    "SPIKE-002": (
        "Determinar bases compartidas y estrategia de paridad funcional para Nexa Operations Mobile y Nexa Buyer Mobile",
        "Matriz de flujos, seguridad, estado local, distribución y paridad entre Android Native/Kotlin, Flutter/Dart e iOS Native/SwiftUI",
        "Trade-offs y límites documentados para las tres tecnologías aceptadas; Liquid Glass queda como consideración de presentación",
    ),
    "SPIKE-003": (
        "Determinar el alcance de Barcode, QR, GS1 y la alternativa manual para identificar productos",
        "Comparación de formatos, permisos, ambigüedad, expiración, reutilización y validación del servidor",
        "Alcance de identificadores, límites de seguridad y preguntas abiertas documentados",
    ),
    "SPIKE-004": (
        "Definir qué información puede conservarse localmente y cómo recuperarla de forma selectiva",
        "Clasificación de datos, protección, reintentos, conflictos, secuencia de sincronización y prueba de recuperación",
        "Límite offline seguro documentado, sin éxito de negocio autoritativo sin confirmación del servidor",
    ),
    "SPIKE-005": (
        "Definir usos autorizados de notificaciones push y deep links",
        "Matriz de evento y canal, permisos, ámbito de Tenant, expiración, reintento y navegación",
        "Clases de notificación, límites de seguridad y relación con el estado de negocio documentados",
    ),
    "SPIKE-006": (
        "Definir el uso móvil de mapas y ubicación respetando privacidad, batería y conectividad",
        "Comparación de navegación externa, observaciones del dispositivo, permisos, consumo y alternativas",
        "Límite mínimo documentado; el alcance inicial se mantiene en navegación externa autorizada",
    ),
}


DESCRIPTIONS: dict[str, str] = {
    "MOB-US-001": "Como Mobile User, quiero continuar de forma segura el trabajo autorizado al volver a Nexa, para reanudarlo sin exponer información protegida.",
    "MOB-US-002": "Como Mobile User, quiero trabajar en la empresa y contexto de negocio previstos, para que cada tarea corresponda a la empresa y relación que pretendo atender.",
    "MOB-US-003": "Como Mobile User, quiero ver solo el trabajo permitido para mi rol, para no intentar tareas que mi rol o relación no autorizan.",
    "MOB-US-004": "Como Business Operations Manager, quiero revisar el trabajo operativo de un vistazo, para priorizarlo usando hechos actuales y confiables.",
    "MOB-US-005": "Como Business Operations Manager, quiero identificar excepciones operativas críticas, para atender trabajo bloqueado antes de que retrase a un customer o delivery.",
    "MOB-US-006": "Como Sales Representative, quiero encontrar una relación de customer y buyer, para trabajar con el customer correcto en un flujo mobile futuro.",
    "MOB-US-007": "Como Sales Representative, quiero revisar productos, precios y disponibilidad, para preparar demanda futura de customer con información confiable.",
    "MOB-US-008": "Como Sales Representative, quiero preparar una solicitud de customer, para organizar una intención antes de una submission autorizada.",
    "MOB-US-009": "Como Sales Representative, quiero enviar una Purchase Request desde el trabajo de campo, para que la demanda del customer entre en un proceso de compromiso autorizado.",
    "MOB-US-010": "Como Sales Representative, quiero seguir los compromisos y el crédito del customer, para comprender el progreso autorizado sin tomar localmente una decisión de crédito.",
    "MOB-US-011": "Como Warehouse Operator, quiero identificar un producto desde el código del paquete o etiqueta, para manipular el producto correcto durante el trabajo de almacén.",
    "MOB-US-012": "Como Warehouse Operator, quiero buscar manualmente un producto cuando el scanning no está disponible, para continuar el trabajo seguro sin adivinar el producto.",
    "MOB-US-013": "Como Warehouse Operator, quiero registrar el stock que acaba de llegar, para que el almacén tenga un registro confiable del stock recibido.",
    "MOB-US-014": "Como Warehouse Operator, quiero registrar el lote, vencimiento y cantidad reales, para que el picking futuro use lo que llegó físicamente.",
    "MOB-US-015": "Como Warehouse Operator, quiero comprobar el lote actual y la condición del stock antes del trabajo físico, para elegir stock seguro y disponible para la tarea.",
    "MOB-US-016": "Como Warehouse Operator, quiero hacer picking del lote y cantidad correctos para el trabajo preparado, para que la entrega reciba el stock realmente preparado.",
    "MOB-US-017": "Como Warehouse Operator, quiero reportar una discrepancia física o disposición autorizada del stock, para mantener visible la excepción sin borrar lo ocurrido.",
    "MOB-US-018": "Como Warehouse Operator, quiero mover stock entre ubicaciones del almacén, para que el movimiento físico sea atribuible desde el origen hasta el destino.",
    "MOB-US-019": "Como Warehouse Operator, quiero registrar evidencia de temperatura para el stock relevante, para que las decisiones de cold-chain usen una lectura física atribuible.",
    "MOB-US-020": "Como Dispatch Coordinator, quiero ver las entregas listas para preparación de dispatch, para preparar únicamente entregas listas para salir del almacén.",
    "MOB-US-021": "Como Dispatch Coordinator, quiero asignar un driver a una entrega lista, para que la responsabilidad quede clara antes del handoff.",
    "MOB-US-022": "Como Dispatch Coordinator, quiero comprobar los bienes salientes contra la entrega preparada, para que el driver reciba lo que la entrega realmente requiere.",
    "MOB-US-023": "Como Dispatch Coordinator, quiero conservar la evidencia del handoff warehouse-to-driver, para que el movimiento de bienes preparados pueda revisarse.",
    "MOB-US-024": "Como Dispatch Coordinator, quiero identificar de forma confiable un dispatch handoff, para mantener vinculados la entrega correcta y el driver durante todo el handoff.",
    "MOB-US-025": "Como Dispatch Coordinator, quiero confirmar que los bienes dejaron el control del almacén, para que todos puedan confiar en el estado de dispatch de la entrega.",
    "MOB-US-026": "Como Driver or Delivery Operator, quiero ver las entregas asignadas a mí, para conocer las entregas de las que soy responsable hoy.",
    "MOB-US-027": "Como Driver or Delivery Operator, quiero iniciar una entrega asignada, para que el Delivery Attempt tenga un inicio claro y autorizado.",
    "MOB-US-028": "Como Driver or Delivery Operator, quiero abrir indicaciones hacia el destino autorizado de la entrega, para viajar al destino correcto sin cambiar el registro de Delivery.",
    "MOB-US-029": "Como Driver or Delivery Operator, quiero compartir la ubicación de una entrega durante una entrega activa, para que un servicio de ubicación futuro y aceptado atienda una necesidad acotada de delivery.",
    "MOB-US-030": "Como Driver or Delivery Operator, quiero contactar al buyer durante la entrega, para resolver una duda de llegada mediante un canal autorizado.",
    "MOB-US-031": "Como Driver or Delivery Operator, quiero registrar el resultado del intento de entrega, para que el proveedor conozca lo ocurrido físicamente en el destino.",
    "MOB-US-032": "Como Driver or Delivery Operator, quiero registrar una entrega parcial o rechazada y lo que queda, para no perder ningún resultado físico ni obligación restante.",
    "MOB-US-033": "Como Driver or Delivery Operator, quiero conservar el Proof of Delivery, para que el resultado de Delivery pueda revisarse sin perder su historial.",
    "MOB-US-034": "Como Driver or Delivery Operator, quiero presentar un código acotado de delivery handoff, para que el buyer identifique correctamente la entrega de forma segura.",
    "MOB-US-035": "Como Driver or Delivery Operator, quiero continuar la evidencia de delivery después de perder conexión, para que un flujo futuro de recuperación proteja la evidencia sin afirmar éxito falso.",
    "MOB-US-036": "Como Customer Buyer, quiero explorar productos del supplier, para revisar productos ofrecidos mediante mi relación con el supplier.",
    "MOB-US-037": "Como Customer Buyer, quiero revisar el precio y disponibilidad del producto, para preparar una request futura con información actual del supplier.",
    "MOB-US-038": "Como Customer Buyer, quiero preparar una Purchase Request, para organizar una compra futura sin confirmarla falsamente.",
    "MOB-US-039": "Como Customer Buyer, quiero repetir una compra anterior, para preparar una nueva request más rápidamente en un flujo futuro.",
    "MOB-US-040": "Como Customer Buyer, quiero enviar una request o realizar un Direct Order, para que mi vía de compromiso elegida sea explícita y autorizada.",
    "MOB-US-041": "Como Customer Buyer, quiero responder a un cambio material, para que mi compromiso futuro refleje una decisión explícita.",
    "MOB-US-042": "Como Customer Buyer, quiero seguir requests y orders, para comprender el progreso comercial autorizado.",
    "MOB-US-043": "Como Customer Buyer, quiero revisar el estado de crédito y payment, para comprender lo adeudado sin tratar la evidencia reportada como confirmación.",
    "MOB-US-044": "Como Customer Buyer, quiero saber cuándo una entrega requiere atención, para responder oportunamente a un cambio relevante.",
    "MOB-US-045": "Como Customer Buyer, quiero ver en un mapa un driver activo, para que un servicio futuro y autorizado me ayude a comprender el horario de llegada.",
    "MOB-US-046": "Como Customer Buyer, quiero contactar al driver, para resolver una duda de llegada mediante un canal autorizado de Delivery.",
    "MOB-US-047": "Como Customer Buyer, quiero verificar una entrega mediante el código de handoff, para confirmar que reviso el Delivery correcto.",
    "MOB-US-048": "Como Customer Buyer, quiero confirmar las cantidades realmente recibidas, para que el proveedor tenga un registro veraz de mi Buyer Receipt.",
    "MOB-US-049": "Como Customer Buyer, quiero reportar una discrepancia sin borrar los hechos, para que el proveedor resuelva la diferencia manteniendo un historial confiable.",
    "MOB-US-050": "Como Warehouse Operator, quiero registrar una discrepancia de recepción inbound con evidencia, para que la decisión de receiving refleje lo encontrado físicamente.",
    "MOB-US-051": "Como Warehouse Operator, quiero colocar stock cuestionable en hold o quarantine y registrar su resolución, para impedir su uso antes de una decisión autorizada.",
    "MOB-US-052": "Como Warehouse Operator, quiero confirmar lo que llegó al destino de una transferencia interna, para que el registro de stock refleje el movimiento físico y cualquier diferencia.",
    "MOB-US-053": "Como Warehouse Operator, quiero contar una ubicación de almacenamiento y solicitar una corrección de stock, para resolver una diferencia física sin reescribir el historial.",
    "MOB-US-054": "Como Warehouse Operator, quiero solicitar una sustitución permitida de lote cuando el lote esperado no puede completar el trabajo, para revisar la order sin saltar la policy de availability.",
    "MOB-US-055": "Como Warehouse Operator, quiero usar información más rica de identidad de producto, paquete y almacenamiento, para manipular el stock previsto con menos errores de identificación.",
    "MOB-US-056": "Como Warehouse Operator, quiero preparar un grupo de tareas de almacén, para trabajar eficientemente sin perder el resultado de cada elemento.",
    "MOB-US-057": "Como Dispatch Coordinator, quiero resolver una discrepancia de dispatch antes del handoff, para que solo una entrega revisada abandone el control del almacén.",
    "MOB-US-058": "Como Dispatch Coordinator, quiero reasignar un driver o reprogramar un dispatch de forma segura, para que la entrega siga siendo responsabilidad de una persona elegible en un momento acordado.",
    "MOB-US-059": "Como Dispatch Coordinator, quiero preparar una carga de delivery agrupada con sus stops, para despachar entregas compatibles manteniendo visibles sus restricciones.",
    "MOB-US-060": "Como Dispatch Coordinator, quiero completar un carrier handoff con responsabilidad clara, para que todos sepan quién controla la carga después de que abandona el almacén.",
    "MOB-US-061": "Como Dispatch Coordinator, quiero registrar evidencia de temperatura en dispatch, para que la decisión de entrega refleje la condición observada antes del handoff.",
    "MOB-US-062": "Como Driver or Delivery Operator, quiero señalar la llegada de una entrega activa, para que el buyer y el equipo de delivery sepan que puede comenzar el handoff.",
    "MOB-US-063": "Como Driver or Delivery Operator, quiero seguir las instrucciones y datos de contacto permitidos de la entrega, para coordinar el handoff con la persona prevista.",
    "MOB-US-064": "Como Customer Buyer, quiero solicitar un horario de entrega diferente, para que el equipo de delivery decida cómo gestionar mi disponibilidad.",
    "MOB-US-065": "Como Driver or Delivery Operator, quiero registrar un incidente de delivery con sus detalles relevantes, para que el equipo tome una decisión de seguimiento informada.",
    "MOB-US-066": "Como Driver or Delivery Operator, quiero conservar evidencia seleccionada de delivery durante una pérdida de conexión, para recuperar el trabajo sin afirmar un resultado de delivery no confirmado.",
    "MOB-US-067": "Como Customer Buyer, quiero proporcionar instrucciones de entrega y un contacto alternativo para receipt, para que la entrega llegue a la persona correcta bajo las condiciones acordadas.",
    "MOB-US-068": "Como Customer Buyer, quiero revisar la línea de tiempo de la entrega y reconocer su completion, para comprender el resultado registrado sin cambiar el historial.",
    "MOB-US-069": "Como Customer Buyer, quiero adjuntar evidencia a una discrepancia de delivery, para que el supplier revise la diferencia reportada con su contexto.",
    "MOB-US-070": "Como Customer Buyer or Sales Representative, quiero ver un business document vinculado a una request u order, para usar la evidencia autorizada del trabajo comercial.",
    "MOB-US-071": "Como Customer Buyer, quiero reportar evidencia de payment y ver su resultado de revisión, para seguir un payment sin afirmar yo mismo su confirmación.",
    "MOB-US-072": "Como Sales Representative, quiero trabajar con un customer mediante una visita de campo autorizada, para iniciar con el contexto correcto de relación y terminar con un seguimiento claro.",
    "MOB-US-073": "Como Warehouse Operator, quiero revisar observaciones avanzadas de almacén mediante una decisión controlada, para que una automation futura ayude al trabajo sin convertirse en verdad de stock no examinada.",
}


AC: dict[str, list[str]] = {
    "MOB-US-001": [
        "Scenario: Retorno válido — Given una sesión válida y no revocada, When la persona vuelve a Nexa, Then Nexa confirma su identidad y expone solo el trabajo permitido.",
        "Scenario: Retorno expirado — Given una sesión expirada, revocada o malformada, When la persona vuelve, Then Nexa solicita nuevamente su identidad y no expone información protegida.",
        "Scenario: Confirmación no disponible — Given no se puede confirmar la identidad, When la persona vuelve sin conexión, Then Nexa indica que el trabajo no está disponible y no expone información protegida.",
        "Scenario: Reintento seguro — Given la persona repite el mismo retorno, When Nexa lo procesa, Then no duplica ninguna acción de negocio ni revela secretos.",
    ],
    "MOB-US-002": [
        "Scenario: Un contexto autorizado — Given existe un contexto autorizado, When la persona inicia el trabajo, Then Nexa usa ese contexto para cada lectura y acción permitida.",
        "Scenario: Varios contextos autorizados — Given existen varios contextos, When la persona elige uno, Then Nexa confirma la elección antes de mostrar trabajo protegido.",
        "Scenario: Contexto ya no válido — Given un contexto está suspendido o no autorizado, When la persona lo elige, Then Nexa lo rechaza y no expone información empresarial de ese alcance.",
        "Scenario: Cambio de contexto — Given la persona cambia de contexto, When el cambio tiene éxito, Then la información del contexto anterior no puede utilizarse en el nuevo.",
    ],
    "MOB-US-003": [
        "Scenario: Trabajo permitido — Given el rol de la persona permite una tarea, When Nexa confirma el rol, Then la persona puede realizarla en el contexto activo.",
        "Scenario: Permiso faltante — Given el rol no permite una tarea, When la persona intenta realizarla, Then Nexa la rechaza aunque información antigua sugiera lo contrario.",
        "Scenario: Cambio de permisos — Given cambian los permisos, When Nexa vuelve a comprobar el rol, Then el trabajo no disponible deja de aceptarse.",
        "Scenario: Permiso no confirmado — Given no se puede comprobar el permiso, When la persona intenta una tarea, Then Nexa la bloquea e indica que se requiere confirmación.",
    ],
    "MOB-US-004": [
        "Scenario: Vista futura — Given existe una vista operativa futura aceptada, When el manager la revisa, Then cada elemento indica su contexto y frescura.",
        "Scenario: Hechos incompletos — Given faltan hechos fuente o están desactualizados, When el manager revisa la vista, Then la limitación es explícita y no se inventa ningún total.",
        "Scenario: Alcance no autorizado — Given el manager carece de permiso de alcance, When solicita la vista, Then no se expone información operativa privada.",
        "Scenario: Postergación — Given la vista requerida no está aceptada, When se considera esta historia, Then permanece fuera de Mobile V1.",
    ],
    "MOB-US-005": [
        "Scenario: Excepción aceptada — Given existe una futura vista de excepciones aceptada, When el manager revisa un elemento, Then quedan claros su alcance, severidad y trabajo owner.",
        "Scenario: Excepción incompleta — Given los hechos de la excepción están incompletos, When se revisa el elemento, Then se marca como incompleto y no se trata como un nuevo estado de negocio.",
        "Scenario: Respuesta autorizada — Given una excepción requiere corrección, When el manager la sigue, Then Nexa dirige a la persona al trabajo owner autorizado.",
        "Scenario: Postergación — Given la vista de excepciones no está aceptada, When se considera esta historia, Then permanece fuera de Mobile V1.",
    ],
    "MOB-US-006": [
        "Scenario: Customer autorizado — Given existe una relación autorizada, When el representative busca, Then solo se devuelven customers permitidos.",
        "Scenario: Customer no relacionado — Given el customer no está relacionado o está suspendido, When el representative lo abre, Then el trabajo protegido no está disponible.",
        "Scenario: Resultado no confiable — Given la búsqueda está vacía o no disponible, When termina, Then no se adivina ni expone ningún customer.",
        "Scenario: Postergación — Given el acceso comercial no forma parte de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-007": [
        "Scenario: Producto autorizado — Given existe una relación autorizada con el customer, When se revisa un producto, Then se muestran precio y disponibilidad permitidos con su frescura.",
        "Scenario: Producto no disponible — Given un producto está oculto o no disponible, When se solicita, Then no puede tratarse como un compromiso.",
        "Scenario: Información modificada — Given cambia el precio o disponibilidad, When el representative continúa, Then Nexa exige confirmación actual.",
        "Scenario: Postergación — Given la revisión comercial está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-008": [
        "Scenario: Preparación de draft — Given se conocen productos permitidos, When el representative prepara una solicitud, Then las cantidades permanecen como intención y no crean compromiso.",
        "Scenario: Información modificada — Given cambia información del producto o customer, When se revisa la solicitud, Then el cambio es visible antes de la submission.",
        "Scenario: Draft local — Given la persona pierde conexión, When edita la solicitud, Then permanece como draft no confirmado.",
        "Scenario: Postergación — Given la preparación comercial de campo está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-009": [
        "Scenario: Request válida — Given existe una request aceptada y una relación autorizada, When el representative la envía, Then se registra una única Purchase Request.",
        "Scenario: Request inválida — Given la información está desactualizada o falta autorización, When el representative la envía, Then no se registra ningún compromiso parcial.",
        "Scenario: Resultado incierto — Given el resultado es desconocido, When el representative reintenta, Then Nexa resuelve el primer resultado sin crear una segunda request.",
        "Scenario: Postergación — Given el envío desde campo está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-010": [
        "Scenario: Progreso autorizado — Given existe una relación autorizada, When se revisa el progreso, Then los hechos de compromiso y crédito relevante muestran su frescura.",
        "Scenario: Hechos financieros incompletos — Given los hechos financieros están desactualizados o incompletos, When se revisan, Then la limitación es explícita y no se inventa ninguna decisión.",
        "Scenario: Pérdida de relación — Given la relación ya no está autorizada, When se solicita el progreso, Then no se exponen hechos protegidos.",
        "Scenario: Postergación — Given esta conveniencia está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-011": [
        "Scenario: Una coincidencia — Given un código permitido tiene una única coincidencia, When el operador lo proporciona, Then Nexa identifica el producto antes de cualquier acción de stock.",
        "Scenario: Código desconocido — Given el código es desconocido, ambiguo o está fuera del alcance de la persona, When el operador lo proporciona, Then Nexa lo rechaza y no adivina.",
        "Scenario: Cámara no disponible — Given la cámara o el scanner no está disponible, When el operador no puede proporcionar un código, Then puede usar la búsqueda manual de producto.",
        "Scenario: Identificación repetida — Given el operador proporciona nuevamente el mismo código, When Nexa lo resuelve, Then la identificación por sí sola no crea un hecho de recepción ni de picking.",
    ],
    "MOB-US-012": [
        "Scenario: Coincidencia exacta — Given se encuentra un producto permitido exacto, When el operador lo selecciona, Then Nexa identifica el producto para el siguiente paso.",
        "Scenario: Coincidencia ambigua — Given varios productos podrían coincidir, When el operador busca, Then Nexa exige una elección clara y no registra ningún hecho de stock.",
        "Scenario: Sin conexión — Given el operador no tiene conexión, When no se puede confirmar un producto, Then Nexa marca la elección como no verificada y bloquea el trabajo autoritativo de stock.",
        "Scenario: Selección repetida — Given el operador selecciona nuevamente el mismo producto, When repite la selección, Then no se duplica ningún hecho de recepción ni picking.",
    ],
    "MOB-US-013": [
        "Scenario: Llegada válida — Given el operador tiene permiso y proporciona producto, lote y cantidad positiva, When registra la llegada, Then Nexa registra un único hecho de stock recibido.",
        "Scenario: Llegada inválida — Given falta información requerida o es inválida, When el operador la registra, Then Nexa no realiza un cambio parcial de stock.",
        "Scenario: Resultado incierto — Given el resultado es desconocido, When el operador repite la misma llegada, Then Nexa devuelve el resultado original sin duplicar el stock.",
        "Scenario: Sin conexión — Given el operador no tiene conexión, When no se puede confirmar la llegada, Then Nexa muestra un estado no confirmado y no presenta el stock recibido como autoritativo.",
    ],
    "MOB-US-014": [
        "Scenario: Datos completos del lote — Given el operador proporciona lote válido, vencimiento y cantidad positiva, When confirma la llegada, Then Nexa conserva esos datos para el stock recibido.",
        "Scenario: Vencimiento inválido — Given falta el vencimiento, está malformado o no es aceptable, When el operador lo registra, Then Nexa rechaza la llegada y no crea stock vendible.",
        "Scenario: Llegada duplicada — Given se vuelve a enviar la misma llegada, When Nexa la recibe, Then permanece una sola llegada y la cantidad no se duplica.",
        "Scenario: Preparación local — Given el operador pierde conexión, When prepara datos del lote, Then permanecen no confirmados y no pueden convertir el stock en vendible.",
    ],
    "MOB-US-015": [
        "Scenario: Stock actual — Given el operador tiene permiso, When comprueba el stock, Then la cantidad física, cantidad vendible, lote y condición aparecen diferenciados.",
        "Scenario: Lote restringido — Given el stock está vencido, retenido, en cuarentena o asignado, When se comprueba, Then no se trata como libremente vendible.",
        "Scenario: Información desactualizada — Given la información está desactualizada o no disponible, When el operador inicia el trabajo, Then Nexa exige confirmación actual.",
        "Scenario: Otro alcance — Given el lote pertenece a otra empresa o almacén, When se comprueba, Then no se expone ningún dato de cantidad ni lote.",
    ],
    "MOB-US-016": [
        "Scenario: Picking FEFO — Given existe una asignación activa y lotes elegibles, When el operador selecciona el lote adecuado más antiguo, Then Nexa registra el picking contra ese lote y cantidad.",
        "Scenario: Picking inseguro — Given el lote es desconocido, vencido, está en cuarentena o no está asignado, When el operador intenta seleccionarlo, Then Nexa rechaza el picking sin consumir stock.",
        "Scenario: Exceso de stock — Given la cantidad solicitada excede la asignación restante, When el operador hace picking, Then Nexa rechaza el exceso y conserva la cantidad restante.",
        "Scenario: Picking repetido — Given el resultado es desconocido, When el operador repite el mismo picking, Then Nexa devuelve un único resultado y no consume stock dos veces.",
    ],
    "MOB-US-017": [
        "Scenario: Diferencia observada — Given el operador observa una diferencia, When se acepta el reporte autorizado, Then las cantidades ofrecidas, seleccionadas y restantes permanecen registradas por separado.",
        "Scenario: Autoridad faltante — Given falta permiso, motivo o evidencia requerida, When el operador reporta la diferencia, Then Nexa no registra ningún cambio de stock no autorizado.",
        "Scenario: Reporte repetido — Given el resultado es desconocido, When el operador repite el mismo reporte, Then Nexa conserva un único hecho de discrepancia.",
        "Scenario: Nota sin conexión — Given el operador no tiene conexión, When prepara un reporte, Then queda marcado como no confirmado y no puede cambiar el stock vendible.",
    ],
    "MOB-US-018": [
        "Scenario: Movimiento autorizado — Given existen origen, destino, lote y cantidad autorizados, When el operador inicia una transferencia, Then Nexa conserva esos datos para revisión.",
        "Scenario: Dato de transferencia faltante — Given falta origen, destino, lote o motivo requerido, When el operador inicia la transferencia, Then Nexa deja el stock sin cambios.",
        "Scenario: Destino incompatible — Given el destino no puede aceptar la transferencia, When el operador la registra, Then Nexa mantiene la transferencia sin resolver y no afirma receipt.",
        "Scenario: Reintento — Given el resultado de la transferencia es desconocido, When el operador repite el movimiento, Then permanece una única transferencia trazable.",
    ],
    "MOB-US-019": [
        "Scenario: Lectura válida — Given el operador tiene permiso y se conoce un lote o almacén, When registra una lectura válida, Then Nexa conserva valor, unidad, momento, persona y sujeto.",
        "Scenario: Lectura preocupante — Given una lectura está fuera del rango aceptado, When se registra, Then Nexa conserva la evidencia y no toma una decisión silenciosa de liberación.",
        "Scenario: Lectura incompleta — Given falta el sujeto o la unidad, When se registra la lectura, Then Nexa la rechaza sin crear evidencia incompleta.",
        "Scenario: Fallo temporal — Given no se puede confirmar la lectura, When el operador prepara la evidencia, Then permanece pendiente y no se afirma una disposición final del stock.",
    ],
    "MOB-US-020": [
        "Scenario: Entrega lista — Given una entrega cumple sus condiciones de preparación, When el coordinador la comprueba, Then se identifica como lista para trabajo de dispatch.",
        "Scenario: No lista — Given la asignación, picking o evidencia están incompletos, When el coordinador comprueba la entrega, Then no se presenta como lista.",
        "Scenario: Preparación desactualizada — Given la información de disponibilidad está desactualizada, When el coordinador inicia la preparación, Then Nexa exige una comprobación actual.",
        "Scenario: Alcance incorrecto — Given la entrega pertenece a otra empresa o almacén, When se comprueba, Then no se expone.",
    ],
    "MOB-US-021": [
        "Scenario: Driver elegible — Given una entrega está lista y un driver es elegible, When el coordinador lo asigna, Then Nexa registra una única asignación.",
        "Scenario: Asignación no elegible — Given la entrega o el driver no son elegibles, When el coordinador realiza la asignación, Then Nexa la rechaza y no cambia la responsabilidad de la entrega.",
        "Scenario: Asignación desactualizada — Given la entrega cambió después de ser leída, When el coordinador asigna el driver, Then Nexa solicita información actual en lugar de sobrescribir el cambio.",
        "Scenario: Asignación repetida — Given el coordinador repite la misma asignación, When Nexa la recibe, Then la entrega conserva un único resultado de asignación.",
    ],
    "MOB-US-022": [
        "Scenario: Bienes coincidentes — Given los bienes salientes coinciden con la asignación actual, When el coordinador los comprueba, Then Nexa registra que la preparación del handoff coincide.",
        "Scenario: Diferencia — Given el lote o cantidad difiere de la asignación, When el coordinador lo comprueba, Then Nexa detiene el handoff y conserva la discrepancia.",
        "Scenario: Asignación modificada — Given la asignación cambió después de la preparación, When el coordinador comprueba los bienes, Then Nexa exige una decisión de preparación nueva.",
        "Scenario: Comprobación repetida — Given se comprueban nuevamente los mismos bienes, When el coordinador repite la comprobación, Then la comprobación no crea un segundo movimiento de stock.",
    ],
    "MOB-US-023": [
        "Scenario: Evidencia completa — Given se conocen la entrega, los bienes y las personas responsables, When se registra el handoff, Then Nexa conserva la evidencia con momento e identidad de entrega.",
        "Scenario: Evidencia faltante — Given falta evidencia requerida, When el coordinador registra el handoff, Then Nexa lo deja no confirmado.",
        "Scenario: Fallo de evidencia — Given no se puede confirmar la evidencia, When el coordinador reintenta, Then Nexa muestra el estado no resuelto y no afirma un handoff completado.",
        "Scenario: Handoff repetido — Given se vuelve a enviar el mismo handoff, When Nexa lo recibe, Then permanece un único hecho de handoff y no se borra evidencia anterior.",
    ],
    "MOB-US-024": [
        "Scenario: Handoff conocido — Given existe una entrega preparada y un driver asignado, When el coordinador identifica el handoff, Then Nexa lo vincula con esa entrega y asignación.",
        "Scenario: Handoff incorrecto — Given un identificador pertenece a otra entrega, When se utiliza, Then Nexa lo rechaza y no cambia ningún hecho de entrega.",
        "Scenario: Identidad expirada — Given la identidad del handoff ya no es válida, When se utiliza, Then Nexa exige un nuevo handoff autorizado.",
        "Scenario: Significados separados — Given el handoff está identificado, When se resuelve su identidad, Then Nexa no lo trata como Driver outcome ni como Buyer receipt.",
    ],
    "MOB-US-025": [
        "Scenario: Handoff completo — Given asignación, comprobaciones salientes, asignación del driver y evidencia de handoff están completas, When el coordinador confirma el dispatch, Then Nexa registra la entrega como dispatched.",
        "Scenario: Handoff incompleto — Given cualquier comprobación requerida está incompleta, When el coordinador confirma el dispatch, Then Nexa deja la entrega como undispatched.",
        "Scenario: Entrega modificada — Given la entrega cambió después de la preparación, When el coordinador confirma el dispatch, Then Nexa exige comprobaciones actuales en lugar de sobrescribir el cambio.",
        "Scenario: Resultado incierto — Given la confirmación pudo tener éxito, When el coordinador reintenta, Then Nexa resuelve un único resultado de dispatch sin duplicar la transición.",
    ],
    "MOB-US-026": [
        "Scenario: Asignaciones actuales — Given el driver está autorizado, When se comprueban sus entregas asignadas, Then solo se muestran sus entregas actuales.",
        "Scenario: Asignación retirada — Given se retira una asignación, When el driver vuelve a comprobar, Then la entrega deja de tratarse como asignada.",
        "Scenario: Lista desactualizada — Given la lista de asignaciones está desactualizada, When el driver inicia el trabajo, Then Nexa exige confirmación actual.",
        "Scenario: Entrega de otro driver — Given una entrega pertenece a otro driver, When se solicita, Then no se expone información protegida de la entrega.",
    ],
    "MOB-US-027": [
        "Scenario: Inicio asignado — Given la entrega está asignada y lista, When el driver la inicia, Then Nexa registra un único Delivery Attempt activo.",
        "Scenario: Inicio no asignado — Given la entrega no está asignada al driver, When intenta iniciarla, Then Nexa la rechaza y no registra ningún Attempt.",
        "Scenario: Ya iniciada — Given ya existe un Attempt, When el driver la inicia nuevamente, Then Nexa devuelve el Attempt actual sin crear otro.",
        "Scenario: Sin conexión — Given no se puede confirmar el inicio, When el driver intenta comenzar, Then Nexa muestra un estado no confirmado y no afirma un Attempt activo.",
    ],
    "MOB-US-028": [
        "Scenario: Destino autorizado — Given una entrega activa y autorizada tiene destino, When el driver solicita indicaciones, Then Nexa entrega ese destino al servicio de navegación elegido.",
        "Scenario: Destino faltante — Given falta el destino o no está autorizado, When se solicitan indicaciones, Then Nexa no revela una ubicación no verificada.",
        "Scenario: Navegación no disponible — Given el servicio de navegación no está disponible, When se solicitan indicaciones, Then el Delivery Attempt no cambia y el fallo queda claro.",
        "Scenario: Sin tracking almacenado — Given se abren las indicaciones, When termina el handoff, Then Nexa no almacena ubicación continua ni background del driver por esta acción.",
    ],
    "MOB-US-029": [
        "Scenario: Consentimiento futuro — Given se acepta una policy futura de ubicación, When el driver comparte una ubicación, Then consentimiento, alcance y retención quedan explícitos.",
        "Scenario: Sin delivery activo — Given no existe una entrega activa, When se solicita la ubicación, Then no se comparte ninguna ubicación.",
        "Scenario: Límite de privacidad — Given la persona retira el permiso, When se solicita compartir ubicación, Then no se divulga ninguna ubicación nueva.",
    ],
    "MOB-US-030": [
        "Scenario: Canal futuro — Given existe una política de contacto aceptada, When el driver contacta al buyer, Then solo se usa el canal autorizado y su uso queda registrado.",
        "Scenario: Consentimiento faltante — Given falta consentimiento o asignación, When se solicita el contacto, Then no se inicia contacto personal.",
        "Scenario: Resultado separado — Given ocurre el contacto, When termina, Then por sí mismo no cambia el resultado de Delivery ni el Buyer receipt.",
        "Scenario: Postergación — Given ningún canal de contacto está aceptado para V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-031": [
        "Scenario: Resultado permitido — Given existe un Attempt activo y asignado, When el driver registra un resultado permitido, Then Nexa conserva resultado, persona y momento.",
        "Scenario: Resultado inválido — Given el Attempt no está activo o el driver no está autorizado, When se registra un resultado, Then Nexa no cambia el estado de Delivery.",
        "Scenario: Evidencia requerida — Given el resultado necesita evidencia que falta, When el driver lo registra, Then Nexa deja el resultado no confirmado.",
        "Scenario: Resultado repetido — Given el resultado es desconocido, When el driver repite el mismo resultado, Then Nexa devuelve un único resultado y no sobrescribe el historial.",
    ],
    "MOB-US-032": [
        "Scenario: Entrega parcial — Given el driver proporciona cantidades entregadas y restantes válidas, When registra el resultado parcial, Then Nexa conserva por separado las cantidades entregadas, rechazadas y restantes.",
        "Scenario: Entrega rechazada — Given los bienes son rechazados con un motivo, When se registra el rechazo, Then Nexa conserva el motivo y no declara completa la entrega.",
        "Scenario: Continuación — Given queda cantidad para una entrega futura, When se confirma el resultado, Then Nexa crea únicamente la continuación autorizada.",
        "Scenario: Resultado incierto — Given el resultado es desconocido, When el driver reintenta, Then Nexa devuelve un único resultado y no sobrescribe hechos previos.",
    ],
    "MOB-US-033": [
        "Scenario: Proof requerido — Given el Attempt y los requisitos de evidencia son válidos, When el driver proporciona el proof requerido, Then Nexa conserva su identidad, persona y momento.",
        "Scenario: Proof faltante — Given falta el proof requerido o es inválido, When el driver finaliza el Attempt, Then Nexa no afirma un proof completado.",
        "Scenario: Fallo temporal — Given no se puede confirmar el proof, When el driver reintenta, Then Nexa mantiene visible el estado no resuelto y no completa falsamente el Delivery.",
        "Scenario: Proof repetido — Given se proporciona nuevamente el mismo proof, When Nexa lo recibe, Then permanece un único hecho de proof y no se borra evidencia anterior.",
    ],
    "MOB-US-034": [
        "Scenario: Código válido — Given existe un Delivery activo y autorizado, When el driver presenta su código, Then Nexa vincula el código con ese Delivery y Attempt.",
        "Scenario: Código expirado o incorrecto — Given el código está expirado, reutilizado o pertenece a otro Delivery, When se comprueba, Then Nexa lo rechaza sin cambiar el estado de Delivery.",
        "Scenario: Código no disponible — Given no se puede presentar el código, When el driver usa el fallback aprobado, Then el handoff permanece explícito y no se registra aceptación falsa.",
        "Scenario: Hechos separados — Given el buyer verifica el código, When la verificación tiene éxito, Then por sí sola no crea receipt, POD, payment ni finalización de Delivery.",
    ],
    "MOB-US-035": [
        "Scenario: Recuperación futura de evidencia — Given se acepta una política futura de recuperación, When se captura evidencia sin conexión, Then su estado pendiente y contenido protegido mínimo quedan claros.",
        "Scenario: Confirmación posterior — Given la evidencia preparada se revisa posteriormente, When Nexa la acepta, Then solo el hecho exacto aceptado se vuelve autoritativo.",
        "Scenario: Rechazo — Given se rechaza la evidencia preparada, When se revisa, Then el motivo permanece claro y no se implica éxito de Delivery.",
        "Scenario: Postergación — Given V1 no tiene autoridad genérica para mutations offline, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-036": [
        "Scenario: Catálogo autorizado — Given existe una relación activa de buyer, When se exploran productos, Then solo se muestran productos permitidos.",
        "Scenario: Relación suspendida — Given la relación del buyer está suspendida, When se exploran productos, Then no se expone información privada del producto.",
        "Scenario: Información desactualizada — Given la información del producto está desactualizada, When se explora, Then queda marcada como advisory y no crea autoridad para ordenar.",
        "Scenario: Postergación — Given Buyer commerce está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-037": [
        "Scenario: Producto actual — Given existe una relación autorizada, When se revisa un producto, Then se muestran precio, términos y disponibilidad vendible con frescura.",
        "Scenario: Producto desactualizado — Given los hechos del producto están desactualizados, When el buyer continúa, Then se requiere confirmación actual.",
        "Scenario: Producto no disponible — Given el producto está oculto o no disponible, When se solicita, Then no puede tratarse como compromiso.",
        "Scenario: Postergación — Given Buyer commerce está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-038": [
        "Scenario: Draft — Given hay productos permitidos disponibles, When el buyer prepara una request, Then permanece como draft y no crea reservation.",
        "Scenario: Producto modificado — Given cambia el precio o disponibilidad, When el buyer revisa el draft, Then el cambio es claro antes de la submission.",
        "Scenario: Preparación local — Given el buyer pierde conexión, When edita el draft, Then permanece no confirmado.",
        "Scenario: Postergación — Given Buyer commerce está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-039": [
        "Scenario: Historial reutilizado — Given el buyer puede acceder al historial anterior, When lo reutiliza, Then Nexa crea un nuevo draft y vuelve a comprobar los datos actuales del producto.",
        "Scenario: Producto modificado — Given un producto anterior ya no está disponible, When se reutiliza el historial, Then Nexa lo marca y no crea una order silenciosa.",
        "Scenario: Acción repetida — Given el buyer repite la acción, When Nexa la procesa, Then no crea un segundo compromiso.",
        "Scenario: Postergación — Given la conveniencia de reorder está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-040": [
        "Scenario: Purchase Request — Given existe un draft válido y una policy válida, When el buyer envía una request, Then se registra una única Purchase Request.",
        "Scenario: Direct order — Given está permitido ordenar directamente, When el buyer elige esa vía, Then se registra una única ruta de Sales Order sin inventar una Purchase Request.",
        "Scenario: Hechos modificados — Given cambiaron precio, disponibilidad, crédito o permiso, When el buyer envía, Then no se registra ningún compromiso parcial.",
        "Scenario: Postergación — Given Buyer commitment está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-041": [
        "Scenario: Aceptar cambio — Given existe un cambio actual y autorizado, When el buyer lo acepta, Then Nexa registra el cambio versionado.",
        "Scenario: Rechazar cambio — Given el buyer lo rechaza, When Nexa registra la decisión, Then el compromiso original permanece intacto.",
        "Scenario: Cambio desactualizado — Given el cambio ya no es actual, When el buyer responde, Then Nexa solicita la decisión actual y no cambia nada silenciosamente.",
        "Scenario: Postergación — Given responder a cambios materiales está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-042": [
        "Scenario: Historial autorizado — Given existe una relación autorizada, When se revisa el progreso, Then el estado e historial de request y order permanecen diferenciados.",
        "Scenario: Progreso actual — Given existe una relación autorizada, When el buyer revisa el progreso, Then el estado de Purchase Request y Sales Order permanece diferenciado.",
        "Scenario: Acceso revocado — Given se revoca el acceso, When se solicita el progreso, Then no se expone información privada.",
        "Scenario: Progreso desactualizado — Given el progreso mostrado está desactualizado, When el buyer hace refresh, Then Nexa expone el resultado actual o un estado no disponible veraz.",
    ],
    "MOB-US-043": [
        "Scenario: Crédito actual — Given existe una relación autorizada, When se revisa el crédito, Then importe, moneda, frescura y fuente quedan claros.",
        "Scenario: Estado de payment — Given existe evidencia de payment, When el buyer la revisa, Then los estados reported, confirmed y rejected permanecen diferenciados.",
        "Scenario: Estado desactualizado — Given el estado de payment está desactualizado, When el buyer hace refresh, Then Nexa expone el estado actual o un estado no disponible veraz.",
        "Scenario: Postergación — Given Buyer finance está fuera de V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-044": [
        "Scenario: Actualización relevante — Given un hecho permitido de Delivery requiere atención del buyer, When Nexa envía una actualización, Then el buyer puede identificar el Delivery relevante.",
        "Scenario: Actualización no relacionada — Given el Delivery está fuera de la relación del buyer, When se prepara una actualización, Then no se revela información privada del Delivery.",
        "Scenario: Fallo de entrega — Given una actualización no puede entregarse, When el buyer abre Nexa, Then los hechos actuales de Delivery siguen disponibles para refresh y ningún hecho cambia.",
        "Scenario: Reintento de actualización — Given una actualización se repite, When el buyer la recibe, Then no crea un segundo Delivery, receipt ni hecho de discrepancia.",
    ],
    "MOB-US-045": [
        "Scenario: Ubicación futura — Given se acepta una policy futura de ubicación, When el buyer abre un Delivery activo, Then solo se muestra ubicación acotada con consentimiento.",
        "Scenario: Sin Delivery activo — Given no existe un Delivery activo, When el buyer solicita un mapa, Then no se divulga la ubicación del driver.",
        "Scenario: Límite de privacidad — Given falta permiso o relación, When el buyer solicita un mapa, Then no se divulga ninguna ubicación.",
    ],
    "MOB-US-046": [
        "Scenario: Canal futuro — Given existe una policy de canal aceptada y un Delivery activo, When el buyer contacta al driver, Then solo se usa el canal autorizado.",
        "Scenario: Sin permiso — Given falta consentimiento o Delivery activo, When se solicita el contacto, Then no se inicia contacto personal.",
        "Scenario: Hechos separados — Given ocurre el contacto, When termina, Then no cambia Driver outcome, Buyer receipt ni el estado de Delivery.",
        "Scenario: Postergación — Given ningún canal de contacto está aceptado para V1, When se considera esta historia, Then permanece deferred.",
    ],
    "MOB-US-047": [
        "Scenario: Código coincidente — Given existe un código válido, no expirado y una relación autorizada, When el buyer lo verifica, Then Nexa identifica el Delivery y Attempt coincidentes.",
        "Scenario: Código inválido — Given el código está expirado, reutilizado, malformado o no relacionado, When el buyer lo verifica, Then Nexa lo rechaza y no cambia ningún hecho de receipt.",
        "Scenario: Sin conexión — Given no se puede confirmar el código, When el buyer lo verifica, Then Nexa muestra un estado no confirmado y ningún receipt tiene éxito.",
        "Scenario: Límite de verificación — Given el código está verificado, When el buyer continúa, Then la verificación por sí sola no confirma cantidades, POD, payment ni finalización de Delivery.",
    ],
    "MOB-US-048": [
        "Scenario: Receipt coincidente — Given existe un handoff verificado y autorizado, When el buyer confirma las cantidades recibidas, Then Nexa registra un único hecho de Buyer receipt con persona, momento y Delivery.",
        "Scenario: Cantidades diferentes — Given las cantidades recibidas difieren del resultado del driver, When el buyer las confirma, Then ambos hechos permanecen separados y la diferencia queda visible.",
        "Scenario: Handoff desactualizado o reutilizado — Given el handoff está desactualizado, expirado o ya utilizado, When el buyer confirma cantidades, Then Nexa rechaza la confirmación o devuelve el resultado original sin un segundo receipt.",
        "Scenario: Sin conexión — Given no se puede comprobar la confirmación del receipt, When el buyer lo intenta, Then Nexa no muestra éxito de receipt hasta recibir confirmación.",
    ],
    "MOB-US-049": [
        "Scenario: Discrepancia registrada — Given existe un contexto de handoff o receipt verificado, When el buyer reporta una discrepancia, Then Nexa conserva motivo, cantidad afectada, persona, momento y evidencia.",
        "Scenario: Historiales separados — Given el resultado del Driver outcome difiere del Buyer receipt, When se registra la discrepancia, Then ambos hechos originales permanecen sin cambios y la diferencia queda visible.",
        "Scenario: Reporte inválido — Given falta motivo, permiso o evidencia requerida, When el buyer lo reporta, Then Nexa no registra una corrección no autorizada.",
        "Scenario: Fallo temporal — Given no se puede confirmar el reporte, When el buyer reintenta, Then Nexa conserva un único resultado pendiente o aceptado y no implica refund, cambio de payment ni finalización de Delivery.",
    ],
    "MOB-US-050": [
        "Scenario: Diferencia capturada — Given se inspecciona una entrega inbound, When el operador registra daño, fuga, producto incorrecto o cantidad incorrecta, Then Nexa conserva motivo, artículos afectados y evidencia para revisión.",
        "Scenario: Receiving controlado — Given se registra una discrepancia, When el operador envía el resultado de receiving, Then Nexa no incrementa el stock vendible más allá de los hechos confirmados.",
        "Scenario: Evidencia faltante — Given falta un hecho o evidencia requerida, When el operador intenta enviar la discrepancia, Then Nexa explica qué falta y no registra una decisión incompleta.",
    ],
    "MOB-US-051": [
        "Scenario: Proteger stock — Given un lote tiene una condición que impide su uso normal, When el operador registra el motivo de hold o quarantine, Then Nexa retira la cantidad afectada del trabajo disponible aplicable.",
        "Scenario: Resolución autorizada — Given un lote retenido fue revisado, When una persona autorizada lo libera o dispone de él, Then Nexa registra decisión, motivo y cantidad afectada sin borrar el historial de hold.",
        "Scenario: Decisión desactualizada — Given el lote cambió después de ser visualizado, When el operador intenta resolverlo, Then Nexa rechaza la decisión desactualizada y muestra el estado actual.",
    ],
    "MOB-US-052": [
        "Scenario: Receipt completo — Given una transferencia autorizada está en tránsito, When el operador destino confirma lote y cantidad esperados, Then Nexa registra destination receipt y cierra el movimiento de transferencia.",
        "Scenario: Receipt parcial o diferente — Given el destino recibe otro lote o cantidad, When el operador lo registra, Then Nexa mantiene separados los hechos de origen y destino y expone la diferencia para resolución.",
        "Scenario: Receipt repetido — Given destination receipt ya tiene un resultado aceptado, When el operador reintenta, Then Nexa devuelve el resultado original sin un segundo receipt.",
    ],
    "MOB-US-053": [
        "Scenario: Conteo registrado — Given existe una ubicación permitida y una vista actual del stock, When el operador registra lote y cantidad observados, Then Nexa conserva el conteo con persona, momento y ubicación.",
        "Scenario: Corrección revisada — Given el conteo difiere del stock registrado, When se aprueba una corrección autorizada, Then Nexa registra evidencia correctiva y la cantidad resultante sin borrar movimientos anteriores.",
        "Scenario: Cambio concurrente — Given el stock cambió después de iniciar el conteo, When el operador envía la corrección, Then Nexa rechaza o reabre el conteo desactualizado en lugar de aplicar una corrección last-write-wins.",
    ],
    "MOB-US-054": [
        "Scenario: Sustitución solicitada — Given el lote esperado no puede suministrar la cantidad preparada, When el operador propone una alternativa elegible, Then Nexa la envía a decisión autorizada con ambos lotes visibles.",
        "Scenario: Decisión controlada — Given una sustitución es rechazada o queda desactualizada, When el operador continúa, Then Nexa conserva la asignación original y explica la siguiente acción permitida.",
    ],
    "MOB-US-055": [
        "Scenario: Identidad resuelta — Given existe un identificador permitido de paquete o almacenamiento, When el operador lo presenta, Then Nexa muestra el producto correspondiente y el contexto actual antes de iniciar el trabajo.",
        "Scenario: Identidad no disponible — Given el identificador es desconocido o ilegible, When el operador intenta continuar, Then Nexa ofrece un fallback explícito o indica que se requiere confirmación.",
    ],
    "MOB-US-056": [
        "Scenario: Grupo preparado — Given hay varias tareas permitidas disponibles, When el operador las agrupa, Then Nexa muestra claramente elementos, secuencia y comprobaciones requeridas.",
        "Scenario: Un elemento difiere — Given una tarea no puede completarse como fue preparada, When el operador registra la diferencia, Then Nexa mantiene separados los resultados de las otras tareas e identifica el elemento que requiere revisión.",
    ],
    "MOB-US-057": [
        "Scenario: Diferencia identificada — Given los bienes salientes no coinciden con la entrega preparada, When el coordinador registra la diferencia, Then Nexa identifica la entrega, lote o cantidad afectados y bloquea el handoff inseguro.",
        "Scenario: Resolución autorizada — Given la diferencia tiene una resolución aceptada, When el coordinador confirma la siguiente acción, Then Nexa actualiza la disponibilidad de dispatch con evidencia trazable.",
        "Scenario: Preparación desactualizada — Given la entrega cambió después de la preparación, When el coordinador resuelve la discrepancia, Then Nexa solicita una decisión nueva en lugar de sobrescribir los hechos actuales.",
    ],
    "MOB-US-058": [
        "Scenario: Reasignación elegible — Given una entrega preparada necesita otro driver, When el coordinador selecciona una persona elegible, Then Nexa registra la nueva responsabilidad y conserva el historial de asignación anterior.",
        "Scenario: Cambio de horario — Given el dispatch no puede continuar en el horario previsto, When el coordinador propone un nuevo horario, Then Nexa muestra el impacto y confirma el cambio una sola vez.",
        "Scenario: Cambio concurrente — Given otra persona cambió primero la entrega, When el coordinador envía el plan antiguo, Then Nexa lo rechaza y muestra la responsabilidad y horario actuales.",
    ],
    "MOB-US-059": [
        "Scenario: Carga compatible — Given las entregas cumplen las reglas de agrupación aceptadas, When el coordinador prepara una carga, Then Nexa muestra cada entrega, stop y condición requerida.",
        "Scenario: Entrega incompatible — Given una entrega incumple una regla de customer o cold-chain, When el coordinador prepara la carga, Then Nexa la mantiene fuera de la carga y explica por qué.",
    ],
    "MOB-US-060": [
        "Scenario: Handoff aceptado — Given existe una carga preparada y un carrier autorizado, When el coordinador registra el handoff, Then Nexa conserva carrier, persona, momento y responsabilidad de delivery.",
        "Scenario: Evidencia incompleta — Given falta evidencia requerida del handoff, When el coordinador intenta finalizarlo, Then Nexa deja la responsabilidad en el owner actual e indica qué se requiere.",
    ],
    "MOB-US-061": [
        "Scenario: Evidencia registrada — Given una entrega requiere una comprobación de temperatura, When el coordinador registra la observación, Then Nexa conserva valor, unidad, persona, momento y contexto de entrega.",
        "Scenario: Fuera de policy — Given la observación está fuera del rango aceptado, When el coordinador la envía, Then Nexa impide un dispatch no revisado y muestra la decisión requerida.",
        "Scenario: Confirmación faltante — Given no se puede confirmar la observación, When el coordinador reintenta, Then Nexa no implica aprobación de cold-chain.",
    ],
    "MOB-US-062": [
        "Scenario: Llegada registrada — Given el driver tiene un Delivery activo y autorizado, When señala su llegada, Then Nexa registra el evento y lo hace visible a recipients permitidos.",
        "Scenario: Sin delivery activo — Given el driver no está asignado a un Delivery activo, When señala llegada, Then Nexa rechaza la señal sin revelar otra entrega.",
        "Scenario: Delivery permanece abierto — Given se registró la llegada, When el buyer o driver consulta el Delivery, Then permanece abierto hasta registrar por separado handoff y receipt.",
    ],
    "MOB-US-063": [
        "Scenario: Contexto autorizado — Given una entrega activa incluye instrucciones permitidas, When el driver las abre, Then Nexa muestra solo la información necesaria para esa entrega.",
        "Scenario: Instrucciones modificadas — Given las instrucciones ya no son actuales, When el driver las consulta, Then Nexa las marca como desactualizadas y exige confirmación nueva antes de usarlas.",
        "Scenario: Información restringida — Given un contacto o instrucción no está permitido para el driver, When solicita acceso, Then Nexa lo oculta y explica la ruta permitida.",
    ],
    "MOB-US-064": [
        "Scenario: Request enviada — Given el buyer está autorizado para una entrega activa, When propone un horario alternativo, Then Nexa registra una request y muestra que espera una decisión de delivery.",
        "Scenario: Decisión devuelta — Given el equipo de delivery acepta o rechaza la request, When el buyer consulta la entrega, Then Nexa muestra la decisión y el horario efectivo sin reescribir hechos anteriores.",
        "Scenario: Request desactualizada — Given la entrega ya es terminal o cambió, When el buyer envía la request antigua, Then Nexa la rechaza con el estado actual de la entrega.",
    ],
    "MOB-US-065": [
        "Scenario: Incidente descrito — Given una entrega activa encuentra un incidente permitido, When el driver registra motivo, lugar dentro de la entrega y evidencia, Then Nexa conserva el incidente para revisión autorizada.",
        "Scenario: El incidente no reescribe el resultado — Given ya existe un resultado de entrega, When se añade un incidente, Then Nexa conserva el resultado original y vincula la evidencia nueva.",
        "Scenario: Incidente incompleto — Given faltan detalles requeridos, When el driver intenta enviarlo, Then Nexa identifica la información faltante y no afirma un seguimiento completado.",
    ],
    "MOB-US-066": [
        "Scenario: Evidencia retenida — Given se captura un elemento de evidencia permitido sin conexión, When el driver vuelve a tener cobertura, Then Nexa muestra su estado pendiente y permite revisarlo antes del envío.",
        "Scenario: Recuperación autoritativa — Given el delivery cambió mientras el dispositivo estaba offline, When se revisa la evidencia, Then Nexa resuelve explícitamente el conflicto y nunca aplica silenciosamente un resultado desactualizado.",
    ],
    "MOB-US-067": [
        "Scenario: Instrucciones proporcionadas — Given el buyer está autorizado para la entrega, When guarda instrucciones, Then Nexa las asocia con esa entrega y muestra su periodo efectivo.",
        "Scenario: Consentimiento del contacto alternativo — Given una persona alternativa debe recibir la entrega, When el buyer proporciona contacto permitido y consentimiento, Then Nexa lo registra únicamente para el propósito de entrega definido.",
        "Scenario: Cambio después del dispatch — Given la entrega está en un estado que no permite cambios, When el buyer edita instrucciones, Then Nexa rechaza el cambio o lo dirige a una decisión explícita.",
    ],
    "MOB-US-068": [
        "Scenario: Timeline visible — Given el buyer puede acceder a una entrega, When abre su línea de tiempo, Then Nexa muestra los hechos autorizados ordenados y su estado actual.",
        "Scenario: Acknowledgement separado — Given la entrega tiene un resultado registrado, When el buyer lo reconoce, Then Nexa registra el acknowledgement separado de receipt, proof o completion.",
        "Scenario: Historial sin cambios — Given el buyer reconoce una entrega, When otra persona permitida la consulta, Then los hechos subyacentes permanecen sin cambios.",
    ],
    "MOB-US-069": [
        "Scenario: Evidencia adjunta — Given el buyer tiene una discrepancia permitida, When añade evidencia, Then Nexa la vincula con esa discrepancia junto con persona y momento.",
        "Scenario: Evidencia no soportada o insegura — Given la evidencia no está disponible, es demasiado grande o no está permitida, When el buyer intenta añadirla, Then Nexa explica el problema y mantiene la discrepancia sin cambios.",
        "Scenario: Hechos originales preservados — Given la evidencia es aceptada, When se revisa la entrega, Then receipt, Driver outcome y discrepancia permanecen separados.",
    ],
    "MOB-US-070": [
        "Scenario: Documento autorizado — Given un documento emitido pertenece a la relación permitida, When la persona lo solicita, Then Nexa proporciona su identidad y contenido autorizado.",
        "Scenario: Documento faltante — Given no existe un documento emitido, When la persona lo solicita, Then Nexa indica que no está disponible y no cambia ningún compromiso.",
        "Scenario: Acceso revocado — Given se revoca el permiso, When la persona solicita el documento, Then Nexa no expone contenido privado.",
    ],
    "MOB-US-071": [
        "Scenario: Evidencia reportada — Given están disponibles una referencia, importe y evidencia permitidos, When el buyer los reporta, Then Nexa registra el reporte como no confirmado.",
        "Scenario: Evidencia revisada — Given el proceso owner revisa el reporte, When el buyer consulta el estado, Then Nexa muestra el resultado de revisión sin reescribir el reporte.",
        "Scenario: Reporte duplicado — Given se vuelve a enviar el mismo reporte, When Nexa lo recibe, Then no aplica la evidencia dos veces.",
    ],
    "MOB-US-072": [
        "Scenario: Visita autorizada — Given el representative tiene permiso para la relación del customer, When inicia una visita, Then Nexa muestra el contexto permitido del customer y su propósito.",
        "Scenario: Seguimiento capturado — Given la visita produce un seguimiento permitido, When el representative lo registra, Then Nexa vincula el resultado con la relación del customer sin crear un compromiso no aprobado.",
    ],
    "MOB-US-073": [
        "Scenario: Resultado valioso antes de seleccionar tecnología — Given Product explora observaciones avanzadas de almacén, When define el resultado de almacén antes de seleccionar un device o provider, Then identifica primero un resultado valioso de almacén.",
        "Scenario: Observación automatizada subordinada — Given existe una observación automatizada considerada para el trabajo, When se revisa para apoyar una decisión de almacén, Then permanece atribuible y revisable y está subordinada a la autorización del owner del Bounded Context.",
        "Scenario: Release sin implementación específica — Given el release contempla esta hipótesis de automatización futura, When se describe su alcance, Then no promete una implementación específica de RFID, scanner, sensor, label ni telemetry.",
    ],
}


def epic_label(epic_id: str) -> str:
    return f"{epic_id} — {EPICS[epic_id][0]}"


def bc_label(bc_id: str) -> str:
    return f"{bc_id} — {BC_NAMES[bc_id]}"


def capability_label(capability_id: str) -> str:
    return f"{capability_id} — {CAP_NAMES[capability_id]}"


def academic_points(row: dict[str, str]) -> str:
    points = row["Story Points"]
    if points in {"1", "2", "3", "5", "8"}:
        return points
    try:
        return UNESTIMATED_POINTS[row["ID"]]
    except KeyError as error:
        raise SystemExit(f"missing academic estimate for {row['ID']}") from error


def planned_sprint(row: dict[str, str]) -> str:
    if row["Target Release"] == "V1":
        return row["Sprint Planned"]
    if row["ID"] in S2_IDS:
        return "S2"
    if row["ID"] in S3_IDS:
        return "S3"
    if row["ID"] in S4_IDS:
        return "S4"
    return "Future"


def relevant_bcs(row: dict[str, str]) -> str:
    secondary = [code.strip() for code in row["Secondary BCs"].split(",") if code.strip()]
    codes = list(dict.fromkeys([row["Primary BC"], *secondary]))
    return ", ".join(bc_label(code) for code in codes)


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").strip()


def render_scenario(line: str, number: int) -> str:
    match = re.fullmatch(r"Scenario: (.+?) — Given (.+?), When (.+?), Then (.+)", line)
    if not match:
        raise SystemExit(f"unrenderable translated scenario: {line}")
    label, given, when, then = (markdown_cell(value) for value in match.groups())
    return "\n".join(
        [
            f"{number}. **Scenario: {label}**",
            f"   - **Given** {given}",
            f"   - **When** {when}",
            f"   - **Then** {then}",
        ]
    )


def story_table(row: dict[str, str]) -> str:
    story_id = row["ID"]
    epic_id = row["Epic"]
    title = TITLE_ES[story_id]
    translated = markdown_cell(translate_text(DESCRIPTIONS[story_id]))
    criteria = "\n".join(
        render_scenario(line, number)
        for number, line in enumerate(academic_scenarios(story_id), start=1)
    )
    app = markdown_cell(app_label(row["Mobile App"]))
    release = markdown_cell(row["Target Release"])
    sprint = markdown_cell(planned_sprint(row))
    return "\n".join(
        [
            f"##### {story_id} — {title}",
            "",
            "| Story ID | User | Priority | Epic |",
            "| :--- | :--- | :--- | :--- |",
            f"| {story_id} | {actor_label(row['Actor'])} | {priority_label(row['Priority'])} | {markdown_cell(epic_label(epic_id))} |",
            "",
            "| Product app | Story points | Target release | Planned Sprint |",
            "| :--- | ---: | :--- | :--- |",
            f"| {app} | {academic_points(row)} | {release} | {sprint} |",
            "",
            "| Owning Bounded Context | Relevant Bounded Contexts | Business capability |",
            "| :--- | :--- | :--- |",
            f"| {markdown_cell(bc_label(row['Primary BC']))} | {markdown_cell(relevant_bcs(row))} | {markdown_cell(capability_label(row['Capability']))} |",
            "",
            f"**Title:** {title}",
            "",
            f"**Description:** {translated}",
            "",
            "**Acceptance Criteria**",
            "",
            criteria,
            "",
        ]
    )


def functional_index(rows: list[dict[str, str]]) -> str:
    output = [
        "#### Índice de historias funcionales",
        "",
        "El catálogo funcional contiene las 73 historias `MOB-US-001` a `MOB-US-073`. "
        "Las 28 historias V1 se organizan en S1, S2 y S3 según la proyección de "
        "producto; las demás historias se distribuyen en S2, S3, S4 o Future para "
        "ordenar la investigación y el desarrollo posterior.",
        "",
        "| # | Story ID | User | Priority | Epic | Release | Planned Sprint |",
        "| ---: | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for index, row in enumerate(rows, start=1):
        output.append(
            f"| {index} | {row['ID']} | {actor_label(row['Actor'])} | "
            f"{priority_label(row['Priority'])} | {epic_label(row['Epic'])} | "
            f"{row['Target Release']} | {planned_sprint(row)} |"
        )
    output.extend(
        [
            "",
            "Reglas transversales: la conectividad es online-first; el almacenamiento local "
            "sólo conserva caché segura, borradores, evidencia temporal y metadatos de "
            "reintento; la autoridad de negocio permanece en el servidor. La ubicación "
            "inicial sólo abre navegación externa hacia el destino autorizado.",
            "",
        ]
    )
    return "\n".join(output)


def supplemental_body(
    existing: str,
    heading: str,
    next_heading: str | None,
    base_heading_level: int,
) -> str:
    """Recover a consolidated subsection at stable Markdown levels."""
    boundary = rf"(?=^{re.escape(next_heading)}\n|\Z)" if next_heading else r"(?=\Z)"
    match = re.search(
        rf"^{re.escape(heading)}\n(.*?){boundary}",
        existing,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        raise SystemExit(f"missing consolidated section: {heading}")
    return normalize_headings(match.group(1).strip(), base_heading_level)


def normalize_headings(body: str, base_level: int) -> str:
    """Keep recovered supplemental sections at stable Markdown levels."""
    matches = list(re.finditer(r"^(#{2,10}) (.+)$", body, re.MULTILINE))
    if any(match.group(2).startswith("LAND-US-") for match in matches):
        return re.sub(
            r"^(#{2,10}) (.+)$",
            lambda match: f"{'#' * (base_level + (1 if match.group(2).startswith('LAND-US-') else 0))} {match.group(2)}",
            body,
            flags=re.MULTILINE,
        )
    if any(match.group(2).startswith(("TS-MOB-", "SPIKE-")) for match in matches):
        return re.sub(
            r"^(#{2,10}) (.+)$",
            lambda match: f"{'#' * base_level} {match.group(2)}",
            body,
            flags=re.MULTILINE,
        )
    levels = [len(match.group(1)) for match in matches]
    if not levels:
        return body
    source_base = min(levels)
    return re.sub(
        r"^(#{2,10}) ",
        lambda match: f"{'#' * (base_level + len(match.group(1)) - source_base)} ",
        body,
        flags=re.MULTILINE,
    )


def generate_user_stories(rows: list[dict[str, str]]) -> str:
    existing = USER_STORIES.read_text(encoding="utf-8") if USER_STORIES.is_file() else ""
    to_be = supplemental_body(existing, "## To-Be Scenario Mapping", "## 2.4.1 User Stories", 3)
    landing = supplemental_body(existing, "### Landing Page User Stories", "### Technical Stories", 4)
    technical = supplemental_body(existing, "### Technical Stories", "### Spike Stories", 4)
    spikes = supplemental_body(existing, "### Spike Stories", None, 4)
    output = [
        "# 2.4 Requirements Specification",
        "",
        "Esta sección especifica las necesidades de Nexa Operations Mobile y Nexa Buyer Mobile "
        "como capacidades de negocio observables. Las User Stories expresan resultados para "
        "personas y roles; la tecnología de implementación se documenta en Technical Stories "
        "y no duplica la autoridad del dominio.",
        "",
        "Las dos aplicaciones proyectadas son `Nexa Operations Mobile` y `Nexa Buyer Mobile`. "
        "La especificación permanece neutral respecto de Android Native/Kotlin, Flutter/Dart "
        "e iOS Native/SwiftUI.",
        "",
        "## To-Be Scenario Mapping",
        "",
        to_be,
        "",
        "## 2.4.1 User Stories",
        "",
        "### Epics",
        "",
        "| Epic ID | Nombre | Descripción | Historias |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for epic_id, (title, description, story_ids) in EPICS.items():
        output.append(f"| {epic_id} | {title} | {description} | {', '.join(story_ids)} |")
    output.extend(
        [
            "",
            "Un Epic organiza requisitos; no representa un Bounded Context, una aplicación "
            "separada ni una unidad de despliegue.",
            "",
            "### Decisiones de producto que orientan la lectura",
            "",
            "La autoridad de los hechos de negocio permanece en el servidor y en el "
            "Bounded Context responsable. La información local puede apoyar continuidad "
            "de presentación, borradores y evidencia temporal, pero no confirma inventario, "
            "crédito, pago, compromiso, entrega o recepción sin respuesta autoritativa.",
            "",
            "Un Representante de Ventas autorizado puede capturar un Direct Order asistido "
            "cuando la política del Tenant sea `DIRECT_ORDER`. Este flujo no suplanta al "
            "Comprador: el borrador de Ventas y el borrador del Comprador son distintos, "
            "y el servidor vuelve a validar la autorización. `MOB-US-040` conserva el "
            "significado del flujo del Comprador; la cobertura de la captura asistida de "
            "Ventas se mantiene como comportamiento de producto y se revisa frente al "
            "catálogo antes de implementación.",
            "",
            "### Mobile Functional User Stories",
            "",
            functional_index(rows),
            "#### Registros de historias funcionales",
            "",
            "Cada registro incluye Story ID, User, Priority, Epic, Title, Description y "
            "Acceptance Criteria. `Scenario`, `Given`, `When` y `Then` siguen la convención "
            "Gherkin; el contenido de cada criterio es una condición observable y no una "
            "descripción de interfaz.",
            "",
        ]
    )
    for row in rows:
        output.append(story_table(row))
    output.extend(
        [
            "### Landing Page User Stories",
            "",
            landing,
            "",
            "### Technical Stories",
            "",
            technical,
            "",
            "### Spike Stories",
            "",
            spikes,
            "",
        ]
    )
    return "\n".join(output)


def generate_product_backlog(rows: list[dict[str, str]]) -> str:
    row_by_id = {row["ID"]: row for row in rows}
    functional_rows = {
        story_id: ("Mobile Functional", story_id, TITLE_ES[story_id], academic_points(row), planned_sprint(row))
        for story_id, row in row_by_id.items()
    }
    supplemental_rows = {
        item[0]: ("Landing Functional", *item)
        for item in LANDING_BACKLOG
    }
    supplemental_rows.update({
        item[0]: ("Technical", *item)
        for item in TECHNICAL_BACKLOG
    })
    supplemental_rows.update({
        item[0]: ("Spike", *item)
        for item in SPIKE_BACKLOG
    })
    all_by_id = {**functional_rows, **supplemental_rows}
    if set(GLOBAL_BACKLOG_ORDER) != set(all_by_id) or len(GLOBAL_BACKLOG_ORDER) != len(all_by_id):
        raise SystemExit("global backlog order must contain each of the 97 backlog IDs exactly once")
    all_rows = [all_by_id[story_id] for story_id in GLOBAL_BACKLOG_ORDER]
    sprint_counts = {
        sprint: sum(1 for item in all_rows if item[4] == sprint)
        for sprint in ("S1", "S2", "S3", "S4", "Future")
    }
    output = [
        "# 2.4.3 Product Backlog",
        "",
        "Este Product Backlog presenta el inventario académico completo: 73 historias "
        "Mobile funcionales, seis historias de Landing, doce Technical Stories y seis Spike "
        "Stories. El orden es de valor de negocio; Sprint es una asignación planificada "
        "de Chapter II y no un Sprint Backlog ni una lista de tareas.",
        "",
        "## Distribución por release",
        "",
        "| Release objetivo | Historias | Lectura de producto |",
        "| :--- | ---: | :--- |",
        "| V1 | 28 | Proyección funcional inicial. |",
        "| V2 | 35 | Evolución funcional posterior. |",
        "| V3 | 9 | Evolución funcional sujeta a investigación adicional. |",
        "| V4_FUTURE | 1 | Hipótesis funcional futura. |",
        "",
        "## Inventario por tipo",
        "",
        "| Tipo | Filas | Alcance |",
        "| :--- | ---: | :--- |",
        "| Mobile Functional Stories | 73 | MOB-US-001..073. |",
        f"| Landing Functional Stories | {len(LANDING_BACKLOG)} | LAND-US; Landing pública de Nexa. |",
        f"| Technical Stories | {len(TECHNICAL_BACKLOG)} | TS-MOB; habilitación técnica móvil. |",
        f"| Spike Stories | {len(SPIKE_BACKLOG)} | SPIKE; investigación delimitada. |",
        f"| **Total de filas** | **{len(all_rows)}** | **Inventario completo de Chapter 2.4.** |",
        "",
        "## Índice completo",
        "",
        "| # Orden | User Story Id | Título | Story Points (1 / 2 / 3 / 5 / 8) | Sprint |",
        "| ---: | :--- | :--- | ---: | :--- |",
    ]
    for index, (_, story_id, title, points, sprint) in enumerate(all_rows, start=1):
        output.append(f"| {index} | {story_id} | {title} | {points} | {sprint} |")
    output.extend(
        [
            "",
            "## Sprints planificados",
            "",
            "| Sprint | Filas | Enfoque académico |",
            "| :--- | ---: | :--- |",
            f"| S1 | {sprint_counts['S1']} | Descubrimiento, arquitectura, Landing y base de operaciones. |",
            f"| S2 | {sprint_counts['S2']} | Android Native, almacén, despacho, entrega y primeras capacidades de campo. |",
            f"| S3 | {sprint_counts['S3']} | Flutter, Buyer comercial, paridad cross-platform y base iOS. |",
            f"| S4 | {sprint_counts['S4']} | Expansión iOS, cierre cross-platform, evidencia técnica y distribución. |",
            f"| Future | {sprint_counts['Future']} | Historias V3/V4 que requieren trabajo posterior. |",
            "",
            "Las historias funcionales se asignan al primer Sprint de producto en el que "
            "se planifica su resultado. Las filas Technical y Spike representan trabajo "
            "habilitador o investigación; no se transforman en tareas.",
            "",
            "## Criterio de orden",
            "",
            "El orden global de las 97 filas prioriza resultados de negocio y continuidad "
            "operativa: adquisición, recepción, despacho, entrega y recepción del comprador; "
            "las capacidades de acceso y contexto se ubican después de esos resultados. "
            "Las filas Technical y Spike aparecen donde "
            "reducen riesgo, aclaran dependencias o sostienen la calidad de ese resultado; "
            "las capacidades futuras quedan después de los resultados de mayor valor. Sprint "
            "sigue siendo una asignación planificada y no redefine el orden de prioridad.",
            "",
            "Referencias: [User Stories](./2.4.1-user-stories.md) "
            "y [Annex D](../../93-annexes/annex-d-spike-story/spike-story.md).",
            "",
        ]
    )
    return "\n".join(output)


def main() -> None:
    rows = parse_master()
    catalog = parse_catalog()
    for row in rows:
        catalog_title = str(catalog[row["ID"]]["title"])
        if catalog_title != row["Title"]:
            raise SystemExit(
                f"title mismatch for {row['ID']}: master={row['Title']!r}; catalog={catalog_title!r}"
            )
    if set(DESCRIPTIONS) != {row["ID"] for row in rows}:
        missing = sorted({row["ID"] for row in rows} - set(DESCRIPTIONS))
        extra = sorted(set(DESCRIPTIONS) - {row["ID"] for row in rows})
        raise SystemExit(f"description map mismatch; missing={missing}, extra={extra}")
    if set(AC) != set(DESCRIPTIONS):
        missing = sorted(set(DESCRIPTIONS) - set(AC))
        raise SystemExit(f"acceptance map mismatch; missing={missing}")
    if set(TITLE_ES) != {row["ID"] for row in rows}:
        missing = sorted({row["ID"] for row in rows} - set(TITLE_ES))
        raise SystemExit(f"Spanish title map mismatch; missing={missing}")
    USER_STORIES.write_text(generate_user_stories(rows), encoding="utf-8")
    PRODUCT_BACKLOG.write_text(generate_product_backlog(rows), encoding="utf-8")
    print("generated 2.4.1: 12 epics, 73 functional stories; 2.4.3: 97 academic backlog rows")


if __name__ == "__main__":
    main()
