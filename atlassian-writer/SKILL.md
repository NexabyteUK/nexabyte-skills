---
name: atlassian-writer
description: Write content in Atlassian Document Format (ADF) — the JSON structure required by Jira and Confluence Cloud REST APIs. Use this skill ANY time the user asks you to create, update, or draft content for Jira (issue descriptions, comments, custom field bodies) or Confluence (pages, blog posts, comments), including via any Atlassian MCP server, the Jira/Confluence REST API, the `jira` / `confluence` CLI, or copy-paste workflows. Trigger even when the user just says "write a Jira ticket for X", "draft a Confluence page about Y", "leave a comment on JIRA-123", "format this as a Jira description", or "give me the body for this issue" — they almost always need ADF, not plain Markdown, even if they don't say so. Also use when reviewing or fixing existing ADF JSON.
---

# Atlassian Document Format (ADF) Writer

Jira and Confluence Cloud APIs do not accept Markdown or HTML for rich-text fields. They require ADF — a JSON tree of typed nodes loosely modelled on ProseMirror. Pasting Markdown into a Jira description field via the API will be stored as literal characters, not formatted text. This skill is your reference for producing valid ADF.

## When this skill kicks in

Whenever a task touches a rich-text field on Jira or Confluence — issue descriptions, comments, page bodies, custom-field text, work-log comments, etc. — the body must be ADF. The user often won't say "ADF" explicitly; they'll say "write the description" or "add a comment". Treat that as the trigger.

If the user only wants the Markdown source (e.g., to paste into the Jira UI manually, where the editor will convert it), produce Markdown instead — but say so explicitly so they know the difference. The default for anything API-bound is ADF.

## Top-level shape

Every ADF document is a `doc` node with `version: 1`:

```json
{
  "version": 1,
  "type": "doc",
  "content": []
}
```

`content` is an array of **block nodes**. Block nodes contain either more block nodes or **inline nodes**. Inline nodes (almost always `text`) carry the actual characters and may have **marks** (bold, italic, link, etc.).

That three-layer mental model — block → inline → marks — is the whole format. Everything else is filling in node types and attributes.

## The 90% you'll actually use

These cover almost every Jira/Confluence body you'll ever write. Reach for `references/nodes.md` only when you need something exotic.

### Paragraph + styled text

```json
{
  "type": "paragraph",
  "content": [
    { "type": "text", "text": "Plain, " },
    { "type": "text", "text": "bold", "marks": [{ "type": "strong" }] },
    { "type": "text", "text": ", " },
    { "type": "text", "text": "italic", "marks": [{ "type": "em" }] },
    { "type": "text", "text": ", and " },
    {
      "type": "text",
      "text": "a link",
      "marks": [{ "type": "link", "attrs": { "href": "https://atlassian.com" } }]
    },
    { "type": "text", "text": "." }
  ]
}
```

Available marks: `strong`, `em`, `code`, `strike`, `underline`, `link`, `subsup`, `textColor`, `backgroundColor`. Multiple marks combine — e.g., a bold link is `marks: [{type:"strong"}, {type:"link", attrs:{...}}]`.

### Headings

```json
{ "type": "heading", "attrs": { "level": 2 }, "content": [{ "type": "text", "text": "Background" }] }
```

`level` is 1–6.

### Bulleted and numbered lists

```json
{
  "type": "bulletList",
  "content": [
    {
      "type": "listItem",
      "content": [
        { "type": "paragraph", "content": [{ "type": "text", "text": "First item" }] }
      ]
    },
    {
      "type": "listItem",
      "content": [
        { "type": "paragraph", "content": [{ "type": "text", "text": "Second item" }] }
      ]
    }
  ]
}
```

`orderedList` is identical but with `"type": "orderedList"` and an optional `attrs.order` to start numbering somewhere other than 1. List items must wrap their text in a `paragraph` — text cannot live directly inside a `listItem`. Nested lists go inside the `listItem`'s content array, alongside (or after) the paragraph.

### Code block

```json
{
  "type": "codeBlock",
  "attrs": { "language": "python" },
  "content": [{ "type": "text", "text": "def hello():\n    print('hi')" }]
}
```

`language` is any Prism language id (e.g., `javascript`, `python`, `bash`, `json`, `yaml`, `sql`, `text`). Text inside a code block cannot have marks.

### Panels (info / note / warning / success / error)

```json
{
  "type": "panel",
  "attrs": { "panelType": "warning" },
  "content": [
    { "type": "paragraph", "content": [{ "type": "text", "text": "Heads up: this is destructive." }] }
  ]
}
```

Use these for callouts. `panelType` ∈ {`info`, `note`, `warning`, `success`, `error`}.

### Tables

```json
{
  "type": "table",
  "content": [
    {
      "type": "tableRow",
      "content": [
        { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Step" }] }] },
        { "type": "tableHeader", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Owner" }] }] }
      ]
    },
    {
      "type": "tableRow",
      "content": [
        { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Deploy" }] }] },
        { "type": "tableCell", "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "@oncall" }] }] }
      ]
    }
  ]
}
```

Cells must contain block content (paragraphs, lists, etc.) — bare text won't render. Use `tableHeader` for the header row, `tableCell` for body rows.

A common useful pattern is a status-lozenge column. Put the `status` node inside a `paragraph` inside the cell — `status` is inline, so it can't sit directly in the cell:

```json
{ "type": "tableCell", "content": [
    { "type": "paragraph", "content": [
        { "type": "status", "attrs": { "text": "In Progress", "color": "yellow" } }
    ]}
]}
```

### Other useful nodes

- **`blockquote`** — wraps `paragraph` / list / `codeBlock` content, like Markdown's `>`.
- **`rule`** — a horizontal divider; just `{ "type": "rule" }`, no content or attrs.
- **`expand`** — collapsible section: `{ "type": "expand", "attrs": { "title": "Details" }, "content": [...] }`. Use `nestedExpand` inside table cells.
- **`mention`** — inline `@user`: `{ "type": "mention", "attrs": { "id": "<accountId>", "text": "@Jane" } }`. The `id` is the Atlassian Account ID, not a username; if you don't have it, ask the user or fall back to plain text.
- **`emoji`** — `{ "type": "emoji", "attrs": { "shortName": ":rocket:", "text": "🚀" } }`.
- **`status`** — inline lozenge: `{ "type": "status", "attrs": { "text": "In Progress", "color": "yellow" } }`. Colors: `neutral`, `purple`, `blue`, `red`, `yellow`, `green`.
- **`inlineCard`** — Atlassian smart link: `{ "type": "inlineCard", "attrs": { "url": "https://..." } }`. Renders as a card preview for Jira/Confluence/Bitbucket URLs.
- **`hardBreak`** — line break inside a paragraph: `{ "type": "hardBreak" }`.

For everything else — media nodes, dates, decision items, task lists, sync blocks — see `references/nodes.md`.

## Rules that catch people out

- **`text` nodes can't be empty.** `"text": ""` is invalid. Omit the node, or use a `hardBreak` for a line break.
- **Block nodes must contain blocks; inline nodes must contain text.** You cannot put `{type: "text"}` directly inside a `listItem` or `tableCell` — wrap it in a `paragraph`. (`taskItem` is the one exception: it accepts inline content directly, no paragraph needed.)
- **`codeBlock` text cannot have marks.** No bold-inside-code. Marks on code-block text will be rejected.
- **`panel` content is restricted** to `paragraph`, `heading`, `bulletList`, `orderedList`. No nested panels, no tables.
- **Don't escape HTML.** ADF text is plain Unicode — write `<` and `&` as themselves.
- **Don't invent attributes.** Each node has a fixed schema; unknown `attrs` keys may silently break rendering. When in doubt, omit `attrs` entirely.
- **Markdown is not ADF.** Never hand the user `**bold**` or `# Heading` strings inside a `text` node — convert to proper marks/heading nodes.

## How to actually write a document

1. **Outline first in your head** as if it were Markdown — headings, paragraphs, lists, callouts. This keeps the structure clean.
2. **Build it as JSON** node-by-node, top to bottom. Don't skip layers (block → paragraph → text).
3. **Validate before delivering.** Run the validator: either pipe the JSON in (`python3 scripts/validate_adf.py < your-doc.json`) or pass the file path (`python3 scripts/validate_adf.py your-doc.json`). It catches ~95% of malformed-ADF errors and is fast.
4. **Match the delivery channel:**
   - **Atlassian MCP tools** (`createJiraIssue`, `createConfluencePage`, comment-creating tools, etc.) — pass the ADF as a **JSON-stringified** value into the body field (`description` for Jira, `body` for Confluence) and set `contentFormat: "adf"`. The field is typed as `string` in the MCP schema even though the content is JSON; serialize the doc with `JSON.stringify` (or `json.dumps`) before passing.
   - **Confluence specifically** also requires `spaceId` — that's the **numeric** id (e.g., `"229380"`), not the human-readable space key (e.g., `"SD"`). Both are returned by the spaces lookup; pick `id`.
   - **Direct REST API** — Jira v3 takes the doc as a JSON object (`{"fields": {"description": {...adf...}}}`). Confluence v2 takes it wrapped in a representation (`{"body": {"representation": "atlas_doc_format", "value": "<stringified-adf>"}}`).
   - **Mentions need real Account IDs.** If the user wants `@someone` and you don't have their Atlassian Account ID, look it up via the user-search MCP tool if available, or render the name as plain `text` and tell the user to add the mention in the UI. Never invent an `id`.

## Worked example: a Jira bug-report description

User asks: *"Write the description for a bug ticket: login button does nothing on Safari 17, repro is just clicking it on the homepage, expected is to open the auth modal. Tag the auth team."*

```json
{
  "version": 1,
  "type": "doc",
  "content": [
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "Summary" }]
    },
    {
      "type": "paragraph",
      "content": [
        { "type": "text", "text": "The login button on the homepage does nothing when clicked in Safari 17." }
      ]
    },
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "Steps to reproduce" }]
    },
    {
      "type": "orderedList",
      "content": [
        {
          "type": "listItem",
          "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Open the homepage in Safari 17." }] }]
        },
        {
          "type": "listItem",
          "content": [{ "type": "paragraph", "content": [{ "type": "text", "text": "Click the Log in button in the top-right." }] }]
        }
      ]
    },
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "Expected vs actual" }]
    },
    {
      "type": "bulletList",
      "content": [
        {
          "type": "listItem",
          "content": [
            {
              "type": "paragraph",
              "content": [
                { "type": "text", "text": "Expected: ", "marks": [{ "type": "strong" }] },
                { "type": "text", "text": "the auth modal opens." }
              ]
            }
          ]
        },
        {
          "type": "listItem",
          "content": [
            {
              "type": "paragraph",
              "content": [
                { "type": "text", "text": "Actual: ", "marks": [{ "type": "strong" }] },
                { "type": "text", "text": "nothing happens; no console error." }
              ]
            }
          ]
        }
      ]
    },
    {
      "type": "panel",
      "attrs": { "panelType": "info" },
      "content": [
        {
          "type": "paragraph",
          "content": [
            { "type": "text", "text": "Flagging the auth team for triage." }
          ]
        }
      ]
    }
  ]
}
```

If a Slack-style mention is needed, replace the trailing paragraph text with a `mention` node — but only if you have the user's Atlassian Account ID. Otherwise, leave the team name as plain text and let the user fill in the mention in the UI.

## References

- `references/nodes.md` — full node and mark catalogue, including media, date, taskList, decisionList, layout columns, and other less-common nodes.
- `references/markdown-to-adf.md` — quick translation table from Markdown constructs to ADF nodes.
- `scripts/validate_adf.py` — structural validator. Run before delivering ADF to the user or an API.
- Official spec: https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/
