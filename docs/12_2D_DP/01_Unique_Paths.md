---
title: "Unique Paths (不同路徑)"
description: "題目給一個 `m x n` 的網格。 機器人位於左上角 `(0, 0)`。 目標是移動到右下角 `(m-1, n-1)`。 機器人每次只能 **向下** 或 **向右** 移動。 問有多少條不同的路徑？"
tags:
  - Dynamic Programming
  - 2D DP
difficulty: Medium
---

# Unique Paths (不同路徑) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #62** — [題目連結](https://leetcode.com/problems/unique-paths/) | [NeetCode 解說](https://neetcode.io/problems/count-paths)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 `m x n` 的網格。
機器人位於左上角 `(0, 0)`。
目標是移動到右下角 `(m-1, n-1)`。
機器人每次只能 **向下** 或 **向右** 移動。
問有多少條不同的路徑？

-   **Input**: `m = 3, n = 7`
-   **Output**: `28`
-   **Input**: `m = 3, n = 2`
-   **Output**: `3`
    -   Right -> Down -> Down
    -   Down -> Down -> Right
    -   Down -> Right -> Down
-   **Constraints**:
    -   $1 <= m, n <= 100$
    -   Answer guaranteed to be <= $2 \times 10^9$.

---

## 2. 🐢 Brute Force Approach (暴力解)

**DFS**:
`countPaths(r, c)` = `countPaths(r+1, c) + countPaths(r, c+1)`。

-   **Time**: $O(2^{M+N})$。這會非常慢。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個標準的 Grid DP。
`dp[i][j]` 表示到達 `(i, j)` 的路徑數。
因為只能從上面或左邊來：
`dp[i][j] = dp[i-1][j] + dp[i][j-1]`。

Base Case:
`dp[0][0] = 1`.
第一行 (Row 0) 和第一列 (Col 0) 上的點，因為只能一直向右或一直向下，所以路徑數都是 1。

**Space Optimization**:
只需要一列 (`dp[j]`)。
`dp[j]` (new) = `dp[j]` (old, representing from top) + `dp[j-1]` (new, representing from left)。

**Math Approach**:
總共要走 `m-1` 步向下，`n-1` 步向右。總步數 `(m-1) + (n-1)`。
這是一個排列組合問題：從總步數中選出 `m-1` 步向下。
$C(\text{total}, \text{down}) = \binom{M+N-2}{M-1}$。
時間複雜度 $O(\min(M, N))$，空間 $O(1)$。
不過面試通常期望看到 DP 解法，排列組合可以作為 Follow-up。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../unique_paths_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../unique_paths_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Space Optimized)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int uniquePaths(int m, int n) {
        // We only need to store the previous row
        // dp[j] will represent the number of paths to reach cell (current_row, j)
        vector<int> dp(n, 1);

        // Iterate through rows starting from 1 (row 0 is all 1s, already set)
        for (int i = 1; i < m; i++) {
            // Iterate through cols starting from 1 (col 0 is always 1)
            for (int j = 1; j < n; j++) {
                // dp[j] (new) = dp[j] (old, from top) + dp[j-1] (new, from left)
                dp[j] = dp[j] + dp[j-1];
            }
        }

        return dp[n-1];
    }
};
```

### Python Reference

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow

        return row[0]
```
Note: The Python solution above fills from right-to-left bottom-up, which is equivalent.
The standard approach is simpler (left-to-right top-down):

```python
class SolutionStandard:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            for j in range(1, n):
                row[j] += row[j-1]
        return row[-1]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int uniquePaths(int m, int n) {
        // dp[j] 代表到達當前行第 j 列的路徑數。
        // 初始狀態：第一行 (Row 0) 所有格子的路徑數都是 1 (只能一直往右走)。
        vector<int> dp(n, 1);

        // 從第二行 (Row 1) 開始遍歷每一行
        for (int i = 1; i < m; i++) {
            // 對於每一行的每一個格子 j (從第 1 欄開始，因為第 0 欄永遠是 1)
            for (int j = 1; j < n; j++) {
                // 狀態轉移方程：
                // 到達 (i, j) 的路徑數 = 從上方來的路徑數 + 從左方來的路徑數
                // dp[j] (等號左邊) 是当前計算的 (i, j)
                // dp[j] (等號右邊) 還是上一行的值 (i-1, j)，即上方
                // dp[j-1] 是這一行剛計算完的值 (i, j-1)，即左方
                dp[j] = dp[j] + dp[j-1];
            }
        }

        // 回傳到達右下角的路徑數
        return dp[n-1];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   Double loop.
-   **Space Complexity**: $O(N)$
    -   Single vector of size $N$ (width).
    -   Can be optimized to $O(\min(M, N))$ by swapping loops.

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

### 進階挑戰
- [Unique Paths Ii](https://leetcode.com/problems/unique-paths-ii/) — LeetCode
