# 如何蒐集即時的財經與科技快訊

> 研究進行中 🔬

## 📋 研究目標

建立自動化的新聞蒐集與篩選系統，即時掌握財經科技動態。

## 🔍 重點關注

### 人物
- 川普 (Trump)
- 馬斯克 (Elon Musk)
- 黃仁勳 (Jensen Huang)
- 奧特曼 (Sam Altman)

### 公司
- Google / Gemini
- OpenAI / ChatGPT
- Anthropic / Claude
- TSMC / 台積電
- Tesla / xAI
- Nvidia

## 🛠️ 目前實作

### 新聞來源
| 來源 | 網址 | 狀態 |
|------|------|------|
| Reuters | reuters.com/technology/ | 🟡 偶爾被擋 |
| TechCrunch | techcrunch.com/category/artificial-intelligence/ | ✅ |
| The Verge | theverge.com/ai-artificial-intelligence | ✅ |
| CNBC | cnbc.com/technology/ | ✅ |

### 社群監控
| 帳號 | 來源 | 狀態 |
|------|------|------|
| @elonmusk | xcancel.com | ✅ |
| @sama | xcancel.com | 🔴 403 錯誤 |
| @OpenAI | xcancel.com | ✅ |
| @AnthropicAI | xcancel.com | ✅ |
| @nvidia | xcancel.com | ✅ |

### 排程設定
- **hourly-news**: 每天 08:00-22:00 整點
- 輸出到 Discord #重要新聞 頻道
- 判斷標準：股市波動 >2%、大廠發布、AI 重大突破

## 📝 研究筆記

### 2026-02-07
- 排程設定完成，但自動觸發有問題（需調查）
- 手動觸發可正常運作
- xcancel.com 是目前最穩定的 Twitter 抓取來源
- 美國原生網站速度比台灣翻譯版快

### 待改進
- [ ] 設定 Brave Search API（更全面的搜尋）
- [ ] 解決排程自動觸發問題
- [ ] 增加更多新聞來源

## 🎯 結論與建議

（持續更新中）

---

*最後更新：2026-02-07*
