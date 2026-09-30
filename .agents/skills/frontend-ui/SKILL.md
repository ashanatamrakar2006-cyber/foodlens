---
name: Frontend UI Development
description: Standard workflow for implementing Next.js React UI components.
---

# Frontend UI Development

## Purpose
Ensure UI components are built mobile-first, adhere to design tokens, and handle all states.

## When to Use
When implementing or modifying React components in `frontend/`.

## Inputs
- UI Implementation Plan / Requirements

## Step-by-Step Workflow
1. Read `docs/DESIGN-SYSTEM.md`.
2. Read `docs/RESPONSIVE-RULES.md`.
3. Inspect existing components.
4. Reuse existing components where possible.
5. Implement mobile-first (320px+).
6. Add desktop behavior progressively.
7. Handle Loading / Error / Empty / Success states.
8. Check accessibility (ARIA, focus rings).
9. Validate 320px+ constraint.
10. Verify visual consistency against tokens.

## Expected Output
React components integrated into the Next.js frontend with styles mapping strictly to design tokens.

## Validation Checklist
- [ ] Works at 320px width?
- [ ] No hardcoded colors/spacing outside of tokens?
- [ ] Loading/Error states handled?
- [ ] Accessible (WCAG 2.2)?

## Common Failure Modes
- Designing desktop-first and shrinking it down.
- Hardcoding non-semantic hex colors instead of tokens.
