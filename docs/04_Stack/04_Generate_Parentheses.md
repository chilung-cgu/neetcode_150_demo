---
title: "Generate Parentheses (生成括號)"
description: "題目給一個整數 `n`，代表有 `n` 對括號。 請生成所有 **格式正確 (Well-formed)** 的括號組合。"
tags:
  - 
Stack  - Monotonic Stack
difficulty: Medium
---

# Generate Parentheses (生成括號) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #22** — [題目連結](https://leetcode.com/problems/generate-parentheses/) | [NeetCode 解說](https://neetcode.io/problems/generate-parentheses)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數 `n`，代表有 `n` 對括號。
請生成所有 **格式正確 (Well-formed)** 的括號組合。

-   **Input**: `n = 3`
-   **Output**: `["((()))","(()())","(())()","()(())","()()()"]`
-   **Input**: `n = 1`
-   **Output**: `["()"]`
-   **Constraints**:
    -   $1 <= n <= 8$. (`n` 比較小，暗示我們可以用 recursion 或 backtracking 指數級算法)。

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試生成所有長度為 `2n` 的括號序列（每個位置放 `(` 或 `)`），然後驗證是否合法。

-   **Time**: $O(2^{2n} \cdot n)$。
-   **Result**: 非常慢。對於 `n=8`， $2^{16} = 65536$，還行，但明顯不是面試要的。

---

## 3. 💡 The "Aha!" Moment (優化)

**Backtracking (回溯法)**：我們只生成 **可能合法** 的路徑，一旦發現不可能合法就停下來。

如何保證合法？我們維護兩個計數器：

1.  `open`: 目前已經放了多少個左括號 `(`。
2.  `close`: 目前已經放了多少個右括號 `)`。

決策樹的規則：

1.  **Add Open**: 隨時可以放左括號，只要 `open < n`。
2.  **Add Close**: 只有當 `close < open` 時，才能放右括號。
    -   這保證了我們不會生成如 `())` 這種非法前綴。
3.  **Base Case**: 當 `open == n` 且 `close == n` 時，我們找到了一個完整且合法的組合，加入結果集。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../generate_parentheses_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../generate_parentheses_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Backtracking

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string current;
        backtrack(n, 0, 0, current, result);
        return result;
    }

private:
    void backtrack(int n, int open, int close, string& current, vector<string>& result) {
        // Base case: 長度達到 2n (或者 open == n && close == n)
        if (current.length() == n * 2) {
            result.push_back(current);
            return;
        }

        // Decision 1: Add Open
        if (open < n) {
            current.push_back('(');
            backtrack(n, open + 1, close, current, result);
            current.pop_back(); // Backtrack
        }

        // Decision 2: Add Close
        if (close < open) {
            current.push_back(')');
            backtrack(n, open, close + 1, current, result);
            current.pop_back(); // Backtrack
        }
    }
};
```

### Python Reference

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        string wString; // working string

        // Start recursion
        generate(n, 0, 0, wString, res);

        return res;
    }

private:
    // Helper function for backtracking
    // n: 總對數
    // open: 目前已放置的左括號數
    // close: 目前已放置的右括號數
    void generate(int n, int open, int close, string& s, vector<string>& res) {

        // 成功條件：左右括號都放滿了
        if (open == n && close == n) {
            res.push_back(s);
            return;
        }

        // 規則 1: 只要左括號還沒滿，就能放左括號
        if (open < n) {
            s.push_back('(');
            generate(n, open + 1, close, s, res);
            s.pop_back(); // 關鍵：遞迴回來後要還原狀態 (Backtracking)
        }

        // 規則 2: 只有當右括號數量小於左括號時，才能放右括號
        // 這保證了括號的閉合是合法的，不會出現 "())"
        if (close < open) {
            s.push_back(')');
            generate(n, open, close + 1, s, res);
            s.pop_back(); // Backtrack
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\frac{4^n}{\sqrt{n}})$
    -   這是一個特殊的數學序列，稱為 **Catalan Number** (卡塔蘭數)。
    -   第 `n` 個卡塔蘭數是 $\frac{1}{n+1}\binom{2n}{n}$。
    -   簡單來說，這是指數級別的，但比 $2^{2n}$ 小很多。
-   **Space Complexity**: $O(n)$
    -   Recursion stack depth 是 $2n$ (最大字串長度)。
    -   Output space 不算。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如何枚舉所有 BST 結構？
- Catalan Number?

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 剪枝條件錯誤
- ⚠️ 沒有維護 open/close 計數

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 清晰的遞迴終止條件
- 💎 解釋 Catalan Number

---

## 📚 Related Problems (相關題目)

### 站內相關
- [01. Valid Parentheses](01_Valid_Parentheses.md)
- [Subsets (子集)](../10_Backtracking/01_Subsets.md)
