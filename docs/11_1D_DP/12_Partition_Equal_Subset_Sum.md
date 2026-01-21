# Partition Equal Subset Sum (分割等和子集) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

給定一個**只包含正整數**的非空陣列 `nums`。
判斷是否可以將這個陣列分割成兩個子集，使得這兩個子集的元素和相等。

換句話說：找出是否存在一個子集，其總和等於 `totalSum / 2`。

- **Input**: `nums = [1,5,11,5]`
- **Output**: `true`
  - Total = 22. Target = 11.
  - Subset `[1, 5, 5]` sums to 11. (Or `[11]`)
- **Input**: `nums = [1,2,3,5]`
- **Output**: `false`
  - Total = 11. Target = 5.5 (Impossible for integers).
- **Constraints**:
  - $1 <= nums.length <= 200$
  - $1 <= nums[i] <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

**DFS**:
每個元素可以選擇放入 Set A 或 Set B。
如果 Set A sum == Set B sum，則成功。
這等同於 subset sum problem。

- **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是經典的 **0/1 Knapsack Problem (背包問題)**。
目標：從 `nums` 中選出一些數字，填滿容量為 `target = totalSum / 2` 的背包。

**Pre-check**:
如果 `totalSum` 是奇數，不可能平分，直接 `false`。

**DP State**:
`dp[i][j]` = 前 `i` 個數字能否湊出和 `j`。
`dp[i][j] = dp[i-1][j] || dp[i-1][j - nums[i]]`
(不選 `nums[i]` OR 選 `nums[i]`)

**Space Optimization**:
我們只需要一維陣列 `dp[j]`。
`dp[j] = dp[j] || dp[j - nums[i]]`。
**注意**：內層迴圈必須從後往前遍歷 (`target` down to `nums[i]`)，以避免同一個數字被重複使用 (這就是 0/1 背包的特性)。

使用 `std::bitset` 優化？
Constraint `length <= 200`, `nums[i] <= 100`. Total sum <= 20000.
可以用 `bitset<20001>` 來做，速度極快 ($O(N \times Sum / 64)$)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../partition_equal_subset_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../partition_equal_subset_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach 1: DP with Set (Easy to understand)

```cpp
#include <vector>
#include <numeric>
#include <unordered_set>

using namespace std;

class SolutionSet {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 != 0) return false;

        int target = sum / 2;
        unordered_set<int> dp;
        dp.insert(0);

        for (int num : nums) {
            unordered_set<int> nextDP = dp; // Copy current possible sums
            for (int s : dp) {
                if (s + num == target) return true;
                if (s + num < target) {
                    nextDP.insert(s + num);
                }
            }
            dp = nextDP;
        }

        return dp.count(target);
    }
};
```

### Approach 2: 0/1 Knapsack DP (Vector) - Standard

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % 2 != 0) return false;

        int target = sum / 2;
        vector<bool> dp(target + 1, false);
        dp[0] = true;

        for (int num : nums) {
            // Iterate backwards to avoid reusing the same element for the same sum
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }
};
```

### Python Reference

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們採用標準的一維 DP 背包解法。

```cpp
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        // 1. 計算總和
        int totalSum = accumulate(nums.begin(), nums.end(), 0);

        // 如果總和是奇數，無法分成兩個相等的整數和
        if (totalSum % 2 != 0) return false;

        int target = totalSum / 2;

        // dp[j] 代表能否湊出總和 j
        // 大小為 target + 1
        vector<bool> dp(target + 1, false);

        // Base case: 湊出 0 是可能的 (都不選)
        dp[0] = true;

        // 2. 0/1 背包處理
        for (int num : nums) {
            // 必須從大到小遍歷，這是 0/1 背包壓縮空間的關鍵
            // 如果從小到大，dp[j - num] 可能是這一輪剛更新過的 (即使用了 num 兩次)
            // 從大到小則保證 dp[j - num] 是上一輪的狀態 (還沒用過 num)
            for (int j = target; j >= num; j--) {
                dp[j] = dp[j] || dp[j - num];
            }
        }

        return dp[target];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

- **Time Complexity**: $O(N \times S)$
  - $N$ is length of numbers. $S$ is the target sum.
  - Worst case: $200 \times 10000 = 2 \times 10^6$. Very fast.
- **Space Complexity**: $O(S)$
  - $DP$ array size is target sum.
