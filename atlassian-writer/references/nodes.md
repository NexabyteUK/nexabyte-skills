# ADF node and mark catalogue

This is the long-form reference. Read this when SKILL.md doesn't cover the node you need, or when you're writing media, layouts, decisions, or task lists.

For each node: type name, classification (block/inline/child), required + optional attrs, allowed content, JSON example.

## Block nodes (top-level)

These can appear directly inside `doc.content`.

### `paragraph`
- **Content:** zero or more inline nodes.
- **Attrs:** `localId` (optional).
- A paragraph with no content is valid and renders as a blank line.

### `heading`
- **Attrs:** `level` (required, 1–6), `localId` (optional).
- **Content:** inline nodes.

### `bulletList` / `orderedList`
- **Content:** one or more `listItem`.
- `orderedList.attrs.order` (optional) — starting number, default 1.

### `listItem`
- **Content:** one or more block nodes. The first child is almost always a `paragraph`. Nested lists go after the paragraph as additional children.

### `codeBlock`
- **Attrs:** `language` (optional Prism id; unsupported values render as plain monospace).
- **Content:** one or more `text` nodes **without marks**.

### `blockquote`
- **Content:** `paragraph`, `bulletList`, `orderedList`, `codeBlock`, `mediaGroup`, `mediaSingle`. Nested blockquotes are not allowed.

### `panel`
- **Attrs:** `panelType` ∈ {`info`, `note`, `warning`, `success`, `error`} (required).
- **Content:** `paragraph`, `heading`, `bulletList`, `orderedList`. No tables, no nested panels.

### `rule`
- Just `{ "type": "rule" }`. No attrs, no content.

### `table`
- **Attrs (all optional):** `isNumberColumnEnabled` (bool), `width` (int, px), `layout` (`center` | `align-start` | `align-end` | `default` | `wide` | `full-width`), `displayMode` (`default` | `fixed`).
- **Content:** one or more `tableRow`.
- Tables don't render on Atlassian mobile clients.

### `tableRow`
- **Content:** one or more `tableCell` and/or `tableHeader`.

### `tableCell` / `tableHeader`
- **Attrs (optional):** `colspan` (int), `rowspan` (int), `colwidth` (array of ints), `background` (string).
- **Content:** block nodes (paragraphs, lists, code blocks, panels, etc.). `nestedExpand` is allowed; standard `expand` is not.

### `expand`
- **Attrs:** `title` (string, required).
- **Content:** block nodes.

### `nestedExpand`
- Same as `expand` but for use inside table cells.

### `mediaSingle`
- A single image or file rendered as a block with optional sizing.
- **Attrs (optional):** `layout` (`wrap-left` | `center` | `wrap-right` | `wide` | `full-width` | `align-start` | `align-end`), `width` (number, percent of column).
- **Content:** exactly one `media` child.

### `mediaGroup`
- A row of file thumbnails.
- **Content:** one or more `media`.

### `mediaInline`
- Inline media reference (rare; use `media` inside `mediaSingle`/`mediaGroup` for most cases).

### `taskList`
- Confluence-style checklist.
- **Attrs:** `localId` (string, required — generate a UUID).
- **Content:** one or more `taskItem`.

### `taskItem`
- **Attrs:** `localId` (required, UUID), `state` (`TODO` | `DONE`).
- **Content:** inline nodes — text and other inline nodes go directly inside, no `paragraph` wrapper needed. (This is the opposite of `listItem`, which does require a `paragraph`.)

### `decisionList` / `decisionItem`
- Same shape as taskList/taskItem.
- `decisionItem.attrs.state` is `DECIDED` (the only value currently used).

### `layoutSection` + `layoutColumn`
- Multi-column layouts in Confluence.
- `layoutSection.content` is two or more `layoutColumn`.
- `layoutColumn.attrs.width` is a percent (must sum to 100 across the section).
- `layoutColumn.content` is block nodes.

### `embedCard`
- A block-level smart link, larger preview than `inlineCard`.
- **Attrs:** `url` (required), `layout`, `width`.

## Child nodes

Cannot appear at the top level — only inside specific parents.

| Node            | Lives inside                   |
|-----------------|--------------------------------|
| `listItem`      | `bulletList`, `orderedList`    |
| `tableRow`      | `table`                        |
| `tableCell`     | `tableRow`                     |
| `tableHeader`   | `tableRow`                     |
| `media`         | `mediaSingle`, `mediaGroup`    |
| `taskItem`      | `taskList`                     |
| `decisionItem`  | `decisionList`                 |
| `layoutColumn`  | `layoutSection`                |
| `nestedExpand`  | `tableCell`, `tableHeader`     |

### `media`
- **Attrs (required one of):**
  - `type: "file"` + `id` (Media API file id) + `collection` (string, may be empty).
  - `type: "external"` + `url` (string).
- **Optional attrs:** `width`, `height`, `alt`, `occurrenceKey`.

## Inline nodes

These go inside `paragraph`, `heading`, `tableCell`, etc.

### `text`
- **Required:** `text` (non-empty string).
- **Optional:** `marks` (array).

### `hardBreak`
- `{ "type": "hardBreak" }`. Line break inside a paragraph; equivalent to `<br>`.

### `mention`
- **Attrs (required):** `id` (Atlassian Account ID), `text` (display name with `@`).
- **Optional:** `userType` (`DEFAULT` | `SPECIAL` | `APP`), `accessLevel`.

### `emoji`
- **Attrs:** `shortName` (required, e.g. `:rocket:`), `text` (optional fallback char), `id` (optional service id).

### `date`
- **Attrs:** `timestamp` (string of Unix ms, e.g. `"1672531200000"`).

### `status`
- **Attrs (required):** `text`, `color` ∈ {`neutral`, `purple`, `blue`, `red`, `yellow`, `green`}.
- **Optional:** `localId` (UUID).
- Does not accept marks.

### `inlineCard`
- **Attrs:** exactly one of `url` or `data`. `data` is JSON-LD.

### `mediaInline`
- Same shape as `media` but renders inline with text. Rare.

## Marks

Applied to `text` nodes via `marks: [...]`.

| Mark              | Attrs                                                        | Notes |
|-------------------|--------------------------------------------------------------|-------|
| `strong`          | none                                                         | Bold |
| `em`              | none                                                         | Italic |
| `code`            | none                                                         | Inline `monospace` |
| `strike`          | none                                                         | Strikethrough |
| `underline`       | none                                                         | |
| `link`            | `href` (required), `title`, `collection`, `id`, `occurrenceKey` | |
| `subsup`          | `type` (`sub` or `sup`)                                      | |
| `textColor`       | `color` (hex string, e.g. `"#ff0000"`)                       | |
| `backgroundColor` | `color` (hex string)                                         | |
| `border`          | `size` (int), `color` (hex)                                  | Rare |

Marks combine: `marks: [{type:"strong"},{type:"em"}]` is bold-italic. Order doesn't matter for rendering, but be consistent.

## Combining nodes — common patterns

### A linked, bold word inside a sentence

```json
{
  "type": "paragraph",
  "content": [
    { "type": "text", "text": "See the " },
    {
      "type": "text",
      "text": "deployment runbook",
      "marks": [
        { "type": "strong" },
        { "type": "link", "attrs": { "href": "https://wiki/runbook" } }
      ]
    },
    { "type": "text", "text": "." }
  ]
}
```

### A nested list

```json
{
  "type": "bulletList",
  "content": [
    {
      "type": "listItem",
      "content": [
        { "type": "paragraph", "content": [{ "type": "text", "text": "Phase 1" }] },
        {
          "type": "bulletList",
          "content": [
            {
              "type": "listItem",
              "content": [
                { "type": "paragraph", "content": [{ "type": "text", "text": "Sub-item" }] }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

### A taskList

```json
{
  "type": "taskList",
  "attrs": { "localId": "list-1" },
  "content": [
    {
      "type": "taskItem",
      "attrs": { "localId": "task-1", "state": "TODO" },
      "content": [{ "type": "text", "text": "Write tests" }]
    },
    {
      "type": "taskItem",
      "attrs": { "localId": "task-2", "state": "DONE" },
      "content": [{ "type": "text", "text": "Open PR" }]
    }
  ]
}
```

### A two-column Confluence layout

```json
{
  "type": "layoutSection",
  "content": [
    {
      "type": "layoutColumn",
      "attrs": { "width": 50.0 },
      "content": [
        { "type": "paragraph", "content": [{ "type": "text", "text": "Left column" }] }
      ]
    },
    {
      "type": "layoutColumn",
      "attrs": { "width": 50.0 },
      "content": [
        { "type": "paragraph", "content": [{ "type": "text", "text": "Right column" }] }
      ]
    }
  ]
}
```
