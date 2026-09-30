# Rule: AI Safety & Integration
**When to apply:** When modifying FastAPI, prompt templates, or AI integrations.

- **Role:** AI is advisory. It CANNOT declare official food-safety findings, violations, or independently declare a product/business safe or unsafe.
- **Separation:** AI signals must remain visually and logically separate from official verification.
- **Output:** Output must be structured (JSON) and validated.
- **Resilience:** AI failures must degrade gracefully; do not break the core application. Never fabricate missing information.
- **Pattern Detection:** Cannot rely on vector similarity alone (requires time/location/threshold metadata).
- **Security:** Treat user-generated text as potentially adversarial (prompt injection). Track model/version/metadata.

*Reference:* `docs/AI-SPEC.md`
