---
title: "Word Break (單字拆分)"
description: "題目給一個字串 `s` 和一個單字字典 `wordDict`。 判斷 `s` 是否可以被拆分成一個或多個在 `wordDict` 中出現的單字 (space-separated sequence)。 同樣的單字可以在拆分中重複使用。"
tags:
  - Dynamic Programming
difficulty: Medium
---

# Word Break (單字拆分) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #139** — [題目連結](https://leetcode.com/problems/word-break/) | [NeetCode 解說](https://neetcode.io/problems/word-break)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串 `s` 和一個單字字典 `wordDict`。
判斷 `s` 是否可以被拆分成一個或多個在 `wordDict` 中出現的單字 (space-separated sequence)。
同樣的單字可以在拆分中重複使用。

-   **Input**: `s = "leetcode", wordDict = ["leet", "code"]`
-   **Output**: `true` ("leet code")
-   **Input**: `s = "applepenapple", wordDict = ["apple", "pen"]`
-   **Output**: `true` ("apple pen apple")
-   **Input**: `s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]`
-   **Output**: `false`
-   **Constraints**:
    -   $1 <= s.length <= 300$
    -   $1 <= wordDict.length <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`canBreak(start)`:
嘗試每一個 `end` (from `start+1` to `s.length`)。
如果 `s[start...end]` 在字典中 AND `canBreak(end)` 回傳 true，則回傳 true。

-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

**DP (Bottom-Up)**:
定義 `dp[i]` 為 `s[0...i-1]` (長度為 i 的前綴) 是否可以被拆分。
`dp[i] = true` if there exists `j < i` such that `dp[j] == true` AND `s[j...i-1]` is in `wordDict`.

初始化：
`dp[0] = true` (空字串可以被拆分，什麼都不選)。
target: `dp[n]`.

優化檢查：
對於每個 `i`，我們不需要從 `0` 遍歷到 `i`，只需要遍歷 `wordDict` 中的每一個單字 `w`。
如果 `i` >= `w.length` 且 `s[i - w.length ... i-1] == w` 且 `dp[i - w.length]` 為 true，則 `dp[i] = true`。

-   **Time**: $O(N \times M \times L)$
    -   $N$: s length (300)
    -   $M$: wordDict size (1000)
    -   $L$: Avg word length (20)
    -   實際上這比遍歷所有 `j` 更快如果字典不大。
    -   或者 $O(N^2)$ 如果我們遍歷 `j` 並檢查 substring (using HashSet)。$N$ 只有 300，$N^2$ 很小。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../word_break_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../word_break_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP

```cpp
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int n = s.length();

        // dp[i] means s[0...i-1] (length i) can be segmented
        vector<bool> dp(n + 1, false);
        dp[0] = true; // Base case

        for (int i = 1; i <= n; i++) {
            // Check all possible split points j
            // Optimization: iterate j backwards or just words
            // Since N is small (300), O(N^2) is fine
            for (int j = 0; j < i; j++) {
                // If s[0...j-1] is valid AND s[j...i-1] is in dict
                if (dp[j]) {
                    string sub = s.substr(j, i - j);
                    if (dict.count(sub)) {
                        dp[i] = true;
                        break; // Found a valid split for i, move to next i
                    }
                }
            }
        }

        return dp[n];
    }
};
```

### Approach: Iterate Words (Cleaner for strict constraints)

```cpp
class SolutionOptimized {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        int n = s.length();
        vector<bool> dp(n + 1, false);
        dp[0] = true;

        for (int i = 1; i <= n; i++) {
            for (const string& w : wordDict) {
                int len = w.length();
                if (i >= len && dp[i - len] && s.substr(i - len, len) == w) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[n];
    }
};
```
However, comparing full string every time is slightly costly.
Since $N=300$, approach 1 with standard substring check is totally fine.

### Python Reference

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        // 將 wordDict 放入 Hash Set 以便 O(1) 查找
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int n = s.length();

        // dp[i] 代表前 i 個字元 (s[0...i-1]) 是否能被成功拆分
        vector<bool> dp(n + 1, false);
        dp[0] = true; // 空字串視為成功

        // 遍歷每一個結束位置 i (長度)
        for (int i = 1; i <= n; i++) {
            // 遍歷每一個分割點 j
            // 我們檢查 s[j...i-1] 是否是單字，以及前面的部分 s[0...j-1] (即 dp[j]) 是否可拆分
            for (int j = 0; j < i; j++) {
                if (dp[j]) { // 如果前半段沒問題，才檢查後半段
                    string sub = s.substr(j, i - j);
                    if (dict.count(sub)) {
                        dp[i] = true;
                        break; // 只要找到一種切法，i 這個位置就通了，不用繼續找 j
                    }
                }
            }
        }

        return dp[n];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^3)$ (Standard DP)
    -   Outer loop $N$, inner loop $N$. Substring generation and hashing takes $O(N)$. Total $O(N^3)$.
    -   Since $N=300$, $27 \times 10^6$ ops, which is acceptable.
-   **Space Complexity**: $O(N)$
    -   DP array.

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

### 進階挑戰
- [Word Break Ii](https://leetcode.com/problems/word-break-ii/) — LeetCode
