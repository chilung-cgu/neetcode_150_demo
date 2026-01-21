---
title: "Longest Substring Without Repeating Characters (無重複字元的最長子字串)"
description: "題目給一個字串 `s`，請找出**不包含重複字元**的**最長子字串**的長度。"
tags:
  - 
Sliding Window  - String
difficulty: Medium
---

# Longest Substring Without Repeating Characters (無重複字元的最長子字串) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #3** — [題目連結](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [NeetCode 解說](https://neetcode.io/problems/longest-substring-without-repeating-characters)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串 `s`，請找出**不包含重複字元**的**最長子字串**的長度。

- **Input**: `"abcabcbb"`
- **Output**: `3` ("abc")
- **Input**: `"pwwkew"`
- **Output**: `3` ("wke", 注意 "pwke" 有兩個 w，所以不行)
- **Wrong Example**: `"subsequence"` vs `"substring"`. 題目要的是連續的 substring，不是跳著選的 subsequence。
- **Constraints**:
  - $0 <= s.length <= 5 * 10^4$.
  - 包含 ASCII 字元 (所以不只是小寫字母)。

---

## 2. 🐢 Brute Force Approach (暴力解)

枚舉所有子字串 `s[i...j]`，檢查它是否有重複字元。

- **Time**: Total substrings $O(n^2)$。Check duplicate $O(n)$。Total $O(n^3)$。
- **Space**: $O(min(n, m))$ for set。
- **Result**: TLE。

---

## 3. 💡 The "Aha!" Moment (優化)

這題是 **Sliding Window** 最經典的入門題。

我們用一個窗口 `[left, right]` 來代表當下的子字串。

1.  **Expand**: 不斷移動 `right` 指標，擴大窗口，把新字元加進來。
2.  **Check**: 如果新加進來的字元 `s[right]` **已經存在於窗口中**，這時窗口內的內容就非法了 (有重複)。
3.  **Shrink**: 我們需要移動 `left` 指標，把窗口左邊的字元踢出去，直到沒有重複為止。
    - 例如視窗是 `"abca"` (遇到第二個 'a')。
    - 我們必須踢掉第一個 `'a'`，變成 `"bca"`，才恢復合法。
4.  **Update**: 在每次窗口合法時，更新最大長度 `maxLen = max(maxLen, right - left + 1)`。

為了快速檢查「是否存在窗口中」，我們需要一個 **Hash Set** (或者 Array 如果是 ASCII)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../longest_substring_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../longest_substring_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Sliding Window + Hash Set

```cpp
#include <string>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> charSet;
        int left = 0;
        int maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            // 如果 s[right] 已經存在，說明重複了。
            // 我們需要持續縮小窗口 (移動 left)，直到 s[right] 不在 set 中為止。
            while (charSet.find(s[right]) != charSet.end()) {
                charSet.erase(s[left]);
                left++;
            }

            // 加入當前字元
            charSet.insert(s[right]);

            // 更新最大長度
            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
```

### Approach: Optimized Sliding Window (Map)

如果我們用 Hash Map 記錄每個字元**上一次出現的索引 (index)**，我們可以不用一步一步 `left++`，而是直接跳過所有重複區間。
例如 `"...a...a"`，當遇到第二個 `a` 時，我們可以把 `left` 直接移到 `last_index_of_a + 1`。

```cpp
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 使用 vector 代替 map，index 是 ASCII 值，value 是該字元上次出現的 index
        vector<int> lastIndex(128, -1);
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s[right];

            // 如果 c 曾經出現過，且出現的位置在 left 之後 (在當前窗口內)
            if (lastIndex[c] >= left) {
                // 直接跳到那個重複字的下一位
                left = lastIndex[c] + 1;
            }

            // 更新這個字最後出現的位置為 right
            lastIndex[c] = right;

            maxLen = max(maxLen, right - left + 1);
        }

        return maxLen;
    }
};
```

### Python Reference

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們來看一般的 Set 解法，這是最通用且面試最容易解釋的。

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // 使用 Hash Set 來記錄當前窗口內的 unique characters
        unordered_set<char> window;
        int left = 0;
        int maxL = 0;

        // right 指標負責擴張窗口
        for (int right = 0; right < s.length(); right++) {
            // Check condition: 我們要加入 s[right]，但如果它已存在...
            while (window.count(s[right])) {
                // Shrink: 從左邊縮小窗口，直到把那個重複的字元踢出去為止
                // 例如 "abca"，現在遇到 a (index 3)，set 裡有 a (index 0)
                // 我們必須先把 s[0] 移除，left 變成 1 ("bca")，這樣 set 裡就沒有 a 了
                window.erase(s[left]);
                left++;
            }

            // 現在窗口安全了，把 s[right] 加進去
            window.insert(s[right]);

            // 記錄當前長度
            maxL = max(maxL, right - left + 1);
        }

        return maxL;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(n)$
  - 雖然有 `while` loop，但 `left` 和 `right` 都只會從 0 走到 n。每個字元最多被 `insert` 一次、`erase` 一次。總運算量 $2n$。
- **Space Complexity**: $O(min(n, m))$
  - $m$ 是字元集大小 (ASCII 128)。Set 最多存這麼多字。
  - 所以實際上是 $O(1)$ 如果 char set 固定。

---

## 7. 💼 Interview Tips (面試技巧) ⭐ 高頻題

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果只算字母呢？
- 如何處理 Unicode？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 滑動窗口邊界更新錯誤
- ⚠️ map 沒有正確更新字元位置

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 使用固定大小陣列優化
- 💎 清晰的窗口收縮條件

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Longest Repeating Character Replacement (替換後的最長重複字元子串)](03_Longest_Repeating_Character_Replacement.md)
