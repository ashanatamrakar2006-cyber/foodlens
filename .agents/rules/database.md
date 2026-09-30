# Rule: Database Management
**When to apply:** When defining schemas, constraints, or relationships.

- **Primary DB:** Supabase PostgreSQL.
- **Migrations:** Schema changes MUST use Supabase migrations (`supabase migration new`). Never modify production schema directly.
- **Security (RLS):** Row Level Security is mandatory for protected data. Never bypass authorization through frontend assumptions. Service-role access is server-side only.
- **Integrity:** Use foreign keys and constraints to preserve data integrity. Avoid unnecessary duplication.

*Reference:* `docs/DATA-MODEL.md`
