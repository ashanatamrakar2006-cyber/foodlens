---
name: Database Change Management
description: Standard workflow for safely updating the Supabase PostgreSQL schema.
---

# Database Change Management

## Purpose
To safely modify the schema using migrations while strictly preserving Row Level Security.

## When to Use
Whenever tables, columns, indexes, or RLS policies need to be created or modified.

## Inputs
- Planned schema update

## Step-by-Step Workflow
1. Read `docs/DATA-MODEL.md`.
2. Identify affected entities.
3. Check existing migrations (`supabase/migrations/`).
4. Plan schema change (forward-only).
5. Define constraints/indexes.
6. Define RLS implications.
7. Create a new migration file.
8. Test migration locally.
9. Test RLS policies locally.
10. Update `docs/DATA-MODEL.md` to reflect changes.

## Expected Output
A new `.sql` migration file in `supabase/migrations/` and an updated DATA-MODEL.md.

## Validation Checklist
- [ ] Is RLS enabled and tested?
- [ ] Is the migration forward-only?
- [ ] Never modify the production database manually?

## Common Failure Modes
- Forgetting to enable RLS on a new table.
- Modifying an already-applied migration instead of creating a new one.
