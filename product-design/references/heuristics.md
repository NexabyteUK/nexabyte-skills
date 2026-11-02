# Heuristics and principles: the reasoning layer

Use this file when you need the *why* behind a decision: to settle a disagreement, to explain a choice, or to check a design against established principles. `SKILL.md` holds the synthesis. This file holds the sources it was built from.

## Contents

1. How the three sources line up
2. Nielsen's 10 usability heuristics
3. Apple's design principles
4. Linear's product philosophy
5. Usability laws and concepts
6. Quick heuristic review

## 1. How the three sources line up

| Core principle (`SKILL.md`) | NN/G | Apple HIG | Linear |
| --- | --- | --- | --- |
| 1. Content leads, every element earns its place | H8 Aesthetic and minimalist design; visual hierarchy | Simplicity ("simplicity isn't minimalism"); Liquid Glass hierarchy, with controls floating above content | "Don't compete for attention you haven't earned"; "Structure should be felt not seen" |
| 2. Always show what's happening | H1 Visibility of system status; response-time limits | Familiarity (clear feedback); Feedback and Loading patterns | Speed: instant, optimistic updates |
| 3. Speak the person's language | H2 Match between system and real world; plain language | Writing; Inclusion | Plain nouns; no invented terminology |
| 4. One primary action, consistent actions | H4 Consistency and standards; Jakob's law | Familiarity ("things that look the same behave the same"); one or two prominent buttons per view | One consistent header pattern across all object types |
| 5. Prevent errors, make recovery easy | H5 Error prevention; H9 Recover from errors | Agency (cheap recovery, undo); alerts only for the unexpected | Quality bar and zero-bugs policy |
| 6. Recognition over recall | H6 Recognition rather than recall | Familiarity (known metaphors); labelled controls | Command menu as a safety net for shortcuts |
| 7. Speed is a feature | H7 Flexibility and efficiency; response times | Craft; brief, interruptible motion | "The fastest of its kind"; local-first |
| 8. Opinionated defaults over settings | Progressive disclosure | Purpose (a focused feature set); few settings with good defaults | "One really good way of doing things" |
| 9. Follow conventions | H4; Jakob's law | Familiarity; standard components | Native feel (arrow cursor, context menus) |
| 10. Design every state | H1, H9; empty-state guidance | Craft; Loading, Launching and Onboarding patterns | "Invisible details" are part of the spec |
| 11. Respect control, attention, privacy | H3 User control and freedom | Agency; Responsibility (privacy, permissions in context) | "Say no to busy work" |
| 12. Accessible by default | Accessibility research | Flexibility (accessibility from the start) | Contrast setting in themes |

The sources agree on nearly everything. Apparent conflicts come down to input (touch or pointer) and audience (daily expert or occasional newcomer). See the tensions table in `SKILL.md`.

## 2. Nielsen's 10 usability heuristics

Jakob Nielsen published these in 1994. NN/G refined the wording in 2020, and the heuristics themselves haven't changed. They're broad rules of thumb, not a checklist, and they apply to every platform.

1. **Visibility of system status.** Keep people informed about what's going on, with timely feedback.
   - Every action gets immediate visible feedback: pressed state, progress, result.
   - Show where people are (the current navigation item, step 2 of 3) and what state things are in.
2. **Match between the system and the real world.** Use people's words, concepts and conventions, not internal jargon.
   - Label things by people's tasks, not by your database or org chart.
   - Follow real-world order and formats (addresses, dates, currency as people expect them).
3. **User control and freedom.** People make mistakes and need a clearly marked emergency exit.
   - Every flow and overlay has a visible Cancel, Close or Back.
   - Support undo, and redo where actions come in quick succession.
4. **Consistency and standards.** Don't make people wonder whether different words or actions mean the same thing. Follow platform and industry conventions.
   - The same word, icon and position mean the same thing everywhere.
   - Don't reinvent standard controls.
5. **Error prevention.** Better than good error messages is a design that prevents problems.
   - Use constraints, good defaults and pickers for bounded values. Disable or hide impossible options.
   - Confirm only actions that are costly and can't be undone.
6. **Recognition rather than recall.** Keep options and information visible. Don't make people remember things from one screen to the next.
   - Show recent items, current selections and the context of the task.
   - Avoid features that exist only as hidden gestures or memorised commands.
7. **Flexibility and efficiency of use.** Offer accelerators that newcomers can ignore and experts can use.
   - Keyboard shortcuts, bulk actions, saved views, remembered choices.
   - Personalisation only where it genuinely helps.
8. **Aesthetic and minimalist design.** Every extra unit of information competes with the relevant ones.
   - Cut rarely needed content, or move it behind progressive disclosure.
   - Make the primary content and action stand out.
9. **Help people recognise, diagnose and recover from errors.** Use plain language with no codes, state the exact problem, and suggest a fix.
   - Put the error next to its cause, and keep what people entered.
10. **Help and documentation.** Ideally the interface needs no explanation. When it does, help should be easy to search, in context and focused on the task.
    - Use inline help at the point of need, written as concrete steps.

## 3. Apple's design principles

Apple's HIG reintroduced eight design principles in June 2026 (WWDC26):

- **Purpose.** Build what people truly value and keep the feature set focused. Don't recreate what the system already does well.
- **Agency.** Stay out of the way. Don't lock people into flows or modes, make guided flows easy to skip, and make recovering from mistakes cheap (undo).
- **Responsibility.** Be open about what you collect and why, ask permission with a reason, collect the minimum, and plan for misuse. For AI features, add previews, confirmations and clear disclaimers.
- **Familiarity.** Use known metaphors. Things that look the same behave the same. Give clear feedback through system patterns.
- **Flexibility.** Design for everyone, with accessibility as a priority from the start. Keep controls in predictable places across sizes, support voice, touch and keyboard, and give each platform the same care.
- **Simplicity.** Simplicity isn't minimalism. Include what's necessary, word it concisely, and set hierarchy through order, spacing and contrast.
- **Craft.** Care about detail, iterate, and keep the product current.
- **Delight.** Choose the feeling you want to create. Delight isn't decoration, and it never gets in the way of the task.

Underneath sits the 2025 Liquid Glass visual system (iOS 26 and the matching releases), framed as **hierarchy** (controls float above and elevate content), **harmony** (concentric shapes echo the hardware) and **consistency** (conventions adapt across window sizes). The older clarity, deference and depth no longer appear in the HIG, though their substance (legible text, content first, layers conveyed through translucency and motion) carries on.

In practice, Apple's guidance for app makers comes down to:

- Use standard components and system behaviours, so the app inherits accessibility, Dynamic Type, dark mode, localisation and future platform changes.
- Put content first. Controls are concise, grouped and reachable.
- Adapt to every context: size class, orientation, text size, appearance, input method.
- Treat accessibility, inclusion and privacy as foundations, not features.
- Write plainly, directly and consistently.

`mobile-touch.md` has Apple's concrete guidance for touch platforms.

## 4. Linear's product philosophy

Linear's principles transfer beyond issue tracking. These describe how the product is built, separate from its visual style (which is the opt-in profile).

- **Speed is a feature.** Interactions feel instant: local-first data, optimistic updates, no spinners for local edits. Small delays add up across hundreds of daily actions and break flow.
- **Opinionated software.** Aim for one really good way of doing things. Be firm about the building blocks, and flexible only at higher levels. Avoid invented terminology. You shouldn't need a handbook to start.
- **Simple first, then powerful.** Easy to start with, and deeper the more it's used. Depth lives in shortcuts, the command menu and display options, not up front.
- **Keyboard-first, with a safety net.** Frequent actions have single-key shortcuts, and a command menu reaches every action, so nobody needs to memorise everything.
- **Content leads, chrome recedes.** Navigation sits quieter than the work. Structure is felt rather than seen.
- **Craft and a quality bar.** Quality is the differentiator. The bar is set by leadership, bugs are fixed quickly, and incomplete work isn't shipped externally. Invisible details (a submenu that tolerates a diagonal cursor path, a focus state, an edge case) are part of the spec. Quality isn't perfection: ship once the bar is met, then iterate.
- **Build for the person doing the work.** Optimise the main working loop before reports and dashboards. Don't add required fields that exist only for administrators.
- **Scope down and keep momentum.** Build the smallest coherent slice to full polish, rather than a broad, rough surface.
- **Design is search.** Explore several directions before committing. Judge in the running product, not a static mockup. A mockup is a reference, never the deliverable.
- **Plain, direct writing.** Short verb-and-noun labels. Messages say what happened in a few words. No marketing tone inside the product.

## 5. Usability laws and concepts

| Concept | What it says | Design rule |
| --- | --- | --- |
| Response-time limits | 0.1 s feels instant, 1 s keeps the train of thought, 10 s is the limit of attention | Feedback within 0.1 s. Indicate work after about 1 s. Show percent done, a description and Cancel beyond 10 s. |
| Fitts's law | Bigger, closer targets are faster to hit | Make primary targets large. Put the commit button by the last field. Space targets apart. Labels next to icons enlarge the target. |
| Hick's law | More choices slow decisions | Don't just remove options. Group, categorise and order them, and lead with sensible defaults. |
| Jakob's law | People spend most of their time in other products | Use established patterns unless a new one is clearly better. |
| Recognition over recall | Recognising is easier than remembering | Visible options, labels, history and recent items. |
| Progressive disclosure | Show the important few first, and the specialist options on request | No more than two levels. Label what the disclosure reveals. |
| Aesthetic-usability effect | Attractive interfaces are perceived as easier and get more forgiveness | Polish helps, but it won't save a broken flow. Watch what people do, not what they say about the visuals. |
| Mental models | People act on what they believe the system does | Change the design to fit the model before trying to teach a new one. |
| Information scent | People predict what's behind a link from its label | Specific link and button text. Never mislead. |
| Scanning patterns | People scan in F-shaped, layer-cake and spotted patterns | Front-load headings and lines. Use meaningful subheads, short paragraphs and bullets. |
| Banner blindness | People skip things that look like ads or sit where ads usually go | Don't style important content as promotion. Don't put critical controls in a right rail. |
| Visual hierarchy | Built from contrast, scale and grouping | About three type sizes and two or three contrast levels per view. Check with the squint test. |
| Proximity (Gestalt) | Things close together read as a group, overriding colour or shape | Keep labels tight to their fields, and leave larger gaps between groups. Re-check at every breakpoint. |
| Change blindness | People miss changes away from where they're looking | Change things near the person's focus. Draw attention with subtle motion or emphasis, especially for errors and counts. |

## 6. Quick heuristic review

Use this to review any screen. It's a fast way to catch problems before people do.

1. Can I tell what state everything is in, right now? (H1)
2. Is every word one the person would use? (H2)
3. Can I get out of every flow, and undo what I just did? (H3)
4. Do the same things look and behave the same everywhere, and like the platform? (H4)
5. What mistakes does this invite, and could the design prevent them? (H5)
6. Am I asking the person to remember anything? (H6)
7. Is there a faster route for someone who does this all day? (H7)
8. What could I remove? (H8)
9. When this fails, does the message say how to fix it, next to the problem? (H9)
10. Would a newcomer need help here, and is it there at the point of need? (H10)
