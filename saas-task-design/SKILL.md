---
name: saas-task-design
description: Rebuild a confusing SaaS screen around the customer's task, with evidence for its claims and actions, a reproducible decision record, and a comprehension check. Use for product screens and flows that remain unclear after copy editing; not marketing pages or a request to change one sentence.
---

# SaaS task design

Use the customer's decision to determine the screen's structure. A voice guide supplies language conventions; it does not justify an existing section or control. Preserve the product's visual system unless the user authorises a visual redesign.

## Establish the task and facts

Read the story, relevant customer decisions, the current screen, the voice guide and the smallest relevant behaviour contract. Distinguish a proposed design, an approved decision and implemented behaviour. Earlier agent recommendations are not customer approval. Separate required outcomes from proposed wording and placement: an acceptance criterion can establish a capability without earning a sentence on the current screen. Preserve functional requirements and explicit customer decisions. If a better placement conflicts with an explicit criterion, show the proposed departure and its reason in the review evidence; do not silently mark that criterion satisfied or treat the proposal as approved. Apply later customer decisions over earlier criteria.

Write a brief in ordinary language: who arrives, what brought them here, what they need to understand, and what they can do next. Identify the actual decision. If the customer has nothing useful to decide, consider an automatic outcome or notification, but don't invent automation to improve the mockup.

For every consequential claim or action, record its source and status: observed in implementation, specified but unimplemented, unknown, or proposed change. Specimen values are example data, not live customer facts. Examples: whether a payment succeeded, whether work is saved, who receives a support request, whether an action can be undone. Ask only when a missing fact prevents a truthful proposal. A local draft may show an explicitly labelled assumption outside the product screen; do not put a speculative promise inside the screen.

Use the [run record](references/run-record.md) as a structure for retaining inputs and decisions in the story, PR or an existing project document. It does not require a new document; follow the host workflow’s evidence rules. Pin the source revision and preserve the original before editing. Honour the user's local/remote boundary.

For a planning-only request, return the brief, evidence and content decisions without implementing or changing files.

## Decide what belongs on the screen

First draft the minimum content for each state from the person's task and verified facts, without using the existing blocks as the outline. Then compare it with the current screen. Reusing the visual system does not mean reusing its composition. A shared component's default layout is not an approved screen structure: compose its existing primitives locally when needed, rather than retaining unnecessary hierarchy or changing the shared component for every caller.

Truth, necessity and placement are separate checks. For each retained line, icon, section and control, name what the person would misunderstand, be unable to do, or materially risk if it were absent **in this state**. "It is true", "it could be useful", "the old screen has it" and "the acceptance criteria mention it" are not sufficient reasons for visibility. An explanation of a visible button often adds nothing. Do not turn rare future tasks into instructions beside an already completed task.

For each existing block, choose one of these dispositions and record that concrete consequence:

- **Visible:** needed to understand the current situation, choose an action or avoid a material mistake.
- **Available on demand:** supporting detail with a distinct customer use that can wait. Name that use, the actual supported destination and how it is reached. Remove redundant content before considering disclosure; hiding it does not justify retaining it. Do not invent a link or move information to a nonexistent surface.
- **Removed:** duplicate information or content that does not help this reader in this state. Do not delete retained business evidence from the product.

Review the whole initial view as well as each element. Choose its leading message and group the facts that explain that outcome; do not give every fact equal prominence through a separate heading, label or row. Necessary somewhere does not mean necessary immediately. Details used only to verify or reconcile an outcome can be available on demand, while consequences and information needed for the current decision stay visible. Choose this per state: success, uncertainty and failure need not share the same summary. Do not impose a disclosure or a line-count limit on every screen.

Translate system events into their customer consequence. Separate known facts from unknown effects. Explain specialised terms only where the customer needs them. Challenge internal labels, capitalisation and repeated status fragments; document intentional exceptions to the voice guide instead of silently changing it for the whole product.

Choose the primary action from the supported behaviours. Where the customer is choosing which data to keep or apply, name that choice in the button. Explain closing or resolving the problem separately when that consequence matters. State a material consequence before the person commits. An action already visible may provide the next step without another instructional sentence. Avoid using brevity to remove the information needed to make the choice.

Draft the useful spoken explanation first, then arrange the screen around it. Do not inherit the previous card count, section headings, status chips or metadata list. Do not force every screen into a headline, paragraph and button: tables, comparisons and multiple actions are appropriate when the task requires them.

## Build and check

Implement the proposal in the project's design source and reuse its components. Include any new disclosure or interaction in the component specimens. Keep the original separately. Test the relevant narrow/wide and light/dark forms, including readable expanded details, keyboard focus, dialog cancellation and the proposed action states. A local simulation must be labelled outside the product UI and must not send real requests.

Check behaviour claims against the evidence again after editing. Keep source tests for important distinctions where the project requires them. Record which runtime behaviours are only illustrated. Passing format, layout or exact-copy tests does not prove understanding.

Before providing the rationale, ask an independent reader or permitted review agent to inspect the rendered screen and answer:

- What happened, and what remains uncertain?
- What should the customer do next?
- What happens after that action? Does anything need confirmation?
- What can the customer continue doing, if the screen establishes that?
- Where would they look for supporting detail?

Also ask what could be removed or moved without making the current task harder, and whether anything implies an unnecessary action. Comprehensible text can still be unnecessary. Treat missing details as candidates, not a list to add: decide whether the reader needs each one now. Keep a retained element when the evidence warrants it; there is no deletion quota.

Record their actual answers and any mistaken inference. Fix a mismatch with the product facts; don't award yourself a clarity score. A model review is a comprehension probe, not user research. Ask the user to judge the concrete proposal without treating agent agreement as approval.

## Deliver a reproducible result

Save the pinned inputs, decision record, edited source or patch, build/render instructions, comparison and verification results. Distinguish reproduction of the exact artifact from reuse of the design method: the patch reproduces this output; the skill guides new decisions and does not promise identical model wording.

Keep unresolved product decisions separate from the screen. Only update the shared product rules or publish changes within the user's authorisation. Refine this skill from observed failures rather than adding a rule for every stylistic preference.
