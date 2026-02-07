# 如何透過 AI 製作高品質簡報

> 研究進行中 🔬

## 📋 研究目標

探索如何利用 AI 高效產出專業簡報，並建立可重複使用的工作流程。

---

## ✅ 最終解決方案

### 確定的工作流程

```
用戶：「幫我做一個關於 XXX 的簡報」
         ↓
AI 生成完整內容：
  • outline.md - 大綱結構
  • slides.md - 每頁詳細內容
  • image_prompts.md - 圖片提示詞（給 Nano Banana）
  • colors.md - 配色建議
         ↓
用戶複製到 Gamma / Canva / PowerPoint
         ↓
用 Nano Banana 生成配圖
         ↓
結果存到 Git 或 Google Drive
```

### 工具推薦

| 場景 | 推薦工具 |
|------|----------|
| 快速產出 | Gamma.app |
| 商務專業 | Beautiful.ai |
| 團隊協作 | Pitch |
| 免費方案 | Google Slides + SlidesAI.io |

### 產出範例

- [AI 簡報工具研究報告](../presentations/2026-02-07_AI簡報工具研究/)

---

## 📝 研究筆記（新 → 舊）

### 2026-02-07 22:28 - 確定最終方案

<details>
<summary>對話紀錄</summary>
<small>

**軒哥**：簡報 Skill 完善，加更多主題、PPTX 轉換工具 >> 這個放到簡報的議題當中，作法已經改變成（Markdown + 圖片提示詞），要做紀錄

**阿福**：了解，記錄下來。最終方案從「生成 HTML 簡報」改為「生成 Markdown 內容 + 圖片提示詞」，讓用戶自己套用到專業工具。

</small>
</details>

**結論**：放棄自己生成 HTML 簡報，改用 Markdown + 圖片提示詞的方式，讓用戶自己套用到 Gamma/Canva/PowerPoint。

---

### 2026-02-07 11:15 - 嘗試 HTML 簡報但設計不理想

<details>
<summary>對話紀錄</summary>
<small>

**軒哥**：感覺設計風格還是不適合。我們回到這個工作流試試看...

**軒哥**：🎨 這種圖像不適合在專業的簡報中出現。第三第四頁的背景明顯不適合，太多文字，與前景衝突。

**阿福**：了解！讓我改用新的工作流程，生成 Markdown 內容 + 圖片提示詞，而不是直接生成 HTML。

</small>
</details>

**嘗試**：
- v1：純 HTML + CSS，太陽春
- v2：加入 Unsplash 背景圖，風格不專業
- v3：用 Gemini API 生成背景圖 + 主題切換，但設計仍不理想

**結論**：自己生成簡報的設計品質無法與專業工具比擬，改變策略。

---

### 2026-02-07 10:43 - 嘗試 Gemini 圖片生成

<details>
<summary>對話紀錄</summary>
<small>

**軒哥**：給你另一個 Gemini api key，嘗試看看加入更多主題，可以在第一頁的時候，讓我切換。

**阿福**：測試 Gemini 2.0 Flash Image Generation 成功！可以生成簡報背景圖。

</small>
</details>

**嘗試**：使用 `gemini-2.0-flash-exp-image-generation` 模型生成背景圖

**結果**：技術上可行，但生成的圖片風格不適合專業簡報

---

### 2026-02-07 10:31 - 開始研究 AI 簡報工具

<details>
<summary>對話紀錄</summary>
<small>

**軒哥**：研究一下 AI 製作簡報的工具有哪些

**阿福**：開始研究 9 款主流 AI 簡報工具：Beautiful.ai、Pitch、Gamma.app、Tome、Canva AI、Microsoft Copilot、Google Slides + Gemini、SlidesAI.io、Slidesgo

</small>
</details>

**產出**：完成 9 款工具的詳細比較分析

---

## 🔍 研究過的工具

| 工具 | 核心特色 | AI 強度 | 價格 | 評價 |
|------|----------|---------|------|------|
| Beautiful.ai | Smart Slides 自動排版 | ⭐⭐⭐⭐⭐ | $12-50/月 | 設計品質最高 |
| Pitch | 協作 + 分析追蹤 | ⭐⭐⭐⭐ | 免費-$80/月 | 團隊首選 |
| Gamma.app | 一鍵生成完整簡報 | ⭐⭐⭐⭐⭐ | 免費-$20/月 | 最快產出 |
| Tome | 敘事型視覺簡報 | ⭐⭐⭐⭐ | 免費-$20/月 | 視覺驚艷 |
| Canva AI | 設計模板豐富 | ⭐⭐⭐⭐ | 免費-$15/月 | 功能全面 |
| MS Copilot | Office 深度整合 | ⭐⭐⭐⭐ | $30/月 | 企業標準 |
| Google + Gemini | 免費 + 雲端協作 | ⭐⭐⭐ | 免費 | 入門首選 |
| SlidesAI.io | Google Slides 外掛 | ⭐⭐⭐⭐ | $10-20/月 | Slides 增強 |

---

## 📚 相關資源

- [Gemini + Nano Banana 影片](../2026-02-06_gemini_nanobanna_ppt.md)
- [GitHub PPT 開源工具](../2026-02-06_github_ppt_tool.md)

---

*最後更新：2026-02-07 22:41*
