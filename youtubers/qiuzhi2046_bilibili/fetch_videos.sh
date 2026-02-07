#!/bin/bash
# B站頻道「秋芝2046」影片資訊抓取腳本

OUTPUT_DIR="/home/ysi/.openclaw/workspace/research/youtubers/qiuzhi2046_bilibili"
COOKIES="/home/ysi/.openclaw/workspace/bilibili_cookies.txt"
YTDLP="/tmp/yt-dlp-new"

VIDEO_IDS=(
"BV1G3FNznEiS"
"BV1no6jBSEnc"
"BV1gKiEBZEHq"
"BV1ibvhBqEmp"
"BV13fvrBoEGo"
"BV1sgBSBVEUA"
"BV14HmSBMEkw"
"BV1ZqmmBJEmP"
"BV1ZY2tB4ERH"
"BV1BHUwBdEpq"
"BV1HdynBrEes"
"BV1ejyGBKENz"
"BV12is1zQELH"
"BV1kMWXzcER2"
"BV1Rz4iz1Exz"
"BV16cx4zoErH"
"BV1HeJQzSEHW"
"BV1CHaGzBEMc"
"BV1xseJzqEBv"
"BV1zqeMzfEiQ"
)

mkdir -p "$OUTPUT_DIR/json"

for vid in "${VIDEO_IDS[@]}"; do
    echo "抓取: $vid"
    $YTDLP --cookies "$COOKIES" -j "https://www.bilibili.com/video/$vid" 2>/dev/null > "$OUTPUT_DIR/json/${vid}.json"
    # 隨機間隔 30-60 秒
    DELAY=$((30 + RANDOM % 31))
    echo "等待 ${DELAY} 秒..."
    sleep $DELAY
done

echo "完成！"
