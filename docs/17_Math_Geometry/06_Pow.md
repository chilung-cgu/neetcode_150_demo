---
title: "Pow(x, n) (數值的 n 次方)"
description: "實現 `pow(x, n)`，即計算 `x` 的 `n` 次冪 ($x^n$)。"
tags:
  - 
Math  - Matrix
difficulty: Medium
---

# Pow(x, n) (數值的 n 次方) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #50** — [題目連結](https://leetcode.com/problems/powx-n/) | [NeetCode 解說](https://neetcode.io/problems/powx-n)


## 1. 🧐 Problem Dissection (釐清問題)

實現 `pow(x, n)`，即計算 `x` 的 `n` 次冪 ($x^n$)。

-   **Input**: `x = 2.00000, n = 10`
-   **Output**: `1024.00000`
-   **Input**: `x = 2.10000, n = 3`
-   **Output**: `9.26100`
-   **Input**: `x = 2.00000, n = -2`
-   **Output**: `0.25000` ($2^{-2} = 1/2^2 = 1/4 = 0.25$)

**Constraints**:

-   $n$ is a 32-bit signed integer `[-2^31, 2^31 - 1]`.
-   Handle negative exponents.
-   Handle edge case `n = INT_MIN`.

---

## 2. 🐢 Brute Force Approach (暴力解)

簡單的循環相乘 $n$ 次。

-   Time: $O(n)$。
-   如果 $n = 2^{31}-1$，這會超時 (Time Limit Exceeded)。

---

## 3. 💡 The "Aha!" Moment (優化)

**Fast Exponentiation (Exponentiation by Squaring)**:
利用 $x^n = (x^2)^{n/2}$ 的性質。

-   如果 $n$ 是偶數：$x^n = (x^2)^{n/2}$
-   如果 $n$ 是奇數：$x^n = x \times (x^2)^{(n-1)/2}$

這樣每次 $n$ 都會減半，時間複雜度變為 $O(\log n)$。

**Handling Negative n**:
$x^{-n} = (1/x)^n$。
注意當 $n = -2147483648$ (INT_MIN) 時，直接去負號會溢出。
我們可以用 `long long` 來存儲 $n$ 的絕對值。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../pow_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../pow_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Recursive Fast Power

```cpp
#include <cmath>

using namespace std;

class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        return fastPow(x, N);
    }

private:
    double fastPow(double x, long long n) {
        if (n == 0) return 1.0;

        double half = fastPow(x, n / 2);

        if (n % 2 == 0) {
            return half * half;
        } else {
            return half * half * x;
        }
    }
};
```

### Approach: Iterative Fast Power (More Efficient)

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double ans = 1;
        double current_product = x;

        while (N > 0) {
            if (N % 2 == 1) {
                ans = ans * current_product;
            }
            current_product = current_product * current_product;
            N /= 2;
        }

        return ans;
    }
};
```

### Python Reference

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        curr = x

        while n > 0:
            if n % 2 == 1:
                ans *= curr
            curr *= curr
            n //= 2

        return ans
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        // 使用 long long 防止 n = INT_MIN 時取絕對值溢位
        // 範圍: [-2^31, 2^31-1]，如果是 -2^31，取負後為 2^31，超過 int 範圍
        long long N = n;

        // 處理負次方：x^-n = (1/x)^n
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }

        double ans = 1;
        double current_product = x;

        // 快速冪迭代法 (Binary Exponentiation)
        // 例如需要計算 x^10 (1010 binary)
        // ans 初始化為 1
        // loop 1: N=10 (LSB=0), current=x^2, N=5
        // loop 2: N=5 (LSB=1), ans=ans*x^2, current=x^4, N=2
        // loop 3: N=2 (LSB=0), current=x^8, N=1
        // loop 4: N=1 (LSB=1), ans=ans*x^8, current=x^16, N=0
        // Result = x^2 * x^8 = x^10
        while (N > 0) {
            // 如果當前 N 是奇數，將當前的冪次乘入結果
            if (N % 2 == 1) {
                ans = ans * current_product;
            }
            // 每輪將底數平方
            current_product = current_product * current_product;
            // 指數減半
            N /= 2;
        }

        return ans;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(\log n)$
    -   We divide n by 2 in each iteration.
-   **Space Complexity**: $O(1)$
    -   Using iterative approach. Recursive approach would be $O(\log n)$ stack space.

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
