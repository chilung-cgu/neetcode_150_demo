---
title: "Sum of Two Integers (兩整數之和)"
description: "給定兩個整數 `a` 和 `b`，請在 **不使用 `+` 和 `-` 運算符** 的情況下計算它們的和。"
tags:
  - Bit Manipulation
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

這題禁止使用加減法，所以必須使用位運算來模擬計算機底層硬體的 **半加器 (Half-Adder)** 邏輯。這段邏輯非常反直覺，讓我們先把程式碼和 `^`、`&` 忘掉，從「人類的加法」開始理解。

### 🧠 Intuitive Breakdown (大白話解析)

#### 1. 人類的加法：拆成兩步來看
假設我們要計算 $57 + 86$，小學老師教我們要對齊，然後相加：
1. **第一步：只算當下的數字，不理會進位。**
   - 個位數：$7 + 6 = 13$（把進位的 $1$ 丟掉，只寫 $3$）
   - 十位數：$5 + 8 = 13$（把進位的 $1$ 丟掉，只寫 $3$）
   - 目前得到一個**半成品：$33$**。
2. **第二步：把剛剛被我們丟掉的進位找回來。**
   - 個位數 $7 + 6$ 產生了 $10$ 的進位。
   - 十位數 $5 + 8$ 產生了 $100$ 的進位。
   - 把進位加總：**$110$**。
3. **第三步：把上面兩步的結果加起來。**
   - $33$（半成品） $+$ $110$（進位） $=$ **$143$**（正確答案！）。

**這題演算法的核心邏輯，完全就是這三步！** 電腦只是把十進制換成了二進制（只有 $0$ 和 $1$）。

---

#### 2. 電腦的工具：`^` 和 `&`
電腦沒有 `+` 號可以用，所以它派出了兩個位元運算的特工來執行上面的步驟：

- **特工一：`^` (XOR)**，它的任務是**「第一步：不理會進位的加法」**。
  - $0 \oplus 0 = 0$
  - $1 \oplus 0 = 1$
  - $0 \oplus 1 = 1$
  - $1 \oplus 1 = 0$ （二進制 $1+1$ 滿 $2$ 要進位，但它不管進位，所以只留 $0$）

- **特工二：`&` (AND) 搭配 `<< 1`**，它的任務是**「第二步：專門抓進位」**。
  - 什麼情況會產生進位？只有 $1 + 1$ 的時候才會。
  - `&` (AND) 剛好只有當兩邊都是 $1$ 時，結果才會是 $1$。
  - 抓出進位後，因為進位是要加給「左邊那一位」的，所以必須向左移動一格：`<< 1`。

---

#### 3. 實際範例推演： $5 + 7 = 12$
迴圈的邏輯就是：只要還有進位 (`b != 0`)，我們就繼續把「半成品」和「進位」加起來。

| 狀態 | `a` (負責儲存半成品) | `b` (負責儲存進位) | 說明 |
| :--- | :--- | :--- | :--- |
| **剛開始** | `0101` (數值 $5$) | `0111` (數值 $7$) | 準備相加。 |
| **第一回合** | `0101 ^ 0111` <br> = **`0010`** | `(0101 & 0111) << 1` <br> = `0101 << 1` <br> = **`1010`** | `a` 算出無進位加法 (半成品)。<br>`b` 抓出了該進位的位元，並往左推了一格。 |
| **第二回合** | `0010 ^ 1010` <br> = **`1000`** | `(0010 & 1010) << 1` <br> = `0010 << 1` <br> = **`0100`** | 把第一回合的半成品 `0010` 跟進位 `1010` 再次相加。又產生了新的進位！ |
| **第三回合** | `1000 ^ 0100` <br> = **`1100`** | `(1000 & 0100) << 1` <br> = `0000 << 1` <br> = **`0000`** | 再加一次。這一次，`a` 變成了 `1100` (十進制的 $12$)！<br>`b` 計算發現完全沒有進位了，變成 `0000`。 |
| **結束** | **`1100`** (正確答案 $12$) | **`0`** | 因為 `b == 0`，沒有進位需要處理了，迴圈結束，回傳 `a`。 |

> 📌 **總結**：<br>`a` 永遠負責記住「目前相加的半成品」。<br>`b` 永遠負責找出「這次相加產生了哪些進位」。<br>只要有進位，就把他們兩個再丟回去重新相加，直到不再產生任何進位為止。

---

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
