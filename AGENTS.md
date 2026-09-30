# FOODLENS: Engineering Rules & Agent Guidelines

## PROJECT OVERVIEW
FOODLENS is a production-ready food discovery, product intelligence, consumer reporting, business response, and food-safety signal platform.

### Core Product Principles
1. Mobile-first is mandatory.
2. Desktop is a responsive extension of the mobile experience.
3. Primary UI theme is light, clean, trustworthy, and food-tech oriented.
4. Consumer trust and transparency are core product principles.
5. AI generates assistance and signals, never official food-safety verdicts.
6. Consumer reports, AI-generated signals, business responses, and official verification must remain clearly separated.

## TECH STACK
**Frontend:**
- Next.js
- React
- JavaScript only
- Tailwind CSS

**Application backend:**
- Next.js API routes

**AI backend:**
- Python
- FastAPI
- Sentence Transformers
- OCR
- Pattern detection

**Infrastructure:**
- Supabase PostgreSQL
- pgvector
- Supabase Auth
- Supabase Storage

**External Services:**
- Open Food Facts
- Google Maps / Places
- AI APIs where appropriate

## ARCHITECTURE & DEPLOYMENT
**Directories & Boundaries:**
- `frontend/`: Next.js frontend and application APIs. (Deployed via Vercel)
- `backend/ai-service/`: Python AI service. (Deployed via Render)
- `supabase/`: Database and Supabase configuration. (Managed via Supabase)
- `docs/`: Documentation.
- `.agents/`: Agent configuration.

**Deployment Rules:**
- Services must remain independently deployable.
- Do not create unnecessary cross-directory runtime dependencies.
- Do not introduce Express unless explicitly approved later.

## CODING RULES
- JavaScript only for the frontend/application layer.
- Python only for the AI service.
- Prefer simple, maintainable production patterns.
- Avoid unnecessary dependencies.
- Reuse existing components and utilities before creating duplicates.
- Never silently change architecture.
- Never introduce a new framework or major dependency without justification.
- Preserve existing functionality when making changes.
- Keep functions and components focused.
- Validate inputs at system boundaries.
- Handle loading, empty, error and success states.

## MOBILE-FIRST RULES
- Design and implement mobile-first.
- Support at least 320px width without horizontal overflow.
- Preserve usability on 375px and 390px mobile layouts.
- Scale progressively to tablet and desktop.
- Do not design desktop first and shrink it afterward.
- Primary actions must remain easy to access on touch devices.
- Tables and dense desktop layouts must have mobile alternatives.

## SECURITY RULES
- Never expose secrets to the frontend.
- Never commit `.env` files or credentials.
- Keep Supabase service-role credentials server-side only.
- Validate user input.
- Enforce authorization server-side.
- Respect Supabase Row Level Security.
- Restrict CORS to approved origins.
- Validate uploaded files by type and size.
- Do not trust client-provided role or identity information.

## AI SAFETY RULES
- AI outputs are advisory signals.
- Never present AI output as official certification.
- Never automatically label a product or business unsafe.
- Preserve confidence and uncertainty where applicable.
- Pattern detection must use defined thresholds from `AI-SPEC.md`.
- AI logic must be testable against known examples.
- Avoid unsupported medical or food-safety claims.

## DOCUMENTATION RULES
Before implementing a significant feature:
1. Read relevant documentation in `docs/`.
2. Check existing architecture.
3. Follow the data model.
4. Follow the design system.
5. Follow acceptance criteria.
6. Create or update a plan when the change is complex.

**Source of Truth Hierarchy:**
`AGENTS.md` → `PRD.md` → Architecture → Requirements → Design System / Responsive Rules → Data Model / API Spec / AI Spec → Feature Plan → Code → Tests / Evals

*When documentation and code disagree:*
- Identify the conflict.
- Do not silently rewrite architecture.
- Follow the higher-level documented requirement.
- Ask for clarification when necessary.

**Documentation References:**
Relevant detailed rules will live in:
`docs/PRD.md`
`docs/ARCHITECTURE.md`
`docs/DESIGN-SYSTEM.md`
`docs/RESPONSIVE-RULES.md`
`docs/DATA-MODEL.md`
`docs/API-SPEC.yaml`
`docs/AI-SPEC.md`
`docs/USER-FLOWS.md`
`docs/ACCEPTANCE-CRITERIA.md`
`docs/SECURITY.md`
`docs/TESTING.md`
`docs/DEPLOYMENT.md`

## AGENT WORKFLOW
For every significant task:
1. Understand the requirement.
2. Inspect the relevant existing files.
3. Read applicable documentation.
4. Create a concise implementation plan.
5. Implement the smallest correct change.
6. Run relevant tests and validation.
7. Review for mobile responsiveness.
8. Review security and error handling.
9. Update documentation when behavior or architecture changes.
10. Summarize what changed and what was verified.

**DO NOT:**
- Build features that were not requested.
- Rewrite working code unnecessarily.
- Create duplicate components.
- Bypass API contracts.
- Ignore mobile layouts.
- Hardcode secrets.
- Mix Python AI logic into frontend JavaScript.
- Mix unrelated responsibilities between services.
- Make architectural decisions silently.
