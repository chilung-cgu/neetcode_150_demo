---
title: "Valid Parenthesis String (有效的括號字串)"
description: "給定一個只包含 `(`, `)`, `*` 的字串。 檢查它是否為有效字串。 規則："
tags:
  - 
Greedy
difficulty: Medium
---

# Valid Parenthesis String (有效的括號字串) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #678** — [題目連結](https://leetcode.com/problems/valid-parenthesis-string/) | [NeetCode 解說](https://neetcode.io/problems/valid-parenthesis-string)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個只包含 `(`, `)`, `*` 的字串。
檢查它是否為有效字串。
規則：

1.  `(` 必須有對應的 `)`。
2.  `(` 必須在 `)` 之前。
3.  `*` 可以被視為 `(`, `)`, 或 空字串 `""`。

-   **Input**: `s = "()"`
-   **Output**: `true`
-   **Input**: `s = "(*)"`
-   **Output**: `true` (star as empty or "))
-   **Input**: `s = "(*))"`
-   **Output**: `true` (star as "(")
-   **Constraints**:
    -   $1 <= s.length <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion / Backtracking**:
對於每個 `*`，嘗試三種可能性：
`check(index, openCount)`

-   If '(': `check(index+1, openCount+1)`
-   If ')': `if openCount>0 check(index+1, openCount-1)`
-   If '*':
    -   `check(index+1, openCount+1)` (treat as '(')
    -   `if openCount>0 check(index+1, openCount-1)` (treat as ')')
    -   `check(index+1, openCount)` (treat as empty)
-   **Time**: $O(3^N)$

---

## 3. 💡 The "Aha!" Moment (優化)

這題可以用 Stack，也可以用 Greedy。
Greedy 的思路非常巧妙：
我們維護左括號數量的 **可能範圍 (Range)**：`[minOpen, maxOpen]`。
因為 `*` 的存在，導致左括號的剩餘數量不是一個定值，而是一個範圍。

-   遇到 `(`：`minOpen` 加 1， `maxOpen` 加 1。
-   遇到 `)`：`minOpen` 減 1， `maxOpen` 減 1。
-   遇到 `*`：
    -   如果當作 `)`：`minOpen` 減 1。
    -   如果當作 `(`：`maxOpen` 加 1。
    -   如果當作空：不變。
    -   綜合起來：`minOpen` 減 1 (最少可能情況)，`maxOpen` 加 1 (最多可能情況)。

在任何時候：

1.  如果 `maxOpen < 0`：說明即使把所有的 `*` 都當成左括號，也無法抵消右括號。這字串無效 (例如 `))((`)。Return False。
2.  如果 `minOpen < 0`：說明 `minOpen` 的假設太激進了 (把太多 `*` 當成右括號了)，但我們還有其他選擇 (把 `*` 當空或左)，所以我們只要把 `minOpen` 重置為 0 即可 (因為左括號數量不可能為負)。

遍歷結束後：
檢查 `minOpen == 0`。

-   如果 `minOpen == 0`，代表我們可以通過某種組合讓左括號剛好被抵消。
-   (注意：我們只關心是否 *包含* 0，而 `minOpen` 一旦被重置為 0，就代表 0 在範圍內)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../valid_parenthesis_string_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../valid_parenthesis_string_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Greedy Range

```cpp
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool checkValidString(string s) {
        int leftMin = 0; // Minimum possible open parentheses count
        int leftMax = 0; // Maximum possible open parentheses count

        for (char c : s) {
            if (c == '(') {
                leftMin++;
                leftMax++;
            } else if (c == ')') {
                leftMin--;
                leftMax--;
            } else { // c == '*'
                leftMin--; // Treat as ')'
                leftMax++; // Treat as '('
            }

            if (leftMax < 0) return false; // Too many ')'

            // leftMin cannot be negative (we can't have negative count of open parens)
            // If it goes negative, it just means treating * as ')' was not viable,
            // so we treat * as empty effectively resetting the lower bound to 0.
            if (leftMin < 0) leftMin = 0;
        }

        return leftMin == 0;
    }
};
```

### Python Reference

```python
class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0

        return leftMin == 0
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool checkValidString(string s) {
        // leftMin: 左括號數量的下界 (盡可能把 * 當成右括號)
        // leftMax: 左括號數量的上界 (盡可能把 * 當成左括號)
        int leftMin = 0;
        int leftMax = 0;

        for (char c : s) {
            if (c == '(') {
                leftMin++;
                leftMax++;
            } else if (c == ')') {
                leftMin--;
                leftMax--;
            } else { // c == '*'
                leftMin--; // 當成 ')'，讓左括號數變少
                leftMax++; // 當成 '(', 讓左括號數變多
            }

            // 如果上界都小於 0，代表把所有 * 都變成左括號也不夠抵消右括號
            // 必定無效 (e.g. "())")
            if (leftMax < 0) return false;

            // 下界如果小於 0，是不合理的 (左括號數量不能是負的)
            // 這代表我們把太多 * 當成右括號了，這條路行不通
            // 但因為 leftMax >= 0 (上面檢查過)，所以我們還有其他選擇 (把 * 當空字串)
            // 所以我們只要把下界重置為 0 即可 (最少就是 0 個左括號)
            if (leftMin < 0) leftMin = 0;
        }

        // 如果最終下界是 0，代表有一種情況可以剛好配對完畢
        return leftMin == 0;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   Only two variables.

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
- [01. Valid Parentheses](../04_Stack/01_Valid_Parentheses.md)
