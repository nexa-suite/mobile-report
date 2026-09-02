#!/usr/bin/env bash
set -euo pipefail

container_name="${NEXA_PERSISTENCE_CONTAINER:-nexa-modern-postgres}"
database_user="${NEXA_PERSISTENCE_DB_USER:-nexa}"
database_name="${NEXA_PERSISTENCE_DB_NAME:-nexa}"

psql=(docker exec "$container_name" psql -U "$database_user" -d "$database_name" -P pager=off)

printf '%s\n' '--- database version ---'
"${psql[@]}" -c 'SELECT version();'

printf '%s\n' '--- relevant tables and isolation flags ---'
"${psql[@]}" -At -F '|' -c "
SELECT n.nspname || '.' || c.relname,
       CASE
         WHEN c.relforcerowsecurity THEN 'FORCE_RLS'
         WHEN c.relrowsecurity THEN 'RLS'
         ELSE 'NO_RLS'
       END
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE c.relkind = 'r'
  AND n.nspname IN ('tenant_management', 'catalog_management', 'warehouse', 'logistics', 'notifications')
  AND c.relname ~* '(workspace|sellable_sku|inventory_lot|physical_allocation|fulfillment|dispatch_order|delivery|proof_of_delivery|temperature|buyer_receipt|push_subscription)'
ORDER BY 1;
"

printf '%s\n' '--- selected columns ---'
"${psql[@]}" -At -F '|' -c "
WITH wanted(schema_name, table_name) AS (
  VALUES
    ('tenant_management', 'workspace'),
    ('tenant_management', 'workspace_membership'),
    ('catalog_management', 'sellable_sku'),
    ('warehouse', 'inventory_lot'),
    ('warehouse', 'inventory_temperature_evaluation'),
    ('warehouse', 'physical_allocation'),
    ('logistics', 'fulfillment'),
    ('logistics', 'dispatch_order'),
    ('logistics', 'delivery'),
    ('logistics', 'delivery_attempt'),
    ('logistics', 'proof_of_delivery'),
    ('logistics', 'temperature_evidence'),
    ('logistics', 'delivery_handoff_token'),
    ('logistics', 'buyer_receipt_fact'),
    ('notifications', 'push_subscription')
)
SELECT w.schema_name || '.' || w.table_name,
       string_agg(a.attname, ', ' ORDER BY a.attnum)
FROM wanted w
JOIN pg_namespace n ON n.nspname = w.schema_name
JOIN pg_class c ON c.relnamespace = n.oid AND c.relname = w.table_name
JOIN pg_attribute a ON a.attrelid = c.oid AND a.attnum > 0 AND NOT a.attisdropped
GROUP BY w.schema_name, w.table_name
ORDER BY 1;
"

printf '%s\n' '--- selected constraint counts ---'
"${psql[@]}" -At -F '|' -c "
SELECT n.nspname || '.' || c.relname,
       count(*) FILTER (WHERE con.contype = 'p') AS primary_keys,
       count(*) FILTER (WHERE con.contype = 'f') AS foreign_keys,
       count(*) FILTER (WHERE con.contype = 'u') AS unique_constraints,
       count(*) FILTER (WHERE con.contype = 'c') AS check_constraints
FROM pg_constraint con
JOIN pg_class c ON c.oid = con.conrelid
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname IN ('tenant_management', 'catalog_management', 'warehouse', 'logistics', 'notifications')
  AND c.relname IN (
    'workspace', 'workspace_membership', 'sellable_sku', 'inventory_lot',
    'inventory_temperature_evaluation', 'physical_allocation', 'fulfillment',
    'dispatch_order', 'delivery', 'delivery_attempt', 'proof_of_delivery',
    'temperature_evidence', 'delivery_handoff_token', 'buyer_receipt_fact',
    'push_subscription'
  )
GROUP BY n.nspname, c.relname
ORDER BY 1;
"

printf '%s\n' '--- selected triggers and policies ---'
"${psql[@]}" -At -F '|' -c "
SELECT event_object_schema || '.' || event_object_table,
       trigger_name,
       action_timing || ' ' || event_manipulation
FROM information_schema.triggers
WHERE event_object_schema IN ('warehouse', 'logistics', 'notifications')
  AND (event_object_table ~* '(delivery|proof|temperature|buyer_receipt|handoff|attempt|disposition)')
ORDER BY 1, 2, 3;
"
"${psql[@]}" -At -F '|' -c "
SELECT schemaname || '.' || tablename, policyname, cmd
FROM pg_policies
WHERE schemaname IN ('warehouse', 'logistics', 'notifications')
  AND (tablename ~* '(delivery|proof|temperature|buyer_receipt|handoff|attempt|disposition)')
ORDER BY 1, 2;
"
