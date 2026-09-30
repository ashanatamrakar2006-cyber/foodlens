# FOODLENS: Design System

## 1. Design Direction
FOODLENS is designed to feel:
- Trustworthy, Modern, Clean, Human, Data-informed, Consumer-friendly, Premium (but not luxurious), and Food-tech oriented.

**Avoid:** Generic AI-dashboard appearance, excessive gradients, glassmorphism, neon/cyberpunk styling, overuse of cards, excessive animations, visual clutter, and dark-first design.

**Primary Theme:** **LIGHT ONLY**
Dark mode is explicitly excluded from the MVP. The product must use a light-first interface to reinforce trust and cleanliness.

## 2. Color System
A restrained, semantic color system built on deep greens (food-trust) and warm neutral backgrounds. Do not use arbitrary colors; all UI colors must reference semantic tokens.

### Core Tokens
- `--color-background`: Warm neutral (e.g., Off-white/slate-50)
- `--color-surface`: Pure white
- `--color-surface-muted`: Light gray/neutral for secondary cards
- `--color-primary`: Deep green (Trust/Food-tech)
- `--color-primary-hover`: Slightly darker deep green
- `--color-primary-active`: Even darker deep green
- `--color-accent`: Fresh green (for secondary actions/highlights)
- `--color-text`: High-contrast dark charcoal (not pure black)
- `--color-text-secondary`: Medium dark gray
- `--color-text-muted`: Light gray
- `--color-border`: Subtle light gray/neutral
- `--color-success`: Green (System status only)
- `--color-warning`: Amber/Yellow (System status only)
- `--color-danger`: Red (System status only)
- `--color-info`: Blue (System status only)

### Semantic Status Colors (CRITICAL)
Statuses must never be visually ambiguous and must communicate system state, not decorate the interface.
- **Consumer Reported:** Neutral/Warning depending on severity (e.g., Amber).
- **AI-Assisted / Pattern Detected:** Distinct visual treatment (e.g., Soft Indigo/Purple or a unique subtle border) to separate it from official reality.
- **Officially Verified:** Distinct authoritative color (e.g., Deep Blue/Shield icon) reserved exclusively for stakeholder actions.

## 3. Typography
- **Font Family:** Clean, legible sans-serif prioritizing mobile readability (e.g., Inter or Roboto).
- **Display Size:** 32px / 40px
- **H1:** 24px (Mobile) / 32px (Desktop)
- **H2:** 20px (Mobile) / 24px (Desktop)
- **H3:** 18px (Mobile) / 20px (Desktop)
- **Body:** 16px (Primary reading size for accessibility)
- **Small / Body Secondary:** 14px
- **Caption:** 12px
- **Label:** 14px (Medium weight)
- **Button Text:** 16px (Medium weight)
- **Numeric / Data:** Tabular numerals for easy scanning.
*Prioritize mobile readability, consistent line heights (e.g., 1.5 for body), and comfortable paragraph widths. Avoid excessively large typography that wastes mobile viewport space.*

## 4. Spacing System
Predictable baseline grid: `4, 8, 12, 16, 20, 24, 32, 40, 48, 64`.
- **4-16px:** Component internals and tight relationships.
- **20-32px:** Section padding and distinct block separation.
- **40-64px:** Major layout separation.
*Avoid arbitrary one-off values.*

## 5. Border Radius & Elevation
- **Small Radius:** 4px (Checkboxes, small tags)
- **Medium Radius:** 8px (Buttons, inputs, inner cards)
- **Large Radius:** 16px (Main surface cards, bottom sheets)
- **Pill Radius:** 9999px (Badges, primary prominent buttons)

**Elevation:** Restrained. Do not make every component look like a floating card. Rely primarily on spacing, typography, borders, and surface contrast for hierarchy. Use subtle, diffuse shadows only for floating elements (modals, bottom navigation, dropdowns).

## 6. Component System Standards
For all required components (Navigation, Buttons, Inputs, Cards, Modals, Toasts, etc.), the following rules apply:
- **Purpose:** Clearly defined use-case.
- **Variants:** Primary, Secondary, Outline, Ghost.
- **States:** Default, Hover (desktop), Active/Pressed, Focus, Disabled, Loading.
- **Behavior:** Must scale appropriately between mobile and desktop.
- **Accessibility:** Minimum contrast ratios, ARIA labels, keyboard focus rings.

## 7. FOODLENS-Specific UI Patterns

### A. Food Discovery
- **Mobile:** Location/Search at the top, Category filter controls, list of nearby business cards, floating Map/List toggle.
- **Desktop:** Dedicated Search/filter area. Map/List split workspace where appropriate.

### B. Product Scanning
- **Mobile-first:** Prominent scan action. Camera viewfinder overlay. Manual barcode fallback. Product lookup fallback. Clear loading and not-found states.

### C. Product Insights
- **Separation:** Product Information (Ingredients, Nutrition, Allergens) must be visually distinct from the AI-Assisted Assessment.
- **AI Rule:** AI assessment MUST explicitly and visually state that it is AI-assisted.

### D. Consumer Reporting
- Step-by-step or structured form: Concern Category -> Description -> Product/Business Selection -> Batch Info -> Evidence Upload.
- Review screen before submission. Clear submission confirmation and status tracking.

### E. Business Response
- Clearly distinguish the Consumer Report bubble/section from the Business Response, the AI-generated signal, and any Official Verification. Do not blend these into a single narrative flow.

### F. Pattern Detection
- **Neutral Presentation:** Use "Detected pattern" or equivalent neutral language.
- **Never visually communicate:** "Confirmed unsafe" (unless explicitly backed by an official verification outcome).

## 8. Touch & Interaction
- **Touch Target:** Minimum 44x44px for practical touch targets.
- **Spacing:** Adequate spacing between interactive controls to prevent mis-clicks.
- **Hover:** No essential interactions should rely solely on hover.
- **Swipe:** Only use swipe when discoverable and non-essential (e.g., dismiss a toast).
- **States:** Visible focus rings and clear pressed/active states.

## 9. Accessibility (WCAG 2.2)
- Keyboard accessibility with visible focus.
- Semantic HTML and proper labels.
- Color contrast meets standards. Do not rely on color alone to communicate state.
- Screen-reader-friendly status changes and accessible dialogs/forms.
- Alt text for meaningful images.
*Accessibility is part of the component definition, not a final cleanup task.*

## 10. Motion
Use motion only when it improves understanding.
- **Speed:** Fast interaction transitions (e.g., 150ms).
- **Avoid:** Excessive parallax, decorative animations everywhere, long transitions, motion that blocks interaction.
- Respect `prefers-reduced-motion`.

## 11. States (Crucial)
Every major data-driven component must define:
`Loading (Skeletons) → Success (Data) → Empty (Actionable) → Error (Retryable) → Offline / Permission Denied`
*Do not allow blank screens when data is unavailable.*

## 12. Forms
- **Labels:** Top-aligned for mobile readability.
- **Validation:** Clear timing (e.g., on blur), accessible inline error presentation, and success feedback.
- **Usability:** Proper input types (to trigger correct mobile keyboards). Forms must remain fully usable at 320px width. File upload validation must be clear.

## 13. Data Visualization
- Prefer simple charts (bar/line). Avoid unnecessary 3D charts.
- Do not use color as the only distinction. Provide labels/tooltips.
- Provide mobile-friendly tabular alternatives. Avoid charts that become unreadable on small screens.

## 14. Content / Language
UI copy must be clear, short, neutral, human, and action-oriented. Avoid fear-based wording, absolute food-safety claims, and technical AI jargon.
- **Prefer:** "AI-assisted assessment", "Reported by consumers", "Pattern detected".
- **Avoid:** "AI certified safe", "Confirmed issue", "Product is unsafe".

## 15. Design Tokens
Implementation must map the defined tokens (Colors, Typography, Spacing, Radius, Shadows, Borders, Breakpoints, Motion, Z-index) to centralized CSS variables or Tailwind configuration. Do not hardcode design values repeatedly across components.
