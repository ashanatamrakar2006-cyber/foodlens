# FOODLENS: Responsive Rules

## 1. Mobile-First Requirement
Mobile-first is a hard product requirement. Design and implementation must begin from the smallest practical mobile viewport and progressively enhance upward. Desktop is treated as a responsive extension of the mobile information architecture, not a separate distinct product. Do not design desktop first and shrink it afterward.

### Required Validation Widths
- `320px` (Minimum supported width - legacy mobile devices)
- `360px` / `375px` / `390px` / `430px` (Modern mobile targets)
- `768px` (Tablet / Portrait)
- `1024px` (Tablet Landscape / Small Desktop)
- `1280px` (Standard Desktop)
- `1440px+` (Large Desktop)

## 2. Breakpoint Behaviors

### 320px - 430px (Mobile)
- **Layout:** Single-column architecture.
- **Interaction:** Touch-first. 
- **Controls:** Compact controls with full-width primary actions (buttons span 100%).
- **Navigation:** Bottom navigation bar for primary consumer destinations.

### 768px (Tablet)
- **Layout:** Introduction of two-column layouts where useful.
- **Density:** Increased information density. Modals may replace full-screen mobile sheets.

### 1024px+ (Desktop)
- **Layout:** Multi-column layouts. Expanded workspaces.
- **Navigation:** Expanded navigation (responsive top or side).

### 1280px+ (Large Desktop)
- **Layout:** Controlled information density. Use a maximum content width and center it to avoid excessive whitespace.
- **Avoid:** Do not simply scale everything proportionally. Stretching single-column text across the entire screen destroys readability.

## 3. Role-Specific Navigation Strategies
Do not force the same navigation architecture onto every role.
- **Consumer Mobile:** Bottom navigation (Discovery, Scan, My Reports, Profile).
- **Consumer Desktop:** Responsive top or side navigation where appropriate.
- **Business User:** Dashboard-oriented side navigation.
- **Authorized Stakeholder:** Information-dense, data-heavy side navigation.

## 4. Component Responsive Behavior
- **Content Stacking:** Flex/Grid columns wrap to rows on mobile.
- **Cards:** Full width minus padding on mobile.
- **Forms:** Labels on top. Inputs full width.
- **Tables:** Dense desktop tables must convert to card-lists or horizontally scrollable containers on mobile.
- **Filters:** Inline sidebar on desktop -> Modal/Bottom sheet on mobile.
- **Search:** Expands or collapses into an icon depending on viewport.
- **Maps:** Split-view or large block on desktop -> Half-screen or togglable full-screen overlay on mobile.
- **Modals:** Centered dialogs on desktop -> Slide-up Bottom Sheets on mobile for easier thumb reach.
- **Evidence Uploads:** Drag-and-drop zone on desktop -> Tap-to-open-camera-roll on mobile.
- **Image Previews:** Expandable modals or full-screen galleries on mobile.
- **AI Result Presentation:** Clearly segmented blocks that stack vertically on mobile.

## 5. Mobile-First Acceptance Checklist
Before any feature is considered complete, it must pass this validation checklist:
- [ ] UI renders correctly and is fully usable at 320px width.
- [ ] UI renders correctly on 360px, 375px, 390px, and 430px.
- [ ] NO horizontal scrolling occurs (unless explicitly designed, like a data table or carousel).
- [ ] Navigation remains accessible and usable.
- [ ] Forms are fully usable without zooming issues (ensure minimum 16px font size on inputs to prevent iOS auto-zoom).
- [ ] Scan flow and camera access are functional and responsive.
- [ ] Evidence upload works smoothly with mobile native interactions.
- [ ] Reports and AI assessments are readable without text truncation.
- [ ] Charts and data visualizations are usable.
- [ ] Modals and bottom sheets are usable and dismissable.
- [ ] Touch targets are at least 44x44px.
- [ ] Important content/interactions do not depend on hover.
- [ ] Keyboard navigation functions sequentially.
- [ ] Screen reader semantics are present (Alt text, ARIA labels).
- [ ] `prefers-reduced-motion` is supported.
