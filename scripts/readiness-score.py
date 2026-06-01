#!/usr/bin/env python3
"""AI-Readiness Score v2 — the metric behind the AI-Readiness Index.

Parses README.md (the single source of truth), de-duplicates entries,
enriches GitHub-hosted tools via the GitHub API, and computes an
AI-Readiness Score that rewards *agent-callability* over popularity.

Outputs:
  - READINESS.md          full ranked table + summary (human-facing)
  - data/readiness.json   machine-readable, citable data asset
  - data/readiness.csv    spreadsheet-friendly export

Score philosophy (max 100): a tool is "AI-ready" when an autonomous agent
can drive it without a GUI. So MCP/Python/CLI weigh far more than stars.

  mcp        35   has an MCP server (`MCP` tag)        — the differentiator
  python     25   native Python API (`Python` tag)
  cli_api    15   LLM/agent interface (`API` tag)
  maintained 15   pushed < 6 mo (15) / < 12 mo (8) / else 0
  adoption   10   log10(stars) scaled, capped          — popularity, on purpose small
  -----------------------------------------------------------------------
  Grades: AI-Native 75+ · Agent-Ready 50-74 · Scriptable 30-49 · Experimental <30

Non-GitHub entries (GitLab/self-hosted) have no stars/activity data; they are
scored on interface signals only and reported in a separate section rather
than mis-ranked at the bottom.
"""

import csv
import json
import math
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timezone

ROOT = os.path.join(os.path.dirname(__file__), "..")
README = os.path.join(ROOT, "README.md")
DATA_DIR = os.path.join(ROOT, "data")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"

# Sections that are not tool lists.
SKIP_SECTIONS = {"Contents", "Core Engine Readiness", "Contributing", "License"}

SECTION_RE = re.compile(r"^##\s+(.+?)\s*$")
# - [Name](URL) `tag` `tag` - Description.   (tags + description optional)
ENTRY_RE = re.compile(
    r"^- \[([^\]]+)\]\((https?://[^)]+)\)\s*((?:`[^`]+`\s*)*)(?:-\s*(.*))?$"
)
GITHUB_RE = re.compile(r"github\.com/([^/]+/[^/#?]+)")


def gh_get(path: str, retries: int = 3) -> dict | None:
    url = f"{API}{path}"
    for attempt in range(retries):
        req = urllib.request.Request(url)
        req.add_header("Accept", "application/vnd.github+json")
        if GITHUB_TOKEN:
            req.add_header("Authorization", f"Bearer {GITHUB_TOKEN}")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            # 403 → rate limit; back off and retry rather than silently zeroing.
            if e.code in (403, 429) and attempt < retries - 1:
                reset = e.headers.get("X-RateLimit-Reset")
                wait = 5
                if reset:
                    wait = max(1, int(reset) - int(time.time())) + 1
                print(f"    rate-limited, waiting {wait}s...", file=sys.stderr)
                time.sleep(min(wait, 60))
                continue
            return None
        except Exception:
            if attempt < retries - 1:
                time.sleep(2)
                continue
            return None
    return None


# Known PyPI package names that differ from the repo basename (reduces false
# negatives). Add here when the heuristic below misses a real package.
PYPI_OVERRIDES = {
    "google-deepmind/mujoco": "mujoco",
    "nvidia/warp": "warp-lang",
    "tum-pbs/phiflow": "phiflow",
    "nvidia/physicsnemo": "nvidia-physicsnemo",
    "anyoptimization/pymoo": "pymoo",
    "meta-pytorch/botorch": "botorch",
    "neuraloperator/neuraloperator": "neuraloperator",
}
_pypi_cache: dict[str, bool] = {}


def pypi_has(pkg: str) -> bool:
    if pkg in _pypi_cache:
        return _pypi_cache[pkg]
    try:
        req = urllib.request.Request(f"https://pypi.org/pypi/{pkg}/json")
        with urllib.request.urlopen(req, timeout=10) as resp:
            _pypi_cache[pkg] = resp.status == 200
    except Exception:
        _pypi_cache[pkg] = False
    return _pypi_cache[pkg]


def is_pip_installable(tool: dict) -> bool:
    """Conservative PyPI check: confirm a match, never penalise a miss.

    Only Python tools are checked. Tries an override map, then the repo
    basename and the display name as candidate package names.
    """
    if "python" not in [t.lower() for t in tool["tags"]]:
        return False
    candidates = []
    if tool["repo"]:
        key = tool["repo"].lower()
        if key in PYPI_OVERRIDES:
            candidates.append(PYPI_OVERRIDES[key])
        candidates.append(tool["repo"].split("/")[-1].lower())
    candidates.append(re.sub(r"[^a-z0-9]+", "-", tool["name"].lower()).strip("-"))
    for c in dict.fromkeys(c for c in candidates if c):
        if pypi_has(c):
            return True
    return False


def parse_readme(path: str) -> list[dict]:
    """Extract de-duplicated tool entries with their category membership."""
    by_key: dict[str, dict] = {}
    section = None
    with open(path) as f:
        for raw in f:
            line = raw.rstrip("\n")
            sec = SECTION_RE.match(line)
            if sec:
                section = sec.group(1).strip()
                continue
            if section in SKIP_SECTIONS or section is None:
                continue
            m = ENTRY_RE.match(line.strip())
            if not m:
                continue
            name, url, tags_raw, desc = m.groups()
            tags = re.findall(r"`([^`]+)`", tags_raw or "")
            gh = GITHUB_RE.search(url)
            repo = gh.group(1).rstrip("/") if gh else None
            # Category name is the short label before any em-dash.
            category = re.split(r"\s+[—–-]\s+", section)[0].strip()
            key = repo.lower() if repo else url.lower()
            if key in by_key:
                # Intentional double-link: merge categories, keep first entry.
                if category not in by_key[key]["categories"]:
                    by_key[key]["categories"].append(category)
                continue
            by_key[key] = {
                "name": name,
                "url": url,
                "repo": repo,
                "tags": tags,
                "categories": [category],
                "desc": (desc or "").strip().rstrip("."),
            }
    return list(by_key.values())


def score_tool(tool: dict) -> dict:
    tags = [t.lower() for t in tool["tags"]]
    has_mcp = "mcp" in tags
    has_python = "python" in tags
    has_cli_api = "api" in tags

    stars = None
    pushed = None
    months_ago = None
    if tool["repo"]:
        data = gh_get(f"/repos/{tool['repo']}")
        if data:
            stars = data.get("stargazers_count", 0)
            pushed = (data.get("pushed_at") or "")[:10]
            if pushed:
                pushed_dt = datetime.fromisoformat(pushed + "T00:00:00+00:00")
                months_ago = (datetime.now(timezone.utc) - pushed_dt).days / 30

    # Component scores
    s_mcp = 35 if has_mcp else 0
    s_python = 25 if has_python else 0
    s_cli = 15 if has_cli_api else 0
    if months_ago is None:
        s_maint = 0
    elif months_ago < 6:
        s_maint = 15
    elif months_ago < 12:
        s_maint = 8
    else:
        s_maint = 0
    s_adopt = 0 if not stars else min(math.log10(stars + 1) / 4 * 10, 10)

    # pip-installability: additive bonus (v2.1). Lifts confirmed-PyPI tools;
    # a miss never scores worse than v2.0 (no penalty), so PyPI false negatives
    # add no public-ranking noise.
    has_pip = is_pip_installable(tool)
    s_pip = 15 if has_pip else 0

    total = round(s_mcp + s_python + s_cli + s_maint + s_adopt + s_pip)
    total = min(total, 100)

    if total >= 75:
        grade = "AI-Native"
    elif total >= 50:
        grade = "Agent-Ready"
    elif total >= 30:
        grade = "Scriptable"
    else:
        grade = "Experimental"

    return {
        **tool,
        "stars": stars,
        "last_push": pushed,
        "score": total,
        "grade": grade,
        "has_github_metrics": tool["repo"] is not None and stars is not None,
        "signals": {
            "mcp": has_mcp,
            "python": has_python,
            "cli_api": has_cli_api,
            "pip": has_pip,
            "maintained_score": s_maint,
            "adoption_score": round(s_adopt, 1),
        },
    }


GRADE_EMOJI = {
    "AI-Native": "🟢",
    "Agent-Ready": "🔵",
    "Scriptable": "🟡",
    "Experimental": "⚪",
}


def iface_badges(t: dict) -> str:
    b = []
    if t["signals"]["mcp"]:
        b.append("MCP")
    if t["signals"]["python"]:
        b.append("Py")
    if t["signals"]["cli_api"]:
        b.append("API")
    if t["signals"]["pip"]:
        b.append("pip")
    out = " ".join(f"`{x}`" for x in b) or "—"
    if t["signals"].get("verified"):
        out += " ✅"
    return out


def write_readiness_md(ranked: list[dict], partial: list[dict], now: str) -> None:
    lines = [
        "# AI-Readiness Scores",
        "",
        f"> Auto-generated on {now} by [`readiness-score.py`](scripts/readiness-score.py).",
        "> Ranks tools by **agent-callability** (MCP / Python / CLI / maintenance), not popularity.",
        "> Machine-readable: [`data/readiness.json`](data/readiness.json) · [`data/readiness.csv`](data/readiness.csv)",
        "",
        "| # | Score | Grade | Tool | Interfaces | ⭐ | Last Push |",
        "|--:|------:|-------|------|------------|--:|-----------|",
    ]
    for i, t in enumerate(ranked, 1):
        stars = f"{t['stars']:,}" if t["stars"] is not None else "—"
        lines.append(
            f"| {i} | {t['score']} | {GRADE_EMOJI[t['grade']]} {t['grade']} "
            f"| [{t['name']}]({t['url']}) | {iface_badges(t)} "
            f"| {stars} | {t['last_push'] or '—'} |"
        )

    grades: dict[str, int] = {}
    for t in ranked:
        grades[t["grade"]] = grades.get(t["grade"], 0) + 1
    lines += [
        "",
        "## Summary",
        "",
        f"- **Tools ranked**: {len(ranked)}",
        f"- 🟢 **AI-Native (75+)**: {grades.get('AI-Native', 0)}",
        f"- 🔵 **Agent-Ready (50-74)**: {grades.get('Agent-Ready', 0)}",
        f"- 🟡 **Scriptable (30-49)**: {grades.get('Scriptable', 0)}",
        f"- ⚪ **Experimental (<30)**: {grades.get('Experimental', 0)}",
    ]
    if partial:
        lines += [
            "",
            "## Interface-tagged (metrics unavailable)",
            "",
            "> Non-GitHub hosts (GitLab/self-hosted) — scored on interface tags only.",
            "",
        ]
        for t in partial:
            lines.append(f"- [{t['name']}]({t['url']}) — {iface_badges(t)}")
    lines.append("")
    with open(os.path.join(ROOT, "READINESS.md"), "w") as f:
        f.write("\n".join(lines))


INDEX_START = "<!-- AI-READINESS-INDEX:START -->"
INDEX_END = "<!-- AI-READINESS-INDEX:END -->"
TOP_N = 15


def inject_readme_index(ranked: list[dict], now: str) -> bool:
    """Replace the region between the index markers in README.md with a
    freshly generated Top-N leaderboard. Returns False if markers absent."""
    with open(README) as f:
        content = f.read()
    if INDEX_START not in content or INDEX_END not in content:
        print("    README index markers not found — skipping injection", file=sys.stderr)
        return False

    rows = ["<table>", '<tr><th align="center">#</th><th align="right">Score</th><th>Grade</th><th>Tool</th><th>Interfaces</th><th align="right">⭐</th></tr>']
    medals = {1: "🥇", 2: "🥈", 3: "🥉"}
    for i, t in enumerate(ranked[:TOP_N], 1):
        rank = medals.get(i, str(i))
        stars = f"{t['stars']:,}" if t["stars"] is not None else "—"
        ifaces = ", ".join(
            x for x, on in (("MCP", t["signals"]["mcp"]), ("Python", t["signals"]["python"]), ("CLI/API", t["signals"]["cli_api"]), ("pip", t["signals"]["pip"])) if on
        ) or "—"
        if t["signals"].get("verified"):
            ifaces += ' <b title="install + import smoke-tested">✅</b>'
        rows.append(
            f'<tr><td align="center">{rank}</td><td align="right"><b>{t["score"]}</b></td>'
            f'<td>{GRADE_EMOJI[t["grade"]]} {t["grade"]}</td>'
            f'<td><a href="{t["url"]}">{t["name"]}</a></td>'
            f"<td>{ifaces}</td><td align=\"right\">{stars}</td></tr>"
        )
    rows.append("</table>")

    grades: dict[str, int] = {}
    for t in ranked:
        grades[t["grade"]] = grades.get(t["grade"], 0) + 1
    dist = (
        f"\n<sub>🟢 {grades.get('AI-Native', 0)} AI-Native · "
        f"🔵 {grades.get('Agent-Ready', 0)} Agent-Ready · "
        f"🟡 {grades.get('Scriptable', 0)} Scriptable · "
        f"⚪ {grades.get('Experimental', 0)} Experimental — across {len(ranked)} ranked tools "
        f"(updated {now}). ✅ = install + import <a href=\"data/verified.json\">execution-verified</a>. "
        f"<a href=\"READINESS.md\">Full ranking →</a></sub>\n"
    )

    block = f"{INDEX_START}\n\n" + "\n".join(rows) + "\n" + dist + f"\n{INDEX_END}"
    pre = content.split(INDEX_START)[0]
    post = content.split(INDEX_END)[1]
    with open(README, "w") as f:
        f.write(pre + block + post)
    print(f"    Injected Top-{TOP_N} index into README.md", file=sys.stderr)
    return True


def write_data(all_scored: list[dict], now: str) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)
    payload = {
        "generated": now,
        "methodology": "AI-Readiness Score v2.1: mcp35 python25 cli15 maintained15 adoption10 + pip15 bonus (capped 100)",
        "count": len(all_scored),
        "tools": [
            {
                "name": t["name"],
                "url": t["url"],
                "repo": t["repo"],
                "categories": t["categories"],
                "score": t["score"],
                "grade": t["grade"],
                "stars": t["stars"],
                "last_push": t["last_push"],
                "signals": t["signals"],
            }
            for t in all_scored
        ],
    }
    with open(os.path.join(DATA_DIR, "readiness.json"), "w") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    with open(os.path.join(DATA_DIR, "readiness.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["score", "grade", "name", "repo", "categories", "stars", "last_push", "mcp", "python", "cli_api", "pip"])
        for t in all_scored:
            w.writerow([
                t["score"], t["grade"], t["name"], t["repo"] or "",
                "|".join(t["categories"]), t["stars"] if t["stars"] is not None else "",
                t["last_push"] or "", t["signals"]["mcp"], t["signals"]["python"], t["signals"]["cli_api"], t["signals"]["pip"],
            ])


def load_verified() -> set[str]:
    """Repos/names that passed the execution smoke-test (data/verified.json)."""
    path = os.path.join(DATA_DIR, "verified.json")
    try:
        with open(path) as f:
            data = json.load(f)
    except Exception:
        return set()
    return {r["name"].lower() for r in data.get("results", []) if r.get("verified")}


def main() -> None:
    tools = parse_readme(README)
    print(f"Parsed {len(tools)} unique tool entries from README.md", file=sys.stderr)

    verified = load_verified()
    scored = []
    for i, tool in enumerate(tools):
        result = score_tool(tool)
        keys = {(result["repo"] or "").lower(), result["name"].lower()}
        result["signals"]["verified"] = bool(keys & verified)
        scored.append(result)
        print(
            f"  [{i + 1}/{len(tools)}] {result['name']}: {result['score']} ({result['grade']})",
            file=sys.stderr,
        )

    ranked = sorted(
        [t for t in scored if t["has_github_metrics"]],
        key=lambda x: (-x["score"], -(x["stars"] or 0), x["name"].lower()),
    )
    partial = [t for t in scored if not t["has_github_metrics"]]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    write_readiness_md(ranked, partial, now)
    write_data(scored, now)
    inject_readme_index(ranked, now)
    print(
        f"\nWrote READINESS.md ({len(ranked)} ranked, {len(partial)} partial) "
        f"+ data/readiness.json + data/readiness.csv",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
