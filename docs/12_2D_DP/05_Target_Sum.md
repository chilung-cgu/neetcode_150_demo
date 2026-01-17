# Target Sum (目標和)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個非負整數陣列 `nums` 和一個整數 `target`。
你需要對每個整數前面添加 `+` 或 `-` 號，使得運算結果等於 `target`。
回傳有多少種方法。

-   **Input**: `nums = [1,1,1,1,1], target = 3`
-   **Output**: `5`
    -   -1+1+1+1+1 = 3
    -   +1-1+1+1+1 = 3
    -   ...
-   **Constraints**:
    -   $1 <= nums.length <= 20$
    -   $0 <= nums[i] <= 1000$
    -   $sum(nums) <= 1000$
    -   $-1000 <= target <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Backtracking**:
每個位置有 2 種選擇。

-   `count(i, currentSum)`:
    -   `count(i+1, currentSum + nums[i])`
    -   `count(i+1, currentSum - nums[i])`
-   **Time**: $O(2^N)$。 $N=20$ 時 $2^{20} \approx 10^6$，在這個約束下其實是可以接受的 (Recursion 也是一種解法)。

---

## 3. 💡 The "Aha!" Moment (優化)

這題可以轉化為 **0/1 背包問題**。
我們將 `nums` 分成兩個子集：

-   `P`: 正數集合 (前面放 `+`)
-   `N`: 負數集合 (前面放 `-`)

我們希望： `sum(P) - sum(N) = target`
且已知： `sum(P) + sum(N) = totalSum`

兩式相加：
`2 * sum(P) = target + totalSum`
`sum(P) = (target + totalSum) / 2`

**問題轉化為**：
找出 `nums` 的一個子集 `P`，使得其和為 `(target + totalSum) / 2`。
這就是 **Subset Sum** 問題 (Partition Equal Subset Sum 的變形)。

**注意**：

1.  如果 `target + totalSum` 是奇數，無解 (return 0)。
2.  如果 `target + totalSum < 0`，無解。

DP 定義：
`dp[j]` = 有多少種方法填滿容量為 `j` 的背包。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../target_sum_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../target_sum_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Subset Sum Optimization)

```cpp
#include <vector>
#include <numeric>
#include <cmath>

using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        long long totalSum = accumulate(nums.begin(), nums.end(), 0LL);

        // Impossible cases
        // 1. target is out of range [-totalSum, totalSum]
        // 2. (target + totalSum) is odd
        if (target > totalSum || target < -totalSum) return 0;
        if ((target + totalSum) % 2 != 0) return 0;

        int subsetSum = (target + totalSum) / 2;

        // dp[j] stores number of ways to get sum j
        vector<int> dp(subsetSum + 1, 0);
        dp[0] = 1; // 0 sum possible with empty subset (1 way)

        // 0/1 Knapsack
        for (int num : nums) {
            // Iterate backwards
            for (int j = subsetSum; j >= num; j--) {
                dp[j] += dp[j - num];
            }
        }

        return dp[subsetSum];
    }
};
```

### Python Reference

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (index, total) -> ways

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtrack(0, 0)
```
Wait, pure recursion/memoization is also good, but DP is more optimal space-wise and avoids recursion overhead. The constraints $N=20$ allow recursion, but DP is $O(N \times Sum)$.

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        long long sum = 0;
        for(int n : nums) sum += n;

        // 數學推導：
        // P - N = target
        // P + N = sum
        // 2P = target + sum
        // P = (target + sum) / 2

        // 如果 target + sum 是奇數，或者 target 絕對值大於 sum，則無解
        if ((target + sum) % 2 != 0 || abs(target) > sum) return 0;

        int subsetTarget = (target + sum) / 2;

        // dp[j] 代表湊出和 j 的方法數
        // 因為是 0/1 背包 (每個數字只能用一次)，外層迴圈遍歷 nums，內層從大到小遍歷 sum
        vector<int> dp(subsetTarget + 1, 0);
        dp[0] = 1; // sum 為 0 有一種方法 (都不選)

        for (int n : nums) {
            for (int j = subsetTarget; j >= n; j--) {
                dp[j] += dp[j - n];
            }
        }

        return dp[subsetTarget];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \times S)$
    -   $N=20$, $S \approx 1000$. $2 \times 10^4$ ops. Extremely fast.
-   **Space Complexity**: $O(S)$
    -   DP array size is subset sum ($\approx 1000$).
