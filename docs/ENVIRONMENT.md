# FOODLENS: Environment Management

## Variable Classification Rules
- **NEVER** commit `.env` files to version control.
- **NEVER** expose service-role keys to the browser.
- **NEVER** expose AI provider keys to the browser.
- **NEVER** put private secrets in `NEXT_PUBLIC_*` variables.
- Production secrets live exclusively in Vercel/Render secret configurations.
- Local secrets live in `.env.local` or `.env` files (which are ignored by Git).

---

## Variable Classifications

Variables are strictly categorized into three domains:

### 1. PUBLIC (Browser-Safe)
Accessible by the Next.js client-side bundle. These identify endpoints or public keys but do not grant administrative privileges.
*Example variable names (do not use these exact values):*
- `NEXT_PUBLIC_SUPABASE_URL` (e.g., `https://xyzcompany.supabase.co`)
- `NEXT_PUBLIC_SUPABASE_ANON_KEY` (e.g., `eyJhbGci...`)

### 2. SERVER-ONLY (Next.js API Private)
Accessible only by the Next.js server runtime. These grant administrative or backend access to databases and services.
*Example variable names (do not use these exact values):*
- `SUPABASE_SERVICE_ROLE_KEY` (Used for bypassing RLS in specific webhooks/admin tasks).
- `INTERNAL_AI_SERVICE_KEY` (Used to authenticate requests made from Next.js to FastAPI).
- `FASTAPI_SERVICE_URL` (The URL of the Render deployment).

### 3. INTERNAL-SERVICE (FastAPI Private)
Accessible only by the FastAPI Python runtime on Render.
*Example variable names (do not use these exact values):*
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY` (Used for vector inserts).
- `AI_PROVIDER_API_KEY` (e.g., OpenAI/Anthropic secret key).
- `INTERNAL_AI_SERVICE_KEY` (Used to validate incoming requests from Next.js).
