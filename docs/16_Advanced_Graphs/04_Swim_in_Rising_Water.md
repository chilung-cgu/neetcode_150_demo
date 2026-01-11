# Swim in Rising Water (在上升的水中游泳)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `n x n` 的整數網格 `grid`，其中 `grid[i][j]` 代表該點的海拔高度。
現在下雨了，雨水的高度 `t` 隨著時間線性增加 (t = 0, 1, 2, ...)。
你可以在高度為 `t` 時游到任意高度 `<= t` 的相鄰格子。
求從左上角 `(0, 0)` 游到右下角 `(n-1, n-1)` 所需的最少時間 `t`。

這是一個 **"最小化路徑上的最大權重" (Minimax)** 問題。
路徑的 "Cost" 定義為該路徑上所有點的最大高度。
我們要找一條路徑，使得這個最大高度最小。

-   **Input**: `[[0,2],[1,3]]`
-   **Output**: `3`
    -   Path: 0 -> 1 -> 3. Max height is 3.
-   **Constraints**:
    -   $n$ up to 50.
    -   Values are a permutation of `0` to `n*n - 1`.

---

## 2. 🐢 Brute Force Approach (暴力解)

DFS 尋找所有路徑，記錄每條路徑的最大值，取最小值。

-   **Time**: 指數級。

---

## 3. 💡 The "Aha!" Moment (優化)

**Dijkstra's Algorithm (Modified)**:
這跟 Network Delay Time 很像。我們不是累加權重，而是維護路徑上的 **最大高度**。
`dist[i][j]` 代表到達 `(i, j)` 所需的最小水位高度。
`new_dist = max(current_max, height[neighbor])`。

**Algorithm**:

1.  **Priority Queue**: Min-Heap `(max_height, r, c)`。
2.  **Start**: Push `(grid[0][0], 0, 0)`。
3.  **Visited**: `set` 或 `matrix` to avoid cycles.
4.  **Loop**:
    -   Pop `(h, r, c)`。
    -   如果 `r == n-1 && c == n-1`，回傳 `h`。
    -   對於鄰居 `(nr, nc)`：
        -   `new_h = max(h, grid[nr][nc])`
        -   Push `(new_h, nr, nc)`
        -   Mark visited.

**Alternative**: Binary Search on Answer + DFS/BFS check.

-   Binary Search range `[0, n*n-1]`.
-   Check if path exists with values `<= mid`.
-   Time: $O(N^2 \log(N^2))$. Dijkstra is $O(N^2 \log N)$. Dijkstra is slightly better.

---

## 4. 💻 Implementation (程式碼)

### Approach: Dijkstra's Algorithm

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();

        // Min-Heap: {max_height_so_far, r, c}
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;

        // Initial node: (0, 0)
        pq.push({grid[0][0], 0, 0});

        vector<vector<bool>> visited(n, vector<bool>(n, false));
        visited[0][0] = true;

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!pq.empty()) {
            vector<int> curr = pq.top();
            pq.pop();

            int h = curr[0];
            int r = curr[1];
            int c = curr[2];

            // Reached destination
            if (r == n - 1 && c == n - 1) {
                return h;
            }

            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    // The cost to reach neighbor is max(current_path_max, neighbor_height)
                    pq.push({max(h, grid[nr][nc]), nr, nc});
                }
            }
        }

        return -1;
    }
};
```

### Python Reference

```python
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set([(0, 0)])
        minH = [[grid[0][0], 0, 0]]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit):
                    continue

                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();

        // 使用 Priority Queue 實現 Dijkstra
        // 儲存格式: {路徑上的最大高度, 行, 列}
        // 我們總是優先擴展「最大高度較小」的路徑
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;

        // 從 (0,0) 出發，初始高度就是 grid[0][0]
        pq.push({grid[0][0], 0, 0});

        // 記錄已訪問的節點，避免走回頭路
        vector<vector<bool>> visited(n, vector<bool>(n, false));
        visited[0][0] = true;

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!pq.empty()) {
            vector<int> curr = pq.top();
            pq.pop();

            int h = curr[0]; // 到達這裡所需的最少水位高度
            int r = curr[1];
            int c = curr[2];

            // 如果到達右下角，則當前的 h 就是答案
            // 因為 Dijkstra 保證我們是按 cost 從小到大訪問的
            if (r == n - 1 && c == n - 1) {
                return h;
            }

            // 擴展鄰居
            for (auto& d : dirs) {
                int nr = r + d[0];
                int nc = c + d[1];

                if (nr >= 0 && nr < n && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    // 關鍵邏輯：
                    // 通往鄰居的路徑高度，等於「當前路徑高度」與「鄰居本身高度」的較大值
                    // pq.push({max(h, grid[nr][nc]), nr, nc});
                    int newHeight = max(h, grid[nr][nc]);
                    pq.push({newHeight, nr, nc});
                }
            }
        }

        return -1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^2 \log N)$
    -   Using Min-Heap. Max $N^2$ elements in heap.
-   **Space Complexity**: $O(N^2)$
    -   Visited array and Heap.
