# Maximum Subarray (最大子陣列和)

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
