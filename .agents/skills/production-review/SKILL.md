---
name: Production Readiness Review
description: Comprehensive checklist for ensuring code is ready for deployment.
---

# Production Readiness Review

## Purpose
To audit the system for critical security, performance, and stability risks before launch.

## When to Use
Before a major deployment or handoff.

## Checklist Categories

### MUST FIX (Blockers)
- [ ] **Security:** No secrets exposed in `NEXT_PUBLIC_` or `.env` commits.
- [ ] **Auth:** Supabase Auth enforced properly.
- [ ] **Authorization:** Server-side checks exist. RLS enabled on all sensitive tables.
- [ ] **CORS:** Origins explicitly restricted.
- [ ] **AI Safety:** AI failures degrade gracefully. AI never makes definitive official claims.
- [ ] **Mobile:** Core paths usable at 320px.
- [ ] **File Uploads:** Validated for size and type.
- [ ] **Migrations:** All DB changes in proper Supabase migrations.

### SHOULD IMPROVE (High Priority)
- [ ] **Error Handling:** Client gets clean errors; internal errors are logged.
- [ ] **API Validation:** All inputs validated (Zod/etc).
- [ ] **Indexes:** Foreign keys and frequent queries are indexed.
- [ ] **Accessibility:** Semantic HTML and ARIA used appropriately.
- [ ] **Documentation:** `API-SPEC.yaml` and `DATA-MODEL.md` are up to date.

### FUTURE (Nice to Have)
- [ ] **Performance:** Advanced caching.
- [ ] **Rate Limiting:** IP/User-based rate limiting on APIs.
- [ ] **Logging:** Advanced observability dashboards.

## Expected Output
A categorized report detailing findings (MUST FIX, SHOULD IMPROVE, FUTURE).
