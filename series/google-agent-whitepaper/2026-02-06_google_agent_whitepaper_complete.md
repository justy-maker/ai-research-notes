# Google AI Agent 白皮書完整拆解 - 五集總整理

> **來源**: Google × Kaggle「5-Day AI Agents Intensive」課程白皮書解讀系列
> **整理日期**: 2026-02-06
> **整理者**: 阿福 🐶

---

## 📚 系列概覽

| 集數 | 主題 | 核心轉變 | 連結 |
|------|------|---------|------|
| ① | Introduction to Agents | 定義架構語言 | [影片](https://youtu.be/...) |
| ② | MCP (Tools Interoperability) | 會回答 → 會行動 | [影片](https://youtu.be/...) |
| ③ | Context Engineering & Memory | 無連續性 → 可進化 | [影片](https://youtu.be/K7lSaM3OoeA) |
| ④ | Agent Quality | 黑盒 → 透明可控 | [影片](https://youtu.be/6rylkEOBqxI) |
| ⑤ | Prototype to Production | 實驗 → 生產落地 | [影片](https://youtu.be/j2xRwa0SECw) |

---

## 🧠 第三集：Context Engineering & Memory

### 核心金句
> **「Memory 不是存出來的，是算出來的。」**

### Memory ETL Pipeline（四步驟）

```
Ingestion → Extraction → Consolidation → Storage
  攝入        提取（LLM）    整合（融合新舊）    落庫
```

- **Extraction**: 用 Topic Definitions 定向過濾，要 Signal 不要 Noise
- **Consolidation**: ⭐ 核心壁壘！新舊記憶融合、衝突解決、保證唯一真理性

### Provenance（血緣）權重

| 來源 | 權重 |
|------|------|
| Explicit Input（用戶親口說） | 高 |
| Implicit Inference（LLM 推測） | 低 |

### 檢索三維打分

| 維度 | 說明 |
|------|------|
| Relevance | 語意相似度 |
| Recency | 新鮮度 |
| Importance | 重要性 |

### Context 注入位置

| 位置 | 適合放 | 風險 |
|------|--------|------|
| System Instructions | 穩定畫像（User Profile） | 無 |
| Conversation History | 當前細節 | Dialogue Injection |

### 安全紅線
1. ACL 隔離（A 的記憶 B 不能看）
2. PII 脫敏
3. 防 Memory Poisoning

---

## 📊 第四集：Agent Quality

### 監控 ≠ 可觀測性

| Monitoring | Observability |
|------------|---------------|
| 系統還在跑嗎？ | Agent 思考的對不對？ |

### 可觀測性三大支柱

| 支柱 | 比喻 | 用途 |
|------|------|------|
| **Logging** | 日記 | 結構化 JSON，記錄 Prompt/Response/Tool Call |
| **Tracing** | 串珍珠的線 | 因果鏈，找 Root Cause |
| **Metrics** | 體檢單 | 整體健康狀況 |

### 💡 Intent-Outcome Pattern（高收益日誌模式）

```
行動前 → 記 Intent（意圖）
行動後 → 記 Outcome（結果）
```
快速區分「沒想做」vs「做砸了」

### 指標分層

| 類型 | 給誰看 | 關注 |
|------|--------|------|
| System Metrics | SRE/運維 | 延遲、錯誤率、Token |
| Quality Metrics | 產品經理 | 準確性、有用性 |

### Dynamic Sampling

| 請求類型 | 採樣率 |
|---------|--------|
| 成功 | 1% |
| 失敗 | 100% |

### Quality Flywheel（質量飛輪）

```
定義質量 → 埋點觀測 → 評估過程 → 反饋回路
                              ↓
              線上失敗 → 沉澱為測試用例 → 持續進化
```

### 🎯 三條心法

1. **Evaluation 是架構支柱**，不是事後補救
2. **Trajectory is the Truth** - 過程即真相
3. **The Human is the Arbiter** - 人是最終裁決者

---

## 🚀 第五集：Prototype to Production

### 兩層協議標準

| 協議 | 解決問題 | 比喻 | 使用場景 |
|------|---------|------|---------|
| **MCP** | 工具集成 | Agent 的手 | 「幫我算 1+1」（具體指令） |
| **A2A** | Agent 協作 | Agent 的社交網路 | 「分析客戶流失原因」（複雜目標） |

> **MCP 是指揮計算器，A2A 是委託專家**

### Agent Card（電子名片）

標準化 JSON，包含：我是誰、技能、安全要求、連接方式
→ Agent 自動發現彼此，無需硬編碼

### Hierarchical Composition（層級組合）

```
        Root Agent（總管）
       /                \
Local SubAgent      Remote Specialist (A2A)
 （簡單任務）           （專業任務）
```

### 分布式協作硬門檻

1. **Distributed Tracing** - Trace ID 必須透傳
2. **State Management** - 多輪長週期需持久化

### Local SubAgent vs A2A

| 場景 | 選擇 |
|------|------|
| 跨團隊、需服務契約 | A2A |
| 同應用內、任務緊密 | Local SubAgent |

> **不要為了微服務而微服務**

### Registry（註冊中心）

| 規模 | 方案 |
|------|------|
| 50 工具 | 手動配置 |
| 5000 工具 | 必須上 Registry |

**三種使用模式**：
- **Generalist**: 全量目錄
- **Specialist**: 預定義子集
- **Dynamic**: 運行時搜索加載

### Auto Delegation（未來方向）

Agent 自動查詢 Registry → 發現並「雇傭」其他 Agent

---

## 🏆 完整 AgentOps 生命周期

```
┌─────────────────────────────────────────────────────────┐
│  開發者內循環                                              │
│       ↓                                                  │
│  帶評估門禁的 CI/CD 流水線                                  │
│       ↓                                                  │
│  安全灰度發布                                              │
│       ↓                                                  │
│  生產環境全鏈路觀測（Logging + Tracing + Metrics）          │
│       ↓                                                  │
│  數據驅動持續進化（Quality Flywheel）                       │
│       ↓                                                  │
│  多 Agent 互操作生態（MCP + A2A + Registry）               │
└─────────────────────────────────────────────────────────┘
```

---

## 💎 核心概念速查表

| 概念 | 一句話解釋 |
|------|-----------|
| **Memory ETL** | Memory 是算出來的，不是存出來的 |
| **Consolidation** | 新舊記憶融合，保證唯一真理性 |
| **Intent-Outcome** | 記意圖+結果，區分沒想做 vs 做砸了 |
| **Quality Flywheel** | 失敗案例 → 測試用例 → 持續進化 |
| **MCP** | 工具集成協議（Agent 的手） |
| **A2A** | Agent 協作協議（Agent 的社交網路） |
| **Agent Card** | Agent 的電子名片，自動發現 |
| **Registry** | 工具/Agent 註冊中心，治理核心 |
| **Auto Delegation** | Agent 自動雇傭其他 Agent |

---

## 🎯 實戰檢查清單

### Memory 系統
- [ ] ETL Pipeline 是否異步後台執行？
- [ ] Consolidation 是否處理新舊衝突？
- [ ] 檢索是否三維打分（Relevance + Recency + Importance）？
- [ ] PII 脫敏是否在入庫前完成？

### 可觀測性
- [ ] 日誌是否結構化 JSON？
- [ ] 是否實現 Intent-Outcome Pattern？
- [ ] System Metrics 和 Quality Metrics 是否分開？
- [ ] 失敗請求是否 100% 採樣？

### 生產化
- [ ] 是否需要 A2A（跨團隊）還是 Local SubAgent（同應用）？
- [ ] Trace ID 是否在分布式調用中透傳？
- [ ] 工具數量是否需要上 Registry？
- [ ] 是否有 Quality Flywheel 持續改進機制？

---

## 📁 相關檔案

- [第三集詳細筆記](./2026-02-06_google_agent_context_memory.md)
- [第四集詳細筆記](./2026-02-06_google_agent_quality.md)
- [第五集詳細筆記](./2026-02-06_google_agent_prototype_to_production.md)

---

*此總整理由阿福 🐶 整理，使用 Whisper 轉錄（影片無字幕）*
*Google × Kaggle 5-Day AI Agents Intensive 課程白皮書解讀系列*
