# N-Queens (N 皇后問題) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目要求在一個 `n x n` 的棋盤上放置 `n` 個皇后，使得它們互不攻擊。

-   皇后可以攻擊同一行、同一列、以及兩條對角線上的任何棋子。
-   回傳所有可能的擺放方案。用 'Q' 代表皇后，'.' 代表空位。

-   **Input**: `n = 4`
-   **Output**:
    ```
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],

     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]
    ```

-   **Constraints**:
    -   $1 <= n <= 9$

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試所有可能的 `n` 個位置組合，共有 $\binom{n^2}{n}$ 種。
對每一種組合檢查是否合法。非常慢。

---

## 3. 💡 The "Aha!" Moment (優化)

**Backtracking (Constraint Programming)**:
我們逐行放置皇后。每行只能放一個。
當我們在第 `r` 行放置皇后時，我們只需要決定它放在哪一列 `c`。
放置前檢查 `(r, c)` 是否安全：

1.  **Column check**: 這一列之前有沒有放過？
2.  **Positive Diagonal check (45度)**: 對角線 `r + c` 是否有皇后？
3.  **Negative Diagonal check (135度)**: 對角線 `r - c` 是否有皇后？

**State Maintenance**:
使用三個 Set (或 boolean array) 來紀錄被佔用的：

-   `cols`: 紀錄哪些列 `c` 已佔用。
-   `posDiag`: 紀錄 `r + c` 的值。
-   `negDiag`: 紀錄 `r - c` 的值。

這樣檢查是否安全只要 $O(1)$。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../n_queens_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../n_queens_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking with Sets

```cpp
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> result;
        vector<string> board(n, string(n, '.'));

        // Use arrays for faster access than checking board manually
        // But here we use sets for clarity of "Aha" moment explanation
        // Actually, vector<bool> is faster for backtracking
        vector<bool> cols(n, false);
        vector<bool> posDiag(2 * n, false); // r + c
        vector<bool> negDiag(2 * n, false); // r - c + n (offset to make positive)

        backtrack(n, 0, board, cols, posDiag, negDiag, result);
        return result;
    }

private:
    void backtrack(int n, int r, vector<string>& board,
                   vector<bool>& cols, vector<bool>& posDiag, vector<bool>& negDiag,
                   vector<vector<string>>& result) {
        // Base case: placed queens on all n rows
        if (r == n) {
            result.push_back(board);
            return;
        }

        for (int c = 0; c < n; c++) {
            // Check if valid
            // r - c can be negative, so add n
            if (cols[c] || posDiag[r + c] || negDiag[r - c + n]) {
                continue;
            }

            // Place Queen
            cols[c] = true;
            posDiag[r + c] = true;
            negDiag[r - c + n] = true;
            board[r][c] = 'Q';

            // Recurse
            backtrack(n, r + 1, board, cols, posDiag, negDiag, result);

            // Backtrack (Remove Queen)
            cols[c] = false;
            posDiag[r + c] = false;
            negDiag[r - c + n] = false;
            board[r][c] = '.';
        }
    }
};
```

### Python Reference

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    vector<vector<string>> ans;
    // 使用 boolean array 來快速檢查特定的 Column 和 Diagonal 是否被佔用
    // cols: 直行
    // diag1: 45度對角線 (r + c = constant)
    // diag2: 135度對角線 (r - c = constant)，需加 offset 防止負數
    vector<bool> cols, diag1, diag2;

public:
    vector<vector<string>> solveNQueens(int n) {
        cols = vector<bool>(n, false);
        diag1 = vector<bool>(2 * n, false);
        diag2 = vector<bool>(2 * n, false);

        // 棋盤初始化
        vector<string> board(n, string(n, '.'));

        dfs(0, n, board);
        return ans;
    }

    // r: 當前嘗試放置皇后的行數 (Row)
    void dfs(int r, int n, vector<string>& board) {
        // Base Case: 成功放置了 n 個皇后 (r 從 0 到 n-1 都放好了)
        if (r == n) {
            ans.push_back(board);
            return;
        }

        // 嘗試將皇后放在第 r 行的第 c 列
        for (int c = 0; c < n; c++) {
            // 檢查衝突
            // r - c 可能為負，加上 n 作為 offset，確保 index >= 0
            if (cols[c] || diag1[r + c] || diag2[r - c + n]) {
                continue;
            }

            // 放置皇后
            board[r][c] = 'Q';
            cols[c] = true;
            diag1[r + c] = true;
            diag2[r - c + n] = true;

            // 遞迴下一行
            dfs(r + 1, n, board);

            // Backtrack (撤銷放置)
            board[r][c] = '.';
            cols[c] = false;
            diag1[r + c] = false;
            diag2[r - c + n] = false;
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N!)$
    -   第一行有 N 種選擇，只有一個 Valid。
    -   第二行除了同列和對角線，大約剩 N-2~N-3 種。
    -   實際上這是一個嚴格的 $N!$ 上界，因為剪枝非常多，實際跑起來比 $N!$ 快很多，但 Big-O 仍視為 $N!$。
-   **Space Complexity**: $O(N)$
    -   Board storage $O(N^2)$, but auxiliary arrays and stack are $O(N)$.
