# 🚀 OpenClaw 高級使用經驗：如何調用 Claude Code 最省 Token！

- **頻道**: AI 超元域
- **日期**: 2026-02-12
- **連結**: https://www.youtube.com/watch?v=iJEfIc1mrsc
- **標籤**: #OpenClaw #ClaudeCode #Token優化 #AgentTeams #Hooks

## 影片摘要

本期影片解決一個常見痛點：在 OpenClaw 中使用 Claude Code 時 Token 消耗過大的問題。透過 Claude Code 的 Hooks 機制，實現零輪詢的自動化開發流程，大幅降低 Token 消耗。

## 問題分析

### 傳統方式的問題
- OpenClaw 每隔幾秒就輪詢一次 Claude Code 的狀態和輸出
- Claude Code 開發任務執行時間越長，OpenClaw 消耗的 Token 越多
- 評論區很多人抱怨 Token 消耗太大

### 解決方案：使用 Claude Code Hooks

不需要 OpenClaw 持續輪詢，而是讓 Claude Code 透過 Hooks 在完成時主動通知。

## 核心流程

```
1. OpenClaw 發送開發任務給 Claude Code（僅一次）
2. Claude Code 獨立運行（使用 Agent Teams 自動開發+測試）
3. 開發完成 → 觸發 Stop Hook
4. Hook 將執行結果寫入指定文件
5. Hook 發送 Wake Event 給 OpenClaw
6. OpenClaw 讀取結果 → 發送通知到聊天群組
```

### 雙重保障機制
- **Stop Hook**（主要）：Claude Code 開發完成時觸發
- **Session End Hook**（備用）：確保即使 Stop Hook 失敗，也能收到通知

### Token 消耗分析
- **步驟 1**（發送任務）：Token 消耗幾乎可忽略
- **步驟 2-4**（Claude Code 獨立執行）：OpenClaw 零消耗
- **步驟 6**（讀取結果）：結果內容不超過 1000 Token，消耗可忽略
- **總結**：整個開發流程中 OpenClaw 的 Token 消耗接近零

## 實際演示

### Claude Code Agent Teams 簡介
- 在 Claude Code 中建立完整開發團隊
- 每個 Agent 是獨立進程，真正並行執行
- Agent 間可溝通、共享任務、自我識別
- 支援角色分工：前端、後端、測試等

### 演示效果
1. 在 OpenClaw 主 Agent 中下達開發任務（使用 Agent Teams 架構模式開發物理引擎 HTML 遊戲）
2. 任務發送後，主 Agent **不被阻塞**，可繼續執行其他任務（查天氣、講笑話等）
3. Claude Code 在背景獨立完成約 6 分鐘的開發
4. 完成後自動通知群組：包含遊戲路徑、Agent Teams 使用情況、184 個測試通過、完整功能和檔案結構
5. 最終成品：一個粒子物理引擎遊戲（沙、水、火、木、蒸汽等元素互動）

### 關鍵優勢
- 不在電腦前也能用手機發送開發指令
- 完成後通知會發到獨立群組，不干擾主 Agent 對話
- 相關代碼和筆記放在影片描述欄和博客

## 關鍵要點

- 傳統輪詢方式浪費大量 Token → 用 Hooks 實現零輪詢
- Claude Code 14 種 Hooks 中，Stop Hook + Session End 最適合此場景
- Agent Teams 讓 Claude Code 實現真正的團隊協作開發
- 整個方案的核心是「發送一次、獨立執行、完成通知」
