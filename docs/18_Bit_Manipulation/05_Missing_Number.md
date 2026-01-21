# Missing Number (缺失數字) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #268** — [題目連結](https://leetcode.com/problems/missing-number/) | [NeetCode 解說](https://neetcode.io/problems/missing-number)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個包含 0 到 n 中 `n` 個不同數字的陣列 `nums`。
請找出那個沒有出現在陣列中的數字。
你必須設計並實現一個線性時間複雜度 $O(n)$ 且只使用常數額外空間 $O(1)$ 的算法。

-   **Input**: `[3,0,1]` (n=3)
-   **Output**: `2`
-   **Input**: `[0,1]` (n=2)
-   **Output**: `2`
-   **Input**: `[9,6,4,2,3,5,7,0,1]` (n=9)
-   **Output**: `8`

---

## 2. 🐢 Brute Force Approach (暴力解)

-   排序：$O(n \log n)$。然後找索引不匹配的。
-   Hash Set：$O(n)$ 時間，但 $O(n)$ 空間。

---

## 3. 💡 The "Aha!" Moment (優化)

這題有兩個經典的 $O(n)$/$O(1)$ 解法：

**Approach 1: Math (Sum Formula)**

-   0 到 n 的總和應該是 $\frac{n(n+1)}{2}$。
-   計算數組 `nums` 的實際總和。
-   兩者之差就是缺失的數字。
-   **Risk**: 如果 n 很大，求和可能會溢出 (Integer Overflow)。但題目 constraints 通常 $n \le 10^4$，不會溢出。

**Approach 2: Bit Manipulation (XOR)**

-   利用 XOR 的性質：$x \oplus x = 0$。
-   如果我們把 `nums` 中的所有數字 XOR 起來，再把 `0` 到 `n` 的所有數字 XOR 起來。
-   所有出現兩次的數字（一個在陣列，一個在索引範圍）都會抵銷。
-   剩下的那個數字就是缺失的數字。
-   **Safe**: 不會有溢出問題。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../missing_number_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../missing_number_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: XOR

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int res = n; // Initialize with n, because loop only goes 0 to n-1

        for (int i = 0; i < n; i++) {
            res ^= i;
            res ^= nums[i];
        }

        return res;
    }
};
```

### Approach: Math

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int expectedSum = n * (n + 1) / 2;
        int actualSum = 0;
        for (int num : nums) {
            actualSum += num;
        }
        return expectedSum - actualSum;
    }
};
```

### Python Reference (XOR)

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res
        # Alternatively using XOR:
        # res = len(nums)
        # for i in range(len(nums)):
        #     res ^= i ^ nums[i]
        # return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        // 我們需要 XOR 兩組數據：
        // 1. 数组中的所有元素 (nums[0]...nums[n-1])
        // 2. 完整的序列 (0...n)

        // 先將 res 初始化為 n (因為循環只跑到 n-1)
        int res = n;

        for (int i = 0; i < n; i++) {
            // XOR 索引 i (代表完整序列的一部分)
            res ^= i;
            // XOR 数组元素 nums[i]
            res ^= nums[i];
        }

        // 最終剩下的就是缺失的數字
        // 例如 nums = [3,0,1], n=3
        // res = 3 ^ (0^3) ^ (1^0) ^ (2^1)
        //     = 3^3 ^ 0^0 ^ 1^1 ^ 2
        //     = 0 ^ 0 ^ 0 ^ 2 = 2
        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   Constant extra space.

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
- [Single Number (只出現一次的數字)](01_Single_Number.md)
