# Best Time to Buy and Sell Stock with Cooldown (買賣股票的最佳時機含冷凍期) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #309** — [題目連結](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | [NeetCode 解說](https://neetcode.io/problems/best-time-to-buy-and-sell-stock-with-cooldown)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個整數陣列 `prices`，代表每天的股價。
你可以多次買賣股票，但有以下限制：

1.  **賣出股票後，第二天無法買入股票** (冷凍期 Cooldown 為 1 天)。
2.  你手中最多只能持有一股（買入前必須先賣掉）。

求最大獲利。

-   **Input**: `prices = [1,2,3,0,2]`
-   **Output**: `3`
    -   Buy day 0 (price 1), Sell day 1 (price 2). Profit 1. Cooldown day 2.
    -   Buy day 3 (price 0), Sell day 4 (price 2). Profit 2.
    -   Total = 1 + 2 = 3.
-   **Input**: `prices = [1]`
-   **Output**: `0`
-   **Constraints**:
    -   $1 <= prices.length <= 5000$
    -   $0 <= prices[i] <= 1000$

---

## 2. 🐢 Brute Force Approach (暴力解)

**DFS/Recursion**:
`dfs(day, canBuy)`

-   If `canBuy`:
    -   Buy: `-price[day] + dfs(day+1, false)`
    -   Cooldown (Wait): `dfs(day+1, true)`
-   If `!canBuy` (must sell):
    -   Sell: `+price[day] + dfs(day+2, true)` (Jump to day+2 because of cooldown)
    -   Cooldown (Wait): `dfs(day+1, false)`
-   **Time**: $O(2^N)$。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個變形的 State Machine DP。
我們定義每一天的三個狀態：

1.  **Hold (持有股票)**: 今天結束時，手中有一張股票。
    -   可能是今天買的。
    -   或者昨天就持有，今天休息。
2.  **Sold (剛賣出股票)**: 今天結束時，剛賣出股票（明天進入冷凍期）。
    -   一定是今天賣的。
3.  **Rest (休息/空手)**: 今天結束時，沒持有股票，且不是剛賣出（明天可以買）。
    -   可能是昨天就沒持有（休息）。
    -   或者是昨天剛賣出（今天冷凍）。

**State Transitions**:

-   `hold[i] = max(hold[i-1], rest[i-1] - prices[i])`
    -   (昨天持有) vs (昨天休息，今天買入)。注意：不能從 sold 轉過來，因為有 cooldown。
-   `sold[i] = hold[i-1] + prices[i]`
    -   (昨天持有，今天賣出)。
-   `rest[i] = max(rest[i-1], sold[i-1])`
    -   (昨天休息) vs (昨天賣出，今天被迫冷凍/休息)。

Target: `max(sold[n], rest[n])`. (最後一天不可能持有股票會有最大收益).

**Space Optimization**:
只需要前一天的狀態。 `prev_hold`, `prev_sold`, `prev_rest`.

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../stock_cooldown_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../stock_cooldown_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: State Machine DP

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // Initialize states
        // hold: max profit if we have stock
        // sold: max profit if we just sold stock
        // rest: max profit if we have no stock (and didn't just sell)

        int hold = INT_MIN;
        int sold = 0;
        int rest = 0;

        for (int price : prices) {
            int prev_hold = hold;
            int prev_sold = sold;
            int prev_rest = rest;

            // To hold today:
            // 1. We held yesterday (prev_hold)
            // 2. We rested yesterday and bought today (prev_rest - price)
            hold = max(prev_hold, prev_rest - price);

            // To be in sold state today:
            // 1. We held yesterday and sold today (prev_hold + price)
            sold = prev_hold + price;

            // To be in rest state today:
            // 1. We rested yesterday (prev_rest)
            // 2. We sold yesterday (prev_sold) -> entering rest/cooldown
            rest = max(prev_rest, prev_sold);
        }

        // Max profit is either we just sold or we were resting
        return max(sold, rest);
    }
};
```

### Python Reference

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        dp = {} # key=(i, buying) val=max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]

        return dfs(0, True)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 定義三個狀態：
        // hold: 持有股票
        // sold: 剛剛賣出股票 (明天將會是 cooldown)
        // rest: 未持有股票，且不是剛賣出 (可以是 cooldown 中，或一直沒買)

        // 初始化
        // 第一天如果 hold，代表買入，收益為 -price[0]，設為 INT_MIN 防止誤判
        // 但其實可以直接寫 -price[0] 如果我們從 loop 0 開始跑且特別處理
        // 這裡為了方便，假設第 -1 天狀態：
        // hold = -inf (不可能持有)
        // sold = 0
        // rest = 0

        long hold = INT_MIN; // 用 long 防止 overflow
        long sold = 0;
        long rest = 0;

        for (int p : prices) {
            long prev_hold = hold;
            long prev_sold = sold;
            long prev_rest = rest;

            // 如果今天結束後持有股票：
            // 1. 昨天就持有 (Rest -> Hold 不行，Hold -> Hold OK)
            // 2. 昨天是 Rest 狀態 (可以買)，今天買入 (Rest -> Hold)
            // 注意：不能從 Sold 直接變 Hold，因為有 cooldown
            hold = max(prev_hold, prev_rest - p);

            // 如果今天結束後是剛賣出狀態：
            // 1. 昨天持有，今天賣出 (Hold -> Sold)
            sold = prev_hold + p;

            // 如果今天結束後是 Rest 狀態：
            // 1. 昨天就是 Rest
            // 2. 昨天是 Sold (今天進入 Cooldown，也是一種 Rest)
            rest = max(prev_rest, prev_sold);
        }

        // 最終最大收益不可能是持有股票的狀態
        return max(sold, rest);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N)$
    -   Loop through `prices` once.
-   **Space Complexity**: $O(1)$
    -   Only 3 variables used.

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
