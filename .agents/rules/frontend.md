# Rule: Frontend Engineering
**When to apply:** When building UI or modifying `frontend/` code.

- **Stack:** JavaScript, Next.js, React, Tailwind CSS.
- **Architecture:** Client/server boundaries must be intentional (Server Components vs Client Components).
- **Design System:** Use centralized design tokens. No unnecessary duplication of styles.
- **UI States:** Ensure proper loading, error, and empty states. No blank screens.
- **Accessibility:** Use semantic HTML and ARIA where needed.
- **Security:** Never expose secrets (no private keys in `NEXT_PUBLIC_`).

*Reference:* `docs/DESIGN-SYSTEM.md`
