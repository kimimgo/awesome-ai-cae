#!/usr/bin/env python3
"""Auto-ranking for PRs: score the tool entries a PR adds to README.md.

Diffs README against the base ref, finds added list-item entries, computes
each one's AI-Readiness Score with the same engine as the weekly ranking,
and prints a Markdown comment to stdout. Used by .github/workflows/pr-readiness.yml
so a contributor sees their tool's score the moment they open a PR.

Usage: pr_score_comment.py [base_ref]   (default: origin/main)
"""

import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Load the scoring engine (filename has a hyphen → import via importlib).
_spec = importlib.util.spec_from_file_location(
    "readiness_score", os.path.join(HERE, "readiness-score.py")
)
rs = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rs)

MARKER = "<!-- ai-readiness-pr-bot -->"


def added_entry_lines(base_ref: str) -> list[str]:
    """Return README list-item lines added by this PR (without the leading +)."""
    try:
        diff = subprocess.run(
            ["git", "diff", f"{base_ref}...HEAD", "--", "README.md"],
            capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        return []
    out = []
    for line in diff.splitlines():
        if line.startswith("+- [") and not line.startswith("+++"):
            out.append(line[1:])  # strip diff '+'
    return out


def parse_line(line: str) -> dict | None:
    m = rs.ENTRY_RE.match(line.strip())
    if not m:
        return None
    name, url, tags_raw, desc = m.groups()
    gh = rs.GITHUB_RE.search(url)
    return {
        "name": name,
        "url": url,
        "repo": gh.group(1).rstrip("/") if gh else None,
        "tags": re.findall(r"`([^`]+)`", tags_raw or ""),
        "categories": [],
        "desc": (desc or "").strip().rstrip("."),
    }


def main() -> None:
    base = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    lines = added_entry_lines(base)
    tools = [t for t in (parse_line(ln) for ln in lines) if t]

    print(MARKER)
    if not tools:
        print("🤖 **AI-Readiness bot** — no new tool entries detected in this PR.")
        return

    scored = [rs.score_tool(t) for t in tools]
    scored.sort(key=lambda x: -x["score"])

    print("🤖 **AI-Readiness bot** — computed scores for the tools this PR adds:\n")
    print("| Tool | Score | Grade | Interfaces | ⭐ |")
    print("|------|------:|-------|------------|--:|")
    for t in scored:
        stars = f"{t['stars']:,}" if t["stars"] is not None else "—"
        print(
            f"| [{t['name']}]({t['url']}) | **{t['score']}** "
            f"| {rs.GRADE_EMOJI[t['grade']]} {t['grade']} "
            f"| {rs.iface_badges(t)} | {stars} |"
        )
    print(
        "\n<sub>Score = agent-callability (MCP 35 · Python 25 · CLI/API 15 · "
        "maintained 15 · adoption 10 · +pip 15 bonus). Merged entries are "
        "re-ranked into [READINESS.md](../blob/main/READINESS.md) weekly.</sub>"
    )


if __name__ == "__main__":
    main()
