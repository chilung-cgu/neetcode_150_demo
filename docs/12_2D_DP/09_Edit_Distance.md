# Edit Distance (編輯距離) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #72** — [題目連結](https://leetcode.com/problems/edit-distance/) | [NeetCode 解說](https://neetcode.io/problems/edit-distance)


## 1. 🧐 Problem Dissection (釐清問題)

給兩個字串 `word1` 和 `word2`。
請計算將 `word1` 轉換成 `word2` 所需的 **最少操作次數**。
允許的操作有三種：

1.  Insert a character (插入)
2.  Delete a character (刪除)
3.  Replace a character (替換)

-   **Input**: `word1 = "horse", word2 = "ros"`
-   **Output**: `3`
    -   horse -> rorse (replace 'h' with 'r')
    -   rorse -> rose (remove 'r')
    -   rose -> ros (remove 'e')
-   **Input**: `word1 = "intention", word2 = "execution"`
-   **Output**: `5`
-   **Constraints**:
    -   $0 <= word1.length, word2.length <= 500$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`minDist(i, j)`: min distance between `word1[i:]` and `word2[j:]`.

-   If `word1[i] == word2[j]`:
    -   `minDist(i+1, j+1)` (Match)
-   If `word1[i] != word2[j]`: `1 + min(`
    -   `minDist(i, j+1)` (Insert: `word1` stays at `i`, `word2` moves `j`)
    -   `minDist(i+1, j)` (Delete: `word1` moves `i`, `word2` stays `j`)
    -   `minDist(i+1, j+1)` (Replace)
    - `)`
-   **Time**: $O(3^N)$.

---

## 3. 💡 The "Aha!" Moment (優化)

標準的 2D DP (Levenshtein Distance)。
`dp[i][j]` 表示 `word1` 前 `i` 個字元和 `word2` 前 `j` 個字元的最少操作數。

**Transition**:

1.  如果 `word1[i-1] == word2[j-1]`:
    -   不需要操作，直接繼承：`dp[i][j] = dp[i-1][j-1]`
2.  如果不相等：
    -   `dp[i][j] = 1 + min(`
        -   `dp[i][j-1]` (Insert into word1 to match word2[j-1])
        -   `dp[i-1][j]` (Delete from word1)
        -   `dp[i-1][j-1]` (Replace)
        - `)`

**Base Case**:

-   `dp[i][0] = i` (word2 為空，word1 需刪除 `i` 次)
-   `dp[0][j] = j` (word1 為空，word1 需插入 `j` 次)

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../edit_distance_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../edit_distance_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: 2D DP

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();

        // dp[i][j]
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        // Base cases
        for (int i = 0; i <= m; i++) dp[i][0] = i; // Delete all chars
        for (int j = 0; j <= n; j++) dp[0][j] = j; // Insert all chars

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1]; // No op needed
                } else {
                    dp[i][j] = 1 + min({
                        dp[i - 1][j],    // Delete
                        dp[i][j - 1],    // Insert
                        dp[i - 1][j - 1] // Replace
                    });
                }
            }
        }

        return dp[m][n];
    }
};
```

### Python Reference

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        return dp[0][0]
```
Note: Python solution uses backward DP (filling from bottom-right), C++ uses standard forward DP. Both are valid.

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.length();
        int n = word2.length();

        // dp[i][j] = 將 word1 前 i 個字元 轉換成 word2 前 j 個字元 的最小步數
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));

        // Base case initialization
        // 當 word2 是空字串 (j=0)，word1 必須刪除所有 i 個字元
        for (int i = 0; i <= m; i++) dp[i][0] = i;
        // 當 word1 是空字串 (i=0)，word1 必須插入所有 j 個字元
        for (int j = 0; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // 如果當前字元相同 (注意 index 是 i-1, j-1)
                if (word1[i-1] == word2[j-1]) {
                    // 不需要做操作，繼承左上角
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    // 如果不同，取三種操作的最小值 + 1
                    dp[i][j] = 1 + min({
                        dp[i-1][j],    // Delete (刪除 word1[i-1])，狀態回到 i-1, j
                        dp[i][j-1],    // Insert (在 word1 後插入 word2[j-1])，狀態回到 i, j-1
                        dp[i-1][j-1]   // Replace (將 word1[i-1] 換成 word2[j-1])，狀態回到 i-1, j-1
                    });
                }
            }
        }

        return dp[m][n];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   $500 \times 500 = 2.5 \times 10^5$. Fast.
-   **Space Complexity**: $O(M \times N)$
    -   Can be optimized to $O(\min(M, N))$ using 1D array (but need `prev_diag` var).
