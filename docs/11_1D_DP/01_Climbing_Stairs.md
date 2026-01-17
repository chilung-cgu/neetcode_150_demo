# Climbing Stairs (爬樓梯)

## 1. 🧐 Problem Dissection (釐清問題)

題目說你在爬一個樓梯。需要 `n` 階才能到達頂端。
每次你可以爬 `1` 階或 `2` 階。
請問有多少種不同的方法可以爬到頂端？

-   **Input**: `n = 2`
-   **Output**: 2
    -   1. 1 step + 1 step
    -   2. 2 steps
-   **Input**: `n = 3`
-   **Output**: 3
    -   1. 1 + 1 + 1
    -   2. 1 + 2
    -   3. 2 + 1
-   **Constraints**:
    -   $1 <= n <= 45$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)`
這就是 Fibonacci 數列的定義。
直接遞迴會計算大量重複的子問題。

-   **Time**: $O(2^N)$。
-   $N=45$ 時會 Timeout。

---

## 3. 💡 The "Aha!" Moment (優化)

**1. Memoization (Top-Down DP)**:
用一個陣列 `memo[n]` 存已經算過的結果。
`memo[i] = memo[i-1] + memo[i-2]`。

-   Time: $O(N)$。

**2. Tabulation (Bottom-Up DP)**:
從 base case 開始往上算：
`dp[1] = 1`, `dp[2] = 2`
`dp[3] = dp[2] + dp[1] = 3`
...

-   Time: $O(N)$。
-   Space: $O(N)$。

**3. Space Optimization**:
我們只需要前兩個狀態 `prev1` 和 `prev2` 就可以算出當前狀態。

-   Time: $O(N)$。
-   Space: $O(1)$。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../climbing_stairs_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../climbing_stairs_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Space Optimized)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;

        int oneStepBefore = 2; // dp[i-1]
        int twoStepsBefore = 1; // dp[i-2]
        int current = 0;

        for (int i = 3; i <= n; i++) {
            current = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = current;
        }

        return oneStepBefore;
    }
};
```

### Python Reference

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int climbStairs(int n) {
        // Base cases
        if (n == 1) return 1;
        if (n == 2) return 2;

        // dp[i] 代表到達第 i 階的方法數
        // 狀態轉移: dp[i] = dp[i-1] + dp[i-2]
        // 因為只能從 i-1 爬 1 階上來，或從 i-2 爬 2 階上來

        // 空間優化：只存前兩個狀態
        int prev2 = 1; // 代表 dp[i-2]，初始為 dp[1] = 1
        int prev1 = 2; // 代表 dp[i-1]，初始為 dp[2] = 2

        for (int i = 3; i <= n; i++) {
            int curr = prev1 + prev2;
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
    -   Linear scan from 3 to N.
-   **Space Complexity**: $O(1)$
    -   Only constant extra space used.
