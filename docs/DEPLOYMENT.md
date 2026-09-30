# FOODLENS: Deployment Architecture

## Deployment Boundaries
FOODLENS strictly separates deployment concerns to ensure services scale independently and remain agnostic to specific frontend/backend hosting peculiarities.

### Vercel → `frontend/`
- Hosts the Next.js application (UI and API routes).
- Does not build or run the Python service.
- Serverless functions handle the application API and coordinate with Supabase and FastAPI.

### Render → `backend/ai-service/`
- Hosts the Python FastAPI service.
- Deployed via the Dockerfile located in `backend/ai-service/`.
- Does not build or run the Next.js application.
- Exists purely to service AI, NLP, and vector generation requests from the Next.js backend.

### Supabase → Infrastructure
- Hosts the PostgreSQL database with `pgvector` extension.
- Hosts Supabase Auth and Storage.
- Runs database migrations.

---

## Environments

### Development (Local)
- **Frontend:** Local Next.js server (`npm run dev` at `http://localhost:3000`).
- **AI Backend:** Local FastAPI server/uvicorn (`http://localhost:8000`).
- **Database:** Local Supabase project (`supabase start`) or a hosted staging project.

### Production
- **Frontend:** Vercel edge/serverless platform.
- **AI Backend:** Render Web Service.
- **Database:** Supabase Managed Production Project.

---

## Deployment Integrity & Ownership
The architecture remains deployable regardless of GitHub ownership changes.

- **Source of Truth:** The repository contains all configuration logic (Dockerfiles, `package.json`, requirements, migrations).
- **No Hardcoded Accounts:** Avoid deployment-specific code that only works under one specific developer's personal account.
- **Reproducibility:** If ownership changes, a new Vercel project, Render web service, and Supabase project can be initialized, and secrets securely mapped, resulting in an identical production environment.
- **Credentials:** When transferring ownership, all secrets (DB passwords, AI API keys, internal auth keys) must be regenerated and stored securely in the new provider's secret manager.
