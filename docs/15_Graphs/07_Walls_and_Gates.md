---
title: "Walls and Gates (牆與門)"
description: "給定一個 `m x n` 的網格，包含以下三種可能的值："
tags:
  - Graph
  - DFS
  - BFS
difficulty: Medium
---

# Walls and Gates (牆與門) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #286** — [題目連結](https://leetcode.com/problems/walls-and-gates/) | [NeetCode 解說](https://neetcode.io/problems/walls-and-gates)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的網格，包含以下三種可能的值：

-   `-1`: 代表牆壁或障礙物。
-   `0`: 代表門 (Gate)。
-   `INF` (通常用 `2147483647` 表示): 代表空房間。

請原地 (in-place) 填入每個空房間到 **最近的門** 的距離。
如果該房間無法到達任何門，則保持為 `INF`。

-   **Input**:
    ```
    INF  -1  0  INF
    INF INF INF  -1
    INF  -1 INF  -1
      0  -1 INF INF
    ```

-   **Output**:
    ```
      3  -1   0   1
      2   2   1  -1
      1  -1   2  -1
      0  -1   3   4
    ```

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一個房間 (`INF`)，啟動 BFS 尋找最近的門。

-   如果有 $k$ 個房間，每個房間 BFS 耗時 $O(m \times n)$。
-   總時間 $O(k \times m \times n)$。如果是稀疏的門，這會接近 $O((m \times n)^2)$。

---

## 3. 💡 The "Aha!" Moment (優化)

**Multi-source BFS**:
這跟 "Rotting Oranges" 是同一個問題。
我們不是從每個房間找門，而是 **從所有門同時出發找房間**。

1.  **Queue Initialization**: 遍歷網格，將所有門 (`0`) 的坐標加入 Queue。
2.  **BFS**:
    -   從 Queue 中取出一個點 `(r, c)`。
    -   檢查它的四周鄰居 `(nr, nc)`。
    -   如果鄰居是房間 (`INF`)，意味著我們找到了該房間到門的最短路徑（因為 BFS 保證是按照距離層次遍歷的）。
    -   更新鄰居的距離：`grid[nr][nc] = grid[r][c] + 1`。
    -   將鄰居加入 Queue。
    -   注意：不需要額外的 visited 陣列，因為我們只更新 `INF` 的房間。如果一個房間已經被更新過了（不再是 `INF`），說明之前已經有更近的門到達了它，我們不需要再去更新（BFS 特性）。

-   **Time**: $O(m \times n)$。每個點最多被訪問一次。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../walls_gates_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../walls_gates_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Multi-source BFS

```cpp
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if (rooms.empty()) return;

        int m = rooms.size();
        int n = rooms[0].size();
        queue<pair<int, int>> q;

        // 1. Add all gates to the queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 2. BFS
        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();

            int r = curr.first;
            int c = curr.second;

            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                // Check bounds and if it is an empty room
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && rooms[nr][nc] == INT_MAX) {
                    // Update distance
                    rooms[nr][nc] = rooms[r][c] + 1;
                    q.push({nr, nc});
                }
            }
        }
    }
};
```

### Python Reference

```python
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return

        rows, cols = len(rooms), len(rooms[0])
        q = deque()

        # Add gates to queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc

                # Check bounds and if empty room
                # (empty room is usually 2**31 - 1)
                if (row < 0 or row == rows or
                    col < 0 or col == cols or
                    rooms[row][col] != 2147483647):
                    continue

                rooms[row][col] = rooms[r][c] + 1
                q.append((row, col))
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        if (rooms.empty()) return;

        int m = rooms.size();
        int n = rooms[0].size();
        queue<pair<int, int>> q;

        // 1. 初始化：將所有門加入 Queue
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rooms[i][j] == 0) {
                    q.push({i, j});
                }
            }
        }

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 2. 開始 BFS 擴散
        while (!q.empty()) {
            pair<int, int> curr = q.front();
            q.pop();

            int r = curr.first;
            int c = curr.second;

            // 檢查四周鄰居
            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                // 如果鄰居在範圍內，且是空房間 (INT_MAX)
                // 我們只需要更新空房間。如果鄰居是牆(-1)或門(0)，或已經被填過數字，都跳過
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && rooms[nr][nc] == INT_MAX) {
                    // 更新距離 = 當前距離 + 1
                    rooms[nr][nc] = rooms[r][c] + 1;
                    // 將新填好的房間加入 Queue，繼續擴散
                    q.push({nr, nc});
                }
            }
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   We visit each cell at most once.
-   **Space Complexity**: $O(M \times N)$
    -   Queue size.

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
- [Rotting Oranges (腐爛的橘子)](06_Rotting_Oranges.md)
