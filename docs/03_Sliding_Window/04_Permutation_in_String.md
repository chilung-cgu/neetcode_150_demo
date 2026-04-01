---
title: "Permutation in String (字串的排列包含)"
description: "題目給兩個字串 `s1` 和 `s2`。請判斷 `s2` 是否包含 `s1` 的任意 **Permutation** (排列組合) 作為子字串。"
tags:
  - Sliding Window
  - String
difficulty: Medium
---

# Permutation in String (字串的排列包含) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #567** — [題目連結](https://leetcode.com/problems/permutation-in-string/) | [NeetCode 解說](https://neetcode.io/problems/permutation-string)


## 1. 🧐 Problem Dissection (釐清問題)

題目給兩個字串 `s1` 和 `s2`。請判斷 `s2` 是否包含 `s1` 的任意 **Permutation** (排列組合) 作為子字串。

- **Input**: `s1 = "ab", s2 = "eidbaooo"`
- **Output**: `true` (`s2` contains "ba", which is a permutation of "ab").
- **Input**: `s1 = "ab", s2 = "eidboaoo"`
- **Output**: `false`.
- **Key Insight**: 如果 `sub` 是 `s1` 的 permutation，那麼它們必須有 **完全相同的字元頻率 (Character Frequency)**。長度也必須相同。
- **Constraints**:
  - $1 <= s1.length, s2.length <= 10^4$.
  - 只包含小寫英文字母。

---

## 2. 🐢 Brute Force Approach (暴力解)

找出 `s1` 的所有排列組合（$n!$ 種），然後在 `s2` 裡找。

- **Time**: $O(n! \cdot m)$。
- **Result**: 絕對 TLE。 `100!` 是天文數字。

---

## 3. 💡 The "Aha!" Moment (優化)

這其實是 **Fixed Size Sliding Window** 的問題。

1.  我們有一個固定長度的窗口，大小等於 `s1.length()`。
2.  這窗口在 `s2` 上滑動。
3.  在每一個時刻，我們檢查 **當前窗口內的字元計數** 是否等於 **`s1` 的字元計數**。

- **Naive Window Check**: 每次移動窗口都要比較兩個長度 26 的 array。
  - Total Time: $O(26 \cdot n)$。因為 $26$ 是常數，所以這已經是 $O(n)$ 了。
- **Optimized Window Check**:
  - 我們可以維護一個 `matches` 變數 (0 到 26)。
  - 當我們 slide window 時，只有一個字元進，一個字元出。
  - 我們只更新變動的這兩個字元的 count，並看它們是否導致 `matches` 增加或減少。
  - 如果 `matches == 26`，return true。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../permutation_string_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../permutation_string_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Sliding Window with Matches Count

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.length() > s2.length()) return false;

        vector<int> s1Count(26, 0);
        vector<int> s2Count(26, 0);

        // 初始化第一個窗口 (長度為 s1.length())
        for (int i = 0; i < s1.length(); i++) {
            s1Count[s1[i] - 'a']++;
            s2Count[s2[i] - 'a']++;
        }

        // 計算初始 matches
        int matches = 0;
        for (int i = 0; i < 26; i++) {
            if (s1Count[i] == s2Count[i]) matches++;
        }

        int l = 0;
        // 開始滑動 (從 s1.length 開始)
        for (int r = s1.length(); r < s2.length(); r++) {
            if (matches == 26) return true;

            // Add new char (s2[r])
            int index = s2[r] - 'a';
            s2Count[index]++;
            if (s2Count[index] == s1Count[index]) {
                matches++; // 剛好補齊
            } else if (s2Count[index] == s1Count[index] + 1) {
                matches--; // 原本剛好，現在多了
            }

            // Remove old char (s2[l])
            index = s2[l] - 'a';
            s2Count[index]--;
            if (s2Count[index] == s1Count[index]) {
                matches++; // 剛好減回來
            } else if (s2Count[index] == s1Count[index] - 1) {
                matches--; // 原本剛好，現在少了
            }
            l++;
        }

        return matches == 26;
    }
};
```

### Simple Approach (O(26\*n))

雖然 `matches` 優化很酷，但在面試有時容易寫錯。直接比較 `vector` 其實夠快了。

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        vector<int> s1Map(26, 0), s2Map(26, 0);

        for (char c : s1) s1Map[c - 'a']++;

        int left = 0;
        int right = 0;

        while (right < s2.size()) {
            s2Map[s2[right] - 'a']++;

            // 窗口大於 s1 長度時，收縮左邊
            if (right - left + 1 > s1.size()) {
                s2Map[s2[left] - 'a']--;
                left++;
            }

            // 檢查是否相等
            if (s1Map == s2Map) return true;

            right++;
        }
        return false;
    }
};
```

### Python Reference

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們用 Simple Approach 的寫法，因為它最易讀且效能差別微乎其微。

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size();
        int m = s2.size();

        if (n > m) return false;

        // 建立目標頻率表
        vector<int> target(26, 0);
        for (char c : s1) target[c - 'a']++;

        // 建立當前窗口頻率表
        vector<int> window(26, 0);

        // 先處理前 n-1 個元素 (如果不夠 n 個就不用比了)
        // 這裡我們選擇直接用完整的 sliding window logic

        int l = 0;
        for (int r = 0; r < m; r++) {
            // 把右邊元素加入窗口
            window[s2[r] - 'a']++;

            // 如果窗口寬度超過 n，把左邊元素移出
            if (r - l + 1 > n) {
                window[s2[l] - 'a']--;
                l++;
            }

            // 檢查匹配
            // vector 的 == operator 會比較所有元素，時間複雜度 O(26) -> O(1)
            if (window == target) return true;
        }

        return false;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(26 \cdot n)$ or $O(n)$
  - 我們遍歷 `s2` 一次。
  - 每次迭代比較兩個長度 26 的 vector。
  - $26$ 是常數，所以是線性時間 $O(n)$。
- **Space Complexity**: $O(1)$
  - 只用了長度 26 的 vector。

**Comparison**:
這題跟 **Valid Anagram** 很像，只是 Anagram 是全域比較，這裡是局部窗口比較。
這題又跟 **Find All Anagrams in a String** (LeetCode 438) 完全一樣，只是那題要回傳所有 index，這題只要 boolean。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- Find All Anagrams in a String?
- 如何處理 Unicode？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 窗口大小不固定
- ⚠️ 比較兩個頻率表方式低效

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 使用 matches 計數器優化
- 💎 固定大小滑動窗口

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Minimum Window Substring (最小覆蓋子字串)](05_Minimum_Window_Substring.md)

### 進階挑戰
- [Find All Anagrams In A String](https://leetcode.com/problems/find-all-anagrams-in-a-string/) — LeetCode
