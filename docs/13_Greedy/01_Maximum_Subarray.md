# Maximum Subarray (最大子陣列和) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #53** — [題目連結](https://leetcode.com/problems/maximum-subarray/) | [NeetCode 解說](https://neetcode.io/problems/maximum-subarray)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums`，找出一個連續子陣列（至少包含一個數字），使得其總和最大。
回傳該最大和。

-   **Input**: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
-   **Output**: `6` ([4,-1,2,1])
-   **Input**: `nums = [1]`
-   **Output**: `1`
-   **Input**: `nums = [5,4,-1,7,8]`
-   **Output**: `23` (all)
-   **Constraints**:
    -   $1 <= nums.length <= 10^5$
    -   $-10^4 <= nums[i] <= 10^4$
    -   **Follow up**: Try Divide and Conquer solution (less optimal but good to know).

---

## 2. 🐢 Brute Force Approach (暴力解)

枚舉所有子陣列 $O(N^2)$ (甚至 $O(N^3)$ 如果重複計算 sum)。
$10^5$ 的數據規模下， $O(N^2)$ 會 TLE。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是經典的 **Kadane's Algorithm**。
核心思想：如果當前的 `current_sum` 變成負數，那麼對於後面的子陣列來說，加上這個負數只會變得更小。
所以如果 `current_sum < 0`，我們就應該**拋棄**前面的部分，重新從當前數字開始計算。

**Logic**:

1.  Initialize `maxTotal = nums[0]`, `currentTotal = 0`.
2.  For each `n` in `nums`:
    `currentTotal += n`
    `maxTotal = max(maxTotal, currentTotal)`
    `if currentTotal < 0: currentTotal = 0` (Reset if negative)

這是一個 Greedy 的過程：我們貪心地只保留 "正貢獻" 的前綴和。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../max_subarray_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../max_subarray_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Kadane's Algorithm (Greedy)

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSub = nums[0];
        int curSum = 0;

        for (int n : nums) {
            // Add current number to running sum
            curSum += n;

            // Check if we found a new max
            maxSub = max(maxSub, curSum);

            // If running sum drops below 0, it's not worth keeping
            // Start fresh from next element (reset to 0)
            if (curSum < 0) {
                curSum = 0;
            }
        }

        return maxSub;
    }
};
```

### Python Reference

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // maxSub 初始化為第一個元素，避免全負數情況下回傳 0
        int maxSub = nums[0];
        int curSum = 0;

        for (int n : nums) {
            // 如果之前的累加和 < 0，那加上去只會讓結果變小
            // 所以不如直接捨棄之前的，從現在這個數字 n 重新開始
            if (curSum < 0) {
                curSum = 0;
            }

            // 將當前數字加入累加和
            curSum += n;

            // 更新全域最大值
            maxSub = max(maxSub, curSum);
        }

        return maxSub;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   No extra space.

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
