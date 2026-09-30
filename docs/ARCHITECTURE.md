# FOODLENS: Production Architecture

## 1. ARCHITECTURAL DECISION & OVERVIEW
FOODLENS uses a strictly separated, production-ready architecture prioritizing simplicity, security, and independent scalability.

```text
Consumer / Business / Authority
            ↓
        Next.js (Vercel)
            ↓
     Next.js API Routes
       ↙          ↘
Supabase          FastAPI (Render)
PostgreSQL        AI Service
Auth              OCR
Storage           Embeddings
pgvector          Pattern Detection
       ↑
       └──── External APIs (Maps, Open Food Facts)
```

### FRONTEND / NEXT.JS
**Responsible for:**
- UI & Client-side interaction (Mobile-first explicitly)
- Routing & Rendering (SSR/SSG where appropriate)
- Form handling & validation feedback
- Calling application APIs (Next.js API Routes)
- Authentication UI
- Consumer, business, and stakeholder interfaces

### NEXT.JS API ROUTES
**Responsible for normal application backend logic:**
- Authentication/session handling (Supabase server-side clients)
- Authorization checks & Role validation
- CRUD for Users, Businesses, Products, Reviews, Reports
- Evidence metadata handling
- Business responses, Report status, Notifications
- External API orchestration (Maps, Open Food Facts)
- Supabase database operations via PostgREST/Supabase SDK
- Calling FastAPI when AI processing is required

### FASTAPI AI SERVICE
**Responsible ONLY for AI/ML-related workloads:**
- OCR of uploaded evidence or labels
- Text preprocessing
- Embeddings generation
- Semantic similarity & Repeated pattern detection
- Report categorization
- AI-assisted product analysis
- AI-related processing pipelines

*Rule: Do NOT move ordinary CRUD/business logic into FastAPI.*

### SUPABASE
**Responsible for:**
- PostgreSQL Database
- pgvector (Vector embeddings for pattern detection)
- Supabase Auth (Identity and access management)
- Supabase Storage (Secure evidence uploads)
- Row Level Security (RLS) policies
- Database relationships, constraints, indexes, and migrations

### EXTERNAL SERVICES
**Integration Boundaries:**
- **Google Maps / Places:** Used by Next.js API to populate/resolve location and business data.
- **Open Food Facts:** Used by Next.js API to resolve barcode scans and fetch baseline nutritional info.
- **AI Provider (Open Decision):** Used by FastAPI for generating summaries and embeddings. Exact provider (e.g., OpenAI, Anthropic, local model) is explicitly deferred.

---

## 2. API BOUNDARIES
Browser → Next.js API → Supabase

When AI processing is required:
Browser → Next.js API → FastAPI → AI Provider → FastAPI → Next.js API → Browser / Supabase

**Hard Rules:**
- The browser must NOT directly call the private FastAPI service.
- The browser must NOT receive Supabase service-role keys.
- The browser must NOT receive AI provider secrets.
- Private backend credentials stay strictly on the server (Next.js API or FastAPI).

---

## 3. CORS STRATEGY
- **Production Origins:** Explicitly defined in Next.js and FastAPI configurations (e.g., `https://app.foodlens.com`).
- **Development Origins:** Explicitly allowed (e.g., `http://localhost:3000`).
- **Private APIs:** Never use `*` for authenticated endpoints. FastAPI must only allow requests originating from the Next.js API's domain or strictly internal network IPs.
- *Note:* CORS is a browser security mechanism, not an authorization mechanism. Full authorization must happen server-side.

---

## 4. AUTHENTICATION AND AUTHORIZATION
**Flow:**
User → Supabase Auth → Session/token → Next.js → Server-side authorization → Supabase RLS

**Roles:**
- `consumer`
- `business`
- `stakeholder`
- *(No global admin role unless genuinely required later)*

**Rules:**
- Authentication is managed via Supabase Auth (JWT).
- Authorization relies on server-side Next.js route checks AND Supabase Row Level Security (RLS).
- Never rely solely on frontend UI hiding for security.
- Service-role usage is strictly limited to backend contexts where bypassing RLS is architecturally necessary (e.g., webhooks, backend-to-backend syncing).

---

## 5. API DESIGN
REST-oriented API contract following consistent `/api/v1/` conventions.

- **Methods:** standard HTTP verbs (GET, POST, PATCH, DELETE).
- **Validation:** Server-side validation using Zod or similar.
- **Standardized Error Format:**
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable message",
    "details": {}
  }
}
```
*Stack traces and sensitive internal DB errors are never exposed.*

---

## 6. SERVICE-TO-SERVICE COMMUNICATION
Next.js communicates with FastAPI synchronously (or asynchronously for heavy tasks) over HTTPS.

**Flow:** Next.js API → Authenticated Internal Request → FastAPI → Structured Result → Next.js API
- **Internal Auth Strategy (Open Decision):** Either a shared symmetric secret (`INTERNAL_AI_SERVICE_KEY`) passed via headers, or a secure internal VPN/VPC mesh depending on deployment provider capabilities.
- **Resilience:** Requests to FastAPI must have explicit timeouts (e.g., 10s).
- **Retries:** Next.js API should handle safe retries for idempotent FastAPI endpoints.

---

## 7. ERROR HANDLING
- **Database / External API Failure:** Graceful degradation. If Open Food Facts fails, allow manual entry.
- **FastAPI / AI Failure:** If AI is unavailable, the core product (reviews, raw nutritional data) must still function normally. AI sections gracefully hide or display a "Temporarily Unavailable" state.
- **Rate Limiting:** Enforced on API routes to protect Supabase and AI budgets.

---

## 8. PRODUCTION REQUIREMENTS
Architecture accounts for:
- HTTPS / Secure Cookies.
- Input validation at the boundary.
- Strict RLS on all tables.
- Database indexes for geospacial search (PostGIS/location) and vectors (pgvector).
- File upload restrictions (<5MB, valid image types) enforced by Next.js and Supabase Storage.

---

## 9. ARCHITECTURAL DECISION RECORDS (ADRs)

### ADR-001: Next.js is the main application layer
- **Reason:** Provides unified frontend and application API layer, ideal for fast iteration and Vercel hosting.
- **Consequence:** All core CRUD and UI logic lives in one repository segment.

### ADR-002: FastAPI is isolated for AI/ML workloads
- **Reason:** Python has the strongest ecosystem for AI/ML (LangChain, embeddings, OCR). Keeping it separate prevents polluting the Next.js app with heavy python dependencies.
- **Consequence:** Requires managing a second deployment (Render) and service-to-service auth.

### ADR-003: Express is not used
- **Reason:** Next.js API routes are sufficient for MVP backend logic.
- **Consequence:** Simplifies stack and reduces boilerplate.

### ADR-004: Supabase is the primary database/auth/storage platform
- **Reason:** Provides out-of-the-box Auth, Postgres, Storage, and vector support (pgvector).
- **Consequence:** High dependency on Supabase ecosystem (vendor lock-in accepted for MVP velocity).

### ADR-005: Vercel hosts Next.js
- **Reason:** Zero-config deployment for Next.js.
- **Consequence:** Application APIs run as serverless functions (must account for cold starts and connection pooling).

### ADR-006: Render hosts FastAPI
- **Reason:** Easy Docker-based deployment for Python services that may need sustained memory/compute compared to serverless.
- **Consequence:** Distinct deployment pipeline from frontend.

### ADR-007: Mobile-first is a product and architecture requirement
- **Reason:** Consumers scan and report issues on the go.
- **Consequence:** UI/UX and API payloads must be optimized for mobile networks and viewports.

---

## 10. UNRESOLVED OPEN DECISIONS
1. **AI Provider:** Which specific LLM API (OpenAI, Anthropic, etc.) to use.
2. **Service Auth Mechanism:** Exact mechanism for Next.js → FastAPI auth (e.g., shared secret vs network isolation).
3. **Caching:** Strategy for caching Open Food Facts / Maps data to prevent rate limits.
