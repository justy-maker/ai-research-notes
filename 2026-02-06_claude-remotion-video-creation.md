# Claude Changed Content Creation - Remotion 影片製作教學

**影片連結:** https://youtu.be/pSnTKR2Phyo  
**創作者:** 不明（科技/AI 教學頻道）  
**時長:** 16:09  
**摘要日期:** 2026-02-06

---

## 📌 摘要

展示如何使用 Claude Desktop 的 Remotion 技能，僅透過 prompting 就能製作影片。從基礎設置到進階技能堆疊（加入語音、AI 生成圖片），最後教學如何串接多個影片片段製作完整 YouTube 影片。

---

## 🎯 核心概念

**Claude = 廚師比喻**
- Claude 像一位有才華的廚師，知道食譜和技巧
- 但若廚房是空的，就無法烹飪
- **Remotion 技能** = 給 Claude 完整的廚房設備
- 沒有技能 → Claude 只能描述影片
- 有技能 → Claude 可以實際製作影片

---

## 📚 三階段教學

### Level 1: 基礎設置與首支影片

**安裝步驟：**
1. 下載 Claude Desktop（Mac/Windows）
2. 開啟 Claude，選擇 "Co-work" 或 "Code" 模式
3. 安裝 Remotion 技能：
   ```
   npx skills add remotion dev skills
   ```
4. 設定工作資料夾存放影片

**製作首支影片：**
- 範例：為 bookedin.ai 網站製作產品 demo
- Prompt 示例：「用 Remotion 製作產品 demo，使用網站上的文案、白底黑字、藍色強調色」
- Claude 會自動瀏覽網站、抓取素材、生成影片

**編輯技巧：**
- 拖入自訂 logo 並告訴 Claude 使用該素材
- 所有編輯都透過對話完成
- 滿意後點擊 render 輸出影片

### Level 2: 技能堆疊（Skill Stacking）

**目標：**
- 維持一致的視覺風格
- 使用定義好的素材庫
- 加入音效、配音

**新增技能：**
- **11 Labs** - AI 語音配音
- **Nano Banana Pro** - AI 圖片生成
- 透過 **Wavespeed API** 整合

**claude.md / agent.md 設定：**
- 像一本筆記本，記錄 Claude 學到的技能
- 告訴 Claude：「當我要求製作影片，使用 Remotion」
- 記錄新服務和偏好設定
- Claude 會自動查閱並更新這份文件

**Wavespeed 設置：**
1. 取得 Wavespeed API key
2. 告訴 Claude 使用 11 Labs V3 做配音
3. 用 Nano Banana Pro 生成圖片
4. Claude 會將這些整合進 Remotion 影片

### Level 3: 影片串接（Video Chaining）

**流程：**
1. 撰寫腳本/大綱
2. 為每個章節分別製作獨立影片（intro、各段落、outro）
3. 放入完整錄影檔案
4. 告訴 Claude：「將這些影片串接在一起」

**實際操作：**
- Claude 成為「指揮」，自動串接所有片段
- 可將自己的錄影與生成影片混合
- 輸出完整的長影片

---

## 🔧 工具清單

| 工具 | 用途 |
|------|------|
| Claude Desktop | 主要 AI 介面 |
| Remotion | 影片製作技能 |
| 11 Labs | AI 語音生成 |
| Nano Banana Pro | AI 圖片生成 |
| Wavespeed | API 整合服務 |
| HeyGen | 影片生成（提及） |

---

## 🔑 關鍵詞

`Claude` `Remotion` `AI影片製作` `Skill Stacking` `11Labs` `自動化` `內容創作` `無程式碼` `Prompting`

---

## 💡 重點筆記

1. **Co-work vs Code 模式**
   - Co-work：較簡單但有限制（沙盒 VM）
   - Code：完整功能，推薦使用

2. **claude.md 的重要性**
   - 讓 Claude 記住你的偏好和技能
   - 隨時間累積，越用越聰明
   - 可以要求 Claude 自動更新

3. **迭代式工作流**
   - 生成 → 預覽 → 用對話修改 → 再生成
   - 所有調整都用自然語言完成

4. **自主化潛力**
   - 可以設置成自動生成行銷影片
   - 結合其他技能可全自動化內容產出

---

## 🎬 適用場景

- 產品 Demo 影片
- 動態圖形（Motion Graphics）
- YouTube 影片（含配音）
- 簡報影片
- 社群媒體內容
- 行銷素材

---

## 📝 下一步

觀看作者的進階影片，學習如何讓影片生成完全自動化運行。
