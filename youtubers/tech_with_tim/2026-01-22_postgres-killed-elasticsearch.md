# Postgres Just Killed Elasticsearch

- **頻道**：Tech With Tim
- **上傳日期**：2026-01-22
- **影片長度**：17:27
- **觀看次數**：42,762
- **連結**：https://www.youtube.com/watch?v=XEiQV4zRC-U

## 分類
資料庫 / 搜尋技術 / AI 時代工具

## 關鍵詞
PostgreSQL、Elasticsearch、BM25、TigerData、全文搜尋、MCP 伺服器

## 核心論點
PostgreSQL 透過新的 pg_textsearch 擴展和 BM25 排序演算法，提供了比 Elasticsearch 更簡單、更有效的搜尋解決方案，特別適合 AI 時代的需求。

## 重點整理

### 資料庫搜尋的痛點
- 傳統 SQL LIKE 查詢效能差
- 設置 Elasticsearch 複雜且昂貴
- 多個系統增加維護成本

### 搜尋技術的演變
- 從簡單字串匹配到全文搜尋
- 從關鍵字搜尋到語義搜尋
- AI 時代對搜尋品質要求更高

### 排序品質問題
- 傳統搜尋只找到匹配，不保證相關性
- 使用者期望最相關的結果排在最前面
- 這是 Elasticsearch 流行的主要原因

### BM25 演算法解決問題
- 專門設計用於計算文件相關性的演算法
- 考慮詞頻、文件長度、反向文件頻率
- 產生更準確的排序結果

### TigerData 解決方案
- 基於 PostgreSQL 的全管理資料庫服務
- 內建 pg_textsearch 擴展
- 支援真正的 BM25 排序

### 資料庫搜尋設置
- 只需要 PostgreSQL，不需要額外服務
- 簡單的 SQL 語法
- 與現有資料庫無縫整合

### MCP 伺服器連接
- 可與 AI 代理直接整合
- 讓 AI 能夠自然語言查詢資料庫
- 簡化開發流程

### 搜尋功能示範
- 模糊匹配和錯字容忍
- 多欄位搜尋
- 即時排序結果

## 金句
> 「不需要為了搜尋而維護兩個資料庫系統，PostgreSQL 現在可以做到一切。」

> 「AI 時代的搜尋不只是找到結果，而是找到最相關的結果。」
