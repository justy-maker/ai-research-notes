# How To Use v0 by Vercel | Tutorial For Beginners

## 影片基本資訊
- **影片 ID**: hlLRN8D_xPc
- **頻道**: (Creator Channel)
- **觀看次數**: 10K
- **連結**: https://www.youtube.com/watch?v=hlLRN8D_xPc

## 學習目標
- 了解 v0 平台的完整工作流程
- 學會從 v0 生成前端程式碼
- 掌握如何將程式碼匯入 Cursor AI
- 學會在 localhost 環境部署和即時預覽

## 操作步驟

### 步驟 1：註冊並進入 v0
1. 前往 v0 網站建立帳號
2. 登入 Dashboard，可看到過去的對話記錄
3. 開始新的對話

### 步驟 2：輸入 Prompt 生成 UI
- 範例 Prompt：「Generate a multi-step wizard to collect information on users when onboarding a SaaS product」
- 按 Enter 送出
- 畫面左側是 AI 對話，右側是程式碼和預覽

### 步驟 3：理解平台特性
**v0 的優勢**：
- 類似 Replit 的沙盒式 UI 開發
- 即時看到程式碼生成過程
- 適合製作 MVP 和原型

**注意事項**：
- 預覽需要網路連線（連接 v0 伺服器）
- 非本地環境（localhost）
- 本地環境可離線開發測試

### 步驟 4：管理對話功能
1. **追問功能** - 繼續修改或增加功能
2. **收藏功能** - 儲存有用的對話
3. **重新命名** - 給對話取名方便管理
4. **查看程式碼** - 點擊右側 Code 按鈕

### 步驟 5：匯出選項
- **Fork** - 複製專案
- **Share** - 分享公開連結
- **Add to Codebase** - 匯入 Cursor AI（最重要）

### 步驟 6：理解 UI vs Backend
- 目前只是前端 UI
- 沒有連接後端
- 表單資料不會儲存
- 純粹是使用者互動體驗

### 步驟 7：匯入 Cursor AI
1. 點擊 Download，複製生成的程式碼
2. 開啟 Cursor AI
3. 點擊左下角 Terminal

### 步驟 8：建立專案
```bash
# 建立新資料夾
mkdir v0-good

# 進入資料夾
cd v0-good
```
然後選擇 Open a Project，選擇剛建立的資料夾

### 步驟 9：匯入程式碼
1. 開啟終端機，貼上複製的程式碼
2. 按 Enter
3. 出現安裝提示時輸入 `Y`
4. 設定 App 名稱（如：my-new-v0）
5. 選擇主題樣式（如：New York）
6. 確認是否使用 CSS 變數做主題 → Yes

### 步驟 10：驗證匯入成功
- 展開資料夾結構
- 路徑：app > components > UI
- 可看到 name, email, company, role, industry 等欄位

### 步驟 11：部署到 localhost
```bash
# 進入專案資料夾
cd my-new-v0

# 啟動開發伺服器
npm run dev
```

### 步驟 12：開啟預覽
- 等待 Ready 訊息
- 點擊 localhost:3000 連結
- 成功部署！

### 步驟 13：即時編輯
- 修改程式碼中的文字（如：Name → Full Name）
- 儲存後自動反映變化
- 不需要刷新頁面

## 重點功能

### v0 平台特色
| 功能 | 說明 |
|------|------|
| 對話式 UI | 用自然語言描述需求 |
| 即時預覽 | 邊生成邊看效果 |
| 程式碼可視化 | 看到程式碼生成過程 |
| 收藏管理 | 保存有用的對話 |
| 匯出功能 | 一鍵匯入 Cursor AI |

### 適用場景
- 沙盒測試
- UI 原型設計
- MVP 快速開發
- 學習前端元件

### 技術架構
- 前端：React / Next.js
- 樣式：CSS Variables
- 開發環境：Node.js
- 部署：localhost:3000

## 學習筆記

### 💡 核心概念
1. **v0 = 前端生成器** - 只處理 UI，不含後端
2. **Localhost** - 本地開發環境，可離線使用
3. **Hot Reload** - 修改程式碼即時反映

### ⚡ 常用指令
```bash
mkdir folder-name   # 建立資料夾
cd folder-name      # 進入資料夾
npm run dev         # 啟動開發伺服器
```

### 🔧 工作流程
```
v0 生成 UI → 下載程式碼 → Cursor AI 開啟 → 
Terminal 設定 → npm run dev → localhost 預覽
```

### 📌 注意事項
- v0 預覽需要網路
- localhost 可離線
- 修改後自動反映，無需刷新
- 前端 UI 不含資料儲存功能
