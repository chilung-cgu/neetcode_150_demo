# Regular Expression Matching (正規表示式匹配)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個輸入字串 `s` 和一個模式 `p`。
實現支持 `.` 和 `*` 的正則表達式匹配：

-   `.` 匹配任意單個字符。
-   `*` 匹配零個或多個前面的那一個元素。

-   **Input**: `s = "aa", p = "a*"`
-   **Output**: `true`
-   **Input**: `s = "ab", p = ".*"`
-   **Output**: `true`
-   **Input**: `s = "aab", p = "c*a*b"`
-   **Output**: `true` (c* repeats 0 times, a* repeats 2 times, b matches b)
-   **Constraints**:
    -   $1 <= s.length <= 20$
    -   $1 <= p.length <= 20$ (Very small constraints!)

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`match(i, j)`: check `s[i:]` vs `p[j:]`.

-   If `p[j+1] == '*'`:
    -   We can ignore `p[j], p[j+1]` -> `match(i, j+2)`
    -   If `s[i]` matches `p[j]`, we can consume `s[i]` and keep using `p[j]*` -> `match(i+1, j)`
-   Else:
    -   If `s[i]` matches `p[j]` -> `match(i+1, j+1)`
    -   Else -> false.
-   **Time**: $O(2^{N+M})$. But constraints are small, so maybe OK. DP is safer.

---

## 3. 💡 The "Aha!" Moment (優化)

標準的 2D DP。
`dp[i][j]` 表示 `s` 的前 `i` 個字元和 `p` 的前 `j` 個字元是否匹配。

**Transition**:
1.  如果 `p[j-1]` 是普通字符或 `.`：
    -   `dp[i][j] = dp[i-1][j-1]` IF `match(s[i-1], p[j-1])`
2.  如果 `p[j-1]` 是 `*`：
    -   `*` 表示前面的字符 `p[j-2]` 出現 0 次：
        -   `dp[i][j] = dp[i][j-2]`
    -   `*` 表示前面的字符 `p[j-2]` 出現 1 次或多次：
        -   `dp[i][j] = dp[i-1][j]` IF `match(s[i-1], p[j-2])`

**Base Case**:
`dp[0][0] = true`.
`dp[0][j]` (s is empty) is tricky. Patterns like `"a*b*c*"` can match empty string.
We need to initialize `dp[0][j]` based on `*`.

---

## 4. 💻 Implementation (程式碼)

### Approach: 2D DP

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();

        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;

        // Initialize Row 0 (Empty string s)
        // Cases like a*, a*b*, a*b*c* can match empty string
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    // Case 1: * matches zero times -> look back 2 chars in p
                    bool zero_match = dp[i][j - 2];

                    // Case 2: * matches one or more times -> look back 1 char in s
                    // Condition: s[i-1] must match p[j-2] (the char before *)
                    bool one_plus_match = false;
                    if (s[i - 1] == p[j - 2] || p[j - 2] == '.') {
                        one_plus_match = dp[i - 1][j];
                    }

                    dp[i][j] = zero_match || one_plus_match;
                } else {
                    // Regular match or dot
                    if (s[i - 1] == p[j - 1] || p[j - 1] == '.') {
                        dp[i][j] = dp[i - 1][j - 1];
                    }
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
    def isMatch(self, s: str, p: str) -> bool:
        # cache = {}
        # def dfs(i, j):
        #     if (i, j) in cache: return cache[(i, j)]
        #     if i >= len(s) and j >= len(p): return True
        #     if j >= len(p): return False
        #     ... (Memoization Solution)

        # Bottom-up DP
        cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = (cache[i][j + 2] or
                                   (first_match and cache[i + 1][j]))
                else:
                    cache[i][j] = first_match and cache[i + 1][j + 1]

        return cache[0][0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();

        // dp[i][j] 代表 s[0...i-1] 與 p[0...j-1] 是否匹配
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

        dp[0][0] = true;

        // 初始化第一列 (s 為空字串時)
        // 只有 "x*" 這種模式可以匹配空字串 (視為 0 個 x)
        for (int j = 1; j <= n; j++) {
            if (p[j-1] == '*') {
                // * 前面的字元是 p[j-2]，我們可以選擇忽略 "x*" 這組，退回 j-2
                dp[0][j] = dp[0][j-2];
            }
        }

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j-1] == '*') {
                    // 情況 1: 忽略 '*' 及其前面的字元 (匹配 0 次)
                    // 直接看 p去掉這兩字元後的狀態
                    bool matchZero = dp[i][j-2];

                    // 情況 2: 使用 '*' 來匹配當前 s[i-1] (匹配 1 次或多次)
                    // 前提是：s[i-1] 必須和 '*' 前面的字元 p[j-2] 相同 (或是 '.')
                    // 如果匹配，則看 s 退一格 (i-1) 是否匹配當前 p
                    bool matchMany = false;
                    if (s[i-1] == p[j-2] || p[j-2] == '.') {
                        matchMany = dp[i-1][j];
                    }

                    dp[i][j] = matchZero || matchMany;
                } else {
                    // 普通字元或 '.'
                    // 必須當前字元相同，且前面的也都匹配
                    if (s[i-1] == p[j-1] || p[j-1] == '.') {
                        dp[i][j] = dp[i-1][j-1];
                    }
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
    -   Constraints are small (20), so this is very fast.
-   **Space Complexity**: $O(M \times N)$
    -   DP Grid.
