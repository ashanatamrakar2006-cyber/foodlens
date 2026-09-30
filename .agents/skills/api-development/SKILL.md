---
name: API Development
description: Standard workflow for creating or modifying Next.js API Routes.
---

# API Development

## Purpose
Ensure application logic endpoints are secure, validated, and consistently formatted.

## When to Use
When working on `frontend/app/api/` routes (Next.js server).

## Inputs
- Endpoint requirement

## Step-by-Step Workflow
1. Read `docs/API-SPEC.yaml`.
2. Identify endpoint contract.
3. Validate request (inputs/body).
4. Authenticate user session (Supabase Auth).
5. Authorize action (RLS/Server-side checks).
6. Execute business logic.
7. Handle errors gracefully (no internal stack traces exposed).
8. Return consistent JSON response format.
9. Update API documentation if the contract changed.
10. Test success and failure paths.

## Expected Output
A secure Next.js API route that strictly matches the API-SPEC contract.

## Validation Checklist
- [ ] Request validated?
- [ ] Auth/Authorization checked?
- [ ] Standard error schema used?

## Common Failure Modes
- Trusting client-provided user IDs instead of extracting them from the secure session.
- Exposing Supabase error details directly to the client.
