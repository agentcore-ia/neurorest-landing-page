```markdown
# Design System Specification: Editorial Intelligence

## 1. Overview & Creative North Star: "The Orchestrated Flow"
This design system is built to move beyond the "boxed-in" nature of traditional SaaS dashboards. For an AI operating system serving the high-pressure environment of a restaurant, the UI must feel like a calm, invisible conductor. 

Our Creative North Star is **"The Orchestrated Flow."** We reject the rigid, line-heavy grids of legacy software. Instead, we embrace a high-end editorial layout characterized by **intentional asymmetry, expansive negative space, and tonal layering.** The goal is to make complex data feel like a premium lifestyle magazine—authoritative yet breathable. We replace "noise" with "nuance," using shifts in surface color and sophisticated typography to guide the eye, rather than borders and heavy shadows.

---

## 2. Colors: Tonal Depth & The "No-Line" Rule
The palette is rooted in deep, trustworthy slates with electric "intelligence" accents. We use color not just for decoration, but as a structural tool.

### Color Strategy
*   **Primary (`#000000`):** Used for absolute authority in text and high-contrast primary actions.
*   **Secondary (`#00687a`) & Tertiary (`#000000`):** These serve as the backbone of the "Deep Navy" trust profile. 
*   **Innovation Accents:** The `secondary_container` (`#57dffe` - Vibrant Cyan) and `on_tertiary_container` (`#9863ff` - Electric Purple) are reserved exclusively for AI-driven insights, automated suggestions, and high-value "moment-of-truth" interactions.

### The "No-Line" Rule
**Explicit Instruction:** Do not use 1px solid borders to section content. Boundaries must be defined solely through background shifts.
*   Use `surface` (`#fcf8fa`) for the base page.
*   Use `surface_container_low` (`#f6f3f5`) to define a sidebar or secondary navigation.
*   Use `surface_container_highest` (`#e4e2e4`) for interactive dashboard widgets.
*   *Why?* Removing lines creates a "boundless" feeling that mimics a premium, custom-coded experience rather than a template.

### The Glass & Gradient Rule
To evoke a high-tech "AI" feel, floating panels (modals, popovers) must use **Glassmorphism**:
*   **Background:** `surface` at 70% opacity.
*   **Effect:** `backdrop-blur: 20px`.
*   **Gradient:** For Hero CTAs, use a subtle linear gradient from `primary` to `primary_container` (`#131b2e`) at 135 degrees to add three-dimensional soul to the button.

---

## 3. Typography: Editorial Authority
We pair **Manrope** (Display/Headline) with **Inter** (Title/Body) to balance high-end brand personality with technical utility.

*   **Display & Headline (Manrope):** Large, bold, and tightly tracked. Used for high-level restaurant health metrics and evocative hero statements. The `display-lg` (3.5rem) should be used asymmetrically—pushed to the edges of the screen to create a "magazine" feel.
*   **Title & Body (Inter):** Optimized for data density. `title-md` (1.125rem) is the workhorse for card headings. `body-md` (0.875rem) is the standard for operational data.
*   **Label (Inter):** Used for micro-copy and AI status tags. 

*Hierarchy Note:* Always lead with a `display` or `headline` element that is significantly larger than the surrounding content to establish a clear editorial "hook."

---

## 4. Elevation & Depth: Tonal Layering
In this design system, "Depth" is a color, not a shadow.

*   **The Layering Principle:** Stack containers to create hierarchy. 
    *   Base: `surface`
    *   Section: `surface_container_low`
    *   Card/Module: `surface_container_lowest` (White)
    *   This "White-on-Grey" stack creates a natural, soft lift that feels cleaner than drop shadows.
*   **Ambient Shadows:** When an element must float (e.g., a "New Order" notification), use an extra-diffused shadow: `box-shadow: 0 20px 40px rgba(27, 27, 29, 0.06)`. Note the low 6% opacity—it should feel like a soft glow of light, not a "drop shadow."
*   **The Ghost Border Fallback:** If accessibility requires a border (e.g., input focus), use `outline_variant` at 15% opacity. Never use 100% opaque outlines.

---

## 5. Components: Precision & Minimalist Rigor

### Buttons
*   **Primary:** Solid `primary` (`#000000`) with `on_primary` text. Corners: `md` (0.75rem).
*   **AI Action:** A gradient-filled button using `tertiary_container` (`#25005a`) to `on_tertiary_container` (`#9863ff`). This signals an "AI-enhanced" action.
*   **Secondary:** Ghost-style but with a `surface_container_high` background on hover. No border.

### Cards & Lists
*   **Forbid Dividers:** Do not use horizontal rules between list items. Use 16px or 24px of vertical white space from the spacing scale to separate items.
*   **Nesting:** Place `surface_container_lowest` (White) cards onto a `surface_container` background for a crisp, elevated look.

### Input Fields
*   **Style:** Minimalist. No bottom line, no full box. Use `surface_container` as the background with `sm` (0.25rem) rounded corners.
*   **Focus State:** Shift background to `surface_container_high` and add a subtle `primary` glow.

### AI Suggestion Chips
*   **Visuals:** Use the `secondary_fixed` (`#acedff`) background with `on_secondary_fixed` (`#001f26`) text. These should always have `full` rounded corners (9999px) to look like pill-shaped "brain-bits."

---

## 6. Do's and Don'ts

### Do:
*   **Embrace Asymmetry:** Place a large headline on the left and a small data card on the far right, leaving the center empty. This is "High-End Editorial."
*   **Use Massive White Space:** If you think there is enough space, double it. Space is the primary "trust" indicator.
*   **Layer Surfaces:** Use the `surface-container` tiers to create depth without relying on CSS shadows.

### Don't:
*   **Don't use 1px lines:** No borders, no dividers, no table lines. Use background color shifts.
*   **Don't use "Pure" Greys:** All neutrals are slightly tinted with slate/navy (`#fcf8fa`) to maintain a premium tech-forward feel.
*   **Don't crowd the AI:** AI insights (purple/cyan) need a 40px "clear zone" to ensure they feel special and intelligent rather than cluttered.

---

## 7. The Spacing Scale
Spacing is the "glue" that allows a borderless UI to function.
*   **Tight (4px/8px):** For related label/input pairs.
*   **System (16px/24px):** Standard padding for cards and containers.
*   **Editorial (64px/80px/120px):** For separating major sections of the dashboard. This extreme spacing is what makes the design feel "High-End."```