# Arrays & Hashing

> **核心技巧**：Hash Map/Set 快速查找、頻率統計、去重

---

## 題目列表

### [Contains Duplicate](../01_Arrays_and_Hashing/01_Contains_Duplicate.md) {: .easy }
**難度：Easy** | **標籤：Hash Set**

檢查陣列中是否存在重複元素。經典的 Hash Set 應用，時間複雜度 O(n)。

---

### [Valid Anagram](../01_Arrays_and_Hashing/02_Valid_Anagram.md) {: .easy }
**難度：Easy** | **標籤：Frequency Count**

判斷兩個字串是否為字母重組。學習字元頻率統計的基本技巧。

---

### [Two Sum](../01_Arrays_and_Hashing/03_Two_Sum.md) {: .easy-star }
**難度：Easy ⭐** | **標籤：Hash Map**

找出陣列中和為目標值的兩個數字。LeetCode 第一題，面試必考經典。

---

### [Group Anagrams](../01_Arrays_and_Hashing/04_Group_Anagrams.md) {: .medium }
**難度：Medium** | **標籤：Hash Map + Sorting**

將字母重組的字串分組。學習如何設計有效的 Hash Key。

---

### [Top K Frequent Elements](../01_Arrays_and_Hashing/05_Top_K_Frequent_Elements.md) {: .medium }
**難度：Medium** | **標籤：Bucket Sort / Heap**

找出陣列中出現頻率最高的 K 個元素。介紹 Bucket Sort 與 Heap 的取捨。

---

### [Product of Array Except Self](../01_Arrays_and_Hashing/06_Product_of_Array_Except_Self.md) {: .medium }
**難度：Medium** | **標籤：Prefix Product**

計算除自身外所有元素的乘積，不使用除法。巧妙的前綴積與後綴積技巧。

---

### [Valid Sudoku](../01_Arrays_and_Hashing/07_Valid_Sudoku.md) {: .medium }
**難度：Medium** | **標籤：Set**

檢查數獨是否有效。練習多維度的重複性檢查。

---

### [Encode and Decode Strings](../01_Arrays_and_Hashing/08_Encode_and_Decode_Strings.md) {: .medium }
**難度：Medium** | **標籤：String**

設計字串編碼與解碼方法。考驗邊界條件處理能力。

---

### [Longest Consecutive Sequence](../01_Arrays_and_Hashing/09_Longest_Consecutive_Sequence.md) {: .medium }
**難度：Medium** | **標籤：Union Find / Hash Set**

找出未排序陣列中最長的連續序列。O(n) 時間複雜度的經典解法。

---

## 學習建議

1. **先完成 Easy 題**：建立對 Hash 資料結構的直覺
2. **理解 Hash Collision**：了解為何 `unordered_map` 的最壞情況是 O(n)
3. **記憶體優化**：在嵌入式環境中，考慮 Sorting 等 O(1) Space 的替代方案

---

**上一主題：** 無 | **下一主題：** [Two Pointers](02-two-pointers.md)
