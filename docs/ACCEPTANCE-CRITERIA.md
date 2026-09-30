# FOODLENS: Acceptance Criteria

## A. Authentication
- **FR-001** (P0): 
  - **Given** a user is on the login screen
  - **When** they enter valid credentials
  - **Then** they are authenticated and redirected to the dashboard.
  - **Edge cases:** Invalid credentials show clear error message; unverified email prompts verification.

## B. Location Discovery
- **FR-002** (P0):
  - **Given** a consumer grants location access
  - **When** they open the discovery tab
  - **Then** a list of businesses within a set radius is displayed.
  - **Edge cases:** No businesses found shows an empty state.

## C. Food-business Profiles
- **FR-003** (P0):
  - **Given** a consumer selects a business
  - **When** the profile loads
  - **Then** basic info, aggregate rating, and verified reviews are visible.

## D. Search/Filter
- **FR-004** (P1):
  - **Given** a user is on the search page
  - **When** they type a keyword
  - **Then** matching businesses and products appear.

## E. Verified Reviews
- **FR-005** (P0):
  - **Given** a consumer leaves a review
  - **When** they submit it
  - **Then** the review is saved and displayed on the profile.

## F. Product Scanning
- **FR-006** (P0):
  - **Given** the camera is active
  - **When** a valid barcode/image is scanned
  - **Then** the system fetches product data.
  - **Edge cases:** Unrecognized scan prompts manual entry.

## G. Product Information
- **FR-007** (P0):
  - **Given** product data is fetched
  - **When** the page renders
  - **Then** ingredients and nutritional data are displayed cleanly.

## H. AI-Assisted Assessment
- **FR-008** (P0):
  - **Given** a product page is viewed
  - **When** AI assessment is available
  - **Then** an advisory signal is shown.
  - **AI Safeguards:** 
    - Must explicitly show it is AI-assisted.
    - Must not present as official verification.
    - Must not automatically declare safe/unsafe.
    - Failures default to standard nutritional data safely without breaking core product.

## I. Concern Reporting
- **FR-009** (P0):
  - **Given** a user wants to report an issue
  - **When** they fill the structured form and submit
  - **Then** a private report is generated and status set to "Submitted".

## J. Evidence Upload
- **FR-010** (P0):
  - **Given** a user is submitting a report
  - **When** they select an image under 5MB
  - **Then** the image uploads successfully.
  - **Edge cases:** File > 5MB or invalid format returns immediate client-side error.

## K. Report Tracking
- **FR-011** (P0):
  - **Given** a user has submitted reports
  - **When** they view "My Reports"
  - **Then** the current status of each report is accurate.

## L. Business Response
- **FR-012** (P0):
  - **Given** a business views a concern
  - **When** they submit a response
  - **Then** the consumer is notified and status updates to "Responded".

## M. Pattern Detection
- **FR-013** (P1):
  - **Given** multiple similar reports occur
  - **When** they cross the similarity threshold
  - **Then** the system flags the entity for stakeholder review.
  - **AI Safeguards:** 
    - False positives are treated as possible signals requiring human review. 
    - Pattern detection based strictly on documented criteria in AI-SPEC.md.

## N. Authorized Verification Workflow
- **FR-014** (P1):
  - **Given** a stakeholder reviews a flagged entity
  - **When** they log an official outcome
  - **Then** the entity's official status updates, clearly distinct from AI signals.

## O. Notifications/Status Updates
- **FR-015** (P1):
  - **Given** a report changes status
  - **When** the business responds
  - **Then** the consumer receives an in-app notification.

## P. Mobile Responsiveness
- **FR-016** (P0):
  - **Given** the app is accessed on any device
  - **When** the viewport is 320px or wider
  - **Then** there is no horizontal overflow. Touch interactions are usable, primary actions are accessible, and desktop does not break mobile hierarchy. Images/forms remain responsive. Important content does not depend on hover.

## Q. Accessibility
- **FR-017** (P1):
  - **Given** a user relies on a screen reader
  - **When** they navigate the app
  - **Then** semantic HTML and ARIA labels provide clear context.

## R. Security
- **FR-018** (P0):
  - **Given** any API request
  - **When** data is accessed or mutated
  - **Then** authorization is enforced server-side via Supabase RLS.
  - **Security Safeguards:** 
    - Users cannot access others' private data.
    - Business users isolated to their data.
    - Service-role credentials never reach client.
    - Uploads validated by type/size.
    - API inputs validated.
    - CORS restricted.

## S. Error/Loading/Empty States
- **FR-019** (P0):
  - **Given** a network request is pending
  - **When** the user waits
  - **Then** a loading skeleton or spinner is shown. Empty results show clear next steps.
