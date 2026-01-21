---
title: "Rotate Image (旋轉圖像)"
description: "給定一個 `n x n` 的二維矩陣 `matrix`，代表一個圖像。 請將圖像 **順時針旋轉 90 度**。 你必須 **原地 (in-place)** 修改矩陣，不能使用另一個 2D 矩陣來旋轉。"
tags:
  - 
Math  - Matrix
difficulty: Medium
---

# Rotate Image (旋轉圖像) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #48** — [題目連結](https://leetcode.com/problems/rotate-image/) | [NeetCode 解說](https://neetcode.io/problems/rotate-image)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `n x n` 的二維矩陣 `matrix`，代表一個圖像。
請將圖像 **順時針旋轉 90 度**。
你必須 **原地 (in-place)** 修改矩陣，不能使用另一個 2D 矩陣來旋轉。

-   **Input**:
    ```
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    ```

-   **Output**:
    ```
    [
      [7,4,1],
      [8,5,2],
      [9,6,3]
    ]
    ```

-   **Constraints**:
    -   $1 <= n <= 20$.
    -   Matrix values range $[-1000, 1000]$.

---

## 2. 🐢 Brute Force Approach (暴力解)

如果可以使用額外空間，我們可以創建一個新矩陣 `new_matrix`。
`new_matrix[j][n - 1 - i] = matrix[i][j]`。

-   **Time**: $O(N^2)$.
-   **Space**: $O(N^2)$. (題目要求 $O(1)$)

---

## 3. 💡 The "Aha!" Moment (優化)

要在原地旋轉，可以通過兩個簡單的矩陣操作組合來實現：

1.  **Transpose (轉置)**: 沿著主對角線翻轉。行變列，列變行。
    -   `swap(matrix[i][j], matrix[j][i])` for `i < j`.
2.  **Reflect (水平鏡像翻轉)**: 每一行左右翻轉。
    -   `reverse(matrix[i])`.

**Example**:
Original:
```
1 2 3
4 5 6
7 8 9
```
Transpose (swap(0,1) with (1,0), etc...):
```
1 4 7
2 5 8
3 6 9
```
Reflect (Reverse each row):
```
7 4 1
8 5 2
9 6 3
```
Result is 90 degrees clockwise!

(如果想逆時針 90 度，則是先 Reflect 再 Transpose，或者先 Transpose 再垂直翻轉)。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../rotate_image_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../rotate_image_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Transpose + Reverse

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // 1. Transpose: Swap matrix[i][j] with matrix[j][i]
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // 2. Reverse each row
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

### Python Reference

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse rows
        for i in range(n):
            matrix[i].reverse()
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();

        // 步驟 1: 轉置矩陣 (Transpose)
        // 將 (i, j) 與 (j, i) 交換
        // 只需遍歷主對角線上方 (j > i) 的元素
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                // 使用 swap 函數進行原地交換
                swap(matrix[i][j], matrix[j][i]);
            }
        }

        // 步驟 2: 每一行進行左右翻轉 (Reverse)
        // 轉置後的矩陣，每一行逆序後，就變成了順時針旋轉 90 度的結果
        for (int i = 0; i < n; i++) {
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^2)$
    -   Transpose involves iterating about $N^2/2$ elements.
    -   Reverse involves iterating $N^2$ elements.
-   **Space Complexity**: $O(1)$
    -   In-place modifications.

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 你會如何處理更大的輸入？
- 有沒有更好的空間複雜度？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 沒有考慮邊界條件
- ⚠️ 未討論複雜度

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 主動討論 trade-offs
- 💎 提供多種解法比較

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Spiral Matrix (螺旋矩陣)](02_Spiral_Matrix.md)
