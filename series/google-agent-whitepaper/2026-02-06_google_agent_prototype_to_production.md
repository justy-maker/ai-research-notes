# Google AI Agent 白皮書拆解⑤ - Prototype to Production（最終章）

## 基本資訊
- **影片連結**: https://youtu.be/j2xRwa0SECw
- **頻道**: AI 技術解讀（推測）
- **時長**: 21:02
- **整理日期**: 2026-02-06
- **系列**: Google 5-Day AI Agents Intensive 課程解讀 (第5集/最終章)

## 分類
- **主題**: AI Agent 生產化 / 多智能體協作
- **標籤**: `#AI-Agent` `#A2A` `#MCP` `#AgentOps` `#Multi-Agent` `#Production` `#Registry`

## 關鍵詞
A2A Protocol, MCP, Agent Card, Hierarchical Composition, Distributed Tracing, State Management, Registry, Auto Delegation, AgentOps, Google ADK

---

## 核心問題：孤島效應 (Silos)

每個團隊都在重複造輪子：
- 能力無法複用
- 洞察無法流通
- **這是規模化最大的瓶頸**

---

## 兩層協議標準

| 層級 | 協議 | 解決的問題 | 比喻 |
|------|------|-----------|------|
| 底層 | **MCP** (Model Context Protocol) | 工具集成（連資料庫、調 API） | Agent 的**手** |
| 上層 | **A2A** (Agent to Agent) | Agent 協作（委託複雜任務） | Agent 的**社交網路** |

### 何時用哪個？

| 場景 | 用什麼 | 說法 |
|------|--------|------|
| 「幫我算 1+1」 | MCP | Do this specific thing（具體指令） |
| 「分析上季度客戶流失原因並給對策」 | A2A | Achieve this complex goal（複雜目標） |

> **MCP 是指揮計算器，A2A 是委託專家**

---

## Agent Card（Agent 的電子名片）

A2A 協議的核心機制，是一個標準化 JSON 文件：

```json
{
  "我是誰": "...",
  "我有什麼技能": "...",
  "我的安全要求": "...",
  "怎麼連接我": "..."
}
```

**價值**：Agent 可以在網路中**自動發現彼此**，不需要人工硬編碼

### Google ADK 一行代碼

```python
# 把你的 Agent 包裝一下
# ADK 自動生成 Agent Card 並啟動服務端口
# 其他 Agent 可以通過 URL 直接消費你的能力
```

---

## Hierarchical Composition（層級組合）

```
            Root Agent（總管）
           /                \
    Local SubAgent      Remote Specialist Agent
    （簡單任務）              （專業任務，via A2A）
```

> 從**單兵作戰**變成**軍團作戰**

---

## 分布式協作的兩個硬門檻

### 1. Distributed Tracing（分布式追踪）
- 請求在多個 Agent 間跳來跳去
- **Trace ID 必須透傳**
- 否則出問題找不到是誰的鍋

### 2. State Management（狀態管理）
- A2A 交互通常是**多輪、長週期**的
- 必須有可靠的持久化層
- 保證**事務一致性**

---

## Local SubAgent vs A2A 服務

不是所有 Agent 都要拆成 A2A 服務！

| 場景 | 選擇 | 原因 |
|------|------|------|
| 跨團隊、跨項目、需要正式服務契約 | A2A | 標準化協作 |
| 同應用內、任務緊密且清晰 | Local SubAgent | 效率更高 |

> **不要為了微服務而微服務**

---

## Registry（註冊中心）

### 何時需要？

| 規模 | 方案 |
|------|------|
| 50 個工具 | 手動配置就行 |
| 5000 個工具（分布在不同部門） | 必須上 Registry |

### 三種工具使用模式

| 模式 | 說明 | 特點 |
|------|------|------|
| **Generalist** | 給 Agent 全量目錄 | 什麼都能幹，但可能不夠精 |
| **Specialist** | 只給預定義的一小部分工具 | 專精且安全 |
| **Dynamic** | Agent 運行時自己去 Registry 搜索並動態加載 | 最靈活 |

### Registry 的價值

| 對象 | 價值 |
|------|------|
| 開發者 | 搜到已有工具，避免重複造輪子 |
| 安全團隊 | 審計誰用了什麼工具 |
| 產品經理 | 一目了然看到能力版圖 |

> **Registry 是治理的核心抓手**

---

## Agent Registry 與 Auto Delegation

- 把 Agent 註冊進去 → 成為公司資產
- 未來更高級的 Agent 可以：
  - 自動查詢 Registry
  - 發現並「雇傭」其他 Agent
  - 實現**真正的自動化委託 (Auto Delegation)**

> **這是未來的方向**

---

## AgentOps 完整生命周期

```
開發者內循環 → 帶評估門禁的流水線 → 安全灰度發布
                    ↓
            生產環境全鏈路觀測
                    ↓
              數據驅動持續進化
                    ↓
           多 Agent 互操作生態
```

---

## 🎯 五集完整回顧

| 集數 | 主題 | 核心能力 |
|------|------|---------|
| ① | Introduction to Agents | 概念基石、架構語言 |
| ② | MCP（Tools Interoperability） | 從「會回答」到「會行動」 |
| ③ | Context Engineering & Memory | 連續性與可進化性 |
| ④ | Agent Quality | 黑盒變透明可控 |
| ⑤ | Prototype to Production | 工程化封頂、落地之路 ⬅️ 本集 |

---

## 💡 研究啟發

1. **MCP vs A2A 的區分很清晰** - 工具 vs 協作，指令 vs 目標
2. **Agent Card 是多智能體生態的基礎** - 自動發現、無需硬編碼
3. **不要過度微服務化** - Local SubAgent 在很多場景更高效
4. **Registry 是規模化的必經之路** - 工具治理、能力複用、安全審計
5. **Auto Delegation 是未來方向** - Agent 自動發現並雇傭其他 Agent

---

## 🏆 系列總結

這五集白皮書拆解構成了完整的 **AI Agent 工程化方法論**：

```
概念定義 → 工具調用 → 記憶系統 → 品質管理 → 生產落地
```

從實驗到生產的完整路徑，值得反覆研讀！

---

*此摘要由阿福 🐶 整理，使用 Whisper 轉錄（影片無字幕）*
