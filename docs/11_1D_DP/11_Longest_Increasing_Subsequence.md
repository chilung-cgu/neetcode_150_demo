# Longest Increasing Subsequence (最長遞增子序列)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個整數陣列 `nums`，找出其中最長的**嚴格遞增子序列** (LIS) 的長度。
子序列 (Subsequence) 不要求連續，但順序必須保持。

-   **Input**: `nums = [10,9,2,5,3,7,101,18]`
-   **Output**: `4` ([2,3,7,101] or [2,3,7,18])
-   **Input**: `nums = [0,1,0,3,2,3]`
-   **Output**: `4`
-   **Input**: `nums = [7,7,7,7,7,7,7]`
-   **Output**: `1`
-   **Constraints**:
    -   $1 <= nums.length <= 2500$
    -   $-10^4 <= nums[i] <= 10^4$
    -   **Follow up**: Can you come up with an algorithm that runs in $O(n \log n)$ time complexity?

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`LIS(prev_val, current_index)`:
對於當前元素，如果 `nums[i] > prev_val`，可以選擇：

1.  包含它：`1 + LIS(nums[i], i + 1)`
2.  不包含它：`LIS(prev_val, i + 1)`
-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

**Approach 1: DP ($O(N^2)$)**
`dp[i]` 表示以 `nums[i]` 為 **結尾** 的最長遞增子序列長度。
`dp[i] = 1 + max(dp[j])` for all `0 <= j < i` where `nums[j] < nums[i]`.
如果找不到比 `nums[i]` 小的，則 `dp[i] = 1`.
最後答案是 `max(dp)`.

**Approach 2: Patience Sorting / Greedy + Binary Search ($O(N \log N)$)**
我們維護一個陣列 `sub`。
遍歷 `x` in `nums`:

1.  如果 `x` 比 `sub` 中所有元素都大，將 `x` 加到 `sub` 末尾。
2.  否則，用 `x` 替換 `sub` 中第一個大於或等於 `x` 的元素。
    -   這一步是 Greedy：我們希望子序列結尾越小越好，這樣後面才有更多機會接上更小的數。
    -   用 Binary Search 找替換位置 (`lower_bound`)。
`sub` 的長度就是 LIS 的長度。
(注意：`sub` 本身**不一定**是真正的 LIS，但其長度是正確的)。

---

## 4. 💻 Implementation (程式碼)

### Approach 1: DP (O(N^2)) - Easier to implement/explain first

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class SolutionDP {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        vector<int> dp(n, 1);
        int maxLen = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    dp[i] = max(dp[i], 1 + dp[j]);
                }
            }
            maxLen = max(maxLen, dp[i]);
        }

        return maxLen;
    }
};
```

### Approach 2: Binary Search (O(N log N)) - Optimal

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) return 0;

        vector<int> sub; // This strictly increases

        for (int x : nums) {
            if (sub.empty() || x > sub.back()) {
                sub.push_back(x);
            } else {
                // Find first element >= x
                auto it = lower_bound(sub.begin(), sub.end(), x);
                *it = x; // Replace it
            }
        }

        return sub.size();
    }
};
```

### Python Reference

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

我們選擇最優的 $O(N \log N)$ 解法作為主要參考。

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        // sub 陣列用來存放當前構建的「潛力」子序列
        // 並非最終的正確序列，但其長度會等於 LIS 長度
        vector<int> sub;

        for (int x : nums) {
            // 如果 sub 為空或 x 比 sub 最後一個元素還大
            // 代表 x 可以接在最長序列後面，直接 push
            if (sub.empty() || x > sub.back()) {
                sub.push_back(x);
            } else {
                // 如果 x 不比最後一個大，我們嘗試用 x 去取代 sub 中的某個元素
                // 根據 Greedy 思想，我們希望序列增長得越慢越好 (結尾越小越好)
                // 所以我們找到 sub 中 "第一個大於或等於 x" 的元素，並將其替換為 x
                // 例如 sub=[2, 5], x=3 -> 把 5 換成 3 -> sub=[2, 3]
                // 這樣長度不變，但結尾變小了，更有利於後面接上 4

                // std::lower_bound 回傳 iterator 指向第一個 >= x 的元素
                auto it = lower_bound(sub.begin(), sub.end(), x);
                *it = x;
            }
        }

        return sub.size();
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N)$
    -   Iterate $N$ elements.
    -   Check/Replace using Binary Search takes $O(\log N)$ (since `sub` length $\le N$).
-   **Space Complexity**: $O(N)$
    -   `sub` array stores up to $N$ elements.
