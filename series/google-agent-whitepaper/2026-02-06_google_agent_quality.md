# Google AI Agent 白皮書拆解④ - Agent Quality

## 基本資訊
- **影片連結**: https://youtu.be/6rylkEOBqxI
- **頻道**: AI 技術解讀（推測）
- **時長**: 19:22
- **整理日期**: 2026-02-06
- **系列**: Google 5-Day AI Agents Intensive 課程解讀 (第4集)

## 分類
- **主題**: AI Agent 品質管理 / 可觀測性
- **標籤**: `#AI-Agent` `#Observability` `#Quality-Engineering` `#Monitoring` `#Tracing` `#MLOps`

## 關鍵詞
Observability, Monitoring, Logging, Tracing, Metrics, Quality Flywheel, PII Scrubbing, Dynamic Sampling, Intent-Outcome Pattern, Trajectory, Evaluation

---

## 核心概念

### 監控 ≠ 可觀測性

| 對比 | Monitoring（監控） | Observability（可觀測性） |
|------|-------------------|-------------------------|
| 比喻 | 快餐店流水線廚師 | 米其林大廚 |
| 問的問題 | 系統還在跑嗎？ | Agent 思考的對不對？ |
| 關注點 | 爐子熱不熱、出餐快不快 | 烹飪思路、食材搭配 |

---

## 可觀測性三大支柱

### 1. Logging（日誌）📓
- **比喻**：日記，記錄每一個離散的事實
- **要求**：
  - 必須是**結構化 JSON**（不是 print 給人看的）
  - 記錄：Prompt、Response、Tool Call 參數、錯誤、內部狀態變化
  - 權衡 Verbosity 與性能（生產環境別打所有 debug）

#### 💡 高收益日誌模式：Intent-Outcome Pattern
```
行動前 → 記錄 Intent（意圖）
行動後 → 記錄 Outcome（結果）
```
**好處**：能區分「沒想做」（Intent 缺失）vs「做砸了」（Outcome 失敗）

### 2. Tracing（鏈路追踪）🔗
- **比喻**：把散落的珍珠串起來的那根線
- **價值**：看到完整的因果鏈，直接帶你到 Root Cause

**範例**：
```
Rug 解鎖失敗 → Tool Call 參數傳空值 → LLM 報錯
（三個孤立錯誤 → 一條因果鏈）
```

**技術關鍵詞**：
- **Span**：鏈路裡的每個步驟（LLM 調用、工具執行）
- **Attributes**：步驟的元數據（耗時、Token 數）
- **Context Propagation**：用 Trace ID 串起全鏈路
- 與 Google Cloud Trace 打通，實現端到端透視

### 3. Metrics（指標）📊
- **比喻**：體檢單，會總看整體健康狀況

---

## 指標分層（重要！）

| 類型 | 給誰看 | 關注什麼 | 比喻 |
|------|--------|---------|------|
| **System Metrics** | SRE/運維 | 延遲、錯誤率、Token 消耗 | 生命體征 |
| **Quality Metrics** | 產品經理 | 準確性、有用性、軌跡一致度 | 智力水平 |

⚠️ **不要混在一起**，否則出問題不知道該找運維還是算法工程師

### Dashboard 也要分開
- **Operational Dashboard**：關注穩定性（紅燈亮 = 系統掛了，立刻修）
- **Quality Dashboard**：關注質量漂移（有用性曲線下降 = 模型過時/Prompt 需優化）

---

## 隱私紅線：PII Scrubbing

> 用戶聊天記錄可能包含電話、地址、甚至密碼

**鐵律**：
- 日誌入庫前，必須加 **PII Scrubbing（隱私清洗）工序**
- 不要等數據存下來再想怎麼刪
- 這是合規底線，也是對用戶的尊重

---

## 成本權衡：Dynamic Sampling

全量開啟 Tracing 非常貴，也會拖慢系統。

**最佳實踐**：動態採樣
| 請求類型 | 採樣率 | 原因 |
|---------|--------|------|
| 成功的請求 | 1% | 統計用，省錢 |
| 失敗的請求 | 100% | 不漏掉任何 Bug |

這是工程上的最優點：既省錢，又不漏 Bug。

---

## Agent Quality Flywheel（質量飛輪）

```
定義質量 → 埋點觀測 → 評估過程 → 反饋回路
                              ↓
              線上失敗案例 → 沉淀為新測試用例
                              ↓
                    每一次轉動，Agent 更聰明更穩健
```

**這就是從 Demo 到生產系統的必經之路**

---

## 🎯 三條核心原則（Agent Quality 心法）

### 1. Evaluation 是架構支柱，不是事後補救
> 要設計在系統裡

### 2. Trajectory is the Truth（過程即真相）
> 不要只看結果

### 3. The Human is the Arbiter（人是最終裁決者）
> 人定義價值

---

## 系列定位

| 集數 | 主題 | 核心能力 |
|------|------|---------|
| ① | Introduction to Agents | 概念基石、架構定義 |
| ② | MCP（Tools Interoperability） | 從「會回答」到「會行動」 |
| ③ | Context Engineering & Memory | 從「無連續性」到「可進化性」 |
| ④ | Agent Quality | 可觀測性與質量飛輪 ⬅️ 本集 |
| ⑤ | Prototype to Production | 部署擴展、A2A、Vertex AI（下一集） |

---

## 💡 研究啟發

1. **Intent-Outcome Pattern** - 簡單但高效的日誌設計，值得採用
2. **指標分層是關鍵** - System vs Quality Metrics 不要混淆
3. **Dynamic Sampling** - 成本與完整性的最優平衡
4. **Quality Flywheel** - 持續改進的閉環系統設計
5. **PII Scrubbing** - 生產系統的合規底線

---

*此摘要由阿福 🐶 整理，使用 Whisper 轉錄（影片無字幕）*
