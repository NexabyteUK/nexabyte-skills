# Visual design

Layout, type, colour, depth, icons and motion, across platforms. The project's design documents set the actual values. This file sets out how to choose and use them well.

## Contents

1. Hierarchy
2. Layout, spacing and grouping
3. Typography
4. Colour
5. Depth and surfaces
6. Icons and imagery
7. Motion
8. Dark mode
9. Identity without a design system
10. Building a minimal token set

## 1. Hierarchy

Every screen needs one clear starting point, then a path through the rest.

- **The squint test:** blur your eyes or the screenshot. The most important thing should still stand out, and related things should still look grouped.
- **Signal importance by size, weight, contrast, position and space,** roughly in that order of subtlety. Use colour last, and keep it for meaning.
- **Use one page heading per screen.** Don't repeat the same title in the breadcrumb, header and card.
- **One primary action per context** is the strongest visual element after the content itself.
- **Reduce competing emphasis.** If everything is bold, coloured or boxed, nothing is. Lower the prominence of secondary items rather than raising the primary ever higher.
- **Apple's layering idea applies everywhere:** content is the base layer, and controls and navigation sit above it, quieter and more transparent to attention.

## 2. Layout, spacing and grouping

- **Use a spacing scale** on a 4 px base (4, 8, 12, 16, 24, 32, 48, 64). Pick from the scale and never improvise values.
- **Proximity groups things.** Space between groups should be clearly larger than space within them, about twice as much works well. Use spacing before reaching for borders or boxes.
- **Align to a few edges.** Every element should line up with something. Ragged left edges are the most common sign of an unconsidered layout.
- **Avoid nested cards and boxes inside boxes.** One container level is usually enough. Lists and tables can sit directly on the surface with hairline separators.
- **Respect safe areas** on devices with rounded corners, notches, home indicators and system bars. Backgrounds can extend edge to edge, but content and controls stay inside.
- **Use a consistent rhythm.** The same kind of element gets the same spacing everywhere.
- **Plan for real content:** long names, translations (30 to 40% longer), large numbers, missing values and large text sizes. Layouts that only work with sample data break in production.

## 3. Typography

- **Use few sizes.** A single screen rarely needs more than three or four (NN/G suggests about three), and five or six cover a whole product. Base them on the platform's text styles (iOS Dynamic Type styles, Android's type scale) or a modest ratio on the web.
- **Body text:** 16 px or more on the web, 17 pt on iOS (Body), 14 to 16 sp on Android. Absolute minimum 11 to 12 px or pt, for captions only, and still meeting contrast.
- **Line height:** about 1.4 to 1.6 for body text, and 1.1 to 1.3 for headings. Make it tighter for large display text and looser for long reading.
- **Line length:** 60 to 75 characters for prose.
- **Weights:** two or three, such as regular, medium and semibold. Use weight for hierarchy before size.
- **Tracking:** tighten large headings slightly. Leave body text at the default. Add slight tracking to small all-caps labels, and avoid all-caps for anything longer than a label.
- **Numbers:** tabular (fixed-width) figures in tables, prices, timers and anything that updates in place, so digits don't shift.
- **Fonts:** the system font is the safe default (SF Pro on Apple platforms, Roboto on Android, `system-ui` on the web). A brand font replaces it consistently. If you use a monospace, keep it for code, IDs and keyboard hints, never running prose.
- **Make text scale:** iOS Dynamic Type, Android font scale and browser zoom. Text must reflow, not clip, at large sizes.

## 4. Colour

- **Use semantic tokens, not raw values:** text (primary, secondary, muted), surface (base, raised, sunken), border, accent, and status (success, warning, danger, info). Components refer to tokens, and themes change the values.
- **One accent colour** for the primary action, selection, focus and links. Spread it across too many elements and it stops signalling anything.
- **Status colours carry status only,** and each is paired with an icon or label (accessibility floor). Red means error or destruction, not emphasis.
- **Keep most of the screen neutral,** so the few coloured elements carry meaning. A rough guide: neutrals cover about 90% of the surface.
- **Check contrast on every surface each colour sits on,** in every theme and every state (hover, selected, disabled).
- **Use perceptual colour spaces** (OKLCH or LCH) when generating ramps and themes, so steps look even and contrast is predictable.
- **Platform system colours** (iOS `label`, `secondaryLabel`, `systemBackground`, tints; Android dynamic colour) adapt automatically to dark mode, increased contrast and vibrancy. Use them in native code unless the brand overrides.
- **Brand colour in UI:** a vivid brand colour often fails as text or as a button background. Derive an accessible "action" shade from it, and keep the pure brand colour for non-text marks.

## 5. Depth and surfaces

- **Separate surfaces in this order:** spacing first, then a background tone change, then a hairline border, then shadow. Each step is louder than the one before.
- **Keep shadows for floating layers:** menus, popovers, dialogs, sheets and drag previews. A shadow tells people "this sits above and will go away".
- **Use a few elevation levels** (for example base, raised and overlay), each with a defined surface tone and shadow. Don't improvise shadows.
- **Translucent materials** (Apple's Liquid Glass, frosted panels) belong to the navigation and control layer that floats above content: tab bars, toolbars, sheets. Don't use them for content itself, and don't stack glass on glass. Check legibility over busy content, and provide solid fallbacks for Reduce Transparency and Increase Contrast.
- **Use a scrim** behind modal layers, strong enough to separate them but light enough to keep context.

## 6. Icons and imagery

- **Use one icon family** with a consistent grid, stroke weight and corner style. On native Apple platforms, SF Symbols match the system type and scale with Dynamic Type. Otherwise choose one outline family (such as Lucide) and stick to it.
- **Size icons with the text they sit beside,** usually 16 to 20 px in UI and 24 px in toolbars and tab bars, and align them optically.
- **Add a label to an icon** unless its meaning is universal (close, search, back, more). Icon-only buttons need an accessible name and, on desktop, a tooltip.
- **One icon means one thing everywhere.** Don't reuse a symbol for two meanings.
- **Use real images:** real product, people or content beats stock and decorative illustration. Every image should identify or explain something.
- **Illustration in working tools** is rare and quiet. Consumer products can use more, consistently.

## 7. Motion

Motion explains change. It shows where something came from, where it went, what changed, and that an action registered.

- **Purposes:** feedback (press, toggle), orientation (a sheet rising from the button that opened it), continuity (a list item expanding into its detail) and attention (a subtle pulse on something new). If a movement serves none of these, remove it.
- **Durations:** 100 to 150 ms for small feedback, 200 to 300 ms for larger transitions, and rarely more than 400 ms. Exits are faster than entrances.
- **Easing:** ease-out (decelerate) for entrances, ease-in for exits, and springs for direct manipulation on iOS. Linear easing only for continuous progress.
- **On the web, animate transform and opacity only.** Animating width, height or top causes layout work and jank.
- **Nothing decorative loops.** No parallax, no floating elements, no scroll-jacking in working products.

## 8. Dark mode

- **Design both themes deliberately.** Dark mode is not inverted light mode.
- **Surfaces:** in dark mode, raised surfaces are lighter than the base. Elevation shows through lightness, because shadows barely show on dark backgrounds. iOS uses true black for the base level and greys for elevated levels. Web and Android products usually use a very dark grey base.
- **Text:** use off-white for primary text, with lower-contrast tiers for secondary text. Each tier must still pass contrast.
- **Colour:** reduce the saturation of accent and status colours slightly, and raise their lightness so they don't vibrate against the dark background. Re-check contrast for every pairing.
- **Images and illustrations:** check them on dark backgrounds. Logos and line art may need dark variants.
- **Follow the system setting by default.** People rarely look for an in-app switch (NN/G), and Apple asks apps not to duplicate it. On the web, an optional System, Light and Dark choice is fine.
- **Contrast in dark mode:** Apple recommends aiming for 7:1 for custom colours, especially small text, because thin light text on dark surfaces blooms and reads less clearly. Light mode generally reads better for people with typical vision, so never force dark.

## 9. Identity without a design system

When a project has no brand guide, don't default to an anonymous system look. Build a small, deliberate identity from what you know:

- **Name:** the product or organisation name appears where people orient themselves (the header, the page title, the app's first screen).
- **Accent:** derive one accent from the brand colour or the domain (green for a park run, for example). Use it confidently on the primary action, the current navigation item, key figures and a few larger areas, not just one button. Derive accessible text and background shades from it.
- **Type:** pair the system font with one decision, such as a heavier weight for headings, tighter tracking at large sizes, or a single display face for public pages.
- **Imagery and shape:** for public and consumer surfaces, use real or representative imagery and a consistent corner radius and illustration style. For working tools, identity comes from the accent, type and voice, not decoration.
- **Voice:** a recognisable, consistent way of speaking (see `voice-and-copy.md`).

Calm and characterful aren't opposites. Remove noise, and keep identity.

## 10. Building a minimal token set

When a project has no design system yet, define only this much and grow it from real needs:

| Group | Tokens |
| --- | --- |
| Colour | text, text-secondary, text-muted, surface, surface-raised, surround, border, border-strong, accent, accent-hover, on-accent, success, warning, danger, info, plus hover, selected and pressed overlays |
| Type | caption, body-small, body, section heading, title, large title (size, line height and weight for each) |
| Space | 4, 8, 12, 16, 24, 32, 48 |
| Radius | small (controls), medium (menus, cards), large (sheets, dialogs) |
| Elevation | raised, overlay (shadow and surface pairs) |
| Motion | fast (about 120 ms), standard (about 200 ms), slow (about 300 ms), plus standard easing curves |
| Size | control heights for pointer and touch, icon sizes |

Name tokens by role (`text-muted`), never by value (`grey-500`), so themes and rebrands change values without touching components.
