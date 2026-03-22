# 📹 影片摘要 SOP

> 收到新影片時，照這個流程走。

---

## 流程

### Step 1：收到影片
軒哥在 **#影音轉檔** 頻道丟影片連結（YouTube / Bilibili / 其他）

### Step 2：下載 & 轉錄
```bash
# YouTube
yt-dlp -x --audio-format mp3 -o "/tmp/%(title)s.%(ext)s" "<URL>"

# Bilibili（需要 cookies）
yt-dlp --cookies-from-browser chrome -x --audio-format mp3 -o "/tmp/%(title)s.%(ext)s" "<URL>"
```

### Step 3：Whisper 轉錄
```bash
cd projects/discord-voice-bot && source venv/bin/activate
python3 -c "
from openai import OpenAI
client = OpenAI(api_key=open('.env').read().split('OPENAI_API_KEY=')[1].split('\n')[0])
with open('/tmp/audio.mp3','rb') as f:
    result = client.audio.transcriptions.create(model='whisper-1', file=f, language='zh')
    print(result.text)
"
```

### Step 4：生成摘要 .md
格式模板：
```markdown
# [影片標題]

> **影片連結**: [URL]
> **頻道**: [頻道名稱]
> **日期**: YYYY-MM-DD
> **時長**: 約 X 分鐘

---

## 重點摘要

### 1. [主題一]
- 要點
- 要點

### 2. [主題二]
- 要點

---

## 關鍵金句
> "引述原文"

## 行動建議
- [ ] 具體行動 1
- [ ] 具體行動 2
```

### Step 5：歸檔
- **檔名格式**: `YYYYMMDD-簡短標題.md`
- **存放位置**: 根據來源頻道放到對應資料夾

| 來源 | 路徑 |
|------|------|
| 已有頻道 | `youtubers/<頻道名>/` |
| B站雜項 | `youtubers/misc_bilibili/` |
| 系列專題 | `series/<系列名>/` |
| 研究報告 | `research/` |
| 新頻道 | 建新資料夾 `youtubers/<新頻道>/` |

### Step 6：更新索引
```bash
cd /home/ysi/.openclaw/workspace/research/youtube_summaries
python3 /tmp/organize_repo.py
```
> 腳本會自動掃描所有 .md，重新生成 INDEX.md

### Step 7：推送
```bash
git add -A
git commit -m "新增：[影片標題] 摘要"
git push
```

---

## 分類標籤（自動偵測）

| 標籤 | 關鍵字 |
|------|--------|
| AI Agent | agent, 智能體 |
| 量化交易 | quant, trading, macd, 股票 |
| AI 工具 | claude, gemini, gpt, 工具 |
| AI 編程 | code, coding, python, github |
| 健康 | 斷食, 飲食, diet, vitamin, berg |
| 創業 | startup, saas, business |
| 心理/自我成長 | mindset, motivation, 成長 |
| 設計/UI | design, ui, ux, figma |
| 影片生成 | video generation, sora, kling |
| 簡報 | presentation, ppt, slides |
| 教育 | education, 學習, 聯考 |
| 自動化 | automation, workflow, n8n |
| SEO/行銷 | seo, marketing, 行銷 |

---

## 頻道對應表

| 頻道名稱 | 資料夾 | 平台 |
|----------|--------|------|
| AI-seeker | `aiseeker_bilibili` | B站 |
| AI超元域 | `aisuperdomain` / `aisuperdomain_bilibili` | YT / B站 |
| Alan UI Design | `alan_design` | YT |
| BRAINY DOSE | `brainydose` | YT |
| Dan Koe | `dankoe` | YT |
| Dan Martell | `dan_martell` | YT |
| Dr. Berg 中文 | `drberg_chinese` | YT |
| GeekyHour | `geekhour` | B站 |
| In The World of AI | `intheworldofai` | YT |
| Liam Ottley | `liam_ottley` | YT |
| Pragmatic Engineer | `pragmatic_engineer` | YT |
| 秋芝2046 | `qiuzhi2046_bilibili` | B站 |
| Simon Sinek | `simon_sinek` | YT |
| Tech With Tim | `tech_with_tim` | YT |
| Y Combinator | `ycombinator` | YT |
| 其他/散件 | `misc_bilibili` | B站/其他 |

---

*最後更新：2026-03-22*
