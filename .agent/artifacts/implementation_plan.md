# 實作計畫 - Arrays & Hashing 視覺化批量添加

## 目標

為 `01_Arrays_and_Hashing` 目錄下的 9 道題目添加互動式演算法視覺化。

## 題目清單與視覺化設計

| #   | 題目                  | 視覺化類型         | 關鍵狀態                |
| --- | --------------------- | ------------------ | ----------------------- |
| 1   | Contains Duplicate    | Array + HashSet    | 遍歷元素、Set 狀態      |
| 2   | Valid Anagram         | Two HashMaps       | 字元計數對比            |
| 3   | Two Sum               | Array + HashMap    | 目標值、Complement 查詢 |
| 4   | Group Anagrams        | HashMap Grouping   | 排序 Key、分組結果      |
| 5   | Top K Frequent        | Bucket Sort        | 頻率桶、結果提取        |
| 6   | Product of Array      | Prefix/Suffix      | 左右累積陣列            |
| 7   | Valid Sudoku          | 9x9 Grid + Sets    | 行/列/Box 衝突檢測      |
| 8   | Encode/Decode Strings | String Parsing     | 編碼/解碼過程           |
| 9   | Longest Consecutive   | HashSet + Sequence | 序列起點、延伸過程      |

## 執行順序

1. 先處理較簡單的題目 (1-3)
2. 再處理中等複雜度 (4-6)
3. 最後處理複雜題目 (7-9)

## 預計檔案結構

```
docs/01_Arrays_and_Hashing/
├── 01_Contains_Duplicate.md
├── contains_duplicate_visualizer.html  [NEW]
├── 02_Valid_Anagram.md
├── valid_anagram_visualizer.html       [NEW]
...
```
