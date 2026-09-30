# Rule: Security Enforcement
**When to apply:** Throughout the entire development lifecycle.

- **Secrets:** Never commit secrets/`.env` files. Never expose service-role or AI provider keys to the browser.
- **Input/Uploads:** Validate all API input and uploaded files (size, type). Treat external API/model output as untrusted.
- **Authorization:** Enforce authorization server-side. Protect sensitive user/business information.
- **CORS:** Restrict CORS; no `*` for private APIs.

*Reference:* `docs/SECURITY.md`
