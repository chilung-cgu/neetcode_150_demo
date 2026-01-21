# Maximum Product Subarray (最大乘積子陣列) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #152** — [題目連結](https://leetcode.com/problems/maximum-product-subarray/) | [NeetCode 解說](https://neetcode.io/problems/maximum-product-subarray)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `nums`，找出一個 **連續子陣列 (Contiguous Subarray)**，使得其元素乘積最大。
回傳該最大乘積。

-   **Input**: `nums = [2,3,-2,4]`
-   **Output**: `6` ([2,3])
-   **Input**: `nums = [-2,0,-1]`
-   **Output**: `0`
-   **Input**: `nums = [-2,3,-4]`
-   **Output**: `24` ([-2,3,-4])
-   **Constraints**:
    -   $1 <= nums.length <= 2 \times 10^4$
    -   $-10 <= nums[i] <= 10$

---

## 2. 🐢 Brute Force Approach (暴力解)

枚舉所有子陣列 $O(N^2)$。

-   計算乘積 $O(N)$。總共 $O(N^3)$。
-   優化乘積計算後總共 $O(N^2)$。
-   $N=20000$， $O(N^2)$ 是 $4 \times 10^8$，可能會超時或很慢。

---

## 3. 💡 The "Aha!" Moment (優化)

這題很像 Maximum Subarray Sum (Kadane's Algorithm)，但是「負負得正」是關鍵。
當遇到負數時，原本的「最大值」會變成「最小值」，原本的「最小值」會變成「最大值」。

所以我們需要同時維護兩個變數：

1.  `curMax`: 包含當前元素的最大乘積。
2.  `curMin`: 包含當前元素的最小乘積（為了應對負數翻身）。

**State Transition**:
當遍歷到 `n` (`nums[i]`) 時：

-   `tempMax = max(n, n * curMax, n * curMin)`
    -   為什麼要比較 `n`？因為子陣列可以重新從 `n` 開始（斷開前面的）。
    -   為什麼要比較 `n * curMin`？因為如果 `n < 0` 且 `curMin < 0`，乘起來可能變超級大。
-   `curMin = min(n, n * curMax, n * curMin)`
-   `curMax = tempMax`
-   `res = max(res, curMax)`

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../max_product_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../max_product_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Kadane's Variant)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (nums.empty()) return 0;

        // Result defaults to first element (handle single negative element case)
         int res = nums[0];
         int curMax = 1;
         int curMin = 1;

         for (int n : nums) {
             // If we encouter 0, the subarray product resets to 1 (conceptually)
             // But the standard logic handles 0 correctly:
             // max(0, 0*max, 0*min) -> 0.
             // But if we want to restart, we can optimize.
             // Actually, Kadane logic handles reset naturally by comparing with `n`.

             // Store curMax in temp because it gets updated
             int tempMax = curMax * n;

             curMax = max({n, curMax * n, curMin * n});
             curMin = min({n, tempMax, curMin * n});

             res = max(res, curMax);
         }

         return res;
    }
};
```

Wait, standard initialization is slightly different.
Common pattern:
Initialize `res` to max of array.
`curMax`, `curMin` starts at 1.

Let's refine:

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];

        for(int n : nums) res = max(res, n); // Find max purely in case all are negative

        int curMin = 1, curMax = 1;

        for(int n : nums) {
            if (n == 0) {
                curMin = 1;
                curMax = 1;
                continue;
            }
            int tmp = curMax * n;
            curMax = max({n * curMax, n * curMin, n});
            curMin = min({tmp, n * curMin, n});
            res = max(res, curMax);
        }
        return res;
    }
};
```

Let's stick to the simplest Kadane form without resetting on 0 explicitly.

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int curMax = 1;
        int curMin = 1;

        for (int n : nums) {
            int tmp = curMax * n;
            curMax = max({n, n * curMax, n * curMin});
            curMin = min({n, tmp, n * curMin});
            res = max(res, curMax);
        }

        return res;
    }
};
```
But if `nums=[5]`, loops once. `curMax=5`, `res=5`. Correct.
If `nums=[-2]`, `curMax=-2`, `res=-2`. Correct.
If `nums=[-2, 3]`.
Init `res=-2`, `curMax=1`, `curMin=1`.
Loop -2: `curMax = max(-2, -2, -2) = -2`. `curMin = min(-2, -2, -2) = -2`. `res = -2`.
Loop 3: `tmp = -6`. `curMax = max(3, -6, -6) = 3`. `curMin = min(3, -6, -6) = -6`. `res = 3`.
Correct.

### Python Reference

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue

            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax)

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // 結果初始化為陣列中的最大單一元素，避免全負數時出錯 (例如 [-2])
        // 其實可以初始為 INT_MIN，但若陣列只有一個元素 [-2]，
        // 跑完迴圈後 res 應該要更新為 -2
        // 為了安全起見，這裡先設為 nums[0] (或遍歷找最大值)
        int res = nums[0];
        for(int n : nums) res = max(res, n);

        int curMax = 1;
        int curMin = 1;

        for (int n : nums) {
            // 遇到 0 會讓乘積歸零，這相當於重置子陣列
            // 但即使不特別處理 0，下面的邏輯 max(n, ...) 也會捕捉到 n=0
            // 這裡為了邏輯清晰 (也是 NeetCode 的寫法)，遇到 0 重置 curMax/curMin
            if (n == 0) {
                curMax = 1;
                curMin = 1;
                continue;
            }

            int temp = curMax * n;

            // 狀態轉移：
            // curMax 可能是：
            // 1. n 本身 (重新開始)
            // 2. n * 原本最大 (正數 * 正數)
            // 3. n * 原本最小 (負數 * 負數，負負得正)
            curMax = max({n, curMax * n, curMin * n});

            // curMin 同理
            curMin = min({n, temp, curMin * n});

            res = max(res, curMax);
        }

        return res;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   Only variables.
