#!/bin/bash
# 自動同步 AI 研究筆記到 GitHub + Google Drive
# 用法: ./sync.sh 或 ./sync.sh "commit message"

cd ~/.openclaw/workspace/research/youtube_summaries

MSG="${1:-Auto sync: $(date '+%Y-%m-%d %H:%M')}"

echo "📝 同步中..."

# 1. 推到 GitHub
git add -A
git commit -m "$MSG" 2>/dev/null
if git push origin main 2>&1; then
    echo "✅ GitHub 同步完成"
else
    echo "⚠️ GitHub 沒有新變更或推送失敗"
fi

# 2. 同步到 Google Drive
if rclone sync . gdrive:AI-Research-Notes --exclude ".git/**" 2>&1; then
    echo "✅ Google Drive 同步完成"
else
    echo "❌ Google Drive 同步失敗"
fi

echo "🎉 完成！"
