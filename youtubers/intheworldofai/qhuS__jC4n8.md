# Claude Code With UNLIMITED Memory! Solves Claude's Memory Problem!

## 摘要

這個影片主要討論了 Anthropic 的 Claude 模型在跨 session 時缺乏持久記憶的問題。由於 Claude 的 session 設計是無狀態的，加上相較於 Gemini 等模型，其 context window 較小，導致每次 session 結束後，模型都會忘記之前的專案背景、決策和過去的工作成果。這使得使用者必須不斷重新解釋，浪費時間和 token，影響模型產生高品質輸出的能力。

影片介紹了一個名為 Claude Mem 的解決方案，它可以將 Claude Code 轉變為一個真正能跨 session 記住專案歷史的工具。Claude Mem 自動捕捉 Claude 在工具使用、決策和觀察方面的行為，將這些資訊壓縮並儲存到本地資料庫中，並在下一個 session 重新載入。這使得 Claude 始終具有上下文，節省了 token 和時間。

## 重點

- Claude 模型的主要限制之一是缺乏跨 session 的持久記憶。
- Claude 的 session 設計是無狀態的，並且 context window 相對較小。
- 每次 session 結束後，Claude 會忘記專案背景、決策和過去的工作成果，需要使用者不斷重新解釋。
- 不斷重新解釋會浪費時間和 token，並降低模型產生高品質輸出的能力。
- Claude Mem 是一個解決方案，可以將 Claude Code 轉變為一個能跨 session 記住專案歷史的工具。
- Claude Mem 自動捕捉 Claude 在工具使用、決策和觀察方面的行為，並儲存到本地資料庫中。
- 下一個 session 時，Claude Mem 會重新載入這些資訊，使 Claude 始終具有上下文。
- Claude Mem 有助於管理長期專案，記錄架構決策、編碼規範、過去的錯誤修復和成功的模式，同時減少 token 成本。
