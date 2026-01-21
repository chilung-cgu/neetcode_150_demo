# Interleaving String (交錯字串) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #97** — [題目連結](https://leetcode.com/problems/interleaving-string/) | [NeetCode 解說](https://neetcode.io/problems/interleaving-string)


## 1. 🧐 Problem Dissection (釐清問題)

給定三個字串 `s1`, `s2`, `s3`。
判斷 `s3` 是否由 `s1` 和 `s2` **交錯 (Interleave)** 組成。
交錯的意思是：
`s3` 包含 `s1` 和 `s2` 的所有字元，且 `s1` 和 `s2` 內部字元的相對順序保持不變。

-   **Input**: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"`
-   **Output**: `true`
    -   s1: "aa" + "bc" + "c"
    -   s2: "dbbc" + "a"
    -   s3: "aa" + "dbbc" + "bc" + "a" + "c"
-   **Input**: `s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"`
-   **Output**: `false`
-   **Constraints**:
    -   $0 <= s1.length, s2.length <= 100$
    -   $0 <= s3.length <= 200$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`check(i, j, k)` checks match between `s1[i:]`, `s2[j:]`, and `s3[k:]`.

-   If `s1[i] == s3[k]`, try `check(i+1, j, k+1)`.
-   If `s2[j] == s3[k]`, try `check(i, j+1, k+1)`.
-   If both match, try both branches.
-   **Time**: $O(2^{M+N})$.

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個標準的 2D DP 問題。
`dp[i][j]` 表示 `s1` 的前 `i` 個字元和 `s2` 的前 `j` 個字元能否交錯組成 `s3` 的前 `i+j` 個字元。

**Transition**:
`dp[i][j]` is true IF:

1.  `s1` 的第 `i` 個字元 (`s1[i-1]`) 等於 `s3` 的第 `i+j` 個字元 (`s3[i+j-1]`)，且 `dp[i-1][j]` 為真。
    **OR**

2.  `s2` 的第 `j` 個字元 (`s2[j-1]`) 等於 `s3` 的第 `i+j` 個字元 (`s3[i+j-1]`)，且 `dp[i][j-1]` 為真。

**Base Case**:
`dp[0][0] = true`
此外，需檢查長度：如果 `len(s1) + len(s2) != len(s3)`，直接 false。

**Space Optimization**:
只需要前一列 `dp[j]`，空間可優化為 $O(N)$。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../interleaving_string_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../interleaving_string_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: 2D DP

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.length();
        int n = s2.length();

        if (m + n != s3.length()) return false;

        // dp[i][j]: can s1[0...i-1] and s2[0...j-1] form s3[0...i+j-1]
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        dp[0][0] = true;

        // Initialize column 0 (using only s1)
        for (int i = 1; i <= m; i++) {
            dp[i][0] = dp[i-1][0] && (s1[i-1] == s3[i-1]);
        }

        // Initialize row 0 (using only s2)
        for (int j = 1; j <= n; j++) {
            dp[0][j] = dp[0][j-1] && (s2[j-1] == s3[j-1]);
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                // Check if s1[i-1] matches s3 current char
                if (s1[i-1] == s3[i+j-1]) {
                    dp[i][j] = dp[i][j] || dp[i-1][j];
                }

                // Check if s2[j-1] matches s3 current char
                if (s2[j-1] == s3[i+j-1]) {
                    dp[i][j] = dp[i][j] || dp[i][j-1];
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
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [ [False] * (len(s2) + 1) for i in range(len(s1) + 1) ]
        dp[len(s1)][len(s2)] = True

        # Here we perform bottom-up recursion (memoization logic backwards)
        # But standard forward DP is more intuitive.
        # Let's stick to forward DP as in C++ logic for explanation.

        # Re-implementing forward DP in Python for clarity
        dp_fwd = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp_fwd[0][0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0: continue

                # Check s2 (left neighbor)
                if j > 0 and dp_fwd[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                    dp_fwd[i][j] = True

                # Check s1 (top neighbor)
                if i > 0 and dp_fwd[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                    dp_fwd[i][j] = True

        return dp_fwd[len(s1)][len(s2)]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int m = s1.size();
        int n = s2.size();

        // 基本檢查：長度必須吻合
        if (m + n != s3.size()) return false;

        // dp[i][j] 代表：
        // s1 的前 i 個字元 + s2 的前 j 個字元
        // 是否能交錯組成 s3 的前 i+j 個字元
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        // Base Case: 兩個空字串組成一個空字串 -> True
        dp[0][0] = true;

        // 填表
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                // 跳過已經初始化的 (0,0)
                if (i == 0 && j == 0) continue;

                // 1. 嘗試從 s1 拿字元
                // 如果 i > 0 (s1 還有剩)，且 s1 當前字元 (i-1) 等於 s3 當前字元 (i+j-1)
                // 且之前的狀態 dp[i-1][j] 是可行的
                if (i > 0 && s1[i-1] == s3[i+j-1] && dp[i-1][j]) {
                    dp[i][j] = true;
                }

                // 2. 嘗試從 s2 拿字元
                // 如果 j > 0 (s2 還有剩)，且 s2 當前字元 (j-1) 等於 s3 當前字元 (i+j-1)
                // 且之前的狀態 dp[i][j-1] 是可行的
                if (j > 0 && s2[j-1] == s3[i+j-1] && dp[i][j-1]) {
                    dp[i][j] = true;
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
    -   Fill the grid. Given constraints (100x100), extremely fast.
-   **Space Complexity**: $O(M \times N)$
    -   Can be optimized to $O(\min(M, N))$ using 1D array.
