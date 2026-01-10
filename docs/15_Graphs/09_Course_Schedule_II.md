# Course Schedule II (課程表 II)

## 1. 🧐 Problem Dissection (釐清問題)

與 Course Schedule I 相同，給定 `numCourses` 和 `prerequisites`。
但這次不是問「是否可能」，而是要求回傳一個 **有效的修課順序** (Vector `[0, 1, ...]`)。
如果不可能完成，則回傳空陣列。
如果有多個有效順序，回傳其中任意一個。

-   **Input**: `numCourses = 2, prerequisites = [[1,0]]`
-   **Output**: `[0,1]`
-   **Input**: `numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
-   **Output**: `[0,2,1,3]` (or `[0,1,2,3]`)
-   **Constraints**:
    -   Same as Course Schedule I.

---

## 2. 🐢 Brute Force Approach (暴力解)

嘗試生成所有排列，並驗證。 $O(N!)$。不可行。

---

## 3. 💡 The "Aha!" Moment (優化)

這就是要求輸出 **拓撲排序 (Topological Sort)** 的結果。

**Algorithm: Kahn's Algorithm (BFS + Indegree)**
1.  建立鄰接表 `adj` 和入度表 `indegree`。
2.  將所有 **入度為 0** 的節點（沒有前置課程的課）加入 Queue。
3.  初始化結果陣列 `result`。
4.  BFS Loop:
    -   Pop `curr`。
    -   Add `curr` to `result`。
    -   對於 `curr` 的每個鄰居 `next`:
        -   `indegree[next]--` (移除 `curr` -> `next` 這條邊)。
        -   如果 `indegree[next] == 0`，加入 Queue。
5.  Check:
    -   如果 `result.size() == numCourses`，回傳 `result`。
    -   否則（圖中有環，有些節點入度永遠不為 0），回傳 `{}`。

**DFS Approach**:
-   如果你使用 DFS (3-colored)，當一個節點狀態變為 2 (Visited) 時，將其加入結果列表。
-   最後將結果列表 **反轉 (Reverse)**。
-   (因為 DFS 是後序遍歷，最深層的節點最先完成)。

BFS 通常更直觀，且不需要最後反轉。

---

## 4. 💻 Implementation (程式碼)

### Approach: Kahn's Algorithm (BFS)

```cpp
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // 1. Build Graph and calculate Indegrees
        for (const auto& edge : prerequisites) {
            // edge: [course, pre] -> pre points to course
            adj[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }
        
        // 2. Add courses with 0 indegree to queue
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        
        // 3. Process Queue
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            result.push_back(curr);
            
            for (int neighbor : adj[curr]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // 4. Check for cycle
        if (result.size() != numCourses) {
            return {};
        }
        
        return result;
    }
};
```

### Python Reference

```python
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = { i:[] for i in range(numCourses) }
        indegree = { i:0 for i in range(numCourses) }
        
        for crs, pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs] += 1
            
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
                    
        return res if len(res) == numCourses else []
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        vector<int> indegree(numCourses, 0);
        
        // 1. 建圖並計算入度 (Indegree)
        // 入度代表還有多少前置課程沒修完
        for (const auto& edge : prerequisites) {
            // edge[1] (pre) -> edge[0] (course)
            adj[edge[1]].push_back(edge[0]);
            indegree[edge[0]]++;
        }
        
        // 2. 將所有「無門檻」的課程 (入度為 0) 加入 Queue
        queue<int> q;
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) {
                q.push(i);
            }
        }
        
        vector<int> result;
        
        // 3. BFS 拓撲排序
        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            // 將當前課程加入結果（修課）
            result.push_back(curr);
            
            // 通知所有後續課程：前置課程已修完
            for (int neighbor : adj[curr]) {
                indegree[neighbor]--;
                // 如果後續課程的入度變為 0，代表它的所有前置都修完了
                // 可以加入 Queue 等待修課
                if (indegree[neighbor] == 0) {
                    q.push(neighbor);
                }
            }
        }
        
        // 4. 環檢測
        // 如果結果課程數不等於總課程數，代表圖中有環 (cycle)，有些課永遠修不到
        if (result.size() != numCourses) {
            return {};
        }
        
        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(V + E)$
    -   Process each node and edge once.
-   **Space Complexity**: $O(V + E)$
    -   Adjacency list uses $O(V + E)$.
    -   Indegree array uses $O(V)$.
