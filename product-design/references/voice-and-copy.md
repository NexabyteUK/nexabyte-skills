# Voice and copy

Every word in an interface is part of the design. Most copy problems come from writing that describes the system instead of helping the person, or that explains things the layout already shows.

## Contents

1. Voice and tone
2. How people read screens
3. Build each message for its purpose
4. Buttons and actions
5. Errors
6. Confirmations
7. Success, progress and feedback
8. Empty states
9. Help text and tooltips
10. Mechanics: case, punctuation, numbers, dates
11. Notifications and email
12. Copy review

## 1. Voice and tone

**Voice** is the product's personality and stays constant. **Tone** is how that voice adapts to the moment. NN/G describes tone on four dimensions: funny to serious, formal to casual, respectful to irreverent, and enthusiastic to matter-of-fact. Most product interfaces sit towards serious, fairly casual, respectful and matter-of-fact.

Default product voice, when the project has none: **a capable colleague**. That means:

| Quality | In the copy |
| --- | --- |
| Clear | Familiar words. The same term for the same thing everywhere. |
| Calm | Facts without drama, jokes or forced enthusiasm. Serious consequences stated plainly. |
| Practical | Useful information first. The next action named when there is one. Stop when nothing more is needed. |
| Considerate | Explain anything unfamiliar or consequential. No blame, no condescension, no assumptions about how people feel. |

Adapt the tone and depth, but keep the vocabulary consistent:

| Context | Tone and depth |
| --- | --- |
| Routine, frequent tasks | Brief and direct. Current state and next action scannable at a glance. |
| Setup and configuration | Measured and explanatory. Give the reason or consequence needed to choose. |
| Onboarding and unfamiliar tasks | Welcoming because it's useful. Orient people, explain the requirement and the next step. No promotion. |
| Failure, money, uncertain results, destructive actions | Explicit and considerate. State the consequence and the recovery path, even if that takes more words. |
| Email and documents | State the purpose straight away. Include enough context for someone reading away from the app. |

Address people as "you" (never "the user"). In system messages, describe the situation rather than the company ("Unable to load bookings" rather than "We're having trouble…"), unless the project's voice deliberately uses "we". Use possessives sparingly ("Bookings", not "Your bookings") where the owner is obvious. Prefer device-neutral verbs ("select", "choose") or the right one for the input ("tap" on touch, "click" on pointer).

Things the voice avoids everywhere: celebration ("You're all set! 🎉"), "Oops", "Whoops", "simply", "just", "easy", "Don't worry", humour about errors, personifying the software ("I'm thinking…"), marketing claims inside the product, and filler reassurance.

## 2. How people read screens

People scan rather than read. NN/G's eye-tracking studies show them reading the start of headings and lines and skipping most body text (the F-pattern and layer-cake patterns).

- **Front-load.** Put the distinguishing words first in headings, labels, list items, menu items and sentences. Write "Invoices overdue", not "There are some invoices that are overdue".
- **Use plain language.** Use short sentences with one idea each, common words and active voice. Even experts prefer plain language because it's faster to read. Explain an unavoidable technical term the first time it matters.
- **Every line earns its place.** If a sentence restates the heading, the button or the layout, delete it. Deleting is usually better than shortening.
- **Don't describe the interface.** "Use the filters below to narrow your results" tells people what they can already see.
- **Don't pre-explain sections.** A heading followed by a sub-line that summarises the content underneath it is noise.

## 3. Build each message for its purpose

Work out who's reading, what triggered the message, what's known for certain, and what they can do next. Use only the parts the person needs. A title names the subject or problem. A body adds a consequence, constraint or recovery step. An action names its outcome. Never say the same thing in all three.

| Purpose | Construction | Example |
| --- | --- | --- |
| Navigation, headings | Name the destination or content | "Payments", "Sales summary" |
| Field label | Name the value | "Email address", "PIN length" |
| Button | Verb, plus the object where needed | "Archive product", "Send" |
| Help text | Define the unfamiliar thing, then its behaviour, then an instruction if needed | "The cash a drawer starts with when a session opens." |
| Field validation | State the correction, beside the field | "Enter an email address, like name@example.com" |
| Task failure | Name the task and the problem, then the safe next step | "Invoices couldn't be loaded." with a Try again button |
| Warning | State the condition and its practical consequence | "This report is missing 2 days of sales. Totals may be low." |
| Confirmation | Action and object as a question, the consequence, labelled choices | "Delete this invoice?" / "You can't undo this." / Delete invoice, Cancel |
| Success | Name the confirmed result | "Invoice sent" |
| Progress | Name the operation actually under way | "Importing 240 contacts…" |
| Empty | Say what's absent here | "No invoices yet" |
| No results | Name the search or filter outcome, and offer a reset | "No invoices match these filters" with Clear filters |
| Offline or unknown | Say what's known, what's limited, and a safe action | "Card result unknown. Check the reader's screen." |

## 4. Buttons and actions

- **Start with a verb that names the outcome.** "Save", "Send invoice", "Publish", "Invite". Never "OK", "Yes", "Submit", "Confirm" or "Go".
- **Use the shortest label that's unambiguous.** In a row menu or a section that already names the object, drop it ("Edit", "Archive"). Standalone and consequential actions keep the object ("Delete event", "Cancel subscription"). "Cancel" + object always keeps the object so it can't be read as dismissal.
- **Use the right verb:**
  - **Cancel** stops the current task.
  - **Discard** abandons unsaved edits.
  - **Remove** detaches something (a member from a team, an item from a list) without destroying it.
  - **Delete** destroys permanently.
  - **Archive** hides something but keeps it.
  - **Close** shuts a sheet or dialog when nothing is pending.
  - **Dismiss** hides a notice.
  - **Done** finishes typed input such as a note, never a destructive or consequential action.
- **When the main action is itself a cancel or discard, name what the other button keeps.** "Discard changes" pairs with "Keep editing". "Cancel subscription" pairs with "Keep subscription".
- **Keep the label stable while the action runs.** Show a spinner in the button and block repeat presses, rather than swapping the label to "Saving…".
- **Don't change a label to explain why it can't be used yet.** Prefer leaving a commit button enabled. If pressing it can't proceed, say what's missing and take focus to the first problem.
- **Links name their destination** ("View invoice", "Billing settings"), never "Click here" or "Learn more" on its own.
- **The same action uses the same words everywhere:** button, menu, shortcut hint, confirmation, toast and email.

## 5. Errors

An error message has two jobs: say what went wrong, and say how to fix it. NN/G's guidelines for error messages come down to these points:

- **Visible:** next to the cause (beside the field, or at the top of the affected content), and noticeable without relying on colour alone. A toast disappears, so it must never be the only place critical recovery instructions appear.
- **Human-readable:** plain words, with no codes, stack traces, raw server or SDK messages, or jargon ("Invalid input", "Error 422", "Request failed").
- **Specific and constructive:** "Enter a date after 1 Jan 2026" rather than "Invalid date". Include the actual limit when you know it.
- **Blameless:** describe the problem, not the person's mistake. No "You failed to…".
- **Preserve work:** keep everything entered. Never clear a form because one field failed.
- **Honest about what's known:** don't guess at a cause. A timeout isn't a decline, an exception isn't proof of data loss, and a network error isn't proof of being offline. When the cause is unknown, use a safe, task-specific fallback ("Changes couldn't be saved. Try again.").
- **No routine apologies.** Validation and expected states need no "Sorry". A short apology is right for a real service failure that matters, alongside the facts and the recovery path, never instead of them.
- **Security-sensitive cases** use the same message whether or not an account exists: "Email or password is incorrect."
- **Timing:** validate when a field loses focus or on submit, not on every keystroke while someone is still typing a plausible value. After the first error, re-check live as they fix it so the error clears as soon as it's resolved.

## 6. Confirmations

Ask for confirmation only for actions that are irreversible, involve money, or reach other people. For anything reversible, act immediately and offer undo. Too many confirmations teach people to press through them without reading.

- **Title:** a question naming the action and the object. "Delete Oakwood Hall?" "Remove Sam from the team?"
- **Body:** the consequence, only if it isn't obvious from the title. Add "You can't undo this." when that's true. Include enough detail to recognise a wrong selection (name, amount, recipient count).
- **Buttons:** the confirming button repeats the action ("Delete venue", "Send to 240 people"). The other button is "Cancel", or names what's kept.
- **Never** use "Are you sure?", "Confirm" or "Yes/No".
- **No destructive default.** Don't make the confirming button respond to Enter. Focus the safe option or the dialog itself, so a stray keypress or tap never commits.

## 7. Success, progress and feedback

- **Name the result and the object:** "Invoice sent", "Draft saved", "Sam removed". Skip "successfully", which adds nothing.
- **Commitments name their details:** "Strimmer booked for Sun 4 Oct. Collect from the shed after 8am." Not just "Booked for Sun 4 Oct", because the tool's name may have scrolled away.
- **Show a toast only when the outcome isn't visible.** If the item visibly appears in the list, the list is the confirmation.
- **Progress copy names the real operation** ("Uploading 3 of 12 photos"). Show a count or percentage only when you can measure one.
- **Don't claim completion early.** "Sent" means the server confirmed it. Offline, say "Will send when you're back online", or the project's equivalent.
- **No celebration** for routine actions. Save warmth for genuine milestones, and keep it brief.

## 8. Empty states

An empty state is often the first thing a new user sees, so it should orient them and point to the first action.

- **First use:** a heading saying what will appear here. Add one line only if it helps someone start (what the thing is for, or how items arrive), and one action if it isn't already visible on the page.
- **No results:** say the search or filter found nothing and offer a reset ("Clear filters"). Don't imply nothing exists.
- **Cleared or done:** "No overdue invoices" is good news and can say so plainly.
- **An error isn't empty, and loading isn't empty.** Never show "No items" while loading or after a failed load.
- No illustrations or jokes in empty states for working tools unless the project's style calls for them.

## 9. Help text and tooltips

- **Explain the unfamiliar or consequential,** not the self-evident. "Name" needs no help text. "Rounding mode" might.
- **Settings descriptions say what turning the setting on does.**
- **Use this order:** what it is, what it does, then what to do (each part optional). "Shows a warning when counted cash differs from the expected total by more than this amount. Set to £0.00 to turn it off."
- **Make essential information visible,** never only in a tooltip. Tooltips need hover, which touch screens don't have.
- **An icon-only button's tooltip is its name** ("Filter"), not an essay.
- **Don't use question-mark help icons** to make up for unclear labels. Fix the label instead.

## 10. Mechanics

- **Case:** sentence case for headings, buttons, labels, menu items, navigation and tabs. Capitalise proper nouns and established product nouns only. Apple's own apps use title case for buttons, menus and tabs. A product can follow that on iOS, or use sentence case everywhere for consistency across platforms. Pick one style per element type and keep it.
- **Full stops:** none on labels, headings, buttons, menu items, table cells or short status fragments. Use them on complete sentences in help, validation, empty-state and dialog body text.
- **Punctuation:** no exclamation marks in product copy. Avoid em dashes in interface text (use a full stop, comma or colon). Use the ellipsis character (…) for operations in progress and for commands that open a further step needing input, following the platform's convention.
- **Numbers:** use numerals ("3 invoices"), and handle singular and plural properly with a plural-aware formatter. Never write "invoice(s)". Small counts read better in words where natural ("Both booked", not "All 2 booked"). Use tabular figures in columns.
- **Money:** show the currency and the right precision ("£12.50"), and use one format throughout. If whole amounts show as "£22" in one place, don't show "£22.00" in another. Say "Free" rather than "£0" for free items. Never show minor units (pence or cents) as if they were the major unit. Say who pays what and when.
- **Dates and times:** use locale formatters. A good compact form is "8 Sep, 14:32", with the year only when it's not the current year. Show absolute times on records and history; relative times ("3 days ago") suit rows and feeds. Name the time zone when ambiguity would matter.
- **Abbreviations:** avoid unexplained ones. Common ones people already know (VAT, PIN, PDF) are fine.
- **Inclusive and localisable:** use "they" for unknown people, and avoid idioms, slang and cultural references. Never build sentences by joining fragments, because word order differs between languages. Allow for 30 to 40% text expansion in translation.
- **Accessible names match visible labels.** A screen reader should announce the same words people see, so voice-control users can say what they see.
- **Truncation:** truncate only when the full value is available somewhere (a tooltip, the detail view, the accessible name). Never truncate numbers or amounts.

## 11. Notifications and email

- **Push notifications:** say what happened and why it matters to this person, specifically enough that they can act without opening the app. "Sam paid invoice INV-204 (£480)" beats "You have a new update". Never use transactional channels for marketing.
- **Email subject:** names the purpose ("Your booking for 12 Oct is confirmed"). Use a recognisable sender.
- **Email body:** the key fact and the action first, then the details someone needs away from the app. Keep the HTML and plain-text versions equivalent. Use the same terms as the screen the email comes from.

## 12. Copy review

Before shipping, read every string in its rendered state, including errors, empty states, long names and plurals, and ask:

1. Would someone say this naturally to the person?
2. Does it use their words, and the same words used elsewhere in the product?
3. Can the person tell what happened and what to do next?
4. Is there a line that could be deleted without losing anything?
5. Does every button name its outcome?
6. Are claims accurate, without promising more than the system does?
7. Do any two strings contradict each other (opening times, limits, prices, what's included)?
