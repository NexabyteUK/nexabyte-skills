#!/usr/bin/env python3
"""
Structural validator for Atlassian Document Format (ADF).

Catches the high-frequency mistakes:
  - empty text nodes
  - text nodes that are bare children of a block (need a paragraph wrapper)
  - panels with disallowed children
  - codeBlock text with marks
  - missing required attrs (heading.level, panel.panelType, link.href, ...)
  - unknown node types

Usage:
  python3 validate_adf.py <file.json>
  cat doc.json | python3 validate_adf.py
  python3 validate_adf.py - <<< '{"version":1,"type":"doc","content":[]}'

Exit code 0 if valid, 1 otherwise. Errors print as `path: message` lines.
"""
from __future__ import annotations

import json
import sys
from typing import Any


# Node classification. A node may be a top-level block, a non-top-level
# block (child node), or an inline node. Some nodes appear in multiple
# columns because their parent constraints determine where they're allowed.
TOP_LEVEL_BLOCKS = {
    "blockquote", "bulletList", "codeBlock", "decisionList", "embedCard",
    "expand", "heading", "layoutSection", "mediaGroup", "mediaSingle",
    "orderedList", "panel", "paragraph", "rule", "table", "taskList",
}
CHILD_BLOCKS = {
    "listItem", "tableRow", "tableCell", "tableHeader", "media",
    "taskItem", "decisionItem", "layoutColumn", "nestedExpand",
}
INLINE_NODES = {
    "text", "hardBreak", "mention", "emoji", "date", "status",
    "inlineCard", "mediaInline",
}
BLOCK_NODES = TOP_LEVEL_BLOCKS | CHILD_BLOCKS
KNOWN_NODES = BLOCK_NODES | INLINE_NODES | {"doc"}

KNOWN_MARKS = {
    "strong", "em", "code", "strike", "underline", "link", "subsup",
    "textColor", "backgroundColor", "border",
}

PANEL_TYPES = {"info", "note", "warning", "success", "error"}
STATUS_COLORS = {"neutral", "purple", "blue", "red", "yellow", "green"}

# What each block accepts as direct children (best-effort; not exhaustive).
PANEL_ALLOWED = {"paragraph", "heading", "bulletList", "orderedList"}
BLOCKQUOTE_ALLOWED = {
    "paragraph", "bulletList", "orderedList", "codeBlock",
    "mediaGroup", "mediaSingle",
}


def validate(node: Any, path: str = "$", parent_type: str | None = None) -> list[str]:
    errors: list[str] = []

    if not isinstance(node, dict):
        return [f"{path}: expected object, got {type(node).__name__}"]

    node_type = node.get("type")
    if not node_type:
        return [f"{path}: missing 'type'"]

    if node_type == "doc":
        if node.get("version") != 1:
            errors.append(f"{path}: doc.version must be 1")
        content = node.get("content", [])
        if not isinstance(content, list):
            errors.append(f"{path}.content: must be an array")
        else:
            for i, child in enumerate(content):
                child_path = f"{path}.content[{i}]"
                if isinstance(child, dict) and child.get("type") not in TOP_LEVEL_BLOCKS:
                    errors.append(
                        f"{child_path}: '{child.get('type')}' is not a top-level block node"
                    )
                errors.extend(validate(child, child_path, "doc"))
        return errors

    if node_type not in KNOWN_NODES:
        errors.append(f"{path}: unknown node type '{node_type}'")
        # keep going — maybe the user is on a newer schema

    attrs = node.get("attrs", {})
    content = node.get("content", [])

    # Per-node required-attr / value checks.
    if node_type == "heading":
        level = attrs.get("level")
        if not isinstance(level, int) or not 1 <= level <= 6:
            errors.append(f"{path}.attrs.level: required int between 1 and 6, got {level!r}")
    elif node_type == "panel":
        ptype = attrs.get("panelType")
        if ptype not in PANEL_TYPES:
            errors.append(
                f"{path}.attrs.panelType: must be one of {sorted(PANEL_TYPES)}, got {ptype!r}"
            )
    elif node_type == "status":
        if not attrs.get("text"):
            errors.append(f"{path}.attrs.text: required non-empty string")
        if attrs.get("color") not in STATUS_COLORS:
            errors.append(
                f"{path}.attrs.color: must be one of {sorted(STATUS_COLORS)}, got {attrs.get('color')!r}"
            )
    elif node_type == "mention":
        if not attrs.get("id"):
            errors.append(f"{path}.attrs.id: mention requires an Atlassian Account ID")
    elif node_type == "emoji":
        if not attrs.get("shortName"):
            errors.append(f"{path}.attrs.shortName: required (e.g. ':rocket:')")
    elif node_type == "expand" or node_type == "nestedExpand":
        if "title" not in attrs:
            errors.append(f"{path}.attrs.title: required")
    elif node_type == "inlineCard":
        if bool(attrs.get("url")) == bool(attrs.get("data")):
            errors.append(f"{path}.attrs: inlineCard requires exactly one of 'url' or 'data'")
    elif node_type == "orderedList":
        order = attrs.get("order")
        if order is not None and (not isinstance(order, int) or order < 0):
            errors.append(f"{path}.attrs.order: must be a non-negative int, got {order!r}")
    elif node_type == "taskItem":
        if attrs.get("state") not in {"TODO", "DONE"}:
            errors.append(f"{path}.attrs.state: must be 'TODO' or 'DONE'")

    # Text node.
    if node_type == "text":
        text = node.get("text")
        if not isinstance(text, str):
            errors.append(f"{path}.text: required string")
        elif text == "":
            errors.append(f"{path}.text: must be non-empty (omit the node or use hardBreak)")
        marks = node.get("marks", [])
        if marks:
            if parent_type == "codeBlock":
                errors.append(f"{path}: text inside codeBlock cannot have marks")
            for j, mark in enumerate(marks):
                errors.extend(_validate_mark(mark, f"{path}.marks[{j}]"))
        return errors

    if node_type == "hardBreak":
        return errors

    # Block-level container checks.
    if node_type == "panel":
        for i, child in enumerate(content):
            ctype = child.get("type") if isinstance(child, dict) else None
            if ctype not in PANEL_ALLOWED:
                errors.append(
                    f"{path}.content[{i}]: panel cannot contain '{ctype}' "
                    f"(allowed: {sorted(PANEL_ALLOWED)})"
                )
    elif node_type == "blockquote":
        for i, child in enumerate(content):
            ctype = child.get("type") if isinstance(child, dict) else None
            if ctype not in BLOCKQUOTE_ALLOWED:
                errors.append(
                    f"{path}.content[{i}]: blockquote cannot contain '{ctype}' "
                    f"(allowed: {sorted(BLOCKQUOTE_ALLOWED)})"
                )
    elif node_type == "listItem":
        # listItem cannot directly hold inline `text` — it must wrap text in a paragraph.
        for i, child in enumerate(content):
            ctype = child.get("type") if isinstance(child, dict) else None
            if ctype in INLINE_NODES:
                errors.append(
                    f"{path}.content[{i}]: listItem cannot directly contain inline '{ctype}' "
                    "— wrap it in a paragraph"
                )
    elif node_type in {"tableCell", "tableHeader"}:
        for i, child in enumerate(content):
            ctype = child.get("type") if isinstance(child, dict) else None
            if ctype in INLINE_NODES:
                errors.append(
                    f"{path}.content[{i}]: {node_type} cannot directly contain inline '{ctype}' "
                    "— wrap it in a paragraph"
                )
    elif node_type == "codeBlock":
        for i, child in enumerate(content):
            ctype = child.get("type") if isinstance(child, dict) else None
            if ctype != "text":
                errors.append(f"{path}.content[{i}]: codeBlock may only contain text nodes")

    # Recurse into content.
    if isinstance(content, list):
        for i, child in enumerate(content):
            errors.extend(validate(child, f"{path}.content[{i}]", node_type))

    return errors


def _validate_mark(mark: Any, path: str) -> list[str]:
    if not isinstance(mark, dict):
        return [f"{path}: mark must be an object"]
    mtype = mark.get("type")
    if mtype not in KNOWN_MARKS:
        return [f"{path}.type: unknown mark '{mtype}'"]
    if mtype == "link":
        href = (mark.get("attrs") or {}).get("href")
        if not href:
            return [f"{path}.attrs.href: link mark requires an href"]
    if mtype == "subsup":
        kind = (mark.get("attrs") or {}).get("type")
        if kind not in {"sub", "sup"}:
            return [f"{path}.attrs.type: subsup must be 'sub' or 'sup'"]
    return []


def main() -> int:
    args = sys.argv[1:]
    if not args or args[0] == "-":
        raw = sys.stdin.read()
    else:
        with open(args[0]) as f:
            raw = f.read()

    try:
        doc = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}", file=sys.stderr)
        return 1

    if not (isinstance(doc, dict) and doc.get("type") == "doc"):
        print("Root must be a 'doc' node with type 'doc'", file=sys.stderr)
        return 1

    errors = validate(doc)
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} error(s).", file=sys.stderr)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
