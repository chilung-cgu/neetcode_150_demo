---
title: "Distinct Subsequences (不同的子序列)"
description: "給兩個字串 `s` 和 `t`。 回傳 `s` 的子序列中，有多少個等於 `t`。 (即從 `s` 中刪除一些字元，讓他變成 `t`，有幾種刪法？)"
tags:
  - Dynamic Programming
  - 2D DP
difficulty: Hard
---

# Distinct Subsequences (不同的子序列) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

> 📌 **LeetCode #115** — [題目連結](https://leetcode.com/problems/distinct-subsequences/) | [NeetCode 解說](https://neetcode.io/problems/count-subsequences)


## 1. 🧐 Problem Dissection (釐清問題)

給兩個字串 `s` 和 `t`。
回傳 `s` 的子序列中，有多少個等於 `t`。
(即從 `s` 中刪除一些字元，讓他變成 `t`，有幾種刪法？)

-   **Input**: `s = "rabbbit", t = "rabbit"`
-   **Output**: `3`
    -   Three ways to choose "rabbit" (pick which 'b' to delete).
-   **Input**: `s = "babgbag", t = "bag"`
-   **Output**: `5`
-   **Constraints**:
    -   $1 <= s.length, t.length <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`numDistinct(i, j)` = number of distinct subsequences of `t[j:]` in `s[i:]`.

-   If `s[i] == t[j]`, we can either:
    1.  Match them: `numDistinct(i+1, j+1)`
    2.  Skip `s[i]`: `numDistinct(i+1, j)` (Keep looking for `t[j]` later in `s`)
-   If `s[i] != t[j]`, we must skip: `numDistinct(i+1, j)`
-   **Time**: $O(2^N)$.

---

## 3. 💡 The "Aha!" Moment (優化)

標準的字串匹配 DP。
`dp[i][j]` 表示 `s` 的前 `i` 個字元中及其子序列中，有多少個等於 `t` 的前 `j` 個字元。

**Transition**:

1.  如果 `s[i-1] == t[j-1]` (字元相同):
    -   選擇匹配：`dp[i-1][j-1]` (用掉這個字元)
    -   選擇不匹配（保留給後面）：`dp[i-1][j]` (像刪除這個字元一樣)
    -   `dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`
2.  如果 `s[i-1] != t[j-1]` (字元不同):
    -   只能不匹配：`dp[i][j] = dp[i-1][j]`

**Base Case**:
`dp[i][0] = 1`. (任何字串都能變出一個空字串 `t=""`)。
`dp[0][j] = 0` (空字串變不出非空 `t`).

**Space Optimization**:
只需要前一列 `dp[j]`。但更新時要注意：如果用 1D 陣列，當 `s[i] == t[j]` 時，我們需要 `dp[j-1]` (來自上一輪 `i-1`)。所以如果要用 1D 陣列，內層迴圈需要**從後往前**遍歷，或者使用變數暫存 `prev`。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../distinct_subsequences_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../distinct_subsequences_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: 2D DP (Standard)

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.length();
        int n = t.length();

        // Use unsigned long long to prevent overflow although int is usually sufficient for LC tests
        // But problem statement says "answer fits in 32-bit", so int is fine.
        // However, intermediate calculation might overflow? No, it's strictly additive.
        vector<vector<unsigned int>> dp(m + 1, vector<unsigned int>(n + 1, 0));

        // Base case: t is empty
        for (int i = 0; i <= m; i++) {
            dp[i][0] = 1;
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s[i-1] == t[j-1]) {
                    // Match + Skip
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                } else {
                    // Skip only
                    dp[i][j] = dp[i-1][j];
                }
            }
        }

        return dp[m][n];
    }
};
```

### Approach: 1D DP (Space Optimized)

```cpp
class SolutionOptimized {
public:
    int numDistinct(string s, string t) {
        int m = s.length();
        int n = t.length();
        vector<unsigned int> dp(n + 1, 0);

        dp[0] = 1; // Empty t can be formed by empty s (and any s)

        for (int i = 1; i <= m; i++) {
            // Traverse backwards for t to use data from previous i (i-1)
            for (int j = n; j >= 1; j--) {
                if (s[i-1] == t[j-1]) {
                    dp[j] = dp[j] + dp[j-1];
                }
                // If not match, dp[j] remains dp[j] (which is dp[i-1][j]), so do nothing.
            }
        }
        return dp[n];
    }
};
```

### Python Reference

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {} # (i, j) -> count

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            if s[i] == t[j]:
                dp[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                dp[(i, j)] = dfs(i + 1, j)
            return dp[(i, j)]

        return dfs(0, 0)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int numDistinct(string s, string t) {
        int m = s.size();
        int n = t.size();

        // dp[j] 代表：用當前遍歷到的 s 的前綴，湊出 t 的前 j 個字元的方法數
        // 使用 long long 防止溢位 (雖然題目保證 int，但在 C++ 中有些 corner case 會爆)
        vector<unsigned long long> dp(n + 1, 0);

        // Base case: 湊出空字串 t (j=0) 的方法數永遠是 1 (就是什麼都不選)
        dp[0] = 1;

        // 遍歷 s (source)
        for (int i = 1; i <= m; i++) {
            // 遍歷 t (target)
            // 必須從後往前遍歷 (j from n to 1)！！
            // 類似 0/1 背包，因為我們要用到的是上一輪 (i-1) 的 dp[j-1]
            // 如果從前往後，dp[j-1] 已經被這一輪更新過了，就變成了重複選取
            for (int j = n; j >= 1; j--) {
                // 如果字元匹配
                if (s[i-1] == t[j-1]) {
                    // dp[j] (new) = dp[j] (old, Skip s[i]) + dp[j-1] (old, Match s[i])
                    dp[j] = dp[j] + dp[j-1];
                }
                // 如果不匹配，dp[j] 保持不變 (只能 Skip s[i]，繼承上一輪的方法數)
            }
        }

        return dp[n];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   $1000 \times 1000 = 10^6$. Fast.
-   **Space Complexity**: $O(N)$
    -   Using 1D array optimization.

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
