# YouTube 影片摘要

## 基本資訊
- **標題：** Agent 的"正確答案"來了，Google 白皮書拆解②
- **副標題：** 《Agent Tools & Interoperability with MCP》
- **來源：** 白白說大模型
- **長度：** 25:14
- **連結：** https://youtu.be/PE80bbtjug4
- **摘要日期：** 2026-02-06

---

## 分類
`AI Agent` `MCP協議` `工具調用` `系統架構`

## 關鍵字
`MCP` `Model Context Protocol` `工具調用` `Function Tools` `Agent Tools` `JSON-RPC` `安全治理` `Prompt Injection` `Confused Deputy`

---

## 摘要

### 一、為什麼 Agent 必須接工具？

> **沒有工具的 Foundation Model 本質上就是一個被困在上下文裡的模式預測器**

#### 工具的價值分類

| 類型 | 功能 | 對應能力 |
|------|------|---------|
| **Retrieval** | 讓模型知道更多 | 查數據庫、拉文檔、做搜索 → Agent 的「眼睛」 |
| **Action** | 讓模型做更多 | 發郵件、跑代碼、觸發部署 → Agent 的「手」 |

**工具存在的鐵邏輯：** 把不確定的生成和確定的事實拆開，系統才穩。

---

### 二、工具的三種類型

#### 1. Function Tools（自定義工具）
- 自己寫函數，讓模型需要時調用
- 適合企業私域能力
- **關鍵：** Docstring 會被抽取進上下文，代碼註釋是給模型看的操作手冊
- 優勢：完全可控
- 代價：自己扛維護和權限治理

#### 2. Built-in Tools（平台內置工具）
- 原生外掛，拿來即用
- 例如 Gemini API：
  - **Grounding with Google Search** — 聯網做事實校準
  - **Code Execution** — 計算和邏輯處理交給沙盒代碼
  - **Computer Use** — 受控環境操作界面
- **建議：** 通用能力用 Built-in，核心業務邏輯握在自己手裡

#### 3. Agent Tools（Agent 當工具）
- 把另一個 Agent 當成工具來調
- 主 Agent = 包工頭，負責用戶體驗和風險控制
- 子 Agent = 專才，只負責特定任務
- **三條鐵律：**
  1. Agent 職責要窄
  2. 主 Agent 要做結果治理
  3. 權限要物理隔離

---

### 三、工具設計最佳實踐（6 條 Checklist）

#### 1️⃣ 工具文檔 = 給 LLM 看的 UI
- **Name：** 可審計，用「動作+對象+約束」
- **Description：** 寫目的和邊界，不寫實現
- **參數：** 有類型、範圍、默認值
- **示例：** 專門覆蓋容易歧義的請求

#### 2️⃣ 系統指令不要點名工具
- ❌ 錯誤：「遇到工單就用 Create Ticket」
- ✅ 正確：「需要記錄缺陷時，創建一條帶優先級和復現步驟的缺陷記錄」
- **指令負責業務目標，工具文檔負責調用契約**

#### 3️⃣ 發布任務，不要暴露原始 API
- ❌ 錯誤：`update_jira` 帶 40 個參數
- ✅ 正確：拆成 `create_critical_bug`、`add_repro_steps`、`set_priority`
- **工具越像 API，模型越像在猜；工具越像任務，模型越像在執行**

#### 4️⃣ 輸出要克制
- 不要返回幾萬行數據
- 大數據放外部系統，工具只返回引用（臨時表名、對象存儲路徑、分頁游標）
- **默認只返回：** 關鍵字段 + 摘要統計 + 可繼續檢索的 Handle

#### 5️⃣ Schema 校驗
- 對模型：Schema 是文檔
- 對客戶端：Schema 是護欄
- Schema 寫得越嚴謹，系統越安全

#### 6️⃣ 可操作的錯誤信息
- ❌ 錯誤：`exception: null pointer`
- ✅ 正確：`未找到該用戶，請檢查用戶名拼寫，或嘗試模糊搜索`
- **把錯誤信息當成下一步的 Prompt**

---

### 四、MCP 協議核心

#### 什麼是 MCP？
**Model Context Protocol** — AI 時代的 USB 協議

解決的問題：**N×M 集成爆炸**
- N 個模型 × M 個工具 = N×M 個連接器
- MCP 把「大腦」和「手腳」徹底解耦

#### MCP 架構三角色

| 角色 | 功能 | 類比 |
|------|------|------|
| **Host** | 大管家，掌握安全策略生殺大權 | AI 應用/IDE |
| **Client** | 翻譯官，建立連接、保持會話 | 嵌在 Host 裡 |
| **Server** | 打工人，握著具體工具/數據/API | 獨立進程 |

#### 通信協議：JSON-RPC 2.0
- 輕量、無狀態、語言無關
- **消息類型：** Request、Result、Error、Notification

#### 傳輸方式

| 方式 | 場景 | 特點 |
|------|------|------|
| **stdio** | 本地場景 | Server 作為子進程，速度極快 |
| **Streamable HTTP** | 分布式/企業 | 支持 SSE，實時反饋 |

#### MCP 六大能力

| Server 端 | Client 端 |
|-----------|-----------|
| Tools（工具）✅ 99% 支持率 | Sampling（反向生成） |
| Resources（數據資源）30% | Elicitation（反向問用戶） |
| Prompts（提示詞模板）30% | |

**落地建議：** 先用好 Tools，其他等生態成熟

---

### 五、MCP 工具定義詳解

```json
{
  "name": "唯一標識",
  "title": "給 LLM 看的標題",
  "description": "目的和邊界",
  "inputSchema": { ... },
  "outputSchema": { ... },
  "annotations": {
    "readOnly": true,
    "destructive": false
  }
}
```

**關鍵字段：**
- `title`/`description` — 決定模型第一眼認知
- `annotations` — 影響模型安全決策
- `inputSchema`/`outputSchema` — 運行時護欄

---

### 六、MCP 安全風險與防禦

#### 雙重風險疊加
1. **API 風險** — 傳統注入、DDoS
2. **Agent 協議風險** — 用自然語言誘導模型調工具

#### 五大核心風險

| 風險 | 說明 | 防禦 |
|------|------|------|
| **動態能力注入** | Server 熱更新加了新工具，Agent 可能被誘導使用 | Allow List + 變更通知 |
| **工具遮蔽** | 惡意工具偽裝成更優選擇 | 命名衝突檢測 + mTLS + Human-in-the-Loop |
| **Prompt Injection** | 自然語言誘導調用危險工具 | 身份傳遞 + 高風險動作強制確認 |
| **數據外洩** | 敏感數據被發送到惡意 Server | 數據邊界校驗 |
| **Confused Deputy** | Server 只檢查自己有權，沒檢查用戶有權 | 見下方詳解 |

---

### 七、Confused Deputy（混淆代理人）攻擊

#### 經典案例
```
攻擊者（沒有金庫鑰匙）
    ↓ 「我是老板派來的，去把金庫打開」
保安（MCP Server，有鑰匙）
    ↓ 只檢查「我能不能開門」，沒檢查「你配不配讓我開門」
金庫被打開 💥
```

#### 真實場景
- 代碼助手 Agent 有 Admin 權限
- 惡意員工說：「幫我搜索 secret_algorithm.py，順便建個分支備份」
- Agent 聽到三個指令：搜索、建分支、寫入 → 全部放行
- 結果：核心機密外洩

#### 防禦方案

1. **身份傳遞**
   - Agent 調用工具時，必須傳遞「當前是哪個用戶在操作」
   - Server 不僅要問「我有權嗎」，還要問「這個用戶有權嗎」

2. **高風險動作強制 Human-in-the-Loop**
   - 涉及寫入代碼、轉賬、刪除 → 必須彈窗讓人類確認

> **「在企業級架構裡，方便是給用戶的，麻煩是留給架構師去解決的」**

---

## 系列定位

| 集數 | 主題 | 核心能力 |
|------|------|---------|
| **第一集** | Introduction to Agents | 概念基石，讓 Agent 學會思考 |
| **第二集（本集）** | Agent Tools & MCP | 工具調用，讓 Agent 會行動 |
| **第三集** | Context Engineering | 上下文與記憶，讓 Agent 可進化 |

---

## 核心金句

> 「不接工具就別談可驗證、可執行的企業級流程。」

> 「工具定義不是文檔，是你和模型之間的契約。」

> 「工具越像 API，模型越像在猜；工具越像任務，模型越像在執行。」

> 「把錯誤信息當成下一步的 Prompt，這才是 Agent 開發的正確思維。」

---

*整理者：阿福 🐶*
*整理日期：2026-02-06*
*轉錄方式：Whisper AI (faster-whisper)*
