# Binary Tree Right Side View (二元樹的右視圖) <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; font-weight: 600; margin-left: 10px; display: inline-flex; align-items: center; gap: 4px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3);">🟡 Medium</span>

> 📌 **LeetCode #199** — [題目連結](https://leetcode.com/problems/binary-tree-right-side-view/) | [NeetCode 解說](https://neetcode.io/problems/binary-tree-right-side-view)


## 1. 🧐 Problem Dissection (釐清問題)

題目給一個 Binary Tree，想像你站在這棵樹的 **右側** 往左看。
請回傳你從上到下能看到的節點值。

-   **Input**: `root = [1,2,3,null,5,null,4]`
    ```
       1   <---
      / \
     2   3 <---
      \   \
       5   4 <---
    ```

-   **Output**: `[1,3,4]`
-   **Input**: `root = [1,null,3]`
-   **Output**: `[1,3]`
-   **Input**: `[]`
-   **Output**: `[]`
-   **Constraints**:
    -   $0 <= nodes <= 100$
    -   $-100 <= Node.val <= 100$

---

## 2. 🐢 Brute Force Approach (暴力解)

這題本質就是 Level Order Traversal，但是每一層只取**最後一個**元素。

---

## 3. 💡 The "Aha!" Moment (優化)

**Approach 1: BFS (Level Order)**
同上一題。
每層遍歷最後一個元素 `q.back()` or 在 loop 內的 `i == size-1` 時取值。

-   **Time**: $O(n)$。
-   **Space**: $O(n)$ (Queue width)。

**Approach 2: DFS (Reverse Pre-order)**
這是一種聰明的 DFS。
我們可以優先遍歷 **右子樹** (Root -> Right -> Left)。
這樣對於每一層深度 `depth`，我們**第一次**到達該深度的節點，一定是右視圖能看到的節點。

-   `vec` 存結果。
-   `dfs(node, depth)`:
    -   如果 `depth == vec.size()`，代表這是我們第一次來到這一層 -> `vec.push_back(node->val)`
    -   `dfs(right, depth + 1)`
    -   `dfs(left, depth + 1)`
-   **Time**: $O(n)$。
-   **Space**: $O(h)$ (Recursion stack)。如果樹很深，DFS 空間可能比 BFS 差 (Skewed Tree)。如果樹很寬，BFS 空間比 DFS 差。

面試時 BFS 更直觀，DFS 更優雅（代碼短）。

### 🎬 Visualization (演算法視覺化)

<div style="position: relative; padding-bottom: 50%; height: 0; overflow: hidden; max-width: 100%; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); background: #0f172a;">
    <iframe src="../right_side_view_visualizer.html" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" loading="lazy"></iframe>
</div>
<p style="text-align: right; margin-top: 8px;"><a href="../right_side_view_visualizer.html" target="_blank" style="font-size: 0.9em; display: inline-flex; align-items: center; gap: 4px; color: #818cf8; text-decoration: none;"><span>⤢</span> 全螢幕開啟視覺化</a></p>

---

## 4. 💻 Implementation (程式碼)

### Approach: Iterative BFS (Queue)

```cpp
#include <vector>
#include <queue>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();

            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front();
                q.pop();

                // Keep the last node of each level
                if (i == size - 1) {
                    result.push_back(node->val);
                }

                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }

        return result;
    }
};
```

### Approach: Recursive DFS (Right-first)

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root, 0, res);
        return res;
    }

    void dfs(TreeNode* node, int depth, vector<int>& res) {
        if (!node) return;

        // 如果當前深度 == output size，代表我們第一次到達這一層
        // 由於我們是先遍歷右邊，這一定是這一層最右邊的節點
        if (depth == res.size()) {
            res.push_back(node->val);
        }

        dfs(node->right, depth + 1, res);
        dfs(node->left, depth + 1, res);
    }
};
```

### Python Reference

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)

            if rightSide:
                res.append(rightSide.val)
        return res
```

---

## 5. 📝 Detailed Code Comments (詳細註解)

```cpp
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) return result;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int levelSize = q.size();

            // 遍歷這一層的所有節點
            for (int i = 0; i < levelSize; i++) {
                TreeNode* curr = q.front();
                q.pop();

                // 如果是這一層的最後一個節點，它就是右視圖看到的那個
                if (i == levelSize - 1) {
                    result.push_back(curr->val);
                }

                // 繼續將下一層的節點加入 Queue
                // 順序：先左後右
                if (curr->left) q.push(curr->left);
                if (curr->right) q.push(curr->right);
            }
        }

        return result;
    }
};
```

---

## 6. 📊 Rigorous Complexity Analysis (複雜度分析)

-   **Time Complexity**: $O(n)$
    -   BFS 遍歷每個節點一次。
-   **Space Complexity**: $O(n)$
    -   Queue 保存一層的節點。對於 Full Binary Tree，最後一層有 $n/2$ 個節點。
