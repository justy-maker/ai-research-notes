# OpenClaw 自動進化：讓 AI 越用越聰明的實戰技巧

- **頻道**：AI超元域
- **影片**：[OpenClaw 自動進化](https://www.youtube.com/watch?v=c5LKNO4YptM)
- **日期**：2026-02-13

## 重點摘要

### OpenClaw 不只是「Cloud Code + 聊天軟體」

OpenClaw（原 CloudBot → MoteBot → OpenClaw）是一個能自動進化的 AI 智能體：
- 持久記憶系統
- 定時任務功能
- 可控制智能家居（Home Assistant）
- **邊執行邊學習**
- 能記住踩過的坑並更新到 Skill 中

### 安全性實測

經過高強度測試，OpenClaw 能：
- 識別危險命令（如 `rm -rf /`）並拒絕執行
- 保護敏感配置文件（不會洩露 API Key）
- 發送配置時自動過濾敏感內容

**結論**：網上說 OpenClaw 刪除數據的說法很可能是為了流量編造的

### 實用功能展示

#### 1. 自動發 Exposed
使用自定義 Skill 實現

#### 2. 每日英文播客生成
- 設定定時任務（每天早上 7/8 點）
- 自動從 RSS 抓取文章
- 生成英文播客推送

#### 3. 操控 Claude Code 實現規格驅動開發
使用 Sparket / OpenSparket 工作流，完全由 OpenClaw 操控 Claude Code 完成開發

### 自動進化流程（核心！）

```
提出需求 → OpenClaw 執行 → 觀察測試 
     ↓                         ↓
   如果報錯 ←←←←←←←←←←←← 進行調試
     ↓
將經驗寫入 Skill → Push 到 GitHub
     ↓
重複測試 Skill → 再次觀察調試
     ↓
更新 Skill → 再次 Push
     ↓
循環迭代 → 得到完善高效的 Skill
```

### 實戰案例：開發私人日記應用

1. **發送需求**：開發 X 分格的私人日記應用
   - 簡單輸入框
   - 無限滾動時間線
   - 情緒標籤、圖片上傳
   - 日曆快速跳轉
   - 去年今日回顧

2. **OpenClaw 執行**：
   - 調用 Claude Code
   - 使用 OpenSparket 工作流
   - 遇到報錯自動調試
   - 修復後更新記憶和 Skill

3. **結果**：完全由 AI 完成的功能完整應用

### 關鍵配置建議

**推薦模型**：GPT 5.2（視頻作者使用）
- 原因：能完成更複雜任務
- 不用 Claude 的原因：怕被封號

### Skill 迭代的關鍵指令

讓 OpenClaw 記住：
```
每當調用這個 Skill 有新的使用技巧和經驗，
都同步更新到這個 Skill 中，
並且 Push 到 GitHub，
同時添加到記憶中。
```

## 個人筆記

這個「自動進化」的概念非常強大！核心思路是：
1. 讓 AI 在實戰中不斷踩坑
2. 踩完坑後把經驗寫入 Skill
3. Skill 隨著使用越來越完善
4. AI 讀取完善的 Skill 就越來越聰明

本質上是在做 **AI 的經驗傳承**——把 context 中學到的東西固化為 Skill，下次新 session 也能用。

**注意**：視頻用的是 GPT 5.2，但 Claude 模型應該也能做到類似效果，重點是 Skill 的設計和迭代流程。
