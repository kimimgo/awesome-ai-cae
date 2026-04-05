#!/usr/bin/env python3
"""AI-Readiness Score v1 — GitHub API only.

Parses README.md, extracts GitHub tool URLs, queries GitHub API for
stars and last-commit date, computes a simple readiness score, and
outputs a Markdown report.

Score formula (v1, GitHub-only):
  stars_score   = min(stars / 100, 25)        # max 25
  activity      = 15 if < 6 months, 8 if < 12, 0 if stale
  has_python    = 10 if 'Python' tag in entry
  has_cli       = 10 if CLI/headless mentioned
  has_mcp       = 25 if 'MCP' tag in entry
  has_package   = 15 if pip-installable (TODO v2)
  ---
  Total max = 100
"""

import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone

README = os.path.join(os.path.dirname(__file__), "..", "README.md")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"


def gh_get(path: str) -> dict | None:
    url = f"{API}{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    if GITHUB_TOKEN:
        req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except Exception:
        return None


def parse_tools(readme_path: str) -> list[dict]:
    """Extract tool entries from README.md list items."""
    pattern = re.compile(
        r"^- \[([^\]]+)\]\((https?://github\.com/([^/)]+/[^/)]+))[^)]*\)"
        r"\s*(`[^`]+`(?:\s*`[^`]+`)*)\s*-\s*(.+)$"
    )
    tools = []
    with open(readme_path) as f:
        for line in f:
            m = pattern.match(line.strip())
            if not m:
                continue
            name, url, repo, tags_raw, desc = m.groups()
            tags = re.findall(r"`([^`]+)`", tags_raw)
            tools.append(
                {
                    "name": name,
                    "url": url,
                    "repo": repo,
                    "tags": tags,
                    "desc": desc.strip().rstrip("."),
                }
            )
    return tools


def score_tool(tool: dict) -> dict:
    """Query GitHub API and compute readiness score."""
    repo_data = gh_get(f"/repos/{tool['repo']}")
    if not repo_data:
        return {**tool, "stars": 0, "last_push": "unknown", "score": 0, "grade": "?"}

    stars = repo_data.get("stargazers_count", 0)
    pushed = repo_data.get("pushed_at", "")
    tags = [t.lower() for t in tool["tags"]]

    # Stars score (max 25)
    stars_score = min(stars / 100, 25)

    # Activity score (max 15)
    activity = 0
    if pushed:
        pushed_dt = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
        months_ago = (datetime.now(timezone.utc) - pushed_dt).days / 30
        if months_ago < 6:
            activity = 15
        elif months_ago < 12:
            activity = 8

    # Python API (max 10)
    has_python = 10 if "python" in tags else 0

    # CLI/headless (max 10)
    has_cli = 10 if any(t in tags for t in ("api", "cli")) else 0

    # MCP (max 25)
    has_mcp = 25 if "mcp" in tags else 0

    # Package (max 15) — v2 will check PyPI
    has_package = 15 if "python" in tags else 0

    total = int(stars_score + activity + has_python + has_cli + has_mcp + has_package)
    total = min(total, 100)

    if total >= 80:
        grade = "AI-Native"
    elif total >= 50:
        grade = "API-Ready"
    elif total >= 20:
        grade = "ML-Powered"
    else:
        grade = "Not Ready"

    return {
        **tool,
        "stars": stars,
        "last_push": pushed[:10] if pushed else "unknown",
        "score": total,
        "grade": grade,
    }


def generate_report(scored: list[dict]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        "# AI-Readiness Scores",
        "",
        f"> Auto-generated on {now} by [`readiness-score.py`](scripts/readiness-score.py).",
        "> Methodology: [Issue #2](https://github.com/kimimgo/awesome-ai-cae/issues/2)",
        "",
        "| Score | Grade | Tool | ⭐ Stars | Last Push | Tags |",
        "|------:|-------|------|--------:|-----------|------|",
    ]

    for t in sorted(scored, key=lambda x: x["score"], reverse=True):
        tags_str = ", ".join(f"`{tag}`" for tag in t["tags"][:3])
        lines.append(
            f"| {t['score']} | {t['grade']} "
            f"| [{t['name']}]({t['url']}) "
            f"| {t['stars']:,} | {t['last_push']} | {tags_str} |"
        )

    # Summary stats
    grades = {}
    for t in scored:
        grades[t["grade"]] = grades.get(t["grade"], 0) + 1

    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- **Total tools scored**: {len(scored)}",
            f"- **AI-Native (80+)**: {grades.get('AI-Native', 0)}",
            f"- **API-Ready (50-79)**: {grades.get('API-Ready', 0)}",
            f"- **ML-Powered (20-49)**: {grades.get('ML-Powered', 0)}",
            f"- **Not Ready (<20)**: {grades.get('Not Ready', 0)}",
            "",
            "## Stale Tools (>12 months inactive)",
            "",
        ]
    )

    stale = [t for t in scored if t.get("last_push", "unknown") != "unknown"]
    stale = [
        t
        for t in stale
        if (
            datetime.now(timezone.utc)
            - datetime.fromisoformat(t["last_push"] + "T00:00:00+00:00")
        ).days
        > 365
    ]
    if stale:
        for t in stale:
            lines.append(f"- [{t['name']}]({t['url']}) — last push {t['last_push']}")
    else:
        lines.append("None detected.")

    lines.append("")
    return "\n".join(lines)


def main():
    tools = parse_tools(README)
    print(f"Found {len(tools)} GitHub tools in README.md", file=sys.stderr)

    scored = []
    for i, tool in enumerate(tools):
        result = score_tool(tool)
        scored.append(result)
        print(
            f"  [{i + 1}/{len(tools)}] {result['name']}: {result['score']} ({result['grade']})",
            file=sys.stderr,
        )

    report = generate_report(scored)

    out_path = os.path.join(os.path.dirname(__file__), "..", "READINESS.md")
    with open(out_path, "w") as f:
        f.write(report)
    print(f"\nReport written to READINESS.md ({len(scored)} tools)", file=sys.stderr)


if __name__ == "__main__":
    main()
