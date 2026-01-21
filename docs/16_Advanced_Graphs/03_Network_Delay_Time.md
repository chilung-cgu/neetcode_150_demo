---
title: "Network Delay Time (網絡延遲時間)"
description: "給定一個網絡，包含 $n$ 個節點（標記為 1 到 n）。 給定一個時間列表 `times`，其中 `times[i] = (u, v, w)` 表示從節點 `u` 到節點 `v` 的信號傳遞需要時間 `w`。 現在我們從某個節點 `k` 發出一個信號。 請問所有 $n$ 個節點都收到信號需要多久？"
tags:
  - Graph
  - Dijkstra
  - MST
difficulty: Medium
---

# Network Delay Time (網絡延遲時間) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #743** — [題目連結](https://leetcode.com/problems/network-delay-time/) | [NeetCode 解說](https://neetcode.io/problems/network-delay-time)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個網絡，包含 $n$ 個節點（標記為 1 到 n）。
給定一個時間列表 `times`，其中 `times[i] = (u, v, w)` 表示從節點 `u` 到節點 `v` 的信號傳遞需要時間 `w`。
現在我們從某個節點 `k` 發出一個信號。
請問所有 $n$ 個節點都收到信號需要多久？
如果不可能所有節點都收到信號，回傳 -1。

在這個問題中，「所有節點都收到信號需要的時間」等於 **從起點 k 到所有其他節點的最短路徑中的最大值**。

-   **Input**: `times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2`
-   **Output**: `2`
    -   2->1 (time 1), 2->3 (time 1), 3->4 (time 1 => total 2 from source). Max(1, 1, 2) = 2.
-   **Constraints**:
    -   $1 <= n <= 100$
    -   $1 <= times.length <= 6000$

---

## 2. 🐢 Brute Force Approach (暴力解)

這是單源最短路徑問題。

-   **Bellman-Ford**: $O(V \times E)$。可行，因為 $V$ 很小 ($100$)。
-   **Floyd-Warshall**: $O(V^3)$。計算任意兩點最短路徑。也可行。
-   **BFS (Queue)**: 僅適用於無權圖。這裡有權重且不為 1，不能直接用簡單 BFS (除非改造成 SPFA，但 SPFA 最壞情況是指數級)。

---

## 3. 💡 The "Aha!" Moment (優化)

**Dijkstra's Algorithm**:
這是解決非負權重圖的中單源最短路徑的最標準、最高效算法。
因為邊權重代表時間，一定是非負的。

**Algorithm**:

1.  **Graph**: 建立鄰接表 `adj[u] -> [(v, w)]`。
2.  **Priority Queue**: Min-Heap 儲存 `(time_from_source, node)`。
3.  **Distances**: 記錄從 k 到每個節點的最短時間。也可以只用一個 `visited` 集合來記錄。
4.  **Process**:
    -   Push `(0, k)`。
    -   Loop while PQ not empty:
        -   Pop `(time, u)`。
        -   如果 `u` 已訪問，跳過。
        -   標記 `u` 為已訪問，更新最大時間 `res = max(res, time)`。
        -   對於鄰居 `v`，Push `(time + w, v)`。
5.  **Result**:
    -   如果訪問過的節點數等於 $n$，回傳 `res`。
    -   否則回傳 -1。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../network_delay_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../network_delay_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Dijkstra's Algorithm

```cpp
#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // Build Graph
        unordered_map<int, vector<pair<int, int>>> adj;
        for (const auto& t : times) {
            adj[t[0]].push_back({t[1], t[2]});
        }

        // Min-Heap: {time, node}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k});

        // Track visited nodes and minimum time found
        vector<int> dist(n + 1, -1);
        int visitedCount = 0;
        int maxTime = 0;

        while (!pq.empty()) {
            pair<int, int> top = pq.top();
            pq.pop();

            int time = top.first;
            int u = top.second;

            if (dist[u] != -1) continue; // Already visited

            dist[u] = time;
            visitedCount++;
            maxTime = max(maxTime, time);

            if (visitedCount == n) return maxTime; // Optimization

            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (dist[v] == -1) {
                    pq.push({time + w, v});
                }
            }
        }

        return visitedCount == n ? maxTime : -1;
    }
};
```

### Python Reference

```python
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            time, u = heapq.heappop(minHeap)
            if u in visit:
                continue

            visit.add(u)
            t = max(t, time)

            if len(visit) == n:
                return t

            for v, w in adj[u]:
                if v not in visit:
                    heapq.heappush(minHeap, (time + w, v))

        return -1
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        // 1. 建圖
        // adj[u] 包含所有從 u 出發的邊 {v, weight}
        unordered_map<int, vector<pair<int, int>>> adj;
        for (const auto& t : times) {
            adj[t[0]].push_back({t[1], t[2]});
        }

        // 2. Dijkstra 初始化
        // Min-Heap 存儲 {當前總耗時, 節點編號}
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        pq.push({0, k}); // 起點 k，耗時 0

        // 記錄每個節點是否已確定最短路徑
        // 使用 vector 來記錄最短時間，初始化為 -1 代表未訪問
        vector<int> dist(n + 1, -1);
        int visitedCount = 0;
        int maxTime = 0;

        // 3. 處理 Heap
        while (!pq.empty()) {
            pair<int, int> top = pq.top();
            pq.pop();

            int time = top.first;
            int u = top.second;

            // 如果已經找到該節點的最短路徑，跳過
            if (dist[u] != -1) continue;

            // 標記該節點已訪問，並記錄其最短時間
            dist[u] = time;
            visitedCount++;
            maxTime = max(maxTime, time); // 答案是所有最短時間中的最大值

            // 優化：如果所有節點都已訪問，可以提早結束
            if (visitedCount == n) return maxTime;

            // 擴展鄰居
            for (const auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                // 只將未確定最短路徑的鄰居加入 Heap
                if (dist[v] == -1) {
                    pq.push({time + w, v});
                }
            }
        }

        return visitedCount == n ? maxTime : -1;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(E \log E)$
    -   Standard Dijkstra with Heap. In worst case we push all edges to heap.
-   **Space Complexity**: $O(V + E)$
    -   Adjacency list. Heap size.

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
- [Cheapest Flights Within K Stops (K 站中轉內最便宜的航班)](06_Cheapest_Flights_K_Stops.md)
