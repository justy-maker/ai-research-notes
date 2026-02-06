# Google AI Agent 白皮書拆解③ - Context Engineering Sessions & Memory

## 基本資訊
- **影片連結**: https://youtu.be/K7lSaM3OoeA
- **頻道**: AI 技術解讀（推測）
- **時長**: 18:40
- **整理日期**: 2026-02-06
- **系列**: Google 5-Day AI Agents Intensive 課程解讀 (第3集)

## 分類
- **主題**: AI Agent 架構 / 記憶系統設計
- **標籤**: `#AI-Agent` `#Memory-Systems` `#Context-Engineering` `#LLM架構` `#RAG` `#向量搜索` `#ETL`

## 關鍵詞
Memory ETL Pipeline, Session Context, Long-term Memory, Ingestion, Extraction, Consolidation, Provenance, Lineage, Vector Search, Retrieval Strategy, ACL隔離, Memory Poisoning

---

## 核心概念

### Memory 的本質
> **「Memory 不是存出來的，是算出來的。」**

Memory 本質上是一個由 LLM 驅動的 ETL 流水線，不像傳統資料庫直接 insert。

---

## Memory 生成流水線（四步驟）

### 1. Ingestion（攝入）
- 把原始對話餵進系統

### 2. Extraction（提取）
- 用 LLM 提取有價值的信息
- 過濾掉廢話和噪音
- 取決於 **Topic Definitions**：
  - 嚴格的 JSON Schema（如：提取航班號和日期）
  - 自然語言描述
  - Few-shot Examples 讓模型模仿
- 目標：**要 Signal，不要 Noise**

### 3. Consolidation（整合）⭐ 最關鍵
- 新信息與舊記憶融合
- **動態自編輯過程**
- 範例：用戶說「我搬家去上海了」→ 系統必須 update/delete「住在北京」的舊記憶
- 保證知識庫的**唯一真理性**

### 4. Storage（存儲）
- 最後才落庫
- 主流做法：存文本，圖片轉成語意描述（如：「用戶發了一張紅色的鞋子」）
- 這樣檢索效率最高

---

## Provenance（血緣）與 Lineage（足譜）

整合時判斷誰更可信：

| 來源類型 | 權重 |
|---------|------|
| Explicit Input（用戶親口說的） | 高 |
| Implicit Inference（LLM 從閒聊猜出來的） | 低 |

記錄：
- **Source Type**（來源類型）
- **Freshness**（新鮮度）

衝突時：高權重覆蓋低權重，新的覆蓋舊的。

---

## ETL 執行時機（工程權衡）

| 策略 | 優點 | 缺點 |
|------|------|------|
| Real-time（每輪跑） | 最新鮮 | 最貴、最慢 |
| Session Completion（會話結束跑） | 最省錢 | 可能丟細節 |

**鐵律**：Memory 生成必須在後台異步進行（Asynchronous Background Process），千萬別讓用戶盯著螢幕轉圈等 ETL。

---

## 檢索策略（三維打分）

不能只看 Vector Search 的語意相似度！

| 維度 | 說明 |
|------|------|
| **Relevance**（相關性） | 與查詢的語意相似度 |
| **Recency**（新鮮度） | 最近發生的權重更高 |
| **Importance**（重要性） | 有些事雖然久遠但刻骨銘心 |

目標：在嚴格的延遲預算內，做到**少而精**。

---

## 檢索時機

| 策略 | 說明 | 優缺點 |
|------|------|--------|
| **Proactive**（預加載） | 每輪對話開始前先搜一圈 | 快，但可能搜一堆廢話 |
| **Reactive**（按需） | 記憶做成 Tool，讓 Agent 自己決定要不要查 | 更智能，但多一次 LLM 調用延遲 |

根據 **Latency Budget**（延遲預算）選擇。

---

## Context 注入位置

記憶要流回 Context，通常兩個位置：

| 位置 | 適合放什麼 | 特性 |
|------|-----------|------|
| **System Instructions** | User Profile（穩定畫像） | 上帝視角，權威性高 |
| **Conversation History** | 剛才聊到的具體細節 | 當前語境 |

⚠️ **風險**：放在 History 裡，模型可能搞不清這是「用戶剛說的」還是「系統注入的記憶」→ **Dialogue Injection 風險**

---

## 評估與安全

### 評估指標
- **Precision**：存得對不對
- **Recall@K**：能不能在前幾條搜到

### 安全紅線
1. **ACL 隔離**：A 的記憶 B 絕對不能看
2. **PII 脫敏**：存進去前把身份證號等敏感資訊抹掉
3. **防 Memory Poisoning（記憶投毒）**：
   - 用戶可能故意說錯話誤導 Agent
   - 系統要有驗證機制
   - 別把垃圾當知識存下來

---

## 系列定位

| 集數 | 主題 | 核心能力 |
|------|------|---------|
| ① | Introduction to Agents | 概念基石、架構定義 |
| ② | MCP（Tools Interoperability） | 從「會回答」到「會行動」 |
| ③ | Context Engineering & Memory | 從「無連續性」到「可進化性」 ⬅️ 本集 |

---

## 💡 研究啟發

1. **Memory 是計算問題，不是存儲問題** - 需要 LLM 驅動的智能 ETL
2. **Consolidation 是核心壁壘** - 新舊記憶融合、衝突解決
3. **三維檢索比單純向量搜索更實用** - Relevance + Recency + Importance
4. **安全設計是生產級系統的必備** - ACL、脫敏、防投毒

---

*此摘要由阿福 🐶 整理，使用 Whisper 轉錄（影片無字幕）*
