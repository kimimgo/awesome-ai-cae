#!/usr/bin/env bash
# awesome-ai-cae KPI Collector — DB 저장 + Telegram 보고
set -euo pipefail

REPO="kimimgo/awesome-ai-cae"
SEND="$HOME/.claude/scripts/telegram-send.sh"
PSQL="docker exec pgvector-memory psql -U memory_admin -d central_memory -tAc"
CREATED="2026-03-13"
DAYS=$(( ($(date +%s) - $(date -d "$CREATED" +%s)) / 86400 ))

# === 1. Collect metrics ===

# Core
STARS=$(gh api "repos/$REPO" --jq '.stargazers_count')
FORKS=$(gh api "repos/$REPO" --jq '.forks_count')
WATCHERS=$(gh api "repos/$REPO" --jq '.subscribers_count')
OPEN_ISSUES=$(gh api "repos/$REPO" --jq '.open_issues_count')
ENTRIES=$(curl -s "https://raw.githubusercontent.com/$REPO/main/README.md" | grep -c "^- \[" || echo 0)

# Traffic
VIEWS_14D=$(gh api "repos/$REPO/traffic/views" --jq '.count' 2>/dev/null || echo 0)
VIEWS_UNQ=$(gh api "repos/$REPO/traffic/views" --jq '.uniques' 2>/dev/null || echo 0)
CLONES_14D=$(gh api "repos/$REPO/traffic/clones" --jq '.count' 2>/dev/null || echo 0)
CLONES_UNQ=$(gh api "repos/$REPO/traffic/clones" --jq '.uniques' 2>/dev/null || echo 0)
REFERRERS=$(gh api "repos/$REPO/traffic/popular/referrers" 2>/dev/null || echo '[]')

# Activity
COMMITS_7D=$(gh api "repos/$REPO/commits?since=$(date -d '7 days ago' -Iseconds)&per_page=100" --jq 'length' 2>/dev/null || echo 0)
OPEN_PRS=$(gh api "repos/$REPO/pulls?state=open" --jq 'length' 2>/dev/null || echo 0)

# Cross-PRs
PR_SCI=$(gh api "repos/nschloe/awesome-scientific-computing/pulls/105" --jq '.state' 2>/dev/null || echo "unknown")
PR_ML=$(gh api "repos/josephmisiti/awesome-machine-learning/pulls/1134" --jq '.state' 2>/dev/null || echo "unknown")

# Maintainer reactions
MAINT_COMMENTS=0
MAINT_REACTIONS=0
MAINT_DETAILS='[]'
MAINT_JSON="["
FIRST=true
for pair in "csml-rpi/Foam-Agent/19" "Terry-cyx/MetaOpenFOAM/12" "dynamicslab/pysindy/687" "llnl/paraview_mcp/5" "neuraloperator/neuraloperator/716" "mathLab/PINA/776" "Koopman-Laboratory/KoopmanLab/11" "rezaakb/pinns-torch/24" "NeuroDiffGym/neurodiffeq/228" "i207M/PINNacle/15" "PolymathicAI/the_well/82"; do
  owner_repo="${pair%/*}"
  num="${pair##*/}"
  c=$(gh api "repos/$owner_repo/issues/$num" --jq '.comments' 2>/dev/null || echo 0)
  r=$(gh api "repos/$owner_repo/issues/$num/reactions" --jq 'length' 2>/dev/null || echo 0)
  s=$(gh api "repos/$owner_repo/issues/$num" --jq '.state' 2>/dev/null || echo "unknown")
  MAINT_COMMENTS=$((MAINT_COMMENTS + c))
  MAINT_REACTIONS=$((MAINT_REACTIONS + r))
  $FIRST || MAINT_JSON+=","
  FIRST=false
  MAINT_JSON+="{\"repo\":\"$owner_repo\",\"issue\":$num,\"state\":\"$s\",\"comments\":$c,\"reactions\":$r}"
done
MAINT_JSON+="]"

# === 2. Previous day comparison ===
PREV_STARS=$($PSQL "SELECT stars FROM awesome_ai_cae_kpi ORDER BY collected_at DESC LIMIT 1" 2>/dev/null || echo "$STARS")
PREV_VIEWS=$($PSQL "SELECT views_14d FROM awesome_ai_cae_kpi ORDER BY collected_at DESC LIMIT 1" 2>/dev/null || echo "$VIEWS_14D")
PREV_CLONES=$($PSQL "SELECT clones_14d FROM awesome_ai_cae_kpi ORDER BY collected_at DESC LIMIT 1" 2>/dev/null || echo "$CLONES_14D")
PREV_MAINT_C=$($PSQL "SELECT maintainer_total_comments FROM awesome_ai_cae_kpi ORDER BY collected_at DESC LIMIT 1" 2>/dev/null || echo "0")

DIFF_STARS=$((STARS - PREV_STARS))
DIFF_VIEWS=$((VIEWS_14D - PREV_VIEWS))
DIFF_CLONES=$((CLONES_14D - PREV_CLONES))
DIFF_MAINT=$((MAINT_COMMENTS - PREV_MAINT_C))

# Delta formatting
fmt_delta() { local v=$1; [[ $v -gt 0 ]] && echo "+$v" || echo "$v"; }

# === 3. Store in DB ===
REFERRERS_ESCAPED=$(echo "$REFERRERS" | sed "s/'/''/g")
MAINT_JSON_ESCAPED=$(echo "$MAINT_JSON" | sed "s/'/''/g")

$PSQL "INSERT INTO awesome_ai_cae_kpi (
  stars, forks, watchers, open_issues, entries,
  views_14d, views_unique_14d, clones_14d, clones_unique_14d, referrers,
  commits_7d, open_prs,
  pr_sci_computing, pr_machine_learning,
  maintainer_total_comments, maintainer_total_reactions, maintainer_details
) VALUES (
  $STARS, $FORKS, $WATCHERS, $OPEN_ISSUES, $ENTRIES,
  $VIEWS_14D, $VIEWS_UNQ, $CLONES_14D, $CLONES_UNQ, '$REFERRERS_ESCAPED'::jsonb,
  $COMMITS_7D, $OPEN_PRS,
  '$PR_SCI', '$PR_ML',
  $MAINT_COMMENTS, $MAINT_REACTIONS, '$MAINT_JSON_ESCAPED'::jsonb
);" 2>/dev/null

# === 4. Telegram report ===
# Referrer summary
REF_SUMMARY=$(echo "$REFERRERS" | python3 -c "
import sys,json
try:
  refs = json.load(sys.stdin)
  print(' | '.join(f'{r[\"referrer\"]}: {r[\"count\"]}' for r in refs[:5]) or 'none')
except: print('none')
")

# Active maintainer issues (comments > 0)
ACTIVE_MAINT=$(echo "$MAINT_JSON" | python3 -c "
import sys,json
try:
  items = json.load(sys.stdin)
  active = [f'{i[\"repo\"]}#{i[\"issue\"]}({i[\"comments\"]}c)' for i in items if i['comments']>0]
  print(', '.join(active) if active else 'none yet')
except: print('error')
")

MSG="<b>📊 awesome-ai-cae Daily KPI (D+${DAYS})</b>

<b>Core</b>
⭐ Stars: <b>${STARS}</b> ($(fmt_delta $DIFF_STARS))
🍴 Forks: ${FORKS}
👀 Watchers: ${WATCHERS}
📋 Entries: ${ENTRIES}

<b>Traffic (14d)</b>
👁 Views: ${VIEWS_14D} ($(fmt_delta $DIFF_VIEWS)) | uniq ${VIEWS_UNQ}
📥 Clones: ${CLONES_14D} ($(fmt_delta $DIFF_CLONES)) | uniq ${CLONES_UNQ}
🔗 Referrers: ${REF_SUMMARY}

<b>Activity (7d)</b>
📦 Commits: ${COMMITS_7D} | PRs: ${OPEN_PRS}

<b>Cross-PRs</b>
• awesome-sci-computing #105: ${PR_SCI}
• awesome-ml #1134: ${PR_ML}

<b>Maintainer Outreach (11)</b>
💬 Comments: ${MAINT_COMMENTS} ($(fmt_delta $DIFF_MAINT)) | 👍 Reactions: ${MAINT_REACTIONS}
📣 Active: ${ACTIVE_MAINT}

<b>Goals</b>
⭐ 100 stars: ${STARS}/100 ($(( STARS * 100 / 100 ))%)
📅 sindresorhus/awesome: D+30 ($(( 30 - DAYS ))d left)"

$SEND --quiet send "$MSG"
