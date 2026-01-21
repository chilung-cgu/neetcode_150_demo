# House Robber (打家劫舍) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

題目說你是一個專業的搶匪，計畫搶劫沿街的房屋。
每間房都有一定數量的現金。
唯一阻止你搶劫單個房屋的限制是：**相鄰的房屋裝有連動防盜系統**。
如果 **兩間相鄰** 的房屋在同一晚被搶，系統會自動報警。

給定一個非負整數陣列 `nums` 代表每間房的金額，計算你在 **不觸發警報** 的情況下能搶到的最大金額。

-   **Input**: `nums = [1,2,3,1]`
-   **Output**: `4`
    -   Rob house 1 (money = 1) and then rob house 3 (money = 3).
    -   Total amount you can rob = 1 + 3 = 4.
-   **Input**: `nums = [2,7,9,3,1]`
-   **Output**: `12`
    -   Rob house 1 (2), house 3 (9), house 5 (1). Total = 12.
-   **Constraints**:
    -   $1 <= nums.length <= 100$
    -   $0 <= nums[i] <= 400$

---

## 2. 🐢 Brute Force Approach (暴力解)

**DFS**:
每個房子有兩個選擇：搶或不搶。

-   如果搶 `i`，那就不能搶 `i+1`，只能考慮 `i+2`。
-   如果不搶 `i`，可以考慮 `i+1`。
`rob(i) = max(nums[i] + rob(i+2), rob(i+1))`

-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個標準的 DP 問題。
定義 `dp[i]` 為：搶劫前 `i` 間房子能得到的最大金額。
對於第 `i` 間房子 (`nums[i]`)，我們有兩個選擇：

1.  **搶它**：那我們就不能搶 `i-1`，所以總金額是 `dp[i-2] + nums[i]`。
    -   注意：這裡的 `dp` 定義如果是「前 i 間」，那 `i-2` 應該對應到 `dp[i-2]`。
2.  **不搶它**：那我們可以保持前 `i-1` 間的最大金額，即 `dp[i-1]`。

遞迴公式：
`dp[i] = max(dp[i-1], dp[i-2] + nums[i])`

只需要兩個變數 `prev1` (dp[i-1]) 和 `prev2` (dp[i-2]) 來做空間優化。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../house_robber_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../house_robber_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Space Optimized)

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

        int prev2 = 0; // dp[i-2]
        int prev1 = 0; // dp[i-1]

        for (int num : nums) {
            int current = max(prev1, prev2 + num);
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
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        // prev2: 搶到上上間房子的最大金額 (dp[i-2])
        // prev1: 搶到上一間房子的最大金額 (dp[i-1])
        // 初始都為 0，方便處理邊界 (例如第一間房子 i=0 時，prev1=0, prev2=0)
        int prev2 = 0;
        int prev1 = 0;

        for (int money : nums) {
            // 對於當前房子 money，我們可以：
            // 1. 搶這間：收益為 prev2 + money (不能搶上一間)
            // 2. 不搶這間：收益為 prev1 (保持上一間的最高收益)
            int curr = max(prev2 + money, prev1);

            // 滾動更新
            prev2 = prev1;
            prev1 = curr;
        }

        // prev1 最終會包含考慮完所有房子後的 max
        return prev1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Loop through array once.
-   **Space Complexity**: $O(1)$
    -   Only constant variables used.
