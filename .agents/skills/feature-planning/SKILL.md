---
name: Feature Planning
description: Standard workflow for planning features prior to implementation.
---

# Feature Planning

## Purpose
To create a concise, safe implementation plan before writing complex code, ensuring architecture and PRD alignment.

## When to Use
Before beginning any significant feature or cross-cutting structural change. Do not modify code during planning.

## Inputs
- Feature Request / Prompt

## Step-by-Step Workflow
1. Read relevant PRD section (`docs/PRD.md`).
2. Read relevant user flow (`docs/USER-FLOWS.md`).
3. Read acceptance criteria (`docs/ACCEPTANCE-CRITERIA.md`).
4. Inspect current implementation (`view_file` / `list_dir`).
5. Identify affected files.
6. Identify API/database implications (`docs/DATA-MODEL.md` / `docs/API-SPEC.yaml`).
7. Identify mobile/UI implications (`docs/DESIGN-SYSTEM.md` / `docs/RESPONSIVE-RULES.md`).
8. Identify security implications.
9. Produce implementation plan.
10. Define validation steps.

## Expected Output
A markdown summary plan detailing the architecture impact, affected files, and validation checklist.

## Validation Checklist
- [ ] Are PRD constraints respected?
- [ ] Is security evaluated?
- [ ] No code was written yet?

## Common Failure Modes
- Jumping straight to code without checking existing components.
- Ignoring mobile-first requirements in the plan.
