# Profile: Linear-style

**Opt-in only.** Apply this profile when the project's design documents name it or the user asks for it.

The idea: *imagine Linear built this product.* The domain and brand are different, but the composition, behaviour and restraint are the same. Keep the project's own typeface, colours, voice and light or dark preference. Take Linear's structure and discipline, not its look. A near-black canvas, lavender accent and glowing gradients copied wholesale produce a generic "Linear clone" that people now recognise as a cliché.

The core principles in `SKILL.md` still apply, including the accessibility floor. This profile adds a visual and behavioural signature on top.

## Contents

1. Fit
2. The signature in six rules
3. Starting tokens
4. Layout patterns
5. Behaviour
6. Guardrails: where the style breaks the floor
7. Sources

## 1. Fit

| Fits | Doesn't fit |
| --- | --- |
| Operator, productivity and developer tools | Consumer, lifestyle and emotional products |
| People who use it daily, for hours | First-time or occasional users |
| Desktop-first work with dense lists, records and tracking | Touch-first or mobile-first products (use the touch adaptations below) |
| Teams that value speed and keyboard use | Audiences with heavy accessibility needs, unless the guardrails are applied in full |
| Admin consoles behind a public site | Brands that need to stand out visually |

## 2. The signature in six rules

1. **Don't compete for attention you haven't earned.** Navigation and chrome sit a step quieter than the work. Dim the sidebar, use fewer and smaller icons, and drop coloured icon backgrounds. (Linear's 2026 refresh.)
2. **Structure should be felt, not seen.** Use alignment, spacing and hairline separators to organise, not boxes, nested cards, tinted panels or heavy dividers.
3. **Near-monochrome with one accent.** Greys do about 90% of the work. The accent marks the primary action, selection, focus and live state. A small fixed set of semantic hues carries status, and nothing else. Restraint isn't absence: the brand accent must still be recognisable at a glance, on the primary action, the current navigation item, focus and key figures.
4. **Hierarchy through grey level and weight,** not through colour or big jumps in size. Use three or four text tiers and two or three weights.
5. **Hairlines over shadows.** Show elevation through small lightness steps between surfaces. Keep shadows for floating layers (menus, popovers, dialogs).
6. **Fast and exact.** Make updates optimistic, transitions short, and support the keyboard throughout. Every hover, focus, empty and edge state is part of the spec, as much as the main state is. Details people never consciously notice, like a submenu that stays open while the cursor travels to it diagonally, are what makes it feel well made.

## 3. Starting tokens

Use these only where the project's documents give no values. They're adapted from Linear's live CSS and the Flow-style rules the profile was built from.

**Colour structure.** Generate themes from a few inputs (base, accent, contrast level) in a perceptual space (LCH or OKLCH), so lightness steps look even across hues.

| Role | Guidance |
| --- | --- |
| Surfaces | 3 or 4 levels: surround (behind the work), surface (the work), raised (menus, dialogs), and optionally sunken |
| Text | Primary, secondary and tertiary all meet 4.5:1 on every surface they appear on. A fourth, quaternary tier is decoration only |
| Separators | One hairline tone inside a surface, and one slightly stronger at a surface's edge |
| Overlays | Hover, selected and pressed as translucent ink (about 5%, 8% and 12%), so they work on any surface |
| Accent | One colour, with hover and pressed steps, and white text on it at 4.5:1 or more |
| Semantic | Red, orange or amber, green and blue, used for status only and always paired with a symbol or label |

**Type.** Use the project's sans-serif (Linear uses Inter, with Inter Display for headings), and a mono for IDs, timestamps and keyboard hints if the brand has one.

| Role | Size and weight |
| --- | --- |
| Metadata, timestamps, control labels | 12 px, 400 to 500, a quieter tier |
| Working text: rows, navigation, menus, property values | 13 px, 400 to 500 |
| Section headings | 14 px, 600 |
| Reading prose | 14 to 16 px, 60 to 75 characters a line, line height about 1.5 to 1.6 |
| Headings | 18, 20 or 24 px, 600, slight negative tracking (about −0.01 em) |

Use tabular figures for numbers, and sentence case throughout. 12 px is the floor, and it must still meet 4.5:1.

**Size roles.** Each control belongs to a named variant. Never use one-off sizes.

| Role | Pointer | Touch (coarse pointer or narrow breakpoint) |
| --- | --- | --- |
| Standard control (button, input, select) | 28 to 32 px | 44 px |
| Compact control (chip remove, stepper) | 24 px | 44 px hit area |
| Navigation item | 28 to 32 px | 44 px |
| List row | 32 to 40 px | grows to two lines |
| Group header | 32 to 36 px | 36 to 44 px |

**Spacing, radius, icons, motion.**
- Spacing: a 4 px base. Collection insets about 16 px, detail insets about 24 px, narrow screens about 12 px.
- Radius: 4 px (micro), 6 px (controls, chips), 8 px (menus, popovers), 12 px (work surface, dialogs).
- Icons: one outline family (such as Lucide) at 14 to 16 px with an even stroke (about 1.5), monochrome, used sparingly.
- Motion: 120 to 200 ms (about 160 ms is typical), easing out, animating only transform and opacity. Overlays appear instantly or almost so. Nothing decorative moves.

## 4. Layout patterns

**App frame.** Navigation sits on the surround. The work sits on a single surface panel, inset a few pixels with a rounded corner and an edge hairline (full width on phones). List work items first in the navigation, with settings, help and account at the foot. Highlight only the deepest matching navigation item.

**Collection (list).**
```
Section                                  [New item]
Search  Filter  Display   Status: Open ×     4 of 42
○ ABC-12  Subject of the item     detail   £240   3d
```
- A header row: where you are on the left, and the primary "New <object>" on the right.
- A view bar: search, Filter (which items appear), Display (how they're arranged: list, board, grouping, ordering), active filters as removable chips, and a count of the full matching set at the end.
- Single-line hairline rows with no outer box by default. A second, quieter line is fine when the item needs it (a next step, a reason). A status symbol and quiet ID lead, then the subject at a slightly heavier weight, then quieter values. Right-align amounts and ages. Add column headings only when people compare across rows.
- Group headers are sticky and show the whole group's count.
- Use a board only when changing an item's stage is the task.
- On phones a row becomes two lines (subject, then ID and status), with the key value kept on the right.

**Detail (record).**
```
Section › ABC-12                          [Primary] ⋯
Subject heading                  │ Status   ○ Open
Saved · 2 min ago                │ Owner    Sam Lee
```
- One header: breadcrumbs ending in the record's reference, then actions ending with the primary and an overflow menu. When space runs out, move secondary actions into the overflow first, then truncate ancestor crumbs. The primary stays put.
- Main content on the left, and a properties column on the right with muted labels and borderless values that edit in place. On phones the properties column becomes a disclosure.
- If the record holds several independent lists (a customer's invoices, bookings, notes), use tabs under the header, with the open tab in the URL. If the record is a document, keep it on one page.
- Activity and history: who did it, the change (old → new) and when.

**Composer (create).** A dialog with a large, unboxed title field and an unboxed description, structured values as compact property buttons, and a single commit button on the right of the footer. Use × to close, and ask first if there's anything to discard. Cmd/Ctrl+Enter submits. Opened directly by URL, the composer becomes a page.

**Settings.** A narrow centred column (about 640 px) with one page heading, then groups made of a small section heading and hairline-separated rows: label (and a one-line explanation if needed) on the left, control on the right. Changes save as they're made, with a quiet toast. Don't add a Save button and don't use cards.

**Command menu.** Cmd/Ctrl+K opens a searchable list of every action, scoped to the current selection when there is one. It sits alongside visible controls and never replaces them.

## 5. Behaviour

- **Keyboard:** offer single-key shortcuts for frequent actions (Linear uses C to create, J and K or the arrow keys to move, X to select, and Esc to clear), plus the command menu. Shortcuts never fire while focus is in a text field. Never override browser or OS shortcuts. Show each shortcut in its menu item and tooltip so it can be discovered. A project may choose to add no custom shortcuts. That's a valid opt-out.
- **Selection:** support keyboard selection (X, Shift+arrows) as well as mouse selection (click, Shift-click). Bulk actions apply to the selection through a toolbar and the command menu.
- **Inline editing:** a value keeps its size and type when edited. It has a hover surface at rest, and shows a caret or picker while editing, with no pencil icons. Enter or moving away applies the change, and Esc restores the old value. Apply a property choice as soon as it's picked.
- **Optimistic and local-first feel:** apply edits instantly and reconcile in the background. Show a quiet "Saving" or "Saved" state, and a clear notice if the server rejects the change.
- **Context menus:** a right-click on a row offers the same actions as its overflow menu.
- **Cursor:** use the arrow cursor on app controls (native-app feel), the pointer cursor for links in reading content, and the I-beam in text.
- **View state:** filters, grouping, the open tab and the selected record live in the URL. Going back from a detail view restores the list position. Previous and next follow the active view's order.
- **Status by shape:** one symbol family that progresses by shape (for example ○ ◐ ● ⊗), coloured semantically, with the label kept in text colour.

## 6. Guardrails: where the style breaks the floor

| Risk | Rule |
| --- | --- |
| Low-contrast grey tiers | Linear's quaternary text measures about 3.5:1 in both themes, which fails AA. Use the quaternary tier for decoration only. Any meaningful text uses tertiary or above. Check muted text on hover, selected and pressed surfaces too. |
| Hairline-only boundaries | A 1.3:1 hairline is fine as a separator. Where a boundary is the only thing showing that a control exists (a checkbox, a radio, a bordered input with no label), it needs 3:1. |
| Density on touch | Switch to touch sizes on coarse pointers and narrow screens (44 pt or 48 dp hit areas). Rows grow to two lines, and the properties column becomes a disclosure. |
| Keyboard-first invisibility | Every action keeps a visible route. Shortcuts and the command menu only speed things up. |
| Dimmed navigation | Navigation labels still meet 4.5:1. Dimming means lower prominence, not illegibility. |
| Monochrome status | Show status by shape and label, as well as colour. |
| Dark-first assumption | Many work tools are used all day in bright offices. Design the light theme with equal care, or make it the default. |
| Clone sameness | Use the project's brand colour, type and voice. The profile is about structure. |
| Marketing effects | Glows, gradients and background blur belong, if anywhere, on marketing pages. The app stays flat. |

## 7. Sources

- The Linear Method: https://linear.app/method
- Linear README (principles): https://linear.app/readme
- How we redesigned the Linear UI (2024, LCH themes, contrast): https://linear.app/now/how-we-redesigned-the-linear-ui
- A design reset (2024): https://linear.app/now/a-design-reset
- Behind the latest design refresh (March 2026, calmer chrome): https://linear.app/now/behind-the-latest-design-refresh
- Invisible details (craft): https://linear.app/now/invisible-details
- Why is quality so rare (2025): https://linear.app/now/why-is-quality-so-rare
- Linear and Liquid Glass (mobile, legibility over refraction, 2025): https://linear.app/now/linear-liquid-glass
- The Linear Method: opinionated software (Figma blog): https://www.figma.com/blog/the-linear-method-opinionated-software/
- Karri Saarinen's 10 rules for crafting products (Figma blog): https://www.figma.com/blog/karri-saarinens-10-rules-for-crafting-products-that-stand-out/
- Secondary, a description of the trend: https://blog.logrocket.com/ux-design/linear-design/
