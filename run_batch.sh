#!/bin/bash
# 批次處理 YC 影片

WORK_DIR=~/.openclaw/workspace/research/youtube_summaries
cd "$WORK_DIR"

# 待處理影片列表
declare -a VIDEOS=(
"2hgjgycOU_0|Inside The Startup Building Reusable Rockets"
"pBlIgs6w7Ss|How Intelligent Is AI, Really?"
"5WN8bfG06Hk|From Pivot Hell To 1.4 Billion Unicorn"
"t8co94HS6tY|How Amplitude Went From Skeptics to All In on AI"
"Z4L4ZqL1xqQ|The Best Consumer Startup Ideas Were Impossible Until Now"
"RynySryqM_0|Cursor Head of Design Roasts Startup Websites"
"KTmxaMdUbHA|AI Is Eating Logistics"
"hKw6cRKcqzY|Inside The Startup Launching AI Data Centers Into Space"
"i_PjjXKNpA4|The Startup Playbook for Hiring Your First Engineers and AEs"
"DULfEcPR0Gc|Good News For Startups: Enterprise Is Bad At AI"
"JZLZQVmfGn8|Transformers Explained: The Discovery That Changed AI Forever"
"nGLmpKi-jRU|Startup Advice: AI GTM, Pivoting And How To Hire"
"Hm-ZIiwiN1o|Billion-Dollar Unpopular Startup Ideas"
"IqwSb2hO1jE|What Everyone Is Getting Wrong About AI And Jobs"
"ENG_DQF5E60|This Startup Is Trying To Delete 29 Percent Of All CO2 Emissions"
"DJjZzzPANBY|Ask These Questions Before Starting An AI Startup"
"bxBzsSsqQAM|The 7 Most Powerful Moats For AI Startups"
"Pdne9xaRLUc|Why Now Is The Best Time To Build In Crypto"
"uqc_vt95GJg|Aaron Levie: Why Startups Win In The AI Era"
"Zyw-YA0k3xo|The FDE Playbook for AI Startups with Bob McGrew"
"TrXi3naD6Og|Michael Truell: Building Cursor At 23"
"raTbhtKZTZA|OpenAI vs Deepseek vs Qwen Comparing Open Source LLM"
"pHuXCzM2ntU|How This 25-Year-Old Built A 675M Legal AI Startup"
"JdT78t1Offo|Anthropic Co-founder: Building Claude Code"
"DH7REvnQ1y4|The Sales Playbook For Founders"
"-7Qz7tSTfUU|Dylan Field: Scaling Figma"
"lqokpIme47A|The Finance Startup Bringing Agentic AI to Wall Street"
"p8Jx4qvDoSo|Scaling and the Road to Human-Level AI"
"uEeFsW9343g|Brand Design Tips From Linear Founder"
"a8-QsBHoH94|Chelsea Finn: Building Robots That Can Do Anything"
"kOyIjt6FUrw|How Replit Went From 10M to 100M ARR"
"2Yguz5U-Nic|Nobel Laureate John Jumper: AI is Revolutionizing Scientific Discovery"
"2jOnoTEk-xA|Aravind Srinivas: Perplexitys Race to Build Agentic Search"
"RNJCfif1dPY|Andrew Ng: Building Faster with AI"
"ShYKkPPhOoc|How to Spend Your 20s in the AI Era"
"5QcCeSsNRks|François Chollet: How We Get To AGI"
"_PioN-CpOP0|Fei-Fei Li: Spatial Intelligence"
"xFQ5mIJdxhA|Legendary Consumer VC Predicts The Future Of AI Products"
"AUUZuzVHKdo|Satya Nadella: Microsofts AI Bets"
"V979Wd1gmTU|Sam Altman: The Future of OpenAI"
"cFIlta1GkiE|Elon Musk: Digital Superintelligence"
"LCEmiRjPEtQ|Andrej Karpathy: Software Is Changing Again"
"5noIKN8t69U|Alexandr Wang: Building Scale AI"
"oOylEw3tPQ8|Cursor CEO: Going Beyond Code"
"XdigD0LOXx0|Fusion Energy Will Power the AI Boom"
"DL82mGde6wo|State-Of-The-Art Prompting For AI Agents"
"WJoZK9sMwvw|How To Design Better AI Apps"
"K4s6Cgicw_A|Startup Ideas You Can Now Build With AI"
"TECDj4JUx7o|How AI Coding Agents Will Change Your Job"
"LKgAx7FWva4|Windsurf CEO: Betting On AI Agents"
"BJjsfNO5JTo|How To Get The Most Out Of Vibe Coding"
"aYK0H85E_oU|How Zepto Became Indias Fastest Growing Startup"
"JOYSDqJdiro|The Next Breakthrough In AI Agents Is Here"
"VIkphkYlkaQ|How To Build A Truly Abundant Future"
"ksGNfd-wQY4|What Founders Can Do To Improve Their Design Game"
"3N3TnaViyjk|DoorDash CEO: Customer Obsession"
"bvjyaz4ZiVI|How Top 1 Percent Founders Navigate Co-founder Conflict"
"VaQA55ZZWBU|From A Pivot To Building A 9.6 Billion Payroll Company"
"4UE4e6b2qtA|Figmas Dylan Field: Exploring the idea maze"
"5uBAQrg4SoQ|GPT-4.5 Big Model Energy"
"IACHfKmZMr8|Vibe Coding Is The Future"
"DBhSfROq3wU|AI Interfaces Of The Future"
"SP7Ua8FKZN4|How To Build The Future: Aravind Srinivas"
"aIKfA3gIXwo|How AI Is Changing Enterprise"
"sOFmYwYa9Pk|How Blake Scholl Built The First Independent Supersonic Jet"
"IRROi-Q1V44|The Right And Wrong Way To Spend Money At Your Startup"
"TANaRNMbYgk|How To Get AI Startup Ideas"
"4Tmn-XP93m4|The Engineering Unlocks Behind DeepSeek"
"eW7rUtYHD9U|Bob McGrew: AI Agents And The Path To AGI"
"0LMK5JYkB94|AI Revolution: What Nobody Else Is Seeing"
"d6Ed5bZAtrM|How Scaling Laws Will Determine AIs Future"
"7Kt9ugD3bGQ|How To Use AI In Your Startup"
"FwD0wqwUjAI|How To Build The Future: Parker Conrad"
"rjyJsbUunQ4|Building A 2 Billion SaaS Company"
"uGjv25IrjoE|The Lightcone 2025 Forecast"
"CcnwFJqEnxU|How David Lieb Turned a Failing Startup Into Google Photos"
"z0wt2pe_LZM|2024: The Year the GPT Wrapper Myth Proved Wrong"
"VDmU0jjklBo|Anthropics Claude Computer Use Is A Game Changer"
"z1aKRhRnVNk|How To Start A Dev Tools Company"
"ASABxNenD_U|Vertical AI Agents Could Be 10X Bigger Than SaaS"
"EW9TUqOgjmQ|Twitter vs. X: Product Lessons For Startup Founders"
"JiwiqYGw4iU|Why The Next AI Breakthroughs Will Be In Reasoning"
"xXCBz_8hM9w|How To Build The Future: Sam Altman"
"lbJilIQhHko|The 10 Trillion Parameter AI Model With 300 IQ"
"Q0Xs0lGgwVA|You Dont Have To Be A Billionaire To Launch Satellites"
"Lv9bKyQgoHo|Why OpenAIs o1 Is A Huge Deal"
"wH3TKpALlw4|Starting A Company: The Key Terms You Should Know"
"jbIQfoldLag|Now Anyone Can Code: How AI Agents Can Build Your Whole App"
"CKfERe55CeA|Why Design Matters: Lessons from Stripe, Lyft and Airbnb"
"HB3l1BPi7zo|How Do Billion Dollar Startups Start?"
)

TOTAL=${#VIDEOS[@]}
COUNT=0
SUCCESS=0

echo "開始處理 $TOTAL 支影片..."
echo "=========================="

for item in "${VIDEOS[@]}"; do
    IFS='|' read -r video_id title <<< "$item"
    COUNT=$((COUNT + 1))
    
    # 檢查是否已存在
    if ls youtubers/ycombinator/${video_id}-*.md 1> /dev/null 2>&1; then
        echo "[$COUNT/$TOTAL] 跳過 (已存在): $title"
        SUCCESS=$((SUCCESS + 1))
        continue
    fi
    
    echo "[$COUNT/$TOTAL] 處理: $title"
    result=$(python3 process_batch.py "$video_id" "$title" 2>&1)
    status=$(echo "$result" | cut -d'|' -f1)
    
    if [ "$status" = "OK" ]; then
        echo "  ✓ 成功"
        SUCCESS=$((SUCCESS + 1))
    elif [ "$status" = "SKIP" ]; then
        echo "  ○ 已存在"
        SUCCESS=$((SUCCESS + 1))
    else
        echo "  ✗ 失敗: $result"
    fi
    
    # 防封：等待 30 秒
    if [ $COUNT -lt $TOTAL ]; then
        echo "  等待 30 秒..."
        sleep 30
    fi
done

echo "=========================="
echo "完成！成功: $SUCCESS / $TOTAL"
