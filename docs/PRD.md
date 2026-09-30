# Product Requirements Document: FOODLENS

## 1. Product Overview
FOODLENS is a location-based food discovery and consumer-trust platform that bridges the gap between consumers, food businesses, and authorized food-safety stakeholders. It combines local food discovery, verified consumer feedback, product scanning (barcode/QR/image), and AI-assisted assessments. 

## 2. Problem Statement
Consumers lack a centralized, trustworthy platform to assess food safety, report concerns, and understand complex product information. Feedback loops between consumers and businesses are broken, and potential food safety issues often go unreported or unnoticed.

## 3. Vision
To create the most trusted food ecosystem where better information leads to better choices, constructive feedback drives business improvement, and transparency builds ultimate trust.

## 4. Goals
- Provide easy access to simplified product and nutrition information.
- Enable structured, verifiable consumer reporting of food concerns.
- Facilitate constructive responses from food businesses.
- Leverage AI to identify patterns and assist users without replacing official verification.

## 5. Non-Goals
- We are not an official certification or food-safety regulatory body.
- We do not replace laboratory testing with AI assessments.
- We do not automatically penalize businesses based solely on consumer report volume.
- We do not handle food delivery, payments, or social networking.

## 6. Target Users
1. **Consumers:** Seeking safe food, reliable reviews, and clear nutritional data.
2. **Food Businesses:** Seeking to monitor feedback, respond to concerns, and improve quality.
3. **Authorized Food-Safety Stakeholders:** Seeking to identify recurring patterns or serious issues for potential verification.
*(AI is a supporting system, not a user role.)*

## 7. User Problems
- **Consumers:** Unsure if a product/business is safe; don't know how to interpret complex ingredients; lack a structured way to report issues.
- **Businesses:** Receive unstructured, sometimes unfair feedback; lack visibility into recurring product issues.
- **Stakeholders:** Struggle to detect early signals of widespread food safety patterns.

## 8. Core Value Proposition
- **Better Information:** Clear, AI-assisted summaries of food products.
- **Better Choices:** Location-based discovery with verified reviews.
- **Better Feedback:** Structured reporting with evidence upload.
- **Better Improvement:** Direct business response workflows.
- **Greater Trust:** Clear separation of consumer reports, AI signals, and official verifications.

## 9. MVP Scope (P0)
- **Mobile-First:** Core consumer experience designed exclusively for mobile usage initially.
- **Consumer:** Location-based discovery, business profiles, verified reviews, product scanning, simplified product info, AI-assisted assessment, concern reporting with evidence, and report tracking.
- **Business:** Claim profile, feedback overview, concern visibility, and business response capabilities.
- **AI:** Product info analysis, consumer-friendly explanations, feedback categorization, and basic pattern detection.

## 10. Future Scope (P2)
- Advanced analytics for stakeholders.
- Complex loyalty systems or gamification.
- Deep integration with regulatory government databases.

## 11. Core Features
- Location-based discovery.
- Barcode/image scanning of products.
- AI-summarized ingredient and safety assessments.
- Issue reporting with image evidence.
- Two-way communication for business responses.

## 12. Three-Sided Ecosystem
1. **Consumer** uses the app to discover and report.
2. **Business** uses the app to listen and respond.
3. **Authorized Stakeholder** uses the app to review serious patterns and record verification outcomes.

## 13. Trust and Transparency Principles
- Consumer reports, AI-generated signals, business responses, and official verification must remain clearly separated visually and logically.

## 14. AI Boundaries
- AI outputs are advisory signals, NOT official certification.
- AI assessments do not represent laboratory testing or legal conclusions.
- AI must NEVER automatically declare a business or product safe or unsafe.

## 15. Evidence and Verification Principles
- Reports require structured input and support evidence uploads (images).
- High volume of reports is a signal, not automatic proof of violation.

## 16. Success Metrics
- Number of active users (consumers and businesses).
- Percentage of concern reports that receive a business response.
- Number of AI pattern detections confirmed as useful by stakeholders.

## 17. Key Product Risks
- Users misinterpreting AI assistance as absolute fact.
- Malicious users submitting fake reports to harm businesses.
- AI hallucinating nutritional information.

## 18. Assumptions
- Open Food Facts and Maps APIs provide sufficient coverage for MVP.
- Businesses have an incentive to respond to protect their reputation.

## 19. Dependencies
- Google Maps / Places API.
- Open Food Facts API.
- Supabase for Auth, Storage, and pgvector.

## 20. Out-of-Scope Items
- Payments, Delivery, Chat, Social networking, Unrelated marketplace functionality.
