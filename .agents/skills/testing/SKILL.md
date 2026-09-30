---
name: Testing & Validation
description: Standard workflow for validating features before completion.
---

# Testing & Validation

## Purpose
Ensure no feature is claimed complete without rigorous execution of tests.

## When to Use
After implementing any feature or bug fix.

## Inputs
- Completed implementation

## Step-by-Step Workflow
1. Identify changed behavior.
2. Identify relevant acceptance criteria (`docs/ACCEPTANCE-CRITERIA.md`).
3. Test the happy path.
4. Test invalid input (edge cases).
5. Test authorization boundaries.
6. Test failure states (e.g., network failure, AI failure).
7. Test mobile UI (320px+) where relevant.
8. Test regression risk.
9. Run relevant automated tests (if any exist).
10. Report exactly what was tested in the final response.

## Expected Output
A validation report confirming the feature meets its acceptance criteria.

## Validation Checklist
- [ ] Error states verified?
- [ ] Mobile UI verified?
- [ ] Auth verified?
- [ ] NEVER claim tests passed if they were not actually executed?

## Common Failure Modes
- Testing only the happy path.
- Assuming desktop works means mobile works.
