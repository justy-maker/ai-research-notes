# How I Setup My OpenClaw as a Professional Developer (Insanely Powerful)

- **影片連結**: https://www.youtube.com/watch?v=NO-bOryZoTE
- **頻道**: Tech With Tim
- **整理日期**: 2026-02-24
- **片長**: 16 分鐘

---

## 📌 核心觀點

Tech With Tim 分享作為專業軟體開發者如何安全且高效地設置 OpenClaw，重點放在安全性、模型選擇、實際用途。

## 🔒 安全設置

### 伺服器安全
- 部署在 VPS 上，使用 **Tailscale**（VPN）限制只有授權電腦可存取
- 防火牆封鎖所有外部流量，OpenClaw 僅監聽 localhost
- 使用非 root 使用者（TIM）運行，限制 sudo 權限

### 通訊安全
- 僅透過 **Telegram** 互動（不用 WhatsApp 避免暴露身份和 2FA）
- Telegram 是他幾乎不使用的 app，即使被入侵損失也小

### 整合安全
- 建立**獨立 Gmail 帳號**給 ClawBot
- 從主帳號設定信件轉發規則，僅轉發信任寄件者的信
- 封鎖直接發送到 bot email 的信件（防止 prompt injection）
- 所有 API 金鑰設嚴格限制 + 通知

## 💰 模型選擇策略
- Opus 4.5 直連 API → 幾分鐘就燒幾美元（月燒千元等級）
- **解法：用 ChatGPT Pro 訂閱（$200/月）的 Codex 模型** → 幾乎無限額度
- 搭配 Claude 訂閱（$20/月）用 Opus 做複雜規劃
- 策略：複雜任務 → Opus，其他全部 → Codex；Opus 額度用完回退 Codex

## 🛠️ 實際用途

### OpsHub 儀表板
- **ClawBot Monitor** — 即時監控所有 sub-agent、工具呼叫、錯誤日誌
- **Token 用量追蹤** — 各模型額度和估計費用
- **YouTube 競品研究** — 每日自動搜尋表現優異的同類影片，計算每小時觀看數
- **YouTube 創意系統** — 從每日報告生成影片點子

### AI 會計系統
- 自動讀取轉發的收據、發票、銀行對帳單
- 提取資訊寫入 Google Sheets
- 自動產生發票、上傳 Google Drive
- 新收款自動匹配對應發票

### 任務管理
- **看板系統** — To-do / In Progress / Done
- 每 30 分鐘 heartbeat 自動啟動 sub-agents 撿取任務並行處理
- 完整活動日誌

### GitHub 整合
- 建立獨立 GitHub 帳號（Tech with Tim ClawBot）
- 所有程式碼自動推送到 organization repo

## 💡 Tim 的評價
- 目前不算改變人生，但確實節省時間
- 最大價值：自動化那些「不想自己寫腳本」的瑣碎任務
- 持續學習中，期待它越來越了解自己的需求
