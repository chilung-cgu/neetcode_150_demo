# Clone Graph (複製圖)

## 1. 🧐 Problem Dissection (釐清問題)

給定一個無向連通圖中的一個節點引用 `Node`。
請回傳該圖的 **深拷貝 (Deep Copy)**。
圖中的每個節點都包含一個值 (`int val`) 和一個列表 (`List[Node] neighbors`)。

-   **Deep Copy**: 意味著你需要創建新的節點物件，並且新圖的結構（連接關係）必須與原圖完全一致。不能直接回傳原圖節點的引用。
-   **Input**: Adjacency list `[[2,4],[1,3],[2,4],[1,3]]` (Node 1 connects to 2,4; Node 2 to 1,3; etc.)
-   **Output**: Same adjacency list (but new objects).
-   **Constraints**:
    -   Nodes count [0, 100].
    -   Node.val is unique.
    -   No self-loops or repeated edges (simple graph).
    -   Graph is connected.

---

## 2. 🐢 Brute Force Approach (暴力解)

這題沒有所謂的暴力解，因為必須遍歷整張圖並複製。
不管是 DFS 還是 BFS，本質上都是遍歷圖的標準算法。
唯一的區別是遍歷順序。

---

## 3. 💡 The "Aha!" Moment (優化)

這題的核心難點在於 **處理環 (Cycles)** 和 **重複訪問**。
無向圖中的邊是雙向的，如果我不記錄訪問過的節點，遞迴就會陷入無限循環。

**Hash Map Is The Key**:
我們需要一個 Map：`Old Node -> New Node`。
-   `map` 充當了兩個角色：
    1.  **Visited Set**: 如果一個節點在 map 中，說明我們已經訪問過或者是正在訪問它，不需要重新創建。
    2.  **Mapping**: 當我們需要連接鄰居時，如果是舊鄰居，我們可以從 map 中拿到對應的新鄰居。

**Algorithm (DFS)**:
`clone(node)`:
1.  如果 `node` 是 null，回傳 null。
2.  如果 `node` 已經在 map 中，回傳 `map[node]` (直接返回已創建的克隆)。
3.  **Create**: 創建新節點 `newNode(node.val)`。
4.  **Register**: 將 `node -> newNode` 放入 map。 (重要！要在遞迴鄰居之前放入，否則遇到環會死循環)。
5.  **Recurse**: 遍歷 `node.neighbors`：
    -   `newNode.neighbors.add(clone(neighbor))`。
6.  回傳 `newNode`。

---

## 4. 💻 Implementation (程式碼)

### Approach: DFS with Hash Map

```cpp
#include <vector>
#include <unordered_map>

using namespace std;

// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution {
public:
    // Map to keep track of created nodes: old_node_ptr -> new_node_ptr
    unordered_map<Node*, Node*> copies;

    Node* cloneGraph(Node* node) {
        if (!node) {
            return nullptr;
        }
        
        // If we have already cloned this node, return the stored clone
        if (copies.find(node) != copies.end()) {
            return copies[node];
        }
        
        // Create a new node (just val initially)
        Node* copy = new Node(node->val);
        // Important: Add to map BEFORE recursing to handle cycles
        copies[node] = copy;
        
        // Clone all neighbors
        for (Node* neighbor : node->neighbors) {
            copy->neighbors.push_back(cloneGraph(neighbor));
        }
        
        return copy;
    }
};
```

### Python Reference

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy
            
        return dfs(node) if node else None
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    // 使用 Hash Map 來儲存舊節點到新節點的映射
    // 這扮演了兩個角色：visited 檢查 + 獲取已創建的副本
    unordered_map<Node*, Node*> visited;

    Node* cloneGraph(Node* node) {
        // 邊界條件：空圖
        if (node == nullptr) {
            return nullptr;
        }
        
        // 檢查是否已經複製過該節點
        // 如果有，直接回傳之前創建的副本，這樣可以正確處理環 (Cycle)
        if (visited.find(node) != visited.end()) {
            return visited[node];
        }
        
        // 1. 創建新節點 (Deep Copy)
        Node* cloneNode = new Node(node->val);
        
        // 2. 註冊到 Map 中 (這步必須在處理鄰居之前做！)
        visited[node] = cloneNode;
        
        // 3. 遞迴處理所有鄰居
        for (Node* neighbor : node->neighbors) {
            // 對每個鄰居調用 cloneGraph
            // 如果鄰居已存在，它會直接回傳；如果不存在，它會被創建
            cloneNode->neighbors.push_back(cloneGraph(neighbor));
        }
        
        return cloneNode;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(V + E)$
    -   We visit every vertex once.
    -   We traverse every edge once (technically twice, once from each end, but it's constant).
-   **Space Complexity**: $O(V)$
    -   The hash map stores V vertices.
    -   The recursion stack can go up to $O(V)$ (for a line graph).
