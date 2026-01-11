# Burst Balloons (戳氣球)

## 1. 🧐 Problem Dissection (釐清問題)

給定 `n` 個氣球，索引從 0 到 n-1。每個氣球上有一個數字 `nums[i]`。
戳破第 `i` 個氣球，你可以獲得 `nums[i-1] * nums[i] * nums[i+1]` 個硬幣。
戳破後，`i-1` 和 `i+1` 變得相鄰。
求能獲得的最大硬幣數量。
邊界之外的氣球視為 1。

-   **Input**: `nums = [3,1,5,8]`
-   **Output**: `167`
    -   nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
    -   coins =  3\*1\*5      +   3\*5\*8   +  1\*3\*8  + 1\*8\*1 = 15 + 120 + 24 + 8 = 167
-   **Constraints**:
    -   $n == nums.length$
    -   $1 <= n <= 300$
    -   $0 <= nums[i] <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Backtracking / Permutation**:
嘗試第一個戳破哪一個？
如果先戳 `1`，陣列變 `[3, 5, 8]`...
子問題變得很難定義，因為戳破一個氣球後，左右鄰居會變。整個陣列結構在變。
嘗試所有戳破順序的排列：$O(N!)$。 $300!$ 太大了。

---

## 3. 💡 The "Aha!" Moment (優化)

**Reverse Thinking (反向思考)**:
與其想「第一個戳破誰」，不如想「**最後一個戳破誰**」。

假設在區間 `(left, right)` 之間（不包含 left 和 right），**最後一個**被戳破的氣球是 `i`。
那麼由此可以得到收益：
`nums[left] * nums[i] * nums[right]`
並且問題被分割成兩個獨立的子問題：

1.  `(left, i)` 之間的最大收益 (最後剩下 `i` 和 `left` 作為邊界)
2.  `(i, right)` 之間的最大收益 (最後剩下 `i` 和 `right` 作為邊界)

**DP State**:
`dp[i][j]` = max coins obtained from bursting all balloons in the **open interval** `(i, j)`.
(Open interval means we do not burst `i` and `j`, they are the boundaries).

**Process**:

1.  Add `1` to head and tail of `nums`. New size $N+2$.
2.  Iterate `len` from 1 to $N$.
3.  Iterate `left` from 0 to $N - len + 1$.
4.  Set `right = left + len + 1`.
5.  Iterate `k` between `left` and `right` (k is the LAST balloon to burst).
    `dp[left][right] = max(dp[left][right], dp[left][k] + dp[k][right] + nums[left] * nums[k] * nums[right])`

---

## 4. 💻 Implementation (程式碼)

### Approach: Interval DP

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxCoins(vector<int>& nums) {
        // Preprocess: adding 1 at boundaries
        int n = nums.size();
        vector<int> arr(n + 2);
        arr[0] = 1;
        arr[n + 1] = 1;
        for (int i = 0; i < n; i++) {
            arr[i + 1] = nums[i];
        }

        // dp[i][j] represents max coins in range (i, j) - exclusive
        // New size is n + 2
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));

        // Iterate length of the range (number of balloons to burst)
        // len is from 1 to n
        for (int len = 1; len <= n; len++) {
            // Iterate start index (left boundary)
            // Range is (left, right)
            // Since right = left + len + 1, and right <= n + 1
            // left + len + 1 <= n + 1  =>  left <= n - len
            for (int left = 0; left <= n - len; left++) {
                int right = left + len + 1;

                // Iterate pivot k (the last balloon bursts in (left, right))
                for (int k = left + 1; k < right; k++) {
                    dp[left][right] = max(dp[left][right],
                        dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right]);
                }
            }
        }

        return dp[0][n + 1];
    }
};
```

### Python Reference

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {} # (l, r) -> maxCoins

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)
```
Note: The Python recursive solution uses inclusive range `[l, r]`, while C++ iterative DP uses exclusive range `(left, right)`. Both are standard. Exclusive range is often cleaner for iterative.

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxCoins(vector<int>& nums) {
        // 1. 處理邊界：在頭尾各加一個 1
        int n = nums.size();
        vector<int> arr(n + 2);
        arr[0] = 1;
        arr[n + 1] = 1;
        for (int i = 0; i < n; i++) arr[i+1] = nums[i];

        // dp[left][right] 代表開區間 (left, right) 內所有氣球被戳破的最大收益
        // 注意：dp table 大小是 (n+2) x (n+2)
        vector<vector<int>> dp(n + 2, vector<int>(n + 2, 0));

        // 2. 區間 DP 框架
        // len: 區間內氣球的數量 (從 1 到 n)
        for (int len = 1; len <= n; len++) {
            // left: 左邊界 (從 0 開始)
            // right: 右邊界 (根據 len 算出)
            // 我們要計算 dp[left][right]
            for (int left = 0; left <= n - len; left++) {
                int right = left + len + 1;

                // k: 最後一個戳破的氣球的位置 (在 left 和 right 之間)
                for (int k = left + 1; k < right; k++) {
                    // 收益 =
                    // 1. 戳破 left 到 k 之間所有氣球的最大收益 (dp[left][k])
                    // 2. 戳破 k 到 right 之間所有氣球的最大收益 (dp[k][right])
                    // 3. 最後戳破 k 自己的收益 (因為最後戳破 k，所以它的鄰居是邊界 left 和 right)
                    //    -> arr[left] * arr[k] * arr[right]
                    dp[left][right] = max(dp[left][right],
                        dp[left][k] + dp[k][right] + arr[left] * arr[k] * arr[right]);
                }
            }
        }

        // 回傳範圍 (0, n+1) 即包含原本所有氣球的最大收益
        return dp[0][n + 1];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^3)$
    -   Triple loop: Length, Left, K.
    -   $N=300 \implies 2.7 \times 10^7$ ops. Acceptable.
-   **Space Complexity**: $O(N^2)$
    -   DP Table.
