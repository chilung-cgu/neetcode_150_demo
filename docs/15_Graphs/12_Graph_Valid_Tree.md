# Graph Valid Tree (圖是否為樹) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

## 1. 🧐 Problem Dissection (釐清問題)

給定 `n` 個節點和一個邊的列表 `edges`。
請判斷這些邊是否構成了一棵有效的樹。

樹的定義：

1.  **Fully Connected**: 所有節點都是連通的。
2.  **No Cycles**: 沒有環。

這等價於：

-   連通分量數量為 1。
-   邊的數量等於 `n - 1`。
-   或者，如果在併查集中，每次 Union 的兩個點原本不連通，最後總共成功合併了 `n - 1` 次。

-   **Input**: `n = 5, edges = [[0,1], [0,2], [0,3], [1,4]]`
-   **Output**: `true`
-   **Input**: `n = 5, edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]`
-   **Output**: `false` (Cycle 1-2-3-1)
-   **Constraints**:
    -   $1 <= n <= 2000$
    -   $0 <= edges.length <= 5000$

---

## 2. 🐢 Brute Force Approach (暴力解)

-   檢查邊數是否為 `n - 1`。如果不是，直接 False。
-   從節點 0 開始 DFS/BFS，確保能訪問到所有 `n` 個節點（連通性）。
-   同時確保沒有訪問到已訪問的節點（無環）。
-   **Time**: $O(V + E)$。

---

## 3. 💡 The "Aha!" Moment (優化)

**Union-Find** 是一個非常自然的解法，因為它可以同時檢測環和連通性。

**Algorithm**:

1.  如果 `edges.size() != n - 1`，回傳 `false` (這是樹的必要條件，避免了連通但不夠邊，或邊太多必有環的情況)。
2.  初始化 Union-Find (Count = n)。
3.  遍歷每條邊 `[u, v]`：
    -   如果 `Find(u) == Find(v)`：說明這條邊連接了兩個已經連通的點 -> **發現環** -> 回傳 `false`。
    -   否則，`Union(u, v)`，`Count--`。
4.  最後檢查 `Count == 1`。如果只剩一個分量，說明全連通 -> 回傳 `true`。
    -   (其實如果第一步 `Diff != n-1` 檢查過了，且無環，那最後 Count 必然是 1。因為無環且邊數 n-1 的圖必然連通)。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../valid_tree_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../valid_tree_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Union-Find

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        // Condition 1: Number of edges must be n - 1
        if (edges.size() != n - 1) {
            return false;
        }

        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);

        int components = n;

        for (const auto& edge : edges) {
            int rootU = find(edge[0]);
            int rootV = find(edge[1]);

            // Condition 2: No cycles
            if (rootU == rootV) {
                return false;
            }

            // Merge
            parent[rootU] = rootV;
            components--;
        }

        // Condition 3: Fully connected (1 component)
        return components == 1;
    }

private:
    vector<int> parent;

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
};
```

### Python Reference

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = { i:[] for i in range(n) }
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False # Loop detected

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        // 樹的一個重要性質：n 個節點的樹一定恰好有 n-1 條邊
        // 如果邊數不對，一定不是樹（邊太少不連通，邊太多有環）
        if (edges.size() != n - 1) {
            return false;
        }

        // 雖然上面的檢查過濾了大部分情況，但我們還需要確認「是否有環」或者「是否連通」
        // (如果有 n-1 條邊但有環，那必定不連通)
        // 使用 Union-Find 來同時檢查這兩點

        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);

        int components = n;

        for (const auto& edge : edges) {
            int rootU = find(edge[0]);
            int rootV = find(edge[1]);

            // 如果两个节点已经在同一个集合中，再次连接它们会形成环
            if (rootU == rootV) {
                return false;
            }

            // 合併
            parent[rootU] = rootV;
            components--;
        }

        // 如果無環且邊數正確，最後一定只剩 1 個連通分量
        // 但為了保險（或者省略掉第一步檢查時），檢查 components == 1 是最穩的
        return components == 1;
    }

private:
    vector<int> parent;

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(N \alpha(N))$
    -   We iterate $N-1$ edges (due to the early check). Union/Find is nearly constant.
-   **Space Complexity**: $O(N)$
    -   Parent array.
