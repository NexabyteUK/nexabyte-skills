# Interaction patterns

Cross-platform guidance for recurring parts of a product. Platform-specific details are in `mobile-touch.md` and `web-desktop.md`, and the words are in `voice-and-copy.md`.

## Contents

1. Designing every state
2. Navigation
3. Forms and input
4. Lists, search and filters
5. Dialogs, sheets, confirmation and undo
6. Feedback: progress, toasts, banners, notifications
7. Onboarding and first use
8. Settings
9. Permissions and privacy
10. Money, sending and other consequential actions
11. Offline, sync and conflicts
12. AI features

## 1. Designing every state

| State | What it needs |
| --- | --- |
| First use | Orientation and one clear first action. Don't show an empty dashboard of zeros. |
| Loading | A stable layout. Nothing for under about 1 s. A skeleton matching the real layout for full views, or a spinner for a single module. Percent done, a description and Cancel beyond about 10 s. Never a false "empty". |
| Refreshing | Keep the existing content visible with a subtle updating indicator. Ignore stale responses that arrive late. |
| Empty | One sentence saying what will appear, plus one useful next step if it isn't already on the page. |
| No results | Say nothing matched and offer a way to reset (Clear filters, check spelling). |
| Partial | Show what loaded, mark what didn't, and offer a retry for the missing part. |
| Error | Plain language, what happened, what to do, and a retry or recovery path. Keep the person's input. |
| Offline | Say what still works, queue what can be queued, and be honest about what hasn't been sent. |
| Pending | Acknowledge, block duplicate submissions, keep the input, and show progress for slow operations. |
| Success | Update the content itself, and toast only when the result isn't visible. For a commitment (a booking, payment, registration or send), show what, when and where, and what happens next. |
| Permission denied | Say the person can't do this and, where useful, who can help. Hide actions people can never use. Explain disabled ones. |
| Stale | Keep the last known values, mark them out of date with the time, and hide advice derived from them. |
| Extreme content | Long names, missing values, zero, one and thousands of items, large text sizes, right-to-left languages if supported. |

**Prototypes.** Make every state reachable (a small state switcher, or URL parameters such as `?state=empty`), so reviewers can see them. Don't leave controls that do nothing: leave them out, or mark them as not built yet. In a web prototype of a mobile app, make browser Back and Escape behave like the platform's back: one layer per press, closing the innermost sheet or dialog first, then returning to the previous screen.

## 2. Navigation

- **Keep top-level destinations visible.** NN/G finds that hidden navigation (a hamburger menu) reduces discovery on both desktop and mobile. Use a tab bar (iOS, Android) or a sidebar (desktop web) with about 3 to 5 top-level items on phones. If you must hide navigation, label the menu button "Menu" and keep it high-contrast.
- **Organise by the person's tasks** and mental model, not by your internal structure.
- **Show location:** the current item highlighted, a heading matching it, and a back route that returns to the previous place and scroll position.
- **Keep hierarchy shallow.** Two or three levels is plenty. Deeper structures need search.
- **Tabs** switch between views of the same thing. Keep them in a single row directly above their content, with 1 to 2 word labels, the selected tab marked by more than one cue, and the most-used tab selected by default. Don't use tabs when people need to compare content across them.
- **Focused flows** (checkout, creating a record, onboarding) can hide global navigation, but always keep a clear exit.
- **Search** is navigation for large content sets. Make it a visible box, not just an icon, wide enough for typical queries.

## 3. Forms and input

NN/G's Eliminate, Automate, Simplify framework is a good order of attack:

1. **Eliminate:** don't ask for anything you don't need now. Postpone optional questions, and use conditional logic so people only see what applies. Don't eliminate what the operation must collect: legal and safety consents, acceptance of terms, guardian consent for children, and access needs that change the service.
2. **Automate:** prefill what you know, infer what you can (town from postcode), and use the camera, location, contacts and autofill.
3. **Simplify** what remains: honest defaults, forgiving formats and the right control.

Then:

- **Labels above fields** in a single column, kept visible while typing. Placeholders aren't labels.
- **Required and optional:** mark required fields with an asterisk explained at the top (except on login forms), and label genuinely optional fields "(optional)".
- **Pick the right control:**

  | Options | Control |
  | --- | --- |
  | 2 to about 5 | Radio buttons or a segmented control, all visible |
  | About 5 to 10 | A dropdown or select |
  | 15 or more | A searchable combobox |
  | A known value (birth year, card number, postcode) | Typed input, with format help |
  | On or off, applying immediately | A switch |
  | A choice submitted with the form | A checkbox |

- **Dates:** spell out the month when displaying ("9 Aug 2026"). Use a calendar picker only for dates within about a year. Let people type distant dates like birth dates, as three fields or one forgiving field. Accept any separator.
- **Keyboards and autofill:** set input types and autocomplete hints. Turn off autocorrect and auto-capitalisation for names, emails, usernames and codes.
- **Validation:** check on blur or on submit, never while someone is still typing a plausible value. After a failed submit, show each error next to its field and move focus to the first problem. On long forms, focus can go instead to an error summary at the top that links to each field (the GOV.UK pattern). The summary never replaces inline errors. Don't put errors in modals or tooltips.
- **Commit:** one primary button at the end, labelled with the outcome. No Reset or Clear buttons. Keep the commit enabled and explain on press what's missing.
- **Long forms:** split into steps only when the steps are genuinely independent. Show progress, allow going back, and keep the entries.
- **Never lose input** on an error, timeout, navigation away (warn first) or app backgrounding (save a draft).

## 4. Lists, search and filters

- **Rows** show the identifier people recognise first (a name, not an ID number), then the most decision-relevant attributes, with secondary details quieter.
- **The whole row opens the item.** Frequent actions are available on the row (swipe actions on touch, hover or visible buttons on desktop), and the full set is in an overflow menu.
- **Sort** in the most useful order by default (most recent, most urgent) and say what the order is.
- **Filter and view controls show their label visibly** ("Site: All sites", "Status: Open"), not just a value, so people can tell what each one controls.
- **Filters:**
  - Use *batch* filters with an Apply button when people have several criteria in mind, and on mobile where every update is costly.
  - Use *interactive* filters (results update on each change) for exploring, with counts per option.
  - Always show the active filters and an obvious way to clear them.
- **Search:** forgiving (typos, partial matches), scoped clearly ("Search invoices"), with recent searches, and results that highlight the match.
- **Bulk actions:** select, then act, with the selection count visible and a clear way to deselect.
- **Large lists:** paginate or "Load more" for lists people return to, use infinite scroll for browsing feeds, and always show the total.

## 5. Dialogs, sheets, confirmation and undo

- **Use a modal only** to prevent losing work or an irreversible mistake, or to collect something needed to continue a flow the person started. Don't use modals for promotion, newsletters or tips, or for anything that hides information the decision needs.
- **Use non-modal panels** (side panels, drawers, inspectors) for editing details while keeping context.
- **Sheets on mobile:** bring up a focused task or options from the bottom. Support swipe-down and the back button to dismiss, include a visible close button, keep the content brief, and never stack sheets on sheets.
- **Every commit is reviewed before or undoable after.** A single tap that takes a shared resource (booking the only rotavator) or resolves someone's issue needs one or the other.
- **Undo beats confirmation** for anything reversible. Act immediately, then offer Undo in the toast. Toasts disappear, so keep a lasting route back (Trash, Archive, Resolved, history) too. When the toast goes, its Undo goes with it, and must not act later.
- **Confirm** irreversible actions, money, and anything reaching other people. Name the object and the consequence, label buttons with the action, and avoid a destructive default (don't make the destructive button respond to Enter). For catastrophic actions (deleting an organisation), ask people to type the name.
- **Dismissing a dialog that holds unsaved input** asks first, or keeps a draft.

## 6. Feedback: progress, toasts, banners, notifications

Match how intrusive the feedback is to how urgent and important it is:

| Feedback | Use for | Never use for |
| --- | --- | --- |
| Inline state (button spinner, row status, a "Saved" indicator) | Results of the current action, where the person is looking | Information needed elsewhere |
| Toast or snackbar | Passive, low-stakes confirmation that disappears on its own, optionally with Undo | Errors that need action, or anything people must read |
| Inline notice or banner | Persistent conditions affecting this content (offline, stale data, a limit reached) | Promotion |
| Modal alert | Blocking problems or decisions that must happen now | Routine success, tips |
| Push notification | Events people asked to hear about, away from the app | Marketing on transactional channels, things visible in the app anyway |

- **Put feedback where the person is looking.** Changes elsewhere on the screen get missed (change blindness).
- **Feedback always matches the current state.** When the state moves on (a queued booking sends, a retry succeeds), replace or dismiss the earlier message. Never leave a toast saying "Waiting for signal" after the booking went through.
- **Badges and counts** are for things needing action, and clear when the person deals with them. Don't badge-farm.
- **Announce** status changes to screen readers without moving focus.

## 7. Onboarding and first use

- **Skip upfront tutorials.** People skip them, forget them, and they don't improve performance (NN/G). Teach in context, at the moment a feature is needed ("pull" help rather than "push").
- **Let people start the real task at once.** Ask only what's needed to begin, with sensible defaults for the rest. Postpone account details, preferences and permissions until they're needed.
- **Use empty states as onboarding:** each one explains what goes there and offers the first action.
- **Sample data or templates** help where an empty canvas is daunting. Label them clearly and make them easy to remove.
- **If you must use a walkthrough:** few cards, one idea each, an obvious Skip, and never for standard conventions.

**Human help.** Where the audience or the stakes call for it (older or less confident people, money, safety, access), give a route to a person: who to contact and how. Keep it in the same place on every screen (WCAG 3.2.6).

## 8. Settings

- **Every setting is a decision handed back to people.** Prefer a good default. Add a setting only for genuine differences between people or organisations.
- **Group settings by what people are trying to do,** not by implementation. Write a short explanation only where the effect isn't obvious from the label.
- **Apply changes immediately** where they're safe and reversible (switches, selections), with a quiet confirmation. Use an explicit Save only for related values that must change together, or for consequential changes.
- **Show the current value** in the list, so people don't have to open each setting to see it.
- **Keep dangerous settings separate** (delete account, leave organisation), at the end, clearly labelled, with confirmation.

## 9. Permissions and privacy

- **Ask in context,** when the person tries to use the feature that needs it, after a one-line explanation of why and what they get. Never ask for everything at launch.
- **Respect a refusal.** The rest of the app keeps working, and the feature explains how to enable it later, linking to system settings.
- **Ask for the least you need** (approximate location, selected photos, while-in-use).
- **Be explicit about data:** say what's collected and why, in plain words, where people make the choice. Never pre-tick consent.

## 10. Money, sending and other consequential actions

- **State the exact amount, recipient and timing** before commit: "Pay £24.00 to Riverside Hall".
- **Confirm before** sending to customers, charging, refunding or anything that can't be recalled. After it's done, report success only once the server has confirmed it.
- **Prevent duplicates:** block repeat presses while pending, and make server operations idempotent.
- **Be honest about uncertainty.** A timeout isn't a decline. If the result is unknown, say so and say where to check, rather than guessing.
- **Keep a record** people can see: what happened, when and by whom.

## 11. Offline, sync and conflicts

- **Design for poor connections** where they're likely (mobile, events, basements, rural sites). Say what works offline, and queue what can be queued.
- **Distinguish "saved on this device" from "synced"** in the interface, and never claim a queued action has been sent.
- **Retry automatically** where safe, with a manual "Try again" as well.
- **On conflict,** keep the person's work, show what changed elsewhere, and offer an explicit choice. Never merge silently or discard work.

## 12. AI features

NN/G has published extensive guidance on AI interfaces since 2024. The essentials:

- **Start from a problem people have, not from "add AI".** Chat is often the wrong interface. AI frequently adds the most value when it's invisible (suggesting, summarising, filling in). "Powered by AI" isn't a benefit.
- **Narrow scope beats broad scope.** Say clearly what the feature can and can't do, and decline off-topic requests gracefully.
- **Reduce the blank-prompt problem:** suggested prompts, visible prompt controls (with text labels, not just icons), and buttons or choices generated in the conversation instead of asking people to type.
- **Label AI features in words.** People don't reliably read the sparkle icon as "AI".
- **Answer first.** AI output follows web-writing rules: lead with the answer, short paragraphs, plain language, no filler ("Great question!"). Say plainly when it can't help.
- **Show sources next to the claims they support,** with meaningful labels and links. Put specific, actionable caveats near the input, not in a footer. In high-stakes areas, show confidence in context.
- **Avoid presenting step-by-step "reasoning" as an explanation** of how a result was produced (NN/G, Dec 2025). It's often not faithful to how the model actually worked. Avoid human-like first-person framing.
- **Keep people in control:** easy to edit, regenerate, undo or discard AI output. Never apply consequential AI changes without review. Don't auto-scroll while a response streams.
- **Disclose AI use** appropriately to the context and audience.
- **Accessible, semantic interfaces are also usable by software agents.** Descriptive labels, real buttons and consistent patterns serve screen readers and AI agents alike.
