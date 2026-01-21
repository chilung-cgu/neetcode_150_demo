---
title: "Multiply Strings (字符串相乘)"
description: "給定兩個以字符串形式表示的非負整數 `num1` 和 `num2`。 請回傳它們的乘積，也以字符串表示。 **不能** 使用任何內建的大數庫（如 Python 的 `BigInteger`）或直接將輸入轉換為整數。"
tags:
  - 
Math  - Matrix
difficulty: Medium
---

# Multiply Strings (字符串相乘) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #43** — [題目連結](https://leetcode.com/problems/multiply-strings/) | [NeetCode 解說](https://neetcode.io/problems/multiply-strings)


## 1. 🧐 Problem Dissection (釐清問題)

給定兩個以字符串形式表示的非負整數 `num1` 和 `num2`。
請回傳它們的乘積，也以字符串表示。
**不能** 使用任何內建的大數庫（如 Python 的 `BigInteger`）或直接將輸入轉換為整數。

-   **Input**: `num1 = "2", num2 = "3"`
-   **Output**: `"6"`
-   **Input**: `num1 = "123", num2 = "456"`
-   **Output**: `"56088"`
-   **Constraints**:
    -   Length of num1, num2 <= 200.
    -   Both contain only digits 0-9.

---

## 2. 🐢 Brute Force Approach (暴力解)

模擬小學乘法。
`num1` 乘以 `num2` 的每一位，然後將結果相加。
例如 `123 * 456`:

-   `123 * 6 = 738`
-   `123 * 50 = 6150`
-   `123 * 400 = 49200`
-   Sum = `56088`
這就是標準解法。

---

## 3. 💡 The "Aha!" Moment (優化)

我們可以更精確地控制每一位的運算，而不需要顯式地進行「字符串加法」。

**Observation**:

-   `num1` 的長度為 `m`，`num2` 的長度為 `n`。
-   乘積的長度最多為 `m + n`。
-   `num1[i] * num2[j]` 的結果將會貢獻到結果數組的索引 `i + j` 和 `i + j + 1` 上。

**Algorithm**:

1.  創建一個大小為 `m + n` 的數組 `pos`，初始化為 0。
2.  從右向左遍歷 `num1` (索引 `i`) 和 `num2` (索引 `j`)。
3.  計算乘積 `mul = (num1[i] - '0') * (num2[j] - '0')`。
4.  加上當前位置已有的進位：`sum = mul + pos[i + j + 1]`。
5.  更新 `pos[i + j + 1] = sum % 10` (個位)。
6.  更新 `pos[i + j] += sum / 10` (進位)。
7.  最後將 `pos` 轉為字符串，並跳過前導零。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../multiply_strings_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../multiply_strings_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Optimized Simulation

```cpp
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int m = num1.size();
        int n = num2.size();
        vector<int> pos(m + n, 0);

        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int p1 = i + j;
                int p2 = i + j + 1;

                // Add to current position
                int sum = mul + pos[p2];

                pos[p2] = sum % 10;
                pos[p1] += sum / 10;
            }
        }

        string sb = "";
        for (int p : pos) {
            // Skip leading zeros
            if (!(sb.length() == 0 && p == 0)) {
                sb += to_string(p);
            }
        }

        return sb.length() == 0 ? "0" : sb;
    }
};
```

### Python Reference

```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int m = num1.size();
        int n = num2.size();
        // 結果的最大長度為 m + n
        // 例如 99 * 99 = 9801 (2位 * 2位 = 4位)
        vector<int> pos(m + n, 0);

        // 雙重循環，從個位數開始相乘
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');

                // 乘積在結果陣列中的位置
                // num1[i] 和 num2[j] 的乘積影響 pos[i+j] 和 pos[i+j+1]
                int p1 = i + j;     // 進位位
                int p2 = i + j + 1; // 當前位

                // 加上之前該位置可能存在的進位
                int sum = mul + pos[p2];

                // 更新當前位 (取餘)
                pos[p2] = sum % 10;
                // 更新進位位 (累加)
                pos[p1] += sum / 10;
            }
        }

        // 將結果陣列轉為字符串
        string sb = "";
        for (int p : pos) {
            // 跳過前導零
            if (!(sb.length() == 0 && p == 0)) {
                sb += to_string(p);
            }
        }
        // 如果結果為空（理論上前面判斷過 num1/num2 為 0 的情況，這裡是以防萬一）
        return sb.length() == 0 ? "0" : sb;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(M \times N)$
    -   Standard multiplication complexity.
-   **Space Complexity**: $O(M + N)$
    -   Output string storage.

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
- [Plus One (加一)](05_Plus_One.md)
