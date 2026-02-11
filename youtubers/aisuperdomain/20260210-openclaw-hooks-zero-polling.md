# OpenClaw 高級使用經驗 - Claude Code Hooks 回調實現零輪詢

> **頻道**：AI 超元域 (@aisuperdomain)
> **影片 ID**：iJEfIc1mrsc
> **日期**：2026-02-10
> **連結**：https://www.youtube.com/watch?v=iJEfIc1mrsc

## 重點摘要

1. **解決 Token 消耗痛點**：傳統方式用 OpenClaw 調用 Claude Code 會因不斷輪詢而消耗大量 Token
2. **Hooks 回調機制**：利用 Claude Code 的 Hooks 功能，實現事件驅動的回調，達到幾乎零 Token 消耗
3. **Agent Teams 協作**：Claude Code 的 Agent Teams 特性允許創建多個 Agent（前端、後端、測試）並行執行
4. **零輪詢流程**：OpenClaw 派發任務 → Claude Code 自主開發 → Stop Hook 觸發 → Wake Event 喚醒 → 讀取結果推送
5. **雙重保障**：使用 `stop hook` + `session_end` 確保回調的穩定性

## 核心概念

透過 **Claude Code 的 Hooks 功能**，將互動模式從高成本的持續輪詢（Polling）轉變為低成本的事件驅動回調（Event-driven Callback）。結合 **Agent Teams 特性**，實現 AI 自主開發與協作能力。

## 實作步驟

1. **OpenClaw 派發任務**：向 Claude Code 發送開發任務
2. **Claude Code 自主開發**：利用 Agent Teams 並行開發（前端/後端/測試 Agent）
3. **設定 Stop Hook**：配置任務完成時觸發的回調
4. **觸發 Wake Event**：完成時自動發送「完成」信號
5. **OpenClaw 讀取結果**：接收 Wake Event 後讀取成果
6. **結果推送**：推送到聊天軟件通知用戶
7. **雙重保障**：結合 `stop hook` 與 `session_end` 兩個機制

## 標籤

#OpenClaw #ClaudeCode #Hooks #AgentTeams #Token優化 #零輪詢 #AI開發
