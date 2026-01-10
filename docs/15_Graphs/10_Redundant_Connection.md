# Redundant Connection (冗餘連接)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個無向圖，該圖原本是一棵樹（$N$ 個節點，$N-1$ 條邊），但此時多了一條邊，使其形成了至少一個環。
圖由 $N$ 個節點組成，標記為 $1$ 到 $N$，以及 $N$ 條邊。
請找出這條「冗餘」的邊。移除它後，圖應該恢復為一棵樹。
如果有多個答案，回傳在輸入 `edges` 中最後出現的那條邊。

-   **Input**: `edges = [[1,2], [1,3], [2,3]]`
-   **Output**: `[2,3]`
    -   1-2, 1-3. Adding 2-3 creates a cycle 1-2-3-1.
-   **Input**: `edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]`
-   **Output**: `[1,4]`
-   **Constraints**:
    -   $3 <= N <= 1000$
    -   Inputs guaranteed to contain a cycle.

---

## 2. 🐢 Brute Force Approach (暴力解)

這是尋找環的邊。
我們可以遍歷每條邊，暫時將其移除，然後檢查剩下的圖是否是連通的樹。
或者，對於每條邊 `(u, v)`，在加入之前檢查 `u` 和 `v` 是否已經連通（DFS/BFS）。如果已經連通，那這條邊就是冗餘的。
-   **Time**: $O(N^2)$。DFS 每次 $O(N)$，做 $N$ 次。

---

## 3. 💡 The "Aha!" Moment (優化)

這是 **並查集 (Union-Find / Disjoint Set Union)** 的標準應用場景。

**Algorithm**:
1.  初始化 Union-Find 結構，每個節點最初是獨立的集合。
2.  遍歷 `edges` 中的每一條邊 `[u, v]`：
    -   `Find(u)`: 查找 `u` 的根節點。
    -   `Find(v)`: 查找 `v` 的根節點。
    -   **Check**: 如果 `root_u == root_v`，說明 `u` 和 `v` 已經在同一個集合中（已經連通）。那麼這條邊 `[u, v]` 就是形成了環的最後一根稻草。**這就是我們要找的冗餘邊**。
    -   **Union**: 如果 `root_u != root_v`，將它們合併。
3.  回傳找到的那條邊。

-   **Why Union-Find?**
    -   它專門用於處理動態連通性問題。
    -   `Find` 和 `Union` 操作接近 $O(1)$ (with Path Compression & Rank/Size optimization, amortized $\alpha(N)$)。

---

## 4. 💻 Implementation (程式碼)

### Approach: Union-Find

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size(); // N edges and N vertices (1 to N)
        parent.resize(n + 1);
        iota(parent.begin(), parent.end(), 0); // Initialize parent[i] = i
        
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            
            // If already connected, this is the redundant edge
            if (find(u) == find(v)) {
                return edge;
            }
            
            // Otherwise, union them
            unite(u, v);
        }
        
        return {};
    }
    
private:
    vector<int> parent;
    
    // Find with Path Compression
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    // Union
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            parent[rootX] = rootY;
        }
    }
};
```

### Python Reference

```python
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                # Path compression
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            parent[p1] = p2
            return True
            
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
                
        return []
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        // 題目說有 N 個節點，標號 1 到 N
        // edges 也有 N 條邊
        // 所以 parent 數組需要大小 N + 1 (0 不用)
        int n = edges.size();
        parent.resize(n + 1);
        
        // 初始化：每個節點的父節點是自己
        // iota 是 C++ numeric 庫函數，將 [begin, end) 填入 0, 1, 2...
        // 這裡我們其實是填入 0 到 n
        iota(parent.begin(), parent.end(), 0);
        
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            
            // 查找 u 和 v 的根節點
            int rootU = find(u);
            int rootV = find(v);
            
            // 如果根節點相同，說明 u 和 v 已經在同一個集合中（已經連通）
            // 再加上這條邊就會形成環，所以這就是冗餘邊
            if (rootU == rootV) {
                return edge;
            }
            
            // 否則，將這兩個集合合併
            // 這裡簡單地將 rootU 掛在 rootV 下面
            parent[rootU] = rootV;
        }
        
        return {};
    }
    
private:
    vector<int> parent;
    
    // 查找並執行「路徑壓縮 (Path Compression)」
    // 這能讓樹的高度保持扁平，加速後續查找
    int find(int x) {
        if (parent[x] != x) {
            // 遞迴查找根節點，並直接更新當前節點的 parent 指向根
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    // 省略了 rank/size 優化的 union，對於這題規模不是必須的
    // 但加上路徑壓縮已經足夠快 (接近 O(1))
    /*
    void unite(int x, int y) { ... }
    */
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \alpha(N))$
    -   $\alpha$ is the Inverse Ackermann function, which is nearly constant ($< 5$ for all practical N).
    -   We iterate through N edges.
-   **Space Complexity**: $O(N)$
    -   Parent array for Union-Find.
