# Single Number (只出現一次的數字) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #136** — [題目連結](https://leetcode.com/problems/single-number/) | [NeetCode 解說](https://neetcode.io/problems/single-number)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個非空整數陣列 `nums`，除了某個元素只出現一次以外，其餘每個元素均出現兩次。
找出那個只出現了一次的元素。
你必須設計並實現一個線性時間複雜度 $O(n)$ 的算法，且只使用常數額外空間 $O(1)$。

-   **Input**: `[2,2,1]`
-   **Output**: `1`
-   **Input**: `[4,1,2,1,2]`
-   **Output**: `4`

---

## 2. 🐢 Brute Force Approach (暴力解)

使用 Hash Map 統計每個數字出現的次數。遍歷 Map 找出次數為 1 的數字。

-   **Time**: $O(n)$。
-   **Space**: $O(n)$。不符合空間要求。

---

## 3. 💡 The "Aha!" Moment (優化)

**XOR (異或運算)**:
利用 XOR 的性質：

1.  $a \oplus 0 = a$
2.  $a \oplus a = 0$
3.  $a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = b$ (結合律與交換律)

因為除了目標數字出現一次，其他都出現兩次。
將所有數字進行 XOR 運算，成對的數字會互相抵銷變成 0，最後剩下的就是那個只出現一次的數字。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../single_number_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../single_number_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Bit Manipulation (XOR)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int n : nums) {
            res ^= n;
        }
        return res;
    }
};
```

### Python Reference

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        // 遍歷所有數字，將它們進行異或運算
        for (int n : nums) {
            // 利用 x ^ x = 0 的性質
            // 所有出現兩次的數字都會被消除
            // 唯獨出現一次的數字會被保留下來
            res ^= n;
        }
        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   One pass through the array.
-   **Space Complexity**: $O(1)$
    -   Only one variable needed.

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
