---
title: "Minimum Interval to Include Each Query (包含每個查詢的最小區間)"
description: "給定一個區間陣列 `intervals`，其中 `intervals[i] = [left_i, right_i]`。 以及一個查詢陣列 `queries`，其中 `queries[j]` 是一個數值。 對於每個查詢 `q`，找出一個區間 `[l, r]` 滿足："
tags:
  - Intervals
  - Sorting
difficulty: Hard
---

# Minimum Interval to Include Each Query (包含每個查詢的最小區間) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

> 📌 **LeetCode #1851** — [題目連結](https://leetcode.com/problems/minimum-interval-to-include-each-query/) | [NeetCode 解說](https://neetcode.io/problems/minimum-interval-including-query)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個區間陣列 `intervals`，其中 `intervals[i] = [left_i, right_i]`。
以及一個查詢陣列 `queries`，其中 `queries[j]` 是一個數值。
對於每個查詢 `q`，找出一個區間 `[l, r]` 滿足：

1.  `l <= q <= r` (包含 q)
2.  區間長度 `r - l + 1` 最小。
如果不存在這樣的區間，回傳 -1。

-   **Input**: `intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]`
-   **Output**: `[3,3,1,4]`
    -   Query 2: in [1,4] (len 4), [2,4] (len 3). Min is 3.
    -   Query 3: in [1,4] (len 4), [2,4] (len 3), [3,6] (len 4). Min is 3.
    -   Query 4: in [1,4], [2,4], [3,6], [4,4] (len 1). Min is 1.
    -   Query 5: in [3,6] (len 4). Min is 4.
-   **Constraints**:
    -   $1 <= intervals.length, queries.length <= 10^5$
    -   $1 <= left_i <= right_i <= 10^7$
    -   $1 <= queries[j] <= 10^7$

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每個查詢，遍歷所有區間，檢查是否包含該查詢值，並記錄最小長度。

-   **Time**: $O(Q \times N)$。
    -   $Q, N = 10^5 \to 10^{10}$ TLE.

---

## 3. 💡 The "Aha!" Moment (優化)

這是一道結合 **Sorting** + **Priority Queue (Min-Heap)** + **Sweepline** 的經典難題。

**策略**：

1.  **Sort Intervals**: 按照起始位置 `left` 排序。
2.  **Sort Queries**: 按照數值大小排序。
    -   (注意：需要保留原始 query 的 index，以便最後按正確順序輸出)。
3.  **Sweep Line and Min-Heap**:
    -   我們依序遍歷每個排序後的查詢 `q`。
    -   **Add**: 隨著 `q` 增加，我們把所有 `left <= q` 的區間加入 Heap。
        -   Heap 中儲存 `{length, right}`。我們要找最小長度，所以 Min-Heap 是根據長度。
    -   **Pop Invalid**: 檢查 Heap 頂部的區間。如果 `heap.top().right < q`，說明這個區間已經結束了，無法覆蓋當前的 `q`。把它彈出。
        -   一直彈出直到堆頂有效，或者堆為空。
    -   **Result**: 此時堆頂就是 **包含 q 且長度最小** 的區間。

**為什麼有效？**

-   區間按 start 排序，保證我們只在適當的時候加入。
-   查詢按 q 排序，保證 `q` 是遞增的，我們不需要回頭。之前如果不滿足條件被彈出的區間 (`right < q_prev`)，對於現在更大的 `q_curr` 當然更不滿足，所以彈出是安全的。
-   Min-Heap 讓我們在 $O(1)$ 或 $O(\log N)$ 時間取到最小長度。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../min_interval_query_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../min_interval_query_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Sort + Min-Heap

```cpp
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size();
        int m = queries.size();

        // Save original indices of queries
        // pair: {value, index}
        vector<pair<int, int>> sortedQueries(m);
        for(int i = 0; i < m; i++) {
            sortedQueries[i] = {queries[i], i};
        }

        // Sort queries by value
        sort(sortedQueries.begin(), sortedQueries.end());

        // Sort intervals by start time
        sort(intervals.begin(), intervals.end());

        // Min-Heap: {length, end_time}
        // C++ priority_queue is max heap by default, use greater for min heap
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        vector<int> result(m, -1);
        int i = 0; // interval pointer

        for (const auto& qPair : sortedQueries) {
            int qVal = qPair.first;
            int qIndex = qPair.second;

            // 1. Add valid intervals (start <= q)
            while (i < n && intervals[i][0] <= qVal) {
                int len = intervals[i][1] - intervals[i][0] + 1;
                int end = intervals[i][1];
                pq.push({len, end});
                i++;
            }

            // 2. Remove invalid intervals (end < q)
            while (!pq.empty() && pq.top().second < qVal) {
                pq.pop();
            }

            // 3. Get minimum length
            if (!pq.empty()) {
                result[qIndex] = pq.top().first;
            }
        }

        return result;
    }
};
```

### Python Reference

```python
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        minHeap = []
        res = {}
        i = 0

        # Sort queries, but keep track of indices or just map results
        # Unique queries sorted
        sorted_queries = sorted(list(set(queries)))

        for q in sorted_queries:
            # Add intervals that start before or at q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            # Remove intervals that end before q
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # Store result
            res[q] = minHeap[0][0] if minHeap else -1

        return [res[q] for q in queries]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        int n = intervals.size();
        int m = queries.size();

        // 為了回答所有查詢，我們將查詢排序，以便使用 sweep-line 技巧
        // 但最後輸出需要按照原始順序，所以要紀錄原始 index
        vector<pair<int, int>> sortedQueries(m);
        for(int i = 0; i < m; i++) {
            sortedQueries[i] = {queries[i], i};
        }
        sort(sortedQueries.begin(), sortedQueries.end());

        // 將區間按起始位置排序，這樣我們可以依序處理
        sort(intervals.begin(), intervals.end());

        // Min-Heap 儲存 {區間長度, 結束時間}
        // 我們希望快速找到「長度最小」的區間
        // 結束時間是用來判斷該區間是否還有效
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        vector<int> result(m, -1);
        int i = 0; // 用來遍歷 intervals

        for (const auto& qPair : sortedQueries) {
            int qVal = qPair.first;
            int qIndex = qPair.second;

            // 步驟 1: 將所有起始位置 <= 當前查詢值的區間加入 Heap
            // 這些區間是有可能覆蓋 qVal 的候選人
            while (i < n && intervals[i][0] <= qVal) {
                int len = intervals[i][1] - intervals[i][0] + 1;
                int end = intervals[i][1];
                pq.push({len, end});
                i++;
            }

            // 步驟 2: 移除無效區間
            // 如果堆頂區間的結束位置 < qVal，代表它已經過期了，無法覆蓋 qVal
            // 因為 qVal 是遞增的，這個過期區間對後面的查詢也一定無效，所以可以直接丟棄
            while (!pq.empty() && pq.top().second < qVal) {
                pq.pop();
            }

            // 步驟 3: 此時堆頂一定是有效的且長度最小的區間
            if (!pq.empty()) {
                result[qIndex] = pq.top().first;
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \log N + Q \log Q)$
    -   Sort intervals: $N \log N$.
    -   Sort queries: $Q \log Q$.
    -   Loop: Each interval is pushed and popped at most once ($O(N \log N)$). Queries iteration is $O(Q \log N)$ (peek heap).
-   **Space Complexity**: $O(N + Q)$
    -   Heap stores intervals. Sorted Queries array.

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
