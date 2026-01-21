# Longest Palindromic Substring (最長回文子字串) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #5** — [題目連結](https://leetcode.com/problems/longest-palindromic-substring/) | [NeetCode 解說](https://neetcode.io/problems/longest-palindromic-substring)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串 `s`，請找出其中最長的 **回文子字串**。
子字串 (Substring) 必須是連續的。
回文 (Palindrome) 是指正著讀和反著讀都一樣的字串。

-   **Input**: `s = "babad"`
-   **Output**: `"bab"` or `"aba"`
-   **Input**: `s = "cbbd"`
-   **Output**: `"bb"`
-   **Constraints**:
    -   $1 <= s.length <= 1000$
    -   s consist of only digits and English letters.

---

## 2. 🐢 Brute Force Approach (暴力解)

檢查每一個可能的子字串是否為回文。

-   總共有 $O(N^2)$ 個子字串。
-   檢查每一個需要 $O(N)$。
-   **Total Time**: $O(N^3)$。 $N=1000$ 時 $10^9$ 次操作，太慢。

---

## 3. 💡 The "Aha!" Moment (優化)

**Approach 1: Dynamic Programming**
`dp[i][j]` 表示 `s[i...j]` 是否為回文。
`dp[i][j] = (s[i] == s[j]) && dp[i+1][j-1]`。

-   Time: $O(N^2)$
-   Space: $O(N^2)$ (Table size)

**Approach 2: Expand Around Center (中心擴展法)**
回文是對稱的。
我們可以枚舉每一個 **中心點**，然後向左右擴展，直到不是回文為止。
中心點有 $2N - 1$ 個（$N$ 個單字元中心 + $N-1$ 個雙字元中心）。

-   例如 "aba" 中心是 'b'。
-   例如 "abba" 中心是 "bb" 之間的空隙。
對每個中心擴展，最壞情況擴展 $O(N)$。

-   Time: $O(N^2)$
-   Space: $O(1)$ (No extra table needed)

**Approach 3: Manacher's Algorithm**
可以在 $O(N)$ 解決，但過於複雜，面試通常不要求寫出，知道即可。
中心擴展法是最實用且面試官最喜歡的解法。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../longest_palindrome_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../longest_palindrome_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Expand Around Center

```cpp
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        int start = 0;
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            // Case 1: Odd length palindrome (Expand from s[i])
            int len1 = expandAroundCenter(s, i, i);

            // Case 2: Even length palindrome (Expand from s[i], s[i+1])
            int len2 = expandAroundCenter(s, i, i + 1);

            int len = max(len1, len2);

            // Update maxLen and start position
            if (len > maxLen) {
                maxLen = len;
                // Consider len=3, i=1 (center). half=1. start = 1 - 1 = 0
                // Consider len=2, i=0 (center is 0,1). half=1. start = 0 - 0 = 0
                // Formula derivation:
                // start = i - (len - 1) / 2
                start = i - (len - 1) / 2;
            }
        }

        return s.substr(start, maxLen);
    }

private:
    int expandAroundCenter(const string& s, int left, int right) {
        while (left >= 0 && right < s.length() && s[left] == s[right]) {
            left--;
            right++;
        }
        // length = right - left - 1
        // Example: "aba", expand from (1,1).
        // l=1,r=1 (ok) -> l=0,r=2 (ok) -> l=-1,r=3 (fail).
        // Length = 3 - (-1) - 1 = 3. Correct.
        return right - left - 1;
    }
};
```

### Python Reference

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if (s.empty()) return "";

        int start = 0;
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            // 1. 以 s[i] 為中心的奇數長度回文
            int len1 = expand(s, i, i);

            // 2. 以 s[i] 和 s[i+1] 之間的空隙為中心的偶數長度回文
            int len2 = expand(s, i, i + 1);

            // 取最長的
            int len = max(len1, len2);

            // 如果比目前最長的還長，更新 start 和 maxLen
            if (len > maxLen) {
                maxLen = len;
                // 計算起始點：
                // 如果是奇數，例如 len=3, center=1 -> start=0. 1 - (3-1)/2 = 0
                // 如果是偶數，例如 len=2, center=0(and 1) -> start=0. 0 - (2-1)/2 = 0
                start = i - (len - 1) / 2;
            }
        }

        return s.substr(start, maxLen);
    }

    // 擴展函數：回傳以此中心擴展得到的最長長度
    int expand(const string& s, int l, int r) {
        while (l >= 0 && r < s.length() && s[l] == s[r]) {
            l--;
            r++;
        }
        // 迴圈結束時，l 和 r 分別在回文範圍的 **外一格**
        // 實際範圍是 [l+1, r-1]
        // 長度 = (r-1) - (l+1) + 1 = r - l - 1
        return r - l - 1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^2)$
    -   Expanding around each center takes up to $O(N)$.
    -   There are $2N-1$ centers.
-   **Space Complexity**: $O(1)$
    -   No extra space except result substring.

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
