# Master Python Requests In 15 Minutes - Call Any API

- **頻道**：Tech With Tim
- **上傳日期**：2025-12-22
- **影片長度**：16:52
- **觀看次數**：28,343
- **連結**：https://www.youtube.com/watch?v=Xnbef8F_Yfc

## 分類
Python 教學 / API 開發 / 技術教程

## 關鍵詞
Python Requests、API 呼叫、HTTP 請求、REST API、錯誤處理

## 核心論點
15 分鐘內掌握 Python requests 函式庫的所有核心功能，學會呼叫任何 API。

## 重點整理

### Requests 理論基礎
**HTTP 方法：**
- GET：獲取資料
- POST：建立資料
- PUT/PATCH：更新資料
- DELETE：刪除資料

**核心概念：**
- URL 結構
- Headers（標頭）
- Body（請求主體）
- Status Codes（狀態碼）

### 設置與安裝
```bash
pip install requests
```
- 使用 uv 或 pip 安裝
- 匯入方式：`import requests`

### 基本請求示範
```python
response = requests.get("https://api.example.com/data")
print(response.json())
```
- GET 請求基礎
- 處理回應資料

### Query Parameters（查詢參數）
```python
params = {"key": "value"}
response = requests.get(url, params=params)
```
- 傳遞 URL 參數
- 篩選和分頁

### Body（POST 請求）
```python
data = {"name": "Tim"}
response = requests.post(url, json=data)
```
- 發送 JSON 資料
- 建立新資源

### 錯誤處理
```python
response.raise_for_status()
```
- 檢查狀態碼
- 處理各種錯誤情況
- try/except 模式

### Authorization（授權）
```python
headers = {"Authorization": "Bearer token"}
response = requests.get(url, headers=headers)
```
- API Key 認證
- Bearer Token
- Basic Auth

## 金句
> 「會呼叫 API 是現代開發者的基本功，requests 讓這件事變得超級簡單。」
