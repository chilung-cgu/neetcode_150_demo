---
title: "Pacific Atlantic Water Flow (太平洋大西洋水流)"
description: "給定一個 `m x n` 的非負整數矩陣 `heights`，代表每個單元格的高度。 矩陣的 **左邊** 和 **上邊** 連接 **太平洋 (Pacific Ocean)**。 矩陣的 **右邊** 和 **下邊** 連接 **大西洋 (Atlantic Ocean)**。 水只能從高處流向低處"
tags:
  - Graph
  - DFS
  - BFS
difficulty: Medium
---

# Pacific Atlantic Water Flow (太平洋大西洋水流) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #417** — [題目連結](https://leetcode.com/problems/pacific-atlantic-water-flow/) | [NeetCode 解說](https://neetcode.io/problems/pacific-atlantic-water-flow)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的非負整數矩陣 `heights`，代表每個單元格的高度。
矩陣的 **左邊** 和 **上邊** 連接 **太平洋 (Pacific Ocean)**。
矩陣的 **右邊** 和 **下邊** 連接 **大西洋 (Atlantic Ocean)**。
水只能從高處流向低處（或等高處）。
找出那些 **既能流向太平洋，又能流向大西洋** 的單元格坐標。

-   **Input**:
    ```
    heights = [
      [1,2,2,3,5],
      [3,2,3,4,4],
      [2,4,5,3,1],
      [6,7,1,4,5],
      [5,1,1,2,4]
    ]
    ```

-   **Output**: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`
-   **Constraints**:
    -   $m, n$ up to 200.
    -   Heights up to $10^5$.

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一個格子 `(r, c)`，執行兩次 DFS/BFS：

1.  檢查能否到達 Pacific (左邊界或上邊界)。
2.  檢查能否到達 Atlantic (右邊界或下邊界)。
如果兩個都返回 True，則加入結果。

-   **Time**: $O((M \times N)^2)$。對於每個點都遍歷全圖。效率太低。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個典型的 **逆向思維** 問題。
與其檢查「每個點能否流到海洋」，不如檢查「**海洋的水能逆流到哪些點**」。

1.  **Pacific Reachable**: 從左邊界和上邊界的所有點開始，進行 DFS/BFS (逆流而上，只能往高處或等高處走)。標記所有能到達的點。
2.  **Atlantic Reachable**: 從右邊界和下邊界的所有點開始，進行 DFS/BFS。標記所有能到達的點。
3.  **Result**: 取兩個集合的 **交集**。

這樣我們只需要遍歷全圖兩次（一次 Pacific，一次 Atlantic）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../pacific_atlantic_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../pacific_atlantic_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DFS Reverse Flow

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty()) return {};

        int m = heights.size();
        int n = heights[0].size();

        // Two visited matrices to keep track of reachability
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));

        // DFS starting from top and bottom rows
        for (int c = 0; c < n; c++) {
            dfs(heights, pacific, 0, c);      // Top row (Pacific)
            dfs(heights, atlantic, m - 1, c); // Bottom row (Atlantic)
        }

        // DFS starting from left and right columns
        for (int r = 0; r < m; r++) {
            dfs(heights, pacific, r, 0);      // Left column (Pacific)
            dfs(heights, atlantic, r, n - 1); // Right column (Atlantic)
        }

        // Find intersection
        vector<vector<int>> result;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }

        return result;
    }

private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int r, int c) {
        visited[r][c] = true;
        int m = heights.size();
        int n = heights[0].size();

        // Direction vectors
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (auto& d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];

            // Check boundaries
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                // Check if unvisited AND height condition implies flow is possible
                // (Reverse flow: neighbor must be >= current)
                if (!visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    dfs(heights, visited, nr, nc);
                }
            }
        }
    }
};
```

### Python Reference

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                (r, c) in visit or heights[r][c] < prevHeight):
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty()) return {};

        int m = heights.size();
        int n = heights[0].size();

        // 兩個矩陣分別記錄能否到達 Pacific 和 Atlantic
        // 初始化為 false
        vector<vector<bool>> pacific(m, vector<bool>(n, false));
        vector<vector<bool>> atlantic(m, vector<bool>(n, false));

        // 從邊界開始 DFS
        // 1. 上下邊界
        // 上邊界 (Row 0) 是 Pacific
        // 下邊界 (Row m-1) 是 Atlantic
        for (int c = 0; c < n; c++) {
            dfs(heights, pacific, 0, c);
            dfs(heights, atlantic, m - 1, c);
        }

        // 2. 左右邊界
        // 左邊界 (Col 0) 是 Pacific
        // 右邊界 (Col n-1) 是 Atlantic
        for (int r = 0; r < m; r++) {
            dfs(heights, pacific, r, 0);
            dfs(heights, atlantic, r, n - 1);
        }

        // 遍歷所有格子，找出交集 (兩者都為 true)
        vector<vector<int>> result;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    result.push_back({i, j});
                }
            }
        }

        return result;
    }

private:
    void dfs(vector<vector<int>>& heights, vector<vector<bool>>& visited, int r, int c) {
        // 標記當前點為可到達
        visited[r][c] = true;

        int m = heights.size();
        int n = heights[0].size();

        // 方向數組：上下左右
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (auto& d : dirs) {
            int nr = r + d[0];
            int nc = c + d[1];

            // 檢查邊界
            if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                // 檢查是否已訪問
                // 檢查逆流條件：鄰居高度必須 >= 當前高度
                // 因為我們是從海洋逆流而上，水只能從高往低流，所以我們只能爬上更高或等高的地方
                if (!visited[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    dfs(heights, visited, nr, nc);
                }
            }
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   We visit each cell a constant number of times (at most once for Pacific BFS/DFS, once for Atlantic BFS/DFS).
-   **Space Complexity**: $O(M \times N)$
    -   For the two visited matrices and recursion stack.

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
