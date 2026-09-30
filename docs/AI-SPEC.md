# FOODLENS: AI Specification

## 1. Core Directive
**FOODLENS AI MUST BE ASSISTIVE.**
It must NEVER independently declare a product/business safe or unsafe, nor issue an official food-safety finding, nor declare a legal violation. AI acts as a sophisticated analytical filter to assist human judgment.

## 2. AI Pipeline
1. **Input:** Raw consumer report, product ingredients, or image.
2. **Validation:** Ensure input meets length/type requirements (Deterministic).
3. **Preprocessing:** Clean text, strip identifiable PII (Deterministic).
4. **OCR (if applicable):** Extract text from image evidence.
5. **AI Reasoning / Embedding:** Call Provider Adapter for LLM/Embeddings.
6. **Structured Output:** Parse LLM response into strict schema (Deterministic).
7. **Confidence Assessment:** Evaluate metadata/confidence scores against thresholds.
8. **Persistence:** Save results to Postgres/pgvector (Deterministic).

## 3. AI Use Cases (MVP)
1. **Product Information Interpretation:** Simplify complex packaged food ingredients.
2. **Allergen Highlighting:** Extract likely allergens from raw ingredient text.
3. **Consumer-friendly Nutrition:** Explain nutritional macros in plain English.
4. **Report Categorization:** Map free-text consumer reports to standard concern categories.
5. **Semantic Similarity:** Map report descriptions to vector space.
6. **Pattern Detection:** Group semantically similar reports over time.
7. **Evidence OCR:** Extract readable text/batch numbers from uploaded images.

## 4. AI Output Contract
Every AI operation must return structured, machine-readable JSON. Arbitrary free-form text generation is strictly prohibited unless wrapped in a defined schema.

```json
{
  "task": "ingredient_analysis",
  "result": {
    "summary": "High in sodium...",
    "allergens": ["Peanuts"]
  },
  "confidence": 0.92,
  "warnings": ["May contain traces of nuts not explicitly listed"],
  "model": "gpt-4o-mini",
  "model_version": "2024-05-13",
  "processing_time_ms": 450
}
```

## 5. Confidence and Fallbacks
- **Limitation:** A high confidence score means the AI is statistically certain of its output relative to its training, NOT that the output is absolute objective truth.
- **Fallback:** If confidence is below the defined threshold (e.g., < 0.75) or the AI provider times out/fails, the system must return uncertainty, fall back to displaying the raw verified source data (e.g., standard un-summarized ingredient list), and gracefully hide the AI assessment. It must never fabricate data to fill UI gaps.

## 6. Pattern Detection Logic
A pattern is NEVER defined by vector similarity alone.
**Candidate Pattern Requirements:**
1. Generate report embedding.
2. Retrieve semantically similar reports from `pgvector`.
3. **Apply Metadata Constraints:** Matches must occur within a specific `time window` AND share the exact `business_id` or `product_id`.
4. **Apply Thresholds:** Minimum number of independent reports required (e.g., N >= 3).
5. If constraints are met, generate an `AI Signal` (Candidate Pattern).
6. The pattern remains a signal until explicitly reviewed by a human (Stakeholder), at which point it may become an `Official Verification`.

## 7. LLM Strategy (Adapter Pattern)
FOODLENS is strictly provider-agnostic at the business logic layer.
`FastAPI Service -> Provider Adapter Interface -> LLM Provider`
- Prevents vendor lock-in.
- Adapter enforces structured JSON output.
- Handles timeouts, retries, and rate limits gracefully.

## 8. OCR Strategy
`Image -> Validation -> External OCR Engine -> Text Normalization -> Structured Extraction`
- OCR errors must not silently become facts. Text must be presented to the user/stakeholder for verification if it drives a critical reporting flow.

## 9. Prompt Management
- Prompts are version-controlled string templates stored in the backend (FastAPI).
- Prompts are NEVER hardcoded in the Next.js frontend UI.
- Changes to prompts that alter output structure require explicit evaluation and API versioning.

## 10. AI Security & Privacy
- **PII Minimization:** Strip unnecessary identifiable data from reports before sending to external LLMs.
- **Prompt Injection:** Treat all model outputs as untrusted input. Escape outputs before rendering in Next.js to prevent XSS.
- **Provider Keys:** Strictly held in Render environment variables; never exposed to Vercel or browsers.

## 11. AI Observability
Log (without storing raw sensitive user content): 
`request_id`, `task`, `model`, `model_version`, `prompt_version`, `latency_ms`, `success_boolean`, `confidence_score`, `token_cost`.

## 12. Open Decisions (Pending Evaluation)
These decisions must be explicitly evaluated and finalized before backend implementation:
1. **Exact LLM Provider:** Balance reasoning capability vs cost vs latency (e.g., Anthropic Claude 3 Haiku vs OpenAI GPT-4o-mini).
2. **Exact Embedding Model:** e.g., `text-embedding-3-small` vs local `all-MiniLM-L6-v2`. Dictates `pgvector` dimension constraint.
3. **Similarity Threshold & Report Volume:** Exactly what cosine distance indicates a "match", and how many matches within what time frame (e.g., 3 reports in 7 days) trigger a signal. Must be evaluated on synthetic dataset.
4. **OCR Engine:** Tesseract (Local/Free but lower accuracy) vs Cloud Vision APIs.
5. **External Data Caching Policy:** Legal review required on Open Food Facts / Google Places Terms of Service regarding normalized data persistence.
