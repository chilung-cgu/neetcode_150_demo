---
title: "Evaluate Reverse Polish Notation (逆波蘭表達式求值)"
description: "題目給一個字串陣列 `tokens`，代表一個 **RPN (Reverse Polish Notation)** 表達式。請計算它的值。 RPN (Postfix Notation) 的特點是運算子在運算元後面。例如 `2 + 1` 寫成 `2 1 +`。"
tags:
  - Stack
  - Monotonic Stack
difficulty: Medium
---

# Evaluate Reverse Polish Notation (逆波蘭表達式求值) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #150** — [題目連結](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | [NeetCode 解說](https://neetcode.io/problems/evaluate-reverse-polish-notation)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個字串陣列 `tokens`，代表一個 **RPN (Reverse Polish Notation)** 表達式。請計算它的值。
RPN (Postfix Notation) 的特點是運算子在運算元後面。例如 `2 + 1` 寫成 `2 1 +`。

-   **Operators**: `+`, `-`, `*`, `/`.
-   **Division**: 整數除法，向零取整 (Truncate toward zero)。例如 `-3 / 2 = -1`。
-   **Input**: `["2","1","+","3","*"]` -> `((2 + 1) * 3)` -> `9`
-   **Input**: `["4","13","5","/","+"]` -> `(4 + (13 / 5))` -> `4 + 2` -> `6`
-   **Constraints**:
    -   $1 <= tokens.length <= 10^4$.
    -   Expression is always valid.
    -   結果與中間值都可以用 32-bit integer 表示。

---

## 2. 🐢 Brute Force Approach (暴力解)

RPN 本身就是為了方便電腦計算而設計的，所以直接模擬它的計算過程就是最佳解。這題很難說有什麼「暴力解」，除非你硬要把 RPN 轉回 Infix 然後再 Parse 一次，那樣更慢且多此一舉。

---

## 3. 💡 The "Aha!" Moment (優化)

使用 **Stack**。

邏輯：

1.  遍歷 `tokens`。
2.  如果是 **數字**：
    -   Push 進 Stack。
3.  如果是 **運算子** (`+`, `-`, `*`, `/`)：
    -   從 Stack Pop 出兩個數字。
    -   注意順序：第一次 Pop 出的是 **右運算元 (b)**，第二次是 **左運算元 (a)**。
    -   執行 `a op b`。
    -   將結果 Push 回 Stack。
4.  最後 Stack 裡剩下的一個數字就是答案。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../rpn_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../rpn_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Stack

```cpp
#include <vector>
#include <string>
#include <stack>
#include <stoi> // C++11

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;

        for (const string& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                // Pop right operand first!
                int b = s.top(); s.pop();
                int a = s.top(); s.pop();

                if (token == "+") s.push(a + b);
                else if (token == "-") s.push(a - b);
                else if (token == "*") s.push(a * b); // 注意 overflow，但題目保證 fit int
                else if (token == "/") s.push(a / b);
            } else {
                // Is number
                s.push(stoi(token));
            }
        }

        return s.top();
    }
};
```

### Python Reference

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                # Python division truncates differently for negative numbers
                # int() cast truncates toward zero exactly like C++
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stk;

        for (const string& t : tokens) {
            // 判斷是否為運算子
            // 小技巧：如果 string 長度大於 1，那肯定是負數或數字 (因為運算子只有 1 char)
            // 所以我們可以先 check size
            if (t.size() > 1 || isdigit(t[0])) {
                // 處理負數情況 e.g. "-11"
                // isdigit('-') is false, so checking size>1 handles negatives
                // 不過 "-1" 也是 size > 1。
                // 唯一例外是單個負號 "-" 作為運算子。
                // 所以最簡單是用 string 比較運算子
                stk.push(stoi(t));
                continue;
            }

            // 這裡一定是運算子 +, -, *, /
            // 因為題目保證 Valid，所以 stack 一定至少有兩個數
            int right = stk.top(); stk.pop();
            int left = stk.top(); stk.pop();

            long long res = 0; // 防止中間運算溢位，雖然題目說 int 夠用，但保險
            if (t == "+") res = (long long)left + right;
            else if (t == "-") res = (long long)left - right;
            else if (t == "*") res = (long long)left * right;
            else if (t == "/") res = left / right; // C++ 除法向 0 取整，符合題目

            stk.push((int)res);
        }

        return stk.top();
    }

    // 輔助判斷是否為數字 (雖然上面用了更簡單的邏輯)
    bool is_number(const string& s) {
        return (s.size() > 1) || isdigit(s[0]);
    }
};
```

**修正 `isdigit` 邏輯**:
`t == "-11"`: `size > 1`, OK.
`t == "-"`: `size == 1`, `isdigit('-')` is false. OK (operator).
`t == "1"`: `size == 1`, `isdigit('1')` is true. OK (number).
所以判斷邏輯：
```cpp
if (t == "+" || t == "-" || t == "*" || t == "/") {
    // operator logic
} else {
    // number logic
}
```
這是最乾淨的。

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   遍歷 tokens 一次。
    -   每個 token 處理時間 $O(1)$ (push or pop+compute)。
-   **Space Complexity**: $O(n)$
    -   Stack 大小。在最壞情況下 (例如先給一堆數字再給一堆運算子)，Stack 存 $\approx n/2$ 個數字。

---

## 7. 💼 Interview Tips (面試技巧)

### 🎯 Follow-up 問題

面試官可能會問的延伸問題：

- 如何從中綴轉後綴？
- 如何處理更多運算符？

### 🚩 常見錯誤 (Red Flags)

避免這些會讓面試官扣分的錯誤：

- ⚠️ 除法順序錯誤 (a/b vs b/a)
- ⚠️ 整數除法截斷方向

### ✨ 加分項 (Bonus Points)

這些會讓你脫穎而出：

- 💎 解釋 RPN 的優勢
- 💎 完整的運算符處理

---

## 📚 Related Problems (相關題目)

### 站內相關

### 進階挑戰
- [Basic Calculator](https://leetcode.com/problems/basic-calculator/) — LeetCode
