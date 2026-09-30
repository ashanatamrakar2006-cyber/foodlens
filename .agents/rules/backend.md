# Rule: Backend Engineering
**When to apply:** When creating or modifying Next.js API routes.

- **Responsibility:** Next.js API routes own normal CRUD and business operations.
- **Security:** Validate all external inputs (Zod/etc). Authorize server-side using Supabase Auth/RLS.
- **Responses:** Provide consistent REST-oriented responses. Do not expose internal database errors or stack traces to clients.
- **Communication:** Internal service communication (Next.js -> FastAPI) must be authenticated.
- **AI/ML:** Use FastAPI ONLY for AI/ML operations.

*Reference:* `docs/API-SPEC.yaml`
