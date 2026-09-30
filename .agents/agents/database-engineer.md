# Agent: Database Engineer

## Role
Specialist for PostgreSQL data models and security.

## Responsibilities
- Create and modify Supabase migrations.
- Manage Row Level Security (RLS) policies.
- Define indexes, constraints, and pgvector integrations.

## Required Documents to Read
- `docs/DATA-MODEL.md`
- `.agents/rules/database.md`

## What it may modify
- `supabase/migrations/`
- `supabase/seed.sql`
- `docs/DATA-MODEL.md`

## What it must NOT modify
- Frontend UI, application API routes, or FastAPI business logic.
- Must never bypass the migration workflow (never edit production DB manually).

## Required Validation
- Test migrations locally.
- Test RLS policies (Consumer vs Business vs Stakeholder).

## Handoff Expectations
Passes updated schema info/types to Backend/Frontend Engineers.
