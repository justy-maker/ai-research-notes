#!/usr/bin/env python3
"""批次處理 YC 頻道影片"""
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

# 已處理的影片
SKIP_IDS = {"qwmmWzPnhog", "cqrJzG03ENE", "YFeb3yAxtjE", "lWmDiDGsLK4", "l0h3nAW13ao", "4uzGDAoNOZc"}

# 待處理影片列表
VIDEOS = [
    ("K5JoLAauzq4", "How We Redesigned Our Website"),
    ("leQ89XSHILw", "Why Your Startup Website Isn't Converting"),
    ("dC_3ys349bU", "The ML Technique Every Founder Should Know"),
    ("0kARDVL2nZg", "How To Get Your First Users"),
    ("2hgjgycOU_0", "Inside The Startup Building Reusable Rockets"),
    ("pBlIgs6w7Ss", "How Intelligent Is AI, Really?"),
    ("5WN8bfG06Hk", "From Pivot Hell To $1.4 Billion Unicorn"),
    ("t8co94HS6tY", "How Amplitude Went From Skeptics to All In on AI"),
    ("Z4L4ZqL1xqQ", "The Best Consumer Startup Ideas Were Impossible Until Now"),
    ("RynySryqM_0", "Cursor Head of Design Roasts Startup Websites"),
    ("KTmxaMdUbHA", "AI Is Eating Logistics"),
    ("hKw6cRKcqzY", "Inside The Startup Launching AI Data Centers Into Space"),
    ("i_PjjXKNpA4", "The Startup Playbook for Hiring Your First Engineers and AEs"),
    ("DULfEcPR0Gc", "Good News For Startups: Enterprise Is Bad At AI"),
    ("JZLZQVmfGn8", "Transformers Explained: The Discovery That Changed AI Forever"),
    ("nGLmpKi-jRU", "Startup Advice: AI GTM, Pivoting & How To Hire"),
    ("Hm-ZIiwiN1o", "Billion-Dollar Unpopular Startup Ideas"),
    ("IqwSb2hO1jE", "What Everyone Is Getting Wrong About AI And Jobs"),
    ("ENG_DQF5E60", "This Startup Is Trying To Delete 29% Of All CO2 Emissions"),
    ("DJjZzzPANBY", "Ask These Questions Before Starting An AI Startup"),
    ("bxBzsSsqQAM", "The 7 Most Powerful Moats For AI Startups"),
    ("Pdne9xaRLUc", "Why Now Is The Best Time To Build In Crypto"),
    ("uqc_vt95GJg", "Aaron Levie: Why Startups Win In The AI Era"),
    ("Zyw-YA0k3xo", "The FDE Playbook for AI Startups with Bob McGrew"),
    ("TrXi3naD6Og", "Michael Truell: Building Cursor At 23"),
    ("raTbhtKZTZA", "OpenAI vs Deepseek vs Qwen: Comparing Open Source LLM"),
    ("pHuXCzM2ntU", "How This 25-Year-Old Built A $675M Legal AI Startup"),
    ("JdT78t1Offo", "Anthropic Co-founder: Building Claude Code"),
    ("DH7REvnQ1y4", "The Sales Playbook For Founders"),
    ("-7Qz7tSTfUU", "Dylan Field: Scaling Figma and the Future of Design"),
    ("lqokpIme47A", "The Finance Startup Bringing Agentic AI to Wall Street"),
    ("p8Jx4qvDoSo", "Scaling and the Road to Human-Level AI"),
    ("uEeFsW9343g", "Brand Design Tips From Linear Founder"),
    ("a8-QsBHoH94", "Chelsea Finn: Building Robots That Can Do Anything"),
    ("kOyIjt6FUrw", "How Replit Went From $10M to $100M ARR"),
    ("2Yguz5U-Nic", "Nobel Laureate John Jumper: AI is Revolutionizing Scientific Discovery"),
    ("2jOnoTEk-xA", "Aravind Srinivas: Perplexity's Race to Build Agentic Search"),
    ("RNJCfif1dPY", "Andrew Ng: Building Faster with AI"),
    ("ShYKkPPhOoc", "How to Spend Your 20s in the AI Era"),
    ("5QcCeSsNRks", "François Chollet: How We Get To AGI"),
    ("_PioN-CpOP0", "Fei-Fei Li: Spatial Intelligence is the Next Frontier in AI"),
    ("xFQ5mIJdxhA", "Legendary Consumer VC Predicts The Future Of AI Products"),
    ("AUUZuzVHKdo", "Satya Nadella: Microsoft's AI Bets"),
    ("V979Wd1gmTU", "Sam Altman: The Future of OpenAI"),
    ("cFIlta1GkiE", "Elon Musk: Digital Superintelligence"),
    ("LCEmiRjPEtQ", "Andrej Karpathy: Software Is Changing (Again)"),
    ("5noIKN8t69U", "Alexandr Wang: Building Scale AI"),
    ("oOylEw3tPQ8", "Cursor CEO: Going Beyond Code"),
    ("XdigD0LOXx0", "Fusion Energy Will Power the AI Boom"),
    ("DL82mGde6wo", "State-Of-The-Art Prompting For AI Agents"),
    ("WJoZK9sMwvw", "How To Design Better AI Apps"),
    ("K4s6Cgicw_A", "Startup Ideas You Can Now Build With AI"),
    ("TECDj4JUx7o", "How AI Coding Agents Will Change Your Job"),
    ("LKgAx7FWva4", "Windsurf CEO: Betting On AI Agents"),
    ("BJjsfNO5JTo", "How To Get The Most Out Of Vibe Coding"),
    ("aYK0H85E_oU", "How Zepto Became India's Fastest Growing Startup"),
    ("JOYSDqJdiro", "The Next Breakthrough In AI Agents Is Here"),
    ("VIkphkYlkaQ", "How To Build A Truly Abundant Future"),
    ("ksGNfd-wQY4", "What Founders Can Do To Improve Their Design Game"),
    ("3N3TnaViyjk", "DoorDash CEO: Customer Obsession"),
    ("bvjyaz4ZiVI", "How Top 1% Founders Navigate Co-founder Conflict"),
    ("VaQA55ZZWBU", "From A Pivot To Building A $9.6 Billion Payroll Company"),
    ("4UE4e6b2qtA", "Figma's Dylan Field: Exploring the idea maze"),
    ("5uBAQrg4SoQ", "GPT-4.5 = Big Model Energy"),
    ("IACHfKmZMr8", "Vibe Coding Is The Future"),
    ("DBhSfROq3wU", "AI Interfaces Of The Future"),
    ("SP7Ua8FKZN4", "How To Build The Future: Aravind Srinivas"),
    ("aIKfA3gIXwo", "How AI Is Changing Enterprise"),
    ("sOFmYwYa9Pk", "How Blake Scholl Built The First Independent Supersonic Jet"),
    ("IRROi-Q1V44", "The Right (And Wrong) Way To Spend Money At Your Startup"),
    ("TANaRNMbYgk", "How To Get AI Startup Ideas"),
    ("4Tmn-XP93m4", "The Engineering Unlocks Behind DeepSeek"),
    ("eW7rUtYHD9U", "Bob McGrew: AI Agents And The Path To AGI"),
    ("0LMK5JYkB94", "AI Revolution: What Nobody Else Is Seeing"),
    ("d6Ed5bZAtrM", "How Scaling Laws Will Determine AI's Future"),
    ("7Kt9ugD3bGQ", "How To Use AI In Your Startup"),
    ("FwD0wqwUjAI", "How To Build The Future: Parker Conrad"),
    ("rjyJsbUunQ4", "Building A $2 Billion SaaS Company"),
    ("uGjv25IrjoE", "The Lightcone 2025 Forecast"),
    ("CcnwFJqEnxU", "How David Lieb Turned a Failing Startup Into Google Photos"),
    ("z0wt2pe_LZM", "2024: The Year the GPT Wrapper Myth Proved Wrong"),
    ("VDmU0jjklBo", "Anthropic's Claude Computer Use Is A Game Changer"),
    ("z1aKRhRnVNk", "How To Start A Dev Tools Company"),
    ("ASABxNenD_U", "Vertical AI Agents Could Be 10X Bigger Than SaaS"),
    ("EW9TUqOgjmQ", "Twitter vs. X: Product Lessons For Startup Founders"),
    ("JiwiqYGw4iU", "Why The Next AI Breakthroughs Will Be In Reasoning"),
    ("xXCBz_8hM9w", "How To Build The Future: Sam Altman"),
    ("lbJilIQhHko", "The 10 Trillion Parameter AI Model With 300 IQ"),
    ("Q0Xs0lGgwVA", "You Don't Have To Be A Billionaire To Launch Satellites"),
    ("Lv9bKyQgoHo", "Why OpenAI's o1 Is A Huge Deal"),
    ("wH3TKpALlw4", "Starting A Company: The Key Terms You Should Know"),
    ("jbIQfoldLag", "Now Anyone Can Code: How AI Agents Can Build Your Whole App"),
    ("CKfERe55CeA", "Why Design Matters: Lessons from Stripe, Lyft and Airbnb"),
    ("HB3l1BPi7zo", "How Do Billion Dollar Startups Start?"),
]

def slugify(text):
    """Convert title to slug"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text[:45].strip('-')

def download_subtitle(video_id):
    """Download subtitle for a video"""
    os.chdir(WORK_DIR)
    cmd = f'{YT_DLP} --write-auto-sub --sub-lang en --skip-download --convert-subs srt -o "temp_sub" "https://www.youtube.com/watch?v={video_id}" 2>&1'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
    
    srt_file = "temp_sub.en.srt"
    if os.path.exists(srt_file):
        with open(srt_file, 'r') as f:
            content = f.read()
        os.remove(srt_file)
        
        # Clean subtitle
        lines = content.split('\n')
        seen = set()
        clean_lines = []
        for line in lines:
            if not line.strip():
                continue
            if re.match(r'^\d+$', line.strip()):
                continue
            if '-->' in line:
                continue
            if line.strip() not in seen:
                seen.add(line.strip())
                clean_lines.append(line.strip())
        
        return ' '.join(clean_lines)[:15000]
    return None

def summarize_with_gemini(title, video_id, transcript):
    """Use Gemini to summarize"""
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

    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        print(f"  Error: {e}")
        return None

def process_video(video_id, title, index, total):
    """Process a single video"""
    print(f"[{index}/{total}] Processing: {title}")
    
    # Check if already exists
    slug = slugify(title)
    filename = f"{video_id}-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    if os.path.exists(filepath):
        print(f"  Skipping (already exists)")
        return filename, title
    
    # Download subtitle
    print(f"  Downloading subtitle...")
    transcript = download_subtitle(video_id)
    
    if not transcript:
        print(f"  Failed to get subtitle")
        return None, title
    
    # Summarize with Gemini
    print(f"  Summarizing with Gemini...")
    summary = summarize_with_gemini(title, video_id, transcript)
    
    if not summary:
        print(f"  Failed to summarize")
        return None, title
    
    # Save file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    print(f"  Saved: {filename}")
    return filename, title

def main():
    # Filter out already processed
    to_process = [(vid, title) for vid, title in VIDEOS if vid not in SKIP_IDS]
    
    # Check for existing files
    existing = set()
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.md') and f != 'index.md':
            vid = f.split('-')[0]
            existing.add(vid)
    
    to_process = [(vid, title) for vid, title in to_process if vid not in existing]
    
    print(f"共 {len(to_process)} 支影片待處理")
    
    # Get start index from command line
    start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    
    results = []
    for i, (video_id, title) in enumerate(to_process[start_idx:], start=start_idx+1):
        try:
            filename, title = process_video(video_id, title, i, len(to_process))
            if filename:
                results.append((filename, title))
        except Exception as e:
            print(f"  Error processing {video_id}: {e}")
        
        # Wait 30 seconds between videos
        if i < len(to_process):
            print(f"  Waiting 30 seconds...")
            time.sleep(30)
    
    print(f"\nCompleted: {len(results)} videos processed")

if __name__ == "__main__":
    main()
