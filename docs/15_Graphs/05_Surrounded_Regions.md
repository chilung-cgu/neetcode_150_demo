# Surrounded Regions (被圍繞的區域)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個 `m x n` 的矩陣 `board`，包含 `'X'` 和 `'O'`。
請 **捕獲 (capture)** 所有被 `'X'` 圍繞的區域。
捕獲的意思是將這些區域中的所有 `'O'` 翻轉成 `'X'`。
如果一個 `'O'` 位於邊界上，或者與位於邊界的 `'O'` 相連，那麼它就不會被圍繞（無法被捕獲）。

-   **Input**:
    ```
    X X X X
    X O O X
    X X O X
    X O X X
    ```

-   **Output**:
    ```
    X X X X
    X X X X
    X X X X
    X O X X
    ```

    -   解釋：唯一沒被圍繞的 `'O'` 是底部的那個 (3, 1)。與它不相連的其他 `'O'` 都被捕獲變成 `'X'`。
-   **Constraints**:
    -   $m, n$ up to 200.

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每個 `'O'`，執行 BFS/DFS 檢查是否能到達邊界。
如果能到達邊界，則保留。
如果不能到達邊界（被圍繞），則標記為需翻轉。

-   這樣重複計算很多。

---

## 3. 💡 The "Aha!" Moment (優化)

**逆向思維 (Reverse Thinking)**:
所有的 `'O'` 只有兩種命運：

1.  **Escaped**: 與邊界上的 `'O'` 相連。這些 `'O'` 應該保留。
2.  **Captured**: 其他所有的 `'O'`。這些 `'O'` 都會變成 `'X'`。

**Algorithm**:
1.  **Phase 1 (Mark Escaped)**:
    -   遍歷矩陣的四條邊界。
    -   如果遇到 `'O'`，則啟動 DFS/BFS，將所有與之相連的 `'O'` 標記為一個特殊字符（例如 `'T'` for Temporary, or `'E'` for Escaped）。
2.  **Phase 2 (Flip Capture)**:
    -   遍歷整個矩陣。
    -   如果遇到 `'O'`：說明它沒有被 Phase 1 標記，意味著它被圍繞了。變成 `'X'`。
    -   如果遇到 `'T'`：說明它是逃脫者。還原回 `'O'`。

這個方法只需要遍歷全圖兩次（一次 DFS + 一次線性掃描）。

---

## 4. 💻 Implementation (程式碼)

### Approach: Boundary DFS

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;

        int m = board.size();
        int n = board[0].size();

        // 1. Mark 'O's connected to boundary as 'T'
        // Check first and last row
        for (int c = 0; c < n; c++) {
            if (board[0][c] == 'O') dfs(board, 0, c);
            if (board[m-1][c] == 'O') dfs(board, m-1, c);
        }

        // Check first and last column
        for (int r = 0; r < m; r++) {
            if (board[r][0] == 'O') dfs(board, r, 0);
            if (board[r][n-1] == 'O') dfs(board, r, n-1);
        }

        // 2. Flip
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X'; // Captured
                } else if (board[i][j] == 'T') {
                    board[i][j] = 'O'; // Restored
                }
            }
        }
    }

private:
    void dfs(vector<vector<char>>& board, int r, int c) {
        int m = board.size();
        int n = board[0].size();

        // Base case: out of bounds or not 'O'
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O') {
            return;
        }

        // Mark as escaped 'T'
        board[r][c] = 'T';

        // Visit neighbors
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }
};
```

### Python Reference

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return

        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                board[r][c] != "O"):
                return

            board[r][c] = "T"

            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. Capture unsurrounded regions (O -> T)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and
                   (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;

        int m = board.size();
        int n = board[0].size();

        // 核心思路：
        // 所有的 'O' 如果最終還能存活，必定是因為它連通到了矩陣的邊界。
        // 所以我們可以從四個邊界上的所有 'O' 出發，進行 DFS。
        // 把這些「活下來」的 'O' 暫時標記為 'T' (Temp / True)。

        // 1. 檢查第一行和最後一行
        for (int c = 0; c < n; c++) {
            if (board[0][c] == 'O') dfs(board, 0, c);
            if (board[m-1][c] == 'O') dfs(board, m-1, c);
        }

        // 2. 檢查第一列和最後一列
        for (int r = 0; r < m; r++) {
            if (board[r][0] == 'O') dfs(board, r, 0);
            if (board[r][n-1] == 'O') dfs(board, r, n-1);
        }

        // 3. 遍歷整個矩陣進行結算
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    // 如果此時還是 'O'，說明它沒有被邊界 DFS 訪問到
                    // 也就是說它被 'X' 包圍了，所以將其變成 'X'
                    board[i][j] = 'X';
                } else if (board[i][j] == 'T') {
                    // 如果是 'T'，說明它是活下來的 'O'
                    // 將其還原回 'O'
                    board[i][j] = 'O';
                }
            }
        }
    }

private:
    void dfs(vector<vector<char>>& board, int r, int c) {
        int m = board.size();
        int n = board[0].size();

        // 邊界檢查，且必須是 'O' 才繼續
        if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O') {
            return;
        }

        // 標記為臨時狀態 'T'
        board[r][c] = 'T';

        // 繼續擴散
        dfs(board, r + 1, c);
        dfs(board, r - 1, c);
        dfs(board, r, c + 1);
        dfs(board, r, c - 1);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   DFS explores each boundary-connected 'O' once.
    -   Final scan iterates all cells once.
-   **Space Complexity**: $O(M \times N)$
    -   Recursive stack depth (worst case: all 'O's).
