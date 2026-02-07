# Build a fullstack app in 7 minutes with v0

## 影片基本資訊
- **影片 ID**: cyFVtaLy-bA
- **頻道**: Vercel（官方）
- **觀看次數**: 233K
- **連結**: https://www.youtube.com/watch?v=cyFVtaLy-bA

## 學習目標
- 了解 v0 的核心功能與工作流程
- 學會從 Figma 設計匯入 v0 生成 React 程式碼
- 掌握快速編輯（Fast Edit）模式的使用
- 學會一鍵部署應用到 Vercel
- 了解如何整合 Supabase 資料庫

## 操作步驟

### 步驟 1：從 Figma 匯入設計
1. 在 Figma 中準備好設計稿（影片示範為電商付款表單）
2. 複製 Figma 設計的連結
3. 進入 v0，貼上 Figma 連結作為起點
4. v0 會自動擷取 Figma 的圖像和資訊

### 步驟 2：自動生成 React 程式碼
- v0 會在背景自動生成 React 程式碼
- 生成的是完整的全端應用程式
- 可以在瀏覽器中即時預覽
- 可以直接查看和編輯程式碼
- 支援 console logs 和錯誤檢視

### 步驟 3：使用快速編輯模式（Fast Edit）
1. 選取想要修改的元件
2. 輸入修改指令（如：「預設選中的按鈕不要黑色背景」）
3. v0 只會修改相關的小部分檔案，加快編輯速度
4. 可以用箭頭按鈕回復到之前的版本

### 步驟 4：樣式調整
- 可以使用 Google Fonts（如 monospace 字體）
- 使用 shadcn/ui 元件
- 低成本實驗：不喜歡可以隨時回復

### 步驟 5：一鍵部署到 Vercel
1. 點擊右上角的部署按鈕
2. 建立新專案（命名如 "payments"）
3. 等待建置完成
4. 獲得即時 URL，可分享和迭代

### 步驟 6：整合 Supabase 資料庫
1. 輸入指令「integrate and connect with Supabase」
2. v0 會詢問是否設定環境變數
3. 前往 Vercel Marketplace 取得 Supabase 連線資訊
4. 複製 Public URL 和 Anon Key
5. 貼入 v0 的環境變數設定
6. 環境變數會安全儲存在 Vercel 專案中

### 步驟 7：多檔案應用開發
- v0 可以建立多個檔案：Server Actions、資料庫連線、更新後的表單
- 可以詢問後續問題（如資料庫 schema 調整、SQL 語法、資料庫遷移）

## 重點功能

### v0 核心功能
1. **Figma 匯入** - 直接從 Figma 設計生成程式碼
2. **螢幕截圖轉換** - 貼上截圖生成 UI
3. **即時預覽** - 在瀏覽器中預覽應用
4. **快速編輯** - 針對特定元件的快速修改
5. **版本控制** - 可回復到任何之前的版本
6. **一鍵部署** - 直接部署到 Vercel
7. **Marketplace 整合** - 連接各種第三方服務
8. **全端開發** - 不只是 UI，還包含後端邏輯

### 程式碼品質
- 使用 React 元件
- 建立在可存取的原語（accessible primitives）上
- 精美樣式，可自訂主題
- 可直接加入現有程式碼庫

### 環境變數管理
- 不儲存在程式碼中
- 安全儲存在 Vercel 專案
- 支援不同環境設定
- 適當的權限控管

## 學習筆記

### 💡 最佳實踐
1. **先用 Figma 設計** - 有明確的視覺設計再開始
2. **小步迭代** - 每次修改一點，確認效果
3. **善用版本回復** - 不怕實驗，隨時可以回去
4. **環境變數分離** - 敏感資訊不要放在程式碼裡

### ⚡ 效率技巧
- 使用 Fast Edit 模式加速局部修改
- 直接複製程式碼到本地編輯器
- 利用 Vercel Marketplace 快速整合服務

### 🔗 相關資源
- [v0.dev](https://v0.dev)
- [shadcn/ui](https://ui.shadcn.com)
- [Vercel Marketplace](https://vercel.com/marketplace)
- [Supabase](https://supabase.com)
