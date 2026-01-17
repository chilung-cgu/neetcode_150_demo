# House Robber II (打家劫舍 II)

## 1. 🧐 Problem Dissection (釐清問題)

這題是 "House Robber" 的進階版。
唯一的差別是：房屋現在圍成了一個 **圓圈 (Circle)**。
這意味著：**第一間房子和最後一間房子是相鄰的**。
限制依然是：不能搶相鄰的兩間房子。

-   **Input**: `nums = [2,3,2]`
-   **Output**: `3`
    -   不能搶房 1 (2) 和房 3 (2)，因為它們相鄰。
    -   只搶房 2 (3)。
-   **Input**: `nums = [1,2,3,1]`
-   **Output**: `4`
    -   Rob house 1 (1) and house 3 (3). Sum = 4.
    -   Cannot rob house 4 (1) because it's adjacent to house 1.
-   **Constraints**:
    -   $1 <= nums.length <= 100$
    -   $0 <= nums[i] <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

這題的難點在於頭尾相連。如果我们直接用 linear DP 會有問題。
直接枚舉：

-   搶第 1 間 -> 不能搶第 2 間，也不能搶最後一間。
-   不搶第 1 間 -> 可以考慮搶或不搶最後一間。
-   暴力遞迴會很慢。

---

## 3. 💡 The "Aha!" Moment (優化)

既然房子排成一個圓，我們可以把它拆解成 **兩個線性的 "House Robber I" 問題**：
因為頭 (`index 0`) 和尾 (`index n-1`) 互斥，所以我們只能選其中一個（或者都不選，這包含在選一個的情況裡）。

所以問題等價於：

1.  **情況一**：不搶最後一間 (`index n-1`)。
    -   搶劫範圍：`nums[0]` 到 `nums[n-2]`。
2.  **情況二**：不搶第一間 (`index 0`)。
    -   搶劫範圍：`nums[1]` 到 `nums[n-1]`。

最終答案就是 `max(HouseRobberI(0 to n-2), HouseRobberI(1 to n-1))`。
邊界情況：只有一間房子時，必須搶那間。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../house_robber_ii_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../house_robber_ii_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Reuse DP Logic

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];

        // Scenario 1: Rob houses 0 to n-2 (Exclude last)
        int max1 = robLinear(nums, 0, n - 2);

        // Scenario 2: Rob houses 1 to n-1 (Exclude first)
        int max2 = robLinear(nums, 1, n - 1);

        return max(max1, max2);
    }

private:
    // Helper function from House Robber I
    int robLinear(vector<int>& nums, int start, int end) {
        int prev2 = 0;
        int prev1 = 0;

        for (int i = start; i <= end; i++) {
            int current = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
};
```

### Python Reference

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        // 邊界條件：如果只有一間房子，直接搶，不用管鄰居
        // 如果這個不處理，下面的 range 可能會有問題
        if (nums.size() == 1) return nums[0];

        // 因為首尾相連，我們把它拆成兩種線性情況：
        // 1. 不包含最後一間房子 (範圍 [0 ... n-2])
        // 2. 不包含第一間房子 (範圍 [1 ... n-1])
        // 這樣就不用擔心首尾同時被搶的問題
        return max(
            robRange(nums, 0, nums.size() - 2),
            robRange(nums, 1, nums.size() - 1)
        );
    }

    // 這就是 House Robber I 的邏輯，只是指定了 start 和 end
    int robRange(vector<int>& nums, int start, int end) {
        int prev2 = 0;
        int prev1 = 0;

        for (int i = start; i <= end; i++) {
            int curr = max(prev2 + nums[i], prev1);
            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Scanning the list twice (once for each range). $2N \approx O(N)$.
-   **Space Complexity**: $O(1)$
    -   Only constant space used in helper function.
