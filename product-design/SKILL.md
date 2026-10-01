---
name: product-design
description: Product design principles for building mobile and web app interfaces, synthesised from Apple's Human Interface Guidelines, Nielsen Norman Group usability research and Linear's product philosophy, with links to the originals. Use this skill whenever you design, build or change anything a person sees or reads in an app, including screens, components, layout, navigation, forms, lists and tables, dialogs, loading, empty and error states, onboarding, settings, notifications, button labels, error messages and other microcopy, colour, type, spacing, motion, dark mode and accessibility. Applies to iOS, Android and React Native or Expo apps, and to web apps and dashboards, even for a one-line UI tweak and even when the request doesn't mention design. Defers to a project's own DESIGN.md and VOICE.md, and includes an opt-in Linear-style profile for dense operator tools.
---

# Product design

This skill brings together three bodies of guidance for building interfaces people can use without having to think about the interface:

- **Nielsen Norman Group (NN/G)** explains *why* interfaces work, from decades of usability research. It applies to every platform.
- **Apple's Human Interface Guidelines (HIG)** show *how* to apply that on a device: hierarchy, platform conventions, touch, type, motion and accessibility.
- **Linear** adds a product philosophy: speed, opinionated defaults, calm surfaces and craft. That philosophy is part of the core principles. Linear's visual style is a separate, opt-in profile.

The three rarely disagree on principle. When they seem to, the cause is nearly always the input (touch or pointer) or the person (a daily expert or an occasional newcomer). The tensions table below resolves those cases.

## Before you design anything

1. **Read the project's own design documents first.** Look for `DESIGN.md`, `VOICE.md` or `voice.md`, `PRODUCT.md`, a design-system README, and UI rules in `CLAUDE.md` or `AGENTS.md`. Use their tokens, components, vocabulary and named rules. This skill supplies principles and fallbacks. The project supplies the system. Where a project has decided something, apply that decision. Don't argue for a default from this skill instead.
2. **Name the surface.** Answer four questions before writing markup, because the answers decide density, target size, navigation and tone:
   - **Platform:** iOS, Android, web, or more than one?
   - **Input:** touch, pointer, keyboard, or a mix?
   - **Person and context:** who is using it and how often (all day, weekly, once)? Where are they: at a desk, at a counter with a customer waiting, one-handed on the move, on poor signal?
   - **Job:** what is the one thing this screen must let them do, and what's the real-world unit of that job? (A family registering together, a team, a repeat booking.) Shape the flow around how people actually do it, not around one record at a time.
3. **Choose a profile only when asked to.** Apply a profile from `references/profiles/` only when the project's design documents name it or the user asks for it. Without one, the project's documents set the visual direction. If the project has none, build a small, deliberate identity from what you do know (the name, the domain, any brand colour). That means one accent used with confidence, a considered type scale, and the product's name in place. Neutral should mean restrained, not anonymous. A screen that could belong to any app has failed to tell people where they are.
4. **Reuse before you invent.** Use the platform's or design system's existing component, with its built-in keyboard, focus, dismissal, gestures and accessibility. A rebuilt control usually loses some of that behaviour, and users notice even when they can't say why.

## Precedence

When sources disagree, the higher item wins:

1. An explicit instruction from the user in this conversation.
2. The project's design and voice documents, including recorded owner decisions.
3. The selected profile.
4. Platform conventions: the HIG on Apple platforms, Android's system behaviour on Android, web standards in the browser.
5. The principles and defaults in this skill.

**The accessibility floor sits outside this order** (`references/accessibility.md`). No profile or default from this skill goes below it. If a project document records a deliberate decision below the floor, follow it. Mention the trade-off once, the first time you work in that area, and don't raise it again.

## Core principles

Each principle gives the rule, why it holds, and what it means in a build. Source tags: `[NN/G H1]` is Nielsen's first heuristic, `[HIG]` is Apple, `[Linear]` is Linear.

### 1. Content leads, and every element earns its place
`[NN/G H8] [HIG Simplicity] [Linear]`
People come for their data and tasks, not the interface. Every extra element competes with the ones that matter and weakens them.
- Make the most important information or action the most visually prominent. Use size, weight, position and contrast before colour.
- Remove anything that restates something already visible: a subtitle that repeats the heading, helper text that repeats the label, a card around content that needs no container.
- Reserve colour for meaning (action, selection, status). Decoration that carries no meaning is noise.
- Use whitespace and alignment for grouping before borders. Use borders before shadows.
- Restraint removes noise, not identity. Match expression to the surface. Tools people work in all day stay calm. Public, consumer and occasional-use surfaces (event pages, sign-up, onboarding) need warmth and character: real imagery, a confident headline, brand colour in larger areas.

### 2. Always show what's happening
`[NN/G H1] [HIG Familiarity]`
People trust a system that tells them its state, and they repeat actions, abandon them or worry when it doesn't.
- Acknowledge every press or click within 100 ms, through a pressed state, optimistic update or spinner. If something takes longer than about 1 s, show that it's working. If it takes longer than about 10 s, show determinate progress and let people carry on with something else.
- Keep a button's label while its action runs. Show a spinner inside it and block repeat presses.
- Never show an empty state while data is loading or after a load failed. "No items" must mean no items.
- Distinguish saved, pending, failed and offline states. Don't claim something was sent or saved before the server confirms it.
- Make the confirmation as weighty as the commitment. A booking, payment, registration or send gets a confirmation that names what, when and where, and what happens next, because the context that led to it may have scrolled away. A routine save can be a quiet indicator.

### 3. Speak the person's language
`[NN/G H2] [HIG Writing]`
An interface is a conversation. Internal vocabulary makes people translate, and translation is where mistakes happen.
- Use the words people use for their own work, never internal terms (tenant, entity, sync job, payload, error codes).
- Use one term for one concept everywhere: navigation, headings, buttons, emails and documents.
- Order things the way people think about them: by task and outcome, not by your data model.
- Read `references/voice-and-copy.md` before writing any visible text.

### 4. One primary action, and consistent actions
`[NN/G H4] [HIG Familiarity] [Jakob's law]`
People learn an interface once and expect it to keep its promises. They also bring expectations from every other app they use.
- Give each context one visually primary action. Make secondary actions quieter, and move rare ones into an overflow menu.
- Give the same action the same name, place and style everywhere. "New invoice" stays top right on every list.
- Make button labels verbs that name the outcome ("Save", "Send invoice", "Delete event"). Never use "OK", "Yes", "Submit" or "Confirm".

### 5. Prevent errors, then make recovery easy
`[NN/G H5] [NN/G H9] [HIG Agency]`
The best error message is the one never needed. The next best tells people exactly how to fix the problem and keeps their work.
- Prevent errors with constraints, sensible defaults, forgiving input formats (accept spaces in card numbers, and dates in several forms) and pickers instead of free text where values are fixed.
- Every commit is either reviewed before it happens or undoable after it. Prefer undo for reversible actions. Ask for confirmation for actions that are irreversible, cost money or affect other people. A clearly labelled one-tap commit ("Book strimmer for Sun 4 Oct") is fine when an immediate Undo follows. Being able to cancel later from another screen doesn't count as undo. Withdrawing, cancelling or resolving is a commit too.
- Undo in a toast is temporary, so keep a lasting way back as well (a history, Resolved, Archive or Trash view). An Undo that has expired must never act later.
- Show errors next to the cause, in plain words that name the fix. Keep everything the person entered.
- Don't let a failed operation look like success, or a timeout look like a decline.

### 6. Recognition over recall
`[NN/G H6] [HIG Familiarity]`
Remembering is harder than recognising. Every hidden option is one that some people never find.
- Keep labels visible. A placeholder is not a label, because it disappears as soon as someone types.
- Show recent items, sensible defaults and the current context (filters, which record, which step) so people don't have to remember them.
- Treat keyboard shortcuts, swipe actions, long-press and command menus as faster routes to visible actions, never as the only route.

### 7. Speed is a feature
`[Linear] [NN/G H7] [HIG Craft]`
Slowness is felt before anything else is seen, and every step adds friction. Fast software feels well made.
- Design for perceived speed: instant feedback, optimistic updates that reconcile with the server, skeletons that match the final layout, and no layout shift when data arrives.
- Remove steps with smart defaults, remembered choices and inline editing where the consequence is small.
- Offer accelerators for frequent users (shortcuts, bulk actions, a command menu on desktop) without making newcomers pay for them.
- Keep motion short (about 100 to 250 ms). Animation that makes people wait is a delay.

### 8. Opinionated defaults over settings
`[Linear] [HIG Purpose] [NN/G progressive disclosure]`
Each setting is a decision handed back to the user. Most people never change defaults, so the default is the product.
- When one answer suits most people, decide it. Add a setting only for real differences between people or organisations.
- Show the common path, and put advanced options one clear step away, behind a disclosure or "More options".
- Prefer one good way to do something over three configurable ones.

### 9. Follow conventions, and differ only when it pays
`[HIG Familiarity] [NN/G H4] [Jakob's law]`
People have already learned the platform from every other app. A custom pattern costs them something, so it must give back more than it takes.
- Keep platform behaviour: system back on Android, swipe-back and sheets on iOS, links that behave like links on the web (open in a new tab, copy the address).
- Behaviour follows the platform and visuals follow the brand. Use native date pickers and share sheets, styled to the brand where the platform allows.
- Keep the URL as the source of truth for web view state (filters, tabs, selected record) so it can be shared, reloaded and used with the back button.

### 10. Design every state
`[NN/G H1, H9] [HIG Craft]`
Most of a product's real life happens outside the ideal state with sample data. Undesigned states are where trust breaks.
- Design each of these: first use, loading, refreshing, empty, no results, partial data, error, offline, pending, success, permission denied, and very long or missing content.
- Test with zero, one and many items, the longest real names, and the smallest supported screen.
- `references/patterns.md` has the state-by-state requirements.

### 11. Respect people's control, attention and privacy
`[NN/G H3] [HIG Agency, Responsibility]`
People forgive a lot from software that respects them, and very little from software that traps or nags them.
- Always offer a clearly marked way out: Cancel, Back, Close or Undo. Never trap people in a flow.
- Ask for permissions (camera, location, notifications) when the feature needs them, after explaining why, never all at launch.
- Interrupt only for things that need action now. Notify only for what people would want to know.
- Never use dark patterns: no confirmshaming, no hidden costs, no pre-ticked consent, no cancellation that's harder than signing up.

### 12. Accessible by default
`[WCAG 2.2 AA] [HIG Flexibility]`
Accessibility fixes help everyone: bigger targets, clearer contrast and real labels make the product better for people in bright sunlight, in a hurry or using one hand.
- Meet the floor in `references/accessibility.md`: contrast, target size, text scaling, a visible focus, screen reader names, and never meaning through colour alone.
- Build it in from the start. Adding accessibility afterwards costs far more.

## Resolving the usual tensions

| Tension | Resolve it by |
| --- | --- |
| Density vs touch targets | Let the input decide. A pointer allows compact rows and controls (24 px minimum target). Touch needs 44 pt on iOS and 48 dp on Android. Pad the hit area when the visual is smaller. On the web, switch with `@media (pointer: coarse)`. |
| Keyboard-first vs discoverability | Shortcuts speed up actions that are already visible. Show the shortcut in menus and tooltips. |
| Minimal chrome vs affordance | Remove decoration, never signifiers. A control shows its purpose before hover, because touch has no hover. |
| Subtle palette vs contrast | The contrast floor wins. Check each muted grey on every surface it sits on, in both themes. |
| Platform consistency vs brand consistency | Behaviour follows the platform; visuals follow the brand. |
| Confirm vs undo | Undo for reversible actions. Confirm for irreversible ones, money, or anything that reaches other people. |
| Live validation vs interruption | NN/G says validate on blur, and Apple favours checking as people type. Show helpful guidance live (password rules ticking off, a username being available), but show errors only when a field loses focus or on submit. Once an error shows, re-check live so it clears as soon as it's fixed. |
| Disabled vs explained commit | NN/G and most product voice guides keep the commit button enabled and explain what's missing on press. Apple accepts disabling Next until required data is entered. Disable only on short native forms where what's missing is obvious, and otherwise keep it enabled and explain. |
| Brevity vs clarity | Clarity wins for consequential moments (payment, deletion, failure). Brevity wins for routine ones. |
| Expert efficiency vs newcomer clarity | Make the visible path clear for newcomers. Add accelerators for experts on top, without taking anything from the newcomer. |
| Restraint vs personality | Calm for working tools, warmth for public and occasional-use surfaces. Either way the product is recognisable: its name, its accent and its voice are present. |

## Defaults when the project is silent

Use these only where the project's documents don't decide.

- **Language:** British English, sentence case for everything (headings, buttons, labels, navigation). No em dashes in interface copy; use a full stop, comma or colon. Contractions are fine in sentences.
- **Formatting:** use locale formatters for dates, times, money and numbers, never hand-built strings. Write a date and time as "8 Sep, 14:32", and add the year only when it isn't the current year. Use tabular figures for numbers in columns.
- **Type:** the platform system font (SF Pro through `-apple-system` or `system-ui` on Apple platforms, Roboto on Android) unless the brand specifies one. Body text at least 16 px on the web (this also stops iOS Safari zooming into inputs) and 17 pt on iOS (the default Body style). Support Dynamic Type and browser zoom.
- **Spacing:** a 4 px base with an 8 px rhythm. Group related items closer together than unrelated ones.
- **Colour:** semantic tokens (text, muted text, surface, border, accent, success, warning, danger), with both light and dark themes designed. One accent colour.
- **Motion:** 100 to 250 ms with ease-out for entrances. Animate only to explain a change (where something came from or went).
- **Icons:** one family and one stroke weight. Add a text label wherever the icon's meaning isn't universal.

## Before you call it done

- [ ] The project's design and voice documents were followed, and existing tokens and components reused.
- [ ] Each context has one primary action, and every label is a verb naming its outcome.
- [ ] Every state is designed: loading, empty, no results, error, offline, pending, success. In a prototype, each one can be reached.
- [ ] Every commit is reviewed before or undoable after, and its confirmation names what was done. Nothing moves money or messages people without confirmation.
- [ ] Every visible control works. Placeholders are left out or marked as not built.
- [ ] Copy uses the person's words, contains no internal terms, says how to fix errors, and has no filler. Read every string together: no two contradict each other, money and numbers share one format, and plurals are right ("Both booked", not "All 2 booked").
- [ ] Touch targets, keyboard paths, focus order and screen reader names are in place.
- [ ] Contrast holds in light and dark themes. Text scales to 200% and the largest Dynamic Type size without clipping.
- [ ] The design works on the smallest supported phone, at 320 px wide on the web, and at in-between widths (around 768 and 1024 px), with long names and with zero, one and many items. No label clips.
- [ ] The product is recognisable: its name appears and its accent is visible.
- [ ] Nothing moves without a reason.
- [ ] Platform conventions still work: back, links, gestures, system sheets.

## Reference map

Read only what the task needs.

| File | Read it when |
| --- | --- |
| `references/heuristics.md` | You need the reasoning behind a decision: NN/G's ten heuristics, Apple's principles, Linear's philosophy and the usability laws. |
| `references/patterns.md` | You're building navigation, forms, lists and tables, dialogs, search and filters, onboarding, settings, notifications or AI features, or designing states. |
| `references/voice-and-copy.md` | You're writing any visible text: labels, buttons, errors, empty states, confirmations, toasts or emails. |
| `references/visual-design.md` | You're working on layout, spacing, type, colour, icons, motion or dark mode. |
| `references/mobile-touch.md` | You're building for iOS, Android, React Native or Expo, or any touch surface. |
| `references/web-desktop.md` | You're building for the browser or desktop, with pointer and keyboard. |
| `references/accessibility.md` | Every time, to check the floor. Read it in full for forms, custom controls, colour and moving content. |
| `references/profiles/linear.md` | Only when the project or user opts into the Linear-style profile. |
| `references/sources.md` | You need to go deeper or check a point against the original guidance. |

Related skills, where installed: `web-design-guidelines` for a code-level review of web interfaces, `dataviz` for charts, and `copywriting` for marketing pages, which persuade rather than inform.
