---
title: "Course Schedule (課程表)"
description: "你必須選修 `numCourses` 門課程，編號從 `0` 到 `numCourses - 1`。 給定一個前置條件陣列 `prerequisites`，其中 `prerequisites[i] = [ai, bi]` 表示要修課程 `ai`，必須先修課程 `bi`。 請判斷是否可能完成所有課程？"
tags:
  - Graph
  - DFS
  - BFS
difficulty: Medium
---

# Course Schedule (課程表) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #207** — [題目連結](https://leetcode.com/problems/course-schedule/) | [NeetCode 解說](https://neetcode.io/problems/course-schedule)


## 1. 🧐 Problem Dissection (釐清問題)

你必須選修 `numCourses` 門課程，編號從 `0` 到 `numCourses - 1`。
給定一個前置條件陣列 `prerequisites`，其中 `prerequisites[i] = [ai, bi]` 表示要修課程 `ai`，必須先修課程 `bi`。
請判斷是否可能完成所有課程？

這等價於：**在一個有向圖中，檢測是否存在環 (Cycle)**。
如果存在環，則無法完成（死鎖）。
如果無環，則可以完成。

-   **Input**: `numCourses = 2, prerequisites = [[1,0]]`
-   **Output**: `true` (Take 0 then 1)
-   **Input**: `numCourses = 2, prerequisites = [[1,0],[0,1]]`
-   **Output**: `false` (Cycle: 0->1->0)
-   **Constraints**:
    -   $1 <= numCourses <= 2000$
    -   $0 <= prerequisites.length <= 5000$

---

## 2. 🐢 Brute Force Approach (暴力解)

對於每個節點啟動 DFS，檢測是否有環。
如果沒有做 memoization，最壞情況是指數級的。

---

## 3. 💡 The "Aha!" Moment (優化)

這是一個標準的 **拓撲排序 (Topological Sort)** 問題，或者是 **有向圖環檢測** 問題。

**Algorithm 1: DFS with 3 States (三色標記法)**
每個節點有三種狀態：

1.  **0 (Unvisited)**: 還沒訪問過。
2.  **1 (Visiting)**: 正在訪問（在當前遞迴堆疊中）。如果 DFS 過程中遇到狀態 1 的節點，說明遇到了 **環**。
3.  **2 (Visited)**: 已經訪問過且沒有發現環。安全的節點。

遍歷所有節點：

-   如果是 0 -> 啟動 DFS。
-   如果是 1 -> Return False (Cycle detected)。
-   如果是 2 -> Return True (Safe)。

**Algorithm 2: Kahns Algorithm (BFS + Indegree)**

1.  計算每個節點的 **入度 (Indegree)**。
2.  將所有入度為 0 的節點加入 Queue。
3.  BFS:
    -   Pop 一個節點，計數 `processed++`。
    -   對其所有鄰居，入度減 1。
    -   如果鄰居入度變為 0，加入 Queue。
4.  最後檢查 `processed == numCourses`。如果不等，說明圖中有環（剩下的節點入度都不為 0，互為前置）。

這兩種方法都是 $O(V + E)$。DFS 比較好寫，BFS 比較直觀。這裡演示 DFS。

---

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../course_schedule_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../course_schedule_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: DFS (Cycle Detection)

```cpp
#include <vector>

using namespace std;

class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // Build adjacency list
        vector<vector<int>> adj(numCourses);
        for (const auto& edge : prerequisites) {
            adj[edge[1]].push_back(edge[0]);
        }

        // 0: Unvisited, 1: Visiting, 2: Visited
        vector<int> state(numCourses, 0);

        for (int i = 0; i < numCourses; i++) {
            if (state[i] == 0) {
                if (hasCycle(adj, state, i)) {
                    return false;
                }
            }
        }

        return true;
    }

private:
    bool hasCycle(const vector<vector<int>>& adj, vector<int>& state, int curr) {
        // If current node is visiting, we found a cycle (back edge)
        if (state[curr] == 1) return true;
        // If current node is already visited and safe, no cycle here
        if (state[curr] == 2) return false;

        // Mark as visiting
        state[curr] = 1;

        for (int neighbor : adj[curr]) {
            if (hasCycle(adj, state, neighbor)) {
                return true;
            }
        }

        // Mark as visited (safe)
        state[curr] = 2;
        return false;
    }
};
```

### Python Reference

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i: [] for i in range(numCourses) }
        for crs, pre in prerequisites:
            preMap[pre].append(crs)

        # visitSet = all nodes along the current DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False # Loop detected
            if preMap[crs] == []:
                return True # No prereqs or already processed (optimization needed for strict O(V+E))

            visitSet.add(crs)
            for neighbor in preMap[crs]:
                if not dfs(neighbor): return False
            visitSet.remove(crs)

            preMap[crs] = [] # Mark as verified to avoid re-visiting
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // 建立鄰接表 (Adjacency List)
        // adj[i] 包含所有依賴 i 的課程
        vector<vector<int>> adj(numCourses);
        for (const auto& edge : prerequisites) {
            // edge 為 [course, prereq] -> 從 prereq 指向 course
            adj[edge[1]].push_back(edge[0]);
        }

        // 狀態陣列
        // 0: 未訪問 (Unvisited)
        // 1: 正在訪問 (Visiting - 在當前遞迴堆疊中)
        // 2: 已訪問且安全 (Visited - 確定無環)
        vector<int> state(numCourses, 0);

        // 對每個節點執行 DFS
        for (int i = 0; i < numCourses; i++) {
            // 只對未訪問的節點啟動，以避免重複計算
            if (state[i] == 0) {
                if (hasCycle(adj, state, i)) {
                    return false; // 發現環，無法完成
                }
            }
        }

        return true; // 無環，可完成
    }

private:
    bool hasCycle(const vector<vector<int>>& adj, vector<int>& state, int curr) {
        // 如果遇到狀態 1，代表在當前遞迴路徑中又回到了自己 -> 發現環
        if (state[curr] == 1) return true;

        // 如果遇到狀態 2，代表這個節點之前檢查過了，且無環 -> 安全
        if (state[curr] == 2) return false;

        // 將當前節點標記為正在訪問
        state[curr] = 1;

        // 遞迴檢查所有鄰居
        for (int neighbor : adj[curr]) {
            if (hasCycle(adj, state, neighbor)) {
                return true;
            }
        }

        // 遞迴結束，標記當前節點為已訪問且安全
        state[curr] = 2;
        return false;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(V + E)$
    -   Vertices are courses, Edges are prerequisites.
    -   We visit each vertex and edge at most once.
-   **Space Complexity**: $O(V + E)$
    -   Adjacency list uses $O(V + E)$.
    -   Recursion stack uses $O(V)$ in worst case.

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
- [Course Schedule II (課程表 II)](09_Course_Schedule_II.md)
