---
name: linear-story-writing
description: Apply Nexabyte's Linear labels, native dependencies and unfinished-work rules when creating, updating or splitting stories and handling implementation findings.
metadata:
  version: "0.2.0"
---

# Nexabyte Linear rules

Use these rules for Nexabyte POS, Attendly and other Nexabyte projects. Follow the invoking workflow's authority, status, assignment and delegation rules.

## Labels and ownership

- Read the destination team's current label groups and descriptions. Apply exactly one Type: **Bug**, **Feature**, **Improvement** or **Chore**. A project's Story or Enabler label does not replace Type.
- Use that project's area and delivery labels. Preserve unrelated labels on edits. Do not copy agent-selection or execution-trigger labels from another issue, or apply retired labels or group names.
- Use the owning project, relevant epic and an existing milestone where appropriate. A discovery's source issue is not automatically its parent. Do not invent a milestone, priority, estimate or deadline to fill fields.

## Dependencies

- When B needs A's deliverable, create the native relation **A blocks B**. A parent groups work; a related link records context. Neither supplies a blocker. Verify direction and check for cycles.
- Preserve a release or sign-off gate while required work remains elsewhere. A Done issue does not prove deployment, external approval or hardware validation. Identify the actual outstanding prerequisite; do not add artificial blocker issues for routine tasks.

## Unfinished work

- Read the owning story's comments and current relationships. Honour existing human decisions, including authorised splits. An agent's decision to file a ticket is not itself a scope waiver.
- An unmet acceptance condition, a defect that defeats the promised outcome or a regression introduced by this change stays owned until completed. PR size alone does not justify moving it out of scope. Keep a demonstrated independent defect outside that outcome separate; search for an existing owner before creating anything.
- For an authorised transfer, record the decision source, remaining criteria and each issue's responsibility in the source story. Preserve the original requirement and any aggregate completion gate. A change to implementation organisation need not change the promised outcome.
- Make unfinished acceptance work explicit even when its implementation PR has merged. Follow the project's status conventions; do not automatically reopen every completed source issue. The outstanding work needs an owner and any real blocking relationship. Filing it, merging code or passing a test suite does not complete the original outcome.

## Save and verify

Use native connector fields or Symphony's `linear_graphql`. Resolve IDs and inspect the current schema as needed. For a GraphQL blocker, `issueRelationCreate` uses `type: blocks`, `issueId: A`, `relatedIssueId: B`.

Follow pagination when comments, label lists or searches are incomplete.

Recheck for duplicates immediately before creating an issue. After an uncertain create result, recover the existing result before retrying. Preserve unrelated metadata and relationships. Read back the saved description, project, labels, parent, milestone, status, assignee, delegate and relations. Repair partial writes on the same issue; report anything unverified.
