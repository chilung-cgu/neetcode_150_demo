---
title: "Group Anagrams (字母異位詞分組)"
description: "題目給我們一個字串陣列 `strs`，要求我們將所有的 **Anagrams** (字母異位詞) 分組在一起。順序不重要。"
tags:
  - Array
  - Hash Table
difficulty: Medium
---

# Group Anagrams (字母異位詞分組) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #49** — [題目連結](https://leetcode.com/problems/group-anagrams/) | [NeetCode 解說](https://neetcode.io/problems/anagram-groups)


## 1. 🧐 Problem Dissection (釐清問題)

題目給我們一個字串陣列 `strs`，要求我們將所有的 **Anagrams** (字母異位詞) 分組在一起。順序不重要。

- **Input**: `["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Output**: `[["bat"], ["nat","tan"], ["ate","eat","tea"]]`
- **Core Definition**: Anagram 意味著「排序後相同」或是「字元計數相同」。
- **Constraints**:
  - `strs` 長度可達 $10^4$。
  - `strs[i]` 長度可達 100。
  - 只包含小寫英文字母。

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每一個字串，去掃描剩下的字串，看是不是 Anagram。
如果是，就放進同一組，並標記為已處理。

- **Time Complexity**: $O(m^2 \cdot n)$，其中 $m$ 是字串數量，$n$ 是平均長度。
- **問題**: $m$ 很大 ($10^4$)，$m^2 = 10^8$，即使 $n$ 很小，這個解法也會在邊緣或稍微超時。而且寫起來很麻煩 (需要 `visited` array)。

---

## 3. 💡 The "Aha!" Moment (優化)

我們需要一個方法來為每一組 Anagram 找到一個 **"代表" (Key)**。
所有屬於同一組的 Anagram，算出來的 Key 必須一樣。

**候選 Key**:

1.  **Sorted String**:
    - "eat" -> sort -> "aet"
    - "tea" -> sort -> "aet"
    - "ate" -> sort -> "aet"
    - 大家 Key 都一樣，可以用 Hash Map 歸類！
    - **Cost**: 計算 Key 需要 $O(n \log n)$。總時間 $O(m \cdot n \log n)$。

2.  **Frequency Count (Hashable)**:
    - 用一個 tuple 或者 string 來表示計數：`"1#0#0#0#1..."` (表示 1個a, 0個b...)
    - **Cost**: 計算 Key 需要 $O(n)$。總時間 $O(m \cdot n)$。
    - **缺點**: C++ 的 `unordered_map` default 不支援 `vector<int>` 當 Key，需要自定義 Hasher，稍微麻煩一點。

**Decision**:
在面試中，**Sorted String** 是最直觀且容易實作的方法。$n$ (字串長度) 通常不大 (題目說是 100)，所以 $n \log n$ 跟 $n$ 差異有限。我們會先採用 Sorted String 方法。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../group_anagrams_visualizer.html" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" 
            loading="lazy">
    </iframe>
</div>
<p style="text-align: right; margin-top: 8px;">
    <a href="../group_anagrams_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;">
        <span>⤢</span> 全螢幕開啟視覺化
    </a>
</p>

---

## 4. 💻 Implementation (程式碼)

### Approach 1: Categorize by Sorted String (Recommended)

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Key: 排序後的字串 (e.g., "aet")
        // Value: 原始字串的列表 (e.g., ["eat", "tea", "ate"])
        unordered_map<string, vector<string>> groups;

        for (string s : strs) {
            string key = s;
            sort(key.begin(), key.end()); // 產生 Key: O(n log n)
            groups[key].push_back(s);     // 歸類: O(1) assuming string hash is fast
        }

        // 轉換 Map 到 Vector
        vector<vector<string>> result;
        // Optimization: reserve 避免 realloc
        result.reserve(groups.size());

        for (auto& pair : groups) {
            result.push_back(move(pair.second)); // move 避免 copy，這是 C++ 的精隨
        }

        return result;
    }
};
```

### Approach 2: Categorize by Count (Optimized for very long strings)

如果字串非常長 (e.g., $n > 1000$)，Sorting 的代價會變高。這時可以用 Count Array。
但在 C++ 中，`map<vector<int>, ...>` (Tree Map) 會增加 $O(\log m)$ 的 lookup，而 `unordered_map` 需要自定義 hasher。這裡為了簡潔展示 Python 的版本，因為 Python 的 tuple 是 hashable 的。

### Python Reference

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            # list 不能當 dict key, 但 tuple 可以
            ans[tuple(count)].append(s)

        return list(ans.values())
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // 使用 unordered_map 進行分組，這是典型的 Hash Map 應用
        unordered_map<string, vector<string>> mp;

        // 遍歷每一個字串
        for (auto& s : strs) {
            // copy 一份出來做 sorting 當作 key
            string t = s;

            // 排序後，所有 anagrams 應該都長得一樣
            // e.g. "nat" -> "ant", "tan" -> "ant"
            sort(t.begin(), t.end());

            // 將原始字串 s 放入對應的 key 下
            mp[t].push_back(s);
        }

        vector<vector<string>> anagrams;
        anagrams.reserve(mp.size()); // 小優化：預先分配空間

        // 遍歷 map，將 value (vector<string>) 取出
        for (auto& p : mp) {
            // map 的元素是 pair<Key, Value>，所以 p.second 就是我們要的 vector<string>
            // 使用 std::move 可以避免 deep copy vector，極大提升效能
            anagrams.push_back(move(p.second));
        }

        return anagrams;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

### Sorted String Approach

- **Time Complexity**: $O(m \cdot n \log n)$
  - $m$ 是字串總數，$n$ 是字串最大長度。
  - 對每個字串 sort 需要 $n \log n$。
  - 總共有 $m$ 個字串。
- **Space Complexity**: $O(m \cdot n)$
  - 我們需要儲存所有的字串在 Map 中。

### Count Approach (Python version)

- **Time Complexity**: $O(m \cdot n)$
  - 對每個字串只需一次遍歷 ($n$) 來計算 count。
- **Space Complexity**: $O(m \cdot n)$ / $O(m \cdot 26)$

**結論**:
考慮到 $n$ 很小 (<= 100)，$n \log n$ 跟 $n$ 差距不大。C++ 的 Sorting 實作非常快 (Introsort)，加上 `std::string` 短字串優化 (SSO)，Sorting 方法通常在實際運行時表現極佳且程式碼最簡潔。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如何處理 Unicode？
- 有比排序更快的 Hash Key 嗎？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ Key 設計不當導致碰撞
- ⚠️ 忘記初始化結果容器

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 討論排序 vs 計數陣列作為 Key
- 💎 時間複雜度分析完整

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Valid Anagram (有效的易位構詞)](02_Valid_Anagram.md)
