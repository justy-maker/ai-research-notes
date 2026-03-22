#!/usr/bin/env python3
"""
ai-research-notes 倉庫整理腳本
1. 合併重複頻道
2. 移動根目錄散落的 .md 到對應頻道
3. 提取所有 .md 的 metadata
4. 生成 INDEX.md
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict

REPO = Path("/home/ysi/.openclaw/workspace/research/youtube_summaries")

# === Step 1: 合併重複頻道 ===
MERGE_MAP = {
    # target: [sources to merge into target]
    "drberg_chinese": ["dr__berg", "dr_berg_chinese"],
    "tech_with_tim": ["techwithtim"],
    "ycombinator": ["y_combinator"],
    "intheworldofai": ["in_the_world_of_ai"],
    # aisuperdomain 和 aisuperdomain_bilibili 保持分開（一個是 YT，一個是 B站）
}

def merge_channels():
    """合併重複頻道資料夾"""
    youtubers = REPO / "youtubers"
    merged = []
    
    for target, sources in MERGE_MAP.items():
        target_dir = youtubers / target
        target_dir.mkdir(exist_ok=True)
        
        for src_name in sources:
            src_dir = youtubers / src_name
            if not src_dir.exists():
                continue
            
            for f in src_dir.iterdir():
                if f.name.startswith('.'):
                    continue
                dest = target_dir / f.name
                if dest.exists():
                    # 檢查是否同名但不同內容
                    if f.is_file() and dest.is_file():
                        if f.read_bytes() == dest.read_bytes():
                            print(f"  [SKIP] 重複檔案: {f.name}")
                        else:
                            # 重命名避免衝突
                            new_name = f"{f.stem}_from_{src_name}{f.suffix}"
                            shutil.move(str(f), str(target_dir / new_name))
                            merged.append(f"  [RENAME] {f.name} → {new_name}")
                    continue
                shutil.move(str(f), str(dest))
                merged.append(f"  [MOVE] {src_name}/{f.name} → {target}/{f.name}")
            
            # 刪除空的來源資料夾
            remaining = list(src_dir.iterdir())
            if not remaining or all(f.name.startswith('.') for f in remaining):
                shutil.rmtree(str(src_dir))
                merged.append(f"  [DELETE] 空資料夾 {src_name}/")
    
    return merged

# === Step 2: 分析根目錄 .md 檔案 ===
def categorize_root_files():
    """把根目錄的 .md 歸類"""
    root_mds = [f for f in REPO.iterdir() if f.suffix == '.md' and f.name not in 
                ('README.md', '_sidebar.md', 'daily-briefing.md', 'INDEX.md', 'VIDEO-SOP.md')]
    
    moves = []
    for f in root_mds:
        content = f.read_text(encoding='utf-8', errors='ignore')[:2000]
        
        # 嘗試從內容判斷來源頻道
        channel = detect_channel(content, f.name)
        if channel:
            dest_dir = REPO / "youtubers" / channel
            dest_dir.mkdir(exist_ok=True)
            dest = dest_dir / f.name
            if not dest.exists():
                shutil.move(str(f), str(dest))
                moves.append(f"  [MOVE] {f.name} → youtubers/{channel}/")
            else:
                moves.append(f"  [SKIP] {f.name} already in {channel}/")
        else:
            # 放到 uncategorized/
            unc_dir = REPO / "uncategorized"
            unc_dir.mkdir(exist_ok=True)
            dest = unc_dir / f.name
            if not dest.exists():
                shutil.move(str(f), str(dest))
                moves.append(f"  [UNCATEGORIZED] {f.name}")
    
    return moves

def detect_channel(content, filename):
    """從內容或檔名偵測頻道"""
    content_lower = content.lower()
    
    # 直接匹配頻道名
    channel_patterns = {
        'google': None,  # Google 白皮書系列不屬於特定頻道
        'musk': None,
        'agent_teams': None,
        'mem0': None,
        'tax_saving': None,
    }
    
    # 從內容中找頻道標記
    channel_markers = {
        'AI-seeker': 'aiseeker_bilibili',
        'ai-seeker': 'aiseeker_bilibili',
        'AI超元域': 'aisuperdomain_bilibili',
        'ai超元域': 'aisuperdomain_bilibili',
        'Dr. Berg': 'drberg_chinese',
        'dr. berg': 'drberg_chinese',
        '柏格醫生': 'drberg_chinese',
        'Tech With Tim': 'tech_with_tim',
        'tech with tim': 'tech_with_tim',
        'Y Combinator': 'ycombinator',
        'Simon Sinek': 'simon_sinek',
        'Dan Koe': 'dankoe',
        'Dan Martell': 'dan_martell',
        'Liam Ottley': 'liam_ottley',
        'BRAINY DOSE': 'brainydose',
        'In The World of AI': 'intheworldofai',
        'GeekyHour': 'geekhour',
        '秋芝': 'qiuzhi2046_bilibili',
        'Alan UI': 'alan_design',
        '程隆': 'chenglung',
    }
    
    for marker, channel in channel_markers.items():
        if marker.lower() in content_lower:
            return channel
    
    return None  # 無法判斷的放 uncategorized

# === Step 3: 提取 metadata ===
def extract_metadata(filepath):
    """從 .md 檔案提取 metadata"""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except:
        return None
    
    meta = {
        'path': str(filepath.relative_to(REPO)),
        'filename': filepath.name,
        'title': '',
        'channel': '',
        'date': '',
        'tags': [],
        'language': 'zh',
    }
    
    lines = content.split('\n')
    
    # 提取標題（第一個 # 開頭的行）
    for line in lines[:20]:
        if line.startswith('# '):
            meta['title'] = line[2:].strip()
            break
    
    if not meta['title']:
        # 用檔名作為標題
        meta['title'] = filepath.stem.replace('-', ' ').replace('_', ' ')
    
    # 提取日期
    date_match = re.search(r'(20\d{2}[-/]?\d{2}[-/]?\d{2})', filepath.name)
    if date_match:
        d = date_match.group(1).replace('/', '-')
        if len(d) == 8:  # 20260206
            d = f"{d[:4]}-{d[4:6]}-{d[6:8]}"
        meta['date'] = d
    
    # 提取頻道
    parent = filepath.parent.name
    if parent != 'youtube_summaries' and parent != 'uncategorized':
        meta['channel'] = parent
    
    # 從內容提取頻道
    for line in lines[:10]:
        if '頻道' in line or 'Channel' in line.lower():
            ch_match = re.search(r'[：:]\s*(.+)', line)
            if ch_match:
                meta['channel_name'] = ch_match.group(1).strip().strip('*')
    
    # 自動標籤
    content_lower = content.lower()
    tag_keywords = {
        'AI Agent': ['agent', 'agentic', '智能體', '智慧體'],
        '量化交易': ['quant', 'trading', '量化', '交易', 'macd', 'rsi', '股票', 'stock'],
        'AI 工具': ['tool', '工具', 'claude', 'gemini', 'gpt', 'chatgpt', 'openai'],
        'AI 編程': ['code', 'coding', '編程', '程式', 'python', 'typescript', 'github'],
        '健康': ['health', '健康', '斷食', '飲食', 'diet', 'vitamin', '維生素', 'berg'],
        '創業': ['startup', '創業', 'saas', 'business', '商業'],
        '心理/自我成長': ['mindset', '心理', 'motivation', '成長', 'sinek', 'habit'],
        '設計/UI': ['design', '設計', 'ui', 'ux', 'figma', 'framer'],
        '影片生成': ['video generation', '影片生成', 'sora', 'kling', 'suno'],
        '簡報': ['presentation', '簡報', 'ppt', 'slides'],
        '教育': ['education', '教育', '學習', 'learning', '聯考'],
        '自動化': ['automation', '自動化', 'workflow', 'n8n', 'zapier'],
        'SEO/行銷': ['seo', 'marketing', '行銷', '推廣'],
    }
    
    for tag, keywords in tag_keywords.items():
        for kw in keywords:
            if kw in content_lower:
                meta['tags'].append(tag)
                break
    
    # 判斷語言
    if re.search(r'[\u4e00-\u9fff]', meta['title']):
        meta['language'] = 'zh'
    else:
        meta['language'] = 'en'
    
    return meta

# === Step 4: 生成 INDEX.md ===
CHANNEL_DISPLAY_NAMES = {
    'aiseeker_bilibili': '🔴 AI-seeker (B站)',
    'aisuperdomain': '🎬 AI超元域 (YouTube)',
    'aisuperdomain_bilibili': '🔴 AI超元域 (B站)',
    'alan_design': '🎨 Alan UI Design',
    'bilibili_favorites': '🔴 B站收藏',
    'brainydose': '🧠 BRAINY DOSE',
    'chenglung': '🎤 程隆',
    'dankoe': '💡 Dan Koe',
    'dan_martell': '🚀 Dan Martell',
    'drberg_chinese': '🏥 Dr. Berg 中文',
    'geekhour': '⚡ GeekyHour',
    'intheworldofai': '🤖 In The World of AI',
    'liam_ottley': '💰 Liam Ottley',
    'pragmatic_engineer': '👨‍💻 Pragmatic Engineer',
    'qiuzhi2046_bilibili': '🔴 秋芝2046 (B站)',
    'simon_sinek': '🎯 Simon Sinek',
    'tech_with_tim': '💻 Tech With Tim',
    'ycombinator': '🏢 Y Combinator',
}

def generate_index(all_meta):
    """生成 INDEX.md"""
    lines = []
    lines.append("# 📚 AI 研究筆記索引\n")
    lines.append(f"> 共 **{len(all_meta)}** 篇摘要 | 最後更新：{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append("---\n")
    
    # === 按主題分類 ===
    lines.append("## 🏷️ 按主題分類\n")
    
    tag_groups = defaultdict(list)
    for m in all_meta:
        if m['tags']:
            for tag in m['tags']:
                tag_groups[tag].append(m)
        else:
            tag_groups['其他'].append(m)
    
    for tag in sorted(tag_groups.keys()):
        items = tag_groups[tag]
        lines.append(f"\n### {tag} ({len(items)} 篇)\n")
        # 按日期排序（新的在前）
        items_sorted = sorted(items, key=lambda x: x['date'] or '0000', reverse=True)
        for m in items_sorted[:50]:  # 每個主題最多顯示 50 篇
            date_str = f" `{m['date']}`" if m['date'] else ""
            channel_str = f" — {m.get('channel_name', m['channel'])}" if m['channel'] else ""
            lines.append(f"- [{m['title']}]({m['path']}){date_str}{channel_str}")
        if len(items) > 50:
            lines.append(f"\n> ... 還有 {len(items)-50} 篇，請到對應頻道查看")
    
    # === 按頻道分類 ===
    lines.append("\n---\n")
    lines.append("## 📺 按頻道分類\n")
    
    channel_groups = defaultdict(list)
    for m in all_meta:
        ch = m['channel'] or 'uncategorized'
        channel_groups[ch].append(m)
    
    for ch in sorted(channel_groups.keys()):
        items = channel_groups[ch]
        display = CHANNEL_DISPLAY_NAMES.get(ch, ch)
        lines.append(f"\n### {display} ({len(items)} 篇)\n")
        items_sorted = sorted(items, key=lambda x: x['date'] or '0000', reverse=True)
        for m in items_sorted:
            date_str = f" `{m['date']}`" if m['date'] else ""
            lines.append(f"- [{m['title']}]({m['path']}){date_str}")
    
    # === 按日期排列（最新 100 篇）===
    lines.append("\n---\n")
    lines.append("## 📅 最新摘要（按日期）\n")
    
    dated = [m for m in all_meta if m['date']]
    dated.sort(key=lambda x: x['date'], reverse=True)
    
    current_month = ""
    for m in dated[:100]:
        month = m['date'][:7]  # YYYY-MM
        if month != current_month:
            current_month = month
            lines.append(f"\n#### {month}\n")
        
        channel_str = f" — {CHANNEL_DISPLAY_NAMES.get(m['channel'], m['channel'])}" if m['channel'] else ""
        tags_str = f" `{'` `'.join(m['tags'][:3])}`" if m['tags'] else ""
        lines.append(f"- [{m['title']}]({m['path']}) `{m['date']}`{channel_str}{tags_str}")
    
    if len(dated) > 100:
        lines.append(f"\n> ... 還有 {len(dated)-100} 篇更早的摘要")
    
    # === 統計 ===
    lines.append("\n---\n")
    lines.append("## 📊 統計\n")
    lines.append(f"| 指標 | 數量 |")
    lines.append(f"|------|------|")
    lines.append(f"| 總摘要數 | {len(all_meta)} |")
    lines.append(f"| 頻道數 | {len(channel_groups)} |")
    lines.append(f"| 主題標籤 | {len(tag_groups)} |")
    
    lang_zh = sum(1 for m in all_meta if m['language'] == 'zh')
    lang_en = len(all_meta) - lang_zh
    lines.append(f"| 中文 | {lang_zh} |")
    lines.append(f"| 英文 | {lang_en} |")
    
    if dated:
        lines.append(f"| 最早 | {dated[-1]['date']} |")
        lines.append(f"| 最新 | {dated[0]['date']} |")
    
    return '\n'.join(lines)

# === Main ===
def main():
    print("=" * 60)
    print("🔧 ai-research-notes 倉庫整理")
    print("=" * 60)
    
    # Step 1: 合併重複頻道
    print("\n📂 Step 1: 合併重複頻道...")
    merge_log = merge_channels()
    for line in merge_log:
        print(line)
    print(f"  合併完成 ✅")
    
    # Step 2: 移動根目錄檔案
    print("\n📁 Step 2: 分類根目錄 .md 檔案...")
    move_log = categorize_root_files()
    for line in move_log:
        print(line)
    print(f"  分類完成 ✅")
    
    # Step 3: 提取所有 metadata
    print("\n🔍 Step 3: 提取 metadata...")
    all_meta = []
    
    # 掃描 youtubers/ 下所有 .md
    youtubers_dir = REPO / "youtubers"
    for md_file in sorted(youtubers_dir.rglob("*.md")):
        if md_file.name in ('index.md', 'index.html', 'README.md', '_sidebar.md'):
            continue
        meta = extract_metadata(md_file)
        if meta and meta['title']:
            all_meta.append(meta)
    
    # 掃描 uncategorized/
    unc_dir = REPO / "uncategorized"
    if unc_dir.exists():
        for md_file in sorted(unc_dir.glob("*.md")):
            meta = extract_metadata(md_file)
            if meta and meta['title']:
                all_meta.append(meta)
    
    # 掃描 topics/
    topics_dir = REPO / "topics"
    if topics_dir.exists():
        for md_file in sorted(topics_dir.glob("*.md")):
            meta = extract_metadata(md_file)
            if meta and meta['title']:
                meta['tags'].append('📌 主題研究')
                all_meta.append(meta)
    
    print(f"  共提取 {len(all_meta)} 篇 metadata ✅")
    
    # Step 4: 生成 INDEX.md
    print("\n📝 Step 4: 生成 INDEX.md...")
    index_content = generate_index(all_meta)
    index_path = REPO / "INDEX.md"
    index_path.write_text(index_content, encoding='utf-8')
    print(f"  INDEX.md 已生成 ({len(index_content)} bytes) ✅")
    
    # 統計
    print("\n" + "=" * 60)
    print("📊 整理結果：")
    print(f"  - 合併操作: {len(merge_log)} 項")
    print(f"  - 檔案移動: {len(move_log)} 項")
    print(f"  - 索引收錄: {len(all_meta)} 篇")
    print("=" * 60)

if __name__ == '__main__':
    main()
