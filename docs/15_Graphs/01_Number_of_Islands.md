# Number of Islands (島嶼數量) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #200** — [題目連結](https://leetcode.com/problems/number-of-islands/) | [NeetCode 解說](https://neetcode.io/problems/number-of-islands)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個由 `'1'` (陸地) 和 `'0'` (水) 組成的二維網格 `grid`。
請計算島嶼的數量。
島嶼被水包圍，由水平或垂直相鄰的陸地連接而成。
你可以假設網格的四個邊之外都被水包圍。

-   **Input**:
    ```
    [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    ```

-   **Output**: `1`
-   **Input**:
    ```
    [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    ```

-   **Output**: `3`
-   **Constraints**:
    -   $m == grid.length$
    -   $n == grid[i].length$
    -   $1 <= m, n <= 300$
    -   `grid[i][j]` is `'0'` or `'1'`.

---

## 2. 🐢 Brute Force Approach (暴力解)

這個問題本身就是一個圖的連通分量計數問題。
我們必須遍歷整個網格的每一個格子。
如果遇到一個未訪問過的 `'1'`，這意味著我們發現了一個新的島嶼。
然後我们需要啟動一個遍歷算法 (DFS 或 BFS) 來標記屬於這個島嶼的所有陸地，以免重複計算。

其實這就是標準解法，沒有所谓的更低效的暴力解 (除非你用隨機漫步...)。

---

## 3. 💡 The "Aha!" Moment (優化)

**DFS / BFS**:
遍歷網格中的每個點 `(r, c)`：

1.  如果 `grid[r][c] == '1'`：
    -   計數器 `islands++`。
    -   呼叫 `dfs(r, c)` 或 `bfs(r, c)`。
    -   在遍歷過程中，將訪問過的 `'1'` 修改為 `'0'` (或標記為 visited)。這樣我們就不會再次計算它。
2.  如果 `grid[r][c] == '0'`：跳過。

這種方法會訪問每個節點常數次。

**In-place Modification**:
為了節省空間，我們可以直接修改 `grid` 本身，把訪問過的 `'1'` 變成 `'0'` (沈沒島嶼)。這樣不需要額外的 `visited` 陣列。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../num_islands_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../num_islands_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DFS (In-place)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int m = grid.size();
        int n = grid[0].size();
        int count = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }

        return count;
    }

private:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        int m = grid.size();
        int n = grid[0].size();

        // Base case: boundaries or water
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == '0') {
            return;
        }

        // Mark as visited (sink the island)
        grid[r][c] = '0';

        // Visit neighbors
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
};
```

### Python Reference

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == '0'):
                return

            grid[r][c] = '0' # Sink

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;

        int m = grid.size();
        int n = grid[0].size();
        int count = 0;

        // 遍歷每一個格子
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 如果遇到陸地 '1'，代表發現一個新島嶼
                if (grid[i][j] == '1') {
                    count++;
                    // 使用 DFS 將與這塊陸地相連的所有陸地都標記為已訪問 (變成 '0')
                    // 這樣下次遍歷到它們時就會跳過
                    dfs(grid, i, j);
                }
            }
        }

        return count;
    }

private:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        // 邊界檢查
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size()) {
            return;
        }

        // 如果是水 '0'，直接返回
        if (grid[r][c] == '0') {
            return;
        }

        // 關鍵步驟：將當前陸地標記為 '0' (沈沒)
        // 這防止了無限遞迴，同时也標記了已訪問
        grid[r][c] = '0';

        // 遞迴訪問上下左右四個鄰居
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   We visit each cell a constant number of times.
-   **Space Complexity**: $O(M \times N)$ (worst case for recursion stack)
    -   In the worst case (grid is full of land), DFS recursion can go up to $M \times N$ deep.
    -   BFS would take $O(\min(M, N))$ space if optimized, or $O(M \times N)$ in general queue usage.

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
