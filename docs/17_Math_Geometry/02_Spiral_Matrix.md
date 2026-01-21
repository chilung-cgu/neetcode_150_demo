---
title: "Spiral Matrix (螺旋矩陣)"
description: "給定一個 `m x n` 的矩陣 `matrix`。 請按照 **順時針螺旋順序** (Spiral Order)，回傳矩陣中的所有元素。"
tags:
  - Math
  - Matrix
difficulty: Medium
---

# Spiral Matrix (螺旋矩陣) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #54** — [題目連結](https://leetcode.com/problems/spiral-matrix/) | [NeetCode 解說](https://neetcode.io/problems/spiral-matrix)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的矩陣 `matrix`。
請按照 **順時針螺旋順序** (Spiral Order)，回傳矩陣中的所有元素。

-   **Input**:
    ```
    [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
    ]
    ```

-   **Output**: `[1,2,3,6,9,8,7,4,5]`
-   **Input**:
    ```
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    ```

-   **Output**: `[1,2,3,4,8,12,11,10,9,5,6,7]`
-   **Constraints**:
    -   $m, n$ up to 10.
    -   Total elements up to 100.

---

## 2. 🐢 Brute Force Approach (暴力解)

這沒有特別的暴力解，主要是模擬。
這是一個模擬題，重點在於邊界控制。

---

## 3. 💡 The "Aha!" Moment (優化)

**Simulation with Boundaries (Layer-by-Layer)**:
維護四個邊界：

-   `top`
-   `bottom`
-   `left`
-   `right`

順序：

1.  **Left to Right**: `matrix[top][left...right]`, then `top++`.
2.  **Top to Bottom**: `matrix[top...bottom][right]`, then `right--`.
3.  **Right to Left**: `matrix[bottom][right...left]`, then `bottom--`.
    -   **Check**: 必須確保 `top <= bottom`，否則會重複遍歷。
4.  **Bottom to Top**: `matrix[bottom...top][left]`, then `left++`.
    -   **Check**: 必須確保 `left <= right`。

**Loop Condition**: `while (top <= bottom && left <= right)`。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../spiral_matrix_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../spiral_matrix_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Simulation

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};

        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> result;

        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;

        while (top <= bottom && left <= right) {
            // 1. Left to Right
            for (int j = left; j <= right; j++) {
                result.push_back(matrix[top][j]);
            }
            top++; // Shrink top boundary

            // 2. Top to Bottom
            for (int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--; // Shrink right boundary

            // Check if done after shrinking
            if (top > bottom || left > right) break;

            // 3. Right to Left
            for (int j = right; j >= left; j--) {
                result.push_back(matrix[bottom][j]);
            }
            bottom--; // Shrink bottom boundary

            // 4. Bottom to Top
            for (int i = bottom; i >= top; i--) {
                result.push_back(matrix[i][left]);
            }
            left++; // Shrink left boundary
        }

        return result;
    }
};
```

### Python Reference

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty()) return {};

        int m = matrix.size();
        int n = matrix[0].size();
        vector<int> result;

        // 定義四個邊界
        int top = 0;
        int bottom = m - 1;
        int left = 0;
        int right = n - 1;

        // 當邊界還沒有交錯時，繼續遍歷
        while (top <= bottom && left <= right) {
            // 1. 從左到右 (遍歷上邊界)
            for (int j = left; j <= right; j++) {
                result.push_back(matrix[top][j]);
            }
            top++; // 上邊界向下收縮

            // 2. 從上到下 (遍歷右邊界)
            for (int i = top; i <= bottom; i++) {
                result.push_back(matrix[i][right]);
            }
            right--; // 右邊界向左收縮

            // 關鍵檢查：
            // 在上縮和右縮之後，可能會導致 top > bottom 或 left > right
            // 例如單行矩陣，遍歷完第一步 top++ 後就結束了
            // 如果不檢查，後面的步驟會重複遍歷或越界
            if (top > bottom || left > right) break;

            // 3. 從右到左 (遍歷下邊界)
            for (int j = right; j >= left; j--) {
                result.push_back(matrix[bottom][j]);
            }
            bottom--; // 下邊界向上收縮

            // 4. 從下到上 (遍歷左邊界)
            for (int i = bottom; i >= top; i--) {
                result.push_back(matrix[i][left]);
            }
            left++; // 左邊界向右收縮
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   Each element is visited exactly once.
-   **Space Complexity**: $O(1)$
    -   If not counting the output array.

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
- [Rotate Image (旋轉圖像)](01_Rotate_Image.md)

### 進階挑戰
- [Spiral Matrix Ii](https://leetcode.com/problems/spiral-matrix-ii/) — LeetCode
