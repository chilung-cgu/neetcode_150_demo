# Coin Change (零錢兌換)

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
