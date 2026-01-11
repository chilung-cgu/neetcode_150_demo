# Rotting Oranges (腐爛的橘子)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的網格，每個單元格可以是：

-   `0`: 空單元格。
-   `1`: 新鮮橘子。
-   `2`: 腐爛橘子。

每一分鐘，任何與腐爛橘子 **相鄰 (4-directionally)** 的新鮮橘子都會變腐爛。
請回傳 **直到所有橘子都腐爛所需的最少分鐘數**。
如果無法讓所有橘子都腐爛，回傳 `-1`。

-   **Input**: `[[2,1,1],[1,1,0],[0,1,1]]`
-   **Output**: `4`
-   **Input**: `[[2,1,1],[0,1,1],[1,0,1]]`
-   **Output**: `-1` (左下角那個橘子永遠不會腐爛)
-   **Input**: `[[0,2]]`
-   **Output**: `0` (沒有新鮮橘子)
-   **Constraints**:
    -   $m, n$ up to 10.

---

## 2. 🐢 Brute Force Approach (暴力解)

重複遍歷整個網格，每一輪找出所有會被感染的橘子，標記它們。
重複直到沒有新的橘子被感染。

-   **Time**: $O(K \times M \times N)$，其中 $K$ 是腐爛時間。這比較慢且繁瑣。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個典型的 **多源廣度優先搜索 (Multi-source BFS)** 問題。
我們可以想像腐爛像病毒一樣從多個源頭同時擴散。BFS 本質上就是按層次（時間）遍歷，所以 BFS 的層數就是所需的分鐘數。

**Algorithm**:

1.  **Queue Initialization**: 遍歷網格，找出所有 **腐爛橘子 (2)** 的位置，加入 Queue。同時，統計 **新鮮橘子 (1)** 的總數 `freshCount`。
2.  **BFS Loop**:
    -   如果 Queue 不為空且 `freshCount > 0`，時間 `time++`。
    -   取出當前層的所有節點 (Queue size)。
    -   對於每個腐爛橘子，檢查其 4 個鄰居。
    -   如果鄰居是新鮮橘子 (1)：
        -   把它變成腐爛 (2) (或者訪問標記)。
        -   `freshCount--`.
        -   加入 Queue。
3.  **Result**:
    -   如果 BFS 結束後 `freshCount == 0`，回傳 `time`。
    -   如果 `freshCount > 0`，說明有橘子無法被觸及，回傳 `-1`。
    -   特例：如果一開始 `freshCount == 0`，直接回傳 `0`。

---

## 4. 💻 Implementation (程式碼)

### Approach: Multi-source BFS

```cpp
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;

        int m = grid.size();
        int n = grid[0].size();
        int freshCount = 0;
        queue<pair<int, int>> q;

        // 1. Initialize BFS
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }

        // Special case: No fresh oranges to begin with
        if (freshCount == 0) return 0;

        int minutes = 0;
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 2. BFS
        while (!q.empty() && freshCount > 0) {
            minutes++;
            int size = q.size();
            for (int k = 0; k < size; k++) {
                pair<int, int> curr = q.front();
                q.pop();

                int r = curr.first;
                int c = curr.second;

                for (auto& d : dirs) {
                    int nr = r + d[0];
                    int nc = c + d[1];

                    // If neighbor is fresh orange
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // Make it rotten
                        freshCount--;
                        q.push({nr, nc});
                    }
                }
            }
        }

        return freshCount == 0 ? minutes : -1;
    }
};
```

### Python Reference

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == rows or
                        col < 0 or col == cols or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;

        int m = grid.size();
        int n = grid[0].size();
        int freshCount = 0;
        queue<pair<int, int>> q;

        // 1. 初始化步驟
        // 掃描矩陣，將所有腐爛橘子加入 Queue (作為 BFS 的起始層)
        // 同時統計新鮮橘子的數量
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    freshCount++;
                }
            }
        }

        // 如果一開始就沒有新鮮橘子，那直接回傳 0 分鐘
        if (freshCount == 0) return 0;

        int minutes = 0;
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 2. BFS 擴散
        // 只要 Queue 不空 且 還有新鮮橘子，就繼續傳染
        while (!q.empty() && freshCount > 0) {
            minutes++;
            int size = q.size(); // 當前層的廣度 (這分鐘內會腐爛的源頭)

            for (int k = 0; k < size; k++) {
                pair<int, int> curr = q.front();
                q.pop();

                int r = curr.first;
                int c = curr.second;

                for (auto& d : dirs) {
                    int nr = r + d[0];
                    int nc = c + d[1];

                    // 檢查鄰居是否是新鮮橘子 (1)
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2; // 傳染腐爛
                        freshCount--;
                        q.push({nr, nc}); // 加入下一層
                    }
                }
            }
        }

        // 如果還有新鮮橘子剩下來，表示有隔離區，回傳 -1
        return freshCount == 0 ? minutes : -1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   Each cell is processed at most once.
-   **Space Complexity**: $O(M \times N)$
    -   Queue can store up to $M \times N$ cells (in worst case).
