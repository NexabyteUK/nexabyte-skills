# Web and desktop

Guidance for products used in a browser or on a desktop, with a pointer and keyboard as well as touch. Read `mobile-touch.md` as well when the same web app must work on phones.

## Contents

1. Responsive layout
2. Input: pointer, hover, touch and keyboard
3. Navigation, links and URLs
4. Keyboard and focus
5. Forms
6. Lists, tables and data-dense screens
7. Dashboards
8. Overlays: dialogs, drawers, popovers, menus
9. Performance is part of the design
10. Browser details

## 1. Responsive layout

- **Design narrow first,** then add columns as space allows. Choose breakpoints where the content breaks, not at named devices. Everything works at 320 CSS px wide with no horizontal scrolling of the page.
- **Use container queries for components** that appear in places of different widths (a card in a sidebar and in a main column).
- **Limit reading width** to about 60 to 75 characters a line. Wide screens get more columns or more whitespace, not longer lines.
- **App frame:** a sidebar for navigation on wide screens. It collapses to a top bar with a menu button, or a bottom tab bar for a few top-level sections, on phones. Hiding all navigation behind a hamburger menu on desktop hurts discoverability, as NN/G has measured repeatedly. Keep top-level destinations visible where there's room.
- **Stack before you shrink.** At narrow widths, put side-by-side fields and panels in a single column before making anything smaller.
- **Use the width, and check the widths in between.** Don't leave a phone-width column floating in a desktop window. Put supporting content beside the main column, or a sticky summary beside a form. Check around 768, 1024 and 1280 px as well as phone and full desktop. Layouts often collapse to one column too early, or clip labels, in between.
- **Tables on narrow screens:** let the table scroll horizontally inside its own container with a sticky first column, or switch to a list of two-line rows. Never let a table make the whole page scroll sideways.

## 2. Input: pointer, hover, touch and keyboard

- **Hover is an enhancement, never a requirement.** Touch screens have no hover. Anything revealed on hover (row actions, previews) must also be reachable by focus, tap or an overflow menu. Use `@media (hover: hover)` for hover-only styling.
- **Size targets by pointer type:** at least 24 × 24 px for fine pointers, and 44 × 44 px for coarse pointers (`@media (pointer: coarse)`). Many web apps run on laptops with touch screens, so don't assume a mouse.
- **Signal what can be clicked:** links look like links (underlined, or clearly styled as navigation), and buttons look like buttons. Text that doesn't act doesn't look like it does.
- **Cursor:** use the pointer cursor for links. In dense app interfaces, some products keep the arrow cursor on buttons for a native feel. Follow the project. Use the I-beam in text fields and the grab cursor for draggable items.
- **Text selection:** don't block selecting or copying text, IDs, amounts or addresses. People copy them all the time.

## 3. Navigation, links and URLs

- **Navigate with real links** (`<a href>`) so Cmd/Ctrl-click, middle-click, "Open in new tab", "Copy link" and the status-bar preview all work. Use buttons for actions that don't navigate.
- **The URL holds the view state:** the selected tab, filters, sort order, search query, page and open record. People share, bookmark and reload these, and expect the back button to undo navigation. Don't push history entries for every keystroke in a search box. Replace the state instead.
- **The back button returns to where people were,** including their scroll position and selection in a list.
- **Show where people are:** highlight the current navigation item, and give the page a heading that matches it. Use breadcrumbs only where there's a real hierarchy deeper than one level.
- **Unknown addresses** show a helpful page inside the app frame, with navigation intact and a route onward.
- **Open external links in the same tab by default.** Use a new tab only when leaving would lose work, and say so ("opens in a new tab").

## 4. Keyboard and focus

- **Make everything work by keyboard:** Tab and Shift+Tab move between controls. Enter and Space activate. Arrow keys move inside menus, tabs, listboxes, grids and radio groups. Escape closes the topmost overlay.
- **Keep focus visible** with `:focus-visible` (at least 3:1 contrast) and never hidden behind sticky headers.
- **Manage focus deliberately:** move it into a dialog when it opens, return it to the trigger on close, and move it to the first error when submission fails.
- **Shortcuts accelerate visible actions.** A command menu (Cmd/Ctrl+K) that lists every action is the most discoverable form. Single-key shortcuts must not fire inside text fields, and must not clash with browser, OS or screen reader shortcuts (WCAG 2.1.4). Show shortcuts in menus and tooltips.
- **Enter submits single-line forms.** Cmd/Ctrl+Enter submits from a multi-line text area.

## 5. Forms

- **Use a single column,** with labels above fields and fields grouped under short headings. Size each field to its expected input (a postcode field is short). `patterns.md` covers choosing controls, dates and required fields.
- **Use native inputs with the right type,** `inputmode` and `autocomplete`, so browsers autofill and phones show the right keyboard. Never block paste, especially into password and one-time-code fields.
- **Ask only for what's needed now.** Each extra field costs completions. Explain why you need anything unexpected (a phone number, a date of birth).
- **Validate when a field loses focus, or on submit.** On submit, focus the first invalid field. Long forms can add a summary at the top linking to each problem. Keep everything entered.
- **Put the commit button at the end of the form,** aligned with the fields, labelled with the outcome ("Create account", "Pay £24.00"). If the form is incomplete, keep the button enabled and explain what's missing on press. A disabled button that doesn't say why leaves people stuck.
- **Protect drafts:** warn before leaving with unsaved changes, and where it's cheap, keep a local draft so a reload doesn't lose work.
- **Long or multi-step forms** show progress ("Step 2 of 3") and let people go back without losing entries.

## 6. Lists, tables and data-dense screens

- **Lists for scanning items, tables for comparing values.** Many "tables" are really lists that don't need column headings.
- **Number columns:** right-align them, use tabular figures, and keep units consistent. Text columns are left-aligned. Headers align with their data.
- **Make headers sticky** on long tables. Sortable columns show their current sort, and expose it with `aria-sort`.
- **Row actions:** make the whole row a link to its detail (a real link, so modified clicks work), with nested controls that act independently. Put frequent actions in view or on hover, with keyboard and overflow access. Rare actions go in the overflow menu.
- **Selection and bulk actions:** a checkbox per row, Shift-click for ranges, and a bulk action bar that names the count ("3 selected").
- **Paging:** use pagination or "Load more" for task lists people return to and need to find their place in. Use infinite scroll only for feeds people browse. Always show the total count of matches.
- **Filters:** show active filters as removable chips, give "Clear filters" a fixed place, and keep the count of matching items visible. Separate *filtering* (which items) from *display* (grouping, sort, columns).
- **Density:** offer compact and comfortable densities only if your users genuinely differ. Otherwise pick one that suits the main user.

## 7. Dashboards

A dashboard answers "what needs my attention, and is everything OK?" before it answers "what happened?"

- **Lead with exceptions and actions:** items needing attention, failures, things due today. Comfort metrics come second. Rank attention items by consequence, not by type: money owed and customers affected first, then things that stop work (an offline till), then housekeeping (low stock). Give each row its most likely action in place.
- **Give every metric context:** its period, a comparison (against the previous period or a target) and, where it matters, a trend. A number without context can't be acted on.
- **Group metrics by the question they answer,** not by data source. Keep the first screen to the handful of things that matter, with depth reached by drilling down.
- **Make every number and item lead somewhere:** clicking a metric opens the filtered list behind it, and clicking an item opens its detail (a side panel works well), so people can act with context.
- **Use the first screen at desktop width.** Put the attention list beside the key comparison, so the first screen answers both "what needs me?" and "are we OK?". Don't stack everything in one long column.
- **Show freshness:** "Updated 14:32", and what's still loading. Mark stale figures as stale rather than showing them as current.
- **Charts:** follow the `dataviz` skill if installed. Prefer bars (length) and lines (position), which people read accurately at a glance. Avoid pie and donut charts, gauges, treemaps and 3D, and don't use colour to show magnitude. Label values directly rather than relying on a legend.

## 8. Overlays: dialogs, drawers, popovers, menus

- **Modal dialog:** for a short, focused task or a decision that must be made before continuing. Don't use it for content people need to compare against the page behind it. Never stack one modal on another.
- **Drawer or side panel (non-modal):** for detail or editing while keeping the list in view.
- **Popover:** for small, contextual controls (a date picker, a property selector) that close on outside click or Escape.
- **Menu:** for actions on an object. A right-click context menu mirrors the overflow menu, and never holds actions available nowhere else.
- **Use the platform `<dialog>` element or the component library's dialog,** with focus moved in and returned, Escape to close, background scroll locked and content behind marked inert.
- **Never lose input on accidental dismissal:** a dialog with unsaved input asks before closing on outside click or Escape, or keeps the draft.

## 9. Performance is part of the design

- **Core Web Vitals targets:** Largest Contentful Paint under 2.5 s, Interaction to Next Paint under 200 ms, Cumulative Layout Shift under 0.1.
- **Reserve space** for images, embeds, ads and late-loading content so nothing jumps. Give images their dimensions.
- **Delay skeletons by about 150 to 300 ms** so quick loads don't flash a placeholder. Once shown, keep a skeleton visible long enough not to flicker.
- **Use optimistic updates** for actions that almost always succeed, and roll back visibly if they fail.
- **Load fonts without invisible text** (`font-display: swap`, with fallback metrics adjusted to reduce shift).

## 10. Browser details

- **Page titles** name the page, then the product ("Invoices · Acme"). Include the record for detail pages.
- **Theme:** respect `prefers-color-scheme`, offer System, Light and Dark where people would want to choose, and set `color-scheme` so form controls and scrollbars match.
- **Printing and exporting:** documents people print (invoices, receipts, reports) get print styles: no navigation, black on white, page breaks that don't split rows.
- **Favicon and app icon,** plus `theme-color`, for a finished feel in tabs and on home screens.
