#!/usr/bin/env python3
"""批次處理 YC 頻道影片 - 單次執行一支"""
import subprocess
import json
import urllib.request
import time
import os
import re
import sys

WORK_DIR = os.path.expanduser("~/.openclaw/workspace/research/youtube_summaries")
YT_DLP = "/tmp/yt-dlp-new"
GEMINI_KEY = "AIzaSyApwdWgaITpJHZ2PXuB3UxpnrwSSnCApZ8"
OUTPUT_DIR = os.path.join(WORK_DIR, "youtubers/ycombinator")

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:45].strip('-')

def download_subtitle(video_id):
    os.chdir(WORK_DIR)
    # 清理舊檔案
    for f in ["temp_sub.en.srt", "temp_sub.en.vtt"]:
        if os.path.exists(f):
            os.remove(f)
    
    cmd = f'{YT_DLP} --write-auto-sub --sub-lang en --skip-download --convert-subs srt -o "temp_sub" "https://www.youtube.com/watch?v={video_id}"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=90)
    
    srt_file = "temp_sub.en.srt"
    if os.path.exists(srt_file):
        with open(srt_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        os.remove(srt_file)
        
        lines = content.split('\n')
        seen = set()
        clean_lines = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            if re.match(r'^\d+$', line):
                continue
            if '-->' in line:
                continue
            if line not in seen:
                seen.add(line)
                clean_lines.append(line)
        
        return ' '.join(clean_lines)[:15000]
    return None

def summarize_with_gemini(title, video_id, transcript):
    prompt = f"""你是專業的 YouTube 影片摘要專家。請根據以下影片字幕，用繁體中文撰寫完整摘要。

影片標題：{title}
影片連結：https://www.youtube.com/watch?v={video_id}

請按以下格式輸出：

# 標題（中文翻譯）

## 影片資訊
- 原標題：{title}
- 連結：https://www.youtube.com/watch?v={video_id}
- 頻道：Y Combinator

## 核心觀點（3-5 個重點）

## 詳細內容摘要（500-800 字）

## 關鍵語錄（2-3 句原文+翻譯）

## 我的評論（對創業者/開發者的啟發）

---

字幕內容：
{transcript}"""

    data = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.3, "maxOutputTokens": 2048}
    }

    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_KEY}",
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )

    with urllib.request.urlopen(req, timeout=90) as response:
        result = json.loads(response.read().decode('utf-8'))
        return result['candidates'][0]['content']['parts'][0]['text']

def process_video(video_id, title):
    slug = slugify(title)
    filename = f"{video_id}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(filepath):
        return "SKIP", filename
    
    transcript = download_subtitle(video_id)
    if not transcript:
        return "NO_SUB", None
    
    summary = summarize_with_gemini(title, video_id, transcript)
    if not summary:
        return "NO_SUM", None
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return "OK", filename

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 process_batch.py VIDEO_ID TITLE")
        sys.exit(1)
    
    video_id = sys.argv[1]
    title = ' '.join(sys.argv[2:])
    
    try:
        status, filename = process_video(video_id, title)
        print(f"{status}|{filename or 'N/A'}")
    except Exception as e:
        print(f"ERROR|{str(e)}")
