# FOODLENS: User Flows

## Ecosystem Flow
`Consumer` → `FOODLENS` → `Business` → `Authorized Stakeholder where applicable`
*(Note: Not every consumer report reaches an authority.)*

---

## FLOW 1: Consumer discovers a nearby food business
- **Actor:** Consumer
- **Trigger:** Opens the app and accesses the discovery tab.
- **Preconditions:** Location services enabled or location manually entered.
- **Main flow:** 
  1. System requests location.
  2. Consumer grants permission.
  3. System displays a map/list of nearby food businesses with basic info and aggregated ratings.
- **Alternative flow:** Consumer denies location; system prompts for manual entry.
- **Error/empty states:** No businesses found nearby -> Show empty state with prompt to expand search radius.
- **Result:** Consumer views nearby options.
- **Trust/safety considerations:** Display clear distinction between verified and unverified businesses.

## FLOW 2: Consumer searches a different location and compares food businesses
- **Actor:** Consumer
- **Trigger:** Enters a specific location or keyword in the search bar.
- **Preconditions:** None.
- **Main flow:**
  1. Consumer inputs search term.
  2. System returns matching businesses.
  3. Consumer selects multiple to compare basic stats.
- **Alternative flow:** Search yields no results.
- **Error/empty states:** "No results found for [term]".
- **Result:** Consumer finds a business in a target area.
- **Trust/safety considerations:** Ensure search rankings are not manipulated.

## FLOW 3: Consumer scans a packaged food product
- **Actor:** Consumer
- **Trigger:** Taps the "Scan" button.
- **Preconditions:** Camera permissions granted.
- **Main flow:**
  1. Consumer aligns barcode/QR/product image in the viewfinder.
  2. System captures and processes the image.
  3. System identifies the product via API (e.g., Open Food Facts).
- **Alternative flow:** Barcode unreadable -> prompt manual search.
- **Error/empty states:** Product not found in database -> Prompt user to add basic details.
- **Result:** Product is identified and ready for display.
- **Trust/safety considerations:** Warn if product match confidence is low.

## FLOW 4: Consumer views simplified ingredients/nutrition/product information
- **Actor:** Consumer
- **Trigger:** Successfully scans or searches a product.
- **Preconditions:** Product exists in database.
- **Main flow:**
  1. System retrieves raw product data.
  2. System processes data into a clean, mobile-friendly UI highlighting key allergens and macros.
- **Alternative flow:** Incomplete data -> display available data with "incomplete info" warning.
- **Error/empty states:** Network error -> "Unable to load data".
- **Result:** Consumer understands what is in the product.
- **Trust/safety considerations:** Clearly state that data relies on third-party databases and may not be 100% accurate.

## FLOW 5: Consumer views AI-assisted assessment and explanation
- **Actor:** Consumer
- **Trigger:** Scrolls down on the product info page.
- **Preconditions:** AI service is available and product data is present.
- **Main flow:**
  1. AI analyzes ingredients against known general health profiles.
  2. System displays a summary (e.g., "High in sodium, contains common allergens").
  3. UI explicitly tags this as an "AI-Assisted Signal".
- **Alternative flow:** AI service timeout -> hide AI section gracefully.
- **Error/empty states:** AI fails to generate -> Show standard nutritional data only.
- **Result:** Consumer gets an easy-to-read health summary.
- **Trust/safety considerations:** MUST display disclaimer that this is advisory, not medical/official advice, and does not declare absolute safety.

## FLOW 6: Consumer submits verified feedback
- **Actor:** Consumer
- **Trigger:** Taps "Leave Feedback" on a business or product.
- **Preconditions:** Consumer is authenticated.
- **Main flow:**
  1. Consumer selects rating and writes feedback.
  2. Consumer submits.
  3. System marks feedback as verified if tied to a scanned product/location check-in.
- **Alternative flow:** Consumer is unauthenticated -> prompted to log in.
- **Error/empty states:** Submission fails -> Prompt retry.
- **Result:** Feedback is visible on the profile.
- **Trust/safety considerations:** Prevent spam through rate limiting.

## FLOW 7: Consumer reports a concern with supporting evidence
- **Actor:** Consumer
- **Trigger:** Taps "Report Concern".
- **Preconditions:** Consumer is authenticated.
- **Main flow:**
  1. Consumer selects concern category (e.g., foreign object, illness).
  2. Consumer provides text description.
  3. Consumer uploads photo evidence.
  4. System confirms submission and provides a tracking ID.
- **Alternative flow:** Consumer skips photo -> warn that evidence helps resolution.
- **Error/empty states:** File too large -> "Image must be under 5MB".
- **Result:** Report is securely stored and routed to the business.
- **Trust/safety considerations:** Report is kept private between user and business/stakeholder; not published as a public review automatically.

## FLOW 8: System identifies repeated/similar reports
- **Actor:** System (AI Backend)
- **Trigger:** New concern report is saved.
- **Preconditions:** Multiple reports exist for the same entity.
- **Main flow:**
  1. Background process creates embeddings for the new report.
  2. System queries `pgvector` for semantically similar recent reports.
  3. If threshold is met, system flags a "Repeated Pattern".
- **Alternative flow:** No similar reports -> do nothing.
- **Error/empty states:** N/A.
- **Result:** Internal signal generated for Stakeholders.
- **Trust/safety considerations:** A pattern is a signal, not proof of guilt.

## FLOW 9: Business reviews a concern and responds
- **Actor:** Business
- **Trigger:** Logs into the business dashboard.
- **Preconditions:** Business profile is claimed and authenticated.
- **Main flow:**
  1. Business views active concern reports.
  2. Business drafts a response.
  3. Business submits response.
  4. Consumer is notified of the response.
- **Alternative flow:** Business requests more information from the consumer.
- **Error/empty states:** No active concerns -> "All clear!".
- **Result:** The concern loop is closed or progressed.
- **Trust/safety considerations:** Business responses must be logged and immutable.

## FLOW 10: Authorized stakeholder reviews serious/repeated concerns
- **Actor:** Authorized Stakeholder
- **Trigger:** Logs into stakeholder portal.
- **Preconditions:** User has stakeholder role.
- **Main flow:**
  1. Views dashboard of AI-flagged patterns.
  2. Reviews consumer reports and uploaded evidence.
  3. Records an official verification outcome (e.g., "Inspected - Passed").
- **Alternative flow:** Pattern deemed false positive -> dismisses flag.
- **Error/empty states:** No flagged patterns -> "No critical issues detected".
- **Result:** Official status is updated on the platform.
- **Trust/safety considerations:** Only stakeholders can issue official verification statuses.

## FLOW 11: Consumer tracks report/response status
- **Actor:** Consumer
- **Trigger:** Opens "My Reports" tab.
- **Preconditions:** Consumer is authenticated and has filed a report.
- **Main flow:**
  1. System lists reports with statuses (Submitted, Under Review, Responded, Closed).
  2. Consumer taps a report to see detailed timeline and business response.
- **Alternative flow:** N/A.
- **Error/empty states:** No reports filed -> "You have no active reports."
- **Result:** Consumer stays informed.
- **Trust/safety considerations:** Ensure users can only see their own reports.
