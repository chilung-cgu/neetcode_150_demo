# Coin Change (零錢兌換) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #322** — [題目連結](https://leetcode.com/problems/coin-change/) | [NeetCode 解說](https://neetcode.io/problems/coin-change)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `coins` 代表不同面額的硬幣，以及一個整數 `amount` 代表總金額。
要求算出湊成該總金額所需的 **最少硬幣數量**。
如果無法湊成，回傳 -1。
假設每種硬幣的數量是無限的。

-   **Input**: `coins = [1, 2, 5], amount = 11`
-   **Output**: `3` (11 = 5 + 5 + 1)
-   **Input**: `coins = [2], amount = 3`
-   **Output**: `-1`
-   **Constraints**:
    -   $1 <= coins.length <= 12$
    -   $0 <= amount <= 10^4$

---

## 2. 🐢 Brute Force Approach (暴力解)

**DFS**:
`minCoins(amount) = 1 + min(minCoins(amount - c))` for each `c` in `coins`.

-   時間複雜度是指數級 $O(S^n)$，其中 $S$ 是金額，$n$ 是硬幣種類數。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個完全背包問題 (Unbounded Knapsack) 的變形。
定義 `dp[a]` 為湊成金額 `a` 所需的最少硬幣數。

**轉移方程**:
`dp[a] = 1 + min(dp[a - c])` 對於所有 `c` in `coins` 且 `a - c >= 0`。

**Base Case**:
`dp[0] = 0` (湊成 0 元需要 0 個硬幣)。

**Initialization**:
`dp[1...amount]` 初始化為一個大數 (例如 `amount + 1`)，表示無法湊成。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../coin_change_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../coin_change_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Bottom-Up)

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // dp[i] stores min coins to make amount i
        // Initialize with amount + 1 (impossible value, akin to infinity)
        vector<int> dp(amount + 1, amount + 1);

        dp[0] = 0;

        for (int a = 1; a <= amount; a++) {
            for (int c : coins) {
                if (a - c >= 0) {
                    dp[a] = min(dp[a], 1 + dp[a - c]);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
};
```

### Python Reference

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        // 建立 DP table，大小為 amount + 1
        // 初始值設為 impossible (比 amount 大的值即可，這裡是 amount + 1)
        // 因為硬幣最小面額是 1，所以最多只需 amount 個硬幣。
        vector<int> dp(amount + 1, amount + 1);

        // Base case: 湊成 0 元需要 0 個硬幣
        dp[0] = 0;

        // 從金額 1 開始計算到 amount
        for (int a = 1; a <= amount; a++) {
            // 嘗試每一種硬幣
            for (int c : coins) {
                // 如果當前金額 a 夠減去硬幣 c
                if (a - c >= 0) {
                    // 轉移方程：dp[a] = min(目前 dp[a], 1 + dp[a-c])
                    // 1 代表用了這枚硬幣 c
                    dp[a] = min(dp[a], 1 + dp[a - c]);
                }
            }
        }

        // 如果 dp[amount] 仍然是大數，代表無法湊成
        if (dp[amount] > amount) {
            return -1;
        } else {
            return dp[amount];
        }
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(A \times C)$
    -   $A$ is amount, $C$ is number of coins.
    -   We fill DP table size $A$, each cell iterates $C$ coins.
-   **Space Complexity**: $O(A)$
    -   DP table size.

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
