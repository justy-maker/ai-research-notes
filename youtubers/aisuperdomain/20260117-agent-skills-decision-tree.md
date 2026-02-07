# Agent Skills 決策樹高級技巧：減少 80% 手動干預

> **影片連結**: https://www.youtube.com/watch?v=Qydk2wlh4YI
> **上傳日期**: 2026-01-17
> **時長**: 14 分鐘

## 分類
`Agent Skills` `工作流優化`

## 關鍵詞
`決策樹` `Agent Skills` `Antigravity` `Claude Code` `Codex CLI` `Gemini CLI` `代碼審查`

## 核心論點

決策樹是 Agent Skills 生態中的「靈魂技術」，通過在 SKILL.md 文件中嵌入結構化的 if-else 決策邏輯，讓 AI 編程助手具備真正的自主決策能力，減少 50%-80% 手動干預。

## 重點整理

### 決策樹概念
- **不是**機器學習算法
- **是**結構化的 if-else 決策邏輯
- 嵌入在 SKILL.md 文件中

### 解決的痛點
AI 編程助手頻繁詢問「下一步該怎麼做」的問題

### 實戰案例：code-review-router
- AI 根據代碼複雜度自動選擇審查工具
- 簡單代碼 → Gemini CLI
- 複雜代碼 → Codex CLI
- 主工具失敗自動切換備選方案

### 容錯機制
```
主工具執行 → 失敗 → 自動切換備選 CLI
```

### 效果
- 減少 50%-80% 手動干預
- 大幅節省 Token 消耗
- 支持斜杠命令快速調用

## 金句

> 「決策樹就是解決 AI 頻繁詢問『下一步該怎麼做』的終極方案！」

---
*摘要來源：AI 超元域頻道*
