# v0.dev 教學影片摘要

> v0.dev 是 Vercel 推出的 AI 驅動的 UI 生成工具，可以用自然語言描述需求，自動生成 React/Next.js 程式碼。

## 📚 影片列表

| # | 影片標題 | 觀看數 | 重點內容 |
|---|---------|--------|----------|
| 1 | [Build a fullstack app in 7 minutes with v0](01-build-fullstack-app-7min.md) | 233K | Vercel 官方教學，Figma 匯入、Supabase 整合 |
| 2 | [How To Use v0 by Vercel For Beginners](02-how-to-use-v0-beginners.md) | 152K | 完整入門教學，Cursor AI 整合 |
| 3 | [How To Use v0 by Vercel - Tutorial](03-how-to-use-v0-tutorial.md) | 10K | 基礎操作流程詳解 |
| 4 | [How to make beautiful UIs with AI](04-beautiful-uis-with-ai.md) | 50K | shadcn/ui 深入講解 |
| 5 | [Convert Figma Designs into CODE](05-figma-to-code-v0.md) | 39K | Figma 轉程式碼評測 |
| 6 | [How I Built an App in 14 minutes](06-build-app-14min.md) | 197K | 快速開發實戰 |

## 🎯 學習路徑建議

### 初學者
1. 先看 #1（官方教學）了解 v0 核心功能
2. 再看 #2 學習完整工作流程
3. 實際操作並嘗試建立簡單 UI

### 進階學習
1. 看 #4 了解 shadcn/ui（v0 背後的魔法）
2. 看 #5 評估 Figma 整合的實用性
3. 看 #6 學習高效開發技巧

## 💡 核心概念

### v0 是什麼？
- Vercel 推出的 AI UI 生成工具
- 用自然語言描述需求 → 自動生成 React 程式碼
- 基於 shadcn/ui 設計系統
- 可一鍵部署到 Vercel

### v0 的工作流程
```
描述需求 → AI 生成 UI → 即時預覽 → 迭代修改 → 部署上線
```

### v0 vs 傳統開發
| 方面 | v0 | 傳統開發 |
|------|-----|----------|
| 速度 | 分鐘級 | 小時/天級 |
| 學習曲線 | 低 | 高 |
| 靈活性 | 中 | 高 |
| 客製化 | 需手動調整 | 完全自由 |

## ⚡ 快速上手

### 基本操作
1. 前往 [v0.dev](https://v0.dev)
2. 登入/註冊帳號
3. 輸入 Prompt 描述你想要的 UI
4. 檢視生成結果並迭代
5. 一鍵部署或匯出程式碼

### Prompt 技巧
- 描述 **具體功能**（如：登入表單、產品卡片）
- 指定 **樣式偏好**（如：極簡風、深色模式）
- 提供 **參考範例**（如：像 Airbnb 的風格）
- 說明 **互動行為**（如：點擊後顯示詳情）

## 🔧 常用工具整合

### Cursor AI
- 從 v0 匯出程式碼
- 在 Cursor 中進一步開發
- 本地 localhost 環境測試

### Figma
- 從 Figma 設計匯入
- 注意：目前精確度有限
- 適合作為起點，需手動調整

### Supabase
- 連接資料庫
- 設定環境變數
- 建立全端應用

## ⚠️ 注意事項

### v0 的限制
- 主要生成**前端 UI**，後端需另外處理
- Figma 匯入**不夠精確**，無法完美複製設計
- 複雜邏輯需要**手動調整**
- 客戶專案可能需要更多客製化

### 適用場景
✅ 快速原型、MVP、個人專案、學習
❌ 需要精確還原設計的專案、複雜商業邏輯

## 📖 延伸學習

- [shadcn/ui](https://ui.shadcn.com) - v0 使用的設計系統
- [Tailwind CSS](https://tailwindcss.com) - 樣式框架
- [Next.js](https://nextjs.org) - React 框架
- [Vercel](https://vercel.com) - 部署平台

---

*整理日期：2026-02-08*
