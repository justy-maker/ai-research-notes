# How I'm Using AI Agents in 2026

- **頻道**: Tech With Tim
- **日期**: 2026-02-22
- **連結**: https://www.youtube.com/watch?v=BikPUaT76i8

## 重點摘要

Tim 展示如何使用 Warp 的 Oz agent 平台在雲端同時運行多個 AI agent 來處理複雜開發任務。

### Warp + Oz 平台介紹
- **Warp**：不只是終端機，是「agentic development environment」
- **Oz**：Warp 的雲端 agent 平台，可從終端、UI 或第三方軟體觸發
- 核心理念：AI 時代下，手動寫程式越來越少，焦點應放在終端（運行命令、設定環境、觸發 agent）

### 核心功能
1. **雲端 Agent 運行**：可同時啟動 5、10、20 個 agent，不受本機限制
2. **環境（Environment）**：Docker 容器 + GitHub repo 連結，agent 在隔離環境中操作
3. **技能（Skills）**：可重複使用的任務定義（如前端開發、後端開發、測試）
4. **排程（Schedules）**：可設定 agent 定時執行（每小時、每天、每月）
5. **整合（Integrations）**：GitHub、Slack、Linear，或自建 API 整合
6. **Session SSH**：可直接 SSH 連入雲端 agent 進行即時操控

### 實作流程
1. 建立 spec 檔案描述專案需求與技術堆疊
2. 用本地 agent 進行專案骨架搭建（scaffolding）
3. 建立 GitHub repo 並推送程式碼
4. 建立 Oz 雲端環境（Team Environment）
5. 執行 `/init` 生成 agents.md（agent 的專案上下文）
6. 用本地 agent 產生三個任務計畫（前端/後端/測試）
7. 建立三個 Skills 對應三個計畫
8. 同時啟動三個雲端 agent 平行執行，各自提交 PR

### GitHub Action 整合
- 設定 GitHub Action：每次 PR 自動觸發 Oz agent 進行程式碼審查
- 需在 GitHub Secrets 中加入 Warp API Key

## 關鍵觀點

- **從單一本地 agent → 多個雲端 agent 平行運作**是 2026 年的開發趨勢
- 關閉筆電 agent 繼續工作：真正的非同步開發
- agent 能自動使用工具，你不需要記住命令語法
- 專案前期投入充分上下文（spec、agents.md、plans）能大幅提升 agent 品質
- 終端 > 程式碼編輯器：AI 時代的開發重心轉移

## 行動建議

1. **試用 Warp**：免費下載，體驗 AI 原生終端的工作方式
2. **學習 agent 工作流設計**：先寫 spec → scaffold → 分拆任務 → 平行執行
3. **設定 CI/CD 的 agent 審查**：每個 PR 自動觸發 AI code review
4. **善用 Skills 機制**：將常見任務封裝為可重複使用的 skill
5. **為專案建立 agents.md**：讓任何 agent 都能快速理解專案上下文
