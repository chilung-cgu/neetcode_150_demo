---
title: "Cheapest Flights Within K Stops (K 站中轉內最便宜的航班)"
description: "給定 `n` 個城市，與一些航班 `flights`，其中 `flights[i] = [from, to, price]`。 每班飛機都有價格。 給定起點 `src`、終點 `dst` 和允許的最多中轉次數 `k`。 請找出從 `src` 到 `dst` 的最便宜價格，且中轉次數 **不超過 k*"
tags:
  - Graph
  - Dijkstra
  - MST
difficulty: Medium
---

# Cheapest Flights Within K Stops (K 站中轉內最便宜的航班) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #787** — [題目連結](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | [NeetCode 解說](https://neetcode.io/problems/cheapest-flight-path)


## 1. 🧐 Problem Dissection (釐清問題)

給定 `n` 個城市，與一些航班 `flights`，其中 `flights[i] = [from, to, price]`。
每班飛機都有價格。
給定起點 `src`、終點 `dst` 和允許的最多中轉次數 `k`。
請找出從 `src` 到 `dst` 的最便宜價格，且中轉次數 **不超過 k**（即最多搭乘 k+1 班飛機）。
如果無法到達，回傳 -1。

-   **Input**: `n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1`
-   **Output**: `200`
    -   0->1->2 (Price 200, Stops 1).
    -   0->2 (Price 500, Stops 0).
    -   Min is 200.
-   **Constraints**:
    -   $1 <= n <= 100$
    -   $0 <= flights.length <= (n * (n - 1) / 2)$
    -   $0 <= k < n$

---

## 2. 🐢 Brute Force Approach (暴力解)

DFS 搜索所有從 `src` 到 `dst` 的路徑。
在遞迴過程中記錄當前的中轉次數 `stops`。如果 `stops > k` 就剪枝。
記錄到達 `dst` 的最小費用。

-   **Time**: $O(n^k)$ (最壞情況)。

---

## 3. 💡 The "Aha!" Moment (優化)

這是單源最短路徑問題，但多了一個限制條件：邊數不超過 $k+1$。

**Bellman-Ford Algorithm**:
Bellman-Ford 算法的核心是「鬆弛 (Relax) 所有邊 $n-1$ 次」。
第 $i$ 次鬆弛保證找到了「最多 $i$ 條邊」的最短路徑。
所以我們只需要運行 Bellman-Ford 算法 $k+1$ 次即可。

**Algorithm**:

1.  **Prices Array**: `arr` 初始化為 INF，`arr[src] = 0`。
2.  **Loop k+1 times**:
    -   複製一份當前的 `arr` 為 `tmp` (為了避免同一次迭代中使用了剛更新的值，導致走了多步)。
    -   遍歷所有航班 `(u, v, w)`：
        -   若 `arr[u]` 不是 INF：
            -   `tmp[v] = min(tmp[v], arr[u] + w)`
    -   將 `tmp` 賦值給 `arr`。
3.  **Result**: 如果 `arr[dst]` 還是 INF，回傳 -1，否則回傳 `arr[dst]`。

**Dijkstra's Algorithm (Modified)**:
也可以用 Dijkstra，但在 Min-Heap 中需要存儲 `(cost, node, stops)`。
只有當 `stops <= k` 時才繼續擴展。
而且，到達同一個節點，如果 `stops` 更少但 `cost` 更大，我們**也需要保留**，因為更少的 `stops` 可能讓我們在後續能走到終點（未耗盡 K）。這使得判重邏輯變複雜。
Bellman-Ford 更直觀且符合「k 次限制」的本質。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../cheapest_flights_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../cheapest_flights_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Bellman-Ford

```cpp
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // Distance array, initialized to Max Integer
        vector<int> prices(n, INT_MAX);
        prices[src] = 0;

        // Loop k + 1 times (max edges allowed is k + 1)
        for (int i = 0; i <= k; i++) {
            // Create a copy to ensure we use values from previous iteration
            vector<int> tmpPrices = prices;

            for (const auto& flight : flights) {
                int u = flight[0];
                int v = flight[1];
                int w = flight[2];

                // If source node is reachable
                if (prices[u] != INT_MAX) {
                    // Start relaxation
                    if (prices[u] + w < tmpPrices[v]) {
                        tmpPrices[v] = prices[u] + w;
                    }
                }
            }

            prices = tmpPrices;
        }

        return prices[dst] == INT_MAX ? -1 : prices[dst];
    }
};
```

### Python Reference

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights: # s=source, d=dest, p=price
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            prices = tmpPrices

        return -1 if prices[dst] == float("inf") else prices[dst]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        // 初始化價格矩陣
        // prices[i] 代表從起點 src 到達 i 的最小費用
        vector<int> prices(n, INT_MAX);
        prices[src] = 0;

        // Bellman-Ford 算法的核心：鬆弛所有邊
        // 我們需要最多 k+1 條邊（k 次中轉），所以循環執行 k+1 次
        for (int i = 0; i <= k; i++) {
            // 每次迭代必須基於上一輪的結果
            // 如果直接使用 prices 更新，可能會在一次循環中通過多條邊（串聯更新）
            // 例如：A->B 更新了 B，然後 B->C 立即使用了新的 B，這樣就走了兩步，不符合 k 的限制
            // 所以要用 tmpPrices 保存当前这一轮的结果
            vector<int> tmpPrices = prices;

            for (const auto& flight : flights) {
                int u = flight[0]; // From
                int v = flight[1]; // To
                int w = flight[2]; // Price

                // 如果起點 u 還是無窮大，說明 u 還不可達，不能作為跳板
                if (prices[u] != INT_MAX) {
                    // 鬆弛操作 (Relaxation)
                    if (prices[u] + w < tmpPrices[v]) {
                        tmpPrices[v] = prices[u] + w;
                    }
                }
            }

            // 更新 prices
            prices = tmpPrices;
        }

        // 如果 dst 還是 INT_MAX，代表無法在 k+1 步內到達
        return prices[dst] == INT_MAX ? -1 : prices[dst];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(K \times E)$
    -   We iterate through all $E$ flights, $K+1$ times.
-   **Space Complexity**: $O(N)$
    -   Price arrays.

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
- [Network Delay Time (網絡延遲時間)](03_Network_Delay_Time.md)
