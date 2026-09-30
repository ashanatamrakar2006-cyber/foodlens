# FOODLENS: Data Model Specification

## 1. Core Principles
- Strict separation between consumer-generated content, AI-generated signals, and official verifications.
- Supabase Auth manages identity; PostgreSQL manages application profiles.
- External provider data (Maps, Open Food Facts) is referenced and minimally cached, not blindly trusted as the absolute internal source of truth.

## 2. Users and Roles
- `profiles`: Application-specific user data. Links 1:1 to `auth.users` via foreign key.
- `roles`: Enum (`consumer`, `business`, `stakeholder`).
- `business_members`: Links `profiles.id` to `businesses.id`, enabling strict authorization for business users to manage specific locations.

## 3. Businesses
- `businesses`: Core business entity (brand/franchise level).
- `business_locations`: Enables multi-location support. Contains PostGIS geography data.
- `business_external_references`: Maps internal locations to external IDs (e.g., Google Places `place_id`).

## 4. Products
- `products`: Represents a packaged food item.
- **Fields:** `barcode` (unique), `name`, `snapshot_data` (JSONB cache of ingredients/nutrition), `last_synced_at`.
- **Strategy:** Option C (Minimal cached snapshot). Caching is necessary to ensure consumer reports/reviews maintain referential integrity even if the external provider (Open Food Facts) alters or deletes the item, while respecting API rate limits.

## 5. Reviews
- `reviews`: Verified consumer feedback.
- **Fields:** `id`, `author_id`, `business_id` (or `product_id`), `rating`, `content`, `status`, `created_at`.
- **Constraint:** One review per user per entity per time-window to prevent spam. Not represented as an official finding.

## 6. Reports (Core Entity)
- `reports`: Structured consumer concern.
- **Fields:** `id`, `reporter_id`, `business_id`, `product_id` (nullable), `category`, `description`, `status` (SUBMITTED, UNDER_REVIEW, RESPONDED, CLOSED), `created_at`.
- *Reports are NOT confirmed violations.*

## 7. Evidence
- `evidence_metadata`: Separates DB metadata from Supabase Storage files.
- **Fields:** `id`, `owner_id`, `report_id`, `storage_path`, `file_type`, `file_size`, `hash`, `upload_status`.
- **Security:** Large binaries stay in Storage; Postgres only handles metadata linking.

## 8. Business Responses
- `business_responses`: A business's reply to a report.
- **Fields:** `id`, `business_id`, `report_id`, `author_id`, `response_text`, `created_at`.
- **Auth:** Businesses can only respond to reports where the `business_id` matches their membership.

## 9. AI Signals / Patterns
- `ai_signals`: Generated when reports form a pattern.
- **Fields:** `id`, `category`, `confidence`, `summary`, `status` (Requires Review, Dismissed, Verified), `created_at`.
- `signal_reports`: Many-to-many mapping table linking `ai_signals` to source `reports`. This ensures complete traceability.

## 10. Official Verification
- `official_verifications`: Stakeholder actions.
- **Fields:** `id`, `stakeholder_id`, `target_entity_type` (Business/Product), `target_entity_id`, `outcome`, `notes`, `created_at`. 
- Completely isolated from consumer reviews and AI signals.

## 11. Notifications
- `notifications`: User alerts.
- **Fields:** `id`, `user_id`, `type`, `message`, `read_status`, `related_entity_id`, `created_at`.

## 12. Database Relationships
- `profiles` (1) → (M) `reviews`, `reports`
- `businesses` (1) → (M) `business_locations`, `reviews`, `reports`, `business_responses`
- `products` (1) → (M) `reviews`, `reports`
- `reports` (1) → (M) `evidence_metadata`, `business_responses`
- `ai_signals` (M) ← `signal_reports` → (M) `reports`

## 13. Indexing Strategy
- **Primary Keys:** Auto-indexed.
- **Foreign Keys:** `business_id`, `user_id`, `product_id` indexed for fast joins.
- **Geospatial:** GIST index on `business_locations.coordinates` for location discovery.
- **Vector:** HNSW or IVFFlat index on `reports.embedding` (pgvector) for semantic similarity.
- **Lookup:** B-Tree on `products.barcode`.
*Indexes are applied strictly based on expected heavy read patterns.*

## 14. Location Data
- **Decision:** Use **PostGIS** `geography(Point, 4326)` for `business_locations`.
- **Reason:** Natively supported in Supabase. Essential for accurate radius-based discovery queries (FR-002) without complex application-side math.

## 15. PGVector
- **What is embedded:** Consumer `reports.description`.
- **Dimension:** *Open Decision* (e.g., 1536 for OpenAI `text-embedding-3-small`, or 384 for a local `SentenceTransformer`).
- **Metric:** Cosine similarity.
- **Re-embedding:** Triggered only when the underlying embedding model version is upgraded.

## 16. Row Level Security (RLS) & Ownership
- **Consumers:** 
  - `SELECT` own private reports/evidence. 
  - `SELECT` public businesses/products/reviews. 
  - `INSERT` own reports/reviews.
- **Businesses:** 
  - `SELECT` reports where `business_id` is mapped via `business_members`. 
  - `INSERT` `business_responses` only for authorized locations.
- **Stakeholders:** 
  - `SELECT` all reports/signals. 
  - `INSERT` `official_verifications`.
- *Security is strictly enforced at the Postgres level. We never rely only on frontend checks.*

## 17. Data Retention & Migration
- **Retention:** Soft-delete implemented via `deleted_at` timestamps for sensitive evidence/reports. Exact legal retention limits require external confirmation.
- **Migrations:** Managed exclusively via Supabase CLI (`supabase migration new ...`). Forward-only principle. Seed data is strictly isolated in `supabase/seed.sql`.
