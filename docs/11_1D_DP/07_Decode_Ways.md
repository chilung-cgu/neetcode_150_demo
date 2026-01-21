# Decode Ways (解碼方法) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #91** — [題目連結](https://leetcode.com/problems/decode-ways/) | [NeetCode 解說](https://neetcode.io/problems/decode-ways)


## 1. 🧐 Problem Dissection (釐清問題)

題目說一條由 'A'-'Z' 組成的訊息已經被加密成數字：

-   'A' -> "1"
-   'B' -> "2"
-   ...
-   'Z' -> "26"

給定一個只包含數字的字串 `s`，計算有多少種解碼方法。
注意：

-   "06" 是無效的（不能有前導零）。"0" 也是無效的。
-   "10" -> 'J' (Valid).
-   "26" -> 'Z' (Valid).
-   "27" -> '2', '7' ('B', 'G') (Valid split), but "27" as one char is Invalid.

-   **Input**: `s = "12"`
-   **Output**: `2` ("AB" (1 2) or "L" (12))
-   **Input**: `s = "226"`
-   **Output**: `3` ("BZ" (2 26), "VF" (22 6), "BBF" (2 2 6))
-   **Input**: `s = "06"`
-   **Output**: `0`
-   **Constraints**:
    -   $1 <= s.length <= 100$
    -   s contains only digits.

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
對於 `s[index]`：

1.  解碼 1 個字元：如果是 '1'-'9'，則有效，遞迴 `index + 1`。
2.  解碼 2 個字元：如果是 "10"-"26"，則有效，遞迴 `index + 2`。
-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這又是典型的 DP。
`dp[i]` = `s[0...i-1]` 的解碼方法數。

轉移方程：

1.  **Single Digit decode**:
    -   如果 `s[i-1]` (current char) != '0'，那麼 `dp[i] += dp[i-1]`。
2.  **Two Digits decode**:
    -   如果 `s[i-2]s[i-1]` 形成的數字在 `10` 到 `26` 之間，那麼 `dp[i] += dp[i-2]`。

Base Cases:
`dp[0] = 1` (空字串視為 1 種解碼，為了讓 Two Digits 的第一組運算正確)。
如果是 '0' 開頭，直接回傳 0。

Space Optimization:
只需要 `dp[i-1]` 和 `dp[i-2]`，可以用兩個變數取代陣列。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../decode_ways_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../decode_ways_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Space Optimized)

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') return 0;

        int n = s.length();
        // dp[i] corresponds to number of ways to decode length i
        // prev1 = dp[i-1], prev2 = dp[i-2]
        int prev1 = 1; // dp[0] - empty string has 1 way
        int prev2 = 0; // dp[-1] - conceptual

        // Actually, let's redefine:
        // prev1 is "number of ways to decode string ending at current position"
        // prev2 is "number of ways to decode string ending at previous position"

        // Let's use array concept mentally but implemented with vars
        // dp[0] = 1 (empty)
        // dp[1] = 1 (first char is valid since we checked '0' above)

        prev2 = 1; // dp[0]
        prev1 = 1; // dp[1]

        for (int i = 2; i <= n; i++) {
            int current = 0;

            // Current digit (1-based index is i, so string index is i-1)
            int oneDigit = s[i-1] - '0';
            // Two digits (string index i-2 and i-1)
            int twoDigits = stoi(s.substr(i-2, 2));

            // Check single digit validity
            if (oneDigit >= 1 && oneDigit <= 9) {
                current += prev1;
            }

            // Check two digits validity
            if (twoDigits >= 10 && twoDigits <= 26) {
                current += prev2;
            }

            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
};
```

### Python Reference

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s) : 1 }

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if (i + 1 < len(s) and (s[i] == "1" or
               (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]

        return dp[0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int numDecodings(string s) {
        // 如果以 '0' 開頭，無法解碼
        if (s.empty() || s[0] == '0') return 0;

        int n = s.length();

        // dp[i] 代表前 i 個字元的解碼方法數
        // dp[0] = 1 (空字串 1 種方法，為了 dp[2] 可以加上 dp[0])
        int dp_i_2 = 1; // dp[i-2], 初始為 dp[0]
        int dp_i_1 = 1; // dp[i-1], 初始為 dp[1] (因為 s[0] != '0')

        for (int i = 2; i <= n; i++) {
            int current_dp = 0;

            // 情況 1: 解碼當前這 1 個數字 (s[i-1])
            int oneDigit = s[i-1] - '0';
            if (oneDigit >= 1) {
                current_dp += dp_i_1;
            }

            // 情況 2: 解碼當前這 2 個數字 (s[i-2]s[i-1])
            int twoDigits = stoi(s.substr(i-2, 2));
            if (twoDigits >= 10 && twoDigits <= 26) {
                current_dp += dp_i_2;
            }

            // 滾動更新
            dp_i_2 = dp_i_1;
            dp_i_1 = current_dp;
        }

        return dp_i_1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Iterate through string once.
-   **Space Complexity**: $O(1)$
    -   Using constant extra space.

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
