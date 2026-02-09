# AI Agents 的最先進 Prompt 工程

## 影片資訊
- 原標題：State-Of-The-Art Prompting For AI Agents
- 連結：https://www.youtube.com/watch?v=DL82mGde6wo
- 頻道：Y Combinator

## 核心觀點
1. **Meta-prompting (元提示工程) 的重要性：** Meta-prompting 是一種強大的工具，可以讓 AI 模型根據先前的查詢動態生成更好的提示，從而提高效能。
2. **Prompt 的結構化設計：** 最佳的 Prompt 通常包含角色設定、任務描述、詳細計畫、推理步驟和範例，並且採用結構化的 Markdown 或 XML 格式，以便 LLM 更好地理解和執行。
3. **系統提示、開發者提示和使用者提示的分層架構：** 這種分層架構有助於區分通用邏輯、客戶特定邏輯和使用者輸入，從而避免變成客製化諮詢公司。
4. **提供 LLM「逃生出口」：** 讓 LLM 在資訊不足時能夠停止並請求更多資訊，而不是隨意生成答案，可以減少幻覺現象。
5. **利用大型模型進行 Meta-prompting，然後將結果應用於較小的模型：** 這種方法可以在保持低延遲的同時，獲得更好的效能，尤其是在語音 AI 代理中。

## 詳細內容摘要
這段影片深入探討了 AI 新創公司在 Prompt 工程方面使用的最先進技術，特別是 Meta-prompting。影片首先展示了一個來自 Parahelp 的實際 Prompt 範例，這是一家為 Perplexity、Replit 和 Bolt 等公司提供 AI 客戶支援的公司。這個 Prompt 非常詳細，長達六頁，首先設定 LLM 的角色為客戶服務代理的經理，然後逐步分解任務，並提供重要的注意事項和輸出格式。

影片強調，最佳的 Prompt 通常採用結構化的 Markdown 或 XML 格式，包含如何計畫、如何創建步驟以及計畫範例等部分。這種結構化的方法有助於 LLM 更好地理解和執行任務。此外，影片還提到了系統提示、開發者提示和使用者提示的分層架構，這種架構可以區分通用邏輯、客戶特定邏輯和使用者輸入，從而避免變成客製化諮詢公司。

Meta-prompting 是一種強大的工具，可以讓 AI 模型根據先前的查詢動態生成更好的提示。例如，一個分類器 Prompt 可以根據先前的查詢生成一個專門的 Prompt。影片還提到了 Prompt Folding 的概念，即一個 Prompt 可以動態生成更好的版本。

影片還強調了提供 LLM「逃生出口」的重要性。如果 LLM 沒有足夠的資訊來做出決定，應該讓它停止並請求更多資訊，而不是隨意生成答案。YC 內部使用的一種方法是在回應格式中包含一個「debug info」參數，讓 LLM 可以向開發者報告它遇到的問題。

最後，影片提到了利用大型模型進行 Meta-prompting，然後將結果應用於較小的模型。這種方法可以在保持低延遲的同時，獲得更好的效能，尤其是在語音 AI 代理中。影片還簡要提到了使用 Gemini Pro 的思考追蹤來偵錯 Prompt，以及 Eval 的重要性。

## 關鍵語錄
1. "Metarprompting is turning out to be a very very powerful tool that everyone's using now." (Meta-prompting 正在成為一種非常非常強大的工具，現在每個人都在使用它。)
2. "You actually have to give the LLM's a real escape hatch. You need to tell it if you do not have enough information to say yes or no or make a determination, don't just make it up. Stop and ask me." (你實際上必須給 LLM 一個真正的逃生出口。你需要告訴它，如果你沒有足夠的資訊來回答是或否，或者做出決定，不要隨意編造。停止並問我。)
3. "So you can actually go in take uh the existing prompt that you have and actually feed it more examples where maybe the prompt failed or didn't quite do what you wanted and you can actually instead of you having to go and rewrite the prompt, you just put it into um you know the raw LLM and say help me make this prompt better. And because it knows itself so well, strangely um metaprompting is turning out to be a very very powerful tool that everyone's using now." (所以你可以實際上拿走你現有的 prompt，並將更多範例餵給它，這些範例可能是 prompt 失敗或沒有完全達到你想要的效果，你可以實際上不必重寫 prompt，而是將它放入原始 LLM 中，並說「幫我讓這個 prompt 更好」。因為它非常了解自己，奇怪的是，meta-prompting 正在成為一種非常非常強大的工具，現在每個人都在使用它。)

## 我的評論
這段影片對於想要深入了解 AI Agent Prompt 工程的創業者和開發者來說非常有價值。它不僅提供了實際的 Prompt 範例，還介紹了 Meta-prompting、Prompt 結構化設計和分層架構等重要概念。

對於創業者來說，這段影片提醒我們，Prompt 工程不僅僅是寫一些文字，而是一門需要深入理解和不斷實驗的技術。透過 Meta-prompting 和結構化的 Prompt 設計，我們可以提高 AI Agent 的效能，並避免變成客製化諮詢公司。

對於開發者來說，這段影片提供了許多實用的技巧和工具，例如如何使用 Gemini Pro 的思考追蹤來偵錯 Prompt，以及如何利用大型模型進行 Meta-prompting，然後將結果應用於較小的模型。此外，影片還強調了提供 LLM「逃生出口」的重要性，這是一個非常重要的設計原則，可以減少幻覺現象。

總之，這段影片是一份關於 AI Agent Prompt 工程的寶貴資源，值得創業者和開發者仔細研究和應用。
