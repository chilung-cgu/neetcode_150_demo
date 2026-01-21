# Min Cost Climbing Stairs (使用最小花費爬樓梯) <span style="background: linear-gradient(135deg, #10b981, #059669); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(16, 185, 129, 0.3);">🟢 Easy</span>

> 📌 **LeetCode #746** — [題目連結](https://leetcode.com/problems/min-cost-climbing-stairs/) | [NeetCode 解說](https://neetcode.io/problems/min-cost-climbing-stairs)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個整數陣列 `cost`，其中 `cost[i]` 是從樓梯第 `i` 階向上爬需要支付的費用。
支付費用後，你可以選擇爬 **1** 階或 **2** 階。
你可以從 index `0` 或 index `1` 開始。
請計算到達樓梯頂端（超過最後一個 index）的最低花費。

-   **Input**: `cost = [10, 15, 20]`
-   **Output**: `15`
    -   Start at index 1 (pay 15), climb 2 steps to top. Total 15.
    -   (Start 0 pay 10 -> climb 1 to index 1 pay 15 -> climb 2 to top. Total 25. bad)
    -   (Start 0 pay 10 -> climb 2 to index 2 pay 20 -> climb 1 to top. Total 30. bad)
-   **Input**: `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`
-   **Output**: `6`
-   **Constraints**:
    -   $2 <= cost.length <= 1000$
    -   $0 <= cost[i] <= 999$

---

## 2. 🐢 Brute Force Approach (暴力解)

**Recursion**:
`minCost(i) = cost[i] + min(minCost(i+1), minCost(i+2))`
這會像 Fibonacci 一樣展開成指數級別的樹。

-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

**DP State Definition**:
`dp[i]` 表示到達第 `i` 階樓梯的總最小花費（已經爬上來了）。
或者定義 `dp[i]` 為：站在第 `i` 階，要往上爬到頂端所需的最小花費。

讓我們用「到達第 `i` 階」的定義：
要到達第 `i` 階，可以從第 `i-1` 階爬上來，或者從第 `i-2` 階爬上來。
`dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`
目標是計算 `dp[n]` (n 是樓梯長度，頂端是 n)。

Base Cases:
`dp[0] = 0` (從 0 開始不用錢，我們是算花費是為了離開這階)
`dp[1] = 0` (從 1 開始不用錢)
Wait, the problem says "Once you pay the cost, you can...". So starting at 0 means you pay `cost[0]`.
Let's redefine:
`dp[i]` = Minimum cost to reach step `i`.
To reach step `i`, we could have come from `i-1` (paying `cost[i-1]`) or `i-2` (paying `cost[i-2]`).
Formula: `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`

Result: `dp[n]`.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../min_cost_stairs_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../min_cost_stairs_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Space Optimized)

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        // dp[i] is the min cost to reach step i
        // We want to reach step n

        // Base cases: Accessing step 0 and 1 is free initially (in terms of previous steps)
        // But the recurrence is simpler if we think:
        // Current state = value at prev1 (cost to reach prev1) + cost[prev1]

        // Let's iterate.
        // To reach step 2: min(cost[0], cost[1])

        int prev2 = 0; // Cost to reach step 0 (implicit start)
        int prev1 = 0; // Cost to reach step 1 (implicit start)

        for (int i = 2; i <= n; i++) {
            int current = min(prev1 + cost[i-1], prev2 + cost[i-2]);
            prev2 = prev1;
            prev1 = current;
        }

        return prev1;
    }
};
```

### Approach: In-place Modification (O(1) Space)

我們可以直接修改 `cost` 陣列。
`cost[i]` 變成「到達並離開第 i 階的最小總花費」。
`cost[i] = cost[i] + min(cost[i-1], cost[i-2])`
最後答案是 `min(cost[n-1], cost[n-2])`。

```cpp
class SolutionInPlace {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        for (int i = 2; i < n; i++) {
            cost[i] += min(cost[i-1], cost[i-2]);
        }
        return min(cost[n-1], cost[n-2]);
    }
};
```

### Python Reference

```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0) # Top of stair has 0 cost to leave

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        // dp[i] 代表到達第 i 階的最小花費
        // 我們的目標是到達第 n 階 (頂端)

        // 初始化：
        // 到達第 0 階的花費：0 (可以直接從這裡開始)
        // 到達第 1 階的花費：0 (可以直接從這裡開始)
        int prev2 = 0; // dp[i-2]
        int prev1 = 0; // dp[i-1]

        // 從第 2 階開始計算
        for (int i = 2; i <= n; i++) {
            // 要到達第 i 階，只有兩條路：
            // 1. 從 i-1 階爬上來：花費是 dp[i-1] + cost[i-1]
            // 2. 從 i-2 階爬上來：花費是 dp[i-2] + cost[i-2]
            int curr = min(prev1 + cost[i-1], prev2 + cost[i-2]);

            // 滾動更新
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
    -   Single pass.
-   **Space Complexity**: $O(1)$
    -   Only storing `prev1` and `prev2`.

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

---

## 📚 Related Problems (相關題目)

### 站內相關
- [Climbing Stairs (爬樓梯)](01_Climbing_Stairs.md)
