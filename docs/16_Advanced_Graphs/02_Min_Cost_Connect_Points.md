---
title: "Min Cost to Connect All Points (連接所有點的最小費用)"
description: "給定一個二維坐標陣列 `points`。 你需要連接所有點，使得這是一個連通圖。 連接兩點 `(xi, yi)` 和 `(xj, yj)` 的費用是曼哈頓距離 `|xi - xj| + |yi - yj|`。 回傳連接所有點的最小總費用。"
tags:
  - Graph
  - Dijkstra
  - MST
difficulty: Medium
---

# Min Cost to Connect All Points (連接所有點的最小費用) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #1584** — [題目連結](https://leetcode.com/problems/min-cost-to-connect-all-points/) | [NeetCode 解說](https://neetcode.io/problems/min-cost-to-connect-points)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個二維坐標陣列 `points`。
你需要連接所有點，使得這是一個連通圖。
連接兩點 `(xi, yi)` 和 `(xj, yj)` 的費用是曼哈頓距離 `|xi - xj| + |yi - yj|`。
回傳連接所有點的最小總費用。

這就是求一個完全圖的 **最小生成樹 (Minimum Spanning Tree, MST)** 的總權重。

-   **Input**: `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`
-   **Output**: `20`
-   **Constraints**:
    -   $1 <= points.length <= 1000$
    -   Coordinates range $[-10^6, 10^6]$.

---

## 2. 🐢 Brute Force Approach (暴力解)

這是一個包含 $N$ 個點的完全圖（每兩個點之間都有邊）。
邊的總數大約是 $N^2 / 2$。
如果我們列出所有邊，並運行 Kruskal 算法（排序邊 + Union-Find）：

-   排序所有的邊：$O(N^2 \log(N^2)) = O(N^2 \log N)$。
-   Union-Find：$O(N^2 \alpha(N))$。
-   因為 $N \le 1000$， $N^2 = 10^6$，在這個範圍內是可以接受的。

---

## 3. 💡 The "Aha!" Moment (優化)

**Prim's Algorithm**:
Prim 算法從一個點開始，每次選擇距離當前生成樹最近的點加入。
因為是稠密圖（Dense Graph，邊數 $E \approx V^2$），使用 Prim 算法通常比 Kruskal 更好，因為我們不需要預先生成和排序所有邊（可以在遍歷時動態計算距離）。

**Algorithm**:

1.  **Min-Heap**: 儲存 `(cost, point_index)`。
2.  **Visited Set**: 記錄已加入 MST 的點。
3.  **Start**: 從點 0 開始，推入 `{0, 0}` 到 Heap。
4.  **Loop**: 當 Visited 大小 < N：
    -   Pop 此刻最小费用的邊 `(cost, u)`。
    -   如果 `u` 已訪問，跳過。
    -   將 `u` 加入 Visited，`res += cost`。
    -   遍歷所有其他點 `v` (如果未訪問)：
        -   計算 `dist(u, v)`，推入 `{dist, v}` 到 Heap。
5.  回傳 `res`。

**Optimized Prim's**:
不用 Heap 存儲所有邊，而是維護一個 `minDist` 陣列，記錄每個點到當前 MST 的最短距離。每次掃描 `minDist` 找出最小值。

-   Time: $O(N^2)$。因為不用 Heap 操作的 $\log N$。
-   對於 $N=1000$，這非常快。

這裡我們演示使用 Min-Heap 的標準 Prim 算法，因為它更通用且直觀。
雖然它的最壞情況是 $O(E \log E) = O(N^2 \log N)$，等同於 Kruskal，但在實踐中，我們只要一連接到點就不再需要處理其他邊，且不用先生成所有邊。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../min_cost_connect_points_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../min_cost_connect_points_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Prim's Algorithm (Min-Heap)

```cpp
#include <vector>
#include <queue>
#include <cmath>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        // Min-Heap: {cost, nodeIndex}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        // Start from node 0 with cost 0
        pq.push({0, 0});

        vector<bool> visited(n, false);
        int edgesCount = 0;
        int totalCost = 0;

        while (edgesCount < n) {
            pair<int, int> top = pq.top();
            pq.pop();

            int cost = top.first;
            int u = top.second;

            if (visited[u]) continue;

            visited[u] = true;
            totalCost += cost;
            edgesCount++;

            // Add neighbors to heap
            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);
                    pq.push({dist, v});
                }
            }
        }

        return totalCost;
    }
};
```

### Python Reference

```python
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i: [] for i in range(N)} # Actually implicit dense graph

        # Min heap: [cost, point_index]
        minH = [[0, 0]]
        visit = set()
        res = 0

        while len(visit) < N:
            cost, u = heapq.heappop(minH)
            if u in visit:
                continue

            res += cost
            visit.add(u)

            for v in range(N):
                if v not in visit:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(minH, [dist, v])

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();

        // 最小堆：儲存 {距離, 點的索引}
        // 我們依據距離從小到大取出
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        // 從任意一點开始 (例如點 0)，連接費用為 0
        pq.push({0, 0});

        vector<bool> visited(n, false);
        int connectedNodes = 0;
        int totalCost = 0;

        // 當我們還沒有連接所有點時
        while (connectedNodes < n) {
            // 取出當前代價最小的邊
            pair<int, int> top = pq.top();
            pq.pop();

            int cost = top.first;
            int u = top.second;

            // 如果這個點已經被連接過了，跳過 (Lazy Deletion)
            if (visited[u]) continue;

            // 將點 u 加入生成樹
            visited[u] = true;
            totalCost += cost;
            connectedNodes++;

            // 將所有從 u 出發到未訪問節點的邊加入 Heap
            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);
                    pq.push({dist, v});
                }
            }
        }

        return totalCost;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N^2 \log N)$
    -   In the worst case (using Heap), we might push $N^2$ edges. Heap operations take $\log(N^2) \approx \log N$.
    -   Optimized Prim's (without Heap) is $O(N^2)$.
-   **Space Complexity**: $O(N^2)$ (Heap size) or $O(N)$ (Optimized).
    -   The heap can store all edges in a dense graph.

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
