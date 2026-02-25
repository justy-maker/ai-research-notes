# 🚀 OpenClaw 高級進階技巧分享：模型精選策略+記憶系統優化+深度搜索集成+Gateway崩潰自動修復

- **頻道**: AI 超元域
- **日期**: 2026-02-21
- **連結**: https://www.youtube.com/watch?v=7n9qbuzwS-U
- **轉錄方式**: whisper

## 摘要

本期影片分享 OpenClaw 的多個高級使用經驗與技巧：

### 1. 模型精選策略
- **Claude Opus 4.6**：Agentic 能力最強，首選模型（Sonnet 4.6 的 agentic 能力不如 Opus）
- **GPT 5.2（Codex 內建）**：適合非複雜任務，額度比 Opus 多很多，可用 think 命令調整思考級別
- **GPT 5.3 Codex**：只適合編碼場景，不適合 agentic 任務
- **MiniMax M2.1**：開源模型首選，響應速度和推理能力都不錯

### 2. 記憶系統優化 — Topics 拆分
- 將 MEMORY.md 按主題拆分到 `memory/topics/` 資料夾
- 拆分前：15KB 單檔混雜 → 拆分後：2.3KB 核心規則 + 獨立主題檔
- 主題包括：配置、多 Agent 協作、瀏覽器自動化、Docker、節點配置等
- 優勢：memory_search 按主題精準命中，各主題獨立膨脹不互干

### 3. 深度搜索集成（Codex CLI）
- OpenClaw 自帶的 Brave Search + web_fetch 功能有限
- 作者寫了一個 skill 整合 Codex CLI 的 deep research 功能
- 決策樹：URL → web_fetch / 簡單查詢 → Brave / 複雜多元 → Codex 多輪搜索

### 4. Gateway 重啟防護機制
- 問題：插件 bug（如 DingTalk 未捕獲異常）導致 Gateway 崩潰
- 解法：systemd OnFailure 觸發修復腳本
- 腳本流程：讀 Gateway 日誌 → 呼叫 Claude Code 分析 → 修改配置/代碼 → 重啟 → 8 秒後檢查
- 最多嘗試 2 次修復，失敗則通知用戶

## 關鍵字
OpenClaw, 模型選擇, Claude Opus 4.6, GPT 5.2, MiniMax, 記憶拆分, Topics, Codex 搜索, Gateway 自動修復, systemd
