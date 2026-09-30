---
name: AI Feature Development
description: Standard workflow for implementing AI-assisted endpoints in FastAPI.
---

# AI Feature Development

## Purpose
Safely implement assistive AI logic without violating the boundaries of truth.

## When to Use
When modifying or creating endpoints in `backend/ai-service/`.

## Inputs
- AI processing requirement

## Step-by-Step Workflow
1. Read `docs/AI-SPEC.md`.
2. Define the exact AI task.
3. Define deterministic preprocessing (PII stripping).
4. Define strict input/output schemas (JSON).
5. Define the provider abstraction.
6. Define confidence and uncertainty thresholds.
7. Define fallback behavior if AI fails.
8. Define security/privacy controls.
9. Define evaluation cases.
10. Implement ONLY after plan approval.

## Expected Output
A robust FastAPI endpoint that processes AI tasks, handles errors, and returns structured data.

## Validation Checklist
- [ ] AI is strictly assistive?
- [ ] Fails gracefully without breaking the app?
- [ ] Output is structured JSON?
- [ ] AI must never become the source of official truth?

## Common Failure Modes
- Treating AI output as absolute truth.
- Allowing AI failures to crash the frontend.
