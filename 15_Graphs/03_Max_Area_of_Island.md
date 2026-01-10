# Max Area of Island (最大的島嶼面積)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的二維二進制網格 `grid`。
島嶼是一組相連的 `1` (水平或垂直)。
請回傳 **最大的** 島嶼面積。如果沒有島嶼，回傳 0。

-   **Input**:
    ```
    [
      [0,0,1,0,0,0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,1,1,0,1,0,0,0,0,0,0,0,0],
      [0,1,0,0,1,1,0,0,1,0,1,0,0],
      [0,1,0,0,1,1,0,0,1,1,1,0,0],
      [0,0,0,0,0,0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,1,1,1,0,0,0],
      [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    ```
-   **Output**: `6`
    -   最大的那塊在中間偏右。
-   **Constraints**:
    -   $m == grid.length$
    -   $n == grid[i].length$
    -   $1 <= m, n <= 50$
    -   `grid[i][j]` is `0` or `1`.

---

## 2. 🐢 Brute Force Approach (暴力解)

和 "Number of Islands" 完全一樣。
遍歷每個點，如果是 `1`，就啟動 DFS/BFS 計算面積。
記錄最大的面積。
訪問過的點標記為 `0` 以免重複計算。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是標準的 DFS 應用。
-   `dfs(r, c)` 回傳以 `(r, c)` 為起點的連接分量的大小。
-   `dfs` 邏輯：
    1.  邊界檢查 or 若 `grid[r][c] == 0`：return 0。
    2.  `grid[r][c] = 0` (標記已訪問)。
    3.  `return 1 + dfs(up) + dfs(down) + dfs(left) + dfs(right)`。

遍歷全圖，維護全局最大值。

---

## 4. 💻 Implementation (程式碼)

### Approach: DFS (Recursive)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int maxArea = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, dfs(grid, i, j));
                }
            }
        }
        
        return maxArea;
    }
    
private:
    int dfs(vector<vector<int>>& grid, int r, int c) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Base case: boundaries or water
        if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
            return 0;
        }
        
        // Mark as visited (sink the island)
        grid[r][c] = 0;
        
        // Return 1 (current cell) + area of neighbors
        return 1 + dfs(grid, r + 1, c) + 
                   dfs(grid, r - 1, c) + 
                   dfs(grid, r, c + 1) + 
                   dfs(grid, r, c - 1);
    }
};
```

### Python Reference

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == 0):
                return 0
            
            # Sink
            grid[r][c] = 0
            
            return (1 + dfs(r+1, c) + dfs(r-1, c) + 
                    dfs(r, c+1) + dfs(r, c-1))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        
        int m = grid.size();
        int n = grid[0].size();
        int maxArea = 0;
        
        // 遍歷所有格子
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // 如果遇到陸地，計算該島嶼的面積，並更新最大值
                if (grid[i][j] == 1) {
                    maxArea = max(maxArea, dfs(grid, i, j));
                }
            }
        }
        
        return maxArea;
    }
    
private:
    // DFS 函數：計算從 (r, c) 開始的連通分量面積
    int dfs(vector<vector<int>>& grid, int r, int c) {
        // 檢查邊界和是否為水 (0)
        // 注意：這裡題目給的是 int grid，不一定是 char
        if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] == 0) {
            return 0;
        }
        
        // 標記為已訪問 (變成 0)
        grid[r][c] = 0;
        
        // 遞迴計算上下左右的面積，並加上當前節點 (1)
        return 1 + dfs(grid, r + 1, c) + 
                   dfs(grid, r - 1, c) + 
                   dfs(grid, r, c + 1) + 
                   dfs(grid, r, c - 1);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   Each cell is visited once.
-   **Space Complexity**: $O(M \times N)$
    -   Recursive stack depth.
