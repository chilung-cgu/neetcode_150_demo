---
title: "Word Search (單字搜尋)"
description: "題目給一個 `m x n` 的字符網格 `board` 和一個單字 `word`。 如果 `word` 存在於網格中，回傳 `true`；否則回傳 `false`。 單字必須由網格中 **相鄰** 的字母組成（水平或垂直），同一個儲存格內的字母在同一個單字中最多只能使用一次。"
tags:
  - Backtracking
  - Recursion
difficulty: Medium
---

# Word Search (單字搜尋) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #79** — [題目連結](https://leetcode.com/problems/word-search/) | [NeetCode 解說](https://neetcode.io/problems/search-for-word)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 `m x n` 的字符網格 `board` 和一個單字 `word`。
如果 `word` 存在於網格中，回傳 `true`；否則回傳 `false`。
單字必須由網格中 **相鄰** 的字母組成（水平或垂直），同一個儲存格內的字母在同一個單字中最多只能使用一次。

-   **Input**:
    ```
    board = [
      ["A","B","C","E"],
      ["S","F","C","S"],
      ["A","D","E","E"]
    ]
    word = "ABCCED"
    ```

-   **Output**: `true`
    -   (0,0)A -> (0,1)B -> (0,2)C -> (1,2)C -> (1,3)E -> (2,3)E ? No, last is D.
    -   (0,0)A -> (0,1)B -> (0,2)C -> (1,2)C -> (2,2)E -> (2,1)D. YES.
-   **Input**: `word = "SEE"`
-   **Output**: `true`
-   **Input**: `word = "ABCB"`
-   **Output**: `false` (B is used, cannot reuse)
-   **Constraints**:
    -   $m, n <= 6$
    -   $1 <= word.length <= 15$
    -   **Follow up**: Could you use pruning to simplify your solution?

---

## 2. 🐢 Brute Force Approach (暴力解)

**Backtracking**:
對 board 上的每一個 cell，如果 `board[i][j] == word[0]`，則以此為起點開始 DFS。

-   DFS 需要維護 `visited` 狀態 (可以用 `board[i][j] = '#'` 來標記)。
-   **Time**: $O(M \times N \times 4^L)$。
    -   $L$ 是 word length。
    -   這題規模很小 ($6 \times 6$)，所以很穩。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是標準的 **DFS Backtracking** on Grid。

**Optimization (Pruning)**:

1.  **Check feasibility first**: 如果 `word` 中的某個字元在 `board` 中出現的總次數比 `word` 中需要的還少，直接回傳 `false`。
2.  **Reverse Word**: 如果 `word` 尾端的字元在 board 中出現次數很少，而首端的字元出現次數很多，可以考慮將 `word` 反轉再搜尋，減少分支 (Branching Factor)。
    -   例如 board 只有很少的 'A' 但有很多 'Z'，而 `word` 是 "ZZZ...A"，從 'Z' 開始搜會有很多無效路徑，從 'A' 開始搜就會很快。
    -   這是一個很厲害的 trick。
3.  **In-place Modification**: modify `board` to mark visited instead of using extra `visited` array.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../word_search_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../word_search_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Standard DFS with Pruning

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();

        // Simple Pruning: Check if board has enough chars
        // (Optional but good for edge cases)
        // ...

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word[0]) {
                    if (dfs(board, i, j, word, 0)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

private:
    bool dfs(vector<vector<char>>& board, int r, int c, string& word, int index) {
        // Base case: All chars matched
        if (index == word.length()) {
            return true;
        }

        // Boundary check and Char match check
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size() || board[r][c] != word[index]) {
            return false;
        }

        // Mark as visited (temporarily)
        char temp = board[r][c];
        board[r][c] = '#';

        // Explore 4 directions
        bool found = dfs(board, r + 1, c, word, index + 1) ||
                     dfs(board, r - 1, c, word, index + 1) ||
                     dfs(board, r, c + 1, word, index + 1) ||
                     dfs(board, r, c - 1, word, index + 1);

        // Backtrack (Restore)
        board[r][c] = temp;

        return found;
    }
};
```

### Python Reference

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size();
        int n = board[0].size();

        // 遍歷每一個格子，找到這字串的第一個字
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                // 如果找到第一個字，就啟動 DFS
                if(board[i][j] == word[0]) {
                    if(dfs(board, i, j, word, 0)) return true;
                }
            }
        }
        return false;
    }

    // DFS 函數：當前在 (r,c)，要匹配 word[index]
    bool dfs(vector<vector<char>>& board, int r, int c, string& word, int index) {
        // Base Case 1: 已經成功匹配完所有的字元
        // 注意：這裡如果 index == word.length() - 1 且當前 char 匹配，也算成功
        // 但常常寫成 index == word.length() 來判斷已經越界，代表前一個都成功了
        // 此實作中，我們每進一層先檢查 board[r][c] == word[index]
        // 所以如果能夠走到 index == word.size()，代表成功。
        // 但這裡我們需要在進入之前先檢查 index 是否到底？
        // 修正邏輯：我們是檢查當前这一格。

        // 邏輯:
        // 1. 檢查越界
        if (r < 0 || r >= board.size() || c < 0 || c >= board[0].size()) return false;

        // 2. 檢查字元是否匹配，或是否已訪問 ('#')
        if (board[r][c] != word[index]) return false;

        // 3. 如果這是最後一個字元，且匹配成功 (上面沒 return false)，則成功
        if (index == word.size() - 1) return true;

        // 4. 標記訪問
        char temp = board[r][c];
        board[r][c] = '#';

        // 5. 遞迴四個方向
        // 只要有一個方向成功，就回傳 true
        bool res = dfs(board, r+1, c, word, index+1) ||
                   dfs(board, r-1, c, word, index+1) ||
                   dfs(board, r, c+1, word, index+1) ||
                   dfs(board, r, c-1, word, index+1);

        // 6. Backtrack 恢復
        board[r][c] = temp;

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N \times 4^L)$
    -   Search starts from each cell.
    -   DFS depth is $L$ (length of word).
-   **Space Complexity**: $O(L)$
    -   Recursion stack.

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
- [Word Search II (單字搜尋 II)](../08_Tries/03_Word_Search_II.md)
