# Longest Common Subsequence (最長公共子序列)

## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個字串 `text1` 和 `text2`。
回傳它們的**最長公共子序列 (LCS)** 的長度。
子序列不要求連續，但順序必須保持。

-   **Input**: `text1 = "abcde", text2 = "ace"`
-   **Output**: `3` ("ace")
-   **Input**: `text1 = "abc", text2 = "abc"`
-   **Output**: `3`
-   **Input**: `text1 = "abc", text2 = "def"`
-   **Output**: `0`
-   **Constraints**:
    -   $1 <= text1.length, text2.length <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`LCS(i, j)` 代表 `text1[i:]` 和 `text2[j:]` 的 LCS 長度。

1.  如果 `text1[i] == text2[j]`，則 `1 + LCS(i+1, j+1)`。
2.  如果不同，則 `max(LCS(i+1, j), LCS(i, j+1))`。
-   **Time**: $O(2^{N+M})$。

---

## 3. 💡 The "Aha!" Moment (優化)

這是標準的 2D DP 問題。
`dp[i][j]` 表示 `text1` 前 `i` 個字元 (0...i-1) 和 `text2` 前 `j` 個字元 (0...j-1) 的 LCS 長度。

**State Transition**:
和 Recursion 邏輯完全一樣：

1.  If `text1[i-1] == text2[j-1]` (注意 index offset):
    `dp[i][j] = 1 + dp[i-1][j-1]`

2.  If `text1[i-1] != text2[j-1]`:
    `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

Base case: `dp[0][j] = 0`, `dp[i][0] = 0` (空字串的 LCS 長度為 0)。
Target: `dp[M][N]`.

**Space Optimization**:
只需要前一列 (`dp[i-1]`) 就可以算出當前列。
空間可降至 $O(\min(M, N))$。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../lcs_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../lcs_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: 2D DP (Standard)

```cpp
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();

        // dp[i][j] stores LCS of text1[0..i-1] and text2[0..j-1]
        // Size is (m+1) x (n+1) initialized to 0
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    // Match found: Diagonal + 1
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    // No match: Max of Left or Top
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return dp[m][n];
    }
};
```

### Approach: Space Optimized (1D Array)

```cpp
class SolutionOptimized {
public:
    int longestCommonSubsequence(string text1, string text2) {
        if (text1.length() < text2.length()) return longestCommonSubsequence(text2, text1);
        // Ensure text2 is smaller for minor space opt

        int m = text1.length();
        int n = text2.length();
        vector<int> dp(n + 1, 0);

        for (int i = 1; i <= m; i++) {
            int prevDiag = 0; // Represents dp[i-1][j-1]
            for (int j = 1; j <= n; j++) {
                int temp = dp[j]; // Store current dp[i-1][j] before overwrite
                if (text1[i-1] == text2[j-1]) {
                    dp[j] = 1 + prevDiag;
                } else {
                    dp[j] = max(dp[j], dp[j-1]);
                }
                prevDiag = temp; // Update prevDiag for next iteration
            }
        }
        return dp[n];
    }
};
```
(面試時通常寫 2D 即可，除非特別要求優化空間)

### Python Reference

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        int m = text1.length();
        int n = text2.length();

        // dp[i][j] 代表 text1 前 i 個字元與 text2 前 j 個字元的 LCS 長度
        // 大小設為 (m+1) x (n+1) 以處理空字串情況 (padding)
        // 初始值全為 0
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // 如果當前字元相同 (注意字串 index 是 i-1, j-1)
                if (text1[i-1] == text2[j-1]) {
                    // 取左上角的解 + 1
                    dp[i][j] = 1 + dp[i-1][j-1];
                } else {
                    // 如果不同，取「上方」或「左方」的最大值
                    // 繼承目前為止最長的記錄
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
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
    -   Fill the grid.
    -   $1000 \times 1000 = 10^6$ ops. Fast.
-   **Space Complexity**: $O(M \times N)$
    -   DP Grid.
    -   Can be optimized to $O(\min(M, N))$.
