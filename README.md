# Nexabyte Skills

A collection of [agent skills](https://www.anthropic.com/news/skills) by [Nexabyte](https://nexabyte.co.uk) for use with Claude (and compatible agent harnesses such as Claude Code, Copilot CLI, and Gemini CLI).

Each subdirectory is a self-contained skill. Drop the directory into your skills location, or install via your harness's plugin/skills mechanism.

## Skills

| Skill | What it does |
|---|---|
| [`atlassian-writer/`](./atlassian-writer) | Writes valid Atlassian Document Format (ADF) JSON for Jira and Confluence Cloud APIs — issue descriptions, comments, page bodies. Triggers automatically when a task touches a Jira or Confluence rich-text field. |
| [`product-design/`](./product-design) | Design principles for mobile and web app UI, synthesised from Apple's Human Interface Guidelines, Nielsen Norman Group research and Linear's product philosophy, with links to the originals. Covers layout, interaction patterns, voice and microcopy, visual design, iOS and Android conventions, web and desktop, and an accessibility floor. Defers to a project's own `DESIGN.md`, and includes an opt-in Linear-style profile. |

## Installing a skill

Most harnesses support either copying the skill directory into a known location or referencing it by path:

- **Claude Code** — copy the skill folder into `~/.claude/skills/` (or a project's `.claude/skills/`). It will be auto-discovered on next session.
- **Other harnesses** — see your harness's skills documentation. The format is portable: every skill is a directory with a `SKILL.md` at its root and optional `references/` and `scripts/` subdirectories.

## Skill structure

```
skill-name/
├── SKILL.md            # YAML frontmatter (name, description) + body
├── references/         # Long-form docs loaded only when needed
└── scripts/            # Optional helpers the skill body invokes
```

The `description` in each `SKILL.md` frontmatter is what the agent uses to decide whether to invoke the skill, so it is the most important field to read if you want to know when a skill triggers.

## Contributing

PRs welcome. New skills should follow the structure above and include a clear, specific `description` in the frontmatter so agents know when to use them.

## License

MIT — see [`LICENSE`](./LICENSE).

## About Nexabyte

Nexabyte is a UK technology company offering IT consultancy, AI automation, and user-focused tech solutions to charities, small businesses, and individuals. <https://nexabyte.co.uk>
