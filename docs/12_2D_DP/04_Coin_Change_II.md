# Coin Change II (零錢兌換 II)

## 1. 🧐 Problem Dissection (釐清問題)

題目給一個整數陣列 `coins` 代表不同面額的硬幣，以及一個整數 `amount`。
要求算出湊成該總金額的 **組合數量**。

-   每種硬幣數量無限。
-   順序不重要 (組合，不是排列)。即 `1+2` 和 `2+1` 視為同一種。

-   **Input**: `amount = 5, coins = [1, 2, 5]`
-   **Output**: `4`
    -   5 = 5
    -   5 = 2 + 2 + 1
    -   5 = 2 + 1 + 1 + 1
    -   5 = 1 + 1 + 1 + 1 + 1
-   **Constraints**:
    -   $1 <= coins.length <= 300$
    -   $1 <= amount <= 5000$

---

## 2. 🐢 Brute Force Approach (暴力解)

DFS: `count(index, target)`

-   Take `coins[index]`: `count(index, target - coins[index])`
-   Skip `coins[index]`: `count(index + 1, target)`
-   **Time**: Exponential.

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個 **Unbounded Knapsack Problem (完全背包問題)**。
定義 `dp[j]` 為湊成金額 `j` 的方法數。

關鍵點：**迴圈順序**。

-   **外層迴圈遍歷 coins，內層迴圈遍歷 amount**。
-   這保證了每一種硬幣只會按順序考慮，避免了重複排列 (例如先選 1 再選 2，和先選 2 再選 1)。這計算的是組合數。
-   如果反過來（外層 amount 內層 coins），會算出排列數 (377. Combination Sum IV)。

 `dp[j] += dp[j - coin]`
 (不選 coin 的方法數 + 選了 coin 後剩下的方法數)。

Base Case:
`dp[0] = 1` (湊成 0 元有 1 種方法：什麼都不選)。

---

## 4. 💻 Implementation (程式碼)

### Approach: DP (Space Optimized)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<unsigned int> dp(amount + 1, 0); // Use unsigned/long to prevent overflow if needed, but prob constraint says int is enough.
        // Actually return type is int. Constraints specify answer fits in 32-bit integer.

        dp[0] = 1;

        for (int coin : coins) {
            // Unbounded knapsack: iterate forward from coin to amount
            for (int j = coin; j <= amount; j++) {
                dp[j] += dp[j - coin];
            }
        }

        return dp[amount];
    }
};
```

### Python Reference

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]

        return dp[amount]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        // dp[j] 代表湊成金額 j 的組合數
        // 初始化為 0，大小為 amount + 1
        // 使用 unsigned int 或 long long 是個好習慣，雖然題目保證不超過 int範圍
        vector<int> dp(amount + 1, 0);

        // Base case: 金額 0 只有 1 種湊法 (空集合)
        dp[0] = 1;

        // 關鍵：外層迴圈硬幣，內層迴圈金額
        // 這樣確保我們考慮 coins[i] 時，已經考慮完 coins[0...i-1]
        // 因此不會產生重複組合 (e.g. {1,2} 和 {2,1} 只會出現一次 {1,2})
        for (int coin : coins) {
            for (int j = coin; j <= amount; j++) {
                // dp[j] (包含 coin 的方法數) =
                //    dp[j] (原本不包含 coin 的方法數) +
                //    dp[j - coin] (用了 coin 後，剩餘金額的方法數)
                dp[j] += dp[j - coin];
            }
        }

        return dp[amount];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(A \times C)$
    -   $A$ is amount, $C$ is number of coins.
    -   $5000 \times 300 = 1.5 \times 10^6$ ops. Fast.
-   **Space Complexity**: $O(A)$
    -   DP array size.
