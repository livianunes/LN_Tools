#!/usr/bin/env python3
"""Regenerate the tool table in README.md from the pages in docs/.

Adding a new tool:
    1. drop the .nk in tools/
    2. write docs/<ToolName>.md — first line "# Name", then a "> one-line summary",
       and a "**Category:** ..." line near the bottom
    3. run:  python build_index.py

Everything between the AUTOGEN markers in README.md is replaced.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
DOCS = ROOT / "docs"
TOOLS = ROOT / "tools"
README = ROOT / "README.md"

START = "<!-- AUTOGEN:TOOLS -->"
END = "<!-- /AUTOGEN:TOOLS -->"

# Categories render in this order; anything unrecognised is appended at the end.
ORDER = [
    "Keying & screens",
    "Edges & mattes",
    "Lens & distortion",
    "CG & deep",
    "Colour",
    "Light & atmosphere",
    "Workflow & QC",
]


def parse(md: pathlib.Path) -> dict | None:
    text = md.read_text(encoding="utf-8")
    title = re.search(r"^# (.+)$", text, re.M)
    summary = re.search(r"^> (.+)$", text, re.M)
    category = re.search(r"\*\*Category:\*\* ([^·\n]+)", text)
    if not (title and summary):
        print(f"  ! {md.name}: needs a '# Title' and a '> summary' line", file=sys.stderr)
        return None
    return {
        "name": title.group(1).strip(),
        "summary": summary.group(1).strip(),
        "category": category.group(1).strip() if category else "Other",
        "doc": f"docs/{md.name}",
    }


def main() -> int:
    entries = [e for e in (parse(p) for p in sorted(DOCS.glob("*.md"))) if e]

    missing = [p.stem for p in sorted(TOOLS.glob("*.nk"))
               if not (DOCS / f"{p.stem}.md").exists()]
    orphans = [e["name"] for e in entries if not (TOOLS / f"{e['name']}.nk").exists()]
    for m in missing:
        print(f"  ! tools/{m}.nk has no docs/{m}.md", file=sys.stderr)
    for o in orphans:
        print(f"  ! docs/{o}.md has no tools/{o}.nk", file=sys.stderr)

    by_cat: dict[str, list] = {}
    for e in entries:
        by_cat.setdefault(e["category"], []).append(e)

    cats = [c for c in ORDER if c in by_cat] + sorted(set(by_cat) - set(ORDER))

    out = []
    for cat in cats:
        out.append(f"### {cat}\n")
        out.append("| Tool | What it does |")
        out.append("| --- | --- |")
        for e in sorted(by_cat[cat], key=lambda x: x["name"]):
            out.append(f"| **[{e['name']}]({e['doc']})** | {e['summary']} |")
        out.append("")
    table = "\n".join(out).rstrip() + "\n"

    readme = README.read_text(encoding="utf-8")
    if START not in readme or END not in readme:
        print(f"error: {README.name} is missing the AUTOGEN markers", file=sys.stderr)
        return 1
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n\n{table}\n{END}",
        readme,
        flags=re.S,
    )
    README.write_text(new, encoding="utf-8")
    print(f"README.md updated — {len(entries)} tools in {len(cats)} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
