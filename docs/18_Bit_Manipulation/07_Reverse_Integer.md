---
title: "Reverse Integer (反轉整數)"
description: "給定一個 32 位的有符號整數 `x`。 請將其數字反轉。 如果反轉後的數值超過了 32 位有符號整數的範圍 $[-2^{31}, 2^{31} - 1]$，則回傳 0。 **假設環境不允許存儲 64 位整數 (signed or unsigned)**。"
tags:
  - 
Bit Manipulation
difficulty: Medium
---

# Reverse Integer (反轉整數) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #7** — [題目連結](https://leetcode.com/problems/reverse-integer/) | [NeetCode 解說](https://neetcode.io/problems/reverse-integer)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個 32 位的有符號整數 `x`。
請將其數字反轉。
如果反轉後的數值超過了 32 位有符號整數的範圍 $[-2^{31}, 2^{31} - 1]$，則回傳 0。
**假設環境不允許存儲 64 位整數 (signed or unsigned)**。

-   **Input**: `x = 123`
-   **Output**: `321`
-   **Input**: `x = -123`
-   **Output**: `-321`
-   **Input**: `x = 120`
-   **Output**: `21`
-   **Input**: `x = 1534236469`
-   **Output**: `0` (Overflows)

---

## 2. 🐢 Brute Force Approach (暴力解)

將整數轉換為字符串，反轉字符串，再轉換回整數。

-   **Pros**: 簡單易寫。
-   **Cons**: 需要解析字符串，且難以處理「環境不支持 64 位」的限制（雖然 Python 自動處理，但 C++ 需要小心）。字符串轉換本身就有開銷。

---

## 3. 💡 The "Aha!" Moment (優化)

**Pop and Push Digits**:
我們可以用數學方法取出最後一位並推入新數字：
`pop = x % 10`
`x /= 10`
`rev = rev * 10 + pop`

**Overflow Check**:
在執行 `rev * 10 + pop` 之前，我們必須檢查是否會溢出。
我們知道 `INT_MAX = 2147483647`，$INT\_MIN = -2147483648$。

1.  **Positive Overflow**: `rev * 10 + pop > INT_MAX`
    -   如果 `rev > INT_MAX / 10`，那麼 `rev * 10` 肯定溢出。
    -   如果 `rev == INT_MAX / 10`，那麼只要 `pop > 7` 就會溢出。
2.  **Negative Overflow**: `rev * 10 + pop < INT_MIN`
    -   如果 `rev < INT_MIN / 10`，肯定溢出。
    -   如果 `rev == INT_MIN / 10`，那麼只要 `pop < -8` 就會溢出。

這樣我們就可以在不使用 64 位整數的情況下檢測溢位。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../reverse_integer_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../reverse_integer_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Math with Overflow Check

```cpp
#include <climits>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            int pop = x % 10;
            x /= 10;

            // Check for overflow before it happens
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) {
                return 0;
            }
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) {
                return 0;
            }

            rev = rev * 10 + pop;
        }

        return rev;
    }
};
```

### Python Reference

```python
class Solution:
    def reverse(self, x: int) -> int:
        # Python handles large integers automatically, so we need manual check
        MIN, MAX = -2147483648, 2147483647

        res = 0
        while x:
            # Python's modulo with negative numbers is different
            # math.fmod is safer for C-like behavior, or handle sign manually
            # Here we simplify by using abs(x) and restoring sign
            pass

        # Simpler Pythonic way considering the constraints:
        sign = [1, -1][x < 0]
        res = sign * int(str(abs(x))[::-1])
        return res if MIN <= res <= MAX else 0
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int reverse(int x) {
        int rev = 0;

        while (x != 0) {
            // 取出最後一位數字
            // 在 C++ 中，-123 % 10 = -3，這符合我們的需求
            int pop = x % 10;
            x /= 10;

            // 檢查正溢位
            // INT_MAX = 2147483647
            // 如果 rev 目前大於 214748364，乘以 10 後一定 > INT_MAX
            // 如果 rev 等於 214748364，且 pop > 7，加上去後會變成 > 2147483647
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > 7)) {
                return 0;
            }

            // 檢查負溢位
            // INT_MIN = -2147483648
            // 邏輯同上，最後一位不能小於 -8
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < -8)) {
                return 0;
            }

            // 安全推入
            rev = rev * 10 + pop;
        }

        return rev;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log_{10} |x|)$
    -   Number of digits is approx 10.
-   **Space Complexity**: $O(1)$

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
