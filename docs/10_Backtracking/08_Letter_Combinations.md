---
title: "Letter Combinations of a Phone Number (電話號碼的字母組合)"
description: "題目給一個包含數字 `2-9` 的字串 `digits`。 回傳這些數字在傳統手機鍵盤上可能代表的所有字母組合。"
tags:
  - Backtracking
  - Recursion
difficulty: Medium
---

# Letter Combinations of a Phone Number (電話號碼的字母組合) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #17** — [題目連結](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | [NeetCode 解說](https://neetcode.io/problems/letter-combinations-of-a-phone-number)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個包含數字 `2-9` 的字串 `digits`。
回傳這些數字在傳統手機鍵盤上可能代表的所有字母組合。

-   2: "abc"
-   3: "def"
-   4: "ghi"
-   5: "jkl"
-   6: "mno"
-   7: "pqrs"
-   8: "tuv"
-   9: "wxyz"

-   **Input**: `digits = "23"`
-   **Output**: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`
-   **Input**: `digits = ""`
-   **Output**: `[]`
-   **Constraints**:
    -   $0 <= digits.length <= 4$
    -   digits[i] is between '2' and '9'.

---

## 2. 🐢 Brute Force Approach (暴力解)

**Iterative / Recursive**:
這就是一個標準的決策樹問題。
第 0 層是第一個 digit 可能的字母，第 1 層是第二個 digit 可能的字母...

-   Time: $O(4^N \times N)$。每個數字最多對應 4 個字母 (7和9)。N 是 digits 長度。
-   $N \le 4$，所以非常非常快。

---

## 3. 💡 The "Aha!" Moment (優化)

Backtracking。
建立一個 lookup table (map or array)。

```
Map:
2 -> "abc"
3 -> "def"
...
9 -> "wxyz"
```

遞迴函數 `dfs(index, current_string)`:

-   如果 `index == digits.length`，加入結果。
-   否則，找出 `digits[index]` 對應的字母集合。
-   對每個字母，加入 `current_string`，遞迴，然後 Backtrack (pop)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../letter_combinations_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../letter_combinations_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking

```cpp
#include <vector>
#include <string>
#include <vector>

using namespace std;

class Solution {
    const vector<string> pad = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) {
            return {};
        }

        vector<string> result;
        string current;
        backtrack(digits, 0, current, result);
        return result;
    }

private:
    void backtrack(const string& digits, int index, string& current, vector<string>& result) {
        if (index == digits.length()) {
            result.push_back(current);
            return;
        }

        int digit = digits[index] - '0';
        const string& letters = pad[digit];

        for (char letter : letters) {
            current.push_back(letter);
            backtrack(digits, index + 1, current, result);
            current.pop_back();
        }
    }
};
```

### Python Reference

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        backtrack(0, "")
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
    // 建立映射表，index 對應 digit
    vector<string> mapping = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

public:
    vector<string> letterCombinations(string digits) {
        // 特判空字串，否則會回傳 [""] (含一個空字串的陣列)
        if (digits.empty()) return {};

        vector<string> res;
        string path;
        dfs(digits, 0, path, res);
        return res;
    }

    void dfs(const string& digits, int index, string& path, vector<string>& res) {
        // Base Case: 路徑長度等於數字長度，完成一組組合
        if (index == digits.size()) {
            res.push_back(path);
            return;
        }

        // 找出當前數字對應的字母字串
        int d = digits[index] - '0';
        string letters = mapping[d];

        // 遍歷每一個可能的字母
        for (char c : letters) {
            path.push_back(c);         // 選擇
            dfs(digits, index + 1, path, res); // 遞迴下一個數字
            path.pop_back();           // 回溯
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(4^N \times N)$
    -   $N$ is length of `digits`.
    -   Max digits map to 4 letters (7 and 9).
    -   So there are at most $4^N$ combinations.
    -   Constructing each string takes $O(N)$.
-   **Space Complexity**: $O(N)$
    -   Recursion stack depth $N$.

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
- [Combination Sum (組合總和)](02_Combination_Sum.md)
