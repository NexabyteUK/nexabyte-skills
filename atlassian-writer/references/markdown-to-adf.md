# Markdown → ADF translation

A quick lookup table for converting common Markdown into ADF. Use when the user gives you Markdown and wants ADF, or when drafting a doc and translating mentally.

## Block-level

| Markdown                        | ADF                                                                |
|---------------------------------|--------------------------------------------------------------------|
| `# Heading`                     | `heading` with `attrs.level: 1`                                    |
| `## Heading`                    | `heading` with `attrs.level: 2` (and so on through level 6)        |
| Plain paragraph                 | `paragraph`                                                        |
| `- item` / `* item`             | `bulletList` → `listItem` → `paragraph`                            |
| `1. item`                       | `orderedList` → `listItem` → `paragraph`                           |
| ```` ```lang\ncode\n``` ````    | `codeBlock` with `attrs.language: "lang"`                          |
| `    indented code`             | `codeBlock` (drop the indent; pick a language or omit attrs)       |
| `> quote`                       | `blockquote` containing a `paragraph`                              |
| `---` / `***`                   | `rule`                                                             |
| `\| col \| col \|` table        | `table` → `tableRow` → `tableHeader`/`tableCell` → `paragraph`     |
| `- [ ] task` / `- [x] task`     | `taskList` → `taskItem` (`state: "TODO"` / `"DONE"`)               |
| `> [!INFO] ...` (GFM callout)   | `panel` with the matching `panelType`                              |

There is no ADF equivalent for raw HTML. Strip `<br>`, `<hr>`, etc. and use the corresponding nodes (`hardBreak`, `rule`).

## Inline

| Markdown               | ADF                                                                  |
|------------------------|----------------------------------------------------------------------|
| `**bold**`             | `text` with `marks: [{type: "strong"}]`                              |
| `*italic*` / `_italic_`| `text` with `marks: [{type: "em"}]`                                  |
| `` `code` ``           | `text` with `marks: [{type: "code"}]`                                |
| `~~strike~~`           | `text` with `marks: [{type: "strike"}]`                              |
| `[label](url)`         | `text` with `marks: [{type: "link", attrs: {href: "url"}}]`          |
| `![alt](url)` (image)  | `mediaSingle` containing `media` with `type: "external", url: "url"` |
| `@user` (mention)      | `mention` with `attrs.id` (account ID) — fall back to plain text if no ID |
| `:emoji:`              | `emoji` with `attrs.shortName: ":emoji:"`                            |
| Two trailing spaces    | `hardBreak`                                                          |

## Edge cases

- **Bold inside a link:** combine marks on a single text node — `marks: [{type: "strong"}, {type: "link", attrs: {href: ...}}]`.
- **A line break inside a list item:** use `hardBreak` inside the `paragraph`. Don't split into multiple paragraphs unless you genuinely want a paragraph break.
- **Inline code inside a heading:** put a `text` node with a `code` mark inside the heading's content. Headings accept inline marks.
- **Code fences with no language:** omit `attrs` entirely (or set `language: "text"`). Don't pass an empty string.
- **Nested blockquotes:** ADF doesn't allow them. Flatten to a single blockquote, or use a panel.
- **Footnotes / definition lists / ToC:** no ADF equivalent. Render as headings + paragraphs.
- **Auto-linked URLs (`https://...` on its own line):** for Atlassian product URLs (Jira/Confluence/Bitbucket), prefer `inlineCard` for a smart preview; otherwise a plain `text` node with a `link` mark is fine.
