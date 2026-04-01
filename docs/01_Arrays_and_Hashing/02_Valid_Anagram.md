---
title: "Valid Anagram (有效的易位構詞)"
description: "題目要求判斷兩個字串 `s` 和 `t` 是否為彼此的重組字 (Anagram)。也就是說，它們必須包含完全相同的字元，且每個字元的出現次數也必須相同。"
tags:
  - Array
  - Hash Table
difficulty: Easy
---

# Valid Anagram (有效的易位構詞) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #242** — [題目連結](https://leetcode.com/problems/valid-anagram/) | [NeetCode 解說](https://neetcode.io/problems/is-anagram)


## 1. 🧐 Problem Dissection (釐清問題)

題目要求判斷兩個字串 `s` 和 `t` 是否為彼此的重組字 (Anagram)。也就是說，它們必須包含完全相同的字元，且每個字元的出現次數也必須相同。

- **Input Constraints**: 字串只包含小寫英文字母嗎？(題目通常說是，但確認 Unicode/ASCII 總是加分題)。
  - _長度檢查_：如果 `s.length() != t.length()`，直接回傳 `false`。這是最快的 check。
- **Follow-up**: "What if the inputs contain Unicode characters?" (例如中文)。這時 `vector<int>(26)` 就不夠用了，需要 `unordered_map`。

---

## 2. 🐢 Brute Force Approach (暴力解)

最簡單的想法：如果兩個字串是 Anagram，那它們排序後應該長得一模一樣。

```cpp
bool isAnagram(string s, string t) {
    if (s.length() != t.length()) return false;
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    return s == t;
}
```

- **Time Complexity**: $O(n \log n)$，被 Sorting 主導。
- **Space Complexity**: $O(1)$ 或 $O(\log n)$ (視 sort 實作而定)。
- **評論**: 雖然不是最佳解，但在字串很短的情況下，這寫法最乾淨、最不容易寫出 Bug。

---

## 3. 💡 The "Aha!" Moment (優化)

我們真的需要排序嗎？我們在乎的只是「每個字母出現了幾次」。
比如 `s = "aab", t = "baa"`。
`s`: a->2, b->1
`t`: a->2, b->1
Match!

**思路引導**:

1.  **Hash Map (Generic Approach)**: 用兩個 Map 分別統計，最後比對 Map。
    - Cost: $O(n)$ Time, $O(n)$ Space (如果字元集很大)。
2.  **Frequency Array (Optimized for lowercase English)**:
    - 因為只有 26 個小寫字母，我們可以用一個大小為 26 的整數陣列來代替 Map。
    - Index 0 代表 'a', Index 1 代表 'b'...
    - 我們不需要兩個 Array。遍歷 `s` 時 `+1`，遍歷 `t` 時 `-1`。最後檢查 Array 是否全為 0。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../valid_anagram_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../valid_anagram_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### approach 1: Frequency Array (Best for interview)

```cpp
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        // 優化 1: 長度不同直接 return
        if (s.length() != t.length()) return false;

        // Space: O(1) 因為固定 26 大小
        int count[26] = {0};

        // Time: O(n)
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++; // s 負責加
            count[t[i] - 'a']--; // t 負責減
        }

        // 檢查是否完全抵銷
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return false;
        }

        return true;
    }
};
```

### Approach 2: Unicode Support (Follow-up)

如果變成了 Unicode，Array[26] 就不能用了，改用 `unordered_map`。

```cpp
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;

        unordered_map<char, int> count;

        for (char c : s) count[c]++;
        for (char c : t) {
            if (count.find(c) == count.end() || count[c] == 0) {
                return false; // t 有 s 沒有的，或是 t 的該字元比 s 多
            }
            count[c]--;
        }

        return true;
    }
};
```

### Python Reference

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
        # 或者直接: return Counter(s) == Counter(t)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們來看 C++ 的 Frequency Array 解法細節。

```cpp
class Solution {
public:
    bool isAnagram(string s, string t) {
        // Boundary check 是好習慣。
        if (s.length() != t.length()) return false;

        // 使用 vector 初始化為 0，也可以用 int count[26] = {0};
        // 在 C++ 中，stack memory (array) 比 heap memory (vector) 稍微快一點點且不需 allocation，
        // 但 vector 更安全。這裡既然是固定 26，array 也是很棒的選擇。
        vector<int> count(26, 0);

        for (int i = 0; i < s.length(); i++) {
            // 's[i] - 'a'' 利用 ASCII code 的順序性將 char 映射到 0-25
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        // 必須再次遍歷 count array 確認歸零
        for (int c : count) {
            if (c != 0) return false;
        }

        return true;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

### Frequency Array Approach

- **Time Complexity**: $O(n)$
  - $n$ 是字串長度。我們遍歷字串一次，再遍歷 Array (26次)，所以是 $O(n + 26) \approx O(n)$。
- **Space Complexity**: $O(1)$
  - 雖然我們用了額外空間，但這個空間大小是固定的 (26)，不隨 $n$ 增長而變大。
  - 嚴格來說是 $O(\Sigma)$，其中 $\Sigma$ 是字元集大小。

### Sorting Approach

- **Time Complexity**: $O(n \log n)$
- **Space Complexity**: $O(1)$ 或 $O(\log n)$

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如果輸入包含 Unicode 字元？
- 如果字串非常長，有更快的方法嗎？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 忘記考慮大小寫敏感
- ⚠️ 沒有處理空字串

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 提到排序解法的 trade-off
- 💎 討論固定大小陣列 vs Hash Map

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Contains Duplicate (存在重複元素)](01_Contains_Duplicate.md)
- [Group Anagrams (字母異位詞分組)](04_Group_Anagrams.md)
