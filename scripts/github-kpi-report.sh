#!/usr/bin/env bash
# awesome-ai-cae GitHub KPI Daily Report → Telegram
set -euo pipefail

REPO="kimimgo/awesome-ai-cae"
SEND="$HOME/.claude/scripts/telegram-send.sh"

# Fetch repo stats
STATS=$(gh api "repos/$REPO" --jq '{stars: .stargazers_count, forks: .forks_count, watchers: .subscribers_count, issues: .open_issues_count}')
STARS=$(echo "$STATS" | jq -r '.stars')
FORKS=$(echo "$STATS" | jq -r '.forks')
WATCHERS=$(echo "$STATS" | jq -r '.watchers')
ISSUES=$(echo "$STATS" | jq -r '.issues')

# Entry count from README
ENTRIES=$(curl -s "https://raw.githubusercontent.com/$REPO/main/README.md" | grep -c "^- \[" || echo "?")

# Recent commits (7 days)
COMMITS_7D=$(gh api "repos/$REPO/commits?since=$(date -d '7 days ago' -Iseconds)&per_page=100" --jq 'length')

# Open PRs
OPEN_PRS=$(gh api "repos/$REPO/pulls?state=open" --jq 'length')

# Cross-PR status
PR_SCI=$(gh api "repos/nschloe/awesome-scientific-computing/pulls?state=all&head=kimimgo:add-awesome-ai-cae" --jq '.[0] | "\(.state) \(.merged_at // "not merged")"' 2>/dev/null || echo "unknown")
PR_ML=$(gh api "repos/josephmisiti/awesome-machine-learning/pulls?state=all&head=kimimgo:add-awesome-ai-cae" --jq '.[0] | "\(.state) \(.merged_at // "not merged")"' 2>/dev/null || echo "unknown")

# Traffic (needs push access)
VIEWS_14D=$(gh api "repos/$REPO/traffic/views" --jq '.count' 2>/dev/null || echo "?")
CLONES_14D=$(gh api "repos/$REPO/traffic/clones" --jq '.count' 2>/dev/null || echo "?")
REFERRERS=$(gh api "repos/$REPO/traffic/popular/referrers" --jq '[.[] | "\(.referrer): \(.count)"] | join(", ")' 2>/dev/null || echo "?")

# Days since creation
CREATED="2026-03-13"
DAYS=$(( ($(date +%s) - $(date -d "$CREATED" +%s)) / 86400 ))

# Build message
MSG="<b>📊 awesome-ai-cae KPI (D+${DAYS})</b>

<b>Core Metrics</b>
⭐ Stars: <b>${STARS}</b>
🍴 Forks: ${FORKS}
👀 Watchers: ${WATCHERS}
📋 Entries: ${ENTRIES}
🔀 Open PRs: ${OPEN_PRS}
📝 Issues: ${ISSUES}

<b>Traffic (14d)</b>
👁 Views: ${VIEWS_14D}
📥 Clones: ${CLONES_14D}
🔗 Referrers: ${REFERRERS}

<b>Activity (7d)</b>
📦 Commits: ${COMMITS_7D}

<b>Cross-PRs</b>
• awesome-scientific-computing: ${PR_SCI}
• awesome-machine-learning: ${PR_ML}

<b>Goals</b>
⭐ 100 stars (${STARS}/100) — $(( STARS * 100 / 100 ))%
📅 sindresorhus/awesome registration — D+30 ($(( 30 - DAYS ))d left)"

$SEND --quiet send "$MSG"
