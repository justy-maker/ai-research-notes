# 10 Python one liners you'll actually use

- **影片連結**: https://www.youtube.com/watch?v=rmenKCClYUs
- **頻道**: Tech With Tim
- **日期**: 2026-02-27

## 重點整理
- **展平巢狀列表**：用雙層 list comprehension `[item for sublist in nested for item in sublist]`
- **一行交換變數**：`a, b = b, a`，也支援多變數和陣列元素交換，不需臨時變數
- **讀取檔案為行列表**：`open(file).read().splitlines()` 自動去除 `\n`
- **Counter 計數器**：`from collections import Counter` 一行統計頻率，支援 `most_common()` 方法
- **反轉字串/序列**：`s[::-1]` 利用 slice 的 step=-1，適用於任何可迭代物件
- **條件賦值（三元運算）**：`result = "even" if x % 2 == 0 else "odd"`
- **鏈式比較**：`1 < x < 10` 取代 `1 < x and x < 10`
- **join 建立分隔字串**：`", ".join(map(str, list))` 將列表轉為逗號分隔字串
- **pprint 美化輸出**：`from pprint import pprint` 格式化巢狀 JSON/字典
- **彩蛋**：`from __future__ import braces` 會拋出 "not a chance" 例外

## 關鍵觀點
- 這些都是實務中高頻使用的技巧，不是炫技——特別是 Counter、splitlines、join
- Python 的 slice 語法（start:stop:step）是理解許多進階用法的基礎

## 行動建議
- 把 `collections.Counter` 和 `pprint` 加入日常工具箱，減少手寫計數和格式化的時間
- 練習用 list comprehension 取代簡單的 for 迴圈，讓程式碼更簡潔
