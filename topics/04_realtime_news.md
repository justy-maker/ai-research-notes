# 如何蒐集即時的財經與科技快訊

> 研究進行中 🔬

## 📋 研究目標

建立自動化的新聞蒐集與篩選系統，即時掌握財經科技動態。

---

## ✅ 最終解決方案

### 目前實作的系統

```
每小時排程（08:00-22:00）
         ↓
web_fetch 抓取新聞網站 + Twitter
         ↓
AI 篩選重要新聞（1-5 則）
         ↓
發送到 Discord #重要新聞 頻道
```

### 追蹤目標

**人物**：川普、馬斯克、黃仁勳、奧特曼
**公司**：Google、OpenAI、Anthropic、TSMC、Tesla、Nvidia

---

## 📝 研究筆記（新 → 舊）

### 2026-02-07 22:45 - 阿福的研究發現與建議

<details>
<summary>研究過程</summary>
<small>

**資料來源**：實際測試各種抓取方式的結果

**研究方法**：試驗不同新聞來源和抓取方式

</small>
</details>

#### 🔍 研究發現

**1. 新聞來源可用性測試**

| 來源 | 方式 | 狀態 | 備註 |
|------|------|------|------|
| Reuters | web_fetch | 🟡 | 偶爾被擋 |
| TechCrunch | web_fetch | ✅ | 穩定可用 |
| The Verge | web_fetch | ✅ | AI 新聞多 |
| CNBC | web_fetch | ✅ | 財經為主 |
| xcancel.com | web_fetch | ✅ | Twitter 替代方案 |
| Twitter 官方 | API | 🔴 | 付費 API |
| Bloomberg | web_fetch | 🔴 | 需付費訂閱 |

**2. Twitter 抓取方案比較**

| 方案 | 狀態 | 優缺點 |
|------|------|--------|
| xcancel.com | ✅ 可用 | 免費、穩定，但部分帳號 403 |
| nitter 實例 | 🟡 不穩 | 實例經常失效 |
| Twitter API | 💰 付費 | 官方但貴（$100/月起） |
| Playwright 爬蟲 | 🟡 可行 | 需要登入、可能被封 |

**3. 目前系統的問題**

| 問題 | 原因 | 解決方案 |
|------|------|----------|
| 排程不自動觸發 | wakeMode 設定 / Gateway 問題 | 待調查 |
| @sama 頁面 403 | xcancel 封鎖 | 嘗試其他來源 |
| 搜尋功能受限 | 無 Brave API key | 設定 Brave API |

**4. 進階方案探索**

| 方案 | 描述 | 成本 |
|------|------|------|
| Brave Search API | 搜尋新聞 | 免費額度/付費 |
| NewsAPI | 新聞聚合 API | $0-449/月 |
| RSS 訂閱 | 傳統但穩定 | 免費 |
| Feedly API | RSS 聚合 | $6-18/月 |

#### 💡 建議作法

**短期改進（本週）**
1. 設定 Brave Search API
2. 加入 RSS 來源（更穩定）
3. 修復 cron 自動觸發問題

**中期改進（本月）**
1. 建立新聞評分系統（重要性判斷）
2. 加入關鍵字追蹤
3. 設定每日摘要 Email

**長期目標**
1. 多語言新聞整合（中/英/日）
2. 情緒分析（市場情緒指標）
3. 與量化交易整合

**推薦的新聞來源組合**

```
主要來源（即時性高）
├── xcancel.com/@elonmusk
├── xcancel.com/@OpenAI
├── TechCrunch AI
└── The Verge AI

補充來源（深度分析）
├── Reuters Technology
├── CNBC Technology
└── Ars Technica

備用來源（RSS）
├── Hacker News
├── MIT Technology Review
└── Wired
```

---

### 2026-02-07 22:00 - 排程問題調查

**發現**：cron job 設定為 `wakeMode: now` 後仍未自動觸發

**嘗試**：重啟 Gateway

**結果**：待觀察明天 08:00 是否正常

---

### 2026-02-07 18:18 - 手動觸發測試

**結果**：成功發送 3 則新聞到 Discord

---

## 🛠️ 技術實作

### 排程設定
```
Job ID: hourly-news
Schedule: 0 8-22 * * * (Asia/Taipei)
wakeMode: now
Discord Channel: 1469479323106021487
```

### 新聞篩選標準
- 股市大波動（>2%）
- 央行政策變化
- 大廠重大發布
- AI 重大突破
- 重要人物聲明

---

## 📚 相關資源

- [Brave Search API](https://brave.com/search/api/)
- [NewsAPI](https://newsapi.org/)
- [xcancel.com](https://xcancel.com/)

---

*最後更新：2026-02-07 22:45*
