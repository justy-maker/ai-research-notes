# 🚀 OpenClaw 進階玩法：自研 LanceDB 記憶插件讓小龍蝦記憶力暴增

- **頻道**: AI 超元域
- **日期**: 2026-02-24
- **連結**: https://www.youtube.com/watch?v=MtukF1C8epQ
- **轉錄方式**: whisper

## 摘要

作者開源了自研的 LanceDB 記憶插件，大幅增強 OpenClaw 的長期記憶能力。

### 為什麼需要額外記憶系統？
- OpenClaw 內建記憶（markdown + sqlite）有局限性
- 內建 LanceDB 嵌入模型只支援 OpenAI，功能基礎
- 新 session 時常「忘記」之前的操作和經驗

### LanceDB 插件 vs 內建記憶

| 功能 | 內建 | LanceDB 插件 |
|------|------|-------------|
| 嵌入模型 | 僅 OpenAI | OpenAI / Jina AI / Gemini / Ollama |
| 搜索方式 | 向量搜索 | BM25 全文 + 向量 + 混合檢索 |
| 評分管線 | 1 層 | 6 層 |
| 去重 | 無 | MMR 多樣性去重 |
| 噪聲處理 | 無 | 自適應檢索跳過噪聲 |
| 記憶隔離 | 無 | 多 scope 隔離（每個 agent 獨立記憶 + 共享知識）|

### 核心功能
- **熱拔插**：修改一行配置即可啟用，不與內建記憶衝突
- **獨立版本升級**：不受 OpenClaw 版本更新影響
- **7 層混合檢索**：向量 + 關鍵詞 + rerank
- **多 scope 隔離**：agent 間隱私保護
- **噪聲攔截 + 保留式延縮 + ID 潛水匹配**

### 安裝方式
1. 註冊 Jina AI 取得 API Key
2. 在 OpenClaw 中輸入 API Key + GitHub 倉庫連結
3. OpenClaw 自動完成安裝配置
4. 設置「鐵律」讓 OpenClaw 自動將踩坑經驗寫入 LanceDB

### 使用效果
- 新 session 上下文只需 18K（不用加載大量歷史）
- 能精準檢索之前的踩坑經驗、方法論、技術細節
- 真正實現「越用越聰明」

## 關鍵字
OpenClaw, LanceDB, 記憶系統, 向量資料庫, 混合檢索, RAG, Jina AI, 插件開發, 長期記憶
