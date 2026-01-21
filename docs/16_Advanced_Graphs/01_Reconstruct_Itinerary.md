# Reconstruct Itinerary (重建行程) <span style="background: linear-gradient(135deg, #ef4444, #dc2626); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(239, 68, 68, 0.3);">🔴 Hard</span>

## 1. 🧐 Problem Dissection (釐清問題)

給定一份機票列表 `tickets`，其中 `tickets[i] = [from, to]`。
請重建行程路徑。
規則：

1.  行程必須從 "JFK" 開始。
2.  必須用完所有機票。
3.  如果有多種有效的行程，請回傳字典序最小的那一個。

-   **Input**: `[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]`
-   **Output**: `["JFK","MUC","LHR","SFO","SJC"]`
-   **Input**: `[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`
-   **Output**: `["JFK","ATL","JFK","SFO","ATL","SFO"]`
    -   Another possible path: `["JFK","SFO","ATL","JFK","ATL","SFO"]` but it is lexicographically larger.

這是一個 **歐拉路徑 (Eulerian Path)** 問題。
我們需要在有向圖中找出一條路徑，經過每一條邊恰好一次。
因為題目保證有解，所以圖一定是半歐拉圖或歐拉圖。

---

## 2. 🐢 Brute Force Approach (暴力解)

DFS 回溯法。
從 "JFK" 出發，嘗試走每一條可用的邊。
如果走不下去了但還有邊沒用完，就回溯。
為了保證字典序最小，我們可以先對鄰接表中的目的地進行排序。

-   **Time**: 指數級（如果有很多死胡同需要回溯）。

---

## 3. 💡 The "Aha!" Moment (優化)

**Hierholzer's Algorithm (Modified DFS)**:
這個算法可以在 $O(E)$ 時間內找到歐拉路徑。
核心思想是：**一直走，直到走投無路，然後把當前節點加入路徑，並逆序輸出**。

1.  **Graph Construction**: 建立鄰接表 `Map<String, PriorityQueue<String>>`。
    -   使用 PriorityQueue (Min-Heap) 或者是排序後的 List，是為了保證我們先選字典序小的目的地。
2.  **DFS (Post-order Traversal)**:
    -   從 "JFK" 開始。
    -   只要當前機場還有目的地可去 (`adj[curr]` 不為空)：
        -   取出並刪除字典序最小的那個目的地 `next`。
        -   遞迴 `dfs(next)`。
    -   當沒有目的地可去時（或者所有邊都訪問完了），將當前機場加入 `result` 列表。
3.  **Reverse**:
    -   因為我們是在「回溯」的時候加入節點（也就是當這條路徑走完的時候），所以得到的列表是逆序的。
    -   將 `result` 反轉即為答案。

這個算法不需要顯式的回溯（撤銷選擇），因為它是基於「歐拉路徑一定存在」的前提，並且通過後序遍歷巧妙地處理了死胡同（死胡同必然是路徑的終點，會最先被加入結果）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../reconstruct_itinerary_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../reconstruct_itinerary_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Hierholzer's Algorithm

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        // Build graph with Priority Queue for lexical order
        unordered_map<string, priority_queue<string, vector<string>, greater<string>>> adj;

        for (const auto& t : tickets) {
            adj[t[0]].push(t[1]);
        }

        vector<string> result;
        dfs("JFK", adj, result);

        // The result is currently in reverse order
        reverse(result.begin(), result.end());
        return result;
    }

private:
    void dfs(string curr, unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& adj, vector<string>& result) {
        // Visit all outgoing edges
        while (!adj[curr].empty()) {
            string next = adj[curr].top();
            adj[curr].pop(); // Remove edge
            dfs(next, adj, result);
        }
        // Add to result after visiting all children (Post-order)
        result.push_back(curr);
    }
};
```

### Python Reference

```python
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = { src: [] for src, dst in tickets }

        # Sort to ensure lexical order
        tickets.sort()

        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(src):
            while src in adj and len(adj[src]) > 0:
                # Pop the smallest lexical neighbor
                v = adj[src].pop(0)
                dfs(v)
            res.append(src)

        dfs("JFK")
        return res[::-1]
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        // 建立鄰接表
        // Key: 出發機場
        // Value: 目的機場列表 (使用 Priority Queue 自動排序，保證字典序最小)
        unordered_map<string, priority_queue<string, vector<string>, greater<string>>> adj;

        for (const auto& t : tickets) {
            adj[t[0]].push(t[1]);
        }

        vector<string> result;
        // 從起點 JFK 開始 DFS
        dfs("JFK", adj, result);

        // Hierholzer 算法是後序添加節點，也就是說終點會最先進入 result
        // 因此最後需要反轉整個列表
        reverse(result.begin(), result.end());
        return result;
    }

private:
    void dfs(string curr, unordered_map<string, priority_queue<string, vector<string>, greater<string>>>& adj, vector<string>& result) {
        // 當前節點還有出邊時，一直訪問
        // 注意這裡是用 while 循環，而不是只訪問一次
        // 這保證了會走完所有的回路
        while (!adj[curr].empty()) {
            string next = adj[curr].top();
            adj[curr].pop(); // 訪問過這條邊就刪除 (歐拉路徑每條邊只能用一次)

            // 遞迴訪問下一個節點
            dfs(next, adj, result);
        }

        // 當沒有出邊可以走的時候（或者所有出邊都已經走過了）
        // 將當前節點加入结果
        // 這就是為什麼它是逆序的：因為我們是「退回來」的時候才記錄
        result.push_back(curr);
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(E \log E)$
    -   Graph construction involves sorting edges (or priority queue operations). Each edge is pushed and popped once.
-   **Space Complexity**: $O(V + E)$
    -   Adjacency list and recursion stack.
