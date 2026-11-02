# Accessibility floor

This is the minimum standard. No profile, style or default in this skill goes below it. It follows WCAG 2.2 level AA plus the platform equivalents on iOS and Android. Design to it from the start: adding accessibility after a screen is built costs far more and works worse.

If a project document records a deliberate decision below this floor, follow it, mention the trade-off once when you first work in that area, and move on.

## Contents

1. The floor at a glance
2. Perception: contrast, colour, text
3. Operation: targets, keyboard, focus, gestures
4. Understanding: labels, errors, consistency
5. Robustness: semantics and screen readers
6. Moving content and time
7. Platform specifics
8. How to check

## 1. The floor at a glance

| Area | Minimum | WCAG |
| --- | --- | --- |
| Body text contrast | 4.5:1 against its actual background | 1.4.3 |
| Large text contrast (24 px, or 18.66 px bold) | 3:1 | 1.4.3 |
| Contrast of icons, control boundaries, focus indicators, chart marks | 3:1 against adjacent colours | 1.4.11 |
| Meaning | Never through colour alone; pair it with text, icon or shape | 1.4.1 |
| Text resize | Usable at 200% zoom; on mobile, at the largest accessibility text size | 1.4.4 |
| Reflow | No two-way scrolling at 320 CSS px wide (except tables, maps, editors) | 1.4.10 |
| Text spacing | Nothing clips or overlaps when people increase line, paragraph, letter and word spacing (so avoid fixed-height text containers) | 1.4.12 |
| Pointer target | At least 24 × 24 CSS px, or enough spacing; platform touch minimums are larger (see section 7) | 2.5.8 |
| Keyboard | Everything operable by keyboard, with no traps | 2.1.1, 2.1.2 |
| Focus | Visible focus indicator, in a logical order, never hidden behind sticky headers or footers | 2.4.3, 2.4.7, 2.4.11 |
| Dragging | Every drag has a single-pointer alternative (buttons, a menu) | 2.5.7 |
| Labels | Every input has a visible label, and its accessible name contains the visible text | 3.3.2, 2.5.3 |
| Errors | Identified in text, with a suggested fix | 3.3.1, 3.3.3 |
| Redundant entry | Don't ask for the same information twice in one process; prefill or offer to reuse it | 3.3.7 |
| Authentication | No cognitive tests (remembering, transcribing); allow paste and password managers | 3.3.8 |
| Status messages | Announced to assistive technology without moving focus | 4.1.3 |
| Consistent help | Help mechanisms in the same place across pages | 3.2.6 |
| Moving content | Anything that moves automatically for more than 5 s can be paused, stopped or hidden | 2.2.2 |
| Flashing | Nothing flashes more than 3 times a second | 2.3.1 |

## 2. Perception: contrast, colour, text

- **Check contrast on every surface a colour sits on:** white, the page background, hover, selected and pressed states, in both light and dark themes. Muted grey that passes on white often fails on a tinted selected row.
- **Placeholder text,** disabled-looking text that still carries information, and text over images all need the same contrast. If text over an image can't be guaranteed, add a scrim.
- **Disabled controls** are exempt from contrast rules, but they still need to be recognisable as controls. Don't rely on low opacity alone, and say why something is unavailable if it isn't obvious.
- **Status needs more than colour:** pair it with a label or a distinct icon shape. About 1 in 12 men has a colour vision deficiency, and everyone struggles to tell colours apart in bright sunlight.
- **Links in body text** need more than colour (an underline, or 3:1 contrast with the surrounding text plus a non-colour cue on hover and focus).
- **Text must scale.** Use relative units on the web (`rem`), and Dynamic Type text styles on iOS and `sp` units on Android. Layouts reflow at large sizes: stack horizontal arrangements and wrap text rather than truncating it.

## 3. Operation: targets, keyboard, focus, gestures

- **Targets:** follow the platform minimums in section 7. Where the visible control is smaller, extend its hit area with padding. Keep at least 8 px between adjacent targets on touch.
- **Keyboard:** make every interactive element reachable with Tab and operable with Enter or Space, and arrow keys within composite widgets (menus, tabs, grids, radio groups). Escape closes overlays. Use native elements (`button`, `a`, `input`, `select`, `dialog`) so this comes for free.
- **Focus:** keep the focus indicator visible and high-contrast (at least 3:1). Use `:focus-visible` so mouse users don't see rings on click. Move focus into a dialog when it opens and back to the trigger when it closes. After deleting an item, put focus somewhere sensible (the next item, or the list).
- **Gestures:** every swipe, long-press, pinch or drag also has a visible alternative. Multi-finger or path-based gestures always have a single-tap alternative.
- **Don't override platform gestures:** iOS swipe-back from the edge, Android system back, and browser shortcuts.

## 4. Understanding: labels, errors, consistency

- **Labels are visible and persistent,** above the field or beside it. Placeholders are hints only.
- **Mark required fields** with an asterisk explained at the top of the form, and label genuinely optional fields "(optional)". Don't rely on colour or the asterisk alone: the required state is also exposed to assistive technology (`required` or `aria-required`).
- **Use the right input type and autocomplete attributes** (`type="email"`, `inputmode="numeric"`, `autocomplete="one-time-code"`, iOS `textContentType`) so keyboards, autofill and password managers work.
- **Errors** are announced and described in text, linked to the field (`aria-describedby` and `aria-invalid` on the web, an accessibility hint or value on native), and focus moves to the first problem when a form submission fails.
- **Help and navigation** stay in the same place on every screen.
- **Time limits:** warn before a session expires and let people extend it. Never lose entered data on timeout.

## 5. Robustness: semantics and screen readers

- **Native elements first.** A `div` with a click handler isn't a button: it has no role, no keyboard support and no focus. Only add ARIA when no native element fits, and then follow the WAI-ARIA Authoring Practices pattern for that widget.
- **Use `aria-label` only on elements with a role** (controls, landmarks, images). On a plain `div` or `span` it's ignored and fails checks. For a loading region, set `aria-busy="true"` and announce "Loading…" through a status region.
- **Every control has an accessible name.** Icon-only buttons get a label naming the action ("Delete invoice", not "trash icon"). Images that convey information get alt text. Decorative images get empty alt text, or are hidden from assistive technology.
- **Use headings and landmarks** (`h1` to `h3`, `main`, `nav`) on the web, and header traits on native, so screen reader users can jump around the page.
- **Announce dynamic changes** (toasts, live counts, "Saved", search results updating) through a live region on the web or an accessibility announcement on native, without stealing focus.
- **Group related content** so a list row reads as one sensible sentence ("Invoice 204, Sam Lee, £480, overdue") rather than a scatter of fragments.
- **Reading order** follows the visual order.

## 6. Moving content and time

- **No parallax, auto-playing video or looping animation** without a way to pause it.
- **Nothing flashes** more than three times per second.
- **Auto-advancing content** (carousels, rotating banners) needs a pause control, or shouldn't auto-advance at all.
- **Toasts** that contain an action stay long enough to use it, or the action is available elsewhere too.

## 7. Platform specifics

| Platform | Minimums and features to support |
| --- | --- |
| iOS and iPadOS | 44 × 44 pt hit targets. Dynamic Type through text styles, up to the accessibility sizes. VoiceOver labels, traits and hints. Reduce Transparency, Increase Contrast, Bold Text, Smart Invert. |
| Android | 48 × 48 dp touch targets. Font scale up to 200% using `sp`. TalkBack content descriptions. Respect system back. |
| React Native and Expo | `accessibilityLabel` (or `aria-label`), `accessibilityRole` (or `role`), `accessibilityState`, `hitSlop` to extend targets, `allowFontScaling` left on, `AccessibilityInfo` for announcements. |
| Web | WCAG 2.2 AA. 24 × 24 CSS px minimum target for pointers, and 44 px for touch layouts. Works at 320 px wide and 400% zoom. Use `:focus-visible`, `prefers-contrast` and `forced-colors`. |

## 8. How to check

- **Keyboard pass:** unplug the mouse. Can you reach, operate and leave everything? Is focus always visible and in a sensible order?
- **Screen reader pass:** try VoiceOver (macOS or iOS), TalkBack, or NVDA on Windows. Does every control announce a sensible name, role and state?
- **Zoom and text size:** check 200% and 400% browser zoom, and the largest Dynamic Type or font scale size.
- **Contrast:** check each text and background pairing in both themes, including hover, selected and disabled states.
- **Automated tools:** axe, Lighthouse, Xcode's Accessibility Inspector or Android's Accessibility Scanner. These catch around a third of issues, so they never replace the manual passes.
