# Number of Connected Components in an Undirected Graph (無向圖中的連通分量數量) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #323** — [題目連結](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | [NeetCode 解說](https://neetcode.io/problems/number-of-connected-components-in-an-undirected-graph)


## 1. 🧐 Problem Dissection (釐清問題)

給定一個包含 `n` 個節點的圖。
給定一個整數 `n` 和一個數組 `edges`，其中 `edges[i] = [ai, bi]` 表示節點 `ai` 和 `bi` 之間有一條邊。
請回傳圖中連通分量的數量。

-   **Input**: `n = 5, edges = [[0,1], [1,2], [3,4]]`
-   **Output**: `2`
    -   Components: `{0, 1, 2}` and `{3, 4}`.
-   **Input**: `n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]`
-   **Output**: `1`
-   **Constraints**:
    -   $1 <= n <= 2000$
    -   $1 <= edges.length <= 5000$

---

## 2. 🐢 Brute Force Approach (暴力解)

建立鄰接表。
使用 `visited` 陣列。
遍歷 0 到 n-1。
如果節點 `i` 沒有被訪問過：

-   `count++`
-   啟動 DFS/BFS 遍歷整個分量並標記為已訪問。
回傳 `count`。

-   **Time**: $O(V + E)$。其實這不是暴力解，這已經是很好的解法了。

---

## 3. 💡 The "Aha!" Moment (優化)

這題和 "Number of Islands" 很像，都是計算島嶼（連通分量）的數量。
但這裡可以用 **Union-Find** 更加優雅地解決。

**Algorithm (Union-Find)**:

1.  最初有 `n` 個分量 (Count = n)。
2.  遍歷每條邊 `[u, v]`：
    -   `Find(u)`, `Find(v)`。
    -   如果 `root_u != root_v`：
        -   `Union(u, v)`。
        -   `Count--` (兩個分量合併成一個了，總數減一)。
    -   如果 `root_u == root_v`：說明已經連通，Count 不變。
3.  回傳 `Count`。

Union-Find 方法的優點是代碼非常簡潔，且不需要顯式建立鄰接表。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../connected_components_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../connected_components_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Union-Find

```cpp
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);

        int components = n;

        for (const auto& edge : edges) {
            int rootU = find(edge[0]);
            int rootV = find(edge[1]);

            if (rootU != rootV) {
                // Merge two components
                parent[rootU] = rootV;
                components--;
            }
        }

        return components;
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0 # Already connected, count doesn't change
            parent[p1] = p2
            return 1 # Successful union, count decreases by 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        // 初始化並查集
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);

        // 初始狀態下，每個節點都是一個獨立的連通分量
        // 所以總數為 n
        int components = n;

        // 遍歷所有邊
        for (const auto& edge : edges) {
            int rootU = find(edge[0]);
            int rootV = find(edge[1]);

            // 如果两个节点不在同一个集合中，合并它们
            if (rootU != rootV) {
                parent[rootU] = rootV;
                // 每成功合并一次，連通分量數量就減一
                // (因為兩個分量變成這一個了)
                components--;
            }
        }

        return components;
    }

private:
    vector<int> parent;

    // 查找並執行路徑壓縮
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

-   **Time Complexity**: $O(E \alpha(N))$
    -   Iterate E edges, Union/Find takes almost constant time.
-   **Space Complexity**: $O(N)$
    -   Parent array.

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
