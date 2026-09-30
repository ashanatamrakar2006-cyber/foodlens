# Rule: Architecture Boundaries
**When to apply:** When planning, modifying, or creating new services/directories.

- **Frontend (`frontend/`):** Next.js application. Handles UI, routing, SSR/SSG.
- **Application Backend (`frontend/app/api` or similar):** Next.js API routes handle normal CRUD, business logic, and API orchestration.
- **AI Backend (`backend/ai-service/`):** Python/FastAPI service exclusively for AI/ML workloads. Do NOT move standard business logic here.
- **Infrastructure (`supabase/`):** Database, auth, and storage layer.
- **Forbidden:** Do NOT use Express. Do NOT introduce new frameworks without explicit approval.
- **Independence:** Keep services independently deployable (Vercel -> frontend, Render -> ai-service).
- **Communication:** Frontend must NOT directly depend on private FastAPI operations; must route through Next.js API.

*Reference:* `docs/ARCHITECTURE.md`
