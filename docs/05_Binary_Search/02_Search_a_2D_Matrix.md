---
title: "Search a 2D Matrix (搜尋二維矩陣)"
description: "題目給一個 `m x n` 的矩陣 `matrix` 和一個整數 `target`。 這個矩陣有兩個特性："
tags:
  - Binary Search
  - Array
difficulty: Medium
---

# Search a 2D Matrix (搜尋二維矩陣) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #74** — [題目連結](https://leetcode.com/problems/search-a-2d-matrix/) | [NeetCode 解說](https://neetcode.io/problems/search-a-2d-matrix)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 `m x n` 的矩陣 `matrix` 和一個整數 `target`。
這個矩陣有兩個特性：

1.  每列 (Row) 的元素從左到右遞增排序。
2.  每列的第一個整數大於前一列的最後一個整數。

這意味著，如果你把這個矩陣「拉直」成一個一維陣列，它也是嚴格遞增排序的。
請判斷 `target` 是否存在於矩陣中。

-   **Input**: `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3`
-   **Output**: `true`
-   **Constraints**:
    -   $m, n <= 100$.
    -   時間複雜度要是 $O(\log(m \cdot n))$。

---

## 2. 🐢 Brute Force Approach (暴力解)

遍歷矩陣中每個元素。

-   **Time**: $O(m \cdot n)$。
-   **Result**: 雖然 Constraints 很小 ($100 \times 100 = 10000$)，暴力解能過，但面試這會被扣分。

---

## 3. 💡 The "Aha!" Moment (優化)

既然矩陣「拉直」後是有序的，我們可以直接把它當作一個大的一維陣列來跑 **Binary Search**。
假設矩陣有 `m` 列 `n` 行，總長度 `L = m * n`。
一維的 index `i` (從 0 到 `L-1`) 可以映射回二維座標 `(r, c)`：

-   `row = i / n`
-   `col = i % n`

**演算法**：

1.  `low = 0`, `high = m * n - 1`。
2.  做標準 Binary Search。
3.  每次取出 `mid`，計算座標 `(mid / n, mid % n)` 來取值。

**Alternative Approach (Two Binary Searches)**:

1.  先對「第一欄」做 BS，找出 target 可能在哪個 Row。
2.  再對那個 Row 做 BS。
這樣邏輯比較複雜一點，但也是 $O(\log m + \log n) = O(\log(mn))$。
「把它視為一維陣列」的方法代碼最簡潔。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../search_2d_matrix_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../search_2d_matrix_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Virtual 1D Array Binary Search

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;

        int m = matrix.size();
        int n = matrix[0].size();

        int low = 0;
        int high = m * n - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            // Map 1D mid to 2D coordinates
            int r = mid / n;
            int c = mid % n;
            int val = matrix[r][c];

            if (val == target) {
                return true;
            } else if (val < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return false;
    }
};
```

### Python Reference

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            m = l + (r - l) // 2
            # Map to 2D
            row = m // COLS
            col = m % COLS

            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1

        return False
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();

        // 將2D矩陣視為長度 m*n 的1D陣列
        // index 範圍從 0 到 m*n - 1
        long long left = 0;
        long long right = (long long)m * n - 1;

        while (left <= right) {
            long long mid = left + (right - left) / 2;

            // 關鍵映射：
            // 行數(row) = index / 寬度(n)
            // 列數(col) = index % 寬度(n)
            int val = matrix[mid / n][mid % n];

            if (val == target) {
                return true;
            } else if (val < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return false;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log(m \cdot n))$
    -   搜尋範圍是 `m*n` 個元素，每次砍一半。
-   **Space Complexity**: $O(1)$
    -   沒有配置額外陣列。我們只做了簡單的座標轉換計算。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- Search a 2D Matrix II?
- 複雜度差異？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 2D 到 1D 轉換公式錯誤
- ⚠️ 邊界處理錯誤

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 清晰的座標轉換
- 💎 討論兩種 2D 矩陣的差異

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Binary Search (二分搜尋)](01_Binary_Search.md)

### 進階挑戰
- [Search A 2D Matrix Ii](https://leetcode.com/problems/search-a-2d-matrix-ii/) — LeetCode
