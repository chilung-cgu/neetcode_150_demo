---
title: "Sum of Two Integers (兩整數之和)"
description: "給定兩個整數 `a` 和 `b`，請在 **不使用 `+` 和 `-` 運算符** 的情況下計算它們的和。"
tags:
  - 
Bit Manipulation
difficulty: Medium
---

# Sum of Two Integers (兩整數之和) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #371** — [題目連結](https://leetcode.com/problems/sum-of-two-integers/) | [NeetCode 解說](https://neetcode.io/problems/sum-of-two-integers)


## 1. 🧐 Problem Dissection (釐清問題)

給定兩個整數 `a` 和 `b`，請在 **不使用 `+` 和 `-` 運算符** 的情況下計算它們的和。

-   **Input**: `a = 1, b = 2`
-   **Output**: `3`
-   **Input**: `a = -2, b = 3`
-   **Output**: `1`

---

## 2. 🐢 Brute Force Approach (暴力解)

這題禁止使用加減法，所以必須使用位運算來模擬加法電路（半加器/全加器）。

---

## 3. 💡 The "Aha!" Moment (優化)

**Bit Manipulation (Full Adder Logic)**:
加法可以分為兩部分：

1.  **無進位加法 (Sum without carry)**: 使用 `XOR` ($a \oplus b$)。
    -   $0+0=0, 1+0=1, 0+1=1, 1+1=0$。這正是 XOR 的行為。
2.  **進位 (Carry)**: 使用 `AND` ($a \& b$) 然後左移一位 (`<< 1`)。
    -   只有當 $1+1$ 時才會產生進位。
    -   $1 \& 1 = 1$，左移變為 $10$（加到下一位）。

**Algorithm**:
循環直到進位為 0：

-   `sum = a ^ b`
-   `carry = (a & b) << 1`
-   `a = sum`
-   `b = carry`
回傳 `a`。

**Special Handling for Python**:
Python 的整數是無限精度的，所以負數的二進制表示（2的補碼）會呈現出無限長的 1。
例如 -1 是 `...11111`。
在 C++/Java 中，整數固定 32 位，溢出會自動截斷（Wrap around），這正是我們想要的。
Python 中需要手動處理 32 位溢出掩碼 (`0xFFFFFFFF`)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../sum_two_integers_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../sum_two_integers_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Bit Manipulation

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        while (b != 0) {
            // Calculate carry (unsigned to avoid overflow issues with left shift on negative numbers)
            int carry = (unsigned int)(a & b) << 1;

            // Calculate sum without carry
            a = a ^ b;

            // Update b to be the carry, process in next iteration
            b = carry;
        }
        return a;
    }
};
```

### Python Reference

```python
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF // 32-bit mask

        while b != 0:
            # Calculate sum without carry
            tmp = (a ^ b) & mask
            # Calculate carry
            carry = ((a & b) << 1) & mask

            a = tmp
            b = carry

        # If a is negative (highest bit is 1), convert to Python's negative format
        if a > 0x7FFFFFFF:
            a = ~(a ^ mask)

        return a
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int getSum(int a, int b) {
        // 重複直到沒有進位 (b == 0)
        while (b != 0) {
            // 1. 計算進位
            // 當兩位都是 1 時產生進位 (a & b)
            // 進位是要加到下一位的，所以左移 1 位 (<< 1)
            // 使用 unsigned int 強制轉型是為了避免在負數左移時觸發 Undefined Behavior (雖然在大多數現代編譯器上沒問題)
            int carry = (unsigned int)(a & b) << 1;

            // 2. 計算無進位加法
            // 使用 XOR 運算模擬不帶進位的加法
            a = a ^ b;

            // 3. 將進位賦值給 b，在下一輪循環中加到 a 上
            b = carry;
        }

        return a;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(1)$.
    -   In worst case (propagating carry through all 32 bits), loop runs 32 times.
-   **Space Complexity**: $O(1)$.

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
