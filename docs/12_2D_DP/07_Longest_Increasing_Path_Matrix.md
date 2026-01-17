# Longest Increasing Path in a Matrix (矩陣中的最長遞增路徑)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的整數矩陣 `matrix`，回傳其中的 **最長遞增路徑** 的長度。
路徑中的每一步，可以向上下左右移動。
不能走出邊界，不能走回頭路 (但因為是嚴格遞增，所以天然不會走回頭路)。

-   **Input**:
    ```
    matrix = [
      [9,9,4],
      [6,6,8],
      [2,1,1]
    ]
    ```

-   **Output**: `4` (The path is [1, 2, 6, 9])
-   **Input**: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`
-   **Output**: `4` ([3, 4, 5, 6])
-   **Constraints**:
    -   $m, n <= 200$
    -   $0 <= matrix[i][j] <= 2^{31} - 1$

---

## 2. 🐢 Brute Force Approach (暴力解)

**DFS**:
從每一個格子 `(i, j)` 出發，嘗試四個方向。
如果鄰居比自己大，就可以走過去。
紀錄每條路徑的長度。

-   **Time**: $O(4^{M \times N})$ ??
    -   因為是遞增，每個點最多只會被訪問一次？
    -   不，如果不做記憶化，即使同樣的點，如果從不同的路徑到達，也會重複計算其後續的最長路徑。
    -   這會導致巨大的重複計算。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個 **DFS + Memoization** (記憶化搜索) 的經典問題。
這其實就是 **DAG (Directed Acyclic Graph)** 上的最長路徑問題。

-   每個格子是一個節點。
-   如果 `A < B` 且相鄰，則有一條邊 `A -> B`。
-   因為嚴格遞增，所以圖中沒有環 (DAG)。

定義 `dp[i][j]` (或 `memo[i][j]`) 為：從 `(i, j)` 出發，能走出的最長遞增路徑長度。
`dp[i][j] = 1 + max(dp[neighbors])` where `neighbor > current`.
如果四週都沒有比自己大的，`dp[i][j] = 1`。

算法：

1.  遍歷矩陣中每一個點 `(i, j)`。
2.  對每個點呼叫 `dfs(i, j)`。
3.  在 `dfs` 中，如果 `memo[i][j]` 已經計算過，直接回傳。
4.  否則，計算 `1 + max(dfs(neighbors))` 並存入 `memo[i][j]`。
5.  全域最大值即為答案。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../longest_increasing_path_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../longest_increasing_path_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DFS + Memoization

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int m, n;
    vector<vector<int>> memo;
    int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if (matrix.empty()) return 0;

        m = matrix.size();
        n = matrix[0].size();
        memo = vector<vector<int>>(m, vector<int>(n, 0));

        int maxLen = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                maxLen = max(maxLen, dfs(matrix, i, j));
            }
        }

        return maxLen;
    }

    int dfs(vector<vector<int>>& matrix, int r, int c) {
        if (memo[r][c] != 0) return memo[r][c];

        int len = 1;

        for (auto& dir : dirs) {
            int nr = r + dir[0];
            int nc = c + dir[1];

            // Check boundary and strictly increasing condition
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && matrix[nr][nc] > matrix[r][c]) {
                len = max(len, 1 + dfs(matrix, nr, nc));
            }
        }

        memo[r][c] = len;
        return len;
    }
};
```

### Python Reference

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {} # (r, c) -> LIP length

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                matrix[r][c] <= prevVal):
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            res = 1
            res = max(res, 1 + dfs(r + 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r - 1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c + 1, matrix[r][c]))
            res = max(res, 1 + dfs(r, c - 1, matrix[r][c]))

            dp[(r, c)] = res
            return res

        longest = 0
        for r in range(ROWS):
            for c in range(COLS):
                longest = max(longest, dfs(r, c, -1))

        return longest
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    int rows, cols;
    // memo[i][j] 用來儲存從 (i, j) 開始的最長遞增路徑長度
    // 0 代表尚未計算
    vector<vector<int>> memo;
    // 上下左右四個方向
    int directions[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        rows = matrix.size();
        cols = matrix[0].size();

        // 矩陣初始化為 0
        memo = vector<vector<int>>(rows, vector<int>(cols, 0));

        int maxPath = 0;

        // 我們必須嘗試從每一個格子出發
        // 因為最長路徑可能始於任何一個 "局部最小值"
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                maxPath = max(maxPath, dfs(matrix, i, j));
            }
        }

        return maxPath;
    }

    // DFS with Memoization
    int dfs(vector<vector<int>>& matrix, int r, int c) {
        // 如果已經計算過，直接回傳
        if (memo[r][c] != 0) return memo[r][c];

        int currentMax = 1; // 至少包含自己，長度為 1

        // 嘗試四個方向
        for (auto& dir : directions) {
            int newRow = r + dir[0];
            int newCol = c + dir[1];

            // 邊界檢查 + 嚴格遞增檢查
            // 只有當鄰居比自己大，才能走過去，這樣保證了不會走回頭路 (不需 visited 陣列)
            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
                matrix[newRow][newCol] > matrix[r][c]) {

                // 遞迴計算並取最大值
                currentMax = max(currentMax, 1 + dfs(matrix, newRow, newCol));
            }
        }

        // 紀錄結果並回傳
        memo[r][c] = currentMax;
        return currentMax;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   Each cell is computed exactly once due to memoization.
    -   For each cell, we check 4 neighbors ($O(1)$).
-   **Space Complexity**: $O(M \times N)$
    -   Memoization table + Recursion stack.
